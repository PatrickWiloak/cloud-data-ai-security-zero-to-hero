---
last-updated: 2026-07-29
---

# CSA 02 - Lists, Forms, and Task Management

Working with records: filtering lists, configuring forms, and the task lifecycle. Heavily
represented on the exam because it is what administrators do daily.

## Lists

- **List view** - a table of records with configurable columns.
- **Condition builder** - the structured filter interface, reached via the funnel icon.
- **Breadcrumb** - the filter shown above the list. Clicking a segment removes the conditions to its right, which is the fastest way to widen a filter.
- **Personalize list (gear icon)** - changes columns for you only.
- **Configure list layout** - changes columns for everyone, and requires a role.

The personalize-versus-configure distinction is exactly the personal-versus-global pattern
the exam tests throughout.

**Filtering operators** - `is`, `is not`, `contains`, `starts with`, `is empty`,
`is one of`, and `is anything`. `AND` narrows, `OR` widens within a filter group.

- **Group by** - collapses the list into groups with counts.
- **Sorting** - click a column header; sort order is part of the saved filter.
- **Saved filter** - reusable, and shareable with a group or globally.
- **List editing** - editing values directly in the list, double-clicking a cell. Not available on all fields.
- **Search** - the search box searches the current list; the global search searches across configured tables.

**Text search operators** in the list search box include `*term` (contains) and `=term`
(exact match).

## Forms

- **Form view** - one record, with sections, fields, and related lists.
- **Form layout / Configure Form Layout** - which fields appear and in what order, for everyone.
- **Form sections** - grouping of fields, displayed as tabs or stacked.
- **Form design** - the drag-and-drop alternative to form layout.
- **Personalize form** - shows or hides fields for the current user only.
- **View** - a named form or list arrangement, so different audiences see different layouts of the same table.
- **View rule** - determines which view a user sees automatically.

**Form controls and indicators**

- **Mandatory field** - marked with a red asterisk or bar; the record cannot be saved without it.
- **Read-only field** - visible but not editable.
- **Field status indicator** - the colored bar at the left of a field showing mandatory or read-only state.
- **Save versus Update** - Save keeps you on the form; Update saves and returns you to the previous list.
- **Insert and Insert and Stay** - available from the context menu, create a *copy* as a new record.

Insert creating a copy rather than updating the original is a favorite exam point.

- **Context menu (three bars / hamburger)** - form actions including Save, Insert, Copy sys_id, Configure, and History.
- **Related list** - records related to this one, for example Affected CIs on a Change.
- **Activity stream / Activity formatter** - the chronological record of changes and journal entries.
- **Work notes versus Additional comments** - Work notes are internal to fulfillers; Additional comments are customer-visible. Choosing the wrong one leaks internal discussion to the requester.

## Task management

- **Task table** - the base table for work items. Incident, Problem, Change Request, and Catalog Task all extend it.
- **Number** - the human-readable identifier, generated from a number maintenance record per table (INC, PRB, CHG, RITM).
- **State** - the lifecycle position. Values differ by table.
- **Assignment group and Assigned to** - who owns the work. Assignment group is usually set first, then an individual.
- **Priority** - calculated from **Impact** and **Urgency** via the priority lookup rules. Priority is normally read-only because it is derived, and administrators change the lookup rules rather than the field.
- **SLA (Service Level Agreement)** - a timed commitment attached to a task, tracked by an SLA definition with start, pause, and stop conditions.
- **Approval** - a record requiring a decision before work proceeds.

**Impact + Urgency = Priority** is a reliably tested relationship.

## The core ITSM processes at CSA depth

- **Incident** - restore service as quickly as possible after an unplanned interruption. Measured on speed of restoration.
- **Problem** - find and remove the underlying cause of incidents. Measured on prevention.
- **Change** - controlled modification of the environment. Types: standard (pre-approved, low risk, from a template), normal (assessed and approved), emergency (expedited, approved retrospectively where necessary).
- **Request (Service Catalog)** - a user asking for something from the catalog, producing a Request (REQ), Requested Items (RITM), and Catalog Tasks (SCTASK).
- **Knowledge** - articles supporting self-service and fulfiller efficiency.

The incident-versus-problem distinction appears in nearly every ServiceNow exam: incidents
restore service, problems remove causes.

## Notifications

- **Notification** - an email triggered by a record event or condition.
- **Trigger types** - record inserted or updated, an event being fired, or a scheduled trigger.
- **Recipients** - users, groups, or fields on the record such as Assigned to.
- **Weight** - controls which of several matching notifications is sent, preventing duplicates.
- **Subscription** - allows users to opt in or out of certain notifications.
- **Email client** - lets fulfillers send email directly from a record, logging it against that record.

## Exam pointers

- Personalize affects you; Configure affects everyone and requires a role.
- Insert creates a copy; Update modifies the existing record.
- Work notes are internal, Additional comments are customer-visible.
- Priority is derived from Impact and Urgency. Change the lookup rules, not the field.
- The breadcrumb is the fastest way to remove filter conditions.
- Incident restores service; Problem removes the cause; Change controls modification.

## Official documentation

**[📖 Lists and filters](https://www.servicenow.com/docs/)** - list configuration reference
**[📖 Now Learning CSA path](https://nowlearning.servicenow.com/lxp/en/now-platform/certified-system-administrator)** - official curriculum
