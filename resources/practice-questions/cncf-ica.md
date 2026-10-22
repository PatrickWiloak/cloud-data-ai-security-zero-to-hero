---
last-updated: 2026-10-22
difficulty: advanced
---

# Istio Certified Associate (ICA) - Practice Questions

30 questions for ICA prep across installation, traffic management, security, observability, resilience, troubleshooting, and multi-cluster and ambient mode.

ICA is performance-based in a live cluster. These questions target the configuration reasoning behind the tasks.

> **Cert page:** [exams/kubernetes/ica/](../../exams/kubernetes/ica/)

---

### Question 1
**Scenario:** Traffic must be split 90/10 between two versions of a service. Which two resources are required?

A. VirtualService for the weights and DestinationRule defining the subsets and their label selectors
B. PeerAuthentication and AuthorizationPolicy, with weights set in the policy rules
C. VirtualService alone, with weighted destinations that name the version labels directly in the `host` field of each route
D. Gateway and ServiceEntry, where the Gateway carries the weights for the two versions

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The VirtualService routes and carries the weights, but it refers to subsets by name, and those names have to be defined in a DestinationRule with the label selectors that identify each version. Forgetting the DestinationRule produces a route to a subset that does not resolve, which is a classic first mistake.
</details>

---

### Question 2
**Scenario:** You want strict mTLS for all workloads in the `payments` namespace.

A. An `AuthorizationPolicy` with `action: ALLOW` for every service account in the namespace, which makes the sidecars reject plaintext
B. A NetworkPolicy that admits traffic only from pods in the same namespace, which forces mutual TLS between those pods
C. A `PeerAuthentication` in `payments` with `mtls.mode: STRICT`
D. A `DestinationRule` with `tls.mode: DISABLE` on the services in the namespace, to stop their sidecars from accepting plaintext

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** PeerAuthentication controls whether the sidecar accepts plaintext. `STRICT` refuses non-mTLS traffic. AuthorizationPolicy decides who may call what once identity is established, which is a different question. A DestinationRule with `DISABLE` would do the opposite on the client side, and NetworkPolicy operates at L3/L4 without identity.
</details>

---

### Question 3
**Scenario:** After enabling STRICT mTLS, one legacy client without a sidecar starts failing.

A. Delete the PeerAuthentication in the namespace so that the legacy client can connect, and recreate it once the client has been migrated
B. Add a Gateway so the legacy client's plaintext traffic enters through the ingress proxy
C. Disable the mesh for the namespace by removing the injection label and restarting its pods
D. A PeerAuthentication in `PERMISSIVE` mode scoped to the called workload, only for the duration of the migration

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** PeerAuthentication can be scoped mesh-wide, per namespace, or per workload with a selector, and more specific wins. `PERMISSIVE` accepts both mTLS and plaintext, which is exactly the migration mode. Reverting the whole namespace throws away the security you just gained for one laggard.
</details>

---

### Question 4
**Scenario:** External HTTP traffic must enter the mesh on a hostname with TLS termination.

A. A VirtualService alone with the hostname in `hosts`, which terminates TLS by itself
B. A ServiceEntry for the hostname, which makes the ingress proxy terminate TLS
C. A Gateway binding the host and TLS config, plus a VirtualService attached to that gateway
D. A Sidecar resource on the ingress pod that sets its inbound listeners

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The Gateway configures the ingress proxy's listener, ports, hosts, and TLS. The VirtualService must then list that gateway in its `gateways` field to attach routing rules to it. A VirtualService without the gateway reference applies only to mesh-internal traffic.
</details>

---

### Question 5
**Scenario:** A workload must reach an external API not registered in the mesh, and the mesh outbound policy is `REGISTRY_ONLY`.

A. A ServiceEntry describing the external host
B. A NetworkPolicy allowing egress to the external API's address range, which also adds the host to the sidecar's registry
C. A DestinationRule with TLS origination for the host, which registers the host and allows the outbound traffic
D. Nothing, because external traffic always works; the sidecar passes unknown destinations through whatever the outbound policy says

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** With `REGISTRY_ONLY`, the sidecar blocks anything not in the service registry. A ServiceEntry adds the external host to that registry so it can be routed and observed. Under the default `ALLOW_ANY` it would have worked without one, which is why understanding the outbound traffic policy setting matters.
</details>

---

### Question 6
**Scenario:** Which AuthorizationPolicy behavior is correct when a namespace has one policy with `action: ALLOW` and rules matching only `service-a`?

A. Only `service-a` is denied and all other traffic is allowed
B. All traffic is allowed, since an ALLOW policy only adds permissions
C. The policy is ignored unless a PeerAuthentication in the namespace is STRICT
D. Only traffic matching the rule is allowed; all else to the selected workloads is denied

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Once any ALLOW policy selects a workload, that workload is default-deny for anything not matched. This surprises people who expect an allow-list to be additive on top of open access. DENY policies are evaluated before ALLOW, and CUSTOM policies delegate to an external authorizer.
</details>

---

### Question 7
**Scenario:** A service should stop receiving traffic from a client after 5 consecutive 5xx responses.

A. Outlier detection in the DestinationRule's `trafficPolicy`
B. A timeout of 5 seconds in the VirtualService route, which ejects the endpoint after repeated slow responses
C. A fault injection rule with an `abort` of 503, which stops the client sending to a failing endpoint
D. A retry policy with `attempts: 5` and `retryOn: 5xx`, which stops traffic to a host once it has failed repeatedly

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Outlier detection is Istio's circuit breaking for unhealthy endpoints: consecutive errors eject the host from the load balancing pool for a base ejection time. Retries would send more traffic at a failing host. Timeouts bound a single request. Fault injection deliberately creates failures for testing.
</details>

---

### Question 8
**Scenario:** You want to test how the application behaves when a dependency is slow, without changing the dependency.

A. Reduce the dependency's replicas to one, so that its response times rise under the normal load from callers
B. Fault injection with a `delay` in the VirtualService
C. Add a timeout of a few seconds on the route, which makes the dependency respond slowly to its callers
D. Enable tracing on the mesh to inject delay

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Fault injection lets you add a fixed delay or an abort to a percentage of requests declaratively, which is chaos testing without touching either service. Scaling down changes capacity unpredictably rather than injecting a controlled fault. Timeouts and tracing observe or bound behavior instead of causing it.
</details>

---

### Question 9
**Scenario:** `istioctl analyze` reports a VirtualService referencing a host that does not exist.

A. Restart istiod, because it has probably not picked up the new host yet
B. Reinstall the mesh, since the message shows the control plane is corrupt
C. Ignore it, because analysis output is advisory and the sidecar will find the host for itself at request time
D. It is a real misconfiguration: the route will not resolve, so fix the host or add a ServiceEntry

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `istioctl analyze` catches exactly the class of errors that produce silent 404s and no obvious log line. An unresolvable host means Envoy has no cluster to route to. Treat analyzer errors as blocking, and use `istioctl proxy-config` to confirm what the sidecar actually received.
</details>

---

### Question 10
**Scenario:** A sidecar is not injected into new pods in a namespace.

A. Reinstall Istio with the `sidecarInjectorWebhook` setting turned on, then redeploy all of the namespace's workloads again
B. Restart istiod, because it caches the namespace list
C. Check the `istio-injection=enabled` label on the namespace or the `sidecar.istio.io/inject` annotation on the pod
D. Check the NetworkPolicy that allows egress from the application pods to istiod on port 15012, which is what decides whether injection happens

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Automatic injection is driven by a mutating webhook that keys off the namespace label (or the revision label when using revisions). Pod-level annotations can opt individual workloads in or out. Injection also only happens at pod creation, so existing pods need to be recreated after labeling.
</details>

---

### Question 11
**Scenario:** What does ambient mode change compared with the sidecar data plane?

A. It removes mTLS between workloads, because encryption is left to the CNI and the network between the nodes
B. It moves L4 handling to a per-node ztunnel and makes L7 optional through waypoint proxies
C. It requires one proxy per container, so each application container gets its own dedicated Envoy
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
B. Istio produces complete traces with no application change, since the sidecars correlate inbound and outbound requests by connection
C. Traces come from Prometheus, which scrapes the span data from the sidecars and stitches it together by request ID
D. Tracing requires rewriting each service with the OpenTelemetry SDK, because the sidecars cannot emit spans at all

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The sidecar can create a span for each hop, but it cannot know that an inbound request caused a given outbound request unless the application copies the trace context headers (`traceparent` or the b3 set) from one to the other. This "mesh gives you tracing for free" misconception is worth being precise about.
</details>

---

### Question 13
**Scenario:** A large mesh has slow sidecar startup and high memory use because every proxy receives config for every service.

A. Disable mTLS on the busiest namespaces, which stops istiod sending certificates and policy to their proxies
B. Reduce the number of VirtualServices to a handful per cluster
C. Use a `Sidecar` resource to scope the services each workload can see
D. Add more CPU and memory to every sidecar

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** By default istiod pushes the full service registry to every proxy. A `Sidecar` resource with an `egress.hosts` list restricts what a workload is told about, which cuts config size and push cost substantially in big meshes. `exportTo` on services and VirtualServices achieves a similar narrowing from the other direction.
</details>

---

### Question 14
**Scenario:** Which upgrade approach lets you move workloads to a new Istio version gradually?

A. Upgrading the CNI only, since it carries the data plane version
B. Revision-based (canary) upgrade with a new control plane revision and namespace revision labels
C. In-place upgrade of istiod, replacing the single control plane at once
D. Delete and reinstall the mesh in each environment, then redeploy every workload

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Revisions install a second control plane alongside the first. You relabel a namespace to the new revision and restart its workloads, so exposure is one namespace at a time and rollback is a relabel. In-place upgrades change every proxy's control plane at once.
</details>

---

### Question 15
**Scenario:** Two clusters should share one mesh with services reachable across both.

A. Two independent meshes joined with a VPN, each with its own root CA, and ServiceEntries pointing at the remote addresses
B. Multi-primary or primary-remote with a shared trust root and east-west gateways
C. Federating Prometheus between the clusters
D. A single Gateway resource in one cluster that is attached to the namespaces of each cluster and shares workload identities across them

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multi-cluster requires a common root of trust so workload identities validate across clusters, endpoint discovery between control planes, and east-west gateways when pod IPs are not directly routable. A VPN gives connectivity without shared identity or service discovery, and Prometheus federation is only observability.
</details>

---

### Question 16
**Scenario:** You install Istio for production with `istioctl` and want istiod plus an ingress gateway, without the extra tracing and high-verbosity settings meant for demos.

A. `istioctl install --set profile=demo`, then remove the demo add-ons by hand
B. `istioctl install --set profile=minimal`, which installs istiod and an ingress gateway
C. `istioctl install --set profile=empty`, which installs the recommended production components
D. `istioctl install --set profile=default`, which installs istiod and an ingress gateway

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The default profile is the recommended starting point for production: istiod plus an ingress gateway. The demo profile enables extra features and high trace sampling for showcasing. Minimal installs only the control plane, with no gateway. Empty installs nothing and is a base for custom configuration.
</details>

---

### Question 17
**Scenario:** You install Istio with Helm instead of istioctl. In what order should the charts be installed?

A. `istiod` first, then `base`, then a gateway, since the control plane creates the CRDs
B. `base` first for CRDs and cluster resources, then `istiod`, then any gateway charts
C. A gateway chart first, then `istiod`, then `base`, so traffic can enter before the mesh exists
D. All three charts at once with a single `helm install` command, since order does not matter

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The `base` chart installs the CRDs and cluster-wide resources that the control plane needs, `istiod` installs the control plane, and gateways come after, since they need istiod for configuration and certificates. Installing istiod first fails without the CRDs. A gateway without istiod cannot get configuration. Each chart is a separate release.
</details>

---

### Question 18
**Scenario:** Requests carrying the header `x-beta-user: true` must go to the `v2` subset of `reviews`, and all other requests to `v1`.

A. A VirtualService with a first route matching the header to `v2`, then a default route to `v1`
B. A DestinationRule with a header-based load balancer that sends beta users to the `v2` subset
C. An AuthorizationPolicy that allows only beta users to reach the `v2` pods of the service
D. A Gateway with a header match, which routes beta users to `v2` for traffic inside the mesh

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** VirtualService HTTP routes are evaluated in order, so a route matching the header to subset `v2` followed by a catch-all route to `v1` gives the required behavior. DestinationRules define subsets and policies but not request routing. AuthorizationPolicy allows or denies and does not route. A Gateway configures ingress listeners, not routing between services inside the mesh.
</details>

---

### Question 19
**Scenario:** Calls to `ratings` should time out after 2 seconds, and failed calls with connection errors or 5xx responses should be retried up to 3 times.

A. A DestinationRule with `outlierDetection` set to 3 errors and an interval of 2 seconds
B. A PeerAuthentication with a 2 second timeout and 3 retries on the `ratings` workload
C. A VirtualService route with `timeout: 2s` and `retries` with `attempts: 3` and a `retryOn` list
D. A Sidecar resource limiting egress to `ratings` with a 2 second connect timeout

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Request timeouts and retries are set on VirtualService routes, with `retryOn` choosing conditions such as `connect-failure` and `5xx`. Outlier detection ejects unhealthy hosts and does not retry. PeerAuthentication configures mTLS. The Sidecar resource scopes configuration and has no request timeout or retries.
</details>

---

### Question 20
**Scenario:** A new version of `payments` must receive a copy of live production traffic for testing, while its responses are discarded and users see only `v1`.

A. Route 1% of traffic to `v2` with a weight, so only a few users see its responses
B. Set `mirror` to the `v2` subset in the VirtualService route, with `mirrorPercentage` as needed
C. Deploy `v2` with a fault injection abort of 100%, so its responses are never returned
D. Add `v2` to an AuthorizationPolicy with action AUDIT, which copies traffic to it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Mirroring sends a copy of each request to the mirror destination fire-and-forget, discarding its responses, while the primary route serves users. Weighted routing exposes real users to `v2`. Abort faults return errors to callers. AUDIT actions mark requests for logging and do not copy traffic.
</details>

---

### Question 21
**Scenario:** All traffic from the mesh to `api.partner.com` must leave through dedicated egress nodes, so the partner can allowlist their addresses.

A. A ServiceEntry for the host only, which makes sidecars send the traffic through istiod
B. A DestinationRule with `tls.mode: DISABLE` for the host, which routes traffic to the egress nodes
C. An egress gateway with a ServiceEntry, a Gateway, and VirtualServices that route through it
D. Set `outboundTrafficPolicy` to `ALLOW_ANY`, which sends unknown hosts to the egress nodes

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The egress gateway pattern uses a ServiceEntry for the external host, a Gateway on the egress gateway, and VirtualServices that send sidecar traffic to the gateway and from the gateway to the host, so traffic exits from the gateway pods' nodes. A ServiceEntry alone lets sidecars connect directly. TLS settings do not change the path. `ALLOW_ANY` lets traffic out directly from each pod.
</details>

---

### Question 22
**Scenario:** A stateful service needs requests from the same user to keep reaching the same pod, based on a `user-id` header.

A. A DestinationRule with `loadBalancer.consistentHash.httpHeaderName: user-id`
B. A VirtualService route match on `user-id` with one route per pod in the service
C. A DestinationRule with `loadBalancer.simple: ROUND_ROBIN` and outlier detection
D. A Service with `sessionAffinity: ClientIP` in place of any Istio configuration

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Consistent hash load balancing on a header gives soft session affinity: requests with the same header value map to the same endpoint while the set of endpoints is stable. Routes per pod do not scale and break when pods change. Round robin spreads requests. Kubernetes `sessionAffinity` is not applied by the sidecar, which does its own load balancing.
</details>

---

### Question 23
**Scenario:** A RequestAuthentication with a JWT issuer is applied to `orders`. Requests with invalid tokens are rejected, but requests with no token at all still succeed.

A. The issuer URL is wrong, since a correct issuer makes RequestAuthentication reject requests without a token
B. PeerAuthentication must be STRICT, which also requires a JWT on every request to the workload
C. The JWKS cache is stale, so requests without tokens are allowed until it refreshes
D. Add an AuthorizationPolicy that requires `requestPrincipals: ["*"]`, so requests without a token are denied

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** RequestAuthentication only validates tokens that are present. Requests without a token are allowed unless an AuthorizationPolicy requires a request principal. Pairing it with a policy requiring `requestPrincipals` denies tokenless requests. The issuer and JWKS do not change that behavior. PeerAuthentication concerns mTLS between workloads, not end-user JWTs.
</details>

---

### Question 24
**Scenario:** A namespace has an ALLOW policy permitting everything from the `frontend` service account, and a DENY policy blocking requests to the path `/admin`. A request from `frontend` to `/admin` arrives.

A. Allowed, because ALLOW policies are evaluated first and the request already matches one
B. Denied, because DENY policies are evaluated before ALLOW policies
C. Allowed, because the more specific source match outranks a path match
D. Denied, because any ALLOW policy denies all paths it does not list explicitly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Istio evaluates CUSTOM policies first, then DENY, then ALLOW. A request matching a DENY policy is rejected regardless of ALLOW policies. Specificity does not change the order. The ALLOW policy here allows all paths from `frontend`; it is the DENY policy that blocks `/admin`.
</details>

---

### Question 25
**Scenario:** You want a default-deny posture in the `finance` namespace, so that only traffic explicitly allowed by later policies reaches its workloads.

A. A PeerAuthentication in `finance` with mode STRICT and no other settings
B. A Sidecar resource in `finance` with an empty egress list
C. An AuthorizationPolicy in `finance` with an empty `spec: {}`
D. A DestinationRule in `finance` with `trafficPolicy` set to DENY

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** An AuthorizationPolicy with an empty spec selects every workload in the namespace and, as an ALLOW policy with no rules, matches nothing, so all requests are denied until further ALLOW policies are added. STRICT mTLS requires mTLS but allows any authenticated peer. A Sidecar resource scopes outbound configuration. DestinationRules have no DENY setting.
</details>

---

### Question 26
**Scenario:** An engineer wants a live graph of services in the mesh, showing traffic rates, error rates, and whether connections use mTLS.

A. Kiali, which builds a service graph from mesh telemetry
B. `istioctl analyze`, which prints the service graph for a namespace
C. Jaeger, which draws the mTLS status of each connection
D. `kubectl top`, which shows traffic and errors between pods

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Kiali uses Prometheus metrics and Istio configuration to draw a service graph with traffic, errors, and security indicators such as mTLS, and it validates configuration. `istioctl analyze` finds configuration problems. Jaeger shows individual traces. `kubectl top` shows CPU and memory.
</details>

---

### Question 27
**Scenario:** Envoy access logs must be turned on for workloads in the `checkout` namespace only, without changing mesh-wide settings.

A. Edit the istio ConfigMap to set `accessLogFile`, which applies to a single namespace
B. A Telemetry resource in `checkout` that enables access logging with the `envoy` provider
C. An EnvoyFilter in `istio-system` that enables logging for every proxy in the mesh
D. Restart the `checkout` pods with a log-level flag on the application containers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Telemetry API configures access logging, metrics, and tracing at mesh, namespace, or workload scope, so a namespaced Telemetry resource enabling the `envoy` access log provider affects only that namespace. `accessLogFile` in mesh config is mesh-wide. An EnvoyFilter in the root namespace applies everywhere. Application log levels do not control Envoy access logs.
</details>

---

### Question 28
**Scenario:** A slow dependency causes callers to queue thousands of pending requests, exhausting their memory. Requests beyond a limit should fail fast instead.

A. A VirtualService with a longer timeout, so pending requests finish before memory runs out
B. A fault injection delay on the dependency, which lowers the number of requests queued
C. An AuthorizationPolicy limiting which callers may reach the dependency during load
D. A DestinationRule `connectionPool` with limits such as `http1MaxPendingRequests` and `maxConnections`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Connection pool settings act as circuit breakers: when connections or pending requests exceed the limits, Envoy rejects new requests immediately, protecting callers. Longer timeouts make queues longer. Fault injection adds failures for testing. Authorization limits who may call, not how many requests are in flight.
</details>

---

### Question 29
**Scenario:** You changed a VirtualService, but one pod's behavior has not changed. You want to know whether that proxy has received the latest configuration from istiod.

A. `istioctl proxy-status`, which shows whether each proxy is SYNCED or STALE
B. `kubectl logs` on istiod, which lists the configuration version of each proxy
C. `istioctl install --verify`, which redeploys the configuration to all proxies
D. `kubectl describe virtualservice`, which shows each proxy's sync state

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `istioctl proxy-status` reports, for each proxy, whether its clusters, listeners, routes, and endpoints are in sync with istiod. Then `istioctl proxy-config` can inspect the proxy's actual routes. istiod logs do not give a clear per-proxy sync view. Reinstalling is not a diagnostic. The VirtualService object holds no proxy sync state.
</details>

---

### Question 30
**Scenario:** A namespace runs in ambient mode. L4 mTLS works, but an AuthorizationPolicy with HTTP path rules for a service is not enforced.

A. Restart the ztunnel DaemonSet, which reloads the L7 policy for the namespace
B. Re-label the namespace for sidecar injection, since ambient mode never supports L7
C. Deploy a waypoint proxy for the service or namespace and target the policy at it
D. Switch PeerAuthentication to PERMISSIVE, which turns on L7 processing in ztunnel

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** In ambient mode, ztunnel handles L4 features such as mTLS and L4 authorization. L7 features, including HTTP-based authorization, need a waypoint proxy, and the policy should target the waypoint. Restarting ztunnel does not add L7 processing. Ambient supports L7 through waypoints, so sidecars are not required. PERMISSIVE affects mTLS acceptance, not L7 handling.
</details>

---

## Where to go deeper

- [ICA cert page](../../exams/kubernetes/ica/) - notes, practice plan, strategy
- [CKA practice questions](./kubernetes-cka.md) - the Kubernetes baseline ICA assumes
- [Kubernetes topic index](../../topics/kubernetes.md) - service mesh in context
- [Zero trust architecture](https://security.noblerworks.com/resources/architecture-patterns/zero-trust-architecture/) - the identity model mTLS implements
- **[📖 Istio documentation](https://istio.io/latest/docs/)** - primary source
