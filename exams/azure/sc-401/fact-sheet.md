---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 12 min
---

# Microsoft Information Security Administrator (SC-401) Fact Sheet

## Exam Overview

**Exam Code:** SC-401
**Exam Name:** Administering Information Security in Microsoft 365
**Level:** Associate
**Duration:** 100 minutes
**Format:** Multiple choice, multiple select, drag-and-drop, case studies, yes/no series
**Questions:** Typically 40-60
**Passing Score:** 700 out of 1000
**Cost:** USD 165 (varies by country)
**Valid For:** 1 year, renewable free online through Microsoft Learn
**Delivery:** Pearson VUE, test center or online proctored
**Prerequisites:** None formally; working knowledge of Microsoft 365 and Purview expected

> **Replaces SC-400.** SC-401 (Information Security Administrator) superseded SC-400 (Information Protection and Compliance Administrator). The scope shifted toward data security operations and now includes Microsoft Purview DSPM for AI and protections for Copilot data access. If you find SC-400 study material, treat the Purview fundamentals as still valid and the domain structure and AI content as out of date.

<!-- -->

> **Verify before booking.** Confirm the current outline and price on the official pages below.

**[📖 SC-401 certification page](https://learn.microsoft.com/en-us/credentials/certifications/information-security-administrator/)** - registration and renewal
**[📖 SC-401 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401)** - the authoritative skills-measured outline
**[📖 Microsoft Purview documentation](https://learn.microsoft.com/en-us/purview/)** - the product this exam is about

## Why this exam is in this repo

The repo has five [compliance guides](../../../resources/compliance-guides/) covering SOC 2, GDPR, HIPAA, PCI DSS, and FedRAMP, plus three AI governance guides. SC-401 is the certification that turns those obligations into configured controls: classification, labeling, DLP, insider risk, and data governance for AI.

It is also the data-protection counterpart to [SC-300](../sc-300/) on identity, and both feed [SC-100](../sc-100/).

## Target Audience

- Information protection and compliance administrators
- Microsoft 365 administrators owning data security
- Security engineers implementing DLP and insider risk controls
- Anyone preparing a Copilot or AI assistant rollout that touches sensitive data

## Exam Domains

### Domain 1: Implement information protection (30-35%)

**Key Concepts:**
- Sensitive information types: built-in, custom, exact data match (EDM), document fingerprinting
- Trainable classifiers: pre-trained and custom, and when each is appropriate
- Sensitivity labels: scopes (items, groups and sites, schematized data assets), label settings, encryption, content marking
- Label policies: publishing, default labels, mandatory labeling, downgrade justification
- Auto-labeling: client-side (in policy) versus service-side (auto-labeling policies), and simulation mode
- Label priority, inheritance, and co-authoring on encrypted documents
- Double Key Encryption and when its trade-offs are acceptable
- Encryption with Rights Management, usage rights, and offline access
- Purview Information Protection scanner for on-premises file shares
- Data map, scanning, and classification across Azure, on-premises, and other clouds
- Data Security Posture Management (DSPM), including DSPM for AI

**[📖 Sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels)** - label design and behavior
**[📖 Trainable classifiers](https://learn.microsoft.com/en-us/purview/classifier-learn-about)** - classification at scale

### Domain 2: Implement data loss prevention (30-35%)

**Key Concepts:**
- DLP policy anatomy: locations, conditions, exceptions, actions, user notifications, overrides, incident reports
- Locations: Exchange, SharePoint, OneDrive, Teams chat and channel messages, devices (endpoint DLP), on-premises repositories, Fabric and Power BI, Defender for Cloud Apps, and AI applications
- Endpoint DLP: onboarding devices, restricted apps, unallowed browsers, network exceptions, printer and removable storage controls
- Policy tips, user overrides with justification, and false positive handling
- DLP for Microsoft 365 Copilot and other AI applications
- Adaptive Protection: dynamically strengthening DLP based on insider risk level
- Alerts, incident management, and DLP reporting
- Testing with simulation mode before enforcement
- Endpoint DLP versus Defender for Cloud Apps session policies

**[📖 Data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)** - policy design across workloads
**[📖 Endpoint DLP](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)** - device-level enforcement

### Domain 3: Manage risks, alerts, and activities (30-35%)

**Key Concepts:**
- Insider Risk Management: policy templates, indicators, triggering events, sequence detection, and risk scoring
- Insider risk policy lifecycle: alerts, triage, cases, and actions including escalation
- Adaptive Protection integration between insider risk and DLP or Conditional Access
- Privacy controls: anonymization of usernames in insider risk
- Communication Compliance: policies, conditions, review workflow, and remediation
- Information Barriers: segments, policies, and modes
- Purview Audit: standard versus premium, search, retention policies for audit logs, high-value events
- eDiscovery: cases, holds, search, export, and premium features
- Content Search and its limits
- Data lifecycle management: retention labels, retention policies, disposition review, records management
- AI activity monitoring: DSPM for AI reports, Copilot interaction auditing

**[📖 Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management)** - policies, indicators, and triage
**[📖 Purview Audit](https://learn.microsoft.com/en-us/purview/audit-solutions-overview)** - audit search and retention
**[📖 Data lifecycle management](https://learn.microsoft.com/en-us/purview/data-lifecycle-management)** - retention and disposition

## Decision quick reference

| Requirement | Feature |
|---|---|
| Protection that travels with the file, including outside the tenant | Sensitivity label with encryption |
| Prevent an action at a boundary (send, copy, print, upload) | DLP policy |
| Classify at scale without user action | Auto-labeling policy with trainable classifiers |
| Keep content for a fixed period regardless of user deletion | Retention policy or retention label |
| Formal records declaration with disposition review | Records management |
| Detect a departing employee exfiltrating data | Insider Risk Management |
| Prevent two groups from communicating | Information Barriers |
| Review messages for policy violations | Communication Compliance |
| Prove who accessed what | Purview Audit |
| Preserve content for litigation | eDiscovery hold |
| See what sensitive data AI is touching | DSPM for AI |

## Related repo material

- [Notes](./notes/) - three notes, one per domain
- [Practice plan](./practice-plan.md) - 6-week schedule
- [Scenarios](./scenarios.md)
- [Strategy](./strategy.md)
- [SC-300](../sc-300/) - the identity counterpart
- [SC-100](../sc-100/) - the design exam this feeds
- [Compliance guides](../../../resources/compliance-guides/) - the obligations behind the controls
- [AI security](../../../resources/ai-security/) - the engineering view of the AI risks Purview governs
