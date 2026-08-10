---
last-updated: 2026-08-09
difficulty: advanced
---

# Google Cloud Professional Cloud Database Engineer - Practice Questions

15 questions for the Professional Cloud Database Engineer exam, covering database selection, migration, scalability and availability, and operations.

> **Cert page:** [exams/gcp/cloud-database-engineer/](../../exams/gcp/cloud-database-engineer/)

---

### Question 1
**Scenario:** A workload needs horizontal scale, strong consistency, and relational semantics across regions.

A. Cloud SQL
B. Cloud Spanner
C. Firestore
D. Bigtable

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spanner is the distinctive Google offering: horizontally scalable, relational, with external consistency across regions using TrueTime. Cloud SQL is a managed single-primary relational service that scales up rather than out. Firestore and Bigtable are non-relational.
</details>

---

### Question 2
**Scenario:** A time-series workload writes millions of events per second with key-range scans.

A. Bigtable
B. Cloud SQL
C. Firestore
D. Memorystore

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Bigtable is a wide-column store designed for very high write throughput with row-key range scans, which is exactly the time-series access pattern. Row key design decides everything: put the time component after a distributing prefix to avoid hotspotting on the newest range.
</details>

---

### Question 3
**Scenario:** A Bigtable table is hotspotting on writes.

A. Add more nodes
B. Redesign the row key so writes distribute, for example by salting or field promotion, avoiding a purely sequential prefix
C. Increase the timeout
D. Use a smaller cell size

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Bigtable splits data into contiguous row ranges served by tablets, so a monotonically increasing key sends all writes to one tablet. Adding nodes does not help because the bottleneck is one range, not total capacity. Key Visualizer shows the hotspot directly.
</details>

---

### Question 4
**Scenario:** A Cloud SQL instance must survive a zone failure automatically.

A. Read replicas
B. High availability configuration with a synchronous standby in another zone and automatic failover
C. Backups
D. A larger machine type

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** HA uses regional persistent disk with a standby in a second zone, and failover keeps the same connection name. Read replicas are asynchronous and exist for read scaling; promoting one loses whatever had not replicated and is a manual disaster action rather than automatic HA.
</details>

---

### Question 5
**Scenario:** A Spanner schema uses a monotonically increasing primary key and writes are slow.

A. Add nodes
B. Avoid sequential keys: use a UUID, a hashed prefix, or bit-reversed sequence so writes spread across splits
C. Increase the timeout
D. Use a secondary index

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spanner also splits by key range, so the same hotspot logic as Bigtable applies. This is the single most important Spanner schema rule, and it is why the documentation warns against timestamp-first or auto-increment primary keys.
</details>

---

### Question 6
**Scenario:** Related child rows should be stored physically near their parent in Spanner.

A. A foreign key
B. Table interleaving, declaring the child table interleaved in the parent
C. A secondary index
D. A view

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Interleaving co-locates child rows with their parent row so a join reads one split rather than several, which is the main Spanner performance design tool. The trade-off is that the relationship becomes part of the physical layout and cannot be changed without a rewrite.
</details>

---

### Question 7
**Scenario:** An on-premises PostgreSQL database must migrate to Cloud SQL with minimal downtime.

A. Dump and restore during a maintenance window
B. Database Migration Service with continuous replication, cutting over after the target catches up
C. Manual replication scripts
D. Export to CSV

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** DMS performs an initial load and then streams ongoing changes, so the source stays live until a short cutover. Dump and restore requires downtime proportional to the database size, which is unacceptable for anything large.
</details>

---

### Question 8
**Scenario:** A heterogeneous migration from Oracle to PostgreSQL is required.

A. It is not possible
B. Use Database Migration Service with conversion tooling, expecting manual work on stored procedures and vendor-specific SQL
C. Copy the datafiles
D. Change the connection string

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Schema and data can be converted largely automatically; PL/SQL, vendor-specific functions, and application SQL are where the real effort sits. Planning for that manual remediation, and testing it, is what separates a realistic migration plan from an optimistic one.
</details>

---

### Question 9
**Scenario:** Read latency must be reduced for a repeated key-value lookup.

A. Add a read replica
B. Memorystore for Redis or Memcached in front of the database, with a defined invalidation strategy
C. Increase the instance size
D. Add an index

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An in-memory cache removes the query entirely for repeated reads. The design decision that must be explicit is invalidation: TTL-based lazy loading is simple but serves stale data for the TTL window, while write-through keeps freshness at the cost of write complexity.
</details>

---

### Question 10
**Scenario:** A mobile application needs real-time sync of documents with offline support.

A. Firestore
B. Cloud SQL
C. Bigtable
D. BigQuery

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Firestore provides document storage with realtime listeners, offline persistence in the client SDKs, and security rules evaluated per request. That client-side feature set is what distinguishes it from the other options, none of which offer offline sync.
</details>

---

### Question 11
**Scenario:** Database credentials must not appear in application configuration.

A. IAM database authentication where supported, or Secret Manager with a workload identity, rather than static passwords
B. Environment variables in the image
C. A config file
D. Hard-coded strings

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** IAM authentication removes the password entirely by issuing short-lived tokens to the service account. Where it is not available, Secret Manager plus workload identity keeps the secret out of the artifact and gives rotation and audit.
</details>

---

### Question 12
**Scenario:** Point-in-time recovery is needed for a Cloud SQL instance.

A. Daily backups only
B. Enable point-in-time recovery, which uses binary or write-ahead logs to restore to a specific moment
C. Snapshots of the disk
D. Export to Cloud Storage

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PITR combines a base backup with transaction logs to reach any moment in the retention window, which is what protects against a bad `DELETE` at 14:32. Exports are logical dumps useful for portability, not for fine-grained recovery.
</details>

---

### Question 13
**Scenario:** A Spanner instance's CPU sits above 65% sustained.

A. Ignore it
B. Add nodes or processing units, since Google recommends staying below the high-priority CPU threshold to leave headroom for failover and latency
C. Reduce the schema size
D. Add secondary indexes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spanner's guidance targets sustained CPU below roughly 65% for regional instances, because the remaining capacity absorbs traffic shifts during zone failure and keeps tail latency stable. Autoscaling can manage this automatically.
</details>

---

### Question 14
**Scenario:** A query on Cloud SQL is slow and the cause is unclear.

A. Increase the machine size
B. Use Query Insights to identify the top queries and wait events, then fix the query or index
C. Restart the instance
D. Add a read replica

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Query Insights attributes load to specific normalized queries with execution plans and wait breakdowns, which usually reveals a missing index or a full scan. Scaling up first pays permanently for a problem an index would fix.
</details>

---

### Question 15
**Scenario:** Analytics must run over operational data without affecting the transactional database.

A. Query the primary directly
B. Replicate to BigQuery (for example with Datastream or federated queries), keeping analytical load off the operational store
C. Increase the instance size
D. Run analytics at night

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Separating operational and analytical workloads is the standard answer because their access patterns conflict: short indexed reads versus large scans. Datastream provides change data capture into BigQuery with low latency, so analysts get near-current data without touching the primary.
</details>

---

## Where to go deeper

- [Professional Cloud Database Engineer cert page](../../exams/gcp/cloud-database-engineer/) - notes, practice plan, strategy
- [GCP Data Engineer practice questions](./gcp-data-engineer.md) - the analytics counterpart
- [DBS-C01 practice questions](./aws-database-dbs-c01.md) - the AWS database specialty
- [SQL vs NoSQL](../../learn/concepts/sql-vs-nosql.md) - the selection decision in plain English
- **[📖 Google Cloud certification](https://cloud.google.com/learn/certification)** - official exam guides
