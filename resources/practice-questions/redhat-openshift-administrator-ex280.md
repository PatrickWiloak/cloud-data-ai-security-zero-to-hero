---
last-updated: 2026-08-09
difficulty: advanced
---

# Red Hat Certified Specialist in OpenShift Administration (EX280) - Practice Questions

15 questions on OpenShift administration: cluster and project management, authentication and RBAC, security context constraints, networking and routes, storage, and application deployment. EX280 is a hands-on performance exam, so these test the concepts you must be able to configure at the CLI.

> **Cert page:** [exams/redhat/openshift-administrator-ex280/](../../exams/redhat/openshift-administrator-ex280/)

---

### Question 1
**Scenario:** How does an OpenShift project relate to a Kubernetes namespace?

A. They are unrelated
B. A project is a Kubernetes namespace with additional annotations and access controls layered on top
C. A project is a cluster
D. A project is a pod

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Projects are the OpenShift wrapper around namespaces, adding self-service creation and per-project access. This is why you work with projects at the `oc` CLI while the underlying object remains a namespace.
</details>

---

### Question 2
**Scenario:** A new identity provider must be configured for user authentication.

A. Edit each user manually
B. Configure an identity provider in the cluster OAuth resource, such as HTPasswd, LDAP, or OIDC
C. Use the kubeadmin account permanently
D. Disable authentication

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OpenShift ships a built-in OAuth server, and identity providers are added to its configuration. The temporary kubeadmin user is meant to be removed once a real identity provider and a cluster administrator are established.
</details>

---

### Question 3
**Scenario:** A user must be able to view resources in a project but not modify them.

A. Cluster admin
B. Bind the `view` cluster role to the user in that project with a role binding
C. Give them edit
D. No binding needed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The default roles are `view`, `edit`, `admin`, and `cluster-admin`, and a role binding scopes the grant to one project. Using a cluster role binding instead would grant it across every project, which is the common over-grant mistake.
</details>

---

### Question 4
**Scenario:** A container image needs to run as a specific user ID but is blocked.

A. Run everything as root
B. Adjust the security context constraints: understand why the restricted SCC blocks it and grant an appropriate SCC to the workload's service account only if justified
C. Disable SCCs
D. Give the pod privileged access

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SCCs are OpenShift's distinctive security control, and the default restricted SCC assigns a random UID and blocks root, which breaks images that assume a fixed UID. The correct fix is a targeted SCC on the service account, not weakening security cluster-wide.
</details>

---

### Question 5
**Scenario:** Which SCC is the most restrictive and applied by default?

A. privileged
B. restricted (restricted-v2), which drops privileges, denies host access, and runs with an arbitrary non-root UID
C. anyuid
D. hostnetwork

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** restricted-v2 is the secure baseline that most workloads should run under. `anyuid` allows a fixed UID including root, and `privileged` removes nearly all isolation, so each is a deliberate escalation to justify rather than a default.
</details>

---

### Question 6
**Scenario:** An application must be reachable from outside the cluster over HTTP.

A. A ClusterIP service only
B. A Route, which exposes a service through the OpenShift router at a hostname, optionally with TLS termination
C. A host port
D. A NodePort always

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Routes are the OpenShift construct built on the ingress router and predate the Kubernetes Ingress they now coexist with. TLS termination modes (edge, passthrough, re-encrypt) are examinable, since the choice determines where certificates live.
</details>

---

### Question 7
**Scenario:** What is the difference between edge and passthrough TLS termination on a route?

A. They are the same
B. Edge terminates TLS at the router and sends plaintext to the pod; passthrough sends encrypted traffic straight to the pod, which terminates it
C. Passthrough terminates at the router
D. Edge does not use TLS

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Edge is simplest and centralizes certificates at the router; passthrough is required when the application must terminate TLS itself, for example for mutual TLS. Re-encrypt is the third mode, terminating at the router then re-encrypting to the pod.
</details>

---

### Question 8
**Scenario:** Persistent storage must be provided to a stateful application.

A. Use emptyDir
B. A PersistentVolumeClaim bound to a PersistentVolume, ideally through a StorageClass for dynamic provisioning
C. Store data in the container
D. A ConfigMap

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** emptyDir and container filesystems are ephemeral and lost on pod restart. The access mode matters for the design: ReadWriteOnce binds to one node, so a workload needing shared writable storage across nodes requires ReadWriteMany, which not every backend supports.
</details>

---

### Question 9
**Scenario:** Resource consumption in a project must be capped.

A. Nothing can limit it
B. A ResourceQuota to bound total consumption per project, and LimitRange to set per-pod and per-container defaults and maximums
C. Delete pods manually
D. A NetworkPolicy

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The two work together: the quota caps the project total, and the limit range both provides defaults and prevents a single pod from claiming the whole quota. Without a limit range, pods with no requests can make quota accounting behave unexpectedly.
</details>

---

### Question 10
**Scenario:** Traffic between projects must be restricted.

A. It cannot be restricted
B. NetworkPolicy resources controlling ingress and egress by pod selector and namespace, with the cluster network plugin enforcing them
C. SCCs
D. Routes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** By default all pods can talk to all pods, so isolation is opt-in through policy. A default-deny policy plus explicit allows is the standard pattern, and it depends on a network plugin that enforces policy.
</details>

---

### Question 11
**Scenario:** An application must be deployed from source code in a Git repository.

A. Build the image manually every time
B. A BuildConfig, for example source-to-image, that builds an image from source and can trigger on pushes, feeding a deployment
C. Copy files into a running pod
D. Use a ConfigMap

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Source-to-image is an OpenShift build strategy that turns source plus a builder image into a runnable image with no Dockerfile. Webhook triggers on the BuildConfig are what make it a pipeline rather than a one-off build.
</details>

---

### Question 12
**Scenario:** A deployment must be updated without downtime.

A. Delete and recreate all pods
B. A rolling update, the default deployment strategy, replacing pods gradually while maintaining availability
C. Scale to zero first
D. A recreate strategy always

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Rolling updates respect max surge and max unavailable to keep capacity during the change, and readiness probes gate whether a new pod counts as available. Recreate is the alternative for applications that cannot run two versions at once, at the cost of a gap.
</details>

---

### Question 13
**Scenario:** Sensitive configuration such as a database password must be provided to a pod.

A. Hardcode it in the image
B. A Secret mounted as a volume or injected as environment variables, referenced by the pod
C. A ConfigMap
D. A plain file in Git

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ConfigMaps are for non-sensitive configuration; Secrets are the object type for credentials. Secrets are only base64-encoded at rest by default, so encrypting etcd and controlling RBAC on secrets is what actually protects them.
</details>

---

### Question 14
**Scenario:** A node must be taken out of service for maintenance.

A. Power it off directly
B. Cordon the node to stop new scheduling, then drain it to evict pods gracefully so they reschedule elsewhere
C. Delete the node object
D. Stop the kubelet

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cordon plus drain is the safe sequence: cordon prevents new pods, drain moves the existing ones respecting pod disruption budgets. Powering off without draining causes an abrupt outage for everything on that node.
</details>

---

### Question 15
**Scenario:** A pod is stuck in `CrashLoopBackOff`. What is the diagnostic path?

A. Delete the project
B. Inspect events and logs: `oc describe pod`, `oc logs` including previous container logs, and check probes, resources, and configuration
C. Restart the cluster
D. Increase the node size

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CrashLoopBackOff means the container starts and exits repeatedly, so the previous container's logs hold the reason. A failing liveness probe, a missing config or secret, or an out-of-memory kill are the usual causes, and describe surfaces the events that name them.
</details>

---

## Where to go deeper

- [EX280 cert page](../../exams/redhat/openshift-administrator-ex280/) - notes, practice plan, strategy
- [CKA practice questions](./kubernetes-cka.md) - the upstream Kubernetes counterpart
- [CKAD practice questions](./kubernetes-ckad.md) - the developer-focused sibling
- [Kubernetes in 10 minutes](../../learn/concepts/kubernetes-in-10-minutes.md) - plain-English foundation
- **[📖 Red Hat EX280](https://www.redhat.com/en/services/certification/ex280)** - official exam objectives
