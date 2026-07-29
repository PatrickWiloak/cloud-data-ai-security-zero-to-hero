---
last-updated: 2026-07-29
---

# CySA+ Domain 3 - Incident Response and Management (20%)

Built on the NIST SP 800-61 lifecycle. Know the phases in order, what belongs in each,
and the evidence-handling rules.

## The NIST SP 800-61 lifecycle

1. **Preparation** - building the capability before anything happens: playbooks, tooling, training, contact lists, baselines.
2. **Detection and Analysis** - identifying that an incident is occurring and determining its scope and severity.
3. **Containment, Eradication, and Recovery** - limiting damage, removing the adversary, restoring service.
4. **Post-Incident Activity** - lessons learned, and feeding improvements back into preparation.

The loop matters: post-incident findings become preparation for the next incident.

## Preparation

- **Incident response plan** - the governing document: authority, escalation, and decision rights.
- **Playbook** - the step-by-step procedure for a specific incident type, for example ransomware or business email compromise.
- **Communication plan** - who is told what, when, and by whom. Includes out-of-band channels, because the attacker may be reading corporate email.
- **Tabletop exercise** - a discussion-based walkthrough of a scenario. Cheap, finds gaps in process rather than technology.
- **Baseline** - a known-good picture of normal. Without it, "abnormal" is not measurable.
- **Business continuity plan (BCP)** - keeping the business running during disruption.
- **Disaster recovery plan (DRP)** - restoring IT systems after a disruptive event.

## Detection and analysis

- **Incident** - an event that actually or potentially jeopardises confidentiality, integrity, or availability.
- **Event** - any observable occurrence. Most events are not incidents.
- **True positive versus false positive** - triage exists to separate them before mobilising a response.
- **Severity and prioritisation** - based on functional impact, information impact, and recoverability effort.
- **Scoping** - determining how many systems and accounts are affected. Under-scoping causes premature eradication and reinfection.

**Impact analysis dimensions**

- **Organisation impact versus localised impact** - one workstation or the whole estate.
- **Immediate versus total impact** - what is happening now against the eventual cost.
- **Data integrity** - whether data can still be trusted.
- **Economic and reputational impact** - fines, downtime cost, customer trust.

## Containment

- **Short-term containment** - stop the bleeding now: isolate a host, block an IP, disable an account.
- **Long-term containment** - temporary fixes that let the business operate while eradication is prepared.
- **Isolation** - removing the system from the network while preserving it for analysis.
- **Segmentation** - restricting movement rather than fully removing the asset.
- **Removal** - taking the asset out of service entirely.

A tested trade-off: pulling the power preserves disk but destroys memory-resident
evidence. If volatile data matters, capture memory before shutting anything down.

## Eradication and recovery

- **Eradication** - removing the cause: malware, attacker accounts, persistence mechanisms, and the vulnerability used for entry.
- **Recovery** - restoring systems to normal operation and confirming they are clean.
- **Reimaging** - rebuilding from a known-good image. The reliable answer when the extent of compromise is uncertain.
- **Patching and hardening** - closing the entry route so the same intrusion does not simply recur.
- **Validation** - scanning, verifying logging is restored, and monitoring closely after return to service.

Eradication before full scoping is a classic mistake: the attacker retains a foothold
elsewhere and returns.

## Evidence handling and forensics

- **Chain of custody** - documented record of who handled evidence, when, and why. Break it and the evidence may be inadmissible.
- **Order of volatility** - collect the most perishable first: CPU registers and cache, memory, network state and running processes, disk, remote logs, then archival media.
- **Forensic image** - a bit-for-bit copy. Analyse the copy, never the original.
- **Write blocker** - hardware or software preventing modification of the source during acquisition.
- **Hashing** - proving the image is identical to the source and unaltered since. Compute at acquisition and verify later.
- **Legal hold** - a directive to preserve data relevant to litigation, overriding normal retention deletion.
- **Data acquisition from cloud** - constrained by the provider's shared responsibility model; you may need vendor cooperation for anything below your layer.

## Root cause analysis and post-incident activity

- **Root cause analysis (RCA)** - determining why the incident was possible, not merely what happened. The "five whys" is a common technique.
- **Lessons learned** - a structured review, ideally within two weeks while memory is fresh.
- **Blameless post-mortem** - focuses on systemic causes rather than individual fault, which is what makes people report problems early.
- **Incident report** - the durable record: timeline, impact, actions, and follow-ups with owners and dates.

See the repo's worked examples: [AWS S3 2017](../../../../resources/postmortem-aws-s3-2017.md) and
[Cloudflare 2019](../../../../resources/postmortem-cloudflare-regex-2019.md).

## Exam pointers

- Order-of-phase questions are common. Containment always precedes eradication, and eradication precedes recovery.
- If a question asks what to do *first* on discovering an active intrusion, containment usually wins over investigation, unless the question stresses evidence preservation.
- Anything mentioning legal proceedings points to chain of custody and forensic imaging.
- If asked what to collect first, apply the order of volatility: memory before disk.
- Reimaging is the safe answer when the question says the extent of compromise cannot be determined.

## Official documentation

**[📖 NIST SP 800-61r2](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)** - computer security incident handling guide
**[📖 NIST SP 800-86](https://csrc.nist.gov/publications/detail/sp/800-86/final)** - integrating forensic techniques into incident response
**[📖 CompTIA CySA+ exam objectives](https://www.comptia.org/certifications/cybersecurity-analyst#examdetails)** - authoritative domain list
