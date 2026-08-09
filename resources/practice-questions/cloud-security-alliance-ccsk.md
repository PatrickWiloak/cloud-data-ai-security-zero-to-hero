---
last-updated: 2026-08-09
difficulty: intermediate
---

# CCSK v5 - Certificate of Cloud Security Knowledge - Practice Questions

15 questions across the CCSK v5 domains, which follow the CSA Security Guidance v5: governance, risk and compliance, infrastructure and networking, identity and access management, cloud workload security, data security, application security, and incident response. The exam is open book against the Guidance, the Cloud Controls Matrix, and the ENISA report.

> **Cert page:** [exams/cloud-security-alliance/ccsk/](../../exams/cloud-security-alliance/ccsk/)

---

### Question 1
**Scenario:** How does the shared responsibility split change between IaaS and SaaS?

A. It is identical
B. The provider's share grows as you move from IaaS to PaaS to SaaS, but the customer always retains responsibility for data, identities, and access configuration
C. The customer is responsible for everything in SaaS
D. The provider is responsible for everything in IaaS

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The constants are what CCSK emphasizes: data classification, identity, and entitlement stay with the customer at every service model. What moves is the operating system, runtime, and application layers.
</details>

---

### Question 2
**Scenario:** Which document establishes what a provider is actually contractually obliged to do?

A. The provider's marketing material
B. The contract and its service level agreements, since the contract is the primary governance tool in cloud
C. A certification badge
D. The customer's policy

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CSA's position is that in cloud you govern through the contract, because you cannot directly control the provider's operations. Certifications and audit reports are evidence supporting the contract rather than substitutes for it.
</details>

---

### Question 3
**Scenario:** What is the Cloud Controls Matrix?

A. A pricing model
B. A cloud-specific control framework mapped to other standards, used with the CAIQ for provider assessment
C. A network diagram
D. An encryption standard

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The mappings are the practical value: satisfying a CCM control lets you point at the corresponding ISO 27001 or NIST requirement. The Consensus Assessments Initiative Questionnaire is the CCM turned into questions a provider answers, published for many providers in the STAR registry.
</details>

---

### Question 4
**Scenario:** A cloud provider's data center is in another jurisdiction.

A. Only the customer's country's law applies
B. Multiple jurisdictions may apply, including where data resides, where the provider operates, and where the customer operates, which is why data residency and sovereignty are contract terms
C. No law applies
D. Only the provider's country's law applies

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Jurisdictional overlap is a first-order legal risk in cloud, and lawful access requests can come from any of them. Region selection, contractual residency commitments, and encryption with customer-held keys are the practical controls.
</details>

---

### Question 5
**Scenario:** Which is the most significant difference in cloud incident response?

A. Nothing changes
B. Limited forensic access to underlying infrastructure, dependence on provider logs and cooperation, and the need to agree escalation paths in advance
C. Incidents do not occur
D. The provider handles everything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** You cannot image a hypervisor you do not own, so the provider's logging and support commitments become part of your response capability. Snapshot-based acquisition of your own instances is fast, which is a genuine cloud advantage in the other direction.
</details>

---

### Question 6
**Scenario:** Which access control model best fits dynamic cloud environments?

A. Static role assignments only
B. Attribute-based access control with policy conditions, combined with just-in-time elevation and federated identity
C. Individual accounts per system
D. Shared credentials

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Attributes such as tags, time, network path, and device posture express policy that a role list cannot. Federation keeps identity in one authoritative source, which is what avoids the account sprawl that makes deprovisioning unreliable.
</details>

---

### Question 7
**Scenario:** What is the primary security benefit of infrastructure as code?

A. It is faster
B. Consistent, reviewable, version-controlled configuration that can be scanned for policy violations before deployment
C. It eliminates all risk
D. It removes the need for monitoring

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Configuration becomes an artifact you can review, diff, and test, which is what makes prevention possible rather than detection after the fact. The corresponding risk is that a flawed template deploys the same flaw everywhere at once.
</details>

---

### Question 8
**Scenario:** Which encryption approach keeps the provider unable to read customer data?

A. Provider-managed keys
B. Customer-managed or customer-held keys, with client-side encryption being the strongest form
C. Encryption at rest by default
D. TLS only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Provider-managed encryption protects against physical media loss but not against the provider itself. The trade-off with client-side encryption is loss of provider-side processing and search, plus the full weight of key management on the customer.
</details>

---

### Question 9
**Scenario:** Which describes the main risk of serverless functions from a security perspective?

A. There is no attack surface
B. The attack surface shifts to code, dependencies, event sources, and over-permissive function roles rather than to hosts
C. They cannot be attacked
D. The provider secures the code

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Removing the server removes patching but not application risk, and event-driven triggers widen the set of untrusted inputs. Function-level least privilege matters more than in a monolith, because each function's role is a separate blast radius.
</details>

---

### Question 10
**Scenario:** A container image must be trusted before deployment.

A. Trust the registry
B. Scan images for vulnerabilities, sign them, verify signatures at admission, and build from minimal trusted base images
C. Scan at runtime only
D. Use the latest tag

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Supply chain assurance runs from base image to admission control, and `latest` breaks it by making the deployed artifact unidentifiable. Runtime scanning alone finds the problem after it is already running.
</details>

---

### Question 11
**Scenario:** Which best describes cloud network security compared with traditional?

A. Identical
B. Software-defined and identity-aware: security groups and micro-segmentation replace the perimeter, and topology is defined by policy rather than by cabling
C. No network controls exist
D. Only firewalls matter

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Segmentation becomes cheap and granular because it is software, so per-workload policy replaces a small number of network zones. The trade is that a misconfigured rule propagates instantly across everything using that group.
</details>

---

### Question 12
**Scenario:** How should cloud misconfiguration be prevented at scale?

A. Manual review
B. Preventive guardrails through policy as code and organization-level controls, backed by continuous posture management to detect drift
C. Annual audits
D. Training only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Misconfiguration is the leading cause of cloud data exposure, and it appears faster than review cycles can catch it. Prevention at the control plane plus detection for what slips through is the two-layer answer.
</details>

---

### Question 13
**Scenario:** What is the significance of the cloud management plane?

A. It is unimportant
B. It is the highest-value target, because control of the management plane means control of every resource regardless of workload-level controls
C. It is the network layer
D. It is the storage layer

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** This is the structural difference from traditional data centers: an API credential can do what once required physical access. Strong authentication, minimal privileged accounts, and comprehensive logging of the management plane follow directly.
</details>

---

### Question 14
**Scenario:** A business unit must be prevented from creating resources in unapproved regions.

A. A policy document
B. Preventive policy at the organization or account level, such as a service control policy or equivalent, denying actions outside approved regions
C. A monthly report
D. Tagging

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Preventive guardrails at the organization level cannot be overridden by an account administrator, which is what makes them a control rather than a guideline. Detective controls only tell you it already happened.
</details>

---

### Question 15
**Scenario:** How should a cloud exit or portability requirement be addressed?

A. Assume the provider will always be available
B. Plan for it: understand data export formats and egress costs, avoid unnecessary proprietary coupling where portability matters, and define exit terms contractually
C. Use multicloud for everything
D. Keep a copy on premises always

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Lock-in is a business risk to manage deliberately rather than avoid absolutely, since managed services deliver real value in exchange for coupling. Egress cost and the practical time to move large data are the parts most often left out of an exit plan.
</details>

---

## Where to go deeper

- [CCSK cert page](../../exams/cloud-security-alliance/ccsk/) - notes, practice plan, strategy
- [CCSP practice questions](./isc2-ccsp.md) - the deeper cloud security professional exam
- [Shared responsibility model](../../learn/concepts/shared-responsibility-model.md) - plain-English foundation
- [Zero trust architecture](../architecture-patterns/zero-trust-architecture.md) - the design pattern behind identity-aware controls
- **[📖 CSA Security Guidance](https://cloudsecurityalliance.org/research/guidance/)** - the primary CCSK source document
