---
last-updated: 2026-08-09
difficulty: advanced
reading-time: 7 min
---

# SC-100 Study Plan

An 8-week schedule assuming 6-8 hours per week and that you already hold one of the prerequisite certifications. If you are coming straight from AZ-500 with no SC-200 or SC-300 background, add two weeks to Domain 2.

## Week 1: Frameworks and strategy

- [ ] Read the [SC-100 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100) end to end and note every verb ("design", "recommend", "evaluate")
- [ ] Work through the Microsoft Cybersecurity Reference Architectures, one diagram at a time
- [ ] Study Zero Trust principles and be able to state all three from memory
- [ ] Read the Cloud Adoption Framework Secure methodology
- [ ] Review the Well-Architected Framework security pillar and its trade-offs
- [ ] Review Notes: `notes/01-security-strategy-and-frameworks.md`

## Week 2: Resiliency, compliance, and landing zones

- [ ] Study ransomware resiliency design: immutable backup, isolated recovery, blast radius
- [ ] Map business continuity requirements (RTO, RPO) onto Azure services
- [ ] Study Microsoft Cloud Security Benchmark structure and how it maps to other frameworks
- [ ] Learn Purview Compliance Manager: assessments, improvement actions, scoring
- [ ] Study Azure landing zone security design and management group hierarchy
- [ ] Practice: given a regulatory requirement, name the Azure control that satisfies it

## Week 3: Identity architecture

- [ ] Entra ID tenant design: single vs multi-tenant, B2B, B2C, external identities
- [ ] Hybrid identity: password hash sync, pass-through authentication, federation, and when each fits
- [ ] Conditional Access design: signals, controls, exclusions, break-glass accounts
- [ ] Identity Protection risk policies and how they feed Conditional Access
- [ ] Privileged Identity Management: eligible vs active, approval, access reviews
- [ ] Enterprise access model and privileged access workstations
- [ ] Review Notes: `notes/02-security-operations-identity-compliance.md`

## Week 4: Security operations

- [ ] Sentinel architecture: workspace strategy, multi-tenant, data connectors, cost drivers
- [ ] Analytics rules, incidents, and automation with playbooks
- [ ] Defender XDR: unified incidents, investigation, and cross-workload correlation
- [ ] Threat intelligence integration and threat hunting design
- [ ] Logging and retention strategy: what to keep hot, what to archive
- [ ] Practice: design a SOC workflow for a 500-person company and for a 50,000-person company. Note what changes

## Week 5: Infrastructure security

- [ ] Defender for Cloud: secure score, CSPM vs workload plans, per-resource coverage
- [ ] Regulatory compliance dashboard and initiative assignment
- [ ] Azure Arc for hybrid servers and Kubernetes; AWS and GCP connectors
- [ ] Network segmentation: hub-and-spoke, Virtual WAN, NSGs, ASGs, Azure Firewall tiers
- [ ] Private Link and private endpoint DNS design
- [ ] Ingress protection: Application Gateway WAF, Front Door, DDoS Protection tiers
- [ ] Review Notes: `notes/03-infrastructure-security-design.md`

## Week 6: Application and data security

- [ ] Workload identities and managed identities; app registration governance
- [ ] Secure DevOps: GitHub Advanced Security, Defender for DevOps, secret scanning
- [ ] API security: API Management policies, Defender for APIs
- [ ] Purview: data map, classification, sensitivity labels, label policies
- [ ] DLP design across endpoint, service, and AI surfaces
- [ ] Encryption: platform-managed vs customer-managed keys, Managed HSM, double encryption
- [ ] Database protections: TDE, Always Encrypted, dynamic data masking, row-level security
- [ ] Review Notes: `notes/04-application-and-data-security.md`

## Week 7: Integration and case studies

- [ ] Work every scenario in [scenarios.md](./scenarios.md) without looking at the solution first
- [ ] Practice case-study technique: build a requirements table before answering any question
- [ ] Take a full-length timed practice exam
- [ ] For every wrong answer, write down which constraint you missed, not just the right answer
- [ ] Re-read MCRA with your weak areas in mind

## Week 8: Consolidation

- [ ] Second full-length timed practice exam
- [ ] Review the service cheat sheet in the [fact sheet](./fact-sheet.md) until each row is automatic
- [ ] Drill the decision pairs: Private Link vs service endpoint, CSPM vs CWP, sensitivity label vs DLP, PIM vs Conditional Access
- [ ] Skim the official study guide one final time, checking nothing is unfamiliar
- [ ] Light review the day before. Do not learn new material

## Readiness check

You are ready when you can, without notes:

- [ ] State the three Zero Trust principles and give an Azure control for each
- [ ] Draw the enterprise access model tiers
- [ ] Explain when Private Link is required rather than a service endpoint
- [ ] Name which Defender for Cloud plan protects a given resource type
- [ ] Describe a Sentinel workspace design for a multi-region, multi-subscription estate and justify the cost trade-off
- [ ] Distinguish a Purview sensitivity label from a DLP policy and say when you need both
- [ ] Choose between customer-managed keys and Managed HSM given a compliance requirement
