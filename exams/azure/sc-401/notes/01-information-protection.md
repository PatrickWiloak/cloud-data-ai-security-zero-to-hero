---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 12 min
---

# 01 - Information protection

**Domain 1: Implement information protection (30-35%)**

Know what the data is, then attach protection that travels with it.

---

## Classification building blocks

| Mechanism | Matches | Use when |
|---|---|---|
| **Built-in sensitive information type** | Known formats: credit card, passport, national ID | Standard regulated data |
| **Custom sensitive information type** | Your regex plus supporting evidence and proximity | Internal formats with distinguishing context |
| **Exact data match (EDM)** | Hashed values from an authoritative table | You hold the real list and need precision |
| **Document fingerprinting** | Structure of a known form or template | Standard forms, patent applications, contracts |
| **Trainable classifier** | A category of content, learned from examples | Source code, resumes, harassment, finance documents |

**Confidence level and instance count** shape a match. High confidence requires more corroborating evidence; instance count sets how many matches trigger the rule. Together they are the main false-positive controls for pattern-based types.

**EDM** works by hashing an uploaded table of real values and matching against the hashes, so the sensitive data itself never sits in the policy. It supports primary and secondary elements, so a match can require the ID and the surname within a proximity window.

**Trainable classifiers** come pre-trained for common categories, and custom classifiers are trained on 50 to 500 seed documents and then tested. Use them when the content cannot be expressed as a pattern.

---

## Sensitivity labels

A label carries classification and, optionally, protection.

### Scopes
- **Items**: files and emails, plus meetings
- **Groups and sites**: Teams, Microsoft 365 groups, SharePoint sites (privacy, external sharing, device access)
- **Schematized data assets**: database columns and data assets in the Purview data map

### Protection settings
- **Encryption**: permissions assigned to users, groups, or user-defined; usage rights (view, edit, print, copy, forward); expiry; offline access period
- **Content marking**: header, footer, watermark
- **Auto-labeling for Office apps** (client-side): applies as the user works
- **Site and group settings**: external sharing, unmanaged device access, privacy

### Label policies
Publish labels to users. Settings include the default label, requiring justification to downgrade, requiring a label on all content, and providing a help link. Multiple policies can apply; the one highest in the priority order wins for a given user.

### Behavior worth knowing
- **Priority**: labels lower in the list are more sensitive; a higher-sensitivity label overrides a lower one when both apply
- **Inheritance**: an email inherits the highest-sensitivity label of its attachments
- **Co-authoring** on encrypted documents requires the tenant setting to be enabled and supported clients
- **Encryption breaks service-side processing** if you go as far as Double Key Encryption: search, eDiscovery, DLP inspection, and co-authoring are lost, which is why DKE is reserved for the smallest set of genuinely most sensitive content

---

## Auto-labeling

Two mechanisms with different reach.

| | Client-side (in the label) | Service-side (auto-labeling policy) |
|---|---|---|
| Where it runs | Office apps as the user works | Service, at rest and in transit |
| Scope | Word, Excel, PowerPoint, Outlook | SharePoint, OneDrive, Exchange |
| Existing content | Only when opened and edited | Yes, scans content at rest |
| User involvement | Can recommend or apply automatically | None |
| Simulation | No | Yes, and it is the expected first step |

For an existing estate, the answer is a service-side auto-labeling policy run in **simulation** first.

---

## Discovery beyond Microsoft 365

- **Purview Information Protection scanner** discovers and labels files on on-premises file shares and SharePoint Server.
- **Purview data map** scans Azure data sources, on-premises databases, and other clouds, applying classification to cataloged assets.
- **DSPM (Data Security Posture Management)** reports where sensitive data lives, how it is protected, and where the gaps are.
- **DSPM for AI** narrows that to AI interactions: which sensitive data types Copilot and other AI applications touch, which users generate risky prompts, and whether policies cover them.

---

## Key terms

- **Sensitive information type** - a definition that identifies specific data patterns such as credit card or national identifier numbers
- **Exact data match** - classification that matches against hashed values from an authoritative uploaded table rather than a pattern
- **Document fingerprinting** - classification based on the structure of a known form or template
- **Trainable classifier** - a machine-learned classifier identifying categories of content that cannot be expressed as a pattern
- **Confidence level** - how much corroborating evidence a sensitive information type requires before declaring a match
- **Sensitivity label** - a Purview classification that can apply encryption, content marking, and access restriction traveling with the content
- **Label policy** - the policy that publishes labels to users and sets defaults, mandatory labeling, and downgrade justification
- **Label priority** - the ordering that determines which label wins when more than one could apply
- **Client-side auto-labeling** - label application in Office apps as the user works with a document
- **Service-side auto-labeling policy** - label application at rest and in transit by the service, supporting simulation mode
- **Simulation mode** - a dry run of an auto-labeling policy that reports what would be labeled without applying anything
- **Double Key Encryption** - encryption using a customer-held key alongside the Microsoft key, at the cost of service-side capabilities
- **Purview Information Protection scanner** - the on-premises component discovering and labeling files on file shares
- **DSPM for AI** - Purview reporting on sensitive data touched by AI interactions including Microsoft 365 Copilot

---

## Related

- [Notes 02: data loss prevention](./02-data-loss-prevention.md)
- [Scenarios](../scenarios.md) - scenarios 1, 2, 3, and 6
- [AI security](../../../../resources/ai-security/)
