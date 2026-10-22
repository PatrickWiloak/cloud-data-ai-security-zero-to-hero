# Certified Argo Project Associate (CAPA) - Practice Questions

30 questions for CAPA prep, weighted like the exam: Argo Workflows 36%, Argo CD 34%, Rollouts 18%, Events 12%.

> **Cert page:** [exams/kubernetes/capa/](../../exams/kubernetes/capa/)

---

### Question 1
**Scenario:** A pipeline fetches from three sources in parallel, validates each, merges, trains, then publishes metrics and uploads an artifact in parallel. Validation durations vary widely.

A. A `steps` template with nested parallel groups, where each group of steps runs together and the next group starts as soon as the previous one finishes
B. A `dag` template with explicit `dependencies` per task, so each task starts as soon as the tasks it needs have finished
C. One container running every stage in sequence with a shell script, which cannot parallelize the fetches
D. Separate Workflows chained by Argo Events, each stage emitting an event for the next Sensor

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `steps` imposes a barrier between step groups, so the merge would wait for the slowest validation in the group. A DAG starts each task as soon as its own dependencies complete, so a fast chain is not blocked by a slow sibling. With varying durations that difference is substantial.
</details>

---

### Question 2
**Scenario:** Step A produces a 2 GB dataset and a single numeric quality score. Step B needs both. How should each be passed?

A. The dataset and the score as output parameters
B. The dataset and the score as artifacts, because parameters cannot hold numeric values, each read back by step B as a file
C. The score as an output parameter and the dataset as an artifact through the artifact repository
D. The dataset and the score through a shared `emptyDir` volume mounted into the pods of the two steps, so that no repository is needed

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Parameters carry small string values held in the workflow object, so a 2 GB value is not viable, but a small numeric score fits fine as a string, so artifacts for both (B) are unnecessary. Artifacts move files through a configured repository such as S3 or MinIO. `emptyDir` does not survive between pods; a `volumeClaimTemplate` would be the volume-based alternative.
</details>

---

### Question 3
**Scenario:** An Argo CD Application deploys an operator, its CRDs, and custom resources using those CRDs. The first sync fails because the custom resource kinds do not exist.

A. Use sync waves: CRDs in a lower wave, then the operator, then the custom resources
B. Retry the sync until it passes, because the CRDs created in the first attempt will exist by the time the second attempt runs
C. Split the contents into two Applications with no ordering between them, so one installs the CRDs and operator and the other holds the custom resources
D. Disable health checks on the Application so that Argo CD stops treating the missing custom resource kinds as a failed sync

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Sync waves order resources within one sync, and Argo CD waits for a wave to become healthy before the next. Retrying works by accident once the CRDs exist and fails again on a fresh cluster. Splitting into Applications with no ordering (C) can hit the same missing-kind failure, whereas waves solve it in one sync.
</details>

---

### Question 4
**Scenario:** With automated sync enabled, a ConfigMap deleted from the repository remains in the cluster, and a manual `kubectl edit` on a Deployment persists.

A. Only self-heal is off, which explains both the orphaned ConfigMap and the persisting edit, since it controls deletion and drift reversal
B. Prune is off (which explains the orphaned ConfigMap) and self-heal is off (which explains the manual edit)
C. Automated sync is not actually enabled on the Application, so nothing is reconciled
D. The Application is out of scope for its AppProject, so Argo CD cannot reconcile it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** They are independent flags. Prune deletes resources no longer present in the source; self-heal reverts drift on resources still declared in it. Automated sync does not imply either.
</details>

---

### Question 5
**Scenario:** A platform team wants a full ephemeral environment per open pull request, torn down on merge or close, with no human action.

A. The list generator, which creates one Application per entry in a fixed list that an engineer maintains in the ApplicationSet
B. The Git directory generator, which creates one Application per folder in a repository and so tracks branches only through folders
C. A CI job creating and deleting Applications with the Argo CD CLI at the start and end of each pipeline run for the pull request
D. The pull request generator in an ApplicationSet, which creates an Application for each open pull request and removes it when the pull request closes

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The pull request generator discovers open pull requests and creates one Application each, removing them when the pull request closes. The list generator is static. The Git generator discovers directories or files. A CI job is push-based and leaves orphans whenever the job fails.
</details>

---

### Question 6
**Scenario:** A canary must reach 10% of traffic for 10 minutes, then 50%, then full, rolling back automatically if the error rate exceeds 1%. NGINX ingress is in use.

A. A blue-green Rollout with `autoPromotionEnabled: false`, which holds the new version until an operator approves each promotion step
B. A Deployment with tuned `maxSurge` and `maxUnavailable`, which paces the rolling update but cannot split traffic by percentage
C. A Rollout with canary steps, the NGINX traffic routing integration, and an AnalysisTemplate with a failure condition
D. A Rollout with canary steps and pauses only, giving the 10%, 50% and full weights on a timer

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** All three parts are required: steps for the weights, a traffic provider so weights apply to real requests rather than approximating through replica counts, and analysis so failure aborts automatically. Pauses alone are timers. Blue-green is an instant cutover, not a graduated shift.
</details>

---

### Question 7
**Scenario:** Which Argo Events objects are required for a webhook to trigger a Workflow?

A. EventSource, EventBus, and Sensor
B. EventSource and Sensor
C. EventSource, Sensor, and a CronWorkflow
D. Sensor only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The EventBus is required and easy to forget: without one deployed in the namespace, the EventSource and Sensor cannot communicate. The EventSource produces, the bus transports, the Sensor filters and triggers.
</details>

---

### Question 8
**Scenario:** Twenty workflows must not hit the same legacy database simultaneously; at most two may run at once.

A. A CronWorkflow with a concurrency policy such as `Forbid`, which stops overlapping runs of one schedule but not different workflows
B. A `retryStrategy` with a backoff on each step, so that workflows that fail to reach the database wait before they try again
C. Use a `synchronization` semaphore backed by a ConfigMap
D. `parallelism` set on each Workflow, which bounds how many steps in that single workflow run at once but not across the others

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Semaphores limit how many workflows or templates run concurrently across the namespace, which is exactly the shared-resource constraint. `parallelism` limits concurrency within a single workflow. A CronWorkflow concurrency policy governs overlapping runs of that one schedule. Retries are unrelated.
</details>

---

### Question 9
**Scenario:** What does an `onExit` handler do?

A. Runs only when the workflow succeeds
B. Runs after the workflow completes regardless of outcome, commonly for notification and cleanup
C. Runs only when the workflow fails
D. Runs before the workflow starts

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The exit handler is unconditional on outcome, which is what makes it suitable for notification and cleanup. Outcome-specific behavior is expressed with a `when` condition inside the handler or with lifecycle hooks.
</details>

---

### Question 10
**Scenario:** Which AppProject setting prevents a tenant's Application from deploying cluster-scoped resources it should not create?

A. Allowed destinations, which limit the clusters and namespaces an Application may deploy into but not the kinds of resource
B. Sync windows, which define when syncs are allowed or denied for the project's Applications, but not which resource kinds are created
C. Allowed cluster-scoped resource kinds
D. Allowed source repositories, which restrict where manifests can come from but not which cluster-scoped kinds those manifests contain

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** AppProjects restrict sources, destinations, and both cluster-scoped and namespace-scoped resource kinds independently. Only the resource-kind list governs what kinds may be created. Sync windows govern when syncs may occur.
</details>

---

### Question 11
**Scenario:** Which Argo CD feature prevents the agent fighting an HPA over a Deployment's replica count?

A. `ignoreDifferences` on the `replicas` field, or removing it from the manifest
B. A PostSync hook that resets the replica count after every sync
C. Disabling automated sync on the Application so that Argo CD never overwrites the HPA's changes without a manual sync
D. Sync waves that apply the HPA before the Deployment so the controller owns the replica count after the first sync

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** This is the standard answer for any field another controller legitimately owns. Waves handle ordering, hooks handle timing of extra work, and disabling automated sync loses reconciliation for everything else.
</details>

---

### Question 12
**Scenario:** A workflow step must repeat once for each item in a JSON array produced by a previous step.

A. A recursive template that calls itself again until a stop condition is met
B. `withSequence`, which generates a numeric range to loop over for each repetition
C. `withItems`
D. `withParam`, which expands a JSON array from a previous step's output

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `withParam` expands a JSON array coming from a previous step's output. `withItems` takes a static list defined in the manifest. `withSequence` generates a numeric range. Recursion is for repeating until a condition is met.
</details>

---

### Question 13
**Scenario:** In a blue-green Rollout, what does `scaleDownDelaySeconds` control?

A. How long before the new version receives traffic, since it delays the service selector switch
B. How long the old ReplicaSet remains available after promotion, enabling fast rollback of a bad release
C. The analysis duration, since it sets how long metrics are evaluated against the new ReplicaSet before the Rollout is promoted
D. The interval between traffic weight increases, as each step shifts more requests over

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Keeping the previous ReplicaSet running briefly after the service selector flips is what makes an immediate rollback possible. Traffic weight increases are a canary concept, not blue-green.
</details>

---

### Question 14
**Scenario:** Which Argo Workflows configuration prevents completed workflow objects accumulating indefinitely in the cluster?

A. `retryStrategy`, which re-runs failed steps with a backoff and so cleans up failed attempts as the Workflow runs
B. `synchronization`, which uses semaphores and mutexes to limit concurrency and so keeps the number of Workflows in the cluster low
C. `ttlStrategy` and `podGC`
D. `activeDeadlineSeconds`, which terminates a Workflow that runs too long and so removes stuck objects from the cluster

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `ttlStrategy` deletes the Workflow object after completion, and `podGC` deletes the pods sooner to free cluster resources. The workflow archive persists history to a database so the UI keeps it after deletion. `activeDeadlineSeconds` is a time limit on execution, not cleanup.
</details>

---

### Question 15
**Scenario:** How does an event payload value, such as an S3 object key, reach a triggered Workflow as a parameter?

A. Through trigger parameterization, using `dataKey` to extract from the payload into the created resource
B. Through an environment variable set on the Sensor
C. It cannot; the workflow must query S3 itself
D. The Workflow reads the EventBus directly

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Trigger parameterization extracts values from the event payload and writes them into a path in the resource the trigger creates. This is the standard mechanism for passing event data into an Argo Workflow.
</details>

---

### Question 16
**Scenario:** Ten teams copy the same build-and-scan steps into their own Workflows in different namespaces. The platform team wants one shared definition that all namespaces can reference.

A. A WorkflowTemplate in each team namespace, kept in sync by hand when the steps change
B. A ClusterWorkflowTemplate, referenced from each Workflow with `templateRef` and `clusterScope: true`
C. A ConfigMap holding the step YAML, mounted into each Workflow's pods at runtime
D. A CronWorkflow in the argo namespace that runs the steps for every team on a schedule

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A ClusterWorkflowTemplate is cluster-scoped, so Workflows in any namespace can reference its templates through `templateRef` with `clusterScope: true`. Namespaced WorkflowTemplates would need a copy per namespace. A ConfigMap of YAML is not something the controller executes. A single CronWorkflow does not let each team run the steps in its own Workflow when it needs them.
</details>

---

### Question 17
**Scenario:** A nightly CronWorkflow sometimes runs longer than 24 hours. A new run must never start while the previous one is still running.

A. Set `startingDeadlineSeconds` to 0, which stops any run starting while another is active
B. Set `successfulJobsHistoryLimit` to 1, so only one run of the CronWorkflow can exist at once
C. Set `concurrencyPolicy: Forbid` on the CronWorkflow
D. Set `activeDeadlineSeconds` to 24 hours on each run, so the old run is killed when the next starts

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `concurrencyPolicy: Forbid` skips a scheduled run while the previous one is still running, matching Kubernetes CronJob semantics. `startingDeadlineSeconds` controls how late a missed run may start. History limits control how many finished runs are kept. A deadline kills the long run, which is not what is wanted.
</details>

---

### Question 18
**Scenario:** A step calling a flaky external API should be retried up to three times with growing delays, but only for failures of the step's own container, not for infrastructure errors.

A. `retryStrategy` with `limit: 3`, `retryPolicy: OnFailure`, and a `backoff` with duration and factor
B. `retryStrategy` with `limit: 3` and `retryPolicy: OnError`, which covers only container failures
C. An `onExit` handler that resubmits the whole Workflow three times when the step fails
D. `activeDeadlineSeconds: 3` on the step, which restarts it three times before failing

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `retryPolicy: OnFailure` retries when the main container fails, `OnError` retries on Argo-level errors such as pod deletion, and `Always` covers both. `backoff` adds increasing delays. `OnError` is the wrong policy for container failures. An exit handler resubmitting the Workflow re-runs everything. `activeDeadlineSeconds` is a timeout, not a retry count.
</details>

---

### Question 19
**Scenario:** A deploy step should run only if the previous test step output the parameter `result` with the value `pass`.

A. Put the deploy step inside an `onExit` handler, which runs it only when tests pass
B. Add a `when` clause to the deploy step comparing the test step's output parameter to `pass`
C. Set `continueOn: failed` on the test step, which skips the deploy step automatically
D. Use `withParam` on the deploy step with the test result, which loops zero times on failure

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A `when` expression such as `"{{steps.test.outputs.parameters.result}} == pass"` makes a step or task conditional. Exit handlers run at the end whether the Workflow succeeded or failed. `continueOn` lets a Workflow continue past failures; it does not skip steps. `withParam` is for loops over lists, and using it as a condition is fragile.
</details>

---

### Question 20
**Scenario:** A release Workflow must pause after staging tests until a human approves, then continue to production.

A. A `sleep` step with a very long duration, which an operator deletes to approve the release
B. A `synchronization` mutex, which an operator releases by hand to let the Workflow continue
C. A `suspend` template between staging and production, resumed with `argo resume` or from the UI
D. Two separate Workflows, with production started by the operator copying staging's YAML

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A `suspend` template pauses the Workflow indefinitely or for a set duration until it is resumed through the CLI, UI, or API, which is the built-in approval gate. Deleting a sleeping pod would fail the step. Mutexes control concurrency between Workflows, not approvals. Splitting by hand loses the single audited run.
</details>

---

### Question 21
**Scenario:** A database schema migration must run as a Job before Argo CD applies the new Deployment in each sync, and the sync must stop if the migration fails.

A. A Job with the `argocd.argoproj.io/hook: PreSync` annotation
B. A Job with the `argocd.argoproj.io/hook: PostSync` annotation
C. A Job in the same wave as the Deployment, with a long backoffLimit
D. A Job outside the Application, run by a CronJob every five minutes

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** PreSync hooks run before the sync applies the main resources, and if the hook fails the sync fails, so the Deployment is not updated. PostSync runs after a successful sync, which is too late. Placing the Job in the same wave gives no ordering guarantee with the Deployment. A CronJob is not tied to syncs at all.
</details>

---

### Question 22
**Scenario:** Every cluster registered in Argo CD with the label `env=prod` must automatically get the monitoring stack, including clusters added in the future.

A. An App of Apps, with one child Application file added to Git for each new cluster
B. An ApplicationSet with the list generator, with each cluster's name typed into the list
C. An ApplicationSet with the Git directory generator, which finds clusters by folder name
D. An ApplicationSet with the cluster generator and a label selector on `env=prod`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The cluster generator creates one Application per registered cluster whose secret matches the selector, so new `env=prod` clusters get the stack automatically. App of Apps and the list generator both need manual edits for each new cluster. The Git directory generator discovers repository paths, not registered clusters.
</details>

---

### Question 23
**Scenario:** Applications that contain a custom resource from an in-house operator always show as Healthy, even when the operator reports the resource as failed in its status.

A. Enable automated sync with self-heal, which recalculates health from the resource's status field
B. Add a custom health check in Lua for that resource kind in the `argocd-cm` ConfigMap
C. Add a PostSync hook that deletes the resource if its status reports a failure
D. Set the resource's sync wave to a negative number, so health is checked before other resources

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Argo CD has built-in health checks for common kinds. For other custom resources, a Lua health script configured in `argocd-cm` (`resource.customizations`) reads the status and returns Healthy, Progressing, or Degraded. Self-heal fixes drift, not health assessment. Deleting failed resources hides the problem. Sync waves order applies and do not define health.
</details>

---

### Question 24
**Scenario:** An Application shows Sync Status: OutOfSync and Health Status: Healthy. What does this mean?

A. The live resources differ from Git, but the running workloads are currently healthy
B. The sync has failed, and Argo CD has rolled the workloads back to the last healthy state
C. The Git repository is unreachable, so Argo CD reports the last known health only
D. The workloads are running the Git version, but some health checks have not run yet

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Sync status compares the live state with the desired state in Git, and health status reports whether the resources are working. They are independent, so a cluster can be healthy and still differ from Git, for example before an automated sync runs or with automated sync disabled. A failed sync is shown in the operation state. An unreachable repository raises a comparison error. Matching Git would show Synced.
</details>

---

### Question 25
**Scenario:** Members of the `team-a` SSO group must be able to view and sync Applications in the `team-a` project only, and nothing else.

A. Add the group to the `admin` role in `argocd-rbac-cm`, then restrict it with an AppProject source list
B. Grant the group read access to the `argocd` namespace with a Kubernetes RoleBinding
C. Define a role in `argocd-rbac-cm` (or a project role) allowing get and sync on `team-a/*`, bound to the group
D. Give each member a local Argo CD account with the password shared within the team

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Argo CD RBAC policies in `argocd-rbac-cm`, or project roles, grant actions such as get and sync on `<project>/<application>` patterns and can be bound to SSO groups. The admin role grants everything, and source restrictions do not limit actions. Kubernetes RBAC on the argocd namespace does not govern Argo CD API actions. Shared local accounts lose individual identity.
</details>

---

### Question 26
**Scenario:** A canary step should query Prometheus for the success rate every minute, failing the rollout if the rate drops below 99% more than twice.

A. An `AnalysisTemplate` with a Prometheus provider, `interval: 1m`, `successCondition: result[0] >= 0.99`, and `failureLimit: 2`
B. A Prometheus alerting rule that pages an operator, who then aborts the rollout with the kubectl plugin
C. A `readinessProbe` on the canary pods that queries Prometheus and fails below 99%
D. A `pause` step of ten minutes followed by a manual check of the Grafana dashboard

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** An AnalysisTemplate defines metrics with a provider, an interval, and success or failure conditions. When failed measurements exceed `failureLimit`, the analysis fails and the Rollout aborts and rolls back automatically. Paging an operator or checking a dashboard is manual. Readiness probes check pod health, not service-level metrics from Prometheus.
</details>

---

### Question 27
**Scenario:** In a blue-green Rollout, the new version should receive test traffic through a separate service and pass analysis before it becomes active, with no automatic promotion.

A. Set `scaleDownDelaySeconds: 0`, which tests the preview service before switching traffic
B. Use a canary strategy with `setWeight: 100`, which is the same as a blue-green promotion
C. Remove the `activeService` field, so that traffic is sent to the preview service until promoted
D. Configure `previewService`, `prePromotionAnalysis`, and `autoPromotionEnabled: false`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** In blue-green, `previewService` routes to the new ReplicaSet for testing, `prePromotionAnalysis` runs before the switch, and `autoPromotionEnabled: false` waits for a manual promote. `scaleDownDelaySeconds` controls how long the old version is kept after the switch. A 100% canary weight shifts all traffic at once with no preview. `activeService` is required for blue-green.
</details>

---

### Question 28
**Scenario:** A canary Rollout with `setWeight: 20` runs without any traffic router such as an ingress controller or service mesh. How is the 20% achieved?

A. Argo Rollouts installs a sidecar proxy in each pod that drops 80% of requests to the canary
B. The Rollout fails validation, since canary steps cannot run without a configured traffic router
C. It approximates the weight by scaling canary and stable ReplicaSets so about 20% of pods are canary
D. The Service is edited so that its selector matches the canary pods for 20% of the time

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Without a traffic router, Argo Rollouts splits traffic through the replica ratio behind the same Service, so the weight is only as precise as the replica count allows. Rollouts does not inject proxies. Canary steps work without a router, just less precisely. Services do not time-share selectors.
</details>

---

### Question 29
**Scenario:** A Sensor listens to a Git webhook EventSource but should trigger the build Workflow only for pushes to the `main` branch.

A. Add a data filter on the Sensor dependency matching the branch ref field in the event payload
B. Create a separate EventBus for main-branch events, which receives only events from main
C. Add a `when` clause to the triggered Workflow, which cancels itself on any other branch
D. Configure the EventSource to drop events from other branches before they reach any bus

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Sensor dependencies support filters, such as data filters on JSON paths in the payload, so only matching events satisfy the dependency and fire the trigger. A second EventBus does not filter by content. A Workflow that cancels itself still starts for every push. Generic webhook EventSources do not filter on payload fields; filtering belongs on the Sensor.
</details>

---

### Question 30
**Scenario:** A training Workflow should start only after both a new dataset arrives in S3 and a model config change is pushed to Git.

A. Two Sensors, each with one dependency, which both trigger the same Workflow on every event
B. One Sensor with both dependencies, and a trigger whose `conditions` require both, such as `dataset && config`
C. One EventSource that combines the S3 and Git events into a single event before the bus
D. A CronWorkflow that polls S3 and Git every minute and starts training when both have changed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A Sensor can declare several dependencies, and trigger `conditions` combine them with boolean logic, so the trigger fires only when both have occurred. Two independent Sensors would start the Workflow twice, once for each event. EventSources do not merge different event types. Polling replaces the event-driven design with delay and extra load.
</details>

---

## Scoring guide

- **26-30 correct (85%+):** Ready. 75% is the pass mark.
- **20-25 correct (67-83%):** Check whether your misses cluster in Argo Workflows, which is the largest domain and the one most candidates under-study.
- **Below 20:** Work the [scenarios](../../exams/kubernetes/capa/scenarios.md) and practice reading Workflow and Application YAML and saying what it does.
