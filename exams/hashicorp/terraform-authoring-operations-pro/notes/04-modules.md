---
last-updated: 2026-10-22
---

# Objective 4: Create, Maintain and Use Terraform Modules

This note covers objective 4 of the HashiCorp Certified: Terraform Authoring and Operations Advanced exam. A module is just a directory of `.tf` files; every configuration is a module (the root module), and it can call child modules. The exam asks you to write a module with a clean interface (4a), call modules correctly from different sources (4b), change a module without breaking the people who use it (4c), and take an existing flat configuration and move its resources into modules without destroying anything (4d).

The tested version is **Terraform 1.6**. Anything later is flagged as "newer than the tested version".

**[📖 Terraform Authoring and Operations Advanced objectives](https://developer.hashicorp.com/terraform/tutorials/pro-cert/adv-review)** - the official objective list this note follows

## 4a. Create a module

### Layout

HashiCorp's standard module structure is a convention the registry understands, and it is what reviewers expect:

```text
terraform-aws-network/
├── README.md          # what it does, a usage example
├── main.tf            # resources
├── variables.tf       # inputs
├── outputs.tf         # outputs
├── versions.tf        # required_version and required_providers
├── examples/
│   └── complete/main.tf
├── modules/           # nested submodules, if any
│   └── subnet/
└── tests/
    └── defaults.tftest.hcl
```

Only the `.tf` files in the directory itself make up the module. Terraform does not recurse into subdirectories; nested modules under `modules/` are separate modules called with `source = "./modules/subnet"`.

### Designing the interface

A module's inputs and outputs are its API. Most of the craft is here.

```hcl
# variables.tf
variable "name" {
  description = "Name prefix for every resource."
  type        = string
}

variable "cidr_block" {
  description = "VPC CIDR."
  type        = string
  validation {
    condition     = can(cidrnetmask(var.cidr_block))
    error_message = "cidr_block must be a valid CIDR."
  }
}

variable "private_subnets" {
  description = "Private subnets keyed by a short name."
  type = map(object({
    cidr = string
    az   = string
    tags = optional(map(string), {})
  }))
  default = {}
}

variable "tags" {
  description = "Tags applied to every resource."
  type        = map(string)
  default     = {}
}
```

```hcl
# main.tf
resource "aws_vpc" "this" {
  cidr_block = var.cidr_block
  tags       = merge(var.tags, { Name = var.name })
}

resource "aws_subnet" "private" {
  for_each          = var.private_subnets
  vpc_id            = aws_vpc.this.id
  cidr_block        = each.value.cidr
  availability_zone = each.value.az
  tags              = merge(var.tags, each.value.tags, { Name = "${var.name}-${each.key}" })
}
```

```hcl
# outputs.tf
output "vpc_id" {
  description = "ID of the VPC."
  value       = aws_vpc.this.id
}

output "private_subnet_ids" {
  description = "Private subnet IDs keyed by the same names as var.private_subnets."
  value       = { for k, s in aws_subnet.private : k => s.id }
}
```

Design choices the exam rewards:

- **Typed inputs with descriptions.** `type = any` and untyped variables push errors downstream. Use `object` with `optional()` attributes for rich inputs (see [note 02](./02-dynamic-configuration.md)).
- **Sensible defaults** for anything optional; required inputs have no default.
- **Validation** at the boundary, so callers get a clear error rather than an API error from the provider.
- **Maps keyed by name** for collections, so `for_each` gives stable addresses.
- **Output what callers need**, including whole objects when useful (`value = aws_vpc.this`), and mark secrets `sensitive`.
- **Name the main resource `this`** when the module has one primary resource of a type. It reads well (`module.network.aws_vpc.this`) and is a common convention.

### Providers in a reusable module

A reusable module declares which providers it needs but **does not configure them**:

```hcl
# versions.tf
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}
```

Do not put a `provider "aws" { region = ... }` block inside a reusable module. A module with its own provider block cannot be used with `count`, `for_each` or `depends_on`, and removing it from a configuration later becomes hard because Terraform needs the provider configuration to destroy its resources. Provider configuration belongs in the root module and is passed down implicitly (default provider) or explicitly through the `providers` argument ([note 05](./05-providers.md)). If a module needs two configurations of the same provider (for example two regions), declare `configuration_aliases = [aws.replica]` in `required_providers`.

### Testing a module

Since Terraform 1.6, `terraform test` can exercise a module through `.tftest.hcl` files with `run` blocks and assertions ([note 02](./02-dynamic-configuration.md)). Example configurations under `examples/` double as documentation and as test fixtures.

## 4b. Use a module in configuration

```hcl
module "network" {
  source  = "app.terraform.io/acme/network/aws"
  version = "~> 2.1"

  name       = "prod"
  cidr_block = "10.0.0.0/16"
  private_subnets = {
    a = { cidr = "10.0.1.0/24", az = "us-east-1a" }
    b = { cidr = "10.0.2.0/24", az = "us-east-1b" }
  }
  tags = local.common_tags
}

resource "aws_instance" "app" {
  subnet_id = module.network.private_subnet_ids["a"]
  # ...
}
```

You can only read a child module's **outputs** (`module.network.vpc_id`), never its internal resources. If you need a value that is not output, the module must be changed.

### Module sources

| Source | Example | `version` argument? |
|---|---|---|
| Local path | `source = "./modules/network"` | No. Local modules are not installed separately; changes are picked up immediately |
| Public Terraform Registry | `source = "terraform-aws-modules/vpc/aws"` (namespace/name/provider) | Yes |
| Private registry (HCP Terraform) | `source = "app.terraform.io/acme/network/aws"` | Yes |
| Git | `source = "git::https://github.com/acme/tf-network.git//modules/vpc?ref=v2.1.0"` | No, use `?ref=` |
| GitHub shorthand | `source = "github.com/acme/tf-network?ref=v2.1.0"` | No |
| S3, GCS, HTTP archive | `source = "s3::https://s3.amazonaws.com/bucket/network.zip"` | No |

The `version` argument works **only for registry sources**. For Git, pin with `?ref=` to a tag or commit; without it you get the default branch, which changes under you. A double slash (`//modules/vpc`) selects a subdirectory inside the repository or archive. After adding or changing a source or version, run `terraform init` (or `terraform get`) to install it.

### Meta-arguments on module blocks

Since Terraform 0.13, module blocks accept `count`, `for_each`, `depends_on` and `providers`:

```hcl
module "regional_bucket" {
  for_each = toset(["us-east-1", "us-west-2"])
  source   = "./modules/bucket"
  name     = "logs-${each.key}"
}

output "bucket_arns" {
  value = { for region, m in module.regional_bucket : region => m.arn }
}
```

Instances are addressed `module.regional_bucket["us-east-1"]`. Note that `for_each` over a module cannot pick a different provider configuration per instance, because `providers` must be static; for per-region modules you write one module block per aliased provider.

`depends_on` on a module makes everything in it wait for the dependency. It is blunt: data sources inside the module may be deferred to apply. Prefer passing an output of the dependency as an input.

## 4c. Refactor a module and use module versioning

### Semantic versioning

Registry modules are versioned by Git tags of the form `v1.2.3` (or `1.2.3`). Use the numbers to tell consumers what kind of change they are getting:

- **Major** (`2.0.0`): breaking. A required input added, an input removed or renamed, a type changed incompatibly, an output removed, or a change that replaces resources.
- **Minor** (`1.3.0`): new behaviour that is backward compatible, such as a new optional input with a default that keeps old behaviour.
- **Patch** (`1.2.4`): bug fixes with no interface change.

Consumers choose how much change they accept with the constraint: `~> 1.2` takes minors and patches but never 2.0; `~> 1.2.0` takes patches only. When you publish 2.0.0, write upgrade notes, and keep fixing 1.x for a while if consumers need time.

### Publishing to a registry

For the public registry or HCP Terraform's private registry, the repository is named `terraform-<PROVIDER>-<NAME>` (for example `terraform-aws-network`), follows the standard structure, and has semver tags. In HCP Terraform you publish from a connected VCS repository; each new tag becomes a new version automatically (tag-based publishing; HCP Terraform also supports branch-based publishing). Consumers then use `app.terraform.io/<org>/<name>/<provider>` as the source.

### Refactoring inside a module without breaking consumers

When you rename a resource inside a module, every caller's state still has the old address. Put a `moved` block **inside the module** and every consumer gets the move automatically the next time they upgrade and apply:

```hcl
# inside the module, after renaming aws_vpc.main to aws_vpc.this
moved {
  from = aws_vpc.main
  to   = aws_vpc.this
}

# after switching a subnet resource from count to for_each
moved {
  from = aws_subnet.private[0]
  to   = aws_subnet.private["a"]
}
```

A move recorded this way is part of the module's public contract. HashiCorp's guidance is to keep `moved` blocks in a shared module for a long time (ideally until the next major version), because you do not know when each consumer will upgrade. Removing a `moved` block too early means a consumer jumping several versions sees destroy and create instead.

Things `moved` cannot fix: changing a resource to a different **type** (for example `aws_s3_bucket_object` to `aws_s3_object`) is not a move in Terraform 1.6; it needs `terraform state rm` plus an import, or a major version bump. (Terraform 1.8 added cross-type moves for providers that support them, newer than the tested version.) Splitting one resource into several (such as the AWS provider v4 split of `aws_s3_bucket` settings into separate resources) also needs imports.

## 4d. Refactor an existing configuration into modules

The classic lab task: a flat root module has resources that should live in a module, and you must move them without anything being destroyed.

**Before:**

```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "a" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
}
```

**After:**

```hcl
module "network" {
  source     = "./modules/network"
  name       = "prod"
  cidr_block = "10.0.0.0/16"
  private_subnets = {
    a = { cidr = "10.0.1.0/24", az = "us-east-1a" }
  }
}

moved {
  from = aws_vpc.main
  to   = module.network.aws_vpc.this
}

moved {
  from = aws_subnet.a
  to   = module.network.aws_subnet.private["a"]
}
```

The steps:

1. Create the module directory and move the resource blocks into it, turning hard-coded values into variables and adding outputs for anything the root still references.
2. Replace the resources in the root with a `module` block, and update root references (`aws_vpc.main.id` becomes `module.network.vpc_id`).
3. Add one `moved` block per resource (or per instance) from the old root address to the new module address. These go in the **calling** module, because that is where both addresses are visible.
4. Run `terraform init` (a new local module must be installed).
5. Run `terraform plan`. The goal is lines saying "has moved to" and **0 to add, 0 to change, 0 to destroy**. Any `-/+` means an argument value differs between the old and new code (often a tag or name built differently); fix the module until it disappears.
6. Apply, so state records the new addresses.

The imperative alternative is `terraform state mv aws_vpc.main module.network.aws_vpc.this`. It works, but leaves nothing reviewable and is easy to get wrong with many resources. Use it when the task says to, or when the target is in a different state file.

If the module will be called with `count` or `for_each`, the destination address includes the instance key: `to = module.network["prod"].aws_vpc.this`.

## Exam traps

- `version` works only with registry sources. Git sources use `?ref=`.
- A reusable module declares `required_providers` but does not contain `provider` blocks.
- You can read only a module's outputs, never its internal resources.
- `moved` blocks that refactor into a module go in the calling module; moves within a module go inside the module.
- A successful refactor plan shows moves and **zero** add, change or destroy.
- Changing resource **type** is not a move in 1.6.
- Every new or changed module source needs `terraform init`.

## Key terms

- **Root module** - The configuration in the working directory where Terraform runs; it calls child modules and owns provider configuration.
- **Child module** - A module called from another module with a module block, whose outputs are the only values the caller can read.
- **Standard module structure** - HashiCorp's recommended layout with main.tf, variables.tf, outputs.tf, a README, examples and nested modules directories.
- **Module source** - The source argument of a module block: a local path, registry address, private registry address, Git URL or archive URL.
- **Module version argument** - Version constraint on a module block that works only for registry sources; Git sources pin with ?ref= instead.
- **configuration_aliases** - required_providers setting in a module that declares which aliased provider configurations the caller must pass in.
- **Semantic versioning** - MAJOR.MINOR.PATCH scheme where a major bump signals a breaking change, minor a compatible feature and patch a fix.
- **Registry module naming** - Repositories published to the Terraform registry are named terraform-PROVIDER-NAME and use semver tags for versions.
- **moved block in a module** - A moved block placed inside a shared module so every consumer's state is updated automatically when they upgrade.
- **Refactor into a module** - Move resources into a module and add moved blocks from old root addresses to module addresses so plan shows no replacements.
- **Double slash in a source** - The // in a module source selects a subdirectory inside a Git repository or archive, for example repo.git//modules/vpc.

## Vendor docs

- **[📖 Modules overview](https://developer.hashicorp.com/terraform/language/modules)** - root and child modules
- **[📖 Standard module structure](https://developer.hashicorp.com/terraform/language/modules/develop/structure)** - the layout the registry expects
- **[📖 Module sources](https://developer.hashicorp.com/terraform/language/modules/sources)** - every supported source type and the `//` and `?ref=` syntax
- **[📖 Module blocks](https://developer.hashicorp.com/terraform/language/modules/syntax)** - calling modules and meta-arguments
- **[📖 Providers within modules](https://developer.hashicorp.com/terraform/language/modules/develop/providers)** - why reusable modules should not configure providers
- **[📖 Refactoring](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring)** - `moved` blocks inside and across modules
- **[📖 Publishing modules](https://developer.hashicorp.com/terraform/registry/modules/publish)** - registry naming and tag requirements
- **[📖 HCP Terraform private registry](https://developer.hashicorp.com/terraform/cloud-docs/registry)** - publishing and consuming private modules
