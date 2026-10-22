---
last-updated: 2026-10-22
applies-to: KCNA curriculum revised November 2025, checked 2026-10-22
difficulty: beginner
---

# Kubernetes and Cloud Native Associate (KCNA)

> **Outline updated 2026-10-22.** The CNCF revised KCNA for exams from 24 November 2025: four domains, with observability folded into Cloud Native Architecture. Earlier versions of this folder taught the five-domain outline.

## Exam Overview

The Kubernetes and Cloud Native Associate (KCNA) is an entry-level certification from the Linux Foundation and the CNCF. It shows foundational knowledge of Kubernetes and the wider cloud native ecosystem. It suits anyone starting out: students, developers, operations staff, and managers who need to understand the landscape. It is also a common first step before the hands-on CKA, CKAD and CKS exams.

The Linux Foundation's own guidance is that the only date that matters is the date you sit the exam: if you test on or after 24 November 2025, study the four-domain outline below.

**Exam Details:**
- **Exam Code:** KCNA
- **Duration:** 90 minutes
- **Format:** Online, proctored, multiple choice. No hands-on tasks
- **Number of Questions:** About 60 (commonly reported; the exam page does not state it)
- **Passing Score:** 75% (commonly reported; the exam page does not state it)
- **Cost:** $250 USD for the exam alone, including one retake. Bundles: $299 with the LFS250 course, $495 THRIVE-ONE
- **Exam eligibility:** 12 months from purchase to schedule and sit the exam
- **Validity:** 2 years
- **Prerequisites:** None

**[📖 KCNA exam page](https://training.linuxfoundation.org/certification/kubernetes-cloud-native-associate/)** - Registration, domains and current pricing
**[📖 KCNA program changes](https://training.linuxfoundation.org/kcna-program-changes/)** - What changed for exams from 24 November 2025
**[📖 CNCF curriculum repository](https://github.com/cncf/curriculum)** - Published curriculum PDFs

**Important:** This is a knowledge exam. Unlike CKA and CKS there are no terminal tasks. Aim to understand concepts, terminology and how cloud native technologies relate to each other. Hands-on practice still helps, because it makes the concepts stick.

## Exam Domains

| # | Domain | Weight | Notes |
|---|--------|--------|-------|
| 1 | Kubernetes Fundamentals | 44% | [01-kubernetes-fundamentals.md](./notes/01-kubernetes-fundamentals.md) |
| 2 | Container Orchestration | 28% | [02-container-orchestration.md](./notes/02-container-orchestration.md) |
| 3 | Cloud Native Application Delivery | 16% | [03-application-delivery.md](./notes/03-application-delivery.md) |
| 4 | Cloud Native Architecture | 12% | [04-cloud-native-architecture.md](./notes/04-cloud-native-architecture.md) |

### What each domain covers

**Domain 1: Kubernetes Fundamentals (44%).** Four competencies: Kubernetes Core Concepts, Administration, Scheduling and Containerization. This is how a cluster is built (control plane and node components, the API, controllers and reconciliation), the workload objects (Pods, Deployments, StatefulSets, DaemonSets, Jobs), namespaces, labels and configuration, how an admin works with kubectl, quotas and upgrades, how the scheduler places Pods (requests, limits, affinity, taints), and how containers and images work underneath (OCI, CRI, containerd, the dockershim removal). It is close to half the exam.

**Domain 2: Container Orchestration (28%).** Four competencies: Networking, Security, Troubleshooting and Storage. Services and DNS, Ingress and the Gateway API, NetworkPolicy, RBAC and ServiceAccounts, Pod Security Standards, Secrets and supply chain security, reading Pod states such as Pending, CrashLoopBackOff and ImagePullBackOff, probes, and persistent storage with PVs, PVCs, StorageClasses and CSI. This domain gained weight in the revision and absorbed topics that used to sit under Fundamentals and Architecture.

**Domain 3: Cloud Native Application Delivery (16%).** Two competencies: Application Delivery and Debugging. CI versus continuous delivery and deployment, the four OpenGitOps principles, Argo CD and Flux, Helm and Kustomize, rollout strategies (rolling, recreate, blue-green, canary) and progressive delivery, plus debugging rollouts, Helm releases and GitOps drift. Its weight doubled in the revision.

**Domain 4: Cloud Native Architecture (12%).** Three competencies: Observability, Cloud Native Ecosystem and Principles, and Cloud Native Community and Collaboration. Metrics, logs and traces with Prometheus, OpenTelemetry, Jaeger and Fluent Bit, the CNCF definition, twelve-factor apps, microservices, serverless and service mesh, CNCF project maturity, and how the CNCF and the Kubernetes project are governed (TOC, TAGs, SIGs, KEPs, release cadence).

### What changed from the old outline

| Old (before 24 Nov 2025) | New (from 24 Nov 2025) |
|---|---|
| Kubernetes Fundamentals 46% | Kubernetes Fundamentals 44% |
| Container Orchestration 22% | Container Orchestration 28% |
| Cloud Native Architecture 16% | Cloud Native Application Delivery 16% |
| Cloud Native Observability 8% | Cloud Native Architecture 12% (now includes observability) |
| Cloud Native Application Delivery 8% | - |

The practical effect: security, troubleshooting and debugging get explicit weight, delivery gets twice the weight, and community and governance appear as a named competency.

## Study Materials

| Material | What it is |
|---|---|
| [fact-sheet.md](./fact-sheet.md) | Exam facts, the four domains with competencies and doc links, quick reference tables |
| [notes/](./notes/) | One in-depth teaching note per domain, in exam order |
| [scenarios.md](./scenarios.md) | Worked scenarios with common distractors |
| [flashcards.csv](./flashcards.csv) | Term and definition cards for Anki or Quizlet |
| [practice-plan.md](./practice-plan.md) | A four-week day-by-day plan weighted to the domains |
| [strategy.md](./strategy.md) | Study approach, priorities and exam tactics |
| [Practice questions](../../../resources/practice-questions/cncf-kcna.md) | Original practice questions for KCNA |

## CNCF Landscape Overview

The CNCF is a vendor-neutral foundation under the Linux Foundation that hosts cloud native open source projects. KCNA expects you to know what the main projects do and roughly how mature they are.

### CNCF Project Maturity Levels
- **Graduated** - Mature, widely adopted, audited (Kubernetes, Prometheus, Envoy, CoreDNS, containerd, CRI-O, etcd, Fluentd, Helm, Jaeger, Argo, Flux, Linkerd, Istio, Cilium, OPA, Falco, Harbor)
- **Incubating** - Growing production use (for example OpenTelemetry, Backstage, Thanos)
- **Sandbox** - Early-stage projects

Maturity changes over time. Check the [CNCF projects page](https://www.cncf.io/projects/) for borderline cases.

### Key projects by category

| Category | Projects |
|----------|----------|
| Orchestration | Kubernetes |
| Container runtime | containerd, CRI-O |
| Networking and DNS | Cilium, Calico (not CNCF-hosted), CoreDNS |
| Service mesh and proxy | Istio, Linkerd, Envoy |
| Metrics | Prometheus, Thanos (Grafana for dashboards, not CNCF) |
| Logging | Fluentd, Fluent Bit |
| Tracing and telemetry | OpenTelemetry, Jaeger |
| GitOps and delivery | Argo, Flux |
| Packaging | Helm |
| Policy and runtime security | Open Policy Agent, Kyverno, Falco |
| Registry | Harbor |
| Serverless and events | Knative, CloudEvents |
| Cost | OpenCost |

## Core Kubernetes Architecture

### Control Plane Components
- **kube-apiserver** - Front end of the control plane; every component talks through it
- **etcd** - Consistent key-value store holding all cluster state
- **kube-scheduler** - Assigns Pods to nodes; does not start them
- **kube-controller-manager** - Runs controller loops (Deployment, ReplicaSet, Node, Job and more)
- **cloud-controller-manager** - Integrates with a cloud provider's API

### Worker Node Components
- **kubelet** - Node agent that runs the Pods bound to its node, via the container runtime
- **kube-proxy** - Programs node rules that route Service traffic to Pods
- **Container runtime** - Runs containers through CRI (containerd, CRI-O)

### Common Add-ons
- **CoreDNS** - Cluster DNS for service discovery
- **CNI plugin** - Pod networking and often NetworkPolicy (Calico, Cilium, Flannel)
- **metrics-server** - CPU and memory metrics for `kubectl top` and the HPA

## Kubernetes Objects Quick Reference

### Workload Resources
- **Pod** - Smallest deployable unit, one or more containers sharing network and storage
- **Deployment** - Stateless replicas with rolling updates and rollback
- **ReplicaSet** - Keeps a set number of Pod replicas running (managed by Deployments)
- **StatefulSet** - Stable names, ordered rollout and per-replica storage
- **DaemonSet** - One Pod per node, or per matching node
- **Job** - Runs Pods to completion
- **CronJob** - Runs Jobs on a schedule

### Networking Resources
- **Service** - Stable virtual IP and DNS name for a set of Pods
- **Ingress** - HTTP routing by host and path; needs a controller
- **Gateway API** - Role-oriented successor to Ingress
- **NetworkPolicy** - Allow-list rules for Pod traffic

### Configuration and Access Resources
- **ConfigMap** - Non-sensitive configuration
- **Secret** - Sensitive data, base64-encoded rather than encrypted by default
- **ServiceAccount, Role, RoleBinding** - Workload identity and RBAC permissions

### Storage Resources
- **PersistentVolume (PV)** - Cluster-scoped storage resource
- **PersistentVolumeClaim (PVC)** - Namespaced request for storage
- **StorageClass** - Provisioner and parameters for dynamic provisioning

## Study Strategy in Brief

Spend time roughly in proportion to the weights: about 45% on Domain 1, 30% on Domain 2, and the rest split between Domains 3 and 4. Domains 3 and 4 are smaller but vocabulary-heavy and quick to learn. See [strategy.md](./strategy.md) for the detail and [practice-plan.md](./practice-plan.md) for a day-by-day plan.

### Study Tips for the Multiple-Choice Format
1. Learn **why** each component exists, not only its name
2. Know which component does what in a request's path (API server, scheduler, controller, kubelet)
3. Know when to use each workload type and each Service type
4. Learn the main CNCF projects by category and maturity
5. Read the Kubernetes Concepts section of the docs
6. Take timed practice exams to get used to the question style

## Study Resources

### Official Resources
- **[KCNA Exam Page](https://training.linuxfoundation.org/certification/kubernetes-cloud-native-associate/)** - Registration and exam details
- **[KCNA Program Changes](https://training.linuxfoundation.org/kcna-program-changes/)** - The November 2025 revision
- **[KCNA Exam Curriculum](https://github.com/cncf/curriculum)** - Official curriculum PDFs
- **[Kubernetes Documentation - Concepts](https://kubernetes.io/docs/concepts/)** - Core concepts reference
- **[CNCF Landscape](https://landscape.cncf.io/)** - Interactive project landscape
- **[Cloud Native Glossary](https://glossary.cncf.io/)** - CNCF terminology
- **[OpenGitOps](https://opengitops.dev/)** - GitOps principles
- **[12-Factor App](https://12factor.net/)** - Twelve-factor methodology

### Courses and Practice
- **Linux Foundation LFS250** - Kubernetes and Cloud Native Essentials, the official prep course (sold as a bundle with the exam)
- **KodeKloud and other KCNA courses** - Beginner-friendly video courses with practice tests
- **[Kubernetes Official Tutorials](https://kubernetes.io/docs/tutorials/)** - Free hands-on basics
- **[CNCF YouTube Channel](https://www.youtube.com/c/cloudnativefdn)** - KubeCon talks and project updates

---

KCNA tests breadth. You do not need deep hands-on experience, but you do need to understand the concepts, the terms and how the pieces relate. Kubernetes Fundamentals (44%) and Container Orchestration (28%) together are nearly three quarters of the exam, so build a solid base there first, then pick up the quick points in delivery and architecture.
