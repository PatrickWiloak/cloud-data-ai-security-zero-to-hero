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

A. One
B. An odd number, typically 3 or 5, to form a Raft quorum
C. As many as there are clients
D. Two

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Raft needs a majority to commit, so an odd count avoids wasted capacity: 3 servers tolerate 1 failure and 5 tolerate 2. Two servers tolerate zero failures and are worse than one, because losing either loses quorum.
</details>

---

### Question 2
**Scenario:** What protocol does Consul use for membership and failure detection?

A. Raft
B. Gossip, based on SWIM, over the LAN and WAN pools
C. BGP
D. DNS

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Gossip handles membership, failure detection, and event broadcast among all agents. Raft is used separately, and only among servers, for consistency of the state store. Keeping the two straight explains why client agents scale to thousands while servers stay at 3 or 5.
</details>

---

### Question 3
**Scenario:** A service must be discoverable by name from any host in the datacenter.

A. Register it with a Consul agent and query `<service>.service.consul` via DNS or the HTTP API
B. Hard-code IP addresses
C. Use a load balancer only
D. Update `/etc/hosts`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Registration plus the DNS interface is the core discovery loop, and only instances passing their health checks are returned. That last part is what makes discovery useful: a failed instance disappears from results without anyone editing configuration.
</details>

---

### Question 4
**Scenario:** A registered service's health check fails.

A. The service is deregistered permanently
B. The instance stops being returned by service discovery queries while remaining registered
C. Consul restarts the service
D. Nothing changes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Health status gates discovery results, not registration. The instance reappears automatically when the check passes again. Consul does not manage process lifecycle, which is Nomad's or the platform's job.
</details>

---

### Question 5
**Scenario:** Service-to-service traffic must be encrypted and authorized by service identity.

A. Consul service mesh (Connect) with sidecar proxies, mTLS, and intentions
B. Gossip encryption
C. TLS on the API only
D. Firewall rules

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Connect issues each service an identity certificate and the sidecar enforces mTLS, while intentions define which service may call which by name rather than by IP. Gossip encryption protects agent membership traffic, which is a different channel entirely.
</details>

---

### Question 6
**Scenario:** A default-deny posture is wanted for the service mesh.

A. Set the default intention to deny and add explicit allow intentions per source and destination
B. Rely on network segmentation
C. Set default allow
D. Disable Connect

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Intentions evaluate most-specific-first with a configurable default, and switching that default to deny turns the mesh into an allow-list. This is the same reasoning as a default-deny NetworkPolicy, but expressed in service identity rather than IP addresses.
</details>

---

### Question 7
**Scenario:** ACLs are enabled and an agent cannot register services.

A. ACLs do not affect registration
B. The agent needs a token with `service:write` for the service name; check the agent token and the ACL policy
C. Restart Consul
D. Disable ACLs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** With ACLs enabled the default policy is deny, so every operation needs an explicitly granted token. Agent tokens, node identities, and service identities are the mechanisms that scope this, and disabling ACLs to make an error go away removes the security model.
</details>

---

### Question 8
**Scenario:** Configuration values must be shared across services and rendered into config files as they change.

A. The Consul KV store with consul-template watching the keys
B. Environment variables
C. A shared NFS mount
D. The catalog

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** KV holds the values and consul-template subscribes to changes, re-rendering a file and optionally reloading the process. This is how legacy applications that read config from disk participate in dynamic configuration without being rewritten.
</details>

---

### Question 9
**Scenario:** Consul state must be backed up before an upgrade.

A. Copy the data directory while running
B. `consul snapshot save` to capture the Raft state, restorable with `consul snapshot restore`
C. Export the KV store only
D. No backup is needed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Snapshots capture the full Raft state including KV, catalog, ACLs, and sessions, taken consistently from the leader. Copying the data directory of a running server risks an inconsistent capture mid-write.
</details>

---

### Question 10
**Scenario:** Two datacenters must share service discovery.

A. WAN federation joining the server clusters, or cluster peering between them
B. A single stretched LAN gossip pool
C. VPN only
D. DNS forwarding only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** WAN federation joins server clusters into a shared WAN gossip pool with a primary datacenter for ACLs and CA. Cluster peering is the newer alternative that connects datacenters without a shared primary, which suits independent teams and different administrative domains.
</details>

---

### Question 11
**Scenario:** Which gateway lets mesh services reach services in another datacenter or outside the mesh?

A. Mesh gateway for cross-datacenter, terminating gateway for external services, ingress gateway for inbound
B. Only the ingress gateway
C. A NAT gateway
D. An API gateway only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Each gateway type solves a distinct edge problem: mesh gateways forward mTLS traffic between datacenters without decrypting it, terminating gateways originate or terminate mTLS for services that cannot run a sidecar, and ingress gateways admit traffic into the mesh.
</details>

---

### Question 12
**Scenario:** Gossip traffic must be encrypted.

A. Set a `encrypt` key in the agent configuration, shared by all agents in the pool
B. Enable TLS on the HTTP API only
C. Use IPsec
D. It is encrypted by default

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Gossip uses a shared symmetric key, distinct from the TLS configuration that protects RPC and HTTP traffic. Securing a Consul cluster means all three: gossip encryption, TLS for RPC and HTTP, and ACLs, and leaving any one out leaves a real gap.
</details>

---

### Question 13
**Scenario:** Consul is installed on Kubernetes.

A. Only by manual manifests
B. With the official Helm chart or the Consul K8s CLI, which wire up sidecar injection and sync with Kubernetes services
C. It does not run on Kubernetes
D. As a DaemonSet only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Helm chart deploys servers, clients or dataplanes, the connect injector webhook, and optional catalog sync. Consul Dataplane removes the per-node client agent requirement, which simplifies the Kubernetes deployment model considerably.
</details>

---

### Question 14
**Scenario:** A Consul server loses quorum after two of three servers fail.

A. The cluster continues normally
B. The remaining server cannot elect a leader, so writes fail while stale reads may still be served; recover by restoring servers or performing an outage recovery
C. Data is lost immediately
D. Clients take over

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Without a majority, Raft cannot commit, so the cluster is read-degraded and write-unavailable. Recovery is either restoring the failed servers or using peers.json outage recovery to force a new configuration, which is a documented last-resort procedure.
</details>

---

### Question 15
**Scenario:** Traffic must be split 80/20 between two versions of a service in the mesh.

A. A service splitter configuration entry, with service resolver subsets defining the versions
B. DNS round robin
C. Two service names
D. An external load balancer

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Consul's L7 traffic management uses three configuration entries in sequence: the router matches requests, the splitter assigns weights, and the resolver defines subsets by instance metadata. Splitting by service name would require every caller to change.
</details>

---

## Where to go deeper

- [Consul Associate cert page](../../exams/hashicorp/consul-associate/) - notes, practice plan, strategy
- [ICA practice questions](./cncf-ica.md) - Istio, the other major service mesh
- [Vault Associate practice questions](./hashicorp-vault-associate.md) - the secrets sibling
- [Networking topic index](../../topics/networking.md) - service networking in context
- **[📖 Consul documentation](https://developer.hashicorp.com/consul/docs)** - primary source
