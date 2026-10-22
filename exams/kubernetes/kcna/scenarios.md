---
last-updated: 2026-10-22
applies-to: KCNA curriculum revised November 2025, checked 2026-10-22
difficulty: beginner
---

# KCNA High-Yield Scenarios and Practice Problems

## Scenario 1: Kubernetes Architecture

**Scenario**: A team is deploying their first Kubernetes cluster. The lead engineer asks you to explain what happens when a user runs `kubectl apply -f deployment.yaml`. Which components are involved and in what order?

**Solution Pattern**:
- **kubectl** sends the request to the **kube-apiserver**
- The **API server** authenticates, authorizes, and validates the request
- The **API server** stores the Deployment object in **etcd**
- The **Deployment controller** (in kube-controller-manager) detects the new Deployment and creates a ReplicaSet
- The **ReplicaSet controller** creates Pod objects based on the replica count
- The **kube-scheduler** assigns each Pod to a suitable node
- The **kubelet** on the assigned node pulls the container image and starts the container via the container runtime

**Common Distractors**:
- The scheduler creates pods (incorrect - the controller manager creates pods, the scheduler assigns them to nodes)
- etcd communicates directly with kubelet (incorrect - all communication goes through the API server)
- kube-proxy schedules pods (incorrect - kube-proxy manages network rules for Services)

**Key Takeaway**: The API server is the single point of communication. All components interact through the API server, never directly with each other or etcd.

---

## Scenario 2: Choosing the Right Service Type

**Scenario**: A company has three applications in their Kubernetes cluster:
1. A backend API that only needs to be reached by other pods in the cluster
2. A web frontend that must be accessible from the internet
3. An external database hosted outside the cluster that internal services need to reference by name

**Solution Pattern**:
- **Backend API**: ClusterIP Service - internal-only access within the cluster
- **Web Frontend**: LoadBalancer Service (or NodePort behind a cloud load balancer) - external access from the internet
- **External Database**: ExternalName Service - creates a CNAME DNS record pointing to the external hostname

**Common Distractors**:
- Using NodePort for the backend (unnecessary external exposure)
- Using LoadBalancer for all services (wasteful and insecure for internal-only services)
- Using ClusterIP for the external database (ClusterIP is for internal pods, not external services)

**Key Takeaway**: Match Service type to access requirements. ClusterIP for internal, LoadBalancer for external, ExternalName for referencing external services.

---

## Scenario 3: Container Orchestration Benefits

**Scenario**: A startup is running 20 containers directly on three VMs using Docker Compose. They experience frequent downtime when containers crash, manual scaling during traffic spikes, and difficulty updating applications without downtime. Which Kubernetes features address each of these problems?

**Solution Pattern**:
- **Container crashes**: Self-healing via restart policies and liveness probes - Kubernetes automatically restarts failed containers
- **Manual scaling**: Horizontal Pod Autoscaler (HPA) scales pods based on CPU/memory metrics or custom metrics
- **Updates without downtime**: Rolling update strategy in Deployments - gradually replaces old pods with new ones

**Common Distractors**:
- Using DaemonSets for scaling (DaemonSets run one pod per node, not for scaling)
- Using ConfigMaps for self-healing (ConfigMaps store configuration, not health management)
- Using StatefulSets for the rolling update feature (StatefulSets are for ordered, stateful workloads)

**Key Takeaway**: Kubernetes solves the core operational challenges of running containers at scale - self-healing, auto-scaling, and zero-downtime deployments.

---

## Scenario 4: CNCF Ecosystem Tool Selection

**Scenario**: An engineering team needs to set up a complete observability stack for their Kubernetes cluster. They need to collect metrics from all pods, aggregate logs from all containers, implement distributed tracing across microservices, and create dashboards for visualization. Which CNCF ecosystem tools should they use?

**Solution Pattern**:
- **Metrics**: Prometheus (CNCF Graduated) - scrapes metrics endpoints, stores time-series data, supports alerting
- **Logs**: Fluentd (CNCF Graduated) or Fluent Bit - collects and forwards log data from containers
- **Tracing**: OpenTelemetry (CNCF Incubating) or Jaeger (CNCF Graduated) - distributed tracing across services
- **Dashboards**: Grafana - visualization and dashboarding for metrics, logs, and traces

**Common Distractors**:
- Using Prometheus for log collection (Prometheus is for metrics, not logs)
- Confusing Envoy (service proxy) with observability tools
- Using Helm for monitoring (Helm is for package management, not observability)

**Key Takeaway**: The three pillars of observability - metrics, logs, and traces - each have dedicated tools in the CNCF ecosystem. Know which tool serves which pillar.

---

## Scenario 5: Cloud Native Architecture Decision

**Scenario**: A company is refactoring a monolithic Java application into microservices for Kubernetes. The application has a user service, order service, payment service, and notification service. The architect asks about deployment and communication patterns. What cloud native best practices should they follow?

**Solution Pattern**:
- **Deployment**: Each microservice gets its own Deployment, Service, and namespace (or at minimum its own Deployment and Service)
- **Communication**: Services communicate via Kubernetes Services using DNS names (e.g., `order-service.orders.svc.cluster.local`)
- **Configuration**: Use ConfigMaps for non-sensitive config and Secrets for credentials - follow the 12-factor app principle of externalizing configuration
- **Resilience**: Implement readiness and liveness probes for each service; use circuit breaker patterns for inter-service calls
- **Scaling**: Each service scales independently based on its own resource requirements

**Common Distractors**:
- Running all microservices in a single pod (defeats the purpose of microservices)
- Hardcoding service URLs (violates cloud native principles - use DNS-based service discovery)
- Storing configuration in container images (violates 12-factor principle of separating config from code)

**Key Takeaway**: Cloud native applications are loosely coupled, independently deployable, and use Kubernetes-native primitives for configuration and communication.

---

## Scenario 6: Application Delivery with GitOps

**Scenario**: A platform team wants to adopt GitOps for deploying applications to their Kubernetes clusters. They currently deploy by running `kubectl apply` manually from developer laptops. What changes should they make?

**Solution Pattern**:
- **Git as source of truth**: Store all Kubernetes manifests in a Git repository
- **GitOps controller**: Deploy ArgoCD or Flux to the cluster to watch the Git repository
- **Workflow**: Developers push manifest changes to Git; the GitOps controller detects changes and syncs the cluster state to match
- **Benefits**: Audit trail via Git history, rollback via Git revert, consistent environments, no direct cluster access needed for deployments
- **Packaging**: Use Helm charts or Kustomize overlays for environment-specific configurations

**Common Distractors**:
- GitOps means using GitHub Actions for CI/CD (CI is separate from GitOps - GitOps is about continuous delivery from Git state)
- Developers still need direct kubectl access (GitOps eliminates this need for deployments)
- Helm replaces GitOps (Helm is a packaging tool that works alongside GitOps, not a replacement)

**Key Takeaway**: GitOps treats Git as the single source of truth for declarative infrastructure. Changes are made via Git commits, and a controller ensures the cluster matches the desired state.

---

## Scenario 7: Storage and StatefulSets

**Scenario**: A team needs to run a three-node PostgreSQL cluster on Kubernetes. Each database instance needs its own persistent storage that survives pod restarts and rescheduling. Which Kubernetes resources should they use?

**Solution Pattern**:
- **StatefulSet**: Provides stable network identities (postgres-0, postgres-1, postgres-2) and ordered deployment
- **PersistentVolumeClaim (PVC) template**: Each pod gets its own PVC, ensuring dedicated storage per instance
- **StorageClass**: Defines the storage backend (cloud SSD, NFS, etc.) with dynamic provisioning
- **Headless Service**: Allows direct DNS resolution to each pod (postgres-0.postgres-svc.namespace.svc.cluster.local)

**Common Distractors**:
- Using a Deployment with a shared PVC (multiple database instances cannot safely share one volume)
- Using DaemonSet for database nodes (DaemonSet runs on every node, not a fixed replica count)
- Using emptyDir volumes (data is lost when the pod is rescheduled to a different node)

**Key Takeaway**: StatefulSets are designed for stateful workloads that need stable identities and persistent storage. Deployments are for stateless workloads.

---

## Scenario 8: A Pod That Will Not Stay Up (Troubleshooting)

**Scenario**: After a deploy, `kubectl get pods` shows one Pod with STATUS `CrashLoopBackOff` and a RESTARTS count that keeps climbing, and a second Pod in another Deployment stuck in `Pending`. A third Deployment's Pods are `Running` but its Service returns connection timeouts. What is the most likely cause of each, and where do you look?

**Solution Pattern**:
- **CrashLoopBackOff**: The container starts and exits, and the kubelet waits longer before each restart. Read `kubectl logs <pod> --previous` to see why the last instance died (missing environment variable, bad config, app error). Check `describe` for a failing liveness probe or `OOMKilled` as the last state.
- **Pending**: The scheduler could not place the Pod, or it is waiting for something. `kubectl describe pod` Events usually say why, for example "Insufficient cpu", an untolerated taint, unmatched node affinity or an unbound PVC.
- **Running but unreachable**: Check the Service's endpoints. An empty list means the Service selector does not match the Pod labels, or the Pods are not ready because the readiness probe fails. Also check that `targetPort` matches the container port.

**Common Distractors**:
- "CrashLoopBackOff is a Pod phase" (it is a container waiting reason; the phase is usually Running)
- "Pending means the image is downloading slowly" (possible, but the classic cause is scheduling)
- "Restart kube-proxy to fix the Service" (kube-proxy is rarely the problem; an empty endpoint list points to selectors or readiness)

**Key Takeaway**: Read state before guessing. `describe` Events, previous logs and Service endpoints answer most troubleshooting questions.

---

## Scenario 9: Locking Down a Shared Cluster (Security)

**Scenario**: Several teams share one cluster, one namespace each. An audit finds that every app uses the `default` ServiceAccount, one team's Pods run as root with privileged mode, database passwords sit in Secrets that "are encrypted because they look scrambled", and any Pod can connect to any other Pod. What should the platform team change?

**Solution Pattern**:
- **Identity and permissions**: Give each app its own ServiceAccount and bind only the verbs it needs with a Role and RoleBinding in its namespace (least privilege). Disable token mounting where the app never calls the API.
- **Pod hardening**: Label each namespace for Pod Security Admission with the `restricted` (or at least `baseline`) profile in `enforce` mode, and set `runAsNonRoot`, `allowPrivilegeEscalation: false` and dropped capabilities in the securityContext.
- **Secrets**: Secrets are base64-encoded, not encrypted. Turn on encryption at rest (ideally with a KMS provider), restrict `get` and `list` on Secrets with RBAC, and consider an external secret manager.
- **Network**: Add a default-deny NetworkPolicy per namespace, then allow only the required flows, on a CNI plugin that enforces policies.
- **Guardrails**: Use a policy engine such as OPA Gatekeeper or Kyverno to reject privileged Pods, images without a digest or signature, and Pods without resource limits.

**Common Distractors**:
- "Namespaces alone isolate teams" (namespaces scope names and policies, but do not block network traffic or grant permissions by themselves)
- "Re-enable PodSecurityPolicy" (it was removed in v1.25; Pod Security Admission replaced it)
- "Base64 is good enough because it is not human-readable" (anyone with read access can decode it)

**Key Takeaway**: Security is layered: identity (RBAC, ServiceAccounts), workload (Pod Security, securityContext), data (Secrets encryption), network (NetworkPolicy) and admission policy.

---

## Scenario 10: A Rollout That Went Wrong (Debugging)

**Scenario**: A team updates a Deployment's image from `v1.8` to `v1.9`. Ten minutes later, half the Pods run `v1.9` and are not ready, half still run `v1.8`, and the Deployment reports `ProgressDeadlineExceeded`. The cluster is managed by Argo CD. The `v1.9` image is distroless and has no shell. How should they debug and recover?

**Solution Pattern**:
- **Read the rollout**: `kubectl rollout status` and `kubectl describe deployment` show the stalled progress; `kubectl rollout history` lists revisions. Kubernetes does not roll back by itself, which is why old and new Pods are mixed.
- **Find the cause**: Check events and `kubectl logs` for the new Pods. Since there is no shell, use `kubectl debug` to attach an ephemeral container with debugging tools, or `kubectl port-forward` to hit the new Pod directly.
- **Recover**: In a GitOps-managed cluster, revert the commit that bumped the image tag so Argo CD syncs back to `v1.8`. A `kubectl rollout undo` would work briefly, but Argo CD would see drift (OutOfSync) and reapply `v1.9`.
- **Prevent**: Use correct readiness probes and consider progressive delivery (Argo Rollouts or Flagger) to stop and roll back automatically on bad metrics.

**Common Distractors**:
- "Kubernetes automatically rolls back after the progress deadline" (it only reports the condition)
- "Use `kubectl exec` to open a shell in the new Pod" (a distroless image has no shell)
- "`kubectl rollout undo` is the permanent fix" (under GitOps, Git is the source of truth)

**Key Takeaway**: Debug from rollout state, events and logs; fix through the source of truth. In GitOps, rollback is a Git revert.

## Key Decision Factors

### Domain Priority for Study
1. **Kubernetes Fundamentals (44%)** - Core concepts, administration, scheduling, containerization
2. **Container Orchestration (28%)** - Networking, security, troubleshooting, storage
3. **Cloud Native Application Delivery (16%)** - GitOps, Helm, Kustomize, rollout strategies, debugging
4. **Cloud Native Architecture (12%)** - Observability, CNCF ecosystem and principles, community and collaboration

### Common Anti-Patterns
- Memorizing commands instead of understanding concepts (this is a knowledge exam)
- Studying from a guide written for the pre-November-2025 five-domain outline
- Ignoring the CNCF ecosystem and community beyond Kubernetes itself
- Not understanding the relationships between components
- Confusing similar-sounding concepts (StatefulSet vs Deployment, ConfigMap vs Secret, liveness vs readiness)
