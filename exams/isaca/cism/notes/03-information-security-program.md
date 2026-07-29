---
last-updated: 2026-07-29
---

# CISM Domain 3 - Information Security Program (33%)

The largest domain. Building and running the program that delivers the strategy:
resources, architecture, controls, awareness, and measurement.

## Program foundations

- **Information security program** - the coordinated set of activities, resources, and controls that execute the security strategy.
- **Program objectives** - derived from the strategy, expressed as outcomes and measurable.
- **Program charter** - authority, scope, and mandate.
- **Program roadmap** - sequenced initiatives with dependencies and resourcing.
- **Program resources** - people, process, technology, and budget. Under-resourcing is a risk to be reported, not absorbed silently.

A program is not a collection of tools. The exam consistently prefers answers about
process, ownership, and measurement over answers about buying technology.

## Security architecture

- **Security architecture** - the structural design translating requirements into a coherent set of controls, so protections work together rather than as isolated point solutions.
- **Defense in depth** - layered, independent controls.
- **Zero trust** - no implicit trust from network location; verify explicitly, least privilege, assume breach. See [zero trust architecture](../../../../resources/architecture-patterns/zero-trust-architecture.md).
- **Segmentation** - limits blast radius and reduces compliance scope.
- **Secure by design and secure by default** - controls built in from the start, with safe default settings.
- **Baselines and hardening standards** - the minimum configuration for a system class, benchmarked against sources such as CIS.

## Control implementation

- **Preventive, detective, corrective, deterrent, compensating, recovery** - know the function of each and be able to classify a described control.
- **Administrative, technical, physical** - the three natures.
- **Control ownership** - each control has an owner responsible for its operation.
- **Control effectiveness** - whether it achieves its objective, evidenced by testing rather than assumed from its existence.
- **Control gap** - the difference between required and implemented control state.

Implementing a control without assigning ownership and a means of testing effectiveness
leaves you with the appearance of control, which is worse than a known gap.

## Identity and access management

- **Provisioning lifecycle** - joiner, mover, leaver. The mover case (role change) is the one most often mishandled, leaving accumulated entitlements.
- **Privilege creep** - accumulated access from previous roles. Addressed by periodic recertification.
- **Least privilege and need to know** - minimum access for the role and task.
- **Privileged access management** - vaulting, session recording, just-in-time elevation.
- **Access recertification** - periodic review by the business owner.
- **Federation and SSO** - convenience and hygiene benefits, concentrated risk in the identity provider.

## Data protection

- **Data classification** - the basis for proportionate protection.
- **Data lifecycle controls** - protection appropriate at creation, storage, use, sharing, archival, and destruction.
- **Encryption at rest and in transit** - with key management as the real control. See [TLS and HTTPS](../../../../learn/concepts/tls-and-https.md).
- **Data loss prevention (DLP)** - detects and blocks unauthorized egress. Requires classification to be effective.
- **Tokenization and masking** - substituting sensitive values, particularly for non-production environments.
- **Secure disposal** - cryptographic erasure, degaussing, or physical destruction, evidenced by certificates.

## Third-party and supply chain

- **Due diligence** - assessing a vendor's security before contracting.
- **Contractual security requirements** - specific obligations, right to audit, breach notification timelines, and subcontractor restrictions.
- **Ongoing monitoring** - attestations, questionnaires, and performance against SLAs.
- **Fourth-party risk** - your vendor's vendors.
- **Exit strategy** - data return and deletion, and transition support.

## Awareness and training

- **Security awareness** - broad, ongoing, for everyone. Targets behavior, not knowledge alone.
- **Role-based training** - developers need secure coding, administrators need hardening, executives need decision context.
- **Phishing simulation** - measures and improves resistance. Results are used to educate, not to punish, or reporting rates collapse.
- **Effectiveness measurement** - measured by behavior change (reporting rates, click rates), not by attendance.

Attendance is an activity metric. The exam prefers outcome metrics.

## Program metrics and reporting

- **Operational metrics** - patch compliance, vulnerability ageing, incident volumes. For the security team.
- **Management metrics** - control effectiveness, risk trend, program progress. For executives.
- **Strategic metrics** - alignment, maturity, and risk posture against appetite. For the board.
- **Maturity model** - shows capability progression and the gap to target.
- **Benchmarking** - comparison against peers, useful for justifying investment.

Match the metric to the audience. Reporting firewall block counts to the board is a
classic wrong answer.

## Integration with business processes

- **Change management** - security assessment integrated into the change process, not bolted on afterwards.
- **SDLC integration** - security requirements defined at requirements stage, threat modeling at design, testing before release.
- **Project involvement** - the security manager engages at project initiation. Late engagement means expensive rework or accepted risk.
- **Procurement** - security requirements in the RFP, not discovered at implementation.
- **Mergers and acquisitions** - due diligence on the target's security posture before integration.

## Exam pointers

- The largest domain, so weight your study here.
- Prefer answers about ownership, process, and measurement over answers about purchasing technology.
- Awareness effectiveness is measured by behavior, not attendance.
- Security must be engaged at project initiation and at the requirements phase.
- A control without an owner and without effectiveness testing is not a functioning control.
- When asked what to do first in building a program, the answer usually traces back to the strategy and business requirements, not to a technical baseline.

## Official documentation

**[📖 ISACA CISM exam content outline](https://www.isaca.org/credentialing/cism)** - authoritative domain list
**[📖 NIST SP 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)** - control catalog
**[📖 ISO/IEC 27002](https://www.iso.org/standard/75652.html)** - information security controls guidance
