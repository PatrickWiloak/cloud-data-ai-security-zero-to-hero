---
last-updated: 2026-08-09
difficulty: advanced
---

# AWS Certified Data Analytics - Specialty (DAS-C01) - Practice Questions

15 questions for DAS-C01 prep, weighted toward processing (24%) and storage and data management (22%), then collection, analysis and visualization, and security (18% each).

DAS-C01 has been retired and replaced by the Data Engineer Associate (DEA-C01). The analytics content is still directly useful; confirm exam availability before planning to sit it.

> **Cert page:** [exams/aws/specialty/data-analytics-das-c01/](../../exams/aws/specialty/data-analytics-das-c01/)

---

### Question 1
**Scenario:** Clickstream events arrive at 50,000 records per second and must be available to several independent consumers.

A. SQS
B. Kinesis Data Streams, where multiple consumers read the same shards independently
C. A single Lambda
D. Direct writes to S3

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A stream retains records for a configurable window and lets many consumers read independently at their own position, which a queue does not: SQS delivers each message to one consumer and then it is gone. Enhanced fan-out gives each consumer its own throughput.
</details>

---

### Question 2
**Scenario:** A Kinesis stream has a hot shard because one partition key dominates.

A. Increase retention
B. Choose a higher-cardinality partition key so records distribute evenly, and resize shards
C. Add consumers
D. Reduce the record size

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Each shard has a fixed write limit, so a skewed key concentrates writes and throttles regardless of total shard count. This is the same hot-partition reasoning as DynamoDB, and the fix is the same: distribute the key.
</details>

---

### Question 3
**Scenario:** Athena queries over a large S3 dataset are slow and expensive.

A. Convert to columnar Parquet or ORC, compress, and partition by the common filter columns
B. Add more Athena capacity
C. Query the raw JSON with more workers
D. Increase the S3 storage class

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Athena bills by data scanned, so the three levers are all about scanning less: columnar formats read only the needed columns, compression shrinks bytes, and partitioning prunes whole prefixes. Together they routinely cut cost by an order of magnitude.
</details>

---

### Question 4
**Scenario:** A data lake needs table-level and column-level permissions across accounts.

A. S3 bucket policies alone
B. AWS Lake Formation permissions on Glue Data Catalog resources
C. IAM policies on prefixes
D. Public read

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Lake Formation adds fine-grained grants at database, table, column, and row level, enforced across Athena, Redshift Spectrum, EMR, and Glue. Bucket policies operate on prefixes, which cannot express "these three columns" without physically splitting the data.
</details>

---

### Question 5
**Scenario:** Redshift queries scan a huge fact table joined to a small dimension.

A. Set the fact table's distribution style to KEY on the join column and the dimension to ALL
B. Use EVEN distribution for both
C. Remove sort keys
D. Increase node count only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Distribution style decides how much data moves between nodes at join time. Co-locating the fact rows by join key and replicating a small dimension to every node removes the redistribution step entirely, which is usually a larger win than adding nodes.
</details>

---

### Question 6
**Scenario:** A Glue ETL job must process only new files since the last run.

A. Reprocess everything
B. Enable job bookmarks so Glue tracks processed data
C. Delete files after processing
D. Use a timestamp in the filename manually

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Bookmarks persist state between runs so the job resumes from where it left off. They must be enabled and, when reprocessing is needed, explicitly reset, which is the operational detail that trips people up during backfills.
</details>

---

### Question 7
**Scenario:** Streaming data must land in S3 in Parquet, batched by size or time, with no code.

A. Kinesis Data Firehose with record format conversion and buffering hints
B. Kinesis Data Streams alone
C. A Lambda per record
D. Direct PUT from producers

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Firehose is the managed delivery service: it buffers, converts JSON to Parquet using a Glue table schema, compresses, partitions, and retries. Writing per-record from Lambda produces the small-file problem that then wrecks query performance downstream.
</details>

---

### Question 8
**Scenario:** EMR jobs are expensive and run nightly.

A. Use a long-running cluster
B. Use transient clusters that terminate on completion, with spot instances for task nodes and instance fleets for capacity
C. Increase instance sizes
D. Move to a single EC2 instance

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A cluster that only exists during the job stops paying between runs, and task nodes are the safe place for spot because they hold no HDFS data. Keeping core nodes on-demand protects the data while most of the compute runs at spot pricing.
</details>

---

### Question 9
**Scenario:** A QuickSight dashboard must be fast over a large dataset.

A. Direct query against the source for every visual
B. Import into SPICE with a scheduled refresh
C. Reduce the number of visuals
D. Increase the source database size

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SPICE is the in-memory engine that decouples dashboard performance from the source and protects the source from dashboard load. The trade-off is data freshness bounded by the refresh schedule, so direct query remains right when near-real-time is the requirement.
</details>

---

### Question 10
**Scenario:** Small files are accumulating in the data lake and query performance is degrading.

A. Ignore it
B. Compact small files into larger ones on a schedule, and tune the producer's buffering to write fewer, larger objects
C. Add more partitions
D. Switch to CSV

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Every file carries listing and open overhead, so thousands of tiny objects dominate query time. Fixing it at the source (buffer hints, fewer output partitions) prevents recurrence, and periodic compaction cleans up what already exists. More partitions makes the problem worse.
</details>

---

### Question 11
**Scenario:** Redshift must query data in S3 without loading it.

A. Redshift Spectrum against external tables in the Glue Data Catalog
B. COPY into Redshift
C. UNLOAD
D. A federated query to RDS

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Spectrum reads S3 directly using the catalog for schema, so cold historical data stays in cheap storage while joins with local tables still work. The same partitioning and columnar-format advice applies, because Spectrum also bills by data scanned.
</details>

---

### Question 12
**Scenario:** PII must be masked for analysts but visible to a small compliance team.

A. Two copies of the data
B. Lake Formation column-level permissions and data filters, or dynamic masking in the query layer
C. Application filtering
D. Deleting the columns

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Enforcing at the catalog and query layer means it applies to every engine and every tool, which is what makes it a control rather than a convention. Maintaining two copies doubles storage and guarantees they drift.
</details>

---

### Question 13
**Scenario:** A streaming aggregation must compute a five-minute rolling count.

A. A batch job hourly
B. A windowed query in a stream processing service such as Managed Service for Apache Flink
C. A DynamoDB scan
D. Athena on raw data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Windowed aggregation is the native stream primitive, with tumbling, sliding, and session windows, plus watermarks to handle late-arriving events. Batch approaches put a floor under latency equal to the batch interval.
</details>

---

### Question 14
**Scenario:** A Glue crawler keeps creating new tables instead of updating one.

A. That is expected
B. Inconsistent schemas or partition structure under the path; fix the layout or configure the crawler's schema change and grouping behavior
C. Delete the catalog
D. Run it less often

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Crawlers group objects into tables by similarity of schema and path structure, so mixed formats or an inconsistent prefix layout fragment the result. Setting a table-level grouping policy and enforcing a consistent partition layout at write time is the durable fix.
</details>

---

### Question 15
**Scenario:** Analytics data must be retained for 7 years but is rarely queried after 90 days.

A. Keep everything in Redshift
B. Tier it: recent data in the warehouse, older data in S3 with lifecycle transitions to colder classes, queried through Spectrum or Athena when needed
C. Delete after 90 days
D. Store everything in S3 Standard

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Matching storage cost to access frequency is the main lever on a long-retention analytics estate. Keeping the query path available through Spectrum or Athena means archived data is still reachable, which is what makes the tiering acceptable to the business.
</details>

---

## Where to go deeper

- [DAS-C01 cert page](../../exams/aws/specialty/data-analytics-das-c01/) - notes, practice plan, strategy
- [Data Engineer Associate practice questions](./aws-data-engineer-associate.md) - the current-generation exam
- [DP-203 practice questions](./azure-data-engineer-dp-203.md) - the Azure counterpart
- [Queues vs streams](../../learn/concepts/queues-vs-streams.md) - question 1 in plain English
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - official exam guides
