---
last-updated: 2026-10-14
applies-to: Associate Google Workspace Administrator exam guide, checked 2026-10-14
difficulty: intermediate
---

# Google Cloud Associate Google Workspace Administrator Certification

> **Level corrected 2026-10-14.** Earlier versions of this folder described a "Professional" exam with five domains. Google's current exam is the **Associate Google Workspace Administrator**, with six sections. The folder name stays `workspace-administrator` so links keep working.

## Exam Overview

**Exam Code:** Associate Google Workspace Administrator
**Level:** Associate
**Duration:** 2 hours (120 minutes)
**Questions:** 50-60 multiple choice and multiple select
**Passing Score:** Not officially published
**Cost:** $125 USD (plus tax where applicable)
**Validity:** Not stated on the exam page; see Google's renewal FAQs
**Languages:** English, Japanese
**Delivery:** Online-proctored or Pearson VUE test center
**Prerequisites:** None. Recommended: about 6 months of Super Admin experience and hands-on time with Business Plus and Enterprise features

**[📖 Associate Google Workspace Administrator certification](https://cloud.google.com/learn/certification/google-workspace-administrator)** - registration, logistics, prep resources.
**[📖 Exam guide (PDF)](https://services.google.com/fh/files/misc/associate_google_workspace_administrator_exam_guide_english.pdf)** - the authoritative topic list. Re-check it before you sit the exam.

## Exam Sections

| # | Section | Weight | Notes |
|---|---|---|---|
| 1 | Managing user accounts, domains, and Directory | ~20% | [01-users-domains-directory](notes/01-users-domains-directory.md) |
| 2 | Managing core Workspace services | ~23% | [02-core-services](notes/02-core-services.md), [03-gen-ai-and-automation](notes/03-gen-ai-and-automation.md) |
| 3 | Managing data governance and compliance | ~15% | [04-data-governance-and-compliance](notes/04-data-governance-and-compliance.md) |
| 4 | Managing security policies and access controls | ~20% | [05-security-and-access](notes/05-security-and-access.md) |
| 5 | Managing browsers and endpoints | ~10% | [06-browsers-and-endpoints](notes/06-browsers-and-endpoints.md) |
| 6 | Monitoring and troubleshooting common issues | ~13% | [07-monitoring-and-troubleshooting](notes/07-monitoring-and-troubleshooting.md) |

### What each section covers

- **1. Users, domains, Directory** - user life cycle (create, sync, SSO, suspend, delete, archive, transfer), OU design, groups (distribution, Collaborative Inbox, dynamic, security), primary and secondary domains, buildings and resources.
- **2. Core services** - Gmail (MX, routing, content compliance, SPF/DKIM/DMARC, delegation), Drive and Docs (sharing, trust rules, target audiences, shared drives, labels, quotas), Calendar, Meet, Chat, plus Gemini controls and AppSheet / Apps Script.
- **3. Governance** - Vault retention and holds, DLP rules, trust rules, Takeout and data export, data regions, classification labels.
- **4. Security and access** - passwords, 2SV and passkeys, context-aware access, admin roles, session control, security center, investigation tool, alert rules, Marketplace allowlist, OAuth app control.
- **5. Browsers and endpoints** - basic vs advanced vs third-party mobile management, account vs device wipe, Chrome Browser Cloud Management, extension policies.
- **6. Troubleshooting** - Email Log Search, Admin Toolbox, audit logs, Status Dashboard, Meet quality tool, HAR files, working with Google Support.

## Study Materials in This Folder

| File | Use it for |
|---|---|
| [fact-sheet.md](fact-sheet.md) | One-page cram sheet: decision tables and numbers |
| [notes/](notes/) | Seven notes, one per exam section (Gemini and AppSheet get their own) |
| [scenarios.md](scenarios.md) | Worked scenarios in the exam's "pick the tool or setting" style |
| [flashcards.csv](flashcards.csv) | Spaced-repetition deck generated from the notes |
| [practice-plan.md](practice-plan.md) | Week-by-week plan built on practice questions and the cram sheet |
| [strategy.md](strategy.md) | Test-taking approach and the traps that cost points |
| [Practice questions](../../../resources/practice-questions/gcp-workspace-administrator.md) | Original scenario questions with explanations |

## How to Get Hands-On

- Use a **Google Workspace trial** with a spare domain (a free-trial Business Plus or Enterprise tenant covers nearly every topic). Admin console access is the whole point of this exam.
- Create a test OU tree, a Collaborative Inbox group, a dynamic group, a trust rule, a DLP rule in audit-only mode, and a Vault retention rule plus a hold.
- Publish SPF, DKIM and DMARC records on a test domain and read the results in a message header with the Admin Toolbox.
- Learn the console paths. Many questions are "where do you change this" in disguise.
- Complete the **Google Workspace Administrator learning path** on Google Cloud Skills Boost.

## Related

- [GCP certifications index](../README.md)
- [IAM topic index](https://security.noblerworks.com/topics/iam/)
