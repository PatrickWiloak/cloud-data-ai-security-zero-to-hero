---
last-updated: 2026-10-22
difficulty: beginner
---

# Oracle Cloud Infrastructure Foundations (1Z0-1085) - Practice Questions

30 questions for OCI Foundations prep, weighted toward OCI architecture and core services (30%), security and identity (20%), then compute, storage, and networking (15% each).

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

### Question 16
**Scenario:** A company moves its finance team onto Oracle Fusion Cloud ERP. Oracle runs the application, its database, and the infrastructure; the company only configures the software and manages its users.

A. Software as a service (SaaS)
B. Platform as a service (PaaS)
C. Infrastructure as a service (IaaS)
D. On-premises private cloud

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** When the provider delivers a complete application and the customer only configures and uses it, that is SaaS. With PaaS the customer still builds and deploys its own application code on a managed platform, and with IaaS the customer manages the operating system and everything above it. An on-premises private cloud is run by the company itself.

**Key Concept:** [Oracle Fusion Cloud ERP](https://www.oracle.com/applications/erp/)
</details>

---

### Question 17
**Scenario:** A tenancy is subscribed to three regions. An administrator in a secondary region tries to create a new IAM group and is told it must be done elsewhere.

A. In whichever region has the most compute instances
B. In any region, since IAM is fully regional on OCI
C. In the tenancy's home region, where IAM resources are defined
D. In a region paired with the secondary region for DR

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The home region is chosen at sign-up and holds the definitions of IAM resources. They are replicated to every subscribed region for use, but they can only be changed in the home region. IAM is not independently regional, and neither instance counts nor DR pairing decides where identity changes are made.

**Key Concept:** [Managing Regions: The Home Region](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/managingregions.htm)
</details>

---

### Question 18
**Scenario:** A student signs up for OCI to learn. After the trial ends they want to keep a small VM and database running at no cost, indefinitely.

A. Keep using the trial credits, which roll over each month
B. Request a support exception to extend the trial
C. Move the workload to preemptible instances, which are free
D. Use Always Free resources, which remain after the trial

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The OCI Free Tier has two parts: a time-limited Free Trial with credits, and Always Free resources (such as small compute instances and Autonomous Databases) that stay available for the life of the account. Trial credits expire rather than rolling over. Preemptible instances are discounted, not free, and support does not turn a trial into free service.

**Key Concept:** [Oracle Cloud Free Tier](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier.htm)
</details>

---

### Question 19
**Scenario:** A compliance rule says the company's virtual machines must run on physical hardware not shared with any other customer, but the team still wants to run several VMs per host.

A. Standard VM shapes in a private subnet
B. Dedicated Virtual Machine Hosts
C. Flexible shapes with extra OCPUs
D. Instances spread across fault domains

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A Dedicated Virtual Machine Host is a single-tenant server on which you place your own VM instances, giving hardware isolation while keeping the flexibility of VMs. A private subnet isolates network traffic, not hardware. Extra OCPUs and fault domain placement still leave the VM on shared multi-tenant hosts.

**Key Concept:** [Dedicated Virtual Machine Hosts](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts.htm)
</details>

---

### Question 20
**Scenario:** A batch rendering job can be interrupted and restarted without harm. The team wants the cheapest compute capacity OCI offers for it.

A. Preemptible instances, which can be reclaimed at any time
B. Bare metal instances, which avoid hypervisor overhead
C. Dedicated VM hosts, which are billed for the whole host
D. Burstable instances sized for the peak demand of the rendering job

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Preemptible capacity costs 50% less than on-demand because OCI can reclaim it, which suits fault-tolerant, interruptible work such as batch jobs. Bare metal and dedicated hosts cost more, not less. Burstable instances are designed for a low baseline with occasional spikes, not for sustained heavy processing.

**Key Concept:** [Preemptible Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/preemptible.htm)
</details>

---

### Question 21
**Scenario:** A self-managed database on a compute instance needs low-latency, persistent disk storage attached to that single instance, which can be resized later.

A. Object Storage, accessed through the bucket API
B. File Storage, mounted over NFS by many hosts
C. Block Volume, attached to the instance as a disk
D. Archive Storage, restored before each read

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Block Volume provides persistent, network-attached disks that behave like local drives, can be resized, and are the normal choice for database data files. Object Storage is accessed over an API, not as a disk. File Storage is a shared NFS file system, and Archive Storage must be restored before it can be read at all.

**Key Concept:** [Overview of Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm)
</details>

---

### Question 22
**Scenario:** Seven-year-old audit records must be kept at the lowest storage cost. They are read perhaps once a year, and waiting a while before reading is acceptable.

A. Object Storage Standard tier
B. Block Volume with the Lower Cost setting
C. File Storage with snapshots
D. Object Storage Archive tier

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The Archive tier is the cheapest storage in OCI and is meant for data kept for long periods and rarely read. Objects are offline and must be restored first, which takes up to an hour before the first byte is available. Standard tier costs more for data that is almost never read, and block or file storage costs far more per GB for this purpose.

**Key Concept:** [Understanding Object Storage Tiers](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm)
</details>

---

### Question 23
**Scenario:** A public web server in a VCN must be reachable from the internet and must also be able to initiate outbound connections to the internet.

A. A NAT gateway added as the default route in the subnet's route table
B. An internet gateway, a public subnet, and a public IP
C. A service gateway for Oracle Services Network
D. A dynamic routing gateway attached to the VCN

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An internet gateway allows traffic in both directions between the internet and resources in a public subnet that have public IP addresses. A NAT gateway only allows outbound connections from private resources. A service gateway reaches Oracle services without the internet, and a DRG connects to on-premises networks or other VCNs.

**Key Concept:** [Internet Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm)
</details>

---

### Question 24
**Scenario:** A bank needs a private, dedicated connection from its data center to OCI with consistent throughput, not traffic carried over the public internet.

A. FastConnect through a partner or colocation provider
B. Site-to-Site VPN with IPSec tunnels over the public internet
C. An internet gateway with a security list
D. Local peering between two VCNs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** FastConnect is a dedicated private connection between on-premises and OCI, with higher bandwidth and more consistent performance than internet-based links. Site-to-Site VPN is encrypted but still runs over the internet. An internet gateway exposes resources to the internet, and local peering connects VCNs to each other, not to a data center.

**Key Concept:** [FastConnect Overview](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm)
</details>

---

### Question 25
**Scenario:** A mobile game needs a fully managed database for player profiles accessed by key, with predictable single-digit-millisecond latency at very high scale.

A. Oracle Base Database Service on a VM
B. A MySQL database on a self-managed instance
C. Oracle NoSQL Database Cloud Service
D. Oracle Exadata Database Service

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** NoSQL Database Cloud Service is a fully managed key-value and document store built for low, predictable latency at scale, which matches simple keyed access. Base Database and Exadata are relational services suited to complex SQL workloads and cost more for this pattern. A self-managed MySQL instance is not fully managed.

**Key Concept:** [Oracle NoSQL Database Cloud Service](https://docs.oracle.com/en-us/iaas/nosql-database/index.html)
</details>

---

### Question 26
**Scenario:** Twelve developers need to manage instances in the Dev compartment. The administrator wants the simplest setup that stays manageable as people join and leave.

A. Write one policy per developer, naming each user
B. Make every developer a tenancy administrator
C. Share one IAM user's credentials across the team
D. Put them in a group and write one policy for the group

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** OCI policies grant access to groups (or dynamic groups), not to individual users, so the standard pattern is one group, one policy, and group membership changes as people come and go. Per-user policies are not how OCI policy subjects work. Tenancy admin rights break least privilege, and shared credentials destroy accountability.

**Key Concept:** [How Policies Work](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/how-policies-work.htm)
</details>

---

### Question 27
**Scenario:** An auditor asks whether data in OCI Block Volume and Object Storage is encrypted at rest if the team never configured anything.

A. No, encryption must be enabled per resource at creation
B. Yes, it is encrypted by default with Oracle-managed keys
C. Only if the data is stored in an Archive tier bucket
D. Only if a Cloud Guard target covers the compartment

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OCI encrypts Block Volume and Object Storage data at rest by default using Oracle-managed keys. Customers can choose their own keys in OCI Vault when they need control over rotation and revocation. Encryption is not opt-in per resource, not limited to Archive, and Cloud Guard detects problems rather than providing encryption.

**Key Concept:** [Overview of Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm)
</details>

---

### Question 28
**Scenario:** Engineers need time-limited SSH access to instances in a private subnet, without giving those instances public IPs or running a jump host themselves.

A. OCI Bastion service with time-limited sessions
B. A public IP added to each instance temporarily
C. An internet gateway on the private subnet
D. A self-managed jump server running in a public subnet of the VCN

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Bastion service is a managed, audited way to reach private resources through sessions that expire automatically. Adding public IPs or an internet gateway exposes the instances to the internet. A self-managed jump server works, but it is exactly the server the team wants to avoid patching and hardening.

**Key Concept:** [Bastion Overview](https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/bastionoverview.htm)
</details>

---

### Question 29
**Scenario:** A security list was changed last night and broke an application. The team needs to know who made the change and when, and nobody had set up any logging beforehand.

A. The Monitoring service's CPU metrics for the subnet
B. The instance's own syslog files
C. The Audit service, which records API calls automatically
D. A Notifications topic subscribed to the VCN

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The Audit service automatically records supported API calls against tenancy resources, including who made the call, when, and from where, with no setup required. Monitoring metrics show resource behavior, not who changed configuration. Syslog on an instance does not see control-plane changes, and a Notifications topic only delivers messages that something else publishes.

**Key Concept:** [Overview of Audit](https://docs.oracle.com/en-us/iaas/Content/Audit/Concepts/auditoverview.htm)
</details>

---

### Question 30
**Scenario:** A company already owns Oracle Database Enterprise Edition licenses and wants to use them for databases it runs on OCI to lower the cost.

A. Pay As You Go pricing with the license included
B. Always Free Autonomous Database
C. Preemptible capacity reservations
D. Bring Your Own License (BYOL) pricing

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** BYOL lets customers apply existing Oracle licenses to eligible OCI services at a lower rate, since they are not paying for the license again. License-included pricing charges for the license on top of the infrastructure. Always Free databases are small and not a home for production licenses, and preemptible capacity relates to compute instances, not database licensing.

**Key Concept:** [Oracle Bring Your Own License](https://www.oracle.com/cloud/bring-your-own-license/)
</details>

---

## Where to go deeper

- [OCI Foundations cert page](../../exams/oracle/oci-foundations/) - notes, practice plan, strategy
- [OCI Architect Associate practice questions](./oracle-oci-architect-associate.md) - the next level up
- [OCI AI Foundations practice questions](https://ai.noblerworks.com/certifications/practice-questions/oracle-oci-ai-foundations/) - the AI sibling
- [What is cloud computing?](../../learn/concepts/what-is-cloud-computing.md) - plain-English foundation
- **[📖 Oracle University certification](https://education.oracle.com/oracle-certification-path/pFamily_647)** - official exam pages
