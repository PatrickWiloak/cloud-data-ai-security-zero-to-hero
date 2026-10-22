---
last-updated: 2026-10-22
difficulty: advanced
---

# IBM Cloud Site Reliability Engineer - Practice Questions

30 questions for this exam, weighted toward monitoring and observability (25%), incident management (20%), automation and IaC (20%), then availability, capacity, and Kubernetes operations.

> **Cert page:** [exams/ibm/cloud-site-reliability-engineer/](../../exams/ibm/cloud-site-reliability-engineer/)

---

### Question 1
**Scenario:** An SLI, an SLO, and an SLA must be distinguished.

A. The SLI is the measurement, the SLO the internal target, and the SLA the external contract
B. They are the same thing under three names
C. The SLA is the internal target, and the SLO is the customer contract
D. The SLO is a measurement taken from monitoring, while the SLI is the target that the team agrees with its product owner

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** SLOs should be tighter than SLAs so you notice before you breach the contract. The practical output of an SLO is the error budget, which converts reliability from an argument into an arithmetic question about how much budget remains.
</details>

---

### Question 2
**Scenario:** An error budget is exhausted mid-quarter.

A. Raise the SLO target so the remaining budget looks larger
B. Continue shipping features at the current pace
C. Stop measuring until the next quarter starts, so the exhausted budget does not trigger alerts or escalations
D. Prioritize reliability work until the budget recovers, per the agreed policy

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The budget policy is agreed in advance precisely so the decision is not relitigated under pressure. Raising the SLO to make the number look better is the failure mode that makes the whole practice performative.
</details>

---

### Question 3
**Scenario:** A distributed request must be followed across six services.

A. Logs from each service, searched one at a time and lined up by timestamp to rebuild the path of the request
B. Ask each team to report how long its service held the request
C. Distributed tracing with context propagated across service boundaries, ideally with OpenTelemetry
D. Metrics only, using per-service latency histograms and error rates to infer where the request spent its time

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Traces show where the latency actually went, which logs cannot without manual correlation. The requirement people underestimate is propagation: every service must forward the trace context, or the trace fragments into disconnected pieces.
</details>

---

### Question 4
**Scenario:** Alerts wake the on-call engineer several times a night for conditions that self-resolve.

A. Alert on user-facing, actionable symptoms with duration conditions, and delete alerts nobody acts on
B. Add more alerts on every metric that moves, including CPU and memory on each host, so that nothing is missed
C. Increase the size of the on-call rotation so that each engineer is woken less often, without changing any alert
D. Ignore the alerts that resolve by themselves and mute the night channel

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Every page should correspond to something a human must do now. Alerts on causes rather than symptoms generate noise, and a self-resolving condition is by definition not one that needed a human. Alert fatigue causes real incidents to be missed.
</details>

---

### Question 5
**Scenario:** A postmortem is written after a major incident.

A. Identify who made the mistake and record it in their performance review so that it is not repeated
B. Add a dashboard for the failing component and consider the incident closed once the graph looks normal
C. Close the ticket as soon as service is restored and move the follow-up work into the next planning cycle
D. Blameless analysis of the timeline and gaps, producing owned action items

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Blame suppresses the information you need, because people stop reporting near misses. The output that matters is a small number of specific actions with owners; a long list nobody owns is the same as no actions.
</details>

---

### Question 6
**Scenario:** Infrastructure changes must be repeatable and reviewable.

A. A runbook describing each manual step in detail, stored in the wiki and followed by whoever is on call
B. Console changes with notes, written in the ticket after each change so the next person can see what was done
C. Infrastructure as code in version control, applied through a pipeline with plan review
D. Shell scripts run by hand from an engineer's laptop, with the latest version copied to a shared folder

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** IaC gives review, history, and rollback for infrastructure, and applying through a pipeline means the same process every time regardless of who is on call. Console changes are invisible to the next person and cause drift from the declared state.
</details>

---

### Question 7
**Scenario:** Toil is consuming most of the team's time.

A. Work longer hours until the backlog of manual tasks clears
B. Accept it as the normal cost of running production
C. Measure the toil, then automate the highest-volume repetitive tasks, capping toil as a share of time
D. Hire more people to share the repetitive work so that each engineer carries a smaller number of manual tasks

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Adding people to unbounded toil scales the problem rather than solving it. Capping toil as a share of the team's time creates the space to automate, which is the mechanism that makes the reduction actually happen.
</details>

---

### Question 8
**Scenario:** A Kubernetes deployment must survive a node failure without dropping requests.

A. A larger node with more CPU and memory, so that the pod is less likely to be evicted for lack of resources
B. Multiple replicas spread across nodes and zones with anti-affinity, plus a PodDisruptionBudget and correct readiness probes
C. Restart on failure, using a restart policy so the container comes back as soon as the node returns
D. One replica with a high resource request, which the scheduler places on the most reliable node available

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spreading covers the failure, the PDB protects against voluntary disruptions such as node drains removing too many at once, and readiness probes keep traffic off pods that are not serving. Missing the last one causes errors during every rollout.
</details>

---

### Question 9
**Scenario:** Capacity planning is needed for a growing service.

A. React when it breaks, then add servers during the incident and tune the settings after the outage is over
B. Model demand growth against measured headroom, load test for the real limit, and plan lead times
C. Autoscaling handles everything, so there is no need to know the limits of the service or its dependencies
D. Over-provision heavily, running several times the expected peak capacity all year to avoid any shortfall

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Autoscaling handles variation within a provisioned envelope; it does not handle quota limits, license ceilings, or a dependency that cannot scale. Knowing the real breaking point, from testing rather than extrapolation, is what makes the plan credible.
</details>

---

### Question 10
**Scenario:** Chaos engineering is proposed.

A. Hypothesize about steady state, run a small experiment with a blast radius limit and abort condition
B. Only test in development, where a failure cannot affect any user
C. It is too risky, because injecting failure can only cause outages
D. Randomly break production components immediately, with no hypothesis, to see what the system does under stress

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** It is an experiment, not vandalism: you predict what should happen, verify the system behaves as designed, and learn when it does not. The blast radius limit and abort condition are what make running it in production defensible.
</details>

---

### Question 11
**Scenario:** A deployment must be rolled back quickly if error rates rise.

A. Automated rollback triggered by SLI-based canary analysis, with the previous version still available
B. Fix forward always, writing a patch while the faulty release stays live and the error rate keeps on rising
C. Investigate by hand first, then decide whether to roll back
D. Wait for user reports to confirm that the problem is real before any change is made to the deployment at all

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Rollback speed is set in advance by whether the previous version is still deployable and whether the trigger is automatic. Fixing forward is reasonable when the fix is trivial and understood, but it should be the exception rather than the plan.
</details>

---

### Question 12
**Scenario:** A dependency's failure must not cascade.

A. No timeouts, so the caller waits as long as the dependency needs and every request completes eventually
B. Fail the whole request every time the dependency errors, so the user always sees a clear failure message
C. Retry indefinitely and immediately until the dependency answers, so no request is ever dropped or lost
D. Timeouts, bounded retries with backoff and jitter, circuit breakers, and a defined degraded mode

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Unbounded retries turn a slow dependency into an outage by exhausting connections and amplifying load, and synchronized retries create thundering herds, which is why jitter matters. Deciding what degraded looks like is a product decision made before the incident.
</details>

---

### Question 13
**Scenario:** Logs are expensive and voluminous.

A. Keep everything at debug level forever and store it on fast disks, so that any past event can be searched
B. Structure logs, set levels appropriately, sample high-volume events, and tier retention so recent data is queryable and older data is archived
C. Log only errors, which removes the noise and cuts the volume by the largest amount available
D. Stop logging and rely on metrics, which are cheaper to store and still show that something went wrong

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Structured logs make sampling and querying possible, which is what lets you cut volume without losing the ability to investigate. Logging only errors removes the context around the error, which is usually where the cause is visible.
</details>

---

### Question 14
**Scenario:** Backups exist but recovery has never been tested.

A. Backups are sufficient, because the job reports success every night and the data is stored in a second region too
B. Test restores on a schedule, measure the actual recovery time against the RTO, and fix what the test reveals
C. Increase the backup frequency to hourly, which reduces the data lost although it does not show that the restore works at all
D. Trust the backup job status and the storage bucket size

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A successful backup job proves data was written, not that it can be read back into a working system. The failures that surface in a restore test are missing keys, incompatible versions, and a recovery time several times longer than anyone assumed.
</details>

---

### Question 15
**Scenario:** On-call must be sustainable.

A. Everyone on call all the time, so that any engineer can answer a page and no single person carries the load
B. No on-call at all, with incidents picked up by whoever notices them first during working hours
C. A rotation with reasonable frequency, clear escalation, current runbooks, handover, and a limit on pages per shift that triggers investigation when exceeded
D. One person permanently, a senior engineer who knows the systems best and answers every page in turn

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Sustainability is a reliability control, not a perk: an exhausted engineer makes worse decisions during the incident that matters. Treating a high page count as a defect to investigate is what keeps the rotation from degrading over time.
</details>

---

### Question 16
**Scenario:** A service has a 99.9% availability SLO over 30 days. Its alert fires whenever the error rate exceeds 0.1% for one minute, which pages the team several times a week for blips that barely touch the error budget. What is a better alerting approach?

A. Raise the threshold to 5% errors for one minute so that only the big outages page
B. Alert on error budget burn rate over multiple windows, paging on fast burns
C. Remove error alerts and rely on users to report problems through support
D. Alert on CPU above 80%, since high CPU usually comes before errors

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Burn-rate alerts measure how fast the error budget is being spent, and using a long and a short window together pages quickly for serious burns while ignoring brief blips. A fixed 5% threshold misses slow, steady burns that still exhaust the budget. Users reporting problems means slow detection. CPU is a cause-based signal that often fires with no user impact.

**Key Concept:** Alert on the SLO, using multi-window burn rates. See [Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/).
</details>

---

### Question 17
**Scenario:** An application on IBM Cloud Kubernetes Service exposes metrics at `/metrics` in Prometheus format. The team uses IBM Cloud Monitoring and wants those custom metrics alongside the platform metrics. What should they do?

A. Write the metrics to the application log and build charts from log lines
B. Install a separate Grafana server and point it at every pod by hand
C. Push the metrics into Activity Tracker as custom audit events once every minute
D. Deploy the Monitoring agent in the cluster and let it scrape Prometheus metrics

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The IBM Cloud Monitoring agent runs in the cluster, collects platform and container metrics, and can scrape Prometheus-format endpoints, so custom metrics land next to everything else. Parsing metrics out of logs is fragile and costly. A hand-wired Grafana server adds a second stack and still needs a metrics store. Activity Tracker records audit events, not application metrics.

**Key Concept:** Use one monitoring pipeline for platform and custom metrics. See [Getting started with IBM Cloud Monitoring](https://cloud.ibm.com/docs/monitoring?topic=monitoring-getting-started).
</details>

---

### Question 18
**Scenario:** During incidents, engineers struggle to follow one customer request through the logs of five services, because each service logs free text with no shared fields. What change helps most?

A. Structured JSON logs that carry a correlation or trace ID through every service
B. More verbose free-text logs in every service, all written at debug level
C. Separate log destinations per service so that each log stream is smaller
D. Shorter log retention so that searches across services run faster

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Structured logs with a shared correlation or trace ID let a single query return every line for one request across all services. More verbose text adds cost without making lines joinable. Splitting destinations makes cross-service search harder. Shorter retention speeds searches but loses history and does not link anything.

**Key Concept:** Correlate signals with shared identifiers in structured logs. See [What is observability?](https://www.ibm.com/think/topics/observability)
</details>

---

### Question 19
**Scenario:** A checkout API failed at 3 a.m. and nobody noticed until customers complained at 8 a.m. There was almost no traffic overnight, so error-rate alerts never fired. What would have caught it?

A. Real user monitoring, which measures what actual visitors experience
B. A dashboard showing request rates, reviewed by the team at the morning stand-up
C. Synthetic monitoring that runs a scripted checkout at a regular interval
D. Longer log retention, so engineers can look back at the night's errors

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Synthetic checks run scripted transactions on a schedule, so they detect failures even when no real users are present. Real user monitoring needs real users, which were absent. A dashboard reviewed in the morning is what already happened. Retention helps investigation, not detection.

**Key Concept:** Synthetic monitoring covers low-traffic periods and critical paths. See [What is observability?](https://www.ibm.com/think/topics/observability)
</details>

---

### Question 20
**Scenario:** During a major incident, six engineers are all debugging different theories, two are changing production at once, and nobody is updating stakeholders. What practice addresses this most directly?

A. Ask the most senior engineer to fix the problem alone while the others watch
B. Pause all work on the incident until the postmortem has been written
C. Open a separate chat channel for each engineer's theory about the cause
D. Name an incident commander who coordinates roles, changes, and updates

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** An incident commander coordinates the response: assigning roles such as operations and communications, controlling who changes production, and making sure stakeholders get updates. One senior engineer working alone loses parallel effort and still leaves communication undone. Postmortems come after resolution. More channels fragment the response further.

**Key Concept:** Clear incident roles prevent chaos and conflicting changes. See [Managing incidents](https://sre.google/sre-book/managing-incidents/).
</details>

---

### Question 21
**Scenario:** Ten minutes after a deployment, error rates spike. The team does not yet know the root cause. What should they do first?

A. Keep debugging in production until the exact root cause has been found
B. Mitigate first by rolling back the deployment, then investigate the cause
C. Scale the service out to twice the number of instances and wait to see
D. Write the postmortem now while the details are still fresh in memory

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The priority in an incident is to stop user impact; a recent deployment is the most likely cause, and rolling back is usually the fastest mitigation. Root cause analysis continues once users are safe. Debugging in production prolongs the outage. Scaling out rarely fixes a code defect. Postmortems come after the incident is resolved.

**Key Concept:** Mitigate first, diagnose second. See [Incident response](https://sre.google/workbook/incident-response/).
</details>

---

### Question 22
**Scenario:** Leadership wants a metric showing how long problems go on before the team even knows about them, to justify investment in monitoring. Which metric fits?

A. Mean time to detect (MTTD)
B. Mean time to repair (MTTR)
C. Mean time between failures (MTBF)
D. Change failure rate

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** MTTD measures the time from when a problem starts to when it is detected, which is exactly what better monitoring improves. MTTR measures time to restore service after a failure. MTBF measures how often failures happen. Change failure rate is the share of deployments that cause problems.

**Key Concept:** Break incident duration into detect, respond, and recover to see where time goes. See [What is MTTR?](https://www.ibm.com/think/topics/mttr)
</details>

---

### Question 23
**Scenario:** Infrastructure is managed with Terraform through IBM Cloud Schematics. An engineer changed a security group rule in the console during an incident and forgot to tell anyone. How should the team find this kind of change?

A. Read the IBM Cloud invoice each month for unexpected new line items
B. Delete and recreate all infrastructure each night from the Terraform code
C. Run a Terraform plan or drift detection to compare real state with the code
D. Rely on the engineer's memory and ask them to update the code later

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A plan compares the real resources with the configuration and shows differences, which is how drift from console changes is found; Schematics workspaces can run plans and drift detection. Invoices do not show rule changes. Nightly rebuilds are disruptive and risky. Memory is what failed here.

**Key Concept:** Detect drift regularly and fold emergency changes back into code. See [Getting started with Schematics](https://cloud.ibm.com/docs/schematics?topic=schematics-getting-started).
</details>

---

### Question 24
**Scenario:** A team wants every change to its Kubernetes clusters to come from a reviewed pull request, and wants any manual change in the cluster to be reverted automatically. Which approach fits?

A. Give every engineer cluster-admin access and ask them to log each change
B. Run `kubectl apply` from engineers' laptops after each pull request merges
C. Take a nightly backup of every cluster and restore it each morning
D. GitOps, where a controller such as Argo CD reconciles the cluster to Git

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** In GitOps, Git holds the desired state and a controller continuously reconciles the cluster to it, so changes arrive through pull requests and manual drift is reverted. Broad admin access and change logs rely on discipline. Laptop applies are unauditable and inconsistent. Nightly restores lose legitimate changes and still leave drift during the day.

**Key Concept:** Git as the source of truth, with continuous reconciliation. See [Argo CD documentation](https://argo-cd.readthedocs.io/en/stable/).
</details>

---

### Question 25
**Scenario:** Servers in a fleet were patched by hand over two years, and now no two are the same. A fix that works on one server fails on another. What practice prevents this in future?

A. Keep patching in place, but write down every change in a shared document
B. Use immutable infrastructure: build new images and replace servers
C. Give each server its own patch schedule tuned to its own workload
D. Stop patching servers so that their configurations stay the same

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Immutable infrastructure replaces servers with new ones built from a versioned image instead of changing them in place, so every server matches its definition. Documents drift from reality. Individual schedules create even more variation. Not patching leaves known vulnerabilities in place.

**Key Concept:** Replace, do not repair, to eliminate configuration drift. See [What is infrastructure as code?](https://www.ibm.com/think/topics/infrastructure-as-code)
</details>

---

### Question 26
**Scenario:** A public web application runs in two IBM Cloud regions. If one region fails, users should automatically go to the healthy region without any DNS changes by hand. What should the team configure?

A. A global load balancer in Cloud Internet Services, with health checks on each region's origin pool
B. A single VPC load balancer in the first region, which also forwards traffic on to the second region
C. Two DNS records with a long TTL, which the on-call engineer edits by hand during an outage
D. A Transit Gateway between the two regions, which redirects public users to the healthy one

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A global load balancer in Cloud Internet Services sends traffic to origin pools in each region and uses health checks to steer users away from a failed pool automatically. A regional load balancer fails with its region. Hand-edited DNS with a long TTL is slow and manual. Transit Gateway connects private networks; it does not route public users.

**Key Concept:** Use health-checked global load balancing for multi-region failover. See [CIS global load balancer pools](https://cloud.ibm.com/docs/cis?topic=cis-glb-features-pools).
</details>

---

### Question 27
**Scenario:** A downstream API has a brief outage. When it recovers, thousands of clients retry at the same instant and knock it over again. What client behaviour prevents this?

A. Retry immediately and as often as possible until the call succeeds
B. Retry at a fixed one-second interval for every client at the same time
C. Never retry, and return an error to the user on any first failure
D. Retry with exponential backoff, random jitter, and a capped retry count

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Exponential backoff spaces retries further apart, jitter spreads clients out so they do not retry in sync, and a cap stops endless retries. Immediate, unlimited retries create the retry storm. A fixed interval keeps clients synchronized. Never retrying turns brief blips into user-facing errors.

**Key Concept:** Retries must be bounded and desynchronized to avoid cascading failures. See [Addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/).
</details>

---

### Question 28
**Scenario:** A service peaks at 900 requests per second and runs evenly across three zones. It must keep serving peak traffic if any one zone fails. What is the minimum capacity each zone must handle?

A. 300 requests per second
B. 600 requests per second
C. 450 requests per second
D. 900 requests per second

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** If one zone fails, the remaining two zones must carry 900 requests per second between them, so each needs 450. Sizing each zone for 300 handles peak only when all three are up. 600 per zone is more than needed. 900 per zone would survive losing two zones, which is beyond the requirement and costs much more.

**Key Concept:** Plan capacity for N-1: peak load divided by the zones that remain after a failure. See [What is disaster recovery?](https://www.ibm.com/think/topics/disaster-recovery)
</details>

---

### Question 29
**Scenario:** A dashboard shows average API latency of 120 ms, well within target, yet users complain that some requests take several seconds. What should the team measure instead?

A. High percentiles such as p95 and p99, which show the slow tail of requests
B. The median latency only, since it ignores any unusual outlier requests
C. The minimum latency, which shows how fast the API can respond at best
D. The average latency measured over a longer window, such as a full day of traffic

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Averages hide the slow tail; p95 and p99 show what the slowest requests experience, which is what the complaints describe. The median also hides the tail. Minimum latency describes the best case. A longer averaging window smooths the problem away even more.

**Key Concept:** Use percentiles, not averages, for latency SLIs. See [Monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/).
</details>

---

### Question 30
**Scenario:** A Horizontal Pod Autoscaler set to scale on 70% CPU never scales the deployment, and its targets show `<unknown>`. The metrics server is running. What is the most likely cause?

A. The deployment has too few replicas for the autoscaler to start working
B. The pods have no CPU requests, so CPU utilization cannot be calculated
C. Autoscalers only work on StatefulSets, not on standard Deployments
D. The cluster is using more than one zone, which disables autoscaling

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CPU utilization targets are a percentage of each pod's CPU request; without requests, the autoscaler cannot compute utilization and shows `<unknown>`. Replica count does not block metrics. Autoscalers work with Deployments as well as StatefulSets. Multi-zone clusters support autoscaling.

**Key Concept:** Set resource requests; autoscaling and scheduling both depend on them. See [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/).
</details>

---

## Where to go deeper

- [IBM Cloud SRE cert page](../../exams/ibm/cloud-site-reliability-engineer/) - notes, practice plan, strategy
- [IBM Cloud Solution Architect practice questions](./ibm-cloud-solution-architect.md) - the design counterpart
- [Observability basics](../../learn/concepts/observability-basics.md) - the monitoring domain in plain English
- [SRE and reliability topic index](../../topics/sre-and-reliability.md) - SLOs and incident practice
- **[📖 IBM Training](https://www.ibm.com/training/)** - official certification pages
