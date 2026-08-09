---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 6 min
---

# PL-300 Study Strategy

## Build, do not read

PL-300 is the most hands-on-rewarding exam in the Microsoft data track. Questions describe a model, a measure, or a report configuration and ask what happens or what to change. If you have built these things, you can reason it out. If you have only read about them, the options all look plausible.

Power BI Desktop is free and needs no cloud account for most of the modeling and DAX work. There is no good reason to study this exam without it open.

## Phase 1: Prepare (week 1-2)

The two topics that carry disproportionate marks:

**Storage mode selection.** Import unless something forbids it. DirectQuery when data must be current to the second or is too large to import, accepting slower interaction and DAX limitations. Dual for dimensions that serve both. Direct Lake for Fabric lakehouse data when you want import-like performance without an import step.

**Query folding.** Steps that fold are pushed to the source; steps that break folding force everything after them to process locally. Breaking folding early on a large source is the classic performance mistake, and incremental refresh requires folding to work at all. Know which operations typically break it: adding an index column, merging with a non-foldable source, and most custom M functions.

## Phase 2: Model (week 3)

**Star schema is the assumed answer.** When a question shows a flat table or a snowflake and asks how to improve the model, the answer usually involves creating dimensions and reducing relationship complexity.

Relationship rules that get tested:
- Single-direction cross-filtering by default; bidirectional creates ambiguity and is a common wrong answer
- Only one active relationship between two tables; use USERELATIONSHIP inside CALCULATE for the others
- Many-to-many relationships have specific behaviors and are usually a sign the model needs a bridge dimension
- Time intelligence requires a **marked date table** with a contiguous date range

## Phase 3: DAX (week 4)

Understand **context** before functions.

- **Row context** exists in calculated columns and inside iterators. It knows the current row.
- **Filter context** comes from visuals, slicers, filters, and relationships. It knows which rows are visible.
- **CALCULATE** is the function that modifies filter context, and it is behind almost every non-trivial measure.

Practise reading a measure and stating what filter context it evaluates in. That skill answers most DAX questions directly.

Calculated column versus measure: a calculated column is computed at refresh and stored in the model, consuming memory and fixed at row level. A measure is computed at query time in the current filter context. If a value must respond to slicers, it must be a measure.

## Phase 4: Visualize (week 5)

Two lines of questions:
- **Which visual** answers a stated business question. Learn the standard mapping: trend over time is a line chart, part-to-whole is limited, comparison across categories is a bar chart, correlation is a scatter, contribution analysis is key influencers or decomposition tree.
- **How interactivity is configured**: drillthrough needs a target page with the right field; bookmarks capture state including the selection pane; report page tooltips need the page size set to tooltip.

Accessibility appears reliably: alt text, tab order, and not relying on colour alone.

## Phase 5: Manage (week 6)

Workspace roles are directly testable. Learn what each can do:

| Role | Can |
|---|---|
| **Admin** | Everything including deleting the workspace and managing access |
| **Member** | Add members below admin, publish and update apps, share content |
| **Contributor** | Create and edit content, schedule refresh; cannot publish an app |
| **Viewer** | View and interact only; RLS applies to viewers |

Row-level security applies to Viewers. Members and Contributors bypass it in the workspace, which is a favourite exam point: RLS must be tested by a real viewer or through the app, not by the author.

## Common traps

| Trap | Reality |
|---|---|
| Using a calculated column where a measure is needed | Calculated columns do not respond to slicers |
| Bidirectional cross-filtering as a default fix | Creates ambiguity; usually the wrong answer |
| Time intelligence without a marked date table | Functions return unexpected results |
| Assuming RLS protects the author | Contributors and above bypass RLS in the workspace |
| Ignoring query folding | Breaks incremental refresh and destroys performance at scale |
| DirectQuery for everything "to stay current" | Slower and imposes DAX restrictions; Import is the default for a reason |
| Sharing a report instead of publishing an app | Harder to govern at scale, and the exam prefers apps for broad distribution |

## Exam day

- 100 minutes, roughly 40-60 items, often with a case study section.
- Some deliveries include a hands-on lab. If one appears, budget 20-30 minutes and do it before agonizing over multiple choice.
- Read DAX questions twice: once for what the measure does, once for what filter context it runs in.
- Nothing blank; no wrong-answer penalty.

## Related

- [Practice plan](./practice-plan.md)
- [Scenarios](./scenarios.md)
- [Fact sheet](./fact-sheet.md)
- [Study strategies](../../../resources/study-strategies.md)
