---
last-updated: 2026-10-22
applies-to: GH-900 skills measured as of January 2026, checked 2026-10-22
difficulty: beginner
---

# GitHub Foundations Certification Fact Sheet

## Exam Overview

**Exam Name:** GitHub Foundations
**Exam Code:** GH-900
**Duration:** 100 minutes
**Questions:** Not published by Microsoft
**Format:** Multiple choice; may include interactive components
**Passing Score:** 700 (scale 1-1000)
**Cost:** Based on country; commonly listed as $99 USD in the US
**Delivery:** Proctored, through Pearson VUE via Microsoft Learn
**Languages:** English, Spanish, Portuguese (Brazil), Korean, Japanese
**Prerequisites:** None
**Valid For:** Does not expire (no renewal required)

**[📖 GitHub Foundations certification page](https://learn.microsoft.com/en-us/credentials/certifications/github-foundations/)** - registration and policies
**[📖 GH-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900)** - skills measured as of January 2026
**[📖 GitHub Foundations learning path, part 1](https://learn.microsoft.com/en-us/training/paths/github-foundations/)** - free modules
**[📖 GitHub Foundations learning path, part 2](https://learn.microsoft.com/en-us/training/paths/github-foundations-2/)** - free modules, continued

Retakes: wait 24 hours before the first retake, then Microsoft's retake policy applies. Scores are on Microsoft's 1-1000 scale, so 700 is not the same as "70% correct".

## Domain Weights

| # | Domain | Weight | Notes |
|---|--------|--------|-------|
| 1 | Understand Git and GitHub basics | 25-30% | [notes/01-git-and-github-basics.md](notes/01-git-and-github-basics.md) |
| 2 | Work with GitHub repositories | 10-15% | [notes/02-repositories.md](notes/02-repositories.md) |
| 3 | Collaborate using GitHub | 10-15% | [notes/03-collaboration.md](notes/03-collaboration.md) |
| 4 | Apply modern development practices | 10-15% | [notes/04-modern-development.md](notes/04-modern-development.md) |
| 5 | Manage projects with GitHub | 5-10% | [notes/05-project-management.md](notes/05-project-management.md) |
| 6 | Understand privacy, security, and administration | 10-15% | [notes/06-privacy-security-administration.md](notes/06-privacy-security-administration.md) |
| 7 | Explore the GitHub community | 5-10% | [notes/07-github-community.md](notes/07-github-community.md) |

## Domain 1: Understand Git and GitHub basics (25-30%)

**Version control** records every change with author and message, enables collaboration, recovery and parallel work on branches.

| | Git | GitHub |
|-|-----|--------|
| What | Distributed version control tool | Cloud platform hosting Git repositories |
| Runs | Your machine | github.com (or self-hosted Enterprise Server) |
| Adds | Commits, branches, merges | PRs, issues, Actions, Projects, security, Copilot |

**Core objects:** repository (files plus history), commit (snapshot with SHA, author, message), branch (movable pointer), HEAD (what you have checked out), remote (`origin`).

| Command | Purpose |
|---------|---------|
| `git clone` | Copy a remote repository with full history |
| `git add` / `git commit` | Stage, then record a snapshot |
| `git fetch` | Download, do not merge |
| `git pull` | Fetch and merge |
| `git push` | Upload commits |
| `git switch -c` | Create and switch branch |
| `git merge` / `git rebase` | Join histories / replay commits linearly |
| `git revert` | New commit undoing an old one (safe on shared history) |
| `git reset` | Move branch pointer back (rewrites history) |
| `git stash` | Shelve uncommitted work |

**Accounts:** personal (a person), organization (shared ownership, roles and teams), enterprise (governs many organizations). **Enterprise options:** Enterprise Cloud (hosted by GitHub) or Enterprise Server (self-hosted). **Plans:** Free, Pro, Team, Enterprise. Free includes unlimited private repositories.

**GitHub Flow:** branch from `main` -> commit -> open PR -> review and checks -> merge -> delete branch. `main` always deployable.

**Markdown:** GitHub Flavored Markdown in issues, PRs, READMEs. `@user` notifies, `#123` links, `- [ ]` task lists, `> [!NOTE]` alerts, Mermaid diagrams.

**Tools:** Desktop = visual Git on Windows/macOS. Mobile = notifications, reviews, merges and 2FA approvals on iOS/Android. CLI (`gh`) = GitHub in the terminal.

## Domain 2: Work with GitHub repositories (10-15%)

| File | Purpose |
|------|---------|
| `README.md` | Front page |
| `LICENSE` | Reuse rights; none means all rights reserved |
| `CONTRIBUTING.md` | How to contribute; linked on new issues and PRs |
| `CODEOWNERS` | Auto-request reviews by path; last match wins; root, `docs/` or `.github/` |
| `SECURITY.md` | How to report vulnerabilities privately |
| `CODE_OF_CONDUCT.md`, `SUPPORT.md`, `.github/FUNDING.yml` | Behaviour, help, Sponsor button |

- Organization `.github` repository supplies default community health files.
- **Template** = fresh history, no link. **Fork** = linked copy for contributing back.
- Add files: web UI (create or upload, 25 MB per file), Git push (100 MB hard limit; use Git LFS for large files), or github.dev.
- **Insights:** Pulse (recent activity), Contributors, Community standards, Traffic (14 days, push access only), Commits, Code frequency, Dependency graph, Network, Forks.
- **Dependency insights:** organization-wide dependency and license view (Enterprise Cloud).
- **Stars** bookmark; **feature preview** opts you into early UI features.
- **Maintenance:** description and topics, auto-delete head branches, Dependabot, releases, **archive** to make read-only.

## Domain 3: Collaborate using GitHub (10-15%)

| Feature | For |
|---------|-----|
| Issue | Tracked work (bug, feature, task); sub-issues and issue types |
| Pull request | Proposed code change with review and checks |
| Discussion | Questions, ideas, announcements; Q&A can mark an answer |

- Draft PRs cannot be merged. Reviews: Comment, Approve, Request changes.
- Merge methods: merge commit, squash and merge, rebase and merge.
- **Closing keywords:** close(s/d), fix(es/ed), resolve(s/d) + `#123`; only closes on merge to the **default branch**.
- Templates: `.github/ISSUE_TEMPLATE/` (Markdown or YAML forms, `config.yml`), `pull_request_template.md`.
- Filters: `is:issue is:open label:bug assignee:@me`, `review-requested:@me`, `no:assignee`.
- Assignees (up to 10) do the work; reviewers review.
- **Watch levels:** Participating and @mentions (default), All Activity, Ignore, Custom (pick issues, PRs, releases, discussions, security alerts).
- Inbox: Done, Save, Unsubscribe, custom filters; delivery to web, email, Mobile.
- **Gist** = snippet repo, public or secret (secret = unlisted, not private). **Wiki** = repo docs pages. **Pages** = static site hosting; `<owner>.github.io` user/org site, `/<repo>` project site.

## Domain 4: Apply modern development practices (10-15%)

- **Actions:** workflows (YAML in `.github/workflows/`) triggered by events; jobs on runners; steps run commands or actions. CI/CD plus any repository automation. Results become status checks.
- **Copilot features:** inline suggestions, Chat, agent mode, coding agent (now Copilot cloud agent), code review, multi-model choice.
- **Agent mode** = IDE, synchronous, edits and runs tests while you watch. **Coding agent** = GitHub, asynchronous, from an assigned issue to a pull request.
- **Plans:** Free, Pro, Pro+ (individual; GitHub also lists Student and Max) and Business, Enterprise (organization seats). Usage metered in GitHub AI Credits.
- **Business/Enterprise add:** policy management, model control, content exclusion, audit logs, IP indemnity; Enterprise adds a larger credit pool and enterprise capabilities (knowledge bases in the outline; Copilot Spaces today).
- **Codespaces:** cloud VM dev environment, defined by `.devcontainer/devcontainer.json`, billed compute while running plus storage while it exists.
- **github.dev:** press `.`; free, browser-only, no terminal, cannot run code.

## Domain 5: Manage projects with GitHub (5-10%)

- **Projects:** owned by a user or organization; items from many repositories plus draft issues. Projects (classic) retired.
- **Layouts:** table (spreadsheet), board (Kanban), roadmap (timeline).
- **Field types:** text, number, date, single select, iteration.
- **Built-in workflows:** item closed or PR merged -> Done, item added -> status, reopened, auto-add by filter, auto-archive.
- **Insights:** charts (bar, column, line, stacked area), current and historical.
- **Labels** many per item; **milestone** one per item with due date and progress; **assignees** up to 10; **saved replies** personal canned responses.

## Domain 6: Understand privacy, security, and administration (10-15%)

- **2FA methods:** authenticator app (TOTP), security key, passkey, GitHub Mobile, SMS (weakest). Keep recovery codes. Required for code contributors on GitHub.com.
- **Passkeys:** phishing-resistant, can satisfy both password and 2FA in one step.
- **Repository roles:** Read < Triage < Write < Maintain < Admin.
- **Organization roles:** Owner, Member, Moderator, Billing manager, Security manager; outside collaborators are not members. Base permissions set default repo access.
- **Teams:** grant access in bulk; nested teams inherit; visible or secret.
- **EMUs:** accounts provisioned by the identity provider via SCIM, sign in via IdP, username suffix, no public activity outside the enterprise (Enterprise Cloud).
- **Copilot policies:** set by enterprise and organization owners (features, models, public code matching, content exclusion, seats).
- **Visibility:** public, private, internal (enterprise only, for InnerSource).
- **Branch protection rule:** one per branch pattern, one repository. **Ruleset:** layered, bypass list, Active/Evaluate/Disabled, branch/tag/push, organization-wide on Enterprise, visible to readers.
- **Security awareness:** Dependabot (packages), secret scanning plus push protection (credentials), code scanning with CodeQL (code), security advisories.

## Domain 7: Explore the GitHub community (5-10%)

- Open source benefits: quality, speed, shared cost, learning, transparency, no lock-in.
- **Permissive:** MIT, Apache 2.0 (patent grant), BSD. **Copyleft:** GPL. **Weak copyleft:** LGPL.
- GitHub supports open source: free public-repo features, Sponsors, Advisory Database, Stars programme, Education, Archive Program.
- **Sponsors** funds maintainers; `.github/FUNDING.yml` shows the Sponsor button.
- **Follow** people and orgs (feed), **star** repos (bookmark), **watch** repos (notifications).
- **Discovery:** topics, Explore, Trending, Collections, `good first issue`.
- **Marketplace:** apps (installed) and actions (referenced in workflows); verified creators.
- **InnerSource:** open source practice inside a company; internal repositories.
- **Fork vs template:** fork keeps link and history; template starts fresh with no link.

## Key Differentiators

| A | B | Difference |
|---|---|-----------|
| Git | GitHub | Tool vs platform |
| `git fetch` | `git pull` | Download only vs download and merge |
| `git revert` | `git reset` | New undo commit vs rewrite history |
| Fork | Template | Linked copy vs fresh copy |
| Issue | Discussion | Tracked work vs conversation |
| Star | Watch | Bookmark vs notifications |
| Agent mode | Coding agent | IDE, synchronous vs GitHub, asynchronous PR |
| github.dev | Codespaces | Free browser editor vs billed cloud VM with terminal |
| Triage | Maintain | Manage issues/PRs vs manage repo without destructive settings |
| Branch protection rule | Ruleset | One per branch, one repo vs layered, org-wide |
| Label | Milestone | Many categories vs one goal with due date |
| Personal + SAML SSO | EMU | Person owns account vs company owns account |
