---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 10 min
---

# 02 - Platform observability, security, and conformance

**Domain 2: Platform Observability, Security, and Conformance (20%)**

---

## Two kinds of observability

A platform has both, and the exam distinguishes them:

- **Observability of the platform**: is the platform itself healthy? Provisioning latency, API availability, delivery pipeline success rate, control plane health. Measured against **platform SLOs**.
- **Observability as a capability**: what the platform gives tenants so their workloads are observable by default. Automatic metrics scraping, log shipping, trace collection, and dashboards a team gets without configuring anything.

The second is a golden path in its own right. A platform where each team must wire up its own telemetry has not reduced cognitive load.

**OpenTelemetry** is the standard collection layer, which is why [OTCA](../../otca/) knowledge composes with this exam.

**Platform SLOs** should describe capabilities users care about: "a namespace claim is fulfilled within 5 minutes, 99% of the time", not "the controller pod is up".

---

## Multi-tenancy

The isolation spectrum, weakest to strongest:

| Model | Boundary | Trade-off | Fits |
|---|---|---|---|
| **Namespace per tenant** | Kubernetes API objects, RBAC, quotas | Shared control plane, shared nodes, shared kernel | Trusted internal teams |
| **Node pool per tenant** | Workloads on dedicated nodes | Higher cost, still one control plane | Compliance-sensitive workloads |
| **Virtual control plane** (vCluster and similar) | A per-tenant API server on shared infrastructure | Logical isolation, shared physical resources | Many tenants needing cluster-level API access |
| **Cluster per tenant** | Full separation | Highest cost and operational load | Regulatory boundaries, untrusted code |

**Namespace isolation is not a security boundary against hostile code**, because the kernel and control plane are shared. Untrusted workloads need at least node-level separation and usually a sandboxed runtime such as gVisor or Kata Containers.

Align the isolation boundary with the **compliance boundary** so that audit scoping is straightforward.

### Tenant isolation controls

- **RBAC** scoped to the tenant's namespaces
- **ResourceQuota** and **LimitRange** so one tenant cannot exhaust the cluster
- **NetworkPolicy** default-deny between tenants
- **Admission control** enforcing what may be created
- **PriorityClass** governance so tenants cannot self-elevate scheduling priority
- **Runtime isolation** where the workload is untrusted

---

## Policy as code and conformance

**Conformance** is the platform's mechanism for guaranteeing that what runs on it meets requirements.

Policy engines:
- **Kyverno** - Kubernetes-native, policies written as YAML resources. Lower learning curve
- **OPA Gatekeeper** - policies in Rego, more expressive, steeper learning curve

Both operate as **admission controllers**, so enforcement happens before a resource is persisted, and both support **validate**, **mutate**, and **generate** behaviors. Mutation is useful for a platform: default a missing security context or inject a required label rather than rejecting the request.

**Rollout discipline**: audit mode first, publish violations to teams, provide a compliant golden path, then enforce. Enforcing on day one breaks delivery and costs the platform its goodwill.

**Enforcement point matters.** A CI-only check is bypassable by anyone who deploys outside the pipeline. Admission control is the enforcement point because everything reaching the cluster passes through it.

---

## Supply chain security

The platform is the natural place to enforce supply chain requirements once, for everyone:

- **Image signing** with Sigstore and cosign, verified at admission
- **Provenance attestation** linking an image to the source and build that produced it, aligned to SLSA levels
- **SBOM** generation and storage per artifact
- **Vulnerability scanning** at build and continuously in the registry
- **Registry allowlisting**, so only approved registries may be pulled from
- **Base image curation**, so the golden path includes a maintained, minimal base

The platform's advantage is uniformity: one policy covers every workload, and the evidence is produced automatically.

---

## Secrets

Multi-tenant secret management patterns:
- **External store** (Vault, cloud secret managers) with per-tenant paths and policies
- **External Secrets Operator** so tenants reference secrets without them entering Git
- **Workload identity** so applications authenticate to cloud services without any stored credential at all
- Per-tenant encryption keys where the compliance posture requires separation

The platform should make the secure pattern the default, so a tenant does not have to know why a Kubernetes Secret alone is insufficient.

---

## Compliance evidence

A mature platform produces compliance evidence as a **by-product** rather than through manual collection: policy decisions logged, admission denials recorded, provenance stored, and access audited. Auditors query the platform instead of asking forty teams for screenshots.

This is a strong argument for platform investment and a recurring exam theme.

---

## Key terms

- **Platform SLO** - a service level objective describing a platform capability from the user's perspective
- **Observability as a capability** - telemetry a tenant receives by default without configuring it
- **Namespace tenancy** - the lightest multi-tenancy model, appropriate for trusted internal tenants
- **Virtual control plane** - a per-tenant API server on shared infrastructure, giving cluster-level access without a full cluster
- **Sandboxed runtime** - a container runtime such as gVisor or Kata Containers providing stronger isolation for untrusted code
- **ResourceQuota** - the Kubernetes object limiting aggregate resource consumption within a namespace
- **Conformance** - validation that workloads and clusters meet the platform's stated requirements
- **Policy as code** - expressing organizational rules as machine-enforced policy, typically at admission
- **Kyverno** - a Kubernetes-native policy engine with policies written as YAML resources
- **OPA Gatekeeper** - a policy engine using Rego, offering greater expressiveness
- **Admission controller** - the Kubernetes component validating or mutating resources before they are persisted
- **Audit mode** - a policy rollout state that records violations without blocking them
- **Provenance attestation** - signed metadata linking an artifact to the source and build process that produced it
- **SBOM** - a software bill of materials enumerating the components inside an artifact
- **Registry allowlist** - a policy restricting which container registries images may be pulled from
- **Compliance evidence** - audit artifacts produced automatically by the platform rather than collected manually

---

## Related

- [Notes 03: delivery, APIs, and provisioning](./03-delivery-apis-provisioning.md)
- [Scenarios](../scenarios.md) - scenarios 2 and 7
- [AI security](../../../../resources/ai-security/) - supply chain thinking applied to models
