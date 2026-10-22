---
last-updated: 2026-10-22
difficulty: intermediate
---

# Power Platform App Maker Associate (PL-100) - Practice Questions

30 questions for PL-100 prep, weighted toward creating apps (30-35%), then designing business solutions (20-25%), working with data and services (15-20%), and deployment and business logic.

> **Cert page:** [exams/azure/pl-100/](../../exams/azure/pl-100/)

---

### Question 1
**Scenario:** Requirements gathering reveals a process with several stages, approvals, and a consistent data model used by internal staff.

A. A Power BI report with slicers and drill-through pages, shared with the staff who work on the process each day
B. A canvas app, designed screen by screen with galleries and forms
C. A model-driven app with a business process flow that guides users through the stages and approvals
D. A Power Pages site, where internal staff sign in with a work account and complete the process on the web

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Model-driven apps generate consistent forms and views from the Dataverse model, and business process flows guide users through defined stages. Canvas apps would mean hand-building each screen and reimplementing stage logic. Process-heavy internal applications are the model-driven sweet spot.
</details>

---

### Question 2
**Scenario:** A canvas app gallery should show only records assigned to the signed-in user, and the data source has 20,000 rows.

A. Set the data row limit to 2,000, the maximum, so the gallery can see more rows than the default of 500
B. `Filter(Cases, Owner.Email = User().Email)` using a delegable source and a delegable column
C. Load all records into a collection first with `ClearCollect`, then filter the collection by owner in the gallery
D. `Filter(Cases, Owner.Email = User().Email)` with a non-delegable expression

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Delegation is the central canvas app performance concept: when an expression is delegable, the filter runs at the data source, so only matching rows come back. Non-delegable expressions silently operate on the first 500 to 2,000 rows and give wrong results without an error. Collecting everything locally has the same ceiling.
</details>

---

### Question 3
**Scenario:** A field must be required only when another field equals "Other".

A. A DLP policy that classifies the connectors in the environment and blocks the ones that are not business data
B. A security role that removes write access to the field
C. A classic workflow that runs after save and clears empty records
D. A Dataverse business rule with a condition and a set-requirement action

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Business rules apply declarative field logic (show or hide, set required, set value, validate) at the table level, so they apply consistently in every model-driven app and form. Implementing it in one form's script would leave the other entry points unvalidated.
</details>

---

### Question 4
**Scenario:** Data is currently in an Excel file on SharePoint and must move into Dataverse.

A. Use Power BI to connect to the workbook and publish the data as a dataset that the app can read from
B. Copy and paste the rows manually into the table grid in batches, checking the columns by eye each time
C. Rebuild the app around Excel as the data source, reading the workbook on SharePoint through a connector
D. Dataflows to map columns, or the import wizard for one-off loads

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Dataflows handle the transform and the column mapping and can be refreshed on a schedule, which is what you want if the source keeps producing files. Keeping Excel as the backing store means no relational integrity, no row-level security, and delegation problems.
</details>

---

### Question 5
**Scenario:** A canvas app should navigate to a detail screen and pass the selected record.

A. `Refresh(Gallery1)`, which reloads the gallery's data source
B. `Navigate(DetailScreen, ScreenTransition.Cover, {SelectedItem: Gallery1.Selected})`
C. `Set(DetailScreen, Gallery1.Selected)`, which stores a global variable
D. `Patch(DetailScreen, Gallery1.Selected)`, which updates the screen

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `Navigate` moves between screens and its third argument passes context variables. `Patch` writes records, `Set` creates a global variable, and `Refresh` re-reads a data source. Using a context variable rather than a global keeps the value scoped to the screen that needs it.
</details>

---

### Question 6
**Scenario:** A form should save a new record and handle failure gracefully.

A. `SubmitForm(Form1)` with `OnFailure` showing the error and `OnSuccess` moving on
B. `Navigate()` only, moving to the confirmation screen right after the button is pressed, without checking the save
C. `Patch()` with no error handling, trusting the data source to report any failure to the user itself
D. `Reset(Form1)`, which clears the form controls so that the user can start the next record straight away

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `SubmitForm` performs validation and writes, and the form's `OnSuccess` and `OnFailure` properties are where you handle both outcomes. Navigating away unconditionally is the common bug that hides save failures from users.
</details>

---

### Question 7
**Scenario:** A solution must be moved from development to production so that production components cannot be edited directly.

A. Export as unmanaged, then import into production and lock the components with a security role
B. Copy the app by hand from the development environment, re-creating each screen and connection in production
C. Export as a managed solution and import into production
D. Let users work in the dev environment

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Managed solutions lock components in the target environment and can be cleanly uninstalled, which is why they are the standard for anything downstream of development. Unmanaged solutions are for the development environment where components are still being authored.
</details>

---

### Question 8
**Scenario:** A connection reference and an environment variable are used in a solution. Why?

A. So connections and configuration values can differ per environment without editing the components
B. To improve performance, because values stored in environment variables are cached in the app after the first load
C. They are mandatory in canvas apps, which will not open without them
D. To hard-code URLs and keys into the components in every environment

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Without them, a flow imported into production would still point at the development SharePoint site and the developer's connection. Connection references and environment variables are the parameterization that makes a solution genuinely portable across environments.
</details>

---

### Question 9
**Scenario:** An app must be usable by someone relying on a screen reader.

A. Add more images with decorative effects, since pictures help users who cannot read long text on the screen
B. Set accessible labels on controls, ensure tab order and focus are logical, and check color contrast with the accessibility checker
C. Increase the font size only, since a larger size is all that a screen reader needs to read the text
D. Nothing, because Power Apps handles it automatically, and every control is labeled for readers by default

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The accessibility checker in Power Apps Studio flags missing labels, contrast problems, and tab order issues. PL-100 explicitly covers accessibility, and it is one of the areas where a low-code tool will happily let you ship something unusable if you never check.
</details>

---

### Question 10
**Scenario:** Users report the app is slow to open.

A. Disable delegation warnings in the app settings, which stops the app from checking the queries it sends
B. Increase the license tier for the users, since higher plans get more capacity for the app to run on
C. Reduce controls per screen, avoid heavy `OnStart` work, use concurrent loading, and delegate queries so the data source does the filtering
D. Add more screens, so that each screen holds fewer controls and users spend less time on each one

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Startup cost is dominated by `OnStart` logic and the number of controls loaded. `Concurrent()` parallelizes independent calls, and delegation keeps data volumes small. Suppressing delegation warnings hides the problem that is most likely causing both slowness and wrong data.
</details>

---

### Question 11
**Scenario:** A model-driven app must show related cases on the account form.

A. A one-to-many relationship with a related records subgrid on the form
B. A Power BI tile embedded on the form, filtered by the account, with the case list shown in the report
C. A separate app that lists the cases, opened from a link on the account form with the account id
D. A canvas gallery added by hand onto the form, filtered by the account through a custom connector

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The relationship is what makes the subgrid possible, so the data model comes first and the form follows. This is the model-driven pattern in miniature: define the relationship in Dataverse and the UI capability follows automatically.
</details>

---

### Question 12
**Scenario:** An app must send a notification when a record's status becomes Approved.

A. A scheduled flow that runs every minute and checks all the records for any with the status Approved
B. A business rule on the table that sends the message when the status field changes to the value Approved
C. A Dataverse-triggered cloud flow filtered on the status column
D. Manual email from the approver to the requester

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The Dataverse connector's "when a row is modified" trigger supports filtering to specific columns, so the flow only fires on the change you care about. A one-minute schedule burns API calls and adds latency. Business rules do field logic and cannot send mail.
</details>

---

### Question 13
**Scenario:** Sensitive salary data in a Dataverse table must be hidden from most users but visible to HR.

A. Column-level security with a security profile granting HR read access
B. A canvas app filter that hides the salary column
C. Hiding the column on the form
D. A different table for salary data, with the same security role as the main table, and a lookup between them

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Column (field) level security enforces at the platform, so the value is masked in every app, view, export, and API call. Hiding a column in a form or filtering in a canvas app is presentation only and is bypassed by anyone using another client.
</details>

---

### Question 14
**Scenario:** A maker needs to validate that a solution meets requirements before release.

A. Ship and see, then collect the feedback from users in the first week and fix what they report
B. A performance test only, run with a load tool against the main screens, with a report of response times
C. Peer review of screenshots, where another maker checks each screen against the requirement list
D. User acceptance testing against the documented requirements, plus the solution checker

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Solution checker analyzes for performance, stability, and security issues automatically, and UAT validates the thing nobody can automate: whether it solves the business problem. PL-100 treats requirements traceability as part of the maker's job, not the sponsor's.
</details>

---

### Question 15
**Scenario:** An app should be shared with a department of 200 users with the least ongoing administration.

A. Email the app link to the department
B. Share with a Microsoft Entra security group
C. Share with each user individually, adding the 200 names in the share panel and the data permissions to match
D. Open the app to the entire tenant

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Group-based sharing means joiners and leavers are handled by group membership, which is already maintained. Individual sharing turns every personnel change into an administrative task and reliably leaves ex-members with access.
</details>

---

### Question 16
**Scenario:** A new solution needs related tables, role-based security at the row level, and business rules, and data volume will grow past what a simple list handles well.

A. An Excel workbook on OneDrive, with one worksheet per table and formulas linking the rows
B. Dataverse, which provides relational tables, security roles, and business rules
C. SharePoint lists, with a lookup column for each relationship and item-level permissions set by hand
D. A Power BI semantic model, which stores the tables and lets apps write back to them

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Dataverse is designed for relational business data, with security roles, business units, business rules, and scale. Excel is not a multi-user database. SharePoint lists work for simple data but have weak relational and row-level security support at scale. Power BI models are read-only analytical stores.
</details>

---

### Question 17
**Scenario:** Several apps need the same header with a logo, a user name, and a menu, and changes to it should flow to every app.

A. Copy the header controls into each app by hand, then edit each copy when the design changes
B. Build the header as a Power Pages template and embed the template in each canvas app
C. Build the header as a canvas component in a component library and import it into each app
D. Put the header in a Power BI report and embed the report at the top of each app screen

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A component library holds reusable canvas components. Apps that use them are notified of updates and can take the new version, so the header is maintained once. Copying controls creates drift. Power Pages templates are for websites. A Power BI report is not a navigation header.
</details>

---

### Question 18
**Scenario:** Field staff need a highly tailored phone interface that combines data from Dataverse, SharePoint, and a SQL database on one screen.

A. A canvas app, which allows a custom layout and connects to many data sources
B. A model-driven app, which renders a standard layout from Dataverse tables only
C. A Power BI dashboard, which phone users edit through tiles pinned from reports
D. A Power Pages site, which field staff open in a browser with an external login

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Canvas apps give full control of layout and can combine many connectors on one screen, which suits a tailored mobile experience. Model-driven apps generate a standard UI from Dataverse and do not combine other sources the same way. Dashboards are for viewing data. Power Pages targets external or web audiences.
</details>

---

### Question 19
**Scenario:** Inspectors lose connectivity on site. The app must keep entered inspections on the device and submit them later.

A. Store each inspection in a global variable, which persists on the device after the app closes
B. Write each inspection straight to Dataverse, which queues writes on the device automatically
C. Use a timer control that retries the Patch call every second until the network returns
D. Collect inspections locally and use SaveData and LoadData, then Patch them when Connection.Connected is true

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A collection saved with SaveData persists on the device and can be reloaded with LoadData. When Connection.Connected becomes true, the app patches the queued records to the data source. Variables are lost when the app closes. A plain canvas app does not queue writes on its own (Dataverse offline mode is a separate, configured feature). A tight retry timer does not survive closing the app.
</details>

---

### Question 20
**Scenario:** A button must mark the selected gallery item as Complete in Dataverse, without using an edit form.

A. Patch(Tasks, ThisItem, {Status: "Complete"})
B. SubmitForm(Gallery1), with the status set on the gallery's Default property
C. UpdateContext({Status: "Complete"}), which writes the value to the record
D. Navigate(Tasks, ThisItem), which opens the record with the new status

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Patch modifies or creates records in a data source directly, so patching the current item with a new status updates it without a form. SubmitForm works only with form controls. UpdateContext sets a local variable on the screen and does not write data. Navigate changes screens.
</details>

---

### Question 21
**Scenario:** A canvas app must adapt its layout to phones, tablets, and desktop browsers without separate screens for each size.

A. Turn on Scale to fit and lock the aspect ratio, which reflows controls for each screen size
B. Build three copies of every screen and pick one with an If on the screen width
C. Use horizontal and vertical containers with relative sizing, and turn off Scale to fit
D. Set every control's X and Y to fixed values, sized for the smallest phone the users have

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Responsive canvas apps use layout containers and formulas based on the parent's width and height, with Scale to fit turned off so the app can reflow. Scale to fit shrinks a fixed layout rather than reflowing it. Duplicate screens multiply maintenance. Fixed positions do not adapt.
</details>

---

### Question 22
**Scenario:** A value chosen on one screen must be read on several other screens of the same canvas app.

A. UpdateContext, which creates a variable visible on every screen of the app
B. Set, which creates a global variable visible on every screen of the app
C. A label control on the first screen, read by name from the other screens
D. Collect, which is the only way to store a single value across screens

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Set creates a global variable available throughout the app. UpdateContext creates a context variable scoped to one screen, unless you pass it with Navigate. Reading a label across screens couples screens together and is fragile. Collect creates a table, which is unnecessary for a single value.
</details>

---

### Question 23
**Scenario:** A maker published a change that broke the app, and users need the previous working version back immediately.

A. Delete the app and ask users to wait while it is rebuilt from the last saved file
B. Export the app to a package and import it again, which rolls it back by one version
C. Ask an administrator to restore the whole environment from its most recent backup
D. Restore the previous version from the app's Versions list, which makes it the live version

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Canvas apps keep a version history, and restoring an earlier version creates a new version from it that can be published, giving users the working app back. Deleting the app loses its sharing and history. Exporting and importing does not roll back. An environment restore affects every app and data, far beyond what is needed.
</details>

---

### Question 24
**Scenario:** A second maker must be able to edit and share a canvas app while the original maker is on leave.

A. Share the app with the second maker as a co-owner
B. Give the second maker the original maker's password
C. Share the app with the second maker as a user
D. Export the app and send the file to the second maker

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Co-owners can edit the app, share it, and manage it without being the original owner. Sharing credentials breaks security policy. User permission allows running the app only. An exported copy is a different app, so edits would not affect the one users run.
</details>

---

### Question 25
**Scenario:** The account form must show the total estimated revenue of all open opportunities related to that account.

A. A calculated column on the account table that sums the opportunities through the lookup
B. A text column filled by hand by each salesperson whenever an opportunity changes
C. A rollup column on the account table that aggregates the related opportunity values
D. A choice column that lists each related opportunity's value as one of its options

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Rollup columns aggregate values, such as sums or counts, from related records in a one-to-many relationship, which fits totals of child records. Calculated columns work on values in the same record and related parent records, not aggregates of many children. Manual entry drifts. Choice columns hold fixed options.
</details>

---

### Question 26
**Scenario:** An app must call an internal REST API that has an OpenAPI definition but no prebuilt connector.

A. Call the API with the Launch function, which sends the request and returns the JSON response
B. Store the API's data in Excel each night and use the Excel connector from the app
C. Use the SQL Server connector, which can call any REST endpoint given its address
D. Create a custom connector from the OpenAPI definition, then add it to the app

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A custom connector can be created from an OpenAPI definition, with authentication configured, and then used in apps and flows like any connector. Launch opens a URL or app and returns nothing. A nightly Excel copy is stale. The SQL Server connector talks only to SQL databases.
</details>

---

### Question 27
**Scenario:** Each inspection record must point to exactly one site record, and users should pick the site from the list of existing sites.

A. A lookup column on the inspection table referencing the site table
B. A choice column with each site name typed in as an option
C. A text column where users type the site's name each time
D. A many-to-many relationship between inspections and sites

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A lookup column creates a many-to-one relationship, so each inspection points to one site chosen from existing records. Choices are static and must be edited as sites change. Free text produces inconsistent values. Many-to-many would allow several sites per inspection, which the requirement rules out.
</details>

---

### Question 28
**Scenario:** A canvas app button must start a flow that creates a PDF, then show the returned file link in the app.

A. A scheduled cloud flow that runs every minute and checks whether the button was pressed
B. A flow with the Power Apps (V2) trigger, run from the button, that returns the link with a respond action
C. A desktop flow started from the app, which opens the PDF on the user's own computer
D. An automated flow triggered when the app is published, which writes the link to a label

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A cloud flow with the Power Apps (V2) trigger is called from the app with parameters, and the "Respond to a Power App or flow" action returns values the app can show. Polling on a schedule is slow and wasteful. A desktop flow is for UI automation. Publishing an app is not a per-click event.
</details>

---

### Question 29
**Scenario:** A rule that sets a field's value must apply when records are created from a model-driven form and also through data imports.

A. Set the business rule scope to the main form only, so it runs on the server for imports too
B. Write the rule as a JavaScript web resource on the form, which also runs during imports
C. Set the business rule scope to Entity (all forms and server), so it also runs on the server
D. Create the rule in a canvas app, since canvas app formulas also run during imports

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A business rule with Entity scope runs server-side as well as on model-driven forms, so it applies to imports and other server operations. A rule scoped to a form runs only in that form. Form JavaScript does not run during imports. Canvas app formulas run only in the app.
</details>

---

### Question 30
**Scenario:** Before building, a maker wants to capture who will use the app and what each person needs to do with it.

A. Start building screens straight away and collect needs as users find problems in production
B. Copy an existing app from another department and change the labels to fit the new process
C. Pick the data source first, then work out which users can be served by the tables it already has
D. Write user stories for each persona, such as "as a technician I need to log a repair offline"

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Personas and user stories capture who the users are and what they need, which guides choices about app type, data, and offline support. Building first and discovering needs in production causes rework. Copying another department's app assumes their process. Choosing data first lets technology drive requirements.
</details>

---

## Where to go deeper

- [PL-100 cert page](../../exams/azure/pl-100/) - notes, practice plan, strategy
- [PL-900 practice questions](./azure-power-platform-fundamentals-pl-900.md) - the fundamentals below this
- [PL-200 practice questions](./azure-power-platform-consultant-pl-200.md) - the functional consultant path
- **[📖 PL-100 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-100)** - official skills outline
