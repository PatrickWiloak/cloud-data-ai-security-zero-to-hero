---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 5 min
---

# ISC2 CC Study Strategy

## This is a vocabulary exam

CC tests whether you know what things are and how they relate, not whether you can configure them. The single highest-value study activity is building precise definitions for terms that sound similar and are constantly offered as each other's distractors.

Make a list, write your own definition of each, then check it against the ISC2 exam outline. The pairs that matter most are in the [practice plan readiness check](./practice-plan.md#readiness-check).

## The distinctions the exam lives on

**Threat, vulnerability, risk.** A vulnerability is a weakness. A threat is something that could exploit it. Risk is the combination of likelihood and impact. A locked door with a weak hinge has a vulnerability; a burglar is the threat; the chance and cost of a break-in is the risk.

**Control type versus control function.** These are two independent axes, and questions often ask for one when you are thinking of the other:

| | Preventive | Detective | Corrective |
|---|---|---|---|
| **Technical** | Firewall | IDS | Automatic patching |
| **Administrative** | Security policy | Audit | Incident response plan |
| **Physical** | Lock | CCTV | Fire suppression |

Plus **deterrent** (discourages: a warning sign, visible cameras) and **compensating** (an alternative when the primary control is not feasible).

**Authentication, authorization, accounting.** Who you are, what you may do, what you did.

**BC, DR, IR.** Business continuity keeps the business functioning. Disaster recovery restores technology. Incident response handles the security event. A ransomware attack invokes all three, and questions frequently ask which one a described activity belongs to.

**RTO and RPO.** Recovery **time** objective is how long until service is back. Recovery **point** objective is how much data you can afford to lose. RPO drives backup frequency; RTO drives recovery capability.

## Phase 1: Principles (week 1)

26% of the exam and the vocabulary the other domains use. Learn the risk terms and the control taxonomy properly here and the rest of the exam gets easier.

The **ISC2 Code of Ethics** canons are directly testable, including their **order**, because the code states that they are to be applied in order of precedence:

1. Protect society, the common good, necessary public trust and confidence, and the infrastructure
2. Act honorably, honestly, justly, responsibly, and legally
3. Provide diligent and competent service to principals
4. Advance and protect the profession

**Governance documents** are also directly testable: a **policy** is high level and mandatory, a **standard** is a mandatory specific requirement, a **procedure** is step by step, and a **guideline** is recommended rather than mandatory.

## Phase 2: Network security (week 2)

24%, and the hardest domain for beginners. Start it early rather than leaving it to the end.

You do not need to configure anything, but you do need to know: what happens at each OSI layer, what the common devices do, what the common protocols are for, and what the common attacks are. Learn the common ports (22, 25, 53, 80, 443, 3389) because they appear as answer options.

Cloud is inside this domain: service models (IaaS, PaaS, SaaS), deployment models (public, private, hybrid, community), and **shared responsibility**. The shared responsibility question shape is "who is responsible for X", and the answer moves toward the provider as you go from IaaS to SaaS.

## Phase 3: Access control and operations (week 3)

Access control is conceptually simple once principles are solid. Focus on the **models** and on least privilege versus need to know, which are related but distinct: least privilege limits what you can do, need to know limits what you can see.

Operations is broad and shallow. Encryption is the one place to be careful: **symmetric** is fast and uses one shared key, **asymmetric** solves key distribution and enables digital signatures, **hashing** is one-way and provides integrity rather than confidentiality.

## Phase 4: BC, DR, IR (week 4)

Only 10%, and mostly a matter of knowing which discipline owns which activity, plus the **incident response phases in order**: preparation, detection and analysis, containment, eradication and recovery, post-incident activity.

## Common traps

| Trap | Reality |
|---|---|
| Confusing threat with vulnerability | A vulnerability is the weakness; the threat is what exploits it |
| Mixing control type with control function | Two independent axes; read which one is asked |
| Assuming a guideline is mandatory | Guidelines are recommended; standards and policies are mandatory |
| Confusing RTO with RPO | Time to restore versus data you can afford to lose |
| Thinking hashing is encryption | Hashing is one way and gives integrity, not confidentiality |
| Treating DR and BC as the same | DR restores technology; BC keeps the business running |
| Over-thinking the question | CC answers are usually the direct, textbook one |

## Exam day

- 120 minutes for 100 questions is 72 seconds each, comfortable.
- Linear, not adaptive, so you can review and change answers.
- 700/1000 to pass; the score is scaled, so do not try to count.
- No penalty for a wrong answer; leave nothing blank.
- Choose the **textbook** answer. CC rewards the standard definition over the clever real-world nuance.

## After you pass

Certification requires agreeing to the ISC2 Code of Ethics and paying the Annual Maintenance Fee. Maintain it with CPE credits over the three-year cycle. If you do not complete the requirements you remain a candidate rather than certified, so check the current terms on the ISC2 site.

## Related

- [Practice plan](./practice-plan.md)
- [Scenarios](./scenarios.md)
- [Fact sheet](./fact-sheet.md)
- [Study strategies](../../../resources/study-strategies.md)
- [Exam day checklist](../../../resources/exam-day-checklist.md)
