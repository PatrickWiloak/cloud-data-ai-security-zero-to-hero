---
last-updated: 2026-08-09
difficulty: beginner
---

# Oracle Cloud Infrastructure Foundations (1Z0-1085) - Practice Questions

15 questions for OCI Foundations prep, weighted toward OCI architecture and core services (30%), security and identity (20%), then compute, storage, and networking (15% each).

> **Cert page:** [exams/oracle/oci-foundations/](../../exams/oracle/oci-foundations/)

---

### Question 1
**Scenario:** What is an OCI availability domain?

A. A compartment
B. One or more data centers within a region, isolated from other availability domains
C. A geographic region, such as us-ashburn-1, that contains several data centers connected by a low-latency network
D. A subnet inside a VCN, defined by a CIDR block and tied to a single availability domain or region

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A region contains one or more availability domains, and each AD has independent power, cooling, and network. Some regions have a single AD, which is why fault domains matter: they provide isolation within an AD when only one exists.
</details>

---

### Question 2
**Scenario:** What is a fault domain?

A. A hardware grouping in an availability domain that isolates failures
B. A network gateway that links an availability domain to the on-premises network and fails over automatically to a standby path in another region
C. A separate region that serves as the disaster recovery partner of the primary region
D. A billing unit

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Each AD has three fault domains, and distributing instances across them protects against hardware failure and maintenance within the AD. In a single-AD region, fault domains are the only intra-region isolation available.
</details>

---

### Question 3
**Scenario:** Resources must be organized for access control and cost tracking.

A. Tags only
B. Regions, because each region can hold its own resources and show a separate line on the cost report
C. Compartments, which are logical containers with their own IAM policies and cost reporting
D. Separate VCNs for each team, each with its own subnets, security lists, route tables and gateways

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Compartments are OCI's distinctive organizing construct: a resource lives in exactly one compartment, policies are written against compartments, and cost can be reported per compartment. They can nest, which supports an organizational hierarchy.
</details>

---

### Question 4
**Scenario:** An OCI IAM policy statement's structure.

A. A JSON document
B. A tag
C. A role assignment only
D. `allow <subject> to <verb> <resource-type> in <location> [where <conditions>]`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** OCI policies are human-readable statements, for example `Allow group Admins to manage all-resources in compartment Dev`. The verbs escalate as inspect, read, use, and manage, which is the granularity you tune for least privilege.
</details>

---

### Question 5
**Scenario:** Which storage type suits large volumes of unstructured data such as backups and media?

A. Block Volume, attached to one instance at a time as a disk
B. Object Storage, with standard and archive tiers
C. Local NVMe storage on the instance's host, lost when it stops
D. File Storage, mounted over NFS by each instance, which suits shared home directories and application files

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Object Storage is durable, effectively unlimited, and accessed by API. Block Volume attaches to a single instance like a disk, File Storage provides shared NFS access, and local NVMe is ephemeral and disappears with the instance.
</details>

---

### Question 6
**Scenario:** Instances in a private subnet must reach the internet for updates.

A. A NAT gateway
B. An internet gateway
C. A service gateway to OCI services
D. A dynamic routing gateway attached to the VCN, with a route rule sending 0.0.0.0/0 to it

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** NAT allows outbound-initiated traffic and blocks inbound. The internet gateway is for public subnets in both directions, the service gateway reaches OCI services privately, and the DRG connects to on-premises or other VCNs.
</details>

---

### Question 7
**Scenario:** A VCN must reach Object Storage without traversing the internet.

A. A local peering gateway to the Object Storage service network, with a route rule for its CIDR
B. A service gateway with the service CIDR label
C. An internet gateway with a public IP on each instance
D. A NAT gateway with a route rule to the Object Storage endpoint

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The service gateway keeps traffic to OCI services on the Oracle network and avoids NAT charges. Distinguishing the four gateway types by purpose is one of the most reliably examined topics on OCI Foundations.
</details>

---

### Question 8
**Scenario:** A database should require no manual patching, tuning, or backup configuration.

A. A database on a compute instance, where an automation script handles the patching, tuning, and backups
B. A VM DB System with automatic backups enabled and a maintenance window set
C. NoSQL Database with on-demand tables and provisioned throughput
D. Autonomous Database, which patches and tunes itself

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Autonomous Database comes in transaction processing and data warehouse flavors and removes the routine DBA work. A DB System is managed infrastructure where you still control patching windows and configuration.
</details>

---

### Question 9
**Scenario:** OCI security posture must be monitored for misconfiguration automatically.

A. Cloud Guard, which detects problems against detector recipes and can take responder actions
B. Audit logs only
C. Vault
D. Manual review

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud Guard is the posture management service, and Security Zones go further by preventing non-compliant resources from being created in the first place. Audit logs record what happened but do not evaluate configuration.
</details>

---

### Question 10
**Scenario:** Encryption keys must be managed by the customer.

A. No encryption
B. OCI Vault, holding customer-managed keys and secrets, optionally in a dedicated HSM partition
C. Oracle-managed keys only, which Oracle rotates automatically and which are the default for all storage
D. Local key files

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** All OCI storage is encrypted by default with Oracle-managed keys; Vault lets you own the key lifecycle instead, which is what a compliance requirement usually means by customer-managed. Vault also stores secrets, which keeps credentials out of code.
</details>

---

### Question 11
**Scenario:** OCI pricing is described as consistent across regions.

A. Oracle prices the same across commercial regions
B. Pricing is negotiated only, per customer, and never published
C. All services are free
D. Prices vary widely by region, with higher rates in regions that have only a single availability domain

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Uniform global pricing is one of OCI's stated commercial differentiators, alongside relatively low egress charges. This is examinable because the exam covers the business case for OCI as well as the technology.
</details>

---

### Question 12
**Scenario:** Compute shapes must match a workload's needs precisely.

A. One size
B. Bare metal only, since dedicated hosts give every workload predictable, exact core counts
C. Fixed shapes only
D. Flexible shapes, where OCPU count and memory are chosen independently

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Flexible shapes avoid paying for memory you do not need because you needed the cores. Note that an OCPU corresponds to a physical core with hyperthreading, so it is not directly comparable to a vCPU on other clouds.
</details>

---

### Question 13
**Scenario:** Support is needed to understand the shared responsibility model on OCI.

A. Oracle secures everything
B. Oracle secures the infrastructure and physical layer; the customer secures data, identities, and workloads, shifting by service
C. The customer secures everything, including the physical data centers and the hypervisor, since the tenancy belongs to the customer alone
D. Responsibility is split equally by percentage, with Oracle and the customer each handling half of every security control

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Data and identity remain the customer's responsibility across every service model, which is consistent across all cloud providers. What changes with Autonomous Database or another managed service is who patches the software layer.
</details>

---

### Question 14
**Scenario:** A budget must alert when spend approaches a threshold.

A. Cost is fixed
B. Nothing exists
C. Budgets scoped to a compartment or tag, with alert rules on actual or forecast spend
D. Check the invoice

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Scoping budgets to compartments is why compartment design and cost management are related decisions. Forecast-based alerts warn before the money is spent rather than after, which is the difference between a control and a report.
</details>

---

### Question 15
**Scenario:** High availability within a region for a web tier.

A. A larger instance shape with more OCPUs and memory, so a single host can absorb any traffic spike without needing a second instance or a load balancer
B. Backups
C. Instances across multiple fault domains (and ADs where available), behind a load balancer with health checks
D. One instance

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The pattern is distribution plus health checking. Which isolation unit to spread across depends on the region: multiple ADs where available, fault domains where the region has a single AD.
</details>

---

## Where to go deeper

- [OCI Foundations cert page](../../exams/oracle/oci-foundations/) - notes, practice plan, strategy
- [OCI Architect Associate practice questions](./oracle-oci-architect-associate.md) - the next level up
- [OCI AI Foundations practice questions](https://ai.noblerworks.com/certifications/practice-questions/oracle-oci-ai-foundations/) - the AI sibling
- [What is cloud computing?](../../learn/concepts/what-is-cloud-computing.md) - plain-English foundation
- **[📖 Oracle University certification](https://education.oracle.com/oracle-certification-path/pFamily_647)** - official exam pages
