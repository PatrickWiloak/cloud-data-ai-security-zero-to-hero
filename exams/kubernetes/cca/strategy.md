---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 5 min
---

# CCA Study Strategy

## Start with the one idea

**Policy is enforced on identity, not IP.**

Cilium computes a numeric identity from a pod's labels. Every pod sharing a label set shares an identity. Policy rules reference identities, and the eBPF datapath enforces against them.

Consequences that show up repeatedly in questions:
- Pod IP churn does not invalidate policy
- The datapath scales with the number of distinct label sets, not with the number of pods
- `CiliumClusterwideNetworkPolicy` and Cluster Mesh work because identity is a cluster-wide (or mesh-wide) concept
- Special **entities** (`world`, `cluster`, `host`, `remote-node`, `health`) are reserved identities for things that are not pods

Almost every architecture and policy question makes more sense once this is fixed in mind.

## Phase 1: eBPF (short, foundational)

Ten percent of the exam, but it explains the other ninety.

An eBPF program is bytecode loaded into the kernel, checked by the **verifier** (which proves it terminates and does not access memory it should not), then JIT-compiled to native instructions and attached to a **hook point**. **Maps** are the shared key-value structures that let user space and kernel space communicate.

Hook points that matter here: **XDP** (earliest, in the driver, fastest, used for DDoS mitigation and load balancing), **TC** (traffic control, where most Cilium datapath logic lives), and **socket** hooks (used for socket-level load balancing that bypasses per-packet NAT).

Why it beats iptables: iptables rules are evaluated as a linear chain, so cost grows with rule count. eBPF uses hash map lookups, so cost stays roughly constant as services and policies scale.

## Phase 2: Architecture (week 1-2)

Know the decisions:

**Datapath mode**
- **Encapsulation** (VXLAN or Geneve): pod traffic is tunnelled between nodes. Works on any underlying network, costs some MTU and overhead. The default.
- **Native routing**: pod CIDRs are routable on the underlying network. Faster and simpler to debug, requires the network to know the routes, usually via a cloud route table or BGP.

**IPAM mode** determines who allocates pod IPs: Cilium's cluster pool by default, Kubernetes host scope from node PodCIDRs, CRD-backed for custom control, or a cloud provider mode where pod IPs come from the VPC.

**kube-proxy replacement** moves service handling into eBPF. Services are resolved at the socket layer where possible, which removes a NAT hop and eliminates the iptables service chains entirely.

## Phase 3: Network policy (week 3)

Learn the layers:

| Layer | Rule expresses |
|---|---|
| **L3** | Which identities, CIDRs, or entities may communicate |
| **L4** | Which ports and protocols |
| **L7** | Which HTTP methods and paths, Kafka topics, or DNS names |

Layer 7 rules are enforced by redirecting matching traffic through **Envoy**, which is why they cost more than layer 3 or 4 rules and why they are applied selectively.

**Default deny** semantics: a pod with no policy selecting it allows everything. As soon as any policy selects it for a direction (ingress or egress), that direction becomes deny-by-default and only explicitly allowed traffic passes. This asymmetry between ingress and egress is a reliable exam question.

**`toFQDNs`** enforces on DNS names by intercepting DNS responses and programming the resulting IPs into the policy datapath. It requires that DNS itself is allowed and visible to Cilium.

## Phase 4: Mesh, observability, operations (week 4-5)

**Service mesh without sidecars**: the per-node Envoy plus eBPF datapath provides layer 7 routing, load balancing, and mTLS without injecting a proxy into every pod. The trade-off is a shared per-node proxy rather than per-pod isolation.

**Hubble** is the observability layer: the agent produces flow records from the datapath, Relay aggregates across nodes, the UI draws service maps, and the CLI queries flows. For troubleshooting, `hubble observe --verdict DROPPED` is the fastest path to a policy denial.

**Cluster Mesh** prerequisites are memorizable and testable: unique cluster name and numeric ID per cluster, non-overlapping pod CIDRs, node-to-node connectivity, and shared or connected identity allocation.

## Common traps

| Trap | Reality |
|---|---|
| Thinking policy is IP-based | Identity-based; IPs are an implementation detail |
| Assuming a pod with no policy is denied | No policy means allow all; deny-by-default begins when a policy selects it |
| Applying deny-by-default to both directions at once | Ingress and egress become default-deny independently |
| Expecting L7 rules for free | L7 enforcement redirects through Envoy and costs more than L3/L4 |
| Confusing encapsulation with native routing requirements | Native routing needs the underlay to route pod CIDRs |
| Forgetting Cluster Mesh CIDR overlap | Overlapping pod CIDRs make cross-cluster routing ambiguous |
| Treating Hubble as required | Hubble is observability; the datapath works without it |

## Exam day

- 90 minutes, 60 questions, knowledge-based.
- 75% to pass, roughly 45 of 60.
- One free retake included.
- Expect to read YAML policy snippets and say what they permit.

## Related

- [Practice plan](./practice-plan.md)
- [Scenarios](./scenarios.md)
- [Fact sheet](./fact-sheet.md)
- [CKS](../cks/) - Kubernetes security including NetworkPolicy
