---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 5 min
---

# Cilium Certified Associate (CCA)

eBPF-based networking, security, and observability for Kubernetes. CCA covers the Cilium datapath, identity-based network policy, sidecar-free service mesh, Hubble observability, cluster mesh, and the eBPF foundations underneath all of it.

This is the only certification in the repo that teaches **eBPF**, which now underpins a large share of cloud native networking, security, and observability tooling.

## Exam Details

- **Exam Code:** CCA
- **Duration:** 90 minutes
- **Questions:** 60, multiple choice and multiple select
- **Passing Score:** 75%
- **Cost:** USD 250, includes one free retake
- **Validity:** 2 years
- **Prerequisites:** None formal; Kubernetes networking assumed
- **Format:** Knowledge-based, not hands-on

Full detail in the [fact sheet](./fact-sheet.md).

## Domains and notes

Eight domains, grouped into four notes:

| Notes | Domains covered | Combined weight |
|---|---|---:|
| [01 eBPF and architecture](./notes/01-ebpf-and-architecture.md) | eBPF (10%), Architecture (20%) | 30% |
| [02 Network policy](./notes/02-network-policy.md) | Network Policy (18%) | 18% |
| [03 Service mesh and observability](./notes/03-service-mesh-and-observability.md) | Service Mesh (16%), Network Observability (10%) | 26% |
| [04 Operations, cluster mesh, and BGP](./notes/04-operations-clustermesh-bgp.md) | Installation (10%), Cluster Mesh (10%), BGP (6%) | 26% |

## The idea that unlocks the exam

**Cilium enforces on identity, not IP address.**

In a traditional network, policy is written against IP ranges. In Kubernetes, pod IPs are ephemeral and reused within seconds, so IP-based policy is both fragile and slow to converge.

Cilium derives a numeric **identity** from a pod's labels. Every pod with the same labels shares one identity, and policy is enforced against identities in the eBPF datapath. That is why Cilium scales where iptables-based approaches struggle: the number of policy entries tracks the number of distinct label sets, not the number of pods.

Once you have that model, the architecture, policy, and cluster mesh domains follow from it.

## Study sequence

1. **eBPF fundamentals** - what it is, the verifier, maps, hook points. Short, and everything else assumes it.
2. **Architecture** - agent, operator, datapath modes, IPAM, kube-proxy replacement, identities.
3. **Network policy** - the largest single domain after architecture, and the most practical.
4. **Service mesh and Hubble.**
5. **Operations, cluster mesh, BGP.**

Schedule in the [practice plan](./practice-plan.md).

## Hands-on

Cilium installs on kind in minutes with the Cilium CLI. Worth doing:

- `cilium install`, then `cilium status` and `cilium connectivity test`
- Apply a default-deny CiliumNetworkPolicy and watch traffic break in Hubble
- Write a layer 7 HTTP policy allowing only `GET /public` and see the difference from a layer 4 rule
- Use `toFQDNs` to allow egress to one domain, then observe DNS-based enforcement
- Enable Hubble UI and look at the service dependency map
- Enable kube-proxy replacement and check that iptables rules for services are gone

## Study resources

- **[📖 Cilium documentation](https://docs.cilium.io/)** - the primary source; the exam tracks it closely
- **[📖 CCA curriculum](https://github.com/cncf/curriculum)** - published domains
- **[📖 Cilium and eBPF labs](https://isovalent.com/labs/)** - free browser-based labs
- **[📖 eBPF documentation](https://ebpf.io/)** - the foundation
- [Practice questions](../../../resources/practice-questions/cncf-cca.md) - question bank in this repo

## Related

- [CKA](../cka/) - Kubernetes operations
- [CKS](../cks/) - Kubernetes security, including network policy
- [OTCA](../otca/) - observability, complementing Hubble
- [Networking topic](../../../topics/networking.md)
- [Load balancing deep dive](../../../resources/networking-deep-dives/load-balancing-deep-dive.md)
