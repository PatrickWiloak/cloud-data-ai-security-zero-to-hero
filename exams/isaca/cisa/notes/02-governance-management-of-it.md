---
last-updated: 2026-07-29
---

# CISA Domain 2 - Governance and Management of IT (17%)

Whether IT is directed and controlled so it supports the organization's objectives. The
recurring exam theme: governance sets direction and accountability, management executes.

## Governance versus management

- **IT governance** - the board and executive responsibility for evaluating stakeholder needs, directing IT, and monitoring performance against objectives. Owned by the board.
- **IT management** - planning, building, running, and monitoring activities aligned to the direction set by governance. Owned by executives.
- **COBIT** - ISACA's framework for enterprise governance and management of IT. Its core distinction is exactly the one above, and it is the framework CISA assumes.
- **Enterprise governance of IT (EGIT)** - ensuring IT delivers value and risks are managed.

The board does not run IT. Exam answers that have the board performing operational tasks
are wrong; answers where the board sets direction, approves strategy, and holds management
accountable are right.

## Strategy and value

- **IT strategy** - how IT will support business objectives. Must derive from business strategy, not run parallel to it.
- **IT steering committee** - cross-functional body prioritizing IT investment and monitoring major projects. Membership includes business representation, which is the point.
- **Strategic alignment** - IT objectives demonstrably supporting business objectives.
- **Value delivery** - IT investments producing the benefits that justified them.
- **Benefits realization** - measuring whether promised benefits actually arrived, after the project closed.
- **Balanced scorecard** - measures performance across financial, customer, internal process, and learning perspectives. An IT balanced scorecard adapts this to IT.
- **Portfolio management** - selecting and balancing the set of investments, rather than judging each in isolation.

## Policies, standards, procedures, guidelines

The hierarchy is tested directly.

- **Policy** - high-level statement of management intent and direction. Approved by senior management or the board. Changes rarely.
- **Standard** - mandatory specification supporting policy, for example a minimum password length.
- **Procedure** - step-by-step instructions for performing a task.
- **Guideline** - recommended, non-mandatory advice.

Policies say *what and why*, standards say *how much*, procedures say *how*, guidelines
*suggest*.

## Organizational structure and roles

- **Segregation of duties (SoD)** - no single individual controls all phases of a transaction. The classic IT example: developers must not have access to promote their own code into production.
- **Compensating controls for SoD** - in small organizations where separation is impossible: supervisory review, audit trails, reconciliation, and rotation of duties.
- **Data owner** - accountable for classification and authorizing access to a data set. A business role, not an IT role.
- **Data custodian** - implements and maintains the controls the owner specifies. Usually IT.
- **Data user** - uses the data within the granted permissions.
- **Chief information security officer (CISO)** - responsible for the security program. Reporting to the CIO can create a conflict of interest, which the exam sometimes probes.
- **Job rotation and mandatory vacation** - detective controls that surface concealed irregularities.

## Risk management

- **Risk appetite** - the amount of risk the organization is willing to accept in pursuit of objectives.
- **Risk tolerance** - acceptable variation around the appetite.
- **Risk register** - the record of identified risks, owners, treatments, and status.
- **Risk treatment options** - mitigate (reduce), transfer (share, for example insurance), avoid (stop the activity), accept (document and monitor).

Risk is never "eliminated." Answers offering elimination are wrong. Accepting risk
requires an owner with the authority to accept it.

## Enterprise architecture and resource management

- **Enterprise architecture (EA)** - the blueprint describing business processes, information, applications, and technology, and how they relate. Prevents point solutions that do not fit.
- **Capacity management** - ensuring resources meet current and forecast demand.
- **Sourcing strategy** - insourcing, outsourcing, hybrid, and the location decision (onshore, nearshore, offshore).
- **Third-party management** - due diligence before contracting, and monitoring throughout the relationship.
- **Right to audit clause** - contractual right to audit the vendor. Its absence is a common finding.
- **Service level agreement (SLA)** - the measurable commitment. Without metrics and penalties it is not enforceable.
- **Vendor concentration risk** - over-dependence on one supplier.

Outsourcing transfers the activity, never the accountability. If a question asks who
remains responsible for the security of outsourced processing, the answer is the
organization.

## Performance and compliance monitoring

- **Key performance indicator (KPI)** - measures whether an objective is being achieved.
- **Key risk indicator (KRI)** - forward-looking measure signaling increasing risk exposure.
- **Maturity model** - assesses process capability on a scale, showing the gap between current and target state.
- **Benchmarking** - comparing performance against peers or standards.
- **Regulatory compliance monitoring** - tracking obligations and evidencing adherence.

KPIs look backward at performance, KRIs look forward at exposure. The exam tests that
distinction.

## Business continuity governance

- **Business impact analysis (BIA)** - identifies critical processes and the impact of their disruption over time. It is the input to continuity planning, and it comes first.
- **RTO (Recovery Time Objective)** - maximum tolerable time to restore a process.
- **RPO (Recovery Point Objective)** - maximum tolerable data loss, expressed as time.
- **MTO / MTD (Maximum Tolerable Outage/Downtime)** - the point beyond which the organization cannot survive the disruption.
- **BCP governance** - senior management owns and approves the plan; it is tested and maintained, not written once.

The BIA always precedes strategy selection. Choosing a recovery site before performing a
BIA is a standard wrong answer.

## Exam pointers

- Governance directs and monitors; management executes. Sort every answer into one of those two before choosing.
- The data owner classifies and authorizes access. The custodian implements. Do not swap them.
- The first step in continuity planning is the BIA.
- Outsourcing never transfers accountability.
- If segregation of duties is impossible, the answer is compensating controls, not accepting the exposure silently.

## Official documentation

**[📖 ISACA CISA exam content outline](https://www.isaca.org/credentialing/cisa)** - authoritative domain list
**[📖 COBIT framework](https://www.isaca.org/resources/cobit)** - governance and management objectives
**[📖 NIST SP 800-34](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)** - contingency planning, including BIA method
