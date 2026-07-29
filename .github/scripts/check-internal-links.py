#!/usr/bin/env python3
"""Check that every relative markdown link resolves to a file on disk.

Complements the lychee workflow, which checks external URLs. External URLs rot for
reasons outside a contributor's control, so that check is advisory. Internal links
are fully under our control, so this check is blocking.

Skips, because these are not real links:
  - fenced code blocks (``` and ~~~)
  - inline code spans (`like this`)
  - external schemes (http, https, mailto, tel) and bare anchors (#section)
  - image and link targets containing < > placeholders, e.g. <topic>/<slug>.png

Run locally: python3 .github/scripts/check-internal-links.py
Exits 1 if any internal link is broken.
"""

import os
import re
import sys

SKIP_DIRS = {".git", "node_modules", ".github/scripts/__pycache__"}
EXTERNAL = re.compile(r"^(https?:|mailto:|tel:|#)")
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE = re.compile(r"`[^`]*`")


def strip_code(lines):
    """Yield (lineno, text) with fenced blocks blanked and inline code removed."""
    in_fence = False
    for i, line in enumerate(lines, 1):
        if FENCE.match(line):
            in_fence = not in_fence
            yield i, ""
            continue
        yield i, "" if in_fence else INLINE_CODE.sub("", line)


def target_path(link):
    """Strip the optional title and the anchor from a markdown link target."""
    link = link.strip()
    if " " in link:  # [text](path "Title")
        link = link.split(" ", 1)[0]
    return link.split("#", 1)[0].strip()


def main():
    broken = []
    checked = 0
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in sorted(files):
            if not name.endswith(".md"):
                continue
            path = os.path.join(root, name)
            with open(path, encoding="utf-8", errors="ignore") as fh:
                lines = fh.readlines()
            for lineno, text in strip_code(lines):
                for match in LINK.finditer(text):
                    dest = target_path(match.group(1))
                    if not dest or EXTERNAL.match(dest) or "<" in dest:
                        continue
                    checked += 1
                    resolved = os.path.normpath(os.path.join(root, dest))
                    if not os.path.exists(resolved):
                        broken.append((path, lineno, dest))

    for path, lineno, dest in broken:
        print(f"BROKEN  {path}:{lineno}  ->  {dest}")

    print(f"\nSummary: {checked} internal links checked. Broken: {len(broken)}.")
    if broken:
        print(
            "\nFix by repointing the link, or drop the link and mark the target "
            "_(planned)_ if it has not been written yet."
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
