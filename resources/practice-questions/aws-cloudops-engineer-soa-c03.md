---
last-updated: 2026-10-22
difficulty: intermediate
---

# AWS Certified CloudOps Engineer - Associate (SOA-C03) - Practice Questions

30 questions for SOA-C03 prep. The exam guide (version 1.1, June 2026) has five domains: monitoring, logging, analysis, remediation, and performance optimization (22%); reliability and business continuity (22%); deployment, provisioning, and automation (22%); security and compliance (16%); and networking and content delivery (18%). There is no separate cost domain: performance tuning sits in Domain 1 and network cost in Domain 5.

SOA-C03 is the successor to SOA-C02 (SysOps Administrator).

> **Cert page:** [exams/aws/associate/cloudops-engineer-soa-c03/](../../exams/aws/associate/cloudops-engineer-soa-c03/)

---

### Question 1
**Scenario:** An EC2 instance's memory utilization must appear in CloudWatch.

A. Install and configure the CloudWatch agent to publish memory and disk metrics
B. Enable detailed monitoring
C. It is available by default
D. Use VPC Flow Logs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The hypervisor cannot see inside the guest, so memory and disk-space metrics require the agent. Detailed monitoring only changes the EC2 metric interval from 5 minutes to 1 minute for the metrics that already exist. This distinction appears on the exam repeatedly.
</details>

---

### Question 2
**Scenario:** An Auto Scaling group must replace instances that fail an application health check, not just an EC2 status check.

A. Increase the cooldown to 600 seconds so instances have more time to pass the application's own checks before being replaced
B. Set the health check type to ELB with a target group that has an application-level health check
C. Use EC2 status checks only
D. Terminate manually

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** EC2 status checks only detect instance and system failures, so a hung application on a running instance stays in service. Switching the ASG health check type to ELB makes the load balancer's application health check the authority, with a health check grace period to allow for startup.
</details>

---

### Question 3
**Scenario:** CloudTrail must record management events across all regions and all accounts in an organization, in a tamper-evident way.

A. A per-account trail in the home region of each account, with management events delivered to a local bucket owned by the account
B. An organization trail, multi-region, to a central S3 bucket with log file validation
C. CloudWatch Logs only
D. Config rules

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An organization trail covers member accounts automatically, including new ones. Log file validation produces digest files that prove the log was not altered, and writing to a separate logging account with Object Lock protects against an attacker with admin in the source account.
</details>

---

### Question 4
**Scenario:** An alarm must fire when a metric is missing entirely, because the reporting instance may be gone.

A. Set the treat-missing-data behavior to breaching
B. Set it to notBreaching
C. Set it to ignore
D. Delete the alarm

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Missing data handling decides what "no data" means, and the safe choice for an availability alarm is breaching, so silence is treated as failure. `ignore` retains the previous state and `notBreaching` treats absence as healthy, which is exactly how outages go unnoticed.
</details>

---

### Question 5
**Scenario:** Patching must be applied to hundreds of EC2 instances on a schedule with compliance reporting.

A. SSH to each instance
B. Systems Manager Patch Manager with patch baselines, maintenance windows, and patch groups
C. Replace all instances every week by relaunching them from the same original AMI and instance type
D. A user data script that runs yum update on each instance when it boots, with results written to a local log file

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Patch Manager applies baselines during maintenance windows and reports compliance per instance, which is the auditable part. User data runs only at launch, and manual SSH does not scale or produce evidence.
</details>

---

### Question 6
**Scenario:** An RDS Multi-AZ deployment fails over. What is the effect on the application?

A. No connections are interrupted, because the standby takes over without any change to the client's session
B. The endpoint changes to the standby's own DNS name, so clients must be reconfigured with the new endpoint and redeployed
C. The endpoint stays the same and points to the standby; connections drop and reconnect
D. Data is lost, because the standby replicates asynchronously and always trails the primary by minutes

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Multi-AZ is for availability, using synchronous replication, and failover swaps the DNS target within roughly a minute or two. Existing connections break, so applications need connection retry logic. Read replicas are the scaling feature, and they are asynchronous.
</details>

---

### Question 7
**Scenario:** S3 objects must move to cheaper storage after 30 days and be deleted after 7 years, automatically.

A. S3 Lifecycle rules for transition and expiration
B. Manual review of the bucket each month by the storage team
C. A scheduled Lambda function that copies objects older than 30 days into a second bucket in the same storage class
D. S3 Versioning with a bucket policy that restricts old versions

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Lifecycle rules handle transitions between storage classes and expiration natively, with no code to run or maintain. If access patterns are unpredictable, S3 Intelligent-Tiering is the alternative that moves objects automatically based on observed access.
</details>

---

### Question 8
**Scenario:** A workload must run across three Availability Zones and survive the loss of one with no capacity reduction.

A. Run everything in one AZ
B. Use two AZs at 50% each, with an Auto Scaling group that adds capacity once an AZ has been lost
C. Rely on the region to move traffic to healthy zones automatically, with no sizing or scaling configuration
D. Provision capacity across three AZs sized so that any two AZs can carry the full load

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Surviving an AZ loss "with no capacity reduction" means N+1 sizing: with three AZs each carries a third but must be able to take half. Two AZs at 50% each means losing one halves capacity, which fails the requirement.
</details>

---

### Question 9
**Scenario:** An engineer needs to find which API call deleted a security group yesterday.

A. VPC Flow Logs
B. CloudWatch metrics
C. CloudTrail event history, filtered on the event name and resource
D. AWS Config alone

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** CloudTrail records who called which API, when, from where, and with what parameters. Config tells you the configuration changed and shows the before and after, which pairs well but does not name the caller as directly. Flow Logs record traffic, not control plane actions.
</details>

---

### Question 10
**Scenario:** EBS volumes must be backed up daily with 30-day retention across many accounts.

A. S3 replication
B. A cron job on each instance that calls the snapshot API with the instance's own role and prunes old snapshots
C. Manual snapshots taken by each account owner every morning and deleted by hand after thirty days
D. AWS Backup with a backup plan and rules, and resource assignment by tag

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** AWS Backup centralizes plans, retention, and cross-account and cross-region copies with a single audit view, and tag-based assignment means new resources are covered automatically. Data Lifecycle Manager is the EBS-only alternative for snapshot scheduling.
</details>

---

### Question 11
**Scenario:** An application in a private subnet needs outbound internet access for updates.

A. A NAT gateway in a public subnet, routed from the private route table
B. An internet gateway attached to the private subnet itself, with a route to it for 0.0.0.0/0 in its route table
C. A public IP address on each instance, plus a default route to the internet gateway
D. A VPC endpoint created for the public update servers that the instances must reach

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** NAT allows outbound-initiated traffic while blocking inbound, which is the definition of a private subnet with internet access. Assigning public IPs would make the instances directly reachable. VPC endpoints are the better answer when the destination is an AWS service, because they avoid NAT data processing charges entirely.
</details>

---

### Question 12
**Scenario:** Costs must be attributed to teams across a large account.

A. Trusted Advisor only, using its cost optimization checks to attribute each team's spend from the weekly summary
B. The bill total
C. Cost allocation tags activated in the billing console, with Cost Explorer grouping by tag
D. CloudWatch metrics

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Tags must be both applied to resources and activated as cost allocation tags before they appear in cost reports, and the activation step is the one people miss. Tag policies and enforcement through SCPs or Config rules keep coverage from decaying.
</details>

---

### Question 13
**Scenario:** A CloudFormation stack update fails partway through.

A. The stack must be recreated from scratch because a failed update leaves it in a state that cannot be repaired
B. All resources in the stack are deleted, including the ones created before the failure
C. It rolls back to the last good state by default; change sets preview updates
D. The stack is left in a broken state that only deleting the whole stack by hand can clear

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Automatic rollback on failure is the default, which is why declarative infrastructure is safer than scripts. Change sets show exactly what will be added, modified, or replaced before you apply, and replacement of a stateful resource is the surprise worth catching there.
</details>

---

### Question 14
**Scenario:** Application logs from EC2 must be searchable centrally with retention control.

A. Email the logs
B. Local log files only, rotated daily on each instance and then collected by hand whenever an investigation needs them
C. S3 with no index, queried by downloading the objects to a bastion host and searching them with grep each time
D. The CloudWatch agent shipping to CloudWatch Logs, with retention and Logs Insights for queries

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Log groups have configurable retention, which defaults to never expire and quietly accumulates cost. Logs Insights gives query capability without standing up a search cluster, and export to S3 covers cheap long-term archive.
</details>

---

### Question 15
**Scenario:** An EC2 instance in a public subnet cannot be reached on port 443, though the security group allows it.

A. Check the network ACL, which is stateless and needs rules in each direction, then the route table and host firewall
B. Recreate the instance from the same AMI in a different subnet and Availability Zone, then retest port 443 from the same client
C. Add a second security group
D. Change the instance type

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Security groups are stateful, so an allowed inbound flow returns automatically. NACLs are stateless, so a missing outbound rule for ephemeral ports blocks the response even though the request arrived. Route table, NACL, security group, host firewall is the checklist worth running in that order.
</details>

---

### Question 16
**Scenario:** An application writes lines containing `ERROR` to a CloudWatch Logs log group. The team wants an alarm when more than 20 errors occur in 5 minutes.

A. Run a CloudWatch Logs Insights query by hand every 5 minutes and page the on-call engineer if it returns more than 20 rows
B. Create a metric filter on the log group that counts `ERROR`, then a CloudWatch alarm on that metric
C. Export the log group to S3 every hour and scan the files with Athena
D. Enable detailed monitoring on the EC2 instances that write the logs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A metric filter turns matching log events into a CloudWatch metric, and an alarm on that metric fires when the count passes the threshold. Running Logs Insights by hand is not monitoring. Hourly exports to S3 are too slow for a 5-minute alarm. Detailed monitoring adds 1-minute EC2 metrics but knows nothing about log content.
</details>

---

### Question 17
**Scenario:** AWS Config flags any security group that allows SSH from `0.0.0.0/0`. The team wants such rules removed automatically when found.

A. Create a CloudTrail trail with data events turned on for every security group in the account
B. Raise a Service Quotas request to lower the maximum number of security group rules in the account
C. Email the account owner whenever the Config rule changes to noncompliant
D. Attach an automatic remediation to the Config rule that runs a Systems Manager Automation runbook

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Config rules support automatic remediation with Systems Manager Automation runbooks, such as one that removes the offending ingress rule, so the fix happens without a person. CloudTrail records API activity but does not fix anything. Quotas limit counts, not content. Email notification still relies on someone acting.
</details>

---

### Question 18
**Scenario:** An operations team suspects many EC2 instances and Lambda functions are over-provisioned and wants recommendations based on actual utilization history.

A. Turn on AWS Compute Optimizer and review its rightsizing recommendations
B. Use AWS Trusted Advisor's service limits check to see which instances are near their quotas
C. Read the EC2 instance type pricing page and choose the cheapest type for each workload
D. Use AWS Artifact

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Compute Optimizer analyzes CloudWatch utilization history and recommends better-sized instance types, Lambda memory settings and more. The service limits check reports quota usage, not over-provisioning. Picking the cheapest type ignores whether the workload fits. AWS Artifact provides compliance reports and agreements, not performance recommendations.
</details>

---

### Question 19
**Scenario:** A gp2 EBS volume of 200 GiB is hitting its IOPS limit. The team needs 6,000 IOPS without paying for more storage they do not need.

A. Take a snapshot and restore it to a gp2 volume in another Availability Zone, which resets the burst balance
B. Increase the gp2 volume to 2,000 GiB so its baseline IOPS reaches 6,000
C. Modify the volume to gp3 and set provisioned IOPS to 6,000
D. Attach a second volume

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** gp3 decouples IOPS and throughput from size, so the volume can stay at 200 GiB with 6,000 IOPS set directly, and Elastic Volumes makes the change online. Restoring to another zone does not raise the baseline. Growing gp2 to 2,000 GiB reaches 6,000 IOPS but pays for storage the team does not need. A second volume needs striping or app changes and is not the simple fix.
</details>

---

### Question 20
**Scenario:** A website runs in one Region with a static maintenance page in an S3 bucket. If the main site's health check fails, DNS should send users to the maintenance page.

A. Use Route 53 weighted routing with 50 percent of traffic sent to each target
B. Use Route 53 failover routing with a health check on the primary record
C. Use Route 53 geolocation routing, which sends users to the maintenance page when the primary is down
D. Use a CloudFront cache behavior

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Failover routing returns the primary record while its health check passes and the secondary record when it fails, which is the requirement. Weighted routing splits traffic all the time, including when the site is healthy. Geolocation routes by user location, not health. A cache behavior controls caching per path and does not perform DNS failover.
</details>

---

### Question 21
**Scenario:** A DynamoDB table must be recoverable to any second in the last 35 days after an accidental bulk delete.

A. Enable DynamoDB Streams and replay the deleted items from the stream
B. Turn on auto scaling for the table's read and write capacity
C. Create a global table replica in a second Region and restore from the replica
D. Enable point-in-time recovery on the table

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Point-in-time recovery keeps continuous backups and restores the table to any second in the retention window, up to 35 days, into a new table. Streams keep changes for only 24 hours and need custom replay code. Auto scaling handles throughput, not recovery. A global table replicates the delete too, so the replica loses the same data.
</details>

---

### Question 22
**Scenario:** An RDS for MySQL primary is overloaded by reporting queries, while write traffic is modest. The team wants to offload reads without changing the write path.

A. Convert it to a Multi-AZ DB instance deployment, which makes the standby available for read queries
B. Create one or more read replicas and point the reporting queries at them
C. Increase the backup retention period to 35 days so that reports read from snapshots
D. Move the database to a larger Region

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Read replicas copy data asynchronously and serve read-only queries, taking reporting load off the primary while writes stay unchanged. The standby in a Multi-AZ DB instance deployment does not serve reads; it exists for failover. Backup retention affects recovery, not query load. Regions are not sized, and moving does not split reads from writes.
</details>

---

### Question 23
**Scenario:** A baseline CloudFormation template with IAM roles and a Config recorder must be deployed to every account in an AWS Organizations OU and to new accounts automatically.

A. Use CloudFormation StackSets with service-managed permissions and automatic deployment to the OU
B. Run `aws cloudformation deploy` from a laptop in each account after it is created
C. Copy the template into each account's S3 bucket and let each account team deploy it
D. Use a single stack in the management account

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** StackSets with service-managed permissions deploy a stack to every account in target OUs and Regions, and automatic deployment covers accounts added later. Running deploys by hand does not scale and misses new accounts. Leaving it to each team gives no consistency. A stack in the management account creates resources only in that account.
</details>

---

### Question 24
**Scenario:** Someone may have changed resources in a CloudFormation stack through the console. The team wants to see which resources no longer match the template.

A. Delete and recreate the stack, then compare the old and new resources by hand
B. Run a change set with the same template, which lists all manual changes made in the console
C. Run drift detection on the stack and review the drift results
D. Enable termination protection on the stack

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Drift detection compares the stack's resources with their expected template configuration and reports which ones were modified or deleted, and how. Deleting and recreating is destructive and loses the evidence. A change set compares a new template with the stack's recorded state, not with the live resources. Termination protection prevents stack deletion and reports nothing.
</details>

---

### Question 25
**Scenario:** Every month the team must produce a patched, hardened AMI with the company's agents installed, test it, and share it with other accounts.

A. Take a snapshot of a running production instance every month and share the snapshot
B. Patch each running instance in place and never build new AMIs at all
C. Install the agents with user data at boot and launch the stock AWS AMI each time
D. Build an EC2 Image Builder pipeline with build and test components and distribution settings

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** EC2 Image Builder automates building, hardening, testing and distributing AMIs on a schedule, including to other accounts and Regions. A snapshot of production captures drift and any temporary data. Patching in place does not produce a tested golden image. User data repeats setup at every boot, slowing launches and never producing a tested artifact.
</details>

---

### Question 26
**Scenario:** A security review requires that an S3 bucket reject any request not sent over HTTPS.

A. Enable default encryption with SSE-S3 on the bucket so that all requests are encrypted
B. Add a bucket policy that denies all actions when `aws:SecureTransport` is false
C. Turn on S3 Versioning for the bucket
D. Enable S3 Transfer Acceleration, which only accepts HTTPS connections from clients

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A bucket policy denying requests where `aws:SecureTransport` is false rejects plain HTTP access. Default encryption protects objects at rest, not requests in transit. Versioning keeps object versions and has nothing to do with transport. Transfer Acceleration speeds uploads through edge locations and does not block HTTP on the normal endpoint.
</details>

---

### Question 27
**Scenario:** A compliance standard requires that the key material of a customer managed KMS key be rotated every year with no application changes.

A. Enable automatic key rotation on the customer managed key
B. Create a new key every year and update every application to use the new key ARN
C. Rotate the IAM access keys of the users who call KMS
D. Delete the key every year

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Automatic rotation creates new key material on a schedule, a year by default, while the key ID and ARN stay the same, so applications need no changes and old data still decrypts. Creating new keys by hand forces application changes. IAM access keys are credentials, not KMS key material. Deleting a key makes everything encrypted with it unreadable.
</details>

---

### Question 28
**Scenario:** An instance cannot receive traffic on port 8080 from another subnet. The team wants to know whether packets reach the ENI and are being rejected.

A. Use CloudTrail to look up the `RejectConnection` events for the instance's ENI
B. Run Trusted Advisor's security checks on the instance's VPC
C. Enable VPC Flow Logs on the subnet or ENI and look for REJECT records on port 8080
D. Check the Personal Health Dashboard for the instance

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** VPC Flow Logs record accepted and rejected traffic at the ENI level, so REJECT records on port 8080 show that a security group or network ACL is blocking it. CloudTrail logs API calls, not packets, and there is no such event. Trusted Advisor flags risky open ports, not rejected flows. The Health Dashboard reports AWS-side events, not your filtering rules.
</details>

---

### Question 29
**Scenario:** A static site is served from an S3 bucket through CloudFront. The bucket must not be readable directly, only through CloudFront.

A. Make the bucket public and rely on CloudFront caching so users rarely reach the bucket
B. Enable S3 static website hosting and restrict access with a Referer header check
C. Put the bucket in a private subnet
D. Use origin access control on the distribution and a bucket policy allowing only that distribution

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Origin access control lets CloudFront sign requests to S3, and a bucket policy granting access only to that distribution keeps Block Public Access on and direct reads denied. A public bucket can be read directly by anyone. Referer headers are easy to forge. S3 buckets are not placed in subnets.
</details>

---

### Question 30
**Scenario:** On-premises servers connected over Direct Connect must resolve names in a Route 53 private hosted zone associated with a VPC.

A. Make the private hosted zone public so on-premises DNS servers can query it over the internet
B. Create a Route 53 Resolver inbound endpoint and forward the zone's queries to it from on-premises DNS
C. Create a Resolver outbound endpoint with a forwarding rule to the on-premises DNS servers
D. Add the records to every on-premises server's hosts file

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An inbound endpoint gives the VPC resolver IP addresses that on-premises DNS can forward queries to, which lets them resolve private hosted zone names. Making the zone public exposes internal names. Outbound endpoints are for the reverse direction, VPC to on-premises. Hosts files do not scale and go stale.
</details>

---

## Where to go deeper

- [SOA-C03 cert page](../../exams/aws/associate/cloudops-engineer-soa-c03/) - notes, practice plan, strategy
- [SOA-C02 practice questions](./aws-sysops-administrator.md) - the predecessor exam's bank
- [Solutions Architect Associate practice questions](./aws-solutions-architect-associate.md) - the design counterpart
- [Observability basics](../../learn/concepts/observability-basics.md) - the monitoring domain in plain English
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - official exam guides
