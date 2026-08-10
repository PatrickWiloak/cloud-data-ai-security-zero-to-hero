---
last-updated: 2026-08-09
difficulty: advanced
---

# SnowPro Advanced: Administrator (ADA-C01) - Practice Questions

15 questions weighted toward security and access control (25-30%), account and organization management and resource management (20-25% each), then performance monitoring (15-20%) and data management and compliance (10-15%).

> **Cert page:** [exams/snowflake/snowpro-advanced-administrator/](../../exams/snowflake/snowpro-advanced-administrator/)

---

### Question 1
**Scenario:** A warehouse's credit consumption must be capped for a business unit.

A. Suspend the warehouse manually
B. A resource monitor assigned to the warehouse or account, with notify, suspend, and suspend-immediately triggers
C. A smaller warehouse size
D. A budget alert only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Resource monitors are the only enforcement mechanism: they act on a credit quota per interval and can notify at one threshold then suspend at another. Suspend lets running queries finish; suspend immediately kills them, which is a deliberate choice rather than a default.
</details>

---

### Question 2
**Scenario:** Which role can create other roles and manage account-level objects but should not be used day to day?

A. SYSADMIN
B. ACCOUNTADMIN, which should be limited to a small number of users with MFA enforced
C. PUBLIC
D. USERADMIN

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The recommended hierarchy grants object ownership under SYSADMIN and user and role administration under USERADMIN, with SECURITYADMIN managing grants. Reserving ACCOUNTADMIN for billing and account settings limits the damage any one compromised session can do.
</details>

---

### Question 3
**Scenario:** A query ran successfully yesterday but its results must be recovered without rerunning it.

A. Not possible
B. `RESULT_SCAN` against the query ID, within the 24-hour result cache retention
C. Time Travel
D. Fail-safe

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The result cache holds results for 24 hours, extended on reuse up to 31 days, and serves them with no warehouse running at all. Time Travel restores table state rather than query results, and Fail-safe is a Snowflake-managed recovery of last resort.
</details>

---

### Question 4
**Scenario:** A table was dropped an hour ago and must be recovered.

A. Restore from backup
B. `UNDROP TABLE`, using Time Travel within the retention period
C. Contact support for Fail-safe
D. Recreate it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Time Travel defaults to one day and extends to 90 on Enterprise editions for permanent objects. Fail-safe adds seven days after Time Travel expires but is only accessible through Snowflake support, so it is a disaster mechanism rather than an operational one. Transient and temporary tables have no Fail-safe.
</details>

---

### Question 5
**Scenario:** Users must not be able to see sensitive column values unless they hold a specific role.

A. A separate table
B. A dynamic data masking policy on the column, branching on `CURRENT_ROLE` or `IS_ROLE_IN_SESSION`
C. A view for each role
D. Revoke SELECT

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Masking policies apply at query time wherever the column is referenced, including through views, which is what per-role view proliferation fails to guarantee. Row access policies are the row-level counterpart, and both can be attached to object tags for scaled application.
</details>

---

### Question 6
**Scenario:** A multi-cluster warehouse is configured with min 1 and max 5 clusters in auto-scale mode.

A. All five clusters run continuously
B. Additional clusters start under concurrency pressure and shut down when demand falls, billing only for running clusters
C. It behaves like a larger warehouse
D. Queries fail past cluster one

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multi-cluster addresses concurrency, not single-query performance; a larger warehouse size addresses the latter. Maximized mode runs all clusters continuously, which is a deliberate choice for predictable heavy concurrency.
</details>

---

### Question 7
**Scenario:** Access to Snowflake must be restricted to a corporate network.

A. A firewall
B. A network policy with allowed IP ranges, applied at account or user level, plus network rules for finer control
C. MFA only
D. Private connectivity only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Network policies are evaluated before authentication. Set them carefully, since an account-level policy that excludes your own address locks you out, and only a user with the right privilege from an allowed address can undo it. Private connectivity such as PrivateLink is the complementary control on the network path.
</details>

---

### Question 8
**Scenario:** Data must be shared with an external organization without copying it.

A. Export to S3
B. A secure share via Snowflake Secure Data Sharing, or a listing on the Marketplace, where the consumer pays their own compute
C. A replicated database
D. An external table

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Sharing grants read access to the provider's storage, so there is no copy to keep in sync and no storage cost for the consumer. Consumers on a different cloud or region require a reader account or database replication first.
</details>

---

### Question 9
**Scenario:** A query is slow and the Query Profile shows a high percentage of bytes spilled to remote storage.

A. Add clustering
B. The warehouse is too small for the operation's memory needs; increase the size or reduce the data volume being processed
C. Add a materialized view
D. Increase the query timeout

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spilling to local disk is a warning sign and spilling to remote storage is a serious one, because the operation no longer fits in memory. Look for exploding joins and unnecessary sorts before simply buying a larger warehouse.
</details>

---

### Question 10
**Scenario:** A large table's queries filter on a date column that does not match the natural load order.

A. An index
B. A clustering key on the date column, letting automatic clustering reorganize micro-partitions
C. A larger warehouse
D. A materialized view

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Snowflake prunes micro-partitions by their min and max values, so clustering improves pruning for the chosen filter. Automatic clustering consumes credits continuously, so it earns its cost only on large tables queried often on that key.
</details>

---

### Question 11
**Scenario:** Account activity must be audited for the past year.

A. The query history page only
B. The `SNOWFLAKE.ACCOUNT_USAGE` schema, which retains up to one year with some latency, versus `INFORMATION_SCHEMA` for recent, low-latency data
C. Warehouse logs
D. Not available

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The trade-off is the point: `ACCOUNT_USAGE` has up to 45 minutes of latency but long retention, while `INFORMATION_SCHEMA` is current but limited to between 7 days and 6 months depending on the view. Choosing the wrong one produces either stale answers or missing history.
</details>

---

### Question 12
**Scenario:** A database must be available in a second region for disaster recovery.

A. Manual export and import
B. Database or account replication to a secondary region, with failover configured for business continuity
C. Time Travel
D. A share

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Replication keeps a read-only secondary current; failover promotes it to primary. Account-level replication also carries users, roles, and warehouses, which is what makes the secondary usable rather than just a copy of the data.
</details>

---

### Question 13
**Scenario:** Credit consumption must be attributed to teams.

A. A single warehouse for everyone
B. Warehouses per team or workload plus object tagging, reported through `WAREHOUSE_METERING_HISTORY` and tag-based views
C. Estimation
D. Query counts

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The warehouse is the unit of compute billing, so warehouse boundaries define the attribution you can report on. Tags extend this to storage and to grouping warehouses under a cost center without creating more of them.
</details>

---

### Question 14
**Scenario:** A user's password authentication must be replaced with key-based authentication for a service account.

A. Rotate the password more often
B. Key pair authentication with an RSA public key on the user, supporting a second key for rotation without downtime
C. OAuth only
D. SSO

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Service accounts cannot complete an interactive SSO or MFA flow, so key pairs are the standard. The `RSA_PUBLIC_KEY_2` slot is what makes rotation a zero-downtime operation rather than a coordinated outage.
</details>

---

### Question 15
**Scenario:** Storage costs are rising faster than data volume.

A. Delete data
B. Investigate Time Travel retention, Fail-safe on permanent objects, and cloned and stale objects, since retained versions and clones with diverged data all consume storage
C. Compress the data
D. Move to a smaller warehouse

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Zero-copy clones cost nothing at creation but accumulate storage as the two copies diverge. Long Time Travel retention on a high-churn table multiplies its storage, which is why retention should be set per object rather than globally.
</details>

---

## Where to go deeper

- [ADA-C01 cert page](../../exams/snowflake/snowpro-advanced-administrator/) - notes, practice plan, strategy
- [SnowPro Core practice questions](./snowflake-snowpro-core.md) - the prerequisite
- [SnowPro Advanced Architect practice questions](./snowflake-snowpro-advanced-architect.md) - the design counterpart
- [SQL vs NoSQL](../../learn/concepts/sql-vs-nosql.md) - plain-English data foundation
- **[📖 Snowflake certification](https://www.snowflake.com/certifications/)** - official exam guides
