---
last-updated: 2026-10-22
applies-to: KCNA curriculum revised November 2025, checked 2026-10-22
difficulty: beginner
---

# Kubernetes and Cloud Native Associate (KCNA) Fact Sheet

> **Outline updated 2026-10-22.** This sheet follows the revised outline for exams taken on or after 24 November 2025: four domains, with observability folded into Cloud Native Architecture.

## Exam Overview

**Exam Code:** KCNA
**Exam Name:** Kubernetes and Cloud Native Associate
**Duration:** 90 minutes
**Format:** Multiple choice, about 60 questions (commonly reported)
**Passing Score:** 75% (commonly reported; not stated on the exam page)
**Cost:** $250 USD exam only, one retake included
**Valid For:** 2 years
**Delivery:** Online proctored
**Prerequisites:** None

Bundles listed on the exam page: $299 with the LFS250 course, and $495 for THRIVE-ONE. You have 12 months from purchase to take the exam. The Linux Foundation's rule for which outline applies: the only date that matters is the date you sit for the exam.

**[📖 Official KCNA Exam Page](https://training.linuxfoundation.org/certification/kubernetes-cloud-native-associate/)** - Registration, domains, pricing and policies
**[📖 KCNA Program Changes](https://training.linuxfoundation.org/kcna-program-changes/)** - The November 2025 revision explained
**[📖 KCNA Exam Curriculum](https://github.com/cncf/curriculum)** - Official curriculum PDFs
**[📖 Linux Foundation Certification FAQ](https://docs.linuxfoundation.org/tc-docs/certification/faq-cka-ckad-cks)** - Scheduling, retakes and exam rules

## Target Audience

- Beginners entering the cloud native ecosystem
- Developers who want to understand Kubernetes concepts
- Operations staff moving to cloud native tooling
- Managers and pre-sales staff who need the vocabulary
- Anyone preparing for the hands-on CKA, CKAD or CKS exams

**[📖 Cloud Native Glossary](https://glossary.cncf.io/)** - CNCF terminology reference
**[📖 CNCF Landscape](https://landscape.cncf.io/)** - Visual map of cloud native technologies

## Exam Domains

| # | Domain | Weight | Competencies | Notes |
|---|--------|--------|--------------|-------|
| 1 | Kubernetes Fundamentals | 44% | Core Concepts, Administration, Scheduling, Containerization | [01](./notes/01-kubernetes-fundamentals.md) |
| 2 | Container Orchestration | 28% | Networking, Security, Troubleshooting, Storage | [02](./notes/02-container-orchestration.md) |
| 3 | Cloud Native Application Delivery | 16% | Application Delivery, Debugging | [03](./notes/03-application-delivery.md) |
| 4 | Cloud Native Architecture | 12% | Observability, Ecosystem and Principles, Community and Collaboration | [04](./notes/04-cloud-native-architecture.md) |

### Domain 1: Kubernetes Fundamentals (44%)

**Kubernetes Core Concepts:** control plane and node components, the API and declarative objects, controllers and reconciliation, Pods, Deployments, ReplicaSets, StatefulSets, DaemonSets, Jobs, CronJobs, namespaces, labels, selectors, annotations, ConfigMaps and Secrets.

**Administration:** kubectl and kubeconfig contexts, imperative versus declarative `apply`, ResourceQuotas and LimitRanges, kubeadm, managed versus self-managed clusters, upgrades and version skew.

**Scheduling:** filtering and scoring, requests and limits, QoS classes, nodeSelector, affinity and anti-affinity, taints and tolerations, priority and preemption.

**Containerization:** containers versus VMs, images and layers, registries, tags versus digests, OCI specs, CRI, containerd and CRI-O, dockershim removal, Dockerfiles and multi-stage builds.

**[📖 Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)** - Cluster architecture overview
**[📖 Workload Resources](https://kubernetes.io/docs/concepts/workloads/controllers/)** - Deployments, StatefulSets, DaemonSets, Jobs
**[📖 Scheduling, Preemption and Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/)** - How Pods are placed
**[📖 Version Skew Policy](https://kubernetes.io/releases/version-skew-policy/)** - Supported component version differences
**[📖 Container Runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)** - CRI runtimes

### Domain 2: Container Orchestration (28%)

**Networking:** the flat Pod network, CNI, Service types, kube-proxy, CoreDNS names, Ingress, Gateway API, NetworkPolicy, service mesh concepts.

**Security:** the 4Cs, authentication, authorization and admission, RBAC, ServiceAccounts, Pod Security Standards and Pod Security Admission, securityContext, Secrets and encryption at rest, image scanning and signing, policy engines (OPA Gatekeeper, Kyverno).

**Troubleshooting:** Pod phases, Pending, CrashLoopBackOff, ImagePullBackOff, OOMKilled, probes, Services with no endpoints, NotReady nodes, `get`, `describe`, `logs`, `events`, `exec`.

**Storage:** volumes and emptyDir, PV, PVC, StorageClass, dynamic provisioning, access modes, reclaim policies, CSI, StatefulSet volumeClaimTemplates.

**[📖 Services, Load Balancing, and Networking](https://kubernetes.io/docs/concepts/services-networking/)** - Networking concepts
**[📖 Security](https://kubernetes.io/docs/concepts/security/)** - Security concepts
**[📖 Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)** - Roles and bindings
**[📖 Troubleshooting Applications](https://kubernetes.io/docs/tasks/debug/debug-application/)** - Debugging Pods and Services
**[📖 Storage](https://kubernetes.io/docs/concepts/storage/)** - Storage concepts

### Domain 3: Cloud Native Application Delivery (16%)

**Application Delivery:** CI, continuous delivery and continuous deployment, the four OpenGitOps principles, Argo CD and Flux, Helm charts, values, releases and repositories, Kustomize bases and overlays, rolling, recreate, blue-green and canary rollouts, progressive delivery (Argo Rollouts, Flagger), autoscaling as it affects delivery.

**Debugging:** rollout status and history, `kubectl rollout undo`, ProgressDeadlineExceeded, `kubectl debug` and ephemeral containers, port-forward, previous container logs, failed Helm releases, GitOps drift and OutOfSync.

**[📖 OpenGitOps](https://opengitops.dev/)** - GitOps principles
**[📖 Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)** - Rollouts and rollback
**[📖 Helm](https://helm.sh/docs/)** - Kubernetes package manager
**[📖 Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/)** - Manifest customisation
**[📖 Debug Running Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/)** - kubectl debug and ephemeral containers

### Domain 4: Cloud Native Architecture (12%)

**Observability:** metrics, logs and traces, Prometheus pull model, exporters, PromQL, Alertmanager, Grafana, OpenTelemetry, Jaeger, Fluentd and Fluent Bit, metrics-server versus kube-state-metrics, SLIs and SLOs, OpenCost.

**Cloud Native Ecosystem and Principles:** the CNCF definition, twelve-factor apps, microservices, immutable infrastructure, declarative APIs, autoscaling, serverless and Knative, service mesh, CNCF maturity levels.

**Cloud Native Community and Collaboration:** CNCF and the Linux Foundation, the TOC, TAGs, Kubernetes SIGs and working groups, KEPs, release cadence, open governance, contributing, KubeCon + CloudNativeCon, Code of Conduct.

**[📖 CNCF Cloud Native Definition](https://github.com/cncf/toc/blob/main/DEFINITION.md)** - Official definition
**[📖 Prometheus Overview](https://prometheus.io/docs/introduction/overview/)** - Metrics and alerting
**[📖 OpenTelemetry](https://opentelemetry.io/docs/)** - Telemetry standard
**[📖 CNCF Projects](https://www.cncf.io/projects/)** - Projects by maturity level
**[📖 Kubernetes community](https://github.com/kubernetes/community)** - SIGs, working groups and governance

## Quick Reference

### Control Plane Components
| Component | Purpose |
|-----------|---------|
| kube-apiserver | Front end for the Kubernetes API; the only component that talks to etcd |
| etcd | Consistent key-value store for all cluster state |
| kube-scheduler | Assigns Pods to nodes (filter, then score) |
| kube-controller-manager | Runs controller loops (Deployment, ReplicaSet, Node and more) |
| cloud-controller-manager | Cloud provider integrations such as load balancers |

### Worker Node Components
| Component | Purpose |
|-----------|---------|
| kubelet | Runs the Pods bound to its node and reports status |
| kube-proxy | Programs rules that route Service traffic to Pods |
| Container runtime | Runs containers through CRI (containerd, CRI-O) |

### Service Types
| Type | Description |
|------|-------------|
| ClusterIP | Internal-only virtual IP (default) |
| NodePort | A port on every node's IP |
| LoadBalancer | External cloud load balancer |
| ExternalName | DNS CNAME to an external name |
| Headless (`clusterIP: None`) | DNS returns Pod IPs directly |

### Pod Symptoms
| Symptom | Usual cause |
|---------|-------------|
| Pending | Not enough requested resources, taints, affinity, unbound PVC |
| ImagePullBackOff | Wrong image name or tag, missing registry credentials |
| CrashLoopBackOff | App exits at start, bad config, failing liveness probe |
| OOMKilled | Memory limit exceeded |
| Running, READY 0/1 | Readiness probe failing |

### OpenGitOps Principles
| Principle | Meaning |
|-----------|---------|
| Declarative | Desired state is expressed declaratively |
| Versioned and immutable | Stored with full, unchangeable history |
| Pulled automatically | Agents pull desired state from the source |
| Continuously reconciled | Agents keep correcting drift |

## Exam Tips

1. **Read carefully** - Watch for "which is NOT" and "best"
2. **Eliminate first** - Two options are often clearly wrong
3. **Weight your study** - Domains 1 and 2 are 72% of the exam together
4. **Know the vocabulary** - Many questions test CNCF terms and project purposes
5. **Know who does what** - API server, scheduler, controllers and kubelet each have one job
6. **Flag and return** - Mark uncertain questions and come back

### Common Pitfalls
- Confusing control plane and worker node components
- Treating CrashLoopBackOff as a Pod phase
- Thinking Secrets are encrypted by default
- Confusing metrics-server with kube-state-metrics
- Confusing CNCF TAGs with Kubernetes SIGs
- Mixing up CNCF maturity levels

---

**Key Takeaway:** KCNA is conceptual. Understand why each piece exists, how the pieces interact, and where each CNCF project fits. Kubernetes Fundamentals (44%) and Container Orchestration (28%) deserve most of your time.
