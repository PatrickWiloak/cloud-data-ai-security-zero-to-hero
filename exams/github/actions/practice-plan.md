---
last-updated: 2026-10-22
---

# GitHub Actions (GH-200) Study Plan

## 4-Week Study Schedule

Time is allocated by the January 2026 weights. Domains 1 and 4 (20-25% each) get the most days.

| Domain | Weight | Days |
|---|---|---|
| Author and manage workflows | 20-25% | 7 |
| Manage GitHub Actions for the enterprise | 20-25% | 5 |
| Consume and troubleshoot workflows | 15-20% | 4 |
| Author and maintain actions | 15-20% | 4 |
| Secure and optimize automation | 10-15% | 3 |
| Review and practice | - | 5 |

### Week 1: Author and Manage Workflows

#### Day 1-2: Triggers and events
- [ ] Read `notes/01-workflow-authoring.md` - "Configure workflow triggers and events"
- [ ] Build a workflow with `push` (branch and path filters), `pull_request` (activity types), `schedule` and `workflow_dispatch` with typed inputs
- [ ] Trigger it each way; confirm which events read the default branch's file

#### Day 3-4: Structure
- [ ] Read "Design and implement workflow structure"
- [ ] Add a job graph with `needs` and an `if: always()` report job
- [ ] Add a Postgres service container and connect from a test step
- [ ] Build a matrix with `include`, `exclude`, `fail-fast: false` and `max-parallel`
- [ ] Refactor repeated blocks with YAML anchors and aliases

#### Day 5-6: Expressions, contexts and outputs
- [ ] Read `notes/02-expressions-contexts.md`
- [ ] Pass values step to step (`GITHUB_OUTPUT`, `GITHUB_ENV`) and job to job (`needs.<id>.outputs`)
- [ ] Write a job summary to `GITHUB_STEP_SUMMARY`; add a status badge to the README
- [ ] Add caching to dependency install and an artifact upload with `retention-days`
- [ ] Set artifact and log retention with `gh api`

#### Day 7: Week 1 review
- [ ] Practice questions on domain 1; list every miss by sub-skill
- [ ] Install the GitHub Actions VS Code extension and fix the schema warnings it shows

### Week 2: Consume, Troubleshoot and Build Actions

#### Day 8-9: Consume and troubleshoot
- [ ] Read `notes/03-consume-and-troubleshoot.md`
- [ ] Break workflows on purpose: missing permission, bad runner label, failing matrix leg
- [ ] Use `gh run view --log-failed`, `gh run download`, `gh run rerun --failed`
- [ ] Turn on step debug logging and read the extra output

#### Day 10-11: Templates and reuse
- [ ] Create an organization workflow template (`.github/workflow-templates/` plus `.properties.json`)
- [ ] Create a reusable workflow with inputs, secrets and outputs; call it from another repository
- [ ] Write down the template vs reusable workflow vs composite action differences from memory
- [ ] Disable and re-enable a workflow

#### Day 12-13: Author and maintain actions
- [ ] Read `notes/04-custom-actions.md`
- [ ] Build a composite action, a JavaScript action (bundled `dist/`) and a Docker action
- [ ] Use `core.setOutput`, `core.setSecret`, `core.setFailed` and an annotation
- [ ] Release `v1.0.0`, add a moving `v1` tag, and call the action by tag and by SHA

#### Day 14: Week 2 review
- [ ] Practice questions on domains 2 and 3
- [ ] Re-read the troubleshooting tables

### Week 3: Enterprise, Security and Optimization

#### Day 15-16: Governance and runners
- [ ] Read `notes/05-enterprise-management.md`
- [ ] In a test organization, walk the Actions policy options (allowed actions, SHA pinning, fork PR approval, default token permissions)
- [ ] Share a private action through the Access setting
- [ ] Register a self-hosted runner with custom labels; put it in a runner group limited to one repository

#### Day 17: Runners at scale and networking
- [ ] Read about ephemeral runners and ARC
- [ ] Note the hosts a self-hosted runner must reach and how IP allow lists affect hosted runners
- [ ] Look up the software list for `ubuntu-latest` in `actions/runner-images`

#### Day 18: Secrets and variables
- [ ] Create organization (selected repos), repository and environment secrets with the same name; confirm precedence
- [ ] Set secrets and variables with `gh secret set` and `gh variable set`; fetch the repository public key with `gh api`

#### Day 19-20: Secure and optimize
- [ ] Read `notes/06-secure-and-optimize.md`
- [ ] Fix a script injection example by moving the value to `env:`
- [ ] Set `permissions: {}` at workflow level and grant per job
- [ ] Configure OIDC to a cloud account and remove the stored cloud secret
- [ ] Pin third-party actions to SHAs; enable Dependabot for actions
- [ ] Generate and verify an artifact attestation

#### Day 21: Week 3 review
- [ ] Practice questions on domains 4 and 5

### Week 4: Review and Exam Prep

#### Day 22-23: Weak areas
- [ ] Revisit the two domains with the lowest practice scores
- [ ] Reread the fact sheet tables

#### Day 24-25: Scenarios
- [ ] Work every scenario in `scenarios.md` without looking at the answer first
- [ ] Explain each distractor's flaw out loud

#### Day 26-27: Practice exams
- [ ] Microsoft Learn practice assessment, timed at 100 minutes
- [ ] Full practice question bank; review every wrong answer against the notes

#### Day 28: Pre-exam
- [ ] Light review of the fact sheet
- [ ] Check the exam sandbox and your Pearson VUE setup

## Quick Links

- **[📖 Exam GH-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200)** - skills measured
- **[📖 GitHub Actions documentation](https://docs.github.com/en/actions)** - reference
- **[📖 Automate your workflow with GitHub Actions](https://learn.microsoft.com/en-us/training/paths/github-actions/)** - free learning path
- **[📖 GitHub Actions certification](https://learn.microsoft.com/en-us/credentials/certifications/github-actions/)** - registration and practice assessment

## Final Exam Checklist

### One week before
- [ ] 80% or more on practice questions in every domain
- [ ] Comfortable reading YAML snippets for trigger, `if:` and `permissions:` traps
- [ ] Enterprise policies, runner groups and secret scopes reviewed

### Exam day
- [ ] Read each snippet line by line before reading the options
- [ ] Flag long questions and come back
- [ ] Use the full 100 minutes
