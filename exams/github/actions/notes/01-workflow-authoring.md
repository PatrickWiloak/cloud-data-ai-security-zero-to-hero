---
last-updated: 2026-10-22
applies-to: GH-200 skills measured as of January 2026, checked 2026-10-22
difficulty: intermediate
---

# Domain 1: Author and Manage Workflows (20-25%) - Part 1

This note covers the first domain's three skill groups: configure workflow triggers and events, design and implement workflow structure, and manage workflow execution and outputs. Expressions and contexts, which the same domain also tests, have their own note: [02-expressions-contexts.md](02-expressions-contexts.md).

**[📖 GH-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200)** - the skills list this note follows.
**[📖 Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)** - the complete YAML reference.
**[📖 Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)** - every event, its activity types and its filters.

## How a workflow is put together

A workflow is a YAML file in `.github/workflows/` on a branch. GitHub reads the file from the commit that the event points at, decides whether the `on:` section matches the event, and if it does, creates a **workflow run**. A run contains one or more **jobs**. Each job gets its own fresh runner (a virtual machine or a container host), so nothing on disk carries over from one job to another unless you move it on purpose with artifacts, caches or outputs. Inside a job, **steps** run one after another on the same machine and share its file system.

That chain - event, workflow, run, job, step - explains most exam questions about ordering and data passing. Jobs are parallel unless you join them with `needs`. Steps are always sequential. A file written by step 2 is visible to step 3, but not to a different job.

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read

env:
  NODE_VERSION: '20'

jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v5
      - uses: actions/setup-node@v5
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: npm
      - run: npm ci
      - run: npm test
```

The top-level keys you must recognise are `name`, `run-name` (a dynamic title for each run), `on`, `permissions`, `env`, `defaults` (default `shell` and `working-directory` for `run` steps), `concurrency` and `jobs`.

**[📖 Understanding GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions)** - the vocabulary of events, runners, jobs, steps and actions.

## Configure workflow triggers and events

### Four families of events

The study guide groups triggers into scheduled, manual, webhook and repository events. In practice they look like this:

- **Repository and webhook events** - `push`, `pull_request`, `pull_request_target`, `issues`, `issue_comment`, `release`, `workflow_run` and dozens more. Each fires when something happens in the repository, and most accept `types:` to narrow the activity (for example `pull_request: types: [opened, synchronize, reopened]`, which is also the default set).
- **Scheduled events** - `schedule` with one or more POSIX cron strings. They run in UTC, on the latest commit of the default branch only, and can be delayed at busy times. GitHub disables scheduled workflows in public repositories after 60 days with no repository activity.
- **Manual events** - `workflow_dispatch`, which adds a "Run workflow" button and an API endpoint, with typed inputs.
- **External events** - `repository_dispatch`, which an outside system calls through the REST API with a custom `event_type` and a `client_payload`.

```yaml
on:
  push:
    branches: [main, 'release/**']
    paths-ignore: ['docs/**', '**.md']
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]
  schedule:
    - cron: '30 3 * * 1-5'      # 03:30 UTC, Monday to Friday
  workflow_dispatch:
  repository_dispatch:
    types: [deploy-requested]
```

### Filters

`branches`, `tags` and `paths` take glob patterns, and each has an `-ignore` twin. You cannot use a filter and its `-ignore` form for the same event, but you can get the same effect with negative patterns (`'!release/**-alpha'`) inside the positive list. When both a branch filter and a path filter are present on `push`, **both** must match for the workflow to run. Path filters are what keep a monorepo from rebuilding everything on every commit.

Exam trap: a `push` that only creates a tag does not match a `branches` filter, and a `push` that only touches ignored paths does not start the run at all, so required status checks that depend on that workflow will sit at "Expected - waiting" on a pull request. The usual fix is a lightweight job that always runs, or a ruleset that does not require the skipped check.

### Choosing scope, permissions and event

The guide asks you to "choose appropriate scope, permissions, and events". Three decisions hide in that phrase:

1. **Which event carries the right context?** `pull_request` runs the code from the pull request's merge commit with a read-only token and no secrets when the PR comes from a fork. `pull_request_target` runs the workflow file from the **base** branch with a token that can write and with access to secrets. That makes `pull_request_target` safe only for jobs that never check out or execute the untrusted PR code (labelling, commenting). The security note covers this in depth.
2. **Which `GITHUB_TOKEN` permissions does the job need?** Declare them with `permissions:` at workflow or job level. Anything you do not list is set to `none` once you list any scope.
3. **Which trigger is narrow enough?** `issue_comment` fires for comments on issues **and** pull requests; check `github.event.issue.pull_request` if you only want PR comments. `workflow_run` runs after another workflow finishes and is the standard way to run privileged follow-up work after an untrusted `pull_request` build.

### `workflow_dispatch` inputs and `workflow_call` inputs

Manual runs accept up to 25 inputs of type `string`, `boolean`, `choice`, `number` or `environment`. Each can be `required` and have a `default`. Inside the workflow they are read through the `inputs` context, which keeps booleans as booleans (the older `github.event.inputs` context turns every value into a string - a classic trap in `if:` conditions).

```yaml
on:
  workflow_dispatch:
    inputs:
      target:
        description: Where to deploy
        type: environment
        required: true
      dry_run:
        type: boolean
        default: true
      replicas:
        type: number
        default: 2
```

A **reusable workflow** declares its interface under `on: workflow_call:` with `inputs`, `secrets` and `outputs`. The caller passes values with `with:` and `secrets:` (or `secrets: inherit`). Inputs to `workflow_call` support `string`, `boolean` and `number`. A common pattern is a workflow that is both manually runnable and reusable: declare the same inputs under both `workflow_dispatch` and `workflow_call`, and read them through `inputs` so the body does not care which trigger fired.

```yaml
on:
  workflow_call:
    inputs:
      environment:
        type: string
        required: true
    secrets:
      deploy_key:
        required: true
    outputs:
      url:
        value: ${{ jobs.deploy.outputs.url }}
```

**[📖 Reusing workflow configurations](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations)** - reusable workflows, YAML anchors and their limits.

## Design and implement workflow structure

### Jobs, steps and conditions

Every job needs `runs-on` (or `uses:` when the job calls a reusable workflow). Useful job keys: `name`, `needs`, `if`, `environment`, `concurrency`, `outputs`, `env`, `defaults`, `timeout-minutes` (default 360), `continue-on-error`, `container`, `services` and `strategy`. Steps are either `uses:` (run an action) or `run:` (run a shell command), and each can have `id`, `name`, `if`, `env`, `with`, `shell`, `working-directory`, `timeout-minutes` and `continue-on-error`.

An `if:` on a job or step is an expression. When you omit the status function, GitHub silently adds `success()`, which is why a cleanup step "never runs" after a failure until you write `if: always()` or `if: failure()`.

### Dependencies between jobs

`needs: build` makes a job wait for `build` and skip itself if `build` fails or is skipped. `needs: [lint, test]` waits for both. To run a job whatever happened upstream, combine `needs` with `if: ${{ always() }}`, and then check `needs.<job>.result` (`success`, `failure`, `cancelled` or `skipped`) inside it. That is the shape of a "notify" or "report" job.

```mermaid
flowchart LR
  lint --> test
  build --> test
  test --> deploy
  test --> report
```

The diagram shows a fan-in: `test` needs both `lint` and `build`, which run in parallel, and `deploy` and `report` both wait for `test`. `report` would carry `if: always()` so it still runs when `test` fails.

### Workflow commands and environment variables

A step talks back to the runner in two ways. **Environment files** are the modern route: append lines to the file named by `GITHUB_ENV` (set a variable for later steps), `GITHUB_OUTPUT` (set a step output), `GITHUB_PATH` (prepend to `PATH`) or `GITHUB_STEP_SUMMARY` (add Markdown to the run summary). **Workflow commands** are special strings printed to standard output, such as `::warning file=app.js,line=10::Deprecated call`, `::error::`, `::notice::`, `::group::`/`::endgroup::`, `::add-mask::` and `::debug::` (shown only when debug logging is on). The old `set-output` and `set-env` commands are deprecated because they let anything printed to the log change the job's state.

Variables have three scopes - workflow `env`, job `env` and step `env` - and the most specific wins. Default variables that GitHub sets, such as `GITHUB_SHA`, `GITHUB_REF`, `GITHUB_WORKSPACE`, `RUNNER_OS` and `RUNNER_TEMP`, are environment variables on the runner. The matching context values (`github.sha`, `runner.os`) are available to expressions before the job reaches the runner.

**[📖 Workflow commands](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands)** - environment files, annotations, masking and grouping.
**[📖 Variables reference](https://docs.github.com/en/actions/reference/workflows-and-actions/variables)** - default environment variables and configuration variables.

### Service containers

When tests need a real database or queue, add `services:` to the job. GitHub starts each service as a Docker container before the steps run and tears it down afterwards. How you reach it depends on where the job runs:

- **Job runs directly on the runner** - map a port (`ports: ['5432:5432']`) and connect to `localhost:5432`.
- **Job runs in a container** (`container:` is set) - the job and its services share a Docker network, so you connect by the service's label as a host name (`postgres:5432`) and need no port mapping.

Health checks go in `options:` as Docker flags, so the job does not start until the service is ready. Service containers need a Linux runner, because they rely on Docker.

```yaml
jobs:
  integration:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: postgres
        ports: ['5432:5432']
        options: >-
          --health-cmd "pg_isready -U postgres"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    steps:
      - uses: actions/checkout@v5
      - run: npm run test:integration
        env:
          DATABASE_URL: postgres://postgres:postgres@localhost:5432/postgres
```

**[📖 About service containers](https://docs.github.com/en/actions/tutorials/use-containerized-services/use-docker-service-containers)** - networking, ports and health checks.

### Matrix strategies

`strategy.matrix` turns one job definition into many. Each key is an axis, and GitHub runs one job per combination, up to 256 jobs per workflow run.

```yaml
strategy:
  fail-fast: false
  max-parallel: 4
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [20, 22, 24]
    exclude:
      - os: windows-latest
        node: 20
    include:
      - os: ubuntu-latest
        node: 24
        coverage: true      # adds a key to an existing combination
      - os: macos-latest
        node: 24            # adds a brand-new combination
```

The rules worth memorising:

- **`exclude` runs first, then `include`.** An `include` entry that matches an existing combination on all its original keys adds the extra keys (here `coverage: true`) to it. An entry that matches nothing becomes a new job.
- **`fail-fast` defaults to `true`.** One failed matrix job cancels the rest that are queued or running. Set it to `false` when you want the full picture across versions.
- **`max-parallel`** caps how many matrix jobs run at once, which protects shared resources and self-hosted capacity.
- **`continue-on-error`** at job level, often driven by a matrix value such as `experimental: true`, lets one variant fail without failing the run.
- **Cost.** A 3 x 3 x 2 matrix is 18 jobs, and macOS and Windows minutes cost more than Linux minutes. Trim axes with `exclude`, run the full matrix only on `main` or on a schedule, and keep pull request runs small.

Runner images also move under you. `ubuntu-latest`, `windows-latest` and `macos-latest` are labels that GitHub re-points to newer images over time. The Ubuntu 20.04 image was retired in 2025, and `windows-latest` has been migrating to Windows Server 2025. A matrix that names an old explicit image (`ubuntu-20.04`) fails once that image is removed, and a matrix on a `-latest` label can break when the label moves to an image with different preinstalled tool versions. Pin explicit image versions for reproducibility, and read the runner-images release notes when a "nothing changed" build starts failing.

**[📖 Running variations of jobs in a workflow](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations)** - matrix, include, exclude, fail-fast and max-parallel.
**[📖 actions/runner-images](https://github.com/actions/runner-images)** - image labels, deprecations and the software on each image.

### YAML anchors and aliases

Since September 2025 GitHub Actions accepts YAML anchors (`&name`) and aliases (`*name`) inside one workflow file. You mark a block once and reuse it, which removes copy-paste between jobs that share the same steps or environment.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    env: &common-env
      NODE_ENV: test
      LOG_LEVEL: debug
    steps:
      - &checkout
        uses: actions/checkout@v5
      - run: npm test
  lint:
    runs-on: ubuntu-latest
    env: *common-env
    steps:
      - *checkout
      - run: npm run lint
```

Three limits decide when to reach for something else. The parser expands anchors before Actions evaluates anything, so an anchor cannot take parameters or be conditional. An anchor must be defined above the alias that uses it. And anchors work only inside one file: reuse across files or repositories needs a composite action or a reusable workflow.

Exam trap: the GH-200 skills list mentions the YAML merge key (`<<: *anchor`), but GitHub's parser follows YAML 1.2, which has no merge key, and community testing after the launch reported that merge keys are not supported. Know what a merge key would do (copy a mapping and override some keys) and read the current GitHub docs before relying on it.

### Predefined contexts and version pinning

The study guide lists the contexts you should be able to use: `github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `strategy`, `job`, `steps`, and the event payload under `github.event`. They are covered with examples in [02-expressions-contexts.md](02-expressions-contexts.md). The same bullet asks you to understand **immutable actions** and version pinning. In short: a tag such as `@v4` can be moved by the action's owner, while a full 40-character commit SHA cannot. GitHub has been moving published actions to immutable packages served from its own registry, which makes a release unchangeable once published. The security note ([06-secure-and-optimize.md](06-secure-and-optimize.md)) explains why pinning to a SHA is still the safe default.

### Editor tooling

The **GitHub Actions extension for VS Code** reads your workflows and the repository's settings, so it can validate syntax against the schema, autocomplete keys and action inputs (IntelliSense from each action's `action.yml`), flag unknown secrets or variables, and show recent runs and logs without leaving the editor. Any YAML language server with the workflow JSON schema gives you completion and validation too. The exam angle is "how do you catch a typo in `runs-on` before you push" - the answer is schema validation in the editor, not trial-and-error commits.

**[📖 GitHub Actions for VS Code](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-github-actions)** - the official extension.

## Manage workflow execution and outputs

### Caching versus artifacts

Both store files, but they solve different problems, and the exam likes to swap them.

- **Cache** (`actions/cache`, or the `cache:` input on `setup-*` actions) - speeds up **future runs** by restoring dependencies that rarely change. It is looked up by a `key`, usually built from a lock-file hash (`${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}`), with `restore-keys` as prefix fallbacks. Caches are scoped to a branch and can be read from the base and default branch. Unused entries are evicted after 7 days, and the repository has a size limit beyond which the oldest entries go.
- **Artifact** (`actions/upload-artifact` and `download-artifact`) - keeps the **output of this run**: build packages, test reports, coverage. Other jobs in the same run can download it, and people can download it from the run page or the API until it expires.

If the question says "speed up dependency install", answer cache. If it says "pass the build to the deploy job" or "keep the test report", answer artifact.

### Retention policies

Artifacts and logs are kept for 90 days by default on public repositories and up to 400 days on private ones. You can lower the limit for one upload with `retention-days:` and set the default at repository, organization or enterprise level in the Actions settings. The study guide expects you to know that these settings are also exposed through the REST API, which is how a platform team applies one policy across hundreds of repositories:

```bash
# Set artifact and log retention for an organization to 30 days
gh api -X PUT orgs/OWNER/actions/permissions/artifact-and-log-retention \
  -f days=30

# Delete one artifact, or one workflow run and its logs
gh api -X DELETE repos/OWNER/REPO/actions/artifacts/ARTIFACT_ID
gh api -X DELETE repos/OWNER/REPO/actions/runs/RUN_ID
```

**[📖 Storing and sharing data from a workflow](https://docs.github.com/en/actions/tutorials/store-and-share-data)** - artifacts, retention and downloading.
**[📖 Dependency caching reference](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching)** - keys, scope, eviction and limits.
**[📖 REST API endpoints for GitHub Actions](https://docs.github.com/en/rest/actions)** - artifacts, caches, runs, permissions and retention.

### Passing data between steps and jobs

- **Step to later step in the same job** - write `name=value` to `$GITHUB_OUTPUT` in a step with an `id`, then read `steps.<id>.outputs.name`. For environment variables, write to `$GITHUB_ENV`; the new value is visible from the **next** step, not the one that wrote it.
- **Job to job** - map a step output to a job output under `jobs.<id>.outputs`, then read `needs.<id>.outputs.<name>` in a job that `needs` it. Job outputs are strings, limited to 1 MB each, and outputs that contain a secret are redacted and not passed.
- **Large files between jobs** - upload and download an artifact.
- **Reusable workflow to caller** - declare `on.workflow_call.outputs` mapped from a job output, then read `needs.<calling-job>.outputs.<name>` in the caller.

Multi-line values use a delimiter: `echo "notes<<EOF" >> "$GITHUB_OUTPUT"`, the lines, then `echo "EOF" >> "$GITHUB_OUTPUT"`.

### Job summaries

Anything a step appends to `$GITHUB_STEP_SUMMARY` is rendered as GitHub-flavoured Markdown on the run's summary page, under the job name. It is the right place for a test results table, a coverage figure or deployment links, and far easier to read than the raw log. Each step's summary is limited to 1 MiB, and secrets that appear in it are masked like they are in logs.

```bash
{
  echo "## Test results"
  echo "| Suite | Passed | Failed |"
  echo "|---|---|---|"
  echo "| unit | 412 | 0 |"
} >> "$GITHUB_STEP_SUMMARY"
```

### Status badges and environment protections

A status badge shows the latest result of a workflow, usually on `main`, in a README:

```markdown
![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg?branch=main)
```

The `branch=` and `event=` query parameters choose which runs the badge reflects. You can copy the snippet from the workflow's page with "Create status badge".

**Environments** are named deployment targets (`staging`, `production`) that a job joins with `environment:`. An environment can hold its own secrets and variables and can carry **protection rules**: required reviewers who must approve the job before it starts, a wait timer, deployment branch and tag rules, and custom protection rules from GitHub Apps. A job waiting for approval does not consume runner minutes. Environment secrets are only released to the job after the rules pass, which is why production credentials belong there and not in repository secrets.

**[📖 Managing environments for deployment](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments)** - protection rules, environment secrets and branch policies.
**[📖 Adding a workflow status badge](https://docs.github.com/en/actions/how-tos/monitor-workflows/add-a-status-badge)** - badge URL options.

### Concurrency

`concurrency:` at workflow or job level makes runs with the same group key queue behind each other, and `cancel-in-progress: true` cancels the older run instead. A typical CI key is `${{ github.workflow }}-${{ github.ref }}`, so new pushes to a pull request cancel the stale build. For deployments you usually want queueing without cancelling, so two deploys never overlap and none is lost halfway.

## Key terms

- **Workflow run** - one execution of a workflow, created when an event matches its `on:` section.
- **Runner** - the machine that executes a job; GitHub-hosted runners are fresh virtual machines for every job.
- **Activity type** - the sub-event that narrows a trigger, such as `opened` or `synchronize` for `pull_request`.
- **workflow_dispatch** - the manual trigger, with up to 25 typed inputs.
- **repository_dispatch** - an external trigger sent through the REST API with a custom event type and payload.
- **workflow_call** - the trigger that makes a workflow reusable, with declared inputs, secrets and outputs.
- **Service container** - a Docker container started next to a job, such as a database for integration tests.
- **fail-fast** - matrix setting, true by default, that cancels the remaining matrix jobs when one fails.
- **max-parallel** - matrix setting that limits how many matrix jobs run at once.
- **YAML anchor** - a `&name` marker on a block that a `*name` alias reuses elsewhere in the same file.
- **GITHUB_OUTPUT** - environment file that sets step outputs.
- **GITHUB_ENV** - environment file that sets environment variables for later steps.
- **GITHUB_STEP_SUMMARY** - environment file whose Markdown appears on the run summary page.
- **Environment** - a named deployment target with its own secrets, variables and protection rules.
- **Concurrency group** - a key that stops two runs of the same group from running at the same time.
