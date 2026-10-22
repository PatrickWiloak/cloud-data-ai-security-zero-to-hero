---
last-updated: 2026-10-22
applies-to: GH-200 skills measured as of January 2026, checked 2026-10-22
difficulty: intermediate
---

# GitHub Actions Certification (GH-200)

> **Outline updated 2026-10-22.** GitHub rewrote GH-200 in January 2026: five domains instead of four, a new "Secure and optimize automation" domain, troubleshooting added to "consume", and enterprise management raised to 20-25%. Earlier versions of this folder taught the older four-domain weights (workflows 40%, actions 25%, consume 20%, enterprise 15%) and logistics from before the move to Microsoft Learn.

## Exam Overview

GH-200 validates that you can automate software delivery with GitHub Actions: write and run workflows, read and debug them, build your own actions, run Actions across an organization or enterprise, and keep the automation secure and efficient. It is aimed at DevOps engineers, developers and platform engineers with intermediate, hands-on Actions experience. Exams are delivered through Microsoft Learn and Pearson VUE.

**Exam Details:**
- **Exam Code:** GH-200
- **Level:** Intermediate
- **Duration:** 100 minutes
- **Format:** Multiple choice, proctored; may include interactive components
- **Passing Score:** 700 (scaled 1-1000)
- **Cost:** Set by country; commonly listed as $99 USD in the US
- **Languages:** English, Spanish, Portuguese (Brazil), Korean, Japanese
- **Validity:** 2 years (GitHub is moving to Microsoft's recertification process)
- **Prerequisites:** None (GitHub Foundations is a sensible first step)
- **Retakes:** 24 hours after a first failed attempt, then per Microsoft's retake policy

**[📖 GitHub Actions certification](https://learn.microsoft.com/en-us/credentials/certifications/github-actions/)** - registration, logistics, practice assessment.
**[📖 Exam GH-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200)** - the skills measured. Re-check it before you sit the exam.

## Exam Domains

| # | Domain | Weight | Notes |
|---|---|---|---|
| 1 | Author and manage workflows | 20-25% | [01-workflow-authoring](notes/01-workflow-authoring.md), [02-expressions-contexts](notes/02-expressions-contexts.md) |
| 2 | Consume and troubleshoot workflows | 15-20% | [03-consume-and-troubleshoot](notes/03-consume-and-troubleshoot.md) |
| 3 | Author and maintain actions | 15-20% | [04-custom-actions](notes/04-custom-actions.md) |
| 4 | Manage GitHub Actions for the enterprise | 20-25% | [05-enterprise-management](notes/05-enterprise-management.md) |
| 5 | Secure and optimize automation | 10-15% | [06-secure-and-optimize](notes/06-secure-and-optimize.md) |

### What each domain covers

**1. Author and manage workflows.** Triggers of every kind (repository, webhook, scheduled, manual), with filters and typed `workflow_dispatch` and `workflow_call` inputs. Workflow structure: jobs, steps, conditions, `needs`, workflow commands and environment variables, service containers, matrices with `include`, `exclude`, `fail-fast` and `max-parallel`, and the effect of runner image changes. YAML anchors and aliases. The predefined contexts and the difference between expressions evaluated when the run is created and those evaluated on the runner. Execution and outputs: caching versus artifacts, retention set through the REST API, passing data with `GITHUB_OUTPUT` and `GITHUB_ENV`, job summaries, status badges and environment protections. Editor tooling such as the VS Code extension.

**2. Consume and troubleshoot workflows.** Reading a run: which event fired it, why a step failed, how a matrix expanded and which variant broke, and how to re-run a single job. Finding logs and artifacts in the UI and through the API or `gh`. Telling workflow templates (copied once), reusable workflows (called as a job) and composite actions (called as a step) apart, using organization templates including non-public ones, and disabling versus deleting a workflow.

**3. Author and maintain actions.** JavaScript, Docker and composite actions, the `action.yml` metadata file, workflow commands from inside an action, troubleshooting an action that will not start or fails, distribution models, publishing to Marketplace, semantic versioning with moving major tags, and immutable actions.

**4. Manage GitHub Actions for the enterprise.** Sharing reusable workflows and actions across an organization, controlling access to private actions, and enterprise and organization policies. Runners at scale: GitHub-hosted, larger and self-hosted runners, ephemeral runners and ARC, runner groups, IP allow lists and network requirements, troubleshooting queued jobs, and the preinstalled software on hosted images. Secrets and variables at organization, repository and environment level, used in workflows and managed through the REST API.

**5. Secure and optimize automation.** Environments with required reviewers, choosing trustworthy actions, script injection and its fixes, the `GITHUB_TOKEN` lifecycle and permissions compared with PATs, OIDC federation to cloud providers, pinning actions to full commit SHAs, action usage policies, artifact attestations and SLSA provenance, and keeping workflows fast and cheap.

## Study Materials in This Folder

| File | Use it for |
|---|---|
| [fact-sheet.md](fact-sheet.md) | One-page cram sheet: syntax, tables and limits |
| [notes/](notes/) | Six notes covering the five domains (domain 1 has two) |
| [scenarios.md](scenarios.md) | Worked scenarios in the exam's "pick the right setting or syntax" style |
| [practice-plan.md](practice-plan.md) | Four-week plan weighted by domain |
| [strategy.md](strategy.md) | Test-taking approach and the traps that cost points |
| [Practice questions](../../../resources/practice-questions/github-actions.md) | Original scenario questions with explanations |

## How to Get Hands-On

The exam rewards people who have broken and fixed real workflows. Create a throwaway repository and build, in order: a CI workflow with a matrix and a service container; a reusable workflow called from a second repository; a composite action and a small JavaScript action; a deployment job behind a protected environment that authenticates to a cloud account with OIDC; and a build that produces an artifact attestation you verify with `gh attestation verify`. Then break each one on purpose (wrong label, missing permission, injected title) and read the logs.

## Study Resources

### Official resources
- **[📖 GitHub Actions documentation](https://docs.github.com/en/actions)** - the source most questions are written from.
- **[📖 Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)** - the YAML reference.
- **[📖 Automate your workflow with GitHub Actions](https://learn.microsoft.com/en-us/training/paths/github-actions/)** - Microsoft Learn's free learning path for GH-200.
- **[📖 GitHub Skills](https://skills.github.com/)** - short interactive courses in your own repositories.
- **[📖 GitHub Changelog: Actions](https://github.blog/changelog/label/actions/)** - new features and deprecations that later appear on the exam.

### Community resources
- **[📖 Awesome Actions](https://github.com/sdras/awesome-actions)** - a curated list of actions and resources.
- **GitHub Community Discussions** - questions and answers from users and staff.

---

**Weighting tip:** domains 1 and 4 together are 40-50% of the exam. Know workflow syntax cold, but do not skip runner groups, policies and secret scopes, which older prep material treated as a small topic.
