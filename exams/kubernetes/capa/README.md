---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 5 min
---

# Certified Argo Project Associate (CAPA)

Four projects, one exam: Argo Workflows, Argo CD, Argo Rollouts, and Argo Events.

The most common preparation mistake is treating this as an Argo CD certification. **Argo Workflows is the largest domain at 36%**, slightly ahead of Argo CD at 34%. Together, Rollouts and Events are another 30%.

## Exam Details

- **Exam Code:** CAPA
- **Duration:** 90 minutes
- **Questions:** 60, multiple choice and multiple select
- **Passing Score:** 75%
- **Cost:** USD 250, includes one free retake
- **Validity:** 2 years
- **Prerequisites:** None formal; Kubernetes fundamentals assumed
- **Format:** Knowledge-based, not hands-on

Full detail in the [fact sheet](./fact-sheet.md).

## Domains

| Domain | Weight | Notes |
|--------|-------:|-------|
| Argo Workflows | 36% | [01](./notes/01-argo-workflows.md) |
| Argo CD | 34% | [02](./notes/02-argo-cd.md) |
| Argo Rollouts | 18% | [03](./notes/03-argo-rollouts.md) |
| Argo Events | 12% | [04](./notes/04-argo-events.md) |

## How the four relate

They are independent projects that compose well:

- **Argo Events** detects that something happened and triggers **Argo Workflows**
- **Argo Workflows** runs the pipeline and commits an image tag
- **Argo CD** notices the commit and syncs the cluster
- **Argo CD** manages a **Rollout** resource, which performs the progressive release

You can run any one of them alone. The exam tests each separately, then occasionally tests where the boundary between them lies.

## Study sequence

1. **Argo Workflows** first, because it is the largest domain and the least familiar to most candidates.
2. **Argo CD** second. If you have used it, this is your fastest domain.
3. **Argo Rollouts**, focusing on canary steps and analysis.
4. **Argo Events**, which is small and mostly structural.

Schedule in the [practice plan](./practice-plan.md).

## Hands-on

All four install on a kind cluster in minutes. Worth building:

- A Workflow with a DAG, parameters passed between steps, and an artifact stored in MinIO
- A CronWorkflow with a TTL strategy, then check that pods are garbage collected
- An Argo CD Application with automated sync, prune, and self-heal, then cause drift
- An ApplicationSet with a list generator producing three Applications
- A Rollout with a canary strategy and a Prometheus AnalysisTemplate that fails, so you see automatic rollback
- A webhook EventSource and a Sensor that triggers a Workflow

## Study resources

- **[📖 Argo Workflows documentation](https://argo-workflows.readthedocs.io/)** - the largest domain
- **[📖 Argo CD documentation](https://argo-cd.readthedocs.io/)**
- **[📖 Argo Rollouts documentation](https://argo-rollouts.readthedocs.io/)**
- **[📖 Argo Events documentation](https://argoproj.github.io/argo-events/)**
- **[📖 CAPA curriculum](https://github.com/cncf/curriculum)** - published domains
- [Practice questions](../../../resources/practice-questions/cncf-capa.md) - question bank in this repo

## Related

- [CGOA](../cgoa/) - the GitOps principles underneath Argo CD
- [CKA](../cka/) - assumed Kubernetes knowledge
- [CNPA](../cnpa/) - the platform engineering layer
- [OTCA](../otca/) - the observability that Rollouts analysis depends on
- [Build a CI/CD pipeline](../../../resources/hands-on-projects/build-ci-cd-pipeline.md)
