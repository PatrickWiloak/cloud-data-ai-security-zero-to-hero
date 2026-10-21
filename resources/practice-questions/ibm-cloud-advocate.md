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

A. Virtualization only, because running many virtual machines on shared hardware is what defines a cloud service
B. Remote hosting of servers in a provider's data center that customers rent under a fixed multi-year contract
C. On-demand self-service, broad network access, resource pooling, rapid elasticity, and measured service
D. Containerization, because portable containers are what makes a service cloud

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** These are the five NIST characteristics, and they are what distinguish cloud from a hosted server you rent by the year. Measured service is the one that underpins consumption billing, which is the commercial change that follows from the technical one.
</details>

---

### Question 2
**Scenario:** A regulated bank must run workloads with dedicated, single-tenant hardware.

A. Dedicated or bare metal options within IBM Cloud, or IBM Cloud Satellite for distributed locations
B. Shared virtual servers on multi-tenant hosts, relying on hypervisor isolation to meet the single-tenant requirement
C. Public multi-tenant services only, since IBM Cloud offers no way to reserve hardware for a single customer
D. It is impossible in cloud

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Single-tenant isolation addresses regulatory requirements that forbid sharing physical hosts, and IBM's financial services focus is built around exactly this constraint. Satellite extends IBM Cloud services into other locations, including on-premises.
</details>

---

### Question 3
**Scenario:** IBM's confidential computing offering protects data while it is in use.

A. Firewalls and network security groups that filter traffic and block unauthorized connections before they reach the virtual servers
B. Hyper Protect services and Secure Execution, which protect data in use so even privileged operators cannot read it
C. TLS only, which encrypts data moving between the client and the server
D. Encryption at rest only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The three states are at rest, in transit, and in use, and the third is what confidential computing addresses through hardware-based isolation. This is IBM's most distinctive security positioning, so expect it on the exam.
</details>

---

### Question 4
**Scenario:** A customer must hold their own encryption keys such that IBM cannot access them.

A. Key Protect with provider-generated root keys, which IBM manages on shared multi-tenant infrastructure
B. No encryption, since customer data in IBM Cloud is protected by physical data center controls alone
C. Provider-managed keys, where IBM generates, stores, and rotates the keys on behalf of the customer
D. Keep Your Own Key with IBM Cloud Hyper Protect Crypto Services, backed by a dedicated HSM

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Key Protect is the multi-tenant managed key service; Hyper Protect Crypto Services adds a dedicated, customer-controlled HSM with the "keep your own key" property that IBM cannot access the key material. The distinction between the two is exactly the kind of thing this exam tests.
</details>

---

### Question 5
**Scenario:** Watson services are used in an application.

A. They are only for chatbots, such as the virtual assistant on a company website
B. They require training a model from scratch on the customer's own data before they return any result
C. They are consumable AI services (language, speech, and now watsonx foundation models) called through APIs
D. They run on-premises only, on IBM Z hardware installed in the customer's own data center

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The value is that AI capability arrives as an API rather than a research project. watsonx is the current generation, covering foundation models (watsonx.ai), data (watsonx.data), and governance (watsonx.governance).
</details>

---

### Question 6
**Scenario:** A workload must survive a zone failure.

A. One zone, sized with redundant power supplies and network cards
B. A larger server in the same zone, so that capacity is not exhausted
C. Deploy across multiple zones within a multi-zone region, with load balancing across the zones and replicated data
D. Backups only, with snapshots copied to another region to restore data after an outage

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Multi-zone regions are the standard availability construct: independent power, cooling, and networking with low-latency links between them. Backups address data loss but not availability, and a bigger single server has the same single failure domain.
</details>

---

### Question 7
**Scenario:** Which describes IBM Cloud's Kubernetes offering?

A. Serverless only, where Code Engine runs short-lived code and there is no cluster or container platform to use
B. Docker only, where containers are started by hand on individual virtual servers without any orchestration layer
C. Only self-managed Kubernetes, in which the customer installs and patches the control plane on virtual servers
D. IBM Cloud Kubernetes Service for managed upstream Kubernetes, and Red Hat OpenShift on IBM Cloud for the OpenShift platform

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The Red Hat relationship is central to IBM's hybrid cloud strategy: OpenShift gives one platform that runs on IBM Cloud, other clouds, and on-premises, which is the portability argument behind most IBM hybrid cloud proposals.
</details>

---

### Question 8
**Scenario:** Costs must be understood before deploying.

A. Costs are fixed, because IBM publishes one flat monthly price for each service that never changes over time
B. Use the cost estimator and pricing calculator, then set budgets and monitor usage against them
C. Ask support to quote the monthly bill after the workload has run for a full billing cycle
D. Deploy and see what the first invoice says, then resize any resources that turned out to be too costly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Estimating first and monitoring afterwards is the basic FinOps loop. Cloud spend surprises come from consumption dimensions people did not model, typically data egress, per-request charges, and resources nobody turned off.
</details>

---

### Question 9
**Scenario:** Access to IBM Cloud resources must follow least privilege.

A. IBM Cloud IAM with access groups, policies scoped to resource groups and services, and service IDs for applications
B. Shared credentials kept in a team vault, so every engineer can reach whichever resources they might need on a given day, without a ticket
C. No access control, because the account is private and only trusted employees know its URL
D. Give everyone administrator access to the account so that nobody is blocked while the project moves fast and deadlines loom

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Access groups are the manageable unit: assign policies to a group and manage membership rather than granting per user. Service IDs give applications their own identity, so an application's access does not depend on a person's account.
</details>

---

### Question 10
**Scenario:** An application should run without managing servers, billed per execution.

A. Virtual servers sized for peak load and billed for every hour they stay provisioned, busy or idle
B. IBM Cloud Code Engine, scaling to zero
C. A container registry that stores images and bills for the storage space that they use
D. Bare metal servers dedicated to the application and billed monthly regardless of the load they handle

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Code Engine runs containers, jobs, and functions with scale-to-zero and no cluster to operate, which fits intermittent workloads. The trade-off is cold start latency, which matters for user-facing endpoints and does not for background jobs.

**Key Concept:** [IBM Cloud Code Engine](https://www.ibm.com/products/code-engine)
</details>

---

### Question 11
**Scenario:** Compliance posture must be monitored continuously.

A. Manual spreadsheets updated by the security team each quarter after reviewing screenshots of the console and the ticket history
B. An annual audit by an external assessor who tests a sample of the controls once a year
C. IBM Cloud Security and Compliance Center, evaluating resources against profiles such as CIS or industry regulations
D. Trust the provider, since IBM's certifications already cover everything the customer configures

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Continuous evaluation catches drift between audits, which is when most non-compliance actually appears. It also produces evidence automatically, which is usually the most expensive part of an audit to assemble by hand.
</details>

---

### Question 12
**Scenario:** A migration approach must be chosen for a legacy application.

A. Always rewrite every application as cloud-native microservices before any of them are moved
B. Assess per application against the migration options: rehost, replatform, refactor, repurchase, retire, or retain
C. Never migrate, because legacy applications cannot run on cloud platforms in any supported form and must stay in the data center
D. Always lift and shift everything unchanged, because it is the fastest option and carries the lowest risk

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The right choice differs per application and depends on business value, technical debt, and remaining lifespan. Rewriting everything is the most expensive default, and lifting and shifting everything unchanged carries the technical debt into a more expensive place.
</details>

---

### Question 13
**Scenario:** Hybrid cloud is described.

A. On-premises infrastructure combined with public cloud, managed consistently with portable workloads
B. Multiple regions of one public cloud provider, linked together to improve availability and latency for users
C. Private cloud only
D. Two public clouds from different providers, used side by side for different workloads

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** IBM's positioning treats hybrid as the normal end state rather than a transition, which is why OpenShift and Satellite matter to them. Multicloud is the related but distinct term for using several public providers.
</details>

---

### Question 14
**Scenario:** Object storage is needed for backups and static content.

A. IBM Cloud Object Storage with storage classes matched to access frequency
B. Block storage volumes attached to virtual servers, which suits databases that need low-latency disks
C. A database service with tables and indexes, billed by provisioned capacity and I/O
D. File storage mounted over NFS by many servers, which suits shared application data

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Object storage is the durable, scalable choice for unstructured data, and matching class to access frequency is the main cost lever. Block storage attaches to a single instance and file storage provides shared POSIX access, both of which cost more per gigabyte.
</details>

---

### Question 15
**Scenario:** The shared responsibility model in IBM Cloud.

A. IBM is responsible for everything in the account, including customer data, who is given access to it, and the applications
B. There is no model; each IBM Cloud service defines its own contract and the customer has no duties
C. The customer is responsible for everything, including the physical data centers, hardware, and network
D. IBM secures the cloud infrastructure; the customer owns data, identities, and access

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The customer always owns data and identity regardless of service model. What shifts between IaaS, PaaS, and SaaS is who patches the operating system and runtime, and misreading that boundary is the most common source of cloud misconfiguration.
</details>

---

## Where to go deeper

- [IBM Cloud Advocate cert page](../../exams/ibm/cloud-advocate/) - notes, practice plan, strategy
- [IBM Cloud Solution Architect practice questions](./ibm-cloud-solution-architect.md) - the architecture level
- [What is cloud computing?](../../learn/concepts/what-is-cloud-computing.md) - plain-English foundation
- [Shared responsibility model](https://security.noblerworks.com/learn/concepts/shared-responsibility-model/) - question 15 in depth
- **[📖 IBM Training](https://www.ibm.com/training/)** - official certification pages
