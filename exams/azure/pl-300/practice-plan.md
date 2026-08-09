---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 5 min
---

# PL-300 Study Plan

Six weeks at 6-8 hours per week. Every week is built around Power BI Desktop, which is free. Use a sample dataset you find interesting; motivation matters more than which dataset.

## Week 1: Getting data in

- [ ] Read the [PL-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300)
- [ ] Connect to files, folders, a database, SharePoint, and the web
- [ ] Storage modes: Import, DirectQuery, Dual, Direct Lake, and their trade-offs
- [ ] Data profiling: column quality, distribution, profile
- [ ] Core Power Query transformations: filter, group by, pivot, unpivot, split, merge, append
- [ ] Handling errors, nulls, and type mismatches
- [ ] **Build**: import a messy CSV and clean it entirely in Power Query, no manual edits
- [ ] Review Notes: `notes/01-prepare-the-data.md`

## Week 2: Query folding, parameters, refresh

- [ ] Query folding: what folds, how to check with View Native Query, and which steps break it
- [ ] Parameters and custom functions
- [ ] Incremental refresh: RangeStart and RangeEnd, partitioning, and prerequisites
- [ ] Dataflows Gen1 and Gen2, and when to centralize preparation
- [ ] On-premises data gateway: standard versus personal
- [ ] **Build**: a parameterized query and a function applied across a folder of files

## Week 3: Modeling

- [ ] Star schema: facts, dimensions, and why flat tables fail
- [ ] Split a flat table into a star schema by hand
- [ ] Relationships: cardinality, cross-filter direction, active versus inactive
- [ ] Why bidirectional filtering is usually the wrong answer
- [ ] Role-playing dimensions and USERELATIONSHIP
- [ ] Create a date table and mark it as a date table
- [ ] Hierarchies, display folders, field parameters
- [ ] **Build**: convert a flat table into a star schema with a working date dimension
- [ ] Review Notes: `notes/02-model-the-data.md`

## Week 4: DAX

- [ ] Calculated column versus measure versus calculated table, and the storage consequence
- [ ] Row context and filter context, and how they interact
- [ ] CALCULATE: filter modifiers, ALL, ALLEXCEPT, KEEPFILTERS, REMOVEFILTERS
- [ ] Iterators: SUMX, AVERAGEX, and when an aggregation is not enough
- [ ] Time intelligence: TOTALYTD, SAMEPERIODLASTYEAR, DATEADD, DATESYTD
- [ ] Variables for readability and to avoid repeated evaluation
- [ ] Calculation groups
- [ ] **Build**: five measures of increasing complexity, each rewritten with variables
- [ ] Practise reading a measure and predicting its result before running it

## Week 5: Visualization and analysis

- [ ] Visual selection: which chart answers which question
- [ ] Filters: visual, page, report, and the filter pane
- [ ] Slicers and sync slicers
- [ ] Drillthrough, drilldown, tooltips, and report page tooltips
- [ ] Bookmarks, selection pane, and buttons
- [ ] AI visuals: key influencers, decomposition tree, smart narrative, Q&A, anomaly detection
- [ ] Accessibility: alt text, tab order, contrast
- [ ] Performance Analyzer and reading its output
- [ ] **Build**: a three-page report with drillthrough, a bookmark-driven view toggle, and a report page tooltip
- [ ] Review Notes: `notes/03-visualize-and-analyze.md`

## Week 6: Service, security, and review

- [ ] Workspace roles and what each can do
- [ ] Apps, audiences, and how app access differs from workspace access
- [ ] Sharing methods and their security implications
- [ ] Scheduled refresh, gateway binding, credentials, and diagnosing refresh failures
- [ ] Row-level security: static and dynamic, USERPRINCIPALNAME, View As testing
- [ ] Sensitivity labels on Power BI content
- [ ] Deployment pipelines and rules
- [ ] Endorsement: promoted versus certified
- [ ] **Build**: a dynamic RLS role, tested with View As, then published and tested as a real viewer
- [ ] Review Notes: `notes/04-manage-and-secure.md`
- [ ] Work every scenario in [scenarios.md](./scenarios.md)
- [ ] Two full timed practice exams

## Readiness check

- [ ] Explain when DirectQuery is required and what it costs you
- [ ] Explain query folding and name three steps that break it
- [ ] Draw a star schema for a given business process
- [ ] Explain the difference between a calculated column and a measure, including storage impact
- [ ] Predict the result of a CALCULATE expression with an ALL modifier
- [ ] Explain why time intelligence needs a marked date table
- [ ] Write a dynamic RLS expression and describe how to test it
- [ ] Name the workspace role that can publish an app
