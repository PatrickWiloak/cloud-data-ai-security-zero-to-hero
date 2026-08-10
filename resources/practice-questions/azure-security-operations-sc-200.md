---
last-updated: 2026-08-09
difficulty: intermediate
---

# Microsoft Security Operations Analyst (SC-200) - Practice Questions

15 questions for SC-200 prep, weighted toward incident response (35-40%), managing a security operations environment (25-30%), and configuring protections and detections (15-20%).

> **Cert page:** [exams/azure/sc-200/](../../exams/azure/sc-200/)

---

### Question 1
**Scenario:** An analyst must find all sign-ins from a specific IP across the last 7 days in Microsoft Sentinel.

A. `SigninLogs | where IPAddress == "1.2.3.4" | where TimeGenerated > ago(7d)`
B. `SigninLogs | search "1.2.3.4"`
C. `search *`
D. Export to Excel and filter

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Filtering the table with an explicit time range and an equality predicate is both correct and efficient, and putting the time filter early lets the engine prune partitions. A free-text `search` scans far more data for the same answer, and `search *` across all tables is the query you run once and never again.
</details>

---

### Question 2
**Scenario:** Which KQL operator joins alert data to enrichment data on a shared column?

A. `union`
B. `join`
C. `summarize`
D. `project`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `join` correlates two result sets on a key, with kinds such as `inner`, `leftouter`, and `leftanti`. `leftanti` is the one worth memorizing because it answers "which of these had no match," which is how you find first-time-seen behavior. `union` stacks rows, `summarize` aggregates, and `project` selects columns.
</details>

---

### Question 3
**Scenario:** A Defender for Endpoint alert shows a device with suspicious activity that must be cut off from the network but remain investigable.

A. Delete the device from the portal
B. Isolate the device, which blocks network traffic while keeping the Defender connection
C. Power it off remotely
D. Run a full antivirus scan only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Isolation preserves the connection back to Defender so you can still run live response, collect an investigation package, and release it afterward. Powering off destroys volatile memory evidence and stops your telemetry. Deleting the device removes your visibility entirely.
</details>

---

### Question 4
**Scenario:** Sentinel should ingest AWS CloudTrail logs.

A. It is not possible
B. A data connector for AWS, configured with a role Sentinel can assume
C. Manual CSV upload
D. A syslog forwarder only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Sentinel has first-party connectors for AWS, GCP, and many third-party sources; the AWS one uses a cross-account IAM role with an external ID. Being multicloud is a large part of why organizations pick Sentinel as the SIEM over a single-cloud tool.
</details>

---

### Question 5
**Scenario:** An analytics rule generates 400 alerts a day for the same benign administrative activity.

A. Disable the rule
B. Tune it: add exclusions for the known-good identity or process, and consider grouping alerts into a single incident
C. Ignore the alerts
D. Increase the ingestion cap

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Alert fatigue is a real security failure, because analysts stop reading. Tuning keeps the detection while removing the known cause, and incident grouping collapses repeated alerts into one investigable unit. Disabling the rule outright loses coverage for the malicious version of the same behavior.
</details>

---

### Question 6
**Scenario:** A phishing email reached 50 mailboxes and must be removed from all of them.

A. Ask users to delete it
B. Threat Explorer in Defender for Office 365 with a soft-delete or hard-delete remediation action
C. A transport rule for future mail only
D. Reset all 50 passwords

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Explorer finds the message across mailboxes and triggers remediation (zero-hour auto purge style removal) as a bulk action with an approval workflow. A transport rule stops the next one but does not touch mail already delivered. Password resets may still be warranted if credentials were entered, but they do not remove the message.
</details>

---

### Question 7
**Scenario:** Which Defender product protects against identity attacks such as Pass-the-Hash against on-premises Active Directory?

A. Defender for Endpoint
B. Defender for Identity
C. Defender for Cloud Apps
D. Defender for Office 365

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Defender for Identity installs sensors on domain controllers and AD FS servers and detects reconnaissance, credential theft, and lateral movement techniques against AD DS. Defender for Endpoint covers devices, Cloud Apps covers SaaS usage, and Office 365 covers mail and collaboration.
</details>

---

### Question 8
**Scenario:** A user's session in a SaaS app should be blocked from downloading sensitive files on an unmanaged device.

A. Defender for Cloud Apps session policy with Conditional Access App Control
B. A NSG rule
C. An analytics rule
D. A retention label

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Conditional Access App Control proxies the session so Cloud Apps can inspect and block actions in real time, including download, upload, copy, and print. Conditional Access alone can allow or deny the sign-in but cannot control what happens inside an allowed session.
</details>

---

### Question 9
**Scenario:** An incident must trigger an automatic Teams message and ticket creation.

A. A workbook
B. An automation rule invoking a Logic Apps playbook
C. A hunting query
D. A watchlist

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Automation rules define when to act (incident created, updated, matching conditions) and playbooks are the Logic Apps that perform the actions. Workbooks visualize, hunting queries search proactively, and watchlists are reference data you join against.
</details>

---

### Question 10
**Scenario:** A hunting hypothesis is "an attacker used a rarely seen parent-child process pair." What is the right Sentinel feature?

A. An analytics rule
B. A hunting query, saved and optionally promoted to an analytics rule once validated
C. A workbook
D. A data connector

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hunting is hypothesis-driven searching that has not yet earned a detection, and the natural lifecycle is hunt, validate, then promote to a scheduled analytics rule. Creating an unvalidated analytics rule first usually produces the alert fatigue from question 5.
</details>

---

### Question 11
**Scenario:** Log ingestion costs are rising and much of the volume is verbose, low-value data needed only for occasional audit.

A. Stop collecting it
B. Route it to a cheaper tier such as auxiliary or basic logs, or archive with long-term retention, keeping analytics tier for data used in detections
C. Reduce retention to one day
D. Sample randomly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Sentinel's tiering exists precisely for this: analytics tier for data your rules query, cheaper tiers plus search jobs and restore for data you need occasionally. Dropping the data or cutting retention to a day removes your ability to investigate a breach discovered weeks later, which is the common case.
</details>

---

### Question 12
**Scenario:** During triage you need to see the full attack story: which device, which user, which files, in sequence.

A. The incident graph and the unified incident timeline in the Defender portal
B. The raw table
C. Secure Score
D. Compliance Manager

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Incident correlation stitches related alerts across Defender workloads and Sentinel into one incident with entities and a timeline, which is the difference between a pile of alerts and an attack narrative. Raw tables are where you go for detail after you know what to look at.
</details>

---

### Question 13
**Scenario:** A device group should get a more aggressive attack surface reduction rule set than the rest of the estate.

A. Device groups in Defender for Endpoint with a targeted ASR policy
B. A single tenant-wide policy
C. Conditional Access
D. A firewall rule

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Device groups let you scope policy and also scope analyst permissions by group. Rolling ASR rules out in audit mode to a pilot group first, then enforcing, is the standard approach because some rules break legitimate line-of-business software.
</details>

---

### Question 14
**Scenario:** After containment, what should close out the incident process?

A. Delete the incident
B. Eradication and recovery, then a post-incident review capturing detection gaps and turning them into new rules
C. Reboot the affected servers
D. Nothing further

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The standard lifecycle is preparation, detection and analysis, containment, eradication, recovery, and lessons learned. The last stage is where a SOC actually improves: each incident should leave behind a new detection, a tuned rule, or a closed gap. Deleting the incident destroys the record you need for that.
</details>

---

### Question 15
**Scenario:** A rule must detect five failed sign-ins followed by a success from the same account within 10 minutes.

A. A scheduled analytics rule with a KQL query using `summarize` over a time window and a `join` for the success
B. A Fusion rule
C. A watchlist
D. A workbook

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Scheduled rules run KQL on an interval with a lookback window, which is where you express multi-event logic like this. Fusion is Microsoft's built-in multistage attack detection using machine learning and is not something you author. Workbooks and watchlists do not generate incidents.
</details>

---

## Where to go deeper

- [SC-200 cert page](../../exams/azure/sc-200/) - notes, practice plan, strategy
- [SC-900 practice questions](./azure-security-compliance-identity-sc-900.md) - the fundamentals below this
- [SC-100 practice questions](./azure-cybersecurity-architect-sc-100.md) - the architecture exam above it
- [AZ-500 practice questions](./azure-security-az-500.md) - the platform security counterpart
- **[📖 SC-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200)** - official skills outline
