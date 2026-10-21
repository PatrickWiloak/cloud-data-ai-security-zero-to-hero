---
last-updated: 2026-08-09
difficulty: intermediate
---

# CompTIA Cloud+ (CV0-004) - Practice Questions

15 questions for Cloud+ prep across cloud architecture, deployment, operations, security, and troubleshooting.

Cloud+ is vendor-neutral, so answers describe concepts rather than a specific provider's service names.

> **Cert page:** [exams/comptia/cloud-plus/](../../exams/comptia/cloud-plus/)

---

### Question 1
**Scenario:** A workload has a predictable baseline plus unpredictable spikes.

A. Provision the minimum
B. Provision for the peak permanently so no spike ever causes a capacity shortfall or latency
C. Provision the average
D. Provision the baseline with a committed discount and use autoscaling for spikes

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Splitting baseline from burst captures the discount on predictable usage while keeping elasticity for peaks. Provisioning for the average is the worst option: it fails during every spike while still paying for idle capacity off-peak.
</details>

---

### Question 2
**Scenario:** A migration approach must be chosen for a legacy application.

A. Always retire any application older than five years, since legacy systems carry the most technical debt
B. Assess per application: rehost, replatform, refactor, repurchase, retire, or retain
C. Always refactor every application into cloud-native microservices before moving anything to the cloud
D. Always rehost every application as is, so that no code changes are needed before the cutover

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The six R's are a per-application decision driven by business value, technical debt, and remaining lifespan. Rehosting everything carries the debt into a more expensive place; refactoring everything is the most expensive default.
</details>

---

### Question 3
**Scenario:** A VM template must be produced so every instance starts identically.

A. Clone a running production instance and edit its settings by hand after each launch
B. A documentation page
C. A golden image built by an automated pipeline, versioned and rebuilt on a patching cadence
D. Configure each instance by hand

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Images built by a pipeline are reproducible and auditable; manual builds embed whatever was on the machine that day. The operational detail people miss is the rebuild cadence: in an immutable model, the pipeline is how patching happens.
</details>

---

### Question 4
**Scenario:** Storage must be shared by many instances with file semantics.

A. File storage (NFS or SMB)
B. Local ephemeral disk
C. Object storage
D. Block storage attached read-write to every instance, each mounting it with its own local file system

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Block attaches to one instance like a disk, file provides concurrent POSIX or SMB access, and object is API-accessed with no file semantics. Matching the storage type to the access pattern is a recurring Cloud+ question shape.
</details>

---

### Question 5
**Scenario:** Data must survive the loss of a whole availability zone.

A. RAID 10 across several disks within one zone, which protects against drive failures and gives fast rebuilds
B. Replication across zones or regions, plus backups tested by restore
C. A larger disk
D. Snapshots taken every hour and stored in the same zone as the volume they protect

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RAID and same-zone snapshots protect against device failure, not zone failure. The other half is the restore test: a backup that has never been restored is an assumption, and its failures surface during the incident.
</details>

---

### Question 6
**Scenario:** Costs are rising and the cause is unclear.

A. Estimate from headcount
B. Reduce all resources
C. Tag resources consistently, analyze cost by tag and service, then act on the largest contributors
D. Cancel unused accounts

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Attribution before action, because cost is normally concentrated in a few resources. Tag enforcement at creation matters, since coverage decays otherwise and untagged spend becomes invisible to the analysis.
</details>

---

### Question 7
**Scenario:** An application tier must not be reachable from the internet.

A. A strong password on every account, plus key-only SSH login and MFA on each instance
B. A host firewall rule on each instance that drops inbound traffic except on port 443
C. A public IP with an allowlist of approved source addresses on the instance's security group
D. A private subnet with no internet gateway route, using NAT for outbound only

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Routing is the structural control and security groups are the filter on top. NAT permits outbound-initiated traffic while blocking inbound. An allowlisted public IP is still internet-reachable and depends on the list staying correct.
</details>

---

### Question 8
**Scenario:** Identity and access must follow least privilege across teams.

A. Role-based groups, per-service scoping, MFA on privileged accounts, and periodic review
B. Full access for every engineer on request, with all activity logged and reviewed after the fact
C. One shared administrator account whose password the team lead rotates every month and stores in a vault
D. Individual permissions per user, granted on request by the team lead and recorded in a shared tracking spreadsheet

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Groups make joiners and leavers a membership change rather than a permission audit. Shared accounts destroy attribution, which is the first thing an incident investigation needs. Access review is what catches privilege creep.
</details>

---

### Question 9
**Scenario:** Encryption keys must be under organizational control.

A. Provider-managed keys only, because the provider rotates them automatically and handles all key storage
B. Customer-managed keys in a key management service, with rotation and audit logging
C. Keys in application configuration
D. No encryption, relying on network isolation and access controls to protect the stored data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Customer-managed keys give revocation and an audit trail, which is usually what the compliance requirement actually means. Keys in configuration files are the anti-pattern: they leak through repositories, images, and backups.
</details>

---

### Question 10
**Scenario:** Capacity planning for a growing service.

A. Trend historical utilization, model growth, load test to find the limit, and plan for lead times
B. Rely entirely on autoscaling, since it adds instances automatically whenever demand rises beyond the current capacity
C. React when it breaks
D. Over-provision heavily from day one so that no load test, forecast or lead-time planning is ever required of the team

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Autoscaling handles variation within a provisioned envelope but not quota ceilings, license limits, or a dependency that cannot scale. Knowing the measured breaking point, rather than the extrapolated one, is what makes the plan credible.
</details>

---

### Question 11
**Scenario:** A deployment must be reversible if it goes wrong.

A. A strategy with a rollback path: blue-green, canary, or rolling with health-gated progression
B. Deploy and hope
C. Deploy at night
D. Notify users first, with a maintenance banner posted a day before

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Blue-green swaps whole environments so rollback is a traffic switch; canary exposes a small share first; rolling replaces gradually. All three require health checks that actually detect failure, or the automation happily rolls out a broken version.
</details>

---

### Question 12
**Scenario:** An instance is unreachable and the cause is unknown.

A. Restart the instance's network service and the virtual router, then retest from the same client; repeat until it responds
B. Rebuild the instance from the template and retest, since that is the quickest way to rule out its configuration
C. Contact the provider first and wait for its support team to diagnose the instance before anyone touches anything
D. Work the layers: instance state and console output, then routing and security groups, then the app

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Systematic layer-by-layer isolation is the Cloud+ troubleshooting method, and it is faster than guessing because each step eliminates a category. Rebuilding destroys the evidence and often recreates the same misconfiguration.
</details>

---

### Question 13
**Scenario:** Monitoring must detect problems before users do.

A. Log everything with no alerts
B. Check the dashboards at the start of each shift and escalate anything that looks abnormal to the team lead by email
C. Metrics with alerting on user-affecting symptoms, log aggregation, synthetic checks, and an escalation path
D. Alert on every metric

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Alerting on symptoms rather than causes is what keeps pages actionable; alerting on every metric produces fatigue and missed real incidents. Synthetic checks give the outside-in view that internal metrics cannot.
</details>

---

### Question 14
**Scenario:** A compliance requirement mandates data stay within a country.

A. Use a CDN
B. Select in-region services and restrict replication, backup, and DR targets to that jurisdiction
C. Add a policy document
D. Encrypt the data with customer-managed keys, which satisfies residency because only the key holder can read it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Residency leaks through the paths nobody chose deliberately: cross-region backups, DR replicas, and telemetry. Verifying each is what turns a residency claim into something defensible.
</details>

---

### Question 15
**Scenario:** Infrastructure must be reproducible across environments.

A. Screenshots
B. Runbooks with detailed console steps, reviewed every quarter and kept on the team wiki for each environment
C. Infrastructure as code in version control, deployed by a pipeline with environment parameters
D. A configuration spreadsheet listing every setting per environment, kept up to date by hand after each change

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** IaC gives review, history, and rollback for infrastructure, and it is the precondition for any credible disaster recovery plan, because the second region must be buildable. Console-driven environments drift and cannot be verified.
</details>

---

## Where to go deeper

- [Cloud+ cert page](../../exams/comptia/cloud-plus/) - notes, practice plan, strategy
- [Security+ practice questions](https://security.noblerworks.com/resources/practice-questions/comptia-security-plus/) - the security sibling
- [AWS Cloud Practitioner practice questions](./aws-cloud-practitioner.md) - a vendor-specific view of the same concepts
- [What is cloud computing?](../../learn/concepts/what-is-cloud-computing.md) - plain-English foundation
- **[📖 CompTIA Cloud+](https://www.comptia.org/certifications/cloud)** - official exam objectives
