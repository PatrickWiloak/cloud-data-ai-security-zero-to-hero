---
last-updated: 2026-07-28
difficulty: n/a
reading-time: 20 min
---

# Improvement roadmap

A repo-wide gap analysis: what is broken, what is missing, and what would raise the
quality bar. Findings are measured against the repo as of 2026-07-28 (1,506 markdown
files, ~2.6M words, 127 cert directories across 27 providers).

Every number below was produced by scanning the tree, not estimated. Re-run the
commands in [How the numbers were produced](#how-the-numbers-were-produced) to refresh.

**Contents**

- [1. Correctness gaps (fix first)](#1-correctness-gaps-fix-first)
- [2. Coverage gaps in existing content](#2-coverage-gaps-in-existing-content)
- [3. Certifications we could add](#3-certifications-we-could-add)
- [4. Structural and experience improvements](#4-structural-and-experience-improvements)
- [5. Suggested sequencing](#5-suggested-sequencing)
- [How the numbers were produced](#how-the-numbers-were-produced)

---

## 1. Correctness gaps (fix first)

These are defects, not missing features. They make the repo look less trustworthy than
the content actually is.

### 1.1 - 383 broken internal links

A scan of every relative markdown link found 383 targets that do not exist on disk.
They fall into four fixable buckets:

| Count | Bucket | Root cause | Fix |
|------:|--------|------------|-----|
| 191 | `docs/freshness.md` rows | Generator emits repo-root-relative paths from a file that lives in `docs/`, so `exams/aws/...` resolves to `docs/exams/aws/...` | One-line fix in `.github/scripts/build-freshness-ledger.sh`: prefix emitted paths with `../` (lines 49 and 83) |
| 87 | Absolute paths like `/exams/aws/shared/services/compute/ec2.md` | Leading slash resolves to the GitHub domain root, not the repo root. Concentrated in `resources/certification-roadmap-*.md` | Rewrite as relative paths (`../exams/...`) |
| 77 | Links to `notes/NN-topic.md` files that were never written | Skeleton certs ship a README and practice-plan that promise notes | Write the notes (see [2.1](#21---ten-certs-have-zero-notes)) or drop the links until they exist |
| 28 | Stale paths from an older directory layout | E.g. `../../cisco/ccna/README.md` (actual: `ccna-200-301`), `../../aws/specialty/security-specialty/` (actual: `security-scs-c02`), `../../axelos/itil-4-foundation/` (provider does not exist) | Repoint or remove |

Roughly 6 more are intentional illustrative snippets in `CLAUDE.md`, `CONTRIBUTING.md`,
and `assets/diagrams/README.md`. Those are fine.

### 1.2 - CI cannot catch any of this

`link-check.yml` runs lychee with `fail: false`, so a broken-link report is uploaded as
an artifact and the job stays green. Nothing enforces internal link integrity on a PR.

Recommended: split into two jobs.

- **Internal links** - fast, offline, no network flake, `fail: true`. This is the one
  that should block a merge.
- **External vendor URLs** - keep `fail: false` plus the existing weekly issue-filing,
  because vendor URL rot is not the contributor's fault.

### 1.3 - Navigation counts have drifted from reality

`STUDY-HUB.md` and `README.md` both advertise "122+ certifications across 22 providers".
Actual: **127 cert directories across 27 provider directories**.

The provider table in `STUDY-HUB.md` (around line 165) is missing five providers entirely
and undercounts three:

| Provider | Table says | Actually present | Note |
|----------|-----------:|-----------------:|------|
| CompTIA | 2 | 4 | Network+ and CySA+ missing from the table |
| Cisco | 1 | 2 | CCNP Enterprise ENCOR missing from the table |
| Salesforce | 2 | 3 | Platform Developer II missing from the table |
| ISACA | absent | 2 | CISA, CISM |
| Offensive Security | absent | 1 | OSCP (PEN-200) |
| Palo Alto Networks | absent | 1 | PCNSA |
| ServiceNow | absent | 1 | CSA |
| VMware | absent | 1 | VCP-DCV |

Content exists and is decent; it is simply undiscoverable from the hub. This is the
cheapest high-impact fix in the repo.

### 1.4 - The documented visual standard has zero instances

`CLAUDE.md` and `docs/ARCHITECTURE.md` specify PNG diagrams under
`assets/diagrams/<topic>/<slug>.png`. `assets/diagrams/` contains exactly one file:
`README.md`. There are zero PNGs, and the three PNG references that exist in markdown are
all documentation examples pointing at files that were never created (including
`docs/ARCHITECTURE.md:206`, which renders as a broken image).

Mermaid is doing the real work: 89 files use fenced mermaid blocks. Two honest options:

1. Produce the PNGs and keep the standard as written, or
2. Promote mermaid to the primary convention, demote PNG to "for diagrams too complex to
   read inline", and remove the broken example references.

Option 2 matches what the repo actually does and costs almost nothing.

### 1.5 - Frontmatter is present on 22% of files, and 326 of them share one date

- 328 of 1,506 markdown files carry `last-updated` frontmatter.
- 326 of those are stamped `2026-05-03`. At the documented 180-day re-verify cadence,
  effectively the entire repo goes stale on the same day (2026-10-30).
- Two files still contain the literal placeholder `last-updated: YYYY-MM-DD`.
- `docs/freshness.md` was last built 2026-05-04 and has not been regenerated since.

The freshness ledger only means something if verification dates are staggered by actual
review work. Suggest re-verifying in provider-sized batches so dates spread naturally,
and adding the ledger rebuild to the structure-validate workflow as a committed artifact
rather than a preview.

---

## 2. Coverage gaps in existing content

### 2.1 - Ten certs have zero notes

These directories have a README, fact-sheet, and practice-plan, but an empty or absent
`notes/` directory. Their READMEs link to notes that do not exist, which is the source of
the 77 broken links in [1.1](#11---383-broken-internal-links).

| Cert | Missing notes |
|------|--------------:|
| `cisco/ccnp-enterprise-encor-350-401` | 6 |
| `comptia/cysa-plus` | - |
| `comptia/network-plus` | - |
| `isaca/cisa` | - |
| `isaca/cism` | - |
| `offensive-security/oscp-pen-200` | - |
| `palo-alto-networks/pcnsa` | - |
| `salesforce/platform-developer-2` | - |
| `servicenow/csa` | - |
| `vmware/vcp-dcv-2v0-21-23` | - |

A cert with no notes is a stub advertised as a study guide. Either fill them or mark them
"skeleton" in the hub so expectations match reality.

### 2.2 - Practice questions cover 34 of 127 certs

`resources/practice-questions/` has 34 files (plus a template). AWS and Azure are well
served. Nothing exists for NVIDIA (10 certs), HashiCorp beyond Terraform Associate (1 of 7),
FinOps beyond Practitioner (1 of 4), MongoDB, Confluent, GitHub, Oracle, IBM, ISACA,
Anthropic, or any of the newer CNCF exams.

### 2.3 - Twenty-one of 27 provider directories have no index README

Only `cloud-security-alliance`, `isaca`, `isc2`, `offensive-security`,
`palo-alto-networks`, and `servicenow` have one. `STUDY-HUB.md` links to
`exams/aws/`, `exams/azure/`, and so on, and those land on a bare GitHub directory
listing with no ordering, no difficulty signal, and no suggested path.

A short generated index per provider (cert name, code, level, status, link) would fix
this and could be script-generated from the fact-sheets.

### 2.4 - Structural inconsistency in the GenAI directories

`exams/aws/genai`, `exams/azure/genai`, and `exams/gcp/genai` sit at provider level while
every sibling cert sits under a level directory. `exams/aws/genai` is actually the AWS
Certified AI Practitioner, which belongs under `exams/aws/foundational/`. The
structure validator counts them as certs, which is part of the 122-vs-127 drift.

### 2.5 - One outstanding structure warning

`aws/professional/genai-developer-aip-c01` is classified senior tier but is missing
`practice-plan.md`, `scenarios.md`, and `strategy.md`. It is also one of the two files
flagged as orphaned by `check-orphan-links.sh` (nothing links to it).

---

## 3. Certifications we could add

Grouped by how well they fit the repo's cloud + data + AI + security remit. Exam codes
and availability churn constantly, so **verify every code against the vendor's site
before building a page** - especially the newer AI and CNCF exams.

### Tier 1 - fills a thematic hole the repo already claims to cover

| Provider | Certification | Why it matters here |
|----------|---------------|---------------------|
| Microsoft | **SC-100** Cybersecurity Architect Expert | The repo has SC-200 and SC-900 but stops short of the expert-level security architect exam, which is the capstone of the Microsoft security track |
| Microsoft | **SC-300** Identity and Access Administrator | The repo has an IAM topic page and an identity service comparison but no identity cert on any cloud |
| Microsoft | **SC-400** Information Protection and Compliance | Pairs with the five compliance guides already in `resources/compliance-guides/` |
| Microsoft | **PL-300** Power BI Data Analyst | The single biggest analytics cert by volume; the repo covers DP-600/DP-700 but not the analyst tier |
| GIAC / SANS | **GSEC, GCIH, GCLD, GCSA, GPEN** | An entire security certification ecosystem is absent. GCLD (Cloud Security Essentials) and GCSA (Cloud Automation) are directly on-theme |
| ISC2 | **CC** (Certified in Cybersecurity) | Free, entry-level, and the natural security on-ramp for the "zero to hero" promise. Currently the security path starts at Security+ |
| Oracle | **OCI Generative AI Professional**, **OCI AI Foundations** | Oracle has five OCI certs here and zero AI ones, in an AI-focused repo |
| Google | **Generative AI Leader**, **Associate Data Practitioner** | Two of the newest GCP exams; the repo has 12 GCP certs but neither |
| CNCF | **OTCA** (OpenTelemetry), **CGOA** (GitOps), **CAPA** (Argo), **CCA** (Cilium), **CNPA** (Platform Engineering) | Seven Kubernetes certs are covered but none of the newer CNCF associates, despite the repo having a platform-engineer roadmap and an observability topic page |
| Splunk / Elastic / Datadog | Core certifications | `resources/service-comparison-observability-monitoring.md` and `topics/observability.md` exist, but there is not a single observability certification anywhere in `exams/` |

### Tier 2 - strong fit, high demand

| Provider | Certification |
|----------|---------------|
| Red Hat | **RHCE (EX294)**, **EX188/EX288** containers, **EX380** OpenShift automation |
| CompTIA | **Linux+**, **PenTest+**, **SecurityX (CASP+)**, **Data+** |
| ISACA | **CRISC**, **CDPSE** |
| Cisco | **CyberOps Associate (200-201)**, **DevNet Associate (200-901)** |
| Palo Alto | **PCNSE**, **PCCSE** (Prisma Cloud), **PCDRA** (Cortex XDR) |
| Offensive Security | **OSEP**, **OSWE**, **OSWA** |
| Salesforce | **Platform App Builder**, **AI Associate**, **Agentforce Specialist** |
| Databricks | **Associate Developer for Apache Spark**, **Data Analyst Associate** |
| Snowflake | **SnowPro Associate: Platform**, **Advanced: Data Scientist** |
| HashiCorp | **Vault Operations Professional** |
| Microsoft | **AZ-140** (Azure Virtual Desktop), **AZ-800/801** (Windows Server Hybrid) |
| IBM | **watsonx Generative AI Engineer - Associate** |

### Tier 3 - broadens the repo into adjacent ecosystems

| Area | Candidates |
|------|-----------|
| Data tooling | **dbt Analytics Engineering**, **Astronomer Airflow**, **Confluent Flink**, **Neo4j**, **Redis** |
| Identity and PAM | **Okta** Certified Professional/Administrator, **CyberArk** Defender |
| Network security | **Fortinet NSE**, **Check Point CCSA/CCSE**, **Zscaler ZCCA/ZCCP** (fits the existing zero-trust architecture pattern), **F5 BIG-IP Administrator**, **Juniper JNCIA-Cloud** |
| Service management | **ITIL 4 Foundation** - already referenced by a dangling link in `exams/servicenow/csa/README.md` |
| Architecture | **TOGAF** Foundation/Practitioner |
| Virtualization and hybrid | **Nutanix NCP**, **Veeam VMCE**, additional **VMware VCP** tracks |
| Non-US clouds | **Alibaba Cloud ACA/ACP**, **Huawei HCIA/HCIP Cloud** |
| Linux | **LPIC-1/2**, **SUSE Certified Administrator** |

### A note on scope

At 127 certs the marginal value of cert number 128 is lower than the marginal value of
finishing the ten skeleton certs and adding practice questions to the 93 certs that lack
them. Recommend capping new-cert work at Tier 1 until [section 1](#1-correctness-gaps-fix-first)
and [2.1](#21---ten-certs-have-zero-notes) are closed.

---

## 4. Structural and experience improvements

### 4.1 - A machine-readable cert index

Add `docs/certs.json` (or `.yaml`) generated from the fact-sheets: provider, exam code,
name, level, status (active / retired / anticipated), duration, cost, path, last-updated.

This single file would let us generate the STUDY-HUB provider table, the per-provider
index READMEs, the freshness ledger, and the badge counts - which removes the entire class
of drift documented in [1.3](#13---navigation-counts-have-drifted-from-reality). Generated
tables cannot go stale the way hand-maintained ones do.

### 4.2 - Spaced repetition assets

There is no flashcard or quiz artifact anywhere in the repo. A per-cert `flashcards.csv`
(Anki-importable, question/answer/tag columns) generated from fact-sheets and notes would
be a genuine differentiator, and it is mechanical to produce from content that already
exists.

### 4.3 - Exam-version tracking

Cert codes rotate (SAA-C03 to C04, SY0-701 to 801). The repo handles retired certs well -
`aws/specialty/data-analytics-das-c01` has a clear retirement notice and points to its
replacement, and the anticipated tracks such as `quantum-practitioner-qpc-c01` are
explicitly labeled as not-yet-real. That discipline is a strength worth extending: add a
`status:` and `exam-version:` field to fact-sheet frontmatter so a script can flag certs
approaching a known revision date.

### 4.4 - Wire the unused automation

`check-orphan-links.sh` exists but is not referenced by any workflow. The glossary scripts
(`glossary-autolink.py`, `glossary-add-anchors.py`, `glossary-upgrade-existing-links.py`)
are likewise manual-only. Either wire them into CI or document in `.github/AUTOMATION.md`
that they are intentionally run by hand.

### 4.5 - Connect labs to certs

`resources/hands-on-projects/` has 15 solid projects and `exams/` has 127 certs, but
nothing maps between them. A "labs for this exam" section in each cert README, or a
mapping table in the projects index, turns two good resources into one better one.

### 4.6 - Repo hygiene

- `.claude/settings.json` carries absolute paths from a previous machine
  (`/home/plw/coding/cloud-certification-study-guides/...`) and a broad `Bash(*)` allow.
  Worth pruning to the permissions actually needed.
- `TODO.md` says "None tracked yet" while the CHANGELOG shows active development. The
  items in this document are the natural backlog.

---

## 5. Suggested sequencing

**Phase 1 - credibility (small, mechanical, high impact)**

1. Fix the `build-freshness-ledger.sh` path bug and regenerate `docs/freshness.md` (191 links).
2. Rewrite the 87 absolute `/exams/...` links in the roadmap files as relative.
3. Repoint or remove the 28 stale-layout links.
4. Update the `STUDY-HUB.md` provider table and both badge counts to 127 / 27.
5. Make internal link checking a blocking CI job.

**Phase 2 - substance**

6. Write notes for the ten skeleton certs, which also clears 77 broken links.
7. Resolve the diagram standard: either produce PNGs or promote mermaid and remove the
   broken example references.
8. Add per-provider index READMEs (21 missing).

**Phase 3 - leverage**

9. Build `docs/certs.json` and generate the hub table, provider indexes, and ledger from it.
10. Add practice questions for the highest-traffic uncovered certs.
11. Add Tier 1 certifications, starting with SC-100/SC-300, the CNCF associates, and the
    Oracle and Google AI exams.

**Phase 4 - differentiation**

12. Flashcard exports.
13. Lab-to-cert mapping.
14. Exam-version tracking with automated revision warnings.

---

## How the numbers were produced

```bash
# Cert directories and providers
find exams -mindepth 2 -type d -name notes | wc -l     # 127 cert dirs
ls -d exams/*/ | wc -l                                  # 27 providers

# Structure and frontmatter validators
bash .github/scripts/validate-cert-structure.sh
bash .github/scripts/validate-frontmatter.sh

# Certs with no notes
for d in $(find exams -mindepth 2 -type d -name notes); do
  [ "$(find "$d" -name '*.md' | wc -l)" -eq 0 ] && echo "$d"
done

# Frontmatter coverage
grep -rl '^last-updated:' --include='*.md' . | wc -l
find . -name '*.md' -not -path './.git/*' | wc -l

# Diagram usage
grep -rl '```mermaid' --include='*.md' . | wc -l
find assets -name '*.png' | wc -l
```

Broken internal links were counted by walking every `.md` file, extracting relative
markdown link targets (excluding `http:`, `https:`, `mailto:`, and pure anchors), and
testing each resolved path with `os.path.exists`.
