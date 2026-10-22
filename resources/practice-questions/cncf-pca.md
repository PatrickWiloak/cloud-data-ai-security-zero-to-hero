---
last-updated: 2026-10-22
difficulty: intermediate
---

# Prometheus Certified Associate (PCA) - Practice Questions

30 questions for PCA prep, weighted toward PromQL (28%), Prometheus fundamentals (20%), and observability concepts (18%).

PromQL is the largest domain and the one candidates most often under-practice, so more than a third of these questions are query semantics.

> **Cert page:** [exams/kubernetes/pca/](../../exams/kubernetes/pca/)

---

### Question 1
**Scenario:** A counter `http_requests_total` resets to zero when the process restarts. Which function handles that correctly when computing per-second traffic?

A. `delta()`
B. `changes()`, which counts how many times the value changed in the window
C. `deriv()`
D. `rate()`, which compensates for counter resets

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `rate()` is built for counters and explicitly compensates for resets by treating a decrease as a restart. `delta()` and `deriv()` are for gauges and would produce a large negative value at a reset. `changes()` counts how often a value changed, which is a different question entirely.
</details>

---

### Question 2
**Scenario:** You need the 95th percentile request latency from a histogram metric `http_duration_seconds_bucket`.

A. `quantile(0.95, http_duration_seconds_bucket)`, taking the 95th percentile across the bucket series at the latest sample, without `rate()`
B. `histogram_quantile(0.95, rate(http_duration_seconds_bucket[5m]))`
C. `avg(http_duration_seconds_bucket) * 0.95`, scaling the average bucket count to estimate where 95 percent of requests fall
D. `topk(0.95, http_duration_seconds_bucket)`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Histogram buckets are cumulative counters, so you take `rate()` first and then `histogram_quantile()` over the result. The `le` label must be preserved, which is why an aggregation, if you add one, must use `by (le)`. `quantile()` aggregates across series rather than across a bucket distribution.
</details>

---

### Question 3
**Scenario:** How does Prometheus normally acquire metrics?

A. An agent on each host forwards syslog messages to the Prometheus server, which parses them into samples as they arrive
B. Prometheus tails the log files written by each application and extracts a sample from every line it reads
C. Prometheus scrapes HTTP endpoints exposed by targets on an interval, which it discovers through service discovery and fetches on a schedule
D. Applications push metrics to Prometheus by sending each sample to a write endpoint when it is recorded

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The pull model is fundamental: Prometheus discovers targets and fetches `/metrics` on a schedule. Pull makes target health observable (`up` becomes 0 when a scrape fails) and makes it trivial to check a target by hand with curl. The Pushgateway exists only for short-lived batch jobs that die before a scrape can reach them.
</details>

---

### Question 4
**Scenario:** `rate(http_requests_total[1m])` returns no data for a target scraped every 60 seconds.

A. `rate()` cannot be used on counters, only on gauges, so the query is invalid and returns an empty result by design
B. A range needs at least two samples; the window is too short for the scrape interval
C. The metric does not exist on the target, so the selector matches no series and the function returns nothing for it
D. The rule evaluation interval is longer than the range window, so Prometheus skips evaluation and returns no data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** With a 60 second scrape interval, a 1 minute window may contain only one sample and `rate()` needs at least two. The usual rule of thumb is a range window of at least four times the scrape interval, so `[5m]` here. This is the most common "my query is empty" cause in practice.
</details>

---

### Question 5
**Scenario:** Which metric type fits "current number of items in a queue"?

A. A gauge, since it rises and falls
B. A histogram with buckets for the queue length
C. A summary with quantiles over the queue length
D. A counter

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A gauge can go up and down and represents a value at a point in time. Counters only increase (and reset to zero). Histograms and summaries describe distributions of observations such as request durations or response sizes.
</details>

---

### Question 6
**Scenario:** You want total requests per second across all instances of a job, broken out by HTTP status code.

A. `sum(rate(http_requests_total[5m])) by (status)`
B. `sum by (instance) (http_requests_total)`, which adds the raw counters per instance without applying `rate()` or grouping by status
C. `avg(rate(http_requests_total[5m]))`, which applies `rate()` first but returns one average across series, with no status breakdown
D. `rate(sum(http_requests_total) by (status)[5m])`, which tries to take a rate over the aggregated sum of the raw counters

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Always `rate()` first, then `sum()`. Summing raw counters across instances produces nonsense at restarts because one series resetting drags the sum down. Option D is not valid syntax anyway. Averaging rates gives per-instance average, not total.
</details>

---

### Question 7
**Scenario:** An alert should only fire if the condition has held continuously for 10 minutes.

A. Set `evaluation_interval: 10m` in the global config
B. Set `group_wait: 10m` in the Alertmanager route
C. Set `for: 10m` in the alerting rule
D. Use `[10m]` in the expression

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `for` makes the alert stay pending until the expression has been true for that whole duration, which is the standard flap suppression. `group_wait` delays the first notification for a group after an alert already fired. A range selector changes what the query computes. The evaluation interval changes how often rules run.
</details>

---

### Question 8
**Scenario:** Which component sends notifications to Slack, PagerDuty, and email?

A. Grafana
B. The Alertmanager component
C. Node exporter
D. The Prometheus server itself, evaluating rules

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Prometheus evaluates rules and pushes firing alerts to Alertmanager, which owns grouping, inhibition, silencing, and routing to receivers. Grafana can alert too, but in the Prometheus stack the exam cares about, Alertmanager is the answer. Node exporter exposes host metrics.
</details>

---

### Question 9
**Scenario:** A team needs metrics from a system that cannot be modified to expose `/metrics`.

A. Increase the scrape interval so the target is queried less often, which reduces load on the system being monitored
B. Write a recording rule that converts the system's data into Prometheus format at evaluation time
C. Use the Pushgateway so the system can send its data to Prometheus in the exposition format on its own schedule
D. Deploy an exporter that translates the system's data into Prometheus format

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Exporters exist exactly for this: they sit beside a system, read its native interface, and expose Prometheus metrics. There are exporters for databases, hardware, SNMP, and much more. Pushgateway is for ephemeral batch jobs, and recording rules precompute queries over data you already have.
</details>

---

### Question 10
**Scenario:** A dashboard query is slow because it aggregates a costly expression evaluated over many series.

A. Create a recording rule that precomputes the expression at evaluation time
B. Increase retention so the dashboard can read more history from disk, which also makes the slow query run faster
C. Add more labels to the series so that the query can select and group its data more precisely
D. Lower the scrape interval

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Recording rules store the result of an expression as a new time series, so the dashboard reads one cheap series instead of recomputing. Adding labels increases cardinality and makes it worse. Scrape interval and retention are not the bottleneck here.
</details>

---

### Question 11
**Scenario:** A metric is labeled with a user ID. What is the concern?

A. Labels must be numeric values only, so a user ID in string form is rejected at ingestion
B. Prometheus rejects string labels and drops any sample with a non-numeric label value
C. High cardinality: each distinct label value creates a separate time series and can exhaust memory
D. Nothing to worry about, because labels are free and Prometheus stores them once per target rather than once per series

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cardinality is the number one operational hazard in Prometheus. Unbounded label values such as user IDs, request IDs, or full URLs multiply series count without bound. Keep labels to values from a small, known set, and put the high-cardinality detail in logs or traces instead.
</details>

---

### Question 12
**Scenario:** How do you check whether a scrape target is currently reachable?

A. `prometheus_build_info`
B. `up{job="myjob"}`, which is 1 when the last scrape worked
C. `process_start_time_seconds`, which reports when the monitored process last started and restarted
D. `scrape_duration_seconds`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Prometheus synthesizes an `up` metric per target on every scrape: 1 for success, 0 for failure. `absent(up{job="myjob"})` covers the harder case where the target has disappeared from service discovery entirely, which is worth knowing because a missing target produces no `up == 0` at all.
</details>

---

### Question 13
**Scenario:** Which service discovery mechanism would you use for pods in a Kubernetes cluster?

A. `file_sd_configs`, reading targets from a JSON or YAML file that the cluster updates whenever pods are created or deleted
B. `dns_sd_configs`, resolving service names with SRV records so each pod appears as a target without extra configuration
C. `kubernetes_sd_configs`, which asks the API server for pods and services and turns them into scrape targets through relabeling, tracking changes as they happen
D. `static_configs`, listing the pod addresses by hand, which works when the set of pods does not change over time

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Kubernetes SD queries the API server for nodes, pods, services, endpoints, and ingresses, and relabeling turns those into scrape targets. Static configs cannot follow a changing pod set. File SD and DNS SD are generic alternatives that would require you to maintain the mapping yourself.
</details>

---

### Question 14
**Scenario:** You need to drop a noisy metric before it is stored.

A. `metric_relabel_configs` with a `drop` action matching `__name__`
B. A recording rule that replaces the noisy metric with an aggregated one, which still leaves the original series stored
C. Delete it after it has been stored, using the admin API, which removes the series but leaves storage used until compaction
D. `relabel_configs` on the target, which can drop whole targets or rewrite their labels before the scrape happens

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `relabel_configs` runs before the scrape and selects and rewrites targets, while `metric_relabel_configs` runs after the scrape and filters individual samples. Dropping a metric by name is the second case. Prometheus has no efficient selective delete after storage.
</details>

---

### Question 15
**Scenario:** A long-term storage and global query view is needed across several Prometheus servers.

A. Increase local retention to 5 years on each server, which keeps data longer but leaves each server's view separate
B. Run one enormous Prometheus that scrapes every target, which gives one view but is a single point of failure with limited scale
C. Federate every metric from every server into a central one, which would copy all series and so double the storage needed
D. Use remote write to a horizontally scalable backend such as Thanos, Cortex, or Mimir, with a global query layer on top of it for all servers

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Prometheus local storage is deliberately designed for the recent window on a single node, with no clustering. Remote write ships samples to a horizontally scalable backend that provides long retention and a global query layer. Federation exists but is intended for pulling a small set of aggregated series, not everything.
</details>

---

### Question 16
**Scenario:** You want the error ratio per instance. `http_errors_total` carries a `code` label that `http_requests_total` does not, and a plain division of the two rates returns no results. Which query works?

A. `rate(http_errors_total[5m]) / on(code) group_right rate(http_requests_total[5m])`
B. `sum without(code) (rate(http_errors_total[5m])) / rate(http_requests_total[5m])`
C. `rate(http_errors_total[5m]) / rate(http_requests_total[5m]) > bool 0`
D. `rate(http_errors_total[5m]) or rate(http_requests_total[5m]) / 100`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Binary operators match series with exactly the same label sets, so the extra `code` label means nothing matches. Aggregating `code` away with `sum without(code)` leaves both sides with the same labels, and the division matches one-to-one. Matching `on(code)` uses a label the right side does not have, so nothing matches. Adding a comparison does not fix the label mismatch. `or` is a set union, not a ratio.

**Key Concept:** Vector matching is by label set; align labels with aggregation, `on`, or `ignoring`. See [PromQL vector matching](https://prometheus.io/docs/prometheus/latest/querying/operators/#vector-matching).
</details>

---

### Question 17
**Scenario:** A product manager asks how many checkout requests were served in the last hour. `checkout_requests_total` is a counter. Which query answers that directly?

A. `rate(checkout_requests_total[1h])`
B. `delta(checkout_requests_total[1h])`
C. `sum_over_time(checkout_requests_total[1h])`
D. `increase(checkout_requests_total[1h])`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `increase()` returns the total growth of a counter over the range, handling resets, which is the count the manager wants. `rate()` returns the per-second average, so it would need multiplying by 3600. `delta()` is meant for gauges and does not handle counter resets. `sum_over_time()` adds up raw sample values, which for a cumulative counter produces a meaningless number.

**Key Concept:** `increase()` is `rate()` multiplied by the range in seconds, and both are for counters only. See [increase()](https://prometheus.io/docs/prometheus/latest/querying/functions/#increase).
</details>

---

### Question 18
**Scenario:** A dashboard should show current request rate divided by the rate at the same time one week earlier, to spot unusual traffic. Which query does that?

A. `rate(http_requests_total[5m]) / rate(http_requests_total[5m] offset 1w)`
B. `rate(http_requests_total[5m]) / rate(http_requests_total[1w])`
C. `rate(http_requests_total[5m]) / increase(http_requests_total[1w]) * 7`
D. `rate(http_requests_total[5m] @ 1w) / rate(http_requests_total[5m])`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The `offset` modifier shifts the evaluation time of a selector into the past, so `offset 1w` gives the same 5 minute window from a week ago. A 1 week range gives the average over the entire week, not the same moment last week. Dividing by a weekly increase mixes units. The `@` modifier takes an absolute Unix timestamp, not a duration.

**Key Concept:** `offset` is relative time; `@` is absolute time. See [Offset modifier](https://prometheus.io/docs/prometheus/latest/querying/basics/#offset-modifier).
</details>

---

### Question 19
**Scenario:** An on-call engineer wants a table of the five pods using the most memory right now, from `container_memory_working_set_bytes`. Which query returns exactly that?

A. `sort_desc(sum by (pod) (container_memory_working_set_bytes))`
B. `max by (pod) (container_memory_working_set_bytes) > 5`
C. `topk(5, sum by (pod) (container_memory_working_set_bytes))`
D. `bottomk(5, sum by (pod) (container_memory_working_set_bytes))`

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `topk(5, ...)` keeps the five series with the largest values. `sort_desc` orders every series but still returns all of them. Comparing against 5 filters on a value of 5 bytes, not a count of pods. `bottomk` returns the five smallest.

**Key Concept:** `topk` and `bottomk` select by value; they are aggregation operators and accept `by` and `without`. See [Aggregation operators](https://prometheus.io/docs/prometheus/latest/querying/operators/#aggregation-operators).
</details>

---

### Question 20
**Scenario:** A team runs Prometheus with default flags and notices that queries for data older than about two weeks return nothing. What explains this, and what changes it?

A. Prometheus compacts old blocks into one sample per day; set `--storage.tsdb.min-block-duration`
B. Scrape targets only keep two weeks of history; increase `scrape_timeout` on each job
C. Remote write has failed silently; set `--storage.remote.flush-deadline` higher
D. Default local retention is 15 days; raise it with `--storage.tsdb.retention.time`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The local TSDB keeps data for 15 days unless retention is set by time or size. Prometheus does not downsample old data; that is a feature of systems like Thanos. Targets do not hold history at all, since Prometheus stores the samples. Remote write sends copies elsewhere and does not affect local retention.

**Key Concept:** Local storage is not designed as long-term storage; use retention flags for local and remote write for durability. See [Storage](https://prometheus.io/docs/prometheus/latest/storage/).
</details>

---

### Question 21
**Scenario:** Each of five clusters runs its own Prometheus. A central Prometheus needs only a handful of pre-aggregated, job-level series from each cluster for a global dashboard. Which built-in approach fits?

A. Hierarchical federation, scraping each cluster's `/federate` endpoint with `match[]`
B. Pointing the central server at every pod in every cluster as direct scrape targets
C. Running the Pushgateway in each cluster and pushing all series to the center
D. Configuring each cluster's Alertmanager to forward series to the central server

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Federation lets one Prometheus scrape selected series from another through `/federate`, and hierarchical federation is the documented pattern for pulling aggregated series into a global view. Scraping every pod centrally defeats the per-cluster split and crosses network boundaries at scale. The Pushgateway is for batch jobs, not for relaying servers. Alertmanager handles alerts, not series.

**Key Concept:** Federate aggregates, not raw series; for full global data, use remote write to a long-term store. See [Federation](https://prometheus.io/docs/prometheus/latest/federation/).
</details>

---

### Question 22
**Scenario:** A developer is naming a new counter that tracks how much data a service has sent over the network. Which name follows Prometheus naming conventions?

A. `networkTransmitKilobytes`
B. `network_transmit_bytes_total`
C. `network_transmit_kilobytes_sum`
D. `total_network_bytes_counter`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Conventions are snake_case, a base unit (bytes, not kilobytes) as a suffix, and `_total` for counters. Camel case breaks the convention. Kilobytes is not a base unit, and `_sum` is the suffix used for histogram and summary sums. Putting `total` first and `counter` at the end is not the standard shape.

**Key Concept:** Use base units, a unit suffix, and `_total` on counters. See [Metric and label naming](https://prometheus.io/docs/practices/naming/).
</details>

---

### Question 23
**Scenario:** An SRE is building a checklist for a storage array that keeps slowing down. They want a method aimed at resources such as disks, CPUs, and network links rather than at request-driven services. Which method fits?

A. RED: rate, errors, duration
B. The four golden signals, which apply only to queues
C. USE: utilization, saturation, errors
D. The SLA method: target, penalty, measurement

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The USE method checks every resource for utilization, saturation, and errors, which suits hardware like a storage array. RED is the request-oriented counterpart for services. The golden signals cover user-facing systems in general, not only queues. There is no standard "SLA method"; an SLA is a contract, not a troubleshooting method.

**Key Concept:** USE for resources, RED for services, golden signals for user-facing systems. See [Prometheus instrumentation practices](https://prometheus.io/docs/practices/instrumentation/).
</details>

---

### Question 24
**Scenario:** A service has an availability SLO of 99.9% over a 30 day window. Roughly how much full downtime does its error budget allow in that window?

A. About 43 minutes
B. About 4 minutes
C. About 7 hours
D. About 9 hours

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** 0.1% of 30 days is 0.001 x 43,200 minutes, which is 43.2 minutes. About 4 minutes is the budget for 99.99%. About 7 hours is 1% of 30 days, which is the 99% budget. About 9 hours is 0.1% of a full year, a common mix-up of windows.

**Key Concept:** Error budget = (1 - SLO) x window. See [SLOs in the Google SRE book](https://sre.google/sre-book/service-level-objectives/).
</details>

---

### Question 25
**Scenario:** A worker pool's job queue keeps growing during peak hours, even though latency for completed jobs looks normal and no errors are logged. Which of the four golden signals does queue growth most directly measure?

A. Latency
B. Traffic
C. Errors
D. Saturation

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Saturation is how full a service is, and a growing queue is a classic early saturation signal, often appearing before latency rises. Latency measures how long completed work takes, which looks normal here. Traffic measures demand, not the backlog. No errors are being logged.

**Key Concept:** Saturation is often a leading indicator; alert on it before users feel latency. See [Monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/).
</details>

---

### Question 26
**Scenario:** A nightly database backup job runs for 4 minutes and exits. The team wants to record when it last succeeded and how long it took, but it is never running when Prometheus scrapes. What is the recommended approach?

A. Add the job as a static scrape target and lower its scrape interval to 10 seconds
B. Push the job's metrics to a Pushgateway at the end of the run, and scrape the Pushgateway
C. Write the metrics to a log line and run a log exporter that converts lines to samples
D. Keep the job's process alive after the backup so the next scrape can still reach it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Pushgateway exists for service-level batch jobs that cannot be scraped; the job pushes its final metrics and Prometheus scrapes the gateway. A faster scrape interval may still miss a short job and would not cover jobs that fail early. Log conversion is fragile and indirect. Keeping a process alive only to be scraped wastes resources and still has gaps.

**Key Concept:** Use the Pushgateway only for batch jobs, not as a general push channel. See [When to use the Pushgateway](https://prometheus.io/docs/practices/pushing/).
</details>

---

### Question 27
**Scenario:** Ten replicas each expose a latency summary with a precomputed 0.99 quantile. A team averages the ten values to get a fleet-wide p99. What is wrong with this?

A. Quantiles from summaries cannot be correctly aggregated across instances
B. Summaries only support the 0.5 quantile, so the 0.99 values are estimates
C. Averaging is correct, but it must use `max` rather than `avg` to be valid
D. Summaries are gauges, so their values have to go through `rate()` first

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A summary computes quantiles on each client, and the average of ten p99 values is not the p99 of the combined traffic. Histograms solve this: sum the bucket rates across instances, then run `histogram_quantile`. Summaries support any configured quantiles. Using `max` gives an upper bound, not a correct quantile. Summary quantiles are not counters that need `rate()`.

**Key Concept:** Use histograms when you need to aggregate quantiles across instances. See [Histograms and summaries](https://prometheus.io/docs/practices/histograms/).
</details>

---

### Question 28
**Scenario:** A Grafana panel uses `rate(http_requests_total[$__interval])`. When zoomed in, the graph shows gaps and empty points. Prometheus scrapes every 30 seconds. What is the best fix?

A. Hard-code the range to `[30s]` so it always matches the scrape interval
B. Switch the query from `rate()` to `irate()` and keep `$__interval` as is
C. Use `$__rate_interval`, which keeps the range at least four scrape intervals
D. Set the panel's minimum interval to 1 second so more points are drawn

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** When zoomed in, `$__interval` can shrink below two scrape intervals, leaving windows with fewer than two samples, so `rate()` returns nothing. Grafana's `$__rate_interval` is designed for `rate()` and stays at least four times the scrape interval. A `[30s]` range holds at most one or two samples. `irate()` still needs two samples in the window. A smaller minimum interval makes the problem worse.

**Key Concept:** In Grafana, use `$__rate_interval` with `rate()` and `increase()`. See [Grafana: $__rate_interval](https://grafana.com/docs/grafana/latest/datasources/prometheus/template-variables/#use-__rate_interval).
</details>

---

### Question 29
**Scenario:** When a cluster loses its network, a `ClusterDown` critical alert fires along with dozens of warning alerts from services in that same cluster. The team wants only the critical page while the cluster is down. Which Alertmanager feature does this?

A. A silence created by hand for each warning alert during the outage
B. A longer `repeat_interval` on the route that handles warning alerts
C. A `for` clause on every warning rule so they wait 30 minutes to fire
D. An inhibit rule that mutes warnings matching the critical alert's `cluster`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Inhibition suppresses alerts that match a target matcher while a source alert is firing, with `equal` labels such as `cluster` limiting it to the same cluster. Manual silences are slow and easy to forget to remove. A longer repeat interval still sends the first notification. A long `for` delays every warning, including real ones when the cluster is healthy.

**Key Concept:** Inhibition is automatic, conditional muting tied to another alert. See [Alertmanager inhibition](https://prometheus.io/docs/alerting/latest/alertmanager/#inhibition).
</details>

---

### Question 30
**Scenario:** A storage outage triggers 200 alerts with the same alert name across one cluster, and the on-call engineer gets 200 separate notifications. Which change reduces this to one notification per cluster?

A. Add a silence for the alert name so that further alerts are hidden
B. Set `group_by: ['alertname', 'cluster']` on the Alertmanager route
C. Raise the Prometheus `evaluation_interval` so rules fire less often
D. Lower `group_wait` to zero so Alertmanager sends alerts immediately

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Grouping batches alerts with the same values for the `group_by` labels into one notification. A silence hides the alerts entirely, including the one the engineer needs. A slower evaluation interval delays detection without grouping anything. Lowering `group_wait` sends sooner and gives less time to collect alerts into a group.

**Key Concept:** Grouping, inhibition, and silences are Alertmanager's three noise controls. See [Alertmanager grouping](https://prometheus.io/docs/alerting/latest/alertmanager/#grouping).
</details>

---

## Where to go deeper

- [PCA cert page](../../exams/kubernetes/pca/) - notes, practice plan, strategy
- [OTCA practice questions](./cncf-otca.md) - the OpenTelemetry counterpart
- [Observability basics](../../learn/concepts/observability-basics.md) - logs, metrics, traces in plain English
- [Observability topic index](../../topics/observability.md) - everything the repo has on this
- **[📖 Prometheus documentation](https://prometheus.io/docs/)** - primary source
