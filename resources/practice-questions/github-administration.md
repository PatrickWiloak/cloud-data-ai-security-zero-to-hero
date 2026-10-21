---
last-updated: 2026-08-09
difficulty: intermediate
---

# GitHub Administration Certification - Practice Questions

15 questions for the GitHub Administration exam, weighted toward user identities and access (20%) and managing Actions (20%), then enterprise support, repositories, Advanced Security, and enterprise administration.

> **Cert page:** [exams/github/administration/](../../exams/github/administration/)

---

### Question 1
**Scenario:** An enterprise must control accounts fully, including creating and deleting them.

A. Personal access tokens issued to each member
B. Enterprise Managed Users, with accounts created and owned by the enterprise through an identity provider
C. SAML SSO over members' existing personal accounts
D. Organization invitations sent to each person's work email

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** EMU accounts are created and owned by the enterprise through the IdP, so users cannot take them elsewhere and offboarding is complete. SAML SSO authenticates personal accounts against your IdP but the account itself still belongs to the individual.
</details>

---

### Question 2
**Scenario:** Repository access must follow team structure and be reviewed easily.

A. Grant to teams, ideally synced from IdP groups, with nested teams for inheritance
B. Use outside collaborators for each project, adding the people involved to every repository they touch with a defined role
C. Grant access to individuals per repository, so every permission is explicit and can be read straight off the settings page
D. Give everyone write access, then use branch protection to stop changes from reaching the default branch without review

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Team-based access means a personnel change updates one membership rather than dozens of repository grants, and team sync from the IdP removes the manual step entirely. Individual grants accumulate and are what access reviews find months later.
</details>

---

### Question 3
**Scenario:** A policy must apply to every repository in the enterprise.

A. A README or contributing file in each repository describing the policy, which every contributor is expected to follow
B. Ask each team to apply the policy to its own repositories and report back when the setting has been changed
C. Enterprise policies and organization rulesets, which cascade down
D. Configure each repository by hand, using a checklist that is repeated whenever a new repository is created

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Policies set at the enterprise constrain what organizations may permit, and rulesets apply branch and tag rules across repositories by pattern. Per-repository configuration drifts and cannot be verified without checking every repository.
</details>

---

### Question 4
**Scenario:** Only vetted actions should be usable in workflows.

A. Restrict to actions by GitHub and verified creators, plus an allowlist, set at enterprise or organization level
B. Disable Actions entirely and let teams use an external CI system
C. Review workflows manually, with security approving every new `uses:` line
D. Allow all actions, since pinning to a full commit SHA makes any action safe

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Every referenced action runs with access to that workflow's secrets, so the action list is a supply chain. Allowlisting is the enforceable control; manual review of every workflow does not scale and misses transitive action usage.
</details>

---

### Question 5
**Scenario:** Self-hosted runners must be available to some repositories only.

A. One shared runner for everything, placed on the production network so that any workflow can reach the systems it needs
B. Runner groups scoped to selected organizations or repositories
C. Register the runners on every repository
D. Public runners only, hosted by GitHub

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Runner groups are the access boundary for infrastructure: a runner with network access to production should be reachable only from the repositories that deploy there. Enterprise-level runners with no grouping give every repository that access.
</details>

---

### Question 6
**Scenario:** Audit data must be exported to a SIEM.

A. Screenshots of the audit log page taken weekly by an organization owner and attached to the SIEM ticket
B. Audit log streaming to a supported destination, plus the audit log API
C. Repository logs, meaning the commit history of each repository, which records every administrative action for the organization
D. A manual export of the audit log each month, saved as JSON and loaded into the SIEM by an administrator

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Streaming gives near real-time delivery and retention beyond GitHub's own window, which is what a security team needs for correlation and long-term investigation. Periodic manual export creates gaps and depends on somebody remembering.
</details>

---

### Question 7
**Scenario:** A departing employee's access must be removed completely.

A. Change the repository visibility to private, which removes the former employee's access to the code they used to work on
B. Remove them from one organization, since the membership there is what grants access to every repository they could use
C. Deprovision through the IdP (EMU or SCIM), then revoke tokens, SSH keys and authorized apps
D. Delete their commits from the repositories they contributed to

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The path people forget is credentials that outlive the session: personal access tokens, SSH keys, and OAuth or GitHub App authorizations. SCIM deprovisioning handles membership, and SAML session revocation plus credential authorization removal closes the rest.
</details>

---

### Question 8
**Scenario:** An organization must migrate repositories from another instance.

A. Recreate the repositories by hand in the new organization
B. Clone and push each repository manually with `git push --mirror`, which brings the issues, pull requests and reviews with it
C. Copy the files from a working tree into a new repository, which preserves the commit authors and every commit date
D. GitHub Enterprise Importer or the migration APIs, which bring issues and pull requests too

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A plain clone and push moves git history but loses issues, pull requests, reviews, and their links, which is often most of the project's institutional memory. The importer is designed to carry that metadata across.
</details>

---

### Question 9
**Scenario:** A repository must not be deleted accidentally.

A. Make it private, since the visibility setting controls who is allowed to delete a repository
B. Hope that nobody removes it, and rely on the confirmation prompt that asks for the repository name to be typed
C. Archive everything in the organization, since an archived repository cannot be deleted by any member or owner
D. Limit repository deletion to owners through member privileges, and keep backups

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Limiting repository deletion to owners is a member privilege setting, and archiving makes a repository read-only while keeping it visible. Deleted repositories can be restored for a limited window, which is not a backup strategy.
</details>

---

### Question 10
**Scenario:** GitHub Apps versus OAuth apps for automation.

A. OAuth apps are more secure because they act as a user and so inherit that user's multi-factor protection on every call they make, whereas apps hold only a key
B. GitHub Apps have their own identity, fine-grained permissions, per-repository installs and short-lived tokens; OAuth apps act as a user
C. Only OAuth apps support webhooks, so an integration that must react to repository events needs to be registered that way
D. They are identical, because they use the same token format and the same permission scopes and differ only in where they are listed in the settings

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A GitHub App's installation token is scoped and expires, and its access does not disappear when a person leaves, which is why it is the recommended pattern for integrations. OAuth apps inherit whatever the authorizing user can do.
</details>

---

### Question 11
**Scenario:** License usage must be understood before renewal.

A. Enterprise license usage reporting, including consumed seats and Advanced Security active committers
B. Count repositories, since the number of repositories in each organization is what drives the seat total at renewal
C. Count users manually from each People page
D. Estimate from last year's invoice plus expected growth, which is close enough for the renewal conversation

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Seat consumption and GHAS active committers are counted differently, and the second is what drives Advanced Security cost. Reviewing dormant accounts before renewal is usually the quickest saving available.
</details>

---

### Question 12
**Scenario:** An enterprise wants innersource: code visible internally but not publicly.

A. Public repositories, since anyone inside the company can find them
B. Private repositories with manual invitations
C. Internal repository visibility, which exposes it to all enterprise members
D. Forks only, where each team keeps a private fork of the code that others cannot find unless they are told about it

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Internal visibility is the innersource default: any enterprise member can find, read, and fork the repository without an invitation, which is what makes reuse actually happen. Private repositories with per-person grants create the discovery problem innersource exists to solve.
</details>

---

### Question 13
**Scenario:** A support case must be raised with sufficient detail.

A. Include the organization, repository, timestamps, and a support bundle where applicable, at the right priority
B. A screenshot of the error message
C. Post publicly in the community forum and tag a GitHub staff member
D. A one-line description of the symptom, since support will ask for any further detail

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** For GitHub Enterprise Server, the support bundle contains the logs support needs and gathering it upfront removes a round trip. Choosing the right priority matters because it determines response targets under the support plan.
</details>

---

### Question 14
**Scenario:** Two-factor authentication must be mandatory for an organization.

A. Ask users to turn on two-factor authentication through an email, then check the member list each month for who has not
B. Rely on strong passwords with a minimum length and a ban on reuse, which gives the same protection as a second factor
C. Enforce the 2FA requirement at the organization or enterprise level; non-compliant members are removed and need reinstatement
D. Enable it per user from the organization's People page, which then forces each user to set up a second factor at their next sign-in

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Enforcement removes members who do not comply, so communicate the deadline before enabling it or you will unexpectedly lock people out. Bots and service accounts need attention too, since they also require a second factor.
</details>

---

### Question 15
**Scenario:** GitHub Enterprise Cloud versus Enterprise Server.

A. Cloud cannot use SAML, so organizations that need single sign-on with their own identity provider must choose Server instead, and run it themselves
B. Server is always newer, because self-hosted releases ship first and Cloud receives the same features some months afterwards
C. They are identical products apart from the licence terms, the billing relationship, and the logo shown on the sign-in page of each
D. Cloud is GitHub-hosted and has the newest features; Server is self-hosted, giving isolation and residency at the cost of running it yourself

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The trade-off is control versus operational burden. Server appeals where regulation or network isolation demands it, and the cost is patching, upgrades, backup, and capacity planning that Cloud handles for you.
</details>

---

## Where to go deeper

- [GitHub Administration cert page](../../exams/github/administration/) - notes, practice plan, strategy
- [GitHub Actions practice questions](./github-actions.md) - the Actions domain in depth
- [GHAS practice questions](https://security.noblerworks.com/resources/practice-questions/github-advanced-security/) - the security domain in depth
- [GitHub Foundations practice questions](./github-foundations.md) - the fundamentals below this
- **[📖 GitHub Certifications](https://learn.github.com/certifications)** - official exam pages
