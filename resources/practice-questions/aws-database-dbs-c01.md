---
last-updated: 2026-08-09
difficulty: advanced
---

# AWS Certified Database - Specialty (DBS-C01) - Practice Questions

15 questions for DBS-C01 prep, weighted toward workload-specific database design (26%), deployment and migration (20%), then operations, monitoring and troubleshooting, and security (18% each).

DBS-C01 has been retired by AWS. The material remains useful for database work on AWS and for the database domains of other exams; confirm availability before planning to sit it.

> **Cert page:** [exams/aws/specialty/database-dbs-c01/](../../exams/aws/specialty/database-dbs-c01/)

---

### Question 1
**Scenario:** A workload needs single-digit millisecond key-value reads at any scale, with no server management.

A. Amazon RDS for PostgreSQL
B. Amazon DynamoDB
C. Amazon Redshift
D. Amazon Neptune

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** DynamoDB is the managed key-value and document store with predictable latency independent of table size, provided access is by partition key. Redshift is an analytical warehouse, Neptune is a graph database, and RDS is relational with different scaling characteristics.
</details>

---

### Question 2
**Scenario:** A DynamoDB table's partition key is `orderStatus` with four possible values.

A. This is fine
B. This is a hot partition problem: pick a high-cardinality key that matches the dominant access pattern, and use a GSI for status queries
C. Add more capacity
D. Use a sort key only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Four values means all traffic concentrates on at most four partitions, so throughput is capped regardless of provisioned capacity. High-cardinality partition keys distribute the load, and a global secondary index serves the low-cardinality query pattern without dictating the base table's layout.
</details>

---

### Question 3
**Scenario:** An Aurora cluster must survive a regional failure with low RPO and a readable secondary region.

A. Automated backups
B. Aurora Global Database, with typical replication lag under a second
C. A read replica in the same region
D. Multi-AZ

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Global Database uses storage-level replication to secondary regions, giving fast cross-region reads and rapid promotion. Multi-AZ protects against an AZ failure within a region, and backups have an RPO measured in minutes at best.
</details>

---

### Question 4
**Scenario:** A migration must move an Oracle database to Aurora PostgreSQL with minimal downtime.

A. Export and import
B. AWS Schema Conversion Tool for the schema and code, then DMS with full load plus change data capture for the data
C. Manual rewriting only
D. Snapshot restore

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SCT converts schema, stored procedures, and application SQL, flagging what needs manual work, and DMS with ongoing replication lets the source stay live until cutover. That CDC phase is what turns a weekend outage into a short switchover.
</details>

---

### Question 5
**Scenario:** A read-heavy RDS workload has repeated identical queries and needs latency reduced.

A. Add read replicas and an in-memory cache such as ElastiCache in front, with a defined invalidation strategy
B. Increase the instance size only
C. Add indexes only
D. Switch to Redshift

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Replicas scale read throughput and a cache removes the repeated work entirely. The part that must be designed rather than assumed is invalidation: lazy loading with TTL is simple, write-through keeps the cache fresh, and choosing wrongly gives you stale data.
</details>

---

### Question 6
**Scenario:** DynamoDB items must expire automatically after 90 days.

A. A scheduled Lambda scanning and deleting
B. Time to Live (TTL) on an attribute holding an epoch timestamp
C. A lifecycle rule
D. Manual deletion

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** TTL deletes expired items in the background without consuming write capacity, and deletions appear in DynamoDB Streams if you need to react. Deletion is not instant at the expiry time, which matters if you were relying on it for access control rather than housekeeping.
</details>

---

### Question 7
**Scenario:** An RDS instance shows high `CPUUtilization` and slow queries.

A. Immediately scale up
B. Use Performance Insights to identify top SQL by wait event and load, then fix the query or index before resizing
C. Restart the instance
D. Add a read replica

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Performance Insights attributes database load to specific SQL and wait types, which usually reveals a missing index or a query pattern rather than genuine capacity exhaustion. Scaling first pays indefinitely for a fixable problem.
</details>

---

### Question 8
**Scenario:** Database credentials must rotate automatically and never appear in application code.

A. AWS Secrets Manager with automatic rotation, or IAM database authentication
B. Environment variables
C. Parameter Store SecureString with manual rotation
D. A configuration file

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Secrets Manager handles scheduled rotation with a Lambda that updates both the secret and the database. IAM database authentication goes further by removing the stored password entirely in favor of short-lived tokens. Parameter Store stores secrets but does not rotate them for you.
</details>

---

### Question 9
**Scenario:** A graph of relationships must be queried with traversals many hops deep.

A. Amazon Neptune with Gremlin or openCypher
B. DynamoDB
C. RDS with recursive CTEs
D. Redshift

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Purpose-built graph databases keep traversal cost proportional to the subgraph touched, while relational joins degrade sharply with depth. Recursive CTEs work for shallow cases and become impractical for deep, highly connected traversals.
</details>

---

### Question 10
**Scenario:** DynamoDB provisioned capacity is throttling during unpredictable spikes.

A. Over-provision permanently
B. Switch to on-demand capacity mode, or keep provisioned with auto scaling and consider adaptive capacity behavior
C. Add a GSI
D. Reduce the item size only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** On-demand absorbs spikes with no capacity planning and costs more per request, which is the right trade for genuinely unpredictable traffic. Auto scaling on provisioned mode reacts on a delay, so it handles trends better than sudden bursts.
</details>

---

### Question 11
**Scenario:** Point-in-time recovery is needed for a DynamoDB table to any second in the last 35 days.

A. On-demand backups
B. Enable point-in-time recovery on the table
C. DynamoDB Streams
D. Global tables

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PITR gives continuous backups restorable to any second within the retention window, which is the protection against an accidental bulk delete. On-demand backups are discrete snapshots, and global tables replicate errors to every region rather than protecting against them.
</details>

---

### Question 12
**Scenario:** Data at rest and in transit must be encrypted with a customer-managed key.

A. Enable encryption at rest with a KMS customer managed key at creation, and require TLS for connections
B. Application-level encryption only
C. Encryption is automatic and sufficient
D. Encrypt backups only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** For RDS, encryption at rest must be enabled when the instance is created; enabling it later requires a snapshot-and-restore into a new encrypted instance. A customer managed key gives you key policy control and the ability to revoke, which is usually why the requirement exists.
</details>

---

### Question 13
**Scenario:** An Aurora writer fails. What happens to connections?

A. Nothing changes
B. A reader is promoted, the cluster writer endpoint follows it, and existing connections must reconnect
C. The cluster is lost
D. Data must be restored

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Aurora promotes a replica within roughly 30 seconds and the endpoint follows, but sessions break, so the application needs retry logic. Using the reader endpoint for reads and the writer endpoint for writes, rather than instance endpoints, is what makes failover transparent to routing.
</details>

---

### Question 14
**Scenario:** A time-series workload writes millions of metrics per second and queries recent windows.

A. Amazon Timestream (or a purpose-built time-series store)
B. RDS MySQL
C. Neptune
D. DocumentDB

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Time-series engines separate recent hot data from historical cold storage automatically and provide time-oriented query functions. Forcing this pattern into a general-purpose relational database produces enormous tables and index maintenance costs that grow without bound.
</details>

---

### Question 15
**Scenario:** A DynamoDB query needs a different partition key from the base table.

A. A local secondary index
B. A global secondary index with the alternate partition key
C. A scan with a filter
D. A new table maintained by the application

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A GSI can use any attributes as its key and has its own capacity. An LSI shares the base table's partition key and only offers an alternate sort key, and it must be created with the table. A filtered scan reads everything and then discards, so it costs the whole table on every query.
</details>

---

## Where to go deeper

- [DBS-C01 cert page](../../exams/aws/specialty/database-dbs-c01/) - notes, practice plan, strategy
- [Solutions Architect Professional practice questions](./aws-solutions-architect-professional.md) - database choice in architecture context
- [SQL vs NoSQL](../../learn/concepts/sql-vs-nosql.md) - the decision in plain English
- [Databases topic index](../../topics/databases.md) - cross-cloud comparisons
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - official exam guides
