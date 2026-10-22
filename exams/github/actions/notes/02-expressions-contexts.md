---
last-updated: 2026-10-22
applies-to: GH-200 skills measured as of January 2026, checked 2026-10-22
difficulty: intermediate
---

# Domain 1: Author and Manage Workflows (20-25%) - Part 2: Expressions and Contexts

The first domain asks you to "use predefined contexts ... to access workflow, repository, and runtime metadata" and to "evaluate expressions with `${{ }}` referencing contexts; distinguish static (workflow parse) vs runtime evaluation; prevent secret leakage in logs and expressions". This note covers exactly that. Triggers, structure, matrices and outputs are in [01-workflow-authoring.md](01-workflow-authoring.md).

**[📖 Evaluate expressions in workflows and actions](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions)** - operators, literals and functions.
**[📖 Contexts reference](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts)** - every context, its properties and where it is available.

## What an expression is

An expression is a small piece of logic inside `${{ }}`. GitHub evaluates it and substitutes the result into the YAML before that part of the workflow is used. Expressions can contain literals, context references, operators and a fixed set of functions. They are not shell: there are no loops, no variables of your own, and no access to the runner's file system except through `hashFiles()`.

In an `if:` key you may leave out the `${{ }}`, because `if:` is always treated as an expression. Everywhere else you need the braces. One trap follows from that: `if: ${{ false }} || true` is not one expression but text after an expression, and text is truthy. Keep the whole condition inside one pair of braces, or leave the braces out entirely.

### Literals and operators

- Strings use single quotes: `'main'`. Escape a quote by doubling it: `'it''s'`.
- Numbers, `true`, `false` and `null` are literals.
- Operators: `( )`, `[ ]` for index access, `.` for property access, `!`, `<`, `<=`, `>`, `>=`, `==`, `!=`, `&&`, `||`.
- There is no ternary operator, but `cond && 'a' || 'b'` behaves like one as long as `'a'` is truthy.

### Loose comparison rules

GitHub compares values loosely and converts types when they differ: `null` becomes `0` (or `''` in string contexts), booleans become `1` or `0`, and strings are parsed as numbers when compared with numbers. String comparison ignores case, so `github.ref_name == 'MAIN'` matches `main`. Objects and arrays are only equal to themselves. Most surprising results in `if:` come from a value that is a **string** `'false'` (truthy, because it is a non-empty string) rather than a boolean `false`. That is exactly what happens when you read a boolean input through `github.event.inputs` instead of `inputs`.

## Static versus runtime evaluation

The study guide singles this out because it explains which context you may use where.

Some keys are evaluated **when the run is created**, before any runner is assigned. `run-name`, the workflow-level `env`, `concurrency` at workflow level, job-level `runs-on`, `environment`, `strategy` and job `if:` fall in this group. At that point GitHub knows the event, the repository, `vars`, `inputs` and the results of earlier jobs (`needs`), but nothing that happens on a runner.

Other keys are evaluated **while the job runs**, step by step. Step `if:`, `with:`, `env:` on a step, `run:` text and `outputs` can see `steps`, `runner`, `job`, `env` values set by earlier steps through `GITHUB_ENV`, and `secrets`.

So `runs-on: ${{ runner.os }}` is impossible (the runner does not exist yet), while `runs-on: ${{ matrix.os }}` is fine (the matrix is expanded when jobs are created). Likewise you cannot read `steps.*` in a job-level `if:`, and you cannot reference `env` in the `with:` block that calls a reusable workflow. The contexts reference has a table of "context availability" per key: if an exam answer uses a context in a key that cannot see it, that answer is wrong.

A second meaning of "static" is the YAML layer. YAML anchors and aliases are expanded by the parser before any expression is evaluated, so an anchor can never depend on a context value.

## The contexts you need

| Context | What it holds | Typical use |
|---|---|---|
| `github` | Run and event metadata: `event_name`, `ref`, `ref_name`, `sha`, `actor`, `repository`, `run_id`, `run_number`, `run_attempt`, `workflow`, `base_ref`, `head_ref`, `event` | Branch and event conditions, naming, links |
| `github.event` | The full webhook payload of the triggering event | `github.event.pull_request.labels.*.name`, `github.event.inputs` |
| `env` | Variables from workflow, job and step `env` | Reusing a value in several steps |
| `vars` | Configuration variables at org, repo or environment level | Non-secret settings such as a region or URL |
| `secrets` | Secrets plus `GITHUB_TOKEN` | Passing credentials to steps and actions |
| `inputs` | Inputs of `workflow_dispatch` or `workflow_call`, with their real types | Manual and reusable workflow parameters |
| `matrix` | The current combination of a matrix job | `runs-on: ${{ matrix.os }}` |
| `strategy` | `fail-fast`, `job-index`, `job-total`, `max-parallel` | Sharding test suites across matrix jobs |
| `needs` | `outputs` and `result` of each job in `needs` | Passing data and reacting to upstream failure |
| `steps` | `outputs`, `outcome` and `conclusion` of earlier steps with an `id` | Branching on a step's result |
| `job` | `status`, `container`, `services` of the current job | Service container network ports |
| `runner` | `os`, `arch`, `name`, `temp`, `tool_cache`, `environment` | OS-specific paths and commands |

Two pairs are worth a second look:

- **`steps.<id>.outcome` versus `steps.<id>.conclusion`.** `outcome` is the raw result before `continue-on-error` is applied. `conclusion` is the result after it. A step that failed with `continue-on-error: true` has `outcome == 'failure'` and `conclusion == 'success'`.
- **`github.ref` versus `github.ref_name`.** `ref` is the full ref (`refs/heads/main`, `refs/tags/v1.2.0`, `refs/pull/42/merge`). `ref_name` is the short name (`main`, `v1.2.0`, `42/merge`).

Dot and index syntax are interchangeable: `github.event.pull_request.head.ref` and `github['event']['pull_request']['head']['ref']` are the same. The object filter `*` returns an array, so `github.event.pull_request.labels.*.name` gives the label names you can pass to `contains()`.

## Status functions and conditions

| Function | True when |
|---|---|
| `success()` | No earlier step or needed job failed or was cancelled. Implicit default. |
| `failure()` | An earlier step (or any ancestor job) failed. |
| `cancelled()` | The run was cancelled. |
| `always()` | Always, even on cancellation. |

Because `success()` is added when no status function is present, a step with `if: github.ref == 'refs/heads/main'` still skips after a failure. Write `if: always() && github.ref == 'refs/heads/main'` when you mean "on main, whatever happened". Prefer `!cancelled()` over `always()` for cleanup that should not run after a user cancels, so a cancelled run does not hang on a long cleanup step.

```yaml
- name: Upload test report even when tests fail
  if: ${{ !cancelled() }}
  uses: actions/upload-artifact@v4
  with:
    name: junit
    path: reports/

- name: Page on-call only for main
  if: failure() && github.ref == 'refs/heads/main'
  run: ./notify.sh
```

## Functions

| Function | Use |
|---|---|
| `contains(search, item)` | Substring or array membership, case-insensitive |
| `startsWith(s, v)` / `endsWith(s, v)` | Prefix and suffix tests, for example tag patterns |
| `format('{0}-{1}', a, b)` | Build a string from parts |
| `join(array, sep)` | Turn an array into one string |
| `toJSON(value)` | Pretty-print an object, handy for debugging a payload |
| `fromJSON(string)` | Parse JSON: turn `'true'` into a boolean, or build a dynamic matrix |
| `hashFiles(patterns)` | SHA-256 over matching files, used in cache keys |

`fromJSON` is how a dynamic matrix works: one job prints a JSON list to `$GITHUB_OUTPUT`, and the next job uses `matrix: ${{ fromJSON(needs.plan.outputs.targets) }}`.

```yaml
jobs:
  plan:
    runs-on: ubuntu-latest
    outputs:
      targets: ${{ steps.list.outputs.targets }}
    steps:
      - id: list
        run: echo 'targets=["api","web","worker"]' >> "$GITHUB_OUTPUT"
  build:
    needs: plan
    runs-on: ubuntu-latest
    strategy:
      matrix:
        target: ${{ fromJSON(needs.plan.outputs.targets) }}
    steps:
      - run: echo "Building ${{ matrix.target }}"
```

## Preventing secret leakage in logs and expressions

GitHub masks the value of every secret it knows about wherever it appears in logs, replacing it with `***`. Masking is a safety net, not a guarantee, and the exam tests where the net has holes:

- **Transformed secrets are not masked.** If a script base64-encodes, URL-encodes or splits a secret, the new string is unknown to the masker. Register derived values yourself with `echo "::add-mask::$value"` before printing anything.
- **Structured secrets mask badly.** A JSON blob stored as one secret is masked as a whole, but a single field extracted from it is not. Store each credential as its own secret.
- **Secrets cannot drive `if:` directly.** The `secrets` context is not available in `if:`. Copy the secret into a job-level `env` variable and test `env.MY_SECRET != ''` instead.
- **Outputs containing secrets are dropped.** A job output whose value contains a masked secret is not passed to downstream jobs.
- **Never interpolate untrusted text into `run:`.** `run: echo "${{ github.event.issue.title }}"` pastes the title into the script before the shell sees it, so a title containing `"; curl ... | sh; "` runs. Pass the value through an environment variable instead (`env: TITLE: ${{ github.event.issue.title }}` and `run: echo "$TITLE"`). This is **script injection**, covered further in [06-secure-and-optimize.md](06-secure-and-optimize.md).
- **Debug logging is verbose.** Setting the `ACTIONS_STEP_DEBUG` secret or variable to `true`, or re-running with debug logging, prints far more detail. Secrets stay masked, but transformed values may not.

## Environment files recap

| File | Effect |
|---|---|
| `$GITHUB_OUTPUT` | `name=value` becomes `steps.<id>.outputs.name` |
| `$GITHUB_ENV` | `NAME=value` becomes an environment variable from the next step on |
| `$GITHUB_PATH` | A directory line is prepended to `PATH` for later steps |
| `$GITHUB_STEP_SUMMARY` | Markdown rendered on the run summary page |

Use the `name<<DELIMITER` form for multi-line values, and pick a random delimiter when the content comes from outside, so the content cannot close the block early and inject extra variables.

## Key terms

- **Expression** - logic inside `${{ }}` that GitHub evaluates and substitutes into the workflow.
- **Context** - a named object, such as `github` or `steps`, that expressions read from.
- **Context availability** - the rule that each workflow key can only read certain contexts, depending on when it is evaluated.
- **outcome** - a step's result before `continue-on-error` is applied.
- **conclusion** - a step's result after `continue-on-error` is applied.
- **success()** - the implicit status check added to every `if:` that does not use a status function.
- **fromJSON** - function that parses a JSON string, used for typed values and dynamic matrices.
- **hashFiles** - function that hashes matching files, used to build cache keys.
- **add-mask** - workflow command that masks a value the runner would not otherwise know is secret.
- **Script injection** - running attacker-controlled text because an expression pasted it into a shell script.
