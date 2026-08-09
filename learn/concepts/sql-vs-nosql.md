---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 9 min
---

# SQL vs NoSQL

> **9-minute read. Assumes no database background.**

## The one-line answer

SQL databases store rows in tables with a fixed schema and let you combine them at read time with joins. NoSQL databases relax one or more of those constraints in exchange for scale, flexibility, or a data shape that fits the problem better.

"NoSQL" is not one thing. It covers at least four quite different families, and choosing between them matters more than the SQL-versus-NoSQL question itself.

## The relational model

A SQL database stores data in tables with defined columns and types, and relationships between them:

```sql
CREATE TABLE customers (
  id       BIGINT PRIMARY KEY,
  email    TEXT UNIQUE NOT NULL,
  country  TEXT NOT NULL
);

CREATE TABLE orders (
  id           BIGINT PRIMARY KEY,
  customer_id  BIGINT REFERENCES customers(id),
  total_cents  INTEGER NOT NULL,
  placed_at    TIMESTAMPTZ NOT NULL
);

SELECT c.email, SUM(o.total_cents)
FROM customers c JOIN orders o ON o.customer_id = c.id
WHERE c.country = 'DE'
GROUP BY c.email;
```

Three properties follow from this design and explain most of what SQL databases are good at:

- **Normalization**: each fact is stored once. Change a customer's email and every query sees the new value immediately, because there is only one copy.
- **Joins at read time**: you do not need to decide in advance which questions you will ask. Any combination of tables is available.
- **ACID transactions**: a group of changes either all happen or none do, and concurrent transactions do not see each other's half-finished work.

## The four NoSQL families

| Family | Stores | Good at | Examples |
|---|---|---|---|
| **Key-value** | A value under a key | Extremely fast lookups by key | Redis, DynamoDB (simple), Memcached |
| **Document** | Nested JSON-like documents | Storing an entity and its sub-parts together | MongoDB, Firestore, DocumentDB |
| **Wide-column** | Rows with flexible column families | Very high write volume, time-series | Cassandra, Bigtable, HBase |
| **Graph** | Nodes and edges | Relationship traversal many hops deep | Neo4j, Neptune |

Plus, increasingly relevant, **vector databases** for similarity search over embeddings. See [Embeddings and vector search](./embeddings-and-vector-search.md).

## The real trade-off

The honest framing is not "SQL is old, NoSQL is scalable". It is:

**SQL decides the data shape once, at write time, and stays flexible about questions.**
**NoSQL usually decides the questions first, and shapes the data to answer them.**

A document database storing an order with its line items nested inside is fast when you always fetch the whole order. It is awkward when someone asks "which products sold best in Germany last quarter", because that question cuts across documents in a way the storage shape did not anticipate.

A relational database handles that question with a join, and pays for it with more work per read and more care at write time.

## Consistency

SQL databases traditionally offer **strong consistency**: a write is visible to the next read.

Many distributed NoSQL databases offer **eventual consistency** by default: a write propagates to replicas over some short window, so a read immediately afterwards may return the old value. This is a deliberate trade for availability and latency, and it is configurable in most modern systems.

The practical question is not "which is better" but "what does my application do when a read returns data from two seconds ago". For a social feed, nothing. For an account balance during a withdrawal, quite a lot.

See [Eventual consistency](./eventual-consistency.md).

## Scaling

**Vertical scaling** means a bigger machine. It works well and is simpler than people admit; a single well-tuned PostgreSQL instance handles workloads far larger than most applications ever reach.

**Horizontal scaling** means spreading data across machines. Relational databases can do it through read replicas (easy, read-only) and sharding (harder, because joins and transactions across shards get expensive). Many NoSQL systems were designed for it from the start, which is their genuine advantage.

The nuance worth knowing: modern distributed SQL databases such as CockroachDB, Spanner, and Aurora blur this line substantially, offering relational semantics with horizontal scale.

## Choosing

Reach for **relational** when:
- The data has clear entities and relationships
- You need transactions across multiple records
- The questions will change over time and you cannot predict them
- Reporting and analytics matter
- You are unsure. It is the safer default, and the ecosystem is deeper

Reach for **key-value** when:
- Access is always by a known key
- You need single-digit millisecond latency at very high volume
- Sessions, caches, feature flags, rate limit counters

Reach for **document** when:
- Each entity is naturally self-contained and read as a whole
- The shape varies between records
- Product catalogs, user profiles, content management, event payloads

Reach for **wide-column** when:
- Write volume is enormous and predictable
- Time-series, telemetry, event logs at very large scale

Reach for **graph** when:
- The relationships *are* the data and queries traverse several hops
- Fraud rings, recommendations, network topology, access control graphs

## Polyglot persistence

Most non-trivial systems use more than one. A typical shape: PostgreSQL as the system of record, Redis for sessions and caching, a search index for full-text queries, and a data warehouse for analytics.

That is normal and usually correct. The cost is operational: each system needs backups, monitoring, upgrades, and expertise. Add one only when the benefit is concrete.

## What to look at next

- **[Eventual consistency](./eventual-consistency.md)** - what "eventually" actually means for your code
- **[Embeddings and vector search](./embeddings-and-vector-search.md)** - the vector database family
- **[Queues vs streams](./queues-vs-streams.md)** - the other big "which one" data question
- **[Caching explained](./caching-explained.md)** - the layer usually sitting in front of the database
- **[Service comparison: databases](../../resources/service-comparison-databases.md)** - AWS, Azure, and GCP equivalents
- **[Databases topic](../../topics/databases.md)** - everything in the repo on this subject
