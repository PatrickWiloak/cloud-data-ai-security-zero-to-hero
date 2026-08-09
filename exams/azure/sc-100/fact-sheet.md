---
last-updated: 2026-08-09
difficulty: advanced
reading-time: 15 min
---

# Microsoft Cybersecurity Architect (SC-100) Fact Sheet

## Exam Overview

**Exam Code:** SC-100
**Exam Name:** Microsoft Cybersecurity Architect
**Level:** Expert
**Duration:** 120 minutes
**Format:** Multiple choice, multiple select, case studies, drag-and-drop, and yes/no series questions
**Questions:** Typically 40-60
**Passing Score:** 700 out of 1000
**Cost:** USD 165 (varies by country)
**Valid For:** 1 year, renewable free online through Microsoft Learn
**Delivery:** Pearson VUE, test center or online proctored
**Prerequisites:** One of SC-200, SC-300, AZ-500, or MS-102 must be held to earn the certification

> **Verify before booking.** Microsoft revises skills-measured documents on a rolling basis and prices vary by region. Confirm the current outline, price, and prerequisite list on the official page below before you build a study schedule around this sheet.

**[📖 SC-100 certification page](https://learn.microsoft.com/en-us/credentials/certifications/cybersecurity-architect-expert/)** - registration, prerequisites, and renewal
**[📖 SC-100 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100)** - the authoritative skills-measured outline
**[📖 Exam readiness zone: SC-100](https://learn.microsoft.com/en-us/shows/exam-readiness-zone/)** - Microsoft's four-part video walkthrough

## What makes this exam different

SC-100 is a design exam, not a configuration exam. You are not asked which blade to click. You are given a business context, existing estate, regulatory pressure, and a set of constraints, then asked which architecture best satisfies them.

Three consequences for how you prepare:

1. **Breadth over depth.** You need working knowledge of Entra ID, Defender XDR, Defender for Cloud, Sentinel, Purview, Azure networking, and Azure Policy, plus how they fit together. You do not need to memorize PowerShell.
2. **The answers are all technically valid.** Selection is driven by the requirement in the stem: least privilege, lowest operational overhead, fastest to implement, minimum licensing, or regulatory fit. Read the constraint before reading the options.
3. **Frameworks matter.** The Microsoft Cybersecurity Reference Architectures (MCRA), the Cloud Adoption Framework's Secure methodology, the Well-Architected Framework security pillar, and Zero Trust principles are the vocabulary the exam thinks in.

## Target Audience

- Security architects designing across identity, data, applications, and infrastructure
- Senior security engineers moving from implementation into design
- Cloud architects who own security outcomes for an Azure or hybrid estate
- Consultants translating regulatory requirements into technical architecture

Microsoft's stated expectation is prior experience implementing or administering solutions in identity and access, platform protection, security operations, data security, and application security, plus hybrid and cloud implementations.

## Exam Domains

### Domain 1: Design solutions that align with security best practices and priorities (20-25%)

The strategy layer. Turning frameworks and business requirements into a defensible architecture.

**Key Concepts:**
- Resiliency strategy against ransomware and other attacks, including backup and restore design
- Business continuity and disaster recovery design as a security concern, not just an availability one
- Zero Trust strategy: verify explicitly, use least privilege, assume breach
- Microsoft Cybersecurity Reference Architectures (MCRA) and the Cloud Adoption Framework Secure methodology
- Well-Architected Framework security pillar trade-offs
- Cloud Security Benchmark as a control baseline
- Hybrid and multicloud strategy, including landing zone design

**[📖 Microsoft Cybersecurity Reference Architectures](https://learn.microsoft.com/en-us/security/adoption/mcra)** - the reference diagrams the exam is built on
**[📖 Cloud Adoption Framework: Secure](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/)** - security methodology
**[📖 Zero Trust guidance center](https://learn.microsoft.com/en-us/security/zero-trust/)** - principles and deployment plans

### Domain 2: Design security operations, identity, and compliance capabilities (30-35%)

The largest domain, and the one that most often decides a pass.

**Key Concepts:**
- Logging and auditing strategy, including which signals to centralize and retention design
- SIEM and SOAR design with Microsoft Sentinel: workspace architecture, data connectors, analytics rules, cost management
- Extended detection and response with Defender XDR across endpoint, identity, email, and cloud apps
- Security operations workflow: incident triage, automation, threat hunting, and threat intelligence
- Identity architecture: Entra ID tenants, external identities, B2B and B2C, hybrid identity with Entra Connect
- Conditional Access as the policy engine: signals, controls, and design for least disruption
- Privileged access strategy: Privileged Identity Management, privileged access workstations, the enterprise access model and tiering
- Entra ID Governance: entitlement management, access reviews, lifecycle workflows
- Regulatory compliance design with Purview Compliance Manager, Azure Policy, and initiative assignment

**[📖 Microsoft Sentinel documentation](https://learn.microsoft.com/en-us/azure/sentinel/)** - SIEM architecture and operations
**[📖 Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/)** - cross-domain detection and response
**[📖 Privileged access strategy](https://learn.microsoft.com/en-us/security/privileged-access-workstations/privileged-access-strategy)** - the enterprise access model

### Domain 3: Design security solutions for infrastructure (20-25%)

**Key Concepts:**
- Posture management with Microsoft Defender for Cloud: secure score, regulatory compliance dashboard, and recommendations
- Defender for Cloud plans by workload: servers, containers, storage, SQL, App Service, key vault, APIs
- Cloud Security Posture Management (CSPM) and Cloud Workload Protection (CWP), and when each applies
- Hybrid and multicloud connection through Azure Arc, and AWS and GCP connectors
- Endpoint security design, including Defender for Endpoint and device compliance through Intune
- Network segmentation design: hub-and-spoke, Virtual WAN, Azure Firewall, network security groups, and application security groups
- Private connectivity: Private Link, private endpoints, service endpoints, and DNS design that supports them
- Ingress protection: Application Gateway with WAF, Front Door, DDoS Protection
- OT and IoT security considerations with Defender for IoT
- Server hardening baselines and update management

**[📖 Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/)** - CSPM and workload protection
**[📖 Azure network security](https://learn.microsoft.com/en-us/azure/networking/security/)** - segmentation and perimeter design
**[📖 Azure Arc](https://learn.microsoft.com/en-us/azure/azure-arc/)** - extending governance to hybrid and multicloud

### Domain 4: Design security solutions for applications and data (20-25%)

**Key Concepts:**
- Securing application onboarding: workload identities, managed identities, and app registration governance
- Application lifecycle security: secure DevOps, GitHub Advanced Security, Defender for DevOps, secret scanning
- API security design, including Azure API Management policies and Defender for APIs
- Data classification and protection with Microsoft Purview: sensitivity labels, data map, DSPM
- Data loss prevention design across endpoints, services, and AI applications
- Encryption strategy: platform-managed keys, customer-managed keys, Managed HSM, and double encryption
- Key, secret, and certificate management with Azure Key Vault, including rotation and access model
- Database security: Always Encrypted, dynamic data masking, row-level security, transparent data encryption
- Securing AI workloads: Azure AI Content Safety, DSPM for AI, and governance of Copilot data access

**[📖 Microsoft Purview](https://learn.microsoft.com/en-us/purview/)** - data governance, classification, and DLP
**[📖 Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/)** - key and secret management
**[📖 Security in Azure AI](https://learn.microsoft.com/en-us/azure/ai-services/security-features)** - AI workload protection

## Service cheat sheet

| Need | Service | Notes |
|------|---------|-------|
| SIEM and SOAR | Microsoft Sentinel | Log Analytics workspace underneath; cost is driven by ingestion |
| XDR across endpoint, identity, email, apps | Defender XDR | Unified incident view, one investigation surface |
| Cloud posture and workload protection | Defender for Cloud | Free CSPM plus paid plans per workload |
| Identity | Microsoft Entra ID | Conditional Access, PIM, Identity Protection, Governance |
| Data governance, classification, DLP | Microsoft Purview | Sensitivity labels, Compliance Manager, DSPM for AI |
| Secrets and keys | Azure Key Vault, Managed HSM | Managed HSM for FIPS 140-2 Level 3 and single tenancy |
| Policy and guardrails | Azure Policy, initiatives | Deny, audit, deployIfNotExists; assigned at management group |
| Hybrid and multicloud governance | Azure Arc, cloud connectors | Brings non-Azure resources into Defender and Policy |
| Perimeter | Azure Firewall, WAF, DDoS Protection | Firewall Premium adds TLS inspection and IDPS |
| Private access | Private Link, private endpoints | Requires a matching private DNS design |

## Renewal

Microsoft certifications are valid for one year and renew free through an unproctored online assessment on Microsoft Learn, available in the six months before expiry. Renewal is shorter than the exam and open book, but it does test updated content.

## Related repo material

- [Notes](./notes/) - four notes, one per domain
- [Practice plan](./practice-plan.md) - 8-week schedule
- [Scenarios](./scenarios.md) - design scenarios in exam shape
- [Strategy](./strategy.md) - how to study and how to take the exam
- [AZ-500](../az-500/) - the implementation-level Azure security exam
- [SC-200](../sc-200/) - security operations, a prerequisite path
- [SC-300](../sc-300/) - identity and access, a prerequisite path
- [Zero trust architecture](../../../resources/architecture-patterns/zero-trust-architecture.md)
- [AI security](../../../resources/ai-security/) - securing the AI workloads Domain 4 now touches
