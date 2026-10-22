---
last-updated: 2026-10-22
difficulty: intermediate
---

# ServiceNow Certified System Administrator (CSA) - Practice Questions

30 questions across the CSA areas: the Now Platform and user interface, lists and forms, tables and the CMDB, access control, workflow and flow automation, notifications, reporting, and platform administration.

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

### Question 16
**Scenario:** An administrator changed roles for a service desk user and needs to confirm exactly which modules, records, and fields that user now sees, without asking for the user's password.

A. Impersonate the user from the user menu
B. Temporarily give the administrator the same roles
C. Export the user's roles to a spreadsheet and review them
D. Reset the user's password and log in as them

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Impersonation lets an administrator see the instance as that user, with the same roles, menus, and access, which is the standard way to test security changes. Actions taken while impersonating are recorded as that user, so test carefully. Giving yourself the roles does not remove your admin access, a role list does not show effective visibility, and resetting a password is disruptive and unnecessary.

**Key Concept:** [Impersonating Users](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/users-and-groups/concept/c_ImpersonateAUser.html)
</details>

---

### Question 17
**Scenario:** Agents viewing an Incident form want to see the incident's child incidents and affected CIs listed below the form fields, without leaving the record.

A. Add a reference field for each related record to the form
B. Create a report and embed its link in the short description
C. Configure the form's related lists to include those relationships
D. Add a client script that opens each related record in a new tab

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Related lists appear at the bottom of a form and show records related to the current one, such as child incidents or affected CIs, and are added through the form's related list configuration. A reference field points to one record, not a list. A report link and a script that opens tabs are both workarounds that take agents away from the form.

**Key Concept:** [Forms in the Classic Environment](https://www.servicenow.com/docs/bundle/zurich-platform-user-interface/page/use/using-forms/concept/c_UsingForms.html)
</details>

---

### Question 18
**Scenario:** An agent wants to move a few fields on the Incident form for their own view only. The admin wants to add a new field to the form for every user.

A. Both use the same personalize option, which applies the change to every user of the form
B. Both must ask a developer to edit the form's HTML template
C. The agent edits the dictionary entry; the admin uses personalize
D. The agent personalizes their own view; the admin configures the form layout

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Personalizing a form changes only the current user's view, while configuring the form layout (or using Form Builder) changes the form for everyone who uses that view. Personalization never applies to all users. Forms are configured, not edited as HTML, and dictionary entries define fields rather than where they appear on a form.

**Key Concept:** [Forms in the Classic Environment](https://www.servicenow.com/docs/bundle/zurich-platform-user-interface/page/use/using-forms/concept/c_UsingForms.html)
</details>

---

### Question 19
**Scenario:** When an agent clicks Submit on a Change form, the browser must check that the planned end date is after the start date and stop the save with a message if not.

A. An onLoad client script that hides the date fields
B. An onSubmit client script that returns false when the check fails
C. An onChange client script on the Short description field
D. A scheduled job that checks the dates on every change record each night

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An onSubmit client script runs when the form is submitted, and returning false cancels the submission so the user can fix the dates. onLoad runs only when the form opens, and an onChange script on an unrelated field never sees the submit. A nightly job finds bad data after it has been saved. Server-side checks (such as a business rule) are still wise for saves that do not come through the form.

**Key Concept:** [Client Scripts](https://www.servicenow.com/docs/bundle/zurich-api-reference/page/script/client-scripts/concept/client-scripts.html)
</details>

---

### Question 20
**Scenario:** On the Incident form, when the Category field changes to Network, the Subcategory field should immediately be cleared and the user shown a message, before saving.

A. A before business rule on the Incident table
B. An ACL on the Subcategory field
C. A scheduled data import into the Incident table
D. An onChange client script on the Category field

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** An onChange client script runs in the browser when a specific field's value changes, so it can clear another field and show a message right away. A business rule runs on the server when the record is saved, which is too late for this. ACLs control access, not field behavior, and imports have nothing to do with live form changes.

**Key Concept:** [Client Scripts](https://www.servicenow.com/docs/bundle/zurich-api-reference/page/script/client-scripts/concept/client-scripts.html)
</details>

---

### Question 21
**Scenario:** Every time a Priority 1 incident is created, the major incident team must be notified and a set of follow-up tasks created, without writing scripts.

A. A scheduled job that queries for P1 incidents every hour
B. A flow with a record-created trigger and a P1 condition
C. A UI policy that shows the tasks section on P1 incidents
D. A related list of tasks added to the incident form

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A flow with a record trigger runs when a record is created (or updated) and its conditions match, and its actions can send notifications and create tasks without code. An hourly job delays the response and needs scripting. UI policies and related lists change how a form looks but take no action.

**Key Concept:** [Flow Trigger Types](https://www.servicenow.com/docs/bundle/zurich-build-workflows/page/administer/flow-designer/reference/flow-triggers.html)
</details>

---

### Question 22
**Scenario:** Every weekday morning, a summary of open high-priority incidents must be compiled and emailed to the service desk manager by a no-code automation.

A. A record-updated trigger on the Incident table
B. An inbound email trigger on the manager's mailbox
C. A flow with a scheduled trigger that looks up the incidents
D. An onLoad client script on the Incident list

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A scheduled trigger starts a flow at set times, and the flow then looks up the records it needs and sends the email. A record-updated trigger fires on individual changes, not on a schedule. An inbound email trigger reacts to received mail, and client scripts run in a user's browser only when someone opens the list.

**Key Concept:** [Flow Trigger Types](https://www.servicenow.com/docs/bundle/zurich-build-workflows/page/administer/flow-designer/reference/flow-triggers.html)
</details>

---

### Question 23
**Scenario:** An administrator creates a new custom table to track equipment loans and wants users to reach its list from the application navigator straight away.

A. Choose the option to create a module when creating the table
B. Add the table name to a user's favorites by hand for each user
C. Create a UI policy on the table to make it visible
D. Import an empty spreadsheet to register the table

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** When creating a table, the administrator can have the platform create an application menu and module for it, so its list appears in the navigator for users with the right roles. Adding favorites one user at a time does not scale. UI policies control form fields, and an import is not how tables are registered.

**Key Concept:** [Table Administration](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/table-administration/concept/c_TableAdministration.html)
</details>

---

### Question 24
**Scenario:** The Assignment group field must be mandatory on incidents whether they are created on a form, through an import set, or through a web service.

A. A UI policy that makes the field mandatory on the form
B. An onSubmit client script that checks the field
C. A data policy that makes the field mandatory
D. Marking the field as required in the form layout

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Data policies enforce mandatory and read-only rules on the data itself, and can apply to import sets and web services as well as forms. UI policies and client scripts run only in the browser on forms, so imports and integrations bypass them. Form layout controls where fields appear, not whether every channel must fill them.

**Key Concept:** [Data Policies](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/field-administration/concept/c_DataPolicy.html)
</details>

---

### Question 25
**Scenario:** An administrator built a custom Asset Request table and later wants two new tables to extend it and inherit its fields, but the option to extend it is not offered.

A. The table must first be added to the CMDB as a CI class
B. The table's Extensible option was not selected in its definition
C. Only tables in the global scope can ever be extended
D. Tables can only extend the Task table, not custom tables

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A table can be used as a parent only if it is marked extensible in its table definition. Custom tables do not have to be CI classes to be extended, scoped applications can contain extensible tables, and any extensible table, not only Task, can be a parent.

**Key Concept:** [Table Administration](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/table-administration/concept/c_TableAdministration.html)
</details>

---

### Question 26
**Scenario:** A report must show incidents together with fields from their SLA records, which live in a separate table that references Incident.

A. Two separate reports placed side by side on a dashboard
B. A new field on Incident copied from the SLA record by a business rule script
C. A list export of each table merged in a spreadsheet
D. A database view joining the two tables, used as the report source

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A database view joins tables into a read-only virtual table that reports can use as their source, so fields from both appear in one report. Two side-by-side reports cannot combine rows. Copying fields by script duplicates data, and spreadsheet merges are manual and stale immediately.

**Key Concept:** [Work with Database Views](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/use/reporting/concept/c_DatabaseViews.html)
</details>

---

### Question 27
**Scenario:** The IT director wants the "Open incidents by assignment group" report delivered to her inbox every Monday at 8 AM, without logging in.

A. Schedule the report to be emailed on a weekly schedule
B. Share the report with her and ask her to open it on Mondays
C. Create a notification on the Incident table for every update
D. Add the report to a dashboard and set it as her homepage

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A scheduled report runs at the chosen time and emails the result to the recipients, which meets the requirement without logging in. Sharing or a dashboard still requires her to log in and look. A notification on every incident update would flood her inbox with individual records, not a report.

**Key Concept:** [Schedule Emails of Core UI Reports](https://www.servicenow.com/docs/bundle/zurich-now-intelligence/page/use/reporting/task/t_ScheduleAReport.html)
</details>

---

### Question 28
**Scenario:** An agent needs to record troubleshooting steps on an incident that the caller should not see, and separately send the caller an update.

A. Put both in the Short description field, separated by a line
B. Use Additional comments for the internal notes and Work notes for the caller
C. Use Work notes for the internal notes and Additional comments for the caller
D. Put internal notes in an attachment and email the caller directly

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Work notes are internal and visible only to fulfillers, while additional comments are customer-visible and can be sent to the caller. Swapping them would expose internal notes to the caller. The short description is a summary field, and attachments plus outside email lose the record's activity history.

**Key Concept:** [Forms in the Classic Environment](https://www.servicenow.com/docs/bundle/zurich-platform-user-interface/page/use/using-forms/concept/c_UsingForms.html)
</details>

---

### Question 29
**Scenario:** Employees must report a broken printer from the service portal using a simple guided form, and the submission should create an Incident record rather than a request.

A. A catalog item with a cart and a fulfillment workflow
B. A record producer that creates records in the Incident table
C. A knowledge article with a link to the Incident form
D. An order guide that bundles several catalog items into one request

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A record producer is a catalog item that creates a task-based record, such as an incident, from a portal form. A standard catalog item creates a request and requested item, not an incident. A knowledge article link sends users to the raw form, and an order guide bundles multiple items into one request.

**Key Concept:** [Record Producer](https://www.servicenow.com/docs/bundle/zurich-servicenow-platform/page/product/service-catalog-management/concept/c_RecordProducer.html)
</details>

---

### Question 30
**Scenario:** When an employee orders a "New Laptop" catalog item, approval and fulfillment tasks must start automatically for that requested item.

A. Associate a flow that uses a Service Catalog trigger with the catalog item
B. Add a scheduled flow that scans all requested items every night for new laptop orders
C. Create a UI policy on the catalog item's variables
D. Attach a report of open requested items to the catalog item

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Flows built with the Service Catalog trigger are associated with a catalog item and run for each requested item, handling approvals and fulfillment tasks. A nightly scan delays every order. UI policies only change variable behavior on the order form, and a report takes no action.

**Key Concept:** [Flow Trigger Types](https://www.servicenow.com/docs/bundle/zurich-build-workflows/page/administer/flow-designer/reference/flow-triggers.html)
</details>

---

## Where to go deeper

- [CSA cert page](../../exams/servicenow/csa/) - notes, practice plan, strategy
- [Salesforce Administrator practice questions](./salesforce-administrator.md) - a comparable platform-admin credential
- [IAM explained](https://security.noblerworks.com/learn/concepts/iam-explained/) - roles, groups, and access in plain English
- **[📖 ServiceNow certification](https://www.servicenow.com/services/training-and-certification.html)** - official exam blueprint
