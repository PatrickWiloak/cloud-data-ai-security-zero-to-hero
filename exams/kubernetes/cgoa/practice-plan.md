---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 4 min
---

# CGOA Study Plan

Four weeks at 4-6 hours per week. This is a concept exam, so reading and reasoning matter more than lab time, though one week of hands-on makes everything concrete.

## Week 1: Principles

- [ ] Read [opengitops.dev](https://opengitops.dev/) end to end, including the principles document
- [ ] Write out the four principles from memory, then check the exact wording
- [ ] For each principle, write down what breaks if you drop it
- [ ] Desired state versus actual state; define drift precisely
- [ ] Reconciliation loops, convergence, and idempotency
- [ ] Articulate why a pipeline running `kubectl apply` is not GitOps
- [ ] Review Notes: `notes/01-gitops-principles.md`

## Week 2: Terminology and patterns

- [ ] Work through the OpenGitOps glossary; define each term in your own words then compare
- [ ] State store, agent, reconciliation, drift, convergence, rollback
- [ ] Pull versus push models and the security consequence of each
- [ ] Repository strategy: monorepo versus polyrepo, app repo versus config repo
- [ ] Environment modeling: branch per environment versus directory per environment, and why directories are usually preferred
- [ ] Promotion between environments, gated and automated
- [ ] Kustomize overlays and Helm values as templating approaches
- [ ] Review Notes: `notes/02-gitops-terminology.md` and `notes/03-gitops-patterns.md`

## Week 3: Secrets, drift, multi-cluster, and practices

- [ ] Secret management: Sealed Secrets, External Secrets Operator, SOPS, and their trade-offs
- [ ] Drift remediation policy: detect and alert versus automatic self-heal, and when each is right
- [ ] Resources that legitimately change outside the state store, such as HPA replica counts
- [ ] Multi-cluster and multi-tenancy patterns
- [ ] Progressive delivery: blue-green, canary, and how they coexist with GitOps
- [ ] CI versus CD boundaries; where the image tag update happens
- [ ] Policy as code with OPA Gatekeeper and Kyverno
- [ ] Security: agent least privilege, signed commits, provenance, admission control
- [ ] DORA metrics and the effect of GitOps on each
- [ ] **Lab**: install Argo CD or Flux on kind, sync an app, cause drift, observe self-heal, revert a commit
- [ ] Review Notes: `notes/04-related-practices-and-tooling.md`

## Week 4: Tooling breadth and review

- [ ] Argo CD and Flux: architecture at a high level, not configuration detail
- [ ] Kustomize, Helm, jsonnet: what each is for
- [ ] Argo Rollouts and Flagger for progressive delivery
- [ ] Where each tool sits in the CNCF landscape and its maturity level
- [ ] Work every scenario in [scenarios.md](./scenarios.md)
- [ ] Two timed practice exams
- [ ] Re-read the principles one final time; they are 30% of the exam

## Readiness check

- [ ] Recite the four OpenGitOps principles in the official wording
- [ ] Explain why push-based CD violates two of them
- [ ] Define drift, convergence, and reconciliation without hedging
- [ ] Argue for directory-per-environment over branch-per-environment
- [ ] Explain three ways to keep secrets out of a state store, and their trade-offs
- [ ] Describe when self-heal should be off
- [ ] Explain where CI ends and GitOps begins in a full delivery pipeline
