#!/usr/bin/env python3
"""Tell IndexNow which site pages a push changed.

Runs in the deploy job of `.github/workflows/docs-site.yml` after Pages has
published. IndexNow feeds Bing, Yandex, Seznam and Naver, and through Bing,
DuckDuckGo and ChatGPT search. Google does not use it; Google reads the
sitemap, which Search Console re-reads once the property is set up (TODO.md).

Which URLs:
- A changed or deleted markdown page maps to its site URL, the same way
  build-site.py stages it (`README.md` is the directory's page, `.templates/`
  is published as `provider-resources/`, `.github/site/home.md` is the home page).
- A change to anything that renders on every page (the head template, the
  hooks, mkdocs.yml, build-site.py, the stylesheet) submits every URL in the
  live sitemap. IndexNow takes 10,000 URLs per request; the site has ~2,000.

MkDocs stamps every sitemap entry with the build date, so diffing sitemaps
(the fleet notifier's method) would announce every page on every push. The git
diff is the honest signal here.

Usage:
  notify-indexnow.py --before <sha> --after <sha> [--dry-run]
  notify-indexnow.py --all [--dry-run]

Exit codes: 0 ok or nothing to send, 1 IndexNow rejected the request, 2 usage.
The workflow step is continue-on-error: a failed ping never fails a deploy,
but it shows as a warning on the run.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SITE = "https://patrickwiloak.github.io/cloud-data-ai-security-zero-to-hero/"
HOST = "patrickwiloak.github.io"
KEY = (REPO / ".github" / "site" / "indexnow-key.txt").read_text(encoding="utf-8").strip()
ENDPOINT = "https://api.indexnow.org/indexnow"

CONTENT_DIRS = ("learn/", "resources/", "exams/", "topics/", "docs/", ".templates/")
# TODO.md and CLAUDE.md are published but noindex (site_hooks.NOINDEX).
ROOT_PAGES = {"README.md", "STUDY-HUB.md", "CONTRIBUTING.md", "CHANGELOG.md"}
SITE_WIDE = (
    "mkdocs.yml",
    ".github/site-overrides/",
    ".github/site/extra.css",
    ".github/scripts/site_hooks.py",
    ".github/scripts/build-site.py",
)


def url_for(path: str) -> str | None:
    if path == ".github/site/home.md":
        return SITE
    if not path.endswith(".md"):
        return None
    if path not in ROOT_PAGES and not path.startswith(CONTENT_DIRS):
        return None
    if path.startswith(".templates/"):
        path = "provider-resources/" + path.removeprefix(".templates/")
    stem = path[:-3]
    if stem == "README":
        return SITE
    if stem.endswith("/README"):
        stem = stem[: -len("/README")]
    return SITE + stem + "/"


def changed_paths(before: str, after: str) -> list[str]:
    out = subprocess.run(
        ["git", "diff", "--name-only", "--no-renames", f"{before}..{after}"],
        cwd=REPO, check=True, capture_output=True, text=True,
    ).stdout
    return [p for p in out.splitlines() if p]


def sitemap_urls() -> list[str]:
    with urllib.request.urlopen(SITE + "sitemap.xml", timeout=30) as r:
        xml = r.read().decode("utf-8")
    return re.findall(r"<loc>([^<]+)</loc>", xml)


def submit(urls: list[str], dry_run: bool) -> int:
    urls = sorted(set(urls))
    print(f"IndexNow: {len(urls)} URL(s)")
    for u in urls[:20]:
        print(f"  {u}")
    if len(urls) > 20:
        print(f"  ... and {len(urls) - 20} more")
    if dry_run or not urls:
        return 0
    body = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": f"{SITE}{KEY}.txt",
        "urlList": urls[:10_000],
    }).encode()
    req = urllib.request.Request(
        ENDPOINT, data=body, method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            print(f"IndexNow accepted: HTTP {r.status}")
            return 0
    except urllib.error.HTTPError as e:
        # 403 SiteVerificationNotCompleted is normal on a brand-new key while
        # Pages propagates the key file; the next push retries.
        print(f"IndexNow REJECTED: HTTP {e.code} {e.read().decode(errors='replace')[:300]}", file=sys.stderr)
        return 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--before")
    ap.add_argument("--after")
    ap.add_argument("--all", action="store_true", help="every URL in the live sitemap")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.all:
        return submit(sitemap_urls(), args.dry_run)
    if not args.after:
        ap.error("--after is required unless --all")
    # A manual run, a new branch or a force push has no usable "before".
    if not args.before or set(args.before) == {"0"}:
        return submit(sitemap_urls(), args.dry_run)

    paths = changed_paths(args.before, args.after)
    if any(p == s or p.startswith(s) for p in paths for s in SITE_WIDE):
        print("Site-wide change: submitting every URL in the sitemap.")
        return submit(sitemap_urls(), args.dry_run)
    return submit([u for p in paths if (u := url_for(p))], args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
