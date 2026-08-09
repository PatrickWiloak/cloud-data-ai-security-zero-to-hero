---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 13 min
---

# 01 - The OpenTelemetry API and SDK

**Domain 1: The OpenTelemetry API and SDK (46%)**

Nearly half the exam.

---

## The split

| | API | SDK |
|---|---|---|
| Who calls it | Application and library code | Configured once by the application |
| What it does | Defines interfaces: tracers, meters, loggers, spans, instruments | Implements them: sampling, processing, batching, exporting |
| Without the other | API alone is a **no-op**; calls succeed and produce nothing | SDK without API calls has nothing to record |
| Stability | Strong backward-compatibility guarantees | Configuration surface may evolve faster |

This design lets a library ship instrumentation without imposing a telemetry pipeline on its users. If the application configures an SDK, the library's telemetry appears; if not, it costs almost nothing.

The practical consequence, and a reliable exam question: **instrumented code that produces nothing usually means no SDK is configured.**

---

## Traces

A **trace** is a tree of **spans** representing one operation across services.

Span anatomy:
- **Name** - the operation, low cardinality (`GET /orders/{id}`, not `GET /orders/8815`)
- **SpanContext** - trace ID, span ID, trace flags (including the sampled bit), trace state. This is what propagates
- **Parent** - the span that caused this one
- **Span kind** - `SERVER`, `CLIENT`, `PRODUCER`, `CONSUMER`, `INTERNAL`
- **Start and end timestamps**
- **Attributes** - key-value pairs describing the operation
- **Events** - timestamped occurrences within the span, such as an exception
- **Links** - references to other spans without a parent-child relationship, used for batch processing and fan-in
- **Status** - `Unset`, `Ok`, or `Error`

**Span kind** matters for backend analysis: a `CLIENT` span and the corresponding `SERVER` span are the two sides of one call, and the difference between their durations is network and queueing time.

---

## Context propagation

**Context** carries the active span across function calls within a process. **Propagators** serialize it across process boundaries.

The W3C Trace Context standard defines two headers:

```text
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
             ^version ^trace-id (16 bytes)        ^span-id (8 bytes) ^flags
tracestate: vendor1=value1,vendor2=value2
```

The trailing `01` in flags is the **sampled** bit, which is how a downstream service learns that the trace was already sampled in.

**Baggage** is a separate propagation mechanism carrying arbitrary key-value pairs alongside the trace. It travels in headers across every service in the path, so it is not a security boundary and must not carry secrets or personal data.

Propagator configuration must **agree across services**. A service configured only for B3 will not read `traceparent`, and the trace breaks silently.

---

## Metrics

**Instruments** record measurements. Choosing the right one is a recurring exam question.

| Instrument | Sync/Async | Monotonic | Use for |
|---|---|---|---|
| **Counter** | Sync | Yes | Totals that only increase: requests, errors, bytes |
| **Asynchronous counter** | Async | Yes | A cumulative total read from elsewhere |
| **Up-down counter** | Sync | No | Values that rise and fall: queue depth, active connections |
| **Asynchronous up-down counter** | Async | No | A bidirectional value read on demand |
| **Histogram** | Sync | n/a | Distributions where you need percentiles: latency, payload size |
| **Gauge (observable)** | Async | n/a | Current sampled values: temperature, memory in use |

**Synchronous** instruments record inline at the moment of the event. **Asynchronous** instruments register a callback the SDK calls at collection time.

**Views** customize how instruments are processed: rename, change aggregation, drop attributes to control cardinality, or configure histogram buckets.

**Temporality**:
- **Cumulative** - each export reports the running total since start. Simple to reason about, larger payloads, and resets are visible on restart.
- **Delta** - each export reports the change since the last export. Smaller payloads, and the backend must accumulate.

Prometheus expects cumulative; several commercial backends prefer delta. The SDK can be configured per exporter.

---

## Logs

OpenTelemetry's logs approach differs from traces and metrics: rather than a new logging API for developers, it defines a **log data model** and a bridge from existing logging libraries.

A log record carries timestamp, severity, body, attributes, resource, and, critically, **trace context** when emitted inside an active span. That correlation is the main value: click a slow span, see the logs from exactly that request.

---

## Resources and semantic conventions

A **Resource** describes the entity producing telemetry: `service.name`, `service.version`, `deployment.environment`, host, container, and cloud attributes. `service.name` is effectively mandatory; without it, backends group everything as unknown.

**Resource detectors** populate these automatically from the environment: container ID, Kubernetes metadata, cloud instance metadata.

**Semantic conventions** standardize attribute names so that tooling works across languages and vendors: `http.request.method`, `http.route`, `server.address`, `db.system`, `messaging.system`. Using conventional names is what makes dashboards and queries portable.

---

## Sampling

| Sampler | Behavior |
|---|---|
| **AlwaysOn** | Sample every trace |
| **AlwaysOff** | Sample none |
| **TraceIdRatioBased** | Sample a deterministic fraction based on the trace ID |
| **ParentBased** | Respect the parent's decision, with configurable behavior for root spans |

`ParentBased(TraceIdRatioBased(0.1))` is the common default: root spans are sampled at 10%, and every downstream service honors the decision so traces are never partially collected.

**Head sampling** decides at the start of the trace, in the SDK. Cheap, but blind to what happens later. **Tail sampling** decides once the trace is complete, in a Collector gateway. Expensive in memory, but able to keep every error and every slow trace.

---

## SDK configuration

Providers own the pipeline: `TracerProvider`, `MeterProvider`, `LoggerProvider`. Each holds processors and exporters.

**Span processors**:
- **Simple** - export each span as it ends. Useful for debugging and short-lived processes, poor throughput.
- **Batch** - buffer and export in batches. The production default.

**Environment variable configuration** is standardized and testable: `OTEL_SERVICE_NAME`, `OTEL_EXPORTER_OTLP_ENDPOINT`, `OTEL_EXPORTER_OTLP_PROTOCOL`, `OTEL_TRACES_SAMPLER`, `OTEL_RESOURCE_ATTRIBUTES`, `OTEL_PROPAGATORS`.

**Zero-code instrumentation** (agents, auto-instrumentation) injects instrumentation without source changes, available for Java, .NET, Python, Node.js, and others, and injectable in Kubernetes by the OpenTelemetry Operator.

---

## Key terms

- **OpenTelemetry API** - the interfaces application and library code call, which are no-ops unless an SDK is configured
- **OpenTelemetry SDK** - the implementation that samples, processes, batches, and exports telemetry
- **Span** - a single named, timed operation within a trace, carrying attributes, events, links, and status
- **SpanContext** - the trace ID, span ID, flags, and trace state that propagate across boundaries
- **Span kind** - the classification of a span as SERVER, CLIENT, PRODUCER, CONSUMER, or INTERNAL
- **Span link** - a reference from one span to another without a causal parent-child relationship
- **Context propagation** - carrying trace context across process boundaries so spans join into one trace
- **traceparent** - the W3C Trace Context header carrying version, trace ID, span ID, and flags
- **Baggage** - propagated key-value pairs travelling alongside trace context, not a security boundary
- **Counter** - a synchronous monotonic instrument for totals that only increase
- **Up-down counter** - a synchronous instrument for values that increase and decrease
- **Histogram** - an instrument recording a distribution so percentiles can be computed
- **Observable gauge** - an asynchronous instrument reading a current value through a callback
- **View** - SDK configuration customizing instrument aggregation, naming, and attribute retention
- **Temporality** - whether metric exports report cumulative totals or deltas since the last export
- **Resource** - attributes describing the entity producing telemetry, including service.name
- **Semantic conventions** - the standardized attribute naming specification that makes telemetry portable
- **ParentBased sampler** - a sampler that honors the upstream sampling decision so traces are never partial
- **Batch span processor** - the production span processor that buffers spans and exports them in batches
- **OTLP** - the OpenTelemetry Protocol, the native wire format over gRPC or HTTP

---

## Related

- [Notes 02: the Collector](./02-collector.md)
- [Scenarios](../scenarios.md) - scenarios 1, 2, 5, and 6
- [Observability basics](../../../../learn/concepts/observability-basics.md)
