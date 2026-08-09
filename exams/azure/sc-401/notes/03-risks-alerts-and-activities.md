---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 12 min
---

# 03 - Risks, alerts, and activities

**Domain 3: Manage risks, alerts, and activities (30-35%)**

Detecting risky behavior, controlling communication, and proving what happened.

---

## Insider Risk Management

Detects patterns of user behavior over time rather than single events.

**Policy templates** include data theft by departing users, data leaks, data leaks by priority users, security policy violations, patient data misuse, risky browser usage, and forensic evidence.

**Structure**:
- **Triggering event** starts the detection window. Commonly a termination date from the **HR connector**, a DLP policy match, or a security alert.
- **Indicators** are the signals scored: SharePoint downloads, USB copies, uploads to personal cloud, printing, renaming to obscure extensions, email to external recipients.
- **Sequence detection** identifies patterns such as download then rename then exfiltrate, which scores higher than any single event.
- **Risk score** accumulates, producing alerts, which analysts triage into **cases** with actions including notice, escalation for investigation, and escalation to eDiscovery.

**Privacy controls**: username anonymization by default, role-based access separating analysts from investigators, and configurable exclusions. These matter in works council and GDPR contexts and are directly testable.

---

## Communication Compliance

Reviews message content in Exchange, Teams, Viva Engage, and connected third-party sources against policy: offensive language, sensitive information, regulatory compliance, and conflict of interest.

Structure: policy with conditions, a reviewer group, and a remediation workflow (resolve, notify the user, escalate, tag as a false positive). Supports sampling percentages and pre-trained classifiers.

It **reviews**; it does not prevent. Requirements to prevent communication point at Information Barriers.

---

## Information Barriers

Prevents communication and discovery between defined groups.

- **Segments** defined by an Entra attribute such as department or job title
- **Policies** between segments in **block** mode (these two cannot communicate) or **allow** mode (this segment may communicate only with those listed)
- Enforcement spans Teams, SharePoint, and OneDrive
- Users cannot search for, message, call, or share with blocked segments

Common in financial services (banking and trading separation) and legal (matter conflict walls).

---

## Purview Audit

| | Standard | Premium |
|---|---|---|
| Retention | 180 days by default | Longer, with configurable audit retention policies up to 10 years |
| High-value events | Not included | MailItemsAccessed, Send, SearchQueryInitiated |
| Bandwidth | Standard | Higher API throughput |

**Audit retention policies** let you keep specific record types longer than the default, scoped by workload, record type, or user.

Audit answers "who did what, when". It is the evidence layer for investigations, and increasingly for AI interactions, since Copilot prompts and responses are auditable events.

---

## eDiscovery

- **Content search** finds content across Microsoft 365 without a case structure. No hold, no export workflow beyond basics.
- **eDiscovery (Standard)** adds cases, legal holds that preserve content in place, search, and export.
- **eDiscovery (Premium)** adds custodian management, legal hold notifications, review sets, analytics such as near-duplicate detection and email threading, and predictive coding.

A hold **preserves**; it does not restrict access or classify. Deleted content covered by a hold moves to preservation storage rather than being removed.

---

## Data lifecycle and records management

**Retention policy** applies broadly at container scope (a site, all mailboxes) and is invisible to users. **Retention label** applies per item, can be applied by users or automatically, supports **disposition review**, and can declare content a record.

**Retention precedence**, in order:
1. Retention wins over deletion
2. The longest retention period wins
3. An explicit label beats an inherited policy
4. The shortest deletion period applies only when nothing requires retention

**Records management** adds a file plan, record declaration (locking content from edit or deletion), regulatory records (which cannot be unlocked), event-based retention, and disposition review with approver sign-off.

---

## Key terms

- **Insider Risk Management** - Purview solution scoring user behavior over time to detect data theft, leaks, and policy violations
- **Triggering event** - the event, often an HR termination date, that opens an insider risk detection window for a user
- **Sequence detection** - insider risk capability identifying multi-step exfiltration patterns rather than isolated actions
- **Username anonymization** - insider risk privacy control hiding user identities from analysts until a case is escalated
- **Communication Compliance** - Purview solution reviewing message content against policy with a reviewer remediation workflow
- **Information Barriers** - Purview capability preventing communication and discovery between defined user segments
- **Segment** - an Information Barriers grouping of users defined by a directory attribute
- **Purview Audit Premium** - the audit tier adding longer retention, configurable retention policies, and high-value events such as MailItemsAccessed
- **Audit retention policy** - configuration keeping selected audit record types longer than the default period
- **eDiscovery hold** - a legal hold preserving content in place without restricting access or altering classification
- **Review set** - the eDiscovery Premium working collection where collected content is analyzed and reviewed
- **Retention policy** - broad container-scoped retention that is invisible to end users
- **Retention label** - per-item retention supporting user application, auto-application, record declaration, and disposition review
- **Disposition review** - the approval step before content reaches the end of its retention period and is deleted
- **Regulatory record** - a record declaration that cannot be unlocked or removed even by an administrator

---

## Related

- [Notes 01: information protection](./01-information-protection.md)
- [Scenarios](../scenarios.md) - scenarios 5, 7, and 8
- [Compliance guides](../../../../resources/compliance-guides/)
- [GDPR](../../../../resources/compliance-guides/gdpr.md)
