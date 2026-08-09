---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 8 min
---

# 02 - GitOps terminology

**Domain 2: GitOps Terminology (20%)**

The exam is literal about vocabulary, and the OpenGitOps glossary is the reference.

---

## Core objects

| Term | Definition |
|---|---|
| **State store** | The system holding desired state, satisfying versioning and immutability. Commonly Git |
| **Desired state** | The declarative configuration describing what the system should be |
| **Actual state** | The current running configuration of the managed system |
| **Managed system** | The environment being reconciled, commonly a Kubernetes cluster but not necessarily |
| **Agent** | Software running in or adjacent to the managed system that pulls and reconciles |
| **Reconciler** | The component computing and applying the difference between desired and actual state |

---

## Process terms

| Term | Definition |
|---|---|
| **Reconciliation** | The process of observing actual state and attempting to make it match desired state |
| **Convergence** | Actual state moving toward desired state over one or more reconciliations |
| **Divergence** or **drift** | A state where actual differs from desired |
| **Drift detection** | Identifying that divergence exists |
| **Self-healing** | Automatically correcting drift by reapplying desired state |
| **Sync** | An agent-specific term for one reconciliation pass |
| **Rollback** | Returning to a previous desired state by changing the state store |

**Rollback deserves emphasis.** In GitOps, rollback is a change to the state store, usually a revert commit. It is not an imperative operation against the cluster, because any such operation is drift that the next reconciliation removes.

---

## Delivery terms

| Term | Definition |
|---|---|
| **Continuous integration** | Automatically building and testing changes as they are merged |
| **Continuous delivery** | Keeping software in a releasable state, with release requiring a human decision |
| **Continuous deployment** | Automatically releasing every change that passes the pipeline |
| **Promotion** | Moving a version from one environment to the next |
| **Environment** | A distinct instance of the system, such as dev, staging, or production |
| **Release** | A specific version made available in an environment |

GitOps is a **continuous delivery** approach. It does not require continuous deployment; whether production updates automatically is a policy choice expressed in the state store's approval process.

---

## Repository terms

| Term | Definition |
|---|---|
| **Application repository** | Where source code lives, and where CI builds from |
| **Configuration repository** (or environment repository) | Where deployment manifests live, and what the agent reads |
| **Monorepo** | One repository holding many components |
| **Polyrepo** | Many repositories, typically one per component |
| **Base** | Shared configuration common to all environments |
| **Overlay** | Environment-specific configuration layered onto a base |

Separating application and configuration repositories is the recommended pattern: different change cadence, different reviewers, and no CI loop where a pipeline commits to the repository that triggers it.

---

## Precision the exam tests

- **A state store is not necessarily Git.** The principles require versioning and immutability, which Git provides and other systems can too.
- **GitOps is not a tool.** Argo CD and Flux are implementations of an approach.
- **Continuous reconciliation is not the same as self-healing.** Reconciliation observes and attempts to apply; whether it corrects automatically is configurable, and legitimate designs alert instead for some resources.
- **Drift is not always a fault.** It is a divergence, and sometimes the desired state is what is wrong.
- **A pull request is not part of the principles.** Review is a widely used practice around GitOps, not a principle of it.

---

## Key terms

- **State store** - the versioned, immutable system of record for desired state
- **Managed system** - the environment an agent reconciles toward desired state
- **Reconciler** - the component computing and applying the difference between desired and actual state
- **Sync** - one reconciliation pass performed by an agent
- **Self-healing** - automatic correction of drift by reapplying desired state
- **Drift detection** - identifying that actual state has diverged from desired state
- **Rollback** - returning to a previous desired state by changing the state store rather than the running system
- **Continuous delivery** - keeping software releasable, with the release decision made by a human
- **Continuous deployment** - releasing every change that passes automated checks, with no human gate
- **Promotion** - moving a validated version from one environment to the next
- **Application repository** - the repository holding source code, built by CI
- **Configuration repository** - the repository holding deployment manifests, read by the GitOps agent
- **Base and overlay** - the pattern of shared configuration plus environment-specific layers

---

## Related

- [Notes 03: GitOps patterns](./03-gitops-patterns.md)
- [Scenarios](../scenarios.md) - scenarios 5 and 6
