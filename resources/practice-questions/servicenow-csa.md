---
last-updated: 2026-08-09
difficulty: intermediate
---

# ServiceNow Certified System Administrator (CSA) - Practice Questions

15 questions across the CSA areas: the Now Platform and user interface, lists and forms, tables and the CMDB, access control, workflow and flow automation, notifications, reporting, and platform administration.

> **Cert page:** [exams/servicenow/csa/](../../exams/servicenow/csa/)

---

### Question 1
**Scenario:** How are tables related in ServiceNow to enable inheritance?

A. Table extension, where a child table extends a parent and inherits its fields, as Incident extends Task
B. Foreign keys only, where each table stores a reference field to a parent record and copies the parent values into its own columns
C. Through the CMDB only, because only configuration item tables are allowed to share fields with another table
D. They are always independent, and shared fields are kept in sync by a scheduled job

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Task table is the classic parent: Incident, Problem, and Change all extend it and inherit fields such as number, state, and assignment group. Understanding extension explains why a field added to Task appears on all of them.
</details>

---

### Question 2
**Scenario:** A field must appear on a form only when a certain condition is met.

A. An ACL on the field, which hides it from users who lack the required role and so removes it from the form
B. Edit the table dictionary so the field is removed from the table and only added back when the condition is met
C. A UI policy, which shows, hides, makes mandatory, or makes read-only fields based on conditions, running in the client
D. A business rule set to run on display, which queries the record and passes a flag to the form so the field is shown only when the condition is met

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** UI policies are the declarative, client-side way to control form behavior and are preferred over client scripts for these cases. Business rules run server-side and are the wrong tool for changing how a field displays.
</details>

---

### Question 3
**Scenario:** Data must be validated or modified when a record is saved, regardless of how it was saved.

A. A UI action, which is a button or context menu item that runs a script when a user clicks it on the form or list
B. A business rule, which runs server-side on database operations, so imports and API writes are covered too
C. A UI policy, which can make a field mandatory or read-only whenever the form loads or a value changes in the browser
D. A client script on onSubmit that validates values before saving

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Client-side logic only fires in the form, so an import or API write bypasses it entirely. Server-side business rules are the enforcement point when the rule must hold for every path that touches the record.
</details>

---

### Question 4
**Scenario:** Which controls whether a user can read or write a specific field on a table?

A. A role alone, since any holder can read and write every field in the table
B. Access control rules (ACLs), evaluated by object and operation, combining roles and conditions and script
C. A business rule that runs on query and strips the field for some users
D. A UI policy

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ACLs are the security enforcement layer, and a UI policy that hides a field is cosmetic rather than secure. Field-level ACLs are evaluated most-specific first, and a user needs to pass both the table and the field ACL to gain access.
</details>

---

### Question 5
**Scenario:** How is access typically granted to users in ServiceNow?

A. Directly per user, by editing each user record and adding the required roles one person at a time as they join
B. Through UI policies that show or hide modules depending on who is logged in at the moment
C. Per record only, by adding each user to a list on the record they need to open
D. Roles assigned to groups, with users placed in groups, so access is managed by group membership

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The group-based model scales: change a group's roles once rather than editing every user. Assigning roles directly to users is possible but becomes unmanageable and obscures who has what, which is the anti-pattern the exam probes.
</details>

---

### Question 6
**Scenario:** A multi-step approval and task process must be automated.

A. A chain of business rules, each one firing when the previous rule updates a field on the record
B. A report scheduled to run every hour that emails the list of pending approvals to the managers involved, who reply by email to approve
C. Flow Designer, the current low-code automation tool for building flows with triggers, conditions, and actions
D. Manual emails sent by the requester, with replies copied into the work notes by hand each time

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Flow Designer is the modern replacement for legacy Workflow, using reusable actions and subflows. Building approvals and task orchestration here rather than in scripted workflows is the direction ServiceNow has taken.
</details>

---

### Question 7
**Scenario:** A user should receive an email when an incident is assigned to their group.

A. A notification, triggered by the record condition, with a recipient and a template
B. A UI action added to the incident form that sends a message when the assigned person clicks it
C. A scheduled report subscription that mails a list of new incidents to the group each morning
D. A business rule that calls gs.eventQueue or sends mail directly, which skips the notification framework controls

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Notifications are the declarative mechanism, with conditions, recipients, and content in one place that administrators can maintain. Sending email from a business rule is possible but scatters the logic and bypasses the notification framework's controls.
</details>

---

### Question 8
**Scenario:** What is the CMDB in ServiceNow?

A. A user directory that stores people, groups, and their roles so that access can be granted by group
B. The Configuration Management Database, which stores configuration items and relationships
C. A reporting tool that builds charts and dashboards from any table and shares them with stakeholders
D. A notification engine that sends email and SMS messages when records meet a given condition, and also stores each recipient and template

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The CMDB models the IT environment as CIs and relationships, which is what lets change management assess impact and incident management find affected services. CI class tables extend the base cmdb_ci table, reusing the same inheritance model.
</details>

---

### Question 9
**Scenario:** Records must be brought in from an external source on a schedule.

A. A report scheduled on the target table that pulls the data in from the source system each night
B. Manual entry by an administrator, repeated whenever the source changes
C. A business rule on the target table that fetches the rows from the source system on every insert into the table
D. An import set with a transform map, run through a scheduled data import or integration

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The import set is a staging table; the transform map defines how staged rows map to the target table, including coalesce fields that decide insert versus update. Coalescing on the wrong field is what produces duplicate records.
</details>

---

### Question 10
**Scenario:** An administrator must find records matching complex criteria and act on many at once.

A. A filtered list view, then a list edit or a bulk action such as update selected
B. Open each record one at a time and edit it, repeating the same change on every match in turn
C. A single record form, where the fields are edited once and the change is applied to the whole table
D. A notification set up to email the administrator a list of matching records after each update

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The condition builder plus list actions is the day-to-day administrative workflow. Understanding the breadcrumb filter and dot-walking to related fields in conditions is what makes the list view powerful rather than just a table dump.
</details>

---

### Question 11
**Scenario:** A report must show incident volume by category over time.

A. A business rule that counts incidents by category each time one is inserted and stores the total
B. Export the table to a spreadsheet and build a pivot chart there, refreshing it by hand each week
C. A notification that emails the count of incidents per category to the service desk manager
D. A report on the incident table, grouped by category, optionally on a dashboard

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Reports are built on tables and their fields, so a clean data model and consistent categorization are what make reporting meaningful. Dashboards assemble reports and other widgets into a single operational view.
</details>

---

### Question 12
**Scenario:** Changes are being developed and must move between instances safely.

A. Capture changes in an update set in a sub-production instance, then move the update set to production after testing
B. Edit production directly, since the change is small and the instance can always be rolled back
C. Copy the changed records manually from the sub-production instance into production, one table at a time, once the testing is done
D. A data import of the configuration tables, loaded through an import set into the production instance

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Update sets carry configuration changes between instances, but not data. Changes made in the wrong scope or outside the current update set are the classic reason something works in test but is missing after promotion.
</details>

---

### Question 13
**Scenario:** What distinguishes application scope from the global scope?

A. Global is more restricted, since every table and script in it is private and no other scope can read it
B. Scoped applications are isolated with their own namespace and restricted cross-scope access, which protects them and the rest of the platform
C. Scope only affects reporting, because it decides which tables show up in the report builder and on which dashboards they can be used
D. Nothing, since scoped applications and global share one namespace and every script can reach every table

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Scoping prevents one application's code and tables from unintentionally affecting another's. Cross-scope access must be explicitly granted, which is why a script failing to reach a table is often a scope boundary rather than an ACL.
</details>

---

### Question 14
**Scenario:** A user reports they cannot see a module in the application navigator.

A. The module is broken, and the platform needs to be restarted so that the navigator can rebuild it
B. Reinstall the application to reset the module defaults
C. Check the module's and application's role requirements against the user's roles
D. Clear the database cache and truncate the sys_app_module table so that the navigator rebuilds the list of modules from scratch

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Navigator modules are commonly role-gated, so visibility is usually an access question rather than a fault. Impersonating the user is the fast way to confirm what they actually see, which is a standard administrative technique.
</details>

---

### Question 15
**Scenario:** Which best describes an SLA in ServiceNow?

A. A dashboard that shows the current ticket counts and ageing for each support group at a glance
B. A report that lists every incident resolved after its target date, grouped by assignment group, so that managers can review the late ones
C. A service level agreement definition that attaches to records, tracking elapsed time against a target with conditions to start, pause, and stop
D. A notification that emails the assignee when a task is due, with a fixed reminder schedule

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** SLA definitions measure against targets and drive escalation, and the start, pause, and stop conditions are what make the measurement accurate. A pause condition for on-hold states is what stops customer wait time counting against the support team unfairly.
</details>

---

## Where to go deeper

- [CSA cert page](../../exams/servicenow/csa/) - notes, practice plan, strategy
- [Salesforce Administrator practice questions](./salesforce-administrator.md) - a comparable platform-admin credential
- [IAM explained](https://security.noblerworks.com/learn/concepts/iam-explained/) - roles, groups, and access in plain English
- **[📖 ServiceNow certification](https://www.servicenow.com/services/training-and-certification.html)** - official exam blueprint
