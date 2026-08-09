---
last-updated: 2026-08-09
difficulty: intermediate
---

# CompTIA CySA+ (CS0-003) - Practice Questions

15 questions for CySA+ prep across security operations, vulnerability management, incident response and management, and reporting and communication.

CySA+ is analyst-level and behavioral: it tests what you do with the data, not just what the terms mean.

> **Cert page:** [exams/comptia/cysa-plus/](../../exams/comptia/cysa-plus/)

---

### Question 1
**Scenario:** A vulnerability scan returns 4,000 findings. What drives remediation order?

A. CVSS base score alone
B. Risk in context: exploitability and known exploitation in the wild, asset criticality, exposure, and compensating controls, alongside the CVSS score
C. Alphabetical by host
D. Oldest first

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A critical CVSS on an isolated internal test box outranks nothing. Environmental and temporal CVSS metrics exist for exactly this adjustment, and known-exploited catalogues turn "theoretically severe" into "actively used", which is the strongest prioritization signal available.
</details>

---

### Question 2
**Scenario:** A scanner reports a vulnerability the analyst confirms is not present.

A. Report it anyway
B. A false positive: validate, document the finding as such with evidence, and tune the scanner or add an exception so it does not recur
C. Ignore all scanner output
D. Disable the scanner

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Validation is the analyst's core job, because untuned scanner output erodes trust in the whole programme. Note the counterpart: a false negative is more dangerous and is why scanning is layered with configuration review and penetration testing.
</details>

---

### Question 3
**Scenario:** A SIEM rule fires 300 times a day for benign administrative activity.

A. Disable the rule
B. Tune it: add exclusions for the known-good identity or process, and consider grouping alerts into one incident
C. Ignore the alerts
D. Increase the alert threshold arbitrarily

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Alert fatigue is a real security failure because analysts stop reading. Tuning preserves the detection for the malicious version of the behavior; disabling the rule loses that coverage entirely, which is what makes the two options meaningfully different.
</details>

---

### Question 4
**Scenario:** Which describes threat hunting?

A. Responding to alerts
B. Hypothesis-driven proactive searching for adversary activity that existing detections have not caught
C. Running vulnerability scans
D. Reading vendor advisories

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hunting starts from a hypothesis ("an attacker would establish persistence via scheduled tasks") rather than from an alert. The lifecycle matters: a validated hunt becomes a new detection, which is how hunting improves the SOC rather than being a one-off exercise.
</details>

---

### Question 5
**Scenario:** An analyst maps observed attacker behavior to a common framework.

A. CVSS
B. MITRE ATT&CK, mapping tactics and techniques
C. OWASP Top 10
D. NIST CSF

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ATT&CK gives a shared vocabulary for behavior, which supports coverage analysis: which techniques do we detect, and where are the gaps. The Cyber Kill Chain and the Diamond Model are the other two models CySA+ expects you to recognize.
</details>

---

### Question 6
**Scenario:** Indicators of compromise versus indicators of attack.

A. They are identical
B. IOCs are artifacts of activity that already happened (hashes, IPs, domains); IOAs describe behavior in progress and generalize better across variants
C. IOAs are historical
D. IOCs are behavioral

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hash and IP indicators are trivially changed by an attacker, which is why behavior-based detection outlives them. The practical implication is where to invest detection effort: atomic indicators for cheap coverage, behavioral analytics for durability.
</details>

---

### Question 7
**Scenario:** A host is confirmed compromised. What comes first?

A. Reimage immediately
B. Containment that preserves evidence: isolate the host from the network while keeping it running, and capture volatile data before shutdown
C. Shut it down
D. Run antivirus

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Powering off destroys memory-resident evidence, which is often where the malware actually lives. Order of volatility guides collection: registers and cache, then memory, then network state, then disk. Isolation stops the spread without losing the artifacts.
</details>

---

### Question 8
**Scenario:** Evidence must hold up in a legal proceeding.

A. Copy the files to a share
B. Maintain chain of custody, take forensically sound images with hash verification, and work from copies
C. Analyze the original disk
D. Screenshot everything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Chain of custody documents every handler and transfer; hashing proves the image is unaltered. Working on the original rather than a verified copy is what gets evidence excluded, regardless of what the analysis found.
</details>

---

### Question 9
**Scenario:** Network traffic shows periodic outbound connections to an unknown domain at exact intervals.

A. Normal traffic
B. Possible command-and-control beaconing: investigate the destination reputation, the process making the connection, and the payload
C. A DNS issue
D. A backup job by definition

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Regularity is the signature; legitimate traffic is usually more irregular, though jitter is used to evade this exact detection. The pivot from network observation to the responsible process on the host is what turns a suspicion into a finding.
</details>

---

### Question 10
**Scenario:** A web server log shows requests containing `' OR '1'='1`.

A. A malformed request
B. An SQL injection attempt: check whether it succeeded, review the application's parameterization, and assess data exposure
C. A scanner artifact to ignore
D. A DDoS attack

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The follow-up matters more than the identification: attempted and successful are different incidents. Response codes and response sizes in the log usually distinguish them, and parameterized queries are the fix rather than input filtering.
</details>

---

### Question 11
**Scenario:** Which log source best answers "which process opened this network connection"?

A. Firewall logs
B. Endpoint detection and response or host process telemetry, correlated with the network connection
C. DNS logs
D. Web server logs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Network logs identify endpoints, not processes. Correlating host and network telemetry is the standard analyst pivot, and it is why EDR deployment coverage gaps are a detection problem rather than just a tooling preference.
</details>

---

### Question 12
**Scenario:** A patch cannot be applied to a critical production system.

A. Accept the risk silently
B. Apply compensating controls (segmentation, virtual patching at the IPS or WAF, tightened monitoring), document the exception with an owner and a review date
C. Take the system offline permanently
D. Patch anyway during business hours

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Exceptions are legitimate when they are documented, time-bounded, and owned. The failure mode is the permanent undocumented exception, which is indistinguishable from having forgotten about the vulnerability entirely.
</details>

---

### Question 13
**Scenario:** A report is being written for executives after an incident.

A. Full packet captures and log excerpts
B. Business impact, what was affected, actions taken, current status, and specific recommendations with owners, keeping technical detail in an appendix
C. Technical detail only
D. A single sentence

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Audience-appropriate reporting is an examinable CySA+ skill. Executives need impact and decisions; the technical team needs the detail. Sending packet captures to an executive is the same communication failure as sending "it's fixed" to the engineers.
</details>

---

### Question 14
**Scenario:** Which metric best shows whether the SOC is improving?

A. Number of alerts
B. Mean time to detect and mean time to respond, trended over time
C. Number of tools deployed
D. Number of rules

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** MTTD and MTTR measure outcomes; alert and rule counts measure activity and can rise while effectiveness falls. Trending matters more than the absolute value, since the baseline differs by environment.
</details>

---

### Question 15
**Scenario:** A phishing email reached 200 users and 12 clicked.

A. Reset all passwords and close
B. Scope it: identify who clicked and who entered credentials, remove the message from all mailboxes, reset affected credentials, hunt for follow-on activity, and feed the indicators into detection
C. Notify users only
D. Block the sender domain and close

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Clicking and entering credentials are different exposure levels requiring different responses. Blocking the sender addresses the next campaign, not this one, and the hunt for post-compromise activity is what distinguishes closing the ticket from closing the incident.
</details>

---

## Where to go deeper

- [CySA+ cert page](../../exams/comptia/cysa-plus/) - notes, practice plan, strategy
- [Security+ practice questions](./comptia-security-plus.md) - the prerequisite level
- [SC-200 practice questions](./azure-security-operations-sc-200.md) - the same role on Microsoft tooling
- [Security topic index](../../topics/security.md) - security across the repo
- **[📖 CompTIA CySA+](https://www.comptia.org/certifications/cybersecurity-analyst)** - official exam objectives
