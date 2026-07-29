---
last-updated: 2026-07-29
---

# CySA+ Domain 4 - Reporting and Communication (17%)

The smallest domain and the one technical candidates most often underprepare. It tests
whether you can turn findings into something a non-analyst can act on.

## Vulnerability management reporting

A report exists to drive a decision. Include:

- **Vulnerability and affected hosts** - what, and where.
- **Risk score** - CVSS adjusted for environment and exposure, not the raw base score.
- **Mitigation and recommendation** - the specific action, not "apply best practice."
- **Prioritization** - the order to work in, with the reasoning visible.
- **Affected business processes** - what breaks if this is exploited, and what breaks while you fix it.

**Metrics and key performance indicators**

- **Mean time to detect (MTTD)** - from compromise to discovery.
- **Mean time to respond (MTTR)** - from discovery to containment or resolution.
- **Mean time to remediate** - from discovery to the vulnerability actually being fixed.
- **Scan coverage** - percentage of known assets actually scanned. Low coverage invalidates every other metric.
- **Vulnerability recurrence rate** - the same finding returning, which indicates a process or imaging failure rather than a patching failure.
- **Service level objective (SLO)** - the agreed target, for example critical vulnerabilities remediated within 15 days.

**Compliance reports** demonstrate that required controls operate. They serve auditors and
regulators, and answer a different question from an operational report: not "what should we
fix" but "can we evidence that the control worked throughout the period."

## Incident reporting and communication

- **Stakeholder identification** - knowing who needs to be told before the incident, not during it.
- **Escalation** - moving an incident to a higher authority when severity, scope, or required decisions exceed the responder's mandate.
- **Incident declaration** - the formal statement that this is an incident, which starts clocks and mandates.
- **Legal and regulatory reporting** - many regimes impose deadlines. GDPR requires notification to the supervisory authority within 72 hours of becoming aware of a qualifying personal data breach. Sector rules differ; know that deadlines exist and are short.
- **Law enforcement involvement** - a decision with consequences for evidence handling and disclosure timing.
- **Public relations and customer communication** - typically owned by communications and legal, informed by security.

**Adjust the message to the audience**

| Audience | What they need |
|---|---|
| Executive leadership | Business impact, decisions required, cost, timeline |
| Technical teams | IoCs, affected systems, precise remediation steps |
| Legal and compliance | Data types involved, regulatory exposure, evidence status |
| Customers and public | Plain-language impact and what they should do |
| Regulators | Facts against the required reporting template, within deadline |

Writing one report for all of them satisfies none of them.

## Root cause and lessons learned communication

- **Lessons learned report** - what happened, why it was possible, what changes, who owns each change, by when. Without owners and dates it is a diary, not a corrective action plan.
- **Blameless culture** - separating the system failure from individual conduct. Blame drives reporting underground and lengthens future detection times.
- **Change control follow-through** - improvements that are not tracked in the normal change process do not happen.

## Inhibitors to remediation, restated for reporting

These belong in the report so decision-makers see the real constraint:

- **Memorandum of understanding (MOU)** and **service level agreement (SLA)** obligations
- **Business process interruption** and **degrading functionality**
- **Legacy systems** and **proprietary systems** that cannot be patched
- **Organizational governance** and required approvals

Reporting an unremediated critical vulnerability without the inhibitor makes the security
team look ineffective; reporting it with the inhibitor turns it into a business decision
with a named owner.

## Ticketing and workflow

- **Ticketing system** - the system of record. If work is not ticketed, it cannot be measured or audited.
- **Automation of enrichment** - attaching asset owner, criticality, and threat context automatically so analysts spend time deciding rather than gathering.
- **Single pane of glass** - consolidating tool output so the ticket carries full context.

## Exam pointers

- Questions that name an audience are testing message-fit. Executives want impact and decisions; engineers want IoCs and steps.
- If a regulatory timeline appears, the answer usually involves notifying within the stated deadline, and 72 hours signals GDPR.
- Metrics questions: MTTD measures detection, MTTR measures response. Do not swap them.
- Recurring vulnerabilities point at a broken process or a stale gold image, not at lazy patching.
- Anything about improving future response points to lessons learned feeding back into preparation.

## Official documentation

**[📖 CompTIA CySA+ exam objectives](https://www.comptia.org/certifications/cybersecurity-analyst#examdetails)** - authoritative domain list
**[📖 NIST SP 800-61r2](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)** - includes reporting and coordination guidance
**[📖 GDPR Article 33](https://gdpr-info.eu/art-33-gdpr/)** - breach notification to the supervisory authority
