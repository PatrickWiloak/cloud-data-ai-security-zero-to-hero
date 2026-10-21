---
last-updated: 2026-08-09
difficulty: beginner
---

# Microsoft Power Platform Fundamentals (PL-900) - Practice Questions

15 questions for PL-900 prep across business value, foundational components, and the capabilities of Power BI, Power Apps, Power Automate, and Copilot Studio.

> **Cert page:** [exams/azure/pl-900/](../../exams/azure/pl-900/)

---

### Question 1
**Scenario:** Which Power Platform component stores structured business data with tables, relationships, and business rules?

A. Power BI datasets, which hold imported data for reports and dashboards but are a reporting layer and not a store for app data
B. SharePoint lists, which hold simple rows and columns for collaboration but lack Dataverse's rich relationships and business rules
C. Dataverse, the native store with tables, relationships, business rules, and role-based security
D. Azure Blob Storage, which holds files and has no tables or relationships

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Dataverse is the platform's native data store, providing tables, relationships, business rules, role-based security, and auditing. SharePoint lists can back an app but lack the relational modeling and row-level security model. Power BI datasets are analytical, not transactional.
</details>

---

### Question 2
**Scenario:** A field technician needs a mobile app to capture inspection data offline, built without professional developers.

A. A canvas app in Power Apps
B. A Power Pages site, which is a website for external users and not a mobile app that works offline for field staff
C. A Power BI report, which visualizes data for analysis but is not an app for capturing inspection data in the field
D. A cloud flow, which automates steps between services on a trigger but provides no screens for a technician to enter data

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Canvas apps give pixel-level control over a mobile-first screen layout and support offline scenarios. Model-driven apps generate their UI from the Dataverse model and suit process-heavy internal applications. Power Pages is for external-facing websites.
</details>

---

### Question 3
**Scenario:** Which best describes the difference between canvas and model-driven apps?

A. Canvas gives you designer control of the layout from any data source; model-driven generates UI from the Dataverse data model and processes
B. They are the same thing, with the model-driven option simply being the name for canvas apps that are opened on a phone or tablet
C. Model-driven apps cannot use Dataverse and read only from SharePoint and Excel, while canvas apps can use Dataverse data
D. Canvas apps are only for desktop use in a browser and cannot be run in the Power Apps mobile app on a phone

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Canvas starts with the screen and connects to over 1,000 connectors. Model-driven starts with the data model and process, then generates responsive forms, views, and dashboards. The choice usually comes down to whether the experience or the data model should lead.
</details>

---

### Question 4
**Scenario:** An approval must run automatically when a SharePoint item is created.

A. An automated cloud flow with a SharePoint "item is created" trigger and an Approvals action
B. A desktop flow, which automates actions in a Windows application or website through the user interface and is not triggered by a SharePoint event
C. An instant flow, which starts when a user presses a button
D. A scheduled flow, which runs at a fixed time such as every morning

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Automated flows start from an event, which is what "when an item is created" is. Instant flows are triggered manually by a user, scheduled flows run on a timer, and desktop flows are robotic process automation for systems with no API.
</details>

---

### Question 5
**Scenario:** A legacy application has no API, and data must be entered into it automatically.

A. A Power BI dataflow, which prepares data for reporting
B. A cloud flow that calls the application's connector, which needs an API or a connector, and this legacy application offers no such interface
C. A canvas app that a person opens to type the data in by hand, which is manual entry and not automatic
D. A desktop flow using Power Automate for desktop (RPA), which drives the application's screens

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** RPA drives the user interface of applications that expose no programmatic interface, which is exactly the legacy case. It is a last resort because UI automation is brittle, but it is the right answer when no API exists. Cloud flows need a connector or API.
</details>

---

### Question 6
**Scenario:** A conversational assistant should answer employee HR questions from a document library.

A. Power Pages, which builds external-facing websites and portals and is not the tool for a chatbot that answers staff questions
B. Microsoft Copilot Studio
C. Power BI, which builds reports and dashboards from data models and does not hold a conversation with employees
D. Dataverse, which stores structured business data and can supply data to a bot but is not the conversational assistant itself

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Copilot Studio (formerly Power Virtual Agents) builds conversational agents with topics, actions, and generative answers grounded in your content sources. Power Pages is a website builder and Power BI is analytics.
</details>

---

### Question 7
**Scenario:** A public-facing site must let customers submit and track support requests against Dataverse data.

A. SharePoint, which suits internal team sites and is not meant for a customer portal
B. Power Pages, the external-facing website product with Dataverse forms and table permissions
C. Power BI, which can embed reports for external viewers but does not let customers submit and track support requests
D. A canvas app, which is designed for internal users who sign in to Power Apps and not for anonymous public customers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Power Pages is the external website product, with anonymous and authenticated access, table permissions, and forms bound to Dataverse. Canvas and model-driven apps require licensed internal users, so they are the wrong fit for customers.
</details>

---

### Question 8
**Scenario:** Which describes a connector?

A. A security role, which sets what a user may read, write, or delete in Dataverse and has nothing to do with integrating a service
B. A visual in Power BI such as a bar chart or map, which displays data in a report and does not read or write a service
C. A prebuilt integration that lets Power Platform read from and write to a service, with triggers and actions
D. A licensing tier that sets the monthly price per user, which affects which connectors are available but is not itself a connector

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Connectors are the integration layer for apps and flows. Standard connectors are included in base licensing, and premium connectors, including those for SQL Server, Azure services, and Dataverse in some contexts, require a premium license. That distinction shows up on the exam.
</details>

---

### Question 9
**Scenario:** An administrator must prevent business data connectors from being used alongside consumer connectors in the same flow.

A. Conditional Access, which sets sign-in rules in Microsoft Entra ID
B. A data loss prevention policy in the Power Platform admin center that groups connectors
C. A security role that controls which Dataverse tables a user can read or edit, which does not restrict the connectors in a flow
D. A sensitivity label that classifies documents and emails and can protect their content, but does not govern flow connectors

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Power Platform DLP policies classify connectors into Business, Non-business, and Blocked groups, and a flow or app cannot combine connectors from different groups. This is the control that stops someone piping SharePoint data into a personal cloud storage account.
</details>

---

### Question 10
**Scenario:** Development, test, and production work should be separated with controlled promotion.

A. Separate environments, with solutions used to move components between them
B. Personal workspaces for each maker, where individuals build and test their own work, which gives isolation but no controlled promotion
C. One production environment with naming conventions such as dev- and test- prefixes, which labels items but does not separate them
D. Separate tenants for each stage, which isolates identities and data but is far heavier than needed and is not how solutions are promoted

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Environments are the isolation boundary, each with its own Dataverse database and security. Solutions package apps, flows, tables, and connection references so they can be exported from development and imported to test and production, ideally as managed solutions.
</details>

---

### Question 11
**Scenario:** In Power BI, what is the difference between a report and a dashboard?

A. Reports cannot be shared with other users, so everything shared with others is published as a dashboard of pinned tiles
B. Dashboards are only for mobile use, whereas reports can be viewed only in a desktop browser or in the Power BI Desktop app
C. A report is multi-page and built on one semantic model; a dashboard is a single-page canvas of pinned tiles that can come from several reports
D. They are the same thing, with report being the name in Power BI Desktop and dashboard the name in the service

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Reports live with their model and support interactive filtering across pages. Dashboards aggregate pinned visuals from multiple reports into one at-a-glance view and exist only in the Power BI service, not in Desktop.
</details>

---

### Question 12
**Scenario:** A maker wants to reuse the same logic across several apps and flows.

A. Store the logic in a spreadsheet and look up the values from each app, which stores data but does not run shared logic
B. Copy and paste it into each app and flow, which means each change is repeated everywhere
C. Rewrite it each time in the local style of each app, so behavior can differ
D. Build a custom connector or a child flow, and use solutions to share components across environments

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Child flows and custom connectors centralize logic so a fix happens in one place. Copy-and-paste guarantees divergence, which is the most common maintenance failure in citizen-developed estates.
</details>

---

### Question 13
**Scenario:** Which describes AI Builder?

A. A database engine for storing large volumes of structured business data, with tables and indexes available to canvas and model-driven apps
B. A code editor in the browser in which developers write and debug extensions, such as PCF components and plug-ins
C. Prebuilt and custom AI models (form processing, object detection, prediction, text classification) usable from apps and flows
D. A licensing portal where administrators assign Power Platform licenses and add-on capacity to users in the tenant

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** AI Builder puts AI capabilities into low-code reach, most commonly document processing to extract fields from invoices or forms. It consumes AI Builder credits, which is a licensing consideration worth knowing.
</details>

---

### Question 14
**Scenario:** Access to specific Dataverse tables must differ by job role.

A. A DLP policy, which controls how connectors can be combined and does not set table access
B. Security roles with table-level privileges assigned to users or teams, scoped from user up to organization
C. Hiding tables in the app, which does not stop a user reaching the data another way
D. Environment variables, which hold configuration values such as URLs for each environment and do not control who can read tables

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Dataverse security roles grant create, read, write, delete, append, append-to, assign, and share privileges at record-ownership scopes from user up to organization. Hiding something in an app is cosmetic and does not stop another client from reading the table.
</details>

---

### Question 15
**Scenario:** The business value case for Power Platform is best summarized as what?

A. Replacing all professional development, so that organizations no longer need developers because citizen makers build every solution
B. Eliminating licensing costs, since the platform is included with Microsoft 365 and extra products carry no additional fees
C. Reducing the need for data governance, since low-code tools handle security, retention, and access policy automatically
D. Letting people close to the business build and automate solutions quickly, with governance and a path to professional development when needed

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The value is speed and proximity to the problem, with fusion teams where pro developers extend what makers build. Governance becomes more important rather than less, which is why environments, DLP policies, and the Center of Excellence toolkit exist.
</details>

---

## Where to go deeper

- [PL-900 cert page](../../exams/azure/pl-900/) - notes, practice plan, strategy
- [PL-100 practice questions](./azure-power-platform-app-maker-pl-100.md) - the app maker next step
- [PL-300 practice questions](https://data.noblerworks.com/resources/practice-questions/azure-power-bi-pl-300/) - Power BI at analyst depth
- [MS-900 practice questions](./azure-m365-fundamentals-ms-900.md) - the Microsoft 365 sibling
- **[📖 PL-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-900)** - official skills outline
