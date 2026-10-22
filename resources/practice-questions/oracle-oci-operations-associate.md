---
last-updated: 2026-10-22
difficulty: intermediate
---

# Oracle Cloud Infrastructure Operations Associate (1Z0-1067) - Practice Questions

30 questions for OCI Operations Associate prep, weighted toward observability and management (20%), then compute, storage, network, and security operations (15% each).

> **Cert page:** [exams/oracle/oci-operations-associate/](../../exams/oracle/oci-operations-associate/)

---

### Question 1
**Scenario:** An alarm must notify a team and trigger an automated response.

A. A Monitoring alarm publishing to a Notifications topic, with email and function subscriptions
B. An on-call engineer checking the Monitoring console dashboards every hour and running the fix by hand when a metric looks high
C. An alarm that sends email only, so the recipient can start any remediation script later from their own laptop
D. A saved Logging log query that the team re-runs each morning to look for the condition

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Notifications topics fan out to multiple subscription types, so one alarm can both inform a human and invoke automation. Using a function subscription is how you build auto-remediation for well-understood conditions.
</details>

---

### Question 2
**Scenario:** Logs from many services and instances must be searched centrally.

A. Log in to each host over SSH and run grep against the local log files, repeating for every instance in the compartment
B. Take screenshots of each service's console log viewer and attach them to the incident ticket for later comparison
C. Leave logs in local files on each instance and rely on operating system log rotation to keep a recent history
D. The Logging service with log groups, plus the agent configuration for custom logs, and Logging Analytics for parsing and correlation

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Service logs, audit logs, and custom logs all land in the Logging service, and Logging Analytics adds parsing and dashboards on top. Central collection matters most during an incident, when logging into hosts is slowest.
</details>

---

### Question 3
**Scenario:** Patching must be applied to many instances on a schedule with reporting.

A. Recreate instances by hand every week from a fresh image, with no record of which instances received which patches
B. Ignore patches until a vulnerability is announced, because Oracle patches guest operating systems automatically
C. OS Management Hub with managed instance groups and scheduled jobs
D. SSH to each instance in turn and run the package manager update during a maintenance window

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Managed groups let one job cover many instances and produce the compliance evidence an auditor asks for. Manual patching neither scales nor leaves a record, which is usually the more expensive gap.
</details>

---

### Question 4
**Scenario:** A block volume must be backed up automatically with retention.

A. Manual snapshots taken from the console whenever an administrator remembers, with no retention schedule applied
B. Copy the files from the mounted volume to another directory on the same instance each night using a cron job
C. A backup policy (bronze, silver, gold, or custom) assigned to the volume, with cross-region copy for DR
D. No backup, because block volumes are replicated three times inside the availability domain and that protects against deletion

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Policy-based backups run on a schedule with defined retention and can copy to another region. Volume groups let you snapshot several volumes at a consistent point, which matters when an application spans volumes.
</details>

---

### Question 5
**Scenario:** An instance must move to a larger shape with minimal disruption.

A. Attach more block volumes to the instance, which adds CPU and memory
B. It cannot be changed, because the shape is fixed at launch
C. Stop the instance, change the shape (or edit a flexible shape's OCPU and memory), and start it
D. Rebuild it by terminating the instance and launching a new one, then reconfiguring the application and IP addresses

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Shape changes require a stop and start on virtual machines, and flexible shapes let you adjust OCPUs and memory independently within the family. Knowing that this is a reboot rather than a rebuild changes how the maintenance window is planned.
</details>

---

### Question 6
**Scenario:** Instance maintenance is announced by Oracle.

A. Read the maintenance notification, then plan a reboot within the window or reboot proactively at a convenient time
B. Delete the instance and launch a replacement from a custom image before the maintenance window begins, whatever the notice says
C. Open a support ticket asking Oracle to cancel the maintenance event permanently, since customers can opt out of host maintenance
D. Ignore it, because every instance is live migrated automatically

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Many instances live migrate transparently, but some, including those with local NVMe or certain shapes, require a reboot. Acting early inside the window means the disruption happens when you choose rather than when the deadline arrives.
</details>

---

### Question 7
**Scenario:** Network connectivity between two instances fails intermittently.

A. Increase the shape of each instance to one with more network bandwidth, since intermittent drops always mean a saturated VNIC
B. Check security lists, NSGs, and route tables, then use Network Path Analyzer and VNIC metrics to localize the problem
C. Recreate the instances in a different subnet, then repeat until the problem stops reproducing in testing
D. Reboot everything, including the instances and the gateways, so that stale connection tracking tables and caches are cleared first

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Configuration first, then measurement: path analysis evaluates the rules and routes for a specific source and destination, which distinguishes a policy problem from a genuine network issue. Rebooting hides intermittent problems without explaining them.
</details>

---

### Question 8
**Scenario:** Cloud Guard reports a problem for a publicly accessible bucket.

A. Delete the bucket immediately, along with its stored objects, since any public bucket is a confirmed data breach
B. Disable Cloud Guard in the compartment so the detector stops raising problems about intended public buckets
C. Dismiss the problem as resolved, because Cloud Guard findings for Object Storage are informational and need no follow-up
D. Investigate whether public access is intended; if not, remove it and add a Security Zone

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Fixing the instance is half the job; preventing the next one is the other half. Security Zones refuse the operation outright, which converts a recurring detection into a configuration that cannot happen in that compartment.
</details>

---

### Question 9
**Scenario:** Costs are rising and the cause is unclear.

A. Use Cost Analysis grouped by compartment, service, and tag, act on the biggest contributors, and set budgets with alerts
B. Estimate the spend from last month's invoice and email the team to cut the least important usage
C. Cancel the account and recreate the workloads in a new tenancy so billing history restarts
D. Reduce all resources by 20 percent across every compartment, then check whether the bill stops rising at the next invoice cycle

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Attribution before action: cost is usually concentrated in a few resources, and cutting broadly hurts things that were not the problem. Budgets with forecast alerts then give warning before the next surprise.
</details>

---

### Question 10
**Scenario:** An audit asks who terminated an instance last week.

A. Nobody can tell, because terminated instances remove their own records and the tenancy keeps no history of API calls
B. The Audit service, which records API calls with the principal, action, and time
C. Monitoring metrics, which show a drop to zero when the instance is terminated and also name the user who did it
D. Instance logs collected by the Logging agent, which keep the termination command in the shell history

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Audit records control plane API activity across the tenancy and is enabled by default with a retention period. Instance logs disappear with the instance, which is exactly the case here.
</details>

---

### Question 11
**Scenario:** Object Storage costs are growing from data nobody reads.

A. Compress only the largest objects with gzip before upload, leaving the stored data in the Standard tier indefinitely and untouched
B. Delete everything older than a week, including objects regulators require to be kept for years
C. Lifecycle policy rules that move objects to infrequent access and archive, and delete them where retention allows
D. Move the data to block storage volumes, which cost less per gigabyte than any Object Storage tier

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Tiering matches storage cost to access frequency automatically. Archive is much cheaper but requires a restore before reading, so apply it to data whose retention is a compliance obligation rather than an operational need.
</details>

---

### Question 12
**Scenario:** An OKE cluster's nodes must be updated to a new Kubernetes version.

A. Upgrade the worker nodes first, then the control plane afterwards, since the nodes must lead the upgrade order
B. Update the nodes in place with no drain, letting the running pods be terminated as each node restarts
C. Update only the control plane and leave the worker nodes on the old version, since nodes upgrade themselves later
D. Add a new node pool on the target version, cordon and drain the old nodes to migrate workloads, then remove the old pool

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Control plane first, then nodes, is the required order. The blue-green node pool approach keeps workloads running and makes rollback a matter of draining back, whereas in-place node updates leave less room to retreat.
</details>

---

### Question 13
**Scenario:** Operational tasks must be automated without maintaining servers.

A. A spreadsheet of tasks that an operator reviews each morning and runs by hand
B. Resource Scheduler or Events triggering Functions, with Resource Manager for infrastructure changes
C. A cron job on a VM that the team patches and monitors, which also needs a server maintained to run the automation
D. Manual runbooks followed by the on-call engineer whenever an alert arrives, with the steps recorded in a wiki

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Event-driven automation responds to the actual condition, and scheduled automation handles the predictable work such as stopping non-production instances overnight. Both remove the person who might forget.
</details>

---

### Question 14
**Scenario:** A database's performance has degraded.

A. Use Database Management and Performance Hub to find the top SQL and wait events, then address the query or index before changing capacity
B. Add storage to the database system immediately, since slow queries are almost always caused by running out of space
C. Resize the compute shape to the next size up straight away, then check whether the same queries still run slowly
D. Restart the database during business hours to clear its caches and reset the execution plans for every session

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Diagnosis first: most degradation traces to a plan change or a missing index rather than genuine capacity exhaustion. Scaling first works, expensively and permanently, on a problem an index would have fixed.
</details>

---

### Question 15
**Scenario:** Access reviews must confirm who can do what in a compartment.

A. Check the console visually by opening each resource page
B. Review IAM policies and group memberships for the compartment, and use Audit to see what was actually used
C. Assume it is correct because policies were reviewed when the compartment was created and have not changed since then
D. Ask people in each team which resources they believe they can reach

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Policy review shows what is permitted; audit data shows what was used. The gap between the two is where you find permissions nobody needs, which is the most productive place to apply least privilege.
</details>

---

### Question 16
**Scenario:** An instance is moved from the Dev compartment to the Prod compartment. The Dev team can still see it in the Console a minute later, but can no longer stop it.

A. The move failed and must be retried by the tenancy administrator
B. The policies of the new compartment now govern access to the instance
C. The instance kept its Dev policies until its next reboot
D. Moving instances is not supported, so the Console view is stale

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Access in OCI follows the compartment a resource is in, so after a move the policies written for the destination compartment apply immediately and the source compartment's policies no longer do. The behavior shows the move worked. Policies are not tied to reboots, and instances can be moved between compartments.

**Key Concept:** [Managing Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/managingcompartments.htm)
</details>

---

### Question 17
**Scenario:** After an edit to `/etc/fstab`, a Linux instance hangs during boot. SSH is unreachable and the team needs to get to the boot console to repair the file.

A. Reboot the instance again from the Console and wait for SSH to recover
B. Attach a new VNIC to the instance in a public subnet
C. Change the instance shape to one with more memory
D. Create an instance console connection and use the serial console

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** An instance console connection provides serial console access that works even when networking and SSH are down, so you can boot into maintenance mode and fix `/etc/fstab`. Rebooting repeats the same failure. A new VNIC does not help an OS that never finishes booting, and more memory does not fix a bad mount entry.

**Key Concept:** [Instance Console Connections](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm)
</details>

---

### Question 18
**Scenario:** A fully configured application server in Ashburn must be reproduced as new instances in Frankfurt, using the same OS configuration.

A. Create a custom image, export it to Object Storage, and import it in Frankfurt
B. Take a boot volume backup and attach it to a Frankfurt instance directly
C. Clone the instance's VNIC into a Frankfurt subnet
D. Copy the instance's OCID into the Frankfurt launch form

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A custom image captures the boot volume's configuration and can be exported to Object Storage and imported in another region (images can also be copied between regions directly). A backup must first be copied cross-region and restored before it can boot anything. VNICs carry network identity, not the OS, and an OCID cannot be used to clone an instance.

**Key Concept:** [Image Import/Export](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/imageimportexport.htm)
</details>

---

### Question 19
**Scenario:** An alarm must fire when the one-minute average CPU utilization of an instance is above 80%.

A. `CpuUtilization > 80`
B. `CpuUtilization[80].mean() > 1m`
C. `CpuUtilization[1m].mean() > 80`
D. `CpuUtilization[1m].count() > 80`

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** An MQL expression names the metric, gives the aggregation interval in brackets, applies a statistic, and compares it with a threshold, so `[1m].mean() > 80` matches the requirement. The bare metric with no interval or statistic is incomplete. Swapping the interval and threshold is invalid, and `count()` counts data points rather than measuring CPU.

**Key Concept:** [Monitoring Query Language (MQL) Reference](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm)
</details>

---

### Question 20
**Scenario:** The operations team needs an alarm on an application's internal job backlog, a number only the application knows.

A. Publish the backlog as a custom metric with the PostMetricData API
B. Write the backlog to the instance's syslog and alarm on disk usage
C. Use the built-in CpuUtilization metric as a stand-in for backlog
D. Ask Oracle Support to add a new service metric for the application

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Applications can publish their own metrics to the Monitoring service in a custom namespace with PostMetricData, and alarms work on custom metrics the same way as on service metrics. Disk usage and CPU are indirect signals that do not track the backlog. Oracle does not add service metrics for customer applications.

**Key Concept:** [Publishing Custom Metrics](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm)
</details>

---

### Question 21
**Scenario:** A planned two-hour maintenance window will trip several CPU and health alarms. The team wants no pages during the window but the alarms active again afterward.

A. Delete the alarms and recreate them after the window ends
B. Unsubscribe the on-call team from the Notifications topic
C. Raise every alarm threshold to 100% for the day
D. Suppress the alarms for the window's start and end time

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Alarm suppression stops notifications for a defined time range and lifts automatically when it ends, with no configuration to restore. Deleting and recreating alarms risks mistakes and loses history. Unsubscribing the team silences every alarm on the topic, and raising thresholds needs manual reversal and can hide genuine problems.

**Key Concept:** [Monitoring Overview](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm)
</details>

---

### Question 22
**Scenario:** An application writes logs to `/var/log/app/*.log` on twenty instances. These must appear in the OCI Logging service for search and retention.

A. Enable service logs on the subnet that hosts the instances
B. Create a custom log with an agent configuration for the log paths
C. Turn on VCN flow logs for the instances' VNICs
D. Mount an Object Storage bucket at `/var/log/app` on each host

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Custom logs collect application log files through the Oracle Cloud Agent's Custom Logs Monitoring plugin, using an agent configuration that names the paths and a dynamic group of instances. Service logs and flow logs record OCI service activity and network traffic, not application files. Mounting a bucket is not a supported way to ingest logs into Logging.

**Key Concept:** [Custom Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/custom_logs.htm)
</details>

---

### Question 23
**Scenario:** Operations collects large volumes of logs from OCI and on-premises systems and wants machine-learning-based clustering, pattern detection, and dashboards across them.

A. The Audit service with a longer retention period
B. VCN flow logs exported to a bucket
C. Oracle Logging Analytics
D. The Notifications service with filters

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Logging Analytics ingests logs from OCI and other sources, parses them, and provides clustering, anomaly and pattern detection, and dashboards. Audit records only API calls. Flow logs in a bucket are raw network records with no analysis, and Notifications delivers messages without analyzing anything.

**Key Concept:** [Oracle Logging Analytics](https://docs.oracle.com/en-us/iaas/logging-analytics/index.html)
</details>

---

### Question 24
**Scenario:** Block volume backups exist only in the primary region. The DR plan requires restorable copies in a second region.

A. Increase the backup policy's retention period
B. Enable a reserved public IP on each volume
C. Move the backups to a different compartment
D. Copy the volume backups to the DR region

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Block volume backups can be copied to another region (manually or through a backup policy's cross-region copy), where they can be restored if the primary region is lost. Longer retention keeps more copies in the same region. Compartments organize access, not location, and a public IP has nothing to do with backups.

**Key Concept:** [Copying a Volume Backup Between Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingvolumebackupcrossregion.htm)
</details>

---

### Question 25
**Scenario:** Users of a File Storage file system often delete files by mistake and need a quick way to recover yesterday's version themselves.

A. Restore the whole file system from a block volume backup
B. Take scheduled snapshots and let users copy files from `.snapshot`
C. Enable Object Storage versioning on the mount target
D. Run `fsck` on the mount point after each deletion

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** File Storage snapshots are point-in-time, read-only copies exposed in the hidden `.snapshot` directory, so users can copy back a single file without an admin restore. File systems are not backed up as block volumes. Versioning is an Object Storage bucket feature, and `fsck` checks file system consistency but does not recover deleted files.

**Key Concept:** [Managing Snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingsnapshots.htm)
</details>

---

### Question 26
**Scenario:** Infrastructure is deployed from a Resource Manager stack. The team suspects someone changed security rules by hand in the Console.

A. Run a fresh apply job and compare the job logs line by line
B. Delete the stack and recreate it from the Terraform files
C. Run a drift detection report on the stack
D. Search the Logging service for the stack's name

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Drift detection compares the actual state of the stack's resources with the last executed configuration and reports what changed, per resource. An apply job would overwrite the manual changes without explaining them first. Deleting the stack destroys its resources, and searching logs by stack name does not report configuration differences.

**Key Concept:** [Overview of Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm)
</details>

---

### Question 27
**Scenario:** A scheduled OCI CLI script runs on an admin instance in OCI. Security forbids storing API keys or config files with credentials on that instance.

A. Run the CLI with `--auth instance_principal` and grant a dynamic group access
B. Store an API key in the instance's metadata and read it at runtime
C. Embed a user's auth token in the script and rotate it monthly
D. Run the script as root so the CLI can skip authentication

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** With instance principal authentication the instance itself is the caller, using automatically rotated credentials, and a dynamic group plus a policy controls what it may do. Keys in metadata or tokens in scripts are still stored credentials. Running as root changes local permissions, not OCI API authentication.

**Key Concept:** [Calling Services from an Instance](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm)
</details>

---

### Question 28
**Scenario:** A teammate updated a Resource Manager stack's Terraform variables. Before anything changes in production, the team wants to see exactly what will be created, changed, or destroyed.

A. Run an apply job with automatic approval enabled
B. Run an import job against the live compartment
C. Run a destroy job followed by an apply job
D. Run a plan job and review its output

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A plan job runs `terraform plan` and lists the proposed creates, updates, and destroys without changing anything, so it can be reviewed before an apply. Auto-approved apply makes the changes immediately. An import job brings existing resources under the stack, and destroy then apply recreates everything with an outage.

**Key Concept:** [Overview of Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm)
</details>

---

### Question 29
**Scenario:** A load balancer shows every backend as Critical, although the application responds when tested locally on each server.

A. Increase the load balancer's bandwidth shape to the maximum
B. Change the load balancing policy from round robin to IP hash on the backend set
C. Check the health check port and path, and allow traffic from the load balancer subnet
D. Add more backend servers so the health checker has more targets

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Backends marked Critical while the app works locally usually means the health check probes the wrong port or path, or security rules (or host firewalls) block the load balancer's subnet. Bandwidth and balancing policy do not affect health checks. Adding servers with the same configuration only adds more failing backends.

**Key Concept:** [Editing Health Checks](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/editinghealthcheck.htm)
</details>

---

### Question 30
**Scenario:** Launching new instances in a compartment fails with a "LimitExceeded" error, although the account has budget and the shape is available in the region.

A. Delete the compartment and launch in a new one
B. Check limits and usage, then request a service limit increase
C. Launch in a different fault domain of the same availability domain
D. Wait for the next billing cycle to reset the counts

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Service limits cap how many resources of a type a tenancy can create. The Limits, Quotas and Usage page shows current use against the limit, and a limit increase request raises it (a compartment quota could also be the cap). A new compartment still counts against tenancy limits, fault domain choice is irrelevant, and limits do not reset with billing.

**Key Concept:** [Service Limits](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm)
</details>

---

## Where to go deeper

- [OCI Operations Associate cert page](../../exams/oracle/oci-operations-associate/) - notes, practice plan, strategy
- [OCI Architect Associate practice questions](./oracle-oci-architect-associate.md) - the design counterpart
- [OCI Foundations practice questions](./oracle-oci-foundations.md) - the fundamentals below
- [Observability basics](../../learn/concepts/observability-basics.md) - the monitoring domain in plain English
- **[📖 Oracle University certification](https://education.oracle.com/oracle-certification-path/pFamily_647)** - official exam pages
