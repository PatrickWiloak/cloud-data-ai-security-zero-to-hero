---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 6 min
---

# OpenTelemetry Certified Associate (OTCA)

The vendor-neutral observability certification. OTCA covers instrumenting applications with the OpenTelemetry API and SDK, running the Collector, and reasoning about traces, metrics, and logs as a system.

This is the first observability certification in the repo. It is also, arguably, the most transferable one available: OpenTelemetry is the ingestion standard for Datadog, Grafana, Splunk, Honeycomb, New Relic, AWS, Azure, and Google Cloud. Learn OTel and you have learned the layer underneath every observability vendor.

## Exam Details

- **Exam Code:** OTCA
- **Duration:** 90 minutes
- **Questions:** 60, multiple choice and multiple select
- **Passing Score:** 75%
- **Cost:** USD 250, includes one free retake
- **Validity:** 2 years
- **Prerequisites:** None
- **Format:** Knowledge-based, not hands-on

Full detail in the [fact sheet](./fact-sheet.md).

## Domains

| Domain | Weight | Notes |
|--------|-------:|-------|
| The OpenTelemetry API and SDK | 46% | [01](./notes/01-api-and-sdk.md) |
| The OpenTelemetry Collector | 26% | [02](./notes/02-collector.md) |
| Fundamentals of Observability | 18% | [03](./notes/03-observability-fundamentals.md) |
| Maintaining and Debugging Observability Pipelines | 10% | [04](./notes/04-maintaining-and-debugging.md) |

The weighting is unusually lopsided. Nearly half the exam is instrumentation, and a quarter is the Collector. Together they are 72%, so that is where the study time goes.

## What makes it tricky

OTCA is a knowledge exam like [KCNA](../kcna/), not a hands-on exam like [CKA](../cka/). But the questions are specific: they ask which processor belongs in which pipeline position, what happens to context when a propagator is missing, and which instrument type fits a given measurement.

The three areas that catch people:

1. **API versus SDK.** The API is what your code calls. The SDK is the implementation that actually records and exports. Without an SDK configured, API calls are no-ops. Library authors depend on the API only; applications wire up the SDK.
2. **Instrument selection.** Counter, up-down counter, histogram, and gauge each fit specific measurement shapes, with synchronous and asynchronous variants. Questions describe a measurement and ask which instrument to use.
3. **Collector component ordering.** Processors run in the order declared. `memory_limiter` first, `batch` last is the canonical guidance, and the exam tests whether you know why.

## Study sequence

1. **Signals and the data model** - traces, metrics, logs, and how they relate.
2. **API and SDK** - instrumentation, context propagation, instruments, sampling.
3. **Collector** - components, pipelines, deployment patterns.
4. **Fundamentals** - cardinality, SLOs, golden signals, semantic conventions.
5. **Debugging** - where telemetry gets lost.

Schedule in the [practice plan](./practice-plan.md).

## Hands-on helps

Not required by the exam format, but the fastest way to make it stick:

- Run the Collector locally with an OTLP receiver and a debug exporter, and watch spans arrive
- Instrument a two-service application manually and confirm the trace joins across the boundary
- Break propagation deliberately by dropping the `traceparent` header and see two disconnected traces
- Add an attribute with high cardinality to a metric and watch the series count explode
- Deploy the OpenTelemetry Operator and use auto-instrumentation injection

## Study resources

- **[📖 OpenTelemetry documentation](https://opentelemetry.io/docs/)** - the primary source; the exam tracks it closely
- **[📖 OTCA curriculum](https://github.com/cncf/curriculum)** - published domains and competencies
- **[📖 Collector documentation](https://opentelemetry.io/docs/collector/)** - architecture and configuration
- **[📖 Semantic conventions](https://opentelemetry.io/docs/specs/semconv/)** - attribute naming standard
- [Practice questions](../../../resources/practice-questions/cncf-otca.md) - question bank in this repo

## Related

- [PCA Prometheus Certified Associate](../pca/) - metrics depth
- [KCNA](../kcna/) - the cloud native fundamentals below this
- [CKA](../cka/) - Kubernetes operations
- [CNPA Platform Engineering Associate](../cnpa/) - the platform layer that consumes this
- [Observability topic](../../../topics/observability.md)
- [Set up a monitoring stack](../../../resources/hands-on-projects/setup-monitoring-stack.md)
