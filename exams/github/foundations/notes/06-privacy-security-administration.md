---
last-updated: 2026-10-22
applies-to: GH-900 skills measured as of January 2026, checked 2026-10-22
difficulty: beginner
---

# Domain 6: Understand privacy, security, and administration (10-15%)

This domain covers how GitHub protects accounts and code, and how administrators control who can do what: two-factor authentication and passkeys, repository and organization roles, teams, Enterprise Managed Users, Copilot policies, repository visibility, and branch protection rules versus rulesets. Security scanning features appear at awareness level.

**[📖 GH-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900)** - the official skills list
**[📖 About two-factor authentication](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-two-factor-authentication)** - 2FA on GitHub
**[📖 Roles in an organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization)** - organization roles
**[📖 Repository roles for an organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)** - read through admin

## Securing accounts: 2FA and passkeys

### Why 2FA matters

A password alone is one stolen secret away from a breach. Because a GitHub account can push code that thousands of people install, GitHub requires two-factor authentication for anyone who contributes code on GitHub.com. Organization owners can also require 2FA for every member, outside collaborator and billing manager, and people without it are removed from the organization.

With 2FA, signing in needs something you know (the password) plus something you have (a phone, an app or a hardware key).

### 2FA methods

| Method | How it works | Notes |
|--------|-------------|-------|
| **Authenticator app (TOTP)** | An app generates a 6-digit code every 30 seconds | Recommended primary method |
| **Security key** | A hardware key (WebAuthn/FIDO2) you touch | Phishing-resistant |
| **Passkey** | A WebAuthn credential stored on a device or in a password manager | Phishing-resistant; can also replace the password |
| **GitHub Mobile** | Approve a sign-in prompt in the app | Convenient second factor |
| **SMS** | A code sent by text message | Least secure; not available in every country; best as a fallback |

When you turn on 2FA, GitHub gives you **recovery codes**. Store them somewhere safe. They are the way back in if you lose your device, and GitHub Support usually cannot bypass 2FA for you.

### Passkeys

A **passkey** is a modern credential based on public-key cryptography (WebAuthn). The private key never leaves your device or password manager, and it only works on the real github.com, so a fake phishing site cannot capture anything useful. On GitHub, a passkey can serve two roles: as a **second factor** after your password, and for **passwordless sign-in**, where the passkey replaces both password and 2FA because it already combines possession of the device with a local unlock (fingerprint, face or PIN).

> **Exam trap:** SMS is the weakest 2FA method. Security keys and passkeys are the phishing-resistant ones. If a question asks for the most secure option, pick a passkey or security key, not SMS.

### Other credentials, briefly

Git operations over the command line do not use your password. They use a **personal access token** (fine-grained tokens, scoped to specific repositories and permissions, are recommended over classic tokens) or an **SSH key**. Commits can be **signed** with GPG, SSH or S/MIME keys so GitHub shows a Verified badge.

- **Two-factor authentication (2FA)** - signing in with a password plus a second factor such as an app code, security key, passkey or GitHub Mobile.
- **Passkey** - a phishing-resistant WebAuthn credential usable as a second factor or for passwordless sign-in.
- **Recovery codes** - one-time codes that restore access if you lose your 2FA device.
- **Fine-grained personal access token** - a token limited to chosen repositories and permissions, with an expiry.

**[📖 About passkeys](https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)** - passkeys on GitHub
**[📖 Configuring two-factor authentication](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)** - set up each method

## Access permissions and roles

GitHub uses **least privilege**: give each person the lowest role that lets them do their job. There are two layers of roles, and questions often test which layer a permission belongs to.

### Repository roles

In an organization repository, five built-in roles stack on each other:

| Role | Typical person | Can do (in addition to the role above) |
|------|----------------|----------------------------------------|
| **Read** | Viewers, non-code contributors | View and clone, open and comment on issues and PRs |
| **Triage** | Issue managers | Manage issues and PRs: labels, assignees, close and reopen, without write access to code |
| **Write** | Developers | Push to branches, merge pull requests (subject to protections) |
| **Maintain** | Project managers, lead maintainers | Manage some repository settings (topics, wiki, merge options) without destructive or sensitive actions |
| **Admin** | Owners of the repository | Everything: all settings, security, access, rename, transfer, delete |

Organizations on GitHub Enterprise Cloud can also define **custom repository roles** that start from one of these and add specific permissions.

> **Exam trap:** Triage is the answer when someone must "label and close issues but must not push code". Maintain is the answer when someone must "manage the repository without being able to delete it or change security settings".

Personal account repositories are simpler: the owner has full control and invited **collaborators** get write access.

### Organization roles

| Role | Scope |
|------|-------|
| **Owner** | Full administrative control of the organization: members, teams, billing, settings, every repository |
| **Member** | Default role; can create repositories (if allowed) and gets repository access through base permissions and teams |
| **Moderator** | A member who can block users, hide comments and limit interactions in public repositories |
| **Billing manager** | Manages billing settings and payment only; no access to code |
| **Security manager** | Can view and manage security alerts and settings across all repositories in the organization, with read access to all of them |
| **Outside collaborator** | Not a member; has access only to specific repositories they are invited to |

Organizations also offer **pre-defined organization roles** (for example, roles that grant read or write on all repositories) and, on Enterprise Cloud, **custom organization roles**. Every organization has **base permissions**, the default repository role all members get on every repository, which owners can set to None, Read, Write or Admin.

> **Exam trap:** Billing managers cannot see private code. Outside collaborators are not organization members and do not count toward member-only features like internal repositories.

### Teams

**Teams** group members, usually mirroring the real organization ("frontend", "security"). You grant a team a role on a repository once, and everyone in the team inherits it. People join and leave a team rather than being added to dozens of repositories one by one. Teams can be **nested**: a child team inherits the parent's repository access. Teams can be @mentioned (`@acme/frontend`), named in CODEOWNERS, and requested as reviewers. A team is either **visible** to all organization members or **secret** (visible only to its members and owners).

- **Least privilege** - granting the minimum access a person needs.
- **Triage role** - manages issues and pull requests without write access to code.
- **Maintain role** - manages a repository without sensitive or destructive settings.
- **Security manager** - organization role that manages security alerts and settings across all repositories.
- **Outside collaborator** - a non-member given access to specific organization repositories.
- **Base permissions** - the default repository role every organization member receives.
- **Team** - a group of organization members granted repository access together; can be nested.

**[📖 About teams](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)** - teams and nesting
**[📖 Setting base permissions for an organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/setting-base-permissions-for-an-organization)** - default access

## Enterprise administration

### Enterprise Managed Users (EMUs)

Normally, a person brings their own personal GitHub account and joins a company's organization with it. With **Enterprise Managed Users**, an option for GitHub Enterprise Cloud, the company's **identity provider** (such as Microsoft Entra ID or Okta) creates and controls the accounts instead.

- Accounts are **provisioned with SCIM** from the identity provider, and removed when the person leaves.
- Users **sign in through the identity provider** (SAML or OIDC), not with a GitHub password.
- Usernames carry the enterprise's short code as a suffix, such as `mona_acme`.
- Managed users **cannot** create public content, collaborate on repositories outside the enterprise, star or fork outside repositories, or be invited into other organizations. They live entirely inside the company's walls.

Why choose EMUs? Full lifecycle control and a clean separation between work and personal identities, which regulated industries often require. The trade-off is that managed users cannot take part in open source from those accounts.

Compare this with **SAML single sign-on** on a regular enterprise: people keep their own personal accounts, and SSO adds a check that they also authenticate with the company identity provider before accessing company resources.

| | Personal accounts with SAML SSO | Enterprise Managed Users |
|-|-------------------------------|--------------------------|
| Who owns the account | The person | The company (via the identity provider) |
| Account creation | Person signs up | SCIM provisioning |
| Public and open source activity | Yes | No |
| Leaving the company | Account remains, access removed | Account deprovisioned |

> **Exam trap:** "The company must control account creation and removal from its identity provider, and employees must not be able to publish public code with those accounts" is an EMU question.

**[📖 About Enterprise Managed Users](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users)** - EMU capabilities and limits

### Organization-wide Copilot policies

Copilot Business and Enterprise are governed by **policies**. Enterprise owners set policies for the whole enterprise, or leave a policy undecided so each organization owner can choose. Typical policies cover which Copilot features are enabled (Chat, agent mode, the coding agent - now called Copilot cloud agent - and Copilot CLI), which AI models are available, whether suggestions that match public code are allowed or blocked, and **content exclusion** for sensitive paths. Organization owners also decide who gets a Copilot **seat**: everyone, selected teams, or selected members.

The point for the exam: in an organization, individual developers do not decide what Copilot may do. Admins do, and the most specific allowed setting wins within the limits the enterprise sets.

**[📖 Managing policies for Copilot in your organization](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-policies)** - organization policies

## Repository visibility

| Visibility | Who can see it | Available to |
|------------|---------------|--------------|
| **Public** | Everyone on the internet | All accounts |
| **Private** | Only people explicitly given access (and organization owners) | All accounts |
| **Internal** | Every member of the enterprise, across its organizations | Organizations in an enterprise account (GitHub Enterprise) |

Internal visibility exists for **InnerSource**: code that the whole company should be able to find and reuse, but that must not be public.

Changing visibility has consequences. Making a repository private detaches public forks. Making a private repository public exposes its entire history, including any secrets ever committed. GitHub warns before both.

> **Exam trap:** Internal repositories need an enterprise account. A standalone organization on GitHub Team has only public and private.

**[📖 About repositories: visibility](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility)** - visibility options
**[📖 Setting repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)** - changing it

## Branch protection rules and rulesets

Both features enforce rules on branches so important code only changes the right way. Typical rules: require a pull request before merging, require a number of approvals, require code owner review, require status checks to pass, require conversation resolution, require signed commits, require linear history, block force pushes and block deletion.

### Branch protection rules

The classic feature. A **branch protection rule** targets a branch name pattern (`main`, `release/*`) in one repository. Only **one** rule applies to a given branch; if several patterns match, GitHub uses the most specific. Rules are managed under repository Settings and only admins can see their full configuration.

### Rulesets

**Rulesets** are the newer, more flexible model:

- **Layering** - many rulesets can apply to the same branch at once. Their rules combine, and the most restrictive wins.
- **Enforcement status** - a ruleset can be **Active** or **Disabled**, and on Enterprise it can run in **Evaluate** mode to report what would be blocked without blocking it.
- **Bypass list** - named roles, teams or apps can be allowed to bypass, which is explicit and auditable.
- **Organization scope** - organizations on GitHub Enterprise can define rulesets once at the organization level and target many repositories by name pattern or property.
- **Tags and pushes** - rulesets can protect tags, and push rulesets can block pushes to private or internal repositories by file path, size or extension.
- **Availability** - rulesets work on public repositories on every plan, and on private repositories with GitHub Pro, Team or Enterprise.
- **Visibility** - anyone with read access can see which rulesets apply, which explains why a push was rejected.

| | Branch protection rule | Ruleset |
|-|-----------------------|---------|
| Rules per branch | One | Many, layered |
| Scope | One repository | Repository or whole organization |
| Targets | Branches | Branches, tags, pushes |
| Trial mode | No | Evaluate mode (Enterprise) |
| Who can view | Admins | Anyone with read access |

> **Exam trap:** "Enforce the same protection on `main` across 200 repositories without configuring each one" is an organization ruleset, not 200 branch protection rules.

**[📖 About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)** - branch protection rules
**[📖 About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)** - rulesets and how they layer

## Organization settings

Organization owners manage, among other things: member privileges (who can create repositories, fork private repositories, or change visibility), base permissions, 2FA requirement, teams, Actions policies (which actions may run), Copilot access and policies, security defaults for new repositories, verified domains, and the **audit log**, which records who did what across the organization. Enterprise owners can set the same kinds of policy above all organizations, and an enterprise policy overrides organization choices.

- **Audit log** - the record of security-relevant actions taken in an organization or enterprise.
- **Ruleset** - a named, layered set of branch, tag or push rules with an enforcement status and bypass list.
- **Branch protection rule** - a single rule set on a branch name pattern in one repository.
- **Enterprise Managed Users** - accounts created and controlled by the company's identity provider, confined to the enterprise.
- **Internal visibility** - repository visibility for all members of an enterprise, used for InnerSource.

## Security features at awareness level

GH-900 expects you to know what each feature is for, not how to configure it.

- **Dependabot alerts** - warn when a dependency has a known vulnerability, using the dependency graph and the GitHub Advisory Database.
- **Dependabot security updates** - open pull requests that upgrade a vulnerable dependency to a fixed version.
- **Dependabot version updates** - open pull requests to keep dependencies current, configured in `.github/dependabot.yml`.
- **Secret scanning** - detects committed credentials such as API keys and tokens.
- **Push protection** - blocks a push that contains a detected secret before it reaches the repository.
- **Code scanning** - static analysis, typically with CodeQL, that finds vulnerabilities and coding errors and shows alerts on pull requests.
- **Security advisories** - let maintainers privately discuss, fix and publish a vulnerability, and request a CVE.

Many of these are free for public repositories. For private repositories, secret scanning and code scanning come with paid **GitHub Secret Protection** and **GitHub Code Security** products (formerly bundled as GitHub Advanced Security).

> **Exam trap:** Secret scanning looks for credentials. Code scanning looks for vulnerable code patterns. Dependabot looks at third-party packages. Match the threat to the tool.

**[📖 About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts)** - dependency vulnerability alerts
**[📖 About secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)** - credential detection
**[📖 About code scanning](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning)** - static analysis

## Key exam points

- 2FA methods: authenticator app, security key, passkey, GitHub Mobile, SMS (weakest). Keep recovery codes.
- Passkeys are phishing-resistant and can enable passwordless sign-in.
- Repository roles: Read, Triage, Write, Maintain, Admin.
- Organization roles include Owner, Member, Moderator, Billing manager, Security manager; outside collaborators are not members.
- Teams grant access in bulk; nested teams inherit parent access.
- EMUs are company-controlled accounts provisioned by the identity provider and confined to the enterprise.
- Copilot policies are set by enterprise and organization owners, not individual developers.
- Visibility: public, private, internal (enterprise only).
- Rulesets layer and can apply organization-wide; branch protection rules are one per branch per repository.
- Dependabot for packages, secret scanning for credentials, code scanning for code.
