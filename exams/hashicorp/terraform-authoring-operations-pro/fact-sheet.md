---
last-updated: 2026-10-22
---

# HashiCorp Certified: Terraform Authoring and Operations Advanced - Fact Sheet

This exam was previously listed by HashiCorp as "Terraform Authoring and Operations Professional"; the old objectives URL now redirects to the Advanced page. "Terraform Infrastructure Engineer Professional" is a different, multiple-choice exam that this guide does not cover.

## Exam Logistics

| Attribute | Value |
|-----------|-------|
| Exam name | HashiCorp Certified: Terraform Authoring and Operations Advanced |
| Level | Advanced (professional tier) |
| Format | Lab-based scenarios plus multiple choice; objective 6 (HCP Terraform) is multiple choice only |
| Delivery | Online proctored |
| Duration | 4 hours, with one 15-minute break |
| Questions | Not published (no published count of labs or questions) |
| Passing score | Not published; HashiCorp publishes no numeric cut score |
| Cost | $295 USD plus taxes, free retake included |
| Terraform version | 1.6 |
| Cloud version | AWS or Azure; both earn the same credential, and renewal can use either |
| Language | English (common non-US QWERTY keyboard layouts available on request) |
| Validity | 2 years |
| Prerequisites | None required; Terraform Associate (or equivalent) strongly recommended |

### What the exam environment gives you

- Terraform documentation, a limited part of the Terraform Registry, limited cloud provider documentation, and the cloud console. No search engines.
- Labs can be done in any order and are scored independently. Grading checks configuration syntax, state files and the settings of provisioned resources, so the end state is what counts, not the commands you used.
- Multiple-choice items can be flagged for review.

## Exam Objectives

HashiCorp publishes six objectives and **no weights**. The study-time split below is **this guide's estimate, not HashiCorp's**. It leans towards the lab-heavy objectives because those take longest to build skill in.

| # | Objective | Official weight | Suggested study time (this guide's estimate) | Note |
|---|---|---|---|---|
| 1 | Manage resource lifecycle | Not published | 20% | [notes/01](./notes/01-manage-resource-lifecycle.md) |
| 2 | Develop and troubleshoot dynamic configuration | Not published | 25% | [notes/02](./notes/02-dynamic-configuration.md) |
| 3 | Develop collaborative Terraform workflows | Not published | 15% | [notes/03](./notes/03-collaborative-workflows.md) |
| 4 | Create, maintain, and use Terraform modules | Not published | 15% | [notes/04](./notes/04-modules.md) |
| 5 | Configure and use Terraform providers | Not published | 10% | [notes/05](./notes/05-providers.md) |
| 6 | Collaborate on infrastructure as code using HCP Terraform (multiple choice only) | Not published | 15% | [notes/06](./notes/06-hcp-terraform.md) |

### Objective 1: Manage resource lifecycle

- 1a Initialize a configuration using `terraform init` and its options
- 1b Generate an execution plan using `terraform plan` and its options
- 1c Apply configuration changes using `terraform apply` and its options
- 1d Destroy resources using `terraform destroy` and its options
- 1e Manage resource state, including importing resources and reconciling resource drift

High-yield facts:

- `-migrate-state` copies state to a new backend; `-reconfigure` ignores the old backend and copies nothing; `-upgrade` moves providers within constraints and rewrites the lock file; `-backend-config` supplies partial backend settings (backend blocks cannot use variables).
- Plan modes are normal, `-destroy` and `-refresh-only`. `-replace` supersedes `taint`. `-target` is for exceptions only. `-out` saves a plan; `apply tfplan` takes no planning options and fails if state changed since the plan.
- `terraform destroy` equals `terraform apply -destroy`. `prevent_destroy` makes destroy plans fail. Removing a resource block destroys the resource on the next apply.
- `terraform state rm` forgets without destroying. `moved` blocks (1.1+) and `terraform state mv` change addresses. Import blocks (1.5+) and `terraform plan -generate-config-out` (1.5+) import declaratively.
- **Newer than the tested version:** `removed` blocks and `for_each` in import blocks (1.7).
- Drift: `plan -refresh-only` to see it, then revert with a normal apply, accept by changing config, or `ignore_changes`.

### Objective 2: Develop and troubleshoot dynamic configuration

- 2a Use language features to validate configuration
- 2b Query providers using data sources
- 2c Compute and interpolate data using HCL functions
- 2d Use meta-arguments in configuration
- 2e Configure input variables and outputs, including complex types
- 2f Analyze best practices for managing sensitive data, such as using Vault for secrets management

High-yield facts:

- Variable `validation` fails before planning; `precondition`/`postcondition` (1.2+) fail the run; `check` blocks (1.5+) only warn.
- In 1.6 a validation condition may reference only its own variable (cross-variable references are 1.9, newer than the tested version).
- `terraform test` is generally available in 1.6 (`.tftest.hcl`, `run`, `assert`, `expect_failures`); mock providers are 1.7, newer.
- Data sources read at plan time unless they depend on unknown values, then at apply.
- `for_each` keys must be known at plan time. `count` addresses by index, `for_each` by key.
- `optional(type, default)` in object types (1.3+); `nullable = false`; `sensitive = true` redacts output but the value is still in state.
- Vault data sources still write the secret to state; dynamic short-lived secrets reduce the impact. Ephemeral resources (1.10) and write-only arguments (1.11) are newer than the tested version.

### Objective 3: Develop collaborative Terraform workflows

- 3a Manage the Terraform binary, providers, and modules using version constraints
- 3b Configure remote state
- 3c Use the Terraform workflow in automation
- 3d Share data across configurations and workspaces

High-yield facts:

- `~> 5.30` means `>= 5.30, < 6.0`; `~> 5.30.0` means `>= 5.30.0, < 5.31.0`.
- `.terraform.lock.hcl` pins providers only, not modules. Commit it. `terraform providers lock -platform=...` adds hashes for other platforms.
- S3 backend in 1.6 locks with `dynamodb_table` (partition key `LockID`); `use_lockfile` is 1.10+, newer. azurerm locks natively with a blob lease. The `cloud` block connects to HCP Terraform.
- Automation: `TF_IN_AUTOMATION=1`, `-input=false` (or `TF_INPUT=0`), `plan -out` then `apply tfplan`, `-detailed-exitcode`.
- `terraform_remote_state` exposes root outputs but needs read access to the whole state; HashiCorp recommends `tfe_outputs` for HCP Terraform.

### Objective 4: Create, maintain, and use Terraform modules

- 4a Create a module
- 4b Use a module in configuration
- 4c Refactor a module and use module versioning
- 4d Refactor an existing configuration into modules

High-yield facts:

- Reusable modules declare `required_providers` but no `provider` blocks.
- `version` works only with registry sources; Git uses `?ref=`; `//` selects a subdirectory.
- Module blocks accept `count`, `for_each`, `depends_on`, `providers`.
- Registry repos are named `terraform-<PROVIDER>-<NAME>` with semver tags.
- `moved` blocks inside a module carry the refactor to every consumer; keep them until the next major version.
- Refactor into a module: `moved { from = aws_vpc.main  to = module.network.aws_vpc.this }`, then plan shows 0 add, 0 change, 0 destroy.

### Objective 5: Configure and use Terraform providers

- 5a Understand Terraform's plugin-based architecture
- 5b Configure providers, including aliasing, versioning, sourcing, and managing upgrades
- 5c Manage provider authentication
- 5d Troubleshoot provider errors

High-yield facts:

- Core talks to provider processes over gRPC; providers call the APIs. Registry tiers: official, partner, community.
- Source address `[hostname/]namespace/type`; omitting `source` means `hashicorp/<name>`.
- Aliased providers are passed to modules explicitly (`providers = { aws.replica = aws.dr }`) and declared with `configuration_aliases`.
- Upgrade with `terraform init -upgrade`, read the upgrade guide, plan for no changes, commit the lock file.
- Credentials from environment variables, profiles, roles or OIDC, never in `.tf` files.
- `TF_LOG` (TRACE, DEBUG, INFO, WARN, ERROR, JSON), `TF_LOG_PATH`, `TF_LOG_CORE`, `TF_LOG_PROVIDER`.

### Objective 6: Collaborate on infrastructure as code using HCP Terraform (multiple choice only)

- 6a Analyze the HCP Terraform run workflow
- 6b Understand HCP Terraform workspaces and their configuration options, including access management
- 6c Manage provider credentials in HCP Terraform
- 6d Analyze policy as code and governance features

High-yield facts:

- Run stages: pending, fetching, pre-plan tasks, plan, post-plan tasks, OPA policy check, cost estimation, Sentinel policy check, confirm, pre-apply tasks, apply, post-apply tasks.
- Workflows: VCS-driven (speculative plans on pull requests), CLI-driven, API-driven. Execution modes: remote, local, agent.
- Variable precedence: priority variable sets beat everything; then CLI values; then workspace variables; then variable sets (narrower scope wins); then `*.auto.tfvars` and `terraform.tfvars`.
- Project roles: Read, Write, Maintain, Admin (or Custom). Workspace roles: Read, Plan, Write, Admin (or Custom).
- Dynamic credentials for AWS: `TFC_AWS_PROVIDER_AUTH=true` plus `TFC_AWS_RUN_ROLE_ARN`; trust policy on the `sub` claim `organization:ORG:project:PROJECT:workspace:WS:run_phase:PHASE`; audience `aws.workload.identity`.
- Sentinel: advisory, soft-mandatory, hard-mandatory. OPA: advisory, mandatory. Overrides need Manage policy overrides.

## Key CLI Commands

```text
terraform init [-upgrade] [-reconfigure] [-migrate-state] [-backend-config=FILE|k=v] [-input=false] [-lockfile=readonly]
terraform plan [-out=tfplan] [-refresh-only] [-destroy] [-replace=ADDR] [-target=ADDR] [-var-file=F] [-detailed-exitcode]
terraform plan -generate-config-out=generated.tf     # with import blocks
terraform apply [tfplan] [-auto-approve] [-replace=ADDR] [-refresh-only] [-parallelism=N]
terraform destroy [-target=ADDR] [-auto-approve]
terraform import ADDR ID
terraform state list | show | mv | rm | pull | push | replace-provider
terraform force-unlock LOCK_ID
terraform output [-raw NAME] [-json]
terraform console | graph | validate | fmt -recursive | test
terraform providers | providers lock -platform=... | providers mirror DIR | version
terraform login | workspace list|new|select
```

## Language Features by Version (know which are in 1.6)

| Feature | Version | In scope for 1.6? |
|---|---|---|
| `moved` blocks | 1.1 | Yes |
| Preconditions and postconditions, `replace_triggered_by` | 1.2 | Yes |
| `optional()` with defaults in object types | 1.3 | Yes |
| `terraform_data` | 1.4 | Yes |
| `import` blocks, `check` blocks, `-generate-config-out` | 1.5 | Yes |
| `terraform test` (GA), S3 backend `assume_role` block | 1.6 | Yes |
| `removed` blocks, import `for_each`, test mocks | 1.7 | No, newer than the tested version |
| Provider-defined functions, cross-type `moved` | 1.8 | No, newer |
| Cross-variable validation, `templatestring` | 1.9 | No, newer |
| Ephemeral resources and values, S3 `use_lockfile` | 1.10 | No, newer |
| Write-only arguments | 1.11 | No, newer |

## Policy Enforcement Levels

| Engine | Level | Behavior |
|-------|-------|----------|
| Sentinel | advisory | Logs failure, run proceeds |
| Sentinel | soft-mandatory | Run stops; a user with Manage policy overrides can override |
| Sentinel | hard-mandatory | Run stops; no override by default; fix the code |
| OPA | advisory | Logs failure, run proceeds |
| OPA | mandatory | Run stops; overridable with Manage policy overrides |

## HCP Terraform Workspace Execution Modes

| Mode | Description | When to use |
|------|-------------|-------------|
| Remote | Plans and applies run on HCP Terraform workers | Default; full run history and governance |
| Local | State stored in HCP Terraform, execution on your machine or runner | Existing pipelines that only need remote state |
| Agent | Runs execute on self-hosted agents in your network | Private resources; credentials from the agent's own identity |

## Readiness Check

You are ready to book when you can, on Terraform 1.6 and without notes:

- Migrate state from local to a remote backend and prove "No changes".
- Import an existing resource with an import block and generated config, and tidy the result.
- Refactor a flat configuration into a module with `moved` blocks and zero replacements.
- Write a variable with a `map(object)` type, `optional()` attributes and validation.
- Configure an aliased provider and pass it into a module.
- Diagnose a provider error with `TF_LOG` and fix the cause.
- Explain the HCP Terraform run stages, variable precedence, team roles, dynamic credentials and policy enforcement levels.
