---
last-updated: 2026-08-09
difficulty: intermediate
---

# Microsoft Fabric Analytics Engineer Associate (DP-600) - Practice Questions

15 questions for DP-600 prep, weighted toward preparing and serving data (40-45%), then semantic models (20-25%) and exploring and analyzing data (20-25%).

> **Cert page:** [exams/azure/dp-600/](../../exams/azure/dp-600/)

---

### Question 1
**Scenario:** What storage layer underpins every Fabric workload?

A. Azure Blob Storage with CSV files
B. OneLake, a single logical data lake per tenant storing data in Delta Parquet
C. Azure SQL Database
D. Cosmos DB

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OneLake is provisioned once per tenant and every workload writes Delta Parquet into it, which is what lets a lakehouse table be queried by Spark, the SQL analytics endpoint, and Direct Lake without copying. "One copy of the data" is the central Fabric idea.
</details>

---

### Question 2
**Scenario:** A team needs to query existing data in an ADLS Gen2 account from Fabric without copying it.

A. A pipeline copy activity
B. A OneLake shortcut to the external location
C. Dataflow Gen2
D. Export to CSV

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Shortcuts create a reference to data in ADLS Gen2, Amazon S3, or another Fabric item, so it appears in your lakehouse without duplication or a refresh schedule. Copy activities and dataflows both move data, which adds cost, latency, and a second copy to keep consistent.
</details>

---

### Question 3
**Scenario:** A semantic model must query lakehouse Delta tables directly at import-like speed without scheduled refresh.

A. Import mode
B. DirectQuery
C. Direct Lake mode
D. Live connection

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Direct Lake reads Delta Parquet from OneLake into the engine's memory on demand, giving import-like performance with no refresh and no per-query trip to a source system. When a query cannot be served that way it falls back to DirectQuery, which is why watching for fallback is part of tuning a Direct Lake model.
</details>

---

### Question 4
**Scenario:** Which item type gives you both a Spark-writable table area and a read-only T-SQL query surface?

A. Warehouse
B. Lakehouse
C. KQL database
D. Power BI dataset

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A lakehouse holds files and Delta tables written by Spark, and it exposes a SQL analytics endpoint that is read-only. A warehouse is the opposite arrangement: full T-SQL read and write, including multi-table transactions. Choosing between them usually comes down to whether your team writes Spark or T-SQL.
</details>

---

### Question 5
**Scenario:** A dimensional model should perform well and be easy to write DAX against.

A. A single wide flat table
B. A star schema: one fact table joined to dimension tables with single-direction one-to-many relationships
C. A fully normalized snowflake
D. Many-to-many relationships throughout

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The VertiPaq engine and DAX filter propagation are both built around star schemas, so this is not just tidiness: it changes performance and makes measures behave predictably. Bidirectional and many-to-many relationships introduce ambiguity and are the usual root cause of "the number is wrong depending on which slicer I use."
</details>

---

### Question 6
**Scenario:** A measure must ignore all filters from slicers on the report page.

A. `CALCULATE([Sales], ALL(Table))`
B. `SUM(Table[Sales])`
C. `CALCULATE([Sales], KEEPFILTERS(Table))`
D. `RELATED(Table[Sales])`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `ALL()` removes filters from the specified table or columns inside the `CALCULATE` modification. `KEEPFILTERS` does the opposite, intersecting rather than replacing. A bare `SUM` respects the filter context, and `RELATED` looks up a value across a relationship.
</details>

---

### Question 7
**Scenario:** A capacity is throttled and interactive reports are slow while a large Spark job runs.

A. Buy more Power BI Pro licenses
B. Review capacity metrics, and either scale the SKU, move the workload to another capacity, or reschedule the background job
C. Delete the semantic model
D. Switch to DirectQuery

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Fabric capacity units are shared across all workloads in a workspace's capacity, so a heavy background job can crowd out interactive queries, and smoothing plus bursting only absorbs so much. The Capacity Metrics app shows which items consumed the units, which is the prerequisite for any of the three fixes.
</details>

---

### Question 8
**Scenario:** Sensitive columns in a warehouse must be hidden from a group of analysts.

A. Column-level security granting SELECT only on permitted columns
B. A separate copy of the table
C. Hiding the column in the report
D. Renaming the column

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Column-level security is enforced by the engine, so it holds regardless of how the user connects. Hiding a field in a report is cosmetic and is bypassed by anyone who builds their own report or connects with another tool. Row-level and object-level security cover the other two shapes of this requirement.
</details>

---

### Question 9
**Scenario:** A medallion architecture is being adopted. What belongs in the bronze layer?

A. Aggregated business metrics
B. Raw ingested data, minimally transformed, retaining source fidelity
C. The star schema
D. Report visuals

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Bronze is raw and append-only so you can always reprocess. Silver is cleaned, conformed, and deduplicated. Gold is the business-ready dimensional model that reports consume. The value of keeping bronze intact is that a logic bug in silver is recoverable without re-ingesting from source.
</details>

---

### Question 10
**Scenario:** Analysts need near-real-time streaming telemetry with sub-second query over high-volume logs.

A. Warehouse
B. Eventhouse with a KQL database
C. Lakehouse batch pipeline
D. Dataflow Gen2

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** KQL databases are built for high-ingest, time-series and log data with fast text and time-range queries, which is a different engine profile from a warehouse. Batch pipelines and dataflows introduce latency measured in minutes at best.
</details>

---

### Question 11
**Scenario:** A workspace must promote content from development to production with review.

A. Copy items by hand
B. Git integration for source control plus deployment pipelines with dev, test, and production stages
C. Export and import PBIX files
D. Share the workspace

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Git integration versions the item definitions so changes are reviewable, and deployment pipelines move content between workspace stages with rules that rebind data sources per stage. Manual copying loses history and reliably drifts.
</details>

---

### Question 12
**Scenario:** A DAX measure calculates year-to-date sales.

A. `TOTALYTD([Sales], 'Date'[Date])` with a marked date table
B. `SUM(Sales[Amount])`
C. `COUNTROWS('Date')`
D. `RELATED(Sales[Amount])`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Time intelligence functions require a proper date table marked as a date table, with a contiguous set of dates covering the full range. Without that, functions such as `TOTALYTD` and `SAMEPERIODLASTYEAR` return wrong or blank results, which is the most common time-intelligence bug.
</details>

---

### Question 13
**Scenario:** A large fact table's Direct Lake model keeps falling back to DirectQuery.

A. Nothing can be done
B. Investigate the cause: unsupported features, guardrail limits for the SKU, or views instead of Delta tables, then remove the blocker
C. Switch every model to import
D. Increase the refresh frequency

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Fallback is a signal, not a setting. Common causes are querying a SQL view rather than a Delta table, row counts beyond the SKU guardrail, or unsupported model constructs. You can also set the fallback behavior to error so the problem is visible instead of silently slow.
</details>

---

### Question 14
**Scenario:** Data lineage must be traceable from a report back to its source tables.

A. The lineage view in the workspace, plus item-level impact analysis
B. The activity log
C. Manual documentation
D. The audit log

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Lineage view renders the dependency graph across pipelines, lakehouses, semantic models, and reports, and impact analysis shows what breaks downstream if you change an item. Activity and audit logs record user actions rather than data dependencies.
</details>

---

### Question 15
**Scenario:** A Delta table accumulates thousands of small files and queries slow down.

A. Convert to CSV
B. Run `OPTIMIZE` (with V-Order) and `VACUUM` to compact files and clean old versions
C. Increase capacity
D. Rewrite the queries

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The small file problem is the classic lakehouse performance issue: each file adds read overhead. `OPTIMIZE` compacts them into fewer, larger files, V-Order improves compression for the Fabric engines, and `VACUUM` removes files no longer referenced after the retention window.
</details>

---

## Where to go deeper

- [DP-600 cert page](../../exams/azure/dp-600/) - notes, practice plan, strategy
- [DP-700 practice questions](./azure-fabric-data-engineer-dp-700.md) - the engineering sibling
- [PL-300 practice questions](./azure-power-bi-pl-300.md) - the Power BI depth this assumes
- [Databases topic index](../../topics/databases.md) - lakehouse in context
- **[📖 DP-600 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600)** - official skills outline
