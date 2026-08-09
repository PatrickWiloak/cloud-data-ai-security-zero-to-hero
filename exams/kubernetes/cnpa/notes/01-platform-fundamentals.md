---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 12 min
---

# 01 - Platform engineering fundamentals

**Domain 1: Platform Engineering Core Fundamentals (36%)** - the largest domain.

Source material: the [CNCF Platforms White Paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/) and the [Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/).

---

## What a platform is

> A platform is a curated set of capabilities, offered as a product, that reduces the cognitive load on the teams using it.

Three parts, all load-bearing:

- **Curated** - opinionated selection, not every tool available. A wiki listing forty options is not a platform.
- **Offered as a product** - it has users, a value proposition, a roadmap, and feedback loops. Users may decline to use it.
- **Reduces cognitive load** - if developers must learn more concepts than before, the platform has made things worse regardless of its capability.

A platform is not the same as a collection of tools. Kubernetes plus Terraform plus a CI system is infrastructure. A platform is what you build on top so that a developer can accomplish a task without understanding all three.

---

## Platform as a product

The framing that generates most correct exam answers.

| Product discipline | Platform equivalent |
|---|---|
| Know your users | Interview the engineering teams; segment them by need |
| Value proposition | State what problem the platform solves and for whom |
| Roadmap | Publish it; let users influence priority |
| Feedback loops | Surveys, office hours, support channels, adoption telemetry |
| Marketing | Internal advocacy, documentation, demos, onboarding sessions |
| Success measure | **Voluntary adoption**, not compliance with a mandate |

**Mandating adoption is an anti-pattern.** A mandate converts a product signal into a compliance exercise: you stop learning whether the platform is good and start learning whether people follow rules. If adoption is low, the platform has a product problem.

---

## Golden paths

A **golden path** (or paved road) is an opinionated, supported, documented route through a common task.

Properties:
- **Easiest**, so teams choose it because it is less work, not because they must
- **Supported**, so the platform team owns its reliability and keeps it current
- **Opinionated**, so it makes decisions the team does not have to make
- **Not the only path**, so legitimate edge cases have an escape hatch

Escape hatches matter. A platform that forbids alternatives becomes a gate, teams route around it, and the platform loses both adoption and visibility. What must remain non-optional is the **thin conformance layer**: policy, telemetry, and supply chain requirements apply whether or not a workload is on the golden path.

---

## Cognitive load

Borrowed from **Team Topologies**, and the central justification for platform work.

- **Intrinsic** load: inherent to the problem domain
- **Extraneous** load: imposed by the environment, tools, and process
- **Germane** load: effort spent building useful understanding

Platforms exist to cut extraneous load so teams can spend their capacity on their domain. A developer who must understand VPC peering, IAM trust policies, Helm chart internals, and a CI DSL to ship a web service is carrying extraneous load the platform should absorb.

Team Topologies vocabulary the white paper uses:
- **Stream-aligned team** - delivers value for a business stream; the platform's user
- **Platform team** - provides internal services that reduce stream-aligned teams' cognitive load
- **Enabling team** - helps other teams build capability, temporarily
- **Complicated subsystem team** - owns something requiring deep specializt knowledge

---

## Interfaces and abstractions

The central design question: **what to hide and what to expose.**

- A good abstraction lets a user express intent (`I need a Postgres database for staging`) without the implementation (instance class, subnet group, parameter group, backup policy, secret rotation).
- A **leaky abstraction** forces the user to understand the layer underneath anyway, which is worse than no abstraction because they now have two things to learn.
- Interfaces should be **stable** even when the implementation changes. That stability is what allows the platform team to migrate underlying infrastructure without a coordinated change across forty teams.

Interface types a platform offers: declarative APIs (custom resources), CLI, portal, templates and scaffolding, and documentation. Most platforms offer several onto the same capability.

---

## Thinnest viable platform

Build the least that delivers value.

- A wiki page and two scripts is a legitimate first platform
- Prefer a **managed service** over building your own. Rebuilding what a cloud provider already operates is a recurring anti-pattern
- Add capability when user demand demonstrates it, not in anticipation
- Every capability is a permanent operational commitment

---

## Maturity model

Four levels, assessed per attribute rather than as one overall score.

| Level | Character |
|---|---|
| **Provisional** | Ad hoc, individual effort, no shared definition of the platform |
| **Operational** | Recognized platform, some standardization, still largely reactive |
| **Scalable** | Self-service, product management, measured, growing adoption |
| **Optimizing** | Continuous improvement driven by data, platform evolves with user needs |

Attributes assessed: **investment** (how the organization funds platform work), **adoption** (how users come to it), **interfaces** (how capabilities are consumed), **operations** (how the platform is run), and **measurement** (how success is judged).

Questions typically describe an organization and ask which level fits an attribute. The tell for **provisional** is individual heroics; for **operational**, a team exists but works through tickets; for **scalable**, self-service and product management; for **optimizing**, decisions driven by measurement.

---

## Anti-patterns

- Building without users, or without asking what they need
- Mandating adoption to disguise weak product-market fit
- Rebuilding what a managed service provides
- The platform team as a **ticket queue**, which is the operational-level trap
- Exposing the full complexity of the underlying infrastructure as the "API"
- Treating the portal as the platform
- Measuring output (features, code) rather than outcome (adoption, delivery performance)

---

## Key terms

- **Platform** - a curated set of capabilities offered as a product that reduces cognitive load for its users
- **Platform as a product** - treating the platform as something with users, a value proposition, a roadmap, and voluntary adoption
- **Golden path** - an opinionated, supported, documented route through a common task, easiest but not mandatory
- **Paved road** - a synonym for golden path, emphasizing that the supported route is the smoothest one
- **Escape hatch** - a supported way to deviate from the golden path for a legitimate edge case
- **Thin conformance layer** - the non-optional policy, telemetry, and supply chain requirements applying to all workloads
- **Cognitive load** - the mental effort a team must expend, which platforms exist to reduce
- **Extraneous load** - cognitive load imposed by tooling and process rather than by the problem domain
- **Stream-aligned team** - a team delivering value for a business stream, the platform's primary user
- **Platform team** - a team providing internal services that reduce other teams' cognitive load
- **Enabling team** - a team that temporarily helps others build capability rather than doing the work for them
- **Leaky abstraction** - an interface that still forces users to understand the layer beneath it
- **Thinnest viable platform** - the smallest platform that delivers value, favoring managed services over building
- **Maturity model levels** - provisional, operational, scalable, and optimizing, assessed per attribute
- **Voluntary adoption** - uptake without mandate, treated as the honest measure of platform success

---

## Related

- [Notes 02: observability, security, conformance](./02-observability-security-conformance.md)
- [Scenarios](../scenarios.md) - scenarios 1, 3, and 6
- [Platform Engineer roadmap](../../../../resources/certification-roadmap-platform-engineer.md)
