---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 11 min
---

# SC-401 High-Yield Scenarios

---

## Scenario 1: Protection that survives leaving the tenant

**Scenario**: A law firm's contracts must remain unreadable to anyone outside the matter team, even if a document is emailed to a personal address or copied to a USB drive. Partners must be able to open them offline while travelling.

**Solution Pattern**:
- **Sensitivity label with encryption**, granting permissions to the matter team security group
- Configure **offline access** for an appropriate number of days so travelling partners are not blocked
- Publish through a **label policy** scoped to the relevant users, with mandatory labeling for the contracts library
- Add a **DLP policy** as a second layer to warn or block on egress, but recognize it is not what satisfies the core requirement

**Common Distractors**:
- DLP alone (does not protect the file once it has legitimately left)
- SharePoint permissions alone (do not travel with a downloaded copy)
- Retention labels (govern lifetime, not access)

**Key Takeaway**: "Must remain protected outside the organization" is always a sensitivity label with encryption. DLP is the complement, not the answer.

---

## Scenario 2: Precise matching of an internal identifier

**Scenario**: A hospital's patient IDs are eight digits. A DLP policy using a custom pattern generates hundreds of false positives daily because invoice numbers, part numbers, and dates match the same shape. The compliance team has an authoritative CSV of the 400,000 real patient IDs.

**Solution Pattern**:
- **Exact data match (EDM)** using the authoritative list: define a schema, hash and upload the sensitive information source table, and reference it in a sensitive information type
- Combine the primary element with supporting elements (surname, date of birth) in the same proximity window to raise precision further
- Rebuild the DLP rule against the EDM-based SIT
- Refresh the uploaded table on a schedule as the record set changes

**Common Distractors**:
- Raising the confidence level of the pattern-based SIT (reduces recall without fixing the fundamental ambiguity)
- Increasing the instance count threshold (misses single-record leaks)
- A trainable classifier (built for categories of content, not for matching known values)

**Key Takeaway**: When you hold the authoritative list of real values, EDM is the precise answer. Trainable classifiers are for categories you cannot express as values or patterns at all.

---

## Scenario 3: Classifying a large existing estate

**Scenario**: Ten million documents already sit in SharePoint and OneDrive, unlabeled. Leadership wants them classified without asking users to do it and without unexpected access breakage.

**Solution Pattern**:
- **Service-side auto-labeling policy** targeting SharePoint and OneDrive, which applies at rest without user involvement
- Run in **simulation mode** first and analyze the matched items before enabling
- Start with a narrow, high-confidence condition and widen iteratively
- Avoid attaching encryption to the first auto-applied label; classify first, protect once the match quality is proven
- Client-side auto-labeling covers documents as users work on them going forward

**Common Distractors**:
- Mandatory labeling in a label policy (forces users to label, contradicting the requirement)
- Client-side auto-labeling only (applies as users open and edit, so untouched content stays unlabeled)
- Enabling immediately without simulation (an encrypting label applied wrongly at this scale is very hard to unwind)

**Key Takeaway**: Existing content at rest means a service-side auto-labeling policy, and the exam expects simulation before enforcement. Separating classification from encryption on the first pass is the safe design.

---

## Scenario 4: Blocking exfiltration to personal cloud storage

**Scenario**: Users copy files containing customer data to personal OneDrive and Dropbox through the browser, and onto USB drives. The organization runs Windows endpoints managed by Intune.

**Solution Pattern**:
- **Endpoint DLP** with the devices **onboarded** through Intune
- Configure **unallowed browsers** so uploads through non-Edge browsers are blocked rather than merely monitored
- Set service domain allow and block lists so approved destinations still work
- Configure **removable storage** and **network share** restrictions
- Use **policy tips with business justification override** initially, then tighten to block
- Pair with **Defender for Cloud Apps** session policies for unmanaged devices, where endpoint DLP cannot reach

**Common Distractors**:
- Exchange-only DLP (does not see browser uploads or USB copies)
- Blocking USB through Group Policy alone (no content awareness, blocks everything or nothing)
- A sensitivity label (classifies, but does not stop the copy action)

**Key Takeaway**: Device-level actions need endpoint DLP with onboarded devices. Unmanaged devices need a different control, typically Defender for Cloud Apps session policies.

---

## Scenario 5: The departing employee

**Scenario**: A company has repeatedly discovered, weeks after the fact, that departing salespeople downloaded the customer list before resigning. They want detection at the time, with an investigation trail, and legal requires investigator access to be privacy-controlled.

**Solution Pattern**:
- **Insider Risk Management** policy from the **data theft by departing users** template
- Connect the **HR connector** so the termination date becomes the triggering event, opening a detection window before and after
- Enable relevant indicators: downloads from SharePoint, copying to USB, uploads to personal cloud, printing
- Use **sequence detection** to catch download-then-exfiltrate patterns rather than single events
- Enable **username anonymization** so analysts triage without seeing identities until a case is escalated
- Configure **Adaptive Protection** so a user at elevated risk automatically receives stricter DLP enforcement
- Escalate confirmed cases to eDiscovery for preservation

**Common Distractors**:
- A DLP policy alone (blocks specific actions but does not build a behavioral case or use HR context)
- Audit log search after the fact (reactive, which is what they already do)
- Communication Compliance (reviews message content, not file exfiltration)

**Key Takeaway**: Insider risk is about behavior over time anchored on a triggering event from HR data. Adaptive Protection is the mechanism connecting that risk level to enforcement.

---

## Scenario 6: Preparing for a Copilot rollout

**Scenario**: Before deploying Microsoft 365 Copilot, legal wants assurance that employees cannot use it to surface documents they should not see, and wants visibility into what sensitive data Copilot interactions touch.

**Solution Pattern**:
- Fix **oversharing first**: Copilot honors existing permissions, so run SharePoint Advanced Management site access reviews, restrict organization-wide sharing links, and remove "Everyone except external users" grants
- **Auto-label** sensitive content so classification exists to enforce against
- **DLP for Microsoft 365 Copilot** to prevent labeled content being processed or summarized where policy forbids it
- **DSPM for AI** to report which sensitive data types AI interactions actually touch, and to surface risky prompts
- **Purview Audit** for the AI interaction record
- Communication and training so users know interactions are auditable

**Common Distractors**:
- Blocking Copilot from sites containing sensitive data (defeats the deployment)
- Relying on Copilot's own filtering (it enforces permissions, it does not fix them)
- Labeling after rollout (exposure occurs from day one)

**Key Takeaway**: An AI assistant amplifies existing permission problems. The correct sequence is fix permissions, then classify, then apply DLP, then monitor with DSPM for AI.

---

## Scenario 7: Retention conflict

**Scenario**: Finance records are covered by a seven-year retention policy on the SharePoint site. An individual document also carries a retention label set to delete after three years. A user deletes the document after one year. What happens, and how should the design change?

**Solution Pattern**:
- The document is **retained for seven years**. Retention wins over deletion, and the longest retention period wins
- The user's deletion moves it to the preservation hold library rather than removing it
- If the three-year deletion is genuinely required for that document type, the site-level policy must be scoped to exclude it, because a label cannot shorten a broader retention obligation
- For records that need formal disposition, use **records management** with disposition review rather than automatic deletion

**Common Distractors**:
- Assuming the more specific label wins (specificity does not override the retain-longest rule)
- Assuming user deletion succeeds (it does not while retention applies)
- Adding an eDiscovery hold to "make sure" (holds preserve but do not resolve the policy conflict)

**Key Takeaway**: Retention precedence: retention beats deletion, longest retention wins, explicit beats inherited, shortest deletion applies only when nothing requires retention. This is directly testable.

---

## Scenario 8: Separating two business units

**Scenario**: After acquiring a competitor, the merged company must prevent the investment banking team and the trading team from communicating in Teams or discovering each other in the directory, for regulatory reasons.

**Solution Pattern**:
- **Information Barriers** with segments defined by an Entra attribute such as department
- Barrier policies in **block mode** between the two segments
- Verify the effect on Teams, SharePoint, and OneDrive, since barrier enforcement extends across them
- Choose between **explicit block** and **allow-only** modes based on how many segments must be isolated

**Common Distractors**:
- Communication Compliance (reviews content after the fact, does not prevent contact)
- Conditional Access (governs sign-in conditions, not who can message whom)
- Separate tenants (achieves it, but at enormous operational cost, and the scenario does not require it)

**Key Takeaway**: Information Barriers is the only feature that prevents communication and discovery between defined groups. Communication Compliance reviews; barriers prevent.

---

## Related

- [Practice plan](./practice-plan.md)
- [Strategy](./strategy.md)
- [Notes](./notes/)
- [Compliance guides](../../../resources/compliance-guides/)
- [Practice questions](../../../resources/practice-questions/azure-information-security-sc-401.md)
