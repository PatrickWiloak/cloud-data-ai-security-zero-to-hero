---
last-updated: 2026-08-09
difficulty: beginner
---

# CompTIA Security+ (SY0-701) - Practice Questions

15 questions for Security+ prep across general security concepts, threats and vulnerabilities, security architecture, operations, and program management.

> **Cert page:** [exams/comptia/security-plus/](../../exams/comptia/security-plus/)

---

### Question 1
**Scenario:** The CIA triad's three components.

A. Control, Integrity, Access
B. Confidentiality, Integrity, Availability
C. Compliance, Identity, Authorization
D. Cryptography, Isolation, Auditing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Confidentiality keeps data from unauthorized viewers, integrity keeps it unaltered, availability keeps it reachable. Most exam questions asking "which principle is affected" resolve by mapping the incident to one of the three: a leak is confidentiality, tampering is integrity, ransomware is availability.
</details>

---

### Question 2
**Scenario:** A control category question: a security guard, a firewall, and a policy document.

A. All technical
B. Physical, technical, and managerial respectively
C. All administrative
D. All operational

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SY0-701 uses managerial, operational, technical, and physical as the categories, cut across by control types: preventive, deterrent, detective, corrective, compensating, and directive. A single control has one category and one type, and questions often ask for both.
</details>

---

### Question 3
**Scenario:** An attacker sends a targeted email to the CFO impersonating the CEO requesting a wire transfer.

A. Phishing
B. Business email compromise, a form of spear phishing known as whaling when it targets executives
C. Vishing
D. Smishing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spear phishing is targeted, whaling targets high-value individuals, and BEC is the fraud pattern built on it. Vishing is voice and smishing is SMS. The exam distinguishes these by the channel and the targeting, so read for both.
</details>

---

### Question 4
**Scenario:** A user's password is stolen but the attacker still cannot log in.

A. Encryption
B. Multi-factor authentication requiring a second factor
C. A firewall
D. Antivirus

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The factors are something you know, something you have, and something you are, with location and behavior as attributes. Two of the same category is not MFA: a password plus a security question is still one factor.
</details>

---

### Question 5
**Scenario:** Which cryptographic property does a hash provide?

A. Confidentiality
B. Integrity, by producing a fixed-length digest that changes if the input changes
C. Availability
D. Non-repudiation on its own

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hashing is one-way and provides no confidentiality. Non-repudiation needs a digital signature, which combines a hash with the signer's private key. Salting defends stored password hashes against precomputed rainbow tables.
</details>

---

### Question 6
**Scenario:** Symmetric versus asymmetric encryption.

A. They are the same
B. Symmetric uses one shared key and is fast; asymmetric uses a public and private key pair, solving key distribution at higher computational cost
C. Asymmetric is always faster
D. Symmetric cannot encrypt bulk data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The practical pattern combines both: asymmetric to exchange a symmetric session key, symmetric for the bulk data. TLS works this way, which is why it needs certificates for the handshake and a cipher for the payload.
</details>

---

### Question 7
**Scenario:** A certificate is presented and the client must verify it is not revoked.

A. Check the expiry date only
B. Check a certificate revocation list or use OCSP, ideally with stapling
C. Trust the certificate
D. Check the hostname only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Validation covers the chain to a trusted root, the hostname, the validity dates, and revocation. OCSP stapling has the server present a signed status response, avoiding a separate client lookup and the privacy leak that comes with it.
</details>

---

### Question 8
**Scenario:** Which describes a zero-day vulnerability?

A. A vulnerability disclosed a year ago
B. A vulnerability with no vendor patch available at the time of exploitation
C. Any unpatched system
D. A misconfiguration

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The defining property is the absence of a fix, which is why compensating controls matter: segmentation, monitoring, and least privilege limit the damage of something you cannot patch. An old unpatched vulnerability is a patch management failure, not a zero-day.
</details>

---

### Question 9
**Scenario:** A network is divided so that a compromised workstation cannot reach the database tier directly.

A. Encryption
B. Segmentation, limiting lateral movement
C. Load balancing
D. Redundancy

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Segmentation assumes a breach will happen and constrains what happens next. Microsegmentation extends it to individual workloads, and a screened subnet (DMZ) is the classic form for internet-facing services.
</details>

---

### Question 10
**Scenario:** An organization must decide how to handle a risk it cannot cost-effectively mitigate.

A. Ignore it
B. Choose among the responses: accept, avoid, transfer (for example insurance), or mitigate, and document the decision
C. Always mitigate
D. Always transfer

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Formal acceptance by an authorized owner is a legitimate outcome and is what the risk register records. The exam also tests the vocabulary around it: risk appetite, residual risk (what remains after controls), and inherent risk (before them).
</details>

---

### Question 11
**Scenario:** The incident response lifecycle order.

A. Detection, preparation, recovery, containment
B. Preparation, detection and analysis, containment, eradication, recovery, lessons learned
C. Containment first, always
D. Recovery, then detection

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Preparation comes first because it is what makes the rest possible, and lessons learned is where the organization actually improves. Containment precedes eradication: stop the spread before you remove the cause.
</details>

---

### Question 12
**Scenario:** RPO and RTO must be distinguished.

A. They are the same
B. RPO is how much data loss is acceptable, driving backup frequency; RTO is how long recovery may take, driving the recovery architecture
C. RTO measures data loss
D. RPO measures downtime

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RPO looks backward from the incident and RTO looks forward. A four-hour RPO means backups at least every four hours; a one-hour RTO usually rules out restoring from tape. MTTR and MTBF are the related availability metrics.
</details>

---

### Question 13
**Scenario:** Logs from many systems must be correlated to detect an attack pattern.

A. A firewall
B. A SIEM, aggregating and correlating log data with alerting
C. An IPS
D. A vulnerability scanner

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Correlation across sources is what reveals patterns invisible in any single log. SOAR adds automated response playbooks on top. An IPS blocks in line, and a scanner finds weaknesses rather than detecting active attacks.
</details>

---

### Question 14
**Scenario:** A penetration test where the tester has no prior knowledge of the environment.

A. White box
B. Unknown environment (black box)
C. Partially known (grey box)
D. A vulnerability scan

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SY0-701 uses known, partially known, and unknown environment terminology. The other distinction the exam tests is scanner versus test: a vulnerability scan identifies potential weaknesses, while a penetration test attempts to exploit them and demonstrate impact.
</details>

---

### Question 15
**Scenario:** Sensitive data must be replaced with a non-sensitive equivalent that can be reversed by an authorized system.

A. Hashing
B. Tokenization, where the token maps back to the original in a secure vault
C. Masking
D. Encryption with a lost key

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Tokenization removes the sensitive value from the processing environment entirely, which is why it is common in payment systems for PCI scope reduction. Masking obscures for display, and hashing is one-way and therefore not reversible.
</details>

---

## Where to go deeper

- [Security+ cert page](../../exams/comptia/security-plus/) - notes, practice plan, strategy
- [CySA+ practice questions](./comptia-cysa-plus.md) - the analyst-level next step
- [ISC2 CC practice questions](./isc2-cc.md) - the entry-level security sibling
- [Security topic index](../../topics/security.md) - security across the repo
- **[📖 CompTIA Security+](https://www.comptia.org/certifications/security)** - official exam objectives
