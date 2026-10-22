---
last-updated: 2026-10-22
applies-to: GH-900 skills measured as of January 2026, checked 2026-10-22
difficulty: beginner
---

# GitHub Foundations (GH-900) Study Strategy

GH-900 was rewritten in January 2026. The biggest change for your study time: **Git and GitHub basics is now the heaviest domain at 25-30%**, and collaboration dropped to 10-15%. Copilot (agents, plans, models), github.dev versus Codespaces, rulesets, passkeys and Enterprise Managed Users are new or much more prominent. Study to the new weights, not to older guides.

## Where to spend your time

| # | Domain | Weight | Share of study time | Note |
|---|--------|--------|--------------------|------|
| 1 | Understand Git and GitHub basics | 25-30% | About a quarter | [01-git-and-github-basics.md](notes/01-git-and-github-basics.md) |
| 2 | Work with GitHub repositories | 10-15% | About an eighth | [02-repositories.md](notes/02-repositories.md) |
| 3 | Collaborate using GitHub | 10-15% | About an eighth | [03-collaboration.md](notes/03-collaboration.md) |
| 4 | Apply modern development practices | 10-15% | About an eighth, more if Copilot is new to you | [04-modern-development.md](notes/04-modern-development.md) |
| 5 | Manage projects with GitHub | 5-10% | A small slice | [05-project-management.md](notes/05-project-management.md) |
| 6 | Understand privacy, security, and administration | 10-15% | About an eighth | [06-privacy-security-administration.md](notes/06-privacy-security-administration.md) |
| 7 | Explore the GitHub community | 5-10% | A small slice | [07-github-community.md](notes/07-github-community.md) |

Domains 2, 3, 4 and 6 together are 40-60% of the exam, so do not treat them as minor just because each one is smaller than Domain 1.

## Study approach

### Phase 1: Git and GitHub basics (week 1)

Goal: be fluent with the vocabulary and the everyday workflow, because every other domain builds on it.

- Read [Domain 1](notes/01-git-and-github-basics.md) and do every command in it on a real repository.
- Walk through GitHub Flow end to end: branch, commit, push, pull request, review, merge, delete branch.
- Be able to explain, in one sentence each: Git vs GitHub, fetch vs pull, merge vs rebase, revert vs reset.
- Know the three account types and the two Enterprise deployment options.
- Use GitHub Desktop and GitHub Mobile once each so the "which tool" questions feel obvious.

### Phase 2: Repositories, collaboration and projects (week 2)

Goal: know the right feature for each collaboration need.

- [Domain 2](notes/02-repositories.md): build a repository with README, LICENSE, CONTRIBUTING, CODEOWNERS and SECURITY.md. Open each Insights view and note what it answers.
- [Domain 3](notes/03-collaboration.md): open an issue, link a PR with `Fixes #1`, review it, merge it. Set a repository to Custom watch. Create a gist, a wiki page and a Pages site.
- [Domain 5](notes/05-project-management.md): build a project with table, board and roadmap views, an iteration field and built-in workflows.

### Phase 3: Modern development, administration and community (week 3)

Goal: handle the newest and most scenario-heavy topics.

- [Domain 4](notes/04-modern-development.md): learn the Copilot plan line-up, agent mode vs the coding agent, and github.dev vs Codespaces until you can answer without thinking.
- [Domain 6](notes/06-privacy-security-administration.md): memorise the five repository roles in order, the organization roles, what EMUs restrict, and branch protection rules vs rulesets.
- [Domain 7](notes/07-github-community.md): licenses at a glance, Sponsors, follow vs star vs watch, Marketplace apps vs actions, InnerSource, fork vs template.

### Phase 4: Review and practice (week 4)

- Re-read the [fact sheet](fact-sheet.md) and its key differentiators table.
- Work through [scenarios.md](scenarios.md) and the [practice questions](../../../resources/practice-questions/github-foundations.md).
- Drill [flashcards.csv](flashcards.csv) for vocabulary.
- For every wrong answer, find the note section and re-read it, then write one line on why the right answer is right.

## Official and free resources

- **[📖 GH-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900)** - the skills measured; the single most important document
- **[📖 GitHub Foundations certification page](https://learn.microsoft.com/en-us/credentials/certifications/github-foundations/)** - logistics and scheduling
- **[📖 GitHub Foundations learning path, part 1](https://learn.microsoft.com/en-us/training/paths/github-foundations/)** - free Microsoft Learn modules
- **[📖 GitHub Foundations learning path, part 2](https://learn.microsoft.com/en-us/training/paths/github-foundations-2/)** - free Microsoft Learn modules, continued
- **[📖 GitHub Docs](https://docs.github.com)** - the reference every note links into
- **[📖 GitHub Skills](https://skills.github.com/)** - free hands-on courses that run inside a repository
- **[📖 Pro Git book](https://git-scm.com/book/en/v2)** - free, official Git book

## On exam day

### Time management

You have **100 minutes**. Microsoft does not publish the question count, so do not plan on a fixed number per minute. A workable approach:

- **First pass (about 65 minutes):** answer everything you know. Flag anything that needs more than a minute or two.
- **Second pass (about 25 minutes):** return to flagged questions. Re-read the scenario and eliminate options.
- **Final check (about 10 minutes):** make sure nothing is unanswered. There is no benefit to leaving a blank.
- If the exam includes interactive components, read their instructions carefully; they can take longer than a single multiple choice question.

### Question tactics

1. **Find the real ask.** Is it the best practice, the cheapest option, the least privilege, or the only feature that can do it?
2. **Spot the look-alike.** Many wrong options are the neighbouring feature: star instead of watch, fork instead of template, Maintain instead of Triage.
3. **Prefer GitHub-native and least effort.** If a built-in workflow does it, the answer is not "write a custom Action".
4. **Prefer least privilege.** If Triage is enough, Write is wrong.
5. **Watch for absolutes.** "Always", "never" and "only" are often the tell in a wrong option.

## Commonly confused pairs

| A | B | Key difference |
|---|---|----------------|
| Git | GitHub | Version control tool vs hosting and collaboration platform |
| `git fetch` | `git pull` | Download only vs download and merge |
| `git revert` | `git reset` | New undoing commit vs rewriting history |
| Fork | Template | Linked copy for contributing vs fresh copy with no link |
| Issue | Discussion | Tracked work vs open conversation |
| Star | Watch | Bookmark vs notifications |
| Assignee | Reviewer | Does the work vs reviews the PR |
| Label | Milestone | Many categories vs one goal with due date |
| Agent mode | Coding agent (Copilot cloud agent) | In the IDE while you watch vs on GitHub, returns a PR |
| Copilot Pro/Pro+ | Copilot Business/Enterprise | Individual vs centrally managed seats with policies |
| github.dev | Codespaces | Free browser editor, no terminal vs billed cloud VM with terminal |
| Triage | Maintain | Manage issues and PRs vs manage the repository without destructive settings |
| Billing manager | Security manager | Billing only vs security alerts and settings across all repositories |
| Branch protection rule | Ruleset | One rule per branch in one repo vs layered rules, org-wide on Enterprise |
| Private | Internal | Explicit access only vs every enterprise member |
| SAML SSO | Enterprise Managed Users | Person owns the account vs company owns the account |
| Secret scanning | Code scanning | Finds credentials vs finds vulnerable code patterns |
| Marketplace app | Marketplace action | Installed on an account vs referenced in a workflow |

## Common pitfalls

- **Studying the old outline.** Older guides weight collaboration as the biggest domain, quote a longer exam with a fixed question count, and say the certification expires. All of that is out of date.
- **Underweighting Domain 1.** It is the largest domain; Git and GitHub vocabulary must be automatic.
- **Treating Copilot as one product.** Know the plans and know agent mode from the coding agent.
- **Assuming "private" means a private website.** A Pages site from a private repository is public unless Enterprise Cloud access control is used.
- **Thinking secret gists are private.** They are unlisted.
- **Expecting closing keywords to work on any branch.** They close issues only on merge into the default branch.
- **Mixing up "public" and "licensed".** No LICENSE means no reuse rights.
- **Only reading.** Most of these features take five minutes to try, and trying them is what makes the scenario questions easy.
