---
last-updated: 2026-10-22
applies-to: GH-900 skills measured as of January 2026, checked 2026-10-22
difficulty: beginner
---

# GitHub Foundations (GH-900) - Exam-Style Scenarios

Each scenario names the domain it practises, using the January 2026 outline. These are original practice items, not vendor exam questions.

## Scenario 1: Repository Setup and Collaboration

**Domain:** Domain 2: Work with GitHub repositories, and Domain 6

### Scenario
A small development team of 5 people is starting a new open source project. They want to allow external contributors while maintaining code quality. The team needs to set up their repository with appropriate settings and protection rules.

**Question:** Which combination of configurations should the team implement?

**Options:**
A. Create a private repository, add all contributors as collaborators, and require signed commits
B. Create a public repository, add branch protection rules requiring PR reviews, create CONTRIBUTING.md and CODE_OF_CONDUCT.md, and add a LICENSE file
C. Create an internal repository with a CODEOWNERS file and enable GitHub Discussions
D. Create a public repository with no branch protection and allow direct pushes to main

**Correct Answer:** B

**Explanation:**
- Public repository is needed for open source projects - external contributors can view and fork
- Branch protection with required PR reviews ensures code quality through peer review
- CONTRIBUTING.md provides guidelines for external contributors
- CODE_OF_CONDUCT.md establishes community behavior standards
- LICENSE file is essential for open source projects to define usage terms

**Why other options are wrong:**
- **A:** Private repository prevents external contributors from seeing or forking the code
- **C:** Internal repositories are only available within organizations, not for open source
- **D:** No branch protection means anyone with write access could push directly to main, risking code quality

---

## Scenario 2: Git Workflow and Commands

**Domain:** Domain 1: Understand Git and GitHub basics

### Scenario
A developer has been working on a feature branch called `feature/login` and has made several commits. They want to incorporate the latest changes from the `main` branch into their feature branch before opening a pull request. They want to maintain a clean, linear commit history.

**Question:** Which Git command should the developer use?

**Options:**
A. `git merge main` (while on feature/login branch)
B. `git rebase main` (while on feature/login branch)
C. `git pull origin main` (while on feature/login branch)
D. `git cherry-pick main`

**Correct Answer:** B

**Explanation:**
- `git rebase main` replays the feature branch commits on top of the latest main branch commits
- This creates a clean, linear history without merge commits
- The developer should be on the feature/login branch when running this command
- After rebasing, the feature branch will appear as if it was started from the latest main

**Why other options are wrong:**
- **A:** `git merge main` would create a merge commit, not maintaining linear history
- **C:** `git pull origin main` would fetch and merge, also creating a merge commit
- **D:** `git cherry-pick` is for selecting specific commits, not integrating an entire branch

---

## Scenario 3: Pull Request and Code Review

**Domain:** Domain 3: Collaborate using GitHub, and Domain 6

### Scenario
A developer opens a pull request that fixes a critical bug. The repository has the following branch protection rules on `main`:
- Require at least 2 approving reviews
- Require status checks to pass (CI tests)
- Require conversation resolution

The CI tests pass, one reviewer approves, and there is one unresolved conversation. The developer wants to merge immediately because the bug is critical.

**Question:** What must happen before this PR can be merged?

**Options:**
A. The developer can force-merge since the bug is critical
B. The developer needs one more approving review and must resolve the unresolved conversation
C. Only the one unresolved conversation needs to be resolved since tests pass
D. An organization admin can bypass all branch protection rules to merge immediately

**Correct Answer:** B

**Explanation:**
- Branch protection rules are enforced - ALL conditions must be met
- The PR currently has: 1 approval (needs 2), passing CI (met), 1 unresolved conversation (needs 0)
- Two remaining requirements: get a second approving review AND resolve the conversation
- Even critical bugs must follow the established process for code quality

**Why other options are wrong:**
- **A:** There is no force-merge option that bypasses branch protection for regular users
- **C:** The PR also needs a second approving review (only has 1 of required 2)
- **D:** Bypassing is not the default. A branch protection rule can be set to apply to administrators, and a ruleset allows bypass only for roles, teams or apps on its bypass list. Even where bypass is allowed, it is an exception, not the normal path for a critical fix

---

## Scenario 4: GitHub Actions Basics

**Domain:** Domain 4: Apply modern development practices

### Scenario
A team wants to automatically run their test suite every time someone pushes code to any branch and whenever a pull request is opened against the `main` branch. They also want tests to run on a schedule every night at midnight.

**Question:** Which workflow trigger configuration correctly implements these requirements?

**Options:**
A.
```yaml
on:
  push:
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * *'
```

B.
```yaml
on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: '0 0 * * *'
```

C.
```yaml
on:
  push:
  pull_request:
  schedule:
    - cron: 'midnight'
```

D.
```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * *'
```

**Correct Answer:** A

**Explanation:**
- `push:` with no branch filter triggers on pushes to ANY branch (requirement 1)
- `pull_request: branches: [main]` triggers when PRs target the main branch (requirement 2)
- `schedule: cron: '0 0 * * *'` runs at midnight UTC daily (requirement 3)
- All three requirements are met with this configuration

**Why other options are wrong:**
- **B:** `push: branches: [main]` only triggers on pushes to main, not all branches
- **C:** `cron: 'midnight'` is not valid cron syntax - must use standard 5-field format
- **D:** `push: branches: [main]` limits push triggers to only the main branch

---

## Scenario 5: Fork and Clone Workflow

**Domain:** Domain 7: Explore the GitHub community

### Scenario
A developer wants to contribute to an open source project on GitHub. They do not have write access to the original repository. They need to make changes and submit them for review by the project maintainers.

**Question:** What is the correct workflow for this developer?

**Options:**
A. Clone the repository, create a branch, make changes, and push directly to the original repository
B. Fork the repository, clone the fork locally, create a branch, make changes, push to the fork, and open a pull request to the original repository
C. Download the repository as a ZIP, make changes, and email the maintainers
D. Clone the repository, make changes on main, and open a pull request from the local clone

**Correct Answer:** B

**Explanation:**
- Forking creates a server-side copy under the developer's account
- Cloning the fork creates a local working copy
- Working on a branch keeps changes organized and the fork's main clean
- Pushing to the fork updates the developer's server-side copy
- Opening a PR from fork to original repository submits changes for review
- This is the standard open source contribution workflow

**Why other options are wrong:**
- **A:** Without write access, the developer cannot push directly to the original repository
- **C:** This bypasses GitHub's collaboration features entirely and is not standard practice
- **D:** Without write access, the developer cannot push to the original repository at all

---

## Scenario 6: Security and Access Management

**Domain:** Domain 6: Understand privacy, security, and administration

### Scenario
An organization admin notices that a team member accidentally committed an API key to a public repository. The commit has already been pushed to GitHub.

**Question:** What should the admin do to handle this situation? (Select the BEST answer)

**Options:**
A. Delete the commit from the repository history and the API key will be safe
B. Immediately rotate or revoke the exposed API key, remove the secret from the repository history (for example with git filter-repo or BFG), enable secret scanning with push protection to prevent future incidents, and review the audit log
C. Make the repository private to hide the exposed key
D. Simply delete the file containing the key and push a new commit

**Correct Answer:** B

**Explanation:**
- The API key must be rotated or revoked immediately since it was exposed publicly
- Simply removing the file does not remove it from Git history
- git filter-repo or BFG Repo-Cleaner can remove secrets from history
- Secret scanning detects committed credentials, and push protection blocks a push that contains one, so a repeat is caught before it reaches GitHub
- Audit log review helps understand the scope of potential exposure

**Why other options are wrong:**
- **A:** Even if the commit is removed from history, it may have been cached, forked, or scraped
- **C:** Making the repository private does not revoke the already-exposed key
- **D:** The key remains in Git history even if the file is deleted in a new commit

---

## Scenario 7: GitHub Projects and Issue Management

**Domain:** Domain 5: Manage projects with GitHub

### Scenario
A product manager is planning a quarterly release with 30 features across 3 teams. They need to track progress, visualize work status, and filter by team. Each team works across multiple repositories.

**Question:** Which GitHub feature best fits this use case?

**Options:**
A. Create a separate Kanban board in one repository with a column for each status
B. Use GitHub Projects with a single select Team field, board and roadmap views, and items from all the teams' repositories
C. Create separate milestone in each repository and track progress independently
D. Use GitHub Discussions to coordinate work across teams

**Correct Answer:** B

**Explanation:**
- A GitHub project belongs to the organization, not one repository, so it can track issues from every team's repositories
- Custom fields allow adding "Team" as a single-select field for filtering
- Multiple views (table, board, roadmap) show the same items from different angles
- Built-in workflows can automate status changes
- Project insights charts show progress by team or status

**Why other options are wrong:**
- **A:** A board scoped to one repository cannot see the other repositories' issues, and the old projects (classic) experience has been retired
- **C:** Separate milestones per repository create silos and no unified tracking view
- **D:** Discussions are for conversations, not project tracking and visualization

---

## Scenario 8: Open Source Licensing

**Domain:** Domain 7: Explore the GitHub community

### Scenario
A company wants to create an open source library that other companies can use in their commercial products without restriction. However, they want any modifications to the library itself to remain open source.

**Question:** Which license best fits this requirement?

**Options:**
A. MIT License - allows any use with minimal restrictions
B. GNU GPL v3 - requires all derivative works to be open source
C. GNU LGPL v3 - allows linking in proprietary software but modifications to the library must stay open source
D. Apache License 2.0 - allows any use but includes patent protection

**Correct Answer:** C

**Explanation:**
- LGPL allows the library to be used (linked) in commercial/proprietary products
- Any modifications to the LGPL-licensed library itself must remain open source
- This balances commercial friendliness with protecting the library's open source nature
- This is commonly used for libraries and frameworks

**Why other options are wrong:**
- **A:** MIT allows modifications to remain closed source - does not meet the requirement
- **B:** GPL requires ALL derivative works (including products using the library) to be open source - too restrictive for commercial use
- **D:** Apache 2.0 allows modifications to remain closed source - does not meet the requirement

---

## Scenario 9: github.dev versus Codespaces

**Domain:** Domain 4: Apply modern development practices

### Scenario
A technical writer is on a shared library computer where they cannot install software. They need to fix broken links in eight Markdown files across two folders and commit the changes in one go. Later the same week, a developer on the team wants to run the project's test suite from a browser on a similar locked-down machine.

**Question:** Which tools best fit the writer and the developer?

**Options:**
A. Both should use GitHub Desktop
B. The writer should use Codespaces; the developer should use github.dev
C. The writer should use github.dev; the developer should use Codespaces
D. Both should use the single-file pencil editor on GitHub.com

**Correct Answer:** C

**Explanation:**
- github.dev (press `.` on the repository) is a free, browser-only editor that can change many files and commit them together, which is all the writer needs
- github.dev has no terminal and cannot run code, so it cannot run tests
- Codespaces gives a full cloud virtual machine with a terminal in the browser, so the developer can install dependencies and run the test suite

**Why other options are wrong:**
- **A:** GitHub Desktop must be installed, which neither person can do
- **B:** This is the wrong way round. A codespace would work for the writer but costs compute for a task that does not need it, and github.dev cannot run the developer's tests
- **D:** The pencil editor edits one file per commit and cannot run anything

---

## Scenario 10: Choosing a Copilot plan

**Domain:** Domain 4: Apply modern development practices, and Domain 6

### Scenario
A 300-person company on GitHub Team wants every developer to use GitHub Copilot. Security requires that administrators decide which Copilot features and AI models are allowed, exclude a folder of sensitive configuration from Copilot's context, and see Copilot activity in the audit log. Developers must not pay personally.

**Question:** Which approach meets these requirements?

**Options:**
A. Ask each developer to subscribe to Copilot Pro+ and expense it
B. Ask each developer to use Copilot Free
C. Buy Copilot Pro for each developer's personal account
D. Buy Copilot Business seats for the organization and configure organization policies

**Correct Answer:** D

**Explanation:**
- Copilot Business is the organization plan: the organization buys and assigns seats
- Business includes organization-wide policy management (features, models, public code matching), content exclusion and audit logs
- Copilot Enterprise would also work but requires GitHub Enterprise Cloud, which this company does not have

**Why other options are wrong:**
- **A:** Pro+ is an individual plan; administrators cannot centrally control its policies, and developers would be paying personally
- **B:** Copilot Free is for individuals without organization access, with limited usage and no admin controls
- **C:** Pro is also an individual plan with no organization policy management, content exclusion or audit log integration

---

## Scenario 11: Company-controlled accounts

**Domain:** Domain 6: Understand privacy, security, and administration

### Scenario
A bank is moving to GitHub Enterprise Cloud. Its compliance team requires that every GitHub account used for work is created and removed automatically from the bank's identity provider, that people sign in only through that identity provider, and that work accounts cannot publish public repositories or contribute to projects outside the company.

**Question:** Which GitHub capability meets all of these requirements?

**Options:**
A. Enterprise Managed Users
B. Requiring two-factor authentication for all organization members
C. Setting the organization's base permissions to Read
D. SAML single sign-on with employees' existing personal accounts

**Correct Answer:** A

**Explanation:**
- With Enterprise Managed Users, the identity provider provisions and deprovisions accounts through SCIM
- Managed users authenticate through the identity provider, not with a GitHub password
- Managed users cannot create public content or collaborate outside the enterprise, which keeps work inside the bank

**Why other options are wrong:**
- **B:** 2FA strengthens sign-in but does not control account creation or block outside activity
- **C:** Base permissions set default repository access inside the organization; they do not affect identity or public activity
- **D:** With SAML SSO on personal accounts, employees still own their accounts and can contribute publicly; the identity provider does not create or remove the GitHub account itself

---

## Scenario 12: Agent mode or the coding agent

**Domain:** Domain 4: Apply modern development practices

### Scenario
A team lead has a backlog of small, well-described issues such as "add unit tests for the date parser". She wants Copilot to work on them in the background while she is in meetings and hand back changes that go through the team's normal pull request review and branch rules.

**Question:** Which Copilot feature best fits?

**Options:**
A. Inline code suggestions in her IDE
B. Copilot Chat in GitHub Mobile
C. Agent mode in VS Code
D. The Copilot coding agent (Copilot cloud agent), assigned to each issue

**Correct Answer:** D

**Explanation:**
- The coding agent runs on GitHub in its own Actions-powered environment, so it works while she is away
- It is started from an issue and returns its work as a pull request, so normal review and branch protections apply

**Why other options are wrong:**
- **A:** Inline suggestions only help while someone is typing
- **B:** Chat answers questions; on its own it does not take an issue through to a reviewed pull request
- **C:** Agent mode is powerful but runs in her IDE and needs her there to steer and approve; it is synchronous, not background work
