---
last-updated: 2026-10-22
difficulty: beginner
---

# GitHub Foundations - Practice Questions

30 questions for GitHub Foundations (GH-900) prep. Questions 16-30 follow the skills measured as of January 2026: Git and GitHub basics (25-30%); repositories, collaboration, modern development, and privacy, security and administration (10-15% each); and projects and the community (5-10% each).

> **Cert page:** [exams/github/foundations/](../../exams/github/foundations/)

---

### Question 1
**Scenario:** What is the difference between Git and GitHub?

A. Git only works with GitHub, because every Git command talks to a GitHub server and the tool cannot be used with another host or offline
B. GitHub replaces Git
C. Git is the distributed version control system; GitHub is a hosting platform that adds collaboration features on top of it
D. They are the same product, and GitHub is simply the name the company uses for the Git command line tool and its history engine

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Git runs locally and works with no network at all. GitHub adds remote hosting plus pull requests, issues, Actions, and access control. Keeping the distinction clear explains why you can commit on a plane and why `git push` is a separate step.
</details>

---

### Question 2
**Scenario:** A change should be proposed for review before it enters `main`.

A. Create a branch, push it, and open a pull request so reviewers and status checks run before the change merges into `main`
B. Email a patch to a maintainer, who applies it to `main` by hand
C. Fork the repository and keep the changes in the fork indefinitely
D. Commit directly to `main` and ask teammates to look at the commit afterward

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The pull request is the review, discussion, and CI surface, and branch protection rules on `main` enforce that it is used. Direct commits skip review and skip the status checks that would catch a broken build.
</details>

---

### Question 3
**Scenario:** A contributor outside the organization wants to propose a change to a public repository.

A. Fork the repository, commit to a branch in their fork, and open a pull request to the upstream repository
B. They cannot contribute to a public repository unless the maintainers first add them as a collaborator with write access to it
C. Clone the upstream repository and push their commits straight to it, which fails because they have no write permission on the repository
D. They need write access to the upstream repository before they can open a pull request, so they must request it from an owner

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The fork and pull model is how open source works: contributors need no write access on the upstream repository, and maintainers review before merging. Clone gives a local copy but not permission to push to the original.
</details>

---

### Question 4
**Scenario:** `main` must require one approving review and passing status checks before merge.

A. A CONTRIBUTING file that explains the review expectations to contributors, which documents the process but does not stop a merge without review
B. Ask the team politely to wait for a review and a green build before merging
C. A repository description that states the review policy at the top of the page, which is shown to visitors but is not enforced
D. A branch protection rule (or ruleset) on `main` requiring reviews and status checks

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Documentation states intent; protection rules enforce it, including for administrators if you enable that option. Rulesets are the newer form and can be applied across many repositories at the organization level.
</details>

---

### Question 5
**Scenario:** What does a `.gitignore` file do?

A. Encrypts the listed files in the working tree so other users who clone cannot read them
B. Tells Git not to track specified untracked files, such as build output, dependency folders, and local configuration
C. Hides the listed files from other users of the repository in the web interface
D. Deletes the listed files from each contributor's clone on the next pull

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** It prevents accidental commits of artifacts and local settings. Note it only affects untracked files: something already committed stays tracked until you remove it, and a secret already pushed stays in history until it is rewritten and rotated.
</details>

---

### Question 6
**Scenario:** A pull request description contains `Closes #42`.

A. Issue 42 is automatically closed when the pull request merges into the default branch
B. Nothing happens, because the text of a pull request is a description only and issues must be closed by hand after the merge
C. The issue is assigned to the pull request author
D. The issue is deleted from the repository together with its comments

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Closing keywords link a pull request to an issue and close it on merge into the default branch, which keeps the issue tracker accurate without manual cleanup. Mentioning `#42` without a keyword creates a reference but does not close it.
</details>

---

### Question 7
**Scenario:** Work must be tracked across several repositories on one board.

A. A repository project only, which cannot show issues from other repositories
B. A spreadsheet maintained by hand, with rows copied in from every repository each week
C. Milestones only, which group issues inside one repository and cannot be shared
D. GitHub Projects at the organization level, pulling issues and pull requests from multiple repositories into custom views and fields

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Organization-level projects span repositories with custom fields, views, and automation. Milestones are per-repository and group issues toward a release, which is a narrower tool.
</details>

---

### Question 8
**Scenario:** GitHub Actions is described in one sentence.

A. A package registry that hosts container images and libraries, so that other projects can install the build output of a repository
B. A code review tool for commenting on lines of a pull request and approving it before the change is merged into the base branch
C. A CI/CD and automation platform where workflows run on events in the repository
D. A code editor that runs in the browser, which lets a contributor change files without a local checkout

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Workflows are YAML files in `.github/workflows` triggered by events such as push, pull request, schedule, or manual dispatch. They run jobs on runners, which can be GitHub-hosted or self-hosted.
</details>

---

### Question 9
**Scenario:** A secret must be available to a workflow without appearing in the repository.

A. Commit it in a file in the repository but keep the repository private, so that only trusted collaborators can ever read the value
B. An encrypted repository, environment, or organization secret referenced as `${{ secrets.NAME }}`
C. Put it in a comment on the pull request, where reviewers can see it, and have the workflow read the comment through the API
D. An environment variable in the workflow YAML, which keeps the value out of a separate file but leaves it visible in the repository

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Encrypted secrets are injected at run time and masked in logs. Anything written into the YAML is in the repository and in its history. Environment secrets add the ability to require approval before a deployment job can read them.
</details>

---

### Question 10
**Scenario:** A repository's visibility options.

A. Public, private, and internal (visible within the enterprise) for organizations on the relevant plans
B. Visibility cannot be changed once a repository is created, so a project must be recreated and its history copied to change it
C. Public only, because private code requires a separate product
D. Public and private only, with no further levels, regardless of the plan that the organization or enterprise account has

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Internal repositories support innersource: visible to everyone in the enterprise but not to the public. Visibility can be changed later, but making a private repository public exposes its entire history, which is why secret scanning before that change matters.
</details>

---

### Question 11
**Scenario:** Documentation should live alongside the code and render as a website.

A. An external CMS connected by a webhook
B. Issues labeled as documentation, which can be searched and linked, but are conversations rather than a rendered website
C. GitHub Pages, optionally built from a `docs` folder or a branch
D. A wiki only, which is a separate repository of pages edited in the browser and is not versioned with the code in the same pull request

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Pages publishes static content directly from the repository, so documentation is versioned and reviewed with the code. Wikis are convenient but sit outside the pull request workflow, so they drift.
</details>

---

### Question 12
**Scenario:** A repository should tell contributors how to participate.

A. Issues only, with contributors reading the open issue list to learn the process, which gives no stable place for rules and setup steps
B. A single comment on the most recent pull request, pinned by a maintainer, explaining how to participate to anyone who finds it
C. Community health files: README, CONTRIBUTING, CODE_OF_CONDUCT, LICENSE, and issue and pull request templates
D. Nothing is needed because contributors can read the source and figure out the conventions from the existing commit history

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** These files answer the questions every new contributor has and can be defaulted at the organization level from a `.github` repository. The license in particular is what determines whether anyone may legally use the code.
</details>

---

### Question 13
**Scenario:** A team needs to discuss an idea that is not a bug or a task.

A. A commit message on the main branch, which is not a place for open discussion
B. GitHub Discussions, a forum-style space for questions, ideas, and announcements outside the issue tracker
C. An issue, which is for bug reports and trackable tasks, not open-ended ideas
D. A pull request, which is meant for reviewing a specific code change and not for talking about an idea with no code behind it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Discussions keep open-ended conversation out of the issue tracker, so issues stay actionable work. Threads can be marked as answered and later converted into an issue when a decision produces work.
</details>

---

### Question 14
**Scenario:** Which describes a fork versus a clone?

A. Forks are private only, so only the account owner can see or change a fork
B. They are the same operation with two names for the same copy
C. A clone is server-side, created on GitHub under another account, while a fork is the local copy on a developer's machine
D. A fork is a server-side copy of a repository under your account; a clone is a local copy on your machine

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** You typically fork on GitHub then clone the fork locally. The fork keeps a link to the upstream repository, which is what makes the pull request across repositories possible and lets you sync later changes.
</details>

---

### Question 15
**Scenario:** GitHub Copilot in one sentence.

A. A code search tool that indexes repositories and returns matching snippets
B. An AI pair programmer that suggests code and answers questions in the editor and on GitHub, including chat and code explanations
C. A package manager that installs and updates dependencies declared in a manifest file
D. A CI runner that executes workflow jobs on virtual machines hosted by GitHub whenever push, pull request, or schedule events fire in a repository

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Copilot suggests completions, generates from comments, explains code, and answers in chat. Suggestions still need review: the developer remains responsible for correctness, licensing, and security of what they commit.
</details>

---

### Question 16
**Scenario:** A new team member asks what a Git commit actually records.

A. Only the lines that changed, stored as a patch that must be replayed from the first commit of the repository
B. A snapshot of the tracked files, with an author, a message and a link to its parent commit
C. A copy of the whole repository uploaded to GitHub each time the developer saves a file
D. A ticket on GitHub that describes work to be done

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A commit records a snapshot of the project's tracked files plus metadata (author, time, message) and a pointer to its parent, identified by a hash. Git stores snapshots efficiently, not as a chain of patches you must replay from the start. Commits are local until pushed and are created on purpose, not on every save. A ticket describing work is an issue, not a commit.
</details>

---

### Question 17
**Scenario:** Which sequence describes GitHub Flow?

A. Commit straight to `main`, tag a release every week, and fix any problems in the next weekly release
B. Keep long-lived `develop`, `release` and `hotfix` branches, merging between them on a fixed schedule
C. Email patches to a maintainer, who applies and pushes them
D. Create a branch, commit changes, open a pull request, review and discuss, then merge

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** GitHub Flow is lightweight: branch from `main`, commit, open a pull request, review, then merge and deploy. Committing straight to `main` skips review entirely. Long-lived `develop`, `release` and `hotfix` branches describe Git Flow, a heavier model. Emailing patches is a valid Git workflow used by some projects, but it is not GitHub Flow.
</details>

---

### Question 18
**Scenario:** A designer who rarely uses the command line wants to clone a repository, commit changes and push them using a graphical app on their computer.

A. GitHub Desktop, the graphical client for Windows and macOS
B. GitHub Mobile, which provides a full Git client for editing files and pushing commits from a phone
C. The GitHub CLI (`gh`), which is a graphical app for people who avoid the terminal
D. GitHub Pages, which edits repository files in a visual editor and commits them for you

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** GitHub Desktop is the graphical client for cloning, committing, branching and pushing without the command line. GitHub Mobile is for triaging notifications, reviewing and commenting on the go, not for full local Git work. The GitHub CLI runs in the terminal, which the designer wants to avoid. GitHub Pages publishes websites from a repository and is not an editor.
</details>

---

### Question 19
**Scenario:** An issue should show a checklist that people can tick off as the work progresses.

A. Use a `<table>` element with checkbox inputs, which GitHub turns into a live checklist
B. Add a label called `checklist` so GitHub renders the issue body as a set of tick boxes
C. Write Markdown task list items such as `- [ ] Write tests` in the issue body
D. Create a separate milestone for every checklist item in the issue

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** GitHub Flavored Markdown turns `- [ ]` and `- [x]` lines into clickable task list items. HTML form inputs are stripped and do not become interactive. Labels categorize issues but do not change how the body renders. Milestones group issues toward a goal; they are far too heavy for checklist items.
</details>

---

### Question 20
**Scenario:** Changes to files under `/infra` must always request review from the platform team automatically.

A. Add the platform team as admins of the repository so they see every pull request on the default branch
B. Ask contributors in the README to tag the platform team
C. Add the platform team to the repository's `SECURITY.md` file under a section for infrastructure
D. Add a `CODEOWNERS` entry mapping `/infra/` to the platform team

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `CODEOWNERS` maps paths to people or teams, and GitHub automatically requests their review on pull requests that touch those paths; branch protection can also require it. Admin rights do not request reviews. A README note relies on people remembering. `SECURITY.md` tells people how to report vulnerabilities and does not drive review requests.
</details>

---

### Question 21
**Scenario:** A company wants every new service repository to start with the same folders, license, README layout and issue templates.

A. Mark a well-set-up repository as a template repository and create new repositories from it
B. Fork the set-up repository for each new service, keeping the fork link back to the original
C. Copy the files by hand into each new repository from a shared drive using a checklist
D. Archive the set-up repository so its files become the default for the whole organization

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A template repository lets people create new repositories with the same files and structure, with a clean history and no fork relationship. Forks keep a link to the upstream and are meant for contributing back, not for starting new projects. Copying by hand drifts and is easy to get wrong. Archiving makes a repository read-only; it does not apply its files anywhere else.
</details>

---

### Question 22
**Scenario:** A developer is overwhelmed by notifications from a busy repository but still wants to hear about pull requests and releases.

A. Unstar the repository, which stops every notification from it immediately
B. Set the repository watch setting to Custom and pick only pull requests and releases
C. Turn off email notifications for the account, which also stops web notifications
D. Leave the organization so the repository no longer sends anything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Custom watch settings let a user choose event types such as pull requests, releases, issues or discussions for one repository. Starring is a bookmark and does not control notifications. Email and web delivery are configured separately, and turning off email does not filter events. Leaving the organization removes access, which is far more than the developer wants.
</details>

---

### Question 23
**Scenario:** A developer wants to share a single useful script snippet publicly with a link, with version history, without creating a full repository.

A. Open an issue in a public repository and paste the script into the issue body
B. Publish the script as a GitHub Pages site
C. Create a public Gist, which has its own URL and revision history
D. Add the script to a wiki page in one of their repositories so it has a URL

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Gists are small Git-backed snippets with their own URL, revisions and the option of being public or secret, which is exactly this use. An issue is for tracking work, not sharing code. Pages publishes websites from a repository, which is more setup than needed. A wiki page needs a repository and is meant for documentation.
</details>

---

### Question 24
**Scenario:** A team wants every Codespace for their repository to open with the same language version, tools and editor extensions already installed.

A. Add a dev container configuration in `.devcontainer/devcontainer.json`
B. Write the setup steps in the README and ask each developer to run them after the Codespace starts
C. Add the tools to the repository's `.gitignore` so Codespaces knows to install them
D. Turn on GitHub Actions caching so the tools are restored into each Codespace from the cache

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A dev container configuration defines the image, features, tools and editor extensions that every Codespace for the repository uses. A README relies on manual steps and drifts. `.gitignore` tells Git which files to ignore and has no install meaning. The Actions cache serves workflow runs, not Codespaces.
</details>

---

### Question 25
**Scenario:** A reviewer wants to quickly edit a few files in the browser by pressing the period key on a repository. They do not need a terminal or to run the code.

A. Use a Codespace, which is the only way to edit files in the browser with a full terminal
B. Use GitHub Desktop, which opens in the browser when the period key is pressed
C. Use GitHub Copilot Chat, which edits files when asked and commits them automatically
D. Use the github.dev editor, which runs in the browser with no compute behind it

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Pressing `.` opens github.dev, a lightweight browser editor with no compute, so there is no terminal and no cost, which fits quick edits. Codespaces gives a full cloud machine with a terminal, which is more than needed and uses compute. GitHub Desktop is a desktop app, not a browser editor. Copilot Chat assists with code; it is not the editor the period key opens.
</details>

---

### Question 26
**Scenario:** A product manager wants to group a set of issues and pull requests toward a release due on a specific date and see the percentage completed.

A. Create a label named after the release and filter issues by it from the repository's issue list
B. Create a milestone with a due date and assign the issues and pull requests to it
C. Pin the issues to the top of the repository's issue list until the release ships
D. Create a discussion category for the release and move each issue into it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Milestones group issues and pull requests, carry a due date, and show progress as a percentage of closed items. Labels categorize but have no due date or progress bar. Pinning highlights up to a few issues and does not track progress. Discussions are for conversation, and moving issues into them is not how release tracking works.
</details>

---

### Question 27
**Scenario:** An organization wants to protect member accounts against stolen passwords.

A. Require every member to use a password of at least 20 characters
B. Make all repositories private so stolen passwords cannot reach any code
C. Require two-factor authentication, with passkeys or authenticator apps as second factors
D. Rotate the organization's name every year so attackers lose track of it

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Two-factor authentication means a stolen password alone is not enough to sign in, and passkeys add phishing resistance; organizations can require 2FA for members. Longer passwords help but are still stolen by phishing and reuse. Private repositories do nothing for a signed-in attacker who is a member. Renaming the organization has no security value.
</details>

---

### Question 28
**Scenario:** An enterprise wants user accounts to be created, named and removed only by its identity provider, with no personal GitHub accounts used for company work.

A. Ask employees to add their work email to their personal GitHub accounts
B. Create one shared login that every employee uses for company repositories
C. Turn on a public profile requirement so the company can see who belongs to the organization
D. Use Enterprise Managed Users, where the identity provider provisions and controls the accounts

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** With Enterprise Managed Users, accounts are provisioned from the company identity provider, their usernames and profiles are controlled by the enterprise, and they are removed when the person leaves. Adding a work email to a personal account leaves the account owned by the individual. Shared logins break auditability and violate GitHub's terms. Public profiles do not provision or remove anyone.
</details>

---

### Question 29
**Scenario:** A large company wants internal teams to contribute to each other's code the way open source projects accept outside contributions.

A. InnerSource, which applies open source practices to code shared inside the company
B. Forking every internal repository to a public account
C. Giving every developer admin rights on every repository in the organization so they can merge their own changes
D. Moving all code into a single repository owned by one team who makes every change on behalf of the others

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** InnerSource applies open source practices, such as visible code, pull requests from other teams and clear contribution guides, inside an organization. Making internal code public exposes it beyond the company. Admin rights for all removes review and ownership. Funnelling every change through one team is the opposite of open contribution.
</details>

---

### Question 30
**Scenario:** A developer wants to give recurring financial support to the maintainer of an open source library they rely on.

A. Star the library's repository every month to signal ongoing support
B. Sponsor the maintainer through GitHub Sponsors
C. Buy the library from the GitHub Marketplace as a paid app
D. Open a pull request that adds the developer's name to the README

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** GitHub Sponsors lets people and organizations fund maintainers with one-time or recurring payments. Stars are a bookmark and a signal of interest, not money. The Marketplace lists apps and actions, and most open source libraries are not sold there. A README pull request does nothing for the maintainer financially.
</details>

---

## Where to go deeper

- [GitHub Foundations cert page](../../exams/github/foundations/) - notes, practice plan, strategy
- [GitHub Actions practice questions](./github-actions.md) - the automation exam
- [GitHub Copilot practice questions](https://ai.noblerworks.com/certifications/practice-questions/github-copilot/) - the Copilot exam
- [Git and GitHub basics](../../learn/day-one/) - the Day One on-ramp
- **[📖 GitHub Certifications](https://learn.github.com/certifications)** - official exam pages
