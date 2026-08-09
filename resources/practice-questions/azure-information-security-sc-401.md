# Microsoft Information Security Administrator (SC-401) - Practice Questions

15 questions for SC-401 prep. SC-401 replaced SC-400. The recurring decision is whether a requirement needs protection that travels with the file (a sensitivity label) or prevention of an action at a boundary (a DLP policy).

> **Cert page:** [exams/azure/sc-401/](../../exams/azure/sc-401/)

---

### Question 1
**Scenario:** Contracts must remain unreadable to anyone outside the matter team even if emailed to a personal address or copied to a USB drive. Partners must be able to open them offline while traveling.

A. A DLP policy blocking egress of documents in the contracts library
B. A sensitivity label with encryption granting permissions to the matter team, with offline access configured, published through a label policy
C. SharePoint permissions restricted to the matter team
D. A retention label applied to the contracts library

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Only label-applied encryption travels with the file and continues to apply once the document has left the tenant. DLP prevents actions at a boundary but does not protect a file that legitimately left. SharePoint permissions do not follow a downloaded copy. Retention governs lifetime, not access.
</details>

---

### Question 2
**Scenario:** Patient IDs are eight digits. A pattern-based custom sensitive information type produces hundreds of false positives because invoice numbers share the format. The compliance team holds an authoritative CSV of 400,000 real patient IDs.

A. Raise the confidence level on the existing SIT
B. Increase the instance count threshold
C. Use exact data match with the authoritative table, adding supporting elements in a proximity window
D. Train a custom classifier on patient records

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** EDM matches hashed values from a real list, so ambiguity with other eight-digit numbers disappears. Raising confidence reduces recall without resolving the ambiguity. Increasing instance count misses single-record leaks. Trainable classifiers identify categories of content, not known values.
</details>

---

### Question 3
**Scenario:** Ten million existing documents in SharePoint and OneDrive must be classified without asking users to do it and without breaking access unexpectedly.

A. Mandatory labeling in the label policy
B. Client-side auto-labeling in the sensitivity label
C. A service-side auto-labeling policy run in simulation first, initially without encryption
D. Manual classification of the highest-risk libraries

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Service-side auto-labeling applies to content at rest without user involvement and supports simulation. Mandatory labeling forces users to act, contradicting the requirement. Client-side auto-labeling only applies as users open and edit documents, leaving untouched content unlabeled. Applying encryption on the first automated pass is what causes unexpected access breakage.
</details>

---

### Question 4
**Scenario:** Users copy customer data to personal OneDrive and Dropbox through the browser and onto USB drives. Windows endpoints are managed by Intune.

A. An Exchange-scoped DLP policy
B. Endpoint DLP with onboarded devices, unallowed browsers configured, and removable storage restrictions
C. A sensitivity label applied to the affected documents
D. Group Policy blocking all USB devices

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Browser uploads and USB copies are device-level actions, which only endpoint DLP sees, and only on onboarded devices. Configuring unallowed browsers is what turns a monitored upload into a blocked one. Exchange DLP does not see either action. A label classifies but does not stop the copy. Blanket USB blocking has no content awareness.
</details>

---

### Question 5
**Scenario:** A company repeatedly discovers weeks later that departing salespeople downloaded the customer list. It wants detection at the time, an investigation trail, and privacy controls on investigator access.

A. A DLP policy blocking downloads from the CRM
B. Insider Risk Management using the data theft by departing users template, the HR connector as the triggering event, sequence detection, and username anonymization
C. Audit log search after each departure
D. Communication Compliance policies on outbound email

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Insider risk scores behavior over time anchored on a triggering event from HR data, which is what produces detection before the departure rather than after. Anonymization satisfies the privacy requirement. DLP blocks specific actions but builds no behavioral case. Audit search is the reactive approach they already have. Communication Compliance reviews message content, not file exfiltration.
</details>

---

### Question 6
**Scenario:** Finance records are covered by a seven-year retention policy on the site. A document also carries a retention label set to delete after three years. A user deletes the document after one year. What happens?

A. The document is deleted immediately
B. The document is retained for seven years; retention wins over deletion and the longest retention period applies
C. The document is retained for three years, because the label is more specific
D. The deletion succeeds but is recoverable for 93 days

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Retention precedence is: retention beats deletion, the longest retention wins, an explicit label beats an inherited policy, and the shortest deletion applies only when nothing requires retention. Specificity does not override the retain-longest rule. The user's deletion moves the item to preservation rather than removing it.
</details>

---

### Question 7
**Scenario:** After an acquisition, the investment banking team and the trading team must not be able to communicate in Teams or discover each other in the directory, for regulatory reasons.

A. Communication Compliance policies reviewing messages between the two groups
B. Information Barriers with segments defined by department and block-mode policies
C. Conditional Access policies scoped to each group
D. Separate Entra tenants

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Information Barriers is the only feature that prevents communication and discovery between defined segments, and enforcement extends across Teams, SharePoint, and OneDrive. Communication Compliance reviews content after the fact rather than preventing contact. Conditional Access governs sign-in conditions. Separate tenants achieve it at enormous operational cost the scenario does not require.
</details>

---

### Question 8
**Scenario:** Before deploying Microsoft 365 Copilot, what is the correct first step to prevent employees surfacing documents they should not see?

A. Apply DLP policies for AI applications
B. Auto-label all sensitive content
C. Fix oversharing at the source, using site access reviews and removing organization-wide sharing links
D. Enable DSPM for AI reporting

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Copilot honors existing permissions, so pre-existing oversharing becomes immediate exposure. Labeling, DLP, and DSPM for AI are all part of the design, but they layer on top of a permissions clean-up rather than substituting for it. The exam tests the ordering.
</details>

---

### Question 9
**Scenario:** Which feature automatically applies stricter DLP enforcement only to users whose risky behavior has increased?

A. Conditional Access with sign-in risk
B. Adaptive Protection
C. A DLP policy scoped to a dynamic group
D. Insider Risk Management alerts

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Adaptive Protection links a user's insider risk level to enforcement strength, tightening DLP actions as risk rises without applying the strictest policy to everyone. Sign-in risk is an identity signal, not a data one. A dynamic group is static membership by attribute, not by behavior. Insider risk alerts inform investigators but do not themselves change enforcement.
</details>

---

### Question 10
**Scenario:** An organization needs protection applied to documents that are not yet classified, must not rely on users, and wants to see what would be affected before anything changes.

A. Mandatory labeling with a default label
B. A service-side auto-labeling policy in simulation mode
C. A DLP policy in test mode
D. The Purview Information Protection scanner

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Simulation mode is the auto-labeling feature that reports what would be labeled without applying anything. DLP test mode simulates a DLP policy, not labeling. A default label applies to new content and relies on the label policy reaching users. The scanner addresses on-premises file shares, which the scenario does not mention.
</details>

---

### Question 11
**Scenario:** What does Double Key Encryption give you, and what does it cost?

A. Two encryption layers with no functional cost
B. A customer-held key alongside the Microsoft key, at the cost of service-side capabilities including search, eDiscovery, and co-authoring
C. FIPS 140-2 Level 3 validation
D. Automatic key rotation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** DKE means Microsoft cannot decrypt the content, which is exactly why service-side processing stops working. That trade-off is why DKE is reserved for the smallest set of genuinely most sensitive content rather than applied broadly.
</details>

---

### Question 12
**Scenario:** Which audit capability is required to see which mailbox items a compromised account accessed?

A. Purview Audit Standard
B. Purview Audit Premium, which includes the MailItemsAccessed event
C. Exchange message trace
D. A Sentinel connector for Microsoft 365

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** MailItemsAccessed is one of the high-value events available with Audit Premium, and it is the specific record used in mailbox compromise investigations. Standard does not include it. Message trace shows mail flow, not item access. A Sentinel connector transports events but cannot create ones that were never generated.
</details>

---

### Question 13
**Scenario:** A retention requirement demands that records cannot be removed even by a global administrator, and that disposal requires reviewer approval.

A. A retention policy with a seven-year period
B. A retention label declaring content a regulatory record, with disposition review enabled
C. An eDiscovery hold
D. A sensitivity label with encryption

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Regulatory record declaration is what prevents removal even by administrators, and disposition review is what inserts the approval step. A retention policy prevents user deletion but does not declare a record. An eDiscovery hold preserves for legal process without a disposition workflow. A sensitivity label governs access, not lifetime.
</details>

---

### Question 14
**Scenario:** An organization wants to know which sensitive data types employees' AI interactions are actually touching.

A. DLP for AI applications
B. Purview DSPM for AI
C. Communication Compliance
D. Insider Risk Management

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** DSPM for AI is the reporting and visibility capability for sensitive data flowing through AI interactions, including Copilot. DLP for AI is the enforcement side of the same problem. Communication Compliance reviews messages. Insider risk scores user behavior.
</details>

---

### Question 15
**Scenario:** Which combination is required so that endpoint DLP can block a file upload through a non-Edge browser?

A. A DLP policy with the Devices location selected
B. A DLP policy with the Devices location selected, the device onboarded, and the browser listed as unallowed
C. Intune compliance policies
D. A sensitivity label with encryption

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** All three are needed. Selecting the Devices location without onboarding enforces nothing. Onboarding without the unallowed-browser setting means uploads through a non-policy-aware browser are monitored rather than blocked. Compliance policies and labels address different problems.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready. Confirm you can state the retention precedence order from memory.
- **10-12 correct (65-80%):** Re-read the label versus DLP distinction and the insider risk material, which candidates commonly under-study.
- **Below 10:** Work the [scenarios](../../exams/azure/sc-401/scenarios.md) and build the labs in the [practice plan](../../exams/azure/sc-401/practice-plan.md).

All three SC-401 domains are 30-35%, so there is no domain you can afford to skip.
