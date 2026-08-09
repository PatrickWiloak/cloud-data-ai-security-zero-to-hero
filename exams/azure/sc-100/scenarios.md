---
last-updated: 2026-08-09
difficulty: advanced
reading-time: 14 min
---

# SC-100 High-Yield Design Scenarios

Design problems in the shape SC-100 uses. Work each one before reading the solution, and pay attention to the constraint line. In every case, more than one option would function; only one satisfies the stated requirement.

---

## Scenario 1: Ransomware resiliency

**Scenario**: A manufacturer runs 400 VMs in Azure and 150 on-premises. A peer was hit by ransomware that encrypted both production and the backup repository, because the backup service account was domain-joined and compromised alongside everything else. The CISO wants a design that survives the same attack. Cost is a secondary concern; recovery certainty is primary.

**Solution Pattern**:
- Azure Backup with a **Recovery Services vault protected by immutability** and soft delete, so backups cannot be deleted or altered within the retention window even by a vault administrator
- **Multi-user authorization (MUA)** on the vault using a Resource Guard in a separate subscription and tenant boundary, so destructive operations need a second approver
- Backup identity separated from the production domain: the backup control plane is Azure, not domain-joined infrastructure
- Azure Arc to bring the 150 on-premises servers into the same backup and Defender for Cloud coverage
- Isolated recovery environment defined in advance, with a tested restore runbook and documented RTO/RPO
- Defender for Servers for detection, plus Sentinel analytics rules for mass-encryption behavior

**Common Distractors**:
- Geo-redundant storage alone (protects against regional failure, not against authorized deletion)
- More frequent backups (increases recovery points, does nothing if the repository itself is reachable)
- A second backup product (adds cost and operational surface without addressing the identity compromise)

**Key Takeaway**: Ransomware resiliency is an identity and immutability problem, not a backup frequency problem. The exam wants immutable vaults plus multi-user authorization plus separation of the backup identity from the production identity plane.

---

## Scenario 2: Choosing the identity access control

**Scenario**: A financial services company needs three things: engineers must not hold standing subscription Owner rights; contractors must be reviewed quarterly and removed automatically if not recertified; and sign-ins from unmanaged devices must be blocked for finance applications. The solution must use existing Entra ID P2 licensing and minimize administrative effort.

**Solution Pattern**:
- **Privileged Identity Management** for the standing-rights problem: Owner becomes an eligible assignment with just-in-time activation, approval, and time limits
- **Entra ID Governance access reviews** (with entitlement management access packages) for the contractor lifecycle: quarterly review, auto-remove on no response
- **Conditional Access** with a device filter requiring compliant or hybrid-joined devices for the finance application group

**Common Distractors**:
- Using Conditional Access for the privileged access problem (Conditional Access governs authentication conditions, not standing role assignment)
- Using PIM for contractor recertification (PIM covers privileged roles, not general application entitlement)
- Using group membership scripts (works, but "minimize administrative effort" rules it out against a native governance feature)

**Key Takeaway**: Three adjacent identity features solving three distinct problems. PIM governs privileged role activation, access reviews govern entitlement over time, Conditional Access governs the conditions of a sign-in. Exam distractors deliberately swap them.

---

## Scenario 3: Sentinel workspace design and cost

**Scenario**: A retailer has 12 subscriptions across three regions and two Entra tenants after an acquisition. The SOC is a single central team. Regulatory requirements mean EU log data must remain in EU regions. Leadership has flagged that the current logging bill is unsustainable.

**Solution Pattern**:
- **One Sentinel workspace per data residency boundary**: an EU workspace and a non-EU workspace, not one per subscription
- **Cross-workspace queries** and Microsoft Sentinel workspace manager so the single SOC team investigates across both
- **Azure Lighthouse** for cross-tenant access, so the acquired tenant is visible without migrating identities first
- Cost control through **table-level retention**, moving verbose tables to Auxiliary or Basic logs, and archiving beyond the interactive retention window
- Data connector review: ingest what analytics rules actually use, not everything available

**Common Distractors**:
- A single global workspace (violates EU data residency)
- One workspace per subscription (12 workspaces, high cost, fragmented investigation)
- Migrating the acquired tenant first (large project; Lighthouse achieves the operational goal now)

**Key Takeaway**: Workspace count is driven by data residency and tenancy, not by subscription count. Cost is driven by ingestion volume and retention tier, so the design lever is which tables you ingest and how long you keep them hot.

---

## Scenario 4: Private connectivity to PaaS

**Scenario**: An insurer must ensure that traffic from application VMs to Azure Storage and Azure SQL never traverses the public internet, that the storage account is unreachable from any other network, and that on-premises systems connected over ExpressRoute can reach the same storage account privately.

**Solution Pattern**:
- **Private endpoints** on both the storage account and Azure SQL, giving each a private IP inside the VNet
- Public network access **disabled** on the storage account, so the only path is the private endpoint
- **Private DNS zones** (`privatelink.blob.core.windows.net`, `privatelink.database.windows.net`) linked to the VNet, with conditional forwarders from on-premises DNS so ExpressRoute clients resolve to the private IP
- Network security groups and Azure Firewall for east-west control

**Common Distractors**:
- Service endpoints (keep traffic on the Microsoft backbone but the resource keeps a public IP and remains reachable from other permitted VNets; they also do not extend to on-premises)
- Storage firewall IP allowlisting (does not satisfy "never traverses the public internet")
- Both a service endpoint and a private endpoint (redundant, and the DNS behavior becomes confusing)

**Key Takeaway**: When the requirement includes on-premises access or "must not be publicly reachable", the answer is a private endpoint plus private DNS. Service endpoints are for VNet-only scenarios where a public IP on the resource is acceptable. DNS is where private endpoint designs fail in practice, so the DNS component is usually part of the correct answer.

---

## Scenario 5: Multicloud posture management

**Scenario**: An organization runs workloads in Azure, AWS, and GCP, plus VMware on-premises. Security leadership wants one place to see misconfigurations, one compliance report covering all environments against ISO 27001, and runtime threat detection on the servers. Minimal agent sprawl is a stated requirement.

**Solution Pattern**:
- **Defender for Cloud** as the single posture plane, with the native **AWS and GCP connectors** for agentless CSPM
- **Azure Arc** for the VMware servers, bringing them in as Arc-enabled servers
- **Defender for Servers Plan 2** for runtime protection, which deploys Defender for Endpoint through Arc rather than a separate agent stack
- **Regulatory compliance dashboard** with the ISO 27001 initiative applied across all connected environments
- Findings routed into Sentinel for incident workflow

**Common Distractors**:
- A third-party CSPM tool (works, but adds a product where the native connectors satisfy the requirement)
- Deploying Defender for Endpoint independently on each server (more agent management, contradicting the constraint)
- Separate compliance reporting per cloud (fails "one compliance report")

**Key Takeaway**: Defender for Cloud plus Arc plus cloud connectors is the standard SC-100 answer for multicloud posture. Arc is the mechanism for anything not natively in Azure, and it also carries the Defender agent, which is why it satisfies the agent-sprawl constraint.

---

## Scenario 6: Protecting data used by an AI assistant

**Scenario**: A company is rolling out an internal AI assistant over SharePoint and OneDrive content. Legal is concerned that employees will surface documents they should not see, and that sensitive documents will be summarized into new files with no protection. The solution must not require reclassifying the entire document estate by hand.

**Solution Pattern**:
- **Microsoft Purview sensitivity labels** with **auto-labeling** policies driven by trainable classifiers and sensitive information types, so classification scales without manual review
- **Label inheritance** so AI-generated content derived from labeled source material carries the label forward
- **DLP policies** extended to AI interactions, blocking sensitive content from leaving through the assistant
- **DSPM for AI** in Purview to see which sensitive data AI interactions actually touch
- Fix the underlying permissions: the assistant honors existing access, so oversharing in SharePoint becomes oversharing in the assistant. Run SharePoint Advanced Management access reviews and site access controls first
- Audit AI interactions through Purview Audit

**Common Distractors**:
- Blocking the assistant from all sites containing sensitive data (defeats the deployment)
- Manual classification (fails the stated constraint)
- Relying on the assistant's own filtering (it enforces existing permissions; it does not fix them)

**Key Takeaway**: An AI assistant is a permissions amplifier. The design answer is auto-labeling plus DLP plus fixing oversharing at the source, not restricting the assistant. This area of the exam has grown as Purview DSPM for AI has matured.

---

## Scenario 7: Hybrid identity method selection

**Scenario**: A hospital group must keep on-premises Active Directory authoritative, needs sign-in to continue working for cloud apps if the on-premises datacenter is unreachable, and has a compliance requirement that password hashes must not be stored in the cloud in any form.

**Solution Pattern**:
- **Pass-through authentication (PTA)** with multiple connectors for redundancy, since no password hash is stored in Entra ID
- **Seamless SSO** for user experience
- Recognize the tension: PTA depends on on-premises connectors, so a full datacenter outage breaks sign-in. Resolving it requires either accepting the risk with geographically separated connectors, or renegotiating the hash-storage requirement in favor of password hash sync
- Break-glass cloud-only accounts excluded from Conditional Access, stored securely

**Common Distractors**:
- Password hash sync (the simplest and most resilient option, but explicitly excluded by the compliance constraint)
- AD FS (meets the constraint but adds substantial infrastructure and is the option Microsoft guidance moves customers away from)
- Cloud-only identities (loses on-premises authority)

**Key Takeaway**: Hybrid identity questions hinge on a constraint that eliminates the default. Password hash sync is Microsoft's recommended answer unless something forbids it. When resilience and hash-storage requirements conflict, the exam expects you to name the conflict rather than pretend one option satisfies both.

---

## Scenario 8: Segmentation for a regulated workload

**Scenario**: A payments company must isolate its cardholder data environment from the rest of its Azure estate, inspect all traffic between the two including TLS-encrypted flows, prevent CDE workloads from reaching the internet directly, and produce evidence for a PCI DSS assessment.

**Solution Pattern**:
- **Hub-and-spoke** with the CDE in a dedicated spoke, and a separate subscription and management group so policy and RBAC boundaries align with the compliance boundary
- **Azure Firewall Premium** in the hub for **TLS inspection** and IDPS, with forced tunneling so no spoke has a direct internet route
- **NSGs and application security groups** for intra-spoke micro-segmentation
- **Azure Policy** initiative assigned at the CDE management group, denying public IPs and non-compliant resource types
- **Defender for Cloud** regulatory compliance dashboard with the PCI DSS initiative for assessment evidence
- Diagnostic logs to a dedicated workspace with retention meeting the assessment requirement

**Common Distractors**:
- Azure Firewall Standard (no TLS inspection or IDPS, so it fails the inspection requirement)
- NSGs alone (no layer 7 inspection, no logging depth for assessment)
- A single subscription with resource groups as the boundary (does not give a clean policy or RBAC boundary and complicates scoping the assessment)

**Key Takeaway**: Compliance boundaries should align with subscription and management group boundaries so that policy, RBAC, and audit scoping are clean. Premium tier is the discriminator whenever TLS inspection or IDPS appears in the requirements.

---

## Related

- [Practice plan](./practice-plan.md) - where these fit in the schedule
- [Strategy](./strategy.md) - reading technique for questions like these
- [Notes](./notes/) - the underlying material
- [Zero trust architecture](../../../resources/architecture-patterns/zero-trust-architecture.md)
- [Practice questions](../../../resources/practice-questions/azure-cybersecurity-architect-sc-100.md)
