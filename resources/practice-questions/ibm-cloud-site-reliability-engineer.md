---
last-updated: 2026-08-09
difficulty: advanced
---

# IBM Cloud Site Reliability Engineer - Practice Questions

15 questions for this exam, weighted toward monitoring and observability (25%), incident management (20%), automation and IaC (20%), then availability, capacity, and Kubernetes operations.

> **Cert page:** [exams/ibm/cloud-site-reliability-engineer/](../../exams/ibm/cloud-site-reliability-engineer/)

---

### Question 1
**Scenario:** An SLI, an SLO, and an SLA must be distinguished.

A. They are the same
B. The SLI is the measurement, the SLO is the internal target for it, and the SLA is the external contract with consequences
C. The SLA is internal
D. The SLO is a measurement

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SLOs should be tighter than SLAs so you notice before you breach the contract. The practical output of an SLO is the error budget, which converts reliability from an argument into an arithmetic question about how much budget remains.
</details>

---

### Question 2
**Scenario:** An error budget is exhausted mid-quarter.

A. Continue shipping features
B. Prioritize reliability work until the budget recovers, per the agreed policy
C. Raise the SLO
D. Stop measuring

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The budget policy is agreed in advance precisely so the decision is not relitigated under pressure. Raising the SLO to make the number look better is the failure mode that makes the whole practice performative.
</details>

---

### Question 3
**Scenario:** A distributed request must be followed across six services.

A. Logs from each service
B. Distributed tracing with context propagated across service boundaries, ideally with OpenTelemetry
C. Metrics only
D. Ask each team

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Traces show where the latency actually went, which logs cannot without manual correlation. The requirement people underestimate is propagation: every service must forward the trace context, or the trace fragments into disconnected pieces.
</details>

---

### Question 4
**Scenario:** Alerts wake the on-call engineer several times a night for conditions that self-resolve.

A. Ignore the alerts
B. Alert on symptoms that affect users and are actionable, add duration conditions, and delete alerts nobody acts on
C. Add more alerts
D. Increase the on-call rotation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Every page should correspond to something a human must do now. Alerts on causes rather than symptoms generate noise, and a self-resolving condition is by definition not one that needed a human. Alert fatigue causes real incidents to be missed.
</details>

---

### Question 5
**Scenario:** A postmortem is written after a major incident.

A. Identify who made the mistake
B. Blameless analysis of the timeline, contributing factors, and detection and mitigation gaps, producing owned action items
C. Close the ticket
D. Add a dashboard

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Blame suppresses the information you need, because people stop reporting near misses. The output that matters is a small number of specific actions with owners; a long list nobody owns is the same as no actions.
</details>

---

### Question 6
**Scenario:** Infrastructure changes must be repeatable and reviewable.

A. Console changes with notes
B. Infrastructure as code in version control, applied through a pipeline with plan review
C. Shell scripts run by hand
D. A runbook

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** IaC gives review, history, and rollback for infrastructure, and applying through a pipeline means the same process every time regardless of who is on call. Console changes are invisible to the next person and cause drift from the declared state.
</details>

---

### Question 7
**Scenario:** Toil is consuming most of the team's time.

A. Hire more people
B. Measure the toil, then automate the highest-volume repetitive tasks, capping toil as a share of time
C. Work longer hours
D. Accept it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Adding people to unbounded toil scales the problem rather than solving it. Capping toil as a share of the team's time creates the space to automate, which is the mechanism that makes the reduction actually happen.
</details>

---

### Question 8
**Scenario:** A Kubernetes deployment must survive a node failure without dropping requests.

A. One replica
B. Multiple replicas spread across nodes and zones with anti-affinity, plus a PodDisruptionBudget and correct readiness probes
C. A larger node
D. Restart on failure

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spreading covers the failure, the PDB protects against voluntary disruptions such as node drains removing too many at once, and readiness probes keep traffic off pods that are not serving. Missing the last one causes errors during every rollout.
</details>

---

### Question 9
**Scenario:** Capacity planning is needed for a growing service.

A. React when it breaks
B. Model demand growth against measured headroom, load test to find the actual limit, and plan lead times for capacity that cannot be added instantly
C. Over-provision heavily
D. Autoscaling handles everything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Autoscaling handles variation within a provisioned envelope; it does not handle quota limits, license ceilings, or a dependency that cannot scale. Knowing the real breaking point, from testing rather than extrapolation, is what makes the plan credible.
</details>

---

### Question 10
**Scenario:** Chaos engineering is proposed.

A. Randomly break production immediately
B. Form a hypothesis about steady state, run a small controlled experiment with a blast radius limit and an abort condition, then widen as confidence grows
C. Only test in development
D. It is too risky to attempt

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** It is an experiment, not vandalism: you predict what should happen, verify the system behaves as designed, and learn when it does not. The blast radius limit and abort condition are what make running it in production defensible.
</details>

---

### Question 11
**Scenario:** A deployment must be rolled back quickly if error rates rise.

A. Fix forward always
B. Automated rollback triggered by SLI-based canary analysis, with the previous version still available
C. Manual investigation first
D. Wait for user reports

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Rollback speed is set in advance by whether the previous version is still deployable and whether the trigger is automatic. Fixing forward is reasonable when the fix is trivial and understood, but it should be the exception rather than the plan.
</details>

---

### Question 12
**Scenario:** A dependency's failure must not cascade.

A. Retry indefinitely
B. Timeouts, bounded retries with exponential backoff and jitter, circuit breakers, and a defined degraded behavior
C. No timeouts
D. Fail the whole request always

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Unbounded retries turn a slow dependency into an outage by exhausting connections and amplifying load, and synchronized retries create thundering herds, which is why jitter matters. Deciding what degraded looks like is a product decision made before the incident.
</details>

---

### Question 13
**Scenario:** Logs are expensive and voluminous.

A. Stop logging
B. Structure logs, set levels appropriately, sample high-volume events, and tier retention so recent data is queryable and older data is archived
C. Keep everything at debug forever
D. Log only errors

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Structured logs make sampling and querying possible, which is what lets you cut volume without losing the ability to investigate. Logging only errors removes the context around the error, which is usually where the cause is visible.
</details>

---

### Question 14
**Scenario:** Backups exist but recovery has never been tested.

A. Backups are sufficient
B. Test restores on a schedule, measure the actual recovery time against the RTO, and fix what the test reveals
C. Trust the backup job status
D. Increase the backup frequency

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A successful backup job proves data was written, not that it can be read back into a working system. The failures that surface in a restore test are missing keys, incompatible versions, and a recovery time several times longer than anyone assumed.
</details>

---

### Question 15
**Scenario:** On-call must be sustainable.

A. One person permanently
B. A rotation with reasonable frequency, clear escalation, current runbooks, handover, and a limit on pages per shift that triggers investigation when exceeded
C. Everyone on call all the time
D. No on-call

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Sustainability is a reliability control, not a perk: an exhausted engineer makes worse decisions during the incident that matters. Treating a high page count as a defect to investigate is what keeps the rotation from degrading over time.
</details>

---

## Where to go deeper

- [IBM Cloud SRE cert page](../../exams/ibm/cloud-site-reliability-engineer/) - notes, practice plan, strategy
- [IBM Cloud Solution Architect practice questions](./ibm-cloud-solution-architect.md) - the design counterpart
- [Observability basics](../../learn/concepts/observability-basics.md) - the monitoring domain in plain English
- [SRE and reliability topic index](../../topics/sre-and-reliability.md) - SLOs and incident practice
- **[📖 IBM Training](https://www.ibm.com/training/)** - official certification pages
