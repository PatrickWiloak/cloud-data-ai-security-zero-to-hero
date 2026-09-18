#!/usr/bin/env python3
"""Verify the GitHub repository's own metadata against the tree.

Why this exists: on 2026-09-17 every counted claim *inside* the repo was under
CI and correct, while the repository description - the one sentence that appears
in GitHub search results, in the sidebar, and in every link preview - still read
"122+ certs across 22 providers, 37 plain-English concepts". The tree was at 148
certs, 27 providers, 46 concept pages. It had been wrong for months because
check-readme-counts.py can only see files, and the description is not a file.

So the same rule applies one level out: the description is generated from
docs/certs.json and the tree, never typed. The homepage and the social preview
are checked too, because both are load-bearing for how the project is found and
neither lives in the repo either.

    python3 .github/scripts/check-repo-metadata.py            # report drift
    python3 .github/scripts/check-repo-metadata.py --check    # exit 1 on drift
    python3 .github/scripts/check-repo-metadata.py --fix      # PATCH the repo

--fix needs a token with administration:write, which the Actions GITHUB_TOKEN
does not have by design. Run it locally with `gh auth` as the repo owner; CI's
job is only to notice.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SLUG = "PatrickWiloak/cloud-data-ai-security-zero-to-hero"
SITE_URL = "https://patrickwiloak.github.io/cloud-data-ai-security-zero-to-hero/"

# The description GitHub shows. Every number is a token; none is typed. Keep it
# under 350 characters, which is GitHub's limit.
DESCRIPTION_TEMPLATE = (
    "Cloud + Data + AI + Security from zero to hero. "
    "{certifications} certs across {providers} providers, "
    "{concept_pages} plain-English concepts, "
    "{hands_on_projects} hands-on builds, "
    "cross-cloud + AI service comparisons."
)

# Topics carry the repo in GitHub's own search and on topic pages, so a missing
# one is lost traffic. This is a floor, not the whole set - extra topics are fine.
REQUIRED_TOPICS = {
    "ai",
    "aws",
    "azure",
    "certifications",
    "cloud",
    "gcp",
    "kubernetes",
    "llm",
    "security",
}


def counts() -> dict[str, int]:
    """Reuse check-readme-counts.py's gather(), so there is one counting rule.

    Loaded by path because the filename has hyphens and is not importable.
    """
    path = Path(__file__).with_name("check-readme-counts.py")
    spec = importlib.util.spec_from_file_location("check_readme_counts", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.gather()


def gh_api(path: str, method: str = "GET", fields: dict | None = None) -> dict:
    cmd = ["gh", "api", "-X", method, path]
    for key, value in (fields or {}).items():
        cmd += ["-f", f"{key}={value}"]
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError(out.stderr.strip() or f"gh api {path} failed")
    return json.loads(out.stdout) if out.stdout.strip() else {}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="exit 1 on drift")
    parser.add_argument("--fix", action="store_true", help="PATCH the repo metadata")
    args = parser.parse_args()

    if not shutil_which("gh"):
        print("gh CLI not found, skipping repository metadata check.")
        print("This check is about GitHub-side settings, so it cannot run offline.")
        return 0

    try:
        repo = gh_api(f"repos/{SLUG}")
    except RuntimeError as exc:
        # No token locally is not a content defect. In CI it is, so say which.
        where = "CI" if os.environ.get("GITHUB_ACTIONS") else "locally"
        print(f"Could not read repository metadata {where}: {exc}")
        return 1 if os.environ.get("GITHUB_ACTIONS") else 0

    actual = counts()
    want_description = DESCRIPTION_TEMPLATE.format(**actual)

    # Split deliberately. `problems` are things a command can fix, so they block.
    # `notices` are things only a human clicking in Settings can fix, so they do
    # not: a check that fails until somebody does something CI cannot do is a red
    # build nobody can clear, and a permanently red build stops being read.
    problems: list[str] = []
    notices: list[str] = []
    patch: dict[str, str] = {}

    have_description = (repo.get("description") or "").strip()
    if have_description != want_description:
        problems.append(
            "Repository description is out of date.\n"
            f"       is:     {have_description or '(empty)'}\n"
            f"       should: {want_description}"
        )
        patch["description"] = want_description

    if (repo.get("homepage") or "").rstrip("/") != SITE_URL.rstrip("/"):
        problems.append(
            f"Homepage should be the published site: {SITE_URL} "
            f"(is: {repo.get('homepage') or '(empty)'})"
        )
        patch["homepage"] = SITE_URL

    missing_topics = sorted(REQUIRED_TOPICS - set(repo.get("topics") or []))
    if missing_topics:
        notices.append(
            f"Missing GitHub topics: {', '.join(missing_topics)}. "
            "Add them under the repository's About panel."
        )

    # The social preview is not exposed for writing by the API, so this can only
    # ever be a report. Without it every share of the repo renders GitHub's
    # generic auto-card instead of the project's own.
    if not repo.get("open_graph_image_url"):
        notices.append(
            "No custom social preview image is set. Upload "
            "assets/brand/social-preview-1280x640.png via "
            "Settings > General > Social preview (the API does not expose it)."
        )

    for notice in notices:
        print(f"  NOTE   {notice}")

    if not problems:
        print(f"Repository metadata is current ({actual['certifications']} certs, "
              f"{actual['providers']} providers, {actual['concept_pages']} concepts).")
        return 0

    for problem in problems:
        print(f"  DRIFT  {problem}")

    if args.fix and patch:
        gh_api(f"repos/{SLUG}", method="PATCH", fields=patch)
        print(f"\nPatched: {', '.join(sorted(patch))}")
        print("Topics and the social preview, if listed above, still need doing by hand.")
        return 0

    if args.check:
        print("\nFix with: python3 .github/scripts/check-repo-metadata.py --fix")
        print("(needs admin rights on the repo, so run it locally, not in CI)")
        return 1
    return 0


def shutil_which(name: str) -> str | None:
    import shutil

    return shutil.which(name)


if __name__ == "__main__":
    sys.exit(main())
