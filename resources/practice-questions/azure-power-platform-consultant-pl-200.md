---
last-updated: 2026-08-09
difficulty: intermediate
---

# Power Platform Functional Consultant Associate (PL-200) - Practice Questions

15 questions for PL-200 prep, weighted toward configuring Dataverse (25-30%) and creating model-driven apps (20-25%), then automation, integrations, and Power BI or Copilot Studio.

> **Cert page:** [exams/azure/pl-200/](../../exams/azure/pl-200/)

---

### Question 1
**Scenario:** A table must store one row per customer and many rows per order, with orders deleted when the customer is deleted.

A. A one-to-many relationship with a cascade delete behavior of Cascade All
B. A many-to-many relationship
C. Two unrelated tables
D. A lookup column with no relationship

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The relationship type follows the cardinality, and cascade behaviors (Cascade All, Cascade Active, Cascade User-Owned, Cascade None, Remove Link) determine what happens to children on delete, assign, share, and reparent. Choosing cascade behavior deliberately is a core Dataverse configuration skill.
</details>

---

### Question 2
**Scenario:** A choice column needs values shared across several tables and kept consistent.

A. A global choice (option set)
B. A local choice on each table
C. A text column
D. A separate table with a lookup

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Global choices are defined once and reused, so adding a value updates everywhere. Local choices duplicate the list and drift. If the values need extra attributes or frequent business-user editing, a reference table with a lookup is the better pattern, which is the nuance worth knowing.
</details>

---

### Question 3
**Scenario:** Users in a regional team should see records owned by their own business unit only.

A. A security role with Business Unit scope on the read privilege
B. Organization scope
C. User scope only
D. Column-level security

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Dataverse privilege depth runs User, Business Unit, Parent-Child Business Unit, and Organization. Setting read to Business Unit gives exactly the regional visibility described. Column security restricts fields, not rows.
</details>

---

### Question 4
**Scenario:** Two users in different business units must collaborate on one specific record.

A. Change both users' business units
B. Share the record with the other user or team, granting specific privileges
C. Give both Organization-level access
D. Duplicate the record

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Sharing grants access to a single record without changing the broader security model. Escalating to Organization scope solves one case by widening access to everything, which is the wrong trade. Access teams are the scalable version of the same idea.
</details>

---

### Question 5
**Scenario:** A business process flow should branch based on the value of a field.

A. Add a condition to the business process flow to create a branch
B. Create two separate flows and ask users to pick
C. Use a business rule
D. Use a canvas app

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Business process flows support conditional branching so a single guided process can handle variant paths. Business rules do field-level logic within a form and cannot restructure stages. Making users choose between two processes moves the decision to the wrong place.
</details>

---

### Question 6
**Scenario:** A cloud flow must process 5,000 records and complete reliably within the platform's limits.

A. Loop sequentially with no concurrency
B. Use pagination, batching, and controlled concurrency, and consider a child flow to isolate the per-item work
C. Increase the timeout indefinitely
D. Run it manually

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Power Automate has request limits, pagination defaults, and per-flow run duration limits. Batching plus controlled concurrency in the Apply to each settings keeps you inside them, and a child flow isolates failures so one bad record does not fail the whole run.
</details>

---

### Question 7
**Scenario:** A flow occasionally fails because a downstream API returns a transient error.

A. Configure retry policy on the action, and add a Scope with a Configure run after path for failure handling
B. Delete the flow
C. Run it twice
D. Ignore the failures

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Retry policies handle transient errors automatically, and scopes with run-after conditions give you try, catch, and finally semantics in a flow. Without them a transient failure looks identical to a permanent one in the run history.
</details>

---

### Question 8
**Scenario:** A model-driven app should show a chart of cases by priority on the main dashboard.

A. A Dataverse chart added to a dashboard
B. An embedded Power BI report requiring a separate license for every viewer
C. A canvas app
D. An Excel export

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Native Dataverse charts and dashboards need no additional licensing and respect the user's security model automatically. Embedded Power BI is the right call for richer analytics across sources, but bring the licensing implication into the design conversation rather than discovering it at go-live.
</details>

---

### Question 9
**Scenario:** Data must be imported with duplicate detection so existing customers are updated rather than duplicated.

A. Configure duplicate detection rules and use an alternate key for upsert during import
B. Import and delete duplicates later
C. Disable duplicate detection for speed
D. Import into a new table

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** An alternate key gives Dataverse a natural business key it can match on, which turns an import into an upsert. Duplicate detection rules catch the cases the key does not cover. Cleaning up afterward is far more expensive and leaves broken relationships behind.
</details>

---

### Question 10
**Scenario:** A consultant must document requirements before configuration begins.

A. Capture functional and non-functional requirements, process maps, data model, and success measures, then validate them with stakeholders
B. Start configuring and adjust as feedback arrives
C. Copy a previous project's document
D. Ask developers to decide

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** PL-200 is a functional consultant exam, so requirements discipline is examinable content, not preamble. Non-functional requirements (volume, performance, retention, compliance) are the ones most often skipped and the ones that most often force rework.
</details>

---

### Question 11
**Scenario:** A Copilot Studio agent should hand a conversation to a human when it cannot resolve the question.

A. Configure escalation to a live agent through the Escalate system topic
B. End the conversation
C. Repeat the question
D. Redirect to a website

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Escalate topic is the built-in handoff path, and it can integrate with Omnichannel or another live-agent service. Designing the escalation path is part of designing the agent: an agent with no exit produces the worst customer experience of all.
</details>

---

### Question 12
**Scenario:** A solution must be deployed through dev, test, and production using a repeatable pipeline.

A. Managed solutions promoted through Power Platform Pipelines or Azure DevOps, with connection references and environment variables
B. Manual export and import each time
C. Editing directly in production
D. One shared environment

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Pipelines make promotion repeatable and auditable, and the parameterization pieces mean the same artifact works in every environment. Editing directly in production is the anti-pattern that leaves you with no way to reproduce or roll back what is running.
</details>

---

### Question 13
**Scenario:** Users must see a form with different sections depending on their role.

A. Multiple forms with form order and security role assignment
B. Hiding sections with JavaScript for everyone
C. One form for all users
D. Separate apps per role

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Assigning forms to security roles is the supported mechanism, and the highest-ordered form the user has access to is shown. Client script can adjust visibility but does not restrict data access, so it should never be the security control.
</details>

---

### Question 14
**Scenario:** An integration must call an external REST API that has no standard connector.

A. Build a custom connector describing the API's operations and authentication
B. Use a desktop flow
C. Copy the data manually
D. Store the API key in the flow

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A custom connector wraps the API with a definition (OpenAPI or manual) plus an authentication configuration, making it reusable across apps and flows and manageable under DLP policy. Embedding credentials directly in a flow bypasses that governance.
</details>

---

### Question 15
**Scenario:** Auditing must record who changed a customer's credit limit and when.

A. Enable auditing at the environment, table, and column level for that column, then read the audit history
B. Rely on the modified-on field
C. Add a note field
D. Enable Application Insights

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Dataverse auditing must be enabled at all three levels before it records anything, which is the detail most people miss. The modified-on field tells you the last change and by whom, not the history of values. Retention for audit data is configurable and should match the compliance requirement.
</details>

---

## Where to go deeper

- [PL-200 cert page](../../exams/azure/pl-200/) - notes, practice plan, strategy
- [PL-100 practice questions](./azure-power-platform-app-maker-pl-100.md) - the app maker sibling
- [PL-900 practice questions](./azure-power-platform-fundamentals-pl-900.md) - the fundamentals below both
- **[📖 PL-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-200)** - official skills outline
