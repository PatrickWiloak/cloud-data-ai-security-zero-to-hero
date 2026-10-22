---
last-updated: 2026-10-22
---

# Objective 2: Develop and Troubleshoot Dynamic Configuration

This note covers objective 2 of the HashiCorp Certified: Terraform Authoring and Operations Advanced exam. "Dynamic configuration" means HCL that works out its own values: it reads facts from providers with data sources, computes values with functions and expressions, creates many resources from one block with meta-arguments, accepts structured inputs, guards itself with validation, and handles secrets carefully. In the labs this is where most of your typing happens. Expect to be handed a broken or incomplete configuration and asked to make it produce a specific result.

The tested version is **Terraform 1.6**. Language features added later are flagged as "newer than the tested version".

**[📖 Terraform Authoring and Operations Advanced objectives](https://developer.hashicorp.com/terraform/tutorials/pro-cert/adv-review)** - the official objective list this note follows

## 2a. Use language features to validate configuration

Terraform gives you four layers of validation. They run at different times and fail in different ways, and the exam expects you to pick the right one.

| Feature | Where it lives | When it runs | What happens on failure |
|---|---|---|---|
| `validation` block | Inside a `variable` | When the variable value is set, before planning | Error, nothing is planned |
| `precondition` | `lifecycle` of a resource or data source, or an `output` | Before that object is planned or read | Error, run stops |
| `postcondition` | `lifecycle` of a resource or data source | After the object is planned or applied | Error, run stops (dependent objects are not touched) |
| `check` block | Top level (Terraform 1.5 and later) | At the end of every plan and apply | **Warning only**, run continues |

### Variable validation

A validation block checks a single input and gives the caller a clear message. You can have several per variable; all must pass.

```hcl
variable "environment" {
  type = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "environment must be dev, staging or prod."
  }
}

variable "vpc_cidr" {
  type = string

  validation {
    condition     = can(cidrnetmask(var.vpc_cidr))
    error_message = "vpc_cidr must be a valid IPv4 CIDR block, for example 10.0.0.0/16."
  }

  validation {
    condition     = tonumber(split("/", var.vpc_cidr)[1]) <= 24
    error_message = "vpc_cidr must be /24 or larger."
  }
}
```

In Terraform 1.6 the `condition` may refer **only to the variable being validated**. A rule like "if environment is prod, instance_type must not be t3.micro" cannot go in a validation block on 1.6. **Validation conditions that reference other variables arrived in Terraform 1.9, newer than the tested version.** On 1.6 you express a cross-input rule as a `precondition` on the resource that uses both values.

`can()` is the usual helper: it returns `false` instead of an error when the expression inside it fails, which turns "this would crash" into "this is invalid".

### Preconditions and postconditions

These live in a resource's `lifecycle` block (or on a data source, or a precondition on an output). A precondition states an assumption that must hold before Terraform plans the object. A postcondition states a guarantee about the result, and can refer to the object itself with `self`.

```hcl
data "aws_ami" "app" {
  most_recent = true
  owners      = ["self"]
  filter {
    name   = "name"
    values = ["app-*"]
  }

  lifecycle {
    postcondition {
      condition     = self.architecture == "x86_64"
      error_message = "The selected AMI must be x86_64."
    }
  }
}

resource "aws_instance" "app" {
  ami           = data.aws_ami.app.id
  instance_type = var.instance_type

  lifecycle {
    precondition {
      condition     = !(var.environment == "prod" && startswith(var.instance_type, "t3."))
      error_message = "Production may not use burstable t3 instances."
    }
  }
}

output "app_url" {
  value = "https://${aws_instance.app.public_dns}"

  precondition {
    condition     = aws_instance.app.public_dns != ""
    error_message = "The instance has no public DNS name."
  }
}
```

The value of a postcondition on a data source is that it fails early: anything that depends on that AMI will not be planned at all, so you never launch the wrong image. Use preconditions and postconditions for things that must be true for the configuration to make sense. Use variable validation for things the caller typed wrong.

### Check blocks

A `check` block (Terraform 1.5 and later) asserts something about the infrastructure as a whole. It can include its own scoped data source, which is read only for the check. A failed assertion is reported as a **warning**; it never blocks the plan or apply.

```hcl
check "site_health" {
  data "http" "home" {
    url = "https://${aws_lb.web.dns_name}/health"
  }

  assert {
    condition     = data.http.home.status_code == 200
    error_message = "Health endpoint returned ${data.http.home.status_code}."
  }
}
```

Checks are for ongoing verification. In HCP Terraform, workspaces with health assessments re-evaluate them on a schedule (continuous validation, see [note 06](./06-hcp-terraform.md)). If a scoped data source errors (for example the site is down), that also becomes a warning rather than a failure.

### validate, fmt and test

`terraform validate` checks syntax and internal consistency: references exist, types fit, required arguments are present. It does not contact remote services, so it runs without credentials (after `terraform init -backend=false`). `terraform fmt -check -recursive` fails if any file is not in canonical format; `terraform fmt -recursive` fixes them. Run both before finishing a lab task.

`terraform test` **became generally available in Terraform 1.6**, so it is in scope. Test files end in `.tftest.hcl` and live in the module root or a `tests/` directory. Each `run` block runs a plan or an apply against the module and makes assertions; resources created by apply runs are destroyed at the end.

```hcl
# tests/inputs.tftest.hcl
variables {
  environment = "dev"
  vpc_cidr    = "10.10.0.0/16"
}

run "plan_creates_three_subnets" {
  command = plan

  assert {
    condition     = length(aws_subnet.private) == 3
    error_message = "Expected three private subnets."
  }
}

run "rejects_bad_cidr" {
  command = plan

  variables {
    vpc_cidr = "not-a-cidr"
  }

  expect_failures = [var.vpc_cidr]
}
```

`expect_failures` lists the checkable objects (variables, resources, outputs, check blocks) whose validation is expected to fail, which is how you test your own validation rules. A `run` block can also contain a `module` block to run a helper module (for example one that sets up prerequisites), and later runs can refer to earlier runs' outputs as `run.<name>.<output>`. **Mock providers and `override_resource` / `override_data` arrived in Terraform 1.7, newer than the tested version.** In 1.6, tests use real providers.

## 2b. Query providers using data sources

A data source asks a provider for information about something that already exists, without managing it. You reference the result as `data.<type>.<name>.<attribute>`.

```hcl
data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

data "aws_availability_zones" "available" {
  state = "available"
}

data "aws_vpc" "shared" {
  tags = { Name = "shared-services" }
}

data "aws_iam_policy_document" "read_bucket" {
  statement {
    actions   = ["s3:GetObject"]
    resources = ["arn:aws:s3:::${var.bucket}/*"]
  }
}

locals {
  account_id = data.aws_caller_identity.current.account_id
  azs        = slice(data.aws_availability_zones.available.names, 0, 3)
}
```

Points that matter:

- **When is it read?** Normally during plan. If any argument depends on a value that is not known until apply (for example the ID of a resource being created in the same run), the read is deferred to apply, and the plan shows `<= read (data resources)`. Anything depending on that data source is then also unknown at plan time.
- **Lookups that must match exactly one object** (`aws_vpc`, `aws_ami` without `most_recent`) fail if they find zero or several. Read the error; it usually says which.
- **`depends_on` on a data source** forces it to wait until apply whenever the dependency has changes, which makes values unknown during plan. Prefer a direct reference that creates the dependency naturally.
- **Utility data sources** compute values locally: `aws_iam_policy_document`, `template_file` (deprecated, use `templatefile()`), `external`, `http`.
- Data sources can have a `provider` meta-argument to read from an aliased provider, for example a different region.

`terraform_remote_state` and `tfe_outputs` are data sources too; they read outputs from other configurations and are covered under sharing data in [note 03](./03-collaborative-workflows.md).

## 2c. Compute and interpolate data using HCL functions

Terraform has no user-defined functions in 1.6. **Provider-defined functions arrived in Terraform 1.8, and `templatestring()` in 1.9, both newer than the tested version.** You work with the built-in library, expressions, and `locals`. The exam has the docs available, so you do not need to memorize every signature, but you must know which function solves which problem.

| Problem | Functions and expressions |
|---|---|
| Combine maps and lists | `merge`, `concat`, `flatten`, `setunion`, `setproduct`, `zipmap` |
| Look up with a fallback | `lookup(map, key, default)`, `try(expr, fallback)`, `coalesce`, `one` |
| Test without failing | `can(expr)`, `contains`, `alltrue`, `anytrue`, `startswith`, `endswith`, `strcontains` (1.5+) |
| Reshape collections | `keys`, `values`, `toset`, `tolist`, `tomap`, `distinct`, `sort`, `reverse`, `slice`, `element`, `length` |
| Networking | `cidrsubnet`, `cidrsubnets`, `cidrhost`, `cidrnetmask` |
| Strings | `format`, `join`, `split`, `replace`, `regex`, `regexall`, `trimspace`, `lower`, `upper`, `substr` |
| Encoding and files | `jsonencode`, `jsondecode`, `yamlencode`, `yamldecode`, `base64encode`, `file`, `templatefile`, `fileset` |
| Sensitivity | `sensitive`, `nonsensitive` |
| Time | `timestamp`, `formatdate`, `timeadd` (note `timestamp()` changes every run) |

Expressions you will write constantly:

```hcl
locals {
  # for expression: list -> map
  subnet_ids_by_az = { for s in aws_subnet.private : s.availability_zone => s.id }

  # filter with if
  public_subnets = { for k, v in var.subnets : k => v if v.public }

  # splat
  instance_ids = aws_instance.web[*].id

  # conditional
  instance_type = var.environment == "prod" ? "m6i.large" : "t3.small"

  # flatten nested data for for_each: one element per (network, subnet) pair
  network_subnets = flatten([
    for net_key, net in var.networks : [
      for sub_key, cidr in net.subnets : {
        key     = "${net_key}.${sub_key}"
        network = net_key
        cidr    = cidr
      }
    ]
  ])

  # carve /24s out of a /16
  private_cidrs = [for i in range(3) : cidrsubnet(var.vpc_cidr, 8, i)]

  # string template with a directive
  greeting = "Hello, %{ if var.name != "" }${var.name}%{ else }stranger%{ endif }!"
}
```

The `flatten` pattern is worth practicing until it is automatic. `for_each` needs a flat map or set, and real inputs are usually nested. You flatten to a list of objects, then turn it into a map keyed by something stable: `for_each = { for ns in local.network_subnets : ns.key => ns }`.

`templatefile("${path.module}/user_data.sh.tftpl", { port = var.port })` renders a file template with variables. Use `path.module` for files that ship with a module; `path.root` and `path.cwd` point elsewhere when the module is called from another directory.

**Troubleshoot expressions with `terraform console`.** It loads the configuration and state, and lets you evaluate any expression interactively. When a function call fails in a plan, paste it into the console with literal values until you see which piece is wrong.

```text
$ terraform console
> cidrsubnet("10.0.0.0/16", 8, 3)
"10.0.3.0/24"
> { for k, v in var.subnets : k => v.cidr if v.public }
> try(var.settings.optional_flag, false)
> type(local.network_subnets)
```

## 2d. Use meta-arguments in configuration

Meta-arguments are arguments Terraform itself understands, available on every resource (and most on module blocks and data sources).

### count and for_each

Both create several instances from one block. They cannot be used together on the same block.

```hcl
# count: a number. Addresses are aws_instance.web[0], [1], ...
resource "aws_instance" "web" {
  count         = var.web_count
  ami           = data.aws_ami.app.id
  instance_type = "t3.small"
  tags          = { Name = "web-${count.index}" }
}

# conditional creation
resource "aws_cloudwatch_log_group" "debug" {
  count = var.enable_debug ? 1 : 0
  name  = "/app/debug"
}

# for_each: a map or a set of strings. Addresses are keyed: aws_iam_user.this["alice"]
resource "aws_iam_user" "this" {
  for_each = toset(var.user_names)
  name     = each.key
}

resource "aws_subnet" "private" {
  for_each          = var.private_subnets   # map(object)
  vpc_id            = aws_vpc.main.id
  cidr_block        = each.value.cidr
  availability_zone = each.value.az
  tags              = { Name = each.key }
}
```

The difference that matters: `count` addresses by position, so removing the first item shifts every later index and Terraform replaces them all. `for_each` addresses by key, so removing one item removes only that instance. Use `count` for "zero or one" and for truly identical copies; use `for_each` for anything with an identity. Switching an existing `count` resource to `for_each` needs `moved` blocks to avoid replacement (see [note 01](./01-manage-resource-lifecycle.md)).

The keys of `for_each` (and the value of `count`) must be **known at plan time**. If you build them from a resource attribute that is computed during apply, you get "The for_each value depends on resource attributes that cannot be determined until apply". The fix is to key on values you control (input variables, static names) and only put computed values in the body.

Referring to multi-instance resources: `aws_instance.web[0].id`, `aws_iam_user.this["alice"].arn`, all of them with `aws_instance.web[*].id` (count) or `values(aws_iam_user.this)[*].arn` (for_each).

### dynamic blocks

`dynamic` generates repeated nested blocks inside one resource, such as security group rules or listener actions:

```hcl
resource "aws_security_group" "web" {
  name   = "web"
  vpc_id = aws_vpc.main.id

  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = "tcp"
      cidr_blocks = ingress.value.cidrs
    }
  }
}
```

The iterator is named after the block (`ingress.key`, `ingress.value`) unless you set `iterator = rule`. Overuse makes configuration hard to read; HashiCorp's guidance is to use it when you need to hide detail behind a clean module interface.

### depends_on

Terraform infers order from references. `depends_on` adds a dependency it cannot see, for example an IAM policy that must exist before an instance's software calls AWS, even though the instance never references the policy.

```hcl
resource "aws_instance" "app" {
  # ...
  depends_on = [aws_iam_role_policy.app_s3]
}
```

Use it as a last resort and add a comment saying why. It makes plans more conservative (more values unknown until apply). `terraform graph` outputs the dependency graph in DOT format so you can see what Terraform inferred: `terraform graph | dot -Tsvg > graph.svg`. A "Cycle" error means two objects depend on each other, often through a `depends_on` or a security group that references itself; break it by splitting the resource (for example separate `aws_security_group_rule` resources).

### provider

Selects a non-default provider configuration: `provider = aws.us_west_2`. On module blocks the equivalent is the `providers` map. Covered in [note 05](./05-providers.md).

### lifecycle

```hcl
resource "aws_launch_template" "app" { /* ... */ }

resource "aws_autoscaling_group" "app" {
  # ...
  lifecycle {
    create_before_destroy = true
    prevent_destroy       = false
    ignore_changes        = [desired_capacity]   # autoscaling changes this
    replace_triggered_by  = [aws_launch_template.app.latest_version]
  }
}
```

- `create_before_destroy` builds the replacement first, so there is no gap. It fails if the new object needs a unique name the old one still holds; use `name_prefix` instead of `name`.
- `prevent_destroy` makes any plan that would destroy the object an error.
- `ignore_changes` stops Terraform reverting specific attributes (or `all`) that change outside Terraform.
- `replace_triggered_by` (1.2 and later) replaces this resource when a referenced resource or attribute changes.

`lifecycle` arguments must be literal values; you cannot set `prevent_destroy = var.protect`.

`terraform_data` (1.4 and later) is the built-in replacement for `null_resource`. It stores a value, and its `triggers_replace` argument is useful as a target for `replace_triggered_by` when you want a plain value (not a resource) to force replacement.

## 2e. Configure input variables and outputs, including complex types

### Variables

```hcl
variable "private_subnets" {
  description = "Private subnets keyed by name."
  type = map(object({
    cidr = string
    az   = string
    tags = optional(map(string), {})
    nat  = optional(bool, true)
  }))
  default  = {}
  nullable = false
}

variable "db_password" {
  type      = string
  sensitive = true
}
```

Types come in three groups:

- **Primitive:** `string`, `number`, `bool`.
- **Collection** (every element the same type): `list(T)`, `set(T)`, `map(T)`.
- **Structural** (named or positional, mixed types): `object({...})` and `tuple([...])`.

`any` lets Terraform infer the type from the value. That is convenient but you lose checking, and a module that takes `any` is harder to use correctly.

**Optional object attributes** (`optional(type, default)`, generally available since Terraform 1.3) let callers leave attributes out. Without a default the missing attribute is `null`; with a default it gets that value. This is how you build a rich object input that is still easy to call.

**`nullable = false`** means a caller passing `null` gets the default instead of null. Without it, an explicit `null` overrides the default, which surprises people.

Terraform converts values to the declared type where it can (`"5"` to `5`, a tuple to a list). If a conversion is impossible you get an "Invalid value for input variable" error that names the attribute path; read it closely.

### Outputs

```hcl
output "private_subnet_ids" {
  description = "Subnet IDs keyed by subnet name."
  value       = { for k, s in aws_subnet.private : k => s.id }
}

output "db_connection_string" {
  value     = "postgres://app:${var.db_password}@${aws_db_instance.main.address}/app"
  sensitive = true
}
```

Outputs from the root module are printed after apply and stored in state; outputs from a child module are how the parent reads values (`module.network.private_subnet_ids`). If an output value is derived from a sensitive value, Terraform requires `sensitive = true` on the output or it errors. Outputs can also have `depends_on` and a `precondition`.

## 2f. Analyze best practices for managing sensitive data

This sub-objective is about understanding where secrets go, not just how to hide them on screen.

### What `sensitive` does and does not do

Marking a variable or output `sensitive = true` (or wrapping a value with `sensitive()`) **redacts it in plan and apply output** and propagates the mark to anything computed from it. It does **not** keep the value out of state. Every attribute of every resource, including passwords you passed in, is stored in plain text in the state file. `terraform output -raw name` and `terraform output -json` will still show a sensitive output to anyone who can read state.

`nonsensitive()` removes the mark. Use it only when you are sure the derived value is not secret (for example a hash, or the length of a list).

So the real protection is around state:

- Use a remote backend with encryption at rest (S3 with SSE-KMS, azurerm with storage encryption, HCP Terraform, which encrypts state).
- Restrict who can read state. In HCP Terraform, workspace state read is a separate permission from viewing runs.
- Never commit state, `.tfvars` files containing secrets, or plan files (they contain values too) to version control.
- Prefer `tfe_outputs` to `terraform_remote_state` across teams, because remote state gives the reader the whole state snapshot (see [note 03](./03-collaborative-workflows.md)).

### Getting secrets in

- Supply them as environment variables (`TF_VAR_db_password`) or as sensitive workspace variables in HCP Terraform, never as defaults in HCL.
- Let providers authenticate from their own environment variables or from dynamic credentials, not from `access_key` arguments in HCL ([note 05](./05-providers.md), [note 06](./06-hcp-terraform.md)).
- Where the target service can generate the secret itself, let it. For example `manage_master_user_password = true` on an RDS instance stores the password in AWS Secrets Manager instead of in your configuration.

### Vault for secrets management

The Vault provider lets Terraform read secrets from HashiCorp Vault at plan or apply time instead of keeping them in variables:

```hcl
provider "vault" {
  # address and token come from VAULT_ADDR and VAULT_TOKEN,
  # or from HCP Terraform Vault-backed dynamic credentials
}

data "vault_kv_secret_v2" "db" {
  mount = "secret"
  name  = "app/db"
}

resource "aws_db_instance" "main" {
  # ...
  password = data.vault_kv_secret_v2.db.data["password"]
}
```

The caveat the exam cares about, in Terraform 1.6: **a secret read through a data source is written to state**, and so is the resource argument it feeds. Vault improves where secrets are stored, rotated and audited, but it does not by itself keep them out of Terraform state. The stronger pattern is **dynamic secrets**: have Vault mint short-lived credentials (for example the `vault_aws_access_credentials` data source with a short TTL, or HCP Terraform's Vault-backed dynamic credentials), so that whatever lands in state has already expired.

**Ephemeral resources, ephemeral variables and outputs (Terraform 1.10) and write-only arguments (Terraform 1.11) are newer than the tested version.** They exist precisely to keep values out of state and plan files. Know they exist for your day job, but on a 1.6 exam the answer is "sensitive hides output, state still holds the value, protect the state".

## Exam traps

- Validation blocks in 1.6 can only reference their own variable. Cross-input rules go in a `precondition`.
- `check` block failures are warnings. If the task says "the apply must fail when X", use a precondition or postcondition.
- `sensitive = true` hides values from CLI output, not from state.
- `for_each` keys must be known at plan time; key on inputs, not on computed IDs.
- `count` with a list reorders and replaces; `for_each` with a map does not.
- `lifecycle` values must be literals.
- `terraform test` is in 1.6; mock providers are 1.7. Provider-defined functions are 1.8. Ephemeral values are 1.10.

## Key terms

- **validation block** - Rule inside a variable block that rejects bad input before planning; in Terraform 1.6 it may reference only its own variable.
- **precondition** - Custom condition in a lifecycle block or output that must hold before the object is planned, failing the run if false.
- **postcondition** - Custom condition in a resource or data source lifecycle block that checks the result, using self, and fails the run if false.
- **check block** - Top-level assertion (Terraform 1.5 and later) evaluated after plan and apply that reports failures as warnings only.
- **terraform test** - Command, generally available in Terraform 1.6, that runs .tftest.hcl files with run blocks, assertions and expect_failures.
- **expect_failures** - List in a terraform test run block naming checkable objects whose validation is expected to fail, used to test validation rules.
- **Data source** - Read-only lookup of existing information from a provider, referenced as data.TYPE.NAME and read at plan time when possible.
- **for_each** - Meta-argument that creates one instance per key of a map or set of strings, addressed by key; keys must be known at plan time.
- **count** - Meta-argument that creates a numbered set of instances addressed by index; best for zero-or-one and truly identical copies.
- **dynamic block** - Construct that generates repeated nested blocks inside a resource from a collection, using a content block and an iterator.
- **replace_triggered_by** - Lifecycle argument (Terraform 1.2 and later) that replaces a resource when a referenced resource or attribute changes.
- **optional()** - Object type modifier (Terraform 1.3 and later) that lets callers omit an attribute, optionally supplying a default value.
- **sensitive** - Flag on variables and outputs that redacts values from CLI output; the values are still stored in plain text in state.
- **Dynamic secrets** - Short-lived credentials generated on demand, for example by Vault, so any copy written to Terraform state soon expires.

## Vendor docs

- **[📖 Custom conditions](https://developer.hashicorp.com/terraform/language/expressions/custom-conditions)** - validation, preconditions, postconditions and checks compared
- **[📖 Checks](https://developer.hashicorp.com/terraform/language/checks)** - check blocks and scoped data sources
- **[📖 Tests](https://developer.hashicorp.com/terraform/language/tests)** - `terraform test` file syntax
- **[📖 Data sources](https://developer.hashicorp.com/terraform/language/data-sources)** - how and when data sources are read
- **[📖 Functions](https://developer.hashicorp.com/terraform/language/functions)** - the built-in function reference
- **[📖 Meta-arguments: for_each](https://developer.hashicorp.com/terraform/language/meta-arguments/for_each)** - including the known-at-plan-time rule
- **[📖 The lifecycle meta-argument](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle)** - create_before_destroy, ignore_changes, replace_triggered_by
- **[📖 Type constraints](https://developer.hashicorp.com/terraform/language/expressions/type-constraints)** - complex types and optional attributes
- **[📖 Input variables](https://developer.hashicorp.com/terraform/language/values/variables)** - validation, sensitive, nullable and precedence
- **[📖 Sensitive data in state](https://developer.hashicorp.com/terraform/language/state/sensitive-data)** - why state must be protected
- **[📖 Vault provider](https://registry.terraform.io/providers/hashicorp/vault/latest/docs)** - reading and generating secrets from Vault
