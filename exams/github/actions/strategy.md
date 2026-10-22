---
last-updated: 2026-10-22
---

# GitHub Actions (GH-200) Study Strategy

## Format reminder

- 100 minutes, proctored, multiple choice with possible interactive items; pass mark 700 on a 1-1000 scale.
- Skills measured as of January 2026: five domains. Workflows (20-25%) and enterprise management (20-25%) are the two biggest; security and optimization (10-15%) is the smallest but feeds distractors everywhere.
- Questions are mostly short scenarios: a YAML snippet or a requirement, then pick the key, setting or fix.

## Study Approach

### Phase 1: Workflows, the largest domain (week 1)

Read [01-workflow-authoring.md](notes/01-workflow-authoring.md) and [02-expressions-contexts.md](notes/02-expressions-contexts.md), and type every example into a test repository. The aim is to predict, before you push, whether a workflow will trigger, which jobs will run in which order, what a matrix expands to, and which context is available in which key. Spend extra time on the topics the January 2026 outline added: service containers, YAML anchors, job summaries, retention through the REST API, and the static versus runtime split.

### Phase 2: Reading and debugging (week 2, first half)

Work through [03-consume-and-troubleshoot.md](notes/03-consume-and-troubleshoot.md) by breaking your own workflows: remove a permission, request a runner label that does not exist, let one matrix leg fail with `fail-fast` on, push with `GITHUB_TOKEN` and watch nothing trigger. Practise `gh run view --log-failed` and `gh run rerun --failed`. Learn the template versus reusable workflow versus composite action table until you can answer it without looking.

### Phase 3: Building actions (week 2, second half)

Build one action of each type from [04-custom-actions.md](notes/04-custom-actions.md). Publish a release with a `v1.0.0` tag and a moving `v1` tag, then call it by tag and by SHA from another repository. Note what changes when the action repository is private.

### Phase 4: Enterprise and security (week 3)

[05-enterprise-management.md](notes/05-enterprise-management.md) is now worth as much as workflows, so give it real time: policy options at each level, private action access, runner groups and labels, ephemeral runners and ARC, IP allow lists, secret scopes and precedence, and the REST flow for secrets. Then [06-secure-and-optimize.md](notes/06-secure-and-optimize.md): script injection, token permissions, OIDC trust policies, SHA pinning, artifact attestations and cost levers. If you can, use a free organization to click through the Actions policy pages.

### Phase 5: Practice (week 4)

Take the free Microsoft Learn practice assessment, the [practice question bank](../../../resources/practice-questions/github-actions.md) and the [scenarios](scenarios.md). For every miss, write down which domain and which rule you missed, and reread that section of the notes.

## Domain-specific tips

### Author and manage workflows (20-25%)
- Know which events read the workflow file from the default branch (`schedule`, `issues`, `issue_comment`, `repository_dispatch`).
- `exclude` is applied before `include`; an `include` entry that matches nothing becomes a new job.
- Service containers: `localhost` and `ports` on the runner, the service label as host name in a job container.
- If an answer uses `runner` or `steps` in a job-level `if:` or `runs-on`, it is wrong.

### Consume and troubleshoot workflows (15-20%)
- Cancelled matrix jobs after one failure are `fail-fast`, not more failures.
- "Set up job" tells you the image version, token permissions and resolved action SHAs.
- Templates are copied once; reusable workflows are called and stay in sync.

### Author and maintain actions (15-20%)
- Docker actions are Linux-only; JavaScript actions must ship bundled code.
- Composite `run` steps must declare `shell:`; composite outputs need `value:`.
- Marketplace needs a public repository with one root `action.yml` and no workflows.

### Manage GitHub Actions for the enterprise (20-25%)
- "Everyone, and nobody can change it" means an enforced policy at the highest level that owns all the repositories.
- A job stuck waiting for a runner: labels, runner group access, or all runners busy.
- Secret precedence: environment, then repository, then organization.

### Secure and optimize automation (10-15%)
- Untrusted text goes through `env:`, never straight into `run:`.
- `GITHUB_TOKEN` with least `permissions:` beats a PAT; OIDC beats stored cloud keys; a full SHA beats a tag.
- The cheapest run is the one you skip: path filters and `cancel-in-progress`.

## Exam Tactics

### Time management (100 minutes)
- Questions are short; aim for about one minute each on the first pass and flag anything that needs YAML tracing.
- Leave 15 minutes to revisit flagged items. Read every `on:`, `if:` and `permissions:` line in a snippet; the trap is usually in one of them.

### Reading answer options
- Eliminate options with invalid syntax first (wrong key names, `secrets` in `if:`, `steps` in `runs-on`).
- Between two valid answers, prefer the one with least privilege and least maintenance (reusable over copy-paste, OIDC over secrets, environment protection over manual process).
- Watch for "most secure" versus "simplest"; they point at different answers.

## Common Pitfalls

### Study mistakes
- Using pre-2026 material that puts workflows at 40% and enterprise at 15%.
- Reading about Actions without running and breaking workflows.
- Skipping the REST and CLI angle on retention, secrets, logs and artifacts.

### Content mistakes
- Confusing `pull_request` and `pull_request_target`.
- Treating `github.event.inputs` booleans as booleans.
- Forgetting the implicit `success()` in `if:`.
- Expecting `env` to flow into a reusable workflow.
- Expecting a re-run to use the latest workflow file.

## Readiness Indicators

- [ ] You can write a workflow with a matrix, a service container and a dependent deploy job from memory.
- [ ] You can explain which contexts each workflow key can see.
- [ ] You can diagnose a failed run from the log and re-run just the broken job.
- [ ] You have built and versioned a JavaScript, a Docker and a composite action.
- [ ] You can design runner groups, action policies and secret scopes for a multi-team organization.
- [ ] You can set up OIDC to a cloud provider and verify an artifact attestation.
- [ ] You score 80% or more on practice questions across all five domains.
