---
last-updated: 2026-07-29
---

# CISA Domain 1 - Information System Auditing Process (21%)

How an audit is planned, executed, and evidenced. ISACA tests the auditor's mindset:
independence, sufficient evidence, and conclusions that follow from what was tested.

## Audit standards and guidance

- **ITAF (Information Technology Assurance Framework)** - ISACA's framework of standards, guidelines, and tools for IS audit and assurance. Standards are mandatory; guidelines are advisory.
- **Code of Professional Ethics** - binding on CISA holders. Breaching it can cost the certification.
- **Due professional care** - applying the diligence a reasonably competent auditor would apply.
- **Independence** - freedom from relationships that impair objectivity. *Independence in appearance* matters as much as independence in fact.
- **Organizational independence** - the audit function reports to the audit committee or board, not to the management it audits.

If an exam scenario has an auditor reviewing a system they helped design, the answer
almost always involves impaired independence and reassignment.

## Types of audit

- **Compliance audit** - tests adherence to laws, regulations, or policy.
- **Financial audit** - accuracy of financial reporting.
- **Operational audit** - efficiency and effectiveness of operations.
- **Integrated audit** - combines financial and IS controls testing.
- **Forensic audit** - evidence gathering for suspected fraud or legal proceedings.
- **Attestation and SOC engagements** - third-party assurance over a service organization's controls.

## Risk-based audit planning

The audit universe cannot all be audited every year, so effort follows risk.

- **Audit universe** - the complete set of auditable entities.
- **Risk assessment** - ranks entities by inherent risk to allocate audit resources.
- **Inherent risk** - risk before any controls are applied.
- **Control risk** - risk that controls fail to prevent or detect a problem.
- **Detection risk** - risk that the auditor's procedures fail to find an existing problem.
- **Residual risk** - risk remaining after controls operate.
- **Materiality** - the threshold above which a misstatement or weakness would influence decisions. In IS audit, materiality is often expressed in terms of criticality and outage impact rather than money.

Audit risk is the combination of inherent, control, and detection risk. The auditor
controls only detection risk, by choosing procedures and sample sizes.

## Controls

- **Preventive control** - stops an event before it occurs, for example input validation or segregation of duties.
- **Detective control** - identifies an event after it occurs, for example log review or reconciliation.
- **Corrective control** - restores after an event, for example restoring from backup.
- **Compensating control** - an alternative where the preferred control is not feasible. Must address the same risk to an acceptable degree.
- **General controls (ITGC)** - apply across the IT environment: access management, change management, operations.
- **Application controls** - specific to one system: input, processing, and output controls.
- **Control objective** - what the control is meant to achieve. Testing without a stated objective produces findings nobody can act on.

## Evidence

- **Sufficient** - enough of it to support the conclusion.
- **Reliable** - the more independent the source, the more reliable. Evidence obtained directly by the auditor beats evidence supplied by the auditee.
- **Relevant** - relates to the control objective being tested.
- **Useful** - helps reach a conclusion.

Reliability ranking, strongest first: auditor-obtained, external third party, auditee
system-generated with strong ITGC, auditee-prepared, verbal representation.

**Evidence-gathering techniques**

- **Inquiry** - asking. Weakest form on its own, never sufficient alone.
- **Observation** - watching a process. Shows what happens while you watch, which is a limitation.
- **Inspection** - examining documents or configuration.
- **Reperformance** - the auditor independently executes the control. Strongest.
- **CAAT (Computer-Assisted Audit Technique)** - software to analyze whole populations rather than samples. Enables 100% testing.

## Sampling

- **Statistical sampling** - each item has a known probability of selection, so results can be projected to the population with a measurable confidence level.
- **Non-statistical (judgmental) sampling** - auditor judgment selects items; results cannot be statistically projected.
- **Attribute sampling** - tests whether a control operated or not, giving a rate of deviation. The usual choice for compliance testing.
- **Variable sampling** - tests monetary or numeric amounts. Used in substantive testing.
- **Stop-or-go sampling** - stops early when results are clearly acceptable, minimizing sample size.
- **Discovery sampling** - designed to find at least one instance of a rare but critical condition, such as fraud.
- **Confidence coefficient, tolerable error, and expected error** - drive sample size. Higher confidence or lower tolerable error means a bigger sample.

## Executing the audit

1. **Planning** - scope, objectives, and risk assessment.
2. **Fieldwork** - testing controls, gathering evidence, documenting workpapers.
3. **Reporting** - findings, risk ratings, recommendations, and management responses.
4. **Follow-up** - verifying that agreed actions were implemented. An audit without follow-up does not close the loop.

- **Compliance testing** - tests whether a control is operating as designed.
- **Substantive testing** - tests the accuracy of the data or balance itself.

Order matters: strong compliance test results allow reduced substantive testing. If
compliance testing shows controls failing, substantive testing must expand.

- **Workpapers** - the record supporting the conclusion. Must let another competent auditor reach the same conclusion.
- **Audit finding** - condition, criteria, cause, effect, and recommendation. All five elements are expected.
- **Management response** - the auditee's stated action, owner, and date. The auditor does not own remediation.

## Reporting and communication

- **Audit charter** - the document granting the audit function its authority, scope, and responsibility. Approved by the board or audit committee.
- **Engagement letter** - scope and terms for a specific audit.
- **Qualified versus unqualified opinion** - unqualified means no material exceptions; qualified means exceptions exist.
- **Exit meeting** - findings are discussed with management before the report is finalized, to confirm factual accuracy.

## Control self-assessment

- **CSA (Control Self-Assessment)** - business process owners assess their own controls, facilitated by audit. Increases ownership and control awareness.
- **The auditor's role in CSA** - facilitator, not owner. Audit still performs independent verification, because self-assessment is not independent assurance.

## Exam pointers

- The first step in almost any audit scenario is understanding the business process and its risks, not testing.
- Inquiry alone is never sufficient evidence. Look for reperformance or inspection.
- If independence is questionable, that is the answer, regardless of how competent the auditor is.
- CAATs are the answer when a question mentions analyzing an entire population or large data volumes.
- The auditor recommends; management decides and owns the remediation. Answers where the auditor implements a fix are wrong.

## Official documentation

**[📖 ISACA CISA exam content outline](https://www.isaca.org/credentialing/cisa)** - authoritative domain list
**[📖 ITAF: A Professional Practices Framework for IS Audit/Assurance](https://www.isaca.org/resources/itaf)** - the standards themselves
**[📖 ISACA Code of Professional Ethics](https://www.isaca.org/credentialing/code-of-professional-ethics)** - binding conduct requirements
