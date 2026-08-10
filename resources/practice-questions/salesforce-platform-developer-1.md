---
last-updated: 2026-08-09
difficulty: intermediate
---

# Salesforce Platform Developer I (PD1) - Practice Questions

15 questions across the PD1 areas: developer fundamentals, process automation and logic (the largest section), user interface, and testing, debugging, and deployment.

> **Cert page:** [exams/salesforce/platform-developer-1/](../../exams/salesforce/platform-developer-1/)

---

### Question 1
**Scenario:** An Apex trigger performs a SOQL query inside a `for` loop over `Trigger.new`.

A. It is fine for small volumes
B. It will hit the SOQL query governor limit on bulk operations; query once outside the loop and build a map keyed by ID
C. Add a `try/catch`
D. Use `Database.query`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Governor limits are per transaction, and 101 queries throws an uncatchable limit exception. Bulkification is the single most examined idea in PD1: query and DML outside loops, and process collections rather than single records.
</details>

---

### Question 2
**Scenario:** How many triggers should exist per object?

A. One per business requirement
B. One, delegating to a handler class so ordering is explicit and logic is testable
C. As many as needed
D. None; use flows only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multiple triggers on one object execute in an undefined order, which makes behavior depend on metadata deployment order. A single trigger with a handler class puts the sequencing in code you control.
</details>

---

### Question 3
**Scenario:** A field value must be set on the record being inserted, before it is saved.

A. An after-insert trigger with an update DML
B. A before-insert trigger, modifying `Trigger.new` directly with no DML needed
C. A workflow rule
D. A scheduled job

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** In a before trigger the record is not yet committed, so assigning to the field is enough. Calling `update` on the same record in an after trigger causes recursion and wastes DML statements.
</details>

---

### Question 4
**Scenario:** Which context variable holds the previous values of updated records?

A. `Trigger.new`
B. `Trigger.oldMap`, keyed by record ID, alongside `Trigger.old` as a list
C. `Trigger.newMap`
D. `Trigger.isUpdate`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Comparing `Trigger.newMap.get(id)` against `Trigger.oldMap.get(id)` is how you detect a field actually changing, rather than firing logic on every save. `Trigger.old` is not available on insert, and `Trigger.new` is not available on delete.
</details>

---

### Question 5
**Scenario:** What minimum code coverage is required to deploy Apex to production?

A. 50%
B. 75% org-wide, with every trigger having at least some coverage and all tests passing
C. 100%
D. No requirement

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Coverage is a floor, not a goal: a test that runs code without asserting anything counts toward it and proves nothing. Meaningful tests use `System.assert` on outcomes and cover bulk, positive, negative, and permission-restricted cases.
</details>

---

### Question 6
**Scenario:** A test class needs data to operate on.

A. Query existing org data
B. Create test data in the test, since tests are isolated from org data by default
C. Use `@isTest(SeeAllData=true)` routinely
D. Hard-code IDs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Isolation is what makes tests portable between orgs. `SeeAllData=true` couples tests to whatever data happens to exist and is reserved for the few objects that cannot be created in a test. `@testSetup` creates shared data once per test class.
</details>

---

### Question 7
**Scenario:** A long-running callout must happen after a record is inserted.

A. A synchronous callout in the trigger
B. An asynchronous method annotated `@future(callout=true)`, or a Queueable that implements `Database.AllowsCallouts`
C. A batch job
D. A validation rule

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Callouts are not allowed from a trigger's synchronous context after DML. Queueable is generally preferred over `@future`: it accepts non-primitive arguments, returns a job ID you can monitor, and can chain.
</details>

---

### Question 8
**Scenario:** Two million records must be processed nightly.

A. A trigger
B. Batch Apex implementing `Database.Batchable`, scheduled with `System.schedule`
C. A single Queueable
D. A flow

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Batch Apex chunks the work so governor limits reset per execute, which is what makes large volumes possible at all. The `start` method returns a `QueryLocator` supporting up to 50 million records.
</details>

---

### Question 9
**Scenario:** Apex must respect the running user's object and field permissions.

A. Apex always respects them
B. Apex runs in system context by default; use `with sharing`, `WITH USER_MODE` on queries, and `Security.stripInaccessible` or `Schema` describe checks
C. Use `without sharing`
D. Only profiles matter

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `with sharing` enforces record sharing but not object or field permissions, which is the distinction that trips people up. `USER_MODE` on SOQL and DML enforces both in one step and is the modern way to do it.
</details>

---

### Question 10
**Scenario:** A Lightning Web Component must fetch records from Apex.

A. A SOQL query in JavaScript
B. An `@AuraEnabled` Apex method, called with the `@wire` decorator when it is cacheable or imperatively when it changes data
C. A REST callout to the same org
D. A trigger

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `@AuraEnabled(cacheable=true)` enables client-side caching and is required for `@wire`, but a cacheable method must not perform DML. Data-modifying calls are imperative.
</details>

---

### Question 11
**Scenario:** A child-to-parent field must be read in SOQL.

A. Two queries
B. Dot notation on the relationship: `SELECT Id, Account.Name FROM Contact`
C. A subquery
D. A formula field

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Child-to-parent traverses up to five levels with dot notation. The parent-to-child direction needs an inner query over the child relationship name, which for custom objects ends in `__r`.
</details>

---

### Question 12
**Scenario:** A partial success is needed on a bulk DML operation.

A. `insert records;`
B. `Database.insert(records, false)`, which allows partial success and returns `SaveResult` records to inspect
C. `try/catch` around the insert
D. Insert one at a time

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The plain DML statement is all-or-nothing: one bad record rolls the whole thing back. The `Database` methods with `allOrNone` false commit the good records and report per-record errors, which you then have to handle rather than ignore.
</details>

---

### Question 13
**Scenario:** Where should reusable business logic live?

A. Duplicated in each trigger
B. In service or helper classes called from triggers, controllers, and batch jobs alike
C. In validation rules
D. In the Lightning component

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Separating trigger handling from business logic is what makes the logic testable in isolation and callable from every entry point. It is also what stops the same rule drifting between the trigger version and the batch version.
</details>

---

### Question 14
**Scenario:** An exception must produce a user-friendly error on a record.

A. Let it throw
B. `addError()` on the record in a trigger, or a caught custom exception with a clear message
C. `System.debug`
D. Ignore it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `addError` attaches the message to the specific record and blocks the save for that record, which is exactly what a user needs to see. An uncaught exception shows a stack trace and the whole transaction rolls back.
</details>

---

### Question 15
**Scenario:** Configuration values must be deployable and queryable in Apex without counting against SOQL limits.

A. A custom object
B. Custom metadata types, which are deployable and whose queries do not count against SOQL query limits
C. Hard-coded constants
D. Custom labels

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Custom metadata is packageable and moves through environments as metadata rather than data, which custom settings do not. Custom labels are for translatable user-facing text, not configuration.
</details>

---

## Where to go deeper

- [PD1 cert page](../../exams/salesforce/platform-developer-1/) - notes, practice plan, strategy
- [Platform Developer II practice questions](./salesforce-platform-developer-2.md) - the advanced follow-on
- [Salesforce Administrator practice questions](./salesforce-administrator.md) - the declarative counterpart
- **[📖 Salesforce Trailhead](https://trailhead.salesforce.com/credentials/platformdeveloperi)** - official exam guide and study path
