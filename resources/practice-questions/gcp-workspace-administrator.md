---
last-updated: 2026-08-09
difficulty: intermediate
---

# Google Cloud Professional Google Workspace Administrator - Practice Questions

15 questions for the Workspace Administrator exam, weighted toward organizational units and users (25%) and Workspace applications (25%), then access and authentication (20%), content management (15%), and mail routing (15%).

> **Cert page:** [exams/gcp/workspace-administrator/](../../exams/gcp/workspace-administrator/)

---

### Question 1
**Scenario:** A setting must apply to the marketing department but not the rest of the organization.

A. Apply it at the top-level organization
B. Apply it to the marketing organizational unit, or use a configuration group for cross-OU targeting
C. Apply it per user manually
D. It is not possible

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Settings inherit down the OU tree and can be overridden at a child OU. Groups add a second targeting axis for people who span OUs, and group-based settings take precedence over OU settings for most services, which matters when both are in play.
</details>

---

### Question 2
**Scenario:** Users must sign in with an existing corporate identity provider.

A. Separate Workspace passwords
B. Configure SAML SSO with the third-party IdP, keeping a super admin account excluded from SSO for break-glass access
C. Sync passwords manually
D. Use Google as the only IdP

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SSO delegates authentication to the IdP so its MFA and lifecycle policies apply. The break-glass detail matters in practice: if the IdP becomes unavailable and every admin authenticates through it, nobody can log in to fix the configuration.
</details>

---

### Question 3
**Scenario:** Users on unmanaged devices should not download sensitive Drive files.

A. Context-Aware Access policies evaluating device and location attributes
B. Disable Drive entirely
C. Change file ownership
D. A retention policy

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Context-Aware Access conditions access on signals such as device management state, OS version, IP, and location, per application. This is the zero trust control in Workspace, and it is enforced at access time rather than relying on user behavior.
</details>

---

### Question 4
**Scenario:** Email containing credit card numbers must not leave the organization.

A. A Gmail filter
B. A DLP rule for Gmail with a predefined detector, blocking or quarantining external sends
C. A retention policy
D. Vault

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** DLP rules scan content against detectors and take an action such as block, quarantine for admin review, or warn. Filters are per-user conveniences without administrative enforcement, and Vault is retention and eDiscovery rather than prevention.
</details>

---

### Question 5
**Scenario:** Email must be retained for 7 years for legal reasons, even if users delete it.

A. Google Vault retention rules
B. Ask users not to delete
C. Gmail labels
D. Drive backup

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Vault retention preserves content beyond user deletion and holds override retention entirely for matters under litigation. This is why a legal hold outranks both retention expiry and user action, which is a distinction the exam tests.
</details>

---

### Question 6
**Scenario:** Inbound mail must be routed through a third-party security gateway before delivery.

A. Change the MX records to the gateway and configure inbound gateway settings in Workspace so SPF checks and spam handling account for it
B. Change nothing
C. Use a Gmail filter
D. Disable spam filtering

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Without registering the gateway as an inbound gateway, every message appears to come from the gateway's IP, which breaks SPF evaluation and sender reputation. That setting tells Gmail to look past the gateway for the true originating IP.
</details>

---

### Question 7
**Scenario:** Which DNS records reduce spoofing of the organization's domain?

A. MX only
B. SPF, DKIM, and DMARC, with DMARC moving from monitoring to quarantine or reject as confidence grows
C. A records
D. CNAME

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SPF authorizes sending IPs, DKIM signs messages cryptographically, and DMARC tells receivers what to do when alignment fails and where to send reports. Starting DMARC at `p=none` to collect reports before enforcing is what prevents blocking legitimate mail from forgotten senders.
</details>

---

### Question 8
**Scenario:** A departing employee's data must be preserved and their license reclaimed.

A. Delete the account immediately
B. Transfer data ownership, place a Vault hold if needed, then suspend or convert to an archived user before deleting
C. Suspend forever
D. Share the password

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Deleting first orphans Drive files and loses mail, and the recovery window is limited. The offboarding order matters: hold, transfer, then remove. Archived User licenses retain the data at lower cost when retention is required beyond employment.
</details>

---

### Question 9
**Scenario:** Admin privileges should be limited to what a helpdesk role needs.

A. Grant super admin
B. Create a custom admin role with only the required privileges, scoped to an OU where possible
C. Share one admin account
D. Grant no access

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Custom roles with delegated administration limit blast radius, and OU scoping restricts which users an admin can affect. Shared accounts destroy attribution in the audit log, which is usually the first thing an incident investigation needs.
</details>

---

### Question 10
**Scenario:** External sharing of Drive files must be restricted to allowlisted domains.

A. Turn off sharing entirely
B. Configure Drive sharing settings with a domain allowlist, and set default link sharing to restricted
C. Ask users to be careful
D. Use DLP only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Allowlisting permits collaboration with named partners while blocking everything else, and setting the default link scope to restricted prevents the accidental "anyone with the link" share. DLP complements this by inspecting content, but the sharing setting is the structural control.
</details>

---

### Question 11
**Scenario:** An investigation needs to find who shared a specific document externally.

A. The security investigation tool with Drive audit logs
B. Ask the user
C. Gmail search
D. The Drive interface

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The investigation tool queries audit log data across services with conditions and supports bulk remediation actions such as removing sharing permissions. Manually inspecting a file shows current state, not the history of who changed it and when.
</details>

---

### Question 12
**Scenario:** MFA should be enforced with phishing-resistant factors for administrators.

A. SMS codes
B. Enforce 2-Step Verification with security keys or passkeys for admin accounts
C. Password complexity only
D. Optional 2SV

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hardware security keys and passkeys are origin-bound, so a phishing site cannot relay the assertion. SMS and one-time codes can be relayed in real time by an attacker-controlled proxy, which is exactly how modern phishing kits defeat them.
</details>

---

### Question 13
**Scenario:** Mobile devices accessing corporate mail must be managed.

A. Do nothing
B. Enable mobile device management with the appropriate policy level, requiring screen lock, encryption, and remote wipe capability
C. Block mobile access
D. Trust the users

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Basic mobile management covers account-level controls with minimal user friction; advanced management enables app management and stronger policy at the cost of enrollment. Selective account wipe is the middle ground that removes corporate data without touching personal content.
</details>

---

### Question 14
**Scenario:** A third-party application requests OAuth access to Workspace data.

A. Allow all apps
B. Use API access controls to block unconfigured third-party apps and allowlist specific client IDs and scopes after review
C. Block everything permanently
D. Let users decide individually

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Unrestricted OAuth grants are a real exfiltration path because a user can authorize an app to read all their mail in two clicks. App access control with trusted-app allowlisting moves that decision to an administrator who can review the requested scopes.
</details>

---

### Question 15
**Scenario:** New users must be provisioned automatically from the HR system.

A. Manual creation
B. Directory sync from the identity source (GCDS for LDAP or Active Directory, or SCIM from a cloud IdP), driving create, update, and suspend
C. A shared spreadsheet
D. Self-registration

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Automated provisioning matters most for deprovisioning: manual processes reliably leave active accounts for people who left months ago. Driving the lifecycle from the authoritative HR or IdP source makes suspension automatic on the day of departure.
</details>

---

## Where to go deeper

- [Workspace Administrator cert page](../../exams/gcp/workspace-administrator/) - notes, practice plan, strategy
- [MS-900 practice questions](./azure-m365-fundamentals-ms-900.md) - the Microsoft 365 counterpart
- [SC-300 practice questions](./azure-identity-access-sc-300.md) - identity administration at depth
- [IAM topic index](../../topics/iam.md) - identity across the repo
- **[📖 Google Cloud certification](https://cloud.google.com/learn/certification)** - official exam guides
