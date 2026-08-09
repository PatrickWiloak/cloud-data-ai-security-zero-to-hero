---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 12 min
---

# SC-300 High-Yield Scenarios

Identity design problems in exam shape. Read the constraint carefully; several options will work technically and only one satisfies the requirement.

---

## Scenario 1: Choosing the governance feature

**Scenario**: A consultancy onboards 200 contractors per quarter. Each needs a specific set of applications, a SharePoint site, and a security group. Access must be requested by the contractor, approved by the engaging partner, and expire automatically after 90 days unless renewed. The tenant has Entra ID Governance licensing.

**Solution Pattern**:
- **Entitlement management access package** containing the applications, SharePoint site, and group
- Access package **policy** with the engaging partner as approver, a 90-day expiry, and a renewal request option
- Package published to a catalog scoped to external users, so contractors can self-request

**Common Distractors**:
- A dynamic group (no request, no approval, no expiry)
- PIM (governs privileged role activation, not bundled resource entitlement)
- Access reviews alone (recertifies existing access, does not provision it)
- Manual assignment with a calendar reminder (fails at 200 per quarter)

**Key Takeaway**: Access packages are the only feature that bundles heterogeneous resources behind a request-approve-expire workflow. When a scenario mentions request, approval, and expiry together, it is entitlement management.

---

## Scenario 2: Phishing-resistant authentication for a subset

**Scenario**: A bank must require phishing-resistant MFA for all administrators accessing the Azure portal, while standard users continue with Microsoft Authenticator. Administrators travel and cannot always carry a security key, so a compliant Windows device is an acceptable alternative.

**Solution Pattern**:
- Define a custom **authentication strength** including FIDO2 security key and Windows Hello for Business
- **Conditional Access policy** targeting the administrative roles, scoped to the Microsoft Azure Management app, with a grant control requiring that authentication strength
- Keep the existing baseline MFA policy for all users
- Exclude two **break-glass accounts** and monitor their sign-ins

**Common Distractors**:
- Requiring MFA generally (does not distinguish phishing-resistant methods)
- Removing SMS from the tenant-wide authentication methods policy (affects all users, not just admins)
- Per-user MFA settings (legacy, cannot express method strength)

**Key Takeaway**: "Phishing-resistant" maps to authentication strengths in Conditional Access, not to a generic MFA requirement. Targeting a role plus a specific cloud app is how you scope it without affecting everyone.

---

## Scenario 3: SSPR for synced users

**Scenario**: A company synchronizes 8,000 users from on-premises Active Directory. Users report that self-service password reset appears to succeed in the portal, but their on-premises password is unchanged and they cannot sign in to domain resources.

**Solution Pattern**:
- Enable **password writeback** in Entra Connect
- Ensure the Entra Connect service account has **Reset Password** and the relevant write permissions on the target OUs
- Confirm the on-premises **password policy** is not rejecting the new password silently
- Verify SSPR is enabled for the correct group and that users have completed **combined registration**

**Common Distractors**:
- Enabling SSPR for all users (already enabled; the issue is writeback)
- Switching to cloud-only accounts (a migration project, not a fix)
- Reconfiguring the authentication methods policy (governs which methods can be used, not writeback)

**Key Takeaway**: For synced users, SSPR without password writeback changes only the cloud password. This is a favorite exam question because the symptom looks like an SSPR configuration problem.

---

## Scenario 4: Delegated versus application permissions

**Scenario**: A nightly job must read all users' calendars to build an occupancy report. There is no signed-in user. A developer registered an app, granted `Calendars.Read` as a delegated permission, and the job returns 403.

**Solution Pattern**:
- Grant `Calendars.Read` as an **application permission**, which requires **admin consent**
- Authenticate with the **client credentials flow**, or better, a **managed identity** if the job runs on an Azure resource
- Scope the blast radius with an **application access policy** in Exchange Online so the app can only read the mailboxes it needs
- Rotate or eliminate the client secret; prefer a certificate or managed identity

**Common Distractors**:
- Granting a higher delegated permission (delegated permissions always require a signed-in user)
- Using a service account with a password (the pattern managed identities exist to replace)
- Granting Global Reader to the service principal (Entra role, not a Graph permission; does not solve it)

**Key Takeaway**: No signed-in user means application permissions and admin consent. Delegated permissions grant the intersection of app and user rights, so they cannot work in a daemon scenario.

---

## Scenario 5: Restricting guest access

**Scenario**: After a partner project, an audit finds that guest users can enumerate the full directory, including all users, groups, and their memberships. Leadership wants guests limited to only the objects they need, without blocking B2B collaboration.

**Solution Pattern**:
- Set **external user permissions** to "Guest user access is restricted to properties and memberships of their own directory objects" (the most restrictive setting)
- Use **cross-tenant access settings** to control which partner tenants can collaborate
- Restrict who can invite guests through the guest invite settings
- Apply an **access review** on guest accounts with auto-removal
- Where guests need directory data for an application, grant it through the application rather than through directory permissions

**Common Distractors**:
- Blocking B2B entirely (fails "without blocking collaboration")
- A Conditional Access policy (governs sign-in conditions, not directory read permissions)
- Converting guests to members (worse: members get more directory access, not less)

**Key Takeaway**: Directory enumeration by guests is controlled by external collaboration settings, not by Conditional Access. Conditional Access answers appear as distractors for many questions that are really about tenant settings.

---

## Scenario 6: Eliminating CI/CD secrets

**Scenario**: A platform team's GitHub Actions workflows deploy to Azure using a service principal with a client secret stored as a repository secret. The secret expired over a weekend and broke every deployment. Security also objects to a long-lived credential with subscription Contributor rights.

**Solution Pattern**:
- Configure **workload identity federation** on the app registration, trusting the GitHub OIDC issuer with a subject scoped to the specific repository, branch, or environment
- Remove the client secret entirely
- Scope the service principal's Azure RBAC to the specific resource groups, not the subscription
- Use separate federated credentials per environment so production cannot be deployed from a feature branch

**Common Distractors**:
- Rotating the secret automatically (still a long-lived credential, more machinery)
- Storing the secret in Key Vault (the workflow still needs a credential to reach Key Vault)
- A user-assigned managed identity (managed identities apply to Azure-hosted resources; GitHub-hosted runners need federation, though federation can also be configured against a managed identity)

**Key Takeaway**: Workload identity federation removes stored secrets for workloads outside Azure. Scoping the federated credential subject to a branch or environment is what makes it safer than the secret it replaces.

---

## Scenario 7: Conditional Access lockout risk

**Scenario**: An administrator plans a policy requiring compliant devices for all users accessing all cloud apps. The tenant has 3,000 users, and Intune enrolment is at 60%. The administrator wants to deploy safely.

**Solution Pattern**:
- Deploy in **report-only mode** first, then analyze the Conditional Access workbook and sign-in logs for the would-be blocked population
- Exclude two **break-glass cloud-only accounts** with FIDO2 keys or long passwords, and alert on their sign-ins
- Pilot with a small group before broad rollout
- Use the **What If** tool to test specific user and app combinations
- Stage enforcement: exclude the non-enrolled population initially, then shrink the exclusion as enrolment completes

**Common Distractors**:
- Enabling for all users immediately (locks out 40% of the organization)
- Using security defaults instead (all or nothing, no granularity, and it disables Conditional Access)
- Excluding the Global Administrator role (a role exclusion is not a break-glass account; break-glass accounts should be specific excluded users)

**Key Takeaway**: Report-only, break-glass exclusions, and staged rollout are expected in every Conditional Access answer. The exam tests deployment safety as much as policy design.

---

## Scenario 8: Removing standing privilege

**Scenario**: Twelve engineers hold permanent Global Administrator. Audit requires no standing privilege, approval before elevation, a justification record, and a quarterly recertification of who is even eligible. The tenant has Entra ID P2.

**Solution Pattern**:
- Convert the assignments to **PIM eligible** rather than active
- Configure activation settings: MFA on activation, justification required, approval required, and a maximum activation duration
- Enable **PIM alerts** for suspicious activation patterns and for any remaining permanent assignment
- Configure a **PIM access review** on the Global Administrator role, recurring quarterly
- Reduce the population: most of the twelve likely need a narrower role such as User Administrator or Application Administrator

**Common Distractors**:
- Conditional Access requiring MFA for admins (adds a sign-in condition but leaves standing privilege in place)
- An access package (governs resource entitlement, not directory role activation)
- Removing the role and re-adding when needed (manual, no audit trail, no approval)

**Key Takeaway**: "No standing privilege" plus "approval" plus "justification" is PIM, every time. The extra point the exam often includes is reducing role scope: least privilege comes before just-in-time.

---

## Related

- [Practice plan](./practice-plan.md)
- [Strategy](./strategy.md)
- [Notes](./notes/)
- [IAM explained](../../../learn/concepts/iam-explained.md)
- [Practice questions](../../../resources/practice-questions/azure-identity-access-sc-300.md)
