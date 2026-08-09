---
last-updated: 2026-08-09
difficulty: intermediate
---

# Prometheus Certified Associate (PCA) - Practice Questions

15 questions for PCA prep, weighted toward PromQL (28%), Prometheus fundamentals (20%), and observability concepts (18%).

PromQL is the largest domain and the one candidates most often under-practice, so more than a third of these questions are query semantics.

> **Cert page:** [exams/kubernetes/pca/](../../exams/kubernetes/pca/)

---

### Question 1
**Scenario:** A counter `http_requests_total` resets to zero when the process restarts. Which function handles that correctly when computing per-second traffic?

A. `delta()`
B. `rate()`
C. `changes()`
D. `deriv()`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `rate()` is built for counters and explicitly compensates for resets by treating a decrease as a restart. `delta()` and `deriv()` are for gauges and would produce a large negative value at a reset. `changes()` counts how often a value changed, which is a different question entirely.
</details>

---

### Question 2
**Scenario:** You need the 95th percentile request latency from a histogram metric `http_duration_seconds_bucket`.

A. `quantile(0.95, http_duration_seconds_bucket)`
B. `histogram_quantile(0.95, rate(http_duration_seconds_bucket[5m]))`
C. `topk(0.95, http_duration_seconds_bucket)`
D. `avg(http_duration_seconds_bucket) * 0.95`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Histogram buckets are cumulative counters, so you take `rate()` first and then `histogram_quantile()` over the result. The `le` label must be preserved, which is why an aggregation, if you add one, must use `by (le)`. `quantile()` aggregates across series rather than across a bucket distribution.
</details>

---

### Question 3
**Scenario:** How does Prometheus normally acquire metrics?

A. Applications push metrics to Prometheus
B. Prometheus scrapes HTTP endpoints exposed by targets on an interval
C. Prometheus reads log files
D. An agent forwards syslog

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The pull model is fundamental: Prometheus discovers targets and fetches `/metrics` on a schedule. Pull makes target health observable (`up` becomes 0 when a scrape fails) and makes it trivial to check a target by hand with curl. The Pushgateway exists only for short-lived batch jobs that die before a scrape can reach them.
</details>

---

### Question 4
**Scenario:** `rate(http_requests_total[1m])` returns no data for a target scraped every 60 seconds.

A. The metric does not exist
B. A range needs at least two samples; the window is too short relative to the scrape interval
C. `rate()` cannot be used on counters
D. The target is down

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** With a 60 second scrape interval, a 1 minute window may contain only one sample and `rate()` needs at least two. The usual rule of thumb is a range window of at least four times the scrape interval, so `[5m]` here. This is the most common "my query is empty" cause in practice.
</details>

---

### Question 5
**Scenario:** Which metric type fits "current number of items in a queue"?

A. Counter
B. Gauge
C. Histogram
D. Summary

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A gauge can go up and down and represents a value at a point in time. Counters only increase (and reset to zero). Histograms and summaries describe distributions of observations such as request durations or response sizes.
</details>

---

### Question 6
**Scenario:** You want total requests per second across all instances of a job, broken out by HTTP status code.

A. `sum(rate(http_requests_total[5m])) by (status)`
B. `rate(sum(http_requests_total) by (status)[5m])`
C. `sum by (instance) (http_requests_total)`
D. `avg(rate(http_requests_total[5m]))`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Always `rate()` first, then `sum()`. Summing raw counters across instances produces nonsense at restarts because one series resetting drags the sum down. Option B is not valid syntax anyway. Averaging rates gives per-instance average, not total.
</details>

---

### Question 7
**Scenario:** An alert should only fire if the condition has held continuously for 10 minutes.

A. Set `for: 10m` in the alerting rule
B. Set `group_wait: 10m` in Alertmanager
C. Use `[10m]` in the expression
D. Set `evaluation_interval: 10m`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `for` makes the alert stay pending until the expression has been true for that whole duration, which is the standard flap suppression. `group_wait` delays the first notification for a group after an alert already fired. A range selector changes what the query computes. The evaluation interval changes how often rules run.
</details>

---

### Question 8
**Scenario:** Which component sends notifications to Slack, PagerDuty, and email?

A. Prometheus server
B. Alertmanager
C. Grafana
D. Node exporter

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Prometheus evaluates rules and pushes firing alerts to Alertmanager, which owns grouping, inhibition, silencing, and routing to receivers. Grafana can alert too, but in the Prometheus stack the exam cares about, Alertmanager is the answer. Node exporter exposes host metrics.
</details>

---

### Question 9
**Scenario:** A team needs metrics from a system that cannot be modified to expose `/metrics`.

A. Write a recording rule
B. Deploy an exporter that translates the system's data into Prometheus format
C. Use the Pushgateway
D. Increase the scrape interval

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Exporters exist exactly for this: they sit beside a system, read its native interface, and expose Prometheus metrics. There are exporters for databases, hardware, SNMP, and much more. Pushgateway is for ephemeral batch jobs, and recording rules precompute queries over data you already have.
</details>

---

### Question 10
**Scenario:** A dashboard query is slow because it aggregates a costly expression evaluated over many series.

A. Add more labels
B. Create a recording rule that precomputes the expression at evaluation time
C. Lower the scrape interval
D. Increase retention

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Recording rules store the result of an expression as a new time series, so the dashboard reads one cheap series instead of recomputing. Adding labels increases cardinality and makes it worse. Scrape interval and retention are not the bottleneck here.
</details>

---

### Question 11
**Scenario:** A metric is labeled with a user ID. What is the concern?

A. Nothing, labels are free
B. High cardinality: each distinct label value creates a separate time series and can exhaust memory
C. Labels must be numeric
D. Prometheus rejects string labels

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cardinality is the number one operational hazard in Prometheus. Unbounded label values such as user IDs, request IDs, or full URLs multiply series count without bound. Keep labels to values from a small, known set, and put the high-cardinality detail in logs or traces instead.
</details>

---

### Question 12
**Scenario:** How do you check whether a scrape target is currently reachable?

A. `up{job="myjob"}`
B. `scrape_duration_seconds`
C. `process_start_time_seconds`
D. `prometheus_build_info`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Prometheus synthesizes an `up` metric per target on every scrape: 1 for success, 0 for failure. `absent(up{job="myjob"})` covers the harder case where the target has disappeared from service discovery entirely, which is worth knowing because a missing target produces no `up == 0` at all.
</details>

---

### Question 13
**Scenario:** Which service discovery mechanism would you use for pods in a Kubernetes cluster?

A. `static_configs`
B. `kubernetes_sd_configs`
C. `file_sd_configs`
D. `dns_sd_configs`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Kubernetes SD queries the API server for nodes, pods, services, endpoints, and ingresses, and relabeling turns those into scrape targets. Static configs cannot follow a changing pod set. File SD and DNS SD are generic alternatives that would require you to maintain the mapping yourself.
</details>

---

### Question 14
**Scenario:** You need to drop a noisy metric before it is stored.

A. `metric_relabel_configs` with a `drop` action matching `__name__`
B. `relabel_configs` on the target
C. A recording rule
D. Delete it after ingestion

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `relabel_configs` runs before the scrape and selects and rewrites targets, while `metric_relabel_configs` runs after the scrape and filters individual samples. Dropping a metric by name is the second case. Prometheus has no efficient selective delete after storage.
</details>

---

### Question 15
**Scenario:** A long-term storage and global query view is needed across several Prometheus servers.

A. Increase local retention to 5 years
B. Use remote write to a system such as Thanos, Cortex, or Mimir
C. Run one enormous Prometheus
D. Federate every metric from every server

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Prometheus local storage is deliberately designed for the recent window on a single node, with no clustering. Remote write ships samples to a horizontally scalable backend that provides long retention and a global query layer. Federation exists but is intended for pulling a small set of aggregated series, not everything.
</details>

---

## Where to go deeper

- [PCA cert page](../../exams/kubernetes/pca/) - notes, practice plan, strategy
- [OTCA practice questions](./cncf-otca.md) - the OpenTelemetry counterpart
- [Observability basics](../../learn/concepts/observability-basics.md) - logs, metrics, traces in plain English
- [Observability topic index](../../topics/observability.md) - everything the repo has on this
- **[📖 Prometheus documentation](https://prometheus.io/docs/)** - primary source
