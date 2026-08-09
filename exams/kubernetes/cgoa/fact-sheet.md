---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 10 min
---

# Certified GitOps Associate (CGOA) Fact Sheet

## Exam Overview

**Exam Code:** CGOA
**Exam Name:** Certified GitOps Associate
**Level:** Associate
**Duration:** 90 minutes
**Format:** Multiple choice and multiple select, online proctored
**Questions:** 60
**Passing Score:** 75%
**Cost:** USD 250 (includes one free retake)
**Valid For:** 2 years
**Delivery:** Online proctored through PSI
**Prerequisites:** None

> **Verify before booking.** CNCF exam details and curriculum versions change. Confirm on the official pages below.

**[📖 CGOA certification page](https://www.cncf.io/training/certification/cgoa/)** - registration and curriculum
**[📖 Linux Foundation CGOA page](https://training.linuxfoundation.org/certification/certified-gitops-associate-cgoa/)** - logistics and candidate handbook
**[📖 OpenGitOps principles](https://opengitops.dev/)** - the four principles the exam is built on
**[📖 CNCF curriculum repository](https://github.com/cncf/curriculum)** - published exam domains

## What kind of exam this is

CGOA is **vendor-neutral and concept-heavy**. It is not an Argo CD or Flux certification. Roughly 70% of the exam is principles, terminology, and patterns, with tooling only 14%.

That surprises people who prepare by learning Argo CD. The exam wants to know whether you can say precisely what makes a deployment approach GitOps rather than merely automated, and where the boundaries of the model are.

The vocabulary is standardized by the **OpenGitOps** project, and the exam uses its definitions literally.

## Target Audience

- Platform and DevOps engineers adopting GitOps
- SREs responsible for deployment reliability
- Anyone running Argo CD or Flux who wants the conceptual grounding
- Kubernetes practitioners extending [CKA](../cka/) or [KCNA](../kcna/) knowledge into delivery

## Exam Domains

### Domain 1: GitOps Principles (30%)

The largest domain. The four OpenGitOps principles, in detail.

**Key Concepts:**
- **Declarative**: the system is described entirely by declarative configuration, not by scripts or imperative commands
- **Versioned and immutable**: desired state is stored so that it is immutable, versioned, and retains a complete version history
- **Pulled automatically**: software agents automatically pull the desired state from the source
- **Continuously reconciled**: agents continuously observe actual state and attempt to apply the desired state
- Why each principle exists and what breaks without it
- Desired state versus actual state, and drift
- Reconciliation loops and convergence
- Idempotency and its role in safe repeated application
- The distinction between GitOps and general CI/CD automation

**[📖 OpenGitOps principles v1.0.0](https://opengitops.dev/)** - the canonical wording

### Domain 2: GitOps Terminology (20%)

The exam is precise about words.

**Key Concepts:**
- **State store**: the system holding desired state (commonly Git, but the principles do not require Git specifically)
- **Desired state, actual state, drift, divergence, convergence**
- **Reconciliation** and the reconciliation loop
- **Agent** and the control plane
- **Rollback** as reverting the state store, not as a separate imperative action
- **Pull versus push** deployment models
- **Immutability** and content addressing
- **Continuous delivery versus continuous deployment**
- **Environment**, **promotion**, and **release**
- Definitions from the OpenGitOps glossary, which the exam follows closely

### Domain 3: GitOps Patterns (20%)

**Key Concepts:**
- Repository strategies: monorepo, polyrepo, and separating application source from deployment configuration
- The **separate config repository** pattern and why it is preferred over committing to the app repo
- Environment modeling: branch per environment versus directory per environment, and the trade-offs
- Promotion between environments, including automated and gated promotion
- Configuration templating and overlays: Kustomize bases and overlays, Helm charts and values
- Secret management in a public state store: sealed secrets, external secret operators, and SOPS
- Progressive delivery: blue-green, canary, and their relationship to GitOps
- Drift detection and remediation policy: alert only, or automatically revert
- Multi-cluster and multi-tenant patterns, including hub-and-spoke
- Handling resources that legitimately change outside Git, such as autoscaled replica counts

### Domain 4: Related Practices (16%)

**Key Concepts:**
- CI versus CD, and where GitOps sits (it is a CD approach; CI still builds and tests)
- Infrastructure as Code and its relationship to GitOps
- Configuration as Code and policy as code
- DevOps and SRE practice alignment
- Observability of the delivery process itself
- Compliance and audit benefits: the state store as an audit log
- Security: least privilege for agents, signed commits, provenance, and admission control
- DORA metrics and how GitOps affects them

### Domain 5: Tooling (14%)

Smallest domain, and deliberately shallow.

**Key Concepts:**
- **Argo CD** and **Flux** as the two CNCF GitOps agents, and their broad architectural differences
- Manifest tooling: Kustomize, Helm, jsonnet
- Policy engines: OPA Gatekeeper, Kyverno
- Progressive delivery controllers: Argo Rollouts, Flagger
- Secret tooling: Sealed Secrets, External Secrets Operator, SOPS
- The GitOps Working Group and the CNCF landscape position of each

## GitOps versus traditional CD

| | Traditional push CD | GitOps |
|---|---|---|
| Trigger | Pipeline runs and pushes to the cluster | Agent pulls from the state store |
| Credentials | Pipeline holds cluster credentials | Agent runs in the cluster; no external cluster credentials |
| Drift | Undetected until the next deploy | Continuously detected and optionally corrected |
| Rollback | Re-run a previous pipeline | Revert the commit |
| Audit | Pipeline logs | The state store history is the audit trail |
| Source of truth | Whatever ran last | The state store, always |

## Related repo material

- [Notes](./notes/) - four notes covering the five domains
- [Practice plan](./practice-plan.md) - 4-week schedule
- [Scenarios](./scenarios.md)
- [Strategy](./strategy.md)
- [CAPA Certified Argo Project Associate](../capa/) - the Argo-specific counterpart
- [CI/CD explained](../../../learn/concepts/cicd-explained.md)
- [Build a CI/CD pipeline](../../../resources/hands-on-projects/build-ci-cd-pipeline.md)
- [Terraform explained](../../../learn/concepts/terraform-explained.md)
