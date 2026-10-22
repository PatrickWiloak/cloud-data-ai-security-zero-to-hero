---
last-updated: 2026-10-22
---

# HashiCorp Certified: Terraform Authoring and Operations Advanced

## Exam Overview

The HashiCorp Certified: Terraform Authoring and Operations Advanced certification validates hands-on Terraform skill beyond the Associate level: writing dynamic configuration and modules, managing the full resource lifecycle and state, running Terraform collaboratively and in automation, configuring providers, and working with HCP Terraform. HashiCorp previously listed this same exam as "Terraform Authoring and Operations Professional", and the old Professional objectives page now redirects to the Advanced one, so guides and posts using either name describe this exam. "Terraform Infrastructure Engineer Professional" is a different, multiple-choice exam that this guide does not cover.

Most of the exam is **lab-based**: you work in a live environment with a terminal, an editor and a cloud account, and each lab is scored by checking what you leave behind (configuration syntax, state files and the settings on provisioned resources). There are also multiple-choice questions, and objective 6 (HCP Terraform) is tested by multiple choice only.

**Exam Name:** HashiCorp Certified: Terraform Authoring and Operations Advanced
**Format:** Lab-based scenarios plus multiple choice (objective 6 is multiple-choice only)
**Duration:** 4 hours, with one 15-minute break
**Terraform Version Tested:** 1.6
**Cost:** $295 USD plus taxes, with a free retake included
**Delivery:** Online proctored
**Cloud Version:** Choose AWS or Azure; both give the same credential
**Passing Score:** Not published (no numeric cut score, no published question or lab count)
**Validity:** 2 years
**Language:** English
**Prerequisites:** None required; HashiCorp strongly recommends the Terraform Associate certification or equivalent experience

During the exam you can use the Terraform documentation, a limited part of the Terraform Registry, limited cloud provider documentation and the cloud console. Search engines are not available. Labs can be done in any order and are scored independently, and multiple-choice items can be flagged for review.

## Who Should Take This Exam

- Engineers who already write and run Terraform in production and want to prove it hands-on
- Platform engineers who build modules and workflows other teams consume
- DevOps and SRE leads who run Terraform pipelines and HCP Terraform organizations
- Consultants who adopt, migrate and govern Terraform for clients

## Prerequisites and Recommended Experience

HashiCorp's orientation page lists the skills it assumes: Terraform Associate-level knowledge or equivalent, comfort on the Linux command line, working cloud credentials, reading YAML, JSON, HCL and CSV, basic TCP/IP and UDP networking, advanced Terraform authoring, and production experience. In practice that means you have imported resources, refactored into modules, migrated state and debugged provider errors yourself, not only read about them.

## Exam Domains

HashiCorp publishes six objectives but **does not publish weights** for them.

| # | Objective | Weight | Note |
|---|---|---|---|
| 1 | Manage resource lifecycle | Not published | [01-manage-resource-lifecycle.md](./notes/01-manage-resource-lifecycle.md) |
| 2 | Develop and troubleshoot dynamic configuration | Not published | [02-dynamic-configuration.md](./notes/02-dynamic-configuration.md) |
| 3 | Develop collaborative Terraform workflows | Not published | [03-collaborative-workflows.md](./notes/03-collaborative-workflows.md) |
| 4 | Create, maintain, and use Terraform modules | Not published | [04-modules.md](./notes/04-modules.md) |
| 5 | Configure and use Terraform providers | Not published | [05-providers.md](./notes/05-providers.md) |
| 6 | Collaborate on infrastructure as code using HCP Terraform (multiple choice only) | Not published | [06-hcp-terraform.md](./notes/06-hcp-terraform.md) |

[fact-sheet.md](./fact-sheet.md) lists the sub-objectives (1a to 6d) and a suggested study-time split, which is this guide's estimate, not HashiCorp's.

## Study Materials

| File | What it covers |
|---|---|
| [fact-sheet.md](./fact-sheet.md) | Exam logistics, every sub-objective, high-yield facts per objective |
| [notes/01-manage-resource-lifecycle.md](./notes/01-manage-resource-lifecycle.md) | init, plan, apply and destroy options; state commands; import; moved; drift |
| [notes/02-dynamic-configuration.md](./notes/02-dynamic-configuration.md) | Validation, preconditions, check blocks, `terraform test`; data sources; functions; meta-arguments; complex types; sensitive data and Vault |
| [notes/03-collaborative-workflows.md](./notes/03-collaborative-workflows.md) | Version constraints and the lock file; S3, azurerm and HCP Terraform backends; automation; `terraform_remote_state` and `tfe_outputs` |
| [notes/04-modules.md](./notes/04-modules.md) | Writing, calling, versioning and refactoring modules |
| [notes/05-providers.md](./notes/05-providers.md) | Plugin architecture, aliases, sourcing, upgrades, authentication, TF_LOG debugging |
| [notes/06-hcp-terraform.md](./notes/06-hcp-terraform.md) | Run workflow, workspaces and permissions, dynamic provider credentials, Sentinel and OPA policy |
| [practice-plan.md](./practice-plan.md) | Week-by-week lab plan mapped to the six objectives |
| [scenarios.md](./scenarios.md) | Real-world scenarios with worked answers |
| [strategy.md](./strategy.md) | Time management and per-objective tactics for exam day |

## Study Path

1. Read [fact-sheet.md](./fact-sheet.md) for the format and the objective list.
2. Work through the six notes in order. Notes 01 to 05 are lab territory: type every example yourself on Terraform 1.6.
3. Follow [practice-plan.md](./practice-plan.md), which builds a lab for each objective.
4. Work [scenarios.md](./scenarios.md) without looking at the answers first.
5. Read [strategy.md](./strategy.md) in the last week.

## Hands-on Lab Requirements

Because labs are graded on end state, you need muscle memory, not recognition. Set up:

- **Terraform 1.6.x** as your main CLI (a version manager such as `tfenv` lets you switch). Newer versions accept syntax the exam environment will reject, such as `removed` blocks (1.7) or cross-variable validation (1.9).
- A sandbox in the cloud you will choose for the exam: AWS or Azure.
- A free HCP Terraform organization for objective 6 concepts and for the `cloud` block.
- Git, `jq`, and an editor you can use quickly.

## Official Resources

- **[📖 Terraform Authoring and Operations Advanced certification](https://developer.hashicorp.com/certifications/terraform-advanced)** - official exam page: format, cost, version, registration
- **[📖 Exam objectives (review guide)](https://developer.hashicorp.com/terraform/tutorials/pro-cert/adv-review)** - the six objectives and sub-objectives, with links to docs and tutorials
- **[📖 Exam orientation](https://developer.hashicorp.com/terraform/tutorials/pro-cert/adv-orientation)** - what the lab environment looks like and which resources are available during the exam
- **[📖 Learning path](https://developer.hashicorp.com/terraform/tutorials/pro-cert/adv-study)** - HashiCorp's suggested study tutorials
- **[📖 Terraform language documentation](https://developer.hashicorp.com/terraform/language)** - the reference you will also have in the exam
- **[📖 Terraform CLI documentation](https://developer.hashicorp.com/terraform/cli)** - every command and option
- **[📖 HCP Terraform documentation](https://developer.hashicorp.com/terraform/cloud-docs)** - workspaces, runs, permissions and policy

## Recertification

The credential is valid for 2 years. You renew by passing the current version of the exam, and you can take either the AWS or the Azure version to renew, whichever you sat originally.

## Common Pitfalls to Avoid

- **Studying on the newest Terraform.** The exam tests 1.6. Practice on 1.6 so the environment never surprises you.
- **Treating it as multiple choice.** Only part of it is. Labs need you to produce working configuration and correct state.
- **Leaving pending changes.** After each lab task, run `terraform plan` and confirm the end state the task asked for.
- **Skipping HCP Terraform because it is "only" multiple choice.** Objective 6 still needs a solid grasp of runs, workspaces, permissions, credentials and policy.
- **Guessing import ID formats and argument names.** You have the docs in the exam; get used to finding things in them fast.

## Time Investment Estimate

This guide's estimate, not HashiCorp's: with a year or more of production Terraform, 40 to 60 hours of focused prep, most of it in labs; with less, 80 to 120 hours. See [practice-plan.md](./practice-plan.md) for the schedule.
