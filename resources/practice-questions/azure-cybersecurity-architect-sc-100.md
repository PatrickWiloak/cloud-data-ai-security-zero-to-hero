# Microsoft Cybersecurity Architect (SC-100) - Practice Questions

15 design questions for SC-100 prep. SC-100 is a **design** exam: more than one option usually works, and the constraint in the question decides which is correct. Read the qualifier before the options.

> **Cert page:** [exams/azure/sc-100/](../../exams/azure/sc-100/)

---

### Question 1
**Scenario:** A company must ensure backups survive an attack in which an administrator account is fully compromised. Cost is a secondary concern. What should the design include?

A. Geo-redundant storage on the Recovery Services vault
B. Immutable vault with soft delete and multi-user authorization using a Resource Guard
C. More frequent backup schedules
D. A second backup product from a different vendor

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The threat is an authorized identity performing destructive operations. Immutability prevents deletion or retention reduction within the retention period, and multi-user authorization requires a second approver held in a separate subscription. Geo-redundancy protects against regional failure, not against authorized deletion. More frequent backups create more recovery points that the same compromised identity could delete. A second product duplicates cost without addressing identity compromise.
</details>

---

### Question 2
**Scenario:** An organization must prevent engineers from holding standing subscription Owner rights while allowing them to perform occasional administrative work. The tenant has Microsoft Entra ID P2. Least administrative effort is required.

A. Conditional Access requiring MFA for administrators
B. Privileged Identity Management with eligible assignments, approval, and time limits
C. An entitlement management access package for the Owner role
D. A scheduled script that adds and removes role assignments

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PIM is the feature for just-in-time privileged role activation with approval, justification, and time bounds. Conditional Access governs the conditions of a sign-in, not standing role assignment. Entitlement management covers resource entitlement, not directory or Azure role activation. A script is manual effort with no audit trail, which fails the least-effort constraint.
</details>

---

### Question 3
**Scenario:** A retailer has 12 subscriptions across three regions and two Entra tenants after an acquisition. A single central SOC operates it. EU log data must remain in EU regions, and the logging bill is unsustainable. What Sentinel design fits?

A. One global workspace for simplicity
B. One workspace per subscription
C. One workspace per data residency boundary, cross-workspace queries, and Azure Lighthouse for cross-tenant access
D. Migrate the acquired tenant first, then use a single workspace

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Workspace count is driven by data residency and tenancy, not subscription count. Two workspaces satisfy the EU boundary, cross-workspace queries keep a single SOC investigation surface, and Lighthouse provides cross-tenant access without a tenant migration project. A global workspace violates residency. Twelve workspaces are costly and fragment investigation. Tenant migration is a large project when Lighthouse achieves the operational goal now.
</details>

---

### Question 4
**Scenario:** An insurer requires that application VMs reach Azure Storage without traffic traversing the public internet, that the storage account is unreachable from any other network, and that on-premises systems over ExpressRoute reach it privately.

A. Service endpoints on the VM subnet
B. Storage firewall rules allowlisting the on-premises IP range
C. Private endpoint with public network access disabled, plus a linked private DNS zone and on-premises conditional forwarders
D. Both a service endpoint and a private endpoint

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Only a private endpoint gives the resource a private IP and allows disabling public access entirely, and only it extends to on-premises over ExpressRoute. Service endpoints keep a public IP on the resource and do not work from on-premises. IP allowlisting still traverses the public internet. Configuring both is redundant and makes DNS resolution ambiguous. The private DNS component is part of the correct answer, not an optional extra.
</details>

---

### Question 5
**Scenario:** An organization runs Azure, AWS, GCP, and VMware on-premises. It wants one posture view, one ISO 27001 compliance report across all environments, and runtime threat detection on servers, with minimal agent sprawl.

A. A third-party CSPM product
B. Defender for Cloud with AWS and GCP connectors, Azure Arc for VMware servers, and Defender for Servers Plan 2
C. Separate compliance reporting per cloud
D. Deploy Defender for Endpoint independently on every server

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Defender for Cloud is the single posture plane; native connectors bring AWS and GCP in agentlessly; Arc projects the VMware servers into Azure Resource Manager; and Defender for Servers Plan 2 deploys Defender for Endpoint through Arc rather than as a separate agent stack, satisfying the agent-sprawl constraint. A third-party tool adds a product the native connectors make unnecessary. Separate reports fail the single-report requirement.
</details>

---

### Question 6
**Scenario:** A hospital group must keep on-premises Active Directory authoritative and has a compliance requirement that password hashes must not be stored in the cloud in any form. Which hybrid identity method fits, and what is the consequence?

A. Password hash sync; no consequence
B. Pass-through authentication with redundant connectors; cloud sign-in depends on on-premises connector availability
C. Cloud-only identities; on-premises authority is lost
D. AD FS; the simplest option to operate

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PTA validates credentials against on-premises AD without storing any hash in Entra ID, satisfying the constraint. The consequence is that sign-in depends on connector availability, so a datacenter outage breaks cloud authentication. Password hash sync is Microsoft's default recommendation but is excluded by the constraint. Cloud-only loses on-premises authority. AD FS meets the constraint but adds substantial infrastructure and is the option Microsoft guidance steers away from.
</details>

---

### Question 7
**Scenario:** A payments company must isolate its cardholder data environment, inspect all traffic between it and the rest of the estate including TLS-encrypted flows, prevent direct internet egress, and produce PCI DSS assessment evidence.

A. NSGs and application security groups only
B. Azure Firewall Standard in a hub, with NSGs in the spoke
C. Azure Firewall Premium in the hub with TLS inspection and IDPS, forced tunneling, a dedicated CDE subscription under its own management group, and the PCI DSS initiative in Defender for Cloud
D. A single subscription with resource groups as the compliance boundary

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Premium is the tier that provides TLS inspection and IDPS, which Standard lacks. Forced tunneling removes direct internet routes. Aligning the compliance boundary with a subscription and management group gives clean policy, RBAC, and audit scoping. The regulatory compliance dashboard supplies assessment evidence. NSGs alone offer no layer 7 inspection.
</details>

---

### Question 8
**Scenario:** A company is deploying an internal AI assistant over SharePoint and OneDrive. Legal is concerned employees will surface documents they should not see. Reclassifying the entire document estate by hand is not acceptable.

A. Block the assistant from all sites containing sensitive data
B. Rely on the assistant's built-in filtering
C. Fix oversharing at the source, then apply Purview auto-labeling, DLP for AI applications, and DSPM for AI
D. Manually classify the highest-risk document libraries first

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** An AI assistant honors existing permissions, so oversharing in SharePoint becomes exposure in the assistant. The correct sequence is fix permissions, then classify at scale with auto-labeling, then enforce with DLP, then monitor with DSPM for AI. Blocking sites defeats the deployment. Built-in filtering enforces permissions, it does not fix them. Manual classification fails the stated constraint.
</details>

---

### Question 9
**Scenario:** A design must ensure that a recommendation about misconfigured storage accounts appears in a compliance report, and that exploitation attempts against those accounts raise alerts. Which Defender for Cloud capabilities are needed?

A. CSPM only
B. Defender for Storage only
C. CSPM for the misconfiguration recommendation and Defender for Storage for runtime alerting
D. Azure Policy only

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Posture and compliance recommendations come from CSPM, which is largely free. Runtime threat detection, including malware scanning and anomalous access alerts, requires the paid Defender for Storage workload plan. The two halves answer different requirements, and questions frequently include both in one scenario.
</details>

---

### Question 10
**Scenario:** Which Zero Trust principle does requiring a compliant device through Conditional Access primarily implement?

A. Assume breach
B. Verify explicitly
C. Use least privilege access
D. Segment everything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Verify explicitly means authenticating and authorizing on all available signals, including device state. Least privilege concerns the scope of granted access, addressed by PIM and RBAC. Assume breach drives segmentation, encryption, and detection. "Segment everything" is not one of the three principles.
</details>

---

### Question 11
**Scenario:** A regulated customer requires that Microsoft cannot access the keys protecting their data, and that the key store is single-tenant and FIPS 140-2 Level 3 validated. What should the design specify?

A. Platform-managed keys
B. Customer-managed keys in the standard Key Vault tier
C. Azure Key Vault Managed HSM
D. Double encryption with platform-managed keys

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Managed HSM provides a single-tenant, FIPS 140-2 Level 3 validated HSM under customer control. Standard Key Vault is multi-tenant and validated at a lower level. Platform-managed keys give the customer no key control at all. Double encryption adds layers but does not satisfy the single-tenancy and validation requirements.
</details>

---

### Question 12
**Scenario:** A design must give a central SOC visibility into on-premises Windows servers, including vulnerability assessment and file integrity monitoring, with the least agent management.

A. Defender for Servers Plan 1 through Azure Arc
B. Defender for Servers Plan 2 through Azure Arc
C. Install Defender for Endpoint manually on each server
D. Forward Windows event logs to Sentinel only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Vulnerability assessment, file integrity monitoring, just-in-time VM access, and agentless scanning are Plan 2 capabilities. Plan 1 covers Defender for Endpoint integration but not those. Arc is the mechanism that brings non-Azure servers into scope and carries the agent, minimizing separate agent management. Log forwarding alone gives no endpoint protection.
</details>

---

### Question 13
**Scenario:** Which control should a design use to ensure that no resource in a management group can be created with a public IP address?

A. A Defender for Cloud recommendation
B. An Azure Policy assignment with a deny effect at the management group scope
C. An NSG rule
D. A Conditional Access policy

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** "Ensure" and "prevent" call for prevention rather than detection. Azure Policy deny stops the resource being created. A Defender for Cloud recommendation reports non-compliance after the fact. NSGs filter traffic, they do not prevent resource creation. Conditional Access governs sign-in conditions.
</details>

---

### Question 14
**Scenario:** An organization has Microsoft-only workloads, standard detection needs, no third-party log sources, and a strict cost constraint. What should the security operations design recommend?

A. Microsoft Sentinel with all connectors enabled
B. Microsoft Defender XDR alone, with Sentinel deferred until a third-party source or long retention is required
C. A third-party SIEM
D. Sentinel with Basic logs for every table

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Defender XDR provides correlated detection and response across the Microsoft estate with per-user or per-workload licensing rather than per-GB ingestion. Sentinel earns its cost when you need third-party sources, custom analytics, or long retention. Enabling all connectors is the classic cost mistake. Basic logs reduce cost but also reduce query capability and do not change the underlying question of whether a SIEM is needed.
</details>

---

### Question 15
**Scenario:** A design must let a single SOC team investigate incidents across two Entra tenants after an acquisition, without migrating identities. What should it use?

A. B2B guest accounts for every analyst
B. Azure Lighthouse delegated resource management
C. A second SOC team for the acquired tenant
D. Merging the tenants immediately

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Lighthouse provides cross-tenant delegated management so one team operates across both without identity migration or duplicated accounts. Guest accounts scale poorly and complicate privileged access. A second team duplicates cost. Tenant merger is a long project that does not answer the immediate operational need.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready. Focus remaining time on case study technique and reading for the constraint.
- **10-12 correct (65-80%):** Re-read the domain notes for your weak areas, especially Domain 2, which is 30-35% of the exam.
- **Below 10:** Work the [scenarios](../../exams/azure/sc-100/scenarios.md) and the Microsoft Cybersecurity Reference Architectures before retesting.

Remember that on SC-100 more than one option is usually technically valid. The qualifier in the question, such as "least administrative effort" or "without additional licensing", is what selects the answer.
