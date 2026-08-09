---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 12 min
---

# Microsoft Power BI Data Analyst (PL-300) Fact Sheet

## Exam Overview

**Exam Code:** PL-300
**Exam Name:** Microsoft Power BI Data Analyst
**Level:** Associate
**Duration:** 100 minutes
**Format:** Multiple choice, multiple select, drag-and-drop, case studies, and occasionally a lab
**Questions:** Typically 40-60
**Passing Score:** 700 out of 1000
**Cost:** USD 165 (varies by country)
**Valid For:** 1 year, renewable free online through Microsoft Learn
**Delivery:** Pearson VUE, test center or online proctored
**Prerequisites:** None formally; hands-on Power BI Desktop experience strongly expected

> **Verify before booking.** Confirm the current outline and price on the official pages below.

**[📖 PL-300 certification page](https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/)** - registration and renewal
**[📖 PL-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300)** - the authoritative skills-measured outline
**[📖 Power BI documentation](https://learn.microsoft.com/en-us/power-bi/)** - product reference

## Why this exam is in this repo

The repo covers [DP-600](../dp-600/) and [DP-700](../dp-700/) for Fabric engineering, and [DP-203](../dp-203/) for data engineering, but had no analyst-tier certification. PL-300 is the highest-volume analytics certification in the market and the natural on-ramp to the Fabric track: the semantic modeling and DAX knowledge it builds is a direct prerequisite for DP-600.

It also fills a career-path gap. Not everyone entering data work starts as an engineer; many start as an analyst.

## Target Audience

- Data analysts building reports and semantic models
- Business intelligence developers
- Finance, operations, and marketing professionals who own reporting
- Data engineers who need to understand the consumption layer
- Anyone heading toward [DP-600](../dp-600/)

## Exam Domains

### Domain 1: Prepare the data (25-30%)

**Key Concepts:**
- Connectivity: files, folders, databases, SharePoint, web, dataflows, OData, and the Fabric lakehouse
- Storage modes: Import, DirectQuery, Dual, and Direct Lake, and the trade-offs of each
- Composite models and table-level storage mode selection
- Power Query transformations: shape, filter, group, pivot and unpivot, split, merge, append
- Data profiling: column quality, distribution, and profile
- Handling errors, nulls, and inconsistent types
- Query folding: what it is, how to check it, and why breaking it matters
- Parameters and functions in Power Query
- Incremental refresh configuration and its RangeStart and RangeEnd requirement
- Dataflows Gen1 and Gen2 for reusable preparation
- The on-premises data gateway: standard versus personal mode

**[📖 Power Query documentation](https://learn.microsoft.com/en-us/power-query/)** - transformation reference
**[📖 Storage modes in Power BI](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-storage-mode)** - Import, DirectQuery, Dual

### Domain 2: Model the data (25-30%)

**Key Concepts:**
- Star schema design: fact and dimension tables, and why it beats a flat table
- Relationships: cardinality, cross-filter direction, active and inactive, bidirectional filtering risks
- Role-playing dimensions and USERELATIONSHIP
- Date table creation and marking, and why time intelligence needs one
- DAX fundamentals: calculated columns, measures, calculated tables, and when each is appropriate
- Filter context and row context; CALCULATE as the context-modifying function
- Iterator functions (SUMX, AVERAGEX) and when they are necessary
- Time intelligence: TOTALYTD, SAMEPERIODLASTYEAR, DATEADD, DATESYTD
- Variables in DAX for readability and performance
- Row-level security: static and dynamic roles, USERPRINCIPALNAME, and testing with View As
- Object-level security concepts
- Hierarchies, display folders, and field parameters
- Calculation groups
- Performance: Performance Analyzer, reducing cardinality, avoiding bidirectional filters, aggregations

**[📖 DAX reference](https://learn.microsoft.com/en-us/dax/)** - function reference
**[📖 Star schema guidance](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)** - the modeling approach the exam assumes

### Domain 3: Visualize and analyze the data (25-30%)

**Key Concepts:**
- Visual selection: which chart answers which question
- Formatting, conditional formatting, and the design pane
- Slicers, sync slicers, filters at visual, page, and report level, and the filter pane
- Drillthrough, drilldown, tooltips, and report page tooltips
- Bookmarks, selection pane, and buttons for navigation
- Custom and AppSource visuals, and organizational visual governance
- Accessibility: alt text, tab order, colour contrast, and report readability
- Mobile layouts
- AI visuals: key influencers, decomposition tree, smart narrative, Q&A, anomaly detection
- Quick measures and the quick measure suggestions experience
- Analyze in Excel, paginated report basics, and when a paginated report is the right tool
- Identifying outliers, trends, and correlations from a report

**[📖 Power BI visualizations](https://learn.microsoft.com/en-us/power-bi/visuals/)** - visual types and configuration
**[📖 Report accessibility](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-accessibility-creating-reports)** - accessible report design

### Domain 4: Manage and secure Power BI (15-20%)

**Key Concepts:**
- Workspaces: roles (Admin, Member, Contributor, Viewer) and what each can do
- Apps: publishing, audiences, and the difference between app and workspace access
- Sharing: reports, dashboards, links, and the security implications of each
- Semantic model settings: scheduled refresh, gateway binding, credentials, and refresh failures
- Row-level security applied through workspace and app membership
- Sensitivity labels on Power BI content and their inheritance
- Deployment pipelines: development, test, and production stages with rules
- Endorsement: promoted and certified content
- Usage metrics and audit
- Capacity concepts: Pro, Premium Per User, and Fabric capacity
- Managing the semantic model as a shared asset

**[📖 Power BI security](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-power-bi-security)** - workspace and content security
**[📖 Deployment pipelines](https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines)** - ALM for Power BI content

## Storage mode quick reference

| Mode | Data location | Refresh | Choose when |
|---|---|---|---|
| **Import** | Cached in the model | Scheduled or on demand | Best performance, data volume fits, latency tolerable |
| **DirectQuery** | Stays in the source | Query at interaction time | Near-real-time need, or volume too large to import |
| **Dual** | Both, decided per query | Both | Dimension tables serving both Import and DirectQuery facts |
| **Direct Lake** | Parquet in OneLake, read directly | No import step | Fabric lakehouse workloads needing import-like speed at scale |

## Related repo material

- [Notes](./notes/) - four notes, one per domain
- [Practice plan](./practice-plan.md) - 6-week schedule
- [Scenarios](./scenarios.md)
- [Strategy](./strategy.md)
- [DP-600 Fabric Analytics Engineer](../dp-600/) - the natural next step
- [DP-900 Azure Data Fundamentals](../dp-900/) - the fundamentals below this
- [Databases topic](../../../topics/databases.md)
