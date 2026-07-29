---
last-updated: 2026-07-29
---

# CSA 04 - Database Administration

Tables, fields, relationships, access control, and importing data. ACL evaluation order is
the highest-yield item in the whole exam.

## Tables and fields

- **Table (`sys_db_object`)** - the definition; records live in it.
- **Dictionary (`sys_dictionary`)** - defines every field: type, length, default, and attributes.
- **Dictionary override** - changes a field's behaviour on a *child* table without altering the parent. The mechanism for making an inherited field mandatory on Incident but not on Task.
- **Label (`sys_documentation`)** - the human-readable field and table names, and how they are translated.
- **Field types** - string, integer, decimal, boolean (true/false), date, date/time, choice, reference, glide list, journal, HTML, currency, duration.
- **Auto-numbering** - configured per table in Number Maintenance, producing INC0010001 and similar.
- **Extending a table** - creating a child that inherits all parent fields.

## Relationships

- **Reference field** - one-to-many. The record stores the sys_id of the referenced record.
- **Glide List** - a list of references in one field, effectively many-to-many for simple cases.
- **Many-to-many (m2m) table** - an intermediate table with references to both sides, used for genuine many-to-many relationships.
- **Related list** - the display of related records on a form.
- **Database view** - joins tables for reporting purposes. Read-only.
- **Reference qualifier** - restricts which records a reference field may select. Simple, dynamic, or scripted.

## Access control (ACLs)

The single most-tested topic in this domain.

- **ACL (`sys_security_acl`)** - a rule granting access to an object, evaluated on operation.
- **Operations** - create, read, write, delete, and for some objects execute.
- **Levels** - table-level (`table.None` is the table itself) and field-level (`table.field`). A wildcard `*` covers all tables or all fields.
- **ACL components** - required roles, a condition, and a script. All three must pass, plus the user must hold at least one required role.

**Evaluation order, most specific first**

1. Field-level ACL matching the exact table and field (`incident.short_description`)
2. Field-level wildcard on the table (`incident.*`)
3. Table-level ACL for the table (`incident.None`)
4. Then up the inheritance chain to the parent table (`task.*`, `task.None`)
5. Finally the global wildcard (`*.*`, `*.None`)

**The rule that decides most ACL questions:** the user must pass **both** the field-level
and the table-level ACL. Access is granted only if all applicable levels grant it. Granting
at one level does not override a denial at another.

Within a single ACL, the role check, condition, and script must **all** evaluate true.

- **admin override** - the admin role bypasses most ACLs, which is why testing access as an admin proves nothing. Use impersonation.
- **security_admin** - required, and must be elevated in the session, to create or modify ACLs.
- **Debug Security Rules** - the diagnostic tool showing which ACL granted or denied access.

## Other access mechanisms

- **Query business rule** - adds a condition to every query on a table, filtering out records a user should not see. This is the standard mechanism for row-level restriction, and it differs from an ACL in that the records simply never appear.
- **Before query business rule** versus ACL: a query rule filters the result set; an ACL denies access to a record the user asked for. Both are used, for different effects.
- **User criteria** - controls access to knowledge bases and catalogs. Not ACLs.
- **Domain separation** - partitions data and process for multiple business units or customers in one instance. An advanced feature, mentioned rather than examined deeply at CSA level.

## Importing data

The import pipeline is a standard exam sequence.

1. **Data source** - defines where data comes from: a file (CSV, Excel, XML), JDBC, or an attachment.
2. **Import set table** - a staging table that receives the raw rows. Never the final destination.
3. **Transform map** - maps import set columns to target table fields.
4. **Field maps** - the individual column-to-field mappings.
5. **Coalesce field** - the matching key. If a record with a matching coalesce value exists, it is **updated**; if not, a new record is **inserted**. Coalescing on nothing means every run inserts duplicates.
6. **Transform** - runs the map and writes to the target table.

- **Transform script (onBefore, onAfter, onStart, onComplete)** - script hooks in the transform process.
- **Import set row states** - inserted, updated, ignored, error.
- **Scheduled import** - runs a data source and transform automatically.

Coalescing is the concept most often tested here: it is what prevents duplicate records on
repeated imports.

## CMDB basics

- **CMDB (Configuration Management Database)** - the record of configuration items and their relationships.
- **Configuration item (CI)** - anything managed: server, application, database, service.
- **CI relationships** - typed connections such as "Runs on" and "Depends on", producing the dependency map.
- **CI class hierarchy** - `cmdb_ci` extended by more specific classes.
- **Discovery and Service Mapping** - populate the CMDB automatically. Licensed separately, and outside CSA depth.
- **CMDB health** - completeness, correctness, and compliance metrics.

## System administration utilities

- **System Definition** - where tables, dictionary, business rules, and scheduled jobs live.
- **System Diagnostics** - logs, stats, and transaction analysis.
- **Table cleaner** - scheduled deletion of aged records from specified tables.
- **System Clone** - copies production data to a sub-production instance, with exclusion and preservation rules.

## Exam pointers

- Learn the ACL evaluation order and the rule that field-level and table-level ACLs must *both* grant access.
- All parts of a single ACL (role, condition, script) must pass.
- Test access by impersonating a user, because admin bypasses ACLs.
- `security_admin` must be elevated to edit ACLs.
- Coalesce determines insert versus update on import.
- Import sets are staging tables; data is transformed into the target table.
- Dictionary overrides change inherited field behaviour on a child table only.
- Query business rules filter what a user can see; ACLs deny access to what they request.

## Official documentation

**[📖 Access control rules](https://www.servicenow.com/docs/)** - ACL structure and evaluation
**[📖 Import sets and transform maps](https://www.servicenow.com/docs/)** - the import pipeline
**[📖 Now Learning CSA path](https://nowlearning.servicenow.com/lxp/en/now-platform/certified-system-administrator)** - official curriculum
