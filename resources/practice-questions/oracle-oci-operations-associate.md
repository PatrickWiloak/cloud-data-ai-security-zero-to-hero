---
last-updated: 2026-08-09
difficulty: intermediate
---

# Oracle Cloud Infrastructure Operations Associate (1Z0-1067) - Practice Questions

15 questions for OCI Operations Associate prep, weighted toward observability and management (20%), then compute, storage, network, and security operations (15% each).

> **Cert page:** [exams/oracle/oci-operations-associate/](../../exams/oracle/oci-operations-associate/)

---

### Question 1
**Scenario:** An alarm must notify a team and trigger an automated response.

A. Email only
B. A Monitoring alarm publishing to a Notifications topic, with subscriptions to email and to a function that performs the remediation
C. A log query
D. Manual checks

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Notifications topics fan out to multiple subscription types, so one alarm can both inform a human and invoke automation. Using a function subscription is how you build auto-remediation for well-understood conditions.
</details>

---

### Question 2
**Scenario:** Logs from many services and instances must be searched centrally.

A. Log in to each host
B. The Logging service with log groups, plus the agent configuration for custom logs, and Logging Analytics for parsing and correlation
C. Local files only
D. Screenshots

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Service logs, audit logs, and custom logs all land in the Logging service, and Logging Analytics adds parsing and dashboards on top. Central collection matters most during an incident, when logging into hosts is slowest.
</details>

---

### Question 3
**Scenario:** Patching must be applied to many instances on a schedule with reporting.

A. SSH to each instance
B. OS Management Hub, with managed instance groups, scheduled jobs, and compliance reporting
C. Recreate instances weekly
D. Ignore patches

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Managed groups let one job cover many instances and produce the compliance evidence an auditor asks for. Manual patching neither scales nor leaves a record, which is usually the more expensive gap.
</details>

---

### Question 4
**Scenario:** A block volume must be backed up automatically with retention.

A. Manual snapshots
B. A backup policy (bronze, silver, gold, or custom) assigned to the volume, with cross-region copy where DR requires it
C. Copy files
D. No backup

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Policy-based backups run on a schedule with defined retention and can copy to another region. Volume groups let you snapshot several volumes at a consistent point, which matters when an application spans volumes.
</details>

---

### Question 5
**Scenario:** An instance must move to a larger shape with minimal disruption.

A. Rebuild it
B. Stop the instance, change the shape (or edit a flexible shape's OCPU and memory), and start it
C. It cannot be changed
D. Attach more volumes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Shape changes require a stop and start on virtual machines, and flexible shapes let you adjust OCPUs and memory independently within the family. Knowing that this is a reboot rather than a rebuild changes how the maintenance window is planned.
</details>

---

### Question 6
**Scenario:** Instance maintenance is announced by Oracle.

A. Ignore it
B. Read the maintenance notification, and for a live-migration-ineligible instance plan the reboot within the window, or proactively reboot at a convenient time
C. Delete the instance
D. Open a support ticket

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Many instances live migrate transparently, but some, including those with local NVMe or certain shapes, require a reboot. Acting early inside the window means the disruption happens when you choose rather than when the deadline arrives.
</details>

---

### Question 7
**Scenario:** Network connectivity between two instances fails intermittently.

A. Recreate the instances
B. Check security lists and NSGs, route tables, and then use the network path analyzer and VNIC metrics to localize the problem
C. Reboot everything
D. Increase the shape

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Configuration first, then measurement: path analysis evaluates the rules and routes for a specific source and destination, which distinguishes a policy problem from a genuine network issue. Rebooting hides intermittent problems without explaining them.
</details>

---

### Question 8
**Scenario:** Cloud Guard reports a problem for a publicly accessible bucket.

A. Dismiss it
B. Investigate whether public access is intended; if not, remove it and consider a Security Zone to prevent recurrence
C. Delete the bucket
D. Disable Cloud Guard

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Fixing the instance is half the job; preventing the next one is the other half. Security Zones refuse the operation outright, which converts a recurring detection into a configuration that cannot happen in that compartment.
</details>

---

### Question 9
**Scenario:** Costs are rising and the cause is unclear.

A. Reduce all resources
B. Use Cost Analysis with grouping by compartment, service, and tag, then act on the largest contributors and set budgets with alerts
C. Cancel the account
D. Estimate

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Attribution before action: cost is usually concentrated in a few resources, and cutting broadly hurts things that were not the problem. Budgets with forecast alerts then give warning before the next surprise.
</details>

---

### Question 10
**Scenario:** An audit asks who terminated an instance last week.

A. Instance logs
B. The Audit service, which records API calls with the principal, action, and time
C. Monitoring metrics
D. Nobody can tell

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Audit records control plane API activity across the tenancy and is enabled by default with a retention period. Instance logs disappear with the instance, which is exactly the case here.
</details>

---

### Question 11
**Scenario:** Object Storage costs are growing from data nobody reads.

A. Delete everything
B. Lifecycle policy rules moving objects to infrequent access and archive, with deletion rules where retention allows
C. Compress only
D. Move to block storage

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Tiering matches storage cost to access frequency automatically. Archive is much cheaper but requires a restore before reading, so apply it to data whose retention is a compliance obligation rather than an operational need.
</details>

---

### Question 12
**Scenario:** An OKE cluster's nodes must be updated to a new Kubernetes version.

A. Update in place with no drain
B. Add a new node pool on the target version, cordon and drain the old nodes to migrate workloads, then remove the old pool
C. Delete the cluster
D. Update only the control plane

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Control plane first, then nodes, is the required order. The blue-green node pool approach keeps workloads running and makes rollback a matter of draining back, whereas in-place node updates leave less room to retreat.
</details>

---

### Question 13
**Scenario:** Operational tasks must be automated without maintaining servers.

A. Cron on a VM
B. Resource Scheduler or Events triggering Functions, with Resource Manager for infrastructure changes
C. Manual runbooks
D. A spreadsheet

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Event-driven automation responds to the actual condition, and scheduled automation handles the predictable work such as stopping non-production instances overnight. Both remove the person who might forget.
</details>

---

### Question 14
**Scenario:** A database's performance has degraded.

A. Resize immediately
B. Use Database Management and Performance Hub to find the top SQL and wait events, then address the query or index before changing capacity
C. Restart it
D. Add storage

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Diagnosis first: most degradation traces to a plan change or a missing index rather than genuine capacity exhaustion. Scaling first works, expensively and permanently, on a problem an index would have fixed.
</details>

---

### Question 15
**Scenario:** Access reviews must confirm who can do what in a compartment.

A. Ask people
B. Review IAM policies and group memberships for the compartment, and use Audit to see what access was actually exercised
C. Check the console visually
D. Assume it is correct

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Policy review shows what is permitted; audit data shows what was used. The gap between the two is where you find permissions nobody needs, which is the most productive place to apply least privilege.
</details>

---

## Where to go deeper

- [OCI Operations Associate cert page](../../exams/oracle/oci-operations-associate/) - notes, practice plan, strategy
- [OCI Architect Associate practice questions](./oracle-oci-architect-associate.md) - the design counterpart
- [OCI Foundations practice questions](./oracle-oci-foundations.md) - the fundamentals below
- [Observability basics](../../learn/concepts/observability-basics.md) - the monitoring domain in plain English
- **[📖 Oracle University certification](https://education.oracle.com/oracle-certification-path/pFamily_647)** - official exam pages
