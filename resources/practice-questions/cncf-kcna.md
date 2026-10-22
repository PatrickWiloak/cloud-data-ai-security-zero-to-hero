---
last-updated: 2026-10-22
difficulty: beginner
---

# Kubernetes and Cloud Native Associate (KCNA) - Practice Questions

30 questions for KCNA prep, weighted toward Kubernetes fundamentals (44%) and container orchestration (28%), which together are almost three quarters of the exam. Questions 16-30 follow the curriculum the CNCF revised in November 2025, which folds observability into cloud native architecture (12%) beside application delivery (16%).

KCNA is multiple choice and knowledge-based, so this format matches the real thing closely.

> **Cert page:** [exams/kubernetes/kcna/](../../exams/kubernetes/kcna/)

---

### Question 1
**Scenario:** Which control plane component decides which node a new pod runs on?

A. kube-proxy on each node
B. kubelet
C. kube-controller-manager
D. kube-scheduler

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The scheduler watches for pods with no assigned node and picks one based on resource requests, affinity, taints, and other constraints. The kubelet runs pods once assigned. The controller manager reconciles higher-level objects toward their desired state. kube-proxy implements Service networking on each node.
</details>

---

### Question 2
**Scenario:** A team wants the smallest deployable unit in Kubernetes described accurately.

A. A node, which is the machine that runs the container runtime and hosts the pods assigned to it
B. A container, which Kubernetes schedules and restarts directly without any wrapper object around it
C. A pod, which holds one or more containers that share a network namespace and can share storage volumes between them
D. A Deployment, which declares the replica count and rolling update strategy for a set of identical workloads

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Kubernetes never schedules a bare container; it schedules pods. Containers in a pod share a network namespace (so they reach each other on `localhost`) and can share volumes. A Deployment manages pods, and a node is the machine they land on.
</details>

---

### Question 3
**Scenario:** Which object guarantees a copy of a pod runs on every node, including nodes added later?

A. DaemonSet, one pod per node
B. StatefulSet, ordered pods with stable names
C. Deployment, a set of identical replicas
D. ReplicaSet

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A DaemonSet is the "one per node" controller, which is why log collectors, CNI agents, and node exporters use it. Deployments and ReplicaSets manage a replica count without node affinity. StatefulSets give stable identities and ordered rollout for stateful workloads.
</details>

---

### Question 4
**Scenario:** What does the Kubernetes control loop actually do?

A. Schedules cron jobs at the times listed in the CronJob objects and records the result of each run
B. Continuously compares desired state in the API to observed state and acts to close the gap between the two
C. Executes commands in the exact order an operator typed them, replaying the whole history if a node restarts later on
D. Runs a fixed installation script when the cluster is created and never looks at the cluster state again after that

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Declarative reconciliation is the central idea. You state what you want, controllers observe what is, and they act repeatedly to converge. This is why deleting a pod managed by a Deployment gets you a replacement rather than an outage, and why the API is the source of truth rather than the command history.
</details>

---

### Question 5
**Scenario:** Which of these is the container runtime interface Kubernetes uses to talk to runtimes such as containerd?

A. CRI
B. CSI, the container storage interface that lets the kubelet attach volumes from storage vendor drivers
C. CNI, the container network interface that sets up pod networking through plugins such as Calico or Cilium
D. OCI, the open container initiative image and runtime specification that containerd and runc implement

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** CRI is the runtime interface between kubelet and the container runtime. CNI is networking, CSI is storage, and OCI is the specification for image and runtime formats that the runtimes themselves implement. Knowing which acronym covers which layer is standard KCNA material.
</details>

---

### Question 6
**Scenario:** A cluster's data store holds all API objects and cluster state.

A. PostgreSQL
B. Redis
C. etcd, a key-value store
D. The kubelet's local disk on each node

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** etcd is the consistent key-value store behind the API server, and it is the thing you must back up to recover a cluster. Nothing else in the list is a supported backing store for upstream Kubernetes.
</details>

---

### Question 7
**Scenario:** What is the purpose of a namespace?

A. A separate control plane with its own API server
B. A logical grouping for names, RBAC scope, and resource quotas
C. Network encryption between the pods in the group
D. Physical isolation across nodes, so the pods of one namespace never share a machine with another namespace

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Namespaces scope object names and provide a boundary for RBAC and quotas. They are not a security boundary at the kernel or network level: pods in different namespaces can talk to each other by default and share the node's kernel.
</details>

---

### Question 8
**Scenario:** Which project provides the packaging and templating format most commonly used to install applications on Kubernetes?

A. Helm, with versioned charts
B. Envoy
C. Fluentd
D. Prometheus, a time series monitoring server

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Helm charts package manifests with templated values and a release lifecycle. Prometheus is monitoring, Envoy is a proxy used by service meshes, and Fluentd is log collection. KCNA expects you to know the shape of the CNCF landscape by category.
</details>

---

### Question 9
**Scenario:** The three pillars of observability, as the cloud native community usually states them.

A. CPU, RAM, disk
B. Logs, metrics, traces
C. Alerts, dashboards, runbooks
D. Availability, latency, throughput

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Logs are discrete events, metrics are aggregated numbers over time, and traces follow a request across services. Alerts and dashboards are things you build on top of these. The last option lists service level indicators, which are what you measure, not how you collect it.
</details>

---

### Question 10
**Scenario:** Which statement about containers versus virtual machines is correct?

A. Containers include their own kernel, packaged in the image alongside the application and its libraries
B. Containers share the host kernel, isolated by namespaces and cgroups
C. Containers cannot limit memory, because only a hypervisor can enforce resource caps on a workload
D. VMs start faster than containers, since a hypervisor boots from a small image and skips image pulls

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Sharing the kernel is what makes containers small and fast to start, and it is also why kernel-level isolation is weaker than a VM's. Namespaces provide the isolated view and cgroups provide the resource limits. Containers absolutely can limit memory, via cgroups.
</details>

---

### Question 11
**Scenario:** An application should scale up when average CPU utilization exceeds 70%.

A. Cluster Autoscaler, which adds nodes when pods cannot be scheduled and removes nodes that sit mostly empty
B. Vertical Pod Autoscaler, which raises pod requests
C. PodDisruptionBudget, which limits evictions
D. Horizontal Pod Autoscaler, which adds replicas to hit a target

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** HPA adds and removes pod replicas based on a metric target. VPA changes the requests and limits of existing pods. Cluster Autoscaler adds and removes nodes, and it typically works together with HPA rather than instead of it. A PDB constrains voluntary disruption.
</details>

---

### Question 12
**Scenario:** What does GitOps mean in one sentence?

A. Hosting your code on GitHub, with pull requests as the way that changes reach the main branch
B. Running CI pipelines for every commit, with the build and test results reported back to the pull request
C. Using git tags for releases, so every release has a version number that can be traced to a commit
D. Declaring desired state in git, with an agent that reconciles the cluster to match

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The OpenGitOps principles are declarative, versioned and immutable, pulled automatically, and continuously reconciled. The pull-and-reconcile part is what separates GitOps from a pipeline that pushes with `kubectl apply`. Argo CD and Flux are the common implementations.
</details>

---

### Question 13
**Scenario:** Which best describes a service mesh?

A. A container registry that stores, scans, and signs images
B. A CNI plugin that gives each pod an IP address
C. A layer of sidecar or node proxies for traffic management, mTLS, and telemetry
D. A storage backend offering replicated block volumes

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A mesh moves cross-cutting network concerns out of application code into proxies. Istio and Linkerd are the common examples. It sits above the CNI, which provides basic pod connectivity, rather than replacing it.
</details>

---

### Question 14
**Scenario:** What is the CNCF's role in the projects it hosts?

A. It provides vendor-neutral governance, hosting projects at sandbox, incubating, and graduated maturity levels, under the Linux Foundation
B. It sells the software under a commercial licence and provides paid support for each project it hosts
C. It certifies cloud providers only, checking that their managed services follow the Kubernetes conformance tests
D. It writes all the code, with a staff of engineers employed by the foundation to maintain every project

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The CNCF is a Linux Foundation project that provides neutral home, governance, and marketing for cloud native projects, and it stages them through sandbox, incubating, and graduated. Kubernetes, Prometheus, and Envoy are graduated examples. The code comes from the contributing community, not the foundation.
</details>

---

### Question 15
**Scenario:** A container image should be identified in a way that cannot change under you.

A. The `latest` tag, which always points to the newest build and so keeps the deployment up to date
B. The image name alone, which is enough because registries keep one image per repository name
C. A digest, such as `image@sha256:...`
D. A semantic version tag such as `v1.4.2`, which is readable but which maintainers can move to a different build

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A digest is a content hash, so it always refers to exactly the same bytes. Tags are mutable pointers: `latest` and even a version tag can be re-pushed. Using digests is a small change that gives you reproducible deployments and closes a real supply chain gap.
</details>

---

### Question 16
**Scenario:** A Deployment is created with 3 replicas. Which object does the Deployment create directly to keep 3 pods running?

A. A StatefulSet, which the Deployment controller uses to give each pod a stable name
B. A ReplicaSet, which in turn creates the pods and replaces any that fail or are deleted
C. Three separate Pod objects, each owned directly by the Deployment with no object in between
D. A DaemonSet scoped to three nodes, so that each node runs exactly one of the replicas

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A Deployment manages ReplicaSets, and each ReplicaSet keeps its pod count; a rollout creates a new ReplicaSet and scales the old one down. StatefulSets are a separate workload type for stable identity and are not used by Deployments. Pods created by a Deployment are owned by the ReplicaSet, not the Deployment itself. DaemonSets run one pod per node and are not how Deployments work.
</details>

---

### Question 17
**Scenario:** Which component runs on every worker node and makes sure the containers described in pod specs are actually running?

A. The kube-scheduler, which also restarts failed containers after placing them on nodes
B. The kube-controller-manager, which connects to each node's runtime over SSH
C. The kubelet, which works with the container runtime through the CRI on that node
D. The cloud-controller-manager, which only runs on cloud-hosted worker nodes

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The kubelet is the node agent: it watches for pods assigned to its node and tells the container runtime to start and keep them running. The scheduler only picks a node and never touches containers. The controller manager runs control loops against the API server and does not connect to nodes over SSH. The cloud-controller-manager integrates with the cloud provider's APIs, such as load balancers and node lifecycle, not container lifecycle.
</details>

---

### Question 18
**Scenario:** A pod should only be scheduled onto nodes that have a GPU. The nodes are labeled `gpu=true`.

A. Add a toleration for `gpu=true` to the pod, which pulls it toward the GPU nodes
B. Set a high `priorityClassName` so the scheduler picks the most capable nodes first
C. Give the pod a large CPU request so only the big GPU nodes can fit it
D. Use a `nodeSelector` or a required node affinity rule that matches the `gpu=true` label

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `nodeSelector` and node affinity restrict scheduling to nodes with matching labels, which is exactly the requirement. A toleration only allows a pod onto tainted nodes; it does not attract the pod there. Priority affects which pods get scheduled or preempted first, not which nodes they land on. A large CPU request is an indirect hack that breaks the moment a non-GPU node has enough CPU.
</details>

---

### Question 19
**Scenario:** Which tool is the standard command-line client for talking to the Kubernetes API server?

A. `kubectl`, which sends authenticated REST requests to the API server for you
B. `kubeadm`, which is used for day-to-day reading and changing of cluster objects
C. `crictl`, which talks to the API server on behalf of the container runtime
D. `etcdctl`, which edits cluster objects by writing directly into the data store

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `kubectl` is the general client for the Kubernetes API: get, apply, describe, logs and so on. `kubeadm` bootstraps and upgrades clusters but is not the everyday object client. `crictl` talks to the container runtime on a node through CRI, not to the API server. `etcdctl` operates on etcd directly and bypasses the API server's validation, which is for backup and repair, not normal use.
</details>

---

### Question 20
**Scenario:** A taint `dedicated=db:NoSchedule` is placed on a node. What happens to new pods without a matching toleration?

A. They are scheduled to the node but given a lower CPU share than tolerating pods
B. They are not scheduled onto that node, while pods already on it stay
C. They are scheduled normally and later evicted once the node becomes busy
D. They fail to start with an image pull error on that node only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A `NoSchedule` taint stops the scheduler from placing pods that lack a matching toleration onto that node. Taints do not affect CPU shares. Eviction of running pods is the `NoExecute` effect, not `NoSchedule`. Taints have nothing to do with image pulling.
</details>

---

### Question 21
**Scenario:** Which statement best describes an Open Container Initiative (OCI) image?

A. A full virtual machine disk that includes its own kernel and boot loader for each image
B. A Kubernetes manifest format that describes a pod and the containers it should run
C. A standard format of filesystem layers plus configuration that any compliant runtime can run
D. A format that works only with Docker Engine and cannot be run by containerd or CRI-O

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The OCI image spec defines layered filesystem content plus a configuration and manifest, so images built by one tool run on any compliant runtime. Container images share the host kernel and do not include one, unlike VM disks. Pod manifests are a Kubernetes API concept, separate from images. containerd and CRI-O both run OCI images, which is the point of the standard.
</details>

---

### Question 22
**Scenario:** An administrator wants to drain a node for maintenance. What does `kubectl drain` do?

A. Marks the node unschedulable and evicts its pods so controllers recreate them elsewhere
B. Deletes the node object from the cluster and deregisters its kubelet permanently
C. Stops the kubelet on the node, leaving its running pods in place until it restarts
D. Moves running containers live to another node without restarting them

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Drain cordons the node so nothing new lands there, then evicts pods, respecting PodDisruptionBudgets, so their controllers recreate them on other nodes. It does not delete the node object; `kubectl uncordon` brings it back. It does not stop the kubelet. Kubernetes does not live-migrate containers; pods are recreated, not moved.
</details>

---

### Question 23
**Scenario:** A pod needs storage that outlives the pod and is provisioned automatically from the cluster's storage backend.

A. An `emptyDir` volume with `medium: Memory` so the data is kept safely in RAM
B. A `hostPath` volume on whichever node the pod happens to land on
C. A ConfigMap mounted as a volume and written to by the application at runtime
D. A PersistentVolumeClaim that references a StorageClass for dynamic provisioning

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A PersistentVolumeClaim with a StorageClass asks the provisioner to create a PersistentVolume, and that volume lives on after the pod is deleted. `emptyDir` is deleted with the pod, in memory or on disk. `hostPath` ties data to one node and is lost if the pod moves. ConfigMap volumes are read-only configuration, not writable storage.
</details>

---

### Question 24
**Scenario:** By default, with no NetworkPolicy in a namespace, which pods can talk to each other?

A. Only pods running on the same node, because traffic between nodes is blocked by default
B. Only pods in the same namespace, because namespaces are network boundaries
C. All pods can reach all other pods, across namespaces and nodes
D. No pods can talk to each other until a Service is created for them

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The Kubernetes network model gives every pod a routable IP and allows all pod-to-pod traffic until a NetworkPolicy restricts it. Cross-node traffic works by design through the CNI plugin. Namespaces group names and permissions but are not network boundaries on their own. Services provide stable names and load balancing, but pods can reach each other by IP without them.
</details>

---

### Question 25
**Scenario:** A pod is stuck in `Pending`. What is the most useful first command?

A. `kubectl logs <pod>`, because the container log shows why it was not scheduled
B. `kubectl describe pod <pod>` to read the scheduling events
C. `kubectl exec -it <pod> -- sh` to look inside the container for the cause
D. `kubectl delete node` on the busiest node to free up space for the pod

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A `Pending` pod usually has not been scheduled, and `kubectl describe` shows the events, such as insufficient CPU, an unbound claim, or no node matching affinity. Logs and exec need a running container, which a pending pod does not have. Deleting nodes is destructive and reduces capacity instead of diagnosing anything.
</details>

---

### Question 26
**Scenario:** Which mechanism does Kubernetes use to decide whether a user or service account may perform an action, such as listing Secrets?

A. RBAC rules in Roles and ClusterRoles, bound to subjects with RoleBindings
B. NetworkPolicy, which allows or denies API calls by source pod IP address
C. Pod Security Admission, which approves every request to the API server
D. Linux file permissions on the etcd data directory on each control plane node

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** RBAC authorizes API requests: Roles and ClusterRoles list allowed verbs on resources, and RoleBindings and ClusterRoleBindings grant them to users, groups and service accounts. NetworkPolicy controls pod network traffic, not API permissions. Pod Security Admission checks pod specs against security levels, not every request. etcd file permissions protect the data store but are not how API authorization works.
</details>

---

### Question 27
**Scenario:** A team wants to release a new version to a small share of users, watch the metrics, then widen the rollout. What is this strategy called?

A. Blue-green deployment, where all traffic switches at once between two full environments
B. Recreate deployment, where all old pods stop before new pods start
C. Canary release that widens in steps as metrics stay healthy
D. Rolling back, where the previous ReplicaSet is scaled up again for safety

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A canary release sends a small share of traffic to the new version first and widens it as metrics stay healthy. Blue-green switches all traffic at once between two complete environments. Recreate stops everything before starting the new version, which causes downtime. Rolling back is what you do when a release goes wrong, not a release strategy.
</details>

---

### Question 28
**Scenario:** What is the role of a CI/CD pipeline in cloud native application delivery?

A. It replaces the need for container images by deploying source code straight to nodes
B. It is only used to provision the cluster and never touches application releases
C. It runs the production workload itself in place of the Kubernetes control plane
D. It automates building, testing and releasing changes so they reach environments repeatably

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** CI builds and tests every change, and CD releases the result to environments in a repeatable, automated way, often by producing an image and updating manifests. Pipelines usually produce images rather than replacing them. Pipelines can provision infrastructure, but application release is their main job. The pipeline delivers workloads; the cluster runs them.
</details>

---

### Question 29
**Scenario:** A team wants a cluster that adds nodes when pods cannot be scheduled for lack of capacity. Which component does this?

A. The Horizontal Pod Autoscaler, which adds nodes when pod CPU is high
B. The Cluster Autoscaler, or a node provisioner such as Karpenter
C. The Vertical Pod Autoscaler, which grows the node's VM size in place
D. The kube-scheduler, which creates new nodes when no node can fit a pod

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Cluster Autoscaler, and node provisioners like Karpenter, watch for unschedulable pods and add nodes, then remove empty ones. The HPA changes the number of pods, not nodes. The VPA adjusts pod resource requests, not node sizes. The scheduler only places pods on existing nodes.
</details>

---

### Question 30
**Scenario:** Which project is the CNCF standard for generating and exporting traces, metrics and logs in a vendor-neutral way?

A. Prometheus, which is a vendor-neutral standard for traces and logs as well as metrics
B. Fluentd, which defines the tracing API that applications call to create spans
C. Jaeger, which collects metrics and logs from every application by default
D. OpenTelemetry, with its APIs, SDKs and collector for all three signal types

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** OpenTelemetry provides the APIs, SDKs and collector for traces, metrics and logs, and exports them to many backends, which is why observability now sits under cloud native architecture in the KCNA outline. Prometheus is a metrics system and does not handle traces or logs. Fluentd collects and routes logs but does not define a tracing API. Jaeger is a tracing backend and does not collect metrics and logs.
</details>

---

## Where to go deeper

- [KCNA cert page](../../exams/kubernetes/kcna/) - notes, practice plan, strategy
- [KCSA practice questions](https://security.noblerworks.com/resources/practice-questions/cncf-kcsa/) - the security sibling exam
- [Kubernetes in 10 minutes](../../learn/concepts/kubernetes-in-10-minutes.md) - plain-English primer
- [Containers vs VMs](../../learn/concepts/containers-vs-vms.md) - the foundation KCNA assumes
- **[📖 Kubernetes concepts](https://kubernetes.io/docs/concepts/)** - the source for most KCNA content
