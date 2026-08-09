---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 10 min
---

# 03 - Delivery, platform APIs, and provisioning

**Domains: Continuous Delivery and Platform Engineering (16%) and Platform APIs and Provisioning Infrastructure (12%)** - 28% combined.

---

## Delivery as a platform capability

The platform's job is not to run every team's pipeline. It is to make the **golden path for delivery** so much easier than rolling your own that teams choose it.

What the platform typically owns:
- Reusable **pipeline templates** for common workload shapes
- The **GitOps** delivery mechanism and the agents that run it
- **Environment provisioning**, including ephemeral preview environments
- **Progressive delivery** capability, so canary and blue-green are a configuration choice rather than a project
- **Artifact management**: registries, retention, promotion between environments
- **Rollback** as a first-class, documented operation

What tenants typically own: their application, their tests, their configuration values, and the decision of when to promote.

Getting this split explicit is a recurring exam theme. A platform that owns tenants' application configuration has taken on unbounded work; a platform that owns none of the delivery mechanism has not reduced cognitive load.

---

## GitOps in a platform context

GitOps (see [CGOA](../../cgoa/)) is the common delivery model, and the platform question is **who owns which repository**.

A workable division:
- **Platform repository**: cluster baselines, policy, platform components, tenant onboarding definitions. Owned by the platform team
- **Tenant repositories**: application manifests and environment overlays. Owned by the stream-aligned team
- The platform **generates** a tenant's Application or Kustomization on onboarding, so a new team gets working delivery without configuring an agent

**Preview environments** are the highest-value self-service capability in many platforms: an environment per pull request, created and destroyed automatically, which removes an entire category of coordination.

---

## The Kubernetes API as a platform API

The insight the domain rests on: **Kubernetes is an extensible API server with a reconciliation engine**, and that makes it a good foundation for a platform API even for things that are not containers.

- **Custom Resource Definitions** add new types to the API
- **Controllers and operators** reconcile those types into real state
- Everything else follows: RBAC, admission control, audit logging, `kubectl`, GitOps agents, and event streams all work on custom resources exactly as they do on built-in ones

That reuse is why platform capabilities are commonly exposed as custom resources rather than as a bespoke REST service.

---

## Control planes and composition

**Crossplane** is the reference implementation of the control plane pattern.

| Object | Role |
|---|---|
| **Provider** | Adds managed resource types for a cloud or service |
| **Managed resource** | A one-to-one representation of a real cloud resource |
| **Composite Resource Definition (XRD)** | Defines the abstract type the platform offers |
| **Composition** | Describes how that abstract type expands into managed resources |
| **Claim** | The namespaced, developer-facing request for an instance |

The developer submits a claim: `engine: postgres, size: small, environment: staging`. The composition expands it into the database instance, subnet group, parameter group, secret, firewall rules, and backup configuration.

Why this beats handing developers Terraform:
- The abstraction is stable while the implementation changes underneath
- Policy constrains what a claim may request
- Reconciliation is continuous, so drift is corrected rather than discovered at the next apply
- The claim lives in Git and follows the same review path as everything else

IaC tools and control planes are not mutually exclusive. Many platforms use Terraform or OpenTofu for foundational, rarely-changing infrastructure and a control plane for the self-service surface.

---

## API design for platforms

A platform API is a product interface, so it needs product discipline:

- **Start narrow.** Expose the smallest field set that covers the common case, and default everything else
- **Version deliberately.** `v1alpha1` signals instability; moving to `v1` is a commitment
- **Deprecate with a path.** Announce, provide a migration, support both for a period
- **Validate early.** Schema validation and admission policy give an immediate, comprehensible error rather than a failure ten minutes into provisioning
- **Default sensibly.** Every field a user must set is cognitive load; every field with a good default is not
- **Resist leaking.** If the abstract type has a field named after an underlying cloud resource's quirk, the abstraction is leaking

The **Kubernetes Resource Model** (declarative spec, observed status, continuous reconciliation) is the pattern to follow, because users already understand it.

---

## Key terms

- **Pipeline template** - a reusable delivery workflow the platform provides so teams do not write their own
- **Preview environment** - an ephemeral environment created per pull request and destroyed on merge or close
- **Custom Resource Definition** - the Kubernetes mechanism adding a new type to the API server
- **Operator** - a controller encoding operational knowledge for a specific application or capability
- **Kubernetes Resource Model** - the declarative spec, observed status, and continuous reconciliation pattern
- **Control plane pattern** - exposing infrastructure provisioning through a reconciling API rather than an imperative tool
- **Crossplane** - the reference implementation of the control plane pattern for cloud infrastructure
- **Provider** - a Crossplane package adding managed resource types for a cloud or service
- **Managed resource** - a Crossplane object corresponding one-to-one with a real external resource
- **Composite Resource Definition** - the Crossplane object defining an abstract, platform-offered type
- **Composition** - the Crossplane definition of how an abstract type expands into managed resources
- **Claim** - the namespaced, developer-facing request for an instance of a composite resource
- **API versioning** - the discipline of signalling stability through alpha, beta, and stable API versions
- **Schema validation** - rejecting invalid input at the API boundary so errors are immediate and comprehensible

---

## Related

- [Notes 04: developer experience and measurement](./04-developer-experience-and-measurement.md)
- [Scenarios](../scenarios.md) - scenario 4
- [CGOA](../../cgoa/) - the delivery model
- [Terraform explained](../../../../learn/concepts/terraform-explained.md)
