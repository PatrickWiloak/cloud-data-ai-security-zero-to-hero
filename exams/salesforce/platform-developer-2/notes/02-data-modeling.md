---
last-updated: 2026-07-29
---

# PD2 02 - Advanced Data Modeling and Management

Relationships, large data volumes, and querying at scale. PD2 tests the performance and
sharing consequences of data model decisions, not just how to create a field.

## Relationships

- **Lookup relationship** - a loose reference. The child can exist without the parent; deleting the parent does not delete children by default.
- **Master-detail relationship** - a tight ownership. The detail cannot exist without its master, inherits the master's sharing and security, is deleted when the master is deleted, and enables **roll-up summary fields**. A record can have at most two master-detail relationships.
- **Roll-up summary field** - aggregates child records (count, sum, min, max) on the master. Only available on the master side of a master-detail relationship.
- **Many-to-many** - implemented with a **junction object**: a custom object with two master-detail relationships. The first master controls ownership and sharing; the order matters.
- **Hierarchical relationship** - a special lookup on the User object, referencing another user.
- **External lookup and indirect lookup** - relate to external objects via Salesforce Connect.

Master-detail versus lookup is a constant exam theme: choose master-detail when you need
roll-ups, cascade delete, or inherited sharing, and lookup when the child must stand alone.

## Schema design considerations

- **Denormalisation for performance** - occasionally duplicating data to avoid expensive queries, weighed against maintenance cost.
- **Record types** - different business processes, page layouts, and picklist values on one object.
- **Field-level considerations** - external ID fields for upsert and integration, unique fields, and required fields.
- **Skinny tables** - a Salesforce-managed performance feature (created by support) containing frequently used fields, avoiding joins to the standard field tables. You cannot create them directly; you request them for large-volume objects.

## Large data volumes (LDV)

The area PD2 emphasises over PD1.

- **Large data volume** - objects with millions of records, where naive queries and operations become slow or hit limits.
- **Selective query** - a query whose filter uses an indexed field with a selective enough value that the optimiser can use the index. Non-selective queries on large objects time out or fail.
- **Indexes** - standard indexes on Id, Name, owner, foreign keys, and audit fields; custom indexes on External ID and unique fields; and support-created indexes for other fields.
- **The selectivity thresholds** - the query optimiser uses an index when the filter matches under a threshold share of records (roughly 10% for a standard index, 5% for a custom index, up to a cap). Filtering on a non-selective value forces a full scan.
- **Data skew** - too many child records pointing at one parent (ownership skew, lookup skew, account data skew), causing lock contention and slow sharing recalculation. Keep ownership per user under the guidance to avoid it.

## Querying at scale

- **SOQL** - retrieves records. `SELECT ... FROM ... WHERE ...`, with relationship queries traversing lookups and master-detail.
- **Parent-to-child query** - a subquery, for example `SELECT Id, (SELECT Id FROM Contacts) FROM Account`.
- **Child-to-parent query** - dot notation, `SELECT Contact.Account.Name FROM Contact`.
- **SOQL for loop** - `for (Account a : [SELECT ...])` processes records in batches of 200, keeping heap usage down for large result sets.
- **QueryLocator** - used by Batch Apex to iterate up to 50 million records, beyond the normal 50,000 query row limit.
- **Aggregate queries** - `GROUP BY`, `COUNT()`, `SUM()`, returning `AggregateResult`.
- **SOSL** - full-text search across multiple objects, better than SOQL when searching text across unknown fields or objects.
- **Selective filtering** - always filter large objects on indexed, selective fields.

SOQL searches known fields on known objects; SOSL searches text across multiple objects.
The exam asks which to use by whether the search is field-specific or text-broad.

## Data management operations

- **DML statements** - `insert`, `update`, `upsert`, `delete`, `undelete`, `merge`.
- **Database methods** - `Database.insert(records, false)` allows partial success, returning results per record rather than failing the whole operation.
- **Upsert** - insert or update based on Id or an external ID field. The standard integration pattern for idempotent data loads.
- **Bulk API** - for loading and extracting large volumes asynchronously, outside Apex transaction limits.
- **Batch Apex** - processes large volumes in chunks within the platform. Covered in the automation note.

## Exam pointers

- Master-detail enables roll-up summaries, cascade delete, and inherited sharing; lookup does not.
- A junction object has two master-detail relationships; the first defines ownership.
- On large objects, filter on selective indexed fields, or the query fails.
- Data skew (too many children on one parent) causes locking and slow sharing recalculation.
- Use the SOQL for loop and Batch Apex QueryLocator to process large result sets within heap and row limits.
- SOSL for broad text search, SOQL for targeted field queries.
- `Database.insert(records, false)` gives partial success with per-record results.

## Official documentation

**[📖 Platform Developer II exam guide](https://trailhead.salesforce.com/credentials/platformdeveloperii)** - authoritative objectives
**[📖 Query & Search Optimization Cheat Sheet](https://developer.salesforce.com/docs/atlas.en-us.salesforce_large_data_volumes_bp.meta/salesforce_large_data_volumes_bp/)** - LDV best practices
**[📖 SOQL and SOSL Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/)** - query language reference
