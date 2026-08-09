---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 9 min
---

# 03 - Argo Rollouts

**Domain 3: Argo Rollouts (18%)**

Progressive delivery: release gradually, measure, and roll back automatically.

---

## The Rollout resource

A `Rollout` **replaces** a Deployment. It has a nearly identical spec (selector, template, replicas) plus a `strategy` block, and it manages ReplicaSets itself.

Migration from a Deployment is either converting the manifest, or referencing the existing Deployment through `workloadRef` so the Rollout adopts it.

---

## Canary strategy

Shift traffic gradually through a list of steps.

```yaml
strategy:
  canary:
    canaryService: api-canary
    stableService: api-stable
    trafficRouting:
      nginx:
        stableIngress: api-ingress
    steps:
      - setWeight: 10
      - pause: {duration: 10m}
      - setWeight: 50
      - pause: {duration: 10m}
      - setWeight: 100
```

Step types:
- **`setWeight`** - percentage of traffic to the canary
- **`pause`** - with a `duration`, or indefinite until manually promoted
- **`analysis`** - run an AnalysisTemplate at this point
- **`setCanaryScale`** - control canary replica count independently of traffic weight
- **`experiment`** - run a side-by-side comparison

**Without a traffic provider**, weight is approximated by replica counts, which is coarse. **With one** (Istio, NGINX, ALB, SMI, Gateway API, Traefik, Apache APISIX), the weight applies to actual request routing.

---

## Blue-green strategy

```yaml
strategy:
  blueGreen:
    activeService: api-active
    previewService: api-preview
    autoPromotionEnabled: false
    scaleDownDelaySeconds: 300
    prePromotionAnalysis:
      templates:
        - templateName: smoke-tests
```

The new version runs in full behind the **preview service** while the **active service** still points at the old one. Promotion flips the active service selector, which is an instant cutover rather than a graduated shift.

- `autoPromotionEnabled: false` requires manual promotion
- `scaleDownDelaySeconds` keeps the old ReplicaSet available for fast rollback
- `prePromotionAnalysis` and `postPromotionAnalysis` gate and verify the switch

**Canary versus blue-green**: canary shifts traffic gradually and needs less capacity; blue-green runs two full environments and switches instantly, which suits changes that cannot serve mixed versions, such as an incompatible schema migration.

---

## Analysis

The mechanism that makes rollouts automatic rather than timed.

- **AnalysisTemplate** (namespaced) and **ClusterAnalysisTemplate** define metrics with `successCondition` or `failureCondition`, an interval, and a count
- **AnalysisRun** is the execution during a rollout
- Metric providers: **Prometheus**, Datadog, New Relic, CloudWatch, Wavefront, Graphite, InfluxDB, **Job** (run a Kubernetes Job and use its exit code), and **Web** (call an HTTP endpoint)

```yaml
metrics:
  - name: error-rate
    interval: 1m
    count: 10
    failureLimit: 2
    failureCondition: result[0] > 0.01
    provider:
      prometheus:
        address: http://prometheus:9090
        query: |
          sum(rate(http_requests_total{status=~"5..",service="api-canary"}[2m]))
          / sum(rate(http_requests_total{service="api-canary"}[2m]))
```

Analysis can run as a **step** (blocking at that point), as **background analysis** (running throughout the rollout), or as pre/post-promotion analysis in blue-green.

A failing AnalysisRun **aborts** the rollout: traffic returns to the stable ReplicaSet automatically.

---

## Experiments

An `Experiment` runs one or more ReplicaSets side by side for a fixed duration with analysis attached, without changing production traffic routing. Used for A/B comparison and for validating a candidate before committing to a rollout.

---

## Operating them

- `kubectl argo rollouts get rollout <name> --watch` shows live progress
- `kubectl argo rollouts promote`, `abort`, `retry`, and `undo` control a rollout manually
- The **Rollouts dashboard** provides the same visually
- Rollouts are usually themselves managed by Argo CD, so the desired state stays in the repository; Argo CD needs a custom health check to understand Rollout status, which it ships by default

---

## Key terms

- **Rollout** - the Argo Rollouts custom resource replacing a Deployment and managing progressive release
- **workloadRef** - the Rollout field adopting an existing Deployment's pod template rather than duplicating it
- **Canary strategy** - gradual traffic shift to a new version through a series of weighted steps
- **Blue-green strategy** - running a full new version behind a preview service, then switching the active service in one cutover
- **setWeight** - the canary step defining the percentage of traffic sent to the new version
- **Traffic routing provider** - the integration (Istio, NGINX, ALB, SMI, Gateway API) applying weights to real traffic
- **setCanaryScale** - the step controlling canary replica count independently of traffic weight
- **Active service** - the blue-green service receiving production traffic
- **Preview service** - the blue-green service pointing at the new version before promotion
- **autoPromotionEnabled** - the blue-green setting determining whether promotion happens automatically
- **scaleDownDelaySeconds** - the delay before the old ReplicaSet is removed, enabling fast rollback
- **AnalysisTemplate** - a reusable definition of metrics and success or failure conditions for a rollout
- **AnalysisRun** - an execution of an AnalysisTemplate during a rollout
- **failureCondition** - the expression that, when true, fails a metric and aborts the rollout
- **Background analysis** - analysis running continuously throughout a rollout rather than at one step
- **Experiment** - a time-boxed side-by-side run of multiple versions with analysis, outside the production traffic path

---

## Related

- [Notes 04: Argo Events](./04-argo-events.md)
- [Scenarios](../scenarios.md) - scenario 6
- [OTCA](../../otca/) - the metrics analysis depends on
