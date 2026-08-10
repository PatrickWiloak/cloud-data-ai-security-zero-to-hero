---
last-updated: 2026-08-09
difficulty: intermediate
---

# Microsoft Fabric Data Engineer Associate (DP-700) - Practice Questions

15 questions for DP-700 prep across ingestion, transformation, real-time intelligence, orchestration, security, and operational monitoring in Microsoft Fabric.

DP-700 is the engineering counterpart to DP-600: more pipelines and Spark, less semantic modeling.

> **Cert page:** [exams/azure/dp-700/](../../exams/azure/dp-700/)

---

### Question 1
**Scenario:** You must ingest 500 GB nightly from an on-premises SQL Server into a lakehouse with the least transformation logic.

A. A Data Factory pipeline Copy activity using an on-premises data gateway
B. Dataflow Gen2 with Power Query transformations
C. A notebook reading over the public internet
D. Manual CSV export

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Copy activity is the high-throughput movement tool and the on-premises data gateway is how Fabric reaches a private network. Dataflow Gen2 is friendlier for shaping but slower and more expensive at this volume. A notebook cannot reach an on-premises server without the gateway either.
</details>

---

### Question 2
**Scenario:** Which choice best fits transforming data with complex custom logic over hundreds of millions of rows?

A. Dataflow Gen2
B. A Spark notebook in the lakehouse
C. A pipeline expression
D. A KQL query

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spark gives you distributed compute and full PySpark, Scala, or Spark SQL for arbitrary logic at scale. Dataflow Gen2 targets low-code shaping and is not the right tool for heavy custom transformation. Pipeline expressions are for control flow, not data processing.
</details>

---

### Question 3
**Scenario:** Streaming events must be captured continuously and be queryable within seconds.

A. Eventstream into an eventhouse KQL database
B. A pipeline on a 15-minute schedule
C. Dataflow Gen2 refresh
D. A notebook run daily

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Eventstream ingests from sources such as Event Hubs, IoT Hub, and custom endpoints and routes to destinations without code, and an eventhouse is built for immediate query over high-velocity data. Everything else in the list is batch and puts a floor under your latency.
</details>

---

### Question 4
**Scenario:** A pipeline must run activity B only when activity A fails.

A. Chain on the Success output
B. Chain on the Failure output of activity A
C. Use a Wait activity
D. Run them in parallel

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Pipeline dependencies come in Success, Failure, Completion, and Skipped, and choosing the right one is how you build error handling. Completion is the "either way" case, which is useful for cleanup steps that must always run.
</details>

---

### Question 5
**Scenario:** A Delta table needs to merge daily changes: update existing rows, insert new ones.

A. Overwrite the whole table
B. `MERGE INTO` on the Delta table keyed on the business key
C. Append everything
D. Delete then insert

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** MERGE is the upsert primitive Delta provides and it is atomic, so readers never see a half-applied batch. Overwriting is wasteful and loses history. Delete-then-insert is not atomic and leaves a window where the data is missing.
</details>

---

### Question 6
**Scenario:** You need to reprocess data from three days ago after discovering a transformation bug.

A. Restore from backup
B. Delta time travel: query or restore the table `VERSION AS OF` or `TIMESTAMP AS OF` the earlier state
C. Re-ingest from source
D. It is not possible

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Delta keeps a transaction log with prior versions, so you can read or restore an earlier state directly, subject to the retention window and whether `VACUUM` has removed the files. This is exactly why the retention setting matters before you need it.
</details>

---

### Question 7
**Scenario:** Notebook runs fail intermittently with out-of-memory errors on a wide join.

A. Increase the Spark pool node size or enable a larger executor configuration, and reduce shuffle by broadcasting the small side
B. Reduce the number of columns in the output
C. Switch to Dataflow Gen2
D. Run at night

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A join between a large and a small table is the standard broadcast case: broadcasting the small side avoids the shuffle that causes the memory pressure. Sizing is the other half. Moving to a lower-scale tool would make it worse, and scheduling does not change memory requirements.
</details>

---

### Question 8
**Scenario:** Several workspaces need the same lakehouse table without copying it.

A. Export to CSV and share
B. A shortcut to the source lakehouse table from the consuming workspaces
C. Duplicate the pipeline in each workspace
D. Grant capacity admin to everyone

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Internal shortcuts point one Fabric item at another so there is one physical copy and one refresh. Duplicating pipelines multiplies cost and guarantees the copies drift. Granting broad admin permissions is not a data-sharing mechanism.
</details>

---

### Question 9
**Scenario:** Access to a warehouse must be limited so a group can query only rows for their region.

A. Row-level security with a predicate on the region column
B. Separate warehouses per region
C. Workspace roles
D. Report-level filters

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** RLS is enforced by the engine on every query path. Workspace roles are coarse and grant or deny whole items. Report filters are cosmetic. Splitting into separate warehouses per region works but multiplies operational overhead for what a predicate solves.
</details>

---

### Question 10
**Scenario:** A pipeline should process only rows changed since the last run.

A. Full reload each time
B. Incremental load using a watermark column, storing the last processed value between runs
C. Randomly sample
D. Rely on Spark caching

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A high-watermark on a monotonic column such as a modified timestamp or an identity value is the standard incremental pattern, with the watermark persisted so the next run picks up from it. Watch for late-arriving data, which is why a small overlap window is common practice.
</details>

---

### Question 11
**Scenario:** You need to know why a scheduled pipeline stopped producing output last Tuesday.

A. Monitoring hub run history with the failed activity's error detail
B. The Fabric roadmap
C. The semantic model refresh log only
D. Guess from the data

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Monitor hub lists runs across pipelines, notebooks, dataflows, and refreshes with status, duration, and error output per activity. Starting there tells you whether the pipeline failed, was skipped, or succeeded while the source was empty, which are three very different investigations.
</details>

---

### Question 12
**Scenario:** A lakehouse table is queried through the SQL analytics endpoint and a newly written column is missing.

A. The endpoint is read-only and metadata sync can lag; refresh the endpoint metadata
B. The column was not written
C. SQL endpoints do not support new columns
D. Recreate the lakehouse

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The SQL analytics endpoint reflects the Delta tables through a metadata sync that is not instantaneous. Knowing that the endpoint is read-only and eventually consistent with Spark writes prevents a lot of wasted debugging.
</details>

---

### Question 13
**Scenario:** Choose between a warehouse and a lakehouse for a team whose skills are entirely T-SQL and who need multi-table transactions.

A. Lakehouse
B. Warehouse
C. KQL database
D. Semantic model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The warehouse supports full T-SQL DDL and DML with multi-table transactions. The lakehouse's SQL endpoint is read-only, so writes must go through Spark. Matching the item to the team's skills and write pattern is the decision DP-700 tests repeatedly.
</details>

---

### Question 14
**Scenario:** Secrets for an external API must be used inside a notebook without appearing in code.

A. Store them in Azure Key Vault and retrieve them at runtime through a workspace connection or `mssparkutils.credentials`
B. Put them in a markdown cell
C. Hard-code them and restrict the workspace
D. Pass them as pipeline parameters in plain text

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Key Vault keeps the secret out of code, out of git, and out of run history, and rotation happens in one place. Anything embedded in a notebook or a parameter value is visible to anyone with read access to the item and often ends up in exported artifacts.
</details>

---

### Question 15
**Scenario:** A capacity is repeatedly throttled by background jobs, causing report timeouts.

A. Delete old items
B. Use the Capacity Metrics app to identify the consuming items, then reschedule, optimize, or move them to a separate capacity
C. Ask users to retry
D. Switch every report to DirectQuery

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Fabric smooths background operations over time but sustained overuse leads to throttling that affects interactive users. The metrics app attributes consumption per item, which is the only way to decide between optimizing a job, moving it, or buying capacity. DirectQuery would add load rather than remove it.
</details>

---

## Where to go deeper

- [DP-700 cert page](../../exams/azure/dp-700/) - notes, practice plan, strategy
- [DP-600 practice questions](./azure-fabric-analytics-dp-600.md) - the analytics sibling
- [DP-203 practice questions](./azure-data-engineer-dp-203.md) - the Synapse-era predecessor skill set
- [Queues vs streams](../../learn/concepts/queues-vs-streams.md) - the streaming concepts underneath
- **[📖 DP-700 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-700)** - official skills outline
