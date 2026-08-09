---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 11 min
---

# 03 - GitOps patterns

**Domain 3: GitOps Patterns (20%)**

Where the design questions concentrate.

---

## Repository strategy

**Separate the application repository from the configuration repository.**

| | Application repository | Configuration repository |
|---|---|---|
| Contains | Source code, Dockerfile, tests | Manifests, overlays, Helm values |
| Changed by | Developers | Developers and platform, often with different reviewers |
| Read by | CI | The GitOps agent |
| Cadence | Every code change | Every release and configuration change |

Why separate: committing an image tag back into the repository that triggers CI creates a build loop; deployment configuration often needs different access controls from source; and a single application's code may deploy to several environments with distinct approval requirements.

**Monorepo versus polyrepo** for configuration is a scale question. One repository is simpler for tens of services; per-team repositories become necessary when review load or access boundaries demand it.

---

## Environment modeling

| Approach | How it works | Assessment |
|---|---|---|
| **Directory per environment** | `envs/dev/`, `envs/staging/`, `envs/prod/` layered on a shared `base/` | **Recommended.** Differences are visible side by side; promotion is an explicit change; per-directory access control through CODEOWNERS |
| **Branch per environment** | `dev`, `staging`, `main` branches | Intuitive but problematic. Branches diverge, cherry-picking becomes routine, merges carry unintended changes, and configuration differences become permanent conflicts |
| **Repository per environment** | Separate repositories | Strong isolation, heavy duplication, hard to share a base |

Promotion in the directory model is a commit changing an image tag or a values file in the target environment's directory, reviewed according to that environment's rules.

---

## Templating and composition

| Tool | Model |
|---|---|
| **Kustomize** | Patch a base with overlays. No templating language; everything is valid YAML |
| **Helm** | Package a chart with a templating language and per-environment values files |
| **jsonnet** | A data templating language for generating configuration programmatically |

All produce declarative output, so none violates principle 1. Choice is about team preference and ecosystem: Helm for third-party software distribution, Kustomize for in-house configuration variation, and the two are often combined.

---

## Secret management

Plaintext secrets must never enter the state store. Three families:

| Approach | Mechanism | Trade-off |
|---|---|---|
| **Sealed Secrets** | Encrypt with a controller's public key; commit the SealedSecret; only that cluster's controller decrypts | Simple, but keys are cluster-scoped, complicating disaster recovery and multi-cluster |
| **SOPS** | Encrypt values in place with age or a cloud KMS key; the agent decrypts at apply | Works across clusters, needs key access management |
| **External Secrets Operator** | Commit a reference; the operator fetches from Vault, AWS Secrets Manager, Azure Key Vault, or GCP Secret Manager | The value never enters the repository or its history; rotation happens externally. Usually the strongest answer |

Base64 is encoding, not encryption. A `Secret` manifest in a repository is a plaintext credential with extra steps.

---

## Drift policy

Self-healing is a decision per resource, not a global default.

**Enable automatic correction** for application configuration you fully own.

**Do not declare, or exclude from comparison**, fields owned by another legitimate controller:
- `replicas` when an HPA manages scaling
- Fields mutated by admission webhooks or sidecar injectors
- Cloud-assigned load balancer IPs and node ports
- Certificates issued by cert-manager

Declaring a field that another controller owns produces a fight loop: the agent reverts, the controller reapplies, repeatedly. The fix is to stop declaring the field, not to disable reconciliation.

**Alert-only** is a valid policy where a human should decide, typically in tightly regulated production environments during an incident freeze.

---

## Progressive delivery

Blue-green and canary releases coexist with GitOps by moving the rollout logic into a controller that itself is declared in the state store.

- **Argo Rollouts** and **Flagger** replace the Deployment with a custom resource describing the rollout strategy, analysis, and promotion criteria
- The desired state remains declarative: it declares the strategy, not the intermediate steps
- Automated analysis against metrics gates promotion, and failure triggers automatic rollback
- The agent reconciles the rollout resource; the rollout controller handles the traffic shifting

---

## Multi-cluster and multi-tenancy

Patterns for scale:

- **Agent per cluster** pulling from a shared repository, with a directory or generator selecting what that cluster gets
- **Hub cluster** running an agent that manages many clusters, simpler to operate and a larger blast radius
- **Generators** (Argo CD ApplicationSets, Flux Kustomization with variable substitution) rendering one definition across many clusters from cluster metadata
- **Base plus overlay** so the platform baseline is defined once
- **Policy as code** (Kyverno, OPA Gatekeeper) enforcing invariants regardless of what a tenant's manifests request
- **Namespace and RBAC boundaries** giving tenants control of their own directory without access to the platform baseline

---

## Key terms

- **Configuration repository** - the repository the GitOps agent reads, holding deployment manifests separate from source code
- **Directory per environment** - the recommended environment model using a shared base and per-environment overlays
- **Branch per environment** - an environment model using long-lived branches, prone to divergence and accidental promotion
- **Base** - shared configuration common to every environment
- **Overlay** - environment-specific configuration layered onto a base
- **Kustomize** - a template-free tool composing configuration through bases and patch overlays
- **Sealed Secrets** - a controller-based approach encrypting secrets with a cluster-held key so ciphertext can be committed
- **SOPS** - a file-level encryption tool encrypting values in place using age or a cloud KMS key
- **External Secrets Operator** - a controller fetching secret values from an external store so only references are committed
- **Self-heal** - automatic reapplication of desired state when drift is detected
- **Ignore differences** - agent configuration excluding specific fields from drift comparison
- **Progressive delivery** - staged release strategies such as canary and blue-green, gated by automated analysis
- **ApplicationSet** - an Argo CD generator rendering many Applications from one templated definition
- **Policy as code** - enforcing configuration invariants through an admission policy engine such as Kyverno or Gatekeeper

---

## Related

- [Notes 04: related practices and tooling](./04-related-practices-and-tooling.md)
- [Scenarios](../scenarios.md) - scenarios 2, 3, 4, and 7
