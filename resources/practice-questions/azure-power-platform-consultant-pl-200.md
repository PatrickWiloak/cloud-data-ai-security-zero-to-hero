---
last-updated: 2026-10-22
difficulty: intermediate
---

# Power Platform Functional Consultant Associate (PL-200) - Practice Questions

30 questions for PL-200 prep, weighted toward configuring Dataverse (25-30%) and creating model-driven apps (20-25%), then automation, integrations, and Power BI or Copilot Studio.

> **Cert page:** [exams/azure/pl-200/](../../exams/azure/pl-200/)

---

### Question 1
**Scenario:** A table must store one row per customer and many rows per order, with orders deleted when the customer is deleted.

A. A lookup column on the order table and no configured relationship behavior
B. A one-to-many relationship with Cascade All delete behavior
C. A many-to-many relationship, which uses an intersect table and cannot cascade deletes from customer to orders
D. Two unrelated tables, with orders matched to customers by a text column

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The relationship type follows the cardinality, and cascade behaviors (Cascade All, Cascade Active, Cascade User-Owned, Cascade None, Remove Link) determine what happens to children on delete, assign, share, and reparent. Choosing cascade behavior deliberately is a core Dataverse configuration skill.
</details>

---

### Question 2
**Scenario:** A choice column needs values shared across several tables and kept consistent.

A. A separate table, with the values copied by a flow into a text column on each table
B. A global choice (option set)
C. A text column
D. A local choice defined separately on each table

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Global choices are defined once and reused, so adding a value updates everywhere. Local choices duplicate the list and drift. If the values need extra attributes or frequent business-user editing, a reference table with a lookup is the better pattern, which is the nuance worth knowing.
</details>

---

### Question 3
**Scenario:** Users in a regional team should see records owned by their own business unit only.

A. Organization scope, which grants read access to every record in the environment regardless of ownership
B. User scope only
C. A security role with Business Unit scope on the read privilege
D. Column-level security

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Dataverse privilege depth runs User, Business Unit, Parent-Child Business Unit, and Organization. Setting read to Business Unit gives exactly the regional visibility described. Column security restricts fields, not rows.
</details>

---

### Question 4
**Scenario:** Two users in different business units must collaborate on one specific record.

A. Change the users' business units to the same unit, which also moves ownership of their other records
B. Share the record with the other user or team, granting specific privileges
C. Give the two users Organization-level access on the table so every record is visible to them
D. Duplicate the record

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Sharing grants access to a single record without changing the broader security model. Escalating to Organization scope solves one case by widening access to everything, which is the wrong trade. Access teams are the scalable version of the same idea.
</details>

---

### Question 5
**Scenario:** A business process flow should branch based on the value of a field.

A. Create two separate business process flows and ask users to pick the right one when they start
B. Add a condition to the business process flow to create a branch
C. Use a canvas app
D. Use a business rule on the form to hide and show the stages of the process

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Business process flows support conditional branching so a single guided process can handle variant paths. Business rules do field-level logic within a form and cannot restructure stages. Making users choose between two processes moves the decision to the wrong place.
</details>

---

### Question 6
**Scenario:** A cloud flow must process 5,000 records and complete reliably within the platform's limits.

A. Use pagination, batching and controlled concurrency, with a child flow for each item
B. Increase the flow timeout to its maximum so that the run is never cut off by the platform limits
C. Loop through all 5,000 records one at a time with no concurrency, and hope it finishes in time
D. Run it manually in small groups of 100 records at a time, and track progress in a spreadsheet

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Power Automate has request limits, pagination defaults, and per-flow run duration limits. Batching plus controlled concurrency in the Apply to each settings keeps you inside them, and a child flow isolates failures so one bad record does not fail the whole run.
</details>

---

### Question 7
**Scenario:** A flow occasionally fails because a downstream API returns a transient error.

A. Run it twice
B. Configure retry policy on the action, and add a Scope with a Configure run after path for failure handling
C. Delete the flow
D. Ignore the failures

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Retry policies handle transient errors automatically, and scopes with run-after conditions give you try, catch, and finally semantics in a flow. Without them a transient failure looks identical to a permanent one in the run history.
</details>

---

### Question 8
**Scenario:** A model-driven app should show a chart of cases by priority on the main dashboard.

A. A canvas app built separately and opened from a link on the dashboard
B. An Excel export that users refresh by hand each morning
C. A Dataverse chart added to a dashboard
D. An embedded Power BI report requiring a separate license for every viewer

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Native Dataverse charts and dashboards need no additional licensing and respect the user's security model automatically. Embedded Power BI is the right call for richer analytics across sources, but bring the licensing implication into the design conversation rather than discovering it at go-live.
</details>

---

### Question 9
**Scenario:** Data must be imported with duplicate detection so existing customers are updated rather than duplicated.

A. Configure duplicate detection rules and use an alternate key for upsert during import
B. Import and delete duplicates later
C. Import into a new table
D. Disable duplicate detection for speed and run a scheduled bulk delete job to remove duplicates afterward

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** An alternate key gives Dataverse a natural business key it can match on, which turns an import into an upsert. Duplicate detection rules catch the cases the key does not cover. Cleaning up afterward is far more expensive and leaves broken relationships behind.
</details>

---

### Question 10
**Scenario:** A consultant must document requirements before configuration begins.

A. Capture functional and non-functional requirements and success measures, then validate them
B. Ask the developers to decide what the requirements are, based on what is easiest for them to build
C. Start configuring straight away and adjust the design as feedback arrives from the business users
D. Copy the requirements document from a previous project and change only the customer name in the title

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** PL-200 is a functional consultant exam, so requirements discipline is examinable content, not preamble. Non-functional requirements (volume, performance, retention, compliance) are the ones most often skipped and the ones that most often force rework.
</details>

---

### Question 11
**Scenario:** A Copilot Studio agent should hand a conversation to a human when it cannot resolve the question.

A. End the conversation
B. Repeat the question
C. Configure escalation to a live agent through the Escalate system topic
D. Redirect to a website that shows the support phone number, without transferring the conversation

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The Escalate topic is the built-in handoff path, and it can integrate with Omnichannel or another live-agent service. Designing the escalation path is part of designing the agent: an agent with no exit produces the worst customer experience of all.
</details>

---

### Question 12
**Scenario:** A solution must be deployed through dev, test, and production using a repeatable pipeline.

A. Editing directly in production
B. One shared environment
C. Manual export and import each time
D. Managed solutions promoted through Power Platform Pipelines or Azure DevOps, with connection references and environment variables

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Pipelines make promotion repeatable and auditable, and the parameterization pieces mean the same artifact works in every environment. Editing directly in production is the anti-pattern that leaves you with no way to reproduce or roll back what is running.
</details>

---

### Question 13
**Scenario:** Users must see a form with different sections depending on their role.

A. Multiple forms with form order and security role assignment
B. One form for all users
C. Separate model-driven apps per role, each pointing at its own copy of the table
D. Hiding sections with JavaScript for everyone, based on a role check written in the form's onLoad event

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Assigning forms to security roles is the supported mechanism, and the highest-ordered form the user has access to is shown. Client script can adjust visibility but does not restrict data access, so it should never be the security control.
</details>

---

### Question 14
**Scenario:** An integration must call an external REST API that has no standard connector.

A. Use a desktop flow that drives a browser to the API's web page and scrapes the results
B. Copy the data manually
C. Store the API key in the flow
D. Build a custom connector describing the API's operations and authentication

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A custom connector wraps the API with a definition (OpenAPI or manual) plus an authentication configuration, making it reusable across apps and flows and manageable under DLP policy. Embedding credentials directly in a flow bypasses that governance.
</details>

---

### Question 15
**Scenario:** Auditing must record who changed a customer's credit limit and when.

A. Enable Application Insights
B. Rely on the modified-on field
C. Add a note field
D. Enable auditing at the environment, table, and column level for that column, then read the audit history

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Dataverse auditing must be enabled at all three levels before it records anything, which is the detail most people miss. The modified-on field tells you the last change and by whom, not the history of values. Retention for audit data is configurable and should match the compliance requirement.
</details>

---

### Question 16
**Scenario:** A nightly integration sends customer records keyed by an ERP customer number. Existing rows must be updated and new ones created, without looking up the Dataverse GUID first.

A. Make the ERP number the table's primary name column, which Dataverse uses as the row's unique key
B. Define an alternate key on the ERP customer number column and use upsert in the integration
C. Turn on duplicate detection rules for the ERP number, which update the existing row on a match
D. Create a calculated column that copies the GUID into the ERP number column for each new row

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An alternate key lets external systems identify rows by their own unique values, and upsert creates or updates in one operation based on that key. The primary name column is not a key and need not be unique. Duplicate detection warns or blocks; it does not merge or update. Calculated columns cannot drive matching for integration.
</details>

---

### Question 17
**Scenario:** Everyone with access to the employee table can see most columns, but only payroll staff may see or edit the bank account number column.

A. Enable column security on the column and grant access through a column security profile
B. Create a separate business unit for payroll and move the bank account rows into it
C. Hide the column on every form and view, which removes access through the API as well
D. Remove read privilege on the employee table from every security role except payroll's

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Column-level security restricts specific columns, and column security profiles grant read, create, or update on them to chosen users or teams. Business units scope whole rows, not columns. Hiding a column on forms is cosmetic and leaves it readable through the API and views. Removing table read would block the whole table.
</details>

---

### Question 18
**Scenario:** Sales managers must see the opportunities owned by people who report to them, at any depth in the management chain, without being given access to the whole business unit.

A. Share each opportunity with the manager manually when it is created
B. Grant managers organization-level read on opportunities in their role
C. Enable hierarchy security using the manager hierarchy
D. Add every manager to every salesperson's owner team

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Hierarchy security, based on the manager hierarchy or a position hierarchy, gives managers access to the records of their reports down the chain, without granting broader business unit access. Manual sharing does not scale. Organization-level read exposes every opportunity. Owner team membership would be a maintenance burden and also grants more than the reporting line.
</details>

---

### Question 19
**Scenario:** Membership of a Dataverse team that owns support cases should follow a Microsoft Entra security group, so adding a person to the group gives them access automatically.

A. An access team, created per case, with members added from the group on demand
B. A business unit named after the group, with members copied in each week by a flow
C. A security role assigned directly to every person who is in the group today
D. A Microsoft Entra group team linked to the security group, with a security role assigned

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A Microsoft Entra group team takes its membership from the Entra group, and the team's security role applies to members as they sign in, so access follows the group. Access teams are per-record sharing. A copying flow lags and adds work. Direct role assignment ignores later group changes.
</details>

---

### Question 20
**Scenario:** Agents on a busy case form need to add a new contact in a few seconds without leaving the case they are working on.

A. A quick create form for the contact table, opened from the lookup on the case form
B. A main form for the contact, opened in a new browser tab from the site map
C. A quick view form for the contact, which shows related data on the case form
D. A card form for the contact, which is used in the mobile app list only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Quick create forms open as a panel over the current form, collect the essentials, and return the user to their work, and they are available from the lookup. Opening the main form in another tab breaks the flow. Quick view forms are read-only displays of related data. Card forms are compact list layouts, not a creation experience.
</details>

---

### Question 21
**Scenario:** All users of a model-driven app need a new view of active high-priority cases, available in the view selector for everyone.

A. A personal view saved by the consultant, which every user then sees automatically
B. A public system view created in the solution and added to the app
C. A chart on the dashboard, which filters the default view for all users
D. An advanced find query emailed to every user with instructions to save it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Public views are created in the solution and appear to everyone with access to the table in the app. Personal views belong to their owner unless shared. Charts visualize data and do not add a view. Emailing a query relies on every user acting and produces inconsistent copies.
</details>

---

### Question 22
**Scenario:** Users want to update the status and due date of many tasks directly in a list without opening each record.

A. A business process flow with a stage for each task, so users update the rows in order
B. A quick view form on the task table, used to change the values for every row
C. The editable grid control on the view, which allows inline editing of the rows
D. A Power BI report on the tasks, with write-back enabled from the table visual

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The editable grid control turns a view or subgrid into an inline editable list. Business process flows guide one record through stages. Quick view forms are read-only. Power BI is for analysis and does not edit Dataverse rows.
</details>

---

### Question 23
**Scenario:** A cloud flow uses the Dataverse "When a row is added, modified or deleted" trigger on accounts. It should run only when the credit limit changes, but it runs on every edit.

A. Add a condition as the first action, which stops the flow before it counts as a run
B. Switch to a scheduled flow that compares every account's credit limit once an hour
C. Change the trigger scope to User, which limits it to changes made by the flow owner
D. Set the trigger's Select columns to the credit limit column, and add a row filter if needed

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The trigger's Select columns property restricts it to modifications of the listed columns, and the Filter rows property adds an OData filter, so the flow does not run for other edits. A condition still triggers and consumes a run each time. A schedule adds delay and load. Scope controls whose rows are watched (user, business unit, organization), not which columns changed.
</details>

---

### Question 24
**Scenario:** Several cloud flows in a solution need the same steps to calculate a discount, and the logic should be maintained in one place.

A. Copy the steps into each flow and keep a document listing every copy to update
B. Build the logic as a child flow in the solution and call it with the Run a Child Flow action
C. Put the steps in a desktop flow, which every cloud flow then calls through an HTTP request
D. Write the logic into a Power BI measure, which the flows then read on each run

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A child flow in the same solution encapsulates reusable logic, and parent flows call it with Run a Child Flow and receive outputs back. Copies drift. Desktop flows automate UI and are not a reuse mechanism for cloud logic. Power BI measures are not callable business logic for flows.
</details>

---

### Question 25
**Scenario:** A purchase request over a set amount must be approved by both the finance manager and the department head before it proceeds.

A. Start and wait for an approval of type "Approve/Reject - Everyone must approve" with both approvers
B. Start and wait for an approval of type "Approve/Reject - First to respond" with both approvers
C. Send two separate emails and continue the flow as soon as either one is answered
D. Create a business process flow stage with both people listed as stage owners

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** "Everyone must approve" waits for all assigned approvers and completes as rejected if any of them rejects. "First to respond" finishes with the first answer, so one approver would be enough. Emails give no tracked outcome. Business process flow stages guide users but do not collect formal approvals.
</details>

---

### Question 26
**Scenario:** A Copilot Studio agent should answer customer questions from the company's public help website without topics being written for every possible question.

A. Write one topic per help article, with the article's text pasted into a message node
B. Add the website as a knowledge source and use generative answers
C. Export the website to a Dataverse table, which the agent then searches by keyword
D. Connect a Power BI report on the help site, which the agent reads to the user

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Adding a public website as knowledge lets the agent use generative answers grounded in that content, covering questions that no topic was written for. One topic per article does not scale and goes stale. A keyword search over an export is weaker and also goes stale. Power BI reports are not a knowledge source for answers.
</details>

---

### Question 27
**Scenario:** Users need to see product inventory, which lives in an external SQL database, in model-driven forms and views without copying the data into Dataverse.

A. A nightly dataflow that loads the inventory into a Dataverse table for the forms
B. An embedded Power BI report on the form, with users updating stock through the report
C. A virtual table backed by the external data source through a data provider
D. A canvas app embedded on the form, which keeps a full copy of the database offline

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Virtual tables present external data as Dataverse tables in forms and views while the data stays in the source system, retrieved at runtime. A dataflow copies data, which the requirement excludes. Power BI is for analysis. An embedded app with an offline copy still duplicates the data.
</details>

---

### Question 28
**Scenario:** In production, makers must not build flows that send Dataverse data to personal social media or consumer storage connectors.

A. Remove the connectors from the tenant, which uninstalls them for every environment and user
B. Ask makers to sign a policy, then review each new flow by hand after it is turned on
C. Assign a security role that denies connector use to every maker in the production environment
D. A data policy that puts Dataverse in Business, consumer connectors in Non-business or Blocked

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Data policies (DLP) classify connectors as Business, Non-business, or Blocked, and an app or flow cannot combine Business and Non-business connectors, while Blocked connectors cannot be used at all. Connectors cannot be uninstalled from a tenant. Manual review is slow and after the fact. Dataverse security roles do not govern connectors.
</details>

---

### Question 29
**Scenario:** A managed solution update is imported into production, but a form change it contains does not appear because someone edited the form directly in production earlier.

A. Import the update again with overwrite selected, which deletes all customizations in production
B. Delete the managed solution and reinstall it, which keeps the direct production edits in place
C. Review the form's solution layers and remove the unmanaged active layer, then keep production edits in dev
D. Publish all customizations in production, which promotes the managed layer above the edit

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Unmanaged changes made in production sit in the active layer on top of managed layers, so they hide later managed updates. Viewing the component's solution layers and removing the active unmanaged layer lets the managed version show, and future changes belong in development. Overwriting everything is unnecessarily destructive. Deleting the solution can delete its data. Publishing does not change layer order.
</details>

---

### Question 30
**Scenario:** A Power BI dashboard should appear as a system dashboard inside a model-driven app, but the option to add Power BI dashboards is not available.

A. Enable Power BI visualization embedding in the environment's settings
B. Convert the dashboard to a Dataverse chart, since dashboards cannot be embedded
C. Rebuild the dashboard as a canvas app, then add it to the app's site map
D. Grant every user a Power Apps per app plan, which turns on embedding

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Embedding Power BI dashboards and reports in model-driven apps must be enabled in the environment settings before Power BI system dashboards can be created. Converting to Dataverse charts loses the report. A canvas app rebuild duplicates work. Power Apps licensing does not toggle this setting, and users still need Power BI access to the content.
</details>

---

## Where to go deeper

- [PL-200 cert page](../../exams/azure/pl-200/) - notes, practice plan, strategy
- [PL-100 practice questions](./azure-power-platform-app-maker-pl-100.md) - the app maker sibling
- [PL-900 practice questions](./azure-power-platform-fundamentals-pl-900.md) - the fundamentals below both
- **[📖 PL-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-200)** - official skills outline
