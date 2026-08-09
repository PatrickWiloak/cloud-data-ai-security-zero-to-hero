---
last-updated: 2026-08-09
difficulty: beginner
---

# IBM Cloud Advocate - Practice Questions

15 questions for IBM Cloud Advocate prep, weighted toward the IBM Cloud platform and services (30%), security and compliance (20%), then cloud concepts, HA and DR, cost management, and migration.

> **Cert page:** [exams/ibm/cloud-advocate/](../../exams/ibm/cloud-advocate/)

---

### Question 1
**Scenario:** Which describes the essential characteristics of cloud computing?

A. Virtualization only
B. On-demand self-service, broad network access, resource pooling, rapid elasticity, and measured service
C. Remote hosting
D. Containerization

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** These are the five NIST characteristics, and they are what distinguish cloud from a hosted server you rent by the year. Measured service is the one that underpins consumption billing, which is the commercial change that follows from the technical one.
</details>

---

### Question 2
**Scenario:** A regulated bank must run workloads with dedicated, single-tenant hardware.

A. Public multi-tenant only
B. Dedicated or bare metal options within IBM Cloud, or IBM Cloud Satellite for distributed locations
C. It is impossible in cloud
D. Shared virtual servers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Single-tenant isolation addresses regulatory requirements that forbid sharing physical hosts, and IBM's financial services focus is built around exactly this constraint. Satellite extends IBM Cloud services into other locations, including on-premises.
</details>

---

### Question 3
**Scenario:** IBM's confidential computing offering protects data while it is in use.

A. Encryption at rest only
B. Hyper Protect services and Secure Execution, which protect data in use so even privileged operators cannot read it
C. TLS only
D. Firewalls

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The three states are at rest, in transit, and in use, and the third is what confidential computing addresses through hardware-based isolation. This is IBM's most distinctive security positioning, so expect it on the exam.
</details>

---

### Question 4
**Scenario:** A customer must hold their own encryption keys such that IBM cannot access them.

A. Provider-managed keys
B. Keep Your Own Key with IBM Cloud Hyper Protect Crypto Services, backed by a dedicated HSM
C. No encryption
D. Key Protect only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Key Protect is the multi-tenant managed key service; Hyper Protect Crypto Services adds a dedicated, customer-controlled HSM with the "keep your own key" property that IBM cannot access the key material. The distinction between the two is exactly the kind of thing this exam tests.
</details>

---

### Question 5
**Scenario:** Watson services are used in an application.

A. They require training a model from scratch
B. They are consumable AI services (language, speech, and now watsonx foundation models) called through APIs
C. They are only for chatbots
D. They run on-premises only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The value is that AI capability arrives as an API rather than a research project. watsonx is the current generation, covering foundation models (watsonx.ai), data (watsonx.data), and governance (watsonx.governance).
</details>

---

### Question 6
**Scenario:** A workload must survive a zone failure.

A. One zone
B. Deploy across multiple zones within a multi-zone region, with load balancing across them
C. Backups only
D. A larger server

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multi-zone regions are the standard availability construct: independent power, cooling, and networking with low-latency links between them. Backups address data loss but not availability, and a bigger single server has the same single failure domain.
</details>

---

### Question 7
**Scenario:** Which describes IBM Cloud's Kubernetes offering?

A. Only self-managed Kubernetes
B. IBM Cloud Kubernetes Service for managed upstream Kubernetes, and Red Hat OpenShift on IBM Cloud for the OpenShift platform
C. Docker only
D. Serverless only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Red Hat relationship is central to IBM's hybrid cloud strategy: OpenShift gives one platform that runs on IBM Cloud, other clouds, and on-premises, which is the portability argument behind most IBM hybrid cloud proposals.
</details>

---

### Question 8
**Scenario:** Costs must be understood before deploying.

A. Deploy and see
B. Use the cost estimator and pricing calculator, then set budgets and monitor usage against them
C. Ask support
D. Costs are fixed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Estimating first and monitoring afterwards is the basic FinOps loop. Cloud spend surprises come from consumption dimensions people did not model, typically data egress, per-request charges, and resources nobody turned off.
</details>

---

### Question 9
**Scenario:** Access to IBM Cloud resources must follow least privilege.

A. Give everyone administrator
B. IBM Cloud IAM with access groups, policies scoped to resource groups and services, and service IDs for applications
C. Shared credentials
D. No access control

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Access groups are the manageable unit: assign policies to a group and manage membership rather than granting per user. Service IDs give applications their own identity, so an application's access does not depend on a person's account.
</details>

---

### Question 10
**Scenario:** An application should run without managing servers, billed per execution.

A. Virtual servers
B. IBM Cloud Code Engine or Cloud Functions, scaling to zero when idle
C. Bare metal
D. A container registry

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Code Engine runs containers, jobs, and functions with scale-to-zero and no cluster to operate, which fits intermittent workloads. The trade-off is cold start latency, which matters for user-facing endpoints and does not for background jobs.
</details>

---

### Question 11
**Scenario:** Compliance posture must be monitored continuously.

A. An annual audit
B. IBM Cloud Security and Compliance Center, evaluating resources against profiles such as CIS or industry regulations
C. Manual spreadsheets
D. Trust the provider

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Continuous evaluation catches drift between audits, which is when most non-compliance actually appears. It also produces evidence automatically, which is usually the most expensive part of an audit to assemble by hand.
</details>

---

### Question 12
**Scenario:** A migration approach must be chosen for a legacy application.

A. Always rewrite
B. Assess per application against the migration options: rehost, replatform, refactor, repurchase, retire, or retain
C. Always lift and shift
D. Never migrate

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The right choice differs per application and depends on business value, technical debt, and remaining lifespan. Rewriting everything is the most expensive default, and lifting and shifting everything carries the technical debt into a more expensive place.
</details>

---

### Question 13
**Scenario:** Hybrid cloud is described.

A. Two public clouds
B. An architecture combining on-premises infrastructure with public cloud, with workload portability and consistent management across them
C. Private cloud only
D. Multiple regions

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** IBM's positioning treats hybrid as the normal end state rather than a transition, which is why OpenShift and Satellite matter to them. Multicloud is the related but distinct term for using several public providers.
</details>

---

### Question 14
**Scenario:** Object storage is needed for backups and static content.

A. Block storage
B. IBM Cloud Object Storage with storage classes matched to access frequency
C. File storage
D. A database

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Object storage is the durable, scalable choice for unstructured data, and matching class to access frequency is the main cost lever. Block storage attaches to a single instance and file storage provides shared POSIX access, both of which cost more per gigabyte.
</details>

---

### Question 15
**Scenario:** The shared responsibility model in IBM Cloud.

A. IBM is responsible for everything
B. IBM secures the cloud infrastructure; the customer remains responsible for data, identities, access configuration, and application security, with the boundary shifting by service model
C. The customer is responsible for everything
D. There is no model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The customer always owns data and identity regardless of service model. What shifts between IaaS, PaaS, and SaaS is who patches the operating system and runtime, and misreading that boundary is the most common source of cloud misconfiguration.
</details>

---

## Where to go deeper

- [IBM Cloud Advocate cert page](../../exams/ibm/cloud-advocate/) - notes, practice plan, strategy
- [IBM Cloud Solution Architect practice questions](./ibm-cloud-solution-architect.md) - the architecture level
- [What is cloud computing?](../../learn/concepts/what-is-cloud-computing.md) - plain-English foundation
- [Shared responsibility model](../../learn/concepts/shared-responsibility-model.md) - question 15 in depth
- **[📖 IBM Training](https://www.ibm.com/training/)** - official certification pages
