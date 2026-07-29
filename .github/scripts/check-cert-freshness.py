#!/usr/bin/env python3
"""Report which cert guides are due for re-verification, and which exams may have moved.

Two problems this solves.

**Staleness clustering.** 326 pages were stamped 2026-05-03 in a single sweep, so at the
documented 180-day cadence the entire repo would fall due on the same day. A ledger where
everything expires at once carries no information. This script assigns each provider a
review month, spreading the work across the year, so "what is due now" is always a
manageable slice rather than everything or nothing.

**Exam revisions.** Vendors rotate exam codes (SAA-C03 to C04, SY0-701 to 801) and retire
exams on announced dates. A fact-sheet can be perfectly accurate about an exam that no
longer exists. Two optional frontmatter fields let a guide declare what it tracks:

    exam-version: SAA-C03        # the exam revision this guide describes
    exam-retires: 2026-11-30     # announced retirement or replacement date, if known

Anything with `exam-retires` inside the warning window is flagged regardless of how
recently it was verified.

Run:    python3 .github/scripts/check-cert-freshness.py            # full report
        python3 .github/scripts/check-cert-freshness.py --due      # only what is due now
        python3 .github/scripts/check-cert-freshness.py --month 3  # pretend it is March
"""

import datetime
import json
import os
import sys

INDEX = "docs/certs.json"
STALE_DAYS = 180
RETIREMENT_WARNING_DAYS = 120


def review_month(provider, providers):
    """Assign each provider a review month, 1-12, spread evenly and stable over time.

    Deterministic on sorted provider order so a provider keeps its slot as certs are
    added. Providers are spread across the year rather than by size, because the point
    is a predictable rhythm, not perfectly equal batches.
    """
    ordered = sorted(providers)
    return (ordered.index(provider) % 12) + 1


def parse_date(value):
    try:
        return datetime.date.fromisoformat(value) if value else None
    except ValueError:
        return None


def main():
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    if not os.path.isfile(INDEX):
        print(f"{INDEX} is missing. Run: python3 .github/scripts/build-certs-index.py")
        return 1
    index = json.load(open(INDEX, encoding="utf-8"))
    certs = index["certs"]
    providers = list(index["providers"])

    today = datetime.date.today()
    this_month = today.month
    if "--month" in sys.argv:
        this_month = int(sys.argv[sys.argv.index("--month") + 1])
    due_only = "--due" in sys.argv

    overdue, due_now, retiring, undated = [], [], [], []
    for cert in certs:
        verified = parse_date(cert.get("last_updated"))
        month = review_month(cert["provider"], providers)
        age = (today - verified).days if verified else None

        # Only warn about exams still presented as current. A cert already marked
        # retired has its replacement documented, so re-flagging it every run is noise.
        retires = parse_date(cert.get("exam_retires"))
        if (retires and cert["status"] != "retired"
                and (retires - today).days <= RETIREMENT_WARNING_DAYS):
            retiring.append((cert, retires))

        if verified is None:
            undated.append(cert)
        elif age > STALE_DAYS:
            overdue.append((cert, age))
        elif month == this_month:
            due_now.append((cert, age))

    if retiring:
        print(f"EXAM CHANGES within {RETIREMENT_WARNING_DAYS} days ({len(retiring)}) "
              f"- these are still presented as current:")
        for cert, retires in sorted(retiring, key=lambda r: r[1]):
            days = (retires - today).days
            state = "RETIRED" if days < 0 else f"in {days}d"
            print(f"  {retires}  {state:<10} {cert['id']}  ({cert.get('exam_version') or cert.get('exam_code') or '-'})")
        print()

    if overdue:
        print(f"OVERDUE - past {STALE_DAYS} days ({len(overdue)}):")
        for cert, age in sorted(overdue, key=lambda r: -r[1]):
            print(f"  {age:4d}d  {cert['id']}")
        print()

    print(f"DUE THIS MONTH - month {this_month} rotation ({len(due_now)}):")
    for cert, age in sorted(due_now, key=lambda r: -r[1]):
        print(f"  {age:4d}d  {cert['id']}")

    if undated and not due_only:
        print(f"\nNO last-updated FRONTMATTER ({len(undated)}):")
        for cert in undated:
            print(f"        {cert['id']}")

    if not due_only:
        print("\nReview rotation by provider:")
        for month in range(1, 13):
            names = [p for p in sorted(providers) if review_month(p, providers) == month]
            if names:
                marker = " <- current" if month == this_month else ""
                print(f"  month {month:2d}: {', '.join(names)}{marker}")

    print(f"\n{len(certs)} certs. Overdue {len(overdue)}, due this month {len(due_now)}, "
          f"undated {len(undated)}, exam changes {len(retiring)}.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        # Piping into head closes stdout early; that is not an error.
        sys.exit(0)
