---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 6 min
---

# Microsoft Power BI Data Analyst (PL-300)

Prepare data, model it, visualize it, and manage the result. PL-300 is the analyst-tier certification and the highest-volume analytics exam Microsoft runs.

For this repo it fills a real gap: [DP-600](../dp-600/) and [DP-700](../dp-700/) cover Fabric engineering, but nothing covered the analyst layer where most people actually enter data work.

## Exam Details

- **Exam Code:** PL-300
- **Level:** Associate
- **Duration:** 100 minutes
- **Questions:** Typically 40-60, often including a case study
- **Passing Score:** 700/1000
- **Cost:** USD 165, varies by region
- **Prerequisites:** None formal
- **Validity:** 1 year, free online renewal

Full detail in the [fact sheet](./fact-sheet.md).

## Domains

| Domain | Weight | Notes |
|--------|-------:|-------|
| Prepare the data | 25-30% | [01](./notes/01-prepare-the-data.md) |
| Model the data | 25-30% | [02](./notes/02-model-the-data.md) |
| Visualize and analyze the data | 25-30% | [03](./notes/03-visualize-and-analyze.md) |
| Manage and secure Power BI | 15-20% | [04](./notes/04-manage-and-secure.md) |

## The two topics that decide most passes

**Star schema.** The exam assumes it throughout. If you model as a single flat table or as a normalized snowflake, half the modeling and DAX questions become confusing, because the correct answers all presume fact tables surrounded by dimensions with single-direction relationships.

**Filter context.** Almost every DAX question is really a question about what filters apply when a measure evaluates, and how CALCULATE changes them. Candidates who memorize function syntax without understanding context struggle; candidates who understand context can reason out functions they have not memorized.

Everything else is learnable by doing.

## Hands-on is not optional

Power BI Desktop is free. Download it, get a sample dataset (AdventureWorks, Contoso, or any CSV you care about), and build:

- An import model with a proper date table, marked as a date table
- A star schema from a flat file, splitting dimensions out by hand
- Measures using CALCULATE with a filter modifier, then the same logic with variables
- A time intelligence measure, then break it by removing the date table and see what happens
- Row-level security with a dynamic role using USERPRINCIPALNAME, tested with View As
- A report with drillthrough, a bookmark, and a report page tooltip
- A deployment pipeline moving content between stages

Reading about DAX does not produce DAX ability. The exam knows the difference.

## Study sequence

1. **Power Query and storage modes** - get data in, understand query folding.
2. **Star schema and relationships** - before any DAX.
3. **DAX: context, then CALCULATE, then time intelligence.**
4. **Visuals and report interactivity.**
5. **Service: workspaces, sharing, refresh, RLS in practice, deployment pipelines.**

Schedule in the [practice plan](./practice-plan.md).

## Study resources

- **[📖 PL-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300)** - authoritative outline
- **[📖 Power BI guidance: star schema](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)** - read this early
- **[📖 DAX reference](https://learn.microsoft.com/en-us/dax/)** - function reference
- **[📖 Microsoft Learn PL-300 path](https://learn.microsoft.com/en-us/training/browse/?terms=PL-300)** - free official modules
- [Practice questions](../../../resources/practice-questions/azure-power-bi-pl-300.md) - question bank in this repo

## Related

- [DP-600 Fabric Analytics Engineer](../dp-600/) - the next step up
- [DP-700 Fabric Data Engineer](../dp-700/)
- [DP-900 Azure Data Fundamentals](../dp-900/)
- [DP-203 Azure Data Engineer](../dp-203/)
- [Data Engineer roadmap](../../../resources/certification-roadmap-data-engineer.md)
- [Databases topic](../../../topics/databases.md)
