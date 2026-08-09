# Certified Argo Project Associate (CAPA) - Practice Questions

15 questions for CAPA prep, weighted like the exam: Argo Workflows 36%, Argo CD 34%, Rollouts 18%, Events 12%.

> **Cert page:** [exams/kubernetes/capa/](../../exams/kubernetes/capa/)

---

### Question 1
**Scenario:** A pipeline fetches from three sources in parallel, validates each, merges, trains, then publishes metrics and uploads an artifact in parallel. Validation durations vary widely.

A. A `steps` template with nested parallel groups
B. A `dag` template with explicit `dependencies` per task
C. One container running everything
D. Separate Workflows chained by Argo Events

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `steps` imposes a barrier between step groups, so the merge would wait for the slowest validation in the group. A DAG starts each task as soon as its own dependencies complete, so a fast chain is not blocked by a slow sibling. With varying durations that difference is substantial.
</details>

---

### Question 2
**Scenario:** Step A produces a 2 GB dataset and a single numeric quality score. Step B needs both. How should each be passed?

A. Both as output parameters
B. Both as artifacts
C. The score as an output parameter and the dataset as an artifact through the artifact repository
D. Both through an `emptyDir` volume

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Parameters carry small string values held in the workflow object, so a 2 GB value is not viable. Artifacts move files through a configured repository such as S3 or MinIO. `emptyDir` does not survive between pods; a `volumeClaimTemplate` would be the volume-based alternative.
</details>

---

### Question 3
**Scenario:** An Argo CD Application deploys an operator, its CRDs, and custom resources using those CRDs. The first sync fails because the custom resource kinds do not exist.

A. Retry the sync
B. Split into two Applications
C. Use sync waves: CRDs in a lower wave, then the operator, then the custom resources
D. Disable health checks

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Sync waves order resources within one sync, and Argo CD waits for a wave to become healthy before the next. Retrying works by accident once the CRDs exist and fails again on a fresh cluster. Splitting Applications works but waves solve it in one.
</details>

---

### Question 4
**Scenario:** With automated sync enabled, a ConfigMap deleted from the repository remains in the cluster, and a manual `kubectl edit` on a Deployment persists.

A. Both symptoms indicate self-heal is off
B. Prune is off (the orphaned ConfigMap) and self-heal is off (the manual edit)
C. Automated sync is not actually enabled
D. The Application is out of scope for its AppProject

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** They are independent flags. Prune deletes resources no longer present in the source; self-heal reverts drift on resources still declared in it. Automated sync does not imply either.
</details>

---

### Question 5
**Scenario:** A platform team wants a full ephemeral environment per open pull request, torn down on merge or close, with no human action.

A. The list generator
B. The Git directory generator
C. The pull request generator in an ApplicationSet
D. A CI job creating and deleting Applications

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The pull request generator discovers open pull requests and creates one Application each, removing them when the pull request closes. The list generator is static. The Git generator discovers directories or files. A CI job is push-based and leaves orphans whenever the job fails.
</details>

---

### Question 6
**Scenario:** A canary must reach 10% of traffic for 10 minutes, then 50%, then full, rolling back automatically if the error rate exceeds 1%. NGINX ingress is in use.

A. A Deployment with tuned `maxSurge` and `maxUnavailable`
B. A Rollout with canary steps, the NGINX traffic routing integration, and an AnalysisTemplate with a failure condition
C. A blue-green Rollout with `autoPromotionEnabled: false`
D. A Rollout with canary steps and pauses only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** All three parts are required: steps for the weights, a traffic provider so weights apply to real requests rather than approximating through replica counts, and analysis so failure aborts automatically. Pauses alone are timers. Blue-green is an instant cutover, not a graduated shift.
</details>

---

### Question 7
**Scenario:** Which Argo Events objects are required for a webhook to trigger a Workflow?

A. Sensor only
B. EventSource and Sensor
C. EventSource, EventBus, and Sensor
D. EventSource, Sensor, and a CronWorkflow

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The EventBus is required and easy to forget: without one deployed in the namespace, the EventSource and Sensor cannot communicate. The EventSource produces, the bus transports, the Sensor filters and triggers.
</details>

---

### Question 8
**Scenario:** Twenty workflows must not hit the same legacy database simultaneously; at most two may run at once.

A. Set `parallelism` on each Workflow
B. Use a `synchronization` semaphore backed by a ConfigMap
C. Use a CronWorkflow with a concurrency policy
D. Add a `retryStrategy`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Semaphores limit how many workflows or templates run concurrently across the namespace, which is exactly the shared-resource constraint. `parallelism` limits concurrency within a single workflow. A CronWorkflow concurrency policy governs overlapping runs of that one schedule. Retries are unrelated.
</details>

---

### Question 9
**Scenario:** What does an `onExit` handler do?

A. Runs only when the workflow succeeds
B. Runs only when the workflow fails
C. Runs after the workflow completes regardless of outcome, commonly for notification and cleanup
D. Runs before the workflow starts

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The exit handler is unconditional on outcome, which is what makes it suitable for notification and cleanup. Outcome-specific behavior is expressed with a `when` condition inside the handler or with lifecycle hooks.
</details>

---

### Question 10
**Scenario:** Which AppProject setting prevents a tenant's Application from deploying cluster-scoped resources it should not create?

A. Allowed source repositories
B. Allowed destinations
C. Allowed cluster-scoped resource kinds
D. Sync windows

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** AppProjects restrict sources, destinations, and both cluster-scoped and namespace-scoped resource kinds independently. Only the resource-kind list governs what kinds may be created. Sync windows govern when syncs may occur.
</details>

---

### Question 11
**Scenario:** Which Argo CD feature prevents the agent fighting an HPA over a Deployment's replica count?

A. Sync waves
B. `ignoreDifferences` on the `replicas` field, or removing it from the manifest
C. A PostSync hook
D. Disabling automated sync

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** This is the standard answer for any field another controller legitimately owns. Waves handle ordering, hooks handle timing of extra work, and disabling automated sync loses reconciliation for everything else.
</details>

---

### Question 12
**Scenario:** A workflow step must repeat once for each item in a JSON array produced by a previous step.

A. `withItems`
B. `withParam`
C. `withSequence`
D. A recursive template

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `withParam` expands a JSON array coming from a previous step's output. `withItems` takes a static list defined in the manifest. `withSequence` generates a numeric range. Recursion is for repeating until a condition is met.
</details>

---

### Question 13
**Scenario:** In a blue-green Rollout, what does `scaleDownDelaySeconds` control?

A. How long before the new version receives traffic
B. How long the old ReplicaSet remains available after promotion, enabling fast rollback
C. The analysis duration
D. The interval between traffic weight increases

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Keeping the previous ReplicaSet running briefly after the service selector flips is what makes an immediate rollback possible. Traffic weight increases are a canary concept, not blue-green.
</details>

---

### Question 14
**Scenario:** Which Argo Workflows configuration prevents completed workflow objects accumulating indefinitely in the cluster?

A. `retryStrategy`
B. `ttlStrategy` and `podGC`
C. `activeDeadlineSeconds`
D. `synchronization`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `ttlStrategy` deletes the Workflow object after completion, and `podGC` deletes the pods sooner to free cluster resources. The workflow archive persists history to a database so the UI keeps it after deletion. `activeDeadlineSeconds` is a time limit on execution, not cleanup.
</details>

---

### Question 15
**Scenario:** How does an event payload value, such as an S3 object key, reach a triggered Workflow as a parameter?

A. The Workflow reads the EventBus directly
B. Through trigger parameterization, using `dataKey` to extract from the payload into the created resource
C. Through an environment variable set on the Sensor
D. It cannot; the workflow must query S3 itself

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Trigger parameterization extracts values from the event payload and writes them into a path in the resource the trigger creates. This is the standard mechanism for passing event data into an Argo Workflow.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready. 75% is the pass mark.
- **10-12 correct (65-80%):** Check whether your misses cluster in Argo Workflows, which is the largest domain and the one most candidates under-study.
- **Below 10:** Work the [scenarios](../../exams/kubernetes/capa/scenarios.md) and practise reading Workflow and Application YAML and saying what it does.
