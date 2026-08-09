---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 9 min
---

# 03 - Service mesh and observability

**Domains: Service Mesh (16%) and Network Observability (10%)** - 26% combined.

---

## Sidecar-free service mesh

A traditional service mesh injects a proxy container into every pod. Cilium provides mesh capabilities from the **per-node datapath plus a per-node Envoy**, with no sidecar.

| | Sidecar mesh | Cilium sidecar-free |
|---|---|---|
| Proxy count | One per pod | One per node |
| Resource overhead | Multiplied by pod count | Multiplied by node count |
| Pod startup | Waits for sidecar readiness | No change |
| Upgrade | Restart every pod | Restart the node agent |
| Isolation | Per pod | Shared per node |
| L7 processing | Every hop through two proxies | Only where an L7 rule or feature requires it |

The trade-off is genuine: a shared per-node proxy has a larger blast radius than a per-pod one, and offers less per-workload isolation. The gain is a large reduction in resource use and operational churn.

Important nuance the exam expects: **L3/L4 traffic does not traverse a proxy at all.** Only traffic subject to an L7 rule or an L7 feature is redirected to Envoy. In a sidecar mesh, every packet crosses two proxies regardless.

---

## Traffic management

- **Gateway API** support for ingress, including HTTPRoute, GRPCRoute, and TLSRoute
- **Ingress** controller support for the older API
- **Layer 7 load balancing**, including traffic splitting for canary patterns
- **Envoy configuration** through `CiliumEnvoyConfig` and `CiliumClusterwideEnvoyConfig` for advanced cases

---

## Encryption

Two transparent encryption options for node-to-node pod traffic:

| | WireGuard | IPsec |
|---|---|---|
| Setup | Simpler, fewer moving parts | More configuration |
| Performance | Generally better | Good, depends on offload |
| Compliance | Modern cryptography | FIPS-validated options available |
| Typical choice | The default recommendation | Where a specific compliance requirement mandates IPsec |

**Transparent** means applications are unchanged: encryption happens in the datapath, not in the application or a sidecar.

**Mutual authentication** adds identity-based authentication between endpoints, backed by SPIFFE identities, so a policy can require that the peer proved its identity rather than merely appearing to have the right labels.

---

## Hubble

The observability layer, built on the same eBPF datapath.

| Component | Role |
|---|---|
| **Hubble (in agent)** | Produces flow records from datapath events on that node |
| **Hubble Relay** | Aggregates flows across all nodes into one API |
| **Hubble UI** | Web interface, including the service dependency map |
| **Hubble CLI** | `hubble observe` for querying flows |

A **flow record** contains source and destination identities, IPs, ports, protocol, the verdict (forwarded, dropped, audit), the drop reason if any, and, when L7 visibility is enabled, protocol details such as the HTTP method, path, and status code.

Because Hubble reads the datapath, it sees traffic **and** policy verdicts, which is what makes it faster than packet capture for diagnosing policy problems.

### Useful queries

```bash
hubble observe --verdict DROPPED
hubble observe --to-pod default/api --protocol http
hubble observe --from-label app=frontend --last 100
```

**L7 visibility** is enabled either by an L7 policy rule or by a visibility annotation, since it requires the traffic to traverse Envoy.

**Metrics**: Hubble exports Prometheus metrics for flows, drops, DNS, HTTP, and TCP, which feed Grafana dashboards and alerting. This is where Cilium and [OpenTelemetry](../../otca/) practice meet: Hubble supplies network-layer signals that application instrumentation cannot.

---

## Tetragon

Adjacent to the exam but worth knowing: **Tetragon** is the Cilium project's runtime security observability and enforcement component, using eBPF LSM and kprobe hooks to observe and enforce process execution, file access, and network activity. It complements the network policy story with process-level visibility.

---

## Key terms

- **Sidecar-free service mesh** - mesh capabilities provided by a per-node datapath and proxy rather than a per-pod sidecar
- **CiliumEnvoyConfig** - the custom resource providing advanced Envoy configuration for a namespace
- **Gateway API** - the successor Kubernetes ingress API supported by Cilium for L7 routing
- **Transparent encryption** - datapath-level encryption of pod-to-pod traffic requiring no application change
- **WireGuard** - the simpler, generally faster transparent encryption option in Cilium
- **IPsec** - the alternative transparent encryption option, chosen where compliance requires it
- **Mutual authentication** - identity-based peer authentication in Cilium, backed by SPIFFE identities
- **Hubble** - Cilium's observability layer producing flow records from the eBPF datapath
- **Hubble Relay** - the component aggregating flow data from all node agents into a single API
- **Flow record** - a Hubble event containing identities, addresses, protocol, verdict, and any drop reason
- **Verdict** - the Hubble field stating whether a flow was forwarded, dropped, or audited
- **L7 visibility** - Hubble's protocol-level detail, available where traffic traverses Envoy
- **Service dependency map** - the Hubble UI view showing which services communicate with which
- **Tetragon** - the Cilium project component providing eBPF-based runtime security observability and enforcement

---

## Related

- [Notes 04: operations, cluster mesh, and BGP](./04-operations-clustermesh-bgp.md)
- [Scenarios](../scenarios.md) - scenarios 3 and 7
- [OTCA](../../otca/) - application-level observability alongside Hubble's network view
