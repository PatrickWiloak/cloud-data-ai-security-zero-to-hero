---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 8 min
---

# CCA High-Yield Scenarios

---

## Scenario 1: Policy that survives pod churn

**Scenario**: A team writes NetworkPolicy rules using `ipBlock` CIDRs matching their pods' current addresses. After a node drain, traffic breaks intermittently, and some pods can suddenly reach services they should not.

**Solution Pattern**:
- Replace CIDR-based rules with **label-based endpoint selectors**, so policy targets Cilium **identities** derived from labels
- Pod IPs are ephemeral and reused; a recycled IP can inherit an allow rule intended for a different workload, which is the source of the unexpected access
- Use `ipBlock` only for genuinely external, stable ranges
- For external services with changing addresses, use **`toFQDNs`** so policy follows the DNS name
- Verify with `cilium endpoint list` that identities are what you expect

**Common Distractors**:
- Reserving static pod IPs (fights Kubernetes rather than using it)
- Widening the CIDR (increases exposure)
- Adding a NetworkPolicy per pod (unmanageable and still IP-fragile)

**Key Takeaway**: Identity-based policy is the reason Cilium exists. IP-based rules in a dynamic cluster are both fragile and a security risk through address reuse.

---

## Scenario 2: Default deny semantics

**Scenario**: A pod has no policies. A CiliumNetworkPolicy is then created selecting it with a single ingress rule allowing traffic from the frontend. The team is surprised that the pod can still make arbitrary outbound calls to the internet.

**Solution Pattern**:
- Ingress and egress become deny-by-default **independently**. The new policy selected the pod for ingress only, so egress is still unrestricted
- Add an egress rule, or an explicit egress-only policy, to bring egress under default deny
- A minimal deny-all baseline is a policy selecting all endpoints with empty `ingress: []` and `egress: []`, then layering allow rules on top
- Consider `CiliumClusterwideNetworkPolicy` for the baseline so it applies across namespaces

**Common Distractors**:
- Assuming any policy makes both directions default-deny
- Assuming Kubernetes NetworkPolicy semantics differ here (they do not; this behavior is the same)
- Adding a second ingress rule (wrong direction entirely)

**Key Takeaway**: Selecting an endpoint for one direction only changes that direction. Egress restriction requires an egress rule, and this is one of the most reliably tested points on the exam.

---

## Scenario 3: Restricting to a specific API path

**Scenario**: A payments service exposes `/health`, `/metrics`, and `/transfer`. A monitoring workload must reach `/metrics` only, using GET, and must not be able to reach `/transfer` even though both are on the same port.

**Solution Pattern**:
- A **layer 7 CiliumNetworkPolicy** with an HTTP rule specifying `method: GET` and `path: /metrics`
- Layer 4 rules cannot express this, because both endpoints share port 8080
- Matching traffic is redirected through the per-node **Envoy** proxy for enforcement, which is why layer 7 rules cost more than layer 3 or 4
- Requests to `/transfer` from that identity receive an HTTP 403 rather than a connection reset, which is a useful diagnostic distinction
- Confirm with `hubble observe` showing the layer 7 verdict

**Common Distractors**:
- A port-based rule (allows the whole port, including `/transfer`)
- Moving `/metrics` to a separate port (works, requires an application change, and the question is about policy capability)
- Relying on application authentication (defense in depth, but not the network control asked for)

**Key Takeaway**: Layer 7 policy is what distinguishes CiliumNetworkPolicy from Kubernetes NetworkPolicy. When endpoints share a port and must be separated, only an L7 rule works.

---

## Scenario 4: Egress to a SaaS endpoint

**Scenario**: A workload must reach `api.stripe.com` and nothing else on the internet. Stripe's addresses change and are served by a CDN with a large, shifting IP range.

**Solution Pattern**:
- A `toFQDNs` egress rule matching `api.stripe.com`
- Also allow DNS egress to the cluster DNS with an L7 DNS rule using `matchPattern`, because Cilium learns the IPs by observing DNS responses. Without visible DNS, FQDN policy cannot populate
- Cilium programs the resolved IPs into the datapath with the DNS record's TTL
- Do not attempt to enumerate CDN CIDRs; they change without notice

**Common Distractors**:
- An `ipBlock` with published CDN ranges (stale within weeks and enormously broad)
- Allowing all egress to `world` (defeats the requirement)
- A layer 7 HTTP rule on the Host header (does not restrict which IPs may be contacted, and fails for TLS)

**Key Takeaway**: FQDN-based egress needs both the `toFQDNs` rule and an allowed, visible DNS path. Forgetting the DNS rule is the classic reason FQDN policy appears not to work.

---

## Scenario 5: Choosing a datapath mode

**Scenario**: A cluster runs on a cloud VPC where the pod CIDR is not known to the VPC route tables. A second cluster runs on-premises on a network where the team controls routing and wants the lowest possible latency and simplest packet capture.

**Solution Pattern**:
- **Cloud cluster**: **encapsulation** (VXLAN or Geneve). The underlay does not need to know pod CIDRs, since pod traffic is tunnelled node to node. Accept the MTU reduction and small overhead
- **On-premises cluster**: **native routing**, since the team controls the underlay and can advertise pod CIDRs, either statically or with the **BGP Control Plane**. Packets appear on the wire with real pod addresses, which makes capture and troubleshooting simpler
- In native routing mode, ensure `auto-direct-node-routes` or an equivalent routing mechanism is in place for node-to-node reachability

**Common Distractors**:
- Native routing in the cloud cluster without route programming (pod traffic is dropped by the VPC)
- Encapsulation everywhere for consistency (fine, but gives up the latency and observability benefit where native routing is available)
- Changing IPAM mode to solve a routing problem (IPAM decides address allocation, not reachability)

**Key Takeaway**: Encapsulation works anywhere and costs MTU and a little overhead. Native routing is faster and easier to debug, and requires the underlying network to route pod CIDRs.

---

## Scenario 6: Cluster Mesh prerequisites

**Scenario**: An organization wants to connect three clusters so that a service in one can fail over to another, and so that network policy can reference workloads across clusters. Cluster A and cluster B were both installed with default settings.

**Solution Pattern**:
- **Unique cluster name and numeric cluster ID** per cluster. Two clusters installed with defaults share the same ID, which must be fixed before meshing
- **Non-overlapping pod CIDRs** across all clusters, otherwise cross-cluster routing is ambiguous
- **Node-to-node connectivity** between clusters, and reachability of the Cluster Mesh API server
- Shared or connected **identity allocation**, so an identity means the same thing in every cluster
- **Global services**: a Service annotated as global is load balanced across clusters; **service affinity** controls whether local endpoints are preferred
- Cross-cluster policy then works because identities are mesh-wide

**Common Distractors**:
- Assuming defaults are fine (default cluster ID collisions are the most common blocker)
- Using a service mesh gateway instead (a valid alternative architecture, but not Cluster Mesh)
- Overlapping CIDRs with NAT (adds complexity and breaks identity-based policy semantics)

**Key Takeaway**: Unique cluster name and ID, non-overlapping pod CIDRs, connectivity, and shared identities. These four are memorizable and are exactly what the exam asks for.

---

## Scenario 7: Finding why traffic is dropped

**Scenario**: After a policy change, one service cannot reach another. The application logs show connection timeouts with no further detail.

**Solution Pattern**:
- `hubble observe --verdict DROPPED --to-pod <pod>` shows the dropped flows and, crucially, the **drop reason**
- A reason of `Policy denied` confirms a policy problem rather than a routing or DNS problem
- `cilium endpoint list` shows whether policy enforcement is active for the endpoint in each direction
- `cilium policy get` shows the policy the agent has actually loaded, which may differ from what was applied if there was a parse error
- For layer 7 denials, the verdict appears with the HTTP details, and the client receives a 403 rather than a timeout, which itself narrows the diagnosis
- `cilium connectivity test` validates the broader datapath if policy is ruled out

**Common Distractors**:
- Reading application logs harder (the drop happens below the application)
- `kubectl describe` on the policy (shows what was requested, not what is enforced)
- Disabling policy to confirm (works as a test, but Hubble gives the answer without an outage)

**Key Takeaway**: Hubble's drop reason is the fastest diagnostic in Cilium. A timeout suggests L3/L4 denial; an HTTP 403 suggests an L7 rule matched and rejected.

---

## Related

- [Practice plan](./practice-plan.md)
- [Strategy](./strategy.md)
- [Notes](./notes/)
- [Kubernetes troubleshooting](../../../resources/troubleshooting/kubernetes-troubleshooting.md)
- [Practice questions](../../../resources/practice-questions/cncf-cca.md)
