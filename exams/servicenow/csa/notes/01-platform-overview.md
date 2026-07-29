---
last-updated: 2026-07-29
---

# CSA 01 - Now Platform Overview

Architecture, instances, releases, navigation, and the user and role model. Everything
later in the exam assumes this vocabulary.

## What ServiceNow is

- **Now Platform** - a multi-instance PaaS on which ITSM, ITOM, HR, CSM, and custom applications are built. Everything is an application on one platform, sharing one data model.
- **Instance** - a dedicated application server and database for one customer, reached at `<name>.service-now.com`. Multi-instance, not multi-tenant: your configuration and data are isolated in your own database schema.
- **Sub-production instances** - Dev, Test, UAT, Sandbox. Development happens here, never in production.
- **Production instance** - the live system.
- **Family / release** - named after cities in alphabetical order, roughly two major releases a year. Upgrades apply the new base system while attempting to preserve customisations.
- **Patch and hotfix** - smaller fixes between family releases.
- **Personal Developer Instance (PDI)** - a free instance for learning. The single most useful study resource for this exam.

## Navigation and the user interface

- **Next Experience UI** - the current interface, replacing the older UI16 frame.
- **All / Application navigator** - the left-hand menu of applications and modules, filterable by typing.
- **Application** - a grouping of functionality, for example Incident.
- **Module** - an item within an application that opens a page, for example "Create New" or "Open".
- **Favorites and history** - quick access to frequently used and recently visited records.
- **Unified Navigation and workspaces** - configurable agent-facing interfaces.
- **List view** - many records.
- **Form view** - one record.
- **Related lists** - records related to the current record, displayed beneath the form.

**Navigation shortcuts worth knowing**

- `<table>.list` in the navigator filter opens a table's list view, for example `incident.list`.
- `<table>.form` opens a new record form.
- `sys_user.list` is the users table; `sys_user_group.list` is groups.

## Data model fundamentals

- **Table** - stores records. Named with a prefix and underscore, for example `sys_user`, `task`, `incident`.
- **Record** - a row.
- **Field (column)** - an attribute. Each has a type: string, integer, reference, choice, date/time, true/false, journal.
- **Sys_id** - the 32-character unique identifier for every record on the platform. It is how records are referenced internally, and it never changes.
- **Reference field** - a pointer to a record in another table, stored as that record's sys_id.
- **Dot-walking** - traversing a reference to reach fields on the referenced record, for example `caller_id.department.name`. Only possible through reference fields.
- **Choice field** - a constrained list of values.
- **Journal field** - append-only entries such as Work notes and Additional comments.

## Table inheritance

The concept the fact-sheet tells you to memorise.

- **Base table** - a parent whose fields are inherited by children.
- **Extended table** - inherits all fields of its parent and adds its own.
- **Task table** - the central base table. Incident, Problem, Change Request, and Catalog Task all extend Task, which is why they share fields such as Number, Short description, Assigned to, State, and Priority.
- **Configuration Item (cmdb_ci)** - the base table of the CMDB, extended by server, database, application, and so on.

Consequences that get tested: a field added to Task appears on every child table, a
business rule on Task runs for records in every child table, and a query against Task
returns Incidents, Problems, and Changes together.

## Users, groups, and roles

- **User (`sys_user`)** - an individual account.
- **Group (`sys_user_group`)** - a collection of users, typically for assignment and notification.
- **Role (`sys_user_role`)** - a set of permissions. Roles are granted to users or, better, to groups.
- **Role inheritance** - a role can contain other roles, and a user receives all contained roles.
- **Best practice** - assign roles to groups and users to groups, rather than roles directly to users. It scales and it is auditable.

**Key roles**

- **admin** - full access, including the ability to bypass most ACLs. Should be tightly limited.
- **itil** - the standard fulfiller role for ITSM records.
- **approver_user** - can approve requests.
- **catalog_admin** - manages the service catalog.
- **security_admin** - required to modify high-security settings including ACLs. Elevated separately.
- **No role** - self-service users, who can raise and view their own requests only.

**Impersonation** - an administrator can impersonate another user to see the platform as
they see it. The activity is logged. It is the correct way to test access, rather than
reasoning about it abstractly.

**Elevated privilege** - `security_admin` must be explicitly elevated for the session
before ACLs can be edited, even by an admin.

## Applications and scope

- **Global scope** - the default scope where the base system lives.
- **Scoped application** - a namespaced application with its own tables and restricted access to other scopes' data, protecting the platform from unintended interference.
- **Application scope selector** - determines which scope new artefacts are created in. Creating something in the wrong scope is a common beginner mistake.

## Instance administration basics

- **System Properties** - instance-wide configuration values, in `sys_properties`.
- **Plugins** - optional functionality activated per instance. Some cannot be deactivated once active, which is why they are activated on sub-production first.
- **Update sets** - the mechanism for moving configuration between instances. Covered in the configuration note.
- **System logs** - platform activity, in `syslog` and related tables.
- **Instance upgrade** - the ServiceNow-run process of applying a new family release, with skipped-changes review for customised records.

## Exam pointers

- Task is the parent of Incident, Problem, and Change. Fields and business rules on Task apply to all of them.
- Sys_id uniquely identifies every record on the platform.
- Assign roles to groups, and users to groups. Direct role assignment to users is the discouraged pattern.
- Impersonation is the correct method for testing what another user can see.
- `security_admin` must be elevated before ACLs can be changed.
- Dot-walking only works through reference fields.

## Official documentation

**[📖 Now Learning CSA path](https://nowlearning.servicenow.com/lxp/en/now-platform/certified-system-administrator)** - the official curriculum
**[📖 ServiceNow product documentation](https://www.servicenow.com/docs/)** - platform reference
**[📖 Personal Developer Instance](https://developer.servicenow.com/dev.do)** - free practice instance
