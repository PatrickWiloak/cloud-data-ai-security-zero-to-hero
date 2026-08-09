# Microsoft Identity and Access Administrator (SC-300) - Practice Questions

15 questions for SC-300 prep. Watch for the licence tier stated in each scenario: it decides several of these outright.

> **Cert page:** [exams/azure/sc-300/](../../exams/azure/sc-300/)

---

### Question 1
**Scenario:** A consultancy onboards 200 contractors per quarter. Each needs specific applications, a SharePoint site, and a group. Access must be self-requested, approved by the engaging partner, and expire after 90 days. The tenant has Entra ID Governance licensing.

A. A dynamic group with a contractor attribute rule
B. An entitlement management access package with an approval policy and 90-day expiry
C. PIM eligible assignments
D. Manual assignment with calendar reminders

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Access packages are the only feature bundling heterogeneous resources behind a request, approval, and expiry workflow. Dynamic groups have no request or approval and no expiry. PIM governs privileged role activation, not resource entitlement. Manual assignment does not scale to 200 per quarter.
</details>

---

### Question 2
**Scenario:** Administrators must use phishing-resistant MFA for the Azure portal. Standard users continue with Microsoft Authenticator. What should be configured?

A. A Conditional Access policy requiring MFA for the administrator roles
B. A custom authentication strength containing FIDO2 and Windows Hello for Business, required by a Conditional Access policy scoped to administrator roles and the Azure Management app
C. Removal of SMS from the tenant authentication methods policy
D. Per-user MFA settings for the administrators

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** "Phishing-resistant" maps to authentication strengths, which name the specific permitted methods. A generic MFA requirement does not distinguish method strength. Removing SMS tenant-wide affects all users, not just administrators. Per-user MFA is legacy and cannot express method strength.
</details>

---

### Question 3
**Scenario:** Users synchronized from on-premises AD report that self-service password reset appears to succeed but their on-premises password is unchanged. What is missing?

A. SSPR is not enabled for their group
B. Password writeback is not enabled in Entra Connect
C. The authentication methods policy blocks their method
D. They have not completed combined registration

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Without password writeback, SSPR changes only the cloud password for a synced user. The symptom is exactly this: the portal reports success and the on-premises directory is untouched. The other options would prevent the reset from appearing to succeed at all.
</details>

---

### Question 4
**Scenario:** A nightly job must read all users' calendars with no signed-in user. `Calendars.Read` was granted as a delegated permission and the job returns 403.

A. Grant a higher delegated permission
B. Grant `Calendars.Read` as an application permission with admin consent, and use client credentials or a managed identity
C. Assign the Global Reader role to the service principal
D. Create a service account with a password

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Delegated permissions require a signed-in user and grant the intersection of app and user rights. A daemon has no user, so application permissions with admin consent are required. Entra roles are not Graph permissions. A service account with a password is the pattern managed identities exist to replace.
</details>

---

### Question 5
**Scenario:** An audit finds guests can enumerate the whole directory. B2B collaboration must continue. What fixes it?

A. A Conditional Access policy targeting guest users
B. Set external user permissions to the most restrictive option, restrict who can invite, and add an access review on guests
C. Convert guests to member accounts
D. Block all B2B collaboration

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Directory enumeration by guests is governed by external collaboration settings, not Conditional Access, which controls sign-in conditions rather than directory read permissions. Converting guests to members grants more directory access, not less. Blocking B2B fails the requirement.
</details>

---

### Question 6
**Scenario:** A GitHub Actions workflow deploys to Azure using a service principal client secret that expired over a weekend. Security also objects to a long-lived credential with subscription Contributor rights.

A. Automate secret rotation
B. Store the secret in Key Vault
C. Configure workload identity federation with the subject scoped to the specific repository and environment, remove the secret, and narrow the RBAC scope
D. Use a user-assigned managed identity on the GitHub runner

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Federation removes the stored credential entirely by trusting GitHub's OIDC issuer. Scoping the federated credential subject to a branch or environment is what makes it safer than the secret it replaces. Rotation still leaves a long-lived credential. Key Vault still requires a credential to reach Key Vault. GitHub-hosted runners are not Azure resources, so a managed identity alone does not apply.
</details>

---

### Question 7
**Scenario:** An administrator plans a Conditional Access policy requiring compliant devices for all users and all cloud apps. Intune enrolment is at 60%. What is the correct deployment approach?

A. Enable it for all users immediately
B. Enable security defaults instead
C. Deploy in report-only mode, review the workbook, exclude two break-glass accounts, and roll out in stages
D. Exclude the Global Administrator role

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Report-only mode, break-glass exclusions, and staged rollout are expected in every Conditional Access answer. Immediate enforcement locks out 40% of the organization. Security defaults are all-or-nothing and disable Conditional Access. A role exclusion is not a break-glass account; break-glass means specific excluded cloud-only user accounts with monitoring.
</details>

---

### Question 8
**Scenario:** Twelve engineers hold permanent Global Administrator. Audit requires no standing privilege, approval before elevation, recorded justification, and quarterly recertification of eligibility. The tenant has Entra ID P2.

A. Conditional Access requiring MFA for administrators
B. Convert to PIM eligible assignments with approval and justification, enable PIM alerts, and configure a quarterly PIM access review
C. An entitlement management access package containing the role
D. Remove the role and re-add it when needed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** No standing privilege plus approval plus justification is PIM. Conditional Access adds a sign-in condition while leaving standing privilege in place. Access packages govern resource entitlement, not directory role activation. Manual add and remove has no approval or audit trail.
</details>

---

### Question 9
**Scenario:** Which role can reset the password of a user who holds the Application Administrator role?

A. User Administrator
B. Authentication Administrator
C. Privileged Authentication Administrator
D. Helpdesk Administrator

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Only Privileged Authentication Administrator can manage authentication methods and credentials for users holding privileged roles. User Administrator, Authentication Administrator, and Helpdesk Administrator are all blocked from acting on privileged-role holders, which is a deliberate protection and a frequent exam point.
</details>

---

### Question 10
**Scenario:** A tenant has Entra ID P1 only. Which requirement cannot be met without a licence upgrade?

A. Conditional Access requiring MFA
B. Self-service password reset with writeback
C. Risk-based Conditional Access using sign-in risk
D. Application Proxy for an on-premises web app

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Sign-in risk and user risk conditions come from Entra ID Protection, which requires P2. Conditional Access itself, SSPR with writeback, and Application Proxy are all P1 capabilities. Licence tier is the single most common decider on this exam.
</details>

---

### Question 11
**Scenario:** What is the difference between an application registration and an enterprise application?

A. They are two names for the same object
B. The registration is the global definition in the home tenant; the enterprise application is the service principal instance in each tenant that consents to it
C. The registration is for single-tenant apps and the enterprise application is for multi-tenant apps
D. The enterprise application is the older term

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Registering an app creates both objects in your tenant. Consenting to a third-party multi-tenant app creates only a service principal locally, because the registration lives in the vendor's tenant. You configure API permissions and credentials on the registration, and SSO, user assignment, and provisioning on the enterprise application.
</details>

---

### Question 12
**Scenario:** A company must ensure that a specific group of users can only sign in from managed devices located in their home country, and that a stolen refresh token cannot be replayed elsewhere.

A. A named location condition alone
B. Conditional Access requiring a compliant device plus a location condition, with token protection as a session control
C. An IP allowlist on the application
D. Sign-in frequency set to one hour

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Device compliance and location are Conditional Access conditions and grant controls. Token protection binds a refresh token to the device it was issued to, which addresses replay. An IP allowlist alone does not verify the device. Sign-in frequency shortens the window but does not prevent replay within it.
</details>

---

### Question 13
**Scenario:** Which hybrid identity method allows Entra ID Protection to detect leaked credentials?

A. Federation with AD FS
B. Pass-through authentication
C. Password hash sync
D. Any of them, since detection is cloud-side

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Leaked credential detection compares synced password hashes against credentials found in breach corpora, so it requires password hash sync. PTA and federation store no hash in Entra ID, so the detection cannot run. This is a common reason to enable password hash sync alongside another method.
</details>

---

### Question 14
**Scenario:** A regional helpdesk must reset passwords only for users in its own region. What should be configured?

A. A custom role scoped to a security group
B. An administrative unit containing the regional users, with the Helpdesk Administrator role assigned over it
C. A Conditional Access policy restricting the helpdesk
D. A dynamic group with the helpdesk as owners

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Administrative units scope a role assignment to a subset of the directory, which is exactly this delegation pattern. Roles are assigned over an administrative unit, not inside it. Conditional Access governs sign-in, not administrative scope. Group ownership does not confer password reset rights.
</details>

---

### Question 15
**Scenario:** An access review must remove access automatically from anyone whose reviewer does not respond. What setting achieves this?

A. Auto-apply results, with "If reviewers don't respond" set to Remove access
B. Auto-apply results, with "If reviewers don't respond" set to No change
C. Recurring reviews with a manual apply step
D. A lifecycle workflow triggered on the review end date

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Both settings are required: auto-apply enacts decisions without an administrator, and the no-response behavior determines what happens to unreviewed access. "No change" leaves access in place, which is the opposite of the requirement. A manual apply step contradicts "automatically". Lifecycle workflows handle joiner, mover, and leaver events, not review outcomes.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready. Spend remaining time in a trial tenant building Conditional Access policies.
- **10-12 correct (65-80%):** Review the licence boundary table and the feature-boundary table in the [strategy notes](../../exams/azure/sc-300/strategy.md).
- **Below 10:** Work through the domain notes, then build the labs listed in the [practice plan](../../exams/azure/sc-300/practice-plan.md).

Two habits carry this exam: read the licence tier first, and know precisely which of Conditional Access, PIM, entitlement management, and access reviews solves the stated problem.
