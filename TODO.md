# TODO

Working task list for **cloud-data-ai-security-zero-to-hero**. Read this at the start of a work session and keep it current as work completes - check items off with a date, add follow-ups as they surface. Stale TODOs are worse than none. Security debt (if any) is tracked separately in `SECURITY-DEBT.md`.

---

## Open

### 🟠 Discoverability (added 2026-08-31)

- [ ] **Upload the social preview image.** GitHub serves an auto-generated card for this repo, so
      every share on X/LinkedIn/Slack renders as a generic placeholder. A 1280x640 card is rendered
      at `/tmp/claude-1000/-home-plw-coding/4ffb6de8-198a-4962-8a8b-1f54e9ab4159/scratchpad/social/cloud-data-ai-security-zero-to-hero-social-1280x640-31AUG2026.png`.
      Upload via **Settings → General → Social preview** (the GitHub API does not expose this).
- [ ] **Commit and push the new `LICENSE` (CC BY 4.0) and `LICENSE-CODE` (MIT).** Until they
      land, GitHub shows this repo as unlicensed - all rights reserved - which is the opposite
      of the "free to use for educational purposes with attribution" the README already states.
      Content is CC BY; the ~9,500 embedded code samples and `scripts/` are MIT so a reader can
      copy a snippet without an attribution obligation.

Backlog derived from the repo-wide gap analysis in
[docs/improvement-roadmap.md](./docs/improvement-roadmap.md) (2026-07-28). See that
document for evidence, counts, and reasoning behind each item.

Add items as `- [ ] task`, grouped by priority or theme. Mark done inline:
`- [x] ~~task~~ ✅ done YYYY-MM-DD`.

### Priority 1 - correctness

- [x] ~~Fix `build-freshness-ledger.sh` path bug, then regenerate `docs/freshness.md`~~ ✅ done 2026-07-29 (cleared 191 broken links)
- [x] ~~Rewrite 87 absolute `/exams/...` links as relative~~ ✅ done 2026-07-29
- [x] ~~Repoint or remove 28 links to the old directory layout~~ ✅ done 2026-07-29
- [x] ~~Update `STUDY-HUB.md` provider table~~ ✅ done 2026-07-29 (added ISACA, Offensive Security, Palo Alto, ServiceNow, VMware; corrected AWS 18, CompTIA 4, Cisco 2, Salesforce 3)
- [x] ~~Update cert/provider badge counts~~ ✅ done 2026-07-29 (133 certs / 26 providers, not 127/27 - see note below)
- [x] ~~Split `link-check.yml` into a blocking internal-link job and an advisory external-URL job~~ ✅ done 2026-07-29
- [x] ~~Fix cert discovery in `validate-cert-structure.sh` and `build-freshness-ledger.sh`~~ ✅ done 2026-07-29

> **Count correction.** The gap analysis first reported 127 certs because both scripts
> discovered cert dirs by looking for a `notes/` subdir, which skipped the 10 certs whose
> notes were never drafted. Counting by `fact-sheet.md` gives 137 cert dirs: 133
> certifications across 26 providers, plus 4 Anthropic study tracks. Both scripts now use
> `fact-sheet.md`, so the validator checks all 137 instead of 127.

### Priority 2 - content substance

- [x] ~~Write notes for the 10 outline-stage certs~~ ✅ done 2026-07-29. All now active with drafted notes, links restored, banners removed. No cert is at outline stage.
  - [x] ~~comptia/cysa-plus~~ (4 notes)
  - [x] ~~comptia/network-plus~~ (5 notes)
  - [x] ~~cisco/ccnp-enterprise-encor-350-401~~ (6 notes)
  - [x] ~~isaca/cisa~~ (5 notes)
  - [x] ~~isaca/cism~~ (4 notes)
  - [x] ~~offensive-security/oscp-pen-200~~ (6 notes)
  - [x] ~~palo-alto-networks/pcnsa~~ (4 notes + scenarios + strategy)
  - [x] ~~salesforce/platform-developer-2~~ (6 notes + strategy)
  - [x] ~~servicenow/csa~~ (6 notes + scenarios + strategy)
  - [x] ~~vmware/vcp-dcv-2v0-21-23~~ (6 notes)
- [x] ~~Resolve the diagram standard~~ ✅ done 2026-07-29 - Mermaid is now the documented default, PNG the exception. Updated `CLAUDE.md`, `docs/ARCHITECTURE.md`, `CONTRIBUTING.md`, `assets/diagrams/README.md`.
- [x] ~~Add index READMEs to the 21 provider directories that lack one~~ ✅ done 2026-07-29 (all 27 now generated from `docs/certs.json`; the 6 hand-written ones kept their editorial content)
- [x] ~~Complete `aws/professional/genai-developer-aip-c01`~~ ✅ done 2026-07-29 - practice-plan, scenarios, strategy written. Structure validator is at zero warnings.
- [x] ~~Move `exams/aws/genai` under `foundational/`; reconcile `azure/genai` and `gcp/genai` placement~~ ✅ done 2026-07-29 (AI Practitioner moved to `exams/aws/foundational/ai-practitioner-aif-c01/`; the Azure and GCP dirs are study tracks, kept in place and now counted as `track` rather than certification)
- [x] ~~Replace the 2 remaining `last-updated: YYYY-MM-DD` placeholders~~ ✅ 2026-07-29 - not applicable. Both live inside ```yaml fenced blocks in `CLAUDE.md` and `CONTRIBUTING.md` that document the frontmatter convention. The original scan did not skip code fences. No stale frontmatter exists.

### Priority 3 - leverage

- [x] ~~Build `docs/certs.json` from fact-sheets; generate the hub table and provider indexes from it~~ ✅ done 2026-07-29 (CI fails if either is stale). Freshness ledger still generates independently - fold it in if it drifts.
- [ ] Add practice questions for uncovered certs. 47 of 150 covered; 103 have none. Use [the template](./resources/practice-questions/template.md). Highest value first: the certs that already have complete notes but no question bank. Next batch by volume: NVIDIA (10 certs, 0 banks), GitHub (5), IBM (5), Anthropic (4), CompTIA (4), MongoDB (3), Salesforce (3).
- [x] ~~Add Tier 1 certifications~~ ✅ done 2026-08-09. All 13 added: SC-100, SC-300, **SC-401** (SC-400 is retired and was replaced by SC-401 - the roadmap entry was out of date), PL-300, the five CNCF associates (OTCA/CGOA/CAPA/CCA/CNPA), ISC2 CC, Oracle OCI AI Foundations + OCI GenAI Professional, Google Generative AI Leader. 137 → 150 cert directories, each with README, fact-sheet, practice-plan, scenarios, strategy, domain notes, a practice question bank, and a generated flashcard deck.
- [x] ~~Stagger `last-updated` re-verification by provider batch~~ ✅ done 2026-07-29 - `check-cert-freshness.py` assigns each provider a review month and reports what is due. The rotation exists; the re-verification work itself is ongoing (12 certs due in month 7).

### Priority 4 - differentiation

- [x] ~~Per-cert `flashcards.csv` (Anki-importable)~~ ✅ done 2026-07-29 - 80 decks, 6,487 cards. 57 certs fall below the 15-card threshold and get no deck; raising that means writing more `- **Term** - definition` lines in their notes.
- [x] ~~Map labs to the certs they support~~ ✅ done 2026-07-29 - 15 labs mapped to 46 certs, generated both directions. 91 certs still have no lab.
- [x] ~~Add `status:` and `exam-version:` frontmatter plus a revision-warning script~~ ✅ done 2026-07-29 - `status` is derived in `certs.json` rather than hand-declared (no drift). `exam-version:`/`exam-retires:` are optional frontmatter, seeded on the 4 retired AWS certs; `check-cert-freshness.py` warns ahead of a known retirement.
- [x] ~~Wire `check-orphan-links.sh` into CI~~ ✅ done 2026-07-29 - runs advisory (never blocking, since orphan detection is heuristic). Orphans are currently 0.
- [x] ~~Prune `.claude/settings.json`~~ ✅ done 2026-07-29
- [x] ~~Publish the repo as a searchable site~~ ✅ done 2026-08-14 - MkDocs Material on GitHub Pages, generated from the markdown tree by `build-site.py`. See below.

---

## Completed 2026-08-14 - published as a searchable website

The repo's 3.0M words had no search: navigation was GitHub's file listing. Every
page is now also published at
[patrickwiloak.github.io/cloud-data-ai-security-zero-to-hero](https://patrickwiloak.github.io/cloud-data-ai-security-zero-to-hero/).

The markdown tree is unchanged and stays the source of truth. `build-site.py`
adapts the tree to MkDocs at build time rather than restructuring the tree for
MkDocs, so there is no second copy of any page.

- [x] `.github/scripts/build-site.py` - staging, generated directory landing
      pages, fence-aware link rewriting, and all 2,032 nav entries generated from
      the tree plus `docs/certs.json`
- [x] `mkdocs.yml` (hand-maintained, no `nav`), `requirements-docs.txt` (fully
      pinned), `.github/site/extra.css`
- [x] `.github/workflows/docs-site.yml` - `--strict` build blocks every PR;
      deploys to Pages on push to main
- [x] Docs updated: README, CONTRIBUTING (local preview), `docs/ARCHITECTURE.md`
      (design + conventions), `.github/AUTOMATION.md`, CHANGELOG

### Defects the strict build surfaced and fixed

All three were broken on GitHub too, and none was catchable by the existing
link checker:

- [x] An unclosed code fence in `exams/gcp/cloud-architect/notes/compute-containers.md`
      swallowed ~130 lines including four headings. A stray duplicate fence in the
      same file compounded it. A repo-wide scan found no other instance.
- [x] 14 broken heading anchors: `resources/community-resources.md` (11 - its
      whole table of contents), `README.md`, `docs/improvement-roadmap.md`, and one
      AWS note. Most omitted the leading hyphen an emoji heading produces.
- [x] Links into `.templates/` had no working site target; it is staged as
      `provider-resources/` and the ~144 inbound links are rewritten.

### Follow-ups closed 2026-08-14 (same day)

- [x] ~~**Pages must be enabled once**: Settings > Pages > Source > **GitHub
      Actions**~~ ✅ enabled via `gh api -X POST .../pages -f build_type=workflow`;
      the previously failing deploy job was re-run and the site is live. Verified
      200 on the homepage, Study Hub, a deep cert page, a generated directory
      index, and the staged `provider-resources/`.
- [x] ~~Theme was Material's default indigo~~ ✅ switched to monochrome (Nobler
      Works house style). `mkdocs.yml` sets `primary: custom` / `accent: custom`
      on **all three** palette entries - the auto entry renders before the palette
      JS runs, so leaving it unset kept showing indigo - and the black/white
      values live in `.github/site/extra.css`. Links carry underlines instead of
      colour, and slate's blue-grey dark surfaces are overridden to neutral black.
      Dark mode is true `#000000` as of the same day: the banners are flattened
      PNGs on pure black, so a near-black page drew a rectangle around each one.
- [x] ~~The themed site still read like a styled README~~ ✅ same day, restyled
      to the gitGood design language, extracted from gitgood.dev's source: green
      accent (`#22c55e`) on links/CTAs/hover borders/glow shadows, Geist + Geist
      Mono, centred staggered hero with accent kickers, card hover = accent
      border + tinted shadow + 2px lift. Also fixed two dark-mode defects the
      monochrome pass shipped (black-on-black hero buttons, washed-out h1),
      hid the header's star/fork repo widget, and stripped leading heading
      emoji on the site only (`strip_heading_emoji()` in build-site.py pins
      each original anchor slug, so no inbound anchor link moved; the repo
      markdown and the sidebar's landmark labels are untouched). See
      CHANGELOG 2026-08-14.
- [x] ~~Both sidebars were rendered, and the populated one appeared to switch
      sides between pages~~ ✅ `navigation.tabs` off, so the left sidebar is the
      same full tree everywhere, and `toc.integrate` folds the page contents into
      it so there is no right column. `toc.integrate` alone drops the ToC on
      every section-index page - Material only emits it for leaf pages - so
      `.github/site-overrides/partials/nav-item.html` overrides that partial.
      **This couples the repo to Material's template internals**: after a version
      bump, re-copy the partial, re-apply the marked block, and check a cert
      landing page by eye. A `--strict` build will not catch a drifted template.
- [x] ~~No promotion of gitGood.dev, the flagship product~~ ✅ promo block in the
      README header and on the landing page, with `assets/brand/gitgood-banner.png`
      cropped from gitGood's loading splash (it ships no marketing banner, and the
      splash carries a progress bar and an "84%" label). Copy names 21
      role-targeted paths and the cert banks by exam code, for search; the long
      lists sit in a collapsed `<details>` so they cost no visible height.
- [x] ~~README counts drifted unnoticed~~ ✅ `check-readme-counts.py` added and
      wired into `structure-validate.yml` as a blocking check. It caught "37
      concept pages" (actually 46), "8 topic indexes" (actually 13), and the
      `2.6M words` figure copied out of the dated `improvement-roadmap.md`
      snapshot (the tree is at 3.0M). Run `--fix` when you add content.
      Then it caught a bug in itself: the first version walked the filesystem
      and counted the `.site-src/` staged copy a local site build leaves behind,
      reporting 6.1M words against a real 3.0M. It now counts via `git ls-files`,
      so no build artifact can inflate a total.
- [x] ~~The site's home page was the repo README~~ ✅ `.github/site/home.md` is
      now rendered over the staged `README.md` by `build-site.py`: hero with
      three entry points, counts strip, four pillars as cards, a two-column jump
      list, 27 provider chips, and the three most recent release notes. GitHub
      keeps its repo front page; the site gets a landing page. No number is typed
      into it - every figure is a token filled from `certs.json` and
      `check-readme-counts.py`, and the release notes are extracted from the
      README, so neither page can drift from the other.
- [x] ~~The README's per-provider table was stale in 8 of 22 rows and missing 5
      providers~~ ✅ Kubernetes/CNCF read 7 against 12, Azure 23 against 26,
      CompTIA 2 against 4, Oracle 5 against 7; ISACA, Offensive Security, Palo
      Alto Networks, ServiceNow and VMware had no row at all, five days after the
      Tier 1 batch added them. The table is now **generated** by
      `build-provider-indexes.py` between markers, like the `STUDY-HUB.md` one,
      so counts and the row set come from `certs.json`.
- [x] ~~The table's "Highlights" column was hand-written and unchecked~~ ✅ It is
      one curated string per provider in `PROVIDER_HIGHLIGHTS`, shared by both
      tables, and the generator refuses to run if a provider has no highlight or
      no `PROVIDER_EMOJI` icon - so a new provider fails CI instead of rendering
      a blank row. Four lines were describing half a provider and were feeding
      STUDY-HUB while they did: Kubernetes/CNCF listed 7 of 12, ISC2 omitted CC,
      Oracle omitted both OCI AI certs, AWS omitted GenAI Developer. All fixed,
      and both tables now say plainly that Highlights is a sample and the Certs
      column is the total.
- [x] ~~Two scripts could rewrite the README's provider rows~~ ✅ The stopgap
      provider-table check in `check-readme-counts.py` was removed once the table
      became generated. Its `--fix` would have corrected a count *inside* a
      generated block, leaving the generator reporting the file stale. One table,
      one owner.
- [x] ~~The "Repository Statistics" block was outside CLAIMS~~ ✅ It still read
      37 concept pages against 46, 8 topic indexes against 13, and 5 compliance
      guides against 8 - the same drift the checker was written to stop, in the
      one section that is nothing but counts. 17 numbers added to `CLAIMS`,
      including the three restated in the repository-structure block.

### Known follow-ups

- The search index is 28 MB uncompressed. It is lazy-loaded and served gzipped,
  but if first-search latency becomes a complaint, the options are splitting the
  index per section or excluding the deepest cert notes from it.
- `check-internal-links.py` and the site build now overlap but are not
  redundant: the former checks the source tree offline, the latter checks
  rendered URLs and heading anchors. Worth folding anchor validation into the
  standalone checker so the failure is reported without a full site build.
- No CI check for unbalanced code fences. The site build catches them only
  indirectly, as missing anchors on the affected page. A direct validator would
  name the file and line.
- `PROVIDER_HIGHLIGHTS` is the last hand-written thing in either provider table.
  Nothing can check that a sample is a *good* sample, only that it exists - so a
  provider that gains a cert can still keep a blurb that does not mention it. The
  blast radius is now one string feeding both tables rather than two that drift
  apart, and both tables state that Highlights is a sample. Worth a look whenever
  a provider's count changes.

---

## Completed 2026-08-09 - content gap expansion

A repo-wide gap analysis found four holes. All four are now closed. Counts below
are measured, not estimated.

### AI security and governance (new)

The repo is named `cloud-data-ai-security-zero-to-hero` and had no dedicated AI
security material: "OWASP LLM Top 10" appeared in exactly one file, "model supply
chain" in zero, and `resources/compliance-guides/` covered FedRAMP, GDPR, HIPAA,
PCI-DSS and SOC 2 with nothing AI-specific.

- [x] `resources/ai-security/` - OWASP LLM Top 10, prompt injection defense, agent
      and tool security, model supply chain, LLM red teaming, plus an index
- [x] `resources/compliance-guides/` - EU AI Act, NIST AI RMF, ISO/IEC 42001
- [x] `learn/concepts/` - prompt injection explained, AI threat modeling
- [x] `topics/ai-security.md` cross-pillar hub

### Tier 1 certifications (13 added)

- [x] Microsoft: SC-100, SC-300, SC-401, PL-300
- [x] CNCF: OTCA, CGOA, CAPA, CCA, CNPA
- [x] ISC2 CC - the free, no-prerequisite entry point the "zero to hero" framing
      implied but the repo did not have (the security path started at Security+)
- [x] Oracle: OCI AI Foundations, OCI Generative AI Professional - Oracle had five
      certs here and zero AI ones
- [x] Google: Generative AI Leader
- [x] OTCA also closes the "no observability certification anywhere in exams/" gap,
      and CCA is the only cert in the repo teaching eBPF

### Learn pillar

Was 54k words against 2.17M in `exams/`.

- [x] 8 new concept pages: caching, SQL vs NoSQL, load balancing, secrets
      management, autoscaling, deployment strategies, cloud cost basics, GPUs for AI
- [x] 3 new day-one pages: file permissions, JSON and YAML, reading error messages
- [x] `topics/platform-engineering.md` hub
- [x] Concepts index gained a Data and Databases section; 34 → 46 concept pages

### Practice questions

- [x] 13 new banks, one per new cert. Coverage 34/137 → 47/150

### Housekeeping

- [x] All generated indexes rebuilt: `docs/certs.json`, 27 provider indexes,
      STUDY-HUB table, flashcards (90 → 103 decks, 9,545 cards), lab map, freshness
- [x] Hand-maintained counts corrected in README, STUDY-HUB, CLAUDE.md, learn/README
- [x] `.cspell.json` extended with 100+ legitimate technical terms
- [x] Validators at zero: structure 0 failures / 0 warnings, 4,053 internal links
      0 broken, frontmatter 0 failures, orphans 0

### Known follow-ups

- Practice question banks for the 103 certs that still have none
- 47 certs remain below the 15-card flashcard threshold; raising them means writing
  more `- **Term** - definition` lines in their notes
- `markdownlint` MD060 (table-column-style) fires across the whole repo, including
  files untouched by this work. It is a newer rule than the pinned CI action, so it
  is version drift rather than a content defect. Decide whether to disable it in
  `.markdownlint.json` or reformat every table

---

## Completed 2026-08-11 - Anthropic certification program refresh

Anthropic launched an official certification program in 2026 (Architect Foundations
in March; Associate, Developer, and Architect Professional in July). The four repo
"study tracks" predated it. This pass aligned the repo with the real program.

- [x] Renamed `claude-certified-architect-advanced` → `claude-certified-architect-professional`
      and `claude-application-developer` → `claude-certified-developer-foundations`
      (git mv, practice banks renamed too, all inbound links repointed)
- [x] Retargeted all three existing technical tracks to the official exams with
      verified blueprints: CCAR-F ($125, 60q), CCAR-P ($175, 63q, 7 domains),
      CCDV-F ($125, 53q, 8 domains) - real domain weights, Pearson VUE delivery,
      Partner Academy registration, 12-month validity, retake policy
- [x] New cert dir `claude-certified-associate-foundations` (CCAO-F, $99, 60q,
      7 domains): full skeleton + 7 notes + 15-question bank, 2,335 lines
- [x] 5 new notes filling blueprint gaps: governance/safety/risk and stakeholder
      lifecycle (CCAR-P); model selection, agents/workflows, security+Claude
      Code+evals (CCDV-F)
- [x] Prompt Engineering Specialist stays a study track (no official prompt exam);
      banner updated to say so
- [x] Provider promoted from "Anthropic Claude (study tracks)" to a certification
      provider in both generator scripts; STUDY-HUB table now lists it with the
      cloud/AI providers
- [x] All indexes regenerated: certs.json (148 certs / 27 providers / 3 tracks),
      27 provider indexes, STUDY-HUB table, lab map, freshness ledger, flashcards
      (105 decks, 9,660 cards)
- [x] Hand-maintained counts corrected in README, STUDY-HUB, CLAUDE.md,
      docs/ARCHITECTURE.md
- [x] Validators at zero: structure 0/0, 4,832 internal links 0 broken

### Known follow-ups

- Exam facts came from the official Pearson VUE page plus secondary 2026 guides;
  domain weights for CCAO-F and CCAR-P could not be confirmed against the official
  exam guides (Partner Academy login required). Verify when Partner Network access
  is available and stamp `docs/freshness.md`.
- `docs/improvement-roadmap.md` (2026-07-28 snapshot) still describes 4 Anthropic
  study tracks; left as a dated historical analysis.
