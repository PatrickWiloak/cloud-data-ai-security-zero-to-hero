---
last-updated: 2026-10-22
applies-to: GH-900 skills measured as of January 2026, checked 2026-10-22
difficulty: beginner
---

# GitHub Foundations (GH-900) Study Plan

A four-week plan of about an hour a day, built around the seven domains of the January 2026 outline. Time follows the weights: Domain 1 (25-30%) gets the most days, Domains 5 and 7 (5-10% each) the fewest. If you already use GitHub daily, compress weeks 1 and 2 and spend the saved time on Domains 4 and 6.

## Time allocation by domain weight

| Domain | Weight | Suggested hours (of about 28) |
|--------|--------|-------------------------------|
| 1. Understand Git and GitHub basics | 25-30% | 7-8 |
| 2. Work with GitHub repositories | 10-15% | 3-4 |
| 3. Collaborate using GitHub | 10-15% | 3-4 |
| 4. Apply modern development practices | 10-15% | 3-4 |
| 5. Manage projects with GitHub | 5-10% | 2 |
| 6. Understand privacy, security, and administration | 10-15% | 3-4 |
| 7. Explore the GitHub community | 5-10% | 2 |
| Review and practice | - | 3-4 |

## Week 1: Git and GitHub basics (Domain 1)

### Day 1: Version control and Git vs GitHub
- [ ] Read: [notes/01-git-and-github-basics.md](notes/01-git-and-github-basics.md), "Version control fundamentals"
- [ ] Explain in your own words why version control exists and the difference between Git and GitHub
- [ ] Install Git, set `user.name` and `user.email`, run `git init` in a test folder
- [ ] Read: [About GitHub and Git](https://docs.github.com/en/get-started/start-your-journey/about-github-and-git)

### Day 2: Commits and the three areas
- [ ] Practise `git status`, `git add`, `git commit`, `git log`, `git diff`
- [ ] Watch a file move from untracked to modified to staged to committed
- [ ] Try `git stash` and `git stash pop`

### Day 3: Branches, merging and conflicts
- [ ] Create, switch and delete branches with `git switch`
- [ ] Merge a branch, then cause and resolve a merge conflict
- [ ] Compare `git revert` and `git reset --soft` on a throwaway repository

### Day 4: Remotes and GitHub Flow
- [ ] Push a repository to GitHub; practise `git fetch` vs `git pull`
- [ ] Run the full GitHub Flow: branch, commit, push, open PR, merge, delete branch
- [ ] Read: [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)

### Day 5: Accounts, plans and enterprise options
- [ ] Re-read the accounts and plans sections of [Domain 1](notes/01-git-and-github-basics.md)
- [ ] Create a free organization and look at its settings
- [ ] Be able to say when Enterprise Cloud or Enterprise Server fits

### Day 6: Markdown, Desktop and Mobile
- [ ] Write an issue using headings, a task list, a code block, an alert and an @mention
- [ ] Install GitHub Desktop and commit through it; install GitHub Mobile and review a PR from it
- [ ] Read: [Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

### Day 7: Week 1 review
- [ ] Re-read the Domain 1 key exam points
- [ ] Complete the first modules of the [GitHub Foundations learning path, part 1](https://learn.microsoft.com/en-us/training/paths/github-foundations/)

## Week 2: Repositories, collaboration and projects (Domains 2, 3, 5)

### Day 8: Repository files
- [ ] Read: [notes/02-repositories.md](notes/02-repositories.md)
- [ ] Add README, LICENSE, CONTRIBUTING, CODEOWNERS and SECURITY.md to a test repository
- [ ] Mark it as a template and create a new repository from it

### Day 9: Files, insights and maintenance
- [ ] Add a file through the web UI with "create a new branch and start a pull request"
- [ ] Open every Insights view and write one line on what each answers
- [ ] Add topics, turn on auto-delete head branches, then archive and unarchive the repository

### Day 10: Issues, pull requests and discussions
- [ ] Read: [notes/03-collaboration.md](notes/03-collaboration.md)
- [ ] Open an issue, link a PR with `Fixes #1`, request a review, leave a suggested change, squash-merge
- [ ] Enable Discussions and post in a Q&A category

### Day 11: Templates, filters and notifications
- [ ] Create an issue form (YAML) and a PR template
- [ ] Practise filters: `is:open label:bug assignee:@me`, `review-requested:@me`
- [ ] Set a repository to Custom watch (releases only) and triage your notification inbox

### Day 12: Gists, wikis and Pages
- [ ] Create a public gist and a secret gist; note who can see each
- [ ] Add a wiki page and publish a GitHub Pages site from `/docs`

### Day 13: GitHub Projects
- [ ] Read: [notes/05-project-management.md](notes/05-project-management.md)
- [ ] Create a project with table, board and roadmap views, a single select Priority field and an iteration field
- [ ] Turn on the item closed and auto-add workflows; add an insights chart
- [ ] Create a milestone, labels and a saved reply

### Day 14: Week 2 review
- [ ] Re-read the key exam points for Domains 2, 3 and 5
- [ ] Complete the [GitHub Foundations learning path, part 1](https://learn.microsoft.com/en-us/training/paths/github-foundations/)

## Week 3: Modern development, administration and community (Domains 4, 6, 7)

### Day 15: GitHub Actions
- [ ] Read: [notes/04-modern-development.md](notes/04-modern-development.md), "GitHub Actions"
- [ ] Add a workflow that runs on `pull_request` and see it appear as a status check
- [ ] Read: [Understanding GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions)

### Day 16: Copilot
- [ ] Read the Copilot section of [Domain 4](notes/04-modern-development.md)
- [ ] Turn on Copilot Free; try inline suggestions, Chat and agent mode
- [ ] Write out the plan line-up and what Business and Enterprise add
- [ ] Read: [Plans for GitHub Copilot](https://docs.github.com/en/copilot/get-started/plans)

### Day 17: Codespaces and github.dev
- [ ] Press `.` on a repository to open github.dev; note there is no terminal
- [ ] Open a codespace, add a `devcontainer.json`, rebuild, and stop it
- [ ] Read: [The github.dev web-based editor](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)

### Day 18: Accounts security and roles
- [ ] Read: [notes/06-privacy-security-administration.md](notes/06-privacy-security-administration.md)
- [ ] Turn on 2FA with an authenticator app, save recovery codes, add a passkey
- [ ] Recite the repository roles in order and the organization roles

### Day 19: Enterprise administration, visibility and rulesets
- [ ] Re-read EMUs, Copilot policies and visibility in [Domain 6](notes/06-privacy-security-administration.md)
- [ ] Add a ruleset to `main` that requires a pull request; try a direct push
- [ ] Turn on Dependabot alerts and secret scanning on a public repository
- [ ] Read: [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)

### Day 20: Community
- [ ] Read: [notes/07-github-community.md](notes/07-github-community.md)
- [ ] Follow a developer, star a repository, watch another for releases only
- [ ] Browse Explore, Topics and Marketplace; find a `good first issue`
- [ ] Add a `.github/FUNDING.yml` to a test repository

### Day 21: Week 3 review
- [ ] Re-read the key exam points for Domains 4, 6 and 7
- [ ] Complete the [GitHub Foundations learning path, part 2](https://learn.microsoft.com/en-us/training/paths/github-foundations-2/)

## Week 4: Review and practice

### Day 22-23: Fact sheet and flashcards
- [ ] Read the whole [fact-sheet.md](fact-sheet.md), especially the key differentiators table
- [ ] Drill [flashcards.csv](flashcards.csv)

### Day 24-25: Scenarios and practice questions
- [ ] Work through [scenarios.md](scenarios.md)
- [ ] Work through the [practice questions](../../../resources/practice-questions/github-foundations.md)
- [ ] For each miss, re-read the matching note section

### Day 26: Weak areas
- [ ] Re-read the two notes where you missed the most questions
- [ ] Re-read the [GH-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900) and tick off each skill

### Day 27: Light review
- [ ] Skim the key exam points of all seven notes
- [ ] Check your exam appointment, ID and (for online delivery) your system check

### Day 28: Exam day
- [ ] Light review of the fact sheet only
- [ ] 100 minutes: first pass, flag, second pass, final check
- [ ] Read every option; eliminate the look-alike feature

## Daily rhythm

- **25 minutes** reading the note section
- **25 minutes** trying it on GitHub
- **10 minutes** flashcards or key exam points
