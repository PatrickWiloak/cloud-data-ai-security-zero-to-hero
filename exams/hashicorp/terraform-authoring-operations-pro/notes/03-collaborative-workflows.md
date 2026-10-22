---
last-updated: 2026-10-22
---

# Objective 3: Develop Collaborative Terraform Workflows

This note covers objective 3 of the HashiCorp Certified: Terraform Authoring and Operations Advanced exam. Once more than one person, or one pipeline, runs a configuration, four problems appear. Everyone must get the same Terraform, provider and module versions (3a). State must live somewhere shared, locked and safe (3b). Pipelines must run Terraform without a human at the keyboard (3c). And separate configurations must be able to read each other's results (3d).

The tested version is **Terraform 1.6**. Anything later is flagged as "newer than the tested version".

**[📖 Terraform Authoring and Operations Advanced objectives](https://developer.hashicorp.com/terraform/tutorials/pro-cert/adv-review)** - the official objective list this note follows

## 3a. Manage the Terraform binary, providers and modules using version constraints

There are three things you can constrain, in three different places:

```hcl
terraform {
  # 1. The Terraform CLI itself
  required_version = ">= 1.6.0, < 2.0.0"

  required_providers {
    # 2. Each provider
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.30"
    }
    random = {
      source  = "hashicorp/random"
      version = ">= 3.5.0"
    }
  }
}

# 3. Each registry module
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.1.0"
}
```

### The constraint syntax

| Operator | Meaning | Example |
|---|---|---|
| `=` (or bare version) | exactly this version | `= 1.6.6` |
| `!=` | anything except this version | `!= 5.31.0` (skip a buggy release) |
| `>`, `>=`, `<`, `<=` | comparisons | `>= 1.6.0, < 2.0.0` |
| `~>` | pessimistic: only the rightmost given part may increase | `~> 5.30` means `>= 5.30, < 6.0`; `~> 5.30.1` means `>= 5.30.1, < 5.31.0` |

Commas combine constraints with AND. The `~>` operator is the one the exam likes to test: count the parts. Two parts (`~> 5.30`) allow minor and patch upgrades; three parts (`~> 5.30.1`) allow only patch upgrades.

Prerelease versions (such as `1.7.0-beta1`) only match an exact `=` constraint.

### Who should constrain what

HashiCorp's guidance differs between reusable modules and root modules:

- **Reusable modules** should declare the **minimum** provider version they need (`>= 5.0`) and avoid upper bounds where possible. Every module in a configuration shares one copy of each provider, so tight constraints in two modules can make them impossible to use together. Terraform combines all constraints from all modules and must find one version that satisfies all of them; if it cannot, init fails with "no available releases match the given constraints".
- **Root modules** should constrain more tightly (`~>`) and rely on the lock file for the exact version.
- `required_version` in a module states which language features it needs. If the CLI is outside the range, every command fails with "Unsupported Terraform Core version".

### The dependency lock file

`terraform init` writes `.terraform.lock.hcl`. It records, **for providers only**, the exact version selected and the checksums of the packages.

```hcl
provider "registry.terraform.io/hashicorp/aws" {
  version     = "5.31.0"
  constraints = "~> 5.30"
  hashes = [
    "h1:...",
    "zh:...",
  ]
}
```

- Commit it to version control. Then every teammate and every pipeline gets the same provider build, even when a newer version matching the constraint is released.
- To move to a newer version within the constraint, run `terraform init -upgrade`, review the lock file change, and commit it.
- **Module versions are not recorded in the lock file.** A module is re-resolved from its `version` constraint on each fresh init, which is one reason to pin modules more tightly.
- The `h1:` hashes are platform-specific. If developers use macOS and CI uses Linux, run `terraform providers lock -platform=linux_amd64 -platform=darwin_arm64` so the file contains checksums for every platform; otherwise CI fails with a checksum mismatch. Provider troubleshooting is covered more in [note 05](./05-providers.md).
- In CI, `terraform init -lockfile=readonly` guarantees the pipeline uses exactly what was committed.

### Managing the binary

Teams usually standardize the CLI version with a version manager (`tfenv`, `asdf`) and a `.terraform-version` file, a pinned container image (`hashicorp/terraform:1.6.6`), or the workspace Terraform version setting in HCP Terraform. Upgrading Terraform itself is a deliberate change: read the upgrade guide, raise `required_version`, run a plan that should show no changes, and let state be written by the new version only once you are sure. A state file written by a newer Terraform may not be readable by an older one.

## 3b. Configure remote state

Local state (`terraform.tfstate` in the working directory) does not work for a team. Nobody else can see it, two people can run at once, and it sits unencrypted on a laptop. A remote backend fixes all three: shared storage, locking, and encryption at rest.

### S3 backend (AWS version of the exam)

```hcl
terraform {
  backend "s3" {
    bucket         = "acme-tfstate-prod"
    key            = "network/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    kms_key_id     = "alias/terraform-state"
    dynamodb_table = "terraform-locks"   # table with a string partition key named LockID
  }
}
```

- **Locking** on the S3 backend in Terraform 1.6 uses a DynamoDB table whose partition key is `LockID` (type String). Without `dynamodb_table` there is no locking at all, and two concurrent applies can corrupt state. **Native S3 locking with `use_lockfile = true` arrived in Terraform 1.10 (generally available in 1.11), newer than the tested version.**
- Enable **bucket versioning** so you can recover an earlier state version, and block public access on the bucket.
- Terraform 1.6 overhauled the S3 backend. Role assumption moved into a nested `assume_role { role_arn = "..." }` block, and the old top-level `role_arn` argument was deprecated. Credentials still come from the normal AWS chain (environment variables, shared config profile, instance role); do not put access keys in the backend block.
- With CLI workspaces, non-default workspaces are stored under `env:/<workspace>/<key>` (the prefix is set by `workspace_key_prefix`).

### azurerm backend (Azure version of the exam)

```hcl
terraform {
  backend "azurerm" {
    resource_group_name  = "rg-tfstate"
    storage_account_name = "acmetfstateprod"
    container_name       = "tfstate"
    key                  = "network.terraform.tfstate"
    use_azuread_auth     = true   # authenticate to storage with Entra ID, not an access key
  }
}
```

- **Locking is native**: the backend takes a lease on the state blob. There is no extra table to create.
- Storage accounts encrypt at rest by default. Enable blob versioning or soft delete for recovery.
- Authentication can use Azure CLI, a service principal, managed identity, or OIDC (`use_oidc = true`), as well as storage access keys or SAS tokens. Prefer Entra ID based auth over shared keys.

### HCP Terraform as the backend

```hcl
terraform {
  cloud {
    organization = "acme"
    workspaces {
      name = "network-prod"
      # or: tags = ["network"]  to work with several workspaces via terraform workspace select
    }
  }
}
```

The `cloud` block (Terraform 1.1 and later) replaces the older `backend "remote"`. State is stored, versioned, encrypted and locked by HCP Terraform; you authenticate with `terraform login` or a `TF_TOKEN_app_terraform_io` environment variable. `organization` and the workspace can also come from `TF_CLOUD_ORGANIZATION` and `TF_WORKSPACE`. Depending on the workspace's execution mode, plans run remotely or locally ([note 06](./06-hcp-terraform.md)).

### Locking in practice

Terraform takes the lock for any operation that could write state (plan, apply, destroy, import, state mv and so on) and releases it at the end. If a process dies holding it, the next run fails with "Error acquiring the state lock" and prints the lock ID, who holds it and when it was taken. Wait (`-lock-timeout=5m`) if it is a live run; use `terraform force-unlock LOCK_ID` only once you have confirmed the holder is dead. `-lock=false` disables locking for one command and is almost never the right answer.

### Migrating state between backends

Change the backend block, then run `terraform init -migrate-state` (take a `terraform state pull > backup.tfstate` first). Afterwards a plan must show no changes. The `-reconfigure` versus `-migrate-state` distinction is covered in [note 01](./01-manage-resource-lifecycle.md).

### CLI workspaces

`terraform workspace new|select|list|show|delete` gives one configuration several named states in the same backend, and `terraform.workspace` lets the configuration vary by name. They suit short-lived copies (feature branches, tests). They are a poor fit for dev, staging and prod: the environments share one backend and one set of credentials, and a wrong `select` hits production. Separate configurations or separate HCP Terraform workspaces give real isolation. CLI workspaces and HCP Terraform workspaces are different things; with a `cloud` block using `tags`, `terraform workspace select` switches between HCP workspaces.

## 3c. Use the Terraform workflow in automation

Running Terraform in a pipeline is the same init, plan, apply workflow with three changes: no prompts, a saved plan between steps, and output fit for logs.

```bash
export TF_IN_AUTOMATION=1      # trims "now run terraform apply" style hints from output
export TF_INPUT=0              # same as -input=false on every command

terraform init -input=false -lockfile=readonly
terraform fmt -check -recursive
terraform validate
terraform plan -input=false -out=tfplan -detailed-exitcode -lock-timeout=5m
# exit 0 = no changes, 2 = changes to review, 1 = error
terraform show -no-color tfplan > plan.txt     # attach for reviewers
# ... approval gate ...
terraform apply -input=false tfplan
```

What each piece is for:

- **`-input=false` / `TF_INPUT=0`** makes a missing variable an error instead of a prompt that would hang the job forever.
- **`TF_IN_AUTOMATION`** set to any non-empty value changes some output so it does not tell a pipeline to run commands it cannot run. It does not change behaviour otherwise.
- **`-out=tfplan` then `apply tfplan`** guarantees that what was reviewed is what gets applied. The plan file must be applied with the same configuration, the same `.terraform` contents (providers and modules) and the same Terraform version, so pipelines either run plan and apply in one job with a pause, or archive the whole working directory between jobs. Plan files contain sensitive values; store them as protected artifacts.
- **`-detailed-exitcode`** lets a pipeline skip the approval step when there is nothing to do.
- **`-no-color`** removes ANSI codes from log output.
- **`TF_CLI_ARGS`** and **`TF_CLI_ARGS_plan`** (and so on per command) append arguments to every invocation, handy for `-no-color` across a whole job.
- **`TF_PLUGIN_CACHE_DIR`** shares downloaded providers between runs to speed up init.
- **Credentials** come from the CI system: environment variables, an OIDC role, or for HCP Terraform a `TF_TOKEN_app_terraform_io` token. Never store them in the repository.

A minimal GitHub Actions job:

```yaml
jobs:
  terraform:
    runs-on: ubuntu-latest
    permissions:
      id-token: write      # OIDC to the cloud provider
      contents: read
    env:
      TF_IN_AUTOMATION: "1"
      TF_INPUT: "0"
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.6.6
      - run: terraform init -lockfile=readonly
      - run: terraform fmt -check -recursive
      - run: terraform validate
      - run: terraform plan -out=tfplan
      - if: github.ref == 'refs/heads/main'
        run: terraform apply tfplan
```

When the configuration uses a `cloud` block, `terraform plan` and `apply` from the pipeline run remotely in HCP Terraform (CLI-driven workflow) and stream logs back. One caveat: saved plan files with remote execution need Terraform 1.6 or later (`terraform plan -out` against HCP Terraform was added in 1.6). HCP Terraform's own VCS-driven workflow removes the need for a custom pipeline entirely ([note 06](./06-hcp-terraform.md)).

## 3d. Share data across configurations and workspaces

Large estates are split into several configurations (network, platform, apps), each with its own state. The downstream ones need values from upstream: VPC IDs, subnet IDs, cluster endpoints. There are three ways to pass them.

### terraform_remote_state

The built-in `terraform_remote_state` data source reads the **root module outputs** of another configuration's state:

```hcl
data "terraform_remote_state" "network" {
  backend = "s3"
  config = {
    bucket = "acme-tfstate-prod"
    key    = "network/terraform.tfstate"
    region = "us-east-1"
  }
}

resource "aws_instance" "app" {
  subnet_id = data.terraform_remote_state.network.outputs.private_subnet_ids["a"]
  # ...
}
```

Only root-level `output` values are exposed, so the upstream configuration must deliberately output what others need (child module outputs must be re-exported at the root). The important caveat, quoted from HashiCorp's docs: although it only exposes outputs, **the reader must have access to the entire state snapshot**, which often contains secrets. It also couples the consumer to the producer's backend layout.

### tfe_outputs (HCP Terraform and Terraform Enterprise)

For workspaces in HCP Terraform, HashiCorp recommends the `tfe_outputs` data source from the `tfe` provider instead, because it reads outputs without needing access to the whole state:

```hcl
data "tfe_outputs" "network" {
  organization = "acme"
  workspace    = "network-prod"
}

resource "aws_instance" "app" {
  subnet_id = data.tfe_outputs.network.nonsensitive_values.private_subnet_ids["a"]
}
```

`values` returns all outputs, but the whole map is marked sensitive. `nonsensitive_values` returns only the outputs that were not marked sensitive upstream, without the sensitive mark, which is usually what you want for IDs. The consumer's token needs permission to read the producing workspace's outputs, and the producing workspace can restrict which workspaces may read its state (remote state sharing setting). Pair it with a **run trigger** so the consumer re-plans whenever the producer applies.

### Publishing through the platform

The loosest coupling is for the producer to write values to a neutral store, and the consumer to read them with an ordinary data source: an SSM parameter (`aws_ssm_parameter`), an Azure App Configuration key, a Consul key, or simply looking the object up by tag (`data "aws_vpc" { tags = { Name = "shared" } }`). The consumer then needs only read access to that value, not to any state, and the producer can reorganize its state freely.

| Method | Coupling | Access needed | Best for |
|---|---|---|---|
| `terraform_remote_state` | Tight (knows the backend) | Whole state of the producer | Small teams, same trust boundary |
| `tfe_outputs` | Medium (knows org and workspace) | Outputs only | HCP Terraform estates |
| Data source lookup or a parameter store | Loose | Just that value | Cross-team, cross-tool sharing |

## Exam traps

- `~> 5.30` allows 5.99 but not 6.0; `~> 5.30.0` allows only 5.30.x.
- The lock file pins providers, not modules.
- `-upgrade` is the only init option that moves a locked provider to a newer version.
- On 1.6 the S3 backend locks only with `dynamodb_table`; `use_lockfile` is newer.
- `azurerm` locks with a blob lease, no extra resource needed.
- `terraform_remote_state` exposes root outputs only, but requires read access to the whole state.
- `TF_IN_AUTOMATION` adjusts output; `-input=false` is what prevents hanging prompts. A pipeline needs both.

## Key terms

- **required_version** - Setting in the terraform block that constrains which Terraform CLI versions may run the configuration.
- **Pessimistic constraint (~>)** - Version operator that lets only the rightmost given part increase, so ~> 5.30 means at least 5.30 and below 6.0.
- **.terraform.lock.hcl** - Dependency lock file recording the exact provider versions and checksums chosen by init; it does not record module versions.
- **terraform providers lock** - Command that adds provider checksums for listed platforms to the lock file so every OS and architecture can verify packages.
- **S3 backend locking** - In Terraform 1.6 the S3 backend locks state with a DynamoDB table whose partition key is LockID, set via dynamodb_table.
- **azurerm backend locking** - The azurerm backend locks state natively by taking a lease on the state blob, so no extra lock resource is needed.
- **cloud block** - Terraform block (1.1 and later) that connects a configuration to HCP Terraform for state and runs, replacing backend remote.
- **TF_IN_AUTOMATION** - Environment variable that, when set to any non-empty value, adjusts output so it does not suggest commands a pipeline cannot run.
- **-input=false** - Option that makes Terraform fail instead of prompting for missing values, essential for unattended pipelines; TF_INPUT=0 is equivalent.
- **-detailed-exitcode** - Plan option returning exit code 0 for no changes, 1 for an error and 2 when changes are present.
- **terraform_remote_state** - Data source that reads another configuration's root outputs but requires read access to that entire state snapshot.
- **tfe_outputs** - tfe provider data source that reads HCP Terraform workspace outputs without full state access; HashiCorp recommends it over remote state.
- **CLI workspaces** - Named states for one configuration in one backend, selected with terraform workspace; distinct from HCP Terraform workspaces.

## Vendor docs

- **[📖 Version constraints](https://developer.hashicorp.com/terraform/language/expressions/version-constraints)** - operators and best practice for modules and roots
- **[📖 Dependency lock file](https://developer.hashicorp.com/terraform/language/files/dependency-lock)** - what is locked and how upgrades work
- **[📖 Backend configuration](https://developer.hashicorp.com/terraform/language/settings/backends/configuration)** - backend blocks and partial configuration
- **[📖 S3 backend](https://developer.hashicorp.com/terraform/language/settings/backends/s3)** - S3 options, locking, assume_role
- **[📖 azurerm backend](https://developer.hashicorp.com/terraform/language/settings/backends/azurerm)** - Azure Blob storage backend and authentication options
- **[📖 HCP Terraform settings (cloud block)](https://developer.hashicorp.com/terraform/cli/cloud/settings)** - the cloud block and its environment variables
- **[📖 Running Terraform in automation](https://developer.hashicorp.com/terraform/tutorials/automation/automate-terraform)** - TF_IN_AUTOMATION, -input=false and saved plans
- **[📖 The terraform_remote_state data source](https://developer.hashicorp.com/terraform/language/state/remote-state-data)** - including the full-state access warning and the tfe_outputs recommendation
- **[📖 tfe_outputs data source](https://registry.terraform.io/providers/hashicorp/tfe/latest/docs/data-sources/outputs)** - reading workspace outputs from HCP Terraform
