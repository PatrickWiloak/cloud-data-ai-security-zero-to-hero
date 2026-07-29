---
last-updated: 2026-07-29
---

# PD2 06 - Performance

Writing code and designing automation that performs at scale. This is what most
distinguishes PD2 from PD1: the exam asks not only whether code works, but whether it works
on 200 records, and on two million.

## The governor-limit mindset

Performance on the platform is inseparable from governor limits. Code that is slow usually
also approaches a limit, and code that respects limits is usually fast enough.

- **Design for bulk from the start** - assume every entry point (trigger, batch, API) can receive many records.
- **Minimise queries and DML** - the scarce resources. Query once, process in memory, write once.
- **Watch CPU time** - complex in-memory processing, nested loops, and heavy string work consume the 10,000 ms synchronous budget. CPU-time limit failures are common in poorly structured triggers.
- **Manage heap** - large query results and collections consume the 6 MB heap. Use the SOQL for loop to process in batches.

## Efficient Apex patterns

- **Bulkify** - collections in, collections out. No SOQL or DML in loops.
- **Use maps for correlation** - build a `Map<Id, SObject>` to relate records without nested loops or per-record queries. Turns an O(n²) nested-loop pattern into O(n).
- **Query only what you need** - select only required fields and filter selectively, both to reduce heap and to enable index use.
- **Avoid repeated describe calls** - cache `Schema` describe results rather than recomputing them.
- **Asynchronous for volume** - move large-volume work to Batch Apex, gaining fresh limits per chunk.
- **Short-circuit** - exit early from loops and methods when further work is unnecessary.
- **Static caching within a transaction** - cache expensive results in static variables for reuse during the same transaction.

The map-based correlation pattern is worth internalising: whenever you find yourself looping
over one list inside a loop over another, a map keyed by the join field removes the inner
loop.

## Query performance and large data volumes

- **Selective queries** - filter on indexed fields with selective values so the optimiser uses the index. Non-selective queries on large objects fail with a timeout.
- **Indexes** - standard on Id, Name, owner, foreign keys, audit fields; custom on External ID and unique fields; and support-created for others.
- **The query plan tool** - shows the cost and whether an index is used. The way to diagnose a slow query.
- **Avoid negative and wildcard-leading filters** - `!=`, `NOT`, and `LIKE '%term'` cannot use an index.
- **Data skew** - ownership, lookup, and account skew cause lock contention and slow sharing recalculation. Distribute ownership and children across parents.
- **Skinny tables and indexes** - request from Salesforce support for very large, read-heavy objects.
- **Archiving and big objects** - move cold data out of the transactional store; **Big Objects** hold billions of records for archival and are queried with async SOQL.

## Trigger and automation performance

- **One trigger per object with a handler** - predictable and testable.
- **Recursion control** - a static flag prevents a trigger re-entering and multiplying queries.
- **Consolidate automation** - many overlapping flows, workflow rules, and triggers on one object each re-run the save logic and compound CPU cost. Consolidating them is both a maintainability and a performance improvement.
- **Order of execution awareness** - understand that workflow field updates re-fire triggers, doubling their cost.
- **Asynchronous offloading** - move non-immediate work (callouts, heavy computation, notifications) out of the synchronous transaction.

## Concurrency and locking

- **Record locks** - DML locks the records it touches for the transaction. Two transactions updating related records can deadlock or throw `UNABLE_TO_LOCK_ROW`.
- **`FOR UPDATE`** - explicitly locks queried rows to serialise access and prevent lost updates.
- **Ownership skew and locking** - many child records under one parent means updates contend for the parent lock. A frequent cause of intermittent `UNABLE_TO_LOCK_ROW` errors at scale.
- **Reduce lock scope** - process in smaller batches, and order operations consistently to avoid deadlock.

`UNABLE_TO_LOCK_ROW` under load usually traces back to data skew or to unordered concurrent
updates on shared parents. The exam presents this as a scenario.

## Asynchronous processing at scale

- **Batch Apex chunking** - default 200 records per chunk, tunable down for heavy per-record work that risks CPU limits, or the chunk size adjusted to balance throughput against limit headroom.
- **Batch chaining and Queueable chaining** - sequence long pipelines while respecting concurrency limits on queued and scheduled jobs.
- **Platform Events for decoupling** - offload downstream work to subscribers so the publishing transaction stays fast.
- **Async limits** - concurrent async jobs and the daily async execution limit are themselves governor limits to design around.

## Diagnosing performance problems

1. Reproduce with a realistic data volume, not one record.
2. Capture a debug log and read the execution timeline and limit usage.
3. Use the query plan tool for slow SOQL.
4. Identify the scarce resource being exhausted: SOQL, DML, CPU, or heap.
5. Apply the matching fix: bulkify, add a selective filter, move to async, or reduce chunk size.

## Exam pointers

- Nested loops over two lists should become a map keyed by the join field.
- Non-selective queries on large objects fail; filter on selective indexed fields.
- `!=`, `NOT`, and leading-wildcard `LIKE` prevent index use.
- `UNABLE_TO_LOCK_ROW` at scale usually means data skew or unordered concurrent updates.
- Batch Apex gives fresh limits per chunk; reduce chunk size when per-record CPU is high.
- Consolidate overlapping automation on an object to cut compounded save-time cost.
- Move callouts and heavy computation to asynchronous processing.

## Official documentation

**[📖 Platform Developer II exam guide](https://trailhead.salesforce.com/credentials/platformdeveloperii)** - authoritative objectives
**[📖 Large Data Volumes Best Practices](https://developer.salesforce.com/docs/atlas.en-us.salesforce_large_data_volumes_bp.meta/salesforce_large_data_volumes_bp/)** - selectivity, skew, indexing
**[📖 Apex Best Practices](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_best_practices.htm)** - bulkification and efficiency
