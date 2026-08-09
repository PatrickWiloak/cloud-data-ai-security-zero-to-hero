---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 8 min
---

# 05 - Business continuity, disaster recovery, and incident response

**Domain 5: Business Continuity, Disaster Recovery, and Incident Response Concepts (10%)** - the smallest domain.

---

## Three disciplines, one incident

| Discipline | Question it answers | Owns |
|---|---|---|
| **Incident response (IR)** | Something bad is happening. How do we handle it? | Detection, containment, eradication, recovery of the event |
| **Business continuity (BC)** | How does the business keep functioning meanwhile? | Alternative processes, critical function continuity |
| **Disaster recovery (DR)** | How do we get the technology back? | Restoring systems, data, and facilities |

A ransomware attack invokes all three, and the exam asks which discipline a described activity belongs to. Isolating a network segment is IR. Switching to paper forms is BC. Restoring servers from backup is DR.

---

## Incident response

**Phases**, in order:

1. **Preparation** - the plan, the team, the tools, and the training. Everything you must do before an incident
2. **Detection and analysis** - identify that an event occurred, determine whether it is an incident, and assess scope and severity
3. **Containment** - limit the damage. Often split into short-term (isolate now) and long-term (rebuild cleanly)
4. **Eradication** - remove the cause: the malware, the compromised account, the vulnerability
5. **Recovery** - restore systems to normal operation and confirm they are clean
6. **Post-incident activity** - lessons learned, and improvements to controls and to the plan itself

Vocabulary:
- An **event** is any observable occurrence. An **incident** is an event that harms, or threatens to harm, security
- A **breach** specifically involves unauthorized access to or disclosure of data
- The **incident response team** (CSIRT) includes technical responders, plus legal, communications, and management
- **Evidence preservation** matters: capture logs and images before remediating, because containment can destroy the evidence needed to understand the incident
- **Chain of custody** documents who handled evidence and when, which is required if the matter reaches a court

---

## Business continuity

**Business impact analysis (BIA)** is the foundation. It identifies:
- **Critical business functions** and their dependencies
- The **impact** of losing each, over time
- The **maximum tolerable downtime** for each
- The resources each requires to operate

The BIA drives the recovery objectives, so it comes first. A recovery plan built without a BIA is guessing at what matters.

The **business continuity plan** then defines: alternative processes, communication procedures, roles and responsibilities, and activation criteria. It must be **tested** and updated; an untested plan is an assumption.

---

## Disaster recovery

**Recovery objectives**, the pair most often confused:

- **RTO (recovery time objective)**: the maximum acceptable **downtime**. Drives recovery capability, such as standby infrastructure
- **RPO (recovery point objective)**: the maximum acceptable **data loss**, measured in time. Drives backup and replication frequency

Nightly backups give an RPO of up to 24 hours regardless of how fast you can restore.

**Backup types**:

| Type | Copies | Restore requires | Backup speed |
|---|---|---|---|
| **Full** | Everything | Just the full backup | Slowest |
| **Incremental** | Changes since the **last backup of any type** | The full plus **every** incremental since | Fastest |
| **Differential** | Changes since the **last full backup** | The full plus the **latest** differential | Middle |

The trade-off is directly testable: incremental backs up fastest and restores slowest; differential is the reverse.

**The 3-2-1 rule**: three copies of the data, on two different media types, with one copy offsite.

**Recovery sites**:

| Site | Equipment | Data | Time to operate | Cost |
|---|---|---|---|---|
| **Hot** | Fully equipped and running | Current | Minutes to hours | Highest |
| **Warm** | Equipped | Periodically synced | Hours to days | Medium |
| **Cold** | Space and utilities only | None | Days to weeks | Lowest |

Related: a **reciprocal agreement** with another organization, and **cloud-based recovery**, which has largely displaced dedicated warm and cold sites.

**Testing** progresses in rigour: read-through, tabletop exercise, walkthrough, simulation, parallel test, and full interruption test. A full interruption test carries real risk and is rarely run in practice.

---

## Key terms

- **Event** - any observable occurrence in a system or network
- **Incident** - an event that harms or threatens to harm security
- **Breach** - an incident involving unauthorized access to or disclosure of data
- **Incident response plan** - the documented approach to detecting, containing, and recovering from incidents
- **Containment** - the incident response phase that limits the damage of an ongoing incident
- **Eradication** - the incident response phase that removes the cause of the incident
- **Post-incident activity** - the lessons learned phase that improves controls and the plan
- **Chain of custody** - documentation of who handled evidence, when, and how
- **Business impact analysis** - the study identifying critical functions, their dependencies, and the impact of losing them
- **Maximum tolerable downtime** - the longest a business function can be unavailable before unacceptable harm
- **Business continuity plan** - the plan keeping critical business functions running during a disruption
- **Disaster recovery plan** - the plan restoring technology and data after a disruptive event
- **RTO** - recovery time objective, the maximum acceptable downtime
- **RPO** - recovery point objective, the maximum acceptable data loss measured in time
- **Full backup** - a complete copy of all selected data
- **Incremental backup** - a copy of changes since the last backup of any type, fast to create and slow to restore
- **Differential backup** - a copy of changes since the last full backup, slower to create and faster to restore
- **3-2-1 rule** - three copies of data, on two media types, with one copy offsite
- **Hot site** - a fully equipped alternate site with current data, able to operate almost immediately
- **Cold site** - an alternate site with space and utilities but no equipment or data
- **Tabletop exercise** - a discussion-based test of a plan without touching production systems

---

## Related

- [Notes 01: security principles](./01-security-principles.md)
- [Scenarios](../scenarios.md) - scenarios 5 and 6
- [Disaster recovery patterns](../../../../resources/architecture-patterns/disaster-recovery-patterns.md)
