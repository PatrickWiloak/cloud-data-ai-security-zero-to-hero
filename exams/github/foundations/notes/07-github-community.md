---
last-updated: 2026-10-22
applies-to: GH-900 skills measured as of January 2026, checked 2026-10-22
difficulty: beginner
---

# Domain 7: Explore the GitHub community (5-10%)

This domain covers GitHub as a community: what open source is and why people do it, how GitHub supports it (including Sponsors), how to follow people and discover projects, GitHub Marketplace, InnerSource inside companies, and the difference between forks and templates.

**[📖 GH-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900)** - the official skills list
**[📖 Open Source Guides](https://opensource.guide/)** - GitHub-backed guides to running and contributing to open source
**[📖 Contributing to a project](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project)** - the fork and pull request route

## Open source and its benefits

**Open source** software publishes its source code under a license that lets anyone use, study, change and share it. Linux, Kubernetes, Python, VS Code and React are all open source, and most commercial software is built on open source libraries.

Why do people and companies take part?

- **Quality through many eyes** - more reviewers find more bugs, including security bugs.
- **Speed** - you build on existing libraries instead of writing everything yourself.
- **Shared cost** - companies that all need the same tool can maintain it together.
- **Learning and career** - contributions are public evidence of skill, and reading real code is how many people learn.
- **Transparency and trust** - you can inspect exactly what the software does.
- **Avoiding lock-in** - if a vendor disappears, the code is still there.

### Licenses at awareness level

A license is what turns "public code" into "open source". Without one, nobody may legally reuse the code (Domain 2). Licenses fall into two families:

**Permissive** licenses allow almost anything, including use in closed-source products, as long as you keep the copyright notice. Examples: **MIT** (short and simple), **Apache 2.0** (adds an explicit patent grant) and **BSD**.

**Copyleft** licenses require that if you distribute a modified version, you release it under the same license. Example: **GPL**. The **LGPL** is a weaker form aimed at libraries: you can link to the library from proprietary software, but changes to the library itself must stay open.

| License | Family | Key point |
|---------|--------|-----------|
| MIT | Permissive | Minimal conditions: keep the notice |
| Apache 2.0 | Permissive | Explicit patent grant |
| GPL v3 | Copyleft | Distributed derivatives must also be GPL |
| LGPL v3 | Weak copyleft | Linking allowed; library changes stay open |

GitHub helps here: choose a license template when creating a repository, and the sidebar shows a plain-language summary of permissions, conditions and limitations. **choosealicense.com**, run by GitHub, explains the options.

> **Exam trap:** "Free to view on GitHub" does not mean "free to reuse". Check the LICENSE file.

**[📖 Choose a license](https://choosealicense.com/)** - GitHub's license chooser
**[📖 Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)** - adding a license

### How to contribute

The standard path for a project you cannot push to:

1. Find a project and read its README, CONTRIBUTING and CODE_OF_CONDUCT.
2. Look for issues labelled `good first issue` or `help wanted`.
3. **Fork** the repository, clone your fork, and create a branch.
4. Make the change, commit and push to your fork.
5. Open a pull request from your fork to the original repository.
6. Respond to review feedback until it is merged.

Contributing is not only code. Documentation fixes, translations, triaging issues, answering discussions and reporting good bugs all help.

## How GitHub supports open source

GitHub invests in open source in several ways, and the exam may ask you to recognise them:

- **Free features for public repositories** - unlimited public repositories, free Actions minutes on standard GitHub-hosted runners, and security features such as Dependabot alerts, secret scanning and code scanning at no cost.
- **GitHub Sponsors** - direct funding for maintainers (see below).
- **Community health tooling** - templates, community standards checklist, Discussions and moderation tools.
- **Security help** - the GitHub Advisory Database, private vulnerability reporting and security advisories with CVE requests.
- **Programmes** - for example GitHub Stars (recognising community leaders), GitHub Education for students and teachers, and the GitHub Archive Program, which preserves public code for the long term.

### GitHub Sponsors

**GitHub Sponsors** lets individuals and companies fund the developers and organizations behind open source, with one-time or monthly payments. A maintainer sets up a Sponsors profile with tiers and goals. Adding a `.github/FUNDING.yml` file makes a **Sponsor** button appear on the repository, which can point to GitHub Sponsors and to other platforms such as Open Collective or Patreon.

Why it matters: much of the world's software depends on a few unpaid maintainers. Sponsors gives them a sustainable income from the people who rely on their work.

- **GitHub Sponsors** - GitHub's programme for funding open source developers and organizations directly.
- **FUNDING.yml** - a file in `.github/` that shows a Sponsor button linking to funding platforms.
- **GitHub Stars** - GitHub's recognition programme for influential community members; unrelated to starring a repository.

> **Exam trap:** "Starring" a repository (a bookmark) and the "GitHub Stars" programme (people) are different things.

**[📖 About GitHub Sponsors](https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors)** - how sponsorship works
**[📖 Displaying a sponsor button in your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository)** - FUNDING.yml

## Following, starring and discovering

### Following users and organizations

**Following** a user or an organization puts their public activity (new repositories, stars, releases) in your personal dashboard feed. It is how you keep up with people whose work you admire. Following does not give you access to anything and does not subscribe you to repository notifications.

| Action | Applies to | Effect |
|--------|-----------|--------|
| **Follow** | A user or organization | Their public activity appears in your feed |
| **Star** | A repository | Bookmarks it and shows appreciation |
| **Watch** | A repository | Sends you notifications at the chosen level |

> **Exam trap:** If the question asks how to get notified about new releases of a project, the answer is **watch** with a custom level including releases, not star or follow.

**[📖 Following people](https://docs.github.com/en/get-started/exploring-projects-on-github/following-people)** - what following does
**[📖 Saving repositories with stars](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars)** - stars and lists

### Discoverable repositories: topics and Explore

**Topics** are tags a repository owner adds (like `react`, `terraform` or `hacktoberfest`). Each topic has its own page listing public repositories with that tag, so adding accurate topics makes a project easier to find.

**Explore** (github.com/explore) is GitHub's discovery hub. It includes **Trending** repositories and developers, **Topics**, curated **Collections** around a theme, and recommendations based on your activity. Search with qualifiers such as `topic:python stars:>1000 good-first-issues:>5` narrows things further.

**[📖 Finding ways to contribute to open source on GitHub](https://docs.github.com/en/get-started/exploring-projects-on-github/finding-ways-to-contribute-to-open-source-on-github)** - Explore, topics and good first issues
**[📖 GitHub Explore](https://github.com/explore)** - the discovery hub

## GitHub Marketplace

**GitHub Marketplace** (github.com/marketplace) is where you find tools that extend GitHub. It lists two kinds of thing:

- **Apps** - integrations installed on an account or organization, such as CI services, code quality tools, project management bridges or chat notifications. Some are free, some paid, billed through GitHub.
- **Actions** - reusable building blocks for GitHub Actions workflows, referenced with `uses:`.

Creators can be **verified** by GitHub, which signals that GitHub has confirmed who the publisher is. Verified does not mean the code is audited, so review what you install and pin actions to a version.

> **Exam trap:** You install a Marketplace **app** on an account or organization. You use a Marketplace **action** by referencing it in a workflow file; there is nothing to install.

**[📖 About GitHub Marketplace for apps](https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/about-github-marketplace-for-apps)** - apps in Marketplace
**[📖 GitHub Marketplace](https://github.com/marketplace)** - browse apps and actions

## InnerSource

**InnerSource** means using open source practices inside a company. Instead of each team guarding its code, teams make code visible across the company, accept pull requests from other teams, document how to contribute, and discuss in the open.

Why do it? It reduces duplicated work (three teams writing three logging libraries), breaks down silos, spreads knowledge, and lets a team with a need fix a shared tool rather than wait in a queue.

GitHub supports InnerSource with **internal repositories** (visible to everyone in the enterprise but not the public; see Domain 6), CONTRIBUTING and CODEOWNERS files, templates, forks inside the enterprise, Discussions and search across the company's code.

> **Exam trap:** InnerSource code is not public. It is shared across the company only, which is exactly what internal visibility is for.

- **Open source** - software whose code is published under a license allowing use, study, change and redistribution.
- **Permissive license** - a license such as MIT or Apache 2.0 that allows reuse in closed-source products.
- **Copyleft license** - a license such as GPL that requires distributed derivatives to use the same license.
- **InnerSource** - applying open source practices to code shared inside one company.
- **Topic** - a tag on a public repository that makes it discoverable on topic pages and in search.
- **GitHub Marketplace** - the catalogue of apps and actions that extend GitHub.

**[📖 InnerSource on GitHub](https://resources.github.com/innersource/fundamentals/)** - InnerSource fundamentals

## Forks versus templates

Both start a new repository from an existing one, so the exam likes to contrast them.

A **fork** is a copy of a repository under your account that keeps a link to the original (the **upstream**). It shares the original's history and appears in its fork network. You can sync changes from upstream and open pull requests back to it. Forks are the open source contribution mechanism.

A **template** produces a brand-new repository with the template's files (and optionally branches) but **fresh history** and **no link** to the source. There is no syncing and no pull request path back. Templates are for starting projects, not contributing.

| | Fork | Template |
|-|------|----------|
| History | Shared with the original | Starts fresh |
| Link to source | Yes (upstream, fork network) | No |
| Pull requests back to source | Yes | No |
| Typical use | Contribute to someone else's project | Start a new project from a standard skeleton |

> **Exam trap:** A fork of a public repository is public. You cannot make a fork of a public repository private while it stays a fork. If you need a private copy with no link, use a template (if available) or create a new repository and push the code.

**[📖 About forks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks)** - what a fork is
**[📖 Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)** - templates

## Key exam points

- Open source benefits: quality, speed, shared cost, learning, transparency.
- Permissive (MIT, Apache 2.0) versus copyleft (GPL); LGPL is weak copyleft for libraries.
- GitHub supports open source with free public-repo features, Sponsors, security tooling and programmes.
- `.github/FUNDING.yml` shows the Sponsor button.
- Follow is for people and organizations; star bookmarks; watch notifies.
- Topics and Explore make projects discoverable.
- Marketplace lists apps (installed) and actions (referenced in workflows).
- InnerSource is open source practice inside a company, using internal repositories.
- Forks keep a link and history; templates start fresh with no link.
