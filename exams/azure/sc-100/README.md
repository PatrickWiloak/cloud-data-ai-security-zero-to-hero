---
last-updated: 2026-08-09
difficulty: advanced
reading-time: 8 min
---

# Microsoft Cybersecurity Architect (SC-100)

The capstone of the Microsoft security certification track. SC-100 asks you to design an end-to-end security posture across identity, operations, infrastructure, applications, and data, under real business constraints.

It is an expert-level exam with a hard gate: you must already hold **SC-200**, **SC-300**, **AZ-500**, or **MS-102** before the certification is awarded. You can sit and pass SC-100 first, but the badge is withheld until a prerequisite is in place.

## Exam Details

- **Exam Code:** SC-100
- **Level:** Expert
- **Duration:** 120 minutes
- **Questions:** Typically 40-60, including case studies
- **Passing Score:** 700/1000
- **Cost:** USD 165, varies by region
- **Prerequisites:** SC-200, SC-300, AZ-500, or MS-102
- **Validity:** 1 year, free online renewal

See the [fact sheet](./fact-sheet.md) for the full breakdown and official links.

## Domains

| Domain | Weight | Notes |
|--------|-------:|-------|
| Design solutions that align with security best practices and priorities | 20-25% | [01](./notes/01-security-strategy-and-frameworks.md) |
| Design security operations, identity, and compliance capabilities | 30-35% | [02](./notes/02-security-operations-identity-compliance.md) |
| Design security solutions for infrastructure | 20-25% | [03](./notes/03-infrastructure-security-design.md) |
| Design security solutions for applications and data | 20-25% | [04](./notes/04-application-and-data-security.md) |

## How to approach it

This is a design exam. The questions give you a scenario and several architectures that would all work; you pick the one that best matches the stated constraint.

Practical reading technique: **find the constraint before you read the options.** The stem almost always contains a qualifier that eliminates three answers, and it is usually one of:

- "with the least administrative effort"
- "with the least privilege"
- "without additional licensing"
- "the solution must minimize cost"
- "must meet [regulatory framework] requirements"
- "must not require changes to the application"

Two answers will be technically correct. Only one satisfies the qualifier.

## Study sequence

1. **Frameworks first.** MCRA, Zero Trust, Cloud Adoption Framework Secure, Well-Architected security pillar. These give you the language the rest of the exam uses.
2. **Domain 2 next.** It is the largest and covers identity plus security operations, the two areas that appear inside other domains' questions.
3. **Infrastructure and data.** Defender for Cloud, network segmentation, Purview, encryption and key management.
4. **Case study practice.** Long multi-question scenarios are a distinct skill. Practice reading requirements into a table before answering.

Detailed schedule in the [practice plan](./practice-plan.md); technique in [strategy](./strategy.md).

## Prior knowledge that helps most

- Conditional Access design, including what a policy cannot do
- The difference between CSPM and workload protection in Defender for Cloud
- When Private Link is required rather than a service endpoint
- Sentinel workspace and cost design
- Purview sensitivity labels versus DLP policies
- Which Defender plan covers which resource type

If any of those are unfamiliar, work [AZ-500](../az-500/) material first. SC-100 assumes the implementation knowledge and tests the design decision on top of it.

## Study resources

- **[📖 SC-100 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100)** - authoritative outline
- **[📖 Microsoft Cybersecurity Reference Architectures](https://learn.microsoft.com/en-us/security/adoption/mcra)** - the diagrams this exam thinks in
- **[📖 Zero Trust deployment plans](https://learn.microsoft.com/en-us/security/zero-trust/deploy/overview)** - applied Zero Trust
- **[📖 Microsoft Learn SC-100 path](https://learn.microsoft.com/en-us/training/browse/?terms=SC-100)** - free official modules
- [Practice questions](../../../resources/practice-questions/azure-cybersecurity-architect-sc-100.md) - question bank in this repo

## Related

- [SC-300 Identity and Access Administrator](../sc-300/) - prerequisite path, identity depth
- [SC-401 Information Security Administrator](../sc-401/) - Purview data protection depth
- [SC-200 Security Operations Analyst](../sc-200/) - prerequisite path, Sentinel and Defender depth
- [AZ-500 Azure Security Engineer](../az-500/) - implementation layer
- [Security Engineer roadmap](../../../resources/certification-roadmap-security-engineer.md)
- [Zero trust architecture](../../../resources/architecture-patterns/zero-trust-architecture.md)
