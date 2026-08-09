---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 10 min
---

# 01 - GitOps principles

**Domain 1: GitOps Principles (30%)**

The largest domain. The OpenGitOps project defines four principles, and the exam uses their exact wording.

---

## The four principles

> **1. Declarative** - A system managed by GitOps must have its desired state expressed declaratively.
>
> **2. Versioned and Immutable** - Desired state is stored in a way that enforces immutability, versioning, and retains a complete version history.
>
> **3. Pulled Automatically** - Software agents automatically pull the desired state declarations from the source.
>
> **4. Continuously Reconciled** - Software agents continuously observe actual system state and attempt to apply the desired state.

Notice what is absent: Git, Kubernetes, and any named tool. The state store is usually Git and the target is usually Kubernetes, but the principles are deliberately broader, and the exam tests whether you know the difference between the principle and the common implementation.

---

## Principle 1: Declarative

Describe **what** the system should look like, not **how** to get there.

```yaml
# Declarative: this is the desired state
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 3
```

```bash
# Imperative: these are steps, and they encode assumptions about current state
kubectl scale deployment api --replicas=3
```

Why it matters: a declarative description is **idempotent** and **comparable**. Applying it twice has the same effect as applying it once, and you can diff it against reality to detect drift. Neither property holds for a script.

Templating (Helm, Kustomize, jsonnet) does not violate this principle. The rendered output is still declarative; templating is how you avoid repeating it.

---

## Principle 2: Versioned and immutable

The state store must retain complete history, and stored states must be immutable.

- **Versioned** gives you a history, an audit trail, and a well-defined thing to revert to.
- **Immutable** means a given version cannot be changed after the fact. A Git commit SHA identifies exact content forever.

Why a plain object storage bucket is a weak state store: overwrite a file and the previous state is gone, so you cannot revert or audit. Add versioning and object lock and it starts to satisfy the principle.

This principle is why mutable image tags such as `latest` are discouraged. `myapp:latest` does not identify content, so the same desired state can produce two different running systems.

---

## Principle 3: Pulled automatically

An **agent** inside the managed environment pulls desired state from the store. Nothing outside pushes into the environment.

The security consequence is the strongest practical argument for GitOps:

| | Push model | Pull model |
|---|---|---|
| Who holds cluster credentials | The CI system, outside the cluster | Nobody outside; the agent uses in-cluster identity |
| Inbound network access to the cluster | Required from CI | Not required |
| Blast radius of a compromised CI system | Full cluster access | Ability to propose a change, subject to review |

A compromised CI system in a push model can do anything to production. In a pull model it can push a commit, which is reviewable and revertable.

---

## Principle 4: Continuously reconciled

The agent runs a loop: read desired state, observe actual state, compute the difference, act.

This runs **continuously**, not only when someone commits. That is what distinguishes GitOps from deploy-time automation. If an engineer runs `kubectl edit` at 3am, the next reconciliation notices.

Note the exact wording: agents "observe actual system state and **attempt to apply** the desired state". It does not mandate automatic correction of everything. Organizations legitimately configure some resources to alert on drift rather than auto-correct, and some fields to be excluded entirely because another controller owns them.

---

## Desired state, actual state, and drift

- **Desired state** - what the state store says the system should be.
- **Actual state** - what the system is.
- **Drift** - a difference between them.
- **Convergence** - the process of actual state moving toward desired state.
- **Reconciliation** - the loop that drives convergence.

Drift causes: manual changes, out-of-band automation, another controller mutating a field, an operator's defaulting behavior, or a failed apply.

Not all drift is bad. An HPA changing replica count is drift against a manifest that declares replicas, and the correct fix is to stop declaring that field, not to fight the HPA.

---

## Why automation alone is not GitOps

A pipeline that runs `kubectl apply` on merge is:
- Declarative ✓
- Versioned ✓
- **Pushed, not pulled** ✗
- **Not continuously reconciled** ✗

It is good automation. It is not GitOps, and the difference is operational: drift between deployments is invisible, and the credentials to change production live in a system outside production.

This comparison is the single most reliable source of exam questions.

---

## Key terms

- **Declarative configuration** - a description of desired end state rather than the steps to reach it
- **Idempotency** - the property that applying an operation repeatedly has the same effect as applying it once
- **State store** - the versioned, immutable system holding desired state, commonly but not necessarily Git
- **Immutability** - the property that a stored version cannot be altered after it is created
- **Agent** - the software running inside the managed environment that pulls desired state and reconciles it
- **Pull model** - delivery where an in-environment agent fetches desired state, requiring no external credentials
- **Push model** - delivery where an external system authenticates into the environment and applies changes
- **Reconciliation loop** - the continuous cycle of reading desired state, observing actual state, and acting on the difference
- **Desired state** - the configuration the state store declares the system should have
- **Actual state** - the configuration the system currently has
- **Drift** - a divergence between actual state and desired state
- **Convergence** - the movement of actual state toward desired state through reconciliation

---

## Related

- [Notes 02: GitOps terminology](./02-gitops-terminology.md)
- [Scenarios](../scenarios.md) - scenario 1
- [CI/CD explained](../../../../learn/concepts/cicd-explained.md)
- [Idempotency explained](../../../../learn/concepts/idempotency-explained.md)
