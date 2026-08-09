---
last-updated: 2026-08-09
difficulty: intermediate
---

# Confluent Certified Administrator for Apache Kafka (CCAAK) - Practice Questions

15 questions weighted toward managing and operating (30%), monitoring and troubleshooting and Confluent Platform (20% each), then Kafka fundamentals and security (15% each).

> **Cert page:** [exams/confluent/certified-administrator/](../../exams/confluent/certified-administrator/)

---

### Question 1
**Scenario:** A broker fails in a cluster with replication factor 3 and `min.insync.replicas` 2.

A. The cluster stops accepting writes
B. Leadership moves to an in-sync replica and producing continues, since two in-sync replicas remain
C. Data is lost
D. Consumers stop

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Leader election among in-sync replicas is what makes the failure survivable. Losing a second broker would drop the partition below `min.insync.replicas`, at which point `acks=all` producers receive `NotEnoughReplicas` rather than silently accepting unreplicated writes.
</details>

---

### Question 2
**Scenario:** Which component replaced ZooKeeper for cluster metadata?

A. Nothing; ZooKeeper is still required
B. KRaft mode, where a quorum of controllers manages metadata in an internal Kafka log
C. Schema Registry
D. Kafka Connect

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** KRaft removes a separate system to operate and improves metadata scalability and failover time. Controllers can run on dedicated nodes or combined with brokers, and combined mode is discouraged for production clusters.
</details>

---

### Question 3
**Scenario:** Partitions are unevenly distributed after adding brokers.

A. New brokers take load automatically
B. Run a partition reassignment to move replicas onto the new brokers, throttling the reassignment to protect live traffic
C. Restart the cluster
D. Create new topics only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Adding a broker only affects new partitions, so existing load stays where it is. The throttle matters: an unthrottled reassignment saturates the network and degrades production traffic while it copies data.
</details>

---

### Question 4
**Scenario:** Consumer lag is growing steadily on one consumer group.

A. Add partitions
B. Diagnose first: check whether consumers are slow, failing, rebalancing, or fewer than the partition count, then scale consumers up to at most the partition count
C. Increase retention
D. Restart brokers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Lag is a symptom with several causes, and adding partitions to an already-underconsumed topic does nothing. Adding consumers beyond the partition count also does nothing, which is why partition count is a capacity planning decision made early.
</details>

---

### Question 5
**Scenario:** Which metric indicates replicas falling behind their leader?

A. `BytesInPerSec`
B. `UnderReplicatedPartitions`, along with `IsrShrinksPerSec` and replica lag
C. `RequestQueueSize`
D. `MessagesInPerSec`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A sustained non-zero under-replicated count is one of the highest-signal broker alerts, because it means durability is degraded before anything has visibly failed. `OfflinePartitionsCount` above zero is the more severe version: those partitions have no leader at all.
</details>

---

### Question 6
**Scenario:** Disk usage on brokers is growing without bound.

A. Add disks only
B. Review per-topic retention by time and size, plus compaction settings, and confirm segment rolling and deletion are actually occurring
C. Delete topics
D. Reduce replication factor

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Retention applies per topic and overrides the broker default, so one misconfigured topic can consume a cluster. Deletion only happens on closed segments, so a large `segment.bytes` with low throughput can hold data far beyond the intended retention window.
</details>

---

### Question 7
**Scenario:** Clients must authenticate and traffic must be encrypted.

A. Network isolation only
B. TLS for encryption plus SASL for authentication (SCRAM, GSSAPI, or OAUTHBEARER), with ACLs or RBAC for authorization
C. ACLs alone
D. A firewall

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The three concerns are distinct and each needs configuring: encryption in transit, identity, and what that identity may do. Listeners are configured per security protocol, which is how a cluster serves internal and external clients differently.
</details>

---

### Question 8
**Scenario:** A specific application must be allowed to read one topic only.

A. Give it cluster admin
B. An ACL granting Read on that topic and Read on its consumer group to that principal, with `allow.everyone.if.no.acl.found` disabled
C. A separate cluster
D. A network policy

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Consumers need the group resource permission as well as the topic, which is the pairing most often missed. Leaving the allow-everyone fallback enabled means an unmatched resource is wide open, which defeats the point of ACLs.
</details>

---

### Question 9
**Scenario:** A cluster must be replicated to a second data center for disaster recovery.

A. Copy the log directories
B. Cluster Linking or MirrorMaker 2 replicating topics, consumer groups, and offsets to the remote cluster
C. Backups only
D. A shared filesystem

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Replicating offsets is what makes consumer failover viable rather than a full reprocess. Cluster Linking preserves offsets natively; MirrorMaker 2 translates them, which is why the two behave differently on cutover.
</details>

---

### Question 10
**Scenario:** A rolling broker upgrade must proceed without downtime.

A. Stop all brokers and upgrade
B. Upgrade one broker at a time, waiting for under-replicated partitions to return to zero before proceeding, and set the inter-broker protocol version deliberately
C. Upgrade all at once
D. Upgrade clients first

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Waiting for replicas to catch up is what preserves durability during the roll; moving on early can leave partitions with too few in-sync replicas. Pinning the inter-broker protocol version until every broker is upgraded is what keeps a rollback possible.
</details>

---

### Question 11
**Scenario:** Frequent consumer group rebalances are disrupting processing.

A. Ignore them
B. Investigate causes: consumers exceeding `max.poll.interval.ms`, unstable instances, or scaling churn; use cooperative sticky assignment and static group membership to reduce impact
C. Reduce partitions
D. Disable consumer groups

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cooperative rebalancing avoids the stop-the-world pause of the eager protocol, and static membership with `group.instance.id` stops a rolling restart from triggering a rebalance per instance. Both reduce impact rather than removing the cause.
</details>

---

### Question 12
**Scenario:** Which Confluent Platform component enforces schema compatibility?

A. Control Center
B. Schema Registry, storing schemas and validating new versions against the subject's compatibility mode
C. REST Proxy
D. ksqlDB

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Schema Registry stores its state in a compacted Kafka topic, so it is itself a Kafka client rather than an external database. Broker-side schema validation can additionally reject records whose schema is not registered.
</details>

---

### Question 13
**Scenario:** Broker request latency is high and the request queue is filling.

A. Add brokers immediately
B. Check network and I/O thread counts against utilization, disk performance, and whether a few clients are producing disproportionate load, before adding capacity
C. Restart the cluster
D. Reduce replication

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Saturated `num.network.threads` or `num.io.threads` produce queueing that looks like a capacity problem but is a configuration one. Client quotas are the other lever, bounding a single misbehaving application's effect on everyone else.
</details>

---

### Question 14
**Scenario:** A topic's partition count must increase.

A. It cannot change
B. Partitions can be added but not removed, and adding them changes key-to-partition mapping so ordering guarantees for existing keys are broken from that point
C. Partitions can be reduced too
D. Recreate the topic only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Existing data is not redistributed, so a key that used to land on partition 2 may now land on partition 5 while its history stays behind. This is why over-provisioning partitions modestly at creation is easier than growing them later.
</details>

---

### Question 15
**Scenario:** An unclean leader election setting must be decided.

A. Enable it for availability
B. Leave `unclean.leader.election.enable` false by default, accepting unavailability rather than data loss, and enable it only where availability genuinely outranks correctness
C. It does not matter
D. Enable it everywhere

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An unclean election promotes an out-of-sync replica, so acknowledged messages it never received are lost. That is a legitimate trade for some telemetry topics and unacceptable for a financial ledger, which is why it is a per-topic decision.
</details>

---

## Where to go deeper

- [CCAAK cert page](../../exams/confluent/certified-administrator/) - notes, practice plan, strategy
- [Confluent Developer practice questions](./confluent-certified-developer.md) - the application counterpart
- [Queues vs streams](../../learn/concepts/queues-vs-streams.md) - plain-English primer on the model
- [Observability basics](../../learn/concepts/observability-basics.md) - what to monitor and why
- **[📖 Confluent certification](https://www.confluent.io/certification/)** - official exam guides
