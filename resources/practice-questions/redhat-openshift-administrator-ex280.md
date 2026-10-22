---
last-updated: 2026-10-22
difficulty: advanced
---

# Red Hat Certified Specialist in OpenShift Administration (EX280) - Practice Questions

30 questions on OpenShift administration: cluster and project management, authentication and RBAC, security context constraints, networking and routes, storage, and application deployment. EX280 is a hands-on performance exam, so these test the concepts you must be able to configure at the CLI.

> **Cert page:** [exams/redhat/openshift-administrator-ex280/](../../exams/redhat/openshift-administrator-ex280/)

---

### Question 1
**Scenario:** How does an OpenShift project relate to a Kubernetes namespace?

A. A project is a Kubernetes namespace with extra annotations and access controls
B. A project is a separate cluster with its own control plane and etcd, which is why each team is given one
C. A project is a pod-level grouping that schedules several containers together onto one node
D. They are unrelated; one project can span namespaces

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Projects are the OpenShift wrapper around namespaces, adding self-service creation and per-project access. This is why you work with projects at the `oc` CLI while the underlying object remains a namespace.
</details>

---

### Question 2
**Scenario:** A new identity provider must be configured for user authentication.

A. Edit each user manually in a ConfigMap in the openshift-config namespace, then restart the API servers to load them
B. Configure an identity provider in the cluster OAuth resource, such as HTPasswd, LDAP, or OIDC
C. Use the kubeadmin account permanently, since it is the supported long-term administrator for every cluster
D. Disable authentication on the API server so the console accepts requests without a login

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OpenShift ships a built-in OAuth server, and identity providers are added to its configuration. The temporary kubeadmin user is meant to be removed once a real identity provider and a cluster administrator are established.
</details>

---

### Question 3
**Scenario:** A user must be able to view resources in a project but not modify them.

A. Bind the cluster-admin role to the user in that project, since reading resources needs elevated rights
B. No binding needed, because every authenticated user can already read all projects through the system:authenticated group
C. Bind the `view` cluster role to the user in that project with a role binding
D. Give them the edit role in that project, since it includes view and they can simply choose not to change anything

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The default roles are `view`, `edit`, `admin`, and `cluster-admin`, and a role binding scopes the grant to one project. Using a cluster role binding instead would grant it across every project, which is the common over-grant mistake.
</details>

---

### Question 4
**Scenario:** A container image needs to run as a specific user ID but is blocked.

A. Give the pod privileged access by granting the privileged SCC to the default service account in the namespace
B. Disable SCC admission cluster-wide so images can pick any UID they need
C. Understand why the restricted SCC blocks it, then grant a suitable SCC to that workload's service account only if justified
D. Run everything as root by setting runAsUser 0 and granting anyuid to every service account in the cluster

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** SCCs are OpenShift's distinctive security control, and the default restricted SCC assigns a random UID and blocks root, which breaks images that assume a fixed UID. The correct fix is a targeted SCC on the service account, not weakening security cluster-wide.
</details>

---

### Question 5
**Scenario:** Which SCC is the most restrictive and applied by default?

A. restricted-v2, which drops capabilities and runs pods with an arbitrary non-root UID
B. hostnetwork, which is applied by default because pods generally need to reach the node's network interfaces directly
C. privileged, which is applied by default to any pod that sets no securityContext, because it avoids permission errors
D. anyuid, which is applied by default so images that expect a fixed UID such as root work out of the box

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** restricted-v2 is the secure baseline that most workloads should run under. `anyuid` allows a fixed UID including root, and `privileged` removes nearly all isolation, so each is a deliberate escalation to justify rather than a default.
</details>

---

### Question 6
**Scenario:** An application must be reachable from outside the cluster over HTTP.

A. A NodePort service on every node, which is the only built-in way to reach pods over HTTP from outside the cluster
B. A Route, which exposes a service through the OpenShift router at a hostname, optionally with TLS
C. A ClusterIP service only, since its virtual IP is routable from external networks
D. A host port on the pod, binding to port 80 on the node so clients use the node address

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Routes are the OpenShift construct built on the ingress router and predate the Kubernetes Ingress they now coexist with. TLS termination modes (edge, passthrough, re-encrypt) are examinable, since the choice determines where certificates live.
</details>

---

### Question 7
**Scenario:** What is the difference between edge and passthrough TLS termination on a route?

A. Passthrough terminates TLS at the router, which then forwards plaintext to the pod, while edge sends the encrypted stream on to the pod untouched
B. They are the same mode under two names; the router decrypts the traffic and re-encrypts it again before it is forwarded on to the application pod
C. Edge does not use TLS at all; it forwards plain HTTP end to end, and only passthrough involves certificates
D. Edge terminates TLS at the router and sends plaintext to the pod; passthrough sends encrypted traffic to the pod, which terminates it

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Edge is simplest and centralizes certificates at the router; passthrough is required when the application must terminate TLS itself, for example for mutual TLS. Re-encrypt is the third mode, terminating at the router then re-encrypting to the pod.
</details>

---

### Question 8
**Scenario:** Persistent storage must be provided to a stateful application.

A. A ConfigMap mounted at the data path, since it persists across pod restarts and can hold application state of any size
B. Store data in the container's writable layer, which is kept when the pod is rescheduled
C. Use an emptyDir volume, which survives pod deletion and rescheduling on the node's disk
D. A PersistentVolumeClaim bound to a PersistentVolume, ideally through a StorageClass for dynamic provisioning

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** emptyDir and container filesystems are ephemeral and lost on pod restart. The access mode matters for the design: ReadWriteOnce binds to one node, so a workload needing shared writable storage across nodes requires ReadWriteMany, which not every backend supports.
</details>

---

### Question 9
**Scenario:** Resource consumption in a project must be capped.

A. Delete pods manually whenever usage grows, since the scheduler enforces no ceiling on a project's CPU or memory
B. Nothing can limit it, because requests and limits on pods only influence scheduling and never cap a project total
C. A ResourceQuota to cap total consumption per project, plus a LimitRange for per-container defaults and maximums, applied in each project
D. A NetworkPolicy that caps bandwidth per project, which also limits the CPU and memory its pods can use

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The two work together: the quota caps the project total, and the limit range both provides defaults and prevents a single pod from claiming the whole quota. Without a limit range, pods with no requests can make quota accounting behave unexpectedly.
</details>

---

### Question 10
**Scenario:** Traffic between projects must be restricted.

A. SCCs, which restrict which projects a pod's service account may open network connections to
B. It cannot be restricted, since the cluster network gives every pod a flat address space and all pods stay reachable
C. NetworkPolicy resources controlling ingress and egress by pod and namespace selector
D. Routes, since a route with an IP allowlist annotation blocks other projects from reaching the pods

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** By default all pods can talk to all pods, so isolation is opt-in through policy. A default-deny policy plus explicit allows is the standard pattern, and it depends on a network plugin that enforces policy.
</details>

---

### Question 11
**Scenario:** An application must be deployed from source code in a Git repository.

A. Build the image manually on a workstation each time, push it to the registry, and update the Deployment by hand
B. Copy the files into a running pod with oc rsync, which keeps the code after the pod restarts
C. Use a ConfigMap to hold the repository files, which OpenShift compiles into an image when the ConfigMap changes
D. A BuildConfig using source-to-image, which builds an image from the repository and can trigger on pushes

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Source-to-image is an OpenShift build strategy that turns source plus a builder image into a runnable image with no Dockerfile. Webhook triggers on the BuildConfig are what make it a pipeline rather than a one-off build.
</details>

---

### Question 12
**Scenario:** A deployment must be updated without downtime.

A. Delete all pods at once with oc delete pod --all, relying on the ReplicaSet to restore them
B. A rolling update, the default strategy, replacing pods gradually while keeping the application available
C. A Recreate strategy always, which stops old pods first and so keeps the service available during the change from start to finish
D. Scale the deployment to zero first, then back to the original count after the push

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Rolling updates respect max surge and max unavailable to keep capacity during the change, and readiness probes gate whether a new pod counts as available. Recreate is the alternative for applications that cannot run two versions at once, at the cost of a gap.
</details>

---

### Question 13
**Scenario:** Sensitive configuration such as a database password must be provided to a pod.

A. A ConfigMap, which is encrypted at rest by default and so is the standard object for passwords
B. A Secret mounted as a volume or injected as environment variables into the pod
C. A plain file committed to Git, referenced by the build so the pod can read it from the source tree
D. Hardcode it in the image at build time, so every pod started from that image has it without extra objects

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ConfigMaps are for non-sensitive configuration; Secrets are the object type for credentials. Secrets are only base64-encoded at rest by default, so encrypting etcd and controlling RBAC on secrets is what actually protects them.
</details>

---

### Question 14
**Scenario:** A node must be taken out of service for maintenance.

A. Cordon the node, then drain it so pods are evicted gracefully and reschedule elsewhere
B. Stop the kubelet service on the node, so the control plane moves the pods away
C. Power it off directly, since the scheduler moves workloads first
D. Delete the node object with oc delete node, which gracefully evicts every pod before removing it

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cordon plus drain is the safe sequence: cordon prevents new pods, drain moves the existing ones respecting pod disruption budgets. Powering off without draining causes an abrupt outage for everything on that node.
</details>

---

### Question 15
**Scenario:** A pod is stuck in `CrashLoopBackOff`. What is the diagnostic path?

A. Inspect events and logs with `oc describe pod` and `oc logs --previous`, then check probes, resource limits, and mounted config or secrets
B. Delete the project and redeploy, since a CrashLoopBackOff state is stored in the project and cannot be cleared otherwise
C. Increase the node size, because CrashLoopBackOff always means the node has run out of CPU and memory
D. Restart the cluster so the scheduler resets its backoff timers, which clears the pod's crash loop status

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** CrashLoopBackOff means the container starts and exits repeatedly, so the previous container's logs hold the reason. A failing liveness probe, a missing config or secret, or an out-of-memory kill are the usual causes, and describe surfaces the events that name them.
</details>

---

### Question 16
**Scenario:** A project has a ResourceQuota on CPU and memory. Developers' pods now fail to create because their containers declare no requests or limits.

A. Delete the ResourceQuota so pods without requests are accepted
B. Add a LimitRange that sets default requests and limits for containers
C. Grant the developers the `cluster-admin` role in the project
D. Add a NetworkPolicy that allows all traffic within the project

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** When a quota covers compute resources, every pod must declare requests and limits for them. A LimitRange fills in defaults for containers that omit them, so pods are admitted and still count against the quota. Deleting the quota removes the cap entirely. Admin rights and network policies have nothing to do with quota admission.

**Key Concept:** [Limit Ranges](https://kubernetes.io/docs/concepts/policy/limit-range/)
</details>

---

### Question 17
**Scenario:** Every new project created by users must automatically include a default NetworkPolicy and a ResourceQuota.

A. Write a cron job that scans for new projects and adds the objects
B. Ask each project owner to apply the objects after creating a project
C. Add the objects to the `default` project so others inherit them
D. Set a custom project request template in the cluster config

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The project request template (generated with `oc adm create-bootstrap-project-template`, created in `openshift-config`, and referenced in `projects.config.openshift.io/cluster`) defines the objects created with every new project. A cron job leaves a window with no policy and adds moving parts. Relying on owners is unreliable, and objects in the `default` project are not inherited by others.

**Key Concept:** [Configuring Project Creation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/building_applications/projects)
</details>

---

### Question 18
**Scenario:** Ordinary authenticated users must no longer be able to create their own projects; only administrators should create them.

A. `oc adm policy remove-cluster-role-from-group self-provisioner system:authenticated:oauth`
B. `oc adm policy remove-role-from-user admin system:authenticated -n default`
C. `oc delete project --all` and recreate projects as `kubeadmin`
D. `oc adm policy add-cluster-role-to-group view system:authenticated:oauth`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The `self-provisioner` cluster role is what lets users create projects, and it is bound to `system:authenticated:oauth` by default; removing that binding (and setting the binding's autoupdate annotation to false so it is not restored) disables self-provisioning. Removing a project-scoped admin role does not touch project creation. Deleting all projects is destructive, and adding `view` grants more rather than less.

**Key Concept:** [Disabling Project Self-Provisioning](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/building_applications/projects)
</details>

---

### Question 19
**Scenario:** Users `alice` and `bob` must be able to create and edit application resources in project `payments`, managed as a team rather than per user.

A. `oc adm policy add-cluster-role-to-user cluster-admin alice bob`
B. `oc adm policy add-role-to-user view alice bob -n payments`
C. `oc adm groups new payments-devs alice bob`, then `oc adm policy add-role-to-group edit payments-devs -n payments`
D. `oc adm groups new payments-devs alice bob`, then `oc adm policy add-role-to-group view payments-devs -n payments`

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A group plus a project-scoped `edit` role binding gives the team create and modify rights in that project only, and membership changes later without new bindings. `cluster-admin` grants control of the whole cluster. The `view` role, whether given per user or per group, is read-only and does not allow editing.

**Key Concept:** [Using RBAC to Define and Apply Permissions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/authentication_and_authorization/using-rbac)
</details>

---

### Question 20
**Scenario:** The cluster already authenticates users with an htpasswd identity provider. A new user, `carol`, must be added.

A. Run `oc create user carol` and set her password with `oc passwd`
B. Add carol to the htpasswd data in the `openshift-config` secret
C. Add carol to `/etc/passwd` on every control plane node
D. Create a new identity provider entry just for carol in the OAuth resource

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The htpasswd provider reads its users from a secret in `openshift-config`, so you extract the file, add the user with bcrypt hashing, and replace the secret's data; the OAuth pods pick up the change. `oc create user` creates a User object with no password, and there is no `oc passwd`. Node accounts are unrelated to OAuth, and one provider per user is not how identity providers work.

**Key Concept:** [Configuring Identity Providers](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/authentication_and_authorization/configuring-identity-providers)
</details>

---

### Question 21
**Scenario:** An operator must be installed from OperatorHub, but upgrades must never happen without an administrator approving them first.

A. Create a Subscription with `installPlanApproval: Manual` on the chosen channel
B. Create a Subscription with `installPlanApproval: Automatic` and watch the channel
C. Install the operator's CRDs by hand and skip OLM completely
D. Delete the operator's CatalogSource after the first install finishes

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** With manual approval, OLM creates an InstallPlan for each new version but waits until an administrator approves it. Automatic approval upgrades as soon as the channel moves. Installing CRDs by hand gives up lifecycle management, and deleting the CatalogSource breaks future updates rather than gating them.

**Key Concept:** [Operators: Administrator Tasks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/operators/administrator-tasks)
</details>

---

### Question 22
**Scenario:** Developers want Prometheus to scrape metrics from their own applications and to define alerts in their projects using the built-in monitoring stack.

A. Install a second Prometheus operator in each developer project
B. Grant every developer `cluster-admin` so they can edit the platform Prometheus
C. Edit the platform Prometheus pods directly to add the scrape targets
D. Set `enableUserWorkload: true` in the `cluster-monitoring-config` ConfigMap

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Monitoring for user-defined projects is enabled by setting `enableUserWorkload: true` in the `cluster-monitoring-config` ConfigMap in `openshift-monitoring`, after which ServiceMonitors and PrometheusRules in projects are used. Red Hat requires removing custom Prometheus instances, not adding more. `cluster-admin` for developers is excessive, and pod edits are reverted by the operator.

**Key Concept:** [Configuring User Workload Monitoring](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/monitoring/configuring-user-workload-monitoring)
</details>

---

### Question 23
**Scenario:** Red Hat Support asks for diagnostic data about the cluster's state for a support case.

A. `oc get all -A > cluster.txt`
B. `oc logs` for every pod, copied by hand
C. `oc adm must-gather`
D. `oc adm top nodes`

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `oc adm must-gather` runs a collection pod that gathers resource definitions, logs, and operator data into a local directory in the format Support expects. `oc get all` misses many resource types and all logs. Copying pod logs by hand is incomplete, and `oc adm top nodes` only shows current resource usage.

**Key Concept:** [Gathering Data About Your Cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/support/gathering-cluster-data)
</details>

---

### Question 24
**Scenario:** You need a root shell on worker node `worker-1` to inspect kubelet and CRI-O status. SSH to nodes is not configured.

A. `oc debug node/worker-1`, then `chroot /host`
B. `oc rsh node/worker-1` and run commands directly
C. `oc exec -it worker-1 -- /bin/bash`
D. `oc adm drain worker-1` to open a console session

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `oc debug node/` starts a privileged debug pod on the node with the host filesystem mounted at `/host`, and `chroot /host` gives you the node's own tools such as `systemctl` and `crictl`. `oc rsh` and `oc exec` work on pods, not nodes. `oc adm drain` evicts workloads and opens no shell.

**Key Concept:** [OpenShift CLI (oc)](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/cli_tools/openshift-cli-oc)
</details>

---

### Question 25
**Scenario:** Traffic must be encrypted from clients to the router and again from the router to the pods, which serve their own TLS certificate signed by an internal CA.

A. An edge route with the internal CA in the route's CA certificate field
B. A re-encrypt route with the internal CA as the destination CA certificate
C. A passthrough route with a custom certificate presented by the router
D. An unsecured route with TLS enabled only on the application pods

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A re-encrypt route terminates client TLS at the router, then opens a new TLS connection to the pod and validates its certificate using the destination CA. Edge termination sends plain HTTP to the pod. Passthrough never decrypts at the router, so the router presents no certificate of its own, and an unsecured route does not use TLS between client and router.

**Key Concept:** [Configuring Routes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html/networking/configuring-routes)
</details>

---

### Question 26
**Scenario:** A PostgreSQL service in the cluster must be reachable by clients outside the cluster on TCP port 5432. It is not HTTP and does not use TLS with SNI.

A. Create an edge route for the service on port 5432
B. Create a passthrough route for the service with a wildcard host
C. Add the service's ClusterIP to the external DNS zone
D. Expose it with a Service of type `LoadBalancer` or `NodePort`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Routes carry HTTP, HTTPS, and TLS traffic that uses SNI, so raw TCP protocols such as PostgreSQL need a `LoadBalancer` or `NodePort` service instead. An edge route expects HTTP, and passthrough relies on the TLS SNI header to pick the backend. A ClusterIP is only reachable from inside the cluster network.

**Key Concept:** [Kubernetes Services](https://kubernetes.io/docs/concepts/services-networking/service/)
</details>

---

### Question 27
**Scenario:** PVCs that do not name a storage class stay Pending. The cluster has a working storage class named `fast-csi`.

A. Rename `fast-csi` to `default` so PVCs find it
B. Create a PersistentVolume by hand for every claim
C. Annotate `fast-csi` with `storageclass.kubernetes.io/is-default-class: "true"`
D. Add `fast-csi` to the project's ResourceQuota

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A PVC with no `storageClassName` uses the cluster's default storage class, which is the class carrying the `is-default-class` annotation. The class name `default` has no special meaning. Hand-made PVs do not scale and still need matching, and a quota limits storage use rather than choosing a class.

**Key Concept:** [Change the Default StorageClass](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/)
</details>

---

### Question 28
**Scenario:** Deployment `web` must scale between 2 and 10 replicas to keep average CPU near 75% of its requests.

A. `oc autoscale deployment/web --min 2 --max 10 --cpu-percent 75`
B. `oc scale deployment/web --replicas 10`
C. `oc set resources deployment/web --limits cpu=75m`
D. `oc rollout restart deployment/web`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `oc autoscale` creates a HorizontalPodAutoscaler that adjusts replicas between the bounds based on CPU utilization measured against the pods' CPU requests, so the containers must declare requests. `oc scale` sets a fixed count. Setting a CPU limit caps each pod without scaling, and a rollout restart only recreates pods.

**Key Concept:** [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
</details>

---

### Question 29
**Scenario:** All pods in project `gpu-jobs` must run only on nodes labeled `accelerator=gpu`, without editing each deployment.

A. Add a toleration for `accelerator=gpu` to the project's service account
B. Cordon every node that lacks the GPU label
C. Set the project's `openshift.io/node-selector` annotation to `accelerator=gpu`
D. Add the label `accelerator=gpu` to the project itself

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A project node selector (the `openshift.io/node-selector` annotation on the namespace) is applied to every pod in the project, so they schedule only on matching nodes. Tolerations allow scheduling onto tainted nodes but do not force placement, and service accounts do not carry them. Cordoning blocks every other project too, and a label on the project does not affect scheduling.

**Key Concept:** [Controlling Pod Placement onto Nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/nodes/controlling-pod-placement-onto-nodes-scheduling)
</details>

---

### Question 30
**Scenario:** An identity provider is configured and a named user has been given `cluster-admin`. Security now requires removing the temporary `kubeadmin` login.

A. `oc delete user kubeadmin`
B. `oc delete secret kubeadmin -n kube-system`
C. `oc adm policy remove-cluster-role-from-user cluster-admin kubeadmin`
D. `oc delete identity kubeadmin`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `kubeadmin` is backed by the `kubeadmin` secret in `kube-system`, and deleting that secret removes the login. Do it only after another user has `cluster-admin`, because it cannot be undone. `kubeadmin` is not a User or Identity object, and its access does not come from an ordinary role binding, so the other commands do not remove it.

**Key Concept:** [Removing the kubeadmin User](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/authentication_and_authorization/removing-kubeadmin)
</details>

---

## Where to go deeper

- [EX280 cert page](../../exams/redhat/openshift-administrator-ex280/) - notes, practice plan, strategy
- [CKA practice questions](./kubernetes-cka.md) - the upstream Kubernetes counterpart
- [CKAD practice questions](./kubernetes-ckad.md) - the developer-focused sibling
- [Kubernetes in 10 minutes](../../learn/concepts/kubernetes-in-10-minutes.md) - plain-English foundation
- **[📖 Red Hat EX280](https://www.redhat.com/en/services/training/red-hat-certified-openshift-administrator-exam)** - official exam objectives
