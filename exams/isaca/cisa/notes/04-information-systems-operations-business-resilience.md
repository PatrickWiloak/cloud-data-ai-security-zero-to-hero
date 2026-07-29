---
last-updated: 2026-07-29
---

# CISA Domain 4 - IS Operations and Business Resilience (23%)

The second-largest domain. Day-to-day IT operations, and the ability to keep running or
recover when they fail.

## IT service management

- **Service level management** - defining, monitoring, and reporting service levels against agreements.
- **Incident management** - restoring normal service as quickly as possible. The objective is restoration, not root cause.
- **Problem management** - identifying and removing the underlying cause of recurring incidents. The objective is prevention.
- **Change management** - controlled modification of the environment.
- **Configuration management and the CMDB** - the authoritative record of assets and their relationships.
- **Release management** - packaging and deploying changes.
- **Capacity management** - matching resources to demand, now and forecast.
- **Availability management** - designing and measuring service uptime.

Incident and problem management are frequently confused on the exam. Restoring service
now is incident management; stopping it recurring is problem management.

## Operations controls

- **Job scheduling** - automated batch execution with dependency handling. Manual scheduling is error-prone and hard to evidence.
- **Console and operator logs** - record of operator actions, reviewed independently.
- **Segregation of duties in operations** - operators should not have the ability to modify programs or data.
- **Help desk / service desk** - single point of contact, ticketing, and escalation.
- **Problem escalation procedures** - defined thresholds for raising severity and involving management.
- **End-user computing (EUC)** - spreadsheets and local databases performing business-critical processing outside IT control. A perennial audit finding because they lack change control, backup, and access control.

## Hardware and infrastructure

- **Capacity monitoring** - utilization trends against thresholds.
- **Preventive maintenance** - scheduled servicing to avoid failure.
- **RAID** - redundancy across disks. RAID 1 mirrors, RAID 5 uses distributed parity, RAID 6 tolerates two failures, RAID 10 mirrors and stripes. RAID protects against disk failure; it is not a backup, because it faithfully replicates deletion and corruption.
- **Uninterruptible power supply (UPS)** - bridges short outages and allows orderly shutdown.
- **Generator** - sustains longer outages. UPS covers the gap until the generator starts.
- **Environmental controls** - HVAC, humidity, water detection, and fire suppression.

## Virtualization and cloud

- **Hypervisor** - the layer running virtual machines. Compromise of the hypervisor exposes every guest, which concentrates risk.
- **VM sprawl** - uncontrolled proliferation of virtual machines, creating unpatched and unmonitored assets.
- **Shared responsibility model** - the division of control between provider and customer. See [shared responsibility](../../../../learn/concepts/shared-responsibility-model.md).
- **Multi-tenancy** - multiple customers on shared infrastructure; isolation is the control of interest.
- **Vendor lock-in and exit strategy** - the ability to leave, including data portability. Absence of an exit plan is a finding.
- **Cloud audit rights** - often satisfied through the provider's third-party attestations (for example SOC 2) rather than direct audit.

## Data management

- **Data classification** - assigning sensitivity so protection is proportionate. Owned by the data owner.
- **Data retention** - how long data is kept, driven by legal and business requirements. Keeping data indefinitely is a liability, not prudence.
- **Data quality** - completeness, accuracy, timeliness, and consistency.
- **Database administration controls** - DBA activity is privileged and must be logged and independently reviewed.
- **Data lifecycle** - creation, storage, use, sharing, archival, and secure destruction.

## Backup and recovery

- **Full backup** - everything. Slowest to take, fastest to restore.
- **Incremental backup** - changes since the last backup of any type. Fastest to take, slowest to restore, needs the full plus every increment.
- **Differential backup** - changes since the last full backup. Middle ground: restore needs the full plus the latest differential only.
- **Offsite storage** - protects against site loss. Rotation and transport controls matter.
- **Grandfather-father-son** - a generational retention scheme.
- **Restoration testing** - the only proof a backup works. Untested backups are the classic finding, because failure is discovered during the incident.

## Business continuity and disaster recovery

- **Business continuity plan (BCP)** - keeping business processes running during disruption. Business-led.
- **Disaster recovery plan (DRP)** - restoring IT services. A component of the BCP.
- **Business impact analysis (BIA)** - identifies critical processes, dependencies, and impact over time. Always the first step.
- **RTO** - how quickly a process must be restored.
- **RPO** - how much data loss is tolerable. RPO drives backup frequency.
- **MTD / MTO** - maximum tolerable downtime before unacceptable consequences.
- **Service delivery objective (SDO)** - the level of service required in the alternate mode.

**Recovery site options**

| Site | Ready in | Cost | Notes |
|---|---|---|---|
| Hot | Hours or less | Highest | Equipment, data, and staff ready |
| Warm | Days | Medium | Hardware present, data not current |
| Cold | Weeks | Lowest | Space and utilities only |
| Mobile | Varies | Medium | Transportable facility |
| Reciprocal agreement | Uncertain | Lowest | Another organization hosts you; rarely enforceable and hard to test |

**Testing**

- **Checklist review** - the plan is distributed and reviewed. Least disruptive, least assurance.
- **Structured walkthrough / tabletop** - team talks through the scenario.
- **Simulation** - a realistic scenario is role-played without affecting production.
- **Parallel test** - recovery systems run alongside production; results compared. No production impact.
- **Full interruption test** - production is stopped and recovery takes over. Highest assurance, highest risk, requires management approval.

The ladder from checklist to full interruption trades disruption against assurance.
Questions asking for the most thorough test point to full interruption; questions
emphasizing no business impact point to parallel.

## Exam pointers

- RPO drives backup frequency; RTO drives recovery capability and site choice.
- RAID is not a backup.
- A backup that has never been restored is not evidence of recoverability.
- BIA comes first, always, before selecting recovery strategies.
- Incident management restores; problem management prevents recurrence.
- End-user computing spreadsheets running critical processes are a control gap worth flagging.

## Official documentation

**[📖 ISACA CISA exam content outline](https://www.isaca.org/credentialing/cisa)** - authoritative domain list
**[📖 NIST SP 800-34](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)** - contingency planning guide
**[📖 ISO 22301](https://www.iso.org/standard/75106.html)** - business continuity management systems
