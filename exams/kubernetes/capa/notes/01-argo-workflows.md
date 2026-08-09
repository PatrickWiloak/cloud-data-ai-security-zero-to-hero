---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 12 min
---

# 01 - Argo Workflows

**Domain 1: Argo Workflows (36%)** - the largest domain.

A container-native workflow engine. Each step runs as a pod; the controller orchestrates them.

---

## The object model

- **Workflow** - one execution. Contains templates and an `entrypoint`.
- **WorkflowTemplate** - a reusable, namespaced definition invoked by other workflows.
- **ClusterWorkflowTemplate** - the cluster-scoped equivalent.
- **CronWorkflow** - a Workflow on a schedule.

---

## Templates

**Work templates** do something:

| Type | Runs |
|---|---|
| `container` | A container with image, command, args |
| `script` | A container plus an inline script; its stdout becomes an output parameter |
| `resource` | A Kubernetes resource operation (create, apply, delete, patch), with success conditions |
| `suspend` | Pauses the workflow until resumed manually or after a duration |
| `http` | An HTTP request without a pod |

**Orchestration templates** call other templates:

| Type | Semantics |
|---|---|
| `steps` | A list of lists. Items within an inner list run in parallel; outer lists run in sequence, forming a barrier between them |
| `dag` | Tasks with explicit `dependencies`. A task starts as soon as its dependencies finish |

```yaml
# steps: b and c run in parallel, but both wait for a, and d waits for both
- - name: a
- - name: b
  - name: c
- - name: d

# dag: d waits only for b and c; a fast chain is not blocked by a slow sibling
tasks:
  - name: a
  - name: b
    dependencies: [a]
  - name: c
    dependencies: [a]
  - name: d
    dependencies: [b, c]
```

Prefer `dag` when task durations vary or the graph is non-trivial.

---

## Parameters and artifacts

**Parameters** carry small string values.

- Inputs declared under `inputs.parameters`, referenced as `{{inputs.parameters.name}}`
- Outputs declared with `valueFrom.path` (a file), `valueFrom.parameter`, or the script template's stdout
- Consumed downstream as `{{steps.<step>.outputs.parameters.<name>}}` or `{{tasks.<task>.outputs.parameters.<name>}}`

**Artifacts** carry files, through an **artifact repository**: S3, GCS, Azure Blob, MinIO, HTTP, Git, or raw.

- Output artifacts are uploaded when the step ends; input artifacts are downloaded before the next step starts
- **Artifact garbage collection** (`artifactGC`) deletes them on workflow completion or deletion, which matters because artifact storage otherwise grows without bound

A **volumeClaimTemplate** is the alternative for sharing data: a PVC created for the workflow and mounted by multiple steps, avoiding the object storage round trip at the cost of scheduling constraints.

---

## Control flow

- **Conditionals**: `when: "{{steps.check.outputs.result}} == success"`
- **Loops**: `withItems` (a static list), `withParam` (a JSON array from a previous step's output), `withSequence` (a numeric range)
- **Recursion**: a template invoking itself, bounded by a `when` condition
- **Parallelism**: limits at workflow, template, and controller level
- **Suspend and resume** for manual approval gates

---

## Reliability and lifecycle

| Feature | Purpose |
|---|---|
| `retryStrategy` | Retry limits, backoff, and `retryPolicy` (Always, OnFailure, OnError, OnTransientError) |
| `activeDeadlineSeconds` | A hard time limit at workflow or template scope |
| `timeout` on a template | Per-step limit |
| `onExit` handler | Runs after the workflow finishes, whatever the outcome; used for notification and cleanup |
| Lifecycle hooks | Run templates on specified expressions, such as a step entering Failed |
| `ttlStrategy` | Deletes the Workflow object after completion, per outcome |
| `podGC` | Deletes pods on completion or success, freeing cluster resources sooner |
| Workflow archive | Persists completed workflows to a database so the UI retains history after the object is deleted |

**Synchronization** limits concurrency with a `mutex` (one at a time) or `semaphore` (N at a time), backed by a ConfigMap. This is how you stop twenty workflows hammering the same database.

---

## Security

- Workflows run pods under a **service account**; the workflow's own RBAC determines what `resource` templates may do
- The **executor** (emissary is the current default) is how the controller supervises the main container and collects outputs
- `podSpecPatch` allows targeted pod spec changes such as resource limits
- Restrict who may create Workflows in a namespace, since a Workflow is effectively arbitrary pod creation

---

## Key terms

- **Workflow** - the Argo custom resource representing one execution of a set of templates
- **WorkflowTemplate** - a reusable namespaced workflow definition invoked by other workflows
- **ClusterWorkflowTemplate** - the cluster-scoped reusable workflow definition
- **CronWorkflow** - a Workflow executed on a schedule with a concurrency policy
- **Entrypoint** - the template a Workflow starts from
- **Container template** - a template running a single container as a pod
- **Script template** - a template running an inline script whose stdout becomes an output parameter
- **Resource template** - a template performing a Kubernetes resource operation with success conditions
- **Suspend template** - a template pausing the workflow until resumed or until a duration elapses
- **Steps template** - an orchestration template of nested lists where inner lists run in parallel and outer lists in sequence
- **DAG template** - an orchestration template where tasks declare explicit dependencies
- **Output parameter** - a small value produced by a step and referenced by later steps
- **Artifact** - a file passed between steps through an artifact repository
- **Artifact repository** - the object storage backing artifact transfer, such as S3, GCS, or MinIO
- **artifactGC** - the configuration deleting artifacts when a workflow completes or is deleted
- **withParam** - the loop construct expanding a JSON array from a previous step into parallel iterations
- **retryStrategy** - per-template retry configuration including limit, backoff, and retry policy
- **onExit handler** - a template that runs after a workflow completes regardless of outcome
- **ttlStrategy** - configuration deleting completed Workflow objects after a specified time
- **podGC** - configuration deleting workflow pods on completion to free cluster resources
- **Synchronization** - mutex or semaphore configuration limiting concurrent workflow or template execution
- **Workflow archive** - database persistence of completed workflows so history survives object deletion

---

## Related

- [Notes 02: Argo CD](./02-argo-cd.md)
- [Scenarios](../scenarios.md) - scenarios 1, 2, and 7
