---
last-updated: 2026-08-09
difficulty: advanced
---

# Salesforce Platform Developer II (PDII) - Practice Questions

15 questions at PDII level: advanced Apex, asynchronous processing, integration patterns, performance at scale, and testing and deployment discipline. The full credential also requires the programmatic assignments.

> **Cert page:** [exams/salesforce/platform-developer-2/](../../exams/salesforce/platform-developer-2/)

---

### Question 1
**Scenario:** A SOQL query on a 20 million row object times out.

A. Add `LIMIT`
B. Make the filter selective on an indexed field, remove leading wildcards and negative operators, and consider a skinny table or a custom index
C. Use `Database.query`
D. Increase the timeout

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The query optimizer only uses an index when the filter is selective enough, and `!=`, `NOT`, leading `%` wildcards, and nulls on non-indexed fields all defeat it. The Query Plan tool in the developer console shows which index, if any, a query would use.
</details>

---

### Question 2
**Scenario:** Work must be chained so each unit runs after the previous completes, with a monitorable job ID.

A. `@future` methods
B. Queueable Apex, enqueuing the next job from `execute`, with `Finalizer` for post-processing
C. Batch Apex
D. Scheduled Apex

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `@future` cannot chain, takes only primitive arguments, and returns nothing to monitor. Queueable chaining is limited in depth from a synchronous context, and a `Finalizer` runs even when the Queueable fails, which is the only reliable place to handle an uncatchable failure.
</details>

---

### Question 3
**Scenario:** An integration must push data to Salesforce in near real time from an external system with high volume.

A. SOAP API record by record
B. Platform Events or Change Data Capture for an event-driven flow, or the Bulk API for large batches
C. Data Loader on a schedule
D. Visualforce

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Choosing the integration pattern is the PDII skill: request-reply for synchronous need, fire-and-forget with platform events for decoupling, batch data synchronization for volume. Row-by-row synchronous API calls exhaust limits and couple the two systems' availability.
</details>

---

### Question 4
**Scenario:** A trigger must not re-enter itself when its own DML fires it again.

A. Ignore recursion
B. A static Boolean or static Set of processed IDs in a helper class, since statics live for the transaction
C. A `try/catch`
D. `without sharing`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Statics are per transaction, which is exactly the scope recursion control needs. A Set of already-processed IDs is safer than a single flag, because a blanket flag can skip records that legitimately need processing later in the same transaction.
</details>

---

### Question 5
**Scenario:** A callout must be tested in an Apex test.

A. Make the real callout
B. `Test.setMock` with an `HttpCalloutMock` or `WebServiceMock` implementation
C. Skip testing it
D. `SeeAllData=true`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Tests cannot make real callouts, so a mock is mandatory rather than a nicety. Mocking also lets you test the error paths, timeouts and 500s, which a live endpoint will not produce on demand.
</details>

---

### Question 6
**Scenario:** A Lightning Web Component must receive updates when a record changes elsewhere.

A. Poll with `setInterval`
B. Lightning Message Service for cross-component communication in the page, or an empApi subscription to a platform event for server-driven updates
C. A page refresh
D. A wire adapter only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The choice depends on where the change originates: LMS crosses component boundaries including Aura and Visualforce in the same page, while platform events over empApi carry changes originating on the server. Polling burns API calls to mostly learn nothing changed.
</details>

---

### Question 7
**Scenario:** Which governor limit applies per transaction in synchronous Apex?

A. 200 SOQL queries
B. 100 SOQL queries, 150 DML statements, 50,000 query rows, and 10 seconds of CPU time
C. No limits
D. Limits apply per day only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Asynchronous contexts double several of these, including 200 SOQL queries and 60 seconds of CPU. CPU time is the one that most often bites at scale, and it is consumed by loops and collection manipulation rather than by queries.
</details>

---

### Question 8
**Scenario:** Sensitive fields must be stripped from a query result according to the running user's access.

A. Manual describe checks on every field
B. `Security.stripInaccessible` with `AccessType.READABLE`, or `WITH USER_MODE` on the query itself
C. `with sharing`
D. Field-level security handles it automatically

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Apex runs in system context by default, so field-level security is not applied unless you apply it. `stripInaccessible` removes inaccessible fields from the records and reports what it removed, which is far less error-prone than hand-written describe checks.
</details>

---

### Question 9
**Scenario:** A large data volume org has slow list views and reports.

A. Delete data
B. Skinny tables, custom indexes, archiving strategies such as Big Objects, and division of large objects by defined data skew avoidance
C. Bigger page size
D. More users

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Ownership skew, where one user owns hundreds of thousands of records, causes sharing recalculation locks and is a classic large-data-volume problem. Big Objects hold archived data with a defined index at the cost of limited query flexibility.
</details>

---

### Question 10
**Scenario:** Apex must expose a REST endpoint to an external system.

A. Visualforce
B. An `@RestResource` class with `@HttpGet`, `@HttpPost` and related methods, secured through a connected app and OAuth
C. A trigger
D. A flow

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The class handles routing by URL mapping and HTTP verb. The security work is outside the class: a connected app, an OAuth flow appropriate to the client, and a minimum-access integration user rather than a shared administrator login.
</details>

---

### Question 11
**Scenario:** A test must verify behavior for a specific user's permissions.

A. Run as the administrator
B. `System.runAs(user)` with a user created in the test carrying the profile or permission set under examination
C. Assume it works
D. Deploy and check manually

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `runAs` changes the user context for sharing and permission checks, though it does not reset governor limits. Testing under a restricted user is what catches logic that only works because the developer was an administrator.
</details>

---

### Question 12
**Scenario:** Two users edit the same record concurrently and one overwrites the other.

A. Nothing can be done
B. `FOR UPDATE` on the SOQL query to lock rows within the transaction, and an optimistic check on `LastModifiedDate` for user-facing edits
C. A validation rule
D. A trigger

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Row locking prevents the interleaving inside a transaction, at the risk of `UNABLE_TO_LOCK_ROW` under contention. For a user editing a record over minutes, an optimistic concurrency check is the right tool, because holding a lock that long is not viable.
</details>

---

### Question 13
**Scenario:** A deployment must run only the tests relevant to the change.

A. Run all tests always
B. Specify `RunSpecifiedTests` with the relevant classes, understanding that production deployments still require 75% org-wide coverage
C. Skip tests
D. `RunLocalTests` only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `RunSpecifiedTests` shortens the deployment for a small change, while `RunLocalTests` excludes managed package tests and is the usual choice for a full run. The coverage requirement does not change with the option you pick.
</details>

---

### Question 14
**Scenario:** Business logic must be shared between a flow and Apex.

A. Duplicate it
B. An `@InvocableMethod` on an Apex class, callable from Flow and from Apex alike
C. A trigger
D. A future method

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Invocable methods take and return lists, which is what keeps them bulk-safe when Flow calls them with multiple records. Duplicating the logic guarantees the two copies drift.
</details>

---

### Question 15
**Scenario:** An unhandled Apex exception in an asynchronous job must be visible to operations.

A. `System.debug` only
B. Custom error logging to a custom object or Big Object plus platform event based logging, since platform events publish even when the transaction rolls back
C. Email the developer
D. Check the debug log

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Writing an error record with plain DML is lost in the rollback that follows the exception. Publishing a platform event with `PUBLISH_IMMEDIATELY` survives the rollback, which is why it is the standard logging pattern on the platform.
</details>

---

## Where to go deeper

- [PDII cert page](../../exams/salesforce/platform-developer-2/) - notes, practice plan, strategy
- [Platform Developer I practice questions](./salesforce-platform-developer-1.md) - the prerequisite
- [Salesforce Administrator practice questions](./salesforce-administrator.md) - the declarative counterpart
- **[📖 Salesforce Trailhead](https://trailhead.salesforce.com/credentials/platformdeveloperii)** - official exam guide and study path
