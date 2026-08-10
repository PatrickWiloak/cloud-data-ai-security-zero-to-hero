---
last-updated: 2026-08-09
difficulty: advanced
---

# Databricks Certified Data Engineer Professional - Practice Questions

15 questions for the Data Engineer Professional exam, weighted toward designing and implementing pipelines (34%), incremental processing (20%), and governance (18%).

> **Cert page:** [exams/databricks/data-engineer-professional/](../../exams/databricks/data-engineer-professional/)

---

### Question 1
**Scenario:** A streaming job must process only new files arriving in cloud storage, at scale.

A. List the directory each run
B. Auto Loader (`cloudFiles`), which tracks discovered files with a scalable file notification or directory listing mode
C. A cron job with timestamps
D. Reprocess everything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Directory listing degrades badly once a path holds millions of objects. Auto Loader maintains its own state of processed files and can use cloud notification services instead of listing, with schema inference and evolution built in.
</details>

---

### Question 2
**Scenario:** A Delta table must apply updates and inserts from a change feed atomically.

A. Overwrite the table
B. `MERGE INTO` keyed on the business key, using the change type to decide insert, update, or delete
C. Append everything
D. Delete then insert

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** MERGE is atomic, so readers never see a partially applied batch, and it expresses all three operations in one statement. Delete-then-insert leaves a window where rows are missing, which streaming consumers will observe.
</details>

---

### Question 3
**Scenario:** Downstream jobs need to know exactly which rows changed in a Delta table.

A. Compare full snapshots
B. Enable Change Data Feed on the table and read the change data with row-level change types
C. Add a timestamp column
D. Use the transaction log manually

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CDF emits inserts, updates (pre and post images), and deletes with commit versions, which is what makes incremental downstream processing correct rather than approximate. Timestamp columns miss deletes entirely and are unreliable under late-arriving data.
</details>

---

### Question 4
**Scenario:** A structured streaming job must guarantee exactly-once processing across restarts.

A. Nothing is needed
B. A checkpoint location plus an idempotent sink, which Delta provides through transactional writes
C. Reprocess from the beginning
D. Manual offset tracking

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The checkpoint records source offsets and the sink's transaction log makes writes idempotent, so a restart neither loses nor duplicates data. Deleting a checkpoint is effectively a full restart, which is why checkpoints are treated as production state.
</details>

---

### Question 5
**Scenario:** A slowly changing dimension must keep history of attribute changes.

A. Overwrite the row (SCD Type 1)
B. SCD Type 2: close the current row with an end timestamp and insert a new current row
C. Delete old rows
D. Use a view

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Type 2 preserves history so a fact from last year joins to the dimension values that were current then. Type 1 overwrites and loses that, which silently changes historical reports. Delta Live Tables has `APPLY CHANGES` support for both patterns.
</details>

---

### Question 6
**Scenario:** Query performance on a large Delta table filtered by two high-cardinality columns is poor.

A. Add more partitions
B. Use liquid clustering (or Z-ordering with `OPTIMIZE`) on the filter columns to co-locate related data
C. Convert to CSV
D. Increase cluster size only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multi-dimensional clustering improves data skipping by co-locating similar values so file-level statistics prune more effectively. Partitioning on high-cardinality columns creates many small files and makes performance worse, which is a common misstep.
</details>

---

### Question 7
**Scenario:** A table has accumulated thousands of small files.

A. Ignore it
B. `OPTIMIZE` to compact, tune the writer to produce fewer larger files, and enable auto compaction and optimized writes
C. Add more nodes
D. Repartition to 10,000

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Each file adds open and metadata overhead, so small files dominate query time. Fixing the writer prevents recurrence and compaction cleans up existing data. Auto-optimize handles it continuously for streaming writes.
</details>

---

### Question 8
**Scenario:** Access must be governed centrally across workspaces with lineage.

A. Table ACLs per workspace
B. Unity Catalog, providing a three-level namespace, centralized grants, lineage, and audit across workspaces
C. Cloud storage permissions only
D. Notebook permissions

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Unity Catalog moves governance above the workspace so one grant applies everywhere, and it captures column-level lineage automatically. Storage-level permissions cannot express table, column, or row scope, and per-workspace ACLs fragment as the estate grows.
</details>

---

### Question 9
**Scenario:** A streaming job's state store grows without bound on a windowed aggregation.

A. Increase memory
B. Set a watermark so state for closed windows can be dropped, and bound how late events are accepted
C. Disable checkpointing
D. Restart daily

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Without a watermark, Spark must retain state indefinitely because any old window might still receive an event. The watermark declares a lateness bound, which is what lets old state be evicted, and it also defines which late records are dropped.
</details>

---

### Question 10
**Scenario:** A pipeline must enforce data quality and stop bad records reaching downstream tables.

A. Trust the source
B. Delta Live Tables expectations, choosing per rule whether to warn, drop the record, or fail the update
C. Check afterwards
D. A comment

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Expectations make quality declarative and observable in the pipeline event log, and the three actions map to different severities. Deciding upfront which rules are fatal is the part that turns quality from a dashboard into a gate.
</details>

---

### Question 11
**Scenario:** Old versions of a Delta table must be removed to reduce storage cost.

A. Delete files from storage directly
B. `VACUUM` with a retention period, understanding it breaks time travel beyond that window
C. Drop the table
D. Nothing can be removed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** VACUUM removes files no longer referenced by any retained version, and the default 7-day retention protects concurrent readers and streams. Deleting files manually corrupts the table because the transaction log still references them.
</details>

---

### Question 12
**Scenario:** A job is failing intermittently with skew: one task takes ten times longer than the rest.

A. Add nodes
B. Address skew: enable adaptive query execution's skew join handling, salt the skewed key, or broadcast the small side
C. Reduce partitions to one
D. Increase the timeout

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Skew means one partition holds far more rows than the others, so total capacity is irrelevant while one task is the critical path. AQE splits skewed partitions automatically in many cases; salting is the manual technique when it does not.
</details>

---

### Question 13
**Scenario:** A production job must be orchestrated with dependencies, retries, and alerting.

A. A scheduled notebook
B. Databricks Jobs with multiple tasks, dependencies, retry policies, and notifications, defined as code
C. An external cron calling a notebook
D. Manual runs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multi-task jobs express the DAG, retries, and failure notification in one place, and defining them through Asset Bundles or the API makes them reviewable and promotable across environments. A single scheduled notebook has no dependency model.
</details>

---

### Question 14
**Scenario:** Development, staging, and production must use the same code against different data.

A. Copy notebooks between workspaces
B. Databricks Asset Bundles or CI/CD with parameterized catalogs and environment-specific configuration
C. Hard-code paths
D. One shared environment

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Parameterizing the catalog and schema means the same artifact is promoted rather than reimplemented, which is what makes staging results meaningful. Copied notebooks drift, and the drift usually surfaces as a production-only bug.
</details>

---

### Question 15
**Scenario:** A pipeline's cost is higher than expected on an all-purpose cluster.

A. Keep it running
B. Use job clusters that terminate on completion, right-size the instance types, enable autoscaling, and consider spot for non-critical work
C. Increase the cluster size
D. Run more frequently

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** All-purpose clusters bill at a higher rate and often stay up between runs; job clusters exist for the run and stop. Photon and serverless SQL warehouses are the other levers, trading a higher unit rate for enough speedup to reduce total cost.
</details>

---

## Where to go deeper

- [Data Engineer Professional cert page](../../exams/databricks/data-engineer-professional/) - notes, practice plan, strategy
- [Data Engineer Associate practice questions](./databricks-data-engineer-associate.md) - the prerequisite level
- [DP-700 practice questions](./azure-fabric-data-engineer-dp-700.md) - the Fabric counterpart
- [Databases topic index](../../topics/databases.md) - lakehouse in context
- **[📖 Databricks certification](https://www.databricks.com/learn/certification)** - official exam guides
