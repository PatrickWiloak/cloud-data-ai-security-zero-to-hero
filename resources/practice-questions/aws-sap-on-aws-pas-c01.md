---
last-updated: 2026-10-22
difficulty: advanced
---

# AWS Certified SAP on AWS - Specialty (PAS-C01) - Practice Questions

30 questions for PAS-C01 prep, weighted toward designing (30%) and implementing (30%) SAP workloads on AWS, then managing and operating (24%) and securing (16%).

PAS-C01 has been retired by AWS. The architectural content remains applicable to running SAP on AWS; confirm exam availability before planning to sit it.

> **Cert page:** [exams/aws/specialty/sap-on-aws-pas-c01/](../../exams/aws/specialty/sap-on-aws-pas-c01/)

---

### Question 1
**Scenario:** An SAP HANA production database must run on AWS with vendor support.

A. An SAP-certified instance type from the certified list, meeting CPU-to-memory and storage KPIs
B. Lambda
C. Any EC2 instance type with enough memory, since SAP supports HANA on any instance that passes the HCMT benchmark
D. A container

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** SAP only supports HANA on certified configurations, so the instance family, size, and storage layout all come from the certification list rather than from general sizing intuition. Running on an uncertified type puts you outside support, which is usually a contractual problem before it is a technical one.
</details>

---

### Question 2
**Scenario:** HANA data and log volumes must meet SAP's storage KPIs.

A. EFS for everything, since its elastic throughput scales automatically and removes the need to size volumes
B. gp2 volumes sized by capacity
C. io2 or gp3 volumes provisioned to meet the KPIs, with separate data, log, and shared volumes
D. Instance store only, using the local NVMe disks that come with the instance for both the data and log files

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** HANA's log writes are latency-sensitive and its data volume is throughput-sensitive, so the volumes are sized against IOPS and MB/s targets rather than capacity alone. Separating data, log, and shared volumes is part of the certified layout, and HCMT is the tool that validates it.
</details>

---

### Question 3
**Scenario:** SAP application servers must fail over across Availability Zones with minimal downtime.

A. A Pacemaker cluster across two AZs with an overlay IP and a shared file system
B. A single instance with backups taken every night and restored by hand after a failure
C. Manual restart of the failed server by an on-call administrator after an alert fires
D. Auto Scaling of the ASCS, so a replacement instance launches and takes over the message server on failure

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The ASCS and ERS instances are the single points of failure, so they run in a cluster with an overlay IP routed by a route table update on failover. Auto Scaling does not apply because these are stateful, licensed singleton components rather than interchangeable replicas.
</details>

---

### Question 4
**Scenario:** A shared file system is needed for `/sapmnt` across application servers.

A. S3 mounted as a filesystem
B. Amazon EFS or Amazon FSx for NetApp ONTAP, mounted across AZs
C. EBS attached to one instance
D. Local disk

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `/sapmnt` and the transport directory need concurrent POSIX access from many hosts, which EFS and FSx provide across AZs. EBS is single-attach for this purpose, and S3 is object storage without the file semantics SAP expects.
</details>

---

### Question 5
**Scenario:** A migration from on-premises SAP ECC to AWS must minimize downtime for a 20 TB database.

A. Offline export and import of the whole 20 TB database during a weekend window, using parallel export options
B. Copy the VM image
C. Near-zero downtime: database replication or backup and restore with log shipping, then a short cutover
D. Rebuild the system from scratch in AWS and re-enter the master and transactional data by hand over several weeks

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Keeping the source running while the target catches up through replication is what compresses the downtime window from days to hours. Classic heterogeneous migration with export and import is still used when a platform change is required, and the parallel export and import options are what make it tolerable.
</details>

---

### Question 6
**Scenario:** HANA must be protected against an AZ failure with an RPO near zero.

A. Backups to S3 only
B. EBS snapshots hourly, copied to a second AZ, which keeps the data loss to at most the last hour
C. Asynchronous replication to a second region only, accepting some data loss when an AZ fails
D. HANA System Replication in synchronous mode to a secondary in another AZ

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Synchronous HSR acknowledges commits only after the secondary has the log, so RPO is effectively zero at the cost of some commit latency across AZs. Asynchronous replication to a distant region is the DR tier, where a larger RPO is accepted in exchange for distance.
</details>

---

### Question 7
**Scenario:** SAP backups must be stored durably and restorable quickly.

A. Backint-integrated backup to S3, with lifecycle rules for older backups
B. No backups, because HANA System Replication already copies every committed change to the secondary
C. Tape
D. Backups to local EBS only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** AWS Backint for SAP HANA writes backups directly to S3 from the database's own backup interface, so it is integrated with HANA Studio and Cockpit rather than bolted on. Replication is not a backup: it faithfully replicates a logical corruption or a bad transport.
</details>

---

### Question 8
**Scenario:** Non-production SAP systems must reduce cost outside business hours.

A. Terminate them every evening and rebuild them from an AMI before the start of the next business day
B. Reduce the database size by archiving old data out of the systems, which lowers the cost of every instance
C. Use Spot Instances, which cost up to 90 percent less and can simply be restarted if one is reclaimed
D. Schedule stop and start with Systems Manager or Instance Scheduler, keeping the EBS volumes

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Stopping instances stops compute charges while EBS persists, which suits development and QA systems used only in working hours. Spot is not appropriate for SAP because an interruption to a stateful, licensed system is disruptive and slow to recover.
</details>

---

### Question 9
**Scenario:** Which service provides SAP-aware operational visibility on AWS?

A. Amazon Inspector
B. AWS Systems Manager for SAP, with AWS Launch Wizard for deployment
C. AWS Glue
D. CloudFront

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Launch Wizard deploys certified SAP architectures with the right instance and storage layout, and Systems Manager for SAP provides discovery, backup integration, and operational actions that understand SAP components rather than just EC2 instances.
</details>

---

### Question 10
**Scenario:** Network latency between application servers and HANA must be minimized.

A. Route through Transit Gateway between the application subnets and the database subnet
B. Use a NAT gateway between the application servers and the database for all connections
C. Place them in the same AZ, in a cluster placement group where supported
D. Spread them across regions so each tier sits close to its own users and is isolated from failures

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** SAP application-to-database traffic is chatty and latency-sensitive, so same-AZ placement is the standard design, with HA achieved by a second AZ pair rather than by splitting a single system. Cross-region separation of app and database is not a supported design.
</details>

---

### Question 11
**Scenario:** SAP systems must be reachable from the corporate network only.

A. An internet-facing load balancer, with the SAP application servers registered as targets and reachable from any client
B. Private subnets reached over Direct Connect or VPN, with no internet-facing endpoints for SAP
C. Public IPs on the servers, filtered only by an allowlist in the OS host firewall
D. Public subnets with security groups open to the internet on the SAP ports, relying on the SAP logon screen alone

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SAP systems are internal business applications, so the default is no direct internet exposure at all. Where external access is genuinely required, such as Fiori for remote users, it is fronted by a reverse proxy or Web Dispatcher in a DMZ subnet with WAF, rather than exposing the application servers.
</details>

---

### Question 12
**Scenario:** SAP data must be encrypted at rest with organizational key control.

A. EBS and S3 encryption with KMS customer managed keys, plus HANA data volume encryption
B. Application-level only, using SAP secure storage and custom encryption in ABAP for sensitive tables
C. No encryption needed on a private network
D. Encrypt backups only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Layered encryption is the norm: the storage layer covers volumes and backups, and HANA's own data and log volume encryption covers the database files independently. A customer managed key gives you revocation and audit through CloudTrail, which is usually the actual compliance requirement.
</details>

---

### Question 13
**Scenario:** Right-sizing an SAP landscape after migration.

A. Guess
B. Always use the largest instance
C. Use SAP sizing outputs (SAPS requirements) plus observed CloudWatch and HANA metrics to resize, then consider Savings Plans or Reserved Instances for the steady state
D. Keep on-premises sizing permanently

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** On-premises sizing usually embeds years of growth headroom bought up front, which is exactly the cost the cloud lets you release. Resize based on measured utilization first, then commit to the resulting steady state to capture the discount.
</details>

---

### Question 14
**Scenario:** A DR region must be maintained cost-effectively for SAP.

A. No DR, relying on the primary region's multiple Availability Zones to cover every possible failure
B. A full-size duplicate landscape running permanently, so failover needs no scaling step but spend doubles
C. Backups only, copied to the DR region, with a full rebuild from scratch once a disaster is declared
D. Pilot light: replicate data continuously, keep little running, and scale up by automation

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Pilot light matches most SAP DR requirements: HANA System Replication keeps the data current while the application tier stays small or stopped until needed. The critical part is that the scale-up is automated and rehearsed, otherwise the RTO is fictional.
</details>

---

### Question 15
**Scenario:** SAP licensing and support obligations on AWS.

A. No licenses are required in the cloud
B. You bring your own SAP licenses; AWS provides certified infrastructure; support is shared by SAP, AWS, and the OS vendor
C. Licenses are per-region
D. AWS provides SAP licenses bundled into the EC2 hourly price, and AWS support handles all application issues for every SAP module

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SAP licensing is a contract with SAP regardless of where it runs. What AWS provides is certified infrastructure and its own support; SAP supports the application, and the OS vendor supports the cluster stack. Knowing which vendor owns which problem is what makes an incident tractable.
</details>

---

### Question 16
**Scenario:** An S/4HANA production database needs about 18 TB of memory. The team prefers a single scale-up node, which SAP recommends for OLTP workloads of this kind.

A. A cluster of memory-optimized r-family instances in scale-out, splitting the OLTP tables across nodes
B. An Amazon EC2 High Memory instance from the SAP-certified list, sized for the 18 TB requirement
C. An x-family instance with additional EBS volumes used as swap to cover the missing memory
D. Amazon RDS with a HANA-compatible engine, sized by the memory needed for the in-memory tables

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** EC2 High Memory instances (the u-family) are certified for very large SAP HANA scale-up deployments and offer memory in the multi-terabyte range in one node. Scale-out for OLTP is possible only in specific certified configurations and adds complexity the team wants to avoid. HANA is an in-memory database, so swap does not substitute for memory. RDS does not offer HANA.
</details>

---

### Question 17
**Scenario:** A BW/4HANA analytics system will outgrow the memory of the largest certified node the company is willing to run, and analytics workloads are expected to keep growing.

A. HANA scale-out across several SAP-certified instances, with a shared file system for /hana/shared
B. A single larger instance each year, migrating the database every time the system outgrows the node
C. Moving older data into Amazon S3 Glacier and querying it directly from HANA without any data tiering tool
D. Splitting the data into several independent HANA systems and joining the results in Excel

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** SAP supports HANA scale-out for OLAP workloads such as BW/4HANA on certified instance types, with nodes sharing /hana/shared (on EFS or FSx for NetApp ONTAP). Repeated scale-up migrations are disruptive. HANA cannot query Glacier directly; data tiering uses supported options such as native storage extension. Independent systems break the single analytical model.
</details>

---

### Question 18
**Scenario:** The team wants HANA data and log volumes on a certified managed storage service that supports near-instant snapshots and space-efficient clones for fast system refreshes.

A. Amazon S3 mounted with a file gateway, which presents buckets as NFS shares to the HANA hosts
B. Instance store volumes, which give the lowest latency and survive stops and restarts of the instance
C. Amazon FSx for NetApp ONTAP, which is certified for HANA data and log and supports snapshots and clones
D. Amazon EFS One Zone, which is certified for HANA log volumes and supports writable clones

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** FSx for NetApp ONTAP is certified for HANA data and log volumes and offers ONTAP snapshots and FlexClone, which make system copies fast and space efficient. S3 through a gateway does not meet HANA latency KPIs. Instance store data is lost when the instance stops. EFS is used for shared directories such as /sapmnt, not HANA data and log, and has no writable clones.
</details>

---

### Question 19
**Scenario:** A company wants to run S/4HANA on AWS but have SAP take responsibility for the infrastructure, technical operations, and the software subscription under a single contract.

A. Bring-your-own-license on EC2, with an AWS Managed Services contract covering the SAP application
B. AWS Launch Wizard for SAP, which transfers operational responsibility to SAP once deployment finishes
C. SAP Business Technology Platform, which runs the customer's S/4HANA system as a multi-tenant service
D. RISE with SAP, choosing AWS as the hyperscaler under SAP's managed offering

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** RISE with SAP bundles the S/4HANA subscription with SAP-managed infrastructure and technical operations on a chosen hyperscaler, such as AWS. BYOL on EC2 keeps the customer (or its partner) responsible for operations. Launch Wizard is a deployment tool and transfers nothing. BTP is a platform for extensions and integration, not where a customer's own S/4HANA system is hosted.
</details>

---

### Question 20
**Scenario:** Analysts want sales order data from SAP S/4HANA in an S3 data lake every day, using a managed AWS service without writing extraction code.

A. Amazon AppFlow with the SAP OData connector, writing the extracted data to Amazon S3 on a schedule
B. AWS DataSync, which reads SAP tables directly from the HANA data volume files on a nightly run
C. Amazon Kinesis Data Firehose, which subscribes to SAP change documents without any source connector
D. AWS Backint Agent, which writes table-level extracts to S3 that analysts can query directly in Athena

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** AppFlow has an SAP OData connector that pulls data from SAP through OData services and lands it in S3 on a schedule or on demand. DataSync copies files, and HANA volume files are not readable as tables. Firehose needs a producer and has no SAP source of its own. Backint writes database backups, which are not queryable extracts.
</details>

---

### Question 21
**Scenario:** An ASCS cluster uses an overlay IP outside the VPC CIDR. Application servers inside the VPC reach it, but users on-premises connecting through a Transit Gateway cannot.

A. Assign an Elastic IP to the overlay IP, so on-premises users reach the ASCS over the internet instead
B. Add the overlay IP to the VPC's DHCP options set, which advertises it to on-premises over BGP
C. Enable route propagation on the VPC subnets, which publishes the overlay IP to every attached network
D. Add a static route for the overlay IP to the Transit Gateway route table, or front the cluster with an NLB

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** An overlay IP is routed by a VPC route table entry pointing at the active node, so traffic from outside the VPC needs a path to it: a static route for the overlay IP on the Transit Gateway pointing at the VPC attachment, or a Network Load Balancer targeting the overlay IP. Elastic IPs map to private addresses on interfaces and would expose the ASCS publicly. DHCP options do not advertise routes, and subnet route propagation does not publish arbitrary VPC route entries to the Transit Gateway.
</details>

---

### Question 22
**Scenario:** A Pacemaker cluster for HANA and ASCS needs an operating system with SAP-specific tuning, the high availability extension, and extended update support.

A. Amazon Linux 2023, which includes Pacemaker and is supported by SAP for HANA production workloads
B. SUSE Linux Enterprise Server for SAP or Red Hat Enterprise Linux for SAP, from AWS or AWS Marketplace
C. Any Linux distribution, with the HA packages compiled from source and tuning applied by hand
D. Windows Server Failover Clustering, which is the supported HA option for HANA on Linux instances

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SLES for SAP and RHEL for SAP are the operating systems supported for HANA production, and the "for SAP" editions include the HA add-on, SAP tuning, and extended update support. Amazon Linux is not a supported HANA OS. Self-compiled HA stacks are unsupported. HANA does not run on Windows.
</details>

---

### Question 23
**Scenario:** ABAP developers want custom SAP programs to put files in Amazon S3 and call Amazon Translate directly from ABAP code.

A. Write the AWS Signature Version 4 request signing by hand in ABAP for every AWS API that is called
B. Export the data to a shared file system and have a cron job on another server copy it to S3
C. The AWS SDK for SAP ABAP, which provides ABAP APIs for AWS services
D. SAP Cloud Connector, which signs AWS API requests from ABAP on behalf of the SAP system

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The AWS SDK for SAP ABAP gives ABAP programs native modules for AWS services such as S3 and Translate, with credential handling and request signing built in. Hand-written signing is error-prone and costly to maintain. A file-copy job adds a hop and does not call Translate. SAP Cloud Connector links on-premises systems to SAP BTP and does not sign AWS API requests.
</details>

---

### Question 24
**Scenario:** SAP support must see AWS infrastructure metrics, such as CPU and storage statistics, inside SAP monitoring transactions for a production system on EC2.

A. Install the AWS Data Provider for SAP on each instance, with an IAM role that allows it to read the metrics
B. Enable detailed CloudWatch monitoring, which forwards metrics to SAP transactions automatically
C. Install the CloudWatch agent alone, since SAP transactions read the agent's log files directly
D. Grant SAP support console access to the AWS account so they can read CloudWatch themselves

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** SAP requires the AWS Data Provider for SAP on EC2 for supported systems. It collects AWS metrics through CloudWatch and EC2 APIs and makes them available to the SAP host agent, so they appear in SAP transactions such as ST06. Detailed monitoring and the CloudWatch agent do not feed SAP transactions. Giving SAP console access is unnecessary and widens access.
</details>

---

### Question 25
**Scenario:** A QA system must be refreshed from production every month, and the current export and restore takes two days.

A. Rebuild QA from installation media each month and import production data with transport requests
B. Run HANA System Replication from production to QA permanently, so QA always mirrors production
C. Copy production data to QA one table at a time with SQL scripts during the weekend window
D. Restore QA from production snapshots, then run SAP post-copy steps such as renaming and anonymizing data

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Storage-level snapshots (EBS or FSx for NetApp ONTAP clones) create a consistent copy of production quickly, after which standard SAP post-copy activities rename the system and protect sensitive data. Rebuilding from media and transports does not copy data. Permanent replication turns QA into a standby that cannot be used for testing. Table-by-table copies are slow and risk inconsistency.
</details>

---

### Question 26
**Scenario:** Operating system patches must be applied to SAP application servers monthly, only during the agreed SAP downtime window, with a record of compliance.

A. Enable automatic unattended upgrades on each server, so patches install as soon as they are released
B. AWS Systems Manager Patch Manager with a patch baseline and a maintenance window aligned to SAP downtime
C. Replace every server with a new AMI each month, without stopping the SAP instances first
D. Patch only when SAP support requests it, since SAP systems do not need regular OS patching

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Patch Manager applies patches from a baseline during a Systems Manager maintenance window and reports patch compliance, so patching happens only in the agreed window and is auditable. Unattended upgrades ignore the downtime window. Replacing servers without stopping SAP risks inconsistency. Skipping regular patching leaves known vulnerabilities in place.
</details>

---

### Question 27
**Scenario:** Operations wants automatic detection and dashboards for HANA problems, such as log volume growth and high memory use, without building custom metrics by hand.

A. CloudWatch Application Insights with SAP HANA as a monitored component
B. AWS Trusted Advisor, which checks HANA memory and log usage against SAP KPIs
C. Amazon Inspector, which scans HANA databases for memory and log space problems
D. AWS Config, which records HANA memory use as a configuration item for each change

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** CloudWatch Application Insights supports SAP HANA (and NetWeaver), sets up relevant metrics, logs, and alarms, and detects common problems with dashboards. Trusted Advisor checks account-level best practices, not HANA internals. Inspector scans for vulnerabilities. Config records resource configuration, not runtime metrics.
</details>

---

### Question 28
**Scenario:** HANA databases use AWS Backint Agent to back up to S3. The security team wants least privilege for the backup path.

A. Attach AdministratorAccess to the instance profile, so backups never fail on missing permissions
B. Store an IAM user's access keys in the Backint configuration file on each HANA host
C. An instance profile role scoped to the backup bucket and prefix, plus the KMS key used for encryption
D. Make the backup bucket public-read, so that restores can run from any host without credentials

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Backint uses the EC2 instance profile, so the role should allow only the S3 actions needed on the specific bucket and prefix and the KMS actions on the key that encrypts the backups. AdministratorAccess breaks least privilege. Long-lived access keys on disk are a leak risk when a role is available. A public bucket exposes database backups.
</details>

---

### Question 29
**Scenario:** SAP Fiori must be reachable by employees on the internet, while SAP application servers stay in private subnets.

A. Put the application servers in public subnets with Elastic IPs and restrict their security groups by country
B. An internet-facing ALB with AWS WAF in public subnets, forwarding to SAP Web Dispatcher in private subnets
C. Open the SAP ports on the HANA instance, since Fiori is served directly by the database
D. Use a gateway VPC endpoint, which publishes the Fiori service to the internet through AWS

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A public ALB with WAF terminates internet traffic in public subnets and forwards it to SAP Web Dispatcher and the application servers in private subnets, keeping SAP hosts unexposed. Public application servers widen the attack surface. Fiori is served by the application layer, not the database. Gateway endpoints give private access to S3 and DynamoDB and publish nothing.
</details>

---

### Question 30
**Scenario:** An architect is sizing SAP application servers on EC2 for a target throughput expressed in SAPS.

A. Pick instances by vCPU count alone, since every EC2 instance family delivers the same SAPS per vCPU
B. Pick the instance with the most memory, since SAPS ratings are calculated from the memory size
C. Use the SAPS benchmark ratings for certified EC2 instance types published in SAP Note 1656099
D. Run the SAP application on Lambda, which scales SAPS automatically with the request volume

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** SAP Note 1656099 lists the EC2 instance types supported for SAP on AWS along with their SAPS benchmark ratings, which is the basis for application server sizing. SAPS per vCPU varies by processor generation and family. SAPS measures throughput, not memory. SAP application servers do not run on Lambda.
</details>

---

## Where to go deeper

- [PAS-C01 cert page](../../exams/aws/specialty/sap-on-aws-pas-c01/) - notes, practice plan, strategy
- [Solutions Architect Professional practice questions](./aws-solutions-architect-professional.md) - the architecture exam alongside this
- [On-premises to AWS migration guide](../migration-guides/on-prem-to-aws.md) - lift-and-shift and replatform patterns
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - official exam guides
