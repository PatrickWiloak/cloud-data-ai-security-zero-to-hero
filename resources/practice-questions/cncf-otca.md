# OpenTelemetry Certified Associate (OTCA) - Practice Questions

15 questions for OTCA prep. Weighted toward the API and SDK (46%) and the Collector (26%), matching the exam.

> **Cert page:** [exams/kubernetes/otca/](../../exams/kubernetes/otca/)

---

### Question 1
**Scenario:** A developer adds OpenTelemetry API calls throughout a service, deploys it, and sees no telemetry and no errors. What is the most likely cause?

A. The exporter endpoint is wrong
B. No SDK is configured, so the API calls are no-ops
C. The backend is rejecting the data
D. The sampler is set to always-off

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The OpenTelemetry API is deliberately a no-op without an SDK, which is why nothing errors. This design lets libraries ship instrumentation without imposing a pipeline on their users. A wrong endpoint or a rejecting backend would usually produce export errors, and an always-off sampler is possible but less common than simply never wiring up the SDK.
</details>

---

### Question 2
**Scenario:** Which instrument should record the number of items currently in a work queue?

A. Counter
B. Up-down counter
C. Histogram
D. Asynchronous gauge

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Queue depth rises and falls and the change happens at a known event, so a synchronous up-down counter fits. A counter is monotonic and cannot decrease. A histogram records distributions. An asynchronous gauge suits values you sample on demand rather than record at an event.
</details>

---

### Question 3
**Scenario:** Service A calls service B. Both are instrumented and export to the same backend, but B's spans appear as separate root spans.

A. Increase the sampling rate
B. Context is not propagating: check propagator configuration on both sides, outbound instrumentation on A, and header-stripping intermediaries
C. Change the exporter protocol
D. Add more span attributes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Disconnected traces are always a propagation problem, never an export problem, because both traces reached the backend. Common causes are mismatched propagators, uninstrumented outbound HTTP clients, and proxies stripping the `traceparent` header.
</details>

---

### Question 4
**Scenario:** A Collector pipeline declares processors in the order `batch`, `attributes`, `memory_limiter`, and is repeatedly OOM-killed under load.

A. Increase the container memory limit
B. Reduce the batch size
C. Reorder to `memory_limiter`, `attributes`, `batch`
D. Remove the attributes processor

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Processors run in declared order. `memory_limiter` must be first so it can refuse data before downstream processors allocate for it, and `batch` belongs last so batching operates on the final data shape. Raising the memory limit delays the problem rather than fixing the ordering.
</details>

---

### Question 5
**Scenario:** After adding the raw request path as an attribute on an HTTP counter, backend costs triple. Paths look like `/orders/8815/items/44`.

A. Reduce the metric export interval
B. Sample the metrics
C. Use the templated route (`http.route`) instead of the raw target, or drop the attribute in a view or the Collector
D. Switch to a different backend

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Every distinct attribute value combination is a separate time series, so an unbounded path attribute multiplies series enormously. `http.route` is the semantic convention for exactly this. A shorter export interval produces fewer points per series, not fewer series. Metrics are aggregates, so sampling them distorts values.
</details>

---

### Question 6
**Scenario:** A platform generates 500,000 spans per second. Cost allows keeping about 1%, but every trace containing an error or exceeding two seconds must be retained in full.

A. Trace ID ratio head sampling at 1%
B. Parent-based sampling
C. Tail sampling in a Collector gateway, with a load-balancing exporter routing by trace ID
D. Sampling in the backend

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The retention decision depends on the outcome of the trace, which is only known once it is complete, so head sampling cannot satisfy it. Tail sampling requires all spans of a trace to reach one instance, which is why it needs a gateway plus trace-ID-aware load balancing.
</details>

---

### Question 7
**Scenario:** Which Collector component enriches telemetry with pod, namespace, and node metadata, and where must it run?

A. The `resource` processor, in a gateway
B. The `k8sattributes` processor, in an agent close to the workload
C. The `attributes` processor, anywhere in the pipeline
D. The `transform` processor, in a gateway

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `k8sattributes` derives metadata from the source IP, which is typically rewritten by the time traffic reaches a gateway. It therefore belongs in an agent (DaemonSet or sidecar) close to the workload. The `attributes` and `resource` processors set static or transformed values rather than looking up pod metadata.
</details>

---

### Question 8
**Scenario:** What does the sampled flag in a `traceparent` header do?

A. Indicates whether the span has finished
B. Tells downstream services that the trace was already sampled in, so they honor the decision
C. Marks the span as an error
D. Identifies the exporter used

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The trace flags byte carries the sampled bit, which is how a consistent sampling decision propagates across services. This is what makes parent-based sampling produce complete traces rather than partially collected ones.
</details>

---

### Question 9
**Scenario:** A team needs percentiles for request duration. Which instrument is required?

A. Counter
B. Up-down counter
C. Histogram
D. Gauge

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Percentiles require a distribution, which only a histogram records. A gauge holds a single current value and cannot yield percentiles. Counters record monotonic totals.
</details>

---

### Question 10
**Scenario:** Which statement about baggage is correct?

A. It is encrypted in transit by the SDK
B. It propagates key-value pairs across service boundaries in headers and must not carry secrets
C. It is stored only within a single process
D. It replaces span attributes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Baggage travels across every service in the request path as plain header content, so it is not a security boundary. It complements rather than replaces span attributes, and it is explicitly cross-process.
</details>

---

### Question 11
**Scenario:** A short-lived batch job is instrumented correctly but its spans never appear in the backend.

A. The sampler is dropping them
B. The batch span processor never flushed before the process exited
C. The exporter protocol is wrong
D. Batch jobs cannot be traced

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The batch processor buffers spans and exports periodically. A process that exits without an explicit SDK shutdown loses whatever is still buffered. Short-lived processes need an explicit shutdown call, or a simple span processor.
</details>

---

### Question 12
**Scenario:** Which Collector metric indicates that the memory limiter is shedding load?

A. `otelcol_exporter_send_failed_spans`
B. `otelcol_receiver_refused_spans`
C. `otelcol_processor_dropped_spans`
D. `otelcol_exporter_queue_size`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Refused-at-receiver is the signature of memory limiter backpressure. Send-failed indicates a backend problem. Processor-dropped indicates a filter or sampling decision. Queue size climbing toward capacity warns that dropping is imminent, but refusal is what the limiter itself produces.
</details>

---

### Question 13
**Scenario:** What is the purpose of the `spanmetrics` connector?

A. Converting metrics into spans
B. Deriving rate, error, and duration metrics from spans, so spans can then be sampled more aggressively
C. Batching spans before export
D. Enriching spans with metric values

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A connector consumes from one pipeline and emits into another. `spanmetrics` computes RED metrics from 100% of spans in the Collector, which lets you keep accurate aggregates while paying to store only a sample of the trace data.
</details>

---

### Question 14
**Scenario:** Which resource attribute is effectively mandatory, and what happens without it?

A. `host.name`; telemetry is dropped
B. `service.name`; backends group telemetry as unknown
C. `deployment.environment`; sampling fails
D. `telemetry.sdk.language`; the exporter errors

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `service.name` is the primary identifier backends use to group telemetry. Without it, everything lands under an unknown service, which makes the data close to unusable even though nothing errors.
</details>

---

### Question 15
**Scenario:** Which statement correctly distinguishes delta from cumulative temporality?

A. Delta reports the running total; cumulative reports the change since last export
B. Cumulative reports the running total since start; delta reports the change since the last export
C. They are the same, with different names per backend
D. Delta applies only to histograms

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cumulative payloads are larger and make restarts visible as resets, and Prometheus expects them. Delta payloads are smaller and require the backend to accumulate, and several commercial backends prefer them. Temporality is configurable per exporter and applies to counters and histograms alike.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready. 75% is the pass mark, so this puts you comfortably clear.
- **10-12 correct (65-80%):** Focus on the API and SDK domain, which is 46% of the exam.
- **Below 10:** Work the [scenarios](../../exams/kubernetes/otca/scenarios.md) and read the OpenTelemetry concepts documentation directly; the exam tracks it closely.
