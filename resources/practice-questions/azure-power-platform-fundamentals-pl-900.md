---
last-updated: 2026-10-22
difficulty: beginner
---

# Microsoft Power Platform Fundamentals (PL-900) - Practice Questions

30 questions for PL-900 prep across business value, foundational components, and the capabilities of Power BI, Power Apps, Power Automate, and Copilot Studio.

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

### Question 16
**Scenario:** A maker with no coding experience wants to describe an app in plain language, such as "track equipment loans with due dates", and have Power Apps propose the table and the app.

A. Power Automate desktop flows, which record the maker's screen and generate an app from the recording
B. Copilot in Power Apps, which builds a Dataverse table and an app from a natural language description
C. Power BI Q&A, which turns the description into a report that users can edit like an app
D. AI Builder form processing, which reads the description and generates the app's screens

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Copilot in Power Apps takes a natural language description, proposes a Dataverse table with columns, and generates an app the maker can refine. Desktop flows automate UI tasks and do not build apps. Q&A answers questions over data in Power BI. AI Builder form processing extracts data from documents.
</details>

---

### Question 17
**Scenario:** Business users build apps for their own processes, while professional developers add custom connectors and code components. What is this collaboration called?

A. A fusion team, where makers and professional developers build solutions together on one platform
B. Shadow IT, where business units build tools without any involvement from the IT department
C. A center of excellence, which is the team that builds every app in the organization
D. Outsourcing, where an external vendor builds the apps that business users specify

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Fusion teams combine business makers, professional developers, and IT on the same platform, each contributing what they do best. Shadow IT describes ungoverned tools built outside IT. A center of excellence sets governance and supports makers rather than building everything. Outsourcing removes the business users from building.
</details>

---

### Question 18
**Scenario:** An organization wants a separate space for the finance department's apps, flows, and data, with its own security and its own Dataverse database.

A. A Power BI workspace, which holds apps and flows alongside reports and semantic models
B. A SharePoint site collection, which stores the apps and flows with Dataverse tables
C. A Power Platform environment, a container for apps, flows, and at most one Dataverse database
D. A solution, which isolates its own Dataverse database from the other solutions in a tenant

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Environments are containers for apps, flows, connections, and data, each with its own security roles and up to one Dataverse database. Power BI workspaces hold BI content. SharePoint sites do not host Power Platform apps and flows as a boundary. Solutions package components for transport and share the environment's database.
</details>

---

### Question 19
**Scenario:** Makers write expressions such as `Filter(Orders, Status = "Open")` in canvas apps. What is this formula language?

A. DAX, the formula language used to build measures in Power BI and Power Pivot
B. Power Fx, the low-code formula language used across Power Platform
C. M, the language Power Query uses for data transformation steps
D. JavaScript, which runs in the browser that hosts the canvas app

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Power Fx is the Excel-like low-code language used in canvas apps and increasingly elsewhere in Power Platform. DAX is for Power BI measures and calculated columns. M is the Power Query language. Canvas app formulas are not JavaScript.
</details>

---

### Question 20
**Scenario:** An administrator must create environments, review Dataverse storage capacity, and manage data policies for the tenant.

A. The Power Apps maker portal, which is where every administrative setting is managed
B. The Microsoft 365 admin center only, since Power Platform has no admin portal of its own
C. Power BI Desktop, which administers environments and capacity from its options menu
D. The Power Platform admin center

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The Power Platform admin center is where administrators manage environments, capacity, data policies, and analytics. The maker portal is for building apps. The Microsoft 365 admin center handles licenses and users but not environments. Power BI Desktop is an authoring tool.
</details>

---

### Question 21
**Scenario:** An analyst built a report in Power BI Desktop and now wants colleagues to view it in a browser, with the data refreshed on a schedule.

A. Email the .pbix file to colleagues, who then refresh the data from their own copies
B. Export the report to PDF every morning and save it to a shared folder for colleagues
C. Publish the report to the Power BI service, share it, and configure scheduled refresh
D. Copy the visuals into an Excel workbook, which refreshes the data from the report

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Power BI Desktop is the authoring tool. Publishing to the Power BI service makes the report available in the browser, where you can share it and schedule refresh of the semantic model. Emailing .pbix files creates uncontrolled copies. PDFs are static. Excel does not refresh from report visuals.
</details>

---

### Question 22
**Scenario:** Sales data arrives with inconsistent date formats, extra header rows, and a column that needs splitting before it can be used in a Power BI report.

A. Power Query, which applies repeatable cleaning and shaping steps when the data is loaded
B. A dashboard tile, which formats each value correctly when pinned
C. Row-level security, which hides badly formatted rows from viewers
D. A bookmark, which saves a view of the report with the data fixed

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Power Query records transformation steps, such as removing rows, changing types, and splitting columns, and replays them on every refresh. Dashboard tiles display visuals. Row-level security filters data by user and does not clean it. Bookmarks save report states such as filters and visibility.
</details>

---

### Question 23
**Scenario:** Managers want to type questions such as "total sales by region last quarter" in a report and get a chart back without building visuals themselves.

A. A paginated report, which prints pixel-perfect pages
B. The Q&A visual, which answers natural language questions
C. A Power Automate visual, which runs a flow from the report
D. A dataflow, which stores prepared data for reuse

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Q&A visual lets users ask questions in natural language and returns a suitable visual. Paginated reports are for fixed-layout printing. The Power Automate visual triggers flows. Dataflows prepare and store data for reuse but do not answer questions.
</details>

---

### Question 24
**Scenario:** A team keeps a list of assets in a SharePoint list and wants a working canvas app over that data in minutes, which it will refine later.

A. Write the app in Visual Studio, then import it into Power Apps as a code component
B. Build a Power BI report on the list, then convert the report into a canvas app
C. Create a model-driven app directly on the SharePoint list, without Dataverse tables
D. Start from data in Power Apps, which generates a browse, detail, and edit app from the list

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Creating a canvas app from data generates a working app with browse, detail, and edit screens connected to the source, which makers then customize. Visual Studio is not how canvas apps are built. Power BI reports cannot be converted into apps. Model-driven apps are built on Dataverse tables, not SharePoint lists.
</details>

---

### Question 25
**Scenario:** Which statement about how a model-driven app's user interface is created is correct?

A. The interface is generated from Dataverse components such as tables, forms, views, and dashboards
B. The maker places every control pixel by pixel on a blank canvas, as in a canvas app
C. The interface is generated from a Power BI report, which supplies the forms and views
D. The interface is written in HTML by a developer, then attached to the Dataverse tables

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Model-driven apps are built from the data model: makers pick tables, forms, views, charts, and dashboards, and the app renders a consistent responsive interface from them. Pixel-level layout is the canvas app approach. Power BI does not supply forms. No HTML is written by hand.
</details>

---

### Question 26
**Scenario:** A summary of overdue invoices must be emailed to the finance team every Monday at 8:00 without anyone starting it.

A. An instant cloud flow, which a user starts from a button
B. A desktop flow, which records clicks on a user's computer
C. A scheduled cloud flow with a weekly recurrence trigger
D. A business process flow, which guides users through stages

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A scheduled cloud flow runs on a recurrence, such as weekly on Mondays at a set time, with no user action. Instant flows need someone to start them. Desktop flows automate UI tasks on a machine. Business process flows guide users through stages in model-driven apps.
</details>

---

### Question 27
**Scenario:** Field staff want to start a flow from their phone that sends their current location and a photo to a supervisor, only when they choose to.

A. An automated cloud flow triggered whenever a new photo is saved to the phone
B. A scheduled cloud flow that checks every staff member's location each hour
C. A desktop flow running on the supervisor's computer, which polls each phone
D. An instant cloud flow, started manually from the Power Automate mobile app

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Instant cloud flows are started on demand, for example from a button in the Power Automate mobile app, and can collect inputs such as location and files. Automated flows fire on events without user choice. Scheduled flows run on a timer. Desktop flows automate a desktop and do not take input from phones.
</details>

---

### Question 28
**Scenario:** A Copilot Studio agent must handle "reset my password" with a fixed, guided set of steps and questions every time.

A. A topic that defines the conversation path for that request
B. A Power BI report that the agent displays to the user
C. A dataflow that loads password reset data into Dataverse
D. A canvas app embedded in the agent's welcome message

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** In Copilot Studio, topics define conversation paths: how the agent recognizes a request and the questions, messages, and actions that follow. A report displays data. A dataflow loads data. An embedded app is not how agents structure a guided conversation.
</details>

---

### Question 29
**Scenario:** An HR agent built in Copilot Studio should be available to employees where they already chat every day.

A. Publish it as a Power BI dashboard tile that employees pin in the workspace
B. Publish it to the Microsoft Teams channel, so employees chat with it in Teams
C. Export it as a desktop flow, which employees start from Power Automate Desktop
D. Embed it in a Dataverse view, which employees open from a model-driven app

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Copilot Studio agents are published to channels, and Teams is a standard channel for internal employee agents, alongside websites and others. Dashboard tiles, desktop flows, and Dataverse views are not channels for conversational agents.
</details>

---

### Question 30
**Scenario:** A department wants to stop retyping data from vendor invoices into a system, extracting fields such as invoice number and total automatically.

A. A Power BI paginated report, which reads printed invoices and summarizes the totals
B. A Power Pages form, which vendors fill in by hand for each invoice they send
C. AI Builder's invoice processing model, used in a Power Automate flow
D. A Dataverse business rule, which reads the invoice files when they are uploaded

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** AI Builder offers a prebuilt invoice processing model that extracts fields from invoices and can be called from Power Automate to write the data into a system. Paginated reports produce output, not input. A vendor portal shifts typing to vendors instead of removing it. Business rules apply field logic and cannot read files.
</details>

---

## Where to go deeper

- [PL-900 cert page](../../exams/azure/pl-900/) - notes, practice plan, strategy
- [PL-100 practice questions](./azure-power-platform-app-maker-pl-100.md) - the app maker next step
- [PL-300 practice questions](https://data.noblerworks.com/resources/practice-questions/azure-power-bi-pl-300/) - Power BI at analyst depth
- [MS-900 practice questions](./azure-m365-fundamentals-ms-900.md) - the Microsoft 365 sibling
- **[📖 PL-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-900)** - official skills outline
