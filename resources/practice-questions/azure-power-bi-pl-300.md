# Microsoft Power BI Data Analyst (PL-300) - Practice Questions

15 questions for PL-300 prep. Most modeling and DAX questions assume a star schema and turn on understanding filter context.

> **Cert page:** [exams/azure/pl-300/](../../exams/azure/pl-300/)

---

### Question 1
**Scenario:** A 4-billion-row fact table lives in Azure Synapse. Current-day data must be accurate to the minute; five years of history is queried far more often and performance is a priority.

A. Full DirectQuery
B. Full Import with hourly refresh
C. A composite model: history in Import, current day in DirectQuery, shared dimensions in Dual
D. Import with incremental refresh only

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A composite model satisfies both requirements at once. Dual mode on the shared dimensions is what prevents an unnecessary DirectQuery round trip for the imported queries. Full DirectQuery meets currency and fails performance. Import with any refresh schedule cannot be minute-accurate.
</details>

---

### Question 2
**Scenario:** A refresh over a 200-million-row SQL table takes four hours. An index column is added as the second Power Query step, with filters and group-by afterwards.

A. Increase gateway memory
B. Move or remove the index column step so filters and grouping fold to the source, and verify with View Native Query
C. Switch to DirectQuery
D. Schedule the refresh overnight

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Adding an index column breaks query folding, so every subsequent step processes locally on the full dataset. Reordering so folding-breaking steps come last restores source-side filtering. More memory treats the symptom. DirectQuery changes the interaction model to solve a refresh problem. Scheduling overnight leaves the four hours in place.
</details>

---

### Question 3
**Scenario:** `Profit Margin` is created as a calculated column with `(Revenue - Cost) / Revenue`, then placed in a card with average aggregation. Finance reports the value is wrong at every level except individual rows.

A. Change the visual aggregation to sum
B. Replace it with a measure: `DIVIDE( SUM(Revenue) - SUM(Cost), SUM(Revenue) )`
C. Add a second calculated column for the weighted average
D. Use `AVERAGEX` over the fact table

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Averaging a row-level ratio gives the average of ratios, not the ratio of totals. Ratios must be measures so aggregation happens before division. `DIVIDE` also handles division by zero. Summing percentages is worse. `AVERAGEX` computes an average of ratios, which is a different, usually unwanted, number here.
</details>

---

### Question 4
**Scenario:** 200 regional managers must each see only their own region. An employee table maps each manager's email to their region.

A. 200 static row-level security roles
B. One dynamic RLS role filtering on `[Email] = USERPRINCIPALNAME()`, with the security table related through to the fact table
C. A slicer defaulted to the user's region
D. Object-level security

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Dynamic RLS with `USERPRINCIPALNAME()` scales to any number of users with one role. Static roles are unmanageable at 200. A slicer is not security, because users can change it. Object-level security hides tables and columns, not rows.
</details>

---

### Question 5
**Scenario:** A `SAMEPERIODLASTYEAR` measure returns blank for every row. The model has a date column on the fact table and no separate date table.

A. Wrap the measure in `CALCULATE` with additional filters
B. Change the fact date column's data type
C. Create a contiguous date table covering full years, mark it as a date table, relate it to the fact, and reference its date column
D. Enable Auto Date/Time

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Time intelligence functions require a marked date table with a complete, gap-free date range. Blank results almost always mean the date table is missing, unmarked, or has gaps. Auto Date/Time creates hidden per-column tables that bloat the model and do not provide the marked-date-table behavior these functions expect.
</details>

---

### Question 6
**Scenario:** A finance report must reach 3,000 employees across four departments, each seeing only their department's pages, while five authors keep editing without disrupting consumers.

A. Share the report directly with all 3,000 users
B. Give all consumers Viewer access to the workspace
C. Publish an app with four audiences, keeping authors in the workspace
D. Create four separate workspaces

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Apps with audiences are the governed distribution mechanism, and publishing separates what consumers see from work in progress. Direct sharing is unmanageable at that scale and exposes edits immediately. Workspace Viewer access shows unpublished changes and offers no audience segmentation. Four workspaces duplicate the model and its maintenance.
</details>

---

### Question 7
**Scenario:** Which workspace role can create and edit content and schedule refresh, but cannot publish an app?

A. Admin
B. Member
C. Contributor
D. Viewer

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Contributor is exactly this boundary and it is directly testable. Admin and Member can both publish apps. Viewer can only consume, and is the only role to which row-level security applies.
</details>

---

### Question 8
**Scenario:** An author tests row-level security in the workspace and sees all rows despite being assigned to a role. Why?

A. The role's DAX expression is wrong
B. Workspace Contributors and above bypass RLS; testing requires View As or a real Viewer
C. RLS requires a Premium capacity
D. The relationship direction is wrong

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RLS applies to the Viewer role. Anyone with Contributor or above sees all rows in the workspace regardless of role membership, so validation must use View As in Desktop and then a genuine Viewer or app consumer in the service.
</details>

---

### Question 9
**Scenario:** A model built from one 60-column flat spreadsheet is 800 MB, slow, and filters inconsistently. What is the correct fix?

A. Add calculated columns to speed up common measures
B. Split into fact and dimension tables with single-direction one-to-many relationships, add a marked date table, and remove unused high-cardinality columns
C. Switch to DirectQuery
D. Reduce the number of visuals per page

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Star schema resolves the ambiguous filtering and the repetition driving size. The largest size win usually comes from removing high-cardinality columns such as transaction IDs and timestamps. Calculated columns increase size. DirectQuery moves the problem to the source. Fewer visuals does not fix a model problem.
</details>

---

### Question 10
**Scenario:** Which relationship configuration should generally be avoided because it introduces ambiguity?

A. Single-direction one-to-many from dimension to fact
B. Bidirectional cross-filtering between two tables
C. An inactive relationship activated with `USERELATIONSHIP`
D. A one-to-one relationship between two dimension tables

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Bidirectional filtering creates ambiguous filter paths and can produce wrong results elsewhere in the model. The usual alternative is single direction plus `CROSSFILTER` inside specific measures where both directions are genuinely needed.
</details>

---

### Question 11
**Scenario:** Incremental refresh cannot be configured on a table. What is the most likely cause?

A. The table is in DirectQuery mode
B. The parameters are not named exactly `RangeStart` and `RangeEnd`, or query folding does not reach the source
C. The dataset is not on a Premium capacity
D. There is no date table in the model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Incremental refresh requires two date/time parameters named exactly `RangeStart` and `RangeEnd`, a filter using them, and query folding so the source can partition. A model date table is unrelated to the parameter requirement.
</details>

---

### Question 12
**Scenario:** One report page renders in 25 seconds while others are instant. The model is Import mode and reasonably sized. What is the first step?

A. Switch the model to DirectQuery
B. Run Performance Analyzer to determine whether time is in the DAX query, visual display, or other
C. Increase the capacity size
D. Split the page into three pages

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The exam expects the diagnostic step before the fix. Performance Analyzer tells you whether the cost is in the query, the visual, or elsewhere, which determines whether you rewrite a measure, change the model, or reduce visual cardinality. Splitting pages may help, but only once you know why.
</details>

---

### Question 13
**Scenario:** Which storage mode allows a dimension table to serve both an imported fact table and a DirectQuery fact table without forcing a source round trip for the imported queries?

A. Import
B. DirectQuery
C. Dual
D. Direct Lake

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Dual lets the engine decide per query, acting as Import when serving imported facts and as DirectQuery when serving DirectQuery facts. That is precisely the problem Dual exists to solve, and it is why composite models depend on it.
</details>

---

### Question 14
**Scenario:** What does a deployment pipeline rule do?

A. Restricts who can deploy between stages
B. Swaps data source parameters and connection details so each stage points at the right data
C. Schedules deployments
D. Validates the semantic model before deployment

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Rules are the mechanism ensuring production content points at production data after promotion. Access control between stages is governed separately by workspace permissions, and rules do not schedule or validate.
</details>

---

### Question 15
**Scenario:** A report must be accessible to keyboard and screen reader users. Which combination is required?

A. Alt text on visuals and a high-contrast theme
B. Alt text on visuals, a logical tab order set in the Selection pane, sufficient contrast, and not relying on color alone
C. A mobile layout
D. Exporting the report to PDF

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Accessibility on this exam consistently covers all four: alt text, tab order, contrast, and not conveying meaning through color alone. A mobile layout addresses screen size, not accessibility. PDF export is a different output, not an accessibility control.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready. Spend remaining time predicting DAX results before running them.
- **10-12 correct (65-80%):** Review filter context and the star schema material, which underpin most wrong answers.
- **Below 10:** Build the models listed in the [practice plan](../../exams/azure/pl-300/practice-plan.md). PL-300 rewards hands-on work more than any other exam in the Microsoft data track.
