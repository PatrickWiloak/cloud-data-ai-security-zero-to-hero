#!/usr/bin/env python3
"""Generate the lab-to-cert mapping from hands-on project frontmatter.

The repo has 15 guided builds and 137 cert guides with nothing connecting them, so a
reader studying for DP-203 had no way to discover that "Build a data pipeline" is the
matching lab. Each project declares the certs it supports:

    certs:
      - aws/associate/data-engineer-dea-c01
      - azure/dp-203

From that, two generated views:

  1. resources/hands-on-projects/README.md - a "which labs for which cert" block,
     so someone browsing labs sees what each one is worth.
  2. resources/hands-on-projects/labs-by-cert.md - the reverse index, so someone
     studying a specific cert can find their labs. This is the direction most readers
     actually need.

Cert IDs are validated against docs/certs.json. A typo fails the run rather than
silently producing a dead link.

Run:    python3 .github/scripts/build-lab-map.py
        python3 .github/scripts/build-lab-map.py --check   # CI: fail if stale
"""

import json
import os
import re
import sys

INDEX = "docs/certs.json"
PROJECTS_DIR = "resources/hands-on-projects"
PROJECTS_README = f"{PROJECTS_DIR}/README.md"
REVERSE_PAGE = f"{PROJECTS_DIR}/labs-by-cert.md"
BEGIN = "<!-- BEGIN GENERATED: {} - run .github/scripts/build-lab-map.py -->"
END = "<!-- END GENERATED: {} -->"

PROVIDER_ORDER = [
    "aws", "azure", "gcp", "kubernetes", "hashicorp", "databricks", "nvidia",
    "github", "redhat", "comptia", "cloud-security-alliance", "anthropic",
]


def read_frontmatter_list(path, key):
    text = open(path, encoding="utf-8").read()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return [], None
    block = match.group(1)
    listed = re.search(rf"^{re.escape(key)}:\n((?:  - .*\n?)+)", block, re.M)
    values = re.findall(r"^  - (.+)$", listed.group(1), re.M) if listed else []
    title = None
    heading = re.search(r"^# (.+)$", text, re.M)
    if heading:
        title = heading.group(1).strip()
    return [v.strip() for v in values], title


def generated_block(name, body):
    return f"{BEGIN.format(name)}\n\n{body}\n\n{END.format(name)}"


def splice(text, name, body):
    pattern = re.compile(re.escape(BEGIN.format(name)) + r".*?" + re.escape(END.format(name)), re.S)
    if not pattern.search(text):
        return None
    return pattern.sub(lambda _: generated_block(name, body), text)


def main():
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    check = "--check" in sys.argv
    index = json.load(open(INDEX, encoding="utf-8"))
    by_id = {c["id"]: c for c in index["certs"]}

    projects = {}
    for filename in sorted(os.listdir(PROJECTS_DIR)):
        if not filename.endswith(".md") or filename in ("README.md", "labs-by-cert.md"):
            continue
        path = os.path.join(PROJECTS_DIR, filename)
        certs, title = read_frontmatter_list(path, "certs")
        if not certs:
            continue
        unknown = [c for c in certs if c not in by_id]
        if unknown:
            print(f"{path}: unknown cert id(s): {', '.join(unknown)}")
            return 1
        projects[filename[:-3]] = {"title": title or filename[:-3], "certs": certs}

    # Forward view: lab -> certs it supports.
    rows = ["| Lab | Certs it supports |", "|------|-------------------|"]
    for slug, data in sorted(projects.items(), key=lambda kv: kv[1]["title"].lower()):
        names = ", ".join(
            f"[{by_id[c]['exam_code'] or by_id[c]['name']}](../../{by_id[c]['path']}/)"
            for c in data["certs"]
        )
        rows.append(f"| [{data['title']}](./{slug}.md) | {names} |")
    forward = "\n".join(rows)

    # Reverse view: cert -> labs, which is the direction readers need.
    labs_for = {}
    for slug, data in projects.items():
        for cert_id in data["certs"]:
            labs_for.setdefault(cert_id, []).append((data["title"], slug))

    sections = []
    providers = sorted({by_id[c]["provider"] for c in labs_for},
                       key=lambda p: (PROVIDER_ORDER.index(p) if p in PROVIDER_ORDER else 99, p))
    for provider in providers:
        entries = sorted((c for c in labs_for if by_id[c]["provider"] == provider),
                         key=lambda c: by_id[c]["name"].lower())
        lines = [f"### {by_id[entries[0]]['provider_name']}", "",
                 "| Cert | Labs |", "|------|------|"]
        for cert_id in entries:
            cert = by_id[cert_id]
            labs = ", ".join(f"[{title}](./{slug}.md)" for title, slug in sorted(labs_for[cert_id]))
            # Most names already carry the code in parentheses; do not repeat it.
            code = cert["exam_code"]
            label = cert["name"] if not code or code in cert["name"] else f"{cert['name']} ({code})"
            lines.append(f"| [{label}](../../{cert['path']}/) | {labs} |")
        sections.append("\n".join(lines))
    reverse_body = "\n\n".join(sections)

    covered = len(labs_for)
    total = index["totals"]["cert_directories"]
    reverse_page = (
        "---\nlast-updated: 2026-07-29\n---\n\n"
        "# Labs by certification\n\n"
        "Which [hands-on projects](./README.md) back up which certification. Doing the lab "
        "is worth more than re-reading the notes: most of these exams test whether you have "
        "actually built the thing.\n\n"
        f"{covered} of {total} cert guides have a matching lab. The rest have no lab yet - "
        "that is a gap, not a judgement about the cert. Labs are mapped by hand in each "
        "project's `certs:` frontmatter.\n\n"
        + generated_block("labs-by-cert", reverse_body) + "\n"
    )

    changed = []
    readme = open(PROJECTS_README, encoding="utf-8").read()
    spliced = splice(readme, "lab-cert-map", forward)
    if spliced is None:
        spliced = readme.rstrip() + "\n\n## Which lab for which cert\n\n" + \
            "Each lab maps to the certs it exercises. The reverse index lives in " \
            "[labs-by-cert.md](./labs-by-cert.md).\n\n" + \
            generated_block("lab-cert-map", forward) + "\n"
    if spliced != readme:
        changed.append(PROJECTS_README)
        if not check:
            open(PROJECTS_README, "w", encoding="utf-8").write(spliced)

    existing = open(REVERSE_PAGE, encoding="utf-8").read() if os.path.isfile(REVERSE_PAGE) else None
    if existing != reverse_page:
        changed.append(REVERSE_PAGE)
        if not check:
            open(REVERSE_PAGE, "w", encoding="utf-8").write(reverse_page)

    if check:
        if changed:
            print("Lab map is out of date:")
            for path in changed:
                print(f"  {path}")
            print("\nRun: python3 .github/scripts/build-lab-map.py")
            return 1
        print("Lab map is up to date.")
        return 0

    print(f"{len(projects)} labs mapped to {covered} certs. Wrote {len(changed)} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
