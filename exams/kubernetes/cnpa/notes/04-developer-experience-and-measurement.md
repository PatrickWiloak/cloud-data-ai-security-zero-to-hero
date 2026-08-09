---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 9 min
---

# 04 - Developer experience and measurement

**Domains: IDPs and Developer Experience (8%) and Measuring Your Platform (8%)** - 16% combined.

---

## Platform versus portal

A distinction the exam tests directly, because the industry uses "IDP" for both.

| | Internal Developer Platform | Internal Developer Portal |
|---|---|---|
| What it is | The capability layer: provisioning, delivery, observability, guardrails | A user interface onto those capabilities |
| Example | Crossplane compositions, GitOps agents, policy, golden paths | Backstage, Port, Cortex |
| Without the other | Usable through APIs and CLI, just less discoverable | A catalog of links to nothing |

**Order matters.** Build capability first, then surface it. A portal deployed over an absent platform improves nothing, which is a common and testable failure.

---

## Backstage and portal patterns

Backstage is the reference open-source portal, and the exam expects familiarity with its concepts rather than its configuration:

- **Software catalog** - the inventory of services, APIs, resources, and their owners. Ownership metadata is often the single most useful thing a portal provides
- **Software templates (scaffolder)** - templates that instantiate a new service **on a golden path**, with repository, pipeline, manifests, and monitoring already wired
- **TechDocs** - documentation built from Markdown in the service's repository, so docs live with the code
- **Plugins** - surfacing CI status, cost, security findings, and other capability-specific views

The scaffolder is the important one conceptually: it is how a golden path becomes the **default** rather than a document someone has to read.

---

## Developer experience

What actually determines whether developers like a platform:

- **Time to first deployment** for a new service, and for a newly-hired engineer. A headline metric, and a direct measure of cognitive load
- **Documentation** treated as a feature with an owner, not an afterthought
- **Error messages** that say what to do next. A schema validation failure that names the field and the allowed values is a developer experience feature
- **Local development** that resembles production closely enough to be useful
- **Feedback loops**: office hours, a support channel, surveys, and treating complaints as product signal rather than user error
- **Onboarding** that does not require a human, because a platform requiring a human per onboarding does not scale

---

## Measurement

### DORA metrics

Delivery performance, and the most widely recognized framing:

| Metric | Measures | Improved by |
|---|---|---|
| **Deployment frequency** | How often you release | Automation, small batches, self-service |
| **Lead time for changes** | Commit to production | Pipeline speed, fewer handoffs, fewer approvals |
| **Change failure rate** | Proportion of releases causing degradation | Testing, policy, progressive delivery |
| **Time to restore service** | Recovery speed after an incident | Rollback, observability, runbooks |

The first two measure throughput, the last two stability. Healthy platforms improve all four together, which is the finding that made DORA persuasive.

### SPACE framework

Broader than delivery, for developer productivity:

- **S**atisfaction and well-being
- **P**erformance (outcomes, not output)
- **A**ctivity (counts of actions, the weakest dimension alone)
- **C**ommunication and collaboration
- **E**fficiency and flow

The point of SPACE is that no single metric captures productivity, and that measuring activity alone is misleading.

### Platform-specific measures

- **Adoption**: proportion of eligible teams and workloads using the platform, **voluntarily**
- **Time to first deployment**
- **Platform SLOs**: availability and latency of the capabilities offered
- **Developer satisfaction**, surveyed regularly with free-text comments
- **Cost per workload or per team**, exposed through **showback**; **chargeback** only where the organization genuinely wants tenants to feel the price
- **Support burden**: a falling ticket count is a success signal for a self-service platform

### Vanity metrics

Reliably wrong answers:
- Features shipped by the platform team (output, not outcome)
- Lines of platform code
- **Tickets closed** (inversely correlated with self-service success)
- Uptime alone (necessary but not sufficient; a reliable platform nobody uses has still failed)

---

## Key terms

- **Internal Developer Platform** - the capability layer providing provisioning, delivery, observability, and guardrails
- **Internal Developer Portal** - the user interface making platform capabilities discoverable and usable
- **Software catalog** - the portal inventory of services, APIs, and resources with their ownership metadata
- **Software template** - a portal scaffolder definition instantiating a new service directly onto a golden path
- **TechDocs** - documentation built from Markdown stored alongside the service's source code
- **Time to first deployment** - the elapsed time for a new service or new engineer to reach production, a core DX measure
- **DORA metrics** - deployment frequency, lead time for changes, change failure rate, and time to restore service
- **Deployment frequency** - how often an organization releases to production
- **Lead time for changes** - the elapsed time from commit to running in production
- **Change failure rate** - the proportion of releases that cause degradation requiring remediation
- **Time to restore service** - how quickly service is recovered after a failure
- **SPACE framework** - satisfaction, performance, activity, communication, and efficiency dimensions of developer productivity
- **Adoption rate** - the proportion of eligible teams or workloads voluntarily using the platform
- **Showback** - exposing cost attribution to teams without billing them
- **Chargeback** - actually billing teams for the resources they consume
- **Vanity metric** - a measure that looks like progress without reflecting outcomes, such as tickets closed

---

## Related

- [Notes 01: platform fundamentals](./01-platform-fundamentals.md)
- [Scenarios](../scenarios.md) - scenarios 5 and 6
- [Platform Engineer roadmap](../../../../resources/certification-roadmap-platform-engineer.md)
