---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 11 min
---

# OpenTelemetry Certified Associate (OTCA) Fact Sheet

## Exam Overview

**Exam Code:** OTCA
**Exam Name:** OpenTelemetry Certified Associate
**Level:** Associate
**Duration:** 90 minutes
**Format:** Multiple choice and multiple select, online proctored
**Questions:** 60
**Passing Score:** 75%
**Cost:** USD 250 (includes one free retake)
**Valid For:** 2 years
**Delivery:** Online proctored through PSI
**Prerequisites:** None

> **Verify before booking.** CNCF exam details, pricing, and curriculum versions change. Confirm on the official pages below.

**[📖 OTCA certification page](https://www.cncf.io/training/certification/otca/)** - registration and curriculum
**[📖 Linux Foundation OTCA page](https://training.linuxfoundation.org/certification/opentelemetry-certified-associate-otca/)** - exam logistics and candidate handbook
**[📖 OpenTelemetry documentation](https://opentelemetry.io/docs/)** - the primary study source
**[📖 CNCF curriculum repository](https://github.com/cncf/curriculum)** - published exam domains

## Why this exam is in this repo

Until now the repo had `topics/observability.md`, an observability service comparison, an LLM observability comparison, and a monitoring stack build, but **not a single observability certification**. OTCA closes that gap, and it does so vendor-neutrally: OpenTelemetry is the instrumentation standard that Datadog, Grafana, Splunk, Honeycomb, New Relic, and every hyperscaler now consume.

That makes it more durable than a vendor certification. Learning OTel is learning the layer underneath all of them.

## Target Audience

- SREs and platform engineers who own the observability pipeline
- Developers instrumenting services
- Anyone running the OpenTelemetry Collector in production
- Kubernetes practitioners extending [PCA](../pca/) or [CKA](../cka/) knowledge into telemetry

Assumed background: comfortable with containers, distributed systems basics, and at least one programming language.

## Exam Domains

### Domain 1: The OpenTelemetry API and SDK (46%)

Nearly half the exam. Instrumentation is the core skill.

**Key Concepts:**
- The API and SDK split, and why the API alone is a no-op
- Signals: traces, metrics, logs, and their data models
- Traces: spans, span context, span kinds, attributes, events, links, status
- Context propagation: the W3C Trace Context standard, `traceparent` and `tracestate`, and baggage
- Propagators and how context crosses process boundaries
- Metrics instruments: counter, up-down counter, histogram, gauge, and their synchronous and asynchronous variants
- Aggregation, temporality (delta and cumulative), and views
- Logs and the log data model, including correlating logs with traces
- Resources and resource detection, and semantic conventions
- Samplers: always on, always off, trace ID ratio, parent-based, and head versus tail sampling
- SDK configuration: providers, processors, exporters, and environment variable configuration
- Automatic (zero-code) instrumentation versus manual instrumentation
- Instrumentation libraries and the OpenTelemetry Protocol (OTLP)

**[📖 OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/)** - signals, context, and the data model
**[📖 Language SDKs](https://opentelemetry.io/docs/languages/)** - per-language instrumentation

### Domain 2: The OpenTelemetry Collector (26%)

**Key Concepts:**
- Collector architecture: receivers, processors, exporters, connectors, extensions
- Pipelines per signal type and how components compose
- Deployment patterns: agent (per host or sidecar) and gateway (standalone cluster)
- Common receivers: OTLP, Prometheus, Jaeger, Zipkin, filelog, hostmetrics, kubeletstats
- Common processors: batch, memory limiter, attributes, resource, filter, transform, tail sampling, k8sattributes
- Common exporters: OTLP, OTLP HTTP, Prometheus remote write, debug, and vendor exporters
- Connectors that join pipelines, such as spanmetrics
- Collector distributions: core, contrib, and building a custom distribution with the OpenTelemetry Collector Builder
- Configuration structure and validation
- The OpenTelemetry Operator for Kubernetes, including auto-instrumentation injection

**[📖 Collector documentation](https://opentelemetry.io/docs/collector/)** - architecture and configuration
**[📖 Collector components registry](https://opentelemetry.io/ecosystem/registry/)** - available receivers, processors, exporters

### Domain 3: Fundamentals of Observability (18%)

**Key Concepts:**
- Observability versus monitoring, and why the distinction matters
- The three signals and what each is good and bad at
- Telemetry correlation: exemplars, trace-to-log and trace-to-metric linking
- Cardinality: what drives it, why it is expensive, and how to control it
- Semantic conventions and why standardized attribute names matter
- SLIs, SLOs, and error budgets
- The golden signals: latency, traffic, errors, saturation
- RED and USE methods
- Sampling strategy and its effect on what you can answer

**[📖 Semantic conventions](https://opentelemetry.io/docs/specs/semconv/)** - standardized attribute names
**[📖 Observability primer](https://opentelemetry.io/docs/concepts/observability-primer/)** - concepts and vocabulary

### Domain 4: Maintaining and Debugging Observability Pipelines (10%)

**Key Concepts:**
- Diagnosing missing telemetry: instrumentation, propagation, collector, or backend
- Collector internal telemetry and health checks
- Debug and file exporters for local troubleshooting
- Memory limiter behavior and backpressure
- Queue and retry configuration, and what happens when a backend is unavailable
- Broken trace context and where propagation typically fails
- Cost control: sampling, filtering, attribute reduction, and metric cardinality limits
- Versioning, stability guarantees, and migration from legacy agents

## Signal quick reference

| Signal | Answers | Cost driver | Watch out for |
|---|---|---|---|
| **Traces** | Why is this request slow, and what did it touch | Span volume | Sampling decisions change what you can debug later |
| **Metrics** | Is the system healthy, is it trending | Time series cardinality | One unbounded attribute can multiply series enormously |
| **Logs** | What exactly happened in this code path | Volume and retention | Unstructured logs are hard to correlate |

## Related repo material

- [Notes](./notes/) - four notes, one per domain
- [Practice plan](./practice-plan.md) - 5-week schedule
- [Scenarios](./scenarios.md)
- [Strategy](./strategy.md)
- [PCA Prometheus Certified Associate](../pca/) - the metrics-specific counterpart
- [Observability basics](../../../learn/concepts/observability-basics.md)
- [Observability topic](../../../topics/observability.md)
- [Set up a monitoring stack](../../../resources/hands-on-projects/setup-monitoring-stack.md)
- [Service comparison: observability and monitoring](../../../resources/service-comparison-observability-monitoring.md)
