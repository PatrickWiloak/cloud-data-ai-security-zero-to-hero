---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 11 min
---

# 02 - The OpenTelemetry Collector

**Domain 2: The OpenTelemetry Collector (26%)**

A vendor-agnostic proxy that receives, processes, and exports telemetry.

---

## Why it exists

Without a Collector, every service exports directly to a backend. That means backend credentials in every service, a redeploy to change destination, no central place to enrich or filter, and no buffering when the backend is unavailable.

The Collector centralizes all of that. Applications export to the Collector over OTLP; the Collector decides what happens next.

---

## Components

| Component | Role |
|---|---|
| **Receiver** | Gets data in: OTLP, Prometheus, Jaeger, Zipkin, filelog, hostmetrics, kubeletstats |
| **Processor** | Transforms data in flight: batch, memory_limiter, attributes, resource, filter, transform, tail_sampling, k8sattributes |
| **Exporter** | Sends data out: OTLP, OTLP HTTP, Prometheus remote write, debug, vendor-specific |
| **Connector** | Joins one pipeline to another, consuming from one and emitting to another: spanmetrics, count, forward |
| **Extension** | Capabilities not in the data path: health_check, pprof, zpages, bearertokenauth |

A **pipeline** is per signal type (traces, metrics, logs) and wires receivers to processors to exporters.

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:

processors:
  memory_limiter:
    limit_mib: 512
    spike_limit_mib: 128
    check_interval: 1s
  k8sattributes:
  batch:
    timeout: 5s
    send_batch_size: 8192

exporters:
  otlp:
    endpoint: backend:4317
    sending_queue:
      enabled: true
    retry_on_failure:
      enabled: true

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [memory_limiter, k8sattributes, batch]
      exporters: [otlp]
```

---

## Processor ordering

Processors run in the order declared, and the ordering is documented guidance rather than preference:

1. **memory_limiter** first, so it can reject data and apply backpressure before anything allocates for it
2. **Data-dropping processors** (filter, sampling) early, so you do not enrich data you are about to discard
3. **Enrichment** (k8sattributes, resource, attributes, transform) in the middle
4. **batch** last, so batching reflects the final data shape

Getting this backwards, particularly putting `batch` before `memory_limiter`, is a classic exam question and a real cause of OOM kills.

---

## Deployment patterns

| Pattern | Shape | Good for |
|---|---|---|
| **Agent** | DaemonSet, sidecar, or host process next to the workload | Local enrichment (k8sattributes needs the source IP), host metrics, log tailing, offloading the application quickly |
| **Gateway** | Standalone deployment, often behind a load balancer | Aggregation, tail sampling, central egress and credentials, backpressure absorption |
| **Both** | Agents forward to a gateway | The common production shape |

**Tail sampling must run in a gateway**, and every span of a trace must reach the same instance. That requires a **load-balancing exporter** routing by trace ID in front of the tail-sampling tier.

**k8sattributes must run in an agent**, because enrichment is based on the source IP, which is rewritten by the time traffic reaches a gateway.

---

## Distributions

- **Core** - the components maintained in the core repository. Small, conservative.
- **Contrib** - core plus the large community component set. What most people run.
- **Custom** - built with the **OpenTelemetry Collector Builder (ocb)**, including only the components you need. Smaller image, smaller attack surface, faster start.
- **Vendor distributions** - preconfigured builds from observability vendors and cloud providers.

---

## The OpenTelemetry Operator

Kubernetes operator managing two custom resources:

- **OpenTelemetryCollector** - declaratively deploy Collectors as deployment, daemonset, statefulset, or sidecar, with the config inline.
- **Instrumentation** - configure zero-code auto-instrumentation, injected into pods by annotation. The operator adds an init container carrying the language agent and sets the environment variables.

This is how large estates instrument applications without touching application code or Dockerfiles.

---

## Reliability behavior

- **sending_queue** buffers when the backend is slow or unavailable. Persistent queues (file storage extension) survive restarts.
- **retry_on_failure** retries with backoff on retryable errors.
- **memory_limiter** applies backpressure and, at the hard limit, refuses data. Set below the container memory limit or the runtime kills the process first.
- Data loss is possible: an in-memory queue is lost on restart, and a full queue drops data. These are trade-offs to configure deliberately.

---

## Key terms

- **Collector** - the vendor-agnostic service that receives, processes, and exports telemetry
- **Receiver** - the Collector component that ingests telemetry in a given format or protocol
- **Processor** - the Collector component that transforms, filters, or batches telemetry in flight
- **Exporter** - the Collector component that sends telemetry to a backend
- **Connector** - a component that consumes from one pipeline and emits into another, such as spanmetrics
- **Extension** - a Collector capability outside the data path, such as health_check or pprof
- **Pipeline** - a per-signal wiring of receivers, processors, and exporters in the service section
- **memory_limiter** - the processor that applies backpressure and refuses data to prevent out-of-memory conditions
- **batch processor** - the processor that groups telemetry before export, declared last in a pipeline
- **k8sattributes processor** - the processor enriching telemetry with Kubernetes metadata based on source IP
- **tail_sampling processor** - the processor that decides sampling after seeing the complete trace
- **Agent deployment** - a Collector running next to the workload for local enrichment and fast offload
- **Gateway deployment** - a standalone Collector tier for aggregation, tail sampling, and central export
- **Load-balancing exporter** - the exporter routing spans by trace ID so tail sampling sees complete traces
- **OpenTelemetry Collector Builder** - the tool producing a custom Collector distribution with only chosen components
- **OpenTelemetry Operator** - the Kubernetes operator managing Collectors and injecting auto-instrumentation
- **sending_queue** - exporter buffering that absorbs backend slowness, optionally persisted to disk

---

## Related

- [Notes 03: observability fundamentals](./03-observability-fundamentals.md)
- [Scenarios](../scenarios.md) - scenarios 3, 5, and 7
