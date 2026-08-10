---
last-updated: 2026-08-09
difficulty: beginner
---

# Azure Data Fundamentals (DP-900) - Practice Questions

15 questions for DP-900 prep, roughly evenly weighted across core data concepts, relational data, non-relational data, and analytics workloads (25-30% each).

DP-900 tests recognition and vocabulary rather than implementation, so these questions match that level.

> **Cert page:** [exams/azure/dp-900/](../../exams/azure/dp-900/)

---

### Question 1
**Scenario:** Which describes structured data?

A. Video files
B. Data organized into rows and columns with a predefined schema
C. Free-text emails
D. Images

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Structured data has a schema defined before the data is written, which is what makes SQL tables queryable in the way they are. Semi-structured data such as JSON carries its own schema in the payload. Video, images, and free text are unstructured.
</details>

---

### Question 2
**Scenario:** Which workload type describes a system handling many small, fast inserts and updates from an application?

A. OLAP
B. OLTP
C. Batch analytics
D. Data warehousing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OLTP is transaction processing: high volumes of short reads and writes, normalized to avoid duplication. OLAP is analytical processing: fewer, larger queries scanning history, usually denormalized into a star schema. The two have opposite design goals, which is why organizations run both.
</details>

---

### Question 3
**Scenario:** What does ACID stand for in a relational database?

A. Available, Consistent, Isolated, Distributed
B. Atomicity, Consistency, Isolation, Durability
C. Access, Control, Identity, Directory
D. Analytics, Caching, Indexing, Data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Atomicity means all or nothing, consistency means valid state to valid state, isolation means concurrent transactions do not interfere, and durability means a committed transaction survives a crash. These four are the guarantees applications rely on when moving money or booking inventory.
</details>

---

### Question 4
**Scenario:** Which Azure service is a fully managed relational PaaS database with automatic patching and backups?

A. Azure SQL Database
B. Azure Blob Storage
C. Azure Cosmos DB
D. Azure Files

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Azure SQL Database is the relational PaaS offering. Cosmos DB is the NoSQL multi-model service. Blob Storage is object storage for unstructured data, and Azure Files provides SMB and NFS file shares.
</details>

---

### Question 5
**Scenario:** A key-value, document, graph, and column-family API from one service.

A. Azure SQL Managed Instance
B. Azure Cosmos DB
C. Azure Synapse Analytics
D. Azure Data Factory

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cosmos DB is multi-model, offering NoSQL (document), MongoDB, Cassandra (column-family), Gremlin (graph), and Table APIs on the same underlying engine with global distribution. The other services in the list are relational, analytical, and orchestration services respectively.
</details>

---

### Question 6
**Scenario:** Unstructured files such as images and backups need cheap, massively scalable storage.

A. Azure Blob Storage
B. Azure SQL Database
C. Azure Table Storage
D. Azure Cache for Redis

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Blob Storage is object storage with hot, cool, cold, and archive access tiers so you can trade retrieval cost against storage cost. Table Storage is a key-value store for structured non-relational data. Redis is an in-memory cache.
</details>

---

### Question 7
**Scenario:** Which service orchestrates data movement and transformation across sources on a schedule?

A. Azure Data Factory
B. Azure Monitor
C. Azure Functions
D. Azure DevOps

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Data Factory (and its Fabric equivalent, Data pipelines) is the ETL and ELT orchestration service with connectors, scheduling, and monitoring built in. Functions can move data but gives you none of the orchestration, retry, and lineage plumbing.
</details>

---

### Question 8
**Scenario:** The difference between ETL and ELT.

A. They are identical
B. ETL transforms before loading into the target; ELT loads raw data first and transforms inside the target system
C. ELT is only for streaming
D. ETL cannot handle relational data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ELT became the common pattern because cloud data warehouses and lakehouses have cheap, elastic compute, so it is often better to land the raw data and transform in place. Keeping the raw copy also means a transformation bug is fixable without re-extracting from source.
</details>

---

### Question 9
**Scenario:** A data warehouse's fact table typically contains what?

A. Descriptive attributes such as product name and category
B. Numeric measures and foreign keys to dimensions, at a defined grain
C. Report definitions
D. User permissions

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Facts hold the measurements (sales amount, quantity) plus keys, while dimensions hold the descriptive attributes you slice by. The grain, meaning what one row represents, is the first thing to define because everything else follows from it.
</details>

---

### Question 10
**Scenario:** Which best describes a data lake?

A. A relational database with a fixed schema
B. Storage for large volumes of raw data in native formats, with schema applied on read
C. A caching layer
D. A reporting tool

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Schema-on-read is the defining property: you store first and interpret later, which suits data whose future use is not yet known. The risk is that without governance a lake becomes a swamp, which is why cataloging and the medallion layering pattern exist.
</details>

---

### Question 11
**Scenario:** Which service provides interactive reports and dashboards for business users?

A. Power BI
B. Azure Data Lake Storage
C. Azure Databricks
D. Azure Data Box

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Power BI is the visualization and self-service BI layer. Databricks is a Spark-based analytics and machine learning platform. Data Lake Storage is where the data sits, and Data Box is a physical appliance for bulk offline transfer.
</details>

---

### Question 12
**Scenario:** Which describes streaming data processing?

A. Processing large sets at scheduled intervals
B. Processing events continuously as they arrive, often with windowed aggregation
C. Only for relational databases
D. Manual data entry

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Stream processing acts on events in near real time, typically over time windows such as tumbling or sliding windows. Batch processes bounded sets on a schedule. Azure Stream Analytics, Event Hubs, and Fabric Real-Time Intelligence are the services in this space.
</details>

---

### Question 13
**Scenario:** A normalized relational design primarily aims to do what?

A. Speed up analytical scans
B. Reduce data redundancy and update anomalies by storing each fact once
C. Store images efficiently
D. Eliminate the need for indexes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Normalization removes duplication so an update happens in one place. The trade-off is more joins, which is why analytical models deliberately denormalize into star schemas where read performance matters more than update anomalies.
</details>

---

### Question 14
**Scenario:** Who is typically responsible for building and maintaining data pipelines?

A. Data analyst
B. Data engineer
C. Database administrator
D. Data scientist

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Data engineers build ingestion and transformation pipelines and the storage that serves them. Analysts model and visualize for business questions, DBAs run and secure database systems, and data scientists build statistical and machine learning models. DP-900 expects you to distinguish these roles.
</details>

---

### Question 15
**Scenario:** Which statement about a relational primary key is correct?

A. It may contain duplicate values
B. It uniquely identifies each row and cannot be null
C. It must be an integer
D. Each table can have many primary keys

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Uniqueness and not-null are the defining constraints. A key can be any type and can span multiple columns as a composite key. A table has at most one primary key, though it can have additional unique constraints, and foreign keys are the references from other tables to it.
</details>

---

## Where to go deeper

- [DP-900 cert page](../../exams/azure/dp-900/) - notes, practice plan, strategy
- [AZ-900 practice questions](./azure-fundamentals-az-900.md) - the cloud fundamentals sibling
- [SQL vs NoSQL](../../learn/concepts/sql-vs-nosql.md) - the choice in plain English
- [Databases topic index](../../topics/databases.md) - everything the repo has on data stores
- **[📖 DP-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)** - official skills outline
