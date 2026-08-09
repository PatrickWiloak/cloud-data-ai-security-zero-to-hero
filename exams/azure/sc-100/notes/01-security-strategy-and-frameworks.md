---
last-updated: 2026-08-09
difficulty: advanced
reading-time: 12 min
---

# 01 - Security strategy and frameworks

**Domain 1: Design solutions that align with security best practices and priorities (20-25%)**

This domain is the strategy layer. It asks whether you can turn a business requirement into a defensible architecture, and whether you can name the framework that justifies it.

---

## Zero Trust

Three principles. Know them verbatim and know an Azure control for each.

| Principle | Meaning | Azure controls |
|---|---|---|
| **Verify explicitly** | Authenticate and authorize on all available signals: identity, device, location, service, data classification, anomalies | Conditional Access, Identity Protection, device compliance in Intune |
| **Use least privilege access** | Just-in-time and just-enough access, risk-based adaptive policy, data protection | PIM, entitlement management, RBAC, Azure Policy |
| **Assume breach** | Segment, encrypt end to end, use analytics to detect, drive improvement | Network segmentation, Defender XDR, Sentinel, micro-segmentation |

Zero Trust is applied across six pillars: identities, endpoints, applications, data, infrastructure, and networks. Exam scenarios often name a pillar implicitly, and the answer is the control for that pillar.

The important architectural consequence: **the network perimeter is no longer the primary control**. Identity is. When a question offers a network answer and an identity answer to an access problem, identity usually wins.

---

## Microsoft Cybersecurity Reference Architectures (MCRA)

MCRA is the set of reference diagrams the exam is built on. It covers the capability map across Microsoft security products, the attack chain coverage, and how the products relate.

What to take from it:

- Which product owns which surface. Defender for Endpoint owns devices, Defender for Identity owns on-premises AD signals, Defender for Office owns email and collaboration, Defender for Cloud Apps owns SaaS, Defender for Cloud owns cloud workloads.
- Where Sentinel sits relative to Defender XDR: XDR correlates within the Microsoft estate, Sentinel is the SIEM that adds third-party sources and long retention.
- The enterprise access model, which replaced the older tier model, and how privileged access flows through it.

---

## Cloud Adoption Framework and Well-Architected

**CAF Secure methodology** describes the security work across the adoption lifecycle: risk insights, security integration, business resilience, and the disciplines of access control, operations, asset protection, security governance, and innovation security.

**Well-Architected Framework security pillar** gives you the trade-off vocabulary. The exam uses phrases from it: defense in depth, blast radius reduction, segmentation, and the recognition that security trades against cost, performance, and operational simplicity.

**Azure landing zones** provide the structural answer to most "how should this be organized" questions: management group hierarchy, subscription per boundary, policy assigned at the management group, and platform subscriptions separated from application landing zones.

---

## Microsoft Cloud Security Benchmark

The Microsoft Cloud Security Benchmark (MCSB) is the control baseline built into Defender for Cloud's secure score. It maps to CIS Controls, NIST SP 800-53, and PCI DSS, which matters because it lets you answer "how do we evidence compliance with X" with "assign the corresponding initiative and use the regulatory compliance dashboard".

Control families cover network security, identity management, privileged access, data protection, asset management, logging and threat detection, incident response, posture and vulnerability management, endpoint security, backup and recovery, DevOps security, and governance.

---

## Resiliency and ransomware

Ransomware design questions are common and they follow a pattern. The right answer is rarely about detection alone.

The three pillars of a defensible answer:

1. **Prepare**: immutable, isolated backups with multi-user authorization; a tested recovery runbook; identified minimum viable business services.
2. **Limit blast radius**: privileged access separation, network segmentation, removing standing admin rights, tiering the administrative model.
3. **Detect and respond**: Defender for Endpoint and Defender for Servers for behavioral detection, Sentinel analytics for mass-encryption patterns, automated containment.

The specific Azure features that come up: Recovery Services vault **immutability**, **soft delete**, **multi-user authorization with Resource Guard**, and cross-region restore.

---

## Business continuity as a security concern

RTO and RPO are security requirements, not just availability ones, because an attacker who can destroy data creates an availability incident.

Map the requirement to the mechanism:

| Requirement | Mechanism |
|---|---|
| Minutes of RPO for a database | Active geo-replication or zone-redundant configuration |
| Hours of RTO for VMs | Azure Site Recovery with a tested failover plan |
| Protection against malicious deletion | Immutable vault, soft delete, MUA |
| Regional outage tolerance | Availability zones, then paired region |
| Preserving evidence for investigation | Snapshot before remediation, immutable log storage |

---

## Regulatory strategy

The design pattern for any "we must comply with X" question:

1. Assign the corresponding **Azure Policy initiative** at the right management group scope.
2. Use **Defender for Cloud's regulatory compliance dashboard** to show control state.
3. Use **Purview Compliance Manager** for the assessment workflow, improvement actions, and evidence collection.
4. Use **Azure Policy deny and deployIfNotExists** effects to prevent drift rather than detect it after the fact.

Prefer prevention to detection when the question mentions "ensure" or "prevent"; prefer detection and reporting when it mentions "identify" or "report".

---

## Key terms

- **Zero Trust** - a security model based on verifying explicitly, granting least privilege access, and assuming breach rather than trusting a network perimeter
- **MCRA** - Microsoft Cybersecurity Reference Architectures, the reference diagrams mapping Microsoft security capabilities to attack surfaces
- **Microsoft Cloud Security Benchmark** - Microsoft's control baseline in Defender for Cloud, mapped to CIS, NIST SP 800-53, and PCI DSS
- **Enterprise access model** - the successor to the AD tier model, organizing privileged access by control, management, and data planes
- **Blast radius** - the extent of damage a single compromise can cause, reduced through segmentation and privilege separation
- **Immutable vault** - a Recovery Services vault configuration preventing backup deletion or retention reduction within the retention period
- **Multi-user authorization** - a Recovery Services vault protection requiring a second approver, through a Resource Guard, for destructive operations
- **Landing zone** - a pre-provisioned, governed environment with policy, identity, networking, and monitoring already in place
- **Management group** - an Azure hierarchy scope above subscriptions where policy and RBAC are assigned for consistent governance
- **deployIfNotExists** - an Azure Policy effect that remediates non-compliant resources by deploying the missing configuration
- **RPO** - recovery point objective, the maximum acceptable data loss measured in time
- **RTO** - recovery time objective, the maximum acceptable time to restore service after an incident

---

## Related

- [Notes 02: security operations, identity, compliance](./02-security-operations-identity-compliance.md)
- [Scenarios](../scenarios.md) - scenarios 1, 7, and 8 exercise this domain
- [Zero trust architecture](../../../../resources/architecture-patterns/zero-trust-architecture.md)
- [Azure Well-Architected](../../../../resources/well-architected/azure-well-architected.md)
- [Disaster recovery patterns](../../../../resources/architecture-patterns/disaster-recovery-patterns.md)
