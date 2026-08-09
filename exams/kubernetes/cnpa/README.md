---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 5 min
---

# Cloud Native Platform Engineering Associate (CNPA)

Platform engineering as a discipline: building an internal platform as a product, with golden paths, self-service APIs, conformance guardrails, and measurement that tells you whether any of it is working.

CNPA is **not** an operations exam. It assumes Kubernetes knowledge and tests the layer above: what to build, for whom, how to expose it, and how to know if it succeeded.

## Exam Details

- **Exam Code:** CNPA
- **Duration:** 120 minutes (longer than other CNCF associate exams)
- **Questions:** 60, multiple choice and multiple select
- **Passing Score:** 75%
- **Cost:** USD 250, includes one free retake
- **Validity:** 2 years
- **Prerequisites:** None formal; cloud native fundamentals assumed
- **Format:** Knowledge-based, not hands-on

Full detail in the [fact sheet](./fact-sheet.md).

## Domains and notes

| Notes | Domains covered | Combined weight |
|---|---|---:|
| [01 Platform fundamentals](./notes/01-platform-fundamentals.md) | Core Fundamentals (36%) | 36% |
| [02 Observability, security, conformance](./notes/02-observability-security-conformance.md) | Observability, Security, Conformance (20%) | 20% |
| [03 Delivery, APIs, provisioning](./notes/03-delivery-apis-provisioning.md) | Continuous Delivery (16%), Platform APIs (12%) | 28% |
| [04 Developer experience and measurement](./notes/04-developer-experience-and-measurement.md) | IDPs and DX (8%), Measuring (8%) | 16% |

## The idea the exam is built on

**A platform is a product, and its users are engineers who can choose not to use it.**

That single framing generates most of the correct answers:

- If nobody adopts it voluntarily, it has failed, regardless of technical quality. Mandating adoption hides the failure rather than fixing it.
- The value is **reduced cognitive load**, not more capability. A platform that adds concepts developers must learn has made things worse.
- **Golden paths** are opinionated defaults that are the easiest route, not the only route. A platform that forbids alternatives is a gate, not a paved road.
- Requirements come from **user research and feedback**, not from what the platform team finds interesting to build.
- The **thinnest viable platform** is the goal: build the least that delivers value, and prefer a managed service over building your own.

Whenever an option describes mandating, gating, or building something a managed service already provides, it is usually the wrong answer.

## Study sequence

1. **Read the CNCF Platforms White Paper.** It is the syllabus, and it is short.
2. **Read the Platform Engineering Maturity Model.** The attributes and levels are directly testable.
3. Core fundamentals, which is 36% of the exam.
4. Observability, multi-tenancy, and conformance.
5. Delivery, platform APIs, and provisioning.
6. Developer experience and measurement.

Schedule in the [practice plan](./practice-plan.md).

## Study resources

- **[📖 CNCF Platforms White Paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)** - the primary source
- **[📖 CNCF Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)** - levels and attributes
- **[📖 CNPA curriculum](https://github.com/cncf/curriculum)** - published domains
- **[📖 Backstage documentation](https://backstage.io/docs/overview/what-is-backstage)** - the reference portal implementation
- **[📖 Crossplane documentation](https://docs.crossplane.io/)** - the reference control plane implementation
- **[📖 Team Topologies](https://teamtopologies.com/)** - the team-shape vocabulary the white paper uses
- [Practice questions](../../../resources/practice-questions/cncf-cnpa.md) - question bank in this repo

## Related

- [Platform Engineer roadmap](../../../resources/certification-roadmap-platform-engineer.md)
- [CGOA](../cgoa/) - GitOps, the delivery model platforms usually adopt
- [OTCA](../otca/) - observability, a platform capability
- [CKA](../cka/) - the Kubernetes layer assumed
- [CAPA](../capa/) - Argo tooling many platforms build on
