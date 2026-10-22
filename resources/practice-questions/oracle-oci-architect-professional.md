---
last-updated: 2026-10-22
difficulty: advanced
---

# Oracle Cloud Infrastructure Architect Professional (1Z0-997) - Practice Questions

30 questions for OCI Architect Professional prep, weighted toward advanced architecture design (20%) and networking and connectivity (20%), then HA/DR, security and compliance, performance, and database architecture.

> **Cert page:** [exams/oracle/oci-architect-professional/](../../exams/oracle/oci-architect-professional/)

---

### Question 1
**Scenario:** A hub-and-spoke topology must let spoke VCNs reach on-premises and each other, with inspection.

A. Separate DRGs per spoke VCN, each with its own attachment to the on-premises circuit, so spoke-to-spoke traffic has no single inspection point
B. Internet gateways in each spoke
C. A DRG with transit routing, spokes attached, and route tables directing traffic through a firewall appliance in the hub
D. A full peering mesh between every pair of spoke VCNs, which scales poorly, cannot transit to on-premises, and gives no central place to inspect traffic

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** DRG route tables and route distributions are what express the policy: which attachment learns which routes and where traffic is steered. Sending spoke-to-spoke traffic through the hub firewall requires explicit routes, because otherwise transit routing delivers it directly.
</details>

---

### Question 2
**Scenario:** FastConnect must be resilient to a single circuit or device failure.

A. Redundant virtual circuits over diverse physical paths and locations, with BGP failover
B. A VPN only over the public internet, which depends on internet path quality and has no bandwidth guarantee
C. A single high-bandwidth circuit with a premium support contract, which cuts repair time but is still one failure domain
D. One virtual circuit on a single FastConnect port at one colocation, with a larger bandwidth tier chosen so a hardware failure is unlikely to matter

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Bandwidth is not redundancy: a single circuit is a single failure domain regardless of size. Diversity must extend to the physical path and the terminating devices, and BGP attributes control which path is preferred in each direction.
</details>

---

### Question 3
**Scenario:** An application must fail over to a second region with an RTO of 15 minutes.

A. A warm standby: data replicated continuously, infrastructure as code pre-provisioned at reduced scale, with automated scale-up and traffic steering on failover
B. A cold rebuild from scratch in the second region using infrastructure code, restoring data from the most recent backup copy once the outage is declared and then testing the stack
C. Multi-AD deployment within the primary region, which survives the loss of one availability domain but not the loss of the whole region
D. Backups restored manually

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A 15-minute RTO does not permit provisioning from nothing, so the standby must already exist in some form. Traffic Management steering policies with health checks handle the redirection, and Full Stack Disaster Recovery can orchestrate the sequence.
</details>

---

### Question 4
**Scenario:** A database must support both high availability and disaster recovery.

A. A read replica in a second AD, which offloads reporting queries and can be promoted by hand, but is not a managed DR configuration
B. Backups to Object Storage only, scheduled nightly, which protect against data loss but give hours of restore time and no standby
C. Data Guard alone in one AD
D. RAC or Data Guard within the region for HA, plus Data Guard or Autonomous Data Guard to a second region for DR

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** HA and DR are different failure domains and need different mechanisms: local redundancy handles instance and AD failure, cross-region replication handles regional loss. Treating one as covering the other is the design error the exam probes.
</details>

---

### Question 5
**Scenario:** A large on-premises Oracle estate must move to OCI with minimal change.

A. Rewrite the applications for a different database engine, which removes Oracle licensing but needs far more than minimal change and long testing
B. Rebuild everything cloud native on managed services and containers, retiring the Oracle schemas, which is a full redesign and far from minimal change
C. Export the schemas to CSV files and reload them into new tables, which loses constraints, code objects and needs a long outage window
D. Assess per workload: lift and shift to compute or Exadata, migrate with Zero Downtime Migration or Data Pump, and use Data Guard for the cutover where downtime must be short

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Oracle-to-Oracle migration is the case where lift and shift is genuinely low risk, and Exadata Cloud Service preserves the performance characteristics some workloads depend on. Standby-based cutover is what compresses the downtime window.
</details>

---

### Question 6
**Scenario:** Traffic between OCI and another cloud provider must be private and high bandwidth.

A. A site-to-site VPN over the internet only, which is encrypted but shares public paths, so bandwidth and latency vary with internet conditions
B. Public endpoints
C. FastConnect to a colocation provider with a cross-connect to the other cloud's direct connectivity service, or Oracle Interconnect for Azure where available
D. A NAT gateway for outbound access from private subnets to the other cloud's public endpoints, which keeps instances unexposed but does not make the traffic private or give it dedicated bandwidth

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Multicloud designs need dedicated connectivity to be predictable. The Oracle and Microsoft interconnect gives low-latency private connectivity in paired regions without a partner circuit, which is why it appears in Oracle multicloud reference architectures.
</details>

---

### Question 7
**Scenario:** Compliance requires that data never leaves a jurisdiction, including for support.

A. Encrypt everything with customer-managed keys in Vault, which does not control where data or support staff are located
B. A public commercial region with tags marking regulated data, which labels the data but does not stop it moving
C. Keep services in-region, restrict replication and backup targets, and consider a sovereign region
D. Documentation of the data flows and a signed policy statement that staff will not move data out in practice

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Residency leaks through the paths you did not choose deliberately: backups, DR replicas, and telemetry. Where the requirement extends to operator access, Dedicated Region or a sovereign region is the answer rather than configuration within a commercial region.
</details>

---

### Question 8
**Scenario:** An architecture must minimize cost without sacrificing the availability target.

A. Right-size shapes, use flexible shapes and preemptible instances for tolerant workloads, apply lifecycle tiering to storage, and commit to universal credits where usage is predictable
B. Turn off monitoring and logging to save on metrics ingestion charges, since the platform already restarts failed instances without help
C. Move everything to bare metal shapes for the best price-performance, keeping each host running at all times so capacity is always available
D. Reduce redundancy

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cost work should attack waste rather than resilience. Preemptible instances suit stateless batch workloads specifically, and lifecycle policies address storage, which is usually a larger share of a mature estate's bill than people expect.
</details>

---

### Question 9
**Scenario:** Performance must be diagnosed for a distributed application.

A. Guess at the cause from past incidents and change one setting at a time
B. CPU graphs only
C. Application Performance Monitoring with tracing, plus Logging Analytics and Monitoring metrics correlated together
D. Increase shape sizes across all tiers first, then measure again, on the assumption that a bigger instance always removes the bottleneck

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Metrics tell you something is slow, traces tell you where, and logs tell you why. APM's synthetic monitoring adds the outside-in view, which distinguishes "our service is slow" from "the path to our service is slow."
</details>

---

### Question 10
**Scenario:** Governance must prevent developers creating internet-exposed resources.

A. A weekly manual review of the compartments for public resources, with tickets raised for any internet-exposed resource found and a deadline set for the owning team to remove it
B. Security Zones with policies denying public access, plus IAM policies restricting who may create gateways, and Cloud Guard detecting anything that slips through
C. Training
D. A naming convention labeling public resources with "public-", which helps humans spot them but stops nothing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Preventive and detective controls together: Security Zones refuse the operation, IAM limits who can even attempt it, and Cloud Guard covers compartments outside a security zone. Any one alone leaves a gap.
</details>

---

### Question 11
**Scenario:** A multi-tenant SaaS application must isolate customers on OCI.

A. One compartment for everything, with a tag on each resource naming the customer, which helps with billing but gives no real isolation boundary
B. Application-level filtering only, where the code checks the tenant on each request and the infrastructure stays shared
C. Separate regions per tenant, which isolates data by geography but multiplies cost and operations without matching the isolation need
D. Compartment-per-tenant or tenancy-per-tenant, with matching IAM policies and network segmentation

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The choice follows the isolation requirement and the operational cost you can carry: compartments give strong policy and cost separation within one tenancy, while separate tenancies give the hardest boundary at the price of managing many tenancies.
</details>

---

### Question 12
**Scenario:** Autonomous Database must be reachable only from a specific VCN.

A. A bastion only, which gives time-limited SSH access to private hosts but does not control how clients reach the database endpoint
B. A private endpoint in the VCN, with public access disabled
C. A public endpoint with an access control list limiting source IPs, which narrows access but still exposes the database to the internet
D. A NAT gateway on the VCN, which gives private subnets outbound internet access and does not restrict who reaches the database

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A private endpoint gives the database an address inside your subnet and removes the public listener entirely. An access control list on a public endpoint narrows exposure but the endpoint still exists on the internet.
</details>

---

### Question 13
**Scenario:** Infrastructure must be reproducible across regions and environments.

A. Manual runbooks kept in a wiki, which a person follows in each region and each environment, and which drift as soon as one step is skipped
B. Terraform (Resource Manager stacks), parameterized per environment and stored in version control
C. Custom images only, which capture the operating system but not the network, IAM, and database configuration around it in each region
D. Console clicks with screenshots

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Reproducible infrastructure is the precondition for any credible DR plan, because the standby region must be buildable. Resource Manager runs Terraform as a managed service with state handling and drift detection.
</details>

---

### Question 14
**Scenario:** A workload has unpredictable bursts and a stable baseline.

A. Provision for the peak permanently, with committed capacity sized to the largest burst ever seen, so the baseline workload pays for idle capacity
B. Provision the baseline with committed capacity and handle bursts with autoscaling, using preemptible capacity where the workload tolerates interruption
C. Provision the average
D. Manual scaling by an on-call engineer who adds shapes when alerts fire, which reacts after bursts have already started and degraded users

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Splitting baseline from burst lets you commit to the predictable part for a discount while paying on demand only for the peaks. Provisioning for the average means failing during every burst, which is why the naive middle option is the worst of the three.
</details>

---

### Question 15
**Scenario:** An architecture review must record why a design was chosen.

A. An architecture decision record with context, options, decision, and consequences, kept with the code
B. Nothing formal; the reasoning stays in the heads of the people who attended the review and can be asked later if a question comes up
C. A meeting
D. A diagram of the final architecture, which shows what was built but not the options that were rejected or the reasons behind the choice

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A diagram captures the result, not the constraints that produced it, so the next team cannot tell which trade-offs still apply. Recording the rejected options is what stops the same debate recurring after the original participants have moved on.
</details>

---

### Question 16
**Scenario:** A new OCI tenancy for a regulated enterprise must start with a CIS-aligned compartment structure, IAM groups and policies, network topology, and security services enabled, deployed as code in days rather than designed from scratch.

A. Build each compartment and policy by hand in the Console, then document the result
B. Copy another company's Terraform files and adjust names until they apply cleanly
C. Deploy the OCI Core Landing Zone and extend it for the workloads
D. Start with one compartment and add structure later as audit findings arrive

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The OCI landing zones are Oracle-maintained Terraform templates that stand up a CIS OCI Benchmark-aligned tenancy baseline (compartments, groups, policies, networking, Cloud Guard, logging) that teams then extend. Console builds are slow and drift from the documentation. Borrowed code carries unknown assumptions, and retrofitting structure after audit findings is far more disruptive than starting with it.

**Key Concept:** [Deploy a secure landing zone that meets the CIS Foundations Benchmark](https://docs.oracle.com/en/solutions/cis-oci-benchmark/index.html)
</details>

---

### Question 17
**Scenario:** Several business units share one tenancy. Each unit's compartment must be capped at a fixed number of compute cores so one unit cannot consume the tenancy's service limits.

A. Write compartment quota policies that set the core count for each unit's compartment
B. Ask Oracle to lower the tenancy-wide service limits to one unit's share
C. Create budgets with alerts at 100% of each unit's forecast spend
D. Tag each instance with the unit name and review usage reports monthly

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Compartment quotas let administrators set, unset, or zero resource counts per compartment, and they are enforced when resources are created. Lowering tenancy service limits caps everyone together rather than per unit. Budgets alert on spend but do not block a launch, and tagging plus monthly reports only shows the problem after the fact.

**Key Concept:** [Overview of Compartment Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas.htm)
</details>

---

### Question 18
**Scenario:** Finance requires every resource to carry a CostCenter tag. Teams keep forgetting it, and finance wants the value applied automatically per compartment.

A. Free-form tags typed by each engineer when a resource is created
B. A naming convention that embeds the cost center in each resource name
C. A monthly script that reads resource names and writes them to a spreadsheet
D. A defined tag namespace with tag defaults set on each compartment

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Defined tags have a controlled schema, and a tag default on a compartment automatically applies the tag (and can require a value) to resources created there. Free-form tags are optional and inconsistent. Names and spreadsheets do not feed OCI cost reports by tag, and both rely on people remembering.

**Key Concept:** [Managing Tag Defaults](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagdefaults.htm)
</details>

---

### Question 19
**Scenario:** A company runs its applications in Microsoft Azure but needs Oracle Exadata performance and features for the database, with the lowest possible latency to those applications.

A. Run Oracle Database on Azure VMs with locally attached disks
B. Use Oracle Database@Azure, running OCI Exadata in Azure data centers
C. Keep the database in OCI and reach it over the public internet
D. Migrate the database to a non-Oracle engine native to Azure

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Oracle Database@Azure deploys Oracle-managed Exadata infrastructure inside Azure data centers, giving Exadata capabilities next to the Azure applications. Self-managed Oracle on Azure VMs does not provide Exadata. Reaching OCI over the internet adds latency and variability, and changing engines is a rewrite rather than an architecture choice.

**Key Concept:** [Oracle Database@Azure](https://docs.oracle.com/en-us/iaas/Content/database-at-azure/oaa.htm)
</details>

---

### Question 20
**Scenario:** A FastConnect private virtual circuit connects a data center to OCI. A new regulation requires that traffic on that link be encrypted with IPSec while keeping FastConnect's bandwidth and consistency.

A. Configure Site-to-Site VPN tunnels over the FastConnect virtual circuit
B. Replace FastConnect with a Site-to-Site VPN over the internet
C. Rely on FastConnect being private, which counts as encrypted
D. Switch the virtual circuit to public peering and require TLS on each application

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** IPSec over FastConnect runs Site-to-Site VPN tunnels on a FastConnect virtual circuit, adding encryption to a link that is already private and dedicated. Moving to an internet VPN loses the consistent performance. A private circuit is not the same as encryption, and public peering with per-application TLS changes the path and does not encrypt all traffic at the network layer.

**Key Concept:** [FastConnect Security](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm)
</details>

---

### Question 21
**Scenario:** On-premises servers must reach Object Storage privately over an existing FastConnect private virtual circuit, without using public peering.

A. Add an internet gateway to the hub VCN and route on-premises traffic to it
B. Create a separate FastConnect public virtual circuit just for Object Storage
C. Route through the DRG to a hub VCN whose service gateway reaches Oracle services
D. Copy the data to a block volume and share it over NFS from an instance

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Transit routing lets traffic arriving at the DRG pass through a hub VCN to its service gateway, giving private access to Oracle Services Network from on-premises. An internet gateway sends traffic to the public internet. A public virtual circuit is public peering, which the scenario rules out, and copying data to block storage changes the design rather than providing access.

**Key Concept:** [Private Access to Oracle Services from On-Premises](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)
</details>

---

### Question 22
**Scenario:** A regulator requires that master encryption keys for data in OCI be held in the customer's own third-party key management system outside OCI, with OCI storing only key references.

A. Import the customer's key material into an OCI Vault HSM
B. Use Oracle-managed keys and document the key rotation schedule
C. Store the keys as secrets in OCI Vault with tightly restricted IAM policies
D. Use the OCI External Key Management Service with the external KMS

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** External Key Management Service keeps key material in a supported third-party key manager outside OCI. OCI stores only references and calls out for each cryptographic operation, so the customer can revoke access. Importing keys into Vault places the material inside OCI, Oracle-managed keys give the customer no custody, and storing keys as secrets still keeps them in OCI.

**Key Concept:** [External Key Management Service](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/external_key_management.htm)
</details>

---

### Question 23
**Scenario:** Security must find which Oracle databases hold sensitive personal data, assess risky user accounts and configurations, and create masked copies for test environments.

A. Cloud Guard detector recipes on each database compartment
B. Oracle Data Safe registered against each target database
C. Vulnerability Scanning Service on the database hosts
D. Logging Analytics parsing the database alert logs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Data Safe provides security and user assessment, sensitive data discovery, data masking, and activity auditing for Oracle databases. Cloud Guard looks at cloud resource configuration rather than inside the database. Vulnerability Scanning checks hosts and images for known CVEs, and Logging Analytics analyzes logs but does not discover or mask sensitive data.

**Key Concept:** [Oracle Data Safe](https://docs.oracle.com/en-us/iaas/data-safe/index.html)
</details>

---

### Question 24
**Scenario:** A hub VCN must inspect all north-south and east-west traffic with intrusion detection and prevention, URL filtering, and TLS inspection, using a managed OCI service.

A. OCI Network Firewall in the hub VCN with route tables steering traffic to it
B. Network security groups on every spoke subnet with detailed per-port allow rules
C. Web Application Firewall policies on every load balancer
D. Stateless security lists on the DRG attachment subnets

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** OCI Network Firewall is a managed next-generation firewall, built on Palo Alto Networks technology, offering IDS/IPS, URL filtering, and TLS inspection, and it is placed in the path with route tables. NSGs and security lists filter on addresses, ports, and protocols without deep inspection. WAF protects HTTP applications behind load balancers, not all traffic between networks.

**Key Concept:** [OCI Network Firewall Overview](https://docs.oracle.com/en-us/iaas/Content/network-firewall/overview.htm)
</details>

---

### Question 25
**Scenario:** A data center runs hundreds of VMs on vSphere. The team wants to move them to OCI quickly and keep using vCenter, existing runbooks, and full administrative control of the VMware stack.

A. Convert every VM to a native OCI compute image and rebuild the runbooks
B. Containerize each application and deploy it to OKE
C. Deploy Oracle Cloud VMware Solution and migrate with VMware tooling
D. Run nested ESXi on bare metal instances without VMware support

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Oracle Cloud VMware Solution deploys a full VMware SDDC on OCI bare metal in the customer's tenancy with full administrative access, so VMs move with familiar VMware tools and operations do not change. Converting to native images or containers is a larger transformation that the scenario does not want. Nested, unsupported ESXi is not an enterprise option.

**Key Concept:** [Oracle Cloud VMware Solution Overview](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/ocvsoverview.htm)
</details>

---

### Question 26
**Scenario:** Two hundred VMs running in VMware and on AWS EC2 must be rehosted as native OCI compute instances, with discovery, replication, and planned cutover handled by an OCI service.

A. Oracle Zero Downtime Migration for each virtual machine
B. OCI Cloud Migrations with source environments and migration plans
C. A manual export of each disk image followed by a custom image import
D. The Data Transfer Service shipping disk images on appliances

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OCI Cloud Migrations discovers source VMs, replicates them, recommends target shapes and costs through migration plans, and launches them as OCI instances. Zero Downtime Migration is for Oracle databases, not whole VMs. Manual image export and import does not scale to hundreds of VMs, and shipping appliances suits bulk offline data rather than live VM rehosting.

**Key Concept:** [OCI Cloud Migrations](https://docs.oracle.com/en-us/iaas/Content/cloud-migration/home.htm)
</details>

---

### Question 27
**Scenario:** Hundreds of terabytes of archive data must move to Object Storage, but the data center's internet uplink would take months to send it.

A. Increase the parallelism of the OCI CLI multipart upload jobs
B. Compress the data and upload it through Site-to-Site VPN
C. Replicate the data with Object Storage cross-region replication
D. Use the OCI Data Transfer Service to ship the data on appliances

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The Data Transfer Service moves large data sets offline on Oracle-provided appliances or customer disks, which are shipped to Oracle and loaded into Object Storage. More upload parallelism or compression cannot overcome a link that is simply too slow. Cross-region replication copies data that is already in OCI, so it does not help get it there.

**Key Concept:** [Overview of Data Transfer Service](https://docs.oracle.com/en-us/iaas/Content/DataTransfer/Concepts/overview.htm)
</details>

---

### Question 28
**Scenario:** A stateless, horizontally scaled microservice fleet on x86 VMs must cut compute cost while keeping throughput, and the code is already built for Linux on Arm64.

A. Move to larger x86 shapes and run fewer, busier instances in each fault domain
B. Move to burstable x86 shapes with a 12.5% baseline
C. Move to Ampere Arm-based flexible shapes for price-performance
D. Move to bare metal x86 shapes to remove hypervisor overhead

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Ampere Arm shapes offer strong price-performance for scale-out, multi-threaded, stateless workloads, and the code already supports Arm64. Fewer, larger instances reduce resilience without changing the unit price. Burstable shapes suit idle-most-of-the-time workloads, not a busy fleet, and bare metal is a bigger, costlier unit for a scale-out service.

**Key Concept:** [Arm-Based Compute](https://docs.oracle.com/en-us/iaas/Content/Compute/References/arm.htm)
</details>

---

### Question 29
**Scenario:** An Autonomous Database application needs a standby in another region with the lowest data loss and fastest recovery Autonomous Database offers for regional failure.

A. Rely on the automatic backups kept in the primary region
B. Configure a cross-region Autonomous Data Guard standby database
C. Export the schema nightly with Data Pump to a bucket in the other region
D. Create a refreshable clone in the same region and refresh it weekly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A cross-region Autonomous Data Guard standby is continuously synchronized and can take over by switchover or failover, giving the lowest RPO and RTO for a regional event. Backups held in the primary region are lost with it. Nightly exports lose up to a day of data and are slow to load, and a weekly same-region clone protects neither data freshness nor the region.

**Key Concept:** [Autonomous Data Guard](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/autonomous-data-guard.html)
</details>

---

### Question 30
**Scenario:** Objects written to a bucket in the primary region must be copied automatically and asynchronously to a bucket in the DR region.

A. A lifecycle policy that moves objects to the Archive tier
B. Versioning enabled on the source bucket
C. A pre-authenticated request shared with the DR region
D. A replication policy on the source bucket targeting the DR bucket

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** An Object Storage replication policy asynchronously copies new and updated objects from the source bucket to a destination bucket, which can be in another region. Lifecycle policies change tiers or delete objects within the same bucket. Versioning protects against overwrites and deletes in place, and a pre-authenticated request is an access URL, not a copy mechanism.

**Key Concept:** [Using Replication](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication.htm)
</details>

---

## Where to go deeper

- [OCI Architect Professional cert page](../../exams/oracle/oci-architect-professional/) - notes, practice plan, strategy
- [OCI Architect Associate practice questions](./oracle-oci-architect-associate.md) - the prerequisite level
- [OCI Operations Associate practice questions](./oracle-oci-operations-associate.md) - the operations counterpart
- [SRE and reliability topic index](../../topics/sre-and-reliability.md) - DR and availability in practice
- **[📖 Oracle University certification](https://education.oracle.com/oracle-certification-path/pFamily_647)** - official exam pages
