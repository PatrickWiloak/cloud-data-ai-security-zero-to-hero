---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 8 min
---

# CAPA High-Yield Scenarios

---

## Scenario 1: Steps or DAG

**Scenario**: A pipeline must: fetch data from three sources in parallel, then validate each result, then merge them, then train a model, then in parallel publish metrics and upload the artifact. Some validations take much longer than others.

**Solution Pattern**:
- Use a **DAG template**. Each task declares its `dependencies`, and the controller starts a task as soon as its dependencies complete
- With `steps`, the merge could not begin until the slowest validation in the whole step group finished, and every parallel group becomes a synchronization barrier
- With a DAG, a fast fetch-and-validate chain proceeds independently of a slow one, and only the merge waits for all three
- Pass results with **output parameters** for small values and **artifacts** for datasets

**Common Distractors**:
- Nested steps templates (works, but recreates DAG semantics awkwardly)
- One container doing everything (loses retry granularity, parallelism, and visibility)
- Separate Workflows chained by Events (adds latency and operational surface for what is one pipeline)

**Key Takeaway**: `steps` imposes a barrier between step groups; `dag` only waits on declared dependencies. When task durations vary, a DAG finishes materially sooner.

---

## Scenario 2: Passing data between steps

**Scenario**: Step A produces a 2 GB processed dataset and a single numeric quality score. Step B needs both.

**Solution Pattern**:
- The quality score is an **output parameter**, written to a file and declared with `valueFrom.path`, then referenced as `{{tasks.a.outputs.parameters.score}}`
- The dataset is an **output artifact**, uploaded to the configured **artifact repository** (S3, GCS, Azure Blob, or MinIO) and declared as an input artifact on step B
- Configure **artifact garbage collection** so 2 GB objects do not accumulate indefinitely
- An alternative for same-node, same-workflow data sharing is a `volumeClaimTemplate` mounted by both steps, which avoids the round trip through object storage

**Common Distractors**:
- Passing the dataset as a parameter (parameters are strings held in the workflow object; a 2 GB value is not viable)
- Writing to `emptyDir` (does not survive between pods)
- Relying on the container image (data is produced at runtime)

**Key Takeaway**: Small values are parameters, files are artifacts, and artifacts require a configured repository. A shared PVC is the alternative when both steps can mount the same volume.

---

## Scenario 3: Resource ordering during sync

**Scenario**: An Argo CD Application deploys an operator, its CustomResourceDefinitions, and several custom resources that the operator manages. The first sync fails because the custom resources are rejected: their kinds do not exist yet.

**Solution Pattern**:
- Use **sync waves** with the `argocd.argoproj.io/sync-wave` annotation
- Lower (including negative) wave numbers apply first: CRDs in wave `-1`, the operator deployment in wave `0`, custom resources in wave `1`
- Argo CD waits for resources in a wave to become healthy before starting the next
- For jobs that must run at specific points, use **hooks**: `PreSync` for a database migration, `PostSync` for a smoke test, `SyncFail` for cleanup
- `Replace` or `ServerSideApply` sync options may also be needed for large CRDs that exceed the annotation size limit

**Common Distractors**:
- Retrying the sync (works by accident once the CRDs exist, and fails again on a fresh cluster)
- Splitting into two Applications (workable, but waves solve it within one)
- Disabling health checks (hides the failure rather than ordering the work)

**Key Takeaway**: Sync waves order resources within one sync; hooks run work before, during, after, or on failure of a sync. Ordering problems are what both exist for.

---

## Scenario 4: Prune versus self-heal

**Scenario**: A team enables automated sync. Someone deletes a ConfigMap from the repository, but it remains in the cluster. Separately, someone edits a Deployment with `kubectl` and the change persists.

**Solution Pattern**:
- The removed ConfigMap persists because **prune** is disabled. Prune deletes cluster resources that are no longer present in the source
- The manual edit persists because **self-heal** is disabled. Self-heal reverts drift on resources still declared in the source
- Enable both in the sync policy for a fully reconciled application
- Consider `prune: false` deliberately for resources whose deletion is destructive, such as PersistentVolumeClaims, and use the `Prune=false` sync option per resource rather than disabling it globally

**Common Distractors**:
- Assuming automated sync implies both (it does not; each is a separate flag)
- Manually deleting the ConfigMap (fixes one instance, not the behavior)
- Disabling automated sync (removes the capability)

**Key Takeaway**: `prune` handles resources removed from the source; `selfHeal` handles drift on resources still in it. They are independent flags, and the distinction is directly testable.

---

## Scenario 5: Preview environments per pull request

**Scenario**: A platform team wants a full ephemeral environment for every open pull request, torn down automatically on merge or close, without a human creating anything.

**Solution Pattern**:
- An **ApplicationSet** with the **pull request generator**, which discovers open pull requests from GitHub, GitLab, Gitea, or Bitbucket
- The generator template creates one Application per pull request, with the branch as the source revision and a namespace derived from the pull request number
- When the pull request closes, the generator stops producing that element and the ApplicationSet deletes the Application
- Combine with an `AppProject` restricting these Applications to a preview namespace pattern and a limited set of resource kinds
- Set resource quotas on the generated namespaces so preview environments cannot exhaust the cluster

**Common Distractors**:
- A CI job creating and deleting Applications (push-based, and cleanup fails whenever the job does)
- The Git generator (discovers directories or files in a repository, not open pull requests)
- The list generator (a static list, so it does not track pull requests)

**Key Takeaway**: Match the generator to the source of truth: list for static sets, cluster for per-cluster fan-out, Git for directory discovery, pull request for preview environments, matrix to combine two.

---

## Scenario 6: Canary with automated rollback

**Scenario**: A payments service must release to 10% of traffic for 10 minutes, then 50% for 10 minutes, then fully, and must roll back automatically if the error rate exceeds 1% at any point. NGINX ingress is in use.

**Solution Pattern**:
- Replace the Deployment with a **Rollout** using the **canary** strategy
- Steps: `setWeight: 10`, `pause: {duration: 10m}`, `setWeight: 50`, `pause: {duration: 10m}`, then full promotion
- **Traffic routing** via the NGINX integration so weights apply to real traffic rather than only to replica counts
- An **AnalysisTemplate** querying Prometheus for the error rate, with a `failureCondition` at 1%, referenced in the canary as a background or step analysis
- A failing `AnalysisRun` aborts the rollout and shifts traffic back to the stable ReplicaSet automatically
- The Rollout resource itself is managed by Argo CD, so the desired state stays in the repository

**Common Distractors**:
- A Deployment with `maxSurge` and `maxUnavailable` (controls pod replacement, not traffic weight, and has no analysis or rollback)
- Manual promotion with a human watching dashboards (does not satisfy automatic rollback)
- Blue-green (an instant cutover, not a graduated traffic shift)

**Key Takeaway**: Canary steps plus a traffic provider plus an AnalysisTemplate is the complete answer. Without a traffic provider the weights only approximate through replica counts; without analysis the pauses are just timers.

---

## Scenario 7: Event-driven pipeline

**Scenario**: When a data file lands in an S3 bucket, a processing pipeline must run with the object key as a parameter. Duplicate events must not trigger duplicate runs of the same object.

**Solution Pattern**:
- An **EventSource** of type S3 (or SQS receiving S3 notifications) producing events
- An **EventBus** transporting them
- A **Sensor** with a dependency on that event source, a **filter** restricting to the relevant prefix and suffix, and a **trigger** creating an Argo Workflow
- **Trigger parameterization** extracts the object key from the event payload into a workflow parameter
- Deduplication through a **synchronization** mutex or semaphore keyed on the object, or by making the workflow idempotent and checking for an existing output

**Common Distractors**:
- A CronWorkflow polling the bucket (latency, and wasted runs when nothing arrives)
- A webhook EventSource (S3 notifications do not post directly to arbitrary webhooks without additional plumbing)
- Handling the event inside the workflow (something must create the Workflow in the first place)

**Key Takeaway**: EventSource produces, EventBus transports, Sensor filters and triggers. Payload values reach the workflow through trigger parameterization, and concurrency control belongs in the workflow's synchronization block.

---

## Related

- [Practice plan](./practice-plan.md)
- [Strategy](./strategy.md)
- [Notes](./notes/)
- [Practice questions](../../../resources/practice-questions/cncf-capa.md)
