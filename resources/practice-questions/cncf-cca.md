# Cilium Certified Associate (CCA) - Practice Questions

15 questions for CCA prep. The organizing idea: Cilium enforces policy on identity, not IP address.

> **Cert page:** [exams/kubernetes/cca/](../../exams/kubernetes/cca/)

---

### Question 1
**Scenario:** A team writes NetworkPolicy rules using `ipBlock` CIDRs matching current pod addresses. After a node drain, traffic breaks intermittently and some pods gain access they should not have.

A. Reserve static pod IPs
B. Widen the CIDR ranges
C. Use label-based endpoint selectors so policy targets Cilium identities
D. Add a NetworkPolicy per pod

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Pod IPs are ephemeral and reused, so a recycled address can inherit an allow rule meant for a different workload. Identity is derived from labels and survives rescheduling. Widening CIDRs increases exposure; static IPs fight Kubernetes.
</details>

---

### Question 2
**Scenario:** A pod has no policies. A CiliumNetworkPolicy is created selecting it with one ingress rule. The team is surprised outbound internet access still works.

A. The policy has not taken effect yet
B. Ingress and egress become default-deny independently; the policy only selected the pod for ingress
C. Cilium does not support egress policy
D. Egress requires a CiliumClusterwideNetworkPolicy

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Selecting an endpoint for one direction makes only that direction deny-by-default. Restricting egress requires an egress rule. This asymmetry is one of the most reliably tested points on the exam.
</details>

---

### Question 3
**Scenario:** A service exposes `/health`, `/metrics`, and `/transfer` on port 8080. Monitoring must reach `/metrics` with GET only, and must never reach `/transfer`.

A. A layer 4 rule allowing port 8080
B. A layer 7 CiliumNetworkPolicy with an HTTP rule for method GET and path `/metrics`
C. Move `/metrics` to a different port
D. Application-level authentication

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Both endpoints share a port, so only a layer 7 rule can separate them. Matching traffic is redirected through the per-node Envoy for enforcement, and a denied request receives an HTTP 403 rather than a connection reset.
</details>

---

### Question 4
**Scenario:** A workload must reach `api.stripe.com` and nothing else on the internet. The addresses are CDN-served and change.

A. An `ipBlock` listing published CDN ranges
B. A `toFQDNs` rule for `api.stripe.com` plus an allowed, visible DNS path with an L7 DNS rule
C. Allow egress to the `world` entity
D. An HTTP rule matching the Host header

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cilium learns the addresses by observing DNS responses, so FQDN policy requires that DNS is permitted and visible. Forgetting the DNS rule is the classic reason FQDN policy appears not to work. Published CDN ranges go stale within weeks.
</details>

---

### Question 5
**Scenario:** What guarantees that an eBPF program cannot crash the kernel or read arbitrary memory?

A. Running it in a container
B. The eBPF verifier, which proves termination and memory safety before the program may load
C. JIT compilation
D. seccomp filtering

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The verifier is the safety mechanism: a program that cannot be proven safe is rejected at load time. JIT compilation is a performance step that happens after verification. Containers and seccomp are unrelated to in-kernel program safety.
</details>

---

### Question 6
**Scenario:** A cloud cluster's pod CIDR is not known to the VPC route tables. Which datapath mode is required?

A. Native routing
B. Encapsulation with VXLAN or Geneve
C. Either, since Cilium handles routing itself
D. Native routing with `auto-direct-node-routes`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Native routing requires the underlying network to route pod CIDRs. Where it does not, tunnelling is required. Encapsulation costs some MTU and overhead but works on any underlay, which is why it is the default.
</details>

---

### Question 7
**Scenario:** What changes when kube-proxy replacement is enabled?

A. Services stop working until pods restart
B. Service handling moves into eBPF maps, iptables service chains disappear, and in-cluster clients can be load balanced at the socket layer
C. NetworkPolicy enforcement is disabled
D. Only NodePort services are affected

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Lookup cost stops growing with service count because eBPF uses hash maps rather than linear rule chains, and socket-level load balancing removes per-packet NAT for in-cluster clients. Policy enforcement is unaffected.
</details>

---

### Question 8
**Scenario:** Which is a prerequisite for Cluster Mesh that commonly blocks a first attempt?

A. All clusters must run the same Kubernetes version
B. All clusters must share one Entra tenant
C. Each cluster needs a unique name and numeric cluster ID, and pod CIDRs must not overlap
D. All clusters must use native routing

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Two clusters installed with defaults share the same cluster ID, which is the most common blocker. Overlapping pod CIDRs make cross-cluster routing ambiguous. Kubernetes version parity and datapath mode are not requirements.
</details>

---

### Question 9
**Scenario:** Which command most quickly reveals why a packet was dropped after a policy change?

A. `kubectl describe networkpolicy`
B. `hubble observe --verdict DROPPED`
C. `kubectl logs` on the application pod
D. `cilium config view`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hubble reports the drop reason from the datapath, so `Policy denied` immediately distinguishes a policy problem from routing or DNS. `kubectl describe` shows what was requested rather than what is enforced, and the drop happens below the application.
</details>

---

### Question 10
**Scenario:** Which reserved entity represents everything outside the cluster?

A. `cluster`
B. `remote-node`
C. `world`
D. `host`

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `world` is the reserved identity for external destinations. `cluster` covers all in-cluster endpoints, `host` is the local node, and `remote-node` covers other nodes in the cluster.
</details>

---

### Question 11
**Scenario:** Why must tail-sampling-style aggregation and cross-node correlation for Hubble use Hubble Relay rather than a single agent?

A. Agents cannot produce flow records
B. Each agent sees only the flows on its own node; Relay aggregates them into one API
C. Relay performs the eBPF processing
D. Agents cannot be queried directly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The agent produces flow records from its own node's datapath. Relay aggregates across nodes so a single query covers the cluster. The UI and CLI consume Relay's API.
</details>

---

### Question 12
**Scenario:** What is the trade-off of Cilium's sidecar-free service mesh compared with a per-pod sidecar mesh?

A. It cannot do layer 7 routing
B. Lower resource use and no per-pod proxy restarts, at the cost of a shared per-node proxy with a larger blast radius
C. It requires more memory per pod
D. It only works with Istio

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** One proxy per node rather than per pod cuts resource use and removes sidecar restart churn, and L3/L4 traffic bypasses a proxy entirely. The cost is less per-workload isolation than a dedicated sidecar provides.
</details>

---

### Question 13
**Scenario:** An on-premises cluster needs LoadBalancer services without a cloud provider, and pod CIDRs advertised to the physical network.

A. NodePort services and static routes
B. LB IPAM for service IP allocation plus the BGP Control Plane to advertise them and the pod CIDRs
C. Encapsulation mode with a hostPort
D. Cluster Mesh

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** LB IPAM assigns service IPs from configured pools without a cloud provider, and BGP advertises both those IPs and pod CIDRs to the network. Together they provide working LoadBalancer services and native routing on-premises.
</details>

---

### Question 14
**Scenario:** A partner requires that traffic from the cluster arrives from a fixed, allowlistable source IP.

A. Masquerading to the node IP
B. Egress gateway routing selected traffic through designated nodes with fixed IPs
C. A NodePort service
D. Cluster Mesh service affinity

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** By default egress is masqueraded to whichever node the pod runs on, so the source address varies and changes on every scale event. Egress gateway pins selected traffic to designated nodes so the partner can allowlist a stable address.
</details>

---

### Question 15
**Scenario:** Which policy resource protects the node itself, for example the kubelet port?

A. A namespaced CiliumNetworkPolicy
B. A CiliumClusterwideNetworkPolicy with a `nodeSelector`, as host firewall
C. A Kubernetes NetworkPolicy
D. An NSG equivalent in the CNI configuration

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Host firewall applies cluster-wide policy to the node's own network namespace using a node selector. Namespaced policies and Kubernetes NetworkPolicy apply to pods, not to host-network ports.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready. 75% is the pass mark.
- **10-12 correct (65-80%):** Review the identity model and the default-deny semantics, which underpin most misses.
- **Below 10:** Install Cilium on kind and work the labs in the [practice plan](../../exams/kubernetes/cca/practice-plan.md).
