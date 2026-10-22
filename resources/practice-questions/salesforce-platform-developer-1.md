---
last-updated: 2026-10-22
difficulty: intermediate
---

# Salesforce Platform Developer I (PD1) - Practice Questions

30 questions across the PD1 areas: developer fundamentals, process automation and logic (the largest section), user interface, and testing, debugging, and deployment.

> **Cert page:** [exams/salesforce/platform-developer-1/](../../exams/salesforce/platform-developer-1/)

---

### Question 1
**Scenario:** An Apex trigger performs a SOQL query inside a `for` loop over `Trigger.new`.

A. It hits the SOQL governor limit on bulk operations; query once outside the loop and use a map
B. Use `Database.query`
C. It is fine for small volumes
D. Add a `try/catch` around the query so the limit exception is caught and the loop can continue with the next record

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Governor limits are per transaction, and 101 queries throws an uncatchable limit exception. Bulkification is the single most examined idea in PD1: query and DML outside loops, and process collections rather than single records.
</details>

---

### Question 2
**Scenario:** How many triggers should exist per object?

A. One per business requirement
B. One, delegating to a handler class so ordering is explicit and logic is testable
C. None; use flows only
D. As many as needed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multiple triggers on one object execute in an undefined order, which makes behavior depend on metadata deployment order. A single trigger with a handler class puts the sequencing in code you control.
</details>

---

### Question 3
**Scenario:** A field value must be set on the record being inserted, before it is saved.

A. A validation rule that populates the field with a default value when the record is saved
B. A scheduled job that fills the field some time after the record has been inserted
C. An after-insert trigger that queries the new record again and issues an update DML to set the field
D. A before-insert trigger that sets the field on `Trigger.new`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** In a before trigger the record is not yet committed, so assigning to the field is enough. Calling `update` on the same record in an after trigger causes recursion and wastes DML statements.
</details>

---

### Question 4
**Scenario:** Which context variable holds the previous values of updated records?

A. `Trigger.newMap`, which holds the record values as they were before the update was applied
B. `Trigger.oldMap`, keyed by record ID
C. `Trigger.new`
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
B. No requirement
C. 75% org-wide, every trigger covered, and all tests passing
D. 100% of lines in every class and trigger, because Salesforce blocks any deployment under full coverage

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Coverage is a floor, not a goal: a test that runs code without asserting anything counts toward it and proves nothing. Meaningful tests use `System.assert` on outcomes and cover bulk, positive, negative, and permission-restricted cases.
</details>

---

### Question 6
**Scenario:** A test class needs data to operate on.

A. Hard-code record IDs copied from the sandbox
B. Create test data inside the test
C. Use `@isTest(SeeAllData=true)` routinely
D. Query existing org data in the sandbox so tests run against realistic records

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Isolation is what makes tests portable between orgs. `SeeAllData=true` couples tests to whatever data happens to exist and is reserved for the few objects that cannot be created in a test. `@testSetup` creates shared data once per test class.
</details>

---

### Question 7
**Scenario:** A long-running callout must happen after a record is inserted.

A. A batch job
B. A validation rule
C. A synchronous callout in the trigger
D. An asynchronous method annotated `@future(callout=true)`, or a Queueable that implements `Database.AllowsCallouts`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Callouts are not allowed from a trigger's synchronous context after DML. Queueable is generally preferred over `@future`: it accepts non-primitive arguments, returns a job ID you can monitor, and can chain.
</details>

---

### Question 8
**Scenario:** Two million records must be processed nightly.

A. Batch Apex implementing `Database.Batchable`, scheduled nightly
B. A flow, because record-triggered flows process up to two million records per run in a single transaction
C. A single Queueable
D. A trigger on the object, which fires on every update and processes the records inline

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Batch Apex chunks the work so governor limits reset per execute, which is what makes large volumes possible at all. The `start` method returns a `QueryLocator` supporting up to 50 million records.
</details>

---

### Question 9
**Scenario:** Apex must respect the running user's object and field permissions.

A. Use `without sharing` on the class, because that keyword makes Apex enforce the running user's field permissions
B. Only profiles matter, since permission sets and sharing rules never apply to any Apex code, in any context
C. Apex runs in system mode; use `with sharing`, `WITH USER_MODE`, and `stripInaccessible`
D. Apex always respects them, because every class and trigger runs as the user who started the transaction

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `with sharing` enforces record sharing but not object or field permissions, which is the distinction that trips people up. `USER_MODE` on SOQL and DML enforces both in one step and is the modern way to do it.
</details>

---

### Question 10
**Scenario:** A Lightning Web Component must fetch records from Apex.

A. A trigger
B. A SOQL query written directly in the component's JavaScript file, executed from the browser against the org
C. A REST callout to the same org's API from the component's JavaScript, using the session ID of the logged-in user
D. An `@AuraEnabled` Apex method, called with `@wire` if cacheable or imperatively if it changes data

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `@AuraEnabled(cacheable=true)` enables client-side caching and is required for `@wire`, but a cacheable method must not perform DML. Data-modifying calls are imperative.
</details>

---

### Question 11
**Scenario:** A child-to-parent field must be read in SOQL.

A. A subquery in the SELECT list that traverses from the child object up to its parent
B. Dot notation on the relationship: `SELECT Id, Account.Name FROM Contact`
C. Run two separate queries and join the results in Apex using the parent record IDs
D. A roll-up summary field on the child object, which copies the parent's name into each child record

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Child-to-parent traverses up to five levels with dot notation. The parent-to-child direction needs an inner query over the child relationship name, which for custom objects ends in `__r`.
</details>

---

### Question 12
**Scenario:** A partial success is needed on a bulk DML operation.

A. `try/catch` around the insert, which commits every valid record and reports only the failed ones in the catch block
B. Insert one at a time
C. `Database.insert(records, false)`, which allows partial success and returns `SaveResult` records
D. The plain `insert records;` statement, which saves every valid record and silently skips the ones that fail

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The plain DML statement is all-or-nothing: one bad record rolls the whole thing back. The `Database` methods with `allOrNone` false commit the good records and report per-record errors, which you then have to handle rather than ignore.
</details>

---

### Question 13
**Scenario:** Where should reusable business logic live?

A. In service or helper classes called from triggers, controllers, and batch jobs
B. In the Lightning component
C. In validation rules
D. Duplicated in each trigger so every object keeps its own copy and a change cannot break another object

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Separating trigger handling from business logic is what makes the logic testable in isolation and callable from every entry point. It is also what stops the same rule drifting between the trigger version and the batch version.
</details>

---

### Question 14
**Scenario:** An exception must produce a user-friendly error on a record.

A. `addError()` on the record in a trigger, or a caught custom exception with a clear message
B. Ignore it
C. `System.debug`
D. Let it throw

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `addError` attaches the message to the specific record and blocks the save for that record, which is exactly what a user needs to see. An uncaught exception shows a stack trace and the whole transaction rolls back.
</details>

---

### Question 15
**Scenario:** Configuration values must be deployable and queryable in Apex without counting against SOQL limits.

A. Hard-coded constants
B. Custom labels, which hold the values as translatable text and are referenced in Apex as System.Label.Name
C. Custom metadata types, which deploy as metadata and whose queries do not count against SOQL limits
D. A custom object, which deploys with the package and whose records can be queried without counting toward limits

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Custom metadata is packageable and moves through environments as metadata rather than data, which custom settings do not. Custom labels are for translatable user-facing text, not configuration.
</details>

---

### Question 16
**Scenario:** A synchronous Apex transaction started from a record save throws `System.LimitException: Too many SOQL queries`. What is the per-transaction SOQL query limit in synchronous Apex?

A. 50 queries
B. 100 queries
C. 200 queries
D. 150 queries

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Synchronous Apex allows 100 SOQL queries per transaction, and asynchronous Apex allows 200. The 150 figure is the limit on DML statements per transaction, and 50 is not a SOQL limit. Limits exist because the platform is multi-tenant, which is why queries belong outside loops and code must be bulkified.

**Key Concept:** [Execution Governors and Limits](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm)
</details>

---

### Question 17
**Scenario:** A before-update trigger on Opportunity sets a Discount field. A custom validation rule checks that Discount stays under 30%. Will the validation rule see the value the trigger set?

A. No, validation rules run before any trigger fires
B. No, validation rules only check values typed by the user
C. Only if the trigger is rewritten as an after-update trigger
D. Yes, custom validation rules run after before triggers

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** In the order of execution, system validation runs, then before triggers, then custom validation rules, so the rules evaluate values the before trigger set. Validation rules check the record as it will be saved, not only user input. Moving the logic to an after trigger would require another DML to change the field.

**Key Concept:** [Triggers and Order of Execution](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm)
</details>

---

### Question 18
**Scenario:** A single query must return each Account's Name together with the last names of its related Contacts.

A. `SELECT Name, (SELECT LastName FROM Contacts) FROM Account`
B. `SELECT Name, Contact.LastName FROM Account`
C. `SELECT Name, (SELECT LastName FROM Contact) FROM Account`
D. `SELECT Account.Name, LastName FROM Contact GROUP BY Account`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Parent-to-child queries use a nested subquery on the child relationship name, which for standard Contacts is the plural `Contacts`. Dot notation only works from child to parent. The singular object name is not the relationship name, and grouping contacts by account returns aggregates rather than each account's list of contacts.

**Key Concept:** [Apex Database: Write SOQL Queries](https://trailhead.salesforce.com/content/learn/modules/apex_database/apex_database_soql)
</details>

---

### Question 19
**Scenario:** A nightly integration sends product records keyed by the ERP's ID. Existing products must be updated and new ones inserted, without duplicates and without querying first.

A. `insert` every record and delete duplicates afterward
B. `update` every record and catch the errors for new ones
C. `upsert` on a custom field marked as an External ID
D. `merge` every record into the oldest matching product

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `upsert` with an External ID field matches incoming records to existing ones by that key, updating matches and inserting the rest in one operation. Inserting everything creates duplicates. Updating fails for records that do not exist yet, and `merge` combines existing duplicates rather than loading data.

**Key Concept:** [Apex Database: Manipulate Records with DML](https://trailhead.salesforce.com/content/learn/modules/apex_database/apex_database_dml)
</details>

---

### Question 20
**Scenario:** A search box must find a term entered by the user across the Name fields of Accounts, Contacts, and Leads in one call.

A. Three SOQL queries with `LIKE` filters, one per object
B. A SOSL `FIND` query returning Account, Contact, and Lead
C. A SOQL query on Account with a semi-join to Contact and Lead
D. A report filtered on the term and exported by Apex

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SOSL searches text across multiple objects in one query using the search index and returns a list of lists, one per object. Three `LIKE` queries use three SOQL calls and scan rather than search. A semi-join filters one object by another's IDs, and Apex cannot run a report as a search mechanism.

**Key Concept:** [Apex Database: Write SOSL Queries](https://trailhead.salesforce.com/content/learn/modules/apex_database/apex_database_sosl)
</details>

---

### Question 21
**Scenario:** An Apex controller returns cases to a component. Users must only see cases they have record-level access to through sharing.

A. Declare the class `without sharing`
B. Declare the class `global` instead of `public`
C. Add `@AuraEnabled(cacheable=true)` to the method
D. Declare the class `with sharing`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `with sharing` makes the class enforce the running user's sharing rules, so queries return only records the user can access. `without sharing` ignores sharing. Access modifiers such as `global` control visibility of code, not data, and `cacheable=true` enables client caching. Object and field security are separate and need user mode or other checks.

**Key Concept:** [Secure Apex Classes](https://developer.salesforce.com/docs/platform/lwc/guide/apex-security.html)
</details>

---

### Question 22
**Scenario:** A cleanup routine written in Apex must run every Sunday at 2 AM without anyone starting it.

A. Implement `Schedulable` and schedule it with `System.schedule` and a cron expression
B. Put the logic in an after-insert trigger on a custom object
C. Annotate the method with `@future` and call it from a trigger
D. Add the class to a Lightning page so it runs when users visit

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A class implementing `Schedulable` can be scheduled with `System.schedule` (or from Setup) using a cron expression, so it runs at the set time automatically. Triggers and Lightning pages run only when someone saves a record or opens a page. `@future` runs code asynchronously soon after it is called, not on a schedule.

**Key Concept:** [Asynchronous Apex: Schedule Jobs Using the Apex Scheduler](https://trailhead.salesforce.com/content/learn/modules/asynchronous_apex/async_apex_scheduled)
</details>

---

### Question 23
**Scenario:** An admin's record-triggered flow needs a complex calculation that is already written in Apex.

A. Rewrite the calculation as nested flow formulas
B. Call the Apex from a validation rule on the object
C. Expose the method with `@InvocableMethod` and call it as a flow action
D. Mark the method `@AuraEnabled` so flows can see it

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `@InvocableMethod` exposes a static Apex method as an action that Flow Builder can call, passing lists of inputs and outputs. Rewriting the logic duplicates it. Validation rules cannot call Apex, and `@AuraEnabled` exposes methods to Lightning components, not to flows.

**Key Concept:** [InvocableMethod Annotation](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_annotation_InvocableMethod.htm)
</details>

---

### Question 24
**Scenario:** When an order ships, several independent systems and Salesforce processes must react, and the code that records the shipment should not need to know who is listening.

A. Call each subscriber's API directly from the trigger
B. Publish a platform event with `EventBus.publish`
C. Insert a Task for each subscriber to poll
D. Send an email alert that subscribers parse

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Platform events decouple publishers from subscribers: Apex publishes with `EventBus.publish`, and triggers, flows, and external clients subscribe without the publisher knowing about them. Direct callouts from a trigger are synchronous coupling and are not allowed from trigger context anyway. Polling Tasks and parsing emails are fragile workarounds.

**Key Concept:** [Platform Events Basics: Define and Publish Platform Events](https://trailhead.salesforce.com/content/learn/modules/platform_events_basics/platform_events_define_publish)
</details>

---

### Question 25
**Scenario:** A child Lightning Web Component has a button. When it is clicked, the parent component must be told which item was selected.

A. The child sets a property marked `@api` on the parent
B. The child calls the parent's Apex controller directly
C. The child writes the value to `sessionStorage` for the parent to poll
D. The child dispatches a `CustomEvent` that the parent handles

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Data flows down through public `@api` properties and up through events: the child dispatches a `CustomEvent` with a `detail` payload, and the parent listens with an `on<eventname>` handler. A child cannot set its parent's properties. Apex is server-side, and polling browser storage is a workaround, not component communication.

**Key Concept:** [Communicate with Events](https://developer.salesforce.com/docs/platform/lwc/guide/events.html)
</details>

---

### Question 26
**Scenario:** A Lightning Web Component on a record page must load two fields of the current record and refresh when the record ID changes, without writing Apex.

A. `@wire(getRecord, { recordId: '$recordId', fields: FIELDS })`
B. `@wire(getRecord, { recordId: 'recordId', fields: FIELDS })`
C. An imperative Apex call in `connectedCallback`
D. A `fetch()` call to the REST API in `renderedCallback`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Lightning Data Service `getRecord` adapter loads record data without Apex, and the `$` prefix makes `recordId` reactive so the wire re-runs when it changes. Without `$`, the literal string "recordId" is passed. Imperative Apex is unnecessary code, and calling the REST API from the browser bypasses Lightning Data Service caching and security handling.

**Key Concept:** [Lightning Web Components and Salesforce Data](https://trailhead.salesforce.com/content/learn/modules/lightning-web-components-and-salesforce-data)
</details>

---

### Question 27
**Scenario:** A component must display and edit a handful of fields on a record, with layout and save handled by the platform and no custom Apex.

A. A Visualforce page with a custom controller
B. An Aura component with a custom Apex save method
C. The `lightning-record-form` base component
D. An LWC with an imperative Apex DML call

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `lightning-record-form` uses Lightning Data Service to view, edit, and save records with field-level security and sharing applied, and needs no Apex. A Visualforce custom controller, an Aura component with Apex, and imperative DML from an LWC all require custom server code for something the base component already does.

**Key Concept:** [Lightning Web Components and Salesforce Data](https://trailhead.salesforce.com/content/learn/modules/lightning-web-components-and-salesforce-data)
</details>

---

### Question 28
**Scenario:** A test calls a method that enqueues a Queueable job, but assertions on the job's results fail because the job has not run yet.

A. Add `Thread.sleep` in the test until the job finishes
B. Wrap the call in `Test.startTest()` and `Test.stopTest()`
C. Mark the test with `@isTest(SeeAllData=true)`
D. Query `AsyncApexJob` in a loop until it completes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Asynchronous work enqueued between `Test.startTest()` and `Test.stopTest()` runs synchronously when `stopTest()` is called, so assertions afterward see the results; the pair also gives the code under test a fresh set of governor limits. Apex has no thread sleep, `SeeAllData` controls access to org data, and polling `AsyncApexJob` never sees the job finish inside a test.

**Key Concept:** [Asynchronous Apex](https://trailhead.salesforce.com/content/learn/modules/asynchronous_apex)
</details>

---

### Question 29
**Scenario:** A test class reaches 95% coverage but would still pass if the method under test returned the wrong value.

A. Add assertions such as `Assert.areEqual(expected, actual)`
B. Add more test methods that call the same code paths
C. Use `@isTest(SeeAllData=true)` to test with real data
D. Mark the class `@isTest(isParallel=true)` to run faster

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Coverage only shows which lines ran; assertions are what verify behavior, and the `Assert` class (`areEqual`, `isTrue`, and so on) makes them explicit. More calls without assertions raise coverage but still verify nothing. Real org data makes tests brittle, and parallel execution affects speed, not correctness.

**Key Concept:** [Assert Class](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_System_Assert.htm)
</details>

---

### Question 30
**Scenario:** A trigger fails only for one sales user in production. The developer needs detailed logs of that user's transactions for the next hour.

A. Add `System.debug` statements and deploy them to production
B. Run all tests in production and read the test results
C. Ask the user to send screenshots of the error message each time it appears
D. Set a user trace flag with a debug level in Setup's Debug Logs

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A trace flag on the user, with a chosen debug level and time window, generates debug logs for that user's transactions so the developer can see the actual execution. `System.debug` output is only captured when logging is active, and deploying just to add it is slow. Test runs use test data, and screenshots show the message but not the execution path.

**Key Concept:** [Set Up Debug Logging](https://help.salesforce.com/s/articleView?id=sf.code_add_users_debug_log.htm&language=en_US&type=5)
</details>

---

## Where to go deeper

- [PD1 cert page](../../exams/salesforce/platform-developer-1/) - notes, practice plan, strategy
- [Platform Developer II practice questions](./salesforce-platform-developer-2.md) - the advanced follow-on
- [Salesforce Administrator practice questions](./salesforce-administrator.md) - the declarative counterpart
- **[📖 Salesforce Trailhead](https://trailhead.salesforce.com/credentials/platformdeveloperi)** - official exam guide and study path
