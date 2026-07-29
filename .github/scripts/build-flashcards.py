#!/usr/bin/env python3
"""Generate per-cert flashcards.csv for spaced-repetition import (Anki, Quizlet, etc).

Cards are extracted, not invented. Two sources, both already present in the repo:

  1. **Exam logistics** from docs/certs.json - duration, question count, passing score,
     cost, validity. These make reliable recall cards and every value is already
     verified against the fact-sheet.

  2. **Term-definition pairs** from the cert's notes, which this repo already writes in
     a consistent shape:

         - **kube-apiserver** - the front end of the control plane, serves the API

     That dash-separated bold-term line is a definition, so it converts to a card with
     no rewriting and no paraphrasing.

Nothing is generated from headings alone: "What is Cluster Architecture?" with no
sourced answer would be a card that teaches nothing. If a cert yields fewer than
MIN_CARDS it gets no file, and is listed in the report instead.

Output is CSV with a header row: Question, Answer, Tags. Anki's import dialog maps
these directly; set the field separator to comma and enable "allow HTML" off.

Run:    python3 .github/scripts/build-flashcards.py            # write all decks
        python3 .github/scripts/build-flashcards.py --report   # counts only, no writes
        python3 .github/scripts/build-flashcards.py --check    # CI: fail if stale
"""

import csv
import io
import json
import os
import re
import sys

INDEX = "docs/certs.json"
OUTPUT_NAME = "flashcards.csv"
MIN_CARDS = 15
MAX_CARDS = 300

# "- **Term** - definition text", the definition shape used throughout the notes.
DEFINITION = re.compile(
    r"^\s*[-*]\s+\*\*([^*]{2,60})\*\*\s*[-–—:]\s+(.{15,400})$", re.M
)
FENCE = re.compile(r"^\s*(```|~~~)")


def clean(text):
    """Flatten markdown so a card reads as plain text."""
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = text.replace("**", "").replace("`", "")
    text = re.sub(r"<[^>]+>", "", text)
    return " ".join(text.split()).strip(" -:")


def strip_fenced(text):
    """Drop fenced code blocks; command listings are not definitions."""
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(line)
    return "\n".join(out)


def logistics_cards(cert):
    """High-confidence recall cards from the verified fact-sheet fields."""
    name = cert["name"]
    specs = [
        ("duration", f"How long is the {name} exam?"),
        ("questions", f"How many questions are on the {name} exam?"),
        ("passing_score", f"What is the passing score for {name}?"),
        ("cost", f"What does the {name} exam cost?"),
        ("validity", f"How long is {name} valid for?"),
        ("delivery", f"How is the {name} exam delivered?"),
    ]
    cards = []
    for key, question in specs:
        value = cert.get(key)
        if value:
            cards.append((question, clean(value), "exam-logistics"))
    return cards


def definition_cards(cert):
    notes_dir = os.path.join(cert["path"], "notes")
    if not os.path.isdir(notes_dir):
        return []
    cards = []
    for filename in sorted(os.listdir(notes_dir)):
        if not filename.endswith(".md"):
            continue
        text = strip_fenced(open(os.path.join(notes_dir, filename), encoding="utf-8").read())
        topic = re.sub(r"^\d+[-.]?\s*", "", filename[:-3]).replace("-", " ")
        for term, definition in DEFINITION.findall(text):
            term, definition = clean(term), clean(definition)
            # Skip pairs where the "definition" is really a continuation or a bare link.
            if not term or len(definition) < 15 or term.lower() == definition.lower():
                continue
            cards.append((f"{term} ({topic})", definition, f"notes,{topic.replace(' ', '-')}"))
    return cards


def build_deck(cert):
    cards, seen = [], set()
    for question, answer, tags in logistics_cards(cert) + definition_cards(cert):
        key = question.lower()
        if key in seen:
            continue
        seen.add(key)
        cards.append((question, answer, tags))
    return cards


def render(cards, truncated):
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Question", "Answer", "Tags"])
    for row in cards:
        writer.writerow(row)
    if truncated:
        # Never truncate silently: a deck that quietly stops at 300 reads as complete.
        writer.writerow([
            f"NOTE: deck truncated at {MAX_CARDS} cards",
            f"{truncated} further term-definition pairs exist in this cert's notes. "
            f"Raise MAX_CARDS in .github/scripts/build-flashcards.py to include them.",
            "meta",
        ])
    return buffer.getvalue()


def main():
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
    if not os.path.isfile(INDEX):
        print(f"{INDEX} is missing. Run: python3 .github/scripts/build-certs-index.py")
        return 1
    index = json.load(open(INDEX, encoding="utf-8"))
    report_only = "--report" in sys.argv
    check = "--check" in sys.argv

    written, skipped, stale, total = [], [], [], 0
    for cert in index["certs"]:
        cards = build_deck(cert)
        path = os.path.join(cert["path"], OUTPUT_NAME)
        if len(cards) < MIN_CARDS:
            skipped.append((cert["id"], len(cards)))
            if os.path.isfile(path) and not (report_only or check):
                os.remove(path)
            continue

        truncated = max(0, len(cards) - MAX_CARDS)
        rendered = render(cards[:MAX_CARDS], truncated)
        total += min(len(cards), MAX_CARDS)
        written.append((cert["id"], min(len(cards), MAX_CARDS)))

        if report_only:
            continue
        existing = open(path, encoding="utf-8").read() if os.path.isfile(path) else None
        if existing == rendered:
            continue
        if check:
            stale.append(path)
        else:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(rendered)

    if check:
        if stale:
            print("Flashcard decks are out of date:")
            for path in stale:
                print(f"  {path}")
            print("\nRun: python3 .github/scripts/build-flashcards.py")
            return 1
        print(f"Flashcard decks are up to date ({len(written)} decks).")
        return 0

    print(f"{len(written)} decks, {total} cards total.")
    print(f"{len(skipped)} certs below the {MIN_CARDS}-card threshold, no deck written:")
    for cert_id, count in sorted(skipped, key=lambda r: -r[1]):
        print(f"  {count:3d}  {cert_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
