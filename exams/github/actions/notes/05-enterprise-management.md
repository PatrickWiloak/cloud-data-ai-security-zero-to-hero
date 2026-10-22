---
last-updated: 2026-10-22
applies-to: GH-200 skills measured as of January 2026, checked 2026-10-22
difficulty: intermediate
---

# Domain 4: Manage GitHub Actions for the Enterprise (20-25%)

The January 2026 rewrite raised this domain to joint-largest. It covers three skill groups: distribute and govern actions and workflows, manage runners at scale, and manage encrypted secrets and variables. Security controls that used to sit here (OIDC, SHA pinning, attestations) moved to their own domain, covered in [06-secure-and-optimize.md](06-secure-and-optimize.md).

**[📖 GH-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200)** - the skills list this note follows.
**[📖 Enforcing policies for GitHub Actions in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)** - every enterprise Actions policy.
**[📖 Self-hosted runners](https://docs.github.com/en/actions/concepts/runners/self-hosted-runners)** - concepts, security and management.

## The policy layers

GitHub settings cascade: **enterprise > organization > repository**. A higher level can set a policy and lock it, in which case lower levels see it greyed out; or it can leave the choice to the level below. When an exam question asks "where do you set X so that every repository gets it and nobody can change it", the answer is the highest level that owns all the affected repositories, with the policy enforced rather than left as a default.

## Distribute and govern actions and workflows

### Reusable components and templates

A platform team usually publishes three things from central repositories:

- **Reusable workflows** for whole pipelines (build, scan, deploy), versioned with tags and called with `uses: org/platform/.github/workflows/deploy.yml@v3`.
- **Composite and JavaScript actions** for repeated steps (toolchain setup, registry login).
- **Workflow templates** in the organization's `.github` repository so new repositories start from an approved pattern.

Governance comes from versioning those repositories like products (release notes, major tags, deprecation windows), keeping them in internal repositories visible to the whole enterprise, and pointing teams at them through templates rather than copy-paste.

### Controlling access to actions and workflows

Private and internal repositories keep their actions and reusable workflows to themselves by default. In the action's repository, **Settings > Actions > General > Access** chooses who can use them:

- **Not accessible** - only this repository.
- **Accessible from repositories in the organization** - any repository in the same organization.
- **Accessible from repositories in the enterprise** - any repository in the enterprise (internal repositories only).

### Organizational use policies

At enterprise and organization level, the **Policies** section of Actions settings controls what may run:

- **Which repositories may use Actions at all** - all, selected, or none (disables Actions).
- **Which actions and reusable workflows are allowed** - all; only those from the enterprise; those from the enterprise plus actions created by GitHub and/or Marketplace verified creators; or an explicit allow list of patterns such as `my-org/*`, `actions/checkout@*` or a specific SHA. Patterns can also block actions with a leading `!`.
- **Require actions to be pinned to a full-length commit SHA** - a newer option that makes tag references fail.
- **Fork pull request workflows** - whether runs from forks need approval (first-time contributors, all outside collaborators), whether private-repository forks may run workflows, send write tokens or send secrets.
- **Workflow permissions** - the default `GITHUB_TOKEN` permission set (read and write, or read-only for `contents` and `packages`), and whether Actions may create or approve pull requests.
- **Artifact and log retention** and **cache size** limits.

Exam pattern: "allow only actions from our organization and actions created by GitHub" maps to the "allow enterprise, and select non-enterprise, actions" option with "Allow actions created by GitHub" ticked, set at organization or enterprise level.

**[📖 Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository)** - the same options at repository level, including Access for private actions.

## Manage runners at scale

### GitHub-hosted runners

GitHub-hosted runners are fresh virtual machines, discarded after each job, on Ubuntu, Windows and macOS (x64 and Arm64 variants). Standard runners come with the plan's included minutes. **Larger runners** (more CPU, RAM, GPU options, Arm) are available on Team and Enterprise Cloud plans; they are billed per minute and can have **static public IP addresses** and, on Enterprise Cloud with Azure, **Azure private networking** so jobs reach private resources without exposing them to the internet. Larger runners are managed in runner groups like self-hosted ones.

### Self-hosted runners

A self-hosted runner is the open-source runner application installed on your own machine, VM or container. You register it at repository, organization or enterprise level with a registration token, give it labels, and it polls GitHub over HTTPS for jobs (outbound only, no inbound ports). Choose self-hosted runners for network access to private systems, special hardware (GPU, ARM boards, large disks), preinstalled licensed software, or cost control at very high volume.

Operational facts:

- **Labels** - every runner gets `self-hosted`, an OS label and an architecture label; add custom labels such as `gpu` or `prod-vpc`. A job with `runs-on: [self-hosted, linux, gpu]` needs a runner with **all** the labels.
- **Ephemeral runners** - register with `--ephemeral` so the runner takes one job and then unregisters. Combined with autoscaling, this gives every job a clean machine, which is the secure default.
- **Autoscaling** - **Actions Runner Controller (ARC)** runs runner scale sets on Kubernetes, creating a pod per job from the queue and scaling to zero. Webhook-driven autoscalers on VMs follow the same idea.
- **Updates** - runners auto-update by default; a runner too far behind the minimum version stops receiving jobs. If you disable auto-update in a container image, you must rebuild the image on each release.
- **Status** - Idle, Active or Offline in the runners list; a runner that has not connected for 14 days is removed automatically (ephemeral ones after a day).

### Networking and IP allow lists

Two separate questions hide behind "networking":

1. **Can the runner reach GitHub?** Self-hosted runners need outbound HTTPS to `github.com`, `api.github.com`, `*.actions.githubusercontent.com`, the artifact and cache storage hosts, `pkg.actions.githubusercontent.com` for immutable actions, and `ghcr.io` for container-based actions. A proxy can be set with `https_proxy` and `no_proxy`.
2. **Can the runner reach your systems, and can GitHub reach it?** If your organization or enterprise uses an **IP allow list** (Enterprise Cloud), only listed source addresses can access its resources, including API calls and git operations from runners. Standard GitHub-hosted runners use large shared Azure ranges that change, so they will be blocked. Fixes: use self-hosted runners whose egress IPs you add to the list, use larger runners with static IPs, or enable the setting that automatically adds IP addresses of installed GitHub Apps.

**[📖 Managing allowed IP addresses for your organization](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)** - how the allow list affects Actions.
**[📖 Communication between self-hosted runners and GitHub](https://docs.github.com/en/actions/reference/runners/self-hosted-runners#communication-between-self-hosted-runners-and-github)** - required hosts.

### Runner groups

Runner groups decide **who may use which runners**. At organization level a group can be shared with all repositories or selected ones, and can be restricted to selected workflows (for example only `org/platform/.github/workflows/deploy.yml@refs/heads/main`). At enterprise level a group is shared with selected organizations. New runners land in the **Default** group unless you pick another, and each runner belongs to exactly one group. A job targets a group with `runs-on: { group: prod-runners, labels: [linux] }`.

Typical design: a "public" group of ephemeral runners for untrusted code, a "prod" group limited to the deploy workflow in the platform repository, and a "gpu" group shared with the ML organization only.

### Troubleshooting runners

| Symptom | Check |
|---|---|
| Job stuck in "Queued" / "Waiting for a runner" | No online runner has all the requested labels; the group does not include the repository or workflow; all matching runners busy |
| Runner shows Offline | Service stopped, machine down, network or proxy blocking outbound HTTPS, expired registration |
| Job fails at "Set up job" downloading actions | Allow list or proxy blocks action download hosts |
| Disk full or leftover files between jobs | Persistent (non-ephemeral) runner; clean the workspace or move to ephemeral runners |
| Works on hosted runner, fails on self-hosted | Missing tools that the hosted image preinstalls |

Runner diagnostic logs live in the runner's `_diag` folder, and setting `ACTIONS_RUNNER_DEBUG=true` adds runner logs to the run.

### Preinstalled software and installing more

Each GitHub-hosted image ships hundreds of tools: language runtimes, package managers, cloud CLIs, browsers, Docker. The exact versions are listed in the image's README and release notes in the `actions/runner-images` repository, and the "Set up job" step of every run names the image version used. Several versions of popular runtimes are kept in the **tool cache** (`runner.tool_cache`), which `setup-*` actions use to switch versions instantly.

When something is missing or the wrong version, the options in order of preference are:

1. A **`setup-*` action** (`actions/setup-node`, `setup-python`, `setup-java`, `setup-go`, `setup-dotnet`) with a pinned version and built-in dependency caching.
2. The OS **package manager** (`sudo apt-get install`, `choco`, `brew`) at run time, cached where possible.
3. A **job container** (`container: image:`) that already has the toolchain.
4. A **custom image**: on self-hosted runners, bake tools into your VM or container image; larger GitHub-hosted runners also support custom images.

Do not rely on a tool being present on `-latest` images forever; images drop old versions on a published schedule.

**[📖 GitHub-hosted runners reference](https://docs.github.com/en/actions/reference/runners/github-hosted-runners)** - labels, hardware and preinstalled software.

## Manage encrypted secrets and variables

### Scopes and precedence

Secrets (encrypted, masked in logs, write-only once saved) and variables (plain configuration, readable) exist at three levels:

| Level | Who can use it | Notes |
|---|---|---|
| Organization | All, private and internal, or selected repositories | Set once, shared; repository access policy per secret |
| Repository | Every workflow in the repository | Not passed to workflows triggered from forks |
| Environment | Jobs that reference the environment | Released only after protection rules pass |

When the same name exists at several levels, the **most specific wins**: environment over repository over organization. Enterprise-level variables and secrets exist only in limited forms, so in exam answers "share with many repositories" usually means organization secrets with selected-repository access.

Limits worth knowing: names may contain only letters, numbers and underscores, cannot start with `GITHUB_` or a number, and are not case-sensitive; a secret value can be up to 48 KB; an organization can hold up to 1,000 secrets and a repository 100. Dependabot and Codespaces have their own separate secret stores.

### Using them in workflows and actions

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production         # unlocks production secrets and vars
    steps:
      - run: ./deploy.sh --region "$REGION"
        env:
          REGION: ${{ vars.AWS_REGION }}
          API_KEY: ${{ secrets.DEPLOY_API_KEY }}
```

Actions never read secrets automatically: a workflow passes them as inputs (`with:`) or environment variables. A reusable workflow gets them only through `secrets:` mapping or `secrets: inherit`. Fork pull requests receive no secrets except a read-only `GITHUB_TOKEN`.

### Managing them programmatically

Secrets are encrypted on the client with the repository's or organization's **public key** (libsodium sealed box) before they are sent, so the REST flow is: fetch the public key, encrypt, then `PUT` the encrypted value with the key ID. The GitHub CLI does the encryption for you:

```bash
# Repository secret and variable
gh secret set DEPLOY_API_KEY --repo OWNER/REPO < key.txt
gh variable set AWS_REGION --repo OWNER/REPO --body us-east-1

# Organization secret shared with selected repositories
gh secret set NPM_TOKEN --org OWNER --visibility selected --repos "api,web"

# Environment secret
gh secret set DB_PASSWORD --repo OWNER/REPO --env production

# REST: get the public key used to encrypt a repository secret
gh api repos/OWNER/REPO/actions/secrets/public-key
```

Rotation, bulk changes and audits are scripted this way. Secret values can never be read back through the API or UI; only names and update dates are listed.

**[📖 Using secrets in GitHub Actions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets)** - creating, scoping and using secrets.
**[📖 REST API endpoints for GitHub Actions secrets](https://docs.github.com/en/rest/actions/secrets)** - public keys and encrypted values.
**[📖 REST API endpoints for GitHub Actions variables](https://docs.github.com/en/rest/actions/variables)** - repository, organization and environment variables.

## Auditing and usage

Actions events (runner registration, policy changes, secret creation and updates, workflow runs) appear in the organization and enterprise **audit log**, searchable in the UI, available through the API, and streamable to a SIEM on Enterprise Cloud. Usage and billing reports show minutes by runner type and storage for artifacts and caches; macOS and Windows minutes cost more than Linux, and larger runners are billed per minute at higher rates. Budgets can cap spending so a runaway workflow cannot run up costs.

## Key terms

- **Policy inheritance** - enterprise settings constrain organizations, which constrain repositories.
- **Allowed actions policy** - the setting that restricts which actions and reusable workflows may run.
- **Access setting** - the option on a private or internal repository that lets other repositories use its actions and reusable workflows.
- **Self-hosted runner** - the runner application on your own infrastructure, polling GitHub for jobs.
- **Ephemeral runner** - a self-hosted runner that runs one job and then unregisters.
- **Actions Runner Controller (ARC)** - Kubernetes operator that autoscales runner scale sets.
- **Runner group** - a set of runners shared with selected repositories, organizations or workflows.
- **Larger runner** - a GitHub-hosted runner with more resources, optional static IPs and private networking.
- **IP allow list** - an Enterprise Cloud control that only accepts traffic from listed addresses.
- **Tool cache** - preinstalled runtime versions on hosted runners that `setup-*` actions switch between.
- **Environment secret** - a secret released only to jobs in that environment after its protection rules pass.
- **Secret precedence** - environment over repository over organization when names collide.
