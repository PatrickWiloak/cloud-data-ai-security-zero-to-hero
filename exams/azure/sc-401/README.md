---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 6 min
---

# Microsoft Information Security Administrator (SC-401)

Data protection in Microsoft 365 and Purview: classify it, label it, stop it leaving, detect the insider, and prove what happened.

**SC-401 replaced SC-400.** The rename to Information Security Administrator came with a shift toward data security operations and the addition of AI-era material: DSPM for AI, DLP for Copilot, and auditing of AI interactions.

## Exam Details

- **Exam Code:** SC-401
- **Level:** Associate
- **Duration:** 100 minutes
- **Questions:** Typically 40-60
- **Passing Score:** 700/1000
- **Cost:** USD 165, varies by region
- **Prerequisites:** None formal
- **Validity:** 1 year, free online renewal

Full detail in the [fact sheet](./fact-sheet.md).

## Domains

| Domain | Weight | Notes |
|--------|-------:|-------|
| Implement information protection | 30-35% | [01](./notes/01-information-protection.md) |
| Implement data loss prevention | 30-35% | [02](./notes/02-data-loss-prevention.md) |
| Manage risks, alerts, and activities | 30-35% | [03](./notes/03-risks-alerts-and-activities.md) |

Three near-equal domains, which is unusual and useful: there is no domain you can afford to skip, and no domain worth over-weighting.

## The distinction the whole exam turns on

**Sensitivity labels classify and protect the content itself.** The protection travels with the file. If a labeled and encrypted document is emailed to a personal address, downloaded to a home machine, or posted to a competitor's site, the encryption still applies and the recipient still needs an authorized identity to open it.

**DLP policies prevent an action at a boundary.** The file itself is unchanged. DLP inspects activity and blocks, warns, or audits when content matching a condition crosses a defined boundary.

Most real designs need both, and most exam distractors offer one when the requirement needs the other. When you read a question, ask: does the requirement describe protection that must persist, or an action that must be prevented?

## Study sequence

1. **Classification first.** Sensitive information types, trainable classifiers, EDM. Everything else consumes these.
2. **Sensitivity labels and label policies.** Including auto-labeling and the client-side versus service-side distinction.
3. **DLP.** Policy anatomy, then location-specific behavior, then endpoint DLP.
4. **Insider risk, Adaptive Protection, and the investigation tools.**
5. **Retention, records, audit, and eDiscovery.**

Schedule in the [practice plan](./practice-plan.md).

## Hands-on

A Microsoft 365 E5 trial gives you everything here. Build:

- A custom sensitive information type and test it with a sample document
- A sensitivity label with encryption, published through a label policy
- An auto-labeling policy in simulation mode, then read the simulation results
- A DLP policy in test mode with policy tips, then review the alerts
- An insider risk policy from a template, and inspect the indicators it enables
- A retention label with disposition review

Simulation and test modes exist because these controls break user workflows when misconfigured. The exam expects you to use them.

## Study resources

- **[📖 SC-401 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401)** - authoritative outline
- **[📖 Microsoft Purview documentation](https://learn.microsoft.com/en-us/purview/)** - primary reference
- **[📖 Microsoft Learn SC-401 path](https://learn.microsoft.com/en-us/training/browse/?terms=SC-401)** - free official modules
- [Practice questions](../../../resources/practice-questions/azure-information-security-sc-401.md) - question bank in this repo

## Related

- [SC-300 Identity and Access Administrator](../sc-300/)
- [SC-100 Cybersecurity Architect](../sc-100/)
- [SC-900 Security, Compliance and Identity Fundamentals](../sc-900/)
- [Compliance guides](../../../resources/compliance-guides/)
- [AI security](../../../resources/ai-security/)
- [Security Engineer roadmap](../../../resources/certification-roadmap-security-engineer.md)
