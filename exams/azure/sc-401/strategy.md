---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 6 min
---

# SC-401 Study Strategy

## The one distinction that decides most questions

**Label = protection on the content. DLP = prevention at a boundary.**

| Requirement language | Answer |
|---|---|
| "must remain protected if the file leaves the organization" | Sensitivity label with encryption |
| "prevent users from sending / copying / printing / uploading" | DLP policy |
| "classify existing content without user action" | Auto-labeling policy |
| "keep for seven years even if the user deletes it" | Retention policy or label |
| "detect a user exfiltrating before they resign" | Insider Risk Management |

Read the requirement for whether the control must persist with the file or must stop an action. Distractors are built by offering the other one.

## Three near-equal domains

Unusually for a Microsoft exam, all three domains are 30-35%. Budget your study time evenly. Candidates commonly over-study labels because that material is the most familiar, and under-study insider risk, audit, and eDiscovery, which together are a third of the exam.

## Phase 1: Classification (week 1)

Everything consumes classification, so get it exact.

- **Built-in SIT** for standard patterns like credit cards. Confidence level and instance count both matter.
- **Custom SIT** when the pattern is yours. Supporting evidence and proximity windows reduce false positives.
- **EDM** when you have an authoritative list (customer IDs, patient numbers). Matches against hashed values of real records, so precision is far higher than a pattern.
- **Document fingerprinting** for forms and templates.
- **Trainable classifiers** for categories that cannot be expressed as a pattern at all, such as source code, resumes, or harassment.

Exam signal: "reduce false positives on an internal identifier format" points at EDM; "identify content by category, not pattern" points at a trainable classifier.

## Phase 2: Labels (week 2-3)

Know precisely:
- Label **priority**: higher in the list wins; a user can be required to justify a downgrade
- **Client-side auto-labeling** applies as the user works in Office apps and requires the label to be published to them; **service-side auto-labeling policies** apply at rest and in transit without user involvement and support **simulation**
- Encryption settings that break things: offline access limits, expiry, and permissions granted to groups that later change
- **Double Key Encryption** protects against Microsoft itself holding a usable key, at the cost of losing service-side capabilities such as search, eDiscovery, and co-authoring

## Phase 3: DLP (week 4)

The policy structure is consistent; the differences are per location.

- **Endpoint DLP** requires device onboarding, and its controls are device-specific: unallowed apps and browsers, removable storage, network share, print, clipboard.
- **Simulation and test mode** first, then policy tips, then enforce. An exam answer that enforces a broad DLP policy immediately is usually wrong.
- **Overrides with business justification** are how you keep a policy usable; the incident report is how you keep it auditable.
- **Adaptive Protection** raises DLP strictness automatically for users with an elevated insider risk level. This is the link between Domains 2 and 3 and is a favourite question.

## Phase 4: Risk and investigation (week 5-6)

- **Insider Risk Management** detects patterns of user behavior over time, usually anchored on a triggering event such as a departure date from HR data.
- **Communication Compliance** reviews message content against policy.
- **Information Barriers** prevent communication between segments.
- **Audit** proves what happened. Premium adds longer retention and high-value events such as MailItemsAccessed.
- **eDiscovery** preserves and exports for legal process. A hold preserves content in place; it does not classify or protect it.

Retention precedence is worth memorizing because it is directly testable: retention wins over deletion, the longest retention wins, an explicit label beats an inherited policy, and a shortest deletion applies only once nothing else requires retention.

## Common traps

| Trap | Reality |
|---|---|
| Using DLP where a label is required | DLP does not protect a file once it has legitimately left |
| Using a label where DLP is required | A label classifies; it does not by itself stop an upload |
| Forgetting device onboarding | Endpoint DLP does nothing on an unonboarded device |
| Enforcing without simulation | The exam expects simulation or test mode first |
| Confusing retention policy with retention label | Policies apply broadly at container scope; labels apply per item and support disposition review |
| Assuming Copilot respects classification | It respects **permissions**. Labels and DLP add controls, but oversharing must be fixed at the source |
| Treating eDiscovery hold as protection | It preserves; it does not restrict access |

## Exam day

- 100 minutes, roughly 40-60 items, sometimes with a case study section.
- Read for "persist with the file" versus "prevent the action" on every data protection question.
- Watch for license hints: several features require E5 or a compliance add-on.
- Nothing blank; there is no wrong-answer penalty.
- Free online renewal within six months of expiry.

## Related

- [Practice plan](./practice-plan.md)
- [Scenarios](./scenarios.md)
- [Fact sheet](./fact-sheet.md)
- [Study strategies](../../../resources/study-strategies.md)
