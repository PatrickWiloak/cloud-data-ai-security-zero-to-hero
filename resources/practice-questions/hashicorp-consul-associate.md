---
last-updated: 2026-08-09
difficulty: intermediate
---

# HashiCorp Consul Associate (003) - Practice Questions

15 questions for Consul Associate prep, weighted toward architecture (18%), service discovery (17%), service mesh (17%), and single-datacenter deployment (16%).

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

## Where to go deeper

- [Consul Associate cert page](../../exams/hashicorp/consul-associate/) - notes, practice plan, strategy
- [ICA practice questions](./cncf-ica.md) - Istio, the other major service mesh
- [Vault Associate practice questions](https://security.noblerworks.com/resources/practice-questions/hashicorp-vault-associate/) - the secrets sibling
- [Networking topic index](../../topics/networking.md) - service networking in context
- **[📖 Consul documentation](https://developer.hashicorp.com/consul/docs)** - primary source
