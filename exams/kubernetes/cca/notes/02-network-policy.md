---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 10 min
---

# 02 - Network policy

**Domain: Network Policy (18%)**

---

## Three policy resources

| Resource | Scope | Capability |
|---|---|---|
| **NetworkPolicy** (Kubernetes) | Namespaced | L3 and L4 only, ingress and egress by pod selector, namespace selector, and CIDR |
| **CiliumNetworkPolicy** | Namespaced | Adds L7 (HTTP, Kafka, DNS), FQDN egress, entities, and richer selectors |
| **CiliumClusterwideNetworkPolicy** | Cluster-scoped | The same, applied across all namespaces; used for baselines and host policy |

Cilium enforces Kubernetes NetworkPolicy as well, so both can coexist.

---

## Default deny semantics

This is the most reliably tested behavior on the exam.

- A pod that **no policy selects** allows all traffic in both directions.
- As soon as **any policy selects it for ingress**, ingress becomes deny-by-default and only explicitly allowed ingress passes.
- The same applies **independently** for egress.

So a policy that only specifies ingress rules leaves egress completely open. Restricting egress requires an egress rule.

A cluster-wide baseline commonly looks like a `CiliumClusterwideNetworkPolicy` selecting everything with empty ingress and egress rule lists, which denies both directions, then per-application policies layer allowances on top.

---

## Layer 3 selectors

| Selector | Matches |
|---|---|
| `endpointSelector` | Endpoints by label, the identity-based selector |
| `toEndpoints` / `fromEndpoints` | Peer endpoints by label |
| `toCIDR` / `fromCIDR` | External IP ranges, with `toCIDRSet` for exclusions |
| `toEntities` / `fromEntities` | Reserved entities: `world`, `cluster`, `host`, `remote-node`, `all` |
| `toServices` | Kubernetes services by name or label |
| `toGroups` | Cloud provider groups, such as an AWS security group |
| `toNodes` | Node identities |

Label-based selection is the default and the correct answer for in-cluster traffic. CIDR selection is for genuinely external, stable ranges.

---

## Layer 4

```yaml
toPorts:
  - ports:
      - port: "443"
        protocol: TCP
```

Combined with an L3 selector, this restricts which identities may reach which ports.

---

## Layer 7

Enforced by redirecting matching traffic to the per-node **Envoy** proxy.

**HTTP**:
```yaml
toPorts:
  - ports:
      - port: "8080"
        protocol: TCP
    rules:
      http:
        - method: "GET"
          path: "/metrics"
```

Also supported: header matching, and host matching.

**Kafka**: restrict by API key, topic, and role.

**DNS**: restrict which names an endpoint may resolve, with `matchName` and `matchPattern`.

Two behaviors worth knowing:
- A denied L7 request receives a protocol-level rejection (an HTTP 403) rather than a dropped packet, which makes the diagnosis different from an L3/L4 denial
- L7 rules cost more than L3/L4 because traffic traverses a proxy, so apply them selectively

---

## FQDN-based egress

```yaml
egress:
  - toEndpoints:
      - matchLabels:
          k8s:io.kubernetes.pod.namespace: kube-system
          k8s:k8s-app: kube-dns
    toPorts:
      - ports:
          - port: "53"
            protocol: ANY
        rules:
          dns:
            - matchPattern: "*"
  - toFQDNs:
      - matchName: "api.stripe.com"
```

Cilium learns the addresses by **observing DNS responses**, then programs them into the policy datapath for the record's TTL. That is why the DNS rule is mandatory: without visible, allowed DNS, `toFQDNs` has nothing to populate from.

Forgetting the DNS rule is the most common reason FQDN policy appears not to work.

---

## Enforcement modes and host policy

**Policy enforcement mode** is a cluster-wide setting:
- `default` - deny-by-default begins per direction once a policy selects the endpoint (the standard behavior described above)
- `always` - every endpoint is deny-by-default from the start, regardless of policy
- `never` - policy is not enforced, useful for a staged rollout or troubleshooting

**Host firewall** applies `CiliumClusterwideNetworkPolicy` with `nodeSelector` to the node itself, protecting host-network ports such as the kubelet and etcd.

---

## Troubleshooting

| Command | Shows |
|---|---|
| `cilium endpoint list` | Identity per endpoint and whether ingress and egress enforcement is on |
| `cilium policy get` | The policy actually loaded by the agent |
| `hubble observe --verdict DROPPED` | Dropped flows with a drop reason |
| `cilium monitor --type drop` | Live drop events from the datapath |

A verdict of `Policy denied` confirms a policy cause. A timeout with no Hubble record usually means the traffic never reached the datapath, which points at routing or DNS instead.

---

## Key terms

- **CiliumNetworkPolicy** - the namespaced Cilium policy resource supporting L3, L4, and L7 rules
- **CiliumClusterwideNetworkPolicy** - the cluster-scoped Cilium policy resource, used for baselines and host firewall
- **Default deny** - the behavior where a direction becomes deny-by-default once any policy selects the endpoint for it
- **endpointSelector** - the label-based selector identifying which endpoints a policy applies to
- **toEntities** - a selector matching reserved identities such as world, host, or remote-node
- **toFQDNs** - an egress rule matching DNS names, populated by observing DNS responses
- **matchPattern** - the wildcard form used in DNS and FQDN rules
- **Layer 7 policy** - policy matching application protocol details, enforced by redirecting traffic through Envoy
- **Policy enforcement mode** - the cluster-wide setting choosing default, always, or never enforcement
- **Host firewall** - policy applied to the node itself through a cluster-wide policy with a node selector
- **Drop reason** - the datapath explanation Hubble reports for a dropped packet, such as Policy denied

---

## Related

- [Notes 03: service mesh and observability](./03-service-mesh-and-observability.md)
- [Scenarios](../scenarios.md) - scenarios 2, 3, 4, and 7
- [CKS](../../cks/) - Kubernetes NetworkPolicy in the security exam
