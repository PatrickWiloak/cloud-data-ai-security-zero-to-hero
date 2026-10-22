---
last-updated: 2026-10-22
---

# HashiCorp Certified: Terraform Authoring and Operations Advanced - Exam Strategy

This exam mixes two kinds of work. Most of it is **labs**: real tasks in a live environment with a terminal, an editor, the cloud console and Terraform 1.6, each scored by inspecting what you leave behind. The rest is **multiple choice**, and objective 6 (HCP Terraform) is tested by multiple choice only. You have 4 hours with one 15-minute break. HashiCorp does not publish how many labs or questions there are, or how they are weighted, so plan your time by what is in front of you rather than by fixed numbers.

## Time Allocation

HashiCorp publishes **no objective weights**. The split below is **this guide's estimate** of where your preparation time pays off, not an official weighting.

| Objective | Suggested share of prep time (this guide's estimate) | Why |
|---|---|---|
| 1. Manage resource lifecycle | 20% | Every lab touches init, plan, apply and state; import and drift are fiddly |
| 2. Dynamic configuration | 25% | Most HCL you type; functions, for_each and validation take practice |
| 3. Collaborative workflows | 15% | Backends, version constraints and automation flags are precise details |
| 4. Modules | 15% | Refactoring into modules without replacements is a classic lab |
| 5. Providers | 10% | Aliases, sourcing and debugging; smaller surface area |
| 6. HCP Terraform (multiple choice) | 15% | Concepts, stages, settings and policy; no lab practice needed beyond familiarity |

On the day: when you start, look at what the exam presents and how many items there are, then set yourself checkpoints (for example a quarter of the items done per hour). Use the 15-minute break deliberately, not at a random moment mid-task.

## The Week Before

- Run the proctoring provider's system check well ahead, on the machine and network you will use.
- If you use a non-US keyboard layout, request it in advance; HashiCorp supports common non-US QWERTY layouts on request.
- Make sure your daily practice CLI is Terraform 1.6.x, not the newest release.
- Sleep. Typing speed and calm reading matter more than one more evening of review.

## Lab Tactics

For every lab task:

1. **Read the whole task twice** and write down the exact end state: names, counts, tags, which resources must not be replaced.
2. **Inspect before you change.** `terraform state list`, read the existing configuration, check the backend and versions block.
3. **Make the smallest change** that reaches the end state. Do not tidy unrelated code.
4. **Plan before you apply**, and read the summary line. Unexpected `-/+` or destroy counts mean stop and rethink.
5. **Verify the end state.** After apply, run `terraform plan` again. "No changes" is usually what a finished task looks like. Run `terraform fmt` and `terraform validate`.
6. **Use the docs.** You have the Terraform docs and limited provider docs. Look up import ID formats and argument names instead of guessing.

Labs are scored independently and can be done in any order. If one is stuck after a reasonable effort, move on and come back; a later lab does not depend on it.

### Per-objective tactics

**Objective 1 - lifecycle.** Know which init option a scenario calls for (`-migrate-state` keeps state, `-reconfigure` does not, `-upgrade` moves providers). Prefer `import` blocks and `moved` blocks to CLI state surgery, unless the task asks for the CLI. Remember `removed` blocks do not exist in 1.6; use `terraform state rm`. For drift, decide explicitly between reverting (normal apply), accepting (change config) and ignoring (`ignore_changes`).

**Objective 2 - dynamic configuration.** Build expressions in `terraform console` before putting them in files. When `for_each` complains about unknown values, key on input variables. Cross-variable rules in 1.6 go in a `precondition`, not a validation block. If a task says the run must fail on a condition, a `check` block is wrong (it only warns).

**Objective 3 - collaborative workflows.** For an S3 backend in 1.6, locking means `dynamodb_table`. Backend settings that vary per environment come from `-backend-config`. In automation, combine `-input=false` with a saved plan. For sharing outputs, root-level `output` blocks are required in the producer.

**Objective 4 - modules.** When refactoring into a module, put `moved` blocks in the calling configuration, run `terraform init`, and iterate until plan shows zero add, change and destroy. Reusable modules get `required_providers`, not `provider` blocks. Registry sources take `version`; Git sources take `?ref=`.

**Objective 5 - providers.** For a second region or account, add an aliased provider and pass it to modules through `providers`. If a provider will not install, check `source` and constraints with `terraform providers`. If it fails at runtime, turn on `TF_LOG_PROVIDER=DEBUG` and read the API error.

**Objective 6 - HCP Terraform (multiple choice).** Questions are about which feature or setting meets a requirement. Know the run stage order (OPA before cost estimation, Sentinel after), variable precedence, the project and workspace roles, the dynamic credentials variables, and the enforcement levels. Eliminate answers that put the right feature at the wrong scope.

## Multiple-Choice Tactics

- Read every option before choosing. Many distractors are real Terraform features used in the wrong place.
- Watch version wording. If an option relies on a feature newer than 1.6 (removed blocks, ephemeral values, `use_lockfile`), it is unlikely to be the intended answer.
- Flag anything you are unsure of and return at the end.

## Frequent Pitfalls

1. **Using a newer Terraform habit.** Syntax that works on your laptop's latest version may fail in the 1.6 environment.
2. **Leaving pending changes.** A lab whose final plan still shows changes is probably not finished.
3. **Destroying during a refactor or import.** Always check the plan summary before apply.
4. **`-reconfigure` when you meant `-migrate-state`.** You lose the link to existing state.
5. **Credentials in `.tf` files.** Use environment variables or the provided identity.
6. **Names that almost match.** If the task says `prod-vpc`, `prod_vpc` is wrong.
7. **Unformatted code.** Run `terraform fmt` before moving on.

## After the Exam

HashiCorp emails results; the credential is valid for 2 years and includes a free retake if you need one. Renewal means passing the current version of the exam, in either the AWS or the Azure version.
