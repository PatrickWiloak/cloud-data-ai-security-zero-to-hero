# Changelog

All notable changes to the cloud certification study guides repository.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project uses calendar-based dating.

---

## [2026-08-11] - Anthropic Claude certification program: 4 official certs covered, Anthropic becomes the 27th certification provider

Anthropic launched an official Claude certification program in 2026 (Architect - Foundations in March, then Associate, Developer, and Architect - Professional in July, all via Pearson VUE). This repo previously carried 4 fictional self-directed Anthropic "study tracks"; this pass replaces them with real coverage of the actual program. Repo totals move from 144 certifications / 26 providers / 6 study tracks to **148 certifications / 27 providers / 3 study tracks** (151 cert directories).

### Added

- **`exams/anthropic/claude-certified-associate-foundations/`** - complete new guide for the Claude Certified Associate - Foundations exam (CCAO-F, $99, 60 questions): README, fact-sheet, 7 domain notes, practice-plan, 10 scenarios, strategy, plus a 15-question practice bank at `resources/practice-questions/anthropic-claude-associate-foundations.md`.
- **Blueprint-gap notes** - CCAR-P gains `notes/08-governance-safety-and-risk-management.md` and `notes/09-stakeholder-communication-and-lifecycle-management.md`; CCDV-F gains `notes/08-model-selection-and-optimization.md`, `notes/09-agents-and-workflows.md`, and `notes/10-security-safety-claude-code-and-evals.md`.

### Changed

- **`claude-certified-architect-advanced/` renamed to `claude-certified-architect-professional/`** and retargeted to the real CCAR-P exam ($175, 63 questions, 7 official domains); its practice bank renamed and updated to match.
- **`claude-application-developer/` renamed to `claude-certified-developer-foundations/`** and retargeted to the real CCDV-F exam ($125, 53 questions, 8 official domains); its practice bank renamed and updated to match.
- **`claude-certified-architect-foundations/`** converted from a study track to the real CCAR-F exam guide (launched March 12, 2026; $125, 60 questions, 5 official domains) with corrected code, delivery, validity, and cost.
- **All four guides** now carry official domain blueprints with weights, Pearson VUE delivery, 720/1000 passing score, 12-month validity with free on-time renewal, retake policy, and Anthropic Partner Academy registration steps.
- **Anthropic promoted to a certification provider** in `build-certs-index.py` / `build-provider-indexes.py` (previously a "(study tracks)" pseudo-provider appended after the totals row). The Claude Prompt Engineering Specialist track remains the sole Anthropic study track, since the program has no prompt engineering exam.
- **Counts regenerated everywhere** - `docs/certs.json`, all 27 provider indexes, STUDY-HUB provider table, freshness ledger, lab map, flashcards (now 105 decks / 9,660 cards), README and STUDY-HUB badges and stats.

### Notes

- CCAO-F and CCAR-P domain weights are sourced from Pearson VUE plus secondary exam guides; official exam guide PDFs sit behind the Anthropic Partner Academy login. Flagged in `TODO.md` for verification.

---

## [2026-07-29] - Gap-analysis pass: fixed 383 broken links, generated cert index + navigation, drafted notes for all 10 outline-stage certs, added flashcards / lab map / freshness rotation

A full pass against the repo-wide gap analysis in [docs/improvement-roadmap.md](./docs/improvement-roadmap.md). Twelve commits, all on `main`. Ended with 0 broken internal links (3,133 checked), 0 structure-validator warnings, and 0 orphaned pages.

### Added

- **`docs/improvement-roadmap.md`** - a measured, evidence-backed gap analysis of the whole repo (what is broken, what is missing, what would raise the bar), and a matching four-phase backlog in `TODO.md`.
- **`docs/certs.json`** - a generated, machine-readable index of all 137 cert directories (exam code, level, status, duration, cost, passing score, notes count, standard files present, last-updated). Built by `.github/scripts/build-certs-index.py`; the single source of truth for every count and table. Fields that cannot be parsed are `null`, never guessed.
- **Per-provider index READMEs for all 27 providers**, generated from `docs/certs.json` by `.github/scripts/build-provider-indexes.py`. The 6 hand-written provider READMEs keep their editorial content; only a marked block is regenerated. Closes the 21 provider directories that previously landed on a bare GitHub file listing.
- **Drafted topic notes for the 10 outline-stage certs** - CompTIA CySA+ (4) and Network+ (5), Cisco CCNP ENCOR (6), ISACA CISA (5) and CISM (4), Offensive Security OSCP (6), Palo Alto PCNSA (4 + scenarios + strategy), Salesforce PD2 (6 + strategy), ServiceNow CSA (6 + scenarios + strategy), VMware VCP-DCV (6). ~50 new note files of original cert content, written to each exam's published blueprint. All 10 flipped from `outline` to `active`; no cert remains at outline stage.
- **`aws/professional/genai-developer-aip-c01`** completed with `practice-plan.md`, `scenarios.md`, and `strategy.md` - the last outstanding structure-validator warning.
- **Per-cert `flashcards.csv`** (Anki-importable) in each cert dir, generated by `.github/scripts/build-flashcards.py`: 90 decks, 8,484 cards. Cards are extracted, not invented - exam logistics from `docs/certs.json`, term-definition cards from the `- **Term** - definition` lines the notes already use. Certs below a 15-card threshold get no deck rather than a thin one.
- **Lab-to-cert mapping**, generated by `.github/scripts/build-lab-map.py`: each hands-on project declares the certs it exercises in frontmatter, producing a lab-to-cert table in the projects index and a reverse index at `resources/hands-on-projects/labs-by-cert.md` (46 of 137 certs have a matching lab).
- **`.github/scripts/check-internal-links.py`** - offline, code-fence-aware internal-link checker, now a blocking CI job.
- **`.github/scripts/check-cert-freshness.py`** - assigns each provider a review month so re-verification spreads across the year instead of all falling due on one date, and warns ahead of exam revisions via optional `exam-version:` / `exam-retires:` frontmatter (seeded on the 4 retired AWS certs).

### Changed

- **Diagram standard: Mermaid is now the documented default**, PNG the exception for diagrams too dense to read inline. Updated `CLAUDE.md`, `docs/ARCHITECTURE.md`, `CONTRIBUTING.md`, and `assets/diagrams/README.md`. This matches what the repo actually does (89 pages use Mermaid, no PNG was ever added), so the documented standard no longer has zero instances.
- **Cert counts corrected across the front door.** README and STUDY-HUB advertised "122+ certifications across 22 providers"; actual is **131 certifications + 6 self-directed study tracks across 137 directories, spanning 26 certification providers**. Badges, prose, and the STUDY-HUB provider table (which was missing 5 providers and undercounted 3) all updated and now generated from `docs/certs.json`.
- **The AWS AI Practitioner moved into the tier structure**: `exams/aws/genai` → `exams/aws/foundational/ai-practitioner-aif-c01/`, with all inbound links repointed. The Azure and GCP GenAI directories were reclassified as self-directed study tracks (they are not single exams) and are no longer counted as certifications.
- **Cert discovery fixed in the validator and ledger.** Both previously found certs by looking for a `notes/` subdirectory, silently skipping the 10 certs whose notes were undrafted. Both now key off `fact-sheet.md`, so all 137 are checked (previously 127).
- **`link-check.yml` split into two jobs**: a blocking internal-link check and an advisory external-URL (lychee) check with the existing weekly issue-filing. Previously lychee ran with `fail: false` and nothing enforced internal link integrity, which is how 383 broken links had accumulated.
- **`.claude/settings.json` pruned** - removed absolute paths from a previous machine and replaced the blanket `Bash(*)` allow with the commands this repo actually uses.
- **`.github/AUTOMATION.md`** documents all the new scripts and their CI wiring.

### Fixed

- **383 broken internal links → 0.** 191 in `docs/freshness.md` (a path-prefix bug in `build-freshness-ledger.sh`, since the ledger renders one directory below the repo root), 87 absolute `/exams/...` links in the roadmap resources (a leading slash resolves to the GitHub domain root), 77 links to notes that were never written (delinked and marked `_(planned)_`, then restored as the notes were drafted), and 28 stale paths from an older directory layout.
- **`check-orphan-links.sh` wired into CI as advisory** and the one real orphan (`docs/tag-taxonomy.md`) linked from CONTRIBUTING. Orphans are now 0.

---

## [2026-05-03] - Senior-tier scenarios + strategy, 20 architecture/networking diagrams, 4 new topic indexes, glossary autolink, orphan-checker fix, tier-aware structure validator, repo governance scaffolding, decision matrices + postmortems + persona playlists, Day-One expansion, cspell, practice-question expansion

A large day of structural quality work. Eight themed batches, all on `main`.

### Added

- **Three decision matrices** in `resources/`: `decision-matrix-vector-database.md` (Pinecone / Weaviate / Qdrant / Milvus / pgvector / OpenSearch / Bedrock KB / Vertex Vector Search), `decision-matrix-iac-tool.md` (Terraform / OpenTofu / Pulumi / CloudFormation / Bicep / CDK), `decision-matrix-llm-serving.md` (vLLM / TGI / SGLang / llama.cpp / TensorRT-LLM / hosted). Each scores criteria, names a default pick, and explains when to pick something else.
- **Three postmortem study guides** in `resources/`: `postmortem-aws-s3-2017.md`, `postmortem-cloudflare-regex-2019.md`, `postmortem-gcp-networking-2019.md`. Each maps a real incident to relevant cert exam domains.
- **Four persona playlists** in `resources/`: `playlist-ai-engineer-30min.md`, `playlist-cloud-security-1hour.md`, `playlist-data-engineer-1hour.md`, `playlist-sre-1hour.md`. Reading sequences across existing concept / comparison / reference pages.
- **Four new Day-One beginner pages**: `learn/day-one/ssh-basics.md`, `package-managers.md`, `networking-troubleshooting.md`, `what-is-an-api-call.md`. Day-One went from 5 to 9 pages.
- **Per-topic Mermaid diagrams** added to 6 of 11 topic indexes (databases, iam, kubernetes, networking, observability, security). 10 of 11 topics now have a "topic at a glance" diagram.
- **Per-term glossary anchors** via new `.github/scripts/glossary-add-anchors.py`: 278 `<a id="term-slug"></a>` anchors added to `learn/glossary.md`. New `.github/scripts/glossary-upgrade-existing-links.py` upgraded 38 prior section-level links to per-term anchors. Autolink now prefers per-term anchors when available.
- **cspell workflow** at `.github/workflows/cspell.yml` (non-strict initial run while the dictionary tunes) plus `.cspell.json` with a 150+ word custom dictionary covering cloud + AI proper nouns (Anthropic, vLLM, Pinecone, ExpressRoute, Kerberoasting, etc.).
- **Scenarios + strategy on all 47 senior-tier certs.** Every cert classified senior (AWS Pro / Specialty, Azure Expert / Specialty, GCP Professional, Kubernetes CKS, ISC2 / ISACA, CompTIA mid-senior, Cisco CCNP+, HashiCorp / Databricks / Snowflake "professional" / "advanced", FinOps Professional, VMware VCP, Anthropic Architect Advanced, OSCP, IBM Cloud Security Engineer) now has both `scenarios.md` (6-8 worked exam-style scenarios with options + analysis + takeaway) and `strategy.md` (cert-specific traps, time math, day-of logistics, pattern map). 49 new files, ~50,000 words of original cert-content. Scenarios are illustrative patterns based on each exam's published blueprint - not real exam questions. Files committed in 5 provider-grouped batches (AWS, Azure, GCP, security, other).
- **20 new Mermaid diagrams** across 16 architecture-pattern files (microservices, event-driven, serverless API, multi-region active-active, CQRS / event sourcing, data pipeline ETL, lakehouse, data mesh, ai-ml-pipeline, disaster recovery, hybrid cloud connectivity, zero trust, cell-based, chaos engineering, strangler fig, api gateway) and all 4 networking-deep-dives (DNS hierarchy, hybrid connectivity options, L4 vs L7 load balancing, multi-cloud networking).
- **4 new topic indexes**: `topics/ai-ml-systems.md`, `topics/serverless.md`, `topics/sre-and-reliability.md`, `topics/finops.md`. Each follows the established Learn / Compare / Reference / Build / Certify pattern. `topics/README.md` updated to list all 11 topics.
- **Glossary auto-link script** at `.github/scripts/glossary-autolink.py`. Parses `learn/glossary.md` for bolded terms (335 found) and links the first occurrence in concept + hands-on pages. Caps at 5 links per file; skips code blocks, headings, existing links. Applied: 38 links across 18 files.
- **Repo governance scaffolding**: `.github/PULL_REQUEST_TEMPLATE.md` (matches CONTRIBUTING.md "in scope / out of scope" framing), `.github/ISSUE_TEMPLATE/{bug_report,content_suggestion,cert_request}.md`, root-level `CODEOWNERS`, root-level `.editorconfig`.

### Changed

- **Practice-question banks expanded** for 4 sparse certs from 15 to 25 questions: `kubernetes-cka.md`, `aws-ai-practitioner.md`, `hashicorp-terraform-associate.md`, `isc2-cissp.md`. Same scenario / four-option / analysis / takeaway shape as existing banks.
- **`validate-frontmatter.sh` scope expanded** to also scan `learn/day-one/`, `topics/`, `resources/architecture-patterns/`, `resources/networking-deep-dives/`, decision-matrix / postmortem / playlist files. Backfilled `last-updated` on those file groups.
- **README.md surfaces new content shapes** - decision matrices, postmortem study guides, persona playlists each get a section in the resource navigation; freshness ledger linked from the front door.
- **Tier-aware cert-structure validator.** `validate-cert-structure.sh` now classifies each cert as `senior` or `junior` and only recommends `scenarios.md` + `strategy.md` for senior tiers. Senior = path contains `/professional/`, `/specialty/`, `/expert/`, OR matches a curated cert-basename list (GCP professional certs, Azure expert / specialty, K8s pro, ISC2 / ISACA / OSCP, Cisco CCNP+, HashiCorp / Databricks / Snowflake "professional" / "advanced", FinOps Certified Professional, VMware VCP, Anthropic Architect Advanced, CompTIA mid-senior). Cuts validator warnings from 70 → 0 once senior-cert content was authored.
- **Orphan-link checker root-cause fix.** Two bugs: root-level markdown (README.md, STUDY-HUB.md, CHANGELOG.md, CONTRIBUTING.md, CLAUDE.md) wasn't in the haystack so anything they linked appeared orphan. Cert `notes/*.md` files were considered orphan even when their parent cert directory was referenced. Result: 310 false-positive orphans → 0 true orphans, 289 covered-by-subtree.
- **Glossary autolink + orphan checker** wired up. Test scripts pass cleanly against the current tree.
- **`assets/diagrams/_src/` placeholder cleanup.** Removed `test.drawio` and `test.png` left from initial setup.
- **Three thin certs filled to baseline structure**: `servicenow/csa/practice-plan.md`, `palo-alto-networks/pcnsa/practice-plan.md`, `offensive-security/oscp-pen-200/{fact-sheet,practice-plan,scenarios,strategy}.md`. Real content based on each exam's existing README / blueprint, not boilerplate.

---

## [2026-05-03] - 100% concept-page diagram coverage

### Changed

- **Twelve more Mermaid diagrams** added to the remaining concept pages without one. Every content concept page (36 / 36) now has at least one diagram.
  - Networking / cloud foundations: `cdn-explained` (multi-PoP cache hit/miss with origin), `dns-explained` (sequence diagram of recursive resolution), `regions-and-availability-zones` (single-AZ vs multi-AZ vs multi-region), `iaas-paas-saas` (responsibility layering across all four service models including on-prem), `what-is-cloud-computing` (pre-cloud vs cloud workflow side-by-side).
  - AI / LLM systems: `context-windows-and-management` (stacked context budget with cached vs live tokens), `inference-servers` (continuous batching: clients → queue → batched forward pass → GPU), `multimodal-models` (text + image + audio + video → shared embedding space → LLM), `prompt-engineering` (test-driven iteration loop), `structured-outputs` (prompt + schema → constrained decoder → guaranteed-valid JSON), `evals-for-llms` (dataset + grader + runner → aggregate score → CI).
  - DevOps: `terraform-explained` (code → init/plan/apply with state file as central truth).
- The two ASCII diagrams in `cdn-explained` and `dns-explained` were upgraded to Mermaid for better rendering and accessibility.

---

## [2026-05-03] - Frontmatter scale-out, six more concept diagrams

### Changed

- **Frontmatter backfill on the remaining 123 cert fact-sheets**. Every cert in the freshness ledger now shows a real `last-updated` date instead of "unknown". `validate-frontmatter.sh` goes from 123 warnings to 0.
- **Six new Mermaid diagrams** added to concept pages that previously had no visual: `cicd-explained.md` (pipeline stages with delivery vs deployment branch), `fine-tuning-vs-rag.md` (decision tree: knowledge vs behavior problem), `embeddings-and-vector-search.md` (query → embedding → cosine-similarity ranking), `shared-responsibility-model.md` (IaaS/PaaS/SaaS layered with you-vs-provider color coding), `serverless-explained.md` (sequence diagram of cold start vs warm), `tls-and-https.md` (sequence diagram of TLS handshake including CA chain verification).

---

## [2026-05-03] - Freshness backfill, hands-on index, automation guards

### Added

- **`resources/hands-on-projects/README.md`** - index for all 15 builds with time estimates, "what you'll have at the end" summaries, and a "how to pick" guide. Closes the discoverability gap where projects were only browsable via directory listing.
- **`.github/scripts/validate-frontmatter.sh`** - validates YAML frontmatter on concept pages, top-level learn pages, hands-on projects, and cert fact-sheets. Fails on malformed YAML or bad date format; warns on missing or stale (>180d) `last-updated`. Wired into `structure-validate.yml`.
- **`.github/scripts/check-orphan-links.sh`** - lists `.md` files with no inbound links from other markdown. Manual one-shot, not a workflow gate.
- **Mermaid diagrams** added to `kubernetes-in-10-minutes.md` (control plane + workers + service routing), `iam-explained.md` (authn/authz request flow), `containers-vs-vms.md` (VM vs container layering).

### Changed

- **`last-updated: 2026-05-03` frontmatter backfilled** on the 21 concept pages, 10 hands-on builds, and 12 high-traffic cert fact-sheets (AWS SAA-C03, SAP-C02, CLF-C02, DVA-C02; Azure AZ-104, AZ-900, AZ-305; GCP Cloud Architect, Cloud Engineer; K8s CKA, CKAD, CKS) plus 4 top-level learn pages (ai-from-scratch, cloud-from-scratch, glossary, youtube) that previously had none.
- **`build-freshness-ledger.sh`** now scans concept pages, top-level learn pages, and hands-on projects in addition to cert fact-sheets. Output split into four sections.
- **`docs/freshness.md`** regenerated. Concepts and hands-on sections now show real dates (not "unknown"); cert section still partially "unknown" by design (only top-traffic backfilled this pass).
- **`structure-validate.yml`** workflow renamed to "Structure and frontmatter validate", expanded to trigger on `learn/**` and `resources/hands-on-projects/**`, and now runs the new frontmatter validator.
- **`README.md`** - "I'm here to..." table now points to the new hands-on index (with a "with time estimates" hint) and adds a row for `learn/youtube.md` ("Learn from videos").

---

## [2026-05-03] - Round out the four-pillar repo

Major build-out across all four pillars (Learn / Build / Certify / Reference) to bring the AI side to parity with the cloud side, plus CI automation and a topic-based cross-pillar index.

### Added

- **15 new concept pages** in `learn/concepts/`. AI: tool-use-and-function-calling, mcp-explained, agentic-loops, context-windows-and-management, structured-outputs, multimodal-models, quantization-and-distillation, inference-servers, prompt-caching, guardrails-and-safety. Cloud: iam-explained, queues-vs-streams, observability-basics, eventual-consistency, idempotency-explained. Each is 5-10 min, frontmatter, Mermaid where it adds clarity, cross-links to comparisons / topics / certs.
- **4 AI service comparisons** in `resources/`: vector-databases (Pinecone, Weaviate, Qdrant, Milvus, pgvector, OpenSearch, Azure AI Search, Vertex Vector Search, Bedrock Knowledge Bases, Chroma), genai-platforms (Anthropic, OpenAI, Bedrock, Azure OpenAI, Vertex, Together, Fireworks, Groq), agent-frameworks (Claude Agent SDK, LangGraph, CrewAI, Autogen, OpenAI Agents SDK, Mastra, Semantic Kernel), llm-observability (LangSmith, Langfuse, Helicone, Phoenix, Braintrust, OpenLLMetry, Datadog).
- **5 AI hands-on builds** in `resources/hands-on-projects/`: build-rag-pipeline (pgvector + Anthropic), build-claude-agent-with-mcp (Claude + filesystem MCP + custom sqlite MCP), run-llama-on-single-gpu (vLLM, OpenAI-compatible endpoint), set-up-eval-harness (golden set, regression detection, CI integration), fine-tune-with-lora (Llama 3.2 3B + peft).
- **`topics/` cross-pillar index** - 8 pages (README + iam, networking, databases, llms-and-genai, observability, security, kubernetes). Each topic links across Learn + Compare + Reference + Build + Certify so a non-cert visitor can navigate by subject.
- **CI automation** under `.github/`:
  - `link-check.yml` - lychee link checker (PR, push, weekly Mondays). Opens an issue automatically on weekly failure.
  - `markdown-lint.yml` - markdownlint-cli2 against `.markdownlint.json`.
  - `structure-validate.yml` - runs `validate-cert-structure.sh`. Fails on missing README.md; warns on missing fact-sheet, practice-plan, scenarios, strategy.
  - Local-runnable scripts: `validate-cert-structure.sh`, `build-freshness-ledger.sh`.
- **`docs/freshness.md`** - per-cert "last verified" ledger generated from `last-updated` frontmatter. Initial state: 136 cert dirs, all "unknown" pending opportunistic backfill.
- **Mermaid diagrams** added to `learn/concepts/llm-basics.md` and `learn/concepts/vpc-explained.md` (the prior pages without one).

### Changed

- **README.md front-door reframe** - four-pillar grid promoted above the cert tables. New "I'm here to..." quick-nav with explicit non-cert paths. Per-provider deep-dive sections cut (now in STUDY-HUB only) since they were duplicated. "What's new" callout linking CHANGELOG. Stat counts updated for new concepts, comparisons, builds, topics.
- **STUDY-HUB.md** - quick-nav adds `topics/` and the freshness ledger. Service comparisons split Cloud / AI. Hands-on Projects line updated to 15 builds.
- **`learn/concepts/README.md`** - all 15 new pages indexed across new sub-categories (AI foundations / building / operations; cloud now has IAM, observability, eventual consistency, idempotency, queues vs streams sections).
- **`assets/diagrams/README.md`** - documents that `_src/` is tracked in git (was untracked).
- **`CONTRIBUTING.md`** - documents the local validator scripts and CI workflows.
- **`CLAUDE.md`** - adds an Automation section pointing to the validator scripts and freshness ledger.
- **`.markdownlint.json`** + **`.lycheeignore`** - new config files at repo root.

---

## [2026-05-03] - Scope expansion: cloud + AI learning, not just certs

### Added

- **`learn/concepts/` AI pages** - 8 promised but missing concept files: llm-basics, transformer-architecture, embeddings-and-vector-search, prompt-engineering, rag-explained, fine-tuning-vs-rag, agents-explained, evals-for-llms. Each is a 5-10 minute plain-English explanation.
- **`learn/day-one/`** - strict beginner on-ramp for people who have never opened a terminal. 5 pages: README, terminal-basics, git-basics, http-and-apis, what-is-a-server.
- **`assets/diagrams/`** - canonical home for PNG diagrams (draw.io exports), organized by topic.
- **Mermaid diagrams** seeded in 3 high-ROI pages: `learn/cloud-from-scratch.md` (region/AZ/subnet topology), `learn/ai-from-scratch.md` (RAG pipeline), `resources/architecture-patterns/web-app-3-tier.md` (3-tier flow). Plus inline mermaid in transformer-architecture.md, rag-explained.md, agents-explained.md, what-is-a-server.md.
- **Visual content standards** in `docs/ARCHITECTURE.md` and `CLAUDE.md`: PNG via draw.io MCP is canonical, Mermaid is an acceptable inline fallback.
- **YAML frontmatter convention** documented in `docs/ARCHITECTURE.md` (`last-updated`, optional `applies-to`, `difficulty`, `reading-time`). Backfill is opportunistic.
- **YouTube tie-in convention** documented in `CONTRIBUTING.md` for connecting topic pages to companion videos on @patrickwiloak.

### Changed

- **README.md repositioned** as cloud + AI learning resource (zero to hero), not cert-only. New hero, new "Four Pillars" section (Learn / Build / Certify / Reference), reordered "What's Inside" to lead with `learn/`. The "122+ certifications" social proof is preserved as the second sentence.
- **STUDY-HUB.md repositioned** as "Cloud + AI Learning Hub" with a new "Not chasing a certification?" section pointing to `learn/`. Cert decision tree is preserved.
- **CLAUDE.md (project)** rewritten to reflect 4-pillar scope, new directory structure, visual content standards, and frontmatter convention.
- **CONTRIBUTING.md** updated with `learn/` contribution rules, diagram expectations, frontmatter expectations, and YouTube tie-in convention.
- **`docs/ARCHITECTURE.md`** - "At a glance" tree updated to include `learn/` and `assets/diagrams/`. New sections: Visual content standards, Frontmatter convention. Repo description broadened.
- **2 career roadmaps retrofit** with "Foundation Concepts" + "Hands-on builds" cross-link sections (cloud-engineer, ai-ml-engineer). Rest are deferred to a follow-up pass. Body content untouched.
- **`learn/README.md`** - reordered to lead with Day One on-ramp, then Concepts, then structured paths. "Coming soon" markers removed - concept pages are shipped.
- **`learn/concepts/README.md`** - added a Day One callout for absolute beginners.

---

## [2026-04-27] - Gap fix and provider expansion

### Added

- **AWS Certified Data Engineer - Associate (DEA-C01)** - full Associate-tier scaffold (README, fact-sheet, 6 notes, practice-plan, scenarios, strategy). The current AWS data-engineering credential, replacing the retired DAS-C01 and DBS-C01.
- **Red Hat certifications** - new provider section with two starter certs:
  - **RHCSA (EX200)** - Red Hat Certified System Administrator
  - **OpenShift Administrator (EX280)** - Red Hat Certified Specialist in OpenShift Administration
- **Cisco CCNA (200-301)** - new provider section with foundational networking cert
- **Azure Microsoft Fabric Data Engineer (DP-700)** - newer Azure cert
- **Azure Network Engineer Associate (AZ-700)** - missing Azure networking cert
- **Microsoft 365 Fundamentals (MS-900)** - foundational M365 cert
- **Salesforce Administrator (ADX-201)** - new provider section, foundational admin cert
- **Salesforce Platform Developer I (DEX-450)** - developer cert
- **Practice question banks** for 10 previously-uncovered popular certs: CKA, Terraform Associate, CISSP, Databricks DE Associate, FinOps Practitioner, AWS AI Practitioner, AWS MLA-C01, Azure AI-102, Snowflake SnowPro Core, RHCSA + CCNA
- **Cloud Practitioner fact-sheet** (was missing despite existing notes and practice-plan)
- **`.templates/resources-{aws,azure,gcp}.md`** - centralized study-resources hub pages referenced from many cert dirs
- **CONTRIBUTING.md** - contribution scope, cert template, link format, retirement workflow, PR checklist
- **CHANGELOG.md** - this file
- **docs/ARCHITECTURE.md** - repo-structure and conventions doc for contributors

### Changed

- **Anthropic certs relabeled as study tracks**. Anthropic does not currently run an official certification program; the four guides under `exams/anthropic/` are now framed as self-directed Claude proficiency tracks.
- **AWS Quantum Practitioner relabeled as anticipated study track**. AWS has not formally announced QPC-C01.
- **Azure GenAI dir relabeled as cross-cert GenAI study track** (was confusingly framed as a specific AI-102/AI-900 variant)
- **GCP GenAI dir relabeled as cross-cert GenAI study track** (was framed as Professional ML Engineer; that cert lives in `exams/gcp/machine-learning-engineer/`)
- **GCP Professional Cloud Architect dirs deduplicated** - merged `exams/gcp/pca/` into `exams/gcp/cloud-architect/`. Cert count dropped from 13 to 12 GCP certs.
- **Counts in README, STUDY-HUB, and CLAUDE.md updated** to reflect actual contents (now 117+ certs across 21 providers, plus 4 vendor study tracks)
- **Roadmap files updated** to reference current AWS certs:
  - `certification-roadmap-cloud-engineer.md` - SOA-C02 → SOA-C03; MLS-C01 → MLA-C01; added DEA-C01
  - `certification-roadmap-ai-ml-engineer.md` - MLS-C01 → MLA-C01
  - `certification-roadmap-solutions-architect.md` - MLS-C01 retired note
  - `certification-roadmap-database-specialist.md` - DBS-C01 retired note + DEA-C01 as replacement
- **Heavy-offender README files rewritten** to match files actually on disk (Oracle x5, IBM x5, Azure AZ-305, AWS SAP-C02, AWS/Azure/GCP GenAI dirs)
- **All 317 broken internal links repaired** through a combination of new files (templates, missing fact-sheets) and corrected references
- **Provider integration into roadmaps**: Red Hat added to platform engineer roadmap; Cisco CCNA added as networking foundation in cloud engineer roadmap
- **STUDY-HUB decision tree, study tracks, and provider table** updated to include Red Hat / Cisco / DEA-C01 / Anthropic study-track separation

### Marked as retired

The following AWS specialty exams were retired by AWS but the study material is preserved for credential holders. Each now has a consistent `RETIRED [DATE]` banner on README and fact-sheet pointing to the modern replacement:

- **AWS Data Analytics Specialty (DAS-C01)** - retired April 8, 2024 → DEA-C01
- **AWS Database Specialty (DBS-C01)** - retired April 29, 2024 → DEA-C01
- **AWS Machine Learning Specialty (MLS-C01)** - retired April 15, 2025 → MLA-C01
- **AWS SysOps Administrator (SOA-C02)** - retired Sept 29, 2025 → SOA-C03 CloudOps Engineer

### Removed

- `exams/gcp/pca/` directory (merged into `exams/gcp/cloud-architect/`); 4 internal roadmap link references updated

### Documentation

- All retired-cert references in active roadmap files now have RETIRED banners
- Anthropic is now consistently presented as study tracks (not certifications) across README, STUDY-HUB, all 4 cert dirs
- Provider count corrected in README, STUDY-HUB, and CLAUDE.md from 19 to 21
- Cert count corrected from 118+ to accurate 117+ + 4 study tracks
- README structure section updated to reflect the new dir layout
- Internal link audit: 0 broken links remain (verified with code-block-aware scanner across all 700+ markdown files)

---

## [2026-04 prior] - Project state before this changelog

The repository existed prior to this entry. Before 2026-04-27, the catalog claimed:

- 118+ certifications across 19 providers
- 12 cross-cloud service comparisons
- 9 CLI cheat sheets
- 17 architecture patterns
- 11 certification roadmaps
- 10 hands-on projects
- 6 interview prep guides
- 5 compliance and 5 migration guides

That state had documentation drift: a duplicate GCP PCA dir, Anthropic certs framed as official, several AWS specialties listed as active despite being retired, broken internal links in dozens of cert READMEs, and a missing CONTRIBUTING.md referenced from the main README. The 2026-04-27 work above resolved those issues.

---

## How to update this changelog

When making user-visible or operationally-significant changes:

1. Add a dated section at the top using `## [YYYY-MM-DD] - Brief description`.
2. Group entries under: **Added**, **Changed**, **Deprecated**, **Removed**, **Fixed**, **Security**.
3. Link to the cert dir or resource file affected.
4. Keep entries concise (one line per item); link out for detail.
5. New cert additions, retirements, schema changes, and provider sections are always logged here.
6. Typo fixes and minor link repairs do not need a changelog entry.
