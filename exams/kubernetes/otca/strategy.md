---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 5 min
---

# OTCA Study Strategy

## Follow the weights

| Domain | Weight | Study time |
|---|---:|---|
| API and SDK | 46% | Roughly half |
| Collector | 26% | Roughly a quarter |
| Fundamentals | 18% | A week |
| Maintaining and debugging | 10% | Folded into the others |

Candidates often spend their time on Collector YAML because it is concrete, and under-study instrumentation because it is language-specific. The weighting says do the opposite.

## The documentation is the syllabus

OTCA tracks the official OpenTelemetry documentation closely. Where a concept has a documentation page, expect a question shaped by that page. Read the concepts section, the Collector section, and the semantic conventions overview directly rather than relying on third-party summaries, which often lag behind specification changes.

## Phase 1: Get the mental model right

Three distinctions that unlock most questions:

**API versus SDK.** The API is the interface your code and third-party libraries call. The SDK is the implementation that samples, batches, and exports. A library instrumented with the API produces nothing unless the application configures an SDK. This design is deliberate: it lets libraries ship instrumentation without forcing a telemetry pipeline on their users.

**Signal independence.** Traces, metrics, and logs have separate providers, separate processors, and separate pipelines in the Collector. They are correlated by shared context and resource attributes, not by being one stream.

**Context is the connective tissue.** A trace spans processes only because context propagates. Almost every "why is my trace broken" question is a propagation question.

## Phase 2: Instruments

Learn to map a described measurement to an instrument:

| Measurement | Instrument |
|---|---|
| A value that only increases (requests served, bytes sent) | **Counter** |
| A value that goes up and down (active connections, queue depth) | **Up-down counter** |
| A distribution you want percentiles from (request duration) | **Histogram** |
| A current value read on demand (CPU temperature, memory in use) | **Gauge** (asynchronous) |

Synchronous instruments record inline where the event happens. Asynchronous (observable) instruments register a callback the SDK invokes at collection time, which suits values you sample rather than count.

## Phase 3: Collector ordering

Processors run in declared order, and the canonical ordering is testable:

1. **memory_limiter** first, so it can shed load before other processors allocate
2. Any processor that drops data (filter, sampling) early, to avoid work on data you discard
3. **attributes / resource / transform** in the middle
4. **batch** last, so batching happens on the final shape of the data

Deployment patterns: an **agent** runs close to the workload (DaemonSet or sidecar) and handles local enrichment such as `k8sattributes`. A **gateway** is a standalone deployment handling aggregation, tail sampling, and export to backends. Tail sampling requires all spans of a trace to reach the same instance, which is why it belongs in a gateway and needs a load-balancing exporter in front of it.

## Phase 4: Cardinality and cost

The practical theme running through the fundamentals domain. Every unique combination of metric attributes is a separate time series. Adding user ID, request ID, or a raw URL path as an attribute can turn ten series into ten million.

Controls: avoid unbounded attributes, use views to drop or aggregate attributes, use the filter and transform processors, and template URL paths into route patterns.

## Common traps

| Trap | Reality |
|---|---|
| Assuming the API records telemetry | Without an SDK, API calls are no-ops |
| Putting batch before memory_limiter | Memory limiter must be first to shed load effectively |
| Using tail sampling on an agent | All spans of a trace must reach one instance; that means a gateway |
| Treating baggage as secure | Baggage propagates across service boundaries in headers; do not put secrets in it |
| Confusing span links with parent-child | Links relate spans without a causal parent relationship, as in batch processing |
| Using a gauge where a counter fits | Counters are monotonic and support rate calculations; gauges do not |
| Ignoring temporality | Delta and cumulative behave differently on restart and in aggregation |

## Exam day

- 90 minutes for 60 questions is 90 seconds each, comfortable if you are not second-guessing.
- Knowledge-based, so no terminal and no kubectl. Do not spend study time on command memorization.
- Multiple-select questions state how many to choose; read that number.
- 75% pass means roughly 45 of 60. There is room for a handful of misses.
- One free retake is included, which is worth remembering if you are debating readiness.

## Related

- [Practice plan](./practice-plan.md)
- [Scenarios](./scenarios.md)
- [Fact sheet](./fact-sheet.md)
- [Observability basics](../../../learn/concepts/observability-basics.md)
