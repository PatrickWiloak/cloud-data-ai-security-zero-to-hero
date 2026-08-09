---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 10 min
---

# Certified Argo Project Associate (CAPA) Fact Sheet

## Exam Overview

**Exam Code:** CAPA
**Exam Name:** Certified Argo Project Associate
**Level:** Associate
**Duration:** 90 minutes
**Format:** Multiple choice and multiple select, online proctored
**Questions:** 60
**Passing Score:** 75%
**Cost:** USD 250 (includes one free retake)
**Valid For:** 2 years
**Delivery:** Online proctored through PSI
**Prerequisites:** None; Kubernetes fundamentals assumed

> **Verify before booking.** Confirm current details on the official pages below.

**[📖 CAPA certification page](https://www.cncf.io/training/certification/capa/)** - registration and curriculum
**[📖 Linux Foundation CAPA page](https://training.linuxfoundation.org/certification/certified-argo-project-associate-capa/)** - logistics
**[📖 Argo Project documentation](https://argoproj.github.io/)** - the four projects
**[📖 CNCF curriculum repository](https://github.com/cncf/curriculum)** - published exam domains

## Four projects, one exam

The Argo Project is four separate tools that share a name and a community. CAPA covers all four, and the weighting surprises people who assume it is an Argo CD exam:

| Project | Weight | What it does |
|---|---|---|
| **Argo Workflows** | 36% | Container-native workflow engine: DAGs and step sequences run as pods |
| **Argo CD** | 34% | GitOps continuous delivery: reconciles cluster state against a repository |
| **Argo Rollouts** | 18% | Progressive delivery: canary and blue-green with automated analysis |
| **Argo Events** | 12% | Event-driven automation: event sources, sensors, and triggers |

**Workflows is the largest domain**, at slightly more than Argo CD. Candidates who study only Argo CD are studying a third of the exam.

## Target Audience

- Platform engineers running any part of the Argo stack
- SREs and DevOps engineers implementing GitOps or progressive delivery
- Data and ML engineers using Argo Workflows for pipelines
- Anyone holding [CKA](../cka/) or [KCNA](../kcna/) extending into delivery tooling

Assumed background: Kubernetes objects, custom resources, and controllers. CAPA does not teach Kubernetes.

## Exam Domains

### Domain 1: Argo Workflows (36%)

**Key Concepts:**
- The `Workflow` custom resource and the workflow controller
- Templates: container, script, resource, suspend, and the DAG and steps orchestration templates
- Template invocation, `templateRef`, and `WorkflowTemplate` versus `ClusterWorkflowTemplate`
- Parameters and artifacts: inputs, outputs, and passing values between steps
- Artifact repositories (S3, GCS, Azure Blob, MinIO) and artifact garbage collection
- Volumes, `volumeClaimTemplates`, and sharing data between steps
- Conditionals (`when`), loops (`withItems`, `withParam`, `withSequence`), and recursion
- Retry strategy, timeouts, and `activeDeadlineSeconds`
- Exit handlers and lifecycle hooks
- `CronWorkflow` for scheduled execution
- Workflow archive, pod garbage collection, and TTL strategy
- Synchronization: mutexes and semaphores for concurrency limits
- Security: service accounts, `podSpecPatch`, and the workflow executor
- The Argo Workflows UI, CLI, and Events integration

**[📖 Argo Workflows documentation](https://argo-workflows.readthedocs.io/)** - templates, artifacts, and orchestration

### Domain 2: Argo CD (34%)

**Key Concepts:**
- Architecture: API server, repository server, application controller, Redis, and Dex or an external OIDC provider
- The `Application` custom resource: source, destination, project, and sync policy
- `ApplicationSet` and its generators: list, cluster, Git, matrix, merge, pull request, SCM provider
- `AppProject` for multi-tenancy: allowed sources, destinations, and resource kinds
- Sync policies: manual versus automated, prune, self-heal
- Sync options, waves, hooks (PreSync, Sync, PostSync, SyncFail), and resource ordering
- Health assessment and custom health checks
- Diffing, `ignoreDifferences`, and managing fields owned by other controllers
- Tools support: Kustomize, Helm, jsonnet, and config management plugins
- Multi-cluster management and cluster registration
- RBAC, projects, and SSO integration
- Notifications and the Argo CD Image Updater
- Declarative setup: managing Argo CD itself with Argo CD (app of apps)

**[📖 Argo CD documentation](https://argo-cd.readthedocs.io/)** - applications, projects, sync

### Domain 3: Argo Rollouts (18%)

**Key Concepts:**
- The `Rollout` custom resource as a Deployment replacement
- Canary strategy: steps, `setWeight`, `pause`, and traffic routing
- Blue-green strategy: active and preview services, `autoPromotionEnabled`, scale-down delay
- Traffic management integrations: Istio, NGINX, ALB, SMI, Gateway API
- `AnalysisTemplate`, `ClusterAnalysisTemplate`, and `AnalysisRun`
- Metric providers: Prometheus, Datadog, New Relic, CloudWatch, Wavefront, Job, Web
- Automated promotion and automatic rollback on failed analysis
- Experiments for comparing versions side by side
- The Rollouts dashboard and `kubectl argo rollouts` plugin

**[📖 Argo Rollouts documentation](https://argo-rollouts.readthedocs.io/)** - strategies and analysis

### Domain 4: Argo Events (12%)

**Key Concepts:**
- Architecture: `EventSource`, `Sensor`, `EventBus`
- Event sources: webhook, S3, calendar, Kafka, SQS, GitHub, GitLab, Redis, resource
- Sensors: dependencies, filters, and triggers
- Triggers: Argo Workflow, Kubernetes object, HTTP, AWS Lambda, Kafka, Slack
- Trigger parameterization from event payloads
- Event filtering by data, context, time, and expression
- The EventBus implementations (NATS, Jetstream, Kafka)

**[📖 Argo Events documentation](https://argoproj.github.io/argo-events/)** - event sources, sensors, triggers

## Which tool for which job

| Requirement | Tool |
|---|---|
| Run a multi-step batch or ML pipeline in containers | Argo Workflows |
| Keep clusters matching a Git repository | Argo CD |
| Release a new version to 10% of traffic and roll back on errors | Argo Rollouts |
| Trigger something when a file lands in S3 or a webhook fires | Argo Events |
| Run a workflow on a schedule | CronWorkflow (Argo Workflows) |
| Generate one Application per cluster from a template | ApplicationSet (Argo CD) |

## Related repo material

- [Notes](./notes/) - four notes, one per project
- [Practice plan](./practice-plan.md) - 5-week schedule
- [Scenarios](./scenarios.md)
- [Strategy](./strategy.md)
- [CGOA](../cgoa/) - the vendor-neutral GitOps concepts underneath Argo CD
- [CKA](../cka/) - the Kubernetes knowledge this assumes
- [Build a CI/CD pipeline](../../../resources/hands-on-projects/build-ci-cd-pipeline.md)
