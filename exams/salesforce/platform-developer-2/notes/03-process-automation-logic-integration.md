---
last-updated: 2026-07-29
---

# PD2 03 - Process Automation, Logic, and Integration

Asynchronous Apex, advanced SOQL, and integration. The largest and most heavily tested
area of PD2.

## Choosing declarative versus programmatic

- **Declarative first** - Salesforce guidance and the exam both prefer configuration (Flow) over code when it meets the requirement. Reach for Apex when logic is too complex for Flow, needs to be reused across contexts, requires callouts with complex handling, or must process very large volumes.
- **Flow** - the primary declarative automation tool. Record-triggered, scheduled, screen, and autolaunched flows.
- **Apex** - for complex logic, bulk processing, and integration beyond declarative capability.

## Asynchronous Apex

The heart of this domain. Each type suits a different need.

- **Future methods (`@future`)** - fire-and-forget for a single asynchronous task, and required for callouts made after DML in the same transaction. Limitations: only primitive arguments (no sObjects, to avoid stale state), no chaining, and no return value. Being superseded by Queueable for most uses.
- **Queueable Apex** - the modern async workhorse. Accepts sObjects and complex types, supports chaining (one job enqueues the next), and returns a job Id for monitoring. Use for sequential async work and callouts.
- **Batch Apex** - processes large data volumes in chunks. Implements `Database.Batchable` with `start` (returns a QueryLocator or Iterable, up to 50 million records), `execute` (runs per chunk, default 200 records, each chunk a separate transaction with its own governor limits), and `finish` (post-processing). Use when the volume exceeds normal transaction limits.
- **Schedulable Apex** - runs Apex on a schedule via `System.schedule` and a cron expression. Often used to kick off a batch job.

**Choosing between them**

| Need | Use |
|---|---|
| Callout right after DML, simple | Future or Queueable |
| Chained async steps, complex types | Queueable |
| Millions of records in chunks | Batch |
| Run on a recurring schedule | Schedulable (often launching a Batch) |

Governor limits reset per async transaction, and per batch chunk, which is precisely why
async is the answer to large-volume scenarios.

## Advanced SOQL and SOSL

- **Relationship queries** - parent-to-child subqueries and child-to-parent dot-walking.
- **Dynamic SOQL** - `Database.query(String)` builds queries at runtime. Guard against SOQL injection by using bind variables or `String.escapeSingleQuotes`.
- **Aggregate functions** - `GROUP BY`, `HAVING`, `COUNT`, `SUM`, returning `AggregateResult`.
- **FOR UPDATE** - locks rows to prevent concurrent update, used to avoid race conditions.
- **Query optimization** - selective filters on indexed fields, as covered in the data note.

Dynamic SOQL injection is a security topic the exam tests: always bind or escape user
input.

## Integration

- **Outbound (Apex callouts)** - `HttpRequest`/`HttpResponse` for REST, or generated stubs for SOAP. Callouts cannot follow uncommitted DML in the same transaction, which is why callouts after DML go in async.
- **Named credentials** - store the endpoint and authentication so credentials are not hard-coded, and OAuth is handled by the platform. The recommended pattern.
- **Inbound REST (`@RestResource`)** - expose an Apex class as a custom REST endpoint with `@HttpGet`, `@HttpPost`, and so on.
- **Apex SOAP web services (`webservice` keyword)** - expose methods as SOAP.
- **Platform Events** - a publish-subscribe event bus for decoupled, near-real-time integration. Publishers and subscribers do not know about each other.
- **Change Data Capture (CDC)** - publishes record change events automatically for downstream systems.
- **Continuation** - for long-running async callouts from a Visualforce or Lightning context without holding the request thread.
- **Salesforce Connect** - surfaces external data as external objects without copying it in.

- **Callout limits** - 100 per transaction, and a cumulative timeout budget. Batch callouts require implementing `Database.AllowsCallouts`.

## Transaction control

- **Savepoints and rollback** - `Database.setSavepoint()` and `Database.rollback(sp)` to undo partial work within a transaction.
- **Idempotency** - designing operations that can safely run twice, important for retried integrations. See [idempotency explained](../../../../learn/concepts/idempotency-explained.md).

## Exam pointers

- Callouts cannot follow DML in the same synchronous transaction; move the callout to async.
- Future methods take only primitives and cannot chain; Queueable takes objects and chains.
- Batch Apex gives fresh governor limits per chunk, which is why it handles large volumes.
- Use named credentials rather than hard-coded endpoints and secrets.
- Guard dynamic SOQL against injection with bind variables or escaping.
- Platform Events are the decoupled pub-sub option for integration.
- Prefer Flow over Apex when it meets the requirement.

## Official documentation

**[📖 Platform Developer II exam guide](https://trailhead.salesforce.com/credentials/platformdeveloperii)** - authoritative objectives
**[📖 Asynchronous Apex](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_async_overview.htm)** - future, queueable, batch, scheduled
**[📖 Apex Integration Services](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_callouts.htm)** - callouts, named credentials, REST
