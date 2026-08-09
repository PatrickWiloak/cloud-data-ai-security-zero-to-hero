---
last-updated: 2026-08-09
difficulty: advanced
---

# AWS Certified SAP on AWS - Specialty (PAS-C01) - Practice Questions

15 questions for PAS-C01 prep, weighted toward designing (30%) and implementing (30%) SAP workloads on AWS, then managing and operating (24%) and securing (16%).

PAS-C01 has been retired by AWS. The architectural content remains applicable to running SAP on AWS; confirm exam availability before planning to sit it.

> **Cert page:** [exams/aws/specialty/sap-on-aws-pas-c01/](../../exams/aws/specialty/sap-on-aws-pas-c01/)

---

### Question 1
**Scenario:** An SAP HANA production database must run on AWS with vendor support.

A. Any EC2 instance type
B. An SAP-certified instance type from the certified list, meeting the required CPU-to-memory ratio and storage KPIs
C. A container
D. Lambda

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SAP only supports HANA on certified configurations, so the instance family, size, and storage layout all come from the certification list rather than from general sizing intuition. Running on an uncertified type puts you outside support, which is usually a contractual problem before it is a technical one.
</details>

---

### Question 2
**Scenario:** HANA data and log volumes must meet SAP's storage KPIs.

A. gp2 volumes sized by capacity
B. io2 or gp3 volumes provisioned to meet the throughput and latency KPIs, with separate volumes for data, log, and shared
C. Instance store only
D. EFS for everything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** HANA's log writes are latency-sensitive and its data volume is throughput-sensitive, so the volumes are sized against IOPS and MB/s targets rather than capacity alone. Separating data, log, and shared volumes is part of the certified layout, and HCMT is the tool that validates it.
</details>

---

### Question 3
**Scenario:** SAP application servers must fail over across Availability Zones with minimal downtime.

A. A single instance with backups
B. An HA cluster (for example SUSE or Red Hat pacemaker) across two AZs with an overlay IP and a shared file system
C. Manual restart
D. Auto Scaling of the ASCS

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The ASCS and ERS instances are the single points of failure, so they run in a cluster with an overlay IP routed by a route table update on failover. Auto Scaling does not apply because these are stateful, licensed singleton components rather than interchangeable replicas.
</details>

---

### Question 4
**Scenario:** A shared file system is needed for `/sapmnt` across application servers.

A. Amazon EFS or Amazon FSx for NetApp ONTAP, mounted across AZs
B. EBS attached to one instance
C. S3 mounted as a filesystem
D. Local disk

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `/sapmnt` and the transport directory need concurrent POSIX access from many hosts, which EFS and FSx provide across AZs. EBS is single-attach for this purpose, and S3 is object storage without the file semantics SAP expects.
</details>

---

### Question 5
**Scenario:** A migration from on-premises SAP ECC to AWS must minimize downtime for a 20 TB database.

A. Offline export and import
B. A near-zero-downtime approach: database replication or backup and restore with log shipping, cut over during a short window
C. Copy the VM image
D. Rebuild and re-enter data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Keeping the source running while the target catches up through replication is what compresses the downtime window from days to hours. Classic heterogeneous migration with export and import is still used when a platform change is required, and the parallel export and import options are what make it tolerable.
</details>

---

### Question 6
**Scenario:** HANA must be protected against an AZ failure with an RPO near zero.

A. Backups to S3 only
B. HANA System Replication in synchronous mode to a secondary in another AZ
C. Asynchronous replication to another region only
D. EBS snapshots hourly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Synchronous HSR acknowledges commits only after the secondary has the log, so RPO is effectively zero at the cost of some commit latency across AZs. Asynchronous replication to a distant region is the DR tier, where a larger RPO is accepted in exchange for distance.
</details>

---

### Question 7
**Scenario:** SAP backups must be stored durably and restorable quickly.

A. Backint-integrated backup to S3, with lifecycle rules for older backups
B. Backups to local EBS only
C. Tape
D. No backups, replication is enough

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** AWS Backint for SAP HANA writes backups directly to S3 from the database's own backup interface, so it is integrated with HANA Studio and Cockpit rather than bolted on. Replication is not a backup: it faithfully replicates a logical corruption or a bad transport.
</details>

---

### Question 8
**Scenario:** Non-production SAP systems must reduce cost outside business hours.

A. Terminate them
B. Schedule stop and start of the instances (for example with Systems Manager or the AWS instance scheduler), keeping EBS volumes
C. Reduce the database size
D. Use spot instances

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Stopping instances stops compute charges while EBS persists, which suits development and QA systems used only in working hours. Spot is not appropriate for SAP because an interruption to a stateful, licensed system is disruptive and slow to recover.
</details>

---

### Question 9
**Scenario:** Which service provides SAP-aware operational visibility on AWS?

A. AWS Systems Manager for SAP, with AWS Launch Wizard for deployment
B. CloudFront
C. Amazon Inspector
D. AWS Glue

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Launch Wizard deploys certified SAP architectures with the right instance and storage layout, and Systems Manager for SAP provides discovery, backup integration, and operational actions that understand SAP components rather than just EC2 instances.
</details>

---

### Question 10
**Scenario:** Network latency between application servers and HANA must be minimized.

A. Spread them across regions
B. Place them in the same AZ, and use a cluster placement group where the instance types support it
C. Use a NAT gateway
D. Route through Transit Gateway

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SAP application-to-database traffic is chatty and latency-sensitive, so same-AZ placement is the standard design, with HA achieved by a second AZ pair rather than by splitting a single system. Cross-region separation of app and database is not a supported design.
</details>

---

### Question 11
**Scenario:** SAP systems must be reachable from the corporate network only.

A. Public subnets with security groups
B. Private subnets, reached over Direct Connect or VPN, with no internet-facing endpoints for SAP components
C. An internet-facing load balancer
D. Public IPs with an allowlist

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SAP systems are internal business applications, so the default is no direct internet exposure at all. Where external access is genuinely required, such as Fiori for remote users, it is fronted by a reverse proxy or Web Dispatcher in a DMZ subnet with WAF, rather than exposing the application servers.
</details>

---

### Question 12
**Scenario:** SAP data must be encrypted at rest with organizational key control.

A. EBS and S3 encryption with KMS customer managed keys, plus HANA data volume encryption
B. No encryption needed on a private network
C. Application-level only
D. Encrypt backups only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Layered encryption is the norm: the storage layer covers volumes and backups, and HANA's own data and log volume encryption covers the database files independently. A customer managed key gives you revocation and audit through CloudTrail, which is usually the actual compliance requirement.
</details>

---

### Question 13
**Scenario:** Right-sizing an SAP landscape after migration.

A. Keep on-premises sizing permanently
B. Use SAP sizing outputs (SAPS requirements) plus observed CloudWatch and HANA metrics to resize, then consider Savings Plans or Reserved Instances for the steady state
C. Always use the largest instance
D. Guess

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** On-premises sizing usually embeds years of growth headroom bought up front, which is exactly the cost the cloud lets you release. Resize based on measured utilization first, then commit to the resulting steady state to capture the discount.
</details>

---

### Question 14
**Scenario:** A DR region must be maintained cost-effectively for SAP.

A. A full-size duplicate landscape running permanently
B. Pilot light: replicate data continuously, keep minimal resources running, and scale up on failover using automation
C. Backups only, with rebuild from scratch
D. No DR

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Pilot light matches most SAP DR requirements: HANA System Replication keeps the data current while the application tier stays small or stopped until needed. The critical part is that the scale-up is automated and rehearsed, otherwise the RTO is fictional.
</details>

---

### Question 15
**Scenario:** SAP licensing and support obligations on AWS.

A. AWS provides SAP licenses
B. You bring your own SAP licenses; AWS provides the certified infrastructure, and support is shared between SAP, AWS, and the operating system vendor
C. No licenses are required in the cloud
D. Licenses are per-region

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SAP licensing is a contract with SAP regardless of where it runs. What AWS provides is certified infrastructure and its own support; SAP supports the application, and the OS vendor supports the cluster stack. Knowing which vendor owns which problem is what makes an incident tractable.
</details>

---

## Where to go deeper

- [PAS-C01 cert page](../../exams/aws/specialty/sap-on-aws-pas-c01/) - notes, practice plan, strategy
- [Solutions Architect Professional practice questions](./aws-solutions-architect-professional.md) - the architecture exam alongside this
- [On-premises to AWS migration guide](../migration-guides/on-prem-to-aws.md) - lift-and-shift and replatform patterns
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - official exam guides
