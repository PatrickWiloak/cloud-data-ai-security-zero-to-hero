---
last-updated: 2026-10-22
applies-to: GH-200 skills measured as of January 2026, checked 2026-10-22
---

# GitHub Actions (GH-200) Fact Sheet

## Exam Overview

**Exam Code:** GH-200
**Exam Name:** GitHub Actions
**Level:** Intermediate
**Duration:** 100 minutes
**Format:** Multiple choice, proctored; may include interactive components
**Passing Score:** 700 (scaled 1-1000)
**Cost:** Set by country; commonly listed as $99 USD in the US
**Valid For:** 2 years
**Delivery:** Pearson VUE, scheduled through Microsoft Learn
**Prerequisites:** None (GitHub Foundations recommended)

**[📖 GitHub Actions certification](https://learn.microsoft.com/en-us/credentials/certifications/github-actions/)** - registration and exam details
**[📖 Exam GH-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200)** - skills measured as of January 2026
**[📖 Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)** - YAML reference

## Exam Domains (January 2026)

| Domain | Weight | Notes |
|---|---|---|
| Author and manage workflows | 20-25% | [01](notes/01-workflow-authoring.md), [02](notes/02-expressions-contexts.md) |
| Consume and troubleshoot workflows | 15-20% | [03](notes/03-consume-and-troubleshoot.md) |
| Author and maintain actions | 15-20% | [04](notes/04-custom-actions.md) |
| Manage GitHub Actions for the enterprise | 20-25% | [05](notes/05-enterprise-management.md) |
| Secure and optimize automation | 10-15% | [06](notes/06-secure-and-optimize.md) |

## Domain 1: Author and Manage Workflows (20-25%)

### Triggers

| Trigger | Fires when | Remember |
|---|---|---|
| `push` | Commits or tags pushed | `branches`, `tags`, `paths` filters; all present filters must match |
| `pull_request` | PR activity (default: opened, synchronize, reopened) | Fork PRs: read-only token, no secrets |
| `pull_request_target` | Same, but base-branch workflow | Has secrets and write token; never run PR code in it |
| `schedule` | Cron, UTC | Default branch only; may be delayed |
| `workflow_dispatch` | Manual or API | Up to 25 inputs: string, boolean, choice, number, environment |
| `workflow_call` | Called by another workflow | Declares inputs, secrets, outputs |
| `repository_dispatch` | REST call with `event_type` | Payload in `github.event.client_payload` |
| `workflow_run` | Another workflow completed | Privileged follow-up after untrusted builds |

### Structure essentials

- Jobs run in parallel; `needs` orders them and skips dependants on failure unless `if: always()`.
- Steps run in order on one runner and share the file system; jobs share nothing unless passed.
- An `if:` without a status function gets an implicit `success()`.
- `timeout-minutes` default is 360 per job.
- **Service containers** (`services:`): on the runner use `localhost` plus mapped `ports`; in a job container use the service label as host name. Linux runners only. Health checks go in `options:`.
- **Matrix**: max 256 jobs per run; `exclude` then `include`; `fail-fast` defaults to `true`; `max-parallel` caps concurrency.
- **YAML anchors** (`&name`, `*name`): same file only, defined before use, no parameters. Merge keys (`<<`) are listed in the study guide but GitHub parses YAML 1.2.
- **Runner images**: `-latest` labels move to new images (Ubuntu 20.04 retired 2025; `windows-latest` moving to Windows Server 2025).

### Expressions and contexts

| Context | Holds |
|---|---|
| `github` | Event, ref, sha, actor, repository, run IDs, `event` payload |
| `env` / `vars` / `secrets` | Variables, configuration variables, secrets |
| `inputs` | Typed dispatch or call inputs (prefer over `github.event.inputs`) |
| `matrix` / `strategy` | Current combination; `job-index`, `job-total` |
| `needs` | `outputs` and `result` of needed jobs |
| `steps` | `outputs`, `outcome` (before `continue-on-error`), `conclusion` (after) |
| `job` / `runner` | Job status, services; runner OS, arch, temp, tool cache |

- Evaluated at run creation (job `if`, `runs-on`, `strategy`, `environment`): no `steps`, `runner` or `secrets`.
- Evaluated on the runner (step `if`, `with`, `run`, step `env`): full runtime contexts.
- Status functions: `success()`, `failure()`, `cancelled()`, `always()`; prefer `!cancelled()` for cleanup.
- Functions: `contains`, `startsWith`, `endsWith`, `format`, `join`, `toJSON`, `fromJSON`, `hashFiles`.
- Secrets cannot be used directly in `if:`; copy into `env` first.

### Execution and outputs

| Need | Use |
|---|---|
| Speed up future runs | `actions/cache` or `setup-*` `cache:` input, key on lock-file hash |
| Pass files to a later job or keep reports | `upload-artifact` / `download-artifact` |
| Pass a value between steps | `echo "k=v" >> "$GITHUB_OUTPUT"`, read `steps.<id>.outputs.k` |
| Pass a value between jobs | Map to `jobs.<id>.outputs`, read `needs.<id>.outputs.k` |
| Set an env var for later steps | `echo "K=v" >> "$GITHUB_ENV"` |
| Rich run report | Markdown to `$GITHUB_STEP_SUMMARY` |
| Human approval before deploy | `environment:` with required reviewers |

- Retention: default 90 days (up to 400 for private repos); `retention-days` per upload; org/repo defaults via settings or REST.
- Badge: `https://github.com/OWNER/REPO/actions/workflows/FILE.yml/badge.svg?branch=main`.
- `concurrency` group plus `cancel-in-progress` for superseded CI runs.

## Domain 2: Consume and Troubleshoot Workflows (15-20%)

- Find the first failing step; read annotations; check "Set up job" for image version, token permissions and resolved action SHAs.
- Debug: `ACTIONS_STEP_DEBUG=true` (step) and `ACTIONS_RUNNER_DEBUG=true` (runner), or re-run with debug logging.
- Re-run all, failed, or one job; re-runs reuse the original commit and workflow file and bump `run_attempt`.
- Pushes made with `GITHUB_TOKEN` do not trigger new workflow runs (except dispatch events).
- CLI: `gh run list`, `gh run view --log-failed`, `gh run download -n NAME`, `gh run rerun --failed`, `gh workflow disable`.

| | Workflow template | Reusable workflow | Composite action |
|---|---|---|---|
| Used by | Copying | `jobs.<id>.uses` | `steps[*].uses` |
| Updates flow to users | No | Yes | Yes |
| Own runner | Yes | Yes | No (caller's) |
| Limit | n/a | 10 nesting levels, 50 unique per file | n/a |

- Org templates: `.github` repo, `workflow-templates/*.yml` plus `.properties.json`. Internal `.github`: internal and private repos may use them; private `.github`: private repos only.
- Disable keeps file and history; delete removes the file (history stays until deleted).

## Domain 3: Author and Maintain Actions (15-20%)

| Type | `runs.using` | Platforms | Notes |
|---|---|---|---|
| JavaScript | `node20` / `node24` | All | Fast; commit bundled `dist/`; toolkit `@actions/*` |
| Docker | `docker` | Linux only | Any language; slower start |
| Composite | `composite` | All | Steps only; `run` steps need `shell:` |

- `action.yml` needs `name`, `description`, `runs`; optional `inputs`, `outputs`, `branding`, `author`.
- Inputs arrive as strings and as `INPUT_<NAME>` env vars; composite outputs need `value:` mapping.
- `core.setOutput`, `core.exportVariable`, `core.addPath`, `core.setSecret`, `core.setFailed`, `core.summary`.
- Marketplace: public repo, single root `action.yml`, no workflow files, unique name; publish from a release.
- Versioning: `v1.2.3` tags plus a moving `v1` major tag; breaking change means a new major.
- Immutable actions: published releases cannot change; self-hosted runners must allow `pkg.actions.githubusercontent.com`.

## Domain 4: Manage GitHub Actions for the Enterprise (20-25%)

- Policy order: enterprise > organization > repository; higher levels can enforce.
- Allowed actions: all; enterprise only; enterprise plus GitHub-created and/or verified creators; explicit patterns (with `!` to block); optional SHA-pinning requirement.
- Private actions shared via the repository's Actions > Access setting (organization or enterprise).
- Runner groups: share runners with selected repos, orgs or workflows; each runner in one group; `runs-on: { group: name }`.
- Self-hosted labels: `self-hosted`, OS, arch, plus custom; a job needs a runner with all requested labels.
- Ephemeral runners (`--ephemeral`) and ARC for clean, autoscaled capacity; never run untrusted public-repo code on persistent self-hosted runners.
- IP allow lists block standard hosted runners; use self-hosted egress IPs or larger runners with static IPs.
- Hosted images list software in `actions/runner-images`; add tools with `setup-*`, package managers, containers or custom images.

| Secret scope | Shared with | Precedence |
|---|---|---|
| Environment | Jobs referencing it, after protection rules | Highest |
| Repository | All workflows in the repo | Middle |
| Organization | All, private, or selected repos | Lowest |

- Limits: 48 KB per secret, 100 per repo, 1,000 per org; names not case-sensitive, no `GITHUB_` prefix.
- REST: get the public key, encrypt with libsodium, `PUT` with `key_id`; or `gh secret set` / `gh variable set`.

## Domain 5: Secure and Optimize Automation (10-15%)

- **Script injection**: never `${{ github.event.* }}` inside `run:`; pass through `env:` and quote.
- **GITHUB_TOKEN**: per job, one repo, revoked at job end; set `permissions:` (unnamed scopes become `none`). Prefer it over PATs; use a GitHub App for cross-repo work.
- **OIDC**: `permissions: id-token: write`; cloud trust policy matches the `sub` claim (repo plus environment or branch); short-lived credentials, no stored cloud keys.
- **Pinning**: full 40-character commit SHA with a version comment; Dependabot keeps it current.
- **Attestations**: `actions/attest-build-provenance` with `id-token: write` and `attestations: write`; verify with `gh attestation verify`.
- **Environments**: required reviewers, wait timer, deployment branch rules, prevent self-review.
- **Optimize**: path filters, concurrency cancel, narrow PR matrices, caching, short retention for intermediate artifacts, `timeout-minutes`, cheapest suitable runner OS.

## Common Pitfalls

- `pull_request` vs `pull_request_target` security context.
- `github.event.inputs` booleans are strings; `inputs` keeps types.
- A cleanup step without `always()` or `!cancelled()` is skipped after a failure.
- Reusable workflow vs composite action vs workflow template.
- Docker actions do not run on Windows or macOS runners.
- Cached dependencies are not artifacts, and artifacts are not caches.
