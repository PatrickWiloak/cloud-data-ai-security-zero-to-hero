---
last-updated: 2026-10-22
applies-to: GH-900 skills measured as of January 2026, checked 2026-10-22
difficulty: beginner
---

# GitHub Foundations (GH-900) Certification Exam Guide

> **Outline updated 2026-10-22.** GitHub rewrote GH-900 in January 2026 and moved delivery to Microsoft Learn. Earlier versions of this folder used the older seven-domain weights and logistics.

## Exam Overview

GitHub Foundations is GitHub's entry-level certification. It checks that you understand Git and GitHub basics, repositories, collaboration, modern development features (Actions, Copilot, Codespaces), project management, privacy and administration, and the GitHub community. It suits developers new to GitHub, students, project managers, and anyone in a technical or business role who works alongside GitHub.

### Exam Details

- **Exam Code:** GH-900
- **Level:** Beginner
- **Duration:** 100 minutes
- **Questions:** Not published by Microsoft
- **Format:** Multiple choice; the exam may include interactive components
- **Passing Score:** 700 (on a scale of 1-1000)
- **Cost:** Based on country; commonly listed as $99 USD in the US
- **Delivery:** Proctored, scheduled through Pearson VUE via Microsoft Learn
- **Languages:** English, Spanish, Portuguese (Brazil), Korean, Japanese
- **Prerequisites:** None
- **Validity:** Does not expire; the certification does not require renewal
- **Retake Policy:** Wait 24 hours before the first retake; after that, Microsoft's exam retake policy applies

### Official Resources

- **[📖 GitHub Foundations certification page](https://learn.microsoft.com/en-us/credentials/certifications/github-foundations/)** - registration, price, languages and policies
- **[📖 GH-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900)** - the official skills measured, with change log
- **[📖 GitHub Foundations learning path, part 1](https://learn.microsoft.com/en-us/training/paths/github-foundations/)** - free Microsoft Learn modules
- **[📖 GitHub Foundations learning path, part 2](https://learn.microsoft.com/en-us/training/paths/github-foundations-2/)** - free Microsoft Learn modules, continued
- **[📖 GitHub Docs](https://docs.github.com)** - the product documentation every note links into

## Exam Domains

| # | Domain | Weight | Notes |
|---|--------|--------|-------|
| 1 | Understand Git and GitHub basics | 25-30% | [01-git-and-github-basics.md](notes/01-git-and-github-basics.md) |
| 2 | Work with GitHub repositories | 10-15% | [02-repositories.md](notes/02-repositories.md) |
| 3 | Collaborate using GitHub | 10-15% | [03-collaboration.md](notes/03-collaboration.md) |
| 4 | Apply modern development practices | 10-15% | [04-modern-development.md](notes/04-modern-development.md) |
| 5 | Manage projects with GitHub | 5-10% | [05-project-management.md](notes/05-project-management.md) |
| 6 | Understand privacy, security, and administration | 10-15% | [06-privacy-security-administration.md](notes/06-privacy-security-administration.md) |
| 7 | Explore the GitHub community | 5-10% | [07-github-community.md](notes/07-github-community.md) |

Weights are from the Microsoft Learn study guide, skills measured as of January 2026. Re-check it before you book.

## What each domain covers

**Domain 1: Understand Git and GitHub basics (25-30%).** The largest domain by a clear margin. It starts with why version control exists and how Git (the tool) differs from GitHub (the platform), then covers repositories, commits and branches. On the GitHub side it covers personal, organization and enterprise accounts, Enterprise Cloud versus Enterprise Server, GitHub Flow, Markdown in issues and pull requests, and when to use GitHub Desktop or GitHub Mobile. Expect plenty of "which is which" questions here.

**Domain 2: Work with GitHub repositories (10-15%).** What a well-built repository contains (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY.md), creating repositories and using templates, adding and managing files, the Insights tab (Pulse, Contributors, Traffic, Dependency graph), stars and feature previews, dependency insights, and maintenance habits such as topics, branch hygiene and archiving.

**Domain 3: Collaborate using GitHub (10-15%).** Issues versus pull requests versus discussions, linking PRs to issues with closing keywords, issue and PR templates, filters and assignments, notifications and watch levels, and the three publishing features: Gists, Wikis and GitHub Pages.

**Domain 4: Apply modern development practices (10-15%).** GitHub Actions at a purpose level, GitHub Copilot including agent mode, the coding agent (now Copilot cloud agent), multi-model choice and the plan line-up (Free, Pro, Pro+, Business, Enterprise), Codespaces and dev containers, and the github.dev editor versus Codespaces.

**Domain 5: Manage projects with GitHub (5-10%).** GitHub Projects with table, board and roadmap layouts, custom fields and iterations, built-in workflow automations, project insights charts, and the supporting tools: labels, milestones, assignees and saved replies.

**Domain 6: Understand privacy, security, and administration (10-15%).** 2FA methods and passkeys, repository roles (read, triage, write, maintain, admin), organization roles, teams, Enterprise Managed Users, organization-wide Copilot policies, repository visibility, branch protection rules versus rulesets, and security features at awareness level.

**Domain 7: Explore the GitHub community (5-10%).** Open source and its benefits, licenses at awareness level, how GitHub supports open source, GitHub Sponsors, following and starring, Explore and topics, GitHub Marketplace, InnerSource, and forks versus templates.

## Study Materials

| Material | What it is for |
|----------|----------------|
| [fact-sheet.md](fact-sheet.md) | Logistics and a one-page cram summary per domain |
| [notes/](notes/) | In-depth teaching notes, one file per domain (links in the domain table above) |
| [scenarios.md](scenarios.md) | Exam-style scenarios with explanations of right and wrong answers |
| [flashcards.csv](flashcards.csv) | Generated flashcards from the notes' glossary lines |
| [practice-plan.md](practice-plan.md) | A four-week day-by-day plan weighted by domain |
| [strategy.md](strategy.md) | How to study, time management on the day, and commonly confused pairs |
| [Practice questions](../../../resources/practice-questions/github-foundations.md) | Additional practice questions for this exam |

## Common exam patterns

- Many questions contrast look-alikes: Git versus GitHub, fetch versus pull, fork versus template, issue versus discussion, star versus watch, agent mode versus the coding agent, github.dev versus Codespaces, branch protection rules versus rulesets.
- Scenario questions ask for the best-fit feature, not the only possible one. Prefer the GitHub-native, least-privilege, least-effort answer.
- Security and administration questions test awareness and role fit, not deep configuration.
- Copilot questions focus on what each plan and agent is for, not on prompt writing.

## Hands-on practice

- Create a free GitHub account, a repository with a README, LICENSE and CODEOWNERS, and run through GitHub Flow end to end.
- Open issues, link a pull request with `Fixes #1`, review it and squash-merge it.
- Create a project with table, board and roadmap views and turn on the built-in workflows.
- Press `.` on a repository to try github.dev, then open a codespace and compare.
- Add a ruleset to `main` and see a direct push get rejected.
- Turn on 2FA with an authenticator app and add a passkey.
