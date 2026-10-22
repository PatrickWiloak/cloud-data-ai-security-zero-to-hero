---
last-updated: 2026-10-22
applies-to: KCNA curriculum revised November 2025, checked 2026-10-22
difficulty: beginner
---

# KCNA Study Plan

## 4-Week Knowledge-Based Study Schedule

This plan follows the four-domain outline for exams from 24 November 2025. Time is weighted to the domains: Kubernetes Fundamentals (44%) gets the first week and a half, Container Orchestration (28%) the next week and a half, and Application Delivery (16%) and Cloud Native Architecture (12%) share week 3.

### Week 1: Kubernetes Fundamentals (44%)

#### Day 1-2: Core Concepts - Architecture and the API
- [ ] Study control plane components (API server, etcd, scheduler, controller manager, cloud controller manager)
- [ ] Study node components (kubelet, kube-proxy, container runtime)
- [ ] Trace a `kubectl apply` of a Deployment through every component
- [ ] Learn desired state, controllers, reconciliation, CRDs and operators
- [ ] Draw the architecture diagram from memory
- [ ] Review Notes: `notes/01-kubernetes-fundamentals.md` (Kubernetes Core Concepts)

#### Day 3-4: Core Concepts - Workloads and Configuration
- [ ] Study Pods, multi-container patterns and init containers
- [ ] Compare Deployments, ReplicaSets, StatefulSets, DaemonSets, Jobs and CronJobs
- [ ] Learn namespaces, labels, selectors and annotations
- [ ] Learn ConfigMaps and Secrets and how they reach a container

#### Day 5: Administration
- [ ] Learn kubeconfig clusters, users and contexts
- [ ] Compare imperative commands with declarative `kubectl apply`
- [ ] Learn ResourceQuota and LimitRange and how they interact
- [ ] Learn kubeadm, managed versus self-managed, upgrade order and version skew
- [ ] Review Notes: `notes/01-kubernetes-fundamentals.md` (Administration)

#### Day 6: Scheduling
- [ ] Learn filtering and scoring
- [ ] Learn requests versus limits, throttling versus OOMKilled, and the three QoS classes
- [ ] Learn nodeSelector, node affinity, pod affinity and anti-affinity
- [ ] Learn taints, tolerations and their three effects
- [ ] Learn PriorityClass and preemption, and DaemonSet placement
- [ ] Review Notes: `notes/01-kubernetes-fundamentals.md` (Scheduling)

#### Day 7: Containerization and Week 1 Review
- [ ] Study containers versus VMs (namespaces, cgroups, shared kernel)
- [ ] Learn images, layers, registries, tags versus digests
- [ ] Learn the three OCI specs, CRI, containerd, CRI-O and the dockershim removal
- [ ] Learn Dockerfile basics and multi-stage builds
- [ ] Take a short practice quiz on Domain 1 and note weak areas

### Week 2: Container Orchestration (28%) and Fundamentals Wrap-up

#### Day 8: Domain 1 Gaps
- [ ] Re-read the weak sections from the Day 7 quiz
- [ ] Answer the "Check yourself" questions at the end of note 01

#### Day 9-10: Networking
- [ ] Learn the Kubernetes network model and CNI
- [ ] Learn every Service type, including headless, and how kube-proxy and EndpointSlices route traffic
- [ ] Learn CoreDNS name formats
- [ ] Compare Ingress with the Gateway API
- [ ] Learn NetworkPolicy isolation rules and the CNI dependency
- [ ] Learn service mesh concepts (data plane, control plane, mTLS)
- [ ] Review Notes: `notes/02-container-orchestration.md` (Networking)

#### Day 11: Security
- [ ] Learn the 4Cs and defence in depth
- [ ] Learn authentication, authorization and admission in order
- [ ] Learn Role, ClusterRole, RoleBinding, ClusterRoleBinding and ServiceAccounts
- [ ] Learn Pod Security Standards, Pod Security Admission modes and securityContext
- [ ] Learn why Secrets are not encrypted by default and how to fix it
- [ ] Learn image scanning, signing, SBOMs, OPA Gatekeeper and Kyverno
- [ ] Review Notes: `notes/02-container-orchestration.md` (Security)

#### Day 12: Troubleshooting
- [ ] Learn the five Pod phases and the difference from container reasons
- [ ] Learn the symptom table: Pending, ImagePullBackOff, CrashLoopBackOff, OOMKilled
- [ ] Learn liveness, readiness and startup probes and their failure actions
- [ ] Learn the Service-with-no-endpoints and NotReady node scenarios
- [ ] Review Notes: `notes/02-container-orchestration.md` (Troubleshooting)

#### Day 13: Storage
- [ ] Learn volumes, emptyDir and ephemeral volumes
- [ ] Learn PV, PVC and StorageClass, static versus dynamic provisioning
- [ ] Learn the four access modes and the reclaim policies
- [ ] Learn CSI and StatefulSet volumeClaimTemplates
- [ ] Review Notes: `notes/02-container-orchestration.md` (Storage)

#### Day 14: Week 2 Review
- [ ] Take a practice quiz covering Domain 2
- [ ] Work through the troubleshooting and security scenarios in `scenarios.md`

### Week 3: Application Delivery (16%) and Cloud Native Architecture (12%)

#### Day 15-16: Application Delivery
- [ ] Separate CI, continuous delivery and continuous deployment
- [ ] Learn the four OpenGitOps principles word for word
- [ ] Learn Argo CD (Application, sync status, health status) and Flux (sources, Kustomization, HelmRelease)
- [ ] Learn Helm charts, values, releases, revisions and repositories
- [ ] Learn Kustomize bases and overlays
- [ ] Compare rolling update, recreate, blue-green and canary; learn progressive delivery
- [ ] Learn how HPA, VPA and node autoscalers interact with delivery
- [ ] Review Notes: `notes/03-application-delivery.md` (Application Delivery)

#### Day 17: Debugging
- [ ] Learn rollout status, history and undo, and ProgressDeadlineExceeded
- [ ] Learn `kubectl debug`, ephemeral containers, port-forward and `logs --previous`
- [ ] Learn Helm release states and how to inspect history
- [ ] Learn GitOps OutOfSync versus Degraded and common causes of drift
- [ ] Review Notes: `notes/03-application-delivery.md` (Debugging)

#### Day 18-19: Observability
- [ ] Learn metrics, logs and traces and how they work together
- [ ] Learn Prometheus pull model, exporters, metric types, PromQL shape, Alertmanager, Grafana
- [ ] Learn metrics-server versus kube-state-metrics
- [ ] Learn Fluentd and Fluent Bit, OpenTelemetry and Jaeger
- [ ] Learn SLI, SLO, error budget and OpenCost
- [ ] Review Notes: `notes/04-cloud-native-architecture.md` (Observability)

#### Day 20: Ecosystem, Principles and Community
- [ ] Learn the CNCF cloud native definition and twelve-factor mapping
- [ ] Learn microservices trade-offs, immutable infrastructure, declarative APIs, serverless and Knative
- [ ] Learn the three CNCF maturity levels with examples
- [ ] Learn CNCF governance (Governing Board, TOC, TAGs) and Kubernetes governance (SIGs, WGs, Steering, KEPs)
- [ ] Learn the release cadence and how to contribute
- [ ] Review Notes: `notes/04-cloud-native-architecture.md` (Ecosystem and Community)

#### Day 21: Week 3 Review
- [ ] Take a practice quiz on Domains 3 and 4
- [ ] Map CNCF projects to categories using the CNCF Landscape
- [ ] Review the GitOps and observability scenarios in `scenarios.md`

### Week 4: Review and Exam Prep

#### Day 22-23: Weighted Review
- [ ] Re-read note 01 and note 02 (72% of the exam together)
- [ ] Answer every "Check yourself" question in all four notes
- [ ] Drill `flashcards.csv` for terms you still miss

#### Day 24-25: Practice Exams
- [ ] Take a full timed practice exam (90 minutes)
- [ ] Review every wrong answer and the reason
- [ ] Do targeted review of weak competencies
- [ ] Use `../../../resources/practice-questions/cncf-kcna.md`

#### Day 26-27: Second Practice Exam and Gaps
- [ ] Take a second timed practice exam
- [ ] Compare scores by domain and fix the weakest one

#### Day 28: Pre-Exam Preparation
- [ ] Light review of the fact sheet quick reference tables
- [ ] Check your exam date is on or after 24 November 2025 for this outline
- [ ] Run the exam system check (webcam, microphone, browser)
- [ ] Rest

## Daily Study Routine (1-2 hours/day)

1. **30-45 minutes**: Read the day's note section
2. **15-30 minutes**: Read the linked Kubernetes or CNCF doc page
3. **30 minutes**: Practice questions and self-check

### Weekend Extended Sessions (3-4 hours)
1. **1 hour**: Deep dive into a hard topic
2. **1 hour**: Practice exam and review
3. **1-2 hours**: Optional hands-on with a local cluster (kind or minikube) to see the concepts work

## Study Resources

- **[KCNA Exam Page](https://training.linuxfoundation.org/certification/kubernetes-cloud-native-associate/)** - Registration and current domains
- **[KCNA Program Changes](https://training.linuxfoundation.org/kcna-program-changes/)** - The November 2025 revision
- **[Kubernetes Docs](https://kubernetes.io/docs/concepts/)** - Concepts section
- **[CNCF Landscape](https://landscape.cncf.io/)** - Ecosystem map
- **[CNCF Glossary](https://glossary.cncf.io/)** - Terminology

---

## Final Exam Checklist

### One Week Before
- [ ] Scoring 80% or more on timed practice exams
- [ ] All four domains reviewed, weakest competency addressed
- [ ] CNCF terms and project categories memorised

### Day Before Exam
- [ ] Light review only
- [ ] Test the exam environment
- [ ] Clear your workspace per the proctoring rules
- [ ] Sleep well

### Exam Day
- [ ] Log in early for the check-in
- [ ] Read each question fully before answering
- [ ] Eliminate wrong answers first
- [ ] Flag uncertain questions and return
- [ ] Use the full 90 minutes
