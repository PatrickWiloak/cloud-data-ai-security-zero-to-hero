---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 10 min
---

# PL-300 High-Yield Scenarios

---

## Scenario 1: Choosing a storage mode

**Scenario**: A logistics company needs a report over a 4-billion-row shipment fact table in Azure Synapse. Operations need current-day shipments accurate to the minute. Historical analysis covers five years and is used far more often. Report performance is a stated priority.

**Solution Pattern**:
- **Composite model**: the historical fact table in **Import** mode, the current-day table in **DirectQuery**
- Shared dimension tables set to **Dual** so they serve both without a round trip for import queries
- Aggregation table over the imported history for common summary queries
- If the estate is on Fabric, **Direct Lake** over the lakehouse is the alternative that avoids the import step entirely

**Common Distractors**:
- Full DirectQuery (meets currency, fails the performance priority)
- Full Import with hourly refresh (fails the minute-level currency requirement)
- Import with incremental refresh alone (still not minute-level current)

**Key Takeaway**: When one part of the data must be live and the rest must be fast, the answer is a composite model with Dual dimensions. Dual exists precisely so shared dimensions do not force a DirectQuery round trip.

---

## Scenario 2: Broken query folding

**Scenario**: A report over a 200-million-row SQL table refreshes in four hours. Investigation shows an index column added as the second step, then filters and group-by operations after it. The gateway machine shows high memory use during refresh.

**Solution Pattern**:
- Remove or move the **index column** step, which breaks folding, so subsequent filters and grouping fold to the source
- Reorder so all foldable operations (filter, group, select columns) come first, and any folding-breaking step comes last
- Verify with **View Native Query** at each step; if it is unavailable, folding has stopped
- Filter rows and remove unneeded columns as early as possible
- Once folding is restored, configure **incremental refresh**, which requires folding

**Common Distractors**:
- Increasing gateway memory (treats the symptom, not the cause)
- Switching to DirectQuery (changes the interaction model to solve a refresh problem)
- Scheduling refresh at night (the refresh still takes four hours)

**Key Takeaway**: High refresh time with local processing almost always means broken folding. Fix by reordering steps so folding-breaking operations come last, then verify with View Native Query.

---

## Scenario 3: Flat table to star schema

**Scenario**: An analyst inherits a model built from one 60-column spreadsheet containing sales transactions with customer, product, and store details repeated on every row. Measures are slow, filters behave inconsistently, and the file is 800 MB.

**Solution Pattern**:
- Split into a **fact table** (transaction grain: date, keys, measures) and **dimension tables** for customer, product, store, and date
- Create the dimensions in Power Query by removing duplicates on the key columns
- Establish **one-to-many relationships** from dimensions to the fact, single-direction filtering
- Create and **mark a date table**
- Remove high-cardinality columns not needed for analysis, which is usually the largest single size reduction
- Set data types correctly and disable Auto Date/Time

**Common Distractors**:
- Adding calculated columns to the flat table (increases size, does not fix filtering)
- Switching to DirectQuery (moves the problem to the source)
- Reducing the visual count (the model is the problem)

**Key Takeaway**: Star schema is the assumed correct model. The size win usually comes from removing high-cardinality columns and eliminating repetition, not from compression settings.

---

## Scenario 4: Calculated column versus measure

**Scenario**: An analyst creates a calculated column `Profit Margin = (Sales[Revenue] - Sales[Cost]) / Sales[Revenue]` and puts it in a card visual with an average aggregation. Finance reports the number is wrong at every level except individual rows.

**Solution Pattern**:
- Replace with a **measure**: `Profit Margin = DIVIDE( SUM(Sales[Revenue]) - SUM(Sales[Cost]), SUM(Sales[Revenue]) )`
- The measure evaluates in the current filter context, aggregating first and then dividing, which is the correct order for a ratio
- Use **DIVIDE** rather than the `/` operator to handle division by zero
- Delete the calculated column to reclaim model memory

**Common Distractors**:
- Changing the visual aggregation to sum (summing percentages is worse)
- Adding a second calculated column (compounds the same error)
- Using AVERAGEX over the fact table (mathematically an average of ratios, not the ratio of totals; occasionally what is wanted, but not here)

**Key Takeaway**: Ratios must be measures. Averaging a row-level ratio gives the average of ratios, not the ratio of aggregates. This is the single most common real-world DAX error and it appears on the exam.

---

## Scenario 5: Row-level security that must scale

**Scenario**: Two hundred regional managers must each see only their own region. Creating 200 static roles is unmanageable. The organization has an employee table mapping each manager's email to their region.

**Solution Pattern**:
- One **dynamic RLS role** with a filter on the security dimension: `[Email] = USERPRINCIPALNAME()`
- Relationship from the security table to the region dimension, propagating to the fact
- Test with **View As** specifying a user, then test as a real Viewer through the app
- Ensure the relationship direction actually filters the fact table; a common failure is the filter stopping at the dimension
- Remember that Contributors and above bypass RLS in the workspace, so viewers must be assigned the Viewer role or given access through the app

**Common Distractors**:
- Two hundred static roles (works, unmanageable, and the scenario rules it out)
- Filtering in the report with a slicer (not security; users can change it)
- Object-level security (hides tables and columns, not rows)

**Key Takeaway**: Dynamic RLS with USERPRINCIPALNAME plus a security dimension is the scalable pattern. Testing must include a real viewer, because the author never sees RLS applied in the workspace.

---

## Scenario 6: Time intelligence returning blanks

**Scenario**: A `SAMEPERIODLASTYEAR` measure returns blank for every row. The model has a `Date` column on the fact table and no separate date table.

**Solution Pattern**:
- Create a dedicated **date table** covering a contiguous range from the earliest to latest fact date, including full years
- **Mark it as a date table** in the model
- Relate it one-to-many to the fact table's date column
- Rewrite the measure to reference the date table's date column
- Turn off Auto Date/Time, which creates hidden per-column date tables and bloats the model

**Common Distractors**:
- Wrapping the measure in CALCULATE with extra filters (does not supply the missing date dimension)
- Changing the data type of the fact date column (necessary but not sufficient)
- Relying on Auto Date/Time (it exists, but produces hidden tables and does not support the marked-date-table behavior these functions expect)

**Key Takeaway**: Time intelligence functions require a marked date table with a contiguous, complete date range. Blank results from time intelligence almost always mean the date table is missing, unmarked, or has gaps.

---

## Scenario 7: Distributing a report to 3,000 people

**Scenario**: A finance report must reach 3,000 employees across four departments, each seeing only their department's page. Report authors are a team of five who need to keep editing without disrupting consumers.

**Solution Pattern**:
- Authors work in a **workspace** as Members or Contributors
- Publish an **app** with **audiences**, one per department, each seeing the relevant pages
- Consumers get the app, not workspace access, so authoring changes do not appear until the app is republished
- **Row-level security** for row-level restrictions within a shared page
- Licence check: consumers need Power BI Pro, or the content must sit on Premium Per User or a Fabric capacity where free users can consume

**Common Distractors**:
- Sharing the report directly with 3,000 users (unmanageable, and edits are immediately visible)
- Four separate workspaces (duplicates the model and the maintenance)
- Giving consumers Viewer access to the workspace (works, but they then see work in progress and there is no audience segmentation)

**Key Takeaway**: Apps with audiences are the governed distribution mechanism. Workspace access is for authors; app access is for consumers. Licensing is frequently the hidden constraint in these questions.

---

## Scenario 8: Diagnosing a slow report page

**Scenario**: One report page takes 25 seconds to render while others are instant. The model is Import mode and reasonably sized.

**Solution Pattern**:
- Run **Performance Analyzer** on the page and identify whether time is in DAX query, visual display, or other
- If DAX query dominates, copy the query into DAX Studio and examine the plan
- Common causes: a measure using an iterator over a large fact table unnecessarily, bidirectional relationships creating expensive filter propagation, a visual with very high cardinality on an axis, or too many visuals on one page
- Fixes: rewrite the measure with variables to avoid repeated evaluation, replace bidirectional with single-direction plus CROSSFILTER where needed, reduce displayed cardinality, and split the page

**Common Distractors**:
- Switching to DirectQuery (almost always slower for this)
- Adding more visuals to spread load (each visual is a separate query)
- Increasing capacity (masks a model problem)

**Key Takeaway**: Performance Analyzer first, then decide whether the problem is the model, the measure, or the visual. The exam expects the diagnostic step, not a guess at a fix.

---

## Related

- [Practice plan](./practice-plan.md)
- [Strategy](./strategy.md)
- [Notes](./notes/)
- [Practice questions](../../../resources/practice-questions/azure-power-bi-pl-300.md)
