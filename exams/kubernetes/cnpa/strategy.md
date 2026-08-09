---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 5 min
---

# CNPA Study Strategy

## The white paper is the syllabus

The CNCF Platforms White Paper and the Platform Engineering Maturity Model are short, free, and the exam follows them closely. Read both before anything else. Most third-party platform engineering content is vendor marketing that will not match the exam's vocabulary.

## The product framing answers most questions

**A platform is a product whose users can choose not to use it.**

Apply that lens and the correct answer usually falls out:

| Option describes | Verdict |
|---|---|
| Mandating platform use | Wrong. Mandates hide adoption failure |
| Building because the platform team finds it interesting | Wrong. Requirements come from users |
| A golden path that is the easiest route, with escape hatches | Right |
| A golden path that is the only permitted route | Wrong. That is a gate, not a paved road |
| Rebuilding what a managed service already provides | Wrong, absent a stated reason |
| Reducing the number of concepts a developer must hold | Right. Cognitive load is the point |
| Measuring adoption, satisfaction, and DORA | Right |
| Measuring lines of platform code or tickets closed | Wrong. Vanity metrics |

## Phase 1: Fundamentals (week 1-2), 36% of the exam

Get these definitions exact:

- **Platform**: a curated set of capabilities, offered as a product, that reduces cognitive load for the teams using it.
- **Golden path**: an opinionated, supported, well-documented route through a common task. It is the easiest option, not the only one.
- **Thinnest viable platform**: the smallest thing that delivers value. It may be a wiki page and two scripts at first.
- **Cognitive load**: the mental effort a team must expend. Platforms exist to reduce extraneous load so teams spend it on their domain.

The **maturity model** deserves memorization. Levels run provisional, operational, scalable, optimizing, assessed across attributes including investment, adoption, interfaces, operations, and measurement. Questions describe an organization and ask which level it sits at for a given attribute.

## Phase 2: Multi-tenancy and conformance (week 3)

The isolation spectrum, with its trade-offs, is the most testable technical content:

| Model | Isolation | Cost | Fits |
|---|---|---|---|
| **Namespace per tenant** | Weakest; shared control plane and nodes | Lowest | Trusted internal tenants |
| **Node pool per tenant** | Better; workloads separated at the node level | Medium | Compliance-sensitive workloads sharing a cluster |
| **Cluster per tenant** | Strong; separate control plane | High | Regulatory or hostile multi-tenancy |
| **Control plane per tenant** (vCluster and similar) | Strong logical, shared physical | Medium | Many tenants needing cluster-level API access |

**Conformance** is the platform's mechanism for making sure what runs on it meets requirements. Policy engines (Kyverno, Gatekeeper) enforce at admission; the platform then produces compliance evidence as a by-product rather than through manual collection.

## Phase 3: APIs and provisioning (week 4)

The key insight: **the Kubernetes API is a platform API**. Custom resources are the interface, and controllers are what make them real.

**Crossplane** takes this further: define a **composite resource** that expands into cloud infrastructure, and expose a simplified **claim** to developers. The developer asks for a database; the composition creates the RDS instance, subnet group, parameter group, secret, and network rules.

That is the abstraction question in miniature: expose the claim, hide the composition, and be deliberate about what leaks through.

## Phase 4: Experience and measurement (week 5)

**Platform versus portal** is a distinction the exam tests: the **Internal Developer Platform** is the capability layer; the **Internal Developer Portal** (Backstage and similar) is a user interface onto it. A portal without a platform behind it is a catalog of links.

**Measurement**: DORA for delivery performance, SPACE for developer productivity dimensions, adoption for whether anyone wants it, and satisfaction for whether they like it. Cost visibility through showback, and chargeback only where the organization genuinely wants tenants to feel the price.

## Common traps

| Trap | Reality |
|---|---|
| Treating CNPA as a Kubernetes exam | It assumes Kubernetes and tests the layer above |
| Choosing the most capable option | The right answer usually reduces what developers must know |
| Mandating adoption to drive numbers | The exam treats this as an anti-pattern |
| Cluster-per-tenant as the default | Expensive; namespace isolation is often sufficient for trusted tenants |
| Confusing IDP the platform with IDP the portal | Different things, and the exam separates them |
| Building a platform team as a ticket queue | The self-service model is the point |

## Exam day

- **120 minutes** for 60 questions, more generous than other CNCF associate exams, because scenario questions are longer.
- Read the full scenario. The constraint is often in the last sentence.
- 75% to pass, roughly 45 of 60.
- One free retake included.

## Related

- [Practice plan](./practice-plan.md)
- [Scenarios](./scenarios.md)
- [Fact sheet](./fact-sheet.md)
- [Platform Engineer roadmap](../../../resources/certification-roadmap-platform-engineer.md)
