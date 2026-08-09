---
last-updated: 2026-08-09
difficulty: advanced
reading-time: 7 min
---

# SC-100 Study Strategy

## The core insight

SC-100 does not test whether you know what a service does. It tests whether you pick the right one under a constraint. Most candidates who fail knew the services; they answered the question they expected rather than the question asked.

Everything below follows from that.

## Reading technique

For every question, in this order:

1. **Read the last sentence first.** It contains the actual ask and usually the qualifier.
2. **Identify the constraint.** Least effort, least privilege, lowest cost, no app changes, meets a named framework, fastest to deploy.
3. **Read the scenario for the disqualifiers.** Existing licensing tier, on-premises dependency, regulatory jurisdiction, an explicitly stated limitation.
4. **Now read the options.** Eliminate the ones that fail the constraint even though they solve the problem.

If two options survive, one of them almost always requires more operational effort or a higher license tier. Pick the other.

## Case study technique

Case studies present a long scenario followed by several questions. Reading the whole thing repeatedly wastes time.

Build a table on your scratch pad on first read:

| Requirement | Constraint | Existing estate |
|---|---|---|
| Protect on-prem servers | Must use existing licences | Windows Server 2019, no Arc |
| Detect identity attacks | Least admin effort | Entra ID P2 already owned |

Then answer each question against the table rather than re-reading. Case study questions are usually independent, so one misread requirement does not have to cost you several marks.

## Phase 1: Frameworks (week 1-2)

Learn the vocabulary before the services.

- **Zero Trust**: verify explicitly, least privilege access, assume breach. Be able to give an Azure control for each.
- **MCRA**: the reference diagrams. Know what sits in which layer and what talks to what.
- **Cloud Adoption Framework Secure**: the methodology and its phases.
- **Microsoft Cloud Security Benchmark**: the control baseline, and how it maps to CIS and NIST.
- **Well-Architected security pillar**: the trade-off language the exam uses.

## Phase 2: Identity and operations (week 3-4)

This is 30-35% of the exam and it bleeds into the other domains.

Concentrate on decisions rather than steps:

- When to use Conditional Access vs PIM vs entitlement management. They solve different problems and questions deliberately blur them.
- Hybrid identity method selection, and what each choice costs you during an outage.
- Sentinel workspace topology and the cost consequence of each option.
- Defender XDR vs Sentinel: when the unified incident view is enough and when you need a SIEM.

## Phase 3: Infrastructure and data (week 5-6)

Focus on the boundaries:

- CSPM vs workload protection. Free posture recommendations vs paid runtime protection.
- Private Link vs service endpoint vs firewall rules. The exam tests this repeatedly.
- Azure Firewall Standard vs Premium. TLS inspection and IDPS are the Premium discriminators.
- Sensitivity labels vs DLP vs Information Barriers. Different problems, frequently conflated in distractors.
- Platform-managed keys vs customer-managed keys vs Managed HSM. Compliance requirements drive the answer.

## Phase 4: Integration (week 7-8)

Practise whole-architecture questions. Take a scenario and design the answer before reading options. If your design matches one of the options, you understand the material. If it does not, work out whether the option is better or whether you missed a constraint.

## Common traps

| Trap | Reality |
|---|---|
| Choosing the most secure option | The most secure option that ignores "least administrative effort" is wrong |
| Assuming a license tier | If the scenario says Entra ID P1, PIM and Identity Protection are off the table |
| Confusing Defender products | Defender for Cloud, Defender for Endpoint, Defender for Identity, Defender for Office, Defender for Cloud Apps all appear in distractors |
| Recommending a rebuild | Options that require application changes usually lose to options that do not |
| Over-indexing on Sentinel | Sometimes Defender XDR alone meets the requirement at lower cost |
| Ignoring the hybrid part | Many scenarios include on-premises or another cloud. Arc and connectors are usually part of the answer |

## Exam day

- 120 minutes for roughly 40-60 items including case studies. Budget the case studies at 15-20 minutes each and do not let them eat the remainder.
- Case studies may appear first and cannot always be revisited once you leave the section. Read the on-screen instructions about navigation carefully.
- Mark and move. A design question you are unsure about will often be clarified by a later question that reveals how the exam is framing the estate.
- Answer everything. There is no penalty for a wrong answer.
- The score is scaled to 1000 with a 700 pass. Domain weights do not translate directly to question counts, so do not try to compute where you stand mid-exam.

## After the exam

The certification is valid for one year and renews free through an unproctored Microsoft Learn assessment in the six months before expiry. Put a calendar reminder at month 10; the renewal window is easy to miss and letting it lapse means retaking the full exam.

## Related

- [Practice plan](./practice-plan.md) - the week-by-week schedule
- [Scenarios](./scenarios.md) - design questions in exam shape
- [Fact sheet](./fact-sheet.md) - domains, services, official links
- [Study strategies](../../../resources/study-strategies.md) - general technique
- [Exam day checklist](../../../resources/exam-day-checklist.md)
