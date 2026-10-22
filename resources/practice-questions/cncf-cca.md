# Cilium Certified Associate (CCA) - Practice Questions

30 questions for CCA prep. The organizing idea: Cilium enforces policy on identity, not IP address.

> **Cert page:** [exams/kubernetes/cca/](../../exams/kubernetes/cca/)

---

### Question 1
**Scenario:** A team writes NetworkPolicy rules using `ipBlock` CIDRs matching current pod addresses. After a node drain, traffic breaks intermittently and some pods gain access they should not have.

A. Use label-based endpoint selectors so policy targets Cilium identities that survive rescheduling
B. Reserve static pod IPs for each workload with an IPAM pool, so the CIDR rules always match the same pod
C. Widen the CIDR ranges to the whole node subnet so rescheduled pods stay allowed
D. Add a NetworkPolicy per pod, rewritten by a controller each time its address changes

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Pod IPs are ephemeral and reused, so a recycled address can inherit an allow rule meant for a different workload. Identity is derived from labels and survives rescheduling. Widening CIDRs increases exposure; static IPs fight Kubernetes.
</details>

---

### Question 2
**Scenario:** A pod has no policies. A CiliumNetworkPolicy is created selecting it with one ingress rule. The team is surprised outbound internet access still works.

A. Egress requires a CiliumClusterwideNetworkPolicy, because namespaced policies only ever apply to ingress
B. Cilium does not support egress policy, so it falls back to default allow
C. Each direction becomes default-deny independently; the policy only selected the pod for ingress
D. The policy has not taken effect yet, because Cilium applies new rules only after the agent restarts on the node

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Selecting an endpoint for one direction makes only that direction deny-by-default. Restricting egress requires an egress rule. This asymmetry is one of the most reliably tested points on the exam.
</details>

---

### Question 3
**Scenario:** A service exposes `/health`, `/metrics`, and `/transfer` on port 8080. Monitoring must reach `/metrics` with GET only, and must never reach `/transfer`.

A. Move `/metrics` to a different port and allow only that port from the monitoring namespace
B. A layer 4 rule allowing port 8080 from the monitoring pods, with a deny rule on the `/transfer` path
C. Application-level authentication on `/transfer`, with the network policy left open on port 8080
D. A layer 7 CiliumNetworkPolicy with an HTTP rule for method GET and path `/metrics`, selecting the service pods

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Both endpoints share a port, so only a layer 7 rule can separate them. Matching traffic is redirected through the per-node Envoy for enforcement, and a denied request receives an HTTP 403 rather than a connection reset.
</details>

---

### Question 4
**Scenario:** A workload must reach `api.stripe.com` and nothing else on the internet. The addresses are CDN-served and change.

A. An HTTP rule matching the Host header `api.stripe.com`, applied to egress from the workload
B. An `ipBlock` listing the published CDN ranges, refreshed from the provider's JSON feed each week
C. A `toFQDNs` rule for `api.stripe.com` plus a visible DNS path with an L7 DNS rule
D. Allow egress to the `world` entity, then block other sites with an HTTP rule on the Host header

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cilium learns the addresses by observing DNS responses, so FQDN policy requires that DNS is permitted and visible. Forgetting the DNS rule is the classic reason FQDN policy appears not to work. Published CDN ranges go stale within weeks.
</details>

---

### Question 5
**Scenario:** What guarantees that an eBPF program cannot crash the kernel or read arbitrary memory?

A. JIT compilation, which translates the bytecode into native instructions that are bounds-checked at runtime
B. seccomp filtering, which limits the system calls the loader may make
C. The eBPF verifier, which proves termination and memory safety before the program may load
D. Running it in a container, whose namespaces confine the program's memory access to that container

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The verifier is the safety mechanism: a program that cannot be proven safe is rejected at load time. JIT compilation is a performance step that happens after verification. Containers and seccomp are unrelated to in-kernel program safety.
</details>

---

### Question 6
**Scenario:** A cloud cluster's pod CIDR is not known to the VPC route tables. Which datapath mode is required?

A. Native routing with `auto-direct-node-routes`, even when the nodes sit in different subnets
B. The mode makes no difference; Cilium edits the VPC route tables
C. Native routing, with the pod CIDRs advertised to the VPC through the Cilium agent
D. Encapsulation with VXLAN or Geneve, which tunnels pod traffic between nodes

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Native routing requires the underlying network to route pod CIDRs. Where it does not, tunnelling is required. Encapsulation costs some MTU and overhead but works on any underlay, which is why it is the default.
</details>

---

### Question 7
**Scenario:** What changes when kube-proxy replacement is enabled?

A. Service handling moves into eBPF maps, iptables service chains go away, and in-cluster clients can be load balanced at the socket layer
B. NetworkPolicy enforcement is disabled, because kube-proxy was the component that enforced policy on each node, and policy must then be rebuilt
C. Services stop working until every pod restarts and receives a new ClusterIP from the agent
D. Only NodePort services are affected, while ClusterIP and LoadBalancer services still use iptables

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Lookup cost stops growing with service count because eBPF uses hash maps rather than linear rule chains, and socket-level load balancing removes per-packet NAT for in-cluster clients. Policy enforcement is unaffected.
</details>

---

### Question 8
**Scenario:** Which is a prerequisite for Cluster Mesh that commonly blocks a first attempt?

A. All clusters must share one Entra tenant, so that a single identity provider signs every cluster's certificates
B. Each cluster needs a unique name and numeric cluster ID, and pod CIDRs must not overlap between clusters, for any datapath mode
C. All clusters must run the same Kubernetes minor version, because the clustermesh API server checks it on connect
D. All clusters must use native routing, since tunnel mode cannot carry cross-cluster traffic

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Two clusters installed with defaults share the same cluster ID, which is the most common blocker. Overlapping pod CIDRs make cross-cluster routing ambiguous. Kubernetes version parity and datapath mode are not requirements.
</details>

---

### Question 9
**Scenario:** Which command most quickly reveals why a packet was dropped after a policy change?

A. `hubble observe --verdict DROPPED`
B. `kubectl logs` on the application pod, which records every request the policy dropped
C. `cilium config view`, which prints each drop reason alongside the matching rule
D. `kubectl describe networkpolicy`, which lists the packets that were dropped by the policy

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Hubble reports the drop reason from the datapath, so `Policy denied` immediately distinguishes a policy problem from routing or DNS. `kubectl describe` shows what was requested rather than what is enforced, and the drop happens below the application.
</details>

---

### Question 10
**Scenario:** Which reserved entity represents everything outside the cluster?

A. `remote-node`, the identity for any destination outside the local cluster network
B. `world`, the reserved identity for destinations outside the cluster
C. `host`, the identity for addresses beyond the cluster
D. `cluster`, the identity for traffic from outside pods

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `world` is the reserved identity for external destinations. `cluster` covers all in-cluster endpoints, `host` is the local node, and `remote-node` covers other nodes in the cluster.
</details>

---

### Question 11
**Scenario:** Why must tail-sampling-style aggregation and cross-node correlation for Hubble use Hubble Relay rather than a single agent?

A. Agents cannot produce flow records, so Relay generates them from the Kubernetes API server events
B. Each agent sees only the flows on its own node; Relay aggregates them into one API
C. Relay performs the eBPF processing that the agents on each node are unable to do for themselves
D. Agents cannot be queried directly, because they listen only on a unix socket

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The agent produces flow records from its own node's datapath. Relay aggregates across nodes so a single query covers the cluster. The UI and CLI consume Relay's API.
</details>

---

### Question 12
**Scenario:** What is the trade-off of Cilium's sidecar-free service mesh compared with a per-pod sidecar mesh?

A. Lower resource use and no sidecar restarts, at the cost of a shared per-node proxy with a larger blast radius
B. It only works with Istio, since the sidecar-free mode reuses Istio's control plane for certificates
C. It cannot do layer 7 routing, so HTTP-aware features are limited to what NetworkPolicy provides
D. It requires more memory per pod, because each workload needs its own copy of the eBPF programs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** One proxy per node rather than per pod cuts resource use and removes sidecar restart churn, and L3/L4 traffic bypasses a proxy entirely. The cost is less per-workload isolation than a dedicated sidecar provides.
</details>

---

### Question 13
**Scenario:** An on-premises cluster needs LoadBalancer services without a cloud provider, and pod CIDRs advertised to the physical network.

A. Cluster Mesh, which allocates LoadBalancer IPs and announces them to routers
B. LB IPAM for service IP allocation plus the BGP Control Plane to advertise them and the pod CIDRs
C. Encapsulation mode with a hostPort on each pod, so clients use the node address
D. NodePort services and static routes on the physical routers, pointing at each node's address and maintained by hand for every node

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** LB IPAM assigns service IPs from configured pools without a cloud provider, and BGP advertises both those IPs and pod CIDRs to the network. Together they provide working LoadBalancer services and native routing on-premises.
</details>

---

### Question 14
**Scenario:** A partner requires that traffic from the cluster arrives from a fixed, allowlistable source IP.

A. Masquerading to the node IP, which gives each pod's traffic the address of the node it runs on
B. Cluster Mesh service affinity, which pins connections to a fixed set of endpoints across clusters
C. Egress gateway routing selected traffic through designated nodes with fixed IPs
D. A NodePort service, whose port and node address stay constant for outbound traffic from the pod

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** By default egress is masqueraded to whichever node the pod runs on, so the source address varies and changes on every scale event. Egress gateway pins selected traffic to designated nodes so the partner can allowlist a stable address.
</details>

---

### Question 15
**Scenario:** Which policy resource protects the node itself, for example the kubelet port?

A. An NSG equivalent in the CNI configuration, applied to the node's network interface by the agent
B. A namespaced CiliumNetworkPolicy that selects the kubelet pod by label in the kube-system namespace
C. A Kubernetes NetworkPolicy with an ipBlock for the node address and port 10250, applied to the host network namespace
D. A CiliumClusterwideNetworkPolicy with a `nodeSelector`, as host firewall

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Host firewall applies cluster-wide policy to the node's own network namespace using a node selector. Namespaced policies and Kubernetes NetworkPolicy apply to pods, not to host-network ports.
</details>

---

### Question 16
**Scenario:** Which Cilium component runs on every node, loads the eBPF programs into the kernel, and enforces policy for the pods on that node?

A. The Cilium operator, which runs once per cluster and programs every node's kernel remotely
B. Hubble Relay, which collects flows from each node and installs the policy programs it needs
C. The Cilium agent, which runs as a DaemonSet with one instance on each node
D. The clustermesh-apiserver, which runs on each node and pushes eBPF programs to pods

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The cilium-agent DaemonSet runs on every node, watches the Kubernetes API, compiles and loads eBPF programs, and manages endpoints and policy locally. The operator handles cluster-wide tasks, such as IPAM allocation and garbage collection, and does not program kernels. Hubble Relay aggregates flows for observability. The clustermesh-apiserver exposes cluster state to other clusters.
</details>

---

### Question 17
**Scenario:** A Deployment scales from 2 to 50 replicas, all with the same labels. How many Cilium security identities does this add for those pods?

A. One identity per pod, so 50 identities that each have their own policy entries in the eBPF maps
B. One identity shared by all replicas, because identity is derived from the security-relevant labels
C. One identity per node that runs a replica, because identities are allocated by each cilium-agent
D. No identities at all, because Deployment pods are matched by their IP addresses instead

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cilium derives a numeric security identity from the set of security-relevant labels, so pods with identical labels share one identity regardless of count or node. That is why scaling does not grow policy state per pod. Identities are allocated cluster-wide (for example as CiliumIdentity resources), not per node, and policy is based on identity rather than IP.
</details>

---

### Question 18
**Scenario:** On AWS, pods must receive IP addresses directly from the VPC subnets so that other VPC resources can reach them without overlay or NAT.

A. Cluster-pool IPAM with tunnel mode, which advertises the pod CIDR into the VPC route tables
B. Kubernetes host-scope IPAM, which assigns VPC addresses taken from each node's own podCIDR
C. Multi-pool IPAM, which allocates pod addresses from a pool outside the VPC address range
D. ENI IPAM mode, which allocates pod IPs from Elastic Network Interfaces attached to the nodes

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** In ENI mode the Cilium operator attaches ENIs and assigns their secondary IPs to pods, so pods have routable VPC addresses. Cluster-pool with tunneling keeps pod addresses in an overlay unknown to the VPC. Host-scope IPAM uses the node's podCIDR, which is not a VPC address range. A pool outside the VPC range is not routable in the VPC by default.
</details>

---

### Question 19
**Scenario:** A namespace is under default deny for egress. An operator pod must be allowed to reach the Kubernetes API server, whose addresses differ between clusters.

A. A `toEntities` rule with the `kube-apiserver` entity in a CiliumNetworkPolicy
B. A `toCIDR` rule with the API server addresses copied from the current cluster
C. A `toFQDNs` rule for `kubernetes.default.svc`, which resolves the API server
D. A `toEntities` rule with the `world` entity, which includes the API server

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The `kube-apiserver` entity represents the API server wherever it runs, inside or outside the cluster, so the rule is portable. Copied CIDRs break between clusters and when addresses change. FQDN rules are for external DNS names and are not the intended mechanism here. `world` allows the whole internet, far beyond the requirement, and may not even cover an in-cluster API server.
</details>

---

### Question 20
**Scenario:** A broad allow policy permits a namespace to receive traffic from the whole cluster. Security now requires that pods labeled `env=sandbox` can never reach it, whatever other allow rules exist.

A. Add a second allow policy that omits the sandbox pods, which overrides the broad one
B. Delete the broad policy, since Cilium does not support deny rules of any kind
C. Add an `ingressDeny` rule selecting `env=sandbox`, since deny rules take precedence over allow rules
D. Lower the priority of the broad allow policy so that it is evaluated after other policies

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cilium supports deny policies (`ingressDeny` and `egressDeny`), and deny rules take precedence over allow rules regardless of the order in which they are created. Allow policies are additive, so another allow cannot remove access. Cilium does support deny. Standard policies have no priority field to reorder evaluation.
</details>

---

### Question 21
**Scenario:** A security team wants one baseline policy, such as allowing DNS to kube-dns, applied to every namespace including namespaces created later.

A. A NetworkPolicy in the default namespace, which Kubernetes copies to every namespace
B. A CiliumClusterwideNetworkPolicy, which is cluster-scoped and selects endpoints in all namespaces
C. A CiliumNetworkPolicy in each namespace, created by hand whenever a namespace is added
D. A Hubble rule, which enforces the baseline at the observability layer for each namespace

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CiliumClusterwideNetworkPolicy is a cluster-scoped resource that can select endpoints across all namespaces, including future ones. NetworkPolicies are namespaced and not copied anywhere. Per-namespace copies drift and miss new namespaces. Hubble observes flows and does not enforce policy.
</details>

---

### Question 22
**Scenario:** A team wants mutual authentication between two services enforced by Cilium policy, with workload identities issued by SPIFFE, without injecting sidecars.

A. Enable WireGuard transparent encryption, which authenticates each workload with its own certificate
B. Install Istio sidecars on both services, since Cilium cannot take part in mutual authentication
C. Add an L7 HTTP rule to the policy, which requires a client certificate on every request
D. Enable Cilium mutual authentication with SPIRE, and set `authentication.mode: required` in the policy

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cilium's mutual authentication uses SPIRE to issue SPIFFE identities and authenticates peers before allowing traffic matched by a policy rule with `authentication.mode: required`, without sidecars. WireGuard encrypts node-to-node traffic and authenticates nodes, not workloads. Sidecars are not needed. L7 HTTP rules match paths and methods, not client certificates.
</details>

---

### Question 23
**Scenario:** A cluster running Cilium needs north-south HTTP routing with path-based rules and header matching, using the standard Kubernetes routing API rather than vendor annotations.

A. Gateway API resources, such as Gateway and HTTPRoute, implemented by Cilium with Envoy
B. A CiliumNetworkPolicy with L7 HTTP rules, which routes requests to different backends
C. Cluster Mesh global services, which route requests between clusters by path
D. NodePort services with one port per path, mapped by the external load balancer

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cilium implements the Kubernetes Gateway API, so Gateway and HTTPRoute resources provide path and header based routing through its Envoy proxy. L7 policy rules allow or deny requests and do not route them. Global services spread load across clusters. One NodePort per path pushes routing outside the cluster.
</details>

---

### Question 24
**Scenario:** The team wants dashboards and alerts on HTTP request rates, error codes, and DNS failures per workload, built from Hubble data in Prometheus.

A. Run `hubble observe` in a loop and parse the output into a spreadsheet for the dashboards
B. Enable Hubble metrics with the needed metric types, such as `http` and `dns`, and scrape them
C. Enable the Cilium operator metrics only, which include per-workload request and DNS data
D. Install a sidecar exporter in every pod, since Hubble data cannot be turned into metrics

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hubble can export flow-derived metrics, configured by metric type such as dns, drop, tcp, flow, and http, for Prometheus to scrape. Parsing CLI output does not scale. Operator metrics describe the operator, not workload traffic. Sidecars are unnecessary because Hubble already sees the flows.
</details>

---

### Question 25
**Scenario:** A new engineer needs a visual map of which services talk to which in a namespace, with live flows and policy verdicts.

A. The Kubernetes dashboard, which draws service dependencies from Service objects
B. The `cilium status` command, which prints a dependency graph of the namespace
C. A Prometheus graph of pod CPU usage, which shows services that call each other
D. Hubble UI, which renders a service dependency map from observed flows

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Hubble UI builds a service map from real flows observed by Hubble and shows flow details, including whether policy allowed or dropped them. The Kubernetes dashboard shows resources, not traffic between them. `cilium status` reports component health. CPU graphs do not reveal communication.
</details>

---

### Question 26
**Scenario:** After installing Cilium on a new cluster, the team wants to confirm components are healthy and that pod-to-pod, pod-to-service, and policy behavior work end to end.

A. Run `kubectl get pods -A`, since running pods prove that the datapath works
B. Run `cilium status --wait`, then `cilium connectivity test`
C. Run `hubble observe` once, since any flow output proves policy works
D. Reboot each node, since Cilium reports problems only during startup

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `cilium status` reports the health of the agents, operator, and related components, and `cilium connectivity test` deploys test workloads that exercise many connectivity and policy scenarios. Running pods do not prove that traffic flows correctly. A single flow sample proves little. Rebooting nodes is disruptive and unnecessary.
</details>

---

### Question 27
**Scenario:** Two clusters connected with Cluster Mesh each run a `checkout` Service in the `shop` namespace. Clients in either cluster should load balance across backends in both clusters.

A. Rename one of the Services, since Cluster Mesh rejects two Services with the same name
B. Create an ExternalName Service in each cluster that points at the other cluster's Service
C. Annotate both Services with `service.cilium.io/global: "true"`
D. Enable BGP on both clusters to advertise the Service IPs to each other

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A global service is a Service with the same name and namespace in each cluster and the `service.cilium.io/global: "true"` annotation, which merges the backends across clusters. Same-named Services are exactly what Cluster Mesh expects. ExternalName only does DNS aliasing. BGP advertises routes and does not merge Service backends.
</details>

---

### Question 28
**Scenario:** A global service should send traffic to local backends normally and use the other cluster's backends only when no local backend is healthy.

A. Set `service.cilium.io/affinity: "local"` on the global service
B. Set `service.cilium.io/shared: "false"` on the global service
C. Set `externalTrafficPolicy: Local` on the Service in each cluster
D. Remove the global annotation from one cluster's Service

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The affinity annotation set to `local` makes Cilium prefer local endpoints and fail over to remote ones when no local endpoint is healthy. `shared: "false"` stops the cluster sharing its backends with others, which breaks failover in one direction. `externalTrafficPolicy` affects external traffic to node ports and load balancers. Removing the annotation ends the global behavior.
</details>

---

### Question 29
**Scenario:** Cilium's eBPF programs need to look up policy decisions, connection tracking entries, and service backends quickly, and user space must update them. Where does that state live?

A. In iptables chains, which the eBPF programs read on each packet
B. In etcd, which the eBPF programs query on each packet
C. In eBPF maps, key-value stores shared by kernel programs and user space
D. In the pod's file system, which the programs read through a mounted volume

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** eBPF maps are kernel data structures, such as hash tables and arrays, that eBPF programs read and write at packet speed and that user space (the cilium-agent) updates. Using eBPF maps instead of iptables chains is a core design point. eBPF programs cannot query etcd or read pod file systems on the packet path.
</details>

---

### Question 30
**Scenario:** An on-premises cluster sits on a flat Layer 2 network with no BGP-capable router. LoadBalancer IPs from a Cilium IP pool must be reachable from other hosts on that network.

A. Advertise the IPs with the BGP Control Plane, which peers with the hosts on the subnet
B. Enable L2 announcements, so a node answers ARP requests for each LoadBalancer IP
C. Enable Cluster Mesh, which publishes LoadBalancer IPs to every host on the network
D. Use hostNetwork pods, which make every LoadBalancer IP reachable on each node

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cilium L2 announcements make an elected node respond to ARP (and NDP) for service IPs, so hosts on the same Layer 2 segment can reach them without routing protocols. BGP needs a peer that speaks BGP, which this network lacks. Cluster Mesh connects clusters. hostNetwork pods do not make pool IPs answer on the network.
</details>

---

## Scoring guide

- **26-30 correct (85%+):** Ready. 75% is the pass mark.
- **20-25 correct (67-83%):** Review the identity model and the default-deny semantics, which underpin most misses.
- **Below 20:** Install Cilium on kind and work the labs in the [practice plan](../../exams/kubernetes/cca/practice-plan.md).
