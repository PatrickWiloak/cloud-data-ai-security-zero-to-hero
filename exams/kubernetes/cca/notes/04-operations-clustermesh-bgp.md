---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 9 min
---

# 04 - Operations, Cluster Mesh, and BGP

**Domains: Installation and Configuration (10%), Cluster Mesh (10%), BGP and External Networking (6%)** - 26% combined.

---

## Installation and configuration

Two supported paths:

- **Cilium CLI**: `cilium install`, which detects the environment and picks sensible defaults. Best for getting started and for labs.
- **Helm**: the production path, with the full values surface, and what you use when Cilium itself is managed by GitOps.

Key operational commands:

| Command | Purpose |
|---|---|
| `cilium status` | Agent and operator health, enabled features, current mode |
| `cilium connectivity test` | Deploys test workloads and validates pod-to-pod, pod-to-service, and external connectivity |
| `cilium config view` | Effective configuration |
| `cilium endpoint list` | Endpoints, identities, and policy enforcement state |
| `cilium sysdump` | A support bundle for troubleshooting |

**Upgrades** run a **pre-flight check** that pulls the new image and validates readiness before the rollout, so failures surface before the datapath is touched. Read the upgrade notes for the target version: Cilium occasionally changes defaults between minor versions, and datapath mode or IPAM changes are not always hot-swappable.

**Managed offerings** matter for the exam's context: GKE Dataplane V2, AKS with Azure CNI powered by Cilium, and EKS with the Cilium CNI are all Cilium underneath, with different degrees of configurability.

---

## Cluster Mesh

Connects multiple clusters into one service and policy domain.

### Prerequisites (memorize these)

1. **Unique cluster name and numeric cluster ID** in each cluster. Two clusters installed with defaults collide, which is the most common blocker.
2. **Non-overlapping pod CIDRs** across all clusters, otherwise cross-cluster routing is ambiguous.
3. **Node-to-node connectivity** between clusters, and reachability of each cluster's Cluster Mesh API server.
4. **Shared or connected identity allocation**, so an identity means the same thing everywhere.

### What it enables

- **Global services**: annotate a Service as global and its endpoints across all meshed clusters are load balanced together, giving transparent failover.
- **Service affinity**: prefer local endpoints, remote endpoints, or none, so cross-cluster traffic only happens when local backends are unavailable.
- **Cross-cluster network policy**: because identities are mesh-wide, a policy in cluster A can reference workloads in cluster B by label.
- **Shared external workloads**: VMs outside Kubernetes can join the mesh as endpoints with identities.

Cluster Mesh is not a service mesh gateway model: there is no central ingress, and traffic goes node to node.

---

## BGP and external networking

### BGP Control Plane

Cilium can peer with the physical network using BGP, configured through `CiliumBGPClusterConfig` and related resources.

Uses:
- **Advertise pod CIDRs** so native routing works without static routes
- **Advertise LoadBalancer service IPs** so external traffic reaches services without a cloud load balancer
- **Receive routes** from the network for external destinations

This is the standard answer for on-premises clusters that need real routed pod networking.

### LB IPAM

**LoadBalancer IP address management** assigns IPs to `type: LoadBalancer` services from pools you define, without a cloud provider. Combined with BGP advertisement, it gives on-premises clusters a working LoadBalancer service type, which is what MetalLB traditionally provided.

### Egress gateway

By default, pod traffic leaving the cluster is masqueraded to the node IP, which means the source address varies by node. **Egress gateway** routes selected egress traffic through designated nodes with fixed IPs, so external systems see a predictable, allowlistable source address.

The typical driver is a partner or legacy system with an IP allowlist. Without an egress gateway, you would have to allowlist every node in the cluster and update it on every scale event.

### External workloads

VMs and bare-metal servers outside Kubernetes can be enrolled so they receive a Cilium identity and participate in policy, which lets a migration proceed incrementally with policy applying consistently to both sides.

---

## Key terms

- **cilium connectivity test** - the command deploying test workloads to validate pod, service, and external connectivity
- **cilium sysdump** - the support bundle command collecting diagnostics for troubleshooting
- **Pre-flight check** - the upgrade step validating readiness and pulling images before the datapath rollout
- **Cluster Mesh** - the capability connecting multiple clusters into one service and policy domain
- **Cluster ID** - the unique numeric identifier each cluster must have before joining a mesh
- **Global service** - a Service annotated so its endpoints across all meshed clusters are load balanced together
- **Service affinity** - the Cluster Mesh setting preferring local or remote endpoints for a global service
- **BGP Control Plane** - Cilium's BGP implementation for peering with the physical network
- **LB IPAM** - LoadBalancer IP address management assigning service IPs from configured pools without a cloud provider
- **Egress gateway** - the feature routing selected egress traffic through designated nodes so external systems see a stable source IP
- **External workload** - a VM or bare-metal host enrolled into Cilium so it receives an identity and participates in policy
- **Dataplane V2** - Google Kubernetes Engine's Cilium-based networking implementation

---

## Related

- [Notes 01: eBPF and architecture](./01-ebpf-and-architecture.md)
- [Scenarios](../scenarios.md) - scenarios 5 and 6
- [Multi-cloud networking](../../../../resources/networking-deep-dives/multi-cloud-networking.md)
- [Hybrid connectivity](../../../../resources/networking-deep-dives/hybrid-connectivity.md)
