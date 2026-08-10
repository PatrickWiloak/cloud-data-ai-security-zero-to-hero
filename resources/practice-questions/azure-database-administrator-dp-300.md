---
last-updated: 2026-08-09
difficulty: intermediate
---

# Azure Database Administrator Associate (DP-300) - Practice Questions

15 questions for DP-300 prep, weighted toward high availability and disaster recovery (20-25%), with secure environment, automation, monitoring and optimization, and deployment.

> **Cert page:** [exams/azure/dp-300/](../../exams/azure/dp-300/)

---

### Question 1
**Scenario:** An application uses SQL Server Agent jobs, cross-database queries, and CLR. It must move to a PaaS offering with minimal code change.

A. Azure SQL Database single database
B. Azure SQL Managed Instance
C. SQL Server on an Azure VM
D. Azure Database for PostgreSQL

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Managed Instance is the PaaS option with near-complete SQL Server surface area, including SQL Agent, cross-database queries, CLR, Service Broker, and linked servers. Single database lacks Agent and cross-database queries. A VM would work but is IaaS, so you keep patching and backup duties.
</details>

---

### Question 2
**Scenario:** A single database must survive a regional outage with an RPO measured in seconds and a readable secondary.

A. Geo-redundant backups only
B. Active geo-replication or a failover group to a secondary region
C. Zone-redundant configuration
D. Long-term retention

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Geo-replication maintains an asynchronous readable secondary in another region with an RPO of about 5 seconds. A failover group adds a listener endpoint so the connection string does not change on failover. Zone redundancy protects against a datacenter, not a region. Backups are recovery, not replication, and have a far larger RPO.
</details>

---

### Question 3
**Scenario:** A query that ran in 200 ms now takes 30 seconds after a statistics update, and the plan changed.

A. Rebuild all indexes
B. Use Query Store to find the regression and force the previously good plan
C. Restart the server
D. Increase the service tier

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Query Store keeps plan history and runtime stats per query, which is what makes a regression identifiable rather than a guess. Forcing the last known good plan stabilizes it immediately while you investigate. Automatic tuning can do this for you when `FORCE_LAST_GOOD_PLAN` is enabled.
</details>

---

### Question 4
**Scenario:** Column-level protection is required so that support staff see only the last four digits of a card number, without changing queries.

A. Transparent Data Encryption
B. Dynamic Data Masking
C. Always Encrypted
D. Row-Level Security

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Dynamic Data Masking rewrites results at query time for unprivileged users while the data stays intact. Be clear about its limit: it is a presentation control, not a cryptographic one, and a user who can run arbitrary queries can often infer the value. Always Encrypted protects against the DBA and the platform but requires client-side key handling.
</details>

---

### Question 5
**Scenario:** Data must be unreadable to Microsoft operators and to the DBA, including in memory on the server.

A. TDE
B. Always Encrypted with secure enclaves
C. Dynamic Data Masking
D. Auditing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Always Encrypted keeps the keys client-side so the engine never sees plaintext, and secure enclaves extend that to allow richer operations such as range comparisons and in-place encryption. TDE encrypts data at rest only, so anyone querying the database sees plaintext.
</details>

---

### Question 6
**Scenario:** Users should only see rows belonging to their own department, enforced in the database.

A. Views for each department
B. Row-Level Security with a security predicate function
C. Application filtering
D. Column encryption

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RLS attaches a predicate to the table so every query is filtered regardless of how it arrives, which closes the gap that per-department views and application-side filtering leave open when someone connects with another tool. Filter predicates control reads and block predicates control writes.
</details>

---

### Question 7
**Scenario:** A database must authenticate application access without storing a password.

A. SQL authentication with a strong password
B. Microsoft Entra ID authentication using a managed identity for the app
C. A shared service account
D. Certificate in the connection string

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A managed identity means no credential exists to leak or rotate: Azure issues tokens to the resource itself, and you create a contained database user for that identity. Shared SQL logins spread across configuration files and lose per-application accountability.
</details>

---

### Question 8
**Scenario:** A workload has unpredictable, bursty usage with long idle periods, and cost must follow usage.

A. Provisioned General Purpose
B. Serverless compute tier with auto-pause
C. Business Critical
D. Hyperscale

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Serverless bills per vCore-second within a range and can auto-pause when idle, which matches intermittent workloads. The trade-off is a cold-start delay on the first connection after a pause. Business Critical targets low latency and high IOPS, and Hyperscale targets very large databases with fast restore.
</details>

---

### Question 9
**Scenario:** A 40 TB database needs near-instant restores and rapid scale-out of read replicas.

A. Hyperscale
B. General Purpose
C. Business Critical
D. Managed Instance General Purpose

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Hyperscale separates compute, log, and page servers, so backups are snapshot-based and restore time is largely independent of database size, and read replicas can be added quickly. General Purpose and Business Critical have much lower size ceilings and size-dependent restore times.
</details>

---

### Question 10
**Scenario:** You must prove who read a sensitive table over the last 90 days.

A. Query Store
B. SQL auditing writing to a Log Analytics workspace or storage account
C. Dynamic Data Masking
D. Extended events on the client

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Auditing records database events with the principal that performed them, and shipping it to Log Analytics gives retention and query. Query Store is a performance feature and does not retain identity. Pair auditing with Microsoft Defender for SQL if you also want anomaly alerting.
</details>

---

### Question 11
**Scenario:** A maintenance job must run nightly against an Azure SQL Database single database, which has no SQL Agent.

A. Elastic Jobs (or Azure Automation / Logic Apps) scheduled against the database
B. SQL Server Agent
C. A cron job on the server
D. It cannot be automated

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Single databases have no Agent, so scheduling comes from outside: Elastic Jobs is the native option and can target groups of databases, while Automation runbooks or Logic Apps are common alternatives. Managed Instance is the deployment option that does include SQL Agent.
</details>

---

### Question 12
**Scenario:** Waits show high `PAGEIOLATCH_SH` and the storage is at its IOPS ceiling.

A. Add indexes to reduce reads, and scale the tier or move to a tier with higher IOPS
B. Rebuild statistics
C. Increase MAXDOP
D. Enable Query Store

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** That wait type means sessions are waiting on data pages to come from storage, so the fix is reading less (better indexes, fewer scans) or having faster storage. Raising MAXDOP adds parallelism to a problem that is I/O bound and can make contention worse.
</details>

---

### Question 13
**Scenario:** A deleted table must be recovered from four days ago on a database with default settings.

A. Point-in-time restore to a new database, then copy the table back
B. Undo the delete
C. Restore the log manually
D. Use geo-replication failover

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Point-in-time restore always creates a new database rather than overwriting the original, so you restore then extract what you need. The default retention is 7 days and can be raised, which is why checking retention before you need it matters. Failover does not travel back in time; the deletion replicated too.
</details>

---

### Question 14
**Scenario:** Connections from the app tier must not traverse the public internet.

A. A firewall rule allowing the app's public IP
B. A private endpoint for the logical server, with public network access disabled
C. A service endpoint plus public access
D. Encrypting the connection string

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A private endpoint gives the server a private IP in your VNet, and disabling public network access closes the internet-facing path completely. Firewall rules still use the public endpoint. Note that with a private endpoint you should use `Proxy` or verify redirect behavior for connection policy.
</details>

---

### Question 15
**Scenario:** Several databases with varying, uncorrelated load should share a cost-efficient resource pool.

A. One large single database
B. An elastic pool
C. Separate provisioned databases at peak size
D. Serverless for each

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Elastic pools let many databases share a pool of DTUs or vCores, which works precisely because their peaks do not coincide. Sizing every database for its own peak wastes most of the capacity most of the time. Serverless per database is an alternative but pays per-database overhead.
</details>

---

## Where to go deeper

- [DP-300 cert page](../../exams/azure/dp-300/) - notes, practice plan, strategy
- [DP-900 practice questions](./azure-data-fundamentals-dp-900.md) - the fundamentals below this
- [SQL vs NoSQL](../../learn/concepts/sql-vs-nosql.md) - choosing a data store
- [Databases topic index](../../topics/databases.md) - cross-cloud comparisons
- **[📖 DP-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300)** - official skills outline
