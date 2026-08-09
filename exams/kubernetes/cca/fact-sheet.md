---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 10 min
---

# Cilium Certified Associate (CCA) Fact Sheet

## Exam Overview

**Exam Code:** CCA
**Exam Name:** Cilium Certified Associate
**Level:** Associate
**Duration:** 90 minutes
**Format:** Multiple choice and multiple select, online proctored
**Questions:** 60
**Passing Score:** 75%
**Cost:** USD 250 (includes one free retake)
**Valid For:** 2 years
**Delivery:** Online proctored through PSI
**Prerequisites:** None; Kubernetes networking fundamentals assumed

> **Verify before booking.** Confirm current details on the official pages below.

**[📖 CCA certification page](https://www.cncf.io/training/certification/cca/)** - registration and curriculum
**[📖 Linux Foundation CCA page](https://training.linuxfoundation.org/certification/cilium-certified-associate-cca/)** - logistics
**[📖 Cilium documentation](https://docs.cilium.io/)** - the primary study source
**[📖 CNCF curriculum repository](https://github.com/cncf/curriculum)** - published exam domains

## Why this exam is in this repo

The repo has four [networking deep dives](../../../resources/networking-deep-dives/), a networking topic page, and seven Kubernetes certifications, but nothing covering the eBPF-based networking layer that has become the default CNI on GKE Dataplane V2, AKS with Azure CNI powered by Cilium, and EKS through the Cilium provider.

CCA is also the only certification in the repo that teaches **eBPF**, which is now the substrate for a large part of cloud native networking, security, and observability.

## Target Audience

- Platform and network engineers running Kubernetes clusters
- SREs debugging cluster networking
- Security engineers implementing network policy and micro-segmentation
- Anyone holding [CKA](../cka/) or [CKS](../cks/) going deeper on the data plane

Assumed background: Kubernetes services, pods, and the CNI concept. Linux networking helps considerably.

## Exam Domains

| Domain | Weight |
|---|---:|
| Architecture | 20% |
| Network Policy | 18% |
| Service Mesh | 16% |
| Network Observability | 10% |
| Installation and Configuration | 10% |
| Cluster Mesh | 10% |
| eBPF | 10% |
| BGP and External Networking | 6% |

### Architecture (20%)

**Key Concepts:**
- Cilium agent, operator, CLI, and the client-server model
- The eBPF datapath and how it replaces iptables for service handling
- Identity-based security: Cilium identities derived from labels, not IP addresses
- The identity allocation model and the key-value store (etcd or CRD mode)
- Endpoint lifecycle and the endpoint state machine
- IPAM modes: cluster pool, Kubernetes host scope, CRD-backed, and cloud-provider modes
- Datapath modes: encapsulation (VXLAN, Geneve) versus native routing
- kube-proxy replacement and how service handling changes
- Envoy's role for layer 7 policy and service mesh
- Hubble as the observability layer

### Network Policy (18%)

**Key Concepts:**
- Kubernetes NetworkPolicy and its limits
- `CiliumNetworkPolicy` and `CiliumClusterwideNetworkPolicy`
- Identity-based rather than IP-based enforcement
- Layer 3 rules by endpoint selector, CIDR, and entity (world, cluster, host, remote-node)
- Layer 4 rules by port and protocol
- Layer 7 rules: HTTP method and path, Kafka topic, DNS
- DNS-based policy with `toFQDNs`
- Default deny and how policy applies once an endpoint is selected
- Policy enforcement modes: default, always, never
- Host firewall policies
- Policy auditing and troubleshooting with `cilium policy` commands and Hubble

### Service Mesh (16%)

**Key Concepts:**
- Sidecar-free service mesh and the argument for it
- Layer 7 load balancing and traffic management
- Gateway API and Ingress support
- Mutual authentication and transparent encryption
- Transparent encryption with WireGuard and IPsec
- Traffic shifting and canary patterns
- Envoy integration and Envoy configuration through custom resources
- Comparison with sidecar meshes such as Istio and Linkerd

### Network Observability (10%)

**Key Concepts:**
- Hubble architecture: the Hubble agent, Hubble Relay, Hubble UI, and the CLI
- Flow visibility and what a flow record contains
- Layer 7 visibility and how it is enabled
- Service dependency maps
- Metrics export to Prometheus and Grafana
- Troubleshooting dropped packets and policy denials with Hubble

### Installation and Configuration (10%)

**Key Concepts:**
- Installation with the Cilium CLI and with Helm
- `cilium status`, `cilium connectivity test`
- Key configuration options and ConfigMap settings
- Upgrades and the pre-flight check
- Cloud provider considerations and managed offerings

### Cluster Mesh (10%)

**Key Concepts:**
- Connecting multiple clusters into one policy and service domain
- Requirements: unique cluster names and IDs, non-overlapping pod CIDRs, connectivity between nodes
- Global services and service affinity
- Cross-cluster network policy
- Cluster Mesh with and without shared identities

### eBPF (10%)

**Key Concepts:**
- What eBPF is: verified, sandboxed programs running in the kernel
- The verifier and JIT compilation
- eBPF maps and their role
- Hook points: XDP, TC (traffic control), socket, kprobes, tracepoints
- Why eBPF replaces iptables for scale and performance
- eBPF versus kernel modules

### BGP and External Networking (6%)

**Key Concepts:**
- Cilium BGP Control Plane and peering configuration
- Advertising pod CIDRs and load balancer IPs
- LoadBalancer IP address management (LB IPAM)
- Egress gateway for predictable source IPs
- External workloads

## Related repo material

- [Notes](./notes/) - four notes covering the eight domains
- [Practice plan](./practice-plan.md) - 5-week schedule
- [Scenarios](./scenarios.md)
- [Strategy](./strategy.md)
- [CKA](../cka/) and [CKS](../cks/) - the Kubernetes layer above
- [Networking deep dives](../../../resources/networking-deep-dives/)
- [VPC explained](../../../learn/concepts/vpc-explained.md)
