# Cloud + AI Learning Resource - Project Instructions

## Overview
A learning resource for cloud and AI - concepts, hands-on builds, deep references, and certification prep. Covers 148 certifications across 27 providers (AWS, Azure, GCP, Kubernetes/CNCF, NVIDIA, Anthropic, HashiCorp, Databricks, Snowflake, GitHub, Red Hat, Cisco, Salesforce, Confluent/Kafka, MongoDB, FinOps, CompTIA, ISC2, ISACA, Cloud Security Alliance, Offensive Security, Palo Alto Networks, Linux Foundation, Oracle, IBM, ServiceNow, VMware) plus 3 self-directed study tracks (Anthropic prompt engineering, plus Azure and GCP GenAI). Counts are generated from `docs/certs.json`, not maintained by hand. Certifications are one pillar; the repo also serves non-cert learners.

## Structure
```
cloud-data-ai-security-zero-to-hero/
├── exams/              # Cert-specific study guides (the certify pillar)
├── learn/              # Plain-English learning content (the learn pillar)
│   ├── concepts/       # Bite-size topic pages (5-10 min): cloud + AI primitives
│   ├── day-one/        # Strict beginner on-ramp: terminal, git, HTTP, servers
│   ├── ai-from-scratch.md
│   ├── cloud-from-scratch.md
│   ├── glossary.md
│   └── youtube.md
├── resources/          # Cross-cert reference (build + reference pillars)
├── topics/             # Cross-pillar topic indexes (LLMs, IAM, networking, K8s, ...)
├── assets/diagrams/    # PNG diagrams (draw.io exports), organized by topic
├── docs/               # Repo-level docs (ARCHITECTURE.md, certs.json, freshness.md, tag-taxonomy.md, improvement-roadmap.md)
├── .github/site/       # Site-only stylesheet (staged to assets/site/ at build)
├── mkdocs.yml          # Site config; nav is generated, not written here
├── README.md           # Top-level overview
├── STUDY-HUB.md        # Navigation hub
└── CONTRIBUTING.md     # How to contribute
```

## Purpose / Usage
- Personal study notes and exam prep materials (cert pillar)
- Plain-English learning content for non-cert students (learn pillar)
- Reference documentation for architecture, comparison, troubleshooting (build + reference pillars)
- Markdown-based knowledge base; `STUDY-HUB.md` is the navigation hub.
- **Also published as a website**: <https://patrickwiloak.github.io/cloud-data-ai-security-zero-to-hero/>, built by `.github/workflows/docs-site.yml` on push to `main` (live since 2026-08-14). The site is generated from the markdown as-is - **never restructure content or add frontmatter to satisfy the site build.** Site-only fixes go in `.github/scripts/build-site.py`, which transforms a staged copy in `.site-src/` and never touches the repo's markdown. Theme colour lives in `.github/site/extra.css` (monochrome, Nobler Works house style; `mkdocs.yml` sets `primary: custom` so Material's palettes are bypassed).
- Organized by purpose (learn / certify / reference) and within each, by provider.
- Each cert dir has: `README.md`, `fact-sheet.md`, `notes/`, `practice-plan.md`, `scenarios.md`, `strategy.md`.
- Resources include: architecture patterns, service comparisons, CLI cheat sheets, roadmaps, compliance guides, migration guides, interview prep, troubleshooting guides, hands-on projects.

## House style / conventions

### House style
- No em dashes (-). Use regular dashes (-) only.
- Plain English, short sentences. Avoid emoji in body text (section markers OK).
- Cite vendor docs, don't paraphrase. Use the `**[📖 Title](URL)** - description` link format.
- No verbatim vendor exam questions.

### Visual content standards
- **Mermaid fenced code blocks are the default.** Write the diagram inline in the page that uses it. GitHub renders Mermaid natively, it stays editable in the markdown, and it diffs as text in review.
- Prefer `flowchart TB` / `flowchart LR` over the older `graph` syntax. Use `subgraph` for grouped components. Don't hard-code colours; the diagram has to read in both light and dark themes.
- Mermaid has no alt text, so give each diagram a caption or a sentence of prose saying what it shows.
- **PNG is the exception**, for diagrams too dense to read inline. Save to `assets/diagrams/<topic>/<slug>.png` (topic subdirs created lazily) and embed with descriptive alt text: `![3-tier architecture with load balancer, app servers, and database](../../assets/diagrams/architecture/web-app-3-tier.png)`
- See [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md#visual-content-standards) for the full convention.

### Frontmatter convention (new and refreshed pages)
```yaml
---
last-updated: YYYY-MM-DD
applies-to: AWS console as of 2026-Q2          # optional
difficulty: beginner | intermediate | advanced  # optional
reading-time: 10 min                            # optional
---
```
Backfill is opportunistic. Don't add frontmatter to thousands of files in one PR.

### Automation
- `.github/workflows/` - link-check (lychee, weekly + on PR), markdown-lint (markdownlint-cli2), structure-validate (custom scripts), docs-site (MkDocs build + Pages deploy; the build runs `--strict` as a blocking PR gate).
- `.github/scripts/validate-cert-structure.sh` - confirm every cert dir has a README; warn on missing fact-sheet, practice-plan, scenarios, strategy.
- `.github/scripts/build-freshness-ledger.sh` - regenerate `docs/freshness.md` from `last-updated` frontmatter. Run after meaningful content updates.
- `.github/scripts/build-site.py` - stage and build the site. `--serve` for live preview, `--strict` to fail on any broken link or anchor.
- See [docs/freshness.md](./docs/freshness.md) for the per-cert verification ledger.

### Counts are checked, not remembered
Every number advertised in `README.md` and `STUDY-HUB.md` is verified by CI. Cert and provider counts come from `docs/certs.json` via `build-certs-index.py --check`; everything else (concept pages, topic indexes, comparisons, cheat sheets, projects, word count, doc-link floor) is verified by `check-readme-counts.py --check`.

**When you add or remove content, run `python3 .github/scripts/check-readme-counts.py --fix` in the same change.** This exists because the README sat at "37 concept pages" while the tree had 46 and TODO.md had already recorded the change, and because a dated `~2.6M words` snapshot from `docs/improvement-roadmap.md` was copied into three files as a current fact when the real figure was 6.1M. If you add a new counted claim to the README, add a matching entry to `CLAIMS` in that script - an unchecked number goes stale.
