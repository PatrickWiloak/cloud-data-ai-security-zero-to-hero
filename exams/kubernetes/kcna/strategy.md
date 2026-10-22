---
last-updated: 2026-10-22
applies-to: KCNA curriculum revised November 2025, checked 2026-10-22
difficulty: beginner
---

# KCNA Study Strategy

This strategy follows the revised outline for exams taken on or after 24 November 2025. If you studied from an older guide, the main changes are: Container Orchestration is now 28% and owns networking, security, troubleshooting and storage; Application Delivery doubled to 16% and added debugging; observability moved into Cloud Native Architecture (12%) alongside a new community and collaboration competency.

## How to split your time

| Domain | Weight | Share of study time | Why |
|---|---|---|---|
| 1. Kubernetes Fundamentals | 44% | About 40% | Biggest domain, and everything else builds on it |
| 2. Container Orchestration | 28% | About 30% | Security and troubleshooting are new emphasis and reward real understanding |
| 3. Cloud Native Application Delivery | 16% | About 15% | GitOps principles and rollout strategies are quick, reliable points |
| 4. Cloud Native Architecture | 12% | About 15% | Small weight but broad vocabulary; worth slightly more than its weight |

Domain 4 gets a little more than its weight because it is mostly recall of names and definitions (CNCF projects, maturity levels, TAGs versus SIGs, metric types), and recall needs repetition.

## Study Approach

### Phase 1: Kubernetes Fundamentals (Week 1)
Read [01-kubernetes-fundamentals.md](./notes/01-kubernetes-fundamentals.md).
1. **Core concepts** - Control plane and node components, how a `kubectl apply` flows through the API server, controllers and reconciliation, the workload types and when to use each, namespaces, labels and selectors, ConfigMaps and Secrets.
2. **Administration** - kubeconfig contexts, imperative versus declarative, ResourceQuota and LimitRange, kubeadm, upgrade order and version skew.
3. **Scheduling** - Filter and score, requests versus limits, QoS classes, affinity, taints and tolerations, priority and preemption.
4. **Containerization** - Containers versus VMs, layers, tags versus digests, OCI, CRI, containerd and CRI-O, dockershim, multi-stage builds.

### Phase 2: Container Orchestration (Week 2)
Read [02-container-orchestration.md](./notes/02-container-orchestration.md).
1. **Networking** - The flat Pod network and CNI, Service types and how kube-proxy routes them, CoreDNS names, Ingress versus Gateway API, NetworkPolicy behaviour.
2. **Security** - The 4Cs, authentication versus authorization versus admission, RBAC objects, ServiceAccounts, Pod Security Standards, why Secrets are not encrypted by default, scanning, signing and policy engines.
3. **Troubleshooting** - Pod phases versus container reasons, the symptom table (Pending, ImagePullBackOff, CrashLoopBackOff, OOMKilled), the three probes, empty Service endpoints, NotReady nodes.
4. **Storage** - emptyDir versus PVs, PV, PVC and StorageClass, access modes including RWOP, reclaim policies, CSI, StatefulSet volumes.

### Phase 3: Delivery and Architecture (Week 3)
Read [03-application-delivery.md](./notes/03-application-delivery.md) and [04-cloud-native-architecture.md](./notes/04-cloud-native-architecture.md).
1. **Application delivery** - CI versus continuous delivery versus continuous deployment, the four OpenGitOps principles word for word, Argo CD and Flux, Helm vocabulary, Kustomize, the four rollout strategies, progressive delivery.
2. **Debugging** - Rollout status, history and undo, ProgressDeadlineExceeded, `kubectl debug` and ephemeral containers, Helm release states, GitOps OutOfSync versus Degraded.
3. **Observability** - Three signals, Prometheus pull model and components, metrics-server versus kube-state-metrics, Fluent Bit, OpenTelemetry versus Jaeger, SLIs and SLOs.
4. **Ecosystem and community** - CNCF definition, twelve-factor, microservices trade-offs, serverless, maturity levels and examples, TOC, TAGs, SIGs, KEPs, release cadence.

### Phase 4: Practice and review (Week 4)
Timed practice questions, [scenarios.md](./scenarios.md), [flashcards.csv](./flashcards.csv) and targeted re-reading of weak sections.

## Study Resources

### Primary Resources
- **[KCNA exam page](https://training.linuxfoundation.org/certification/kubernetes-cloud-native-associate/)** - Current domains and weights
- **[KCNA program changes](https://training.linuxfoundation.org/kcna-program-changes/)** - The November 2025 revision
- **[Kubernetes Documentation](https://kubernetes.io/docs/concepts/)** - Read the Concepts section thoroughly
- **[CNCF curriculum](https://github.com/cncf/curriculum)** - Official curriculum PDFs
- **[Cloud Native Glossary](https://glossary.cncf.io/)** - Terminology
- **[CNCF Landscape](https://landscape.cncf.io/)** - Project map
- **[OpenGitOps](https://opengitops.dev/)** - GitOps principles

### Supplementary Resources
- **[Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)** - Builds deep architecture intuition
- **[Prometheus Documentation](https://prometheus.io/docs/introduction/overview/)** - Monitoring concepts
- **[Helm Documentation](https://helm.sh/docs/)** - Packaging
- **[12-Factor App](https://12factor.net/)** - Application design principles
- **[Kubernetes community repository](https://github.com/kubernetes/community)** - SIGs and governance, for the community competency
- **[Practice questions](../../../resources/practice-questions/cncf-kcna.md)** - Original practice questions

### Courses
- **Linux Foundation LFS250** - Kubernetes and Cloud Native Essentials, the official course
- **KodeKloud, freeCodeCamp and similar** - Visual introductions; check that a course has been updated for the November 2025 outline

## Exam Tactics

### Time Management (90 minutes, about 60 questions)
- About 90 seconds per question on average
- Answer the ones you know first, in under a minute each
- Flag uncertain questions and move on
- Keep 10-15 minutes at the end for flagged questions

### Question Strategy
1. **Read the whole question** before the options
2. **Eliminate clearly wrong answers** first
3. **Watch keywords** - "best", "most", "primary" and "NOT" change the answer
4. **Distrust absolutes** - "always" and "never" are often wrong
5. **Pick the most specific correct answer** when several look right
6. **Change an answer only for a clear reason**

## Common Pitfalls

### Study Mistakes
- **Using a pre-November-2025 guide** - The weights and some topics have changed; security, troubleshooting, debugging and community now have explicit weight
- **Too much terminal time** - Hands-on helps understanding, but this is a knowledge exam
- **Skipping Domain 4** - 12% is roughly seven questions, and most are fast recall
- **Learning commands instead of meanings** - Know what `kubectl rollout undo` does, not its flags

### Content Mistakes
- Thinking the scheduler starts containers (the kubelet does)
- Thinking Secrets are encrypted by default (they are base64-encoded)
- Treating CrashLoopBackOff as a Pod phase
- Confusing liveness (restart) with readiness (remove from endpoints)
- Confusing RWO (one node) with RWOP (one Pod)
- Calling push-based CI deploys "GitOps"
- Confusing metrics-server with kube-state-metrics
- Confusing CNCF TAGs with Kubernetes SIGs
- Thinking containers have their own kernel

## Progress Tracking

### Self-Assessment Questions

**Domain 1:**
- Can I trace a `kubectl apply` of a Deployment through every component?
- Can I explain requests versus limits and the three QoS classes?
- Can I explain taints versus affinity and when to combine them?
- Can I explain why dockershim's removal did not break Docker-built images?

**Domain 2:**
- Can I name every Service type and when to use it?
- Can I explain the order authentication, authorization, admission?
- Can I diagnose Pending, ImagePullBackOff, CrashLoopBackOff and OOMKilled from a description?
- Can I explain PV, PVC, StorageClass and the four access modes?

**Domain 3:**
- Can I state the four OpenGitOps principles?
- Can I compare rolling, recreate, blue-green and canary?
- Can I explain what OutOfSync and Degraded mean in Argo CD?

**Domain 4:**
- Can I describe the Prometheus pull model and Alertmanager's role?
- Can I name the three CNCF maturity levels with examples?
- Can I explain TOC, TAG, SIG and KEP?

### Readiness Indicators
You are ready when:
- [ ] You can explain every control plane and node component from memory
- [ ] You can diagnose the common Pod symptoms from a description
- [ ] You can state the four GitOps principles and the four rollout strategies
- [ ] You know the main CNCF projects by category and maturity
- [ ] You score 80% or more on timed practice sets, consistently
