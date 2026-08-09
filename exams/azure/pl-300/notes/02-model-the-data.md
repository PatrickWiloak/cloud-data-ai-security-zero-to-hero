---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 13 min
---

# 02 - Model the data

**Domain 2: Model the data (25-30%)**

---

## Star schema

The assumed model shape throughout the exam.

- **Fact table**: the events being measured. Long and narrow: keys plus numeric measures, at a defined grain.
- **Dimension tables**: the things you slice by. Short and wide: a key plus descriptive attributes.
- **Relationships**: one-to-many from dimension to fact, filtering in a single direction, from the one side to the many side.

Why it beats a flat table: less repetition so a smaller model, unambiguous filter paths, and predictable DAX behavior. Why it beats a snowflake: fewer relationship hops means simpler filter propagation and faster queries; denormalize dimension levels into one table.

**Model size reduction**, in order of usual impact: remove columns you do not use (especially high-cardinality ones like transaction IDs and timestamps), reduce cardinality (split date and time into separate columns), summarize to the needed grain, and disable Auto Date/Time.

---

## Relationships

| Property | Options | Notes |
|---|---|---|
| **Cardinality** | One-to-many, one-to-one, many-to-many | One-to-many is the norm; many-to-many usually signals a missing bridge dimension |
| **Cross-filter direction** | Single, Both | Single by default; Both creates ambiguity and circular paths |
| **Active** | One active per table pair | Additional relationships are inactive until invoked |

**Role-playing dimensions**: a date table related to order date, ship date, and delivery date. Only one relationship can be active; the others are activated per measure with `USERELATIONSHIP` inside `CALCULATE`.

**Bidirectional filtering** is a common wrong answer. It solves an immediate problem and introduces ambiguity that produces wrong numbers elsewhere. Prefer single direction plus `CROSSFILTER` in specific measures.

---

## Date tables

Time intelligence requires a proper date table:

- A contiguous date range with no gaps, covering full years from the earliest to the latest date in the data
- One row per date
- **Marked as a date table** in the model
- Related to fact date columns

Create with `CALENDAR`, `CALENDARAUTO`, Power Query, or a source table. Turn **Auto Date/Time off**: it silently creates a hidden date table per date column, inflating the model and behaving inconsistently.

---

## DAX: the object types

| Object | Evaluated | Stored | Use for |
|---|---|---|---|
| **Calculated column** | At refresh, row by row | Yes, in the model | Values needed on an axis, in a slicer, or in a relationship |
| **Measure** | At query time, in filter context | No | Anything that must respond to slicers and filters, especially aggregations and ratios |
| **Calculated table** | At refresh | Yes | Date tables, bridge tables, disconnected parameter tables |

The recurring error: writing a ratio as a calculated column and then aggregating it. Averaging row-level ratios is not the ratio of totals. Ratios are measures.

---

## Context

**Row context** exists in a calculated column and inside an iterator. It knows the current row but does not filter the model by itself.

**Filter context** is the set of filters applied when a measure evaluates: visual axis, slicers, page and report filters, and filters propagating across relationships.

**Context transition** happens when `CALCULATE` is used inside a row context: the current row becomes a filter. This is why `CALCULATE(SUM(...))` inside an iterator behaves differently from a bare `SUM`.

**CALCULATE** is the central function. It evaluates an expression in a modified filter context:

```dax
Sales Europe = CALCULATE( SUM(Sales[Amount]), Geography[Region] = "Europe" )
Sales All Products = CALCULATE( SUM(Sales[Amount]), ALL(Product) )
Sales Keep Slicer = CALCULATE( SUM(Sales[Amount]), KEEPFILTERS(Product[Category] = "Bikes") )
```

Filter modifiers to know: `ALL`, `ALLEXCEPT`, `ALLSELECTED`, `REMOVEFILTERS`, `KEEPFILTERS`, `USERELATIONSHIP`, `CROSSFILTER`.

---

## Iterators and variables

**Iterators** (`SUMX`, `AVERAGEX`, `MAXX`, `RANKX`) evaluate an expression per row then aggregate. Necessary when the calculation must happen at row level before aggregating:

```dax
Total Revenue = SUMX( Sales, Sales[Quantity] * Sales[UnitPrice] )
```

**Variables** improve readability and avoid re-evaluating the same expression:

```dax
YoY Growth =
VAR CurrentSales = SUM(Sales[Amount])
VAR PriorSales = CALCULATE( SUM(Sales[Amount]), SAMEPERIODLASTYEAR('Date'[Date]) )
RETURN DIVIDE( CurrentSales - PriorSales, PriorSales )
```

A variable is evaluated once, in the filter context where it is defined, and does not change afterwards. That property is occasionally the point of a question.

---

## Time intelligence

`TOTALYTD`, `TOTALQTD`, `TOTALMTD`, `SAMEPERIODLASTYEAR`, `DATEADD`, `DATESYTD`, `PREVIOUSMONTH`, `PARALLELPERIOD`. All require a marked date table.

`DATEADD` shifts by a period; `SAMEPERIODLASTYEAR` is shorthand for a one-year shift. Blank results almost always mean a missing, unmarked, or gapped date table.

---

## Security in the model

**Row-level security**: roles containing DAX filter expressions on tables.

- **Static**: `[Region] = "Europe"`. One role per group, unmanageable at scale.
- **Dynamic**: `[Email] = USERPRINCIPALNAME()` against a security dimension that relates through to the fact. One role serves everyone.

Test with **View As** in Desktop, then verify as a real Viewer in the service, because workspace Contributors and above bypass RLS.

**Object-level security** hides tables or columns entirely from a role, including from field lists and metadata. Configured through external tools rather than the Desktop UI.

---

## Performance

- **Performance Analyzer** shows DAX query, visual display, and other time per visual
- Reduce cardinality, remove unused columns, and avoid unnecessary calculated columns
- Avoid bidirectional relationships
- Use **aggregations** over large fact tables in composite models
- Use variables to avoid repeated evaluation
- **Calculation groups** replace many near-identical measures with one reusable set of calculation items

---

## Key terms

- **Star schema** - a model of a central fact table surrounded by dimension tables joined one-to-many
- **Fact table** - the table of measured events, defined at a specific grain, holding keys and numeric measures
- **Dimension table** - a descriptive table used to slice and filter facts
- **Cross-filter direction** - whether a relationship propagates filters one way or both ways
- **Inactive relationship** - an additional relationship between two tables, invoked with USERELATIONSHIP
- **Role-playing dimension** - a single dimension related multiple times to the same fact, such as a date table used for order and ship dates
- **Marked date table** - a date table designated in the model so time intelligence functions behave correctly
- **Calculated column** - a column computed at refresh and stored in the model, fixed at row level
- **Measure** - a calculation evaluated at query time in the current filter context
- **Row context** - the evaluation context knowing the current row, present in calculated columns and iterators
- **Filter context** - the set of filters applied when an expression evaluates, coming from visuals, slicers, and relationships
- **Context transition** - the conversion of row context into filter context that CALCULATE performs
- **CALCULATE** - the DAX function that evaluates an expression in a modified filter context
- **Iterator** - a function such as SUMX that evaluates an expression per row before aggregating
- **Calculation group** - a reusable set of calculation items applied across measures, replacing many similar measures
- **Row-level security** - DAX filter expressions in roles that restrict which rows a user can see
- **Object-level security** - restriction hiding entire tables or columns from a role, including from metadata

---

## Related

- [Notes 03: visualize and analyze](./03-visualize-and-analyze.md)
- [Scenarios](../scenarios.md) - scenarios 3, 4, 5, and 6
