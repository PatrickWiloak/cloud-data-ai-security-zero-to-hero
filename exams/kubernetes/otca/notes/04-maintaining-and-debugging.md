---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 9 min
---

# 04 - Maintaining and debugging observability pipelines

**Domain 4: Maintaining and Debugging Observability Pipelines (10%)**

The smallest domain, but it draws on everything else.

---

## Debugging missing telemetry, layer by layer

Work down the path. Confirm each layer before moving to the next.

| Layer | Check | Common cause |
|---|---|---|
| 1. Instrumentation | Is an **SDK** configured, not just the API? | API-only, so all calls are no-ops |
| 2. Sampling | Is the sampler passing anything? | AlwaysOff, or a ratio set to zero |
| 3. Export from the app | Add a **console or debug exporter** temporarily | Wrong endpoint, wrong protocol, TLS failure |
| 4. Process lifetime | Does the process flush before exit? | Batch processor never flushed in a short-lived job |
| 5. Collector receive | Collector **internal telemetry**, `zpages`, logs | Receiver not enabled, port mismatch, auth |
| 6. Collector process | Is a processor dropping data? | filter or sampling policy broader than intended |
| 7. Collector export | Queue and retry metrics, exporter errors | Backend unreachable, credentials, quota |
| 8. Backend | Backend ingestion view | Rate limiting, schema rejection |

The single most common first-time cause is layer 1, because the bare API fails silently by design.

---

## Collector self-observability

The Collector emits its own telemetry, and it is the fastest diagnostic:

- `otelcol_receiver_accepted_spans` and `otelcol_receiver_refused_spans`
- `otelcol_processor_dropped_spans`
- `otelcol_exporter_sent_spans`, `otelcol_exporter_send_failed_spans`
- `otelcol_exporter_queue_size` and `otelcol_exporter_queue_capacity`

Refused at the receiver usually means the memory limiter is shedding. Send-failed at the exporter means the backend is the problem. Queue size climbing toward capacity means you are about to start dropping.

Extensions that help: **health_check** for liveness and readiness, **pprof** for profiling, **zpages** for live in-process debug pages.

---

## Backpressure and loss

The chain is: application exporter queue, Collector receiver, Collector queue, backend.

- **memory_limiter** refuses data when memory approaches the limit, pushing backpressure upstream. Set `limit_mib` comfortably below the container memory limit, or the runtime kills the Collector before the limiter engages.
- **sending_queue** absorbs temporary backend slowness. When it fills, data is dropped. Persistent queues backed by the file storage extension survive restarts.
- **retry_on_failure** retries retryable errors with backoff. Non-retryable errors (a 400 from the backend, a schema rejection) are dropped immediately and should be alerted on.

Decide deliberately whether your pipeline is lossy under pressure or applies backpressure to applications. Both are valid; silently discovering which one you chose during an incident is not.

---

## Broken trace context

Where propagation typically fails:

- Mismatched propagators between services (W3C on one side, B3 on the other)
- An intermediary stripping unknown headers: some proxies, API gateways, and CDNs
- Message queues, where context must be injected into and extracted from message attributes explicitly
- Thread pools, async runtimes, and background jobs, where context does not follow automatically
- Manual span creation that ignores the incoming context and starts a new root

---

## Cost control

Observability spend grows faster than traffic if nothing constrains it.

| Lever | Effect |
|---|---|
| **Head sampling** | Cheapest; reduces span volume at source, blind to outcome |
| **Tail sampling** | Keeps errors and slow traces, costs gateway memory |
| **Attribute reduction** | Drop unused attributes in views or the Collector |
| **Cardinality limits** | Prevents a single bad attribute causing a series explosion |
| **Log filtering** | Drop debug-level logs before export |
| **Retention tiering** | Short hot retention, longer cheap archive |
| **spanmetrics connector** | Derive RED metrics from spans, then sample spans harder |

The spanmetrics pattern is worth knowing: generate request rate, error rate, and duration metrics from 100% of spans in the Collector, then sample the spans themselves aggressively. You keep accurate aggregates and pay only for a fraction of the trace data.

---

## Versioning and stability

OpenTelemetry components carry stability levels: stable, beta, alpha, development. Traces and metrics are stable across most languages; logs matured later; profiling is newer still.

Practical consequences: pin Collector and SDK versions, read release notes before upgrading contrib components, and expect experimental semantic conventions to change attribute names between versions. An attribute rename silently breaks dashboards and alerts, which is why convention stability level is worth checking before building on one.

---

## Key terms

- **Debug exporter** - a Collector exporter that prints telemetry to logs, used to confirm data is arriving
- **zpages** - a Collector extension serving live in-process diagnostic pages
- **health_check extension** - the Collector extension exposing liveness and readiness endpoints
- **Backpressure** - the mechanism by which a saturated component slows or refuses upstream data rather than failing
- **sending_queue** - the exporter buffer absorbing backend slowness, optionally persisted to disk
- **retry_on_failure** - exporter configuration retrying retryable errors with backoff
- **Persistent queue** - a Collector queue backed by the file storage extension so buffered data survives restarts
- **spanmetrics connector** - a connector deriving rate, error, and duration metrics from spans
- **Stability level** - the maturity guarantee (stable, beta, alpha, development) attached to a component or convention
- **Refused spans** - the Collector metric indicating telemetry rejected at the receiver, usually due to the memory limiter

---

## Related

- [Notes 01: the API and SDK](./01-api-and-sdk.md)
- [Scenarios](../scenarios.md) - scenarios 4, 5, and 6
- [Kubernetes troubleshooting](../../../../resources/troubleshooting/kubernetes-troubleshooting.md)
