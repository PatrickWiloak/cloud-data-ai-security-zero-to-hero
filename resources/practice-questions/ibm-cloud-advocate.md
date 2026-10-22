---
last-updated: 2026-10-22
difficulty: beginner
---

# IBM Cloud Advocate - Practice Questions

30 questions for IBM Cloud Advocate prep, weighted toward the IBM Cloud platform and services (30%), security and compliance (20%), then cloud concepts, HA and DR, cost management, and migration.

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

### Question 16
**Scenario:** A CFO asks how moving from an owned data center to IBM Cloud changes the way IT spending shows up in the accounts. What is the main change?

A. All spending becomes a one-time capital purchase made at the start of the contract
B. Spending stops entirely, because the provider absorbs all of the infrastructure costs
C. Spending stays the same, because hardware is still bought and depreciated
D. Large up-front capital purchases shift toward ongoing, usage-based operating costs

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cloud replaces buying and depreciating hardware (capital expenditure) with paying for resources as they are consumed (operating expenditure). It is not a single up-front purchase, and the customer still pays for what it uses. Owned hardware no longer has to be bought and depreciated for workloads that move.

**Key Concept:** Cloud shifts CapEx to OpEx and ties cost to usage. See [What is cloud computing?](https://www.ibm.com/think/topics/cloud-computing)
</details>

---

### Question 17
**Scenario:** A company runs its customer portal on IBM Cloud, its analytics on another public cloud, and its email on a SaaS provider. It has no private cloud or on-premises workloads left. Which term best describes this setup?

A. Multicloud, because it uses services from more than one cloud provider
B. Hybrid cloud, because it combines public cloud services with a private cloud
C. Private cloud, because each workload has its own dedicated provider
D. Community cloud, because several organizations share the same services

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Multicloud means using cloud services from more than one provider. Hybrid cloud specifically combines public cloud with private cloud or on-premises infrastructure, which this company no longer has. Using several providers does not make any of them private. A community cloud is shared infrastructure for organizations with common needs, which does not describe this setup.

**Key Concept:** Hybrid mixes public and private; multicloud mixes providers. The two often overlap. See [What is multicloud?](https://www.ibm.com/think/topics/multicloud)
</details>

---

### Question 18
**Scenario:** An account hosts resources for three projects. The administrator wants each project's resources grouped so access can be granted per project and usage can be viewed per project. What should they use?

A. A separate IBM Cloud region for each project, chosen at random
B. A separate VPC for each project, with no other organization needed
C. Resource groups, one per project, with access policies scoped to each group
D. A naming convention only, with every resource kept in the default group

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Resource groups organise account resources so that IAM access can be assigned per group and usage can be broken down by group. Regions are about location, not ownership. VPCs isolate networks but do not cover non-network services or access management on their own. Names alone cannot drive access policies.

**Key Concept:** Resource groups are the unit for organising resources, access, and usage views. See [Managing resource groups](https://cloud.ibm.com/docs/account?topic=account-rgs).
</details>

---

### Question 19
**Scenario:** A manufacturer must keep production data inside its own factories for latency and regulatory reasons, but wants to use IBM Cloud managed services there with one control plane. Which offering fits?

A. IBM Cloud Object Storage with a Single Data Center bucket
B. IBM Cloud Satellite, which runs IBM Cloud services on the customer's own sites
C. IBM Cloud Direct Link, which connects the factory network to an IBM region
D. IBM Power Virtual Server, which hosts AIX and IBM i servers in IBM data centers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Satellite extends IBM Cloud services to customer locations, such as on-premises sites, edge sites, or other clouds, managed from IBM Cloud, so data can stay in the factory. A single-site Object Storage bucket still lives in an IBM data center. Direct Link is a private network connection, not a way to run services on site. Power Virtual Server runs in IBM data centers.

**Key Concept:** Satellite brings the cloud to where the data must stay. See [Getting started with Satellite](https://cloud.ibm.com/docs/satellite?topic=satellite-getting-started).
</details>

---

### Question 20
**Scenario:** A company has standardized on Red Hat OpenShift on premises and wants a managed version on IBM Cloud with the same tools and workflows. Which service fits?

A. Red Hat OpenShift on IBM Cloud
B. IBM Cloud Kubernetes Service
C. IBM Cloud Code Engine
D. IBM Cloud Virtual Servers for VPC

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Red Hat OpenShift on IBM Cloud is a managed OpenShift service, so teams keep their OpenShift tooling, operators, and workflows. IBM Cloud Kubernetes Service is managed upstream Kubernetes without the OpenShift platform layer. Code Engine is a serverless platform that hides the cluster. Virtual servers would mean building and running OpenShift themselves.

**Key Concept:** Choose OpenShift when the organization has standardized on it; Kubernetes Service for plain Kubernetes. See [Getting started with Red Hat OpenShift on IBM Cloud](https://cloud.ibm.com/docs/openshift?topic=openshift-getting-started).
</details>

---

### Question 21
**Scenario:** A bank needs a dedicated, private, high-bandwidth connection between its data center and IBM Cloud that does not cross the public internet. Which service fits?

A. IBM Cloud Internet Services, for global load balancing at the edge
B. A public gateway attached to the bank's VPC subnets
C. Transit Gateway, which links VPCs across regions
D. IBM Cloud Direct Link, for private on-premises connections

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Direct Link provides private connectivity between on-premises networks and IBM Cloud without using the public internet. Internet Services handles edge security, DNS, and load balancing for public traffic. A public gateway gives VPC resources outbound internet access. Transit Gateway connects IBM Cloud networks to each other, and can include Direct Link, but is not itself the on-premises link.

**Key Concept:** Direct Link for private on-premises connections, Transit Gateway for cloud network to cloud network. See [Getting started with Direct Link](https://cloud.ibm.com/docs/dl?topic=dl-get-started-with-ibm-cloud-dl).
</details>

---

### Question 22
**Scenario:** A retailer runs core systems on IBM i and AIX on Power hardware. It wants to move them to IBM Cloud without rewriting them for x86. Which offering fits?

A. IBM Cloud Code Engine, which runs the existing binaries as containers
B. IBM Power Virtual Server, which provides Power-based virtual servers
C. IBM Cloud Virtual Servers for VPC, using an x86 emulation layer
D. IBM Cloud Kubernetes Service, with AIX worker node images installed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Power Virtual Server provides IBM Power-based virtual servers that run AIX, IBM i, and Linux on Power, so these workloads can move without re-platforming. Code Engine and Kubernetes Service run containers, not AIX or IBM i. Virtual Servers for VPC run x86 and do not offer an emulation layer for Power workloads.

**Key Concept:** Match the platform to the workload's architecture to avoid a rewrite. See [Getting started with Power Virtual Server](https://cloud.ibm.com/docs/power-iaas?topic=power-iaas-getting-started).
</details>

---

### Question 23
**Scenario:** Developers keep API keys and TLS certificates in configuration files. Security wants them stored centrally, with access control, rotation, and certificate expiry tracking. Which service fits?

A. IBM Cloud Object Storage, with each secret saved as a private object
B. IBM Cloud Container Registry, which stores secrets next to images
C. IBM Cloud Secrets Manager, which stores, controls, and rotates secrets
D. IBM Cloud Monitoring, which alerts when a secret appears in a log

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Secrets Manager stores secrets such as API keys, credentials, and certificates centrally, controls access with IAM, and supports rotation and expiry notifications. Object Storage can hold files but offers no rotation or secret lifecycle features. Container Registry stores images. Monitoring tracks metrics and alerts, not secrets.

**Key Concept:** Centralise secrets, rotate them, and keep them out of code. See [Getting started with Secrets Manager](https://cloud.ibm.com/docs/secrets-manager?topic=secrets-manager-getting-started).
</details>

---

### Question 24
**Scenario:** An Object Storage bucket was deleted overnight, and the security team needs to know which identity deleted it and when. Which source holds this information?

A. Audit events captured by Activity Tracker Event Routing for the account
B. Application logs written by the web app that used the deleted bucket
C. The monthly invoice, which lists each resource deleted that month
D. IBM Cloud Monitoring metrics, which record who changed each resource

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Activity Tracker Event Routing captures audit events for actions on IBM Cloud resources, including who did what and when, and routes them to a target such as IBM Cloud Logs or Object Storage. Application logs record what the app did, not account actions. Invoices list charges, not identities. Monitoring records performance metrics, not who made changes.

**Key Concept:** Audit events answer who, what, and when for account and resource actions. See [Getting started with Activity Tracker Event Routing](https://cloud.ibm.com/docs/atracker?topic=atracker-getting-started).
</details>

---

### Question 25
**Scenario:** A company wants its database service reachable only from its corporate IP ranges and its own VPC, even if valid API credentials leak. What should the administrator configure?

A. A stronger password policy for every user in the account
B. A second resource group to hold only the database instance
C. Spending notifications on the database service instance
D. Context-based restrictions with network zones for the IPs and VPC

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Context-based restrictions add rules based on where a request comes from, such as allowed IP ranges and VPCs, on top of IAM, so stolen credentials used from elsewhere are refused. Password policies strengthen sign-in but do not restrict network origin. Resource groups organise access but do not filter by network. Spending notifications are about cost.

**Key Concept:** IAM decides who; context-based restrictions decide from where. See [Restrict access with context-based restrictions](https://www.ibm.com/products/tutorials/restrict-access-to-your-ibm-cloud-resources-using-context-based-restrictions).
</details>

---

### Question 26
**Scenario:** Backup data in Object Storage must remain available even if an entire metropolitan area, such as one region, becomes unavailable. Which bucket resiliency should be chosen?

A. Single Data Center, which keeps copies in one site
B. Cross Region, which spreads data across several metro areas
C. Regional, which spreads data across one metro area's zones
D. Any of them, since all buckets copy data to every region

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cross Region resiliency spreads data across several metropolitan areas, so it survives the loss of one. Regional resiliency spreads data across zones within a single metro area and survives a site outage but not a regional one. Single Data Center keeps data in one site. Buckets do not automatically copy data to every region.

**Key Concept:** A bucket's resiliency is set by the endpoint used to create it. See [Object Storage endpoints and resiliency](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-endpoints).
</details>

---

### Question 27
**Scenario:** A business owner says the order system can be down for at most 4 hours after a disaster and can lose no more than 15 minutes of orders. How should these two requirements be named?

A. An RPO of 4 hours and an RTO of 15 minutes
B. An SLA of 4 hours and an SLO of 15 minutes
C. An MTTR of 4 hours and an MTBF of 15 minutes
D. An RTO of 4 hours and an RPO of 15 minutes

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Recovery time objective (RTO) is how long the system can be down; recovery point objective (RPO) is how much data, measured in time, can be lost. So 4 hours is the RTO and 15 minutes the RPO. Swapping them is a common mistake. SLAs and SLOs describe service targets and commitments. MTTR and MTBF describe repair and failure rates.

**Key Concept:** RTO is about time to recover; RPO is about data loss. See [What is disaster recovery?](https://www.ibm.com/think/topics/disaster-recovery)
</details>

---

### Question 28
**Scenario:** Finance wants to see IBM Cloud usage broken down by project and by environment, such as dev and prod, without creating separate accounts. What should the administrator set up?

A. Resource groups per project, plus consistent tags for environment
B. One VPC per environment, with all projects sharing the same VPC
C. A cost estimate for each project, refreshed once every quarter by hand
D. Separate IBM IDs for each project, used to deploy its resources

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Resource groups give a usage view per project, and consistent tags such as `env:prod` let usage be filtered further. VPCs organise networks, not cost views, and do not cover every service. Estimates predict cost but do not report actual usage. Splitting deployments across user IDs does not organise billing data and weakens access control.

**Key Concept:** Organise for cost visibility from the start with resource groups and tags. See [Managing resource groups](https://cloud.ibm.com/docs/account?topic=account-rgs).
</details>

---

### Question 29
**Scenario:** A student wants to experiment with several IBM Cloud services, including Watson APIs, without risk of being charged. What should they look for?

A. Subscription accounts, which include a fixed amount of credit each month
B. Reserved capacity, which removes charges for one-year commitments
C. Services that offer a Lite plan, which is free and does not expire
D. Enterprise accounts, which waive charges for individual developers

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Many IBM Cloud services offer Lite plans that are always free, with usage limits, and never expire, which suits learning and experiments. A subscription is a paid commitment. Reserved capacity is a discounted paid commitment. Enterprise accounts are for organizing multiple accounts and do not waive charges.

**Key Concept:** Lite plans give free, limited access for learning. See [IBM Cloud Free Tier](https://www.ibm.com/cloud/free).
</details>

---

### Question 30
**Scenario:** A company runs 600 VMware virtual machines on premises and must leave its data center within six months. It wants to keep its VMware tools and avoid re-platforming the VMs. What is the most suitable approach?

A. Rebuild every VM as a container and deploy them to Code Engine
B. Use IBM Cloud VMware Solutions to run the VMware stack on IBM Cloud
C. Convert every VM into a serverless function triggered by events
D. Move only the data to Object Storage and retire every application

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** IBM Cloud VMware Solutions run the VMware stack on IBM Cloud, so VMs can be moved with familiar tools and little change, which is a rehost approach suited to a tight deadline. Containerizing or rewriting 600 VMs as functions is a long modernization project. Retiring every application is not a migration plan.

**Key Concept:** Rehost first when time is short; modernize later. See [Getting started with VMware Solutions](https://cloud.ibm.com/docs/vmwaresolutions?topic=vmwaresolutions-getting-started).
</details>

---

## Where to go deeper

- [IBM Cloud Advocate cert page](../../exams/ibm/cloud-advocate/) - notes, practice plan, strategy
- [IBM Cloud Solution Architect practice questions](./ibm-cloud-solution-architect.md) - the architecture level
- [What is cloud computing?](../../learn/concepts/what-is-cloud-computing.md) - plain-English foundation
- [Shared responsibility model](https://security.noblerworks.com/learn/concepts/shared-responsibility-model/) - question 15 in depth
- **[📖 IBM Training](https://www.ibm.com/training/)** - official certification pages
