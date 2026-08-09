---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 11 min
---

# 01 - eBPF and Cilium architecture

**Domains: eBPF (10%) and Architecture (20%)** - 30% combined.

---

## eBPF

**eBPF** lets you run sandboxed programs inside the Linux kernel without writing a kernel module or rebooting.

The lifecycle:
1. A program is compiled to eBPF bytecode.
2. The **verifier** checks it: bounded loops, no invalid memory access, no unbounded execution. A program that cannot be proven safe is rejected.
3. It is **JIT-compiled** to native machine instructions.
4. It is **attached to a hook point**.

**Maps** are typed key-value structures that persist across program invocations and are readable and writable from user space. They are how the Cilium agent (user space) and the datapath (kernel) share state such as policy decisions, service backends, and connection tracking.

### Hook points

| Hook | Where | Used for |
|---|---|---|
| **XDP** | In the network driver, before an `sk_buff` is allocated | Fastest possible processing: DDoS drop, load balancing |
| **TC** (traffic control) | Ingress and egress of a network interface | Most of Cilium's datapath logic |
| **Socket** | System call level | Socket-level load balancing, bypassing per-packet NAT |
| **kprobes / tracepoints** | Arbitrary kernel functions and static trace points | Observability and tracing |
| **LSM** | Linux Security Module hooks | Runtime security enforcement (Tetragon) |

### Why it beats iptables

iptables evaluates rules as a linear chain, so cost grows with rule count. A cluster with thousands of services produces tens of thousands of rules, and every packet walks them.

eBPF uses **hash map lookups**, so lookup cost is roughly constant regardless of how many services or policies exist. Updates are also cheaper: changing one map entry does not require rewriting a ruleset.

---

## Cilium components

| Component | Runs as | Role |
|---|---|---|
| **Cilium agent** | DaemonSet, one per node | Compiles and loads eBPF programs, manages endpoints, enforces policy, exposes the API |
| **Cilium operator** | Deployment, one per cluster | Cluster-wide duties: IPAM allocation, identity garbage collection, CRD registration |
| **Cilium CLI** | Client tool | Install, status, connectivity test |
| **cilium-dbg** | In-agent client | Low-level debugging of endpoints, policy, and maps |
| **Hubble** | Embedded in the agent, plus Relay and UI | Flow observability |
| **Envoy** | Per node, embedded or separate | Layer 7 policy enforcement and service mesh |

---

## Identity

The central concept.

Cilium assigns a numeric **identity** to each endpoint, derived from its **security-relevant labels**. Every pod with the same label set shares one identity. Policy is expressed and enforced against identities.

Consequences:
- Pod IP churn does not invalidate policy
- Datapath state scales with the number of distinct label sets, not the number of pods
- Identity is meaningful cluster-wide, and mesh-wide with Cluster Mesh

**Reserved identities** cover things that are not pods:

| Entity | Means |
|---|---|
| `host` | The local node itself |
| `remote-node` | Other nodes in the cluster |
| `world` | Everything outside the cluster |
| `cluster` | All endpoints inside the cluster |
| `health` | Cilium's own health-checking endpoints |
| `init` | An endpoint whose identity is not yet resolved |
| `unmanaged` | An endpoint Cilium does not manage |

Identities are allocated through a key-value store: **etcd** (Cilium's own or the cluster's) or **CRD mode**, where identities are Kubernetes custom resources. CRD mode is the common default and removes the etcd dependency.

---

## Endpoints

An **endpoint** is a network-addressable entity Cilium manages, usually a pod. Each has an identity, an IP, and a set of eBPF programs and maps.

The endpoint moves through states as its identity is resolved and policy is computed: creating, waiting-for-identity, waiting-to-regenerate, regenerating, ready, and disconnecting. `cilium endpoint list` shows the state plus whether ingress and egress policy enforcement is enabled, which is the fastest way to check whether a policy actually selected a pod.

---

## Datapath modes

| Mode | Mechanism | Choose when |
|---|---|---|
| **Encapsulation** (VXLAN or Geneve) | Pod traffic tunnelled node to node | The underlying network does not route pod CIDRs. The default; works anywhere |
| **Native routing** | Pod CIDRs routed by the underlying network | You control the underlay and can advertise routes, statically or via BGP. Lower overhead, no MTU reduction, simpler packet capture |

---

## IPAM

Who allocates pod IPs:

- **Cluster pool** (default): Cilium carves per-node CIDRs from a cluster-wide pool
- **Kubernetes host scope**: uses the `PodCIDR` the Kubernetes controller manager assigns per node
- **CRD-backed**: allocation driven by custom resources for full control
- **Cloud provider modes** (AWS ENI, Azure IPAM, GKE): pod IPs come directly from the VPC, so pods are first-class network citizens and reachable without encapsulation

---

## kube-proxy replacement

Cilium can replace kube-proxy entirely, implementing Service handling in eBPF.

What changes:
- Service ClusterIP, NodePort, LoadBalancer, and ExternalIPs are handled by eBPF maps rather than iptables chains
- **Socket-level load balancing** translates the destination at `connect()` time for in-cluster clients, so there is no per-packet NAT at all
- Service lookup cost stops growing with service count
- iptables service chains disappear, which is directly observable and a good lab check

**Direct server return** and **Maglev** consistent hashing are available for external traffic, reducing hops and improving backend stability during scaling.

---

## Key terms

- **eBPF** - a technology for running verified, sandboxed programs inside the Linux kernel without kernel modules
- **eBPF verifier** - the kernel component proving an eBPF program terminates and accesses only permitted memory before it may load
- **eBPF map** - a typed key-value structure shared between kernel-side eBPF programs and user space
- **XDP** - the earliest eBPF network hook, in the driver, used for high-performance drop and load balancing
- **TC hook** - the traffic control hook where most of Cilium's datapath logic runs
- **Cilium agent** - the per-node DaemonSet compiling and loading eBPF programs and enforcing policy
- **Cilium operator** - the cluster-wide component handling IPAM, identity garbage collection, and CRD management
- **Identity** - a numeric value derived from an endpoint's labels, against which policy is enforced
- **Reserved entity** - a predefined identity such as world, host, remote-node, or cluster
- **Endpoint** - a network-addressable entity managed by Cilium, typically a pod
- **CRD identity mode** - identity allocation using Kubernetes custom resources instead of an external etcd
- **Encapsulation mode** - a datapath mode tunnelling pod traffic between nodes with VXLAN or Geneve
- **Native routing mode** - a datapath mode relying on the underlying network to route pod CIDRs directly
- **Cluster pool IPAM** - the default mode where Cilium allocates per-node pod CIDRs from a cluster-wide pool
- **kube-proxy replacement** - Cilium's eBPF implementation of Kubernetes Service handling, removing iptables service chains
- **Socket-level load balancing** - translating the service address at connect time so no per-packet NAT is needed
- **Maglev** - a consistent hashing algorithm improving backend stability for external service traffic

---

## Related

- [Notes 02: network policy](./02-network-policy.md)
- [Scenarios](../scenarios.md) - scenarios 1 and 5
- [Containers vs VMs](../../../../learn/concepts/containers-vs-vms.md)
