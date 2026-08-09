---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 5 min
---

# CAPA Study Strategy

## Do not treat this as an Argo CD exam

Argo Workflows is 36% and Argo CD is 34%. Rollouts and Events add another 30%. Candidates arrive having used Argo CD daily and having never written a Workflow, then study the thing they already know.

Allocate study time by weight, and start with Workflows because it is both the largest domain and the one most candidates have never touched.

## Phase 1: Argo Workflows (week 1-2)

The mental model: a Workflow is a graph of **templates**, each of which runs as a pod. Two kinds of template matter:

- **Work templates** do something: `container`, `script`, `resource`, `suspend`
- **Orchestration templates** call other templates: `steps` (sequential lists, with parallelism inside a list) and `dag` (explicit dependencies)

`steps` is a list of lists: items in the same inner list run in parallel, and the outer lists run in sequence. `dag` declares dependencies per task and lets the controller work out the ordering, which is better for complex graphs.

Then learn the data flow:
- **Parameters** pass small values between steps, referenced as `{{steps.x.outputs.parameters.y}}` or `{{tasks.x.outputs.parameters.y}}`
- **Artifacts** pass files, through an artifact repository such as S3 or MinIO

Then the operational features: `retryStrategy`, `activeDeadlineSeconds`, exit handlers, `CronWorkflow`, TTL and pod garbage collection, and synchronization with mutexes and semaphores.

## Phase 2: Argo CD (week 3)

If you use Argo CD, focus on the parts people skip:

- **Sync waves** order resources within a sync, using an annotation. Negative waves run first. This is how you apply a CRD before the custom resource that uses it
- **Hooks** run at PreSync, Sync, PostSync, and SyncFail, typically as Jobs for migrations
- **ApplicationSet generators** and which one fits: list for a fixed set, cluster for per-cluster, Git for directory or file discovery, matrix to combine two generators, pull request for preview environments
- **AppProject** as the multi-tenancy boundary, restricting allowed sources, destinations, and resource kinds
- **ignoreDifferences** for fields another controller owns, which is the same pattern CGOA tests conceptually

## Phase 3: Rollouts and Events (week 4)

**Rollouts** replaces a Deployment with a `Rollout` resource. Canary questions revolve around the `steps` list: `setWeight`, `pause` (with or without a duration), and analysis. Blue-green questions revolve around active and preview services and `autoPromotionEnabled`.

**Analysis** is the interesting part: an `AnalysisTemplate` defines metrics with success and failure conditions, an `AnalysisRun` executes them during the rollout, and failure aborts and rolls back automatically.

**Events** is small and structural. Learn the three objects: an `EventSource` produces events, an `EventBus` transports them, a `Sensor` subscribes with dependencies and filters and fires triggers. Know that a common trigger is an Argo Workflow, and that trigger parameters can be extracted from the event payload.

## Common traps

| Trap | Reality |
|---|---|
| Studying only Argo CD | It is a third of the exam |
| Confusing steps with DAG semantics | Steps is a list of lists with implicit ordering; DAG is explicit dependencies |
| Assuming parameters can carry files | Small values are parameters; files are artifacts, and artifacts need a repository |
| Thinking prune and self-heal are the same | Prune deletes resources no longer in the source; self-heal reverts drift on existing resources |
| Ignoring sync waves | Ordering problems (CRD before CR, namespace before workload) are exactly what waves solve |
| Treating a Rollout as a Deployment with extra fields | It is a separate resource; the Deployment is usually removed |
| Forgetting the analysis provider | A canary without analysis is just a timed pause |

## Exam day

- 90 minutes, 60 questions, knowledge-based. No terminal.
- Multiple-select questions state how many answers to select.
- 75% to pass, so roughly 45 of 60.
- One free retake is included.
- Expect YAML snippets to read, not to write. Practise reading a Workflow or Application manifest and saying what it does.

## Related

- [Practice plan](./practice-plan.md)
- [Scenarios](./scenarios.md)
- [Fact sheet](./fact-sheet.md)
- [CGOA](../cgoa/) - the concepts underneath Argo CD
