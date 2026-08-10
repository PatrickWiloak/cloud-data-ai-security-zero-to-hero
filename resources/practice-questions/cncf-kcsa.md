---
last-updated: 2026-08-09
difficulty: intermediate
---

# Kubernetes and Cloud Native Security Associate (KCSA) - Practice Questions

15 questions for KCSA prep, weighted toward cluster component security (22%) and security fundamentals (22%), with the threat model and platform security at 16% each.

KCSA is knowledge-based multiple choice. It tests whether you can reason about Kubernetes threats, not whether you can type `kubectl` fast.

> **Cert page:** [exams/kubernetes/kcsa/](../../exams/kubernetes/kcsa/)

---

### Question 1
**Scenario:** The 4Cs of cloud native security, from outermost to innermost.

A. Cloud, Cluster, Container, Code
B. Code, Container, Cluster, Cloud
C. Compute, Cluster, Container, Code
D. Cloud, Compliance, Container, Code

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Each layer sits inside the one before it, and a weakness in an outer layer cannot be fixed by hardening an inner one. If the cloud account is compromised, container hardening does not save you. The model is useful precisely because it forces you to name the layer a control belongs to.
</details>

---

### Question 2
**Scenario:** Which component, if compromised, gives an attacker the broadest control of the cluster?

A. kube-proxy on one node
B. The API server
C. A single application pod
D. CoreDNS

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Every read and write to cluster state passes through the API server, and it holds the credentials and authorization decisions. Compromising it is effectively compromising the cluster. kube-proxy and CoreDNS are serious but scoped, and a single pod is the narrowest of the four.
</details>

---

### Question 3
**Scenario:** etcd is exposed on the network without client certificate authentication. What is the impact?

A. Slower API responses
B. Full read and write access to all cluster state, including secrets
C. Pods cannot schedule
D. Only metrics are exposed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** etcd holds every object, and secrets are stored there. Direct access bypasses the API server entirely, which means it bypasses RBAC, admission control, and audit logging. This is why etcd must use mutual TLS and be reachable only from the control plane.
</details>

---

### Question 4
**Scenario:** In the order the API server processes a request, what comes after authentication?

A. Admission control, then authorization
B. Authorization, then admission control
C. Validation, then authentication
D. Audit, then authorization

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The chain is authentication (who are you), authorization (may you do this), then admission control (mutating webhooks, then validating webhooks) before the object is persisted. Getting the order right matters: an admission policy cannot substitute for RBAC, because admission only sees requests that authorization already allowed.
</details>

---

### Question 5
**Scenario:** Which Kubernetes RBAC statement is true?

A. RBAC supports deny rules that override allows
B. RBAC is additive: permissions are granted only, and the union of all matching bindings applies
C. ClusterRoles can only be bound cluster-wide
D. A RoleBinding can grant permissions in any namespace

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** There is no deny rule in Kubernetes RBAC, so you reduce access by removing bindings, not by adding restrictions. A ClusterRole can be bound namespace-scoped with a RoleBinding, which is how the built-in `view` and `edit` roles get reused. A RoleBinding grants only within its own namespace.
</details>

---

### Question 6
**Scenario:** Which Pod Security Standard forbids running as root, requires seccomp `RuntimeDefault`, and drops all capabilities except `NET_BIND_SERVICE`?

A. Privileged
B. Baseline
C. Restricted
D. Default

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Restricted is the hardened profile and is the target for most application workloads. Baseline blocks known privilege escalations but permits running as root. Privileged is unrestricted. There is no profile called Default.
</details>

---

### Question 7
**Scenario:** A pod runs with `hostPID: true`. What does that enable?

A. Faster networking
B. Visibility of, and potential interaction with, all processes on the node
C. Access to host storage
D. A shared IP with the node

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Sharing the host PID namespace lets the container see every process on the node, which frequently exposes credentials in command lines and enables process manipulation. `hostNetwork` is the shared IP case and `hostPath` is host storage. All of these are blocked by the Baseline standard.
</details>

---

### Question 8
**Scenario:** Which threat does image signing and verification primarily address?

A. Denial of service
B. Running an artifact that is not the one your build produced
C. Excessive resource consumption
D. Weak passwords

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Signing binds an artifact to a producer and verification refuses anything unsigned or altered, which counters registry compromise, tag mutation, and typosquatted images. It says nothing about whether the signed image is free of vulnerabilities, which is what scanning is for.
</details>

---

### Question 9
**Scenario:** Where does a NetworkPolicy sit in the threat model?

A. It prevents an attacker gaining code execution in a pod
B. It limits lateral movement after a pod is compromised
C. It encrypts pod traffic
D. It authenticates services

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** NetworkPolicy is a segmentation control: it does not stop the initial compromise, it shrinks what the attacker can reach next. Encryption and service identity come from a mesh with mTLS. Understanding which stage of an attack a control affects is the core KCSA skill.
</details>

---

### Question 10
**Scenario:** Which is an example of a supply chain attack against a Kubernetes workload?

A. A brute-force login against the dashboard
B. A malicious dependency pulled during the image build
C. A misconfigured Service exposing a port
D. A node running out of memory

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Supply chain attacks compromise something upstream of your deployment: dependencies, base images, build systems, or registries. The other options are access control, misconfiguration, and capacity problems respectively. SBOMs, pinned digests, and provenance attestation are the countermeasures.
</details>

---

### Question 11
**Scenario:** A cluster must satisfy an external benchmark of hardening settings.

A. CIS Kubernetes Benchmark, checked with a tool such as kube-bench
B. The OWASP Top 10
C. SOC 2 Type I
D. PCI DSS

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The CIS Benchmark is the configuration-level standard for Kubernetes, and kube-bench automates checking it. OWASP is application-focused, while SOC 2 and PCI DSS are organizational compliance frameworks that may require hardening but do not specify Kubernetes flags.
</details>

---

### Question 12
**Scenario:** What does a "confused deputy" look like in a Kubernetes context?

A. Two controllers fighting over an object
B. A workload using a highly privileged service account to perform an action on behalf of a less privileged caller
C. A pod with no resource limits
D. A duplicate DNS record

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The deputy has authority the requester lacks and does not check whether the requester should have it. In clusters this appears as CI runners, operators, and dashboards with cluster-admin acting on user input. The fix is to bind actions to the caller's identity rather than the service's.
</details>

---

### Question 13
**Scenario:** Which is the best description of defense in depth applied to a cluster?

A. Choosing the single strongest control and relying on it
B. Layering independent controls so that failure of one does not grant full access
C. Encrypting everything
D. Blocking all inbound traffic

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The point is independence: RBAC, admission policy, network policy, runtime detection, and image provenance fail in different ways, so an attacker must defeat several. Relying on one control creates a single point of failure, and "encrypt everything" is one control among many.
</details>

---

### Question 14
**Scenario:** An organization wants to isolate tenants but keep one cluster. What is the honest assessment?

A. Namespaces alone provide strong tenant isolation
B. Namespaces plus RBAC, network policy, quotas, and Pod Security Standards give soft multi-tenancy; hard isolation needs separate clusters or sandboxed runtimes
C. Separate clusters offer no benefit
D. Isolation is a networking problem only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Soft multi-tenancy is achievable and common between cooperating teams. Between mutually untrusted tenants the shared kernel and shared control plane remain a real risk, so the answer is separate clusters, separate node pools, or a sandboxed runtime such as gVisor or Kata.
</details>

---

### Question 15
**Scenario:** What should be in place before an incident so you can reconstruct what an attacker did in the cluster?

A. Audit logging with a policy retaining sensitive-resource requests, shipped off-cluster
B. Dashboards showing CPU
C. A backup of etcd only
D. Verbose application logs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The API audit log is the record of who asked the API for what, and it must be shipped off the cluster so an attacker with node access cannot erase it. Metrics do not carry identity or intent, an etcd backup is a point-in-time snapshot rather than a history, and application logs miss control plane activity entirely.
</details>

---

## Where to go deeper

- [KCSA cert page](../../exams/kubernetes/kcsa/) - notes, practice plan, strategy
- [KCNA practice questions](./cncf-kcna.md) - the fundamentals sibling
- [CKS practice questions](./kubernetes-cks.md) - the hands-on security exam
- [AI threat modeling](../../learn/concepts/ai-threat-modeling.md) - the same reasoning applied to AI systems
- **[📖 Kubernetes security concepts](https://kubernetes.io/docs/concepts/security/)** - primary source
