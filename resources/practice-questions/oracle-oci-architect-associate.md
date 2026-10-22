---
last-updated: 2026-10-22
difficulty: intermediate
---

# Oracle Cloud Infrastructure Architect Associate (1Z0-1072) - Practice Questions

30 questions for OCI Architect Associate prep, weighted toward networking (25%), then compute, storage, and security (15% each), and IAM, database, and observability (10% each).

> **Cert page:** [exams/oracle/oci-architect-associate/](../../exams/oracle/oci-architect-associate/)

---

### Question 1
**Scenario:** An instance must access Object Storage without any credential stored on it.

A. A public bucket
B. An API key and private PEM file stored in the opc user's .oci directory and rotated manually by an administrator each quarter
C. A shared password
D. A dynamic group matching the instance, with a policy granting that dynamic group access (instance principals)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Instance principals let a compute instance authenticate as itself, so there is no key to rotate or leak. The dynamic group's matching rule defines which instances are included, typically by compartment or by a defined tag.
</details>

---

### Question 2
**Scenario:** Two VCNs in the same region must communicate privately.

A. A local peering gateway in each VCN, with route rules and non-overlapping CIDRs
B. An internet gateway
C. A service gateway
D. A NAT gateway in each VCN, which lets the instances reach the private addresses of the other VCN

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Local peering connects VCNs in the same region; remote peering through DRGs connects across regions. Both require non-overlapping address space and explicit route rules and security list entries on each side.
</details>

---

### Question 3
**Scenario:** Many VCNs and an on-premises network must interconnect with centralized routing.

A. A load balancer
B. A dynamic routing gateway with route tables and route distribution (transit routing)
C. Separate internet gateways on each VCN, with traffic between networks crossing the public internet
D. A full mesh of local peering gateways between every pair of VCNs, each with its own static routes and no central route table

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The DRG is the hub: VCN attachments plus FastConnect or VPN attachments, with DRG route tables controlling which attachment learns which routes. A peering mesh grows quadratically and gives no central place to express policy.
</details>

---

### Question 4
**Scenario:** Security lists and network security groups both exist. Which should be preferred?

A. Security lists, because they let you target individual VNICs and can reference other lists as sources
B. Network security groups, which apply to chosen VNICs and can reference each other
C. Skip them, because OCI relies only on host-based firewalls inside each instance for traffic filtering
D. Security lists, because they are the newer feature and replace network security groups entirely

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** NSGs let you write rules like "the application NSG may reach the database NSG on 1521" without hard-coding CIDRs, which survives IP changes. Security lists apply to the whole subnet, which is coarser and harder to reason about as the subnet grows.
</details>

---

### Question 5
**Scenario:** A workload must scale out automatically based on CPU.

A. Manual instance creation by an operator who watches the CPU graph in the Console and adds instances
B. A larger shape
C. A load balancer alone, which spreads traffic across the existing instances but never adds any new ones
D. An instance pool from an instance configuration, with an autoscaling policy on a metric

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The instance configuration is the template, the pool manages the set, and the autoscaling configuration adds and removes members. Scheduled autoscaling is the alternative when the load pattern is known in advance.
</details>

---

### Question 6
**Scenario:** Block volume performance must be increased for a database.

A. Change the volume performance level (balanced, higher performance, or ultra high performance), since IOPS scales with size and performance units
B. Change the instance shape
C. Add more volumes only
D. Use Object Storage

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** OCI block volumes have selectable performance tiers, and the setting can be changed on a live volume. Note that performance also scales with volume size, so a small volume at a high tier still has a ceiling.
</details>

---

### Question 7
**Scenario:** A database must survive an availability domain failure with minimal data loss.

A. A read replica in the same availability domain, which offloads queries but fails together with the primary
B. Backups only
C. Data Guard in synchronous (maximum availability) mode to a standby in another AD or region
D. A larger shape

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Data Guard maintains a standby that can take over, with the protection mode setting the RPO: maximum availability gives near-zero data loss at the cost of commit latency, while maximum performance is asynchronous with a larger RPO.
</details>

---

### Question 8
**Scenario:** Administrative access to a private instance is needed without a public IP.

A. Open port 22 to the internet
B. A jump host with a public IP and port 22 open to 0.0.0.0/0, shared by all of the administrators
C. A VPN for every user
D. OCI Bastion service, creating time-limited managed SSH sessions to private resources

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The Bastion service provides ephemeral sessions with a defined TTL and IAM control over who may create them, so there is no permanently exposed jump host to patch and defend. Sessions are also audited.
</details>

---

### Question 9
**Scenario:** A load balancer must terminate TLS and route by URL path.

A. A NAT gateway, which lets private instances start outbound connections to the internet
B. A flexible load balancer at layer 7 with a certificate and path-based routing
C. A network load balancer, which works at layer 4 and passes TLS through without inspecting URL paths
D. DNS round robin across the backend servers, with no health checks or path awareness

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The layer 7 load balancer terminates TLS and can inspect the request to route by hostname or path. The network load balancer is layer 4, preserves the source IP, and offers lower latency but cannot read a URL.
</details>

---

### Question 10
**Scenario:** Object Storage costs must fall for data accessed rarely.

A. Delete it
B. Move to Block Volume, which offers lower per-gigabyte pricing than infrequent access object tiers
C. Lifecycle policy rules transitioning objects to infrequent access and then archive tiers
D. Compress it only, using a client-side tool before upload, and leave it in the standard tier forever

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Lifecycle rules automate tiering and deletion. The archive tier is much cheaper per gigabyte but requires a restore before the object can be read, so it suits compliance retention rather than anything that must be available on demand.
</details>

---

### Question 11
**Scenario:** A compartment's resources must be constrained so nobody can create non-compliant configurations.

A. A Security Zone on the compartment, which denies operations that violate its policies
B. Tags applied to the compartment's resources to mark them as compliant, which label but do not block operations
C. Documentation that lists the approved configurations and is circulated to every team in the tenancy
D. Budgets with alert rules that email the compartment owners when spending passes a set threshold

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Security Zones are preventive: they refuse the create or update operation, for example a public bucket or an unencrypted volume. Cloud Guard is the detective counterpart that finds problems after the fact.
</details>

---

### Question 12
**Scenario:** An alarm must notify a team when CPU exceeds a threshold.

A. A Monitoring alarm on the metric with a notification topic, subscribed by email, a function, or another endpoint
B. An event only
C. A log search
D. Check manually

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Alarms evaluate metric queries and publish to Notifications topics, which fan out to subscriptions. Events are the separate, resource-lifecycle mechanism that fires on state changes such as an instance being created.
</details>

---

### Question 13
**Scenario:** Cost must be attributed to teams sharing one tenancy.

A. Estimate
B. Compartment-based reporting and cost-tracking tags, with budgets scoped accordingly
C. One compartment for everything
D. Split evenly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cost-tracking tags are a specific tag category that appears in cost reports, and tag defaults on a compartment make application automatic for new resources. Without enforcement, tag coverage decays and the attribution becomes fiction.
</details>

---

### Question 14
**Scenario:** A file share must be mounted by many instances concurrently.

A. Object Storage, which serves objects over HTTP and has no mount targets or file locking
B. Local disk
C. File Storage service, providing NFS shares with mount targets in a subnet
D. Block Volume attached read-write to each instance and formatted with an ordinary ext4 file system

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** File Storage gives POSIX semantics with concurrent access, which is what shared application state or home directories need. Block volumes support multi-attach only with a cluster-aware filesystem, which is a more specialized arrangement.
</details>

---

### Question 15
**Scenario:** An architecture must span two regions for disaster recovery.

A. A second availability domain in the same region, with the workload spread evenly across both domains and a load balancer
B. Cross-region replication of the data, infrastructure as code, and a rehearsed failover
C. One region with frequent backups kept in a bucket in that same region, and restored after an outage if needed
D. Larger instances with more OCPUs and memory in the primary region, to absorb the extra load after any failure

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Three pieces are required: the data must already be there, the infrastructure must be reproducible, and the failover must have been practiced. Missing the third is why untested DR plans fail on a dependency nobody documented.
</details>

---

### Question 16
**Scenario:** A private subnet's instances must reach the on-premises network 172.16.0.0/16, which is connected to the VCN through a DRG with a Site-to-Site VPN.

A. Add a route rule for 172.16.0.0/16 targeting the VCN's NAT gateway
B. Add a route rule for 172.16.0.0/16 targeting the attached DRG
C. Add a route rule for 0.0.0.0/0 targeting the VCN's internet gateway
D. Add an ingress rule for 172.16.0.0/16 to the subnet's security list only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Traffic leaves a subnet according to its route table, so the on-premises CIDR needs a rule whose target is the DRG that carries the VPN. A NAT gateway or internet gateway sends traffic to the internet, not over the VPN. Security list rules allow or deny traffic but do not route it anywhere.

**Key Concept:** [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm)
</details>

---

### Question 17
**Scenario:** For a high-volume service, an architect replaced stateful security list rules with a stateless ingress rule allowing TCP 443. Clients now connect but never receive responses.

A. Stateless rules only work with network security groups, not lists
B. Stateless rules require a NAT gateway for the return path
C. TCP 443 cannot be used in a stateless security rule
D. A matching stateless egress rule for the return traffic is missing

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Stateless rules do not track connections, so response traffic is evaluated on its own and needs its own egress rule (to the client ports). Stateful rules allow responses automatically, which is why they are the default. Both security lists and NSGs support stateless rules, any port can be used, and a NAT gateway has nothing to do with responses to inbound connections.

**Key Concept:** [Security Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm)
</details>

---

### Question 18
**Scenario:** A fleet of firewall appliances needs load balancing for TCP and UDP traffic with very low latency, and the backends must see the original client source IP.

A. Network Load Balancer in pass-through mode
B. Flexible Load Balancer with an HTTP listener
C. Flexible Load Balancer with SSL termination
D. A DNS traffic management steering policy

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Network Load Balancer is a non-proxy, layer 4 service that preserves source and destination IPs and suits appliances, UDP, and latency-sensitive flows. The flexible Load Balancer is a layer 7 proxy, so backends see the load balancer's address, and HTTP or SSL listeners do not handle UDP. DNS steering distributes by name resolution and is not a per-flow load balancer.

**Key Concept:** [Network Load Balancer Overview](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/overview.htm)
</details>

---

### Question 19
**Scenario:** A VCN in Frankfurt must communicate privately with a VCN in London without traffic crossing the internet.

A. A local peering gateway in each VCN
B. A Site-to-Site VPN between two internet gateways
C. A remote peering connection between DRGs in each region
D. A service gateway in each VCN

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Peering VCNs in different regions uses a remote peering connection (RPC) on the DRG in each region, and the traffic stays on Oracle's backbone. Local peering only works within a single region. A VPN between internet gateways is not how OCI connects VCNs, and a service gateway reaches Oracle services, not other VCNs.

**Key Concept:** [Remote VCN Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm)
</details>

---

### Question 20
**Scenario:** Instances in OCI must resolve names in an on-premises DNS zone, and on-premises servers must resolve names in an OCI private zone.

A. Copy every record into public DNS zones in both locations
B. Use the VCN private resolver with listening and forwarding endpoints
C. Add all hostnames to each instance's `/etc/hosts` file
D. Point every instance at a public DNS resolver on the internet

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A VCN's private resolver can forward queries for on-premises domains through a forwarding endpoint and accept queries from on-premises through a listening endpoint, giving hybrid resolution in both directions. Publishing private records in public zones exposes them. Host files do not scale or stay current, and public resolvers cannot see private zones.

**Key Concept:** [Private DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm)
</details>

---

### Question 21
**Scenario:** A DR plan depends on launching 40 instances of a specific shape in the standby region during a regional outage, when many other customers may be doing the same.

A. Rely on on-demand capacity being available at failover time
B. Pre-create instance configurations for the shape in the standby region
C. Use preemptible instances in the standby region to save cost
D. Create a compute capacity reservation in the standby region

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A capacity reservation sets aside compute capacity for your tenancy so launches succeed when demand spikes, which is the risk in a regional failover. On-demand capacity is not guaranteed. An instance configuration is only a template and reserves nothing, and preemptible instances can be reclaimed, the opposite of what DR needs.

**Key Concept:** [Reserving Compute Capacity](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm)
</details>

---

### Question 22
**Scenario:** A workload ran on 8 vCPUs in another cloud. It is moving to an OCI x86 flexible shape billed in OCPUs, and should get the equivalent processing capacity.

A. 4 OCPUs, because one x86 OCPU equals two vCPUs
B. 8 OCPUs, because one OCPU equals one vCPU
C. 16 OCPUs, because one vCPU equals two OCPUs
D. 2 OCPUs, because one OCPU equals four vCPUs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** On x86 processors one OCPU is one physical core with two hardware threads, which equals two vCPUs, so 8 vCPUs maps to 4 OCPUs. Choosing 8 OCPUs doubles the capacity and cost, and 16 quadruples it. Two OCPUs would halve the capacity. Sizing errors here are a common source of overspending after migration.

**Key Concept:** [Compute Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm)
</details>

---

### Question 23
**Scenario:** An external partner without an OCI account must upload files to one bucket for the next 7 days, and must not be able to read anything else.

A. Create an IAM user for the partner with bucket-level policies
B. Make the bucket public for writes for 7 days
C. Create a pre-authenticated request for object writes that expires in 7 days
D. Share an administrator's API signing key with the partner

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A pre-authenticated request gives URL-based access to a bucket or object with a chosen operation and an expiry date, without an OCI identity. Creating an IAM user is heavier than needed for a short external task. Public buckets cannot grant anonymous writes safely, and sharing an admin key hands over far more than one bucket.

**Key Concept:** [Using Pre-Authenticated Requests](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)
</details>

---

### Question 24
**Scenario:** An application's data is spread across a boot volume and three block volumes. Backups must capture all four at the same point in time so the application restores consistently.

A. Schedule separate backups for each volume at the same minute
B. Put the volumes in a volume group and back up the group
C. Copy the files to Object Storage with a cron job each night
D. Clone each volume one after another during off-hours

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A volume group backup takes a coordinated, crash-consistent point-in-time copy of every volume in the group. Separate backups scheduled for the same minute still run independently and can differ. A cron copy at file level is not consistent across volumes, and sequential clones each capture a different moment.

**Key Concept:** [Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
</details>

---

### Question 25
**Scenario:** A public web application behind an OCI load balancer must be protected against SQL injection, cross-site scripting, and bot traffic.

A. Attach a Web Application Firewall policy to the load balancer
B. Add stricter stateful rules to the subnet's security lists
C. Enable Cloud Guard detector recipes on the compartment
D. Move the application into a private subnet with no load balancer

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** OCI WAF inspects HTTP requests and blocks application-layer attacks such as SQL injection and XSS, and offers bot management, and it can be attached to a load balancer. Security lists filter by IP, port, and protocol and cannot see request content. Cloud Guard finds configuration problems, and removing the load balancer makes a public application unreachable.

**Key Concept:** [Web Application Firewall Overview](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/overview.htm)
</details>

---

### Question 26
**Scenario:** Employees already sign in with Microsoft Entra ID. They must use the same corporate identity to access the OCI Console, without separate OCI passwords.

A. Create matching local users in OCI and sync passwords nightly
B. Give every employee an API signing key instead of a password
C. Share a single OCI administrator account across the employees
D. Federate the OCI identity domain with Entra ID using SAML

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Federation lets the identity domain trust the corporate identity provider, so users sign in with existing credentials and group mappings drive their OCI permissions. Syncing passwords into local users duplicates identities and secrets. API keys are for programmatic access, not console sign-in, and a shared account breaks accountability.

**Key Concept:** [Federating with Identity Providers](https://docs.oracle.com/en-us/iaas/Content/Identity/federating/federating_section.htm)
</details>

---

### Question 27
**Scenario:** A policy `allow group NetAdmins to manage virtual-network-family in compartment Prod` exists. Prod contains child compartments Prod-Web and Prod-DB.

A. NetAdmins can manage networking in Prod only, not its children
B. NetAdmins need separate policies in each child compartment
C. NetAdmins can manage networking in Prod and all its children
D. NetAdmins can manage networking anywhere in the tenancy

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Policies are inherited downward: access granted in a compartment applies to all compartments nested inside it. Separate child policies are unnecessary for this reason. The grant does not extend upward or sideways, so it does not cover the rest of the tenancy. Inheritance is why policies at high levels deserve careful review.

**Key Concept:** [How Policies Work](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/how-policies-work.htm)
</details>

---

### Question 28
**Scenario:** An Oracle database on OCI must keep running if one database server node fails, with no failover to a standby and no change of connection endpoint.

A. A single-node DB system with daily automatic backups
B. A multi-node RAC DB system in Base Database Service
C. A single-node DB system with a cross-region backup copy
D. A Data Guard standby in a second region

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Real Application Clusters runs one database across multiple nodes, so the loss of a node leaves the others serving connections without a role change. Backups require a restore, which means downtime. Data Guard protects against larger failures but works by switching to a separate standby database, which the scenario rules out.

**Key Concept:** [About Oracle Base Database Service](https://docs.oracle.com/en-us/iaas/base-database/doc/overview-base-database-service.html)
</details>

---

### Question 29
**Scenario:** All logs from the Logging service must be copied continuously to an Object Storage bucket for long-term retention, without writing custom code.

A. Create a Connector Hub connector from Logging to Object Storage
B. Write a scheduled function that exports logs to the bucket
C. Increase the log group retention period to ten years
D. Enable the Audit service on the bucket's compartment

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Connector Hub (formerly Service Connector Hub) moves data between OCI services, such as from Logging to Object Storage, Streaming, or Monitoring, with no code to maintain. A scheduled function works but is custom code the scenario rules out. Logging retention is capped and is not archival storage, and Audit records API calls rather than exporting logs.

**Key Concept:** [Connector Hub Overview](https://docs.oracle.com/en-us/iaas/Content/connector-hub/overview.htm)
</details>

---

### Question 30
**Scenario:** A multi-tier application spans compute, databases, and load balancers. Cross-region switchover must be orchestrated in the right order with one action and tested regularly.

A. A runbook document that operators follow step by step
B. Cross-region backup copies restored by hand when needed
C. A DNS steering policy that points at the standby region
D. OCI Full Stack Disaster Recovery with a DR protection group

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Full Stack Disaster Recovery groups the application's resources into protection groups and runs ordered DR plans for switchover and failover, including prechecks for testing. A manual runbook and hand restores are slow and error-prone. DNS steering only redirects traffic; it does not bring the standby tiers up in order.

**Key Concept:** [Full Stack Disaster Recovery](https://docs.oracle.com/en-us/iaas/disaster-recovery/index.html)
</details>

---

## Where to go deeper

- [OCI Architect Associate cert page](../../exams/oracle/oci-architect-associate/) - notes, practice plan, strategy
- [OCI Foundations practice questions](./oracle-oci-foundations.md) - the level below
- [OCI Architect Professional practice questions](./oracle-oci-architect-professional.md) - the level above
- [VPC explained](../../learn/concepts/vpc-explained.md) - cloud networking fundamentals
- **[📖 Oracle University certification](https://education.oracle.com/oracle-certification-path/pFamily_647)** - official exam pages
