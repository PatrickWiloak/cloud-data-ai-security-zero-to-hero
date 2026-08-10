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

A. They are the same
B. Git is the distributed version control system; GitHub is a hosting platform that adds collaboration features on top of it
C. GitHub replaces Git
D. Git only works with GitHub

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Git runs locally and works with no network at all. GitHub adds remote hosting plus pull requests, issues, Actions, and access control. Keeping the distinction clear explains why you can commit on a plane and why `git push` is a separate step.
</details>

---

### Question 2
**Scenario:** A change should be proposed for review before it enters `main`.

A. Commit directly to `main`
B. Create a branch, push it, and open a pull request
C. Email a patch
D. Fork and never merge

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The pull request is the review, discussion, and CI surface, and branch protection rules on `main` enforce that it is used. Direct commits skip review and skip the status checks that would catch a broken build.
</details>

---

### Question 3
**Scenario:** A contributor outside the organization wants to propose a change to a public repository.

A. They need write access
B. Fork the repository, commit to a branch in their fork, and open a pull request to the upstream repository
C. They cannot contribute
D. Clone and push directly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The fork and pull model is how open source works: contributors need no write access on the upstream repository, and maintainers review before merging. Clone gives a local copy but not permission to push to the original.
</details>

---

### Question 4
**Scenario:** `main` must require one approving review and passing status checks before merge.

A. Ask the team politely
B. A branch protection rule (or ruleset) on `main` requiring reviews and status checks
C. A CONTRIBUTING file
D. A repository description

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Documentation states intent; protection rules enforce it, including for administrators if you enable that option. Rulesets are the newer form and can be applied across many repositories at the organization level.
</details>

---

### Question 5
**Scenario:** What does a `.gitignore` file do?

A. Deletes files
B. Tells Git not to track specified files, such as build output and local configuration
C. Hides files from other users
D. Encrypts files

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** It prevents accidental commits of artifacts and local settings. Note it only affects untracked files: something already committed stays tracked until you remove it, and a secret already pushed stays in history until it is rewritten and rotated.
</details>

---

### Question 6
**Scenario:** A pull request description contains `Closes #42`.

A. Nothing happens
B. Issue 42 is automatically closed when the pull request merges
C. The issue is deleted
D. The issue is assigned

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Closing keywords link a pull request to an issue and close it on merge into the default branch, which keeps the issue tracker accurate without manual cleanup. Mentioning `#42` without a keyword creates a reference but does not close it.
</details>

---

### Question 7
**Scenario:** Work must be tracked across several repositories on one board.

A. A repository project only
B. GitHub Projects at the organization level, pulling issues and pull requests from multiple repositories
C. A spreadsheet
D. Milestones only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Organization-level projects span repositories with custom fields, views, and automation. Milestones are per-repository and group issues toward a release, which is a narrower tool.
</details>

---

### Question 8
**Scenario:** GitHub Actions is described in one sentence.

A. A code editor
B. A CI/CD and automation platform where workflows run on events in the repository
C. A package registry
D. A code review tool

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Workflows are YAML files in `.github/workflows` triggered by events such as push, pull request, schedule, or manual dispatch. They run jobs on runners, which can be GitHub-hosted or self-hosted.
</details>

---

### Question 9
**Scenario:** A secret must be available to a workflow without appearing in the repository.

A. Commit it in a file
B. An encrypted repository, environment, or organization secret referenced as `${{ secrets.NAME }}`
C. A comment
D. An environment variable in the YAML

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Encrypted secrets are injected at run time and masked in logs. Anything written into the YAML is in the repository and in its history. Environment secrets add the ability to require approval before a deployment job can read them.
</details>

---

### Question 10
**Scenario:** A repository's visibility options.

A. Public and private only
B. Public, private, and internal (visible within the enterprise) for organizations on the relevant plans
C. Public only
D. Visibility cannot be changed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Internal repositories support innersource: visible to everyone in the enterprise but not to the public. Visibility can be changed later, but making a private repository public exposes its entire history, which is why secret scanning before that change matters.
</details>

---

### Question 11
**Scenario:** Documentation should live alongside the code and render as a website.

A. GitHub Pages, optionally built from a `docs` folder or a branch
B. A wiki only
C. An external CMS
D. Issues

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Pages publishes static content directly from the repository, so documentation is versioned and reviewed with the code. Wikis are convenient but sit outside the pull request workflow, so they drift.
</details>

---

### Question 12
**Scenario:** A repository should tell contributors how to participate.

A. Nothing is needed
B. Community health files: README, CONTRIBUTING, CODE_OF_CONDUCT, LICENSE, and issue and pull request templates
C. Issues only
D. A single comment

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** These files answer the questions every new contributor has and can be defaulted at the organization level from a `.github` repository. The license in particular is what determines whether anyone may legally use the code.
</details>

---

### Question 13
**Scenario:** A team needs to discuss an idea that is not a bug or a task.

A. An issue
B. GitHub Discussions, a forum-style space for questions, ideas, and announcements
C. A pull request
D. A commit message

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Discussions keep open-ended conversation out of the issue tracker, so issues stay actionable work. Threads can be marked as answered and later converted into an issue when a decision produces work.
</details>

---

### Question 14
**Scenario:** Which describes a fork versus a clone?

A. They are the same
B. A fork is a server-side copy of a repository under your account; a clone is a local copy on your machine
C. A clone is server-side
D. Forks are private only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** You typically fork on GitHub then clone the fork locally. The fork keeps a link to the upstream repository, which is what makes the pull request across repositories possible and lets you sync later changes.
</details>

---

### Question 15
**Scenario:** GitHub Copilot in one sentence.

A. A code search tool
B. An AI pair programmer that suggests code and answers questions in the editor and on GitHub
C. A CI runner
D. A package manager

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Copilot suggests completions, generates from comments, explains code, and answers in chat. Suggestions still need review: the developer remains responsible for correctness, licensing, and security of what they commit.
</details>

---

## Where to go deeper

- [GitHub Foundations cert page](../../exams/github/foundations/) - notes, practice plan, strategy
- [GitHub Actions practice questions](./github-actions.md) - the automation exam
- [GitHub Copilot practice questions](./github-copilot.md) - the Copilot exam
- [Git and GitHub basics](../../learn/day-one/) - the Day One on-ramp
- **[📖 GitHub Certifications](https://resources.github.com/learn/certifications/)** - official exam pages
