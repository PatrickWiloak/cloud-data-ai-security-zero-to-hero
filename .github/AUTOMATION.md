# Automation reference: `.github/` scripts and workflows

This directory holds CI workflows, validation scripts, and contributor templates. Everything here exists to keep the repo's content honest at scale (160+ cert dirs, 1000+ markdown files).

## At a glance

```
.github/
├── README.md                 # this file
├── PULL_REQUEST_TEMPLATE.md  # auto-applied to new PRs
├── ISSUE_TEMPLATE/
│   ├── bug_report.md
│   ├── cert_request.md
│   └── content_suggestion.md
├── workflows/                # GitHub Actions CI gates
│   ├── cspell.yml
│   ├── link-check.yml
│   ├── markdown-lint.yml
│   └── structure-validate.yml
└── scripts/                  # local-runnable validators + helpers
    ├── build-certs-index.py
    ├── build-flashcards.py
    ├── build-freshness-ledger.sh
    ├── build-lab-map.py
    ├── build-provider-indexes.py
    ├── check-cert-freshness.py
    ├── check-internal-links.py
    ├── check-orphan-links.sh
    ├── glossary-add-anchors.py
    ├── glossary-autolink.py
    ├── glossary-upgrade-existing-links.py
    ├── validate-cert-structure.sh
    └── validate-frontmatter.sh
```

The root `CODEOWNERS` and `.editorconfig` files complement this directory.

## Workflows

GitHub Actions run on PR, push to main, and a weekly schedule. All four are designed to be informative rather than punitive - the structure validator and link-check are the only ones that gate merging.

| Workflow | Triggers | What it does | Strict? |
|---|---|---|---|
| `link-check.yml` | PR, push, weekly Mondays | Two jobs. **Internal** runs `check-internal-links.py` and blocks the merge. **External** runs lychee and opens an auto-issue on weekly failure. | Internal: yes. External: no (vendor URL rot is not a contributor's fault) |
| `markdown-lint.yml` | PR, push | Runs `markdownlint-cli2` against `.markdownlint.json` config | Yes |
| `structure-validate.yml` | PR, push | Runs `validate-cert-structure.sh`, `validate-frontmatter.sh`, and `--check` on both index generators | Yes (fails on missing required files, malformed frontmatter, or stale generated files; warns are advisory) |
| `cspell.yml` | PR, push to `**/*.md` | Spell-checks against `.cspell.json` | No (currently non-strict; will flip once dictionary is tuned) |

## Scripts

All scripts are runnable locally. They print human-readable output and exit non-zero on failure. None of them mutate files except where noted.

### Validators (also run in CI)

**`validate-cert-structure.sh`**
Walks `exams/<provider>/<cert>/` directories, discovered by the presence of `fact-sheet.md`. Discovery deliberately does not key off a `notes/` subdir: that skipped every cert whose notes were still undrafted, which are the ones most likely to be incomplete. Hard-fails on missing `README.md`. Warns on missing `fact-sheet.md`, `practice-plan.md`, and (for senior-tier certs only) `scenarios.md` + `strategy.md`. Tier classification: senior = path contains `/professional/`, `/specialty/`, `/expert/`, OR matches a curated cert-basename list. Junior tiers don't get scenarios + strategy warnings.

```bash
bash .github/scripts/validate-cert-structure.sh
```

**`validate-frontmatter.sh`**
Validates YAML frontmatter on a defined set of file groups: concept pages, day-one pages, top-level learn pages, hands-on projects, cert fact-sheets, topic indexes, architecture patterns, networking deep dives, and decision-matrix / postmortem / playlist files. Fails on malformed YAML or bad date format. Warns on missing `last-updated` or stale (>180 days) entries.

```bash
bash .github/scripts/validate-frontmatter.sh
```

**`build-freshness-ledger.sh`**
Regenerates `docs/freshness.md` from `last-updated` frontmatter across the same file groups. Sections: cert fact-sheets, concept pages, hands-on projects, topic indexes. Run after meaningful content updates.

```bash
bash .github/scripts/build-freshness-ledger.sh > docs/freshness.md
```

**`check-orphan-links.sh`**
Lists `.md` files with zero inbound links from other markdown. Useful before retiring or moving a file. Manual one-shot, not a workflow gate. Recognizes that cert `notes/*.md` are covered by their parent cert dir's links.

```bash
bash .github/scripts/check-orphan-links.sh
```

### Index generators (also run in CI)

**`build-certs-index.py`**
Parses every `exams/**/fact-sheet.md` into `docs/certs.json`: exam code, level, status, duration, cost, passing score, notes count, and which standard files exist. This file is the source of truth for anything that counts or lists certs. Fields that cannot be parsed are `null` rather than guessed, because a wrong value would propagate into every generated table.

```bash
python3 .github/scripts/build-certs-index.py            # write docs/certs.json
python3 .github/scripts/build-certs-index.py --report   # per-field fill rates
python3 .github/scripts/build-certs-index.py --check    # CI mode: fail if stale
```

Status is derived: `retired` and `anticipated` from the README banner, `outline` when no notes are drafted, otherwise `active`.

**`build-provider-indexes.py`**
Generates the per-provider index tables in `exams/<provider>/README.md` and the provider table in `STUDY-HUB.md` from `docs/certs.json`. Only the block between the `<!-- BEGIN GENERATED: ... -->` markers is replaced, so the hand-written editorial content in the six curated provider READMEs survives regeneration. The one-line "Highlights" blurb per provider stays curated in `PROVIDER_HIGHLIGHTS` inside the script.

```bash
python3 .github/scripts/build-provider-indexes.py
python3 .github/scripts/build-provider-indexes.py --check
```

**`check-internal-links.py`**
Verifies every relative markdown link resolves on disk. Skips fenced code blocks, inline code spans, external schemes, and `<placeholder>` targets. Blocking in CI.

```bash
python3 .github/scripts/check-internal-links.py
```

**`build-lab-map.py`**
Reads the `certs:` frontmatter list from each `resources/hands-on-projects/*.md` and generates two views: a lab-to-cert table in the projects README, and the reverse index at `resources/hands-on-projects/labs-by-cert.md`. Cert IDs are validated against `docs/certs.json`, so a typo fails the run instead of producing a dead link. Blocking in CI.

**`build-flashcards.py`**
Writes `flashcards.csv` (Anki-importable) into each cert dir. Cards are extracted, never invented: exam logistics come from `docs/certs.json`, and term-definition cards come from the `- **Term** - definition` lines the notes already use. Certs yielding fewer than 15 cards get no deck and are listed in the report. Decks are capped at 300 cards with an explicit in-deck note when truncated. Blocking in CI.

```bash
python3 .github/scripts/build-flashcards.py --report   # counts, no writes
```

**`check-cert-freshness.py`**
Advisory. Reports which cert guides are due for re-verification, using a per-provider monthly rotation so the whole repo does not fall due on one day. Also warns when a fact-sheet declares `exam-version:` / `exam-retires:` frontmatter and the retirement date is near.

```bash
python3 .github/scripts/check-cert-freshness.py --due     # just this month's batch
python3 .github/scripts/check-cert-freshness.py --month 3 # preview another month
```

### Glossary autolink (mutates files)

These three scripts work as a pipeline. Run them in order when the glossary gains new terms or when adding a new content directory to the autolink scope.

**`glossary-add-anchors.py`** - prepends `<a id="term-slug"></a>` to each bolded term in `learn/glossary.md` so links can target individual terms (not just section headers). Idempotent; safe to re-run.

**`glossary-autolink.py`** - parses the glossary for bolded terms (335 found) and links the first occurrence in scoped pages. Caps at 5 links per file. Skips code blocks, headings, existing links. Scope (`TARGET_DIRS` + `TARGET_FILES`):
- `learn/concepts/`
- `topics/`
- `resources/hands-on-projects/`
- `resources/architecture-patterns/`
- `resources/networking-deep-dives/`
- `resources/decision-matrix-*.md`
- `resources/postmortem-*.md`
- `resources/playlist-*.md`

**`glossary-upgrade-existing-links.py`** - upgrades old section-level glossary links (`glossary.md#cloud-fundamentals`) to per-term anchors (`glossary.md#term-availability-zone`) when a term anchor is available. Run after `glossary-add-anchors.py` adds new anchors.

```bash
python3 .github/scripts/glossary-add-anchors.py
python3 .github/scripts/glossary-autolink.py
python3 .github/scripts/glossary-upgrade-existing-links.py
```

## Templates

- `PULL_REQUEST_TEMPLATE.md` - auto-applied to new PRs. Matches the "in scope / out of scope" framing from `CONTRIBUTING.md`. Contributors edit it down to a checklist of what they actually verified.
- `ISSUE_TEMPLATE/bug_report.md` - for broken links, factual errors, doc drift.
- `ISSUE_TEMPLATE/content_suggestion.md` - for proposing new pages, expanded coverage, missing cross-links.
- `ISSUE_TEMPLATE/cert_request.md` - for proposing a new cert scaffold (open before doing the work, to confirm scope).

## Conventions

- **Scripts are bash or python3**. No external runtime deps (no Node, no npm). The CI workflows install whatever the underlying linter needs (lychee binary, cspell via npx, etc.).
- **Validators print path + reason on failure** so you can grep the output and fix in order.
- **Mutating scripts are idempotent**. Re-running them is always safe.
- **Output is plain text**, not JSON. These scripts are meant to be read by humans.

## When to update what

| Trigger | What to update |
|---|---|
| New cert added | Add `fact-sheet.md`, then run `build-certs-index.py`, `build-provider-indexes.py`, and `build-flashcards.py` so counts, tables, and decks regenerate. If it's a new senior tier, add it to the curated senior-cert list in `validate-cert-structure.sh` |
| New hands-on project | Add a `certs:` list to its frontmatter, then run `build-lab-map.py` |
| Cert notes edited | Re-run `build-flashcards.py`; the deck is derived from the notes |
| New provider added | Add a display name to `PROVIDER_NAMES` and a highlights line to `PROVIDER_HIGHLIGHTS`, then regenerate. CI fails until both generators are re-run |
| Cert renamed, retired, or its fact-sheet edited | Re-run both generators. `structure-validate.yml` fails with the exact command if you forget |
| New concept / hands-on / topic page | Add `last-updated` frontmatter; rerun `build-freshness-ledger.sh` |
| New content shape (matrix / postmortem / playlist / etc.) | Add the file path glob to `validate-frontmatter.sh` and `glossary-autolink.py` |
| New glossary term | Run `glossary-add-anchors.py` then `glossary-autolink.py` |
| New common false positive in cspell | Add to `.cspell.json` words list |
