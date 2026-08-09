---
last-updated: 2026-08-09
difficulty: intermediate
---

# GitHub Actions Certification - Practice Questions

15 questions for the GitHub Actions exam, weighted toward authoring and maintaining workflows (40%), authoring actions (25%), consuming workflows (20%), and enterprise management (15%).

> **Cert page:** [exams/github/actions/](../../exams/github/actions/)

---

### Question 1
**Scenario:** A workflow must run on pull requests to `main` and on a nightly schedule.

A. `on: push`
B. `on: { pull_request: { branches: [main] }, schedule: [{ cron: '0 3 * * *' }] }`
C. `on: workflow_dispatch` only
D. Two separate repositories

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The `on` key accepts multiple event types with their own filters. Scheduled workflows run on the default branch only and use UTC cron, which is the detail that catches people out when a nightly job fires at the wrong local hour.
</details>

---

### Question 2
**Scenario:** A job must run only after another job succeeds.

A. Order them in the file
B. `needs: <job-id>` on the dependent job
C. `if: success()` alone
D. Separate workflows

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Jobs run in parallel by default; `needs` creates the dependency and also makes the upstream job's outputs available. File order has no effect. `if: always()` combined with `needs` is how you build a cleanup job that runs regardless of outcome.
</details>

---

### Question 3
**Scenario:** A matrix must test across three Node versions and two operating systems.

A. Six separate jobs written by hand
B. `strategy: { matrix: { node: [18, 20, 22], os: [ubuntu-latest, windows-latest] } }`
C. A loop in a script
D. Three workflows

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The matrix expands to the cross product automatically, with `include` and `exclude` for exceptions. `fail-fast: false` is worth knowing: by default one failing combination cancels the rest, which hides whether the failure is specific to one platform.
</details>

---

### Question 4
**Scenario:** A workflow needs to publish a package to a registry using short-lived credentials.

A. A long-lived personal access token in a secret
B. OIDC with a cloud provider or registry trust relationship, requesting a token at run time
C. A password in the YAML
D. A shared account

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OIDC lets the workflow exchange a signed identity token for short-lived credentials, so no long-lived secret exists to rotate or leak. The trust policy on the other side should be scoped to the specific repository, branch, or environment.
</details>

---

### Question 5
**Scenario:** A deployment job must wait for manual approval.

A. Add a `sleep`
B. Target an environment with required reviewers configured
C. Ask in chat
D. Use a schedule

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Environments carry protection rules (required reviewers, wait timers, branch restrictions) and their own secrets, so the approval gate and the credentials are bound together. That means production credentials are only reachable from an approved deployment.
</details>

---

### Question 6
**Scenario:** Common workflow logic must be shared across many repositories.

A. Copy the YAML into each repository
B. A reusable workflow called with `uses: org/repo/.github/workflows/build.yml@v1`, or a composite action
C. A shell script in each repo
D. Documentation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Reusable workflows are called as a job and can take inputs and secrets; composite actions bundle steps for use inside a job. Either way a fix happens in one place, which is the whole point when 50 repositories share a build.
</details>

---

### Question 7
**Scenario:** A third-party action is referenced as `@v3`.

A. This is fully immutable
B. Tags are mutable, so pin to a full commit SHA for third-party actions in sensitive workflows
C. SHAs are not supported
D. Only branches can be referenced

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A tag can be repointed by the action's owner, so `@v3` today may not be the same code tomorrow. Pinning to a commit SHA makes the dependency immutable, which is the supply-chain control that matters most for actions with access to your secrets.
</details>

---

### Question 8
**Scenario:** A workflow triggered by `pull_request_target` handles code from a fork.

A. It is safe by default
B. It runs with repository secrets and write access in the base repository context, so never check out and execute untrusted fork code in it
C. It has no permissions
D. It cannot access secrets

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** This is the highest-severity Actions misconfiguration: `pull_request_target` exists so maintainers can label or comment on fork PRs, but checking out the PR head and running its build hands secrets to an attacker. Use `pull_request` for building fork code.
</details>

---

### Question 9
**Scenario:** Dependencies should not be reinstalled on every run.

A. Nothing can be done
B. `actions/cache` with a key derived from the lock file hash, plus a restore-keys fallback
C. Commit `node_modules`
D. Use a self-hosted runner only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Keying the cache on the lock file hash means it invalidates exactly when dependencies change. Several setup actions have caching built in, which is simpler. Committing dependencies bloats the repository and creates review noise on every update.
</details>

---

### Question 10
**Scenario:** The default `GITHUB_TOKEN` permissions must follow least privilege.

A. Leave the defaults
B. Set `permissions:` explicitly at workflow or job level, granting only what each job needs
C. Use a personal access token instead
D. Disable the token

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Declaring `permissions: contents: read` and adding scopes only where required limits what a compromised step can do. A personal access token is worse: it carries a human's full access and does not expire with the run.
</details>

---

### Question 11
**Scenario:** A self-hosted runner is needed for a workflow that reaches internal systems.

A. Use it on public repositories freely
B. Use self-hosted runners for private repositories, or with strict controls, because fork pull requests could otherwise execute untrusted code on your infrastructure
C. There is no risk
D. Self-hosted runners cannot reach internal systems

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** GitHub explicitly warns against self-hosted runners on public repositories, because a fork PR can run arbitrary code on a machine inside your network that is not reset between jobs. Ephemeral runners and runner groups are the mitigations when the requirement is unavoidable.
</details>

---

### Question 12
**Scenario:** A custom action must be written in TypeScript.

A. Only container actions are supported
B. A JavaScript or TypeScript action with an `action.yml` declaring inputs, outputs, and the entry point
C. Bash only
D. A workflow file

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** JavaScript actions run directly on the runner and start fastest. Docker container actions offer any language but only run on Linux and pay image pull time. Composite actions wrap existing steps without new code at all.
</details>

---

### Question 13
**Scenario:** Output from one step must be used by a later step.

A. Global variables
B. Write to `$GITHUB_OUTPUT` and reference it as `${{ steps.<id>.outputs.<name> }}`
C. A temporary file only
D. It is not possible

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Step outputs need a step `id` and a write to the `$GITHUB_OUTPUT` file. `$GITHUB_ENV` sets environment variables for later steps, and job-level `outputs` pass values to a dependent job. The three serve different scopes.
</details>

---

### Question 14
**Scenario:** Actions usage must be governed across an enterprise.

A. Trust developers
B. Organization and enterprise policies restricting which actions may run (verified creators, an allowlist), plus required workflows and runner groups
C. Disable Actions
D. Review after the fact

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Allowlisting actions is the main supply-chain control at scale, since any action referenced in a workflow runs with access to that workflow's secrets. Runner groups control which repositories can reach which infrastructure.
</details>

---

### Question 15
**Scenario:** A long-running workflow should be cancelled when a newer commit arrives on the same branch.

A. Cancel manually
B. A `concurrency` group keyed on the ref with `cancel-in-progress: true`
C. Reduce the timeout
D. Fewer jobs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Concurrency groups prevent redundant runs and wasted minutes on superseded commits. For deployments the opposite setting is usually right: same group, `cancel-in-progress: false`, so deployments queue rather than interrupt each other.
</details>

---

## Where to go deeper

- [GitHub Actions cert page](../../exams/github/actions/) - notes, practice plan, strategy
- [GitHub Administration practice questions](./github-administration.md) - the enterprise exam
- [GHAS practice questions](./github-advanced-security.md) - security scanning in the pipeline
- [CI/CD explained](../../learn/concepts/cicd-explained.md) - pipelines in plain English
- **[📖 GitHub Certifications](https://resources.github.com/learn/certifications/)** - official exam pages
