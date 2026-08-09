---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 4 min
---

# CCA Study Plan

Five weeks at 5-7 hours per week, with a kind cluster running Cilium throughout.

## Week 1: eBPF and architecture

- [ ] What eBPF is: verified, sandboxed programs attached to kernel hook points
- [ ] The verifier, JIT compilation, and why eBPF is safe to run in the kernel
- [ ] eBPF maps and how user space and kernel space share state
- [ ] Hook points: XDP, TC, socket, kprobes, tracepoints
- [ ] Why eBPF outperforms iptables at scale
- [ ] Cilium components: agent, operator, CLI, Hubble
- [ ] Identity-based security and how identities derive from labels
- [ ] Endpoints and the endpoint state machine
- [ ] **Lab**: `cilium install` on kind, then `cilium status` and `cilium connectivity test`
- [ ] Review Notes: `notes/01-ebpf-and-architecture.md`

## Week 2: Datapath, IPAM, and kube-proxy replacement

- [ ] Encapsulation (VXLAN, Geneve) versus native routing, and when each applies
- [ ] IPAM modes: cluster pool, Kubernetes host scope, CRD-backed, cloud provider
- [ ] kube-proxy replacement: what changes, and how services are handled in eBPF
- [ ] Direct server return and socket-level load balancing
- [ ] Masquerading and its eBPF implementation
- [ ] **Lab**: enable kube-proxy replacement and confirm service iptables rules are gone

## Week 3: Network policy

- [ ] Kubernetes NetworkPolicy and where it stops
- [ ] CiliumNetworkPolicy and CiliumClusterwideNetworkPolicy
- [ ] Layer 3 selectors: endpoint selector, CIDR, entities (world, cluster, host, remote-node)
- [ ] Layer 4 rules by port and protocol
- [ ] Layer 7 rules for HTTP, Kafka, and DNS
- [ ] `toFQDNs` DNS-based egress policy and how it works
- [ ] Default deny semantics: an endpoint becomes deny-by-default once selected
- [ ] Policy enforcement modes: default, always, never
- [ ] Host firewall policies
- [ ] **Lab**: default-deny, then a layer 4 allow, then a layer 7 HTTP path restriction
- [ ] Review Notes: `notes/02-network-policy.md`

## Week 4: Service mesh and observability

- [ ] Sidecar-free service mesh: what it does and does not replace
- [ ] Envoy's role and where it sits in the datapath
- [ ] Gateway API and Ingress support
- [ ] Transparent encryption with WireGuard and IPsec
- [ ] Mutual authentication
- [ ] Hubble: agent, Relay, UI, CLI
- [ ] Flow records, layer 7 visibility, service dependency maps
- [ ] Metrics export to Prometheus
- [ ] **Lab**: enable Hubble, break traffic with a policy, and find the drop reason in `hubble observe`
- [ ] Review Notes: `notes/03-service-mesh-and-observability.md`

## Week 5: Operations, cluster mesh, BGP, and review

- [ ] Installation with the CLI and with Helm; key configuration options
- [ ] Upgrades and the pre-flight check
- [ ] Cluster Mesh: requirements, global services, service affinity, cross-cluster policy
- [ ] BGP Control Plane: peering, advertising pod CIDRs and load balancer IPs
- [ ] LB IPAM and egress gateway
- [ ] Troubleshooting: `cilium status`, `cilium endpoint list`, `cilium policy get`, `hubble observe`
- [ ] Review Notes: `notes/04-operations-clustermesh-bgp.md`
- [ ] Work every scenario in [scenarios.md](./scenarios.md)
- [ ] Two timed practice exams

## Readiness check

- [ ] Explain what an eBPF program is and what the verifier guarantees
- [ ] Explain how a Cilium identity is derived and why identity beats IP for policy
- [ ] Choose between encapsulation and native routing given a network constraint
- [ ] Explain what changes when kube-proxy replacement is enabled
- [ ] Write out what a default-deny CiliumNetworkPolicy does to an unselected pod
- [ ] Explain how `toFQDNs` enforcement works
- [ ] State the Cluster Mesh prerequisites from memory
- [ ] Describe how to find why a packet was dropped
