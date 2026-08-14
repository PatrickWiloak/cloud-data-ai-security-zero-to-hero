#!/usr/bin/env python3
"""Build the MkDocs Material site from the repository's markdown tree.

The repository is a browsable knowledge base first and a website second, so the
markdown tree at the repo root stays exactly as it is. This script adapts it to
MkDocs at build time instead of restructuring it:

1.  Stage every content file into `.site-src/`, mirroring the repo layout so that
    relative links, `edit_uri`, and the on-GitHub reading experience all keep
    working unchanged.
2.  Generate an index page for any directory that has markdown children but no
    `README.md`, so that the ~1,200 directory-style links (`](../foo/)`) resolve
    and every nav section has a landing page.
3.  Generate the whole `nav` from the staged tree, with human-readable labels
    pulled from each page's H1 and cert labels pulled from `docs/certs.json`.
4.  Append that nav to a copy of `mkdocs.yml` and build from the copy.

Nothing here is hand-maintained per page: add a markdown file to the repo and it
appears in the site nav on the next build.

Usage:
    python3 .github/scripts/build-site.py            # build into site/
    python3 .github/scripts/build-site.py --strict   # warnings become errors (CI)
    python3 .github/scripts/build-site.py --serve    # stage, then live-reload
    python3 .github/scripts/build-site.py --stage-only
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
STAGE = REPO / ".site-src"
# Site chrome lives outside the content tree: `assets/` is the repo's diagram
# store and should stay that way. Copied into the stage at `assets/site/`, which
# is what `extra_css` in mkdocs.yml points at.
SITE_CHROME = REPO / ".github" / "site"
SITE_CHROME_DEST = "assets/site"
BASE_CONFIG = REPO / "mkdocs.yml"
GENERATED_CONFIG = REPO / "mkdocs.generated.yml"
CERTS_JSON = REPO / "docs" / "certs.json"

# Top-level directories and files that make up the site, in tab order. Anything
# not listed is not staged. Keeping this explicit means adding a new top-level
# directory is a deliberate choice rather than an accident.
ROOT_FILES = ["README.md", "STUDY-HUB.md"]
CONTENT_DIRS = ["learn", "resources", "exams", "topics", "docs", "assets", ".templates"]
ABOUT_FILES = ["CONTRIBUTING.md", "CHANGELOG.md", "TODO.md", "CLAUDE.md"]

# MkDocs ignores dot-directories inside docs_dir, but `.templates/` holds three
# real pages (the shared per-provider resource lists) that cert guides link to
# 144 times. Stage it under a visible name and rewrite the inbound links.
# The name must not be `templates`: MkDocs reserves a root `/templates/` and
# silently drops it from the build.
STAGE_RENAMES = {".templates": "provider-resources"}

# Never staged at any depth: VCS and tooling clutter.
EXCLUDED_DIR_NAMES = {".git", "__pycache__", "node_modules", ".ipynb_checkpoints"}

# Never staged, but only where they actually live, at the repo root. Matching
# these by bare name at any depth would silently drop legitimate content
# directories that happen to share a name (`assets/site/`, for instance).
EXCLUDED_ROOT_DIRS = {
    REPO / ".git",
    REPO / ".github",
    REPO / ".claude",
    REPO / ".venv-docs",
    STAGE,
    REPO / "site",
}

# Files copied as static assets rather than rendered as pages.
STATIC_SUFFIXES = {".csv", ".json", ".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp", ".pdf", ".css"}

# Where each top-level path hangs in the navigation. Order here is tab order.
TABS: list[tuple[str, list[str]]] = [
    ("Learn", ["learn"]),
    (
        "Build",
        [
            "resources/hands-on-projects",
            "resources/architecture-patterns",
            "resources/cli-cheat-sheets",
            "resources/well-architected",
            "resources/troubleshooting",
        ],
    ),
    (
        "Certify",
        [
            "STUDY-HUB.md",
            "exams",
            "resources/practice-questions",
            "resources/certification-roadmaps",
            "resources/exam-prep",
        ],
    ),
    (
        "Reference",
        [
            "resources/README.md",
            "resources/service-comparisons",
            "resources/interview-prep",
            "resources/decision-matrices",
            "resources/ai-security",
            "resources/compliance-guides",
            "resources/cost-optimization",
            "resources/networking-deep-dives",
            "resources/migration-guides",
            "resources/postmortems",
            "resources/playlists",
            "resources/misc",
            "provider-resources",
        ],
    ),
    ("Topics", ["topics"]),
    ("About", ["docs"] + ABOUT_FILES),
]

# `resources/` is a flat drawer of ~90 files. These patterns sort them into the
# virtual groups referenced in TABS above. First match wins; the fallback is
# `resources/misc`.
RESOURCE_GROUPS: list[tuple[str, str]] = [
    (r"^cli-cheat-sheet-", "resources/cli-cheat-sheets"),
    (r"^certification-roadmap-", "resources/certification-roadmaps"),
    (r"^service-comparison-", "resources/service-comparisons"),
    (r"^decision-matrix-", "resources/decision-matrices"),
    (r"^postmortem-", "resources/postmortems"),
    (r"^playlist-", "resources/playlists"),
    (r"^(exam-day-checklist|study-strategies|practice-resources|budget-study-plan|recommended-courses)", "resources/exam-prep"),
]

# Human labels for the virtual groups and for directories whose basename does not
# make a good title.
GROUP_LABELS = {
    "resources/cli-cheat-sheets": "CLI Cheat Sheets",
    "resources/certification-roadmaps": "Career Roadmaps",
    "resources/service-comparisons": "Service Comparisons",
    "resources/decision-matrices": "Decision Matrices",
    "resources/postmortems": "Postmortems",
    "resources/playlists": "Video Playlists",
    "resources/exam-prep": "Exam Prep",
    "resources/misc": "More Reference",
    "resources/hands-on-projects": "Hands-on Projects",
    "resources/architecture-patterns": "Architecture Patterns",
    "resources/well-architected": "Well-Architected",
    "resources/troubleshooting": "Troubleshooting",
    "resources/ai-security": "AI Security",
    "resources/compliance-guides": "Compliance Guides",
    "resources/cost-optimization": "Cost Optimization",
    "resources/networking-deep-dives": "Networking Deep Dives",
    "resources/practice-questions": "Practice Questions",
    "resources/interview-prep": "Interview Prep",
    "resources/migration-guides": "Migration Guides",
    "learn/day-one": "Day One",
    "learn/concepts": "Concepts",
    "provider-resources": "Provider Resource Lists",
    "exams": "All Certifications",
    "docs": "Project Docs",
    "assets": "Assets",
}

# Certification level directories sort by exam progression, not alphabetically.
LEVEL_ORDER = {
    "foundational": 0,
    "associate": 1,
    "professional": 2,
    "specialty": 3,
    "expert": 4,
    "shared": 9,
}

# Within a cert directory, the study materials have a natural reading order.
CERT_FILE_ORDER = {
    "README.md": 0,
    "fact-sheet.md": 1,
    "practice-plan.md": 2,
    "notes": 3,
    "scenarios.md": 4,
    "strategy.md": 5,
}

H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.DOTALL)


# --------------------------------------------------------------------------- #
# Staging
# --------------------------------------------------------------------------- #

def iter_source_files() -> list[Path]:
    """Every repo-relative path that should be staged."""
    found: list[Path] = []
    for name in ROOT_FILES + ABOUT_FILES:
        p = REPO / name
        if p.is_file():
            found.append(p)
    for d in CONTENT_DIRS:
        root = REPO / d
        if not root.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = sorted(
                n
                for n in dirnames
                if n not in EXCLUDED_DIR_NAMES and (Path(dirpath) / n) not in EXCLUDED_ROOT_DIRS
            )
            for fn in sorted(filenames):
                p = Path(dirpath) / fn
                if p.suffix.lower() in STATIC_SUFFIXES or p.suffix == ".md":
                    found.append(p)
    return found


def stage() -> list[str]:
    """Copy sources into .site-src/. Returns staged paths relative to the stage."""
    if STAGE.exists():
        shutil.rmtree(STAGE)
    STAGE.mkdir(parents=True)

    staged: list[str] = []
    for src in iter_source_files():
        rel = src.relative_to(REPO)
        parts = list(rel.parts)
        if parts[0] in STAGE_RENAMES:
            parts[0] = STAGE_RENAMES[parts[0]]
            rel = Path(*parts)
        dest = STAGE / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        staged.append(rel.as_posix())

    if SITE_CHROME.is_dir():
        for src in sorted(SITE_CHROME.rglob("*")):
            if not src.is_file():
                continue
            rel = Path(SITE_CHROME_DEST) / src.relative_to(SITE_CHROME)
            dest = STAGE / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            staged.append(rel.as_posix())
    return staged


def generate_missing_indexes() -> list[str]:
    """Give every directory holding markdown a landing page.

    Directory-style links (`](../notes/)`) are used ~1,200 times across the repo
    and resolve to a directory listing on GitHub. On the site they need a real
    page. Any directory that already ships a README.md is left alone.
    """
    created: list[str] = []
    for dirpath, dirnames, filenames in os.walk(STAGE):
        dirnames[:] = sorted(dirnames)
        d = Path(dirpath)
        if d == STAGE:
            continue
        if "README.md" in filenames or "index.md" in filenames:
            continue
        md_children = sorted(f for f in filenames if f.endswith(".md"))
        # Only link subdirectories that will themselves have a landing page.
        # A directory holding nothing but static assets gets no index, so
        # linking it would emit a dead link into a generated page.
        subdirs = sorted(sd for sd in dirnames if any((d / sd).rglob("*.md")))
        if not md_children and not subdirs:
            continue

        rel = d.relative_to(STAGE)
        title = label_for_dir(rel.as_posix(), d.name)
        lines = [f"# {title}", ""]
        if subdirs:
            lines.append("## Sections")
            lines.append("")
            for sd in subdirs:
                lines.append(f"- [{label_for_dir((rel / sd).as_posix(), sd)}]({sd}/)")
            lines.append("")
        if md_children:
            if subdirs:
                lines.append("## Pages")
                lines.append("")
            for f in md_children:
                lines.append(f"- [{title_of(d / f)}]({f})")
            lines.append("")
        lines.append(
            "<!-- Generated by .github/scripts/build-site.py because this directory "
            "has no README.md. Add one to replace this page. -->"
        )
        (d / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        created.append((rel / "README.md").as_posix())
    return created


# --------------------------------------------------------------------------- #
# Link rewriting
# --------------------------------------------------------------------------- #

LINK_RE = re.compile(r"(?<=\])\(\s*(?P<target>[^)\s]+)(?P<title>\s+\"[^\"]*\")?\s*\)")
FENCE_RE = re.compile(r"^\s{0,3}(?P<marker>```+|~~~+)")
INLINE_CODE_RE = re.compile(r"(`+)(?:(?!\1).)*?\1", re.DOTALL)

SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#", "//", "/")

# Repo tooling that is deliberately not part of the site. Links to it are sent to
# GitHub rather than dropped, because the pages they point at are real.
GITHUB_BLOB = "https://github.com/PatrickWiloak/cloud-data-ai-security-zero-to-hero/blob/main/"
OFF_SITE_PREFIXES = (".github/", ".gitignore", ".markdownlint.json", ".cspell.json", "CODEOWNERS")


def _rewrite_target(target: str, page_dir: Path) -> str:
    """Adapt one link target to how MkDocs resolves links.

    Two shapes need help. `.templates/` was staged as `templates/`, and MkDocs
    only resolves links that name a file, so the repo's ~1,200 directory links
    (`](../notes/)`, which GitHub renders as a directory listing) have to point
    at that directory's README.md instead.
    """
    if not target or target.startswith(SKIP_PREFIXES):
        return target

    anchor = ""
    if "#" in target:
        target, _, anchor_part = target.partition("#")
        anchor = "#" + anchor_part
        if not target:
            return target + anchor

    for original, staged_as in STAGE_RENAMES.items():
        if f"{original}/" in target:
            target = target.replace(f"{original}/", f"{staged_as}/")

    # Point at GitHub for the repo-tooling files the site does not publish.
    normalised = target
    while normalised.startswith(("./", "../")):
        normalised = normalised.split("/", 1)[1]
    for prefix in OFF_SITE_PREFIXES:
        if normalised.startswith(prefix):
            return GITHUB_BLOB + normalised + anchor

    # Directory links appear both with and without a trailing slash. Anything
    # that is not obviously a file gets probed against the staged tree.
    last = target.rsplit("/", 1)[-1]
    if target.endswith("/") or "." not in last:
        try:
            resolved = (page_dir / target).resolve()
            resolved.relative_to(STAGE.resolve())
        except (ValueError, OSError):
            return target + anchor
        if resolved.is_dir() and (resolved / "README.md").is_file():
            target = target.rstrip("/") + "/README.md"

    return target + anchor


def rewrite_links() -> int:
    """Fence-aware link rewrite across the staged tree. Returns files changed."""
    changed = 0
    for md_path in sorted(STAGE.rglob("*.md")):
        original = md_path.read_text(encoding="utf-8", errors="replace")
        page_dir = md_path.parent
        out_lines: list[str] = []
        fence: str | None = None

        for line in original.splitlines(keepends=True):
            m = FENCE_RE.match(line)
            if fence is not None:
                # Inside a fence: only a matching closing marker ends it.
                if m and m.group("marker")[0] == fence[0] and len(m.group("marker")) >= len(fence):
                    fence = None
                out_lines.append(line)
                continue
            if m:
                fence = m.group("marker")
                out_lines.append(line)
                continue

            # Mask inline code so link-like text inside backticks is untouched.
            spans: list[str] = []

            def _mask(mo: re.Match) -> str:
                spans.append(mo.group(0))
                return f"\x00{len(spans) - 1}\x00"

            masked = INLINE_CODE_RE.sub(_mask, line)
            masked = LINK_RE.sub(
                lambda mo: "(" + _rewrite_target(mo.group("target"), page_dir) + (mo.group("title") or "") + ")",
                masked,
            )
            restored = re.sub(r"\x00(\d+)\x00", lambda mo: spans[int(mo.group(1))], masked)
            out_lines.append(restored)

        updated = "".join(out_lines)
        if updated != original:
            md_path.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


# --------------------------------------------------------------------------- #
# Labels
# --------------------------------------------------------------------------- #

_title_cache: dict[Path, str] = {}
_cert_labels: dict[str, str] = {}
_provider_labels: dict[str, str] = {}


def load_cert_labels() -> None:
    """Use certs.json for cert and provider display names in the nav."""
    if not CERTS_JSON.is_file():
        return
    data = json.loads(CERTS_JSON.read_text(encoding="utf-8"))
    for cert in data.get("certs", []):
        path, name = cert.get("path"), cert.get("name")
        if path and name:
            _cert_labels[path.rstrip("/")] = name
    for meta in data.get("providers", {}).values():
        path, name = meta.get("path"), meta.get("name")
        if path and name:
            _provider_labels[path.rstrip("/")] = name


def prettify(stem: str) -> str:
    words = stem.replace("_", "-").split("-")
    small = {"a", "an", "and", "as", "at", "by", "for", "in", "of", "on", "or", "the", "to", "vs", "with"}
    acronyms = {
        "ai", "api", "aws", "cd", "ci", "cli", "cncf", "dns", "gcp", "genai", "gpu", "iam",
        "iac", "k8s", "llm", "llms", "mcp", "ml", "nvidia", "rag", "sre", "sql", "ssl", "tls", "vpc",
    }
    out = []
    for i, w in enumerate(words):
        lw = w.lower()
        if lw in acronyms:
            out.append(lw.upper())
        elif i > 0 and lw in small:
            out.append(lw)
        else:
            out.append(w[:1].upper() + w[1:] if w else w)
    return " ".join(out)


def title_of(path: Path) -> str:
    """Prefer the page's H1; fall back to a prettified filename."""
    if path in _title_cache:
        return _title_cache[path]
    title = ""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        body = FRONTMATTER_RE.sub("", text)
        m = H1_RE.search(body)
        if m:
            title = m.group(1)
    except OSError:
        pass
    if not title:
        title = prettify(path.stem)
    # Nav labels are one line in a narrow column: drop decoration and trailing
    # parentheticals that only repeat the exam code already shown on the page.
    title = re.sub(r"[#*`]", "", title).strip()
    title = re.sub(r"^[^\w(]+\s*", "", title)  # leading emoji or symbols
    title = re.sub(r"\s+", " ", title)
    if len(title) > 72:
        title = title[:69].rstrip() + "..."
    _title_cache[path] = title
    return title


def label_for_dir(rel_posix: str, basename: str) -> str:
    if rel_posix in GROUP_LABELS:
        return GROUP_LABELS[rel_posix]
    if rel_posix in _cert_labels:
        return _cert_labels[rel_posix]
    if rel_posix in _provider_labels:
        return _provider_labels[rel_posix]
    if basename in LEVEL_ORDER:
        return basename.capitalize()
    return prettify(basename)


# --------------------------------------------------------------------------- #
# Navigation
# --------------------------------------------------------------------------- #

def sort_key_for(rel_posix: str, basename: str, is_dir: bool) -> tuple:
    """Reading order: level dirs by progression, cert files by study order."""
    if basename in LEVEL_ORDER:
        return (0, LEVEL_ORDER[basename], basename.lower())
    if basename in CERT_FILE_ORDER:
        return (0, CERT_FILE_ORDER[basename], basename.lower())
    if basename.rstrip(".md") in CERT_FILE_ORDER:
        return (0, CERT_FILE_ORDER[basename.rstrip(".md")], basename.lower())
    # Numbered notes (01-foo.md) sort naturally by their prefix.
    m = re.match(r"^(\d+)[-_]", basename)
    if m:
        return (1, int(m.group(1)), basename.lower())
    return (2, 0, label_for_dir(rel_posix, basename).lower() if is_dir else basename.lower())


def build_dir_nav(dirpath: Path) -> list:
    """Recursively turn a staged directory into a MkDocs nav list."""
    rel_dir = dirpath.relative_to(STAGE).as_posix()
    entries: list[tuple[tuple, object]] = []

    readme = dirpath / "README.md"
    children: list = []
    if readme.is_file():
        # navigation.indexes renders a bare path first in a section as its landing page.
        children.append((readme.relative_to(STAGE)).as_posix())

    for child in sorted(dirpath.iterdir()):
        name = child.name
        if name in EXCLUDED_DIR_NAMES:
            continue
        rel = child.relative_to(STAGE).as_posix()
        if child.is_dir():
            sub = build_dir_nav(child)
            if sub:
                entries.append((sort_key_for(rel, name, True), {label_for_dir(rel, name): sub}))
        elif child.suffix == ".md":
            if name == "README.md":
                continue
            entries.append((sort_key_for(rel, name, False), {title_of(child): rel}))

    entries.sort(key=lambda e: e[0])
    children.extend(item for _, item in entries)
    return children


def resource_group_of(filename: str) -> str:
    for pattern, group in RESOURCE_GROUPS:
        if re.match(pattern, filename):
            return group
    return "resources/misc"


def build_resource_groups() -> dict[str, list]:
    """Bucket the flat files directly inside resources/ into virtual groups."""
    groups: dict[str, list[tuple[str, str]]] = {}
    res = STAGE / "resources"
    if not res.is_dir():
        return {}
    for child in sorted(res.iterdir()):
        if not child.is_file() or child.suffix != ".md":
            continue
        if child.name == "README.md":
            continue
        group = resource_group_of(child.name)
        groups.setdefault(group, []).append((title_of(child), child.relative_to(STAGE).as_posix()))
    return {g: [{t: p} for t, p in sorted(items)] for g, items in groups.items()}


def build_nav() -> list:
    resource_groups = build_resource_groups()
    nav: list = ["README.md"]

    for tab_name, members in TABS:
        section: list = []
        for member in members:
            if member in resource_groups:
                section.append({GROUP_LABELS.get(member, prettify(Path(member).name)): resource_groups[member]})
                continue
            path = STAGE / member
            if path.is_dir():
                sub = build_dir_nav(path)
                if not sub:
                    continue
                # A tab with a single directory member (Learn, Topics) reads better
                # flattened than nested one level deeper under its own name.
                if len(members) == 1:
                    section.extend(sub)
                else:
                    section.append({label_for_dir(member, path.name): sub})
            elif path.is_file() and path.suffix == ".md":
                section.append({title_of(path): member})
        if section:
            nav.append({tab_name: section})
    return nav


def dump_nav(nav: list, indent: int = 2) -> str:
    """Emit nav as YAML. Written by hand so the base config's `!!python/name:`
    tags survive: the config is treated as text and never round-tripped."""
    lines: list[str] = []

    def quote(s: str) -> str:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

    def walk(items: list, depth: int) -> None:
        pad = " " * (depth * indent)
        for item in items:
            if isinstance(item, str):
                lines.append(f"{pad}- {item}")
            elif isinstance(item, dict):
                (title, value), = item.items()
                if isinstance(value, str):
                    lines.append(f"{pad}- {quote(title)}: {value}")
                else:
                    lines.append(f"{pad}- {quote(title)}:")
                    walk(value, depth + 1)

    lines.append("nav:")
    walk(nav, 1)
    return "\n".join(lines) + "\n"


# Pages deliberately built and searchable but kept out of the nav: they document
# the asset directories for contributors rather than teaching anything.
NAV_EXEMPT = {"assets/README.md", "assets/diagrams/README.md"}


def nav_coverage(nav: list) -> list[str]:
    """Staged pages that no nav entry points at.

    Without this, adding a directory the TABS table does not mention drops its
    pages out of the navigation silently: MkDocs only reports the first few and
    only at INFO level, so it never fails a build.
    """
    referenced: set[str] = set()

    def walk(items: list) -> None:
        for item in items:
            if isinstance(item, str):
                referenced.add(item)
            elif isinstance(item, dict):
                (_, value), = item.items()
                if isinstance(value, str):
                    referenced.add(value)
                else:
                    walk(value)

    walk(nav)
    staged = {p.relative_to(STAGE).as_posix() for p in STAGE.rglob("*.md")}
    return sorted(staged - referenced - NAV_EXEMPT)


def count_entries(nav: list) -> int:
    n = 0
    for item in nav:
        if isinstance(item, str):
            n += 1
        elif isinstance(item, dict):
            (_, value), = item.items()
            n += 1 if isinstance(value, str) else count_entries(value)
    return n


# --------------------------------------------------------------------------- #

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true", help="treat MkDocs warnings as errors")
    ap.add_argument("--serve", action="store_true", help="stage, then run mkdocs serve")
    ap.add_argument("--stage-only", action="store_true", help="stage and generate config, skip the build")
    args = ap.parse_args()

    load_cert_labels()

    print("Staging content into .site-src/ ...")
    staged = stage()
    md = sum(1 for p in staged if p.endswith(".md"))
    print(f"  staged {len(staged)} files ({md} markdown, {len(staged) - md} static)")

    created = generate_missing_indexes()
    print(f"  generated {len(created)} directory index pages")

    rewritten = rewrite_links()
    print(f"  rewrote links in {rewritten} pages")

    print("Generating navigation ...")
    nav = build_nav()
    print(f"  {count_entries(nav)} nav entries")

    orphans = nav_coverage(nav)
    if orphans:
        print(f"ERROR: {len(orphans)} staged pages are not reachable from the nav.", file=sys.stderr)
        print("Add the directory to TABS in this script, or to NAV_EXEMPT if that is intended:", file=sys.stderr)
        for o in orphans[:20]:
            print(f"  - {o}", file=sys.stderr)
        if len(orphans) > 20:
            print(f"  ... and {len(orphans) - 20} more", file=sys.stderr)
        return 1

    base = BASE_CONFIG.read_text(encoding="utf-8")
    if re.search(r"^nav:", base, re.MULTILINE):
        print("ERROR: mkdocs.yml defines `nav`; it must be generated here.", file=sys.stderr)
        return 1
    banner = (
        "\n# ---------------------------------------------------------------------\n"
        "# GENERATED by .github/scripts/build-site.py. Do not edit; edit the\n"
        "# generator or mkdocs.yml instead. This file is gitignored.\n"
        "# ---------------------------------------------------------------------\n"
    )
    GENERATED_CONFIG.write_text(base + banner + dump_nav(nav), encoding="utf-8")
    print(f"  wrote {GENERATED_CONFIG.relative_to(REPO)}")

    if args.stage_only:
        return 0

    mkdocs = REPO / ".venv-docs" / "bin" / "mkdocs"
    cmd = [str(mkdocs) if mkdocs.exists() else "mkdocs"]
    cmd += ["serve"] if args.serve else ["build", "--clean"]
    cmd += ["-f", str(GENERATED_CONFIG)]
    if args.strict:
        cmd.append("--strict")

    print(f"Running: {' '.join(cmd)}")
    return subprocess.call(cmd, cwd=REPO)


if __name__ == "__main__":
    sys.exit(main())
