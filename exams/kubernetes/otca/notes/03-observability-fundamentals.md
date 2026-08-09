---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 10 min
---

# 03 - Fundamentals of observability

**Domain 3: Fundamentals of Observability (18%)**

---

## Monitoring versus observability

**Monitoring** asks known questions: is CPU above 80%, is the error rate above 1%. You decide the questions in advance and build dashboards and alerts for them.

**Observability** is the property of being able to ask new questions without shipping new code. When a novel failure appears, you can interrogate existing telemetry to understand it.

The practical difference is cardinality and context. A monitoring system aggregates aggressively because it only needs the questions you anticipated. An observable system preserves enough context on individual events to answer questions nobody thought of.

---

## The signals

| Signal | Strength | Weakness | Cost driver |
|---|---|---|---|
| **Traces** | Causality and latency across services | Sampling means not every request is retained | Span volume |
| **Metrics** | Cheap aggregates, good for alerting and trends | Cannot explain a single request | Time series cardinality |
| **Logs** | Full detail of what code did | Expensive at volume, hard to aggregate | Volume and retention |

They are complementary. Metrics tell you something is wrong, traces tell you where, logs tell you exactly what.

**Correlation** is what makes them a system rather than three tools:
- **Exemplars** attach a trace ID to a metric data point, so a latency spike links to an example slow trace
- **Trace context on log records** links logs to the request that produced them
- **Shared resource attributes** (`service.name`, `k8s.pod.name`) join all three to the same entity

---

## Cardinality

The dominant cost and performance factor in metrics.

Each unique combination of attribute values is a separate time series. A counter with `method` (5 values) and `status` (6 values) is 30 series. Add `user_id` with 100,000 values and it becomes 3,000,000.

Unbounded attributes to keep off metrics: user ID, session ID, request ID, raw URL path, full error message, timestamp, IP address.

Controls:
- Use `http.route` (the templated path) rather than the raw target
- Drop or aggregate attributes with SDK **views**
- Filter or transform in the Collector
- Put high-cardinality data on **spans and logs**, where it belongs, and keep metrics low-cardinality

---

## Semantic conventions

Standardized attribute and metric names so that telemetry from different languages, libraries, and vendors is comparable.

Examples: `http.request.method`, `http.response.status_code`, `http.route`, `server.address`, `db.system`, `db.query.text`, `messaging.system`, `error.type`.

Why it matters practically: a dashboard or alert written against conventional names works across every service, in any language, without per-service customization. Inventing your own names is the fastest way to make telemetry unusable at scale.

Conventions have stability levels; some are stable and some experimental, and experimental ones can change between releases.

---

## SLIs, SLOs, and error budgets

- **SLI** (service level indicator) - a measured signal of user-visible behavior, such as the proportion of requests served successfully in under 300 ms.
- **SLO** (service level objective) - the target for that indicator, such as 99.9% over 30 days.
- **Error budget** - the allowed shortfall, here 0.1%, which is roughly 43 minutes in 30 days. It converts reliability from an argument into arithmetic: if the budget is intact, ship; if it is spent, stabilize.
- **SLA** - a contractual commitment, usually looser than the internal SLO, with financial consequences.

Good SLIs measure what users experience, not what infrastructure reports. CPU utilization is not an SLI.

---

## Golden signals, RED, and USE

**The four golden signals** (Google SRE): latency, traffic, errors, saturation.

**RED** for request-driven services: Rate, Errors, Duration.

**USE** for resources: Utilization, Saturation, Errors.

They overlap deliberately. RED describes the service from the caller's side; USE describes the resources underneath. A complete dashboard usually has both.

---

## Alerting

Alert on symptoms that users feel, not on causes. An alert on "CPU above 80%" fires during healthy load; an alert on SLO burn rate fires when users are actually affected.

**Burn-rate alerting** compares how fast the error budget is being consumed against how fast it would be consumed at exactly the SLO. Fast burn over a short window pages; slow burn over a long window raises a ticket. This is the pattern that reduces alert fatigue without missing real degradation.

---

## Key terms

- **Observability** - the property of being able to answer new questions about a system from existing telemetry without shipping code
- **Exemplar** - a trace ID attached to a metric data point, linking an aggregate to an example request
- **Cardinality** - the number of unique attribute value combinations, and therefore of time series, in a metric
- **Semantic convention** - the OpenTelemetry specification standardizing attribute and metric names
- **SLI** - a service level indicator, a measured signal of user-visible behavior
- **SLO** - a service level objective, the target value for an SLI over a time window
- **Error budget** - the permitted shortfall against an SLO, used to balance reliability against change velocity
- **SLA** - a contractual service level agreement, typically looser than the internal SLO
- **Golden signals** - latency, traffic, errors, and saturation, the four core service health measures
- **RED method** - Rate, Errors, and Duration, the request-driven service monitoring pattern
- **USE method** - Utilization, Saturation, and Errors, the resource monitoring pattern
- **Burn-rate alerting** - alerting on the speed at which an error budget is consumed rather than on raw thresholds

---

## Related

- [Notes 04: maintaining and debugging](./04-maintaining-and-debugging.md)
- [Observability basics](../../../../learn/concepts/observability-basics.md)
- [Observability topic](../../../../topics/observability.md)
