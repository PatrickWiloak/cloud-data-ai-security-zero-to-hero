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

- [ ] Fix `build-freshness-ledger.sh` path bug (lines 49, 83 emit root-relative paths from `docs/`), then regenerate `docs/freshness.md`. Clears 191 broken links.
- [ ] Rewrite 87 absolute `/exams/...` links as relative, mostly in `resources/certification-roadmap-*.md`.
- [ ] Repoint or remove 28 links to the old directory layout (`cisco/ccna/`, `aws/specialty/security-specialty/`, `axelos/itil-4-foundation/`).
- [ ] Update `STUDY-HUB.md` provider table: add ISACA, Offensive Security, Palo Alto, ServiceNow, VMware; correct CompTIA (4), Cisco (2), Salesforce (3).
- [ ] Update cert/provider badge counts in `README.md` and `STUDY-HUB.md` from 122/22 to 127/27.
- [ ] Split `link-check.yml` into a blocking internal-link job and a non-blocking external-URL job.

### Priority 2 - content substance

- [ ] Write notes for the 10 skeleton certs (cisco/ccnp-encor, comptia/cysa-plus, comptia/network-plus, isaca/cisa, isaca/cism, offensive-security/oscp, palo-alto/pcnsa, salesforce/pd2, servicenow/csa, vmware/vcp-dcv). Also clears 77 broken links.
- [ ] Resolve the diagram standard: produce PNGs under `assets/diagrams/` or promote mermaid to primary and remove the broken PNG example in `docs/ARCHITECTURE.md:206`.
- [ ] Add index READMEs to the 21 provider directories that lack one.
- [ ] Complete `aws/professional/genai-developer-aip-c01` (missing practice-plan, scenarios, strategy) and link it from the hub.
- [ ] Move `exams/aws/genai` under `foundational/` as the AI Practitioner cert; reconcile `azure/genai` and `gcp/genai` placement.
- [ ] Replace the 2 remaining `last-updated: YYYY-MM-DD` placeholders.

### Priority 3 - leverage

- [ ] Build `docs/certs.json` from fact-sheets; generate the hub table, provider indexes, and freshness ledger from it.
- [ ] Add practice questions for uncovered certs (34 of 127 covered today).
- [ ] Add Tier 1 certifications: SC-100, SC-300, SC-400, PL-300, CNCF associates (OTCA/CGOA/CAPA/CCA/CNPA), Oracle OCI GenAI, Google GenAI Leader, ISC2 CC, an observability cert.
- [ ] Stagger `last-updated` re-verification by provider batch so 326 files do not all go stale on 2026-10-30.

### Priority 4 - differentiation

- [ ] Per-cert `flashcards.csv` (Anki-importable) generated from fact-sheets and notes.
- [ ] Map `resources/hands-on-projects/` labs to the certs they support.
- [ ] Add `status:` and `exam-version:` fact-sheet frontmatter plus a revision-warning script.
- [ ] Wire `check-orphan-links.sh` into CI or document it as manual in `.github/AUTOMATION.md`.
- [ ] Prune stale absolute paths and the blanket `Bash(*)` allow from `.claude/settings.json`.
