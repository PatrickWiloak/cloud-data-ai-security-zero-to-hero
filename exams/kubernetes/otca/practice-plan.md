---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 5 min
---

# OTCA Study Plan

Five weeks at 5-7 hours per week. Weight your effort to the domain weights: API and SDK plus Collector are 72% of the exam.

## Week 1: Signals and the data model

- [ ] Read the OpenTelemetry observability primer and concepts pages
- [ ] Traces: spans, span context, span kinds, attributes, events, links, status
- [ ] Metrics: the data model, data points, temporality
- [ ] Logs: the log data model and how it differs from a log line
- [ ] Resources and resource detection
- [ ] Semantic conventions: why standardized names matter, and the main namespaces
- [ ] **Lab**: run the Collector locally with an OTLP receiver and debug exporter, send a trace
- [ ] Review Notes: `notes/03-observability-fundamentals.md`

## Week 2: Instrumentation with the API and SDK

- [ ] API versus SDK: what each provides, and why an API call without an SDK is a no-op
- [ ] TracerProvider, Tracer, and span creation and nesting
- [ ] Span processors: simple versus batch, and their trade-offs
- [ ] Exporters: OTLP gRPC and HTTP, console, and vendor exporters
- [ ] Automatic (zero-code) instrumentation versus manual
- [ ] Instrumentation libraries for common frameworks
- [ ] Environment variable configuration (`OTEL_*`)
- [ ] **Lab**: manually instrument a small service, add attributes and an event to a span
- [ ] Review Notes: `notes/01-api-and-sdk.md`

## Week 3: Context, metrics instruments, and sampling

- [ ] Context propagation and the W3C Trace Context standard
- [ ] `traceparent` and `tracestate` header format
- [ ] Propagators, and what happens when they are missing or mismatched
- [ ] Baggage: what it carries and why it is not a security boundary
- [ ] Metric instruments: counter, up-down counter, histogram, gauge
- [ ] Synchronous versus asynchronous (observable) instruments
- [ ] Aggregation, views, and temporality (delta versus cumulative)
- [ ] Sampling: always on, always off, trace ID ratio, parent-based, head versus tail
- [ ] **Lab**: instrument two services, confirm the trace joins, then break propagation and observe the result

## Week 4: The Collector

- [ ] Architecture: receivers, processors, exporters, connectors, extensions
- [ ] Pipelines per signal, and how components are wired
- [ ] Deployment patterns: agent versus gateway, and when to use both
- [ ] Key receivers: OTLP, Prometheus, filelog, hostmetrics, kubeletstats
- [ ] Key processors: memory_limiter, batch, attributes, resource, filter, transform, tail_sampling, k8sattributes
- [ ] Processor ordering and why it matters
- [ ] Key exporters and queue and retry behavior
- [ ] Connectors, including spanmetrics
- [ ] Distributions: core, contrib, and building a custom one with ocb
- [ ] OpenTelemetry Operator and auto-instrumentation injection
- [ ] **Lab**: build a Collector config with a full pipeline, then add tail sampling
- [ ] Review Notes: `notes/02-collector.md`

## Week 5: Operations, debugging, and review

- [ ] Diagnosing missing telemetry, layer by layer
- [ ] Collector internal telemetry, health check and pprof extensions
- [ ] Memory limiter behavior and backpressure
- [ ] Cardinality control and cost management
- [ ] SLIs, SLOs, error budgets, golden signals, RED and USE
- [ ] Stability guarantees and signal maturity
- [ ] Review Notes: `notes/04-maintaining-and-debugging.md`
- [ ] Work every scenario in [scenarios.md](./scenarios.md)
- [ ] Two timed practice exams; review every wrong answer against the documentation

## Readiness check

- [ ] Explain the API and SDK split and what happens without an SDK
- [ ] Choose the correct metric instrument for a described measurement
- [ ] Write out a `traceparent` header and name its fields
- [ ] Explain why memory_limiter goes first and batch goes last
- [ ] Explain the difference between head and tail sampling and what each costs
- [ ] Name three causes of a broken trace across a service boundary
- [ ] Explain what drives metric cardinality and how to control it
