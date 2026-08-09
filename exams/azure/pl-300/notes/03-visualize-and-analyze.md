---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 10 min
---

# 03 - Visualize and analyze

**Domain 3: Visualize and analyze the data (25-30%)**

---

## Choosing a visual

The exam asks which visual answers a stated question. The mapping is conventional:

| Question shape | Visual |
|---|---|
| Trend over time | Line chart, or area chart for cumulative |
| Comparison across categories | Bar or column chart |
| Ranking | Sorted bar chart |
| Part of a whole, few categories | Stacked bar, or pie only for two or three slices |
| Relationship between two measures | Scatter chart, with a third measure as bubble size |
| Distribution | Histogram, or box plot as a custom visual |
| A single number against a target | Card, KPI, or gauge |
| Geographic pattern | Map, filled map, or shape map |
| Detail rows | Table; matrix when you need row and column grouping |
| What drives a metric | Key influencers |
| Where a total breaks down | Decomposition tree |

Pie and donut charts are correct answers less often than candidates expect. A bar chart usually communicates the same comparison more accurately.

---

## Filtering

Four levels, narrowest first:

1. **Visual-level filter** - one visual
2. **Page-level filter** - all visuals on a page
3. **Report-level filter** - every page
4. **Slicer** - a visual the user controls, filtering the page by default

**Sync slicers** apply one slicer across several pages, configured in the Sync slicers pane with separate visibility and sync settings.

**Edit interactions** controls whether selecting in one visual filters, highlights, or does nothing to each other visual on the page.

**Filter pane** formatting controls what users can see and change: hidden filters, locked filters, and applied filter cards.

---

## Navigation and interactivity

- **Drilldown** moves through a hierarchy within one visual.
- **Drillthrough** moves to a detail page filtered by the selected context. The target page needs the drillthrough field configured; keep-all-filters is a setting.
- **Tooltips** show extra values on hover. A **report page tooltip** is a page sized as a tooltip and assigned to a visual, allowing rich hover content.
- **Bookmarks** capture report state: filters, slicer selections, sort, drill level, and visibility from the Selection pane. Combined with buttons they build show-and-hide toggles and guided navigation.
- **Buttons and page navigation** provide app-like movement between pages.
- **Personalize visuals** lets consumers change a visual without editing the report, when enabled.

---

## AI and analytical visuals

| Visual | Answers |
|---|---|
| **Key influencers** | Which factors most affect a metric or outcome |
| **Decomposition tree** | Where a total breaks down, with AI-suggested next splits |
| **Smart narrative** | An automatically written summary of the visual or page |
| **Q&A** | Natural language questions against the model |
| **Anomaly detection** | Outliers in a time series, with explanations |

**Analytics pane** adds reference lines: constant, average, median, percentile, trend, forecast, and min/max.

**Quick measures** generate common DAX without writing it, which is also a good way to learn patterns.

Q&A quality depends on the model: table and column names, synonyms defined in the Q&A setup, and hidden technical columns all matter.

---

## Accessibility

Reliably tested. A report should be usable without relying on color or a mouse.

- **Alt text** on every meaningful visual
- **Tab order** set in the Selection pane so keyboard navigation is logical
- **Color contrast** sufficient, and never the only means of conveying meaning
- Themes with accessible palettes
- Avoid excessive visuals per page; each is another stop for a screen reader
- Titles and labels that read as sentences

---

## Other output paths

- **Analyze in Excel** connects Excel PivotTables to the semantic model.
- **Paginated reports** are the right tool for pixel-perfect, printable, multi-page output such as invoices and statements, rather than interactive exploration.
- **Subscriptions** email a snapshot on a schedule.
- **Export** to PDF, PowerPoint, or Excel, with governance settings controlling what is permitted.

---

## Key terms

- **Drillthrough** - navigation to a detail page filtered by the context selected in the source visual
- **Report page tooltip** - a page sized as a tooltip and assigned to a visual for rich hover content
- **Bookmark** - a saved report state including filters, selections, sort, drill level, and visual visibility
- **Selection pane** - the pane controlling visual visibility and tab order
- **Sync slicer** - a slicer whose selection applies across multiple report pages
- **Edit interactions** - the setting controlling whether a selection in one visual filters, highlights, or ignores another
- **Key influencers** - an AI visual identifying which factors most affect a chosen metric or outcome
- **Decomposition tree** - an AI visual breaking a measure down across dimensions with suggested next splits
- **Smart narrative** - an automatically generated text summary of a visual or report page
- **Anomaly detection** - a time-series analytic identifying outliers and offering explanations
- **Analytics pane** - the pane adding reference, trend, and forecast lines to a visual
- **Personalize visuals** - a setting letting consumers modify a visual without edit rights on the report
- **Paginated report** - a pixel-perfect, printable report format suited to operational documents rather than exploration
- **Tab order** - the keyboard navigation sequence through visuals, set in the Selection pane

---

## Related

- [Notes 04: manage and secure](./04-manage-and-secure.md)
- [Scenarios](../scenarios.md) - scenario 8
