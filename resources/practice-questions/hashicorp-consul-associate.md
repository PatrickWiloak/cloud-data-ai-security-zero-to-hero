---
last-updated: 2026-10-22
difficulty: intermediate
---

# HashiCorp Consul Associate (003) - Practice Questions

30 questions for Consul Associate prep, weighted toward architecture (18%), service discovery (17%), service mesh (17%), and single-datacenter deployment (16%).

> **Cert page:** [exams/hashicorp/consul-associate/](../../exams/hashicorp/consul-associate/)

---

### Question 1
**Scenario:** How many Consul servers should a production datacenter run?

A. As many as there are clients
B. One
C. Two
D. An odd number, typically 3 or 5, to form a Raft quorum

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Raft needs a majority to commit, so an odd count avoids wasted capacity: 3 servers tolerate 1 failure and 5 tolerate 2. Two servers tolerate zero failures and are worse than one, because losing either loses quorum.
</details>

---

### Question 2
**Scenario:** What protocol does Consul use for membership and failure detection?

A. DNS, which resolves service names and also tracks which nodes are still alive in the datacenter
B. BGP
C. Gossip, based on SWIM, over the LAN and WAN pools
D. Raft consensus, run among the servers to replicate state

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Gossip handles membership, failure detection, and event broadcast among all agents. Raft is used separately, and only among servers, for consistency of the state store. Keeping the two straight explains why client agents scale to thousands while servers stay at 3 or 5.
</details>

---

### Question 3
**Scenario:** A service must be discoverable by name from any host in the datacenter.

A. Put the service behind a load balancer and share the balancer's IP address in the documentation
B. Register with a Consul agent; query `<service>.service.consul` via DNS
C. Publish the service name in `/etc/hosts` on every host and refresh the file with a nightly configuration-management run
D. Hard-code the IP addresses in each client's application configuration and redeploy on change

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Registration plus the DNS interface is the core discovery loop, and only instances passing their health checks are returned. That last part is what makes discovery useful: a failed instance disappears from results without anyone editing configuration.
</details>

---

### Question 4
**Scenario:** A registered service's health check fails.

A. Nothing changes
B. The instance stops being returned by discovery queries while remaining registered
C. Consul restarts the service
D. The instance is deregistered automatically the moment the check fails, and an operator must register it again

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Health status gates discovery results, not registration. The instance reappears automatically when the check passes again. Consul does not manage process lifecycle, which is Nomad's or the platform's job.
</details>

---

### Question 5
**Scenario:** Service-to-service traffic must be encrypted and authorized by service identity.

A. TLS on the Consul HTTP API and RPC ports only, with an ACL token required on every request
B. Consul service mesh (Connect) with sidecar proxies, mTLS, and intentions
C. Firewall rules
D. Gossip encryption

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Connect issues each service an identity certificate and the sidecar enforces mTLS, while intentions define which service may call which by name rather than by IP. Gossip encryption protects agent membership traffic, which is a different channel entirely.
</details>

---

### Question 6
**Scenario:** A default-deny posture is wanted for the service mesh.

A. Set the default intention to deny, then add explicit allow intentions per service pair
B. Rely on network segmentation and security groups between subnets, with each team owning its own allow rules
C. Disable Connect
D. Set default allow

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Intentions evaluate most-specific-first with a configurable default, and switching that default to deny turns the mesh into an allow-list. This is the same reasoning as a default-deny NetworkPolicy, but expressed in service identity rather than IP addresses.
</details>

---

### Question 7
**Scenario:** ACLs are enabled and an agent cannot register services.

A. Restart the Consul agent and all servers, which clears the cached ACL decisions and lets registration succeed
B. Disable ACLs
C. The agent needs a token granting `service:write` for that service name, so check its ACL policy
D. ACLs apply only to reads from the KV store and do not affect registration, so the failure is a network problem

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** With ACLs enabled the default policy is deny, so every operation needs an explicitly granted token. Agent tokens, node identities, and service identities are the mechanisms that scope this, and disabling ACLs to make an error go away removes the security model.
</details>

---

### Question 8
**Scenario:** Configuration values must be shared across services and rendered into config files as they change.

A. The Consul KV store with consul-template watching the keys
B. The catalog, which stores the list of nodes and services and pushes updates into config files
C. Environment variables baked into each container image at build time
D. A shared NFS mount

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** KV holds the values and consul-template subscribes to changes, re-rendering a file and optionally reloading the process. This is how legacy applications that read config from disk participate in dynamic configuration without being rewritten.
</details>

---

### Question 9
**Scenario:** Consul state must be backed up before an upgrade.

A. No backup is needed, because Raft replication already keeps a full copy on every server
B. Copy the data directory from the leader while Consul is still running, then restore it by file copy
C. `consul snapshot save`, restored later with `consul snapshot restore`
D. Export the KV store only with `consul kv export` and keep the JSON file in version control

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Snapshots capture the full Raft state including KV, catalog, ACLs, and sessions, taken consistently from the leader. Copying the data directory of a running server risks an inconsistent capture mid-write.
</details>

---

### Question 10
**Scenario:** Two datacenters must share service discovery.

A. DNS forwarding only
B. VPN only
C. WAN federation joining the server clusters, or cluster peering between them
D. A single stretched LAN gossip pool

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** WAN federation joins server clusters into a shared WAN gossip pool with a primary datacenter for ACLs and CA. Cluster peering is the newer alternative that connects datacenters without a shared primary, which suits independent teams and different administrative domains.
</details>

---

### Question 11
**Scenario:** Which gateway lets mesh services reach services in another datacenter or outside the mesh?

A. A NAT gateway
B. Mesh gateway between datacenters, terminating gateway for external services, ingress gateway for inbound
C. An API gateway only, which proxies external requests to the services but does not carry mTLS between datacenters
D. Only the ingress gateway, which handles inbound traffic and also forwards mTLS traffic out to other datacenters and external services

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Each gateway type solves a distinct edge problem: mesh gateways forward mTLS traffic between datacenters without decrypting it, terminating gateways originate or terminate mTLS for services that cannot run a sidecar, and ingress gateways admit traffic into the mesh.
</details>

---

### Question 12
**Scenario:** Gossip traffic must be encrypted.

A. Enable mTLS in the service mesh
B. Enable TLS on the HTTP API only
C. It is encrypted by default
D. Set a `encrypt` key in the agent configuration, shared by all agents in the pool

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Gossip uses a shared symmetric key, distinct from the TLS configuration that protects RPC and HTTP traffic. Securing a Consul cluster means all three: gossip encryption, TLS for RPC and HTTP, and ACLs, and leaving any one out leaves a real gap.
</details>

---

### Question 13
**Scenario:** Consul is installed on Kubernetes.

A. Only by manual manifests
B. It does not run on Kubernetes, because it needs a stable host IP per agent that pods cannot provide
C. As a DaemonSet only
D. With the official Helm chart or the Consul K8s CLI, which wire up sidecar injection

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The Helm chart deploys servers, clients or dataplanes, the connect injector webhook, and optional catalog sync. Consul Dataplane removes the per-node client agent requirement, which simplifies the Kubernetes deployment model considerably.
</details>

---

### Question 14
**Scenario:** A Consul server loses quorum after two of three servers fail.

A. The remaining server cannot elect a leader, so writes fail; restore servers or run outage recovery
B. The cluster continues normally, because the one remaining server is promoted to leader and keeps accepting writes
C. Clients take over as servers automatically after a timeout, promoting the healthiest client agent into the Raft quorum
D. Data is lost immediately, because a server that loses quorum wipes its Raft log, state store and snapshots

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Without a majority, Raft cannot commit, so the cluster is read-degraded and write-unavailable. Recovery is either restoring the failed servers or using peers.json outage recovery to force a new configuration, which is a documented last-resort procedure.
</details>

---

### Question 15
**Scenario:** Traffic must be split 80/20 between two versions of a service in the mesh.

A. A service splitter config entry, with resolver subsets defining the versions
B. DNS round robin with a weighted record set pointing at the instances of both versions
C. An external load balancer in front of the mesh, with weighted target groups for each version
D. Two separate service names, with callers updated to choose between them by percentage

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Consul's L7 traffic management uses three configuration entries in sequence: the router matches requests, the splitter assigns weights, and the resolver defines subsets by instance metadata. Splitting by service name would require every caller to change.
</details>

---

### Question 16
**Scenario:** A datacenter runs 3 Consul servers and 200 client agents. An engineer asks which agents take part in Raft consensus and leader election. What is the answer?

A. Every agent in the datacenter, so all 203 agents vote in each leader election
B. Only client agents, because servers are reserved for answering queries
C. Only the server agents; clients forward requests to the servers
D. Only the current leader, which replicates its log to no other agent

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Raft runs among the server agents only; they elect a leader and replicate the log. Client agents join the gossip pool, run health checks, and forward RPCs to servers, but they hold no Raft state. Making every agent a voter would make quorum unworkable at scale. The leader replicates to the other servers, and a quorum of them must acknowledge writes.

**Key Concept:** Servers do consensus; clients do membership and local work. See [Consensus protocol](https://developer.hashicorp.com/consul/docs/concept/consensus).
</details>

---

### Question 17
**Scenario:** Consul runs in two federated datacenters. Which statement about gossip pools is correct?

A. All agents in both datacenters share one gossip pool, which spans the WAN
B. There is no gossip between datacenters; federation relies only on DNS
C. Clients join the WAN pool to reach other datacenters, and servers join only the LAN pool
D. Each datacenter has a LAN pool of all its agents, and servers also join a WAN pool

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Every agent joins the LAN gossip pool of its own datacenter, and only servers join the WAN gossip pool that links datacenters, so cross-datacenter requests are forwarded server to server. One pool spanning the WAN would flood slow links with gossip. Federation does use gossip on the WAN pool. Clients never join the WAN pool.

**Key Concept:** LAN gossip for membership within a datacenter, WAN gossip for servers across datacenters. See [Gossip protocol](https://developer.hashicorp.com/consul/docs/concept/gossip).
</details>

---

### Question 18
**Scenario:** A high-volume service discovery workload overloads the Consul leader. The application can tolerate results that are a moment out of date. Which change spreads read load across all servers?

A. Use the `stale` consistency mode so any server can answer reads
B. Use the `consistent` consistency mode for every read request
C. Add more client agents, which answer reads from their own copy of the catalog
D. Disable health checks so the leader does less work for each read

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** In `stale` mode any server, leader or follower, can answer a read, which scales reads across the cluster at the cost of possibly slightly old data. `consistent` mode adds a leader round trip to every read, increasing load. Client agents forward catalog reads to servers rather than holding their own copy. Disabling health checks removes the value of discovery.

**Key Concept:** Choose a consistency mode per read: default, consistent, or stale. See [Consistency modes](https://developer.hashicorp.com/consul/api-docs/features/consistency).
</details>

---

### Question 19
**Scenario:** An operator starts three new Consul servers with the same configuration. They want no leader election until all three have joined. Which setting does this?

A. `server = true` with `ui_config` enabled on each of the three servers
B. `retry_join` with the IP address of the first server on each of them
C. `bootstrap_expect = 3` on each of the three servers
D. `bootstrap = true` on every one of the three servers

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `bootstrap_expect` tells each server how many servers to wait for before the cluster bootstraps and elects a leader. `server = true` makes an agent a server but does not control bootstrapping, and the UI is unrelated. `retry_join` helps agents find each other but does not delay the election. `bootstrap = true` on several servers can create multiple leaders and is meant for a single server only.

**Key Concept:** Set `bootstrap_expect` to the planned server count on every server. See [Bootstrap configuration](https://developer.hashicorp.com/consul/docs/reference/agent/configuration-file/bootstrap).
</details>

---

### Question 20
**Scenario:** Consul servers in AWS run in an Auto Scaling group, so their IP addresses change when instances are replaced. How should agents find the servers to join?

A. Hard-code the current server IP addresses in each agent's `retry_join` list
B. Use cloud auto-join in `retry_join`, matching the servers by their instance tags
C. Run `consul join` by hand on each new agent after checking the console for IPs
D. Put the servers behind a public load balancer and join through its address

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cloud auto-join lets `retry_join` take a provider expression such as `provider=aws tag_key=consul tag_value=server`, so agents look up current server addresses through the cloud API. Hard-coded IPs break when instances are replaced. Manual joins do not scale or survive restarts. A load balancer hides individual servers, while gossip needs to reach real agent addresses, and making it public adds exposure.

**Key Concept:** Discover servers dynamically in elastic environments. See [Cloud auto-join](https://developer.hashicorp.com/consul/docs/deploy/server/cloud-auto-join).
</details>

---

### Question 21
**Scenario:** The `db` service has instances tagged `primary` and `replica`. An application must resolve only the primary instances through Consul DNS. Which name should it query?

A. `db.primary.service.dc1.consul`
B. `service.db.primary.consul`
C. `primary.service.db.consul`
D. `primary.db.service.consul`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The standard DNS form is `[tag.]<service>.service[.datacenter].<domain>`, so the tag comes first: `primary.db.service.consul`. The other orders do not match the lookup format and return no records. Consul's DNS interface listens on port 8600 by default, which is why many setups forward the `.consul` domain to it.

**Key Concept:** Filter DNS results by tag by putting the tag before the service name. See [Static DNS lookups](https://developer.hashicorp.com/consul/docs/discover/service/static).
</details>

---

### Question 22
**Scenario:** When every instance of the `payments` service in `dc1` is unhealthy, clients should automatically be given healthy instances from `dc2`, without application changes. Which Consul feature does this?

A. A prepared query with failover to other datacenters, queried through DNS
B. A key in the KV store that the application reads to choose a datacenter
C. A TTL health check that marks `dc2` instances as preferred when needed
D. A gossip encryption key that is shared between the two datacenters

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Prepared queries can define a failover policy that returns healthy instances from other datacenters when none are healthy locally, and they can be resolved through DNS, so clients need no change. A KV key requires the application to read and act on it. TTL checks report health but do not route across datacenters. Sharing a gossip key is unrelated to failover.

**Key Concept:** Prepared queries add failover and filtering to service lookups. See [Failover with prepared queries](https://developer.hashicorp.com/consul/docs/manage-traffic/failover/prepared-query).
</details>

---

### Question 23
**Scenario:** A batch worker has no HTTP endpoint or open port, but it knows when it is healthy. The team wants Consul to mark it critical if it stops reporting. Which check type fits?

A. An HTTP check that polls a status URL every ten seconds
B. A TCP check that connects to the worker's main port
C. A TTL check that the worker updates through the Consul API
D. A gRPC check that calls the standard gRPC health service

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A TTL check expects the application to report its state through the API before the TTL expires; if updates stop, the check goes critical. HTTP, TCP, and gRPC checks all need something listening for Consul to probe, which this worker does not have.

**Key Concept:** Use probe-based checks when Consul can reach the service, and TTL checks when the service must report itself. See [Health checks](https://developer.hashicorp.com/consul/docs/register/health-check/vm).
</details>

---

### Question 24
**Scenario:** Two automation jobs sometimes update the same KV key at the same moment, and one silently overwrites the other's change. How can each job make sure it only writes if the key has not changed since it last read it?

A. Use `consul kv put -recurse` so that all nested keys are written together in a single call
B. Store the value in two keys and compare them before reading either
C. Lower the agent's gossip interval so updates spread across agents faster
D. Use check-and-set: `consul kv put -cas -modify-index=<index>` with the read index

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Check-and-set writes only if the key's current modify index matches the one supplied, so a job that read stale data fails instead of overwriting. `-recurse` is for deleting or reading trees, not concurrency control. Duplicating keys does not prevent races. KV writes go through Raft on the servers, so gossip timing does not help.

**Key Concept:** Use CAS for safe concurrent updates, and sessions for locks. See [consul kv put](https://developer.hashicorp.com/consul/commands/kv/put).
</details>

---

### Question 25
**Scenario:** An application polls a KV key every second to detect changes, creating heavy load on the servers. What is the more efficient approach?

A. Poll every ten seconds instead, and accept the slower reaction to changes
B. Use a blocking query with the last index, which returns when the key changes
C. Read the key from a client agent's local disk instead of from the servers
D. Copy the key into an environment variable when the application starts

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Blocking queries pass the last seen index, and the request waits until the data changes or a timeout passes, so clients react almost immediately with far fewer requests. Tools such as `consul watch` and consul-template use this mechanism. Slower polling trades load for lag. Client agents do not keep a local KV copy on disk. An environment variable never updates.

**Key Concept:** Blocking queries are Consul's long-poll mechanism for change detection. See [Blocking queries](https://developer.hashicorp.com/consul/api-docs/features/blocking).
</details>

---

### Question 26
**Scenario:** An operator restores a Consul snapshot into a rebuilt cluster after a disaster. Which of these is NOT restored by the snapshot?

A. Each agent's configuration files and TLS certificates on disk
B. KV store entries and their modify indexes
C. The service catalog, sessions, and prepared queries
D. ACL policies and tokens created through the API

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A snapshot captures the Raft state held by the servers: KV data, the catalog, sessions, prepared queries, and ACLs. Agent configuration files and certificates live on each host's disk outside Raft, so they must be backed up and restored separately, for example through configuration management.

**Key Concept:** Snapshots cover cluster state, not host files. See [consul snapshot](https://developer.hashicorp.com/consul/commands/snapshot).
</details>

---

### Question 27
**Scenario:** A team writes a service intention that allows `web` to call `api` only on `GET /status`. The intention is accepted but not enforced at the HTTP level. What is the most likely cause?

A. Intentions can only allow or deny whole services, never specific paths
B. The `web` service is missing a TTL health check, so its traffic is not inspected
C. The `api` service's protocol is not set to `http` in its service-defaults
D. Gossip encryption is disabled, so the sidecar proxies ignore any HTTP rules

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Layer 7 intentions, which match on paths, methods, or headers, require the destination's protocol to be HTTP-based, set through a service-defaults or proxy-defaults config entry. With the default `tcp` protocol, proxies can only enforce layer 4 rules. Intentions do support L7 matching. Health check type and gossip encryption do not affect intention enforcement.

**Key Concept:** Set the service protocol before relying on L7 traffic features. See [Service intentions](https://developer.hashicorp.com/consul/docs/secure-mesh/intention).
</details>

---

### Question 28
**Scenario:** A team enables Consul service mesh on virtual machines and is asked which proxy will sit next to each service instance by default. What is it?

A. NGINX, configured by consul-template from the service catalog
B. HAProxy, configured through the Consul DNS interface
C. A sidecar built into every Consul client agent binary
D. Envoy, configured dynamically by Consul over xDS

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Consul service mesh uses Envoy as its sidecar and gateway proxy, and Consul configures it dynamically through the xDS APIs; `consul connect envoy` starts it for a service. NGINX and HAProxy can integrate with Consul for other uses but are not the mesh default. Consul's old built-in proxy was for development only and has been removed.

**Key Concept:** Envoy is Consul's data plane; Consul is the control plane. See [Envoy proxy configuration](https://developer.hashicorp.com/consul/docs/reference/proxy/envoy).
</details>

---

### Question 29
**Scenario:** TLS is enabled for RPC with `verify_incoming` and `verify_outgoing`. A security review warns that a stolen client certificate could be used to pose as a server. Which setting closes this gap?

A. `verify_server_hostname = true`, so certificates must name `server.<datacenter>.<domain>`
B. `encrypt_verify_incoming = true`, so gossip messages are checked for the right key
C. `acl.default_policy = deny`, so that clients without a token cannot read or write any data
D. `ports.https = 8501`, so TLS traffic moves to a dedicated port

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** With `verify_server_hostname`, agents check that a server's certificate is valid for `server.<datacenter>.<domain>`, which client certificates are not, so a client certificate cannot impersonate a server. Gossip key verification protects the gossip layer, not RPC identity. ACLs control what tokens can do, not certificate identity. A port change does not alter validation.

**Key Concept:** Verify server hostnames to stop clients posing as servers. See [mTLS encryption](https://developer.hashicorp.com/consul/docs/secure/encryption/tls/mtls).
</details>

---

### Question 30
**Scenario:** Consul is installed on Kubernetes with the Helm chart. A team wants their pods to get Envoy sidecars and join the mesh. Connect injection is enabled but not set as the default. What should the team add?

A. A Consul KV entry named after each pod, holding the value `mesh=true`
B. The annotation `consul.hashicorp.com/connect-inject: "true"` on the pod template
C. A Kubernetes NetworkPolicy that allows traffic from the Consul servers
D. A sidecar container defined by hand in every deployment, running `consul agent`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Consul injector adds the sidecar to pods annotated with `consul.hashicorp.com/connect-inject: "true"`, or to all pods when injection is set as the default. KV entries do not trigger injection. A NetworkPolicy controls traffic but does not add a proxy. Hand-written sidecars running a Consul agent are not how the injector works and are hard to maintain.

**Key Concept:** On Kubernetes, the Helm chart plus annotations replace manual sidecar setup. See [Consul service mesh on Kubernetes](https://developer.hashicorp.com/consul/docs/connect/k8s).
</details>

---

## Where to go deeper

- [Consul Associate cert page](../../exams/hashicorp/consul-associate/) - notes, practice plan, strategy
- [ICA practice questions](./cncf-ica.md) - Istio, the other major service mesh
- [Vault Associate practice questions](https://security.noblerworks.com/resources/practice-questions/hashicorp-vault-associate/) - the secrets sibling
- [Networking topic index](../../topics/networking.md) - service networking in context
- **[📖 Consul documentation](https://developer.hashicorp.com/consul/docs)** - primary source
