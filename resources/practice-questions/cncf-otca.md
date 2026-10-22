# OpenTelemetry Certified Associate (OTCA) - Practice Questions

30 questions for OTCA prep. Weighted toward the API and SDK (46%) and the Collector (26%), matching the exam.

> **Cert page:** [exams/kubernetes/otca/](../../exams/kubernetes/otca/)

---

### Question 1
**Scenario:** A developer adds OpenTelemetry API calls throughout a service, deploys it, and sees no telemetry and no errors. What is the most likely cause?

A. The Collector's batch processor timeout is set too high, so the backend receives data only after a long delay
B. The exporter endpoint is wrong
C. No SDK is configured, so the API calls are no-ops
D. The backend is rejecting the data with an authentication or schema error, which would show up as export failures in the SDK logs

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The OpenTelemetry API is deliberately a no-op without an SDK, which is why nothing errors. This design lets libraries ship instrumentation without imposing a pipeline on their users. A wrong endpoint or a rejecting backend would usually produce export errors, and a long batch timeout only delays data rather than hiding it completely.
</details>

---

### Question 2
**Scenario:** Which instrument should record the number of items currently in a work queue?

A. Histogram, which records the distribution of measured values such as durations and sizes into buckets rather than a current level
B. Asynchronous gauge, for non-additive readings
C. Up-down counter, because the depth rises and falls as items are added and removed
D. Counter, which only increases monotonically, so it can record items added to the queue but cannot go down when they are removed

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Queue depth rises and falls and the change happens at a known event, so a synchronous up-down counter fits. A counter is monotonic and cannot decrease. A histogram records distributions. An asynchronous gauge suits non-additive values you sample on demand, such as a temperature, rather than counts recorded at an event.
</details>

---

### Question 3
**Scenario:** Service A calls service B. Both are instrumented and export to the same backend, but B's spans appear as separate root spans.

A. Increase the sampling rate so that more spans are kept, which raises the volume exported but does not link a child span to its parent
B. Context is not propagating: check the propagator configuration on service A and service B, outbound instrumentation on A, and header-stripping intermediaries
C. Change the exporter protocol from gRPC to HTTP, which alters the transport to the backend but not how trace context moves between services
D. Add more span attributes on service B, which adds detail to each span but does not set the parent span identity

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Disconnected traces are always a propagation problem, never an export problem, because both traces reached the backend. Common causes are mismatched propagators, uninstrumented outbound HTTP clients, and proxies stripping the `traceparent` header.
</details>

---

### Question 4
**Scenario:** A Collector pipeline declares processors in the order `batch`, `attributes`, `memory_limiter`, and is repeatedly OOM-killed under load.

A. Reduce the batch size so that each batch holds fewer spans, which lowers the size of one batch but leaves nothing guarding memory ahead of it
B. Increase the container memory limit, which delays the OOM kill under load but does not stop the pipeline from accepting more data than it can hold
C. Remove the attributes processor, since attribute edits copy data and add memory pressure, even though the missing guard is the actual problem
D. Reorder to `memory_limiter`, `attributes`, `batch`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Processors run in declared order. `memory_limiter` must be first so it can refuse data before downstream processors allocate for it, and `batch` belongs last so batching operates on the final data shape. Raising the memory limit delays the problem rather than fixing the ordering.
</details>

---

### Question 5
**Scenario:** After adding the raw request path as an attribute on an HTTP counter, backend costs triple. Paths look like `/orders/8815/items/44`.

A. Switch to a different backend that has cheaper storage per series, which hides the cardinality growth rather than removing it from the data
B. Use the templated route (`http.route`), such as /orders/{id}/items/{itemId}, instead of the raw target, or drop the attribute with a metrics view or in the Collector before export
C. Reduce the metric export interval to five seconds, which makes the backend receive more points per series and does not reduce series count
D. Sample the metrics at 10% in the SDK, which drops data points but does not change how many unique path values create new series

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Every distinct attribute value combination is a separate time series, so an unbounded path attribute multiplies series enormously. `http.route` is the semantic convention for exactly this. A shorter export interval produces fewer points per series, not fewer series. Metrics are aggregates, so sampling them distorts values.
</details>

---

### Question 6
**Scenario:** A platform generates 500,000 spans per second. Cost allows keeping about 1%, but every trace containing an error or exceeding two seconds must be retained in full.

A. Tail sampling in a Collector gateway, with a load-balancing exporter routing by trace ID so that every span of a trace reaches one instance, using error and latency policies
B. Trace ID ratio head sampling at 1%, which decides at the root before the outcome is known, so most error and slow traces are dropped
C. Parent-based sampling with a fixed ratio on the root, which makes children follow the root decision and also cannot see errors or latency
D. Sampling in the backend after ingestion, which saves storage but still pays to send and receive all 500,000 spans per second

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The retention decision depends on the outcome of the trace, which is only known once it is complete, so head sampling cannot satisfy it. Tail sampling requires all spans of a trace to reach one instance, which is why it needs a gateway plus trace-ID-aware load balancing.
</details>

---

### Question 7
**Scenario:** Which Collector component enriches telemetry with pod, namespace, and node metadata, and where must it run?

A. The `k8sattributes` processor, in an agent close to the workload
B. The `transform` processor in a gateway, which rewrites telemetry with OTTL statements but does not query the Kubernetes API for pod metadata
C. The `attributes` processor anywhere in the pipeline, which sets or edits attributes you specify but does not look up pod metadata by itself
D. The `resource` processor in a gateway, which sets resource attributes to fixed values you configure and does not look up pod metadata

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `k8sattributes` derives metadata from the source IP, which is typically rewritten by the time traffic reaches a gateway. It therefore belongs in an agent (DaemonSet or sidecar) close to the workload. The `attributes` and `resource` processors set static or transformed values rather than looking up pod metadata.
</details>

---

### Question 8
**Scenario:** What does the sampled flag in a `traceparent` header do?

A. Indicates whether the span has finished and is ready to export
B. Marks the span as an error for the backend so that error-rate dashboards include it in their calculations
C. Identifies the exporter used by the sender
D. Tells downstream services that the trace was already sampled in, so they should honor the decision

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The trace flags byte carries the sampled bit, which is how a consistent sampling decision propagates across services. This is what makes parent-based sampling produce complete traces rather than partially collected ones.
</details>

---

### Question 9
**Scenario:** A team needs percentiles for request duration. Which instrument is required?

A. Up-down counter, which records a value that moves up and down such as queue depth but keeps no distribution of observed values
B. Counter, which only increases and sums to a total, so it can give a request rate but cannot produce a percentile of durations
C. Gauge, which captures the latest observed value at each collection and does not keep the spread of individual measurements
D. Histogram

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Percentiles require a distribution, which only a histogram records. A gauge holds a single current value and cannot yield percentiles. Counters record monotonic totals.
</details>

---

### Question 10
**Scenario:** Which statement about baggage is correct?

A. It is encrypted in transit by the SDK, so sensitive values such as customer identifiers can be carried safely between services in headers
B. It propagates key-value pairs across service boundaries in headers and must not carry secrets
C. It replaces span attributes, so values set as baggage are automatically recorded on every span in the trace without further code
D. It is stored only within a single process and never leaves it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Baggage travels across every service in the request path as plain header content, so it is not a security boundary. It complements rather than replaces span attributes, and it is explicitly cross-process.
</details>

---

### Question 11
**Scenario:** A short-lived batch job is instrumented correctly but its spans never appear in the backend.

A. The batch span processor never flushed its buffered spans before the short-lived process exited
B. The sampler is dropping them because the job runs briefly
C. Batch jobs cannot be traced because tracing needs a long-running process
D. The exporter protocol is wrong, so the SDK logs repeated connection errors during the run and the spans never leave the process

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The batch processor buffers spans and exports periodically. A process that exits without an explicit SDK shutdown loses whatever is still buffered. Short-lived processes need an explicit shutdown call, or a simple span processor.
</details>

---

### Question 12
**Scenario:** Which Collector metric indicates that the memory limiter is shedding load?

A. `otelcol_exporter_queue_size`, which shows how full the exporter's sending queue is and points at a slow backend, not a memory limiter
B. `otelcol_receiver_refused_spans`
C. `otelcol_exporter_send_failed_spans`, which counts spans that an exporter tried to send and failed, a symptom of the backend side
D. `otelcol_processor_dropped_spans`, which counts spans a processor discarded, such as through a filter rule, and not refusals at the receiver

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Refused-at-receiver is the signature of memory limiter backpressure. Send-failed indicates a backend problem. Processor-dropped indicates a filter or sampling decision. Queue size climbing toward capacity warns that dropping is imminent, but refusal is what the limiter itself produces.
</details>

---

### Question 13
**Scenario:** What is the purpose of the `spanmetrics` connector?

A. Batching spans before export so the exporter sends fewer, larger requests
B. Deriving rate, error, and duration metrics from spans, so spans can then be sampled more aggressively
C. Converting existing metrics into spans for search in the tracing backend
D. Enriching spans with metric values from the host, such as CPU and memory, so that slow spans can be correlated with load

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A connector consumes from one pipeline and emits into another. `spanmetrics` computes RED metrics from 100% of spans in the Collector, which lets you keep accurate aggregates while paying to store only a sample of the trace data.
</details>

---

### Question 14
**Scenario:** Which resource attribute is effectively mandatory, and what happens without it?

A. `service.name`; backends group telemetry under an unknown service
B. `host.name`; the Collector drops the telemetry
C. `telemetry.sdk.language`; the exporter errors when it is missing because the backend needs to know which SDK produced the data
D. `deployment.environment`; sampling fails without it because the sampler uses the environment to choose a ratio per tier

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `service.name` is the primary identifier backends use to group telemetry. Without it, everything lands under an unknown service, which makes the data close to unusable even though nothing errors.
</details>

---

### Question 15
**Scenario:** Which statement correctly distinguishes delta from cumulative temporality?

A. Delta reports the running total since process start; cumulative reports the change since the last export
B. They are the same thing with different names per backend
C. Cumulative reports the running total since start; delta reports the change since the last export
D. Delta applies only to histograms and cumulative only to counters

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cumulative payloads are larger and make restarts visible as resets, and Prometheus expects them. Delta payloads are smaller and require the backend to accumulate, and several commercial backends prefer them. Temporality is configurable per exporter and applies to counters and histograms alike.
</details>

---

### Question 16
**Scenario:** An HTTP server instrumentation records a request that returns 404 Not Found because the caller asked for an order ID that does not exist. What span status should the server span carry?

A. Error, because every 4xx or 5xx response code means the request failed on the server
B. Unset, because a 4xx on a server span reflects a caller mistake, not a server failure
C. Ok, because the server handled the request and sent back a well-formed response
D. Error only when the response body is empty, otherwise Ok with the code as an event

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The HTTP semantic conventions say a server span leaves status Unset for 4xx codes, because the server behaved correctly and the caller made the mistake. 5xx codes mark a server span as Error. Treating all 4xx as Error inflates server error rates with client mistakes. Ok is reserved for an application developer explicitly overriding the status, so instrumentation should not set it. The response body plays no part in the rule.

**Key Concept:** Server spans: 5xx is Error, 4xx stays Unset. Client spans: both 4xx and 5xx are Error. See [HTTP span semantic conventions](https://opentelemetry.io/docs/specs/semconv/http/http-spans/).
</details>

---

### Question 17
**Scenario:** A consumer pulls 50 messages from a queue and processes them in one operation. Each message carries the trace context of the request that produced it. How should the processing span relate to those 50 producer traces?

A. Make the processing span a child of the first message and record the other 49 as span events
B. Copy all 50 trace IDs into baggage so every downstream service can see the full batch
C. Create the processing span with a link to the span context of each message in the batch
D. Start 50 separate root spans and store the batch ID as a resource attribute on each one

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A span has one parent, but it can carry many links, and links exist for exactly this fan-in case: one operation causally related to many other traces. Parenting to the first message misrepresents the other 49. Baggage carries application key-values downstream and is not a way to relate spans. Fifty root spans fragment the work, and a resource attribute describes the emitting entity, not a single operation.

**Key Concept:** Span links connect a span to other span contexts, often in other traces, for batch and async work. See [Span links](https://opentelemetry.io/docs/concepts/signals/traces/#span-links).
</details>

---

### Question 18
**Scenario:** A latency histogram uses default bucket boundaries, which are too coarse for an API whose requests mostly finish under 50 ms. The team wants new boundaries for this one instrument without touching the instrumentation call sites. What should they do?

A. Recreate the instrument in each call site with the new boundaries passed at creation
B. Add a Collector processor that rebuckets histogram data points after they are exported
C. Put the boundaries in baggage so that every service applies the same bucket layout
D. Register a View in the SDK MeterProvider that overrides the aggregation for that instrument

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Views are the SDK mechanism for changing how an instrument is aggregated, including explicit bucket boundaries, renaming, and dropping attributes, all without editing the code that records measurements. Recreating the instrument at each call site is the code change the team wanted to avoid. Rebucketing after export cannot recover detail the coarse buckets already discarded. Baggage is request context and has nothing to do with aggregation.

**Key Concept:** A View selects instruments and customises their stream: name, attributes, and aggregation. See [Metrics SDK: View](https://opentelemetry.io/docs/specs/otel/metrics/sdk/#view).
</details>

---

### Question 19
**Scenario:** A busy production service exports spans over OTLP. Which span processor should the TracerProvider use, and why?

A. BatchSpanProcessor, because it queues ended spans and exports them in groups off the request path
B. SimpleSpanProcessor, because exporting each span the moment it ends guarantees nothing is lost
C. SimpleSpanProcessor, because holding no queue makes it use less memory under heavy load
D. No processor at all, because the exporter can be attached directly to the TracerProvider

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The batch processor buffers ended spans and exports them on a schedule or when the batch fills, so export cost is amortised and kept off the hot path. The simple processor exports synchronously on every span end, which adds latency per span and suits only debugging. It does not guarantee delivery either, since an export can still fail. Exporters are attached through a processor; there is no supported way to skip that layer.

**Key Concept:** Use the batch processor in production and the simple processor for tests and debugging. See [Tracing SDK: built-in span processors](https://opentelemetry.io/docs/specs/otel/trace/sdk/#built-in-span-processors).
</details>

---

### Question 20
**Scenario:** A team wants each service to start sampling 10% of new traces, while always following the sampling decision of an incoming parent span. Which environment variables do this?

A. `OTEL_TRACES_SAMPLER=traceidratio` with `OTEL_TRACES_SAMPLER_ARG=10`
B. `OTEL_TRACES_SAMPLER=always_on` with `OTEL_TRACES_SAMPLER_ARG=0.1`
C. `OTEL_TRACES_SAMPLER=parentbased_traceidratio` with `OTEL_TRACES_SAMPLER_ARG=0.1`
D. `OTEL_TRACES_SAMPLER=parentbased_always_off` with `OTEL_TRACES_SAMPLER_ARG=0.1`

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `parentbased_traceidratio` honours the parent's sampled flag when there is one and applies the ratio to new root traces. The argument is a probability between 0 and 1, so 10% is `0.1`. Plain `traceidratio` ignores the parent, and an argument of `10` is not a valid ratio. `always_on` ignores the argument and keeps everything. `parentbased_always_off` drops every new root trace.

**Key Concept:** Parent-based samplers keep traces whole across services; the ratio only decides for roots. See [SDK environment variables](https://opentelemetry.io/docs/languages/sdk-configuration/general/).
</details>

---

### Question 21
**Scenario:** A team runs a Java service they cannot change or rebuild this quarter. They want traces for its inbound HTTP and database calls. What is the quickest route?

A. Add the OpenTelemetry API dependency and rely on its default implementation
B. Deploy a Collector with the k8sattributes processor next to the service pods
C. Enable the Collector's Prometheus receiver to scrape the service's JVM metrics
D. Attach the OpenTelemetry Java agent to the JVM with the `-javaagent` flag

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The Java agent is zero-code instrumentation: it is added at JVM startup and instruments common libraries such as HTTP servers and JDBC without a rebuild. The API on its own is a no-op without an SDK, and it would need code changes anyway. The k8sattributes processor only enriches telemetry that already exists. Scraping JVM metrics gives metrics, not traces.

**Key Concept:** Zero-code instrumentation gives broad coverage fast; add manual spans later for business logic. See [Java agent](https://opentelemetry.io/docs/zero-code/java/agent/).
</details>

---

### Question 22
**Scenario:** A developer asks whether they should replace their SLF4J logging calls with calls to the OpenTelemetry Logs API. What is the intended role of the Logs API?

A. Bridging existing logging libraries, such as SLF4J or Log4j, into OpenTelemetry log records
B. Replacing logging frameworks with a new call that developers use directly in application code
C. Converting spans into log lines for teams that do not have a tracing backend available
D. Tailing log files from disk inside the SDK, which replaces the Collector's filelog receiver

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Logs API is designed for log appenders and bridges, so the logging library a team already uses can emit OpenTelemetry log records with trace context attached. Developers keep their existing logging calls. It is not a new end-user logging framework, it does not turn spans into logs, and reading files from disk is the job of the Collector's filelog receiver, not the SDK.

**Key Concept:** OpenTelemetry embraces existing logging libraries rather than replacing them. See [Logs specification](https://opentelemetry.io/docs/specs/otel/logs/).
</details>

---

### Question 23
**Scenario:** An engineer adds a second `otlp` exporter for a new backend under the `exporters:` key of a Collector config. The Collector starts cleanly, but no data reaches the new backend. What is the most likely cause?

A. The new exporter needs its own batch processor declared directly above it in the file
B. The exporter is defined but not listed in any pipeline under `service: pipelines:`
C. Exporters added to the file stay inactive until the Collector binary is rebuilt
D. A pipeline can hold one exporter per signal, so the first exporter always wins

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Defining a component only configures it. A component runs when it is referenced in a pipeline in the `service` section, and an unreferenced exporter is silently ignored. Processor placement is set in the pipeline, not by position in the file. Configuration changes need a restart, not a rebuild, unless the component is missing from the distribution. A pipeline can fan out to many exporters.

**Key Concept:** Configure components in their sections, then enable them in `service.pipelines`. See [Collector configuration: service](https://opentelemetry.io/docs/collector/configuration/#service).
</details>

---

### Question 24
**Scenario:** Spans reach a fleet of node-level Collector agents and then a pool of gateway Collectors that run the tail sampling processor. Sampling decisions are inconsistent because spans of one trace land on different gateways. What fixes this?

A. Run tail sampling in every node agent, since each agent sees the full trace
B. Move the tail sampling decision into the SDK so it is made before export
C. Route spans by trace ID with the loadbalancing exporter in the agent tier
D. Put a round-robin load balancer in front of the gateway pool instead

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Tail sampling needs every span of a trace on the same Collector instance. The loadbalancing exporter hashes on trace ID so all spans of a trace go to one gateway. A node agent sees only the spans produced on its node, not the whole trace. The SDK cannot make a tail decision because it never sees the complete trace. Round-robin balancing is what causes the split in the first place.

**Key Concept:** Tail sampling at scale is a two-tier pattern: trace-aware load balancing in front of sampling gateways. See [Gateway deployment](https://opentelemetry.io/docs/collector/deployment/gateway/).
</details>

---

### Question 25
**Scenario:** A security team wants the Collector to contain only the OTLP receiver, the batch and memory limiter processors, and one vendor exporter, to keep the binary and its attack surface small. What should the platform team do?

A. Build a custom distribution with the OpenTelemetry Collector Builder listing those components
B. Run the contrib distribution and leave the unused components out of the config file
C. Run the core distribution, which already includes every vendor exporter by default
D. Use the SDK's built-in exporter and skip running a Collector at all for this service

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Collector Builder (`ocb`) produces a binary containing only the components named in its manifest, which is the documented way to minimise size and attack surface. Contrib ships hundreds of components; leaving them out of the config does not remove them from the binary. Core is small but does not include vendor exporters. Dropping the Collector removes the processing the team wants to keep.

**Key Concept:** Core, contrib, and vendor distributions are starting points; production teams often build their own. See [Build a custom Collector](https://opentelemetry.io/docs/collector/custom-collector/).
</details>

---

### Question 26
**Scenario:** Kubernetes liveness probes hit `/healthz` every few seconds, and their spans make up 30% of trace volume. The team wants to drop them in the Collector before export. Which component fits?

A. The attributes processor, which can delete the `url.path` attribute from those spans
B. The batch processor, configured with a smaller batch size for that endpoint only
C. The memory limiter processor, which sheds the lowest-value spans under pressure
D. The filter processor, with a condition that matches spans whose path is `/healthz`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The filter processor drops telemetry that matches configured conditions, written in OTTL, which is exactly this job. The attributes processor changes attributes on a span but still forwards the span. The batch processor groups data for export and does not drop anything by content. The memory limiter refuses data when memory is high, regardless of value, and is a safety valve, not a filter.

**Key Concept:** Drop noise as early as possible, ideally before it costs storage. See [Filter processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/filterprocessor).
</details>

---

### Question 27
**Scenario:** A firewall team asks which ports to open so services can send OTLP to a Collector using its default receiver settings. What do you tell them?

A. 9411 for gRPC and 14268 for HTTP
B. 4317 for gRPC and 4318 for HTTP
C. 4318 for gRPC and 4317 for HTTP
D. 9090 for gRPC and 8888 for HTTP

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OTLP uses 4317 for gRPC and 4318 for HTTP by default. Swapping them is a common mistake. 9411 is the Zipkin port and 14268 a legacy Jaeger collector port. 9090 is the usual Prometheus server port, and 8888 is where the Collector exposes its own internal metrics, not a receiver.

**Key Concept:** OTLP is the native protocol for all signals, over gRPC or HTTP. See [OTLP specification](https://opentelemetry.io/docs/specs/otlp/).
</details>

---

### Question 28
**Scenario:** During an incident, an engineer finds a suspicious error log line and wants to jump straight to the request trace that produced it. What makes this possible?

A. The log line and the trace share the same `service.name`, which links each log to one trace
B. The backend matches the log timestamp to the nearest span start time in the same service
C. The log record carries the active trace ID and span ID, which are recorded when it is emitted
D. Baggage copies every log line into the span as an event, so the trace already holds the log

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** When a log is emitted inside an active span, OpenTelemetry log bridges attach the trace ID and span ID to the log record, so a backend can link the log to that exact span. `service.name` identifies a service, which has thousands of traces. Timestamp matching is a guess that breaks under concurrency. Baggage carries key-values between services and does not copy logs into spans.

**Key Concept:** Shared context, not shared timing, is what correlates signals. See [Logs: trace context](https://opentelemetry.io/docs/concepts/signals/logs/).
</details>

---

### Question 29
**Scenario:** Two teams record the HTTP method under different attribute names, `method` and `http_verb`, and a shared dashboard only works for one of them. What is the standard fix?

A. Pick whichever name the larger team uses and ask the other team to rename later
B. Add a resource attribute to each service that says which naming scheme it follows
C. Record the method as a span event rather than as an attribute so names do not matter
D. Adopt the semantic convention name, `http.request.method`, in both teams' instrumentation

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Semantic conventions define standard names, such as `http.request.method`, so telemetry from different teams, languages, and libraries lines up without per-team mapping. Picking a house name just recreates the problem with the next team. A resource attribute describing the scheme still leaves every query needing two paths. Events still have attribute names, so moving the data does not help.

**Key Concept:** Semantic conventions make telemetry portable across teams and backends. See [Semantic conventions](https://opentelemetry.io/docs/specs/semconv/).
</details>

---

### Question 30
**Scenario:** An engineer suspects a processor in the Collector is stripping attributes and wants to see exactly what the Collector is about to export, without changing the backend. What is the simplest check?

A. Add the debug exporter with `verbosity: detailed` to the pipeline alongside the real exporter
B. Raise the Collector's own log level to debug, which prints every span it receives in full
C. Point the SDK at a second backend and compare what the two backends end up storing
D. Remove the processors one at a time and wait for users to report what has changed

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The debug exporter writes telemetry to the Collector's console, and at `verbosity: detailed` it prints every attribute, so adding it next to the real exporter shows exactly what leaves the pipeline. Debug logging shows the Collector's own operation, not the full content of every span. A second backend adds its own processing and cost. Removing processors in production trades one problem for another and gives slow feedback.

**Key Concept:** Fan the pipeline out to the debug exporter to inspect data in flight. See [Debug exporter](https://github.com/open-telemetry/opentelemetry-collector/tree/main/exporter/debugexporter).
</details>

---

## Scoring guide

- **26-30 correct (85%+):** Ready. 75% is the pass mark, so this puts you comfortably clear.
- **20-25 correct (67-83%):** Focus on the API and SDK domain, which is 46% of the exam.
- **Below 20:** Work the [scenarios](../../exams/kubernetes/otca/scenarios.md) and read the OpenTelemetry concepts documentation directly; the exam tracks it closely.
