---
last-updated: 2026-10-22
applies-to: GH-900 skills measured as of January 2026, checked 2026-10-22
difficulty: beginner
---

# Domain 2: Work with GitHub repositories (10-15%)

This domain is about the repository itself: what a well-built repository contains, how to create and organize one, how to add and manage files, what the Insights tab tells you, and how to keep a repository healthy over time.

**[📖 GH-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900)** - the official skills list
**[📖 About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)** - repository overview
**[📖 Quickstart for repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories)** - create your first repository

## Repository structure and key files

A repository is more than code. A newcomer landing on it should be able to answer: what is this, can I use it, how do I help, who owns which part, and how do I report a security problem? GitHub recognises a set of special files that answer those questions, and it treats them specially in the UI.

### README

The README is the front page. GitHub renders `README.md` (or `README`, `README.rst` and similar) below the file list. A good README says what the project does, how to install and use it, how to get help and how to contribute. If a repository has READMEs in more than one place, GitHub shows the one in `.github/` first, then the root, then `docs/`.

There is also a special case: a public repository with the same name as your username (for example `octocat/octocat`) shows its README on your profile page. That is your **profile README**.

**[📖 About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)** - what to include and where GitHub looks

### LICENSE

A license tells others what they may legally do with the code. Without one, normal copyright applies and nobody has permission to copy, modify or distribute the work, even if the repository is public. That surprises many beginners. You can pick a license from a template when creating the repository, and GitHub then shows a license summary in the sidebar.

> **Exam trap:** "Public" is about visibility, not permission. A public repository with no LICENSE is viewable but not open source.

**[📖 Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)** - choosing and adding a license

### CONTRIBUTING

`CONTRIBUTING.md` explains how to contribute: how to set up the project, coding style, how to run tests, how to name branches and what makes a good pull request. GitHub links it when someone opens an issue or pull request, so contributors see it at the right moment.

### CODEOWNERS

A `CODEOWNERS` file maps file paths to the people or teams responsible for them. When a pull request touches a matching path, GitHub automatically requests a review from those owners. Combined with a branch protection rule or ruleset that requires code owner review, it also blocks the merge until an owner approves.

```text
# .github/CODEOWNERS
*           @acme/maintainers
*.js        @acme/frontend
/docs/      @acme/docs-team
/infra/     @alice @acme/platform
```

The file can live in the root, `docs/` or `.github/`. Patterns work like `.gitignore`, and the **last** matching pattern wins, which is why the catch-all `*` usually goes first.

**[📖 About code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)** - syntax and behaviour

### SECURITY

`SECURITY.md` is the repository's security policy. It tells people how to report a vulnerability privately rather than opening a public issue that would tip off attackers. GitHub shows it on the Security tab. Pair it with **private vulnerability reporting**, which lets researchers submit a report directly through GitHub.

**[📖 Adding a security policy](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository)** - creating SECURITY.md

### The rest of the community health set

| File | Purpose |
|------|---------|
| `README.md` | What the project is and how to use it |
| `LICENSE` | Legal terms for reuse |
| `CONTRIBUTING.md` | How to contribute |
| `CODE_OF_CONDUCT.md` | Expected behaviour in the community |
| `SECURITY.md` | How to report a vulnerability |
| `SUPPORT.md` | Where to get help |
| `CODEOWNERS` | Who must review which paths |
| `.github/FUNDING.yml` | Shows a Sponsor button |
| `.github/ISSUE_TEMPLATE/` | Issue forms and templates |
| `.github/pull_request_template.md` | Default PR description |
| `.gitignore` | Files Git should not track |

An organization can create a public repository named `.github` and put default community health files in it. Any repository in the organization that lacks its own copy uses the default. Public repositories also get a **Community Standards** checklist under Insights that shows which of these files are present.

- **README** - the rendered front page of a repository explaining what it is and how to use it.
- **LICENSE** - a file granting legal permission to use, modify and share the code; without it, all rights are reserved.
- **CONTRIBUTING** - guidelines that GitHub links when someone opens an issue or pull request.
- **CODEOWNERS** - a file mapping paths to owners who are automatically requested for review.
- **SECURITY.md** - the security policy describing how to report vulnerabilities privately.
- **Community health files** - the standard set of files (code of conduct, contributing, security, support) that can be defaulted from an organization's `.github` repository.

**[📖 Creating a default community health file](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)** - organization-wide defaults

## Create, organize and maintain repositories

### Creating a repository

From the **+** menu on GitHub.com you choose an owner (you or an organization), a name, a description, a visibility and optional starter files (README, `.gitignore` template, license). You can also create one with `gh repo create`, GitHub Desktop, or the REST API.

Visibility is chosen at creation and can be changed later in settings. Public repositories are visible to everyone. Private repositories are visible only to people given access. Internal repositories, available to organizations in an enterprise, are visible to every member of the enterprise. Domain 6 covers visibility in detail.

### Template repositories

Mark a repository as a **template** in its settings, and others can click **Use this template** to create a new repository with the same files and folders. The new repository starts with fresh history and no link back to the template. You can optionally include all branches.

Compare that with a **fork**. A fork is a copy that keeps a connection to the original (the upstream), shares its history, and exists so you can propose changes back with a pull request.

| Need | Use |
|------|-----|
| Start a new project from a standard skeleton | Template |
| Contribute changes back to someone else's project | Fork |
| Work on a repository you already have write access to | Clone and branch |

> **Exam trap:** "Standardize the starting structure of new microservice repositories across the company" is a template question. Forking would tie every new service to the original's history and network.

**[📖 Creating a template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository)** - set up a template
**[📖 Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)** - use one

### Organizing with branches

Branches organize work in progress. The **default branch** (usually `main`) is what visitors see and what pull requests target by default. You can rename it in settings, and GitHub redirects old links. Good habits: short-lived feature branches, clear names (`feature/search`, `fix/login-timeout`), and protection on `main` so changes arrive through reviewed pull requests.

**[📖 About branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)** - branch concepts on GitHub

## Add and manage files

There are three common ways to get files into a repository, and the exam can ask which suits a situation.

**In the web UI**, open the repository and choose **Add file**, then **Create new file** or **Upload files**. You can drag and drop files. Each save is a commit, and GitHub asks whether to commit straight to the current branch or to create a new branch and open a pull request. On a protected branch, the second option is the one that works. You can also edit a file in place with the pencil icon, rename it by changing its name, or delete it from the file menu.

**With Git on your machine**, you edit files locally, then `git add`, `git commit` and `git push`. This is the normal route for real development, because you can run and test the code first.

**In a browser editor**, press `.` on a repository to open github.dev, a lightweight VS Code in the browser that can edit many files and commit them together. Domain 4 compares it with Codespaces.

Some practical limits: the web upload limit is 25 MB per file, and GitHub blocks files over 100 MB pushed with Git. Large binaries belong in **Git Large File Storage (Git LFS)**, which stores a pointer in the repository and the file content elsewhere.

**[📖 Adding a file to a repository](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)** - web and command line
**[📖 About large files on GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)** - limits and Git LFS

## Repository insights and metrics

The **Insights** tab is the repository's built-in metrics dashboard. Each view answers a different question, and look-alike views are a favourite exam topic.

| Insights view | Question it answers |
|---------------|--------------------|
| **Pulse** | What happened recently? A summary of merged and open PRs, closed and new issues for a chosen period |
| **Contributors** | Who contributes, and how much, over time (commits on the default branch) |
| **Community standards** | Which community health files does this public repository have? |
| **Traffic** | How many views and clones in the last 14 days, top referrers and popular content (people with push access only) |
| **Commits** | Commit activity per week over the last year |
| **Code frequency** | Lines added and removed per week |
| **Dependency graph** | Which packages this repository depends on and which repositories depend on it |
| **Network** | The branch and fork history as a graph |
| **Forks** | Who has forked the repository |

> **Exam trap:** Traffic data covers only the last 14 days and is visible only to people with write (push) access or above. If a question asks why a read-only member cannot see clone counts, that is why.

### Dependency insights

The **dependency graph** is built from manifest and lock files (such as `package.json`, `requirements.txt` or `pom.xml`). It lists dependencies, their versions and their licenses, and it is the foundation for Dependabot alerts. You can export it as a software bill of materials (SBOM). At organization level, GitHub Enterprise Cloud adds **dependency insights**, a view across all the organization's repositories that answers questions like "which of our repositories use this vulnerable package?" or "which licenses do we depend on?".

**[📖 About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph)** - how it is built
**[📖 Viewing a project's contributors](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-a-projects-contributors)** - one of the Insights views
**[📖 Viewing traffic to a repository](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository)** - traffic rules

### Stars and feature previews

**Starring** a repository bookmarks it in your stars list and shows appreciation. The star count is a rough signal of popularity. You can group stars into lists. Starring does not subscribe you to notifications: that is **watching**, covered in Domain 3.

**Feature preview** is the menu (under your profile picture) where you can switch on early versions of new GitHub features before they become the default, and switch them off again. It is how GitHub lets users try changes such as new UI layouts at their own pace.

- **Pulse** - the Insights summary of recent pull request and issue activity.
- **Traffic** - the Insights view of views, clones and referrers over the last 14 days, for people with push access.
- **Dependency graph** - the list of packages a repository depends on and that depend on it, built from manifest files.
- **Dependency insights** - an organization-wide view of dependencies, vulnerabilities and licenses across repositories.
- **Star** - a bookmark and a public signal of appreciation; not a notification subscription.
- **Feature preview** - a user setting to opt in to early versions of new GitHub features.

## Maintenance best practices

A repository that is easy to find and safe to depend on takes ongoing care.

**Describe it.** Add a short description, a website link and **topics** (tags like `python`, `machine-learning`). Topics make the repository discoverable in search and on topic pages.

**Keep branches tidy.** Turn on **Automatically delete head branches** so merged PR branches disappear. Delete stale branches. Protect the default branch.

**Keep dependencies current.** Enable the dependency graph, Dependabot alerts and Dependabot updates so vulnerable or outdated packages are flagged and patched through pull requests.

**Use releases and tags.** Tag versions and publish **releases** with notes so users know what changed.

**Archive when done.** When a project is finished but should stay readable, **archive** it. An archived repository becomes read-only: no new issues, pull requests, comments or pushes. It is still visible and can be forked, and it can be unarchived later. Deleting is permanent after a short restore window and breaks everyone who depends on it, so archiving is usually the better choice.

> **Exam trap:** Archiving is not the same as making a repository private. Archiving freezes it; visibility controls who can see it. You can archive a public repository and it stays public.

**[📖 Archiving repositories](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories)** - what archiving does
**[📖 Classifying your repository with topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)** - add topics
**[📖 Managing the automatic deletion of branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-the-automatic-deletion-of-branches)** - tidy merged branches

## Key exam points

- README explains, LICENSE permits, CONTRIBUTING guides, CODEOWNERS routes reviews, SECURITY.md routes vulnerability reports.
- No LICENSE means all rights reserved, even on a public repository.
- CODEOWNERS can live in root, `docs/` or `.github/`; the last matching pattern wins.
- An organization's `.github` repository supplies default community health files.
- Templates give a fresh copy with no link; forks keep the upstream link.
- Insights: Pulse is recent activity, Contributors is who, Traffic is 14 days of views and clones, Dependency graph is packages.
- Stars bookmark; watching notifies.
- Archive makes a repository read-only without deleting it.
