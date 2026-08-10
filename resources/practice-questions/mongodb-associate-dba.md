---
last-updated: 2026-08-09
difficulty: intermediate
---

# MongoDB Associate DBA - Practice Questions

15 questions weighted toward server administration (25%), replication and sharding (20% each), then security (15%), backup and recovery, and monitoring (10% each).

> **Cert page:** [exams/mongodb/associate-dba/](../../exams/mongodb/associate-dba/)

---

### Question 1
**Scenario:** How many voting members should a replica set have?

A. Any number
B. An odd number, so an election can reach a strict majority without ties
C. Exactly two
D. Exactly five

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Elections need a majority of voting members. An even count gives no advantage and can deadlock, which is why an arbiter exists: it adds a vote without carrying data. Prefer a data-bearing member where you can, because an arbiter cannot become primary.
</details>

---

### Question 2
**Scenario:** The primary becomes unreachable.

A. The cluster stops accepting writes permanently
B. The remaining members hold an election and a secondary with the most recent oplog becomes the new primary
C. An administrator must promote manually
D. All data is lost

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Automatic failover typically completes in seconds, and drivers with retryable writes replay the in-flight write against the new primary. Writes acknowledged only by the old primary and not replicated can be rolled back, which is exactly what majority write concern prevents.
</details>

---

### Question 3
**Scenario:** A shard key must be chosen for a large collection.

A. A monotonically increasing field such as a timestamp
B. A field with high cardinality, low frequency, and non-monotonic change, or a compound or hashed key that achieves the same
C. A low-cardinality field such as country
D. `_id` always

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A monotonic key sends every insert to the same chunk, creating a hot shard. Low cardinality caps the number of chunks. Hashed sharding distributes evenly but gives up range query targeting, which is the trade-off to state explicitly.
</details>

---

### Question 4
**Scenario:** What does the config server replica set store in a sharded cluster?

A. Application data
B. Cluster metadata: the chunk ranges, shard list, and authentication data used to route queries
C. Backups
D. Index data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `mongos` reads this metadata to route each operation to the right shard. Config servers run as a replica set, and losing them makes the cluster unroutable even though the shards still hold every byte of data.
</details>

---

### Question 5
**Scenario:** Which backup method gives point-in-time recovery?

A. `mongodump` alone
B. Continuous oplog-based backup, as in Atlas continuous backups or Ops Manager
C. A filesystem copy of a running server
D. Replica set members alone

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Point-in-time recovery needs a snapshot plus the oplog to replay forward to a chosen moment. `mongodump` gives you the moment it ran. Replication is high availability, not backup: a dropped collection replicates instantly to every secondary.
</details>

---

### Question 6
**Scenario:** Authentication must be enabled on a replica set.

A. Application-level checks only
B. Enable authorization plus internal cluster authentication, using a keyfile or x.509 certificates between members
C. Firewall rules only
D. No authentication is needed on a private network

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Two separate things need turning on: client authentication and member-to-member authentication. Enabling one without the other either leaves clients unauthenticated or breaks replication. A private network is not a substitute, as the historical wave of exposed unauthenticated MongoDB instances demonstrated.
</details>

---

### Question 7
**Scenario:** Which role grants read and write on one database only?

A. `root`
B. `readWrite` scoped to that database
C. `dbAdmin`
D. `clusterAdmin`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Roles are granted per database, so the same user can hold `readWrite` on one and `read` on another. `dbAdmin` covers schema and index administration without data access, and `clusterAdmin` is cluster-wide operations.
</details>

---

### Question 8
**Scenario:** The oplog is too small for a secondary's downtime window.

A. Nothing can be done
B. Increase the oplog size, because a secondary whose lag exceeds the oplog window must perform a full initial sync
C. Restart the secondary
D. Add a shard

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The oplog is a capped collection, and once entries a secondary still needs have been overwritten, incremental catch-up is impossible. Size it against your longest expected maintenance window plus peak write rate, and it can be resized on a running server in current versions.
</details>

---

### Question 9
**Scenario:** Slow operations must be identified on a running server.

A. Guessing
B. The database profiler, plus the slow query log threshold and `currentOp` for what is executing now
C. Restarting the server
D. Adding memory

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The profiler writes to `system.profile` at level 1 for slow operations or level 2 for everything, and level 2 in production is itself a performance problem. `currentOp` shows live operations, and `killOp` stops one that is causing harm right now.
</details>

---

### Question 10
**Scenario:** Which storage engine is the default and what concurrency does it provide?

A. MMAPv1 with collection-level locking
B. WiredTiger with document-level concurrency, compression, and checkpointing
C. In-memory only
D. No storage engine

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** WiredTiger has been the default for many years and MMAPv1 is removed. Document-level concurrency is why write throughput scales; the WiredTiger cache defaults to roughly half of RAM minus 1 GB, which is the tuning knob that matters most.
</details>

---

### Question 11
**Scenario:** Reads must be served from secondaries to offload the primary.

A. Not possible
B. Set a read preference such as `secondaryPreferred`, accepting eventual consistency
C. Add more primaries
D. Shard the collection

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Secondaries replicate asynchronously, so a secondary read can return stale data. Offloading reads also does nothing for a write-bound workload, and replication traffic means secondaries are not idle. Sharding is the answer when writes are the constraint.
</details>

---

### Question 12
**Scenario:** Chunks are unevenly distributed across shards.

A. Manual migration only
B. The balancer migrates chunks automatically to even out distribution, and it can be scheduled to a maintenance window
C. Restart the cluster
D. Nothing can be done

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Balancing consumes I/O and network, so restricting it to a window is a common production practice. Persistent imbalance despite a running balancer usually means the shard key is the problem, not the balancer.
</details>

---

### Question 13
**Scenario:** Data at rest must be encrypted.

A. Application-level encryption only
B. Encryption at rest via the storage engine's encryption (Enterprise or Atlas), with TLS for data in transit and optional client-side field level encryption for the most sensitive fields
C. Filesystem permissions
D. Not supported

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The three layers are distinct: at rest, in transit, and in use. Client-side field level encryption is the one where the server never sees plaintext, which is what a requirement to protect data from the database operator actually needs. Queryable Encryption extends it to equality and range queries.
</details>

---

### Question 14
**Scenario:** A major version upgrade must be performed on a replica set with minimal downtime.

A. Stop everything and upgrade
B. Rolling upgrade: upgrade secondaries one at a time, step down the primary, upgrade it, then set the feature compatibility version
C. Restore from backup
D. Upgrade the primary first

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The rolling order keeps a primary available throughout. Holding the feature compatibility version back until every member is upgraded is what preserves the ability to downgrade if something goes wrong.
</details>

---

### Question 15
**Scenario:** Which metric most directly indicates a working set exceeding RAM?

A. CPU utilization
B. A rising cache eviction rate and disk read I/O, with the WiredTiger cache consistently full
C. Network throughput
D. Connection count

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** When the working set fits in cache, reads are served from memory. Eviction pressure plus climbing disk reads is the signature of a working set that no longer fits, and the fixes are more RAM, better indexes so less data is touched, or sharding to spread the working set.
</details>

---

## Where to go deeper

- [MongoDB Associate DBA cert page](../../exams/mongodb/associate-dba/) - notes, practice plan, strategy
- [MongoDB Associate Developer practice questions](./mongodb-associate-developer.md) - the application-side counterpart
- [MongoDB Atlas Administrator practice questions](./mongodb-associate-atlas-administrator.md) - the same work on the managed service
- [SQL vs NoSQL](../../learn/concepts/sql-vs-nosql.md) - plain-English primer
- **[📖 MongoDB University](https://learn.mongodb.com/)** - official courses and exam pages
