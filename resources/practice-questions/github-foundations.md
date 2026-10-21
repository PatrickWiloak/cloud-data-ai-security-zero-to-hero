---
last-updated: 2026-08-09
difficulty: beginner
---

# GitHub Foundations - Practice Questions

15 questions for GitHub Foundations prep, weighted toward collaboration features (30%) and introduction to Git and GitHub (22%), then modern development, privacy and security, and the community.

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

## Where to go deeper

- [GitHub Foundations cert page](../../exams/github/foundations/) - notes, practice plan, strategy
- [GitHub Actions practice questions](./github-actions.md) - the automation exam
- [GitHub Copilot practice questions](https://ai.noblerworks.com/certifications/practice-questions/github-copilot/) - the Copilot exam
- [Git and GitHub basics](../../learn/day-one/) - the Day One on-ramp
- **[📖 GitHub Certifications](https://learn.github.com/certifications)** - official exam pages
