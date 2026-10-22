---
last-updated: 2026-10-22
difficulty: intermediate
---

# GitHub Administration Certification - Practice Questions

30 questions for the GitHub Administration exam, weighted toward user identities and access (20%) and managing Actions (20%), then enterprise support, repositories, Advanced Security, and enterprise administration.

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

### Question 16
**Scenario:** GitHub Support asks a GitHub Enterprise Server administrator for diagnostic data about an appliance that keeps failing background jobs. What should the administrator provide?

A. A screenshot of the site admin dashboard taken while the jobs are failing
B. An export of the organization audit log covering the previous 90 days
C. A copy of the appliance's license file and the current admin password
D. A support bundle, generated with `ghe-support-bundle` or the Management Console

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A support bundle packages the logs and configuration Support needs to diagnose an appliance, and it can be generated from the administrative shell with `ghe-support-bundle` or downloaded from the Management Console. A screenshot lacks the underlying logs. The audit log records user and admin actions, not service failures. Credentials should never be sent to Support.

**Key Concept:** Support bundles and diagnostics speed up GHES tickets. See [Providing data to GitHub Support](https://docs.github.com/en/enterprise-server@latest/support/contacting-github-support/providing-data-to-github-support).
</details>

---

### Question 17
**Scenario:** Developers across an Enterprise Cloud account report that Actions jobs have been queued for 20 minutes in every organization. Nothing has changed in their configuration. What should the administrator check first?

A. Each repository's workflow files, line by line, for syntax errors
B. The GitHub Status page, for an ongoing incident affecting Actions
C. The enterprise license count, to see whether seats have run out
D. The audit log, for a recent change to the runner group settings

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A sudden, enterprise-wide problem with no local changes points to a platform incident, and GitHub publishes incident status for each service. Checking it first avoids wasted investigation and needless tickets. Syntax errors would fail jobs, not queue them everywhere. Seat counts do not queue jobs. Runner group changes would affect specific runners, not every organization at once.

**Key Concept:** Rule out a platform incident before debugging configuration. See [GitHub Status](https://www.githubstatus.com/).
</details>

---

### Question 18
**Scenario:** A company uses Enterprise Managed Users. A developer cannot open a pull request against a public open-source project hosted outside the enterprise, though the same action works with their personal account. Why?

A. Managed user accounts cannot create content or contribute outside their enterprise
B. The open-source project has blocked all users from the company's email domain
C. The developer lacks a GitHub Copilot license, which is required to open pull requests
D. Pull requests to public repositories require the enterprise to enable public forking first

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Managed user accounts are owned by the enterprise and restricted to it: they can view public content but cannot push code, open issues, or create pull requests in repositories outside the enterprise. The project has not blocked anyone. Copilot is unrelated to pull requests. Fork policies govern private and internal repositories inside the enterprise, not contributions to outside projects.

**Key Concept:** EMU trades open collaboration for full central control of accounts. See [About Enterprise Managed Users](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users).
</details>

---

### Question 19
**Scenario:** An enterprise with 40 organizations on Enterprise Cloud, using personal accounts, wants every organization protected by the same identity provider with one configuration. Where should SAML single sign-on be configured?

A. In each organization separately, using the same IdP metadata 40 times
B. In the personal settings of every member, linked to their IdP account
C. At the enterprise account level, which enforces it for every organization
D. In a GitHub App installed on all 40 organizations with SAML permissions

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Configuring SAML SSO on the enterprise account applies it to all organizations owned by the enterprise, which removes repetition and prevents a new organization being left unprotected. Per-organization setup is possible but repetitive and easy to miss. Members do not configure SSO themselves. GitHub Apps do not provide SAML authentication.

**Key Concept:** Set identity controls at the highest level that covers everything. See [Configuring SAML single sign-on for your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise).
</details>

---

### Question 20
**Scenario:** Team membership on GitHub drifts from the company directory. People who change departments keep old access for weeks. How should the administrator keep team membership aligned?

A. Run a quarterly manual review of every team, comparing it with the HR system
B. Grant all members admin access so team membership no longer matters at all
C. Ask team maintainers to remove members whenever they hear about a move
D. Connect each team to an identity provider group so membership follows the directory

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Linking teams to IdP groups, through team synchronization or EMU group management, means directory changes update GitHub team membership automatically. Quarterly reviews leave months of drift. Admin for everyone removes least privilege entirely. Relying on maintainers to hear about moves is the process that is already failing.

**Key Concept:** Let the directory drive access so moves and leavers take effect automatically. See [Managing team synchronization](https://docs.github.com/en/enterprise-cloud@latest/organizations/organizing-members-into-teams/synchronizing-a-team-with-an-identity-provider-group).
</details>

---

### Question 21
**Scenario:** An organization owner wants to require pull request reviews on the default branch of every repository in the organization. Before enforcing it, they want to see which pushes it would have blocked. What should they use?

A. An organization ruleset targeting default branches, set to Evaluate mode first
B. Branch protection rules added to each repository one by one, then deleted if noisy
C. A required workflow that fails every push which does not come from a pull request
D. A CODEOWNERS file in each repository that lists the organization owners as reviewers

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Organization rulesets apply to many repositories at once, and Evaluate mode, available on GitHub Enterprise, records what the rules would have blocked without enforcing them, so impact can be checked first. Per-repository branch protection does not scale and has no dry-run mode. A workflow runs after the push, so it cannot block it. CODEOWNERS requests reviews but does not by itself require them, and it does not report impact.

**Key Concept:** Rulesets layer across repositories and support a test mode before enforcement. See [About rulesets](https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).
</details>

---

### Question 22
**Scenario:** Every member of an organization needs to read every private repository, while write access stays limited to specific teams. What is the simplest setting?

A. Add every member as a direct collaborator with Read on each repository
B. Set the organization's base permission for members to Read
C. Make every repository public so that all members can read it
D. Create one team with all members and add it to each repository

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The base permission applies to all organization members on all repositories, so Read gives everyone read access at once, and teams then grant write where needed. Direct collaborators and an all-members team both require changes in every repository, including new ones. Making repositories public exposes them to the world.

**Key Concept:** Base permissions set the floor; teams and roles raise access from there. See [Setting base permissions for an organization](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/setting-base-permissions-for-an-organization).
</details>

---

### Question 23
**Scenario:** A security review finds that workflows across the organization run with a `GITHUB_TOKEN` that can write to repository contents by default. The team wants least privilege without editing hundreds of workflows. What should the administrator do?

A. Delete the `GITHUB_TOKEN` secret from each repository so workflows stop using it
B. Require every workflow to use a personal access token from a service account instead
C. Set the organization's default workflow permissions to read-only for the token
D. Disable GitHub Actions for the organization until every workflow has been reviewed

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The default `GITHUB_TOKEN` permissions can be set to read-only at the organization or enterprise level; workflows that need more can request it with a `permissions` block. The token is generated per job and is not a stored secret you can delete. Long-lived personal access tokens are a worse security posture. Disabling Actions stops all delivery.

**Key Concept:** Default to a read-only token and grant write per workflow or job. See [Automatic token authentication](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication).
</details>

---

### Question 24
**Scenario:** Workflows deploy to a cloud provider using long-lived access keys stored as repository secrets. Security wants to remove stored cloud credentials entirely. What should the administrator recommend?

A. Configure OpenID Connect so workflows exchange a short-lived token with the cloud
B. Store the access keys as organization secrets rather than repository secrets
C. Rotate the access keys monthly with a scheduled workflow that updates the secrets
D. Encrypt the access keys with a second key stored as an environment secret

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** With OIDC, the workflow presents a GitHub-issued token to the cloud provider, which trusts it based on claims such as repository and branch and returns short-lived credentials, so nothing long-lived is stored. Moving secrets to the organization level still stores them. Rotation shortens their lifetime but keeps stored keys. Encrypting a key with another stored key just moves the secret.

**Key Concept:** Federated identity replaces stored cloud keys in CI. See [About security hardening with OpenID Connect](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect).
</details>

---

### Question 25
**Scenario:** A platform team runs self-hosted runners on Kubernetes. They want runners to scale with the job queue and give every job a clean environment. What is the GitHub-supported approach?

A. A fixed pool of long-lived runner pods that are restarted by hand each weekend
B. A single large runner VM that runs every job, cleaned by a nightly script
C. GitHub-hosted larger runners attached to the cluster as additional nodes
D. Actions Runner Controller running ephemeral runner scale sets on the cluster

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Actions Runner Controller is GitHub's Kubernetes operator for self-hosted runners; runner scale sets scale on demand and create ephemeral runners that handle one job and are removed. Long-lived pods and a single shared VM carry state between jobs and do not scale with demand. GitHub-hosted runners run on GitHub's infrastructure and cannot join a customer cluster.

**Key Concept:** Ephemeral, autoscaled runners limit cross-job contamination and idle cost. See [About Actions Runner Controller](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/about-actions-runner-controller).
</details>

---

### Question 26
**Scenario:** After a leaked token incident, leadership wants to stop developers from pushing commits that contain supported secret types, rather than only detecting them afterwards. Which feature does this?

A. Secret scanning alerts, which notify administrators after a secret lands
B. Push protection, which blocks pushes that contain detected secrets
C. Dependabot alerts, which flag dependencies with known vulnerabilities
D. Code scanning, which runs static analysis on each pull request

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Push protection checks pushes for supported secrets and blocks them before they reach the repository, with a bypass flow that is recorded. Secret scanning alerts find secrets after they are committed. Dependabot deals with vulnerable dependencies. Code scanning finds code vulnerabilities, not committed credentials.

**Key Concept:** Prevent first, detect second: push protection plus secret scanning alerts. See [About push protection](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/introduction/about-push-protection).
</details>

---

### Question 27
**Scenario:** Repositories receive Dependabot alerts for vulnerable dependencies, but nobody acts on them. The administrator wants pull requests that update vulnerable dependencies to a fixed version to be raised automatically. What should be enabled?

A. Dependabot version updates on a weekly schedule for every package ecosystem
B. The dependency graph alone, which lists every dependency in each repository
C. Code scanning default setup, which also proposes patched dependency versions
D. Dependabot security updates, which raise pull requests for vulnerable dependencies

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Dependabot security updates open pull requests that bump a vulnerable dependency to the minimum fixed version when an alert is raised. Version updates keep everything current on a schedule regardless of vulnerability, which creates far more pull requests. The dependency graph only lists dependencies. Code scanning analyses your own code, not dependency versions.

**Key Concept:** Alerts tell you; security updates fix it with a pull request. See [About Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates).
</details>

---

### Question 28
**Scenario:** An organization wants CodeQL code scanning on 500 repositories this week. Most teams have no Actions expertise, and nobody wants to add workflow files to every repository. What is the fastest path?

A. Enable CodeQL default setup at scale, for example through a security configuration
B. Copy an advanced setup workflow file into each of the 500 repositories by script
C. Ask each team to write and test its own CodeQL workflow before enabling scanning
D. Run CodeQL locally on a developer laptop and upload the results once a quarter

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Default setup enables CodeQL without workflow files, choosing languages and settings automatically, and it can be applied to many repositories at once through organization security settings. Scripted advanced setup files work but add workflows to maintain in every repository. Asking each team is slow. Quarterly laptop scans are neither continuous nor tied to pull requests.

**Key Concept:** Use default setup for breadth, advanced setup where a repository needs customisation. See [About the default setup for code scanning](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning).
</details>

---

### Question 29
**Scenario:** A regulated company on Enterprise Cloud must make sure its private repositories can only be reached from the corporate network and VPN, including through the API and Git. What should the enterprise owner configure?

A. Required two-factor authentication for every member in each organization
B. A ruleset that blocks pushes to private repositories from unknown users
C. An IP allow list at the enterprise level covering the corporate ranges
D. An audit log stream that alerts when a login comes from a new country

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** An enterprise IP allow list restricts access to the enterprise's organizations and private assets, through the web, API, and Git, to listed IP ranges. Two-factor authentication strengthens login but does not limit where access comes from. Rulesets govern branch and tag operations, not network origin. An audit stream detects after the fact rather than preventing access.

**Key Concept:** Network restrictions and identity controls are separate layers. See [Restricting network traffic with an IP allow list](https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/hardening-security-for-your-enterprise/restricting-network-traffic-to-your-enterprise-with-an-ip-allow-list).
</details>

---

### Question 30
**Scenario:** A GitHub Enterprise Server administrator is planning an upgrade to a newer feature release next weekend. What preparation is most important?

A. Disable SAML authentication during the upgrade so users can still log in
B. Take a backup with GitHub Enterprise Server Backup Utilities and confirm the upgrade path
C. Delete archived repositories so the upgrade finishes faster and uses less disk space
D. Ask users to push all their branches to personal accounts in case of data loss

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A recent backup from Backup Utilities is the recovery plan if the upgrade fails, and the upgrade path matters because GHES only supports upgrading from a limited number of earlier feature releases at a time. Disabling SAML weakens security and does not help the upgrade. Deleting data to save time risks loss. Copying code to personal accounts creates a data leak.

**Key Concept:** Back up, check the upgrade path, and use maintenance mode. See [Upgrading GitHub Enterprise Server](https://docs.github.com/en/enterprise-server@latest/admin/upgrading-your-instance/preparing-to-upgrade/overview-of-the-upgrade-process).
</details>

---

## Where to go deeper

- [GitHub Administration cert page](../../exams/github/administration/) - notes, practice plan, strategy
- [GitHub Actions practice questions](./github-actions.md) - the Actions domain in depth
- [GHAS practice questions](https://security.noblerworks.com/resources/practice-questions/github-advanced-security/) - the security domain in depth
- [GitHub Foundations practice questions](./github-foundations.md) - the fundamentals below this
- **[📖 GitHub Certifications](https://learn.github.com/certifications)** - official exam pages
