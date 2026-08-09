---
last-updated: 2026-08-09
difficulty: advanced
---

# SnowPro Advanced: Data Engineer - Practice Questions

15 questions weighted toward data movement and data pipelines and transformations (25-30% each), then performance and optimization (20-25%) and data governance and security (15-20%).

> **Cert page:** [exams/snowflake/snowpro-advanced-data-engineer/](../../exams/snowflake/snowpro-advanced-data-engineer/)

---

### Question 1
**Scenario:** Files land in cloud storage every few minutes and must be loaded with low latency.

A. A scheduled `COPY INTO` every hour
B. Snowpipe with auto-ingest, triggered by storage event notifications
C. A manual load
D. An external table

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Snowpipe loads within a minute or so of the notification and uses serverless compute, so no warehouse idles waiting. Snowpipe also tracks loaded files for 14 days to avoid duplicates, which a hand-rolled `COPY` loop has to reimplement.
</details>

---

### Question 2
**Scenario:** A pipeline must process only rows changed since the last run.

A. Compare full snapshots
B. A stream on the source table, which exposes change records and advances its offset when consumed in a DML statement
C. A timestamp filter
D. Time Travel

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Standard streams show net changes including deletes and updates; append-only streams show inserts only and are cheaper. A stream becomes stale if not consumed within the source table's data retention period, which is the failure mode to monitor for.
</details>

---

### Question 3
**Scenario:** A multi-step transformation must run on a schedule with dependencies between steps.

A. External cron calling each step
B. A task DAG, with child tasks defined by `AFTER` on their predecessor, optionally gated by `SYSTEM$STREAM_HAS_DATA`
C. A stored procedure loop
D. A materialized view

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Only the root task carries a schedule; children fire on completion of their parent. Gating on stream contents means the DAG skips a run entirely when there is nothing new, which is where serverless task credits are saved.
</details>

---

### Question 4
**Scenario:** A pipeline should be declarative rather than a chain of streams and tasks.

A. A view
B. A dynamic table, defined by its query with a target lag, refreshed incrementally by Snowflake
C. A materialized view
D. An external table

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** You declare the result you want and the freshness you need instead of orchestrating the steps. Not every query supports incremental refresh; those that do not fall back to full refresh, which changes the cost profile substantially.
</details>

---

### Question 5
**Scenario:** Semi-structured JSON must be loaded and queried efficiently.

A. Parse it in the application first
B. Load into a `VARIANT` column and query with path notation, flattening arrays with `LATERAL FLATTEN`
C. Store it as a string
D. Convert to CSV

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Snowflake extracts and stores frequently accessed paths columnar-style behind the scenes, so `VARIANT` is not merely a text blob. Where a path is queried constantly, materializing it into a typed column still helps, and consistently large documents may need flattening at load.
</details>

---

### Question 6
**Scenario:** A `COPY INTO` fails partway through on malformed rows.

A. Loading always aborts
B. Set `ON_ERROR` to `CONTINUE`, `SKIP_FILE`, or a threshold, and inspect `VALIDATION_MODE` or `COPY_HISTORY` for the rejected rows
C. Fix the source only
D. Use Snowpipe instead

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The default aborts the whole statement, which is correct when partial loads would corrupt downstream results and wrong when a few bad rows in a large file should not block everything. `VALIDATION_MODE` lets you dry-run the load before committing to it.
</details>

---

### Question 7
**Scenario:** Row-level streaming ingestion is required with sub-second latency.

A. Snowpipe file-based auto-ingest
B. Snowpipe Streaming, writing rows directly through the streaming API without staging files
C. `INSERT` statements per row
D. Kafka Connect to files

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** File-based Snowpipe latency is bounded by how often files are written. Snowpipe Streaming skips the file entirely, and the Kafka connector can use it directly, which is the standard event-streaming path into Snowflake.
</details>

---

### Question 8
**Scenario:** A transformation is written in Python and must run inside Snowflake.

A. Export the data
B. Snowpark Python: DataFrame operations pushed down to SQL, plus UDFs, UDTFs, and stored procedures running in the secure sandbox
C. An external function
D. A SQL script only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Snowpark keeps the data in place and runs on warehouse compute. Vectorized UDFs that process batches with pandas are substantially faster than scalar UDFs when the operation allows it.
</details>

---

### Question 9
**Scenario:** A merge pattern must apply inserts, updates, and deletes from a change stream.

A. Delete then insert
B. A `MERGE` statement matching on the key, with `WHEN MATCHED` and `WHEN NOT MATCHED` clauses driven by the stream's metadata columns
C. Truncate and reload
D. An update only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `METADATA$ACTION` and `METADATA$ISUPDATE` on the stream tell you which branch applies. Duplicate keys in the source cause a nondeterministic merge error, so deduplicating to one row per key before the merge is part of the pattern.
</details>

---

### Question 10
**Scenario:** A load job's warehouse is oversized and finishes in seconds.

A. Keep it for speed
B. Right-size to the file count and size, since loading parallelism comes from the number of files, and split very large files or combine tiny ones toward the 100-250 MB compressed range
C. Use the largest warehouse
D. Use a multi-cluster warehouse

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A single large file cannot use more threads, so a bigger warehouse buys nothing. Thousands of tiny files waste per-file overhead instead, which is why file sizing is the first thing to check on a slow load.
</details>

---

### Question 11
**Scenario:** Pipeline failures must be detected and alerted on.

A. Check manually
B. Query `TASK_HISTORY`, `COPY_HISTORY`, and `PIPE_USAGE_HISTORY`, and use alerts with notification integrations for automated notification
C. Rely on downstream complaints
D. Email on completion

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A task that errors leaves its DAG's children unrun, so a silent failure quietly stops the whole pipeline. Alerts evaluate a condition on a schedule and fire an action, which turns the history views into monitoring rather than forensics.
</details>

---

### Question 12
**Scenario:** Data in an external data lake must be queried without loading it.

A. Load it first
B. External tables over the staged files, or Iceberg tables when Snowflake should read and optionally write the open table format
C. A share
D. Not possible

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** External tables need partition metadata refreshed as files arrive and give weaker performance than native tables. Iceberg tables carry their own metadata and support proper schema evolution, which is why they are the current answer for lake data.
</details>

---

### Question 13
**Scenario:** Sensitive columns must be masked in non-production clones.

A. Delete the columns
B. Masking policies attached through tags, which clones inherit, plus role design so the development role sees masked values
C. Separate tables
D. No clone

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Clones inherit policies, so a cloned environment is not automatically an unprotected copy. The remaining work is making sure the development roles are not the same roles the policy unmasks for.
</details>

---

### Question 14
**Scenario:** A transformation pipeline must be developed and tested safely.

A. Test in production
B. Zero-copy clone the database for a development branch, run the pipeline, then discard the clone
C. A subset extract
D. A separate account

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cloning gives production-representative data instantly at no immediate storage cost, which a sampled extract cannot. Clone lifecycle matters: an abandoned clone accumulates storage as its data diverges from the source.
</details>

---

### Question 15
**Scenario:** Query costs on a pipeline must be attributed and reduced.

A. Guess
B. Attribute by warehouse and query tag through `QUERY_HISTORY` and `WAREHOUSE_METERING_HISTORY`, then reduce by pruning better, avoiding unnecessary full scans, and setting appropriate auto-suspend
C. Fewer queries
D. A smaller warehouse only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `QUERY_TAG` set on a session is what makes per-pipeline attribution possible at all, since one warehouse usually serves many jobs. The Query Profile's partitions-scanned versus partitions-total figure is the specific number that tells you whether pruning is working.
</details>

---

## Where to go deeper

- [SnowPro Advanced Data Engineer cert page](../../exams/snowflake/snowpro-advanced-data-engineer/) - notes, practice plan, strategy
- [SnowPro Core practice questions](./snowflake-snowpro-core.md) - the prerequisite
- [SnowPro Advanced Architect practice questions](./snowflake-snowpro-advanced-architect.md) - the design counterpart
- [Queues vs streams](../../learn/concepts/queues-vs-streams.md) - plain-English streaming primer
- **[📖 Snowflake certification](https://www.snowflake.com/certifications/)** - official exam guides
