---
last-updated: 2026-08-09
difficulty: advanced
---

# Istio Certified Associate (ICA) - Practice Questions

15 questions for ICA prep across installation, traffic management, security, observability, resilience, troubleshooting, and multi-cluster and ambient mode.

ICA is performance-based in a live cluster. These questions target the configuration reasoning behind the tasks.

> **Cert page:** [exams/kubernetes/ica/](../../exams/kubernetes/ica/)

---

### Question 1
**Scenario:** Traffic must be split 90/10 between two versions of a service. Which two resources are required?

A. Gateway and ServiceEntry
B. VirtualService for the weights and DestinationRule defining the subsets
C. VirtualService alone
D. PeerAuthentication and AuthorizationPolicy

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The VirtualService routes and carries the weights, but it refers to subsets by name, and those names have to be defined in a DestinationRule with the label selectors that identify each version. Forgetting the DestinationRule produces a route to a subset that does not resolve, which is a classic first mistake.
</details>

---

### Question 2
**Scenario:** You want strict mTLS for all workloads in the `payments` namespace.

A. A `PeerAuthentication` in the `payments` namespace with `mtls.mode: STRICT`
B. An `AuthorizationPolicy` with `action: ALLOW`
C. A `DestinationRule` with `tls.mode: DISABLE`
D. A NetworkPolicy

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** PeerAuthentication controls whether the sidecar accepts plaintext. `STRICT` refuses non-mTLS traffic. AuthorizationPolicy decides who may call what once identity is established, which is a different question. A DestinationRule with `DISABLE` would do the opposite on the client side, and NetworkPolicy operates at L3/L4 without identity.
</details>

---

### Question 3
**Scenario:** After enabling STRICT mTLS, one legacy client without a sidecar starts failing.

A. Delete the PeerAuthentication
B. Use a workload-scoped PeerAuthentication in `PERMISSIVE` mode for that workload while it is migrated
C. Disable the mesh
D. Add a Gateway

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PeerAuthentication can be scoped mesh-wide, per namespace, or per workload with a selector, and more specific wins. `PERMISSIVE` accepts both mTLS and plaintext, which is exactly the migration mode. Reverting the whole namespace throws away the security you just gained for one laggard.
</details>

---

### Question 4
**Scenario:** External HTTP traffic must enter the mesh on a hostname with TLS termination.

A. A Gateway resource binding the host and TLS config, plus a VirtualService attached to that gateway
B. A VirtualService alone
C. A ServiceEntry
D. A Sidecar resource

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Gateway configures the ingress proxy's listener, ports, hosts, and TLS. The VirtualService must then list that gateway in its `gateways` field to attach routing rules to it. A VirtualService without the gateway reference applies only to mesh-internal traffic.
</details>

---

### Question 5
**Scenario:** A workload must reach an external API not registered in the mesh, and the mesh outbound policy is `REGISTRY_ONLY`.

A. A ServiceEntry describing the external host
B. A DestinationRule
C. A NetworkPolicy
D. Nothing, external traffic always works

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** With `REGISTRY_ONLY`, the sidecar blocks anything not in the service registry. A ServiceEntry adds the external host to that registry so it can be routed and observed. Under the default `ALLOW_ANY` it would have worked without one, which is why understanding the outbound traffic policy setting matters.
</details>

---

### Question 6
**Scenario:** Which AuthorizationPolicy behavior is correct when a namespace has one policy with `action: ALLOW` and rules matching only `service-a`?

A. All traffic is allowed
B. Only traffic matching the rule is allowed; everything else to selected workloads is denied
C. Only `service-a` is denied
D. The policy is ignored without a PeerAuthentication

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Once any ALLOW policy selects a workload, that workload is default-deny for anything not matched. This surprises people who expect an allow-list to be additive on top of open access. DENY policies are evaluated before ALLOW, and CUSTOM policies delegate to an external authorizer.
</details>

---

### Question 7
**Scenario:** A service should stop receiving traffic from a client after 5 consecutive 5xx responses.

A. A retry policy
B. Outlier detection in the DestinationRule's `trafficPolicy`
C. A timeout
D. A fault injection rule

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Outlier detection is Istio's circuit breaking for unhealthy endpoints: consecutive errors eject the host from the load balancing pool for a base ejection time. Retries would send more traffic at a failing host. Timeouts bound a single request. Fault injection deliberately creates failures for testing.
</details>

---

### Question 8
**Scenario:** You want to test how the application behaves when a dependency is slow, without changing the dependency.

A. Fault injection with a `delay` in the VirtualService
B. Reduce the dependency's replicas
C. Add a timeout
D. Enable tracing

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Fault injection lets you add a fixed delay or an abort to a percentage of requests declaratively, which is chaos testing without touching either service. Scaling down changes capacity unpredictably rather than injecting a controlled fault. Timeouts and tracing observe or bound behavior instead of causing it.
</details>

---

### Question 9
**Scenario:** `istioctl analyze` reports a VirtualService referencing a host that does not exist.

A. Ignore it, analysis is advisory
B. It is a real misconfiguration: the route will not resolve, so fix the host or add a ServiceEntry
C. Restart istiod
D. Reinstall the mesh

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `istioctl analyze` catches exactly the class of errors that produce silent 404s and no obvious log line. An unresolvable host means Envoy has no cluster to route to. Treat analyzer errors as blocking, and use `istioctl proxy-config` to confirm what the sidecar actually received.
</details>

---

### Question 10
**Scenario:** A sidecar is not injected into new pods in a namespace.

A. Check the `istio-injection=enabled` label on the namespace or the `sidecar.istio.io/inject` annotation on the pod
B. Restart the pods
C. Reinstall Istio
D. Check the NetworkPolicy

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Automatic injection is driven by a mutating webhook that keys off the namespace label (or the revision label when using revisions). Pod-level annotations can opt individual workloads in or out. Injection also only happens at pod creation, so existing pods need to be recreated after labeling.
</details>

---

### Question 11
**Scenario:** What does ambient mode change compared with the sidecar data plane?

A. It removes mTLS
B. It moves L4 handling to a per-node ztunnel and makes L7 processing optional through waypoint proxies
C. It requires one proxy per container
D. It only works on a single cluster

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Ambient splits the data plane: ztunnel runs per node and provides mTLS and L4 authorization with no pod restart needed, and a waypoint proxy is deployed only where L7 features such as HTTP routing or request-level authorization are required. That reduces per-pod resource overhead and removes the sidecar injection lifecycle.
</details>

---

### Question 12
**Scenario:** You need distributed traces across services in the mesh.

A. Istio generates spans in the sidecars, but applications must propagate the trace headers
B. Istio produces complete traces with no application change
C. Tracing requires rewriting services with the OpenTelemetry SDK
D. Traces come from Prometheus

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The sidecar can create a span for each hop, but it cannot know that an inbound request caused a given outbound request unless the application copies the trace context headers (`traceparent` or the b3 set) from one to the other. This "mesh gives you tracing for free" misconception is worth being precise about.
</details>

---

### Question 13
**Scenario:** A large mesh has slow sidecar startup and high memory use because every proxy receives config for every service.

A. Add more CPU
B. Use a `Sidecar` resource to scope each workload's visible services
C. Disable mTLS
D. Reduce the number of VirtualServices

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** By default istiod pushes the full service registry to every proxy. A `Sidecar` resource with an `egress.hosts` list restricts what a workload is told about, which cuts config size and push cost substantially in big meshes. `exportTo` on services and VirtualServices achieves a similar narrowing from the other direction.
</details>

---

### Question 14
**Scenario:** Which upgrade approach lets you move workloads to a new Istio version gradually?

A. In-place upgrade of istiod
B. Revision-based (canary) upgrade with a new control plane revision and namespace revision labels
C. Delete and reinstall
D. Upgrading the CNI only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Revisions install a second control plane alongside the first. You relabel a namespace to the new revision and restart its workloads, so exposure is one namespace at a time and rollback is a relabel. In-place upgrades change every proxy's control plane at once.
</details>

---

### Question 15
**Scenario:** Two clusters should share one mesh with services reachable across both.

A. A multi-primary or primary-remote setup with a shared trust root and east-west gateways
B. Two independent meshes with a VPN
C. A single Gateway resource
D. Federating Prometheus

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Multi-cluster requires a common root of trust so workload identities validate across clusters, endpoint discovery between control planes, and east-west gateways when pod IPs are not directly routable. A VPN gives connectivity without shared identity or service discovery, and Prometheus federation is only observability.
</details>

---

## Where to go deeper

- [ICA cert page](../../exams/kubernetes/ica/) - notes, practice plan, strategy
- [CKA practice questions](./kubernetes-cka.md) - the Kubernetes baseline ICA assumes
- [Kubernetes topic index](../../topics/kubernetes.md) - service mesh in context
- [Zero trust architecture](../architecture-patterns/zero-trust-architecture.md) - the identity model mTLS implements
- **[📖 Istio documentation](https://istio.io/latest/docs/)** - primary source
