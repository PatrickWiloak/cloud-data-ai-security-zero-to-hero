---
last-updated: 2026-10-22
difficulty: advanced
---

# Salesforce Platform Developer II (PDII) - Practice Questions

30 questions at PDII level: advanced Apex, asynchronous processing, integration patterns, performance at scale, and testing and deployment discipline. The full credential also requires the programmatic assignments.

> **Cert page:** [exams/salesforce/platform-developer-2/](../../exams/salesforce/platform-developer-2/)

---

### Question 1
**Scenario:** A SOQL query on a 20 million row object times out.

A. Increase the query timeout in Setup, since the query is correct and the platform is cutting it off too early
B. Make the filter selective on an indexed field, remove leading wildcards and negative operators, and consider a skinny table or a custom index
C. Rewrite it as `Database.query` with a dynamic SOQL string, which gives the optimizer a different plan
D. Add `LIMIT 50000` so the platform stops reading once enough rows are returned

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The query optimizer only uses an index when the filter is selective enough, and `!=`, `NOT`, leading `%` wildcards, and nulls on non-indexed fields all defeat it. The Query Plan tool in the developer console shows which index, if any, a query would use.
</details>

---

### Question 2
**Scenario:** Work must be chained so each unit runs after the previous completes, with a monitorable job ID.

A. Queueable Apex, enqueuing the next job from `execute`, with `Finalizer` for post-processing
B. Batch Apex, launched from a trigger for each record so the jobs queue behind one another in Apex Jobs
C. `@future` methods, calling the next `@future` from the end of each one
D. Scheduled Apex that polls a custom object every minute

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `@future` cannot chain, takes only primitive arguments, and returns nothing to monitor. Queueable chaining is limited in depth from a synchronous context, and a `Finalizer` runs even when the Queueable fails, which is the only reliable place to handle an uncatchable failure.
</details>

---

### Question 3
**Scenario:** An integration must push data to Salesforce in near real time from an external system with high volume.

A. Visualforce pages that the external system posts to, inserting each record
B. Data Loader on a schedule, run every few minutes from the external company's network
C. Platform Events or Change Data Capture for an event-driven flow, or the Bulk API for large batches
D. SOAP API calls made record by record, with one login and one `create` per row

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Choosing the integration pattern is the PDII skill: request-reply for synchronous need, fire-and-forget with platform events for decoupling, batch data synchronization for volume. Row-by-row synchronous API calls exhaust limits and couple the two systems' availability.
</details>

---

### Question 4
**Scenario:** A trigger must not re-enter itself when its own DML fires it again.

A. Mark the handler class `without sharing` so that the DML it performs does not fire the trigger again on records it cannot see
B. A static Boolean or static Set of processed IDs in a helper class, since statics live for the transaction
C. Wrap the DML in a `try/catch` and swallow the exception thrown when the trigger is invoked a second time in the same transaction
D. Ignore recursion, because the platform stops a trigger from firing a second time on the same record within one transaction

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Statics are per transaction, which is exactly the scope recursion control needs. A Set of already-processed IDs is safer than a single flag, because a blanket flag can skip records that legitimately need processing later in the same transaction.
</details>

---

### Question 5
**Scenario:** A callout must be tested in an Apex test.

A. Add `SeeAllData=true` to the test class
B. Make the real callout inside the test method and assert on the live response, because that exercises the true integration
C. `Test.setMock` with an `HttpCalloutMock` or `WebServiceMock` implementation
D. Skip testing the callout and cover the surrounding code only

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Tests cannot make real callouts, so a mock is mandatory rather than a nicety. Mocking also lets you test the error paths, timeouts and 500s, which a live endpoint will not produce on demand.
</details>

---

### Question 6
**Scenario:** A Lightning Web Component must receive updates when a record changes elsewhere.

A. Lightning Message Service for cross-component communication in the page, or an empApi subscription to a platform event for server-driven updates
B. Poll with `setInterval` in the component's `connectedCallback`, calling an `@AuraEnabled` method every few seconds to fetch the current record and compare it with what is already displayed
C. Ask the user for a page refresh whenever the record changes, since components only read data when the page first loads and cannot be told about later saves
D. A wire adapter only, since `@wire` re-pushes data to the component whenever any other user or process saves the record

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The choice depends on where the change originates: LMS crosses component boundaries including Aura and Visualforce in the same page, while platform events over empApi carry changes originating on the server. Polling burns API calls to mostly learn nothing changed.
</details>

---

### Question 7
**Scenario:** Which governor limit applies per transaction in synchronous Apex?

A. 100 SOQL queries, 150 DML statements, 50,000 query rows, and 10 seconds of CPU time
B. 200 SOQL queries, 150 DML statements, 50,000 query rows and 60 seconds of CPU time, which is the synchronous limit set
C. No limits apply to a transaction run by a system administrator
D. Limits apply per day across the whole org only, and a single transaction can use as many queries as it needs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Asynchronous contexts double several of these, including 200 SOQL queries and 60 seconds of CPU. CPU time is the one that most often bites at scale, and it is consumed by loops and collection manipulation rather than by queries.
</details>

---

### Question 8
**Scenario:** Sensitive fields must be stripped from a query result according to the running user's access.

A. Declare the class `with sharing`, which enforces record visibility and so also removes fields the running user cannot read
B. Field-level security handles it automatically, because Apex always applies the profile of the running user to every query
C. `Security.stripInaccessible` with `AccessType.READABLE`, or `WITH USER_MODE` on the query itself
D. Manual describe checks on every field, calling `isAccessible()` in a loop before reading and remembering to repeat it in each class

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Apex runs in system context by default, so field-level security is not applied unless you apply it. `stripInaccessible` removes inaccessible fields from the records and reports what it removed, which is far less error-prone than hand-written describe checks.
</details>

---

### Question 9
**Scenario:** A large data volume org has slow list views and reports.

A. Add more user licenses so that the load is spread across more sessions and each list view returns its rows sooner
B. Skinny tables, custom indexes, archiving to Big Objects, and avoiding data skew on large objects
C. Delete data aggressively, including records that audit and retention rules say must be kept, until the object is small
D. Raise the list view page size to the maximum so fewer round trips are needed to render every row in the report on screen

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Ownership skew, where one user owns hundreds of thousands of records, causes sharing recalculation locks and is a classic large-data-volume problem. Big Objects hold archived data with a defined index at the cost of limited query flexibility.
</details>

---

### Question 10
**Scenario:** Apex must expose a REST endpoint to an external system.

A. A flow with an HTTP listener element, secured by a connected app
B. A trigger on the object that listens for inbound HTTP traffic
C. Visualforce page with `action` and a custom controller that returns JSON to the external system when it requests the page
D. An `@RestResource` class with `@HttpGet` and `@HttpPost` methods, secured through a connected app and OAuth

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The class handles routing by URL mapping and HTTP verb. The security work is outside the class: a connected app, an OAuth flow appropriate to the client, and a minimum-access integration user rather than a shared administrator login.
</details>

---

### Question 11
**Scenario:** A test must verify behavior for a specific user's permissions.

A. Deploy to production and check manually by logging in as a user with the profile
B. Assume it works, since the platform enforces profile rules the same way in every test
C. `System.runAs(user)` with a user created in the test carrying the profile or permission set under examination
D. Run the test as the administrator who wrote it

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `runAs` changes the user context for sharing and permission checks, though it does not reset governor limits. Testing under a restricted user is what catches logic that only works because the developer was an administrator.
</details>

---

### Question 12
**Scenario:** Two users edit the same record concurrently and one overwrites the other.

A. A validation rule that compares the record's current values with `PRIORVALUE` and blocks the save whenever the two users have entered different values in the same field
B. `FOR UPDATE` on the SOQL query to lock rows in the transaction, plus an optimistic `LastModifiedDate` check for user edits
C. Nothing can be done, because the last save always wins on the platform and concurrent edits cannot be detected
D. A before-update trigger that locks the record for the whole length of the user's editing session on the page

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Row locking prevents the interleaving inside a transaction, at the risk of `UNABLE_TO_LOCK_ROW` under contention. For a user editing a record over minutes, an optimistic concurrency check is the right tool, because holding a lock that long is not viable.
</details>

---

### Question 13
**Scenario:** A deployment must run only the tests relevant to the change.

A. `RunSpecifiedTests` with the relevant classes, remembering that each deployed class still needs 75% coverage
B. Skip tests for the small change and rely on the sandbox validation that ran earlier in the same release
C. Run all tests in the org on every deployment, including managed package tests, so that nothing is ever missed, whatever the size of the change
D. `RunLocalTests` only, which runs just the tests in the changed classes and their direct dependencies and meets the 75% rule

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `RunSpecifiedTests` shortens the deployment for a small change, while `RunLocalTests` excludes managed package tests and is the usual choice for a full run. Production still enforces the 75% coverage rule whichever option you pick.
</details>

---

### Question 14
**Scenario:** Business logic must be shared between a flow and Apex.

A. A trigger on the object that the flow and the Apex each call by updating a field, so the logic runs in one place
B. A `@future` method, which Flow and Apex can each call asynchronously to run the shared logic in the background
C. Duplicate the logic in a flow formula and in an Apex class, and keep the two in step with a documented review process
D. An `@InvocableMethod` on an Apex class, callable from Flow and from Apex alike

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Invocable methods take and return lists, which is what keeps them bulk-safe when Flow calls them with multiple records. Duplicating the logic guarantees the two copies drift.
</details>

---

### Question 15
**Scenario:** An unhandled Apex exception in an asynchronous job must be visible to operations.

A. Check the debug log after each failure, setting a trace flag on the automated process user for the day of the job
B. Email the developer from a `catch` block using `Messaging.sendEmail`, which also covers unexpected failures in the job and tells them straight away
C. `System.debug` only, with logging set to ERROR level so the message is captured in the debug log for the job and can be searched later by operations staff
D. Custom error logging to a custom object plus platform event logging, since events publish even when the transaction rolls back

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Writing an error record with plain DML is lost in the rollback that follows the exception. Publishing a platform event with `PUBLISH_IMMEDIATELY` survives the rollback, which is why it is the standard logging pattern on the platform.
</details>

---

### Question 16
**Scenario:** Apex code inserts a list of 1,000 Account records in a single DML statement. How does the Account before-insert trigger process them?

A. Once, with all 1,000 records in `Trigger.new`
B. 1,000 times, with one record in `Trigger.new` each time
C. Five times, in chunks of 200 records, within the same transaction
D. Five times, in five separate transactions with fresh governor limits

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Triggers process records in chunks of up to 200, so 1,000 records cause five trigger invocations, all inside the one transaction and sharing its governor limits (and its static variables). The trigger never sees all 1,000 at once, and it is not invoked per record. Chunks do not start new transactions, which is why a static "already ran" flag can wrongly skip later chunks.

**Key Concept:** [Apex Triggers: Bulk Apex Triggers](https://trailhead.salesforce.com/content/learn/modules/apex_triggers/apex_triggers_bulk)
</details>

---

### Question 17
**Scenario:** An org must retain several billion historical device readings on-platform for compliance, queried occasionally by device ID and date, with consistent performance.

A. A custom big object with an index on device ID and date
B. A custom object with a skinny table and a custom index on device ID
C. A hierarchy custom setting storing the readings
D. Files attached to each Account record as CSV

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Big objects are built to store billions of records with consistent performance, queried through their defined index fields, which suits archival and compliance data. Standard custom objects degrade and consume storage at this scale even with tuning. Custom settings are for small configuration data, and CSV files cannot be queried.

**Key Concept:** [Big Objects](https://developer.salesforce.com/docs/atlas.en-us.bigobjects.meta/bigobjects/big_object.htm)
</details>

---

### Question 18
**Scenario:** Apex makes callouts to a partner API that uses OAuth. Endpoints and credentials must differ between sandbox and production, and no secrets may appear in code or custom fields.

A. Store the token in a custom setting and add it as a header
B. Use a named credential (with an external credential) as the callout endpoint
C. Hardcode the endpoint and read the secret from a static resource
D. Ask the partner to allowlist Salesforce IP ranges and skip authentication on calls

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A named credential defines the endpoint and, with its external credential, the authentication, and Salesforce handles the auth headers so code only references `callout:Name`. Each org can hold its own values. Custom settings and static resources store secrets in plain places, and IP allowlisting is not a substitute for authenticating the caller.

**Key Concept:** [Named Credentials as Callout Endpoints](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)
</details>

---

### Question 19
**Scenario:** A Lightning component calls an external service that can take up to a minute to respond. Synchronous callouts are tying up server resources and hitting timeouts.

A. Increase the HTTP timeout to five minutes on the request
B. Move the callout to a before-insert trigger
C. Retry the synchronous callout in a loop until it succeeds
D. Return a `Continuation` from the `@AuraEnabled` Apex method

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A Continuation makes the callout asynchronously from a component's Apex method and calls a callback when the response arrives, allowing longer waits without holding a server thread. Apex callout timeouts cannot be raised that far. Triggers cannot make synchronous callouts, and retry loops make the problem worse.

**Key Concept:** [Continuations](https://developer.salesforce.com/docs/platform/lwc/guide/apex-continuations.html)
</details>

---

### Question 20
**Scenario:** A mobile app must create an Account, then a Contact and an Opportunity linked to it, and wants one round trip to Salesforce with later steps using the new Account's ID.

A. A REST Composite request with reference IDs between subrequests
B. Three sequential REST calls, each waiting for the previous one to return
C. A Bulk API 2.0 job containing all three records
D. A SOQL query followed by two separate SOAP calls

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Composite resource runs a series of subrequests in one call, and a later subrequest can reference an earlier one's result, such as the new Account ID. Three sequential calls are three round trips. A Bulk API job loads one object per job and is meant for large volumes, and mixing SOQL and SOAP adds calls rather than removing them.

**Key Concept:** [Composite Resource](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite_composite.htm)
</details>

---

### Question 21
**Scenario:** A Batch Apex job must count how many records failed validation across all `execute` calls and email the total from `finish`. The count is always zero.

A. Declare the counter `static` so it survives between batches
B. Store the counter in a local variable inside `execute`
C. Implement `Database.Stateful` so instance variables keep their values
D. Increase the batch size to 2,000 so there is only one batch

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Each `execute` call runs in its own transaction, and only a class implementing `Database.Stateful` keeps instance member values between them. Static variables reset between transactions, and a local variable is gone after each call. Batch size is capped at 2,000, and relying on one batch breaks as data grows.

**Key Concept:** [Asynchronous Apex: Use Batch Apex](https://trailhead.salesforce.com/content/learn/modules/asynchronous_apex/async_apex_batch)
</details>

---

### Question 22
**Scenario:** A test method inserts a User with a role and then an Account in the same method, and fails with `MIXED_DML_OPERATION`.

A. Insert both records in one `Database.insert` call with `allOrNone` false
B. Perform the setup-object DML inside a `System.runAs` block
C. Mark the test method `@isTest(SeeAllData=true)`
D. Insert the Account before the User instead of after it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** DML on setup objects (such as User with a role) and non-setup objects (such as Account) cannot be mixed in one transaction, but in tests the setup DML can be isolated inside `System.runAs` (or moved to an asynchronous job). A single mixed insert still violates the rule. `SeeAllData` affects data visibility, and the order of the statements does not matter.

**Key Concept:** [Mixed DML Operations in Test Methods](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_dml_non_mix_sobjects_test_methods.htm)
</details>

---

### Question 23
**Scenario:** An Apex method inserts an Order and then its line items. If any line item fails, the Order insert must be undone while the method handles the error gracefully.

A. Delete the Order in the `catch` block using its saved ID
B. Throw an unhandled exception so the platform rolls everything back
C. Insert the line items before the Order so failures happen first
D. Use `Database.setSavepoint()` and `Database.rollback()`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A savepoint marks the database state, and rolling back to it discards every DML after it while the code continues and handles the error. Deleting by hand is a second operation that can also fail and leaves traces such as consumed autonumbers. An unhandled exception rolls back but gives the user an error rather than graceful handling, and line items need the Order's ID first.

**Key Concept:** [Transaction Control](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/langCon_apex_transaction_control.htm)
</details>

---

### Question 24
**Scenario:** A dynamic SOQL query builds its WHERE clause from a search term typed by the user. A security review flags it.

A. Use bind variables, such as `Database.queryWithBinds`
B. Convert the input to upper case before adding it to the query
C. Limit the input to 255 characters in the component
D. Run the query in a `without sharing` class

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Concatenating user input into a query string allows SOQL injection. Bind variables keep input as data rather than query syntax, and `String.escapeSingleQuotes` is the fallback where binding is impossible. Changing case or length does not neutralize quotes, and `without sharing` widens access, which makes injection worse.

**Key Concept:** [SOQL Injection Due to Insecure Database Query Construction](https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packagingGuide/secure_code_violation_soql_injection.htm)
</details>

---

### Question 25
**Scenario:** After a user saves a new record in a Lightning Web Component, the component must open that record's standard record page without hardcoding a URL.

A. Set `window.location.href` to `/lightning/r/` plus the record ID
B. Dispatch a `CustomEvent` named `navigate` to the parent component with the ID
C. Call an Apex method that returns a `PageReference`
D. Use `NavigationMixin.Navigate` with a `standard__recordPage` page reference

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The navigation service takes a PageReference object describing the destination, so it works across Lightning Experience, mobile, and Experience Cloud without building URLs. Setting `window.location` hardcodes a URL format and reloads the app. A custom event only notifies a parent, and an Apex `PageReference` is a Visualforce concept.

**Key Concept:** [Navigation](https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-navigation.html)
</details>

---

### Question 26
**Scenario:** A component displays records from a wired `cacheable=true` Apex method. After the component updates a record through an imperative Apex call, the list still shows the old values.

A. Remove `cacheable=true` so the wire cannot be cached
B. Call `refreshApex()` on the wired result after the update succeeds
C. Call the cacheable method imperatively in a loop until values change
D. Reload the whole browser page with `location.reload()`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `refreshApex` re-queries the server for a wired Apex result and refreshes the client cache, so the component shows current data. A wired Apex method must be cacheable, so removing the flag breaks the wire. Polling imperatively does not update the wired value, and reloading the page is a poor user experience.

**Key Concept:** [Client-Side Caching](https://developer.salesforce.com/docs/platform/lwc/guide/apex-result-caching.html)
</details>

---

### Question 27
**Scenario:** A component must list up to 100,000 order lines in a table. Loading them all at once makes the page slow and hits heap limits.

A. Query all rows in one Apex call and filter them in JavaScript
B. Render each row as its own child component with its own query
C. Use `lightning-datatable` with infinite loading and fetch rows in pages
D. Increase the Apex heap limit in Setup for this component

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Infinite loading (`enable-infinite-loading` with an `onloadmore` handler) loads a first page and fetches more as the user scrolls, keeping queries, heap, and DOM size small. Loading everything is exactly what fails. A query per row multiplies calls, and the heap limit is a governor limit that cannot be raised in Setup.

**Key Concept:** [Datatable](https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-datatable.html)
</details>

---

### Question 28
**Scenario:** A complex trigger misbehaves in a sandbox. The developer wants to step through the execution with breakpoints and inspect variables, using VS Code.

A. Add `System.debug` after every line and read the raw log in Setup
B. Capture a debug log and use the Apex Replay Debugger
C. Run the code in Anonymous Apex with `System.assert` calls
D. Write a test class and read only its code coverage report

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Apex Replay Debugger in the Salesforce Extensions for VS Code replays a debug log as if it were a live session, with breakpoints, variable inspection, and the call stack. Reading raw logs filled with debug statements is slow. Anonymous Apex assertions halt at the first failure without stepping, and coverage shows which lines ran, not what values they held.

**Key Concept:** [Find and Fix Bugs with Apex Replay Debugger](https://trailhead.salesforce.com/content/learn/modules/find-and-fix-bugs-with-apex-replay-debugger)
</details>

---

### Question 29
**Scenario:** A large org wants its customizations split into modular, versioned units it can install, upgrade, and track independently across environments from source control.

A. Change sets built by hand in each sandbox for every release
B. A single metadata ZIP of the whole org deployed each time
C. Copying metadata between orgs with the Metadata API by hand
D. Unlocked packages built with Salesforce CLI from the repository

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Unlocked packages group related metadata into versioned artifacts built from source control, which can be installed and upgraded independently in each org. Change sets are manual, unversioned, and cannot be scripted. Deploying the whole org every time is not modular, and hand copies are neither versioned nor repeatable.

**Key Concept:** [Unlocked Packages for Customers](https://trailhead.salesforce.com/content/learn/modules/unlocked-packages-for-customers)
</details>

---

### Question 30
**Scenario:** An Apex service recalculates the same exchange rate table on almost every request, repeating identical queries and computation across many users.

A. Store the table in a static variable so all users share it
B. Query the table with `FOR UPDATE` to speed later reads
C. Cache the computed table in Platform Cache with a time-to-live
D. Move the computation into a before-insert trigger

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Platform Cache (org or session partitions) keeps computed data in memory across transactions and users, with a time-to-live, avoiding repeated queries and computation. Static variables last only for one transaction. `FOR UPDATE` locks rows and slows concurrency, and moving the work into a trigger does not reduce how often it runs.

**Key Concept:** [Platform Cache Basics](https://trailhead.salesforce.com/content/learn/modules/platform_cache)
</details>

---

## Where to go deeper

- [PDII cert page](../../exams/salesforce/platform-developer-2/) - notes, practice plan, strategy
- [Platform Developer I practice questions](./salesforce-platform-developer-1.md) - the prerequisite
- [Salesforce Administrator practice questions](./salesforce-administrator.md) - the declarative counterpart
- **[📖 Salesforce Trailhead](https://trailhead.salesforce.com/credentials/platformdeveloperii)** - official exam guide and study path
