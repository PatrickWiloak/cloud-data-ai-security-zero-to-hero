---
last-updated: 2026-07-29
---

# CISM Domain 2 - Information Security Risk Management (20%)

Identifying, analysing, treating, and monitoring risk. The domain where the exam is most
precise about vocabulary, so learn the definitions exactly.

## Core vocabulary

- **Asset** - anything of value: data, systems, people, reputation.
- **Threat** - a potential cause of an unwanted incident. Threats exist independently of you and cannot be reduced.
- **Vulnerability** - a weakness that a threat can exploit. This is what controls reduce.
- **Risk** - the combination of likelihood and impact. Expressed as threat exploiting a vulnerability to cause harm to an asset.
- **Exposure** - the extent of loss when a threat is realised.
- **Likelihood / probability** - how often the event is expected.
- **Impact** - the consequence, expressed in business terms.
- **Inherent risk** - before controls.
- **Residual risk** - after controls. Residual risk must be within appetite or explicitly accepted.
- **Risk appetite** - how much risk the organisation is willing to take.
- **Risk tolerance** - acceptable deviation from appetite.
- **Risk capacity** - the maximum the organisation could absorb and survive.

You cannot reduce a threat. You reduce vulnerability, and thereby risk. Exam options
offering "reduce the threat" are usually wrong.

## Risk assessment

**Qualitative analysis** - ratings such as high, medium, and low. Fast, subjective, good
for prioritisation and for risks that resist quantification such as reputation.

**Quantitative analysis** - monetary values.

- **Asset value (AV)** - the worth of the asset.
- **Exposure factor (EF)** - the proportion of the asset lost in a single event, as a percentage.
- **Single loss expectancy (SLE)** - AV x EF.
- **Annual rate of occurrence (ARO)** - expected events per year.
- **Annual loss expectancy (ALE)** - SLE x ARO.

A control is economically justified when its annual cost is less than the reduction in
ALE it delivers. This calculation appears on the exam, so be able to run it.

- **Semi-quantitative** - numeric scales without full monetary modelling. A common practical compromise.
- **Risk register** - the record: risk, owner, rating, treatment, status, and target date.

## Risk treatment

- **Mitigate / modify** - apply controls to reduce likelihood or impact.
- **Transfer / share** - insurance or contractual transfer. Transfers financial consequence, never accountability or reputational damage.
- **Avoid** - stop the activity generating the risk.
- **Accept** - documented acceptance by the risk owner, with justification and review date.

Risk is never eliminated. Some residual risk always remains, and accepting it is a
legitimate, documented business decision made by the business owner.

## Control selection

- **Cost-benefit justification** - the control must cost less than the loss it prevents.
- **Control types by function** - preventive, detective, corrective, deterrent, compensating, recovery.
- **Control types by nature** - administrative (policy, training), technical (logical), physical.
- **Defence in depth** - layered controls so no single failure is catastrophic.
- **Compensating control** - used when the primary control is impractical, and must address the same risk to a comparable degree.

## Risk in context

- **Third-party and supply chain risk** - due diligence before contracting, monitoring during, and defined exit. Accountability stays with your organisation.
- **Cloud risk** - shaped by the shared responsibility model. Assurance often comes from provider attestations rather than direct audit.
- **Emerging technology risk** - AI, IoT, and similar introduce risks the existing control set may not address. The manager's job is to assess before adoption, not after.
- **Business impact analysis (BIA)** - identifies critical processes and impact over time, feeding both risk management and continuity planning.

## Monitoring and reporting

- **Key risk indicator (KRI)** - a metric that signals rising exposure before loss occurs. Good KRIs are predictive, measurable, and tied to a specific risk.
- **Risk reporting** - to management and the board, in business terms, with trends rather than snapshots.
- **Continuous monitoring** - risk is not static. Assessments have a shelf life, and material change triggers reassessment.
- **Risk aggregation** - many individually acceptable risks may be unacceptable in combination.
- **Change triggers** - new systems, new regulation, mergers, and incidents all require reassessment.

## Integrating risk management

- **Enterprise risk management (ERM)** - information security risk is one category within enterprise risk, and should be reported in the same terms as other risks so it can be compared and prioritised.
- **Risk ownership** - every risk has a named business owner. Unowned risks are not managed.
- **Risk-aware culture** - staff who recognise and report risk early.

## Exam pointers

- Learn SLE = AV x EF and ALE = SLE x ARO cold. Calculation questions are common.
- Threats cannot be reduced; vulnerabilities can.
- Insurance transfers financial impact, not accountability.
- The risk owner is a business owner, never the security manager.
- The first step in risk assessment is identifying and valuing assets. You cannot assess risk to something you have not identified.
- A control costing more than the loss it prevents should not be implemented, even if it is technically superior.

## Official documentation

**[📖 ISACA CISM exam content outline](https://www.isaca.org/credentialing/cism)** - authoritative domain list
**[📖 NIST SP 800-30](https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final)** - guide for conducting risk assessments
**[📖 ISO/IEC 27005](https://www.iso.org/standard/80585.html)** - information security risk management
