---
last-updated: 2026-08-09
difficulty: advanced
---

# CCSP - Certified Cloud Security Professional - Practice Questions

15 questions across the six CCSP domains: cloud concepts and architecture, cloud data security, cloud platform and infrastructure security, cloud application security, cloud security operations, and legal, risk and compliance.

CCSP rewards vendor-neutral thinking. Answers describe concepts and processes rather than a specific provider's service names.

> **Cert page:** [exams/isc2/ccsp/](../../exams/isc2/ccsp/)

---

### Question 1
**Scenario:** What are the phases of the cloud secure data lifecycle?

A. Create, store, delete
B. Create, store, use, share, archive, destroy
C. Ingest, process, output
D. Collect, analyze, report

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The lifecycle is a CCSP staple because controls differ per phase, and the question is usually which control belongs where. Destroy in cloud typically means cryptographic erasure, since you cannot physically destroy media you do not own.
</details>

---

### Question 2
**Scenario:** Data must be rendered unrecoverable on a cloud provider's multi-tenant storage.

A. Physical destruction
B. Cryptoshredding: destroy the encryption keys so the ciphertext is unrecoverable
C. Overwriting
D. Degaussing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Physical media methods are unavailable to a tenant and overwriting cannot guarantee coverage of every replica. Cryptographic erasure is the recognized cloud answer, and it only works if the data was encrypted with keys you control.
</details>

---

### Question 3
**Scenario:** Which technique replaces sensitive values with non-sensitive surrogates that can be reversed by an authorized system?

A. Hashing
B. Tokenization, where a token vault maps tokens back to the original values
C. Masking
D. Anonymization

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Tokenization is reversible through the vault, which is what makes it work for payment card scope reduction. Hashing is one-way, masking obscures for display, and anonymization is meant to be irreversible.
</details>

---

### Question 4
**Scenario:** Which cloud deployment model serves a group of organizations with shared concerns?

A. Public
B. Community cloud
C. Private
D. Hybrid

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The four NIST models are public, private, community, and hybrid. Community is the one candidates forget: a shared infrastructure for organizations with common compliance or mission requirements, such as a government or healthcare consortium.
</details>

---

### Question 5
**Scenario:** What does a Type 2 SOC 2 report add over a Type 1?

A. Nothing
B. Testing of operating effectiveness over a period, rather than design suitability at a point in time
C. A different scope
D. A financial audit

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Type 1 answers whether the controls are designed appropriately as of a date; Type 2 answers whether they actually worked across a period, typically 6 to 12 months. SOC 1 covers financial reporting controls and SOC 3 is the public summary.
</details>

---

### Question 6
**Scenario:** A cloud application must be assessed for vulnerabilities during development.

A. Penetration testing only, after release
B. SAST on source, SCA on dependencies, DAST on the running application, and threat modeling during design
C. A code review only
D. Runtime monitoring

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The techniques find different classes of defect, which is why they are layered rather than alternatives. Software composition analysis matters disproportionately in cloud applications, where most of the code is third-party dependencies.
</details>

---

### Question 7
**Scenario:** Which best describes a cloud access security broker?

A. A firewall
B. A control point between users and cloud services enforcing visibility, compliance, data security, and threat protection
C. An identity provider
D. A load balancer

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CASBs address shadow IT discovery and consistent policy across SaaS that individual applications cannot provide. API-based deployment inspects data at rest in the service; proxy-based deployment sits inline and sees traffic in real time.
</details>

---

### Question 8
**Scenario:** Virtualization introduces which distinctive risk?

A. None
B. Hypervisor escape and inter-VM attacks, plus VM sprawl and snapshot data leakage
C. Only network risk
D. Only physical risk

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The hypervisor is a shared trust boundary, so a compromise there crosses every tenant on the host. Snapshots are the quieter risk: they capture memory and disk including secrets, and they are frequently stored with weaker controls than the running system.
</details>

---

### Question 9
**Scenario:** A business impact analysis is being performed for a cloud-hosted service.

A. Focus on technical recovery only
B. Identify critical processes, their maximum tolerable downtime, and dependencies including the provider's own dependencies, then derive RTO and RPO
C. Copy the provider's SLA
D. Assume the provider handles continuity

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The BIA drives the recovery objectives, not the other way around. Provider dependency mapping is the cloud-specific addition, because a regional service outage can take down a component you never considered separately.
</details>

---

### Question 10
**Scenario:** Which key management approach gives the customer the most control in a cloud service?

A. Provider-managed keys
B. Hold Your Own Key, where keys remain in customer-controlled infrastructure and the provider requests use
C. Provider-generated customer-managed keys
D. No encryption

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Control escalates from provider-managed, to customer-managed within the provider's KMS, to bring your own key, to hold your own key. Each step increases control and increases the customer's operational burden and the risk of locking themselves out.
</details>

---

### Question 11
**Scenario:** An eDiscovery request covers data held by a cloud provider.

A. The provider handles it
B. The customer remains responsible for producing the data; the contract should address preservation, collection assistance, and chain of custody
C. It cannot be fulfilled
D. Only the provider's data is discoverable

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Legal hold in a multi-tenant environment is a contractual capability rather than a technical one you can perform yourself. Agreeing it before the litigation is what makes it possible; negotiating it after is not a strong position.
</details>

---

### Question 12
**Scenario:** Which control best addresses the risk of a malicious insider at the cloud provider?

A. Trusting the provider
B. Customer-held encryption keys, comprehensive logging, and contractual and audit assurance over the provider's personnel controls
C. Network segmentation
D. Multi-factor authentication for customer staff

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** You cannot administer the provider's staff, so the durable technical control is making the data unreadable without your keys. The rest is assurance: background screening, separation of duties, and privileged access monitoring evidenced through audit reports.
</details>

---

### Question 13
**Scenario:** Which describes the correct approach to security in a DevOps pipeline?

A. A security gate at the end
B. Security integrated throughout: threat modeling in design, automated scanning in the pipeline, policy as code, and secrets handled through a managed store
C. Manual review before release
D. Post-deployment scanning only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A single gate at the end becomes the bottleneck teams route around, and it finds problems at their most expensive point. Secrets in code and in CI variables are the specific recurring failure, which is why a managed secret store is called out.
</details>

---

### Question 14
**Scenario:** Which logging capability is most important for cloud security operations?

A. Application logs only
B. Management plane and API activity logs, centralized in tamper-resistant storage with defined retention, alongside workload and network logs
C. Provider status pages
D. Billing records

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The control plane is where an attacker with credentials does the most damage in the least time. Making those logs immutable and stored in an account the compromised identity cannot reach is what preserves them through an incident.
</details>

---

### Question 15
**Scenario:** How should a cloud provider's compliance certifications be used in a customer's own compliance program?

A. As full transfer of the requirement
B. As inherited controls covering the provider's share, with the customer documenting its own controls and any complementary user entity controls
C. As irrelevant
D. As a replacement for the customer's own audit

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Inheritance is real and useful: you do not re-audit the provider's data centers. What remains is everything above the responsibility line plus the controls the provider's report assumes you implement, which is the part most often skipped.
</details>

---

## Where to go deeper

- [CCSP cert page](../../exams/isc2/ccsp/) - notes, practice plan, strategy
- [CISSP practice questions](./isc2-cissp.md) - the broader prerequisite-level exam
- [CCSK practice questions](./cloud-security-alliance-ccsk.md) - the CSA counterpart
- [Shared responsibility model](../../learn/concepts/shared-responsibility-model.md) - plain-English foundation
- **[📖 ISC2 CCSP](https://www.isc2.org/certifications/ccsp)** - official exam outline
