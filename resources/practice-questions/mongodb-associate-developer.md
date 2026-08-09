---
last-updated: 2026-08-09
difficulty: intermediate
---

# MongoDB Associate Developer - Practice Questions

15 questions weighted toward CRUD operations (30%), aggregation (25%), data modeling (20%), then indexes (15%) and Atlas tools (10%).

> **Cert page:** [exams/mongodb/associate-developer/](../../exams/mongodb/associate-developer/)

---

### Question 1
**Scenario:** A document must be updated if it exists and created if it does not, in one operation.

A. `insertOne` then catch the duplicate key error
B. `updateOne` with `{ upsert: true }`
C. `replaceOne` without options
D. `findOne` then branch in application code

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The upsert option makes the operation atomic at the document level, so two concurrent writers cannot both decide the document is missing. The find-then-branch pattern has a race window between the read and the write.
</details>

---

### Question 2
**Scenario:** A query filters on `status` and sorts by `createdAt` descending.

A. Two separate single-field indexes
B. A compound index on `{ status: 1, createdAt: -1 }`
C. An index on `createdAt` only
D. No index; MongoDB sorts in memory

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The equality-sort-range rule puts the equality field first, then the sort field. That ordering lets the index satisfy both the filter and the sort, so the plan avoids an in-memory sort, which fails outright past the 100 MB limit unless `allowDiskUse` is set.
</details>

---

### Question 3
**Scenario:** Which aggregation stage placement most improves pipeline performance?

A. `$sort` first
B. `$match` and `$project` as early as possible, so later stages process fewer and smaller documents
C. `$group` first
D. `$lookup` first

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Filtering early is the single biggest lever, and an early `$match` can also use an index, which no later stage can. The query planner reorders some stages automatically, but writing the pipeline in the efficient order removes any doubt.
</details>

---

### Question 4
**Scenario:** A blog post has a small, bounded set of comments always read with the post.

A. A separate `comments` collection with a `postId` reference
B. Embed the comments in the post document
C. A separate database
D. Store comments as a string

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Data accessed together should be stored together. Embedding gives a single read with no join. The counter-case is unbounded growth: if comments could reach thousands, embedding risks the 16 MB document limit and the extended reference or subset pattern applies instead.
</details>

---

### Question 5
**Scenario:** `$lookup` in an aggregation pipeline does what?

A. Creates an index
B. Performs a left outer join to another collection in the same database
C. Deletes matching documents
D. Sorts results

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `$lookup` returns an array field of matched documents from the foreign collection, empty when nothing matches, which is what makes it a left outer join. It is available on sharded collections in current versions, but an indexed foreign field still matters for performance.
</details>

---

### Question 6
**Scenario:** Multiple documents across two collections must be updated atomically.

A. Update them one at a time
B. A multi-document transaction with a session, committed or aborted as a unit
C. Embed everything in one document
D. MongoDB cannot do this

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Transactions give ACID guarantees across documents and collections on a replica set or sharded cluster. They carry real cost, so the usual advice stands: model related data together so a single-document write suffices, and reserve transactions for genuine cross-entity invariants.
</details>

---

### Question 7
**Scenario:** A query returns only the `name` and `email` fields.

A. Retrieve full documents and filter in application code
B. A projection: `find(filter, { name: 1, email: 1, _id: 0 })`
C. A separate collection
D. `$unset` on the documents

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Projection reduces network transfer and memory. `_id` is returned unless explicitly excluded, which is the detail most often missed. If the projected fields are all in an index, the query can be covered and never touch the documents at all.
</details>

---

### Question 8
**Scenario:** Which index type supports queries on an array field's elements?

A. A text index
B. A standard index on the array field, which MongoDB creates as a multikey index automatically
C. A geospatial index
D. A hashed index

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multikey indexes are created implicitly when the indexed field holds an array, storing one index entry per element. The restriction to know: a compound index cannot have more than one multikey field, because the number of entries would multiply.
</details>

---

### Question 9
**Scenario:** A write must be acknowledged by a majority of replica set members.

A. `writeConcern: { w: 1 }`
B. `writeConcern: { w: "majority" }`
C. `writeConcern: { w: 0 }`
D. `readConcern: "majority"`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Majority write concern means the write survives a primary failover, because a new primary must be elected from members that have it. `w: 1` acknowledges from the primary only, so an unreplicated write can be rolled back.
</details>

---

### Question 10
**Scenario:** Which aggregation stage computes totals per category?

A. `$match`
B. `$group` with `_id` set to the category field and an accumulator such as `$sum`
C. `$project`
D. `$sort`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `$group` collapses documents by the `_id` expression and applies accumulators. Setting `_id: null` groups everything into one bucket, which is the idiom for a grand total.
</details>

---

### Question 11
**Scenario:** Application code must react to inserts and updates as they happen.

A. Poll the collection on a timer
B. A change stream, which delivers change events from the oplog and can be resumed with a resume token
C. A cron job
D. A trigger in the driver

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Change streams push changes rather than polling, and the resume token is what makes them reliable across a disconnect. On Atlas, Triggers are the managed layer built on the same mechanism.
</details>

---

### Question 12
**Scenario:** A slow query must be diagnosed.

A. Read the source
B. `explain("executionStats")` to see the winning plan, index usage, documents examined, and keys examined
C. Add an index and hope
D. Increase server memory

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The ratio of documents examined to documents returned is the diagnostic: close to 1 means the index is doing its job, and a large ratio with a COLLSCAN stage means it is not. Guessing at indexes without this measurement usually adds indexes that are never used.
</details>

---

### Question 13
**Scenario:** A field must be unique across a collection.

A. Check before every insert
B. A unique index on the field, which the server enforces
C. A validation rule in application code
D. A compound key

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Server-side enforcement is the only version that holds under concurrency. If some documents lack the field, a partial index with a filter expression avoids the problem that missing fields are treated as null and collide with each other.
</details>

---

### Question 14
**Scenario:** Documents must expire automatically after 30 days.

A. A scheduled delete job
B. A TTL index on a date field with `expireAfterSeconds` set
C. A capped collection
D. Manual cleanup

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A background thread removes expired documents roughly every 60 seconds, so expiry is approximate rather than immediate. A capped collection evicts by size in insertion order, which is a different guarantee.
</details>

---

### Question 15
**Scenario:** Which Atlas feature runs full-text search without a separate search cluster?

A. A regex query
B. Atlas Search, built on Apache Lucene and queried with the `$search` aggregation stage
C. A text index only
D. Atlas Data Federation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Atlas Search adds analyzers, relevance scoring, fuzzy matching, and faceting that the basic text index does not have, with no separate system to synchronize. Atlas Vector Search is the sibling feature for embedding similarity.
</details>

---

## Where to go deeper

- [MongoDB Associate Developer cert page](../../exams/mongodb/associate-developer/) - notes, practice plan, strategy
- [MongoDB Associate DBA practice questions](./mongodb-associate-dba.md) - the operations counterpart
- [MongoDB Atlas Administrator practice questions](./mongodb-associate-atlas-administrator.md) - the managed-service angle
- [SQL vs NoSQL](../../learn/concepts/sql-vs-nosql.md) - plain-English primer
- **[📖 MongoDB University](https://learn.mongodb.com/)** - official courses and exam pages
