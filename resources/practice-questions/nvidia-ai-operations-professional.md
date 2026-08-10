---
last-updated: 2026-08-09
difficulty: advanced
---

# NVIDIA Certified Professional - AI Operations (NCP-AIO) - Practice Questions

15 questions for NCP-AIO prep, evenly weighted across MLOps and model lifecycle, deployment and serving, GPU monitoring with DCGM, fleet management, and incident response (20% each).

> **Cert page:** [exams/nvidia/ai-operations-professional/](../../exams/nvidia/ai-operations-professional/)

---

### Question 1
**Scenario:** A model in production must be traceable back to the exact code, data, and hyperparameters that produced it.

A. A model registry entry linking the artifact to its training run, dataset version, and container image digest
B. A note in the wiki
C. The filename
D. The deployment date

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Lineage is what makes rollback and incident investigation possible, and it must be captured automatically at training time rather than reconstructed later. Pinning the container image by digest rather than tag closes the last mutable link in the chain.
</details>

---

### Question 2
**Scenario:** Triton must serve two model versions simultaneously so traffic can be shifted gradually.

A. Two separate servers
B. A model repository with both versions and a version policy, fronted by traffic splitting
C. Restart with the new version
D. Only the latest version can be served

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Triton's model repository supports multiple versions per model with a configurable version policy, so both can be loaded at once. Combined with a router or service mesh doing the split, this gives canary deployment without duplicating the serving infrastructure.
</details>

---

### Question 3
**Scenario:** DCGM should detect a degrading GPU before it fails a production job.

A. Run DCGM diagnostics on a schedule and alert on health checks, XID errors, thermal throttling, and remapped rows
B. Wait for job failures
C. Monitor CPU only
D. Check quarterly

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** DCGM exposes health watches and a diagnostic suite at several levels, and XID error codes identify specific fault classes. Proactive detection lets you drain the node during a maintenance window instead of losing a multi-day training run.
</details>

---

### Question 4
**Scenario:** An inference service must meet a p99 latency SLO under variable load.

A. Size for average load
B. Define the SLO, measure p99 not mean, autoscale on a queue or latency signal, and reserve headroom for the tail
C. Increase batch size indefinitely
D. Use a larger model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Averages hide the tail that users actually experience, and larger batches trade latency for throughput, which pushes p99 the wrong way. Scaling on queue depth or latency responds faster than CPU or GPU utilization for serving workloads.
</details>

---

### Question 5
**Scenario:** Model accuracy in production degrades although the model file has not changed.

A. Data drift or concept drift: monitor input distributions and outcome metrics, and trigger retraining
B. The GPU is broken
C. The container is corrupt
D. The network is slow

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The world moves even when the artifact does not. Monitoring input feature distributions catches data drift, and tracking realized outcomes against predictions catches concept drift. Without both, the first signal is a business metric moving months later.
</details>

---

### Question 6
**Scenario:** Driver versions have diverged across a 200-node fleet.

A. Fix them one at a time by hand
B. Manage drivers declaratively (GPU Operator or configuration management), enforce a supported version policy, and roll upgrades in waves
C. Ignore the divergence
D. Reinstall the operating system everywhere

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Divergence produces failures that reproduce on some nodes and not others, which is the most expensive kind to debug. Declarative management makes the fleet converge and makes drift visible. Wave-based rollout limits the blast radius of a bad driver.
</details>

---

### Question 7
**Scenario:** A CI pipeline for models should gate promotion to production.

A. Automated tests: data validation, training reproducibility, evaluation against a threshold, and a canary before full rollout
B. Manual approval only
C. Deploy on merge with no checks
D. Test in production

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The distinctive part of ML CI is that the artifact depends on data, so data validation and an evaluation gate sit alongside ordinary code tests. Manual approval without evidence is a rubber stamp, and the canary catches what offline evaluation cannot.
</details>

---

### Question 8
**Scenario:** An incident occurs: inference errors spike at 03:00.

A. Restart everything
B. Follow the incident process: assess impact against the SLO, mitigate (roll back to the last known good version), then investigate root cause
C. Wait for business hours
D. Retrain the model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Mitigation precedes diagnosis: the fastest path back to a working service is usually rollback, and root cause analysis is done after users are safe. Retraining during an incident is the slowest possible response and often is not the cause.
</details>

---

### Question 9
**Scenario:** GPU utilization on the serving fleet averages 20%.

A. Leave it, headroom is good
B. Consolidate with MIG or multi-model serving, right-size instances, and use autoscaling so idle capacity shrinks
C. Add more GPUs
D. Increase the model size

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Persistent low utilization is money spent on idle silicon. MIG or Triton's concurrent model execution packs several models onto one GPU, and scaling policies release capacity off-peak. Keep enough headroom for the tail, but 20% average is far past that.
</details>

---

### Question 10
**Scenario:** Which metric best indicates that an inference server is saturated?

A. GPU temperature
B. Queue delay and its effect on end-to-end latency
C. Disk usage
D. Model file size

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Triton reports queue duration separately from compute duration, which cleanly distinguishes "the model is slow" from "there is more work arriving than capacity to do it." Those two lead to different fixes: optimize the model, or add replicas.
</details>

---

### Question 11
**Scenario:** A disaster recovery plan is needed for an inference service in one region.

A. Backups only
B. A second region with the model registry replicated and deployment automation tested, plus a documented and rehearsed failover
C. A runbook that has never been executed
D. Rely on the cloud provider

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** DR is only real if it has been exercised: an untested runbook reliably fails on a dependency nobody remembered, such as the registry, secrets, or DNS. Model artifacts and the deployment pipeline both need to exist in the second region before the incident.
</details>

---

### Question 12
**Scenario:** Compliance requires knowing which model version produced a given prediction six months ago.

A. Log the model name, version, and input and output identifiers with each inference, retained per the policy
B. Store predictions only
C. Rely on the deployment history
D. Nothing is needed

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Correlating a prediction to a version requires the version to be recorded at request time. Deployment history tells you what was live in a window, which breaks down during canaries when two versions serve simultaneously.
</details>

---

### Question 13
**Scenario:** A model update must be rolled back quickly if error rates rise.

A. Keep the previous version loaded and shift traffic back, with an automated rollback trigger on the error-rate SLO
B. Rebuild the old model from source
C. Restore from backup
D. Retrain

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Rollback speed is set by whether the previous artifact is already loaded and routable. Rebuilding or restoring turns a 30-second recovery into hours. Automating the trigger removes the human latency during the window that matters most.
</details>

---

### Question 14
**Scenario:** Multiple teams share a GPU cluster and cost must be attributed.

A. Label workloads by team and namespace, collect GPU-hours per label from DCGM and the scheduler, and report showback or chargeback
B. Split the bill evenly
C. Estimate from headcount
D. Do not attribute costs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Attribution needs a label applied at submission time and metrics keyed by it, which is a policy decision as much as a technical one. Even splits remove any incentive to release idle capacity, which is where most GPU waste comes from.
</details>

---

### Question 15
**Scenario:** A post-incident review is scheduled after a serving outage.

A. Identify who caused it
B. Establish the timeline, contributing factors, and detection and mitigation gaps, then produce specific action items with owners
C. Close the ticket
D. Add more monitoring dashboards generally

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Blameless review focuses on the conditions that let the failure happen and stay undetected. The output that matters is a small number of specific, owned actions, most often a missing alert, a missing guardrail, or a rollback path that was slower than assumed.
</details>

---

## Where to go deeper

- [NCP-AIO cert page](../../exams/nvidia/ai-operations-professional/) - notes, practice plan, strategy
- [NCP-AII practice questions](./nvidia-ai-infrastructure-professional.md) - the infrastructure counterpart
- [Observability basics](../../learn/concepts/observability-basics.md) - the monitoring foundation
- [SRE and reliability topic index](../../topics/sre-and-reliability.md) - SLOs and incident practice
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
