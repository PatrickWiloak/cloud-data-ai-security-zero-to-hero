---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 11 min
---

# 01 - Prepare the data

**Domain 1: Prepare the data (25-30%)**

---

## Storage modes

| Mode | Data lives | Trade-off |
|---|---|---|
| **Import** | Compressed in the model (VertiPaq) | Fastest queries, full DAX, but data is as old as the last refresh |
| **DirectQuery** | In the source, queried at interaction | Current data, but slower, and DAX and modeling features are restricted |
| **Dual** | Both; the engine decides per query | Used for dimensions shared between Import and DirectQuery facts |
| **Direct Lake** | Parquet files in OneLake, read directly | Fabric only; import-like speed with no import step |

Default to Import. Move to DirectQuery only when data currency or volume forbids it. A **composite model** mixes modes per table, which is how you satisfy "most of it fast, some of it live".

**Dual** matters more than its obscurity suggests: without it, a dimension shared with a DirectQuery fact forces a source round trip even for imported queries.

---

## Power Query

The transformation layer. Steps are recorded in order and re-executed on every refresh.

Core transformations: filter rows, remove and reorder columns, change type, split column, group by, pivot and unpivot, merge (join) and append (union), fill down, extract, and add conditional or custom columns.

**Data profiling** in the View ribbon shows column quality (valid, error, empty), distribution, and profile. It is the intended first step before transforming anything, and it is the source of exam questions about identifying data quality issues.

**Error handling**: remove errors, replace errors, or keep errors to investigate. Type conversion is the usual cause.

---

## Query folding

Power Query translates steps into the source's native query language where it can. Steps that fold execute at the source; from the first step that cannot fold, everything after it is processed locally by the mashup engine.

**Why it matters**: on a large source, broken folding means the entire table is pulled to the gateway or service and transformed in memory. It is also a hard requirement for incremental refresh.

**Check it**: right-click a step and look for **View Native Query**. If it is greyed out, folding has stopped at or before that step.

**Typically folds**: filtering rows, removing and renaming columns, group by, joins against the same source, simple type changes.

**Typically breaks folding**: adding an index column, merging with a different source type, most custom M functions, adding a column with complex logic, and anything referencing a local file mid-stream.

**Design rule**: put every foldable operation first, and any folding-breaking step last.

---

## Parameters, functions, and reuse

**Parameters** hold values referenced by queries: a server name, a file path, a date threshold. They make a model portable across environments and are the mechanism behind deployment pipeline rules.

**Custom functions** convert a query into a reusable transformation applied across many inputs, most commonly every file in a folder.

**Dataflows** move preparation into the service so several models share one cleaned source. Gen1 outputs to Dataverse or Azure Data Lake; Gen2 is the Fabric version with more destinations.

---

## Incremental refresh

Refreshes only recent partitions instead of the whole table.

Requirements:
- Two reserved parameters named exactly **RangeStart** and **RangeEnd**, of date/time type
- A filter on a date column using those parameters
- **Query folding** must work, so the source can filter by partition
- Configured per table with an archive period and an incremental period

Optional: detect data changes using a last-modified column, and refresh only complete periods.

---

## The gateway

The on-premises data gateway bridges the service to sources that are not publicly reachable.

| Mode | Use |
|---|---|
| **Standard** | Shared, supports multiple users and scheduled refresh, installed on a server |
| **Personal** | Single user, Import only, on a workstation |

A refresh that works in Desktop and fails in the service is usually a gateway or credentials problem.

---

## Key terms

- **Import mode** - storage mode caching a compressed copy of the data in the model for fastest query performance
- **DirectQuery** - storage mode leaving data in the source and querying it at interaction time, giving currency at the cost of speed
- **Dual mode** - storage mode allowing a table to act as Import or DirectQuery depending on the query, used for shared dimensions
- **Direct Lake** - Fabric storage mode reading Parquet files directly from OneLake without an import step
- **Composite model** - a model combining tables in different storage modes
- **Query folding** - Power Query translating transformation steps into the source system's native query
- **View Native Query** - the Power Query option revealing the generated source query, used to confirm folding
- **Data profiling** - Power Query column quality, distribution, and profile views used to assess data before transforming
- **Parameter** - a stored value referenced by queries, enabling portability and deployment pipeline rules
- **Dataflow** - a reusable, service-hosted Power Query preparation layer shared across models
- **Incremental refresh** - partitioned refresh of only recent data, requiring RangeStart and RangeEnd parameters and query folding
- **On-premises data gateway** - the connector allowing the Power BI service to reach data sources that are not publicly accessible

---

## Related

- [Notes 02: model the data](./02-model-the-data.md)
- [Scenarios](../scenarios.md) - scenarios 1 and 2
