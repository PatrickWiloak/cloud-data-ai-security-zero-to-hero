---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 8 min
---

# CNPA High-Yield Scenarios

---

## Scenario 1: Nobody is using the platform

**Scenario**: A platform team spent a year building a deployment system. Six months after launch, four of forty teams use it. The rest still deploy with their own scripts. Leadership proposes mandating the platform.

**Solution Pattern**:
- **Do not mandate.** Low voluntary adoption is a product signal, and a mandate hides it while creating resentment
- Run **user research**: interview the thirty-six non-adopting teams and find out what the platform costs them that their scripts do not
- Common causes: the platform solves a problem teams do not have, onboarding is slower than the status quo, it lacks an escape hatch for a legitimate edge case, or documentation is poor
- Identify the **golden path** for the most common workload and make it genuinely the easiest route
- Reduce **time to first deployment** as the headline metric
- Treat the four adopting teams as design partners, and publish a roadmap informed by the feedback

**Common Distractors**:
- Mandating use (the anti-pattern the exam is testing)
- Adding more features (the problem is rarely missing capability)
- Building a portal on top (a nicer front door to something people do not want)

**Key Takeaway**: Voluntary adoption is the honest measure of platform success. When it is low, the answer is user research and a better golden path, never a mandate.

---

## Scenario 2: Choosing a tenancy model

**Scenario**: A platform must host workloads from three groups: forty internal product teams with normal trust, a regulated payments division requiring documented isolation, and an external partner running code the company does not control.

**Solution Pattern**:
- **Internal product teams**: **namespace per team** with RBAC, resource quotas, network policy, and admission control. Cheapest, and appropriate for trusted tenants
- **Payments division**: **dedicated node pools** within a cluster, or a **dedicated cluster** if the regulatory scope must be clean. Separation should align with the compliance boundary so audit scoping is simple
- **External partner**: **dedicated cluster** with strong runtime isolation, and consider sandboxed runtimes such as gVisor or Kata Containers, because the code is untrusted
- Apply consistent policy across all three through **policy as code**, so the platform's guarantees do not depend on which model a tenant sits in

**Common Distractors**:
- One model for everyone (either overspends on the internal teams or under-isolates the partner)
- Namespace isolation for the untrusted partner (a shared kernel and control plane is not a trust boundary against hostile code)
- Cluster per team for all forty (cost and operational load with no corresponding benefit)

**Key Takeaway**: Match the isolation model to the trust level and the compliance boundary. Namespace isolation is sufficient for trusted tenants and insufficient for untrusted code.

---

## Scenario 3: Golden path with an escape hatch

**Scenario**: The platform offers one supported way to deploy a stateless HTTP service. A team needs to run a workload requiring a GPU and a custom scheduler, which the golden path does not support. They ask for an exception.

**Solution Pattern**:
- **Grant the exception** and keep the guardrails: the workload still passes admission policy, still emits telemetry, still meets supply chain requirements
- Golden paths are the easiest route, not the only route. Blocking a legitimate need turns the platform into a gate and pushes teams to route around it entirely
- **Record the exception as product input.** If several teams need GPUs, that is a signal for a second golden path, not a series of one-off approvals
- Maintain a **thin conformance layer** that applies to everything, whether on the golden path or not, so exceptions do not become policy holes

**Common Distractors**:
- Refusing the exception (drives shadow platforms and loses visibility entirely)
- Granting it with no guardrails (loses conformance and observability)
- Immediately building GPU support for one team (premature; wait for the pattern)

**Key Takeaway**: Golden paths need escape hatches, and exceptions are product signal. What must never be optional is the thin conformance layer: policy, telemetry, and supply chain requirements.

---

## Scenario 4: Self-service database provisioning

**Scenario**: Developers wait five days for a database because they file a ticket and the platform team runs Terraform manually. The team wants self-service without giving developers cloud console access or Terraform state.

**Solution Pattern**:
- A **control plane pattern**: Crossplane with a **composite resource definition** describing a Database abstraction, and a **composition** that expands it into the real cloud resources (instance, subnet group, parameter group, secret, firewall rules, backups)
- Developers submit a small **claim**: engine, size class, environment. Everything else is defaulted by the composition
- The claim lives in the team's Git repository and is applied by the GitOps agent, so provisioning follows the same review path as everything else
- **Policy** constrains what a claim may request: allowed size classes per environment, mandatory encryption, mandatory backup retention
- The platform team owns the composition and can change the underlying implementation without changing the developer-facing API

**Common Distractors**:
- Giving developers Terraform and cloud credentials (fast, and abandons the guardrails and the abstraction)
- A web form that files a ticket faster (still ticket-driven; the wait is the problem)
- Exposing the full cloud resource as a custom resource (leaks the complexity the abstraction exists to hide)

**Key Takeaway**: Expose a simple claim, hide the composition, constrain with policy. The platform API is the product surface, and its stability is what lets the implementation change underneath.

---

## Scenario 5: Measuring the platform

**Scenario**: A platform team is asked to justify its budget. It proposes reporting the number of features shipped, lines of platform code, and tickets closed.

**Solution Pattern**:
Replace all three with measures of outcome:
- **DORA metrics** for delivery performance: deployment frequency, lead time for changes, change failure rate, time to restore service, measured for teams on the platform
- **Adoption**: what proportion of eligible teams and workloads use it, voluntarily
- **Time to first deployment** for a new service or a new engineer
- **Developer satisfaction**, surveyed regularly, with qualitative comments
- **Platform SLOs**: availability and latency of the capabilities the platform offers
- **Cost per workload**, with showback so teams can see what they consume

Tickets closed is actively misleading: a successful self-service platform should drive the ticket count **down**.

**Common Distractors**:
- Features shipped (output, not outcome)
- Lines of code (measures effort, not value)
- Tickets closed (inversely correlated with success)
- Uptime alone (necessary, not sufficient; a reliable platform nobody uses is still a failure)

**Key Takeaway**: Measure outcomes for platform users, not the platform team's output. DORA, adoption, time to first deployment, satisfaction, and platform SLOs. Vanity metrics are a reliable wrong answer.

---

## Scenario 6: Platform or portal

**Scenario**: Leadership asks the team to "build an IDP" and points at Backstage. The team installs Backstage, imports a service catalog, and after three months developers say nothing has improved.

**Solution Pattern**:
- Distinguish the two: an **Internal Developer Platform** is the capability layer (provisioning, delivery, observability, guardrails); an **Internal Developer Portal** is a user interface onto it
- Backstage without capabilities behind it is a catalog of links, which is why nothing improved
- Build the **capabilities first**: self-service environment provisioning, a golden path for the commonest workload, and delivery automation
- Then use the portal as a **discovery and scaffolding surface**: software templates that instantiate a golden path, TechDocs for documentation, and the catalog for ownership
- Both matter; the ordering is what was wrong

**Common Distractors**:
- Adding more Backstage plugins (more surface onto the same absent capability)
- Abandoning the portal (it has real value once there is something to surface)
- Treating the catalog as the deliverable (an inventory is not a capability)

**Key Takeaway**: Platform is capability, portal is interface. A portal makes a good platform discoverable and does nothing for a platform that does not exist.

---

## Scenario 7: Conformance without blocking delivery

**Scenario**: Security requires that every production image is signed, has no critical CVEs, declares resource limits, and does not run as root. The platform team must enforce this without becoming a review bottleneck.

**Solution Pattern**:
- **Policy as code** at admission with Kyverno or OPA Gatekeeper, so enforcement is automatic and uniform
- **Signature and provenance verification** as an admission check against a trusted key or a Sigstore identity
- Roll out in **audit mode first**, publish the violations to teams, then enforce once the noise is understood
- Provide the **golden path** that satisfies the policy by default, so compliance is the path of least resistance rather than a hurdle
- Emit **compliance evidence** from the platform automatically, so audits query the platform rather than asking teams for screenshots
- Reserve human review for policy **exceptions**, not for every deployment

**Common Distractors**:
- Manual security review per release (the bottleneck they asked to avoid)
- A CI-only check (bypassable by anyone deploying outside the pipeline; admission control is the enforcement point)
- Enforcing immediately without an audit phase (breaks delivery and destroys goodwill)

**Key Takeaway**: Enforce at admission, roll out in audit mode first, and make the compliant path the easiest one. The platform's job is to make the right thing automatic, then produce the evidence as a by-product.

---

## Related

- [Practice plan](./practice-plan.md)
- [Strategy](./strategy.md)
- [Notes](./notes/)
- [Platform Engineer roadmap](../../../resources/certification-roadmap-platform-engineer.md)
- [Practice questions](../../../resources/practice-questions/cncf-cnpa.md)
