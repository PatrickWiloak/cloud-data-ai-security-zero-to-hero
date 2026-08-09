---
last-updated: 2026-08-09
difficulty: intermediate
---

# MongoDB Associate Atlas Administrator - Practice Questions

15 questions weighted toward cluster management (25%), security and access and data management (20% each), then performance (15%), monitoring and backup (10% each).

> **Cert page:** [exams/mongodb/associate-atlas-administrator/](../../exams/mongodb/associate-atlas-administrator/)

---

### Question 1
**Scenario:** An Atlas cluster must survive the loss of a cloud availability zone.

A. A single-region M0 cluster
B. A replica set spread across at least three availability zones in a region, which Atlas does by default for dedicated tiers
C. A standalone instance
D. Manual failover

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Atlas places the three replica set members in separate zones automatically on dedicated tiers, so zone loss triggers an election rather than an outage. Surviving the loss of a whole region requires a multi-region cluster with electable members elsewhere.
</details>

---

### Question 2
**Scenario:** Application traffic must reach Atlas without traversing the public internet.

A. IP access list only
B. VPC peering or a private endpoint (AWS PrivateLink, Azure Private Link, or GCP Private Service Connect)
C. A VPN client on each developer machine
D. Public endpoint with TLS

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The IP access list restricts who may connect over the public endpoint but the traffic still leaves your network. Private endpoints are the stronger option because they work across overlapping CIDR ranges and do not require the routing changes peering does.
</details>

---

### Question 3
**Scenario:** Which Atlas tier supports auto-scaling of compute?

A. M0 free tier
B. Dedicated tiers (M10 and above), which can scale cluster tier up and down within configured bounds
C. All tiers
D. Shared tiers only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Shared tiers have fixed resources. Setting both a minimum and a maximum on dedicated tiers is what makes auto-scaling safe: an unbounded maximum turns a traffic spike into a bill. Storage auto-scaling is a separate setting and scales up only.
</details>

---

### Question 4
**Scenario:** A cold dataset must move to cheaper storage while remaining queryable.

A. Delete it
B. Online Archive, which moves data matching an archiving rule to cloud object storage and keeps it queryable through a federated connection string
C. A separate cluster
D. `mongodump` to S3

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Online Archive keeps the data addressable while removing it from the cluster's storage and working set. Query performance against archived data is much slower, so the archiving rule should reflect access patterns rather than age alone.
</details>

---

### Question 5
**Scenario:** Which Atlas feature recommends indexes based on observed queries?

A. Real-Time Performance Panel
B. Performance Advisor, which analyzes slow queries and suggests indexes and schema improvements
C. The profiler only
D. Atlas Search

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Performance Advisor surfaces suggestions from actual slow query logs, and it also flags unused indexes, which cost write throughput and storage for nothing. The Real-Time Performance Panel shows what is happening right now rather than making recommendations.
</details>

---

### Question 6
**Scenario:** Database users must authenticate without static passwords.

A. SCRAM passwords only
B. Cloud provider IAM authentication, x.509 certificates, or federated identity via LDAP or OIDC
C. API keys
D. No authentication

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** IAM authentication ties database access to a workload's existing cloud role, so there is no password to rotate or leak. Note that database users are a separate concept from Atlas organization and project users, who administer the platform rather than read data.
</details>

---

### Question 7
**Scenario:** A cluster must be restored to a specific moment before an accidental deletion.

A. A snapshot restore only
B. Continuous cloud backup with point-in-time restore, restoring to the moment before the deletion
C. Replica set members
D. Online Archive

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Snapshots give you fixed points; continuous backup replays the oplog to any moment inside the retention window. Replication does not help here at all, because the deletion replicates to every member immediately.
</details>

---

### Question 8
**Scenario:** Encryption keys for Atlas must be controlled by the customer.

A. Not possible
B. Encryption at rest using customer key management with AWS KMS, Azure Key Vault, or GCP KMS
C. Client-side only
D. Filesystem encryption

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Atlas encrypts at rest by default with provider-managed keys; customer key management puts the key lifecycle, including revocation, in your control. Client-side field level encryption is the separate, stronger control where Atlas never sees plaintext for those fields.
</details>

---

### Question 9
**Scenario:** Which Atlas capability runs code in response to database changes?

A. Change streams only
B. Atlas Triggers: database triggers on change events, plus scheduled and authentication triggers
C. Cron on an application server
D. Alerts

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Triggers are the managed layer over change streams, so there is no long-running listener process of your own to keep alive and resume. Scheduled triggers cover the cron use case in the same place.
</details>

---

### Question 10
**Scenario:** An alert must fire when a cluster's disk approaches capacity.

A. Manual checks
B. An Atlas alert on the disk space used metric, routed to email, Slack, PagerDuty, or a webhook
C. A support ticket
D. Nothing exists

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Atlas has default alerts and supports custom conditions on any exposed metric. Disk is the one to configure deliberately, since a full disk stops writes; storage auto-scaling reduces but does not eliminate the need for the alert.
</details>

---

### Question 11
**Scenario:** Users in different countries must read from a nearby region while writes stay authoritative.

A. Separate clusters per region
B. A multi-region cluster with read-only or electable nodes in the additional regions, and a read preference of `nearest`
C. Sharding by country
D. A CDN

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Read-only nodes serve local reads without participating in elections. If write locality is the requirement rather than read locality, global clusters with zone sharding are the mechanism, pinning documents to a region by shard key.
</details>

---

### Question 12
**Scenario:** Atlas infrastructure must be managed as code.

A. Console only
B. The Atlas Administration API, the Terraform MongoDB Atlas provider, the Atlas CLI, or the Kubernetes Operator
C. Shell scripts against the database
D. Not possible

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** All of these sit on the Administration API. Terraform is the common choice where cluster configuration should live beside the rest of the infrastructure, and programmatic API keys with a project-scoped role are how you authenticate them.
</details>

---

### Question 13
**Scenario:** Which Atlas feature enables vector similarity search for a retrieval-augmented generation application?

A. Atlas Search
B. Atlas Vector Search, indexing embedding fields and queried with `$vectorSearch`
C. A text index
D. Data Federation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Vector Search does approximate nearest-neighbor search over embeddings stored alongside the source documents, so there is no separate vector database to keep in sync. Combining it with normal filters in the same query is the practical advantage.
</details>

---

### Question 14
**Scenario:** Data in Atlas and in an S3 bucket must be queried together.

A. Copy S3 data into Atlas
B. Atlas Data Federation, which queries across cluster and object storage with a single MQL endpoint
C. Not possible
D. Export both to a warehouse

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Federation avoids the copy, which is the whole point when the object storage data is large and cold. Expect object storage query performance rather than cluster performance, and partition the S3 layout to match the filters you run.
</details>

---

### Question 15
**Scenario:** A project's costs must be attributed to teams.

A. One project for everything
B. Organize by organization, project, and cluster with tags, since Atlas billing reports break down by project and cluster
C. Separate accounts
D. Manual estimation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The project is the natural allocation boundary because it also scopes network access, users, and alerts, so the security boundary and the cost boundary line up. Retrofitting a project split later means recreating clusters.
</details>

---

## Where to go deeper

- [Atlas Administrator cert page](../../exams/mongodb/associate-atlas-administrator/) - notes, practice plan, strategy
- [MongoDB Associate DBA practice questions](./mongodb-associate-dba.md) - the self-managed counterpart
- [MongoDB Associate Developer practice questions](./mongodb-associate-developer.md) - the application-side view
- [Embeddings and vector search](../../learn/concepts/embeddings-and-vector-search.md) - context for Atlas Vector Search
- **[📖 MongoDB University](https://learn.mongodb.com/)** - official courses and exam pages
