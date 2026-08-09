---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 9 min
---

# OTCA High-Yield Scenarios

---

## Scenario 1: The trace stops at the boundary

**Scenario**: Service A calls service B over HTTP. Both are instrumented and both export to the same backend. Traces from A look complete, traces from B appear as separate root spans, and nothing joins them.

**Solution Pattern**:
- Context is not propagating. The `traceparent` header is either not being injected by A, not extracted by B, or being stripped in between
- Confirm both services configure a **propagator**, and that they agree. The default is W3C Trace Context; a service configured only for B3 will not read `traceparent`
- Check that A's HTTP client is instrumented, not just its server side. Injection happens on the outbound call
- Check for an intermediary (proxy, API gateway, load balancer) stripping unknown headers
- Verify B's server instrumentation extracts context before creating its span, so its span becomes a child rather than a root

**Common Distractors**:
- Increasing the sampling rate (both traces exist, they are simply unconnected)
- Adding more attributes (does not affect linkage)
- Changing the exporter (both already reach the backend)

**Key Takeaway**: Disconnected traces are a propagation problem, never an export problem. Check propagator configuration on both sides, outbound instrumentation, and header-stripping intermediaries.

---

## Scenario 2: Choosing an instrument

**Scenario**: A team needs four measurements: total orders processed, current items in a work queue, HTTP request duration with p95 and p99, and the host's available disk space read from the OS.

**Solution Pattern**:
- **Orders processed**: synchronous **counter**. Monotonic, supports rate calculations.
- **Items in queue**: **up-down counter**. Goes both directions and is recorded where the change happens.
- **Request duration**: **histogram**. Percentiles require a distribution, which only a histogram provides.
- **Available disk space**: **asynchronous gauge** (observable gauge). Read on demand through a callback rather than recorded per event.

**Common Distractors**:
- A gauge for orders processed (loses the ability to compute rates correctly)
- A counter for queue depth (counters are monotonic and cannot decrease)
- A gauge for request duration (a single current value cannot yield percentiles)
- A synchronous instrument for disk space (there is no event to hook; it is sampled)

**Key Takeaway**: Monotonic totals are counters, bidirectional values are up-down counters, distributions are histograms, and sampled current values are asynchronous gauges. Instrument selection is a reliable source of exam questions.

---

## Scenario 3: Collector processor ordering

**Scenario**: An engineer writes a Collector pipeline with processors in this order: `batch`, `attributes`, `memory_limiter`. Under load the Collector is OOM-killed repeatedly.

**Solution Pattern**:
- Reorder to `memory_limiter`, `attributes`, `batch`
- **memory_limiter must be first** so it can refuse data and apply backpressure before downstream processors allocate memory for it
- **batch last** so batching operates on the final data shape and the batch size reflects what is actually exported
- Configure the memory limiter's `limit_mib` and `spike_limit_mib` below the container memory limit
- Set the container memory limit and the limiter consistently, or the runtime kills the process before the limiter engages

**Common Distractors**:
- Increasing the container memory limit (delays the problem)
- Reducing the batch size only (helps a little, does not fix the ordering)
- Removing the attributes processor (removes function, not the cause)

**Key Takeaway**: Processors execute in declared order. memory_limiter first, drop-data processors early, enrichment in the middle, batch last. This ordering is documented guidance and directly testable.

---

## Scenario 4: Metric cardinality explosion

**Scenario**: After adding an attribute for the request path to an HTTP request counter, the backend bill triples and queries slow to a crawl. The API uses paths like `/orders/8815/items/44`.

**Solution Pattern**:
- The raw path is unbounded, so every distinct URL creates a new time series
- Use the **route template** (`/orders/{order_id}/items/{item_id}`) as the attribute value, which is what the `http.route` semantic convention specifies
- Where the SDK cannot template, use a **view** to drop or transform the attribute, or the Collector's `transform` or `attributes` processor
- Keep high-cardinality identifiers on **spans**, where they are searchable per request, rather than on metrics
- Set cardinality limits where the SDK or backend supports them

**Common Distractors**:
- Reducing the metric export interval (fewer data points per series, same series count)
- Sampling metrics (metrics are aggregates; sampling them distorts the values)
- Moving to a different backend (the same series count costs money there too)

**Key Takeaway**: Cardinality is driven by unique attribute value combinations. High-cardinality identifiers belong on traces and logs, never on metric attributes. `http.route` rather than `http.target` is the canonical fix.

---

## Scenario 5: Sampling strategy

**Scenario**: A platform generates 500,000 spans per second. Cost requires keeping about 1%. The SRE team insists that every trace containing an error, and every trace slower than two seconds, must be retained in full.

**Solution Pattern**:
- **Tail sampling** in a Collector **gateway**, because the decision requires seeing the complete trace
- Policies: keep all traces with an error status, keep all traces above a latency threshold, and apply a probabilistic policy to the remainder
- Place a **load-balancing exporter** in front of the gateway, routing by trace ID so all spans of a trace reach the same tail-sampling instance
- Size the gateway for the buffering window, since tail sampling holds spans until the trace is judged complete
- Head sampling alone cannot satisfy this: the decision is made at the root before the error or the latency is known

**Common Distractors**:
- Trace ID ratio head sampling at 1% (drops 99% of errors too)
- Parent-based sampling (consistent, but still decided at the start)
- Sampling in the backend (the spans already cost money to transmit and ingest)

**Key Takeaway**: When the retention decision depends on the outcome of the trace, only tail sampling works. It requires a gateway deployment plus trace-ID-aware load balancing, and it costs memory for the buffering window.

---

## Scenario 6: No telemetry at all

**Scenario**: A developer adds OpenTelemetry API calls throughout a service, deploys it, and sees nothing in the backend. No errors are logged.

**Solution Pattern**:
- Check that an **SDK is configured**. API calls without an SDK are deliberate no-ops, which is why nothing errors
- Check the **exporter endpoint** and protocol (OTLP gRPC on 4317, OTLP HTTP on 4318 by convention)
- Add a **console or debug exporter** temporarily to confirm spans are produced at all
- Check the **sampler**: an always-off or misconfigured ratio sampler drops everything silently
- Check the Collector is reachable and its own **internal telemetry and health check** for receive errors
- Check that the span processor is flushing; short-lived processes need an explicit shutdown or a simple processor

**Common Distractors**:
- Adding more instrumentation (more no-ops)
- Changing the backend (the data never leaves the process)
- Increasing log verbosity in the application (the SDK is silent by design here)

**Key Takeaway**: Debug telemetry loss layer by layer: SDK configured, spans produced, sampler passing, exporter reaching the Collector, Collector accepting and exporting, backend ingesting. The silent no-op behavior of the bare API is the classic first-time mistake.

---

## Scenario 7: Enriching Kubernetes telemetry

**Scenario**: Traces from a Kubernetes cluster arrive without pod, namespace, or node attributes, making it impossible to correlate a slow trace with a noisy neighbor.

**Solution Pattern**:
- Deploy a Collector **agent as a DaemonSet** and add the **k8sattributes processor**, which enriches telemetry with pod, namespace, node, and workload metadata based on the source IP
- Give the Collector service account RBAC to read pods and namespaces
- Set `resource` attributes for service name and version through the Downward API or environment variables
- Use the **OpenTelemetry Operator** to manage the Collector and to inject auto-instrumentation into workloads
- Ensure resource detection is not overwriting the enriched attributes downstream

**Common Distractors**:
- Adding attributes manually in each application (unmaintainable, and wrong the moment a pod is rescheduled)
- Using the attributes processor with static values (does not vary per pod)
- Enriching at the gateway (the source IP has usually been rewritten by then)

**Key Takeaway**: k8sattributes belongs in an agent close to the workload, because enrichment depends on the source IP. Enriching at a gateway generally fails for that reason.

---

## Related

- [Practice plan](./practice-plan.md)
- [Strategy](./strategy.md)
- [Notes](./notes/)
- [Kubernetes troubleshooting](../../../resources/troubleshooting/kubernetes-troubleshooting.md)
- [Practice questions](../../../resources/practice-questions/cncf-otca.md)
