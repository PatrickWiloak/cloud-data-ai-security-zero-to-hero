---
last-updated: 2026-10-22
applies-to: GH-900 skills measured as of January 2026, checked 2026-10-22
difficulty: beginner
---

# Domain 3: Collaborate using GitHub (10-15%)

This domain covers the features people use to work together: issues, pull requests and discussions; linking, templates, filters and assignments; notifications and how to tune them; and the three publishing-style features, Gists, Wikis and GitHub Pages.

**[📖 GH-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900)** - the official skills list
**[📖 About issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)** - issues overview
**[📖 About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)** - pull requests overview
**[📖 About discussions](https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/about-discussions)** - discussions overview

## Issues, pull requests and discussions

These three features look similar (each is a thread with comments) but they do different jobs. Picking the right one is the most common question in this domain.

| Feature | Use it for | Ends when |
|---------|-----------|-----------|
| **Issue** | A unit of work to track: a bug, a feature, a task | It is closed as completed or not planned |
| **Pull request** | Proposing a specific code change for review and merge | It is merged or closed |
| **Discussion** | Open-ended conversation: questions, ideas, announcements | It is answered, or simply goes quiet |

The rule of thumb: if there is work to do, it is an issue. If there is code to review, it is a pull request. If people want to talk, ask or brainstorm without a clear piece of work, it is a discussion. Discussions can be converted into issues once a concrete task appears, and issues can be converted into discussions when they turn out to be questions.

### Issues

An issue has a title and a Markdown body, and it carries metadata in the sidebar: **assignees**, **labels**, a **milestone**, **projects**, an **issue type** where the organization has defined them (such as Bug or Feature), and a **Development** section showing linked branches and pull requests. Large pieces of work can be broken into **sub-issues**, which show progress on the parent. Issues are numbered per repository, and that number is shared with pull requests, so `#42` is either one.

Closing an issue asks for a reason: **completed** or **not planned** (for duplicates, won't-fix and so on). That keeps reports honest about what actually got done.

### Pull requests

A pull request asks to merge one branch (the **head** or compare branch) into another (the **base**, usually `main`). The PR page has a **Conversation** tab, a **Commits** tab, a **Checks** tab for automated results and a **Files changed** tab for review.

A **draft pull request** signals that the work is not ready. It cannot be merged and does not request code owner reviews until it is marked **Ready for review**. Opening a draft early is good practice: it shares direction before you invest too much.

Reviewers can leave three kinds of review: **Comment** (feedback without a verdict), **Approve**, or **Request changes**. A reviewer can also write a **suggested change**, a code block the author can commit with one click.

When it is time to merge, GitHub offers three methods, which repository admins can enable or disable:

| Method | Result on the base branch |
|--------|---------------------------|
| **Create a merge commit** | All commits kept, plus a merge commit joining the branches |
| **Squash and merge** | All the PR's commits combined into one new commit |
| **Rebase and merge** | Each commit replayed on top of the base, no merge commit |

Squash is popular for keeping `main` readable when a branch has many small "fix typo" commits. Merge commits keep the full story. Rebase gives a straight line but rewrites commit SHAs.

**[📖 About pull request reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews)** - review types
**[📖 About merge methods on GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github)** - the three merge options

### Discussions

Discussions are a forum inside a repository or an organization. They are organized into **categories**, and the defaults are Announcements, General, Ideas, Polls, Q&A and Show and tell. In a **Q&A** category, the asker or a maintainer can **mark an answer**, which pins it under the question. Maintainers can pin important discussions and lock heated ones. Discussions must be turned on in the repository settings.

Why bother? Without Discussions, questions and ideas pile up as issues, and the issue list stops being a reliable list of work.

- **Issue** - a tracked unit of work such as a bug, feature or task.
- **Pull request** - a proposal to merge changes from a head branch into a base branch, with review and checks.
- **Draft pull request** - a pull request marked not ready; it cannot be merged until marked ready for review.
- **Discussion** - a forum-style thread for questions, ideas and announcements that is not a unit of work.
- **Sub-issue** - an issue nested under a parent issue to break down larger work.

## Linking, templates, filters and assignments

### Linking pull requests to issues

When a pull request resolves an issue, link them. The issue then shows the PR in its Development section, and the issue closes automatically when the PR merges.

The easy way is a **closing keyword** in the PR description followed by the issue number:

```text
Fixes #123
Closes octo-org/other-repo#45
```

The supported keywords are `close`, `closes`, `closed`, `fix`, `fixes`, `fixed`, `resolve`, `resolves` and `resolved`. You can also link manually from the Development section of the PR or issue sidebar.

> **Exam trap:** Automatic closing happens only when the pull request merges into the repository's **default branch**. A PR merged into a `release` branch with "Fixes #12" will not close issue 12. Also, simply mentioning `#123` without a keyword creates a cross-reference, not a closing link.

**[📖 Linking a pull request to an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)** - keywords and manual linking

### Issue and pull request templates

Templates make sure reports arrive with the information you need. Issue templates live in `.github/ISSUE_TEMPLATE/`. They come in two styles: Markdown templates that pre-fill the body, and **issue forms** (YAML) that present real form fields such as dropdowns, checkboxes and required text boxes. A `config.yml` file in the same folder controls the template chooser, for example turning off blank issues or adding a link to Discussions for questions.

A pull request template lives at `.github/pull_request_template.md` (or the root or `docs/`). Its content pre-fills every new PR description, which is a good place for a checklist ("tests added", "docs updated").

> **Exam trap:** Issue forms are YAML files; ordinary issue templates are Markdown. Both live in `.github/ISSUE_TEMPLATE/`.

**[📖 Configuring issue templates for your repository](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)** - templates and forms
**[📖 Creating a pull request template](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)** - PR templates

### Filters and search

The issue and pull request lists accept a search syntax that is worth knowing at a basic level:

```text
is:issue is:open label:bug assignee:@me
is:pr is:open review-requested:@me
is:pr is:merged author:octocat
is:issue no:assignee milestone:"v2.0"
```

`@me` means the signed-in user. `no:assignee`, `no:label` and `no:milestone` find things missing metadata. Saved views in Projects (Domain 5) build on the same filters.

**[📖 Filtering and searching issues and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests)** - filter syntax

### Assignments and review requests

**Assignees** are the people responsible for doing the work. An issue or PR can have up to 10 assignees. **Reviewers** are different: they are asked to review a pull request and their approval may be required. On a PR the author is often the assignee while others are reviewers. CODEOWNERS adds reviewers automatically (see Domain 2).

> **Exam trap:** Assigning someone to a pull request does not request their review. Use **Reviewers** for that.

## Notifications

GitHub notifies you about conversations you are part of and repositories you watch. Learning to tune notifications is an exam objective because the default for an active organization can be overwhelming.

### Why you get a notification

You are **participating** in a thread when you opened it, commented, were assigned, were @mentioned, or were requested for review. You are **subscribed** to a thread you participate in, or one you subscribed to manually with the Subscribe button. You also get notifications for everything in repositories you **watch** at the All Activity level.

### Watch levels for a repository

| Watch setting | You are notified about |
|---------------|------------------------|
| **Participating and @mentions** | Only threads you take part in or are mentioned in (the default) |
| **All Activity** | Every issue, pull request, discussion and release |
| **Ignore** | Nothing, not even @mentions |
| **Custom** | Participating, plus the event types you pick: issues, pull requests, releases, discussions, security alerts |

Custom is the answer when a question says "notify me about new releases but not every issue". Ignore is a blunt tool: it hides even direct mentions.

You can also unsubscribe from a single noisy thread without changing the repository's watch level.

### Where notifications arrive

Notifications can go to the **web inbox** (github.com/notifications), to **email**, and to **GitHub Mobile** as push notifications. You choose per notification type in your settings, and you can route email for an organization to a work address.

### Managing the inbox

The inbox works like an email client. You can mark items **Done**, **Save** them for later, **Unsubscribe**, or mark them read. It has default filters (Assigned, Participating, Mentioned, Team mentioned, Review requested) and you can create **custom filters** using queries like `reason:review-requested repo:acme/web`. Grouping by repository helps when you watch many.

- **Watching** - subscribing to a repository's activity at a chosen level; different from starring.
- **Participating** - being involved in a thread by authoring, commenting, being assigned, mentioned or requested for review.
- **Custom watch** - a watch level that adds chosen event types such as releases on top of participating notifications.
- **Notification inbox** - the web view of notifications with Done, Save and custom filters.

**[📖 About notifications](https://docs.github.com/en/subscriptions-and-notifications/concepts/about-notifications)** - how notifications work
**[📖 Configuring notifications](https://docs.github.com/en/subscriptions-and-notifications/get-started/configuring-notifications)** - watch levels and delivery
**[📖 Managing notifications from your inbox](https://docs.github.com/en/subscriptions-and-notifications/how-tos/viewing-and-triaging-notifications/managing-notifications-from-your-inbox)** - Done, Save and filters

## Gists, Wikis and GitHub Pages

These three features all publish text or content, so the exam likes to ask which one fits.

### Gists

A **gist** is a quick way to share a snippet, a single file or a few files. Every gist is a small Git repository, so it has history and can be cloned, forked and starred. Gists are either **public** (listed and searchable) or **secret**. Secret gists are not listed or searchable, but anyone with the URL can see them.

> **Exam trap:** Secret gists are not private. Never put credentials in a gist, secret or not.

**[📖 Creating gists](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists)** - public and secret gists

### Wikis

A **wiki** is a set of documentation pages attached to a repository, edited in the browser or cloned as its own Git repository (`<repo>.wiki.git`). Wikis suit long-form documentation that lives beside the code but should not clutter the main tree. Wikis are available in public repositories on all plans, and in private repositories on paid plans. Admins can restrict editing to collaborators.

**[📖 About wikis](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis)** - what wikis offer

### GitHub Pages

**GitHub Pages** hosts a static website (HTML, CSS, JavaScript) straight from a repository. There is no server-side code and no database. You publish from a branch and folder (the root or `/docs`), or with a GitHub Actions workflow for custom build tools. Jekyll is supported out of the box.

There are two kinds of site:

- A **user or organization site** comes from a repository named `<owner>.github.io` and is served at `https://<owner>.github.io`. Each account gets one.
- A **project site** comes from any other repository and is served at `https://<owner>.github.io/<repo>`.

You can add a custom domain with HTTPS. Pages is free for public repositories; publishing from private repositories needs a paid plan.

> **Exam trap:** A Pages site built from a private repository is still public on the internet, unless the organization uses Enterprise Cloud access control. Do not assume a private repository means a private website.

**[📖 What is GitHub Pages?](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)** - overview and limits
**[📖 Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)** - set one up

| Need | Use |
|------|-----|
| Share a code snippet or config file | Gist |
| Write multi-page project documentation next to the code | Wiki |
| Publish a public website or documentation site | GitHub Pages |

- **Gist** - a small Git repository for sharing snippets, either public or secret (unlisted).
- **Wiki** - repository documentation pages stored in a separate Git repository.
- **GitHub Pages** - static website hosting from a repository branch, folder or Actions workflow.

## Branch protection

Branch protection rules and rulesets (requiring reviews, status checks or signed commits before merging) are part of collaboration in practice, but the January 2026 outline places them under administration. See [Domain 6: Privacy, security and administration](06-privacy-security-administration.md#branch-protection-rules-and-rulesets).

## Key exam points

- Issues track work, pull requests propose code, discussions host conversation.
- Draft pull requests cannot be merged.
- Review outcomes: Comment, Approve, Request changes.
- Merge methods: merge commit, squash and merge, rebase and merge.
- Closing keywords close the issue only when the PR merges into the default branch.
- Issue templates and forms live in `.github/ISSUE_TEMPLATE/`; forms are YAML.
- Assignees do the work; reviewers review.
- Watch levels: Participating and @mentions (default), All Activity, Ignore, Custom.
- Secret gists are unlisted, not private.
- Pages hosts static sites only; `<owner>.github.io` is the user or organization site.
