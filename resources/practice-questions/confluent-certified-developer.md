---
last-updated: 2026-08-09
difficulty: intermediate
---

# Confluent Certified Developer for Apache Kafka (CCDAK) - Practice Questions

15 questions weighted toward development (30%), then application design, Kafka Streams, Kafka Connect, and Schema Registry (15% each) and ksqlDB (10%).

> **Cert page:** [exams/confluent/certified-developer/](../../exams/confluent/certified-developer/)

---

### Question 1
**Scenario:** Message ordering must be guaranteed for all events about a single customer.

A. Use a single partition for the topic
B. Use the customer ID as the message key, so the default partitioner routes all of that customer's events to one partition
C. Set `acks=all`
D. Enable idempotence

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Kafka guarantees order within a partition, not across a topic. Keying gives per-entity ordering while keeping parallelism across entities; a single-partition topic gives global ordering at the price of no parallelism at all.
</details>

---

### Question 2
**Scenario:** A producer must not lose messages if the leader broker fails.

A. `acks=0`
B. `acks=all` with `min.insync.replicas` set to at least 2 and a replication factor of 3
C. `acks=1`
D. More retries

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `acks=all` alone is not enough: without `min.insync.replicas`, a topic down to one in-sync replica still acknowledges. The pairing of replication factor 3 with `min.insync.replicas` 2 tolerates one broker loss while still refusing to acknowledge unreplicated writes.
</details>

---

### Question 3
**Scenario:** A producer retries and creates duplicate messages.

A. Accept duplicates
B. Enable idempotence with `enable.idempotence=true`, which deduplicates retries per producer session and partition
C. Reduce retries to zero
D. Use `acks=1`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The producer stamps a sequence number that the broker uses to reject duplicates. Idempotence is on by default in current clients, and it covers retries within a session; exactly-once across a read-process-write cycle additionally needs transactions.
</details>

---

### Question 4
**Scenario:** A consumer group has 4 consumers and the topic has 3 partitions.

A. Each consumer gets a share of every partition
B. Three consumers each own one partition and the fourth is idle
C. The group fails
D. Partitions are split

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A partition is assigned to at most one consumer in a group, so partition count is the ceiling on group parallelism. The idle consumer is not useless: it takes over immediately on a rebalance if another consumer dies.
</details>

---

### Question 5
**Scenario:** A consumer must not reprocess messages after a restart.

A. Set `auto.offset.reset=earliest`
B. Commit offsets, ideally after processing rather than before, choosing manual commits when at-least-once matters
C. Disable offsets
D. Use a new group ID

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Auto-commit on a timer can commit offsets for records not yet processed, which loses messages on a crash. Committing after processing gives at-least-once, so consumers still need to be idempotent. `auto.offset.reset` only applies when there is no committed offset at all.
</details>

---

### Question 6
**Scenario:** Schema changes must not break existing consumers.

A. Version the topic
B. Schema Registry with a compatibility mode: backward compatibility lets new consumers read old data, which is the common default for consumer-first upgrades
C. Send JSON without a schema
D. Recreate the topic

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Backward compatibility permits deleting fields and adding optional ones with defaults. Forward compatibility is the mirror image for producer-first upgrades, and full compatibility requires both. Getting the direction wrong is the classic Schema Registry mistake.
</details>

---

### Question 7
**Scenario:** A topic must retain only the latest value per key indefinitely.

A. `cleanup.policy=delete` with long retention
B. `cleanup.policy=compact`, which keeps the most recent value per key
C. A single partition
D. A short retention window

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Compaction is what makes a topic usable as a changelog or state store, and it is how Kafka Streams backs its state. A null value is the tombstone that marks a key for deletion, and keyless messages cannot be compacted at all.
</details>

---

### Question 8
**Scenario:** A stream must be joined to a lookup table of reference data.

A. Query a database per record
B. A KStream-KTable join in Kafka Streams, with the table materialized from a compacted topic and co-partitioned with the stream
C. Two consumers
D. A window join

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Co-partitioning is the requirement people miss: both sides need the same key and the same partition count, or the join silently produces incomplete results. A GlobalKTable avoids co-partitioning by replicating the whole table to every instance, which suits small reference data.
</details>

---

### Question 9
**Scenario:** Which Kafka Streams operation requires a state store?

A. `filter`
B. Stateful operations such as `aggregate`, `count`, `reduce`, joins, and windowing
C. `map`
D. `peek`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** State stores are local RocksDB instances backed by a compacted changelog topic, which is what makes them recoverable after a failure. Stateless operations need no such backing, so scaling them is purely a matter of partitions.
</details>

---

### Question 10
**Scenario:** Data must move from a database into Kafka without writing code.

A. A custom producer
B. Kafka Connect with a source connector, running in distributed mode for fault tolerance
C. A Streams application
D. ksqlDB only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Connect handles offsets, restarts, and scaling for you, and Single Message Transforms cover light per-record changes without a separate application. Sink connectors move the other direction, and change-data-capture source connectors read the database log rather than polling.
</details>

---

### Question 11
**Scenario:** A consumer takes 10 minutes to process a batch and is repeatedly removed from the group.

A. Increase `session.timeout.ms` only
B. Increase `max.poll.interval.ms` to exceed the processing time, or reduce `max.poll.records` so each batch is smaller
C. Disable heartbeats
D. Add consumers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Heartbeats run on a background thread, so `session.timeout.ms` is not what fails here. `max.poll.interval.ms` bounds the time between poll calls, and exceeding it makes the group assume the consumer is stuck and rebalance.
</details>

---

### Question 12
**Scenario:** Exactly-once semantics are required across a consume-transform-produce cycle.

A. Idempotence alone
B. Transactions: a `transactional.id` on the producer, offsets committed inside the transaction, and consumers set to `read_committed`
C. Manual deduplication
D. `acks=all`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** All three parts are needed. Committing the consumer's offsets within the same transaction as the output records is what makes the cycle atomic, and `read_committed` is what stops downstream consumers seeing aborted records.
</details>

---

### Question 13
**Scenario:** Messages that repeatedly fail processing must not block the partition.

A. Skip them silently
B. Route them to a dead letter topic after bounded retries, with enough context to diagnose and replay
C. Retry forever
D. Delete the topic

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A poison message with unbounded retries halts the partition, so throughput for every other key behind it goes to zero. The dead letter record needs the original headers and error detail, otherwise it is unactionable.
</details>

---

### Question 14
**Scenario:** Producer throughput must increase without losing durability.

A. `acks=0`
B. Increase `batch.size` and set `linger.ms` above zero to fill batches, and enable compression such as lz4 or zstd
C. More partitions only
D. Larger messages

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Batching and compression trade a small amount of latency for a large gain in throughput, and compression applies per batch so bigger batches compress better. Reducing `acks` gains throughput by giving up the durability the question says to keep.
</details>

---

### Question 15
**Scenario:** A stream of events must be aggregated into 5-minute buckets.

A. A global aggregation
B. A windowed aggregation with a tumbling window, plus a grace period for late-arriving events
C. A join
D. A filter

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Tumbling windows are fixed and non-overlapping; hopping windows overlap; session windows are activity-driven with a gap. Grace period is the key operational setting, since events arriving after it are dropped rather than counted.
</details>

---

## Where to go deeper

- [CCDAK cert page](../../exams/confluent/certified-developer/) - notes, practice plan, strategy
- [Confluent Administrator practice questions](./confluent-certified-administrator.md) - the operations counterpart
- [Queues vs streams](../../learn/concepts/queues-vs-streams.md) - plain-English primer on the model
- [Idempotency explained](../../learn/concepts/idempotency-explained.md) - why at-least-once needs idempotent consumers
- **[📖 Confluent certification](https://www.confluent.io/certification/)** - official exam guides
