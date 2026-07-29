---
last-updated: 2026-07-29
---

# Salesforce Platform Developer II - Exam Strategy

> Cert-specific tactics. General study advice lives in [study-strategies.md](../../../resources/study-strategies.md).

## What PD2 actually is

Platform Developer II is the **proctored multiple-choice exam** that, combined with the
**Platform Developer II superbadge set** on Trailhead, earns the credential. Historically
PD2 involved a separate hands-on component; today the practical assessment is delivered
through superbadges. Confirm the current structure on the
[credential page](https://trailhead.salesforce.com/credentials/platformdeveloperii),
because Salesforce changes this periodically.

- Multiple-choice, roughly 60 scored questions
- About 105 minutes
- Passing around 68% (verify current value)
- Prerequisite: Platform Developer I
- The superbadges are where the real hands-on rigour lives

## How PD2 differs from PD1

PD1 asks whether you can write Apex and build components. PD2 asks whether you can do it
**at scale, securely, and with proper testing**. The same topic appears one level deeper:

- PD1: write a trigger. PD2: write a bulkified trigger that survives 200 records and does not breach a governor limit.
- PD1: query with SOQL. PD2: query a large object selectively so the optimiser uses an index.
- PD1: write a test to hit 75%. PD2: write meaningful tests with assertions, negative cases, and bulk data.

If you find a PD2 question that feels like a PD1 question, look for the scale, security, or
testing twist in the answer options.

## The top themes

1. **Governor limits and bulkification.** The most-tested idea. Any code with SOQL or DML in a loop is wrong. The fix is always collections and maps.

2. **Asynchronous Apex selection.** Future versus Queueable versus Batch versus Schedulable. Know which fits: callout-after-DML, chained complex work, millions of records, or a schedule.

3. **Order of execution.** Explains most "why did automation not see that value" questions. Before-triggers change the current record; workflow field updates re-fire triggers.

4. **Large data volumes.** Selective queries, indexes, data skew, and `UNABLE_TO_LOCK_ROW`.

5. **Security enforcement in Apex.** Apex enforces neither CRUD, FLS, nor sharing automatically. Know `WITH SECURITY_ENFORCED`, `stripInaccessible`, and the sharing keywords.

6. **LWC.** Decorators, wire versus imperative Apex, component communication (properties down, events up, Lightning Message Service across), and preferring Lightning Data Service for CRUD.

7. **Testing rigour.** `Test.startTest`/`stopTest`, `@testSetup`, `System.runAs`, callout mocking, assertions, and bulk tests.

## The traps

- **SOQL/DML in a loop** hidden inside otherwise plausible code. Scan every answer's loops first.
- **Future methods with sObject arguments** - not allowed; future takes only primitives. This makes an option wrong on sight.
- **Callout after DML in a synchronous transaction** - not allowed; the answer moves it to async.
- **Assuming Apex enforces security** - it does not unless you make it.
- **Confusing master-detail and lookup** capabilities: roll-ups, cascade delete, and inherited sharing need master-detail.
- **Choosing the wrong async type** for the described volume or chaining need.
- **Tests without assertions** offered as adequate - they are not.

## Question triage

Read for the discriminating constraint: the record count, the security requirement, the
"in a single transaction," or the "must run on a schedule." That phrase usually eliminates
two options immediately.

Where two answers both work, prefer the one that is bulk-safe, security-enforcing, and
uses the modern tool (Queueable over future, LWC over Aura, LDS over manual Apex CRUD,
unlocked packages over change sets).

## Study sequence

1. **Fundamentals** - governor limits, order of execution, trigger patterns.
   See [notes/01-fundamentals.md](notes/01-fundamentals.md).
2. **Process automation and integration** - async Apex, the largest area.
   See [notes/03-process-automation-logic-integration.md](notes/03-process-automation-logic-integration.md).
3. **Data modeling** - relationships and large data volumes.
   See [notes/02-data-modeling.md](notes/02-data-modeling.md).
4. **Performance** - which ties the above together.
   See [notes/06-performance.md](notes/06-performance.md).
5. **User interface** - LWC depth.
   See [notes/04-user-interface.md](notes/04-user-interface.md).
6. **Testing, debugging, deployment**.
   See [notes/05-testing-debugging-deployment.md](notes/05-testing-debugging-deployment.md).
7. **Work the superbadges.** They are mandatory for the credential and are the best possible practice for the exam's scale-oriented thinking.

Follow the week-by-week structure in [practice-plan.md](practice-plan.md).

## Hands-on is not optional

Build in a Developer Edition org or scratch org:

- A bulkified trigger with a handler class, tested with 200 records
- A Batch Apex job processing a large data set
- A Queueable making a callout after DML
- An LWC using `@wire`, and one calling Apex imperatively
- A test class using `Test.startTest`/`stopTest`, `@testSetup`, and `System.runAs`

Everything on the exam is something you can build, and building it is how the patterns
become automatic.

## The week before

- Recite the async decision table: future, queueable, batch, schedulable.
- Recite the order of execution well enough to place any automation in it.
- Review the ways Apex enforces (or fails to enforce) CRUD, FLS, and sharing.
- Review LWC communication patterns.
- Do not start new material in the final two days; consolidate.

## Exam day

Standard logistics are in the [exam-day checklist](../../../resources/exam-day-checklist.md).

PD2 specifics: the questions are dense, and several answers differ only by the scale or
security detail. Read every option fully, and check each code option for a SOQL or DML call
inside a loop before anything else.

## After passing

You are a certified Platform Developer II. Natural next steps are the **Application
Architect** path (which PD2 partially credits toward) via the Data Architect and Sharing
and Visibility Architect certifications, or the **Salesforce Architect** track more broadly.
