---
last-updated: 2026-07-29
---

# PD2 01 - Advanced Developer Fundamentals

Platform Developer II builds on PD1. It assumes you already know Apex and Lightning basics
and tests depth: governor limits under pressure, the order of execution, and advanced Apex
patterns. This note sets the foundation the rest build on.

## The multi-tenant platform

- **Multi-tenancy** - many customers (orgs) share the same infrastructure. Your code runs alongside everyone else's, which is why governor limits exist: they stop one tenant monopolizing shared resources.
- **Governor limits** - per-transaction ceilings enforced by the runtime. Exceeding one throws an uncatchable `LimitException` that rolls back the transaction. Designing within limits is the central discipline of the exam.
- **Metadata-driven** - the platform is configuration and metadata over a shared engine; your customisations are metadata.

## Key governor limits to internalize

- **SOQL queries** - 100 synchronous, 200 asynchronous per transaction.
- **DML statements** - 150 per transaction.
- **Records retrieved by SOQL** - 50,000 per transaction.
- **Records processed by DML** - 10,000 per transaction.
- **CPU time** - 10,000 ms synchronous, 60,000 ms asynchronous.
- **Heap size** - 6 MB synchronous, 12 MB asynchronous.
- **Callouts** - 100 per transaction, with a total timeout budget.

The exam does not ask you to recite every number, but it constantly asks you to recognize
when code will breach one, and the fix is nearly always the same principle: bulkify.

## Bulkification

- **Bulkification** - writing code that processes collections rather than single records, so it works whether a trigger fires on one row or two hundred.
- **The cardinal rules** - never place SOQL or DML inside a loop. Query once into a collection, process in memory, and perform DML once on a collection.
- **Maps for lookups** - build a `Map<Id, SObject>` to relate records without querying inside a loop.
- **Collections** - `List`, `Set`, and `Map`. Sets deduplicate; maps key by a field, commonly Id.

SOQL-in-a-loop and DML-in-a-loop are the two errors the exam tests most, because they are
the two that most reliably blow a governor limit at scale.

## Order of execution

When a record is saved, the platform runs a defined sequence. Knowing it explains most
"why did my automation not see that value" questions.

1. Load the record and overwrite with request values.
2. System validation (required fields, field types).
3. **Before triggers**.
4. Custom validation rules, duplicate rules.
5. **After triggers**.
6. Assignment rules, auto-response, workflow rules.
7. Workflow field updates (which re-fire before and after update triggers once).
8. Processes and flows (depending on configuration and timing).
9. Escalation rules.
10. Roll-up summary recalculation, and parent record recalculation.
11. Commit to the database, then post-commit logic (async such as `@future`, and Platform Events depending on publish behavior).

The practical consequences the exam probes: before-triggers can change field values without
DML because the record is not yet saved; workflow field updates re-fire triggers; and
roll-up summaries recalculate after triggers.

## Apex language depth

- **SObject** - the generic type for any record; specific types like `Account` extend it.
- **sObject dynamic access** - `record.get('Field__c')` and `record.put(...)` for generic code.
- **Collections and iteration** - efficient iteration matters for CPU limits.
- **Exception handling** - `try/catch/finally`; custom exceptions extending `Exception`. `LimitException` cannot be caught.
- **Interfaces** - the basis of Batch, Queueable, Schedulable, and design patterns.
- **Inheritance** - `virtual`, `abstract`, and `override`.
- **Static versus instance** - static variables persist for the life of a transaction, useful for recursion control.

## Trigger design

- **One trigger per object** - the standard pattern, delegating logic to a handler class. Multiple triggers on one object have an undefined execution order.
- **Trigger handler framework** - a class structure separating before/after and insert/update/delete logic, making triggers testable and maintainable.
- **Context variables** - `Trigger.new`, `Trigger.old`, `Trigger.newMap`, `Trigger.oldMap`, and the boolean context flags.
- **Recursion control** - a static boolean to prevent a trigger re-entering itself when its own DML re-fires it.

## Exam pointers

- The fix for a governor-limit scenario is almost always bulkification: query and DML on collections, never in loops.
- Know the order of execution well enough to explain when a value is visible to which automation.
- Before-triggers modify the current record without DML; after-triggers are for related records and for reading system-populated fields like Id.
- One trigger per object, logic in a handler.
- `LimitException` is uncatchable and rolls back the transaction.
- Static variables persist across the transaction and are the standard recursion guard.

## Official documentation

**[📖 Platform Developer II exam guide](https://trailhead.salesforce.com/credentials/platformdeveloperii)** - authoritative objectives
**[📖 Apex Developer Guide - Execution Governors and Limits](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm)** - the limit values
**[📖 Triggers and Order of Execution](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm)** - the save sequence
