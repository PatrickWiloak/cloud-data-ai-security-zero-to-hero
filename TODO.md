# TODO

Working task list for **cloud-data-ai-security-zero-to-hero**. Read this at the start of a work session and keep it current as work completes - check items off with a date, add follow-ups as they surface. Stale TODOs are worse than none. Security debt (if any) is tracked separately in `SECURITY-DEBT.md`.

---

## Open

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

- [ ] Write notes for the 10 outline-stage certs (cisco/ccnp-encor, comptia/cysa-plus, comptia/network-plus, isaca/cisa, isaca/cism, offensive-security/oscp, palo-alto/pcnsa, salesforce/pd2, servicenow/csa, vmware/vcp-dcv). As each lands, restore the real links and drop its `_(planned)_` markers and the outline-stage banner.
- [ ] Resolve the diagram standard: produce PNGs under `assets/diagrams/` (currently zero exist) or promote mermaid to primary in `CLAUDE.md` and `docs/ARCHITECTURE.md`.
- [ ] Add index READMEs to the 21 provider directories that lack one.
- [ ] Complete `aws/professional/genai-developer-aip-c01` (missing practice-plan, scenarios, strategy) and link it from the hub.
- [ ] Move `exams/aws/genai` under `foundational/` as the AI Practitioner cert; reconcile `azure/genai` and `gcp/genai` placement.
- [ ] Replace the 2 remaining `last-updated: YYYY-MM-DD` placeholders.

### Priority 3 - leverage

- [ ] Build `docs/certs.json` from fact-sheets; generate the hub table, provider indexes, and freshness ledger from it.
- [ ] Add practice questions for uncovered certs (34 of 137 covered today).
- [ ] Add Tier 1 certifications: SC-100, SC-300, SC-400, PL-300, CNCF associates (OTCA/CGOA/CAPA/CCA/CNPA), Oracle OCI GenAI, Google GenAI Leader, ISC2 CC, an observability cert.
- [ ] Stagger `last-updated` re-verification by provider batch so 326 files do not all go stale on 2026-10-30.

### Priority 4 - differentiation

- [ ] Per-cert `flashcards.csv` (Anki-importable) generated from fact-sheets and notes.
- [ ] Map `resources/hands-on-projects/` labs to the certs they support.
- [ ] Add `status:` and `exam-version:` fact-sheet frontmatter plus a revision-warning script.
- [ ] Wire `check-orphan-links.sh` into CI or document it as manual in `.github/AUTOMATION.md`.
- [ ] Prune stale absolute paths and the blanket `Bash(*)` allow from `.claude/settings.json`.
