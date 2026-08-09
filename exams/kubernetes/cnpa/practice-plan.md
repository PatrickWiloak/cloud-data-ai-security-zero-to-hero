---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 4 min
---

# CNPA Study Plan

Five weeks at 4-6 hours per week. This is a concepts exam; reading and reasoning matter more than lab time.

## Week 1: The white paper and platform fundamentals

- [ ] Read the [CNCF Platforms White Paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/) end to end
- [ ] Define, in your own words: platform, product, golden path, cognitive load, thinnest viable platform
- [ ] Platform as a product: users, value, roadmap, feedback, voluntary adoption
- [ ] Why mandating adoption is an anti-pattern
- [ ] Team Topologies vocabulary: platform team, enabling team, stream-aligned team, cognitive load
- [ ] Interfaces and abstractions: what to hide, what to expose, leaky abstractions
- [ ] Review Notes: `notes/01-platform-fundamentals.md`

## Week 2: Maturity model and platform boundaries

- [ ] Read the [Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)
- [ ] The levels: provisional, operational, scalable, optimizing
- [ ] The attributes: investment, adoption, interfaces, operations, measurement
- [ ] Place a platform you know at a level for each attribute, and justify it
- [ ] Anti-patterns: no users, mandated adoption, rebuilding managed services, ticket-queue platform teams
- [ ] Where a platform should stop, and when to buy rather than build

## Week 3: Observability, security, and conformance

- [ ] Platform observability versus observability offered to tenants
- [ ] SLOs for platform capabilities and error budgets
- [ ] Multi-tenancy models: namespace, cluster, and control plane isolation, with trade-offs
- [ ] Tenant isolation controls: RBAC, network policy, quotas, admission control, runtime isolation
- [ ] Policy as code with Kyverno and OPA Gatekeeper
- [ ] Supply chain: signing, provenance, SBOMs, admission verification
- [ ] Conformance validation and compliance evidence as a platform output
- [ ] Review Notes: `notes/02-observability-security-conformance.md`

## Week 4: Delivery, APIs, and provisioning

- [ ] CI and CD boundaries in a platform context
- [ ] GitOps as the delivery model; who owns what between platform and tenant
- [ ] Progressive delivery and preview environments as self-service capabilities
- [ ] The Kubernetes API as a platform API; custom resources as the interface
- [ ] Operators and controllers as the reconciliation mechanism
- [ ] Crossplane and control plane patterns; composition and claims
- [ ] API design: versioning, deprecation, defaults, validation
- [ ] Review Notes: `notes/03-delivery-apis-provisioning.md`

## Week 5: Developer experience, measurement, and review

- [ ] Internal Developer Platform versus Internal Developer Portal
- [ ] Backstage: catalog, software templates, TechDocs, scaffolding
- [ ] Onboarding and time to first deployment
- [ ] DORA metrics, and what each one tells you
- [ ] SPACE framework dimensions
- [ ] Adoption, satisfaction, cost, showback and chargeback
- [ ] Vanity metrics versus actionable ones
- [ ] Review Notes: `notes/04-developer-experience-and-measurement.md`
- [ ] Work every scenario in [scenarios.md](./scenarios.md)
- [ ] Two timed practice exams

## Readiness check

- [ ] Explain what makes something a platform rather than a collection of tools
- [ ] Define a golden path and say why it must not be the only path
- [ ] Argue why mandating adoption hides failure
- [ ] Place a platform on the maturity model across all attributes
- [ ] Compare namespace, cluster, and control plane multi-tenancy with a use case for each
- [ ] Explain the difference between an Internal Developer Platform and a portal
- [ ] Name the four DORA metrics and what each reveals
- [ ] Explain what a Crossplane composition and claim do
