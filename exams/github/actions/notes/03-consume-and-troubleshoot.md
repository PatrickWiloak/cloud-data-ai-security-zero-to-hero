---
last-updated: 2026-10-22
applies-to: GH-200 skills measured as of January 2026, checked 2026-10-22
difficulty: intermediate
---

# Domain 2: Consume and Troubleshoot Workflows (15-20%)

This domain is about reading and running workflows someone else wrote: interpreting what a run did and why it failed, finding logs and artifacts in the UI and the API, and using templates and reusable workflows. It was called "Consume workflows" before January 2026; troubleshooting is the new half.

**[📖 GH-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200)** - the skills list this note follows.
**[📖 Monitoring and troubleshooting workflows](https://docs.github.com/en/actions/how-tos/monitor-workflows)** - run history, logs, re-runs and debug logging.
**[📖 Reusing workflow configurations](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations)** - reusable workflows, their limits and YAML anchors.

## Interpret workflow behaviour and results

### Reading triggers from configuration and logs

When a workflow ran (or did not run) unexpectedly, start from the trigger. The run's summary page names the event (`push`, `pull_request`, `schedule`, `workflow_dispatch` and so on), the actor and the commit. Compare that against the `on:` section of the workflow **as it existed in that commit**, because GitHub reads the workflow file from the event's ref. Three behaviours explain most "why did it not run?" questions:

- **Filters must all match.** With both `branches` and `paths` on `push`, a commit that changes only ignored paths does not start a run.
- **Some events use the default branch's file.** `schedule`, `repository_dispatch`, `issues` and `issue_comment` read the workflow from the default branch (`workflow_dispatch` uses the branch you pick, which defaults to the default branch). Editing the file on a feature branch changes nothing for those events until it is merged.
- **Runs triggered by `GITHUB_TOKEN` do not trigger new runs.** A push made with the built-in token will not fire `push` workflows, to prevent loops. `workflow_dispatch` and `repository_dispatch` are the exceptions. Use a GitHub App token or a PAT when one workflow must deliberately trigger another through a push.

Approval gates also look like "nothing happened": a first-time contributor's fork pull request waits for a maintainer to approve the run, and a job targeting a protected environment waits for reviewers.

### Diagnosing failed runs

Every run page shows a graph of jobs, each with a status, and each job opens to a log grouped by step. Work top down:

1. **Find the first red step.** Later failures are often knock-on effects.
2. **Read the annotations.** Errors and warnings raised with `::error::` and `::warning::` or by actions appear at the top of the summary, often with file and line.
3. **Check the setup steps.** "Set up job" lists the runner image version, the `GITHUB_TOKEN` permissions and every action that was downloaded, with its resolved SHA. A job that worked yesterday and fails today on the same commit often shows a new image version here.
4. **Compare with the last green run.** Run history lets you filter by workflow, branch, event, actor and status.
5. **Turn on debug logging.** Re-run with "Enable debug logging", or set the repository secret or variable `ACTIONS_STEP_DEBUG` to `true` for step debug output and `ACTIONS_RUNNER_DEBUG` to `true` for runner diagnostic logs.

Common causes and their tells:

| Symptom | Likely cause |
|---|---|
| `Resource not accessible by integration` | `GITHUB_TOKEN` lacks a permission; add it under `permissions:` |
| Job queued for a long time, then cancelled | No runner matches the `runs-on` labels, or the runner group excludes the repository |
| Secret is empty | Fork pull request (no secrets), or the secret is in an environment the job does not reference |
| `Unable to resolve action` | Typo in `uses:`, a private action the repo cannot access, or an action blocked by policy |
| Step skipped unexpectedly | An implicit `success()` in its `if:` after an earlier failure |
| Works on Ubuntu, fails on Windows | Default shell is PowerShell on Windows; set `shell: bash` |

### Expanding YAML anchors when reading a workflow

A workflow that uses anchors (`&name`) and aliases (`*name`) is harder to read because the logic you need is written somewhere else in the file. Expand it mentally: wherever you see `*name`, paste the block that `&name` marks, exactly as written, at that position. The anchor must appear earlier in the file than the alias. If a question shows a job whose `env:` is `*common` and asks what `LOG_LEVEL` is, scroll up to the anchored mapping. The study guide also lists merge keys (`<<: *name`, which copy a mapping and then let later keys override it); GitHub's parser follows YAML 1.2, and merge-key support was reported missing when anchors launched, so check the current docs before writing them.

### Interpreting matrix expansions

Each matrix job is named after the job plus its values, for example `test (ubuntu-latest, 22)`. That name is how you map a failure to an axis. Patterns to look for:

- **Fails on every `windows-latest` job** - an OS problem: shell, path separators, line endings.
- **Fails on one version across all OSes** - a runtime version problem.
- **One combination only** - often flaky, or an `include` entry that added an unexpected key.
- **Many jobs show "cancelled"** - `fail-fast: true` (the default) cancelled them after one failure. Only the first failure is real evidence.

You can re-run all jobs, only the failed jobs, or a single job (including one matrix job) from the run page or with `gh run rerun RUN_ID --failed` or `--job JOB_ID`. A re-run uses the same commit and workflow file as the original run and increments `github.run_attempt`, so it does not pick up a fix you pushed since.

**[📖 Re-running workflows and jobs](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/re-run-workflows-and-jobs)** - re-run all, failed or single jobs, with debug logging.

## Access workflow artifacts and logs

In the UI, the **Actions** tab lists workflows on the left and runs on the right. A run page shows the summary (with job summaries and annotations), the job graph and an **Artifacts** section. Logs can be viewed per step, searched, and downloaded as a zip from the gear menu. Deleting logs is also there for people with write access.

The same data is available through the API and the GitHub CLI, which is how you script it:

```bash
gh run list --workflow ci.yml --branch main --limit 5
gh run view RUN_ID --log-failed        # only logs of failed steps
gh run download RUN_ID -n test-report  # one artifact by name
gh run watch RUN_ID --exit-status      # follow a run, fail if it fails

# REST equivalents
gh api repos/OWNER/REPO/actions/runs/RUN_ID/logs > logs.zip
gh api repos/OWNER/REPO/actions/runs/RUN_ID/artifacts
```

Inside a later job of the same run, download with `actions/download-artifact`. Since v4 of the artifact actions, artifacts are immutable once uploaded, names must be unique within a run, and a download can pull artifacts from another run or repository when given a token and run ID. Artifacts expire at the retention limit (90 days by default for public repositories), and an expired artifact cannot be recovered.

**[📖 Downloading workflow artifacts](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/download-workflow-artifacts)** - UI, CLI and API.
**[📖 Using workflow run logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs)** - searching, downloading and deleting logs.

## Use and manage workflow templates

### Three ways to share automation

The exam expects you to tell these apart, because they solve different problems.

- **Workflow template** (still called a **starter workflow** in the guide) - a file that is **copied** into a repository when someone picks it from "New workflow". After the copy, the new workflow is independent: improvements to the template do not reach it. Good for giving teams a sensible starting point they will customise.
- **Reusable workflow** - a whole workflow with `on: workflow_call` that other workflows **call** with `jobs.<id>.uses: owner/repo/.github/workflows/file.yml@ref`. One central, versioned definition; callers get updates when they move the ref. It runs its own jobs, on runners it chooses.
- **Composite action** - a list of steps packaged as an action (`runs.using: composite`) and called with `steps[*].uses`. It runs inside the caller's job, on the caller's runner. Good for a repeated sequence of steps such as "set up toolchain and restore cache".

| | Workflow template | Reusable workflow | Composite action |
|---|---|---|---|
| How it is used | Copied once | Called as a job | Called as a step |
| Updates reach users | No | Yes, when the ref moves | Yes, when the ref moves |
| Contains | Full workflow | Jobs, with their own `runs-on` | Steps only |
| Secrets | Normal for the repo | Passed explicitly or `secrets: inherit` | Passed as inputs or env |
| Logs | Normal | Each job and step shown separately | Shown as one step with collapsed sub-steps |
| Nesting limit | n/a | 10 levels; up to 50 unique reusable workflows per file | Composite actions can call other actions |

### Organization templates, including non-public ones

Organization workflow templates live in the organization's `.github` repository under `workflow-templates/`. Each template is a `.yml` file plus a matching `.properties.json` with its name, description, icon and `filePatterns` that decide when GitHub suggests it. A template can use `$default-branch` and `$protected-branches` placeholders.

Since September 2025 the `.github` repository does not have to be public. If it is **internal**, internal and private repositories in the organization can use its templates. If it is **private**, only private repositories can. Public repositories still need a public `.github` repository.

**[📖 Creating workflow templates for your organization](https://docs.github.com/en/actions/how-tos/reuse-automations/create-workflow-templates)** - file layout and metadata.

### Consuming organization and reusable workflows

```yaml
jobs:
  ci:
    uses: my-org/platform-workflows/.github/workflows/node-ci.yml@v3
    with:
      node-version: '22'
    secrets: inherit
    permissions:
      contents: read
  deploy:
    needs: ci
    uses: ./.github/workflows/deploy.yml     # same repository
    with:
      environment: staging
```

Rules to remember when consuming one:

- **Reference format.** `{owner}/{repo}/.github/workflows/{file}@{ref}` for another repository, or `./.github/workflows/{file}` for the same repository and commit. The ref can be a SHA, tag or branch; a SHA is safest.
- **Access.** A reusable workflow in a private or internal repository can only be called if that repository's Actions settings allow access from the caller.
- **Permissions only go down.** The called workflow can reduce the `GITHUB_TOKEN` permissions it receives from the caller, never raise them.
- **`env` does not flow.** Environment variables set in the caller are not visible in the called workflow, and the `env` context cannot be used in the caller's `with:` for it. Use inputs.
- **Outputs come back through `needs`.** The caller reads `needs.ci.outputs.<name>`.

### Disabling versus deleting workflows

**Disabling** (Actions tab, workflow menu, "Disable workflow", or `gh workflow disable`) stops new runs from any trigger but keeps the file and all history; you can enable it again. It is the right move for a misbehaving scheduled job or a workflow you need to pause during an incident. **Deleting** the YAML file from the default branch removes the workflow from the list going forward, but its past runs stay until you delete them. GitHub also disables scheduled workflows automatically in public repositories after 60 days without activity.

## Triggering one workflow from another

- **`workflow_run`** - start this workflow when another workflow completes (`types: [completed]`, filter on `workflows:` and branches). Runs from the default branch with access to secrets, which makes it the safe second stage after an untrusted `pull_request` build.
- **`workflow_dispatch` via API** - `POST /repos/{owner}/{repo}/actions/workflows/{file}/dispatches` with a `ref` and `inputs`, or `gh workflow run file.yml -f key=value`.
- **`repository_dispatch`** - `POST /repos/{owner}/{repo}/dispatches` with an `event_type` and `client_payload`; useful for cross-repository and external triggers.

## Key terms

- **Run history** - the filterable list of runs for a workflow, used to compare a failure against the last success.
- **Annotation** - an error, warning or notice attached to a run, often pointing at a file and line.
- **Step debug logging** - extra log detail enabled by `ACTIONS_STEP_DEBUG` or by re-running with debug logging.
- **Runner diagnostic logging** - runner-level logs enabled by `ACTIONS_RUNNER_DEBUG`.
- **run_attempt** - counter that increases each time a run is re-run.
- **Workflow template** - a starter workflow copied into a repository, independent after creation.
- **Reusable workflow** - a workflow with `on: workflow_call` that other workflows call as a job.
- **Composite action** - an action made of steps that runs inside the caller's job.
- **secrets: inherit** - passes all of the caller's secrets to a reusable workflow in the same organization or enterprise.
- **workflow_run** - trigger that starts a workflow when another workflow finishes.
- **Disable workflow** - stops a workflow from running without deleting its file or history.
