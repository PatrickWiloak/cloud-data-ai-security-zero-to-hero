---
last-updated: 2026-07-29
---

# CISM Domain 4 - Incident Management (30%)

Preparing for, responding to, and recovering from incidents, and the continuity planning
that surrounds them. Second-largest domain, and heavily scenario-based.

## Definitions

- **Event** - any observable occurrence. Most are routine.
- **Incident** - an event that adversely affects, or threatens, confidentiality, integrity, or availability.
- **Breach** - an incident resulting in confirmed unauthorized access to or disclosure of protected data. Breach usually triggers legal notification duties, which is why the distinction matters.
- **Disaster** - a disruption severe enough to invoke continuity and recovery plans.
- **Crisis** - an event threatening the organization's viability or reputation, requiring executive-level management.

## Incident response planning

- **Incident response plan (IRP)** - authority, roles, severity definitions, escalation, and communication.
- **Incident response team (IRT/CSIRT)** - the responders. Membership spans security, IT, legal, communications, HR, and business owners, because incidents are not purely technical.
- **Playbooks** - procedures per incident type: ransomware, business email compromise, data exfiltration, insider misuse.
- **Severity classification** - defined in advance so escalation is objective rather than negotiated during the event.
- **Escalation criteria** - thresholds triggering management or executive involvement.
- **Communication plan** - internal and external, including out-of-band channels, because the attacker may be reading corporate email.
- **Retainer arrangements** - pre-agreed forensic and legal support, negotiated before an incident rather than during one.

The manager's contribution is the plan, the authority, and the decisions. Preparing before
the incident is what the exam rewards.

## The response lifecycle

Aligned to NIST SP 800-61:

1. **Preparation** - plans, tooling, training, and exercises.
2. **Detection and analysis** - recognizing and validating the incident, and scoping it.
3. **Containment, eradication, and recovery** - limiting damage, removing the cause, restoring service.
4. **Post-incident activity** - lessons learned feeding back into preparation.

- **Triage** - validating and prioritizing. Separates real incidents from false positives.
- **Scoping** - determining full extent before eradication. Eradicating on partial scope means the attacker returns.
- **Containment strategy** - short-term to stop damage, long-term to allow business operation while eradication is prepared. Balance evidence preservation against speed.
- **Eradication** - removing malware, attacker accounts, persistence, and closing the entry vector.
- **Recovery** - restoring, validating, and monitoring closely on return to service.

## Evidence and forensics

- **Chain of custody** - documented handling record, without which evidence may be inadmissible.
- **Order of volatility** - collect the most perishable first: memory before disk.
- **Forensic image** - a bit-for-bit copy; analyze the copy.
- **Legal hold** - preservation directive overriding routine deletion.
- **When to involve law enforcement** - a business and legal decision with consequences for disclosure and control of the investigation. The security manager advises; executives and legal decide.

## Communication and notification

- **Internal notification** - management, affected business owners, and staff as appropriate.
- **Regulatory notification** - subject to statutory deadlines. GDPR requires notifying the supervisory authority within 72 hours of becoming aware of a qualifying personal data breach.
- **Customer notification** - often legally required, and always a reputational decision.
- **Public relations** - owned by communications, informed by security. Security does not brief the press.
- **Notification triggers** - defined in advance, so the decision is not improvised under pressure.

Never speculate publicly about cause or scope before it is established. Retracted
statements damage credibility more than an initial "investigation ongoing."

## Business continuity and disaster recovery

- **Business impact analysis (BIA)** - identifies critical processes, dependencies, and impact over time. The first step, and the input to everything else.
- **RTO (Recovery Time Objective)** - maximum tolerable restoration time.
- **RPO (Recovery Point Objective)** - maximum tolerable data loss. Drives backup frequency.
- **MTD / MTO** - maximum tolerable downtime before the consequences become unsurvivable.
- **SDO (Service Delivery Objective)** - the service level required while operating in recovery mode.
- **Business continuity plan (BCP)** - keeping business processes running.
- **Disaster recovery plan (DRP)** - restoring IT services; a component of the BCP.

**Recovery sites** - hot (ready in hours, highest cost), warm (days), cold (weeks, lowest
cost), mobile, and reciprocal agreements (cheap but rarely enforceable or testable).

## Testing and exercises

- **Checklist review** - least disruptive, least assurance.
- **Structured walkthrough / tabletop** - discussion-based, finds process gaps cheaply.
- **Simulation** - realistic role-play without production impact.
- **Parallel test** - recovery environment runs alongside production and results are compared.
- **Full interruption test** - production is stopped. Highest assurance, highest risk, requires executive approval.

Plans that are never tested fail when used. Testing frequency and after material change
are both expected.

## Post-incident

- **Lessons learned review** - conducted promptly, blameless, with owners and dates for each action.
- **Root cause analysis** - why it was possible, not merely what happened.
- **Plan updates** - the review's output must change the plan, or the exercise was theater.
- **Metrics** - mean time to detect, mean time to respond, mean time to recover, and incident recurrence.

## Exam pointers

- Containment precedes eradication; eradication precedes recovery. Sequence questions are common.
- The security manager coordinates and advises; executives make business decisions such as public disclosure and law enforcement involvement.
- BIA is always the first step in continuity planning.
- RPO drives backup frequency; RTO drives recovery capability.
- An untested plan provides no assurance.
- A breach is an incident with confirmed unauthorized data access, and that distinction usually triggers notification obligations.

## Official documentation

**[📖 ISACA CISM exam content outline](https://www.isaca.org/credentialing/cism)** - authoritative domain list
**[📖 NIST SP 800-61r2](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)** - incident handling guide
**[📖 ISO 22301](https://www.iso.org/standard/75106.html)** - business continuity management
**[📖 GDPR Article 33](https://gdpr-info.eu/art-33-gdpr/)** - 72-hour breach notification
