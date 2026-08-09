---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 4 min
---

# CAPA Study Plan

Five weeks at 5-7 hours per week. Weight the first two weeks toward Argo Workflows, which is the largest and least familiar domain.

## Week 1: Argo Workflows fundamentals

- [ ] Install Argo Workflows on kind and run the hello-world example
- [ ] The Workflow custom resource and the controller's role
- [ ] Template types: container, script, resource, suspend
- [ ] Orchestration templates: steps versus DAG, and when each fits
- [ ] Entrypoint, templateRef, WorkflowTemplate, ClusterWorkflowTemplate
- [ ] Input and output parameters, and passing values between steps
- [ ] **Lab**: build a DAG with four tasks and a parameter flowing through
- [ ] Review Notes: `notes/01-argo-workflows.md`

## Week 2: Argo Workflows advanced

- [ ] Artifacts: repositories, input and output artifacts, artifact garbage collection
- [ ] Volumes and volumeClaimTemplates for sharing data
- [ ] Conditionals with `when`, loops with withItems, withParam, withSequence
- [ ] Retry strategy, timeouts, activeDeadlineSeconds
- [ ] Exit handlers and lifecycle hooks
- [ ] CronWorkflow, and the concurrency policy options
- [ ] Pod garbage collection, TTL strategy, and the workflow archive
- [ ] Synchronization with mutexes and semaphores
- [ ] Service accounts and workflow security
- [ ] **Lab**: a CronWorkflow with an artifact, a retry strategy, an exit handler, and a TTL

## Week 3: Argo CD

- [ ] Architecture: API server, repo server, application controller, Redis
- [ ] The Application resource: source, destination, project, syncPolicy
- [ ] Sync policy: manual versus automated, prune, self-heal
- [ ] Sync waves, hooks (PreSync, Sync, PostSync, SyncFail), and ordering
- [ ] Health status and custom health checks
- [ ] ignoreDifferences and fields owned by other controllers
- [ ] AppProject for multi-tenancy: allowed sources, destinations, kinds
- [ ] ApplicationSet generators: list, cluster, Git, matrix, merge, pull request
- [ ] Kustomize, Helm, and plugin support
- [ ] App of apps and declarative Argo CD management
- [ ] **Lab**: an Application with automated sync and self-heal, then an ApplicationSet with a list generator
- [ ] Review Notes: `notes/02-argo-cd.md`

## Week 4: Argo Rollouts and Argo Events

- [ ] Rollout as a Deployment replacement, and how it manages ReplicaSets
- [ ] Canary strategy: steps, setWeight, pause, and traffic routing
- [ ] Blue-green: active and preview services, autoPromotionEnabled, scaleDownDelay
- [ ] Traffic providers: Istio, NGINX, ALB, SMI, Gateway API
- [ ] AnalysisTemplate, AnalysisRun, and metric providers
- [ ] Automatic promotion and rollback behavior
- [ ] Experiments
- [ ] Argo Events: EventSource, Sensor, EventBus
- [ ] Event sources, filters, triggers, and payload parameterization
- [ ] **Lab**: a canary Rollout with a Prometheus analysis that fails, and a webhook Sensor triggering a Workflow
- [ ] Review Notes: `notes/03-argo-rollouts.md` and `notes/04-argo-events.md`

## Week 5: Integration and review

- [ ] Trace an end-to-end path: event, workflow, commit, sync, rollout
- [ ] Know which project owns which responsibility, and where boundaries lie
- [ ] Work every scenario in [scenarios.md](./scenarios.md)
- [ ] Two timed practice exams
- [ ] Re-read the Workflows documentation on templates and artifacts

## Readiness check

- [ ] Explain the difference between steps and DAG templates and when each is right
- [ ] Describe how a parameter and an artifact each pass between workflow steps
- [ ] Explain what prune and self-heal do in an Argo CD sync policy
- [ ] Describe when to use an ApplicationSet rather than several Applications
- [ ] Explain sync waves and give a case that needs them
- [ ] Describe a canary rollout with analysis and what happens when analysis fails
- [ ] Explain the roles of EventSource, Sensor, and EventBus
