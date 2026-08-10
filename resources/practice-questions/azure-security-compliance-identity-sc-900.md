---
last-updated: 2026-08-09
difficulty: beginner
---

# Microsoft Security, Compliance, and Identity Fundamentals (SC-900) - Practice Questions

15 questions for SC-900 prep, weighted toward Microsoft security solutions (35-40%), identity and access management (25-30%), and compliance solutions (25-30%).

SC-900 tests whether you can name the right capability for a requirement, not whether you can configure it.

> **Cert page:** [exams/azure/sc-900/](../../exams/azure/sc-900/)

---

### Question 1
**Scenario:** Which principle states that no request is trusted based on network location alone?

A. Defense in depth
B. Zero trust
C. Least privilege
D. Separation of duties

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Zero trust's guiding principles are verify explicitly, use least privilege access, and assume breach. The consequence is that being inside the corporate network grants nothing by itself. Defense in depth and least privilege are complementary ideas, not the same one.
</details>

---

### Question 2
**Scenario:** A user proves identity with a password plus a code from an authenticator app.

A. Single sign-on
B. Multi-factor authentication
C. Federation
D. Conditional Access

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** MFA combines factors from different categories: something you know, something you have, and something you are. SSO means authenticating once for multiple applications. Federation is trust between identity systems. Conditional Access is the policy engine that can require MFA under given conditions.
</details>

---

### Question 3
**Scenario:** Access to a finance app should require MFA only when the sign-in comes from outside the corporate network.

A. A Conditional Access policy with a location condition and an MFA grant control
B. Turning on per-user MFA for everyone
C. Privileged Identity Management
D. A sensitivity label

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Conditional Access evaluates signals (user, device, location, application, risk) and applies controls, which is what makes the requirement conditional. Per-user MFA is unconditional. PIM handles just-in-time elevation of privileged roles, and labels classify data.
</details>

---

### Question 4
**Scenario:** An administrator should hold the Global Administrator role only for approved windows, with justification and approval.

A. Conditional Access
B. Microsoft Entra Privileged Identity Management with just-in-time activation
C. Access reviews
D. Entitlement management

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PIM makes a role assignment eligible rather than active, so it must be activated with justification, optional approval, and a time limit. Access reviews periodically confirm whether existing access is still needed, which is a different and complementary control.
</details>

---

### Question 5
**Scenario:** Which service is Microsoft's cloud identity provider?

A. Active Directory Domain Services
B. Microsoft Entra ID
C. Microsoft Defender for Identity
D. Microsoft Purview

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Entra ID (formerly Azure AD) is the cloud identity and access management service. AD DS is the on-premises directory using Kerberos and LDAP. Defender for Identity monitors AD DS for attacks, and Purview handles data governance and compliance.
</details>

---

### Question 6
**Scenario:** Which capability lets an external partner sign in to your resources using their own organization's credentials?

A. Entra External ID (B2B collaboration)
B. Managed identities
C. Service principals
D. Passwordless sign-in

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** B2B collaboration invites guests who authenticate at their home tenant, so you never manage their credentials or their offboarding. Managed identities are for Azure resources authenticating to services, and service principals represent applications.
</details>

---

### Question 7
**Scenario:** A workload in Azure must call Azure Storage without any stored credential.

A. A managed identity granted an RBAC role on the storage account
B. A shared access signature in the app config
C. The storage account key
D. A user account with a password

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Managed identities are created and rotated by the platform, so there is no secret in code or configuration to leak. Both the account key and a long-lived SAS are secrets you must store, rotate, and hope nobody commits to git.
</details>

---

### Question 8
**Scenario:** Which service provides cloud security posture management and workload protection across Azure, AWS, and GCP?

A. Microsoft Sentinel
B. Microsoft Defender for Cloud
C. Microsoft Purview
D. Azure Monitor

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Defender for Cloud combines CSPM (secure score, recommendations, regulatory compliance) with CWPP (Defender plans for servers, containers, storage, databases) and is multicloud. Sentinel is the SIEM and SOAR. Purview is data governance. Azure Monitor is telemetry.
</details>

---

### Question 9
**Scenario:** A security team needs to collect logs from many sources, correlate them, and run automated response playbooks.

A. Microsoft Sentinel
B. Defender for Cloud
C. Entra ID Protection
D. Compliance Manager

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Sentinel is the cloud-native SIEM and SOAR: data connectors, analytics rules, incidents, hunting, and Logic Apps playbooks for automation. Defender for Cloud protects workloads and feeds Sentinel rather than replacing it.
</details>

---

### Question 10
**Scenario:** Which Microsoft 365 capability classifies a document as Confidential and encrypts it so protection travels with the file?

A. Data loss prevention
B. Sensitivity labels
C. Retention policies
D. eDiscovery

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A sensitivity label can apply encryption and rights so the protection persists even when the file leaves the tenant. DLP prevents actions at a boundary such as sending or copying. Retention governs how long content is kept, and eDiscovery finds and preserves content for legal matters.
</details>

---

### Question 11
**Scenario:** An organization must stop credit card numbers from being emailed externally.

A. A sensitivity label
B. A DLP policy with the credit card sensitive information type, blocking external sharing
C. A retention label
D. Insider Risk Management

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** DLP detects sensitive information types in content and enforces an action at the moment of sharing, with policy tips and optional user override. Labels classify but do not by themselves block a send. Insider risk detects patterns of risky user behavior over time.
</details>

---

### Question 12
**Scenario:** Which tool gives a score and improvement actions mapped to regulations such as GDPR and ISO 27001?

A. Secure Score
B. Compliance Manager
C. Service Trust Portal
D. Azure Advisor

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Compliance Manager tracks improvement actions against regulatory templates and produces a compliance score. Secure Score measures security posture rather than regulatory alignment. The Service Trust Portal publishes Microsoft's own audit reports and certifications.
</details>

---

### Question 13
**Scenario:** Under the shared responsibility model in SaaS, who is responsible for the data and for identity management?

A. Microsoft entirely
B. The customer, always, for data and for identities and accounts
C. Neither party
D. It varies by month

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Data, devices, accounts, and identities remain the customer's responsibility in every service model. What shifts between IaaS, PaaS, and SaaS is the infrastructure and application layers. This is the single most repeated concept across all Microsoft fundamentals exams.
</details>

---

### Question 14
**Scenario:** Sign-ins from an anonymous IP address should be flagged as risky and challenged automatically.

A. Microsoft Entra ID Protection risk policies, combined with Conditional Access
B. A firewall rule
C. Purview auditing
D. A retention policy

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** ID Protection calculates sign-in risk and user risk from signals such as impossible travel, anonymous IPs, and leaked credentials, and Conditional Access consumes that risk level as a condition to require MFA or a password change. Auditing records events but takes no action.
</details>

---

### Question 15
**Scenario:** Which describes the difference between authentication and authorization?

A. They are the same
B. Authentication proves who you are; authorization decides what you may do
C. Authorization happens first
D. Authentication applies only to administrators

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** AuthN establishes identity, AuthZ evaluates permissions for that identity, and it happens after. Keeping the two distinct is what makes it obvious that MFA (an authentication strength control) does nothing about over-permissioned accounts, which is an authorization problem.
</details>

---

## Where to go deeper

- [SC-900 cert page](../../exams/azure/sc-900/) - notes, practice plan, strategy
- [SC-300 practice questions](./azure-identity-access-sc-300.md) - identity at administrator depth
- [SC-200 practice questions](./azure-security-operations-sc-200.md) - the SOC analyst path
- [Shared responsibility model](../../learn/concepts/shared-responsibility-model.md) - the concept behind question 13
- **[📖 SC-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900)** - official skills outline
