---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 5 min
---

# CGOA Study Strategy

## Study the principles, not the tool

The commonest preparation mistake is learning Argo CD and assuming that is GitOps knowledge. Tooling is 14% of the exam. Principles, terminology, and patterns are 70%.

Read [opengitops.dev](https://opengitops.dev/) directly. It is short, and the exam uses its exact vocabulary. Third-party blog definitions of GitOps drift from the official ones, often by adding "Git" or "Kubernetes" as requirements that the principles deliberately do not impose.

## The trap questions

Nearly every CGOA question set contains variants of these. Learn to spot the shape.

**"Is this GitOps?"** A scenario describes a workflow, and you decide whether it satisfies the principles. Check all four:

| Symptom in the scenario | Principle violated |
|---|---|
| A pipeline runs `kubectl apply` after merge | Pulled automatically (3) |
| Nothing happens between deployments; drift persists | Continuously reconciled (4) |
| Engineers run scripts to configure the cluster | Declarative (1) |
| State is in a mutable bucket with no history | Versioned and immutable (2) |
| Rollback means re-running an old pipeline | Not a violation on its own, but a strong hint the model is push-based |

**"What does GitOps require?"** The answer is usually narrower than candidates expect. GitOps does not require Git, does not require Kubernetes, does not require a specific tool, and does not require automatic self-healing (continuous reconciliation means observing and attempting to apply, and an organization may choose to alert rather than auto-correct for some resources).

**"Which term is this?"** The exam is literal about vocabulary. Drift, divergence, convergence, reconciliation, desired state, actual state, and state store all have precise definitions in the glossary.

## Phase 1: Principles (week 1)

Learn the four principles as written, then go deeper than the wording:

- **Declarative** rules out imperative scripts, but note that a declarative description can still be templated (Helm, Kustomize) before it is applied.
- **Versioned and immutable** is why a mutable S3 bucket without versioning is a poor state store, and why a Git commit SHA is a good one.
- **Pulled automatically** is the security argument: the agent runs inside the target environment and needs no inbound access, so no external system holds cluster credentials.
- **Continuously reconciled** is what distinguishes GitOps from deploy-time automation. The loop runs whether or not anyone committed.

## Phase 2: Patterns (week 2-3)

The design questions concentrate here.

**Repository strategy**: separate the application source repository from the deployment configuration repository. This avoids the CI loop where a pipeline commits an image tag back into the repository that triggers the pipeline, and it lets the two have different access controls.

**Environments**: directory per environment is generally preferred over branch per environment, because branches drift, merges between them become confusing, and promotion becomes a merge conflict exercise rather than a deliberate change.

**Secrets** must never sit in plaintext in the state store. Three families of answer:
- **Encrypt in the repo**: SOPS, Sealed Secrets. The encrypted value is committed; only the cluster can decrypt.
- **Reference from the repo**: External Secrets Operator pulling from Vault, AWS Secrets Manager, Azure Key Vault, or GCP Secret Manager. The repo holds a reference, never a value.
- **Inject at runtime**: a sidecar or CSI driver mounting from an external store.

**Drift policy** is a design decision, not a default. Automatic self-heal is right for most application configuration and wrong where a legitimate external controller changes the resource, such as HPA-managed replica counts. The usual answers are to exclude those fields from comparison, or to not manage them declaratively.

## Phase 3: Related practices and tooling (week 4)

Breadth, not depth. Know what each tool is for and roughly how it differs from its alternative. You will not be asked for YAML.

The one boundary worth being clear on: **CI builds and tests and produces an artifact; GitOps delivers it.** The handover is usually an automated commit updating an image tag in the config repository, or an image-updating controller watching the registry.

## Common traps

| Trap | Reality |
|---|---|
| "GitOps requires Git" | The principles say a versioned, immutable state store. Git is the common choice, not a requirement |
| "GitOps requires Kubernetes" | The principles are target-agnostic |
| "GitOps replaces CI" | It replaces the CD half. CI still builds and tests |
| "Self-heal must always be on" | Continuous reconciliation means observe and attempt; alerting is a valid policy for some resources |
| "Branch per environment is the standard" | Directory per environment is the more common recommendation |
| "Encrypted secrets in the repo are forbidden" | Encrypted values are fine; plaintext is not |
| "Push-based delivery can be GitOps if the manifests are in Git" | Violates the pull principle regardless of where manifests live |

## Exam day

- 90 minutes for 60 questions.
- Concept exam: no terminal, no YAML authoring.
- Multiple-select questions state how many to pick.
- 75% pass, so roughly 45 of 60.
- One free retake included.

## Related

- [Practice plan](./practice-plan.md)
- [Scenarios](./scenarios.md)
- [Fact sheet](./fact-sheet.md)
- [CI/CD explained](../../../learn/concepts/cicd-explained.md)
