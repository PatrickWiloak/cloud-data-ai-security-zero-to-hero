---
last-updated: 2026-10-22
---

# HashiCorp Certified: Terraform Authoring and Operations Advanced - Practice Plan

An 8-week plan at 8 to 12 hours a week, mostly hands-on. Weeks 1 to 6 each map onto one exam objective; weeks 7 and 8 are mixed labs and review. Compress to 6 weeks if you already do this work daily. HashiCorp publishes no objective weights, so the time per week is this guide's estimate.

## Before Week 1

- Install **Terraform 1.6.x** (with `tfenv` or `asdf` so you can pin it) and use it for every lab. Newer versions accept syntax the exam will not.
- A sandbox in the cloud you will sit the exam for: **AWS or Azure**, with a budget alert.
- A free HCP Terraform organization and `terraform login`.
- Git, `jq`, and an editor.

## Week 1: Objective 1 - Manage resource lifecycle

**Read:** [notes/01-manage-resource-lifecycle.md](./notes/01-manage-resource-lifecycle.md)

**Labs**
- Build a small configuration (network plus one VM) on local state. Then add a remote backend and run `terraform init -migrate-state`; confirm "No changes".
- Use partial backend configuration with `-backend-config=dev.tfbackend` and `prod.tfbackend`.
- Practice `plan -out`, `show -json`, `apply tfplan`; then `plan -replace`, `plan -target`, `plan -destroy -out`.
- Create a resource in the console and import it twice: once with `terraform import`, once with an import block and `-generate-config-out`. Tidy the generated file until plan shows only the import.
- Change a tag in the console, then run `plan -refresh-only`, `apply -refresh-only`, and decide revert or accept.
- Rename a resource with a `moved` block, and forget one with `terraform state rm`.

**Checkpoint:** you can state from memory what `-upgrade`, `-reconfigure` and `-migrate-state` each do, and every lab ends with a clean plan.

## Week 2: Objective 2 - Dynamic configuration

**Read:** [notes/02-dynamic-configuration.md](./notes/02-dynamic-configuration.md)

**Labs**
- Write a `map(object)` variable with `optional()` attributes and two validation blocks.
- Create subnets with `for_each` from that map, and security group rules with a `dynamic` block.
- Flatten a nested input (networks containing subnets) into a `for_each` map.
- Add a postcondition to an AMI or image data source, a precondition that compares two inputs, and a `check` block. Make each one fail on purpose and note error versus warning.
- Write a `terraform test` file with a plan-only run, an assertion, and an `expect_failures` run for a bad input.
- Mark a password variable sensitive, apply, then find the value in state with `terraform show -json`.

**Checkpoint:** you can explain when to use validation, precondition, postcondition and check, and why `sensitive` does not protect state.

## Week 3: Objective 3 - Collaborative workflows

**Read:** [notes/03-collaborative-workflows.md](./notes/03-collaborative-workflows.md)

**Labs**
- Set up an S3 backend with a DynamoDB lock table (AWS) or an azurerm backend (Azure). Hold a lock in one terminal and watch the second run fail; use `-lock-timeout`.
- Experiment with version constraints: set two conflicting provider constraints across modules and read the error; fix it. Upgrade a provider with `init -upgrade` and inspect the lock file diff.
- Run `terraform providers lock -platform=linux_amd64 -platform=darwin_arm64`.
- Write a small pipeline (GitHub Actions or a shell script) with `TF_IN_AUTOMATION`, `-input=false`, `plan -out`, `-detailed-exitcode` and `apply tfplan`.
- Split network and app into two configurations. Share VPC and subnet IDs with `terraform_remote_state`, then with a `cloud` block and `tfe_outputs`.

**Checkpoint:** you can explain why `tfe_outputs` is preferred over `terraform_remote_state` in HCP Terraform.

## Week 4: Objective 4 - Modules

**Read:** [notes/04-modules.md](./notes/04-modules.md)

**Labs**
- Turn the week 2 network code into a module with typed inputs, outputs, a README and an example.
- Call it from a local path, from a Git tag with `?ref=`, and (if you can) from the HCP Terraform private registry with `version`.
- Call the module with `for_each` for two environments.
- Refactor a flat configuration into the module with `moved` blocks until plan shows 0 add, 0 change, 0 destroy.
- Rename a resource inside the module, add a `moved` block in the module, tag a new version, and upgrade a consumer.

**Checkpoint:** you can refactor into a module without a single replacement.

## Week 5: Objective 5 - Providers

**Read:** [notes/05-providers.md](./notes/05-providers.md)

**Labs**
- Add a second aliased provider (another region, or another subscription) and create a resource with it.
- Write a module that needs two configurations of the same provider (`configuration_aliases`) and pass them in from the root.
- Authenticate with environment variables, then with a role or managed identity; never with keys in HCL.
- Break things on purpose: wrong `source`, impossible constraint, missing credentials, missing permission. Read each error, then use `TF_LOG_PROVIDER=DEBUG` and `TF_LOG_PATH` to find the API call.
- Run `terraform providers`, `terraform version` and `terraform providers mirror`.

**Checkpoint:** given any provider error, you can say whether it is installation, configuration, authentication, authorization, or a provider bug.

## Week 6: Objective 6 - HCP Terraform

**Read:** [notes/06-hcp-terraform.md](./notes/06-hcp-terraform.md)

**Activities** (this objective is multiple choice, so aim for understanding)
- Create a VCS-driven workspace, open a pull request and watch the speculative plan; merge and follow the run through its stages.
- Create a project, a team with Write on it, and a variable set scoped to the project. Test variable precedence with a workspace variable of the same name.
- Configure dynamic provider credentials for your cloud and remove static keys.
- Read a Sentinel policy and an OPA policy, and work out what each would block. If your organization's plan includes policies, attach an advisory policy set.
- Set up a run trigger between the network and app workspaces.

**Checkpoint:** you can list the run stages in order and name the project and workspace roles.

## Week 7: Mixed labs

- Work every scenario in [scenarios.md](./scenarios.md) by hand before reading the answer.
- Redo any week 1 to 5 lab that felt slow, without notes.
- Practice finding things fast in the Terraform docs: import ID formats, function signatures, backend arguments.

## Week 8: Mock exam and review

- Build a 4-hour mock with one break: pick six to eight labs from the weeks above (for example migrate state, import with generated config, refactor into a module, add an aliased provider, fix a broken `for_each`, set up a backend with locking) plus a page of HCP Terraform questions you write yourself from note 06.
- Review [fact-sheet.md](./fact-sheet.md) and [strategy.md](./strategy.md) two days before.
- Day before: rest, light review of CLI options, no new material.

## Lab Environment Checklist

- [ ] `terraform version` shows 1.6.x
- [ ] Sandbox credentials for AWS or Azure available without keys in code
- [ ] `terraform login` done against HCP Terraform
- [ ] A Git repository for VCS-driven workspaces and module tags
- [ ] `jq` installed for reading `show -json` output
- [ ] Budget alert on the sandbox
