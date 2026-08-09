---
last-updated: 2026-08-09
difficulty: advanced
---

# Certified Kubernetes Security Specialist (CKS) - Practice Questions

15 questions for CKS prep, weighted toward the three 20% domains: minimizing microservice vulnerabilities, supply chain security, and runtime security.

CKS is performance-based and requires a valid CKA. These questions reinforce the reasoning; the exam tests whether you can implement it under time pressure.

> **Cert page:** [exams/kubernetes/cks/](../../exams/kubernetes/cks/)

---

### Question 1
**Scenario:** An auditor asks you to prove which service accounts can create pods in the `payments` namespace.

A. Read every RoleBinding manifest in git
B. `kubectl auth can-i --list --as=system:serviceaccount:payments:<sa> -n payments`
C. Check the audit log
D. Inspect the API server flags

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `kubectl auth can-i` asks the API server's authorizer directly, so it accounts for every Role, ClusterRole, and binding that applies, including ones nobody remembered. Reading manifests misses bindings created outside git. The audit log shows what was done, not what is permitted. API server flags tell you which authorization modes are on, not the effective permissions.
</details>

---

### Question 2
**Scenario:** A pod does not use the Kubernetes API at all, but its service account token is mounted by default.

A. Delete the default service account
B. Set `automountServiceAccountToken: false` on the pod spec or the service account
C. Add a NetworkPolicy blocking the API server
D. Set `runAsNonRoot: true`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An unused token is free credential material for an attacker who gets code execution in the container. Turning off automount is the direct fix and can be set per pod or defaulted on the service account. Deleting the default service account breaks pod admission. A NetworkPolicy is a coarser control and does not remove the credential. `runAsNonRoot` is unrelated.
</details>

---

### Question 3
**Scenario:** You need to restrict which syscalls a container can make, using a profile shipped with the node.

A. AppArmor annotation
B. `seccompProfile` with `type: Localhost` and a `localhostProfile` path
C. SELinux options
D. `capabilities.drop: ["ALL"]`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** seccomp filters syscalls, and `Localhost` loads a profile from the node's seccomp directory. `RuntimeDefault` is the easier baseline when you do not need a custom profile. AppArmor and SELinux are mandatory access control for file and capability access rather than syscall filtering. Dropping capabilities removes privileged operations but does not filter the syscall surface.
</details>

---

### Question 4
**Scenario:** Pod Security Admission is enabled. A namespace is labeled `pod-security.kubernetes.io/enforce: baseline` and `pod-security.kubernetes.io/audit: restricted`. A pod that violates `restricted` but satisfies `baseline` is applied.

A. Rejected
B. Admitted, with an audit annotation recorded
C. Admitted silently
D. Admitted with a warning to the user only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The three modes are independent. `enforce` decides admission, `audit` writes an annotation to the audit event, and `warn` returns a message to the client. Since only `baseline` is enforced the pod is admitted, and because `restricted` is set to audit the violation is recorded for review. This staged pattern is how teams migrate toward `restricted` without breaking workloads.
</details>

---

### Question 5
**Scenario:** You must ensure only images signed by your organization can run.

A. An ImagePullPolicy of `Always`
B. A validating admission webhook or policy engine that verifies signatures before admission
C. A private registry
D. `imagePullSecrets` on every pod

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Signature verification has to happen at admission, before the workload is created. Tools like Sigstore policy controllers, Kyverno, or OPA Gatekeeper enforce it. Pull policy controls caching. A private registry controls who can push, not whether what runs was signed. Pull secrets are authentication for the pull, not integrity of the artifact.
</details>

---

### Question 6
**Scenario:** `kube-bench` reports that the API server allows anonymous authentication.

A. Set `--anonymous-auth=false` on the API server
B. Add a NetworkPolicy in `kube-system`
C. Rotate the API server certificate
D. Enable audit logging

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Anonymous auth is an API server flag, and disabling it stops unauthenticated requests being mapped to `system:anonymous`. Be aware that some health endpoints and bootstrap flows rely on it, so verify the cluster still comes up. NetworkPolicies do not apply to the control plane's own listener. Certificate rotation and audit logging are worthwhile but address different findings.
</details>

---

### Question 7
**Scenario:** A container is compromised and the attacker attempts to write to `/etc`. You want the write to fail regardless of the process's UID.

A. `readOnlyRootFilesystem: true`
B. `runAsUser: 1000`
C. `allowPrivilegeEscalation: false`
D. A ResourceQuota

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A read-only root filesystem makes the whole image layer immutable at runtime, so writes fail even as root. Pair it with `emptyDir` mounts for the paths the app genuinely needs to write. Running as a non-root UID helps but a misconfigured directory could still be writable. Privilege escalation controls are orthogonal.
</details>

---

### Question 8
**Scenario:** You need runtime detection of a shell being spawned inside a production container.

A. `kubectl logs`
B. Falco with a rule matching shell execution in a container
C. Prometheus alerts on CPU
D. An admission webhook

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Falco reads kernel syscall events and alerts on behavior at runtime, which is exactly "a shell started where one should not." Logs only show what the application chose to print. CPU metrics are a weak proxy. Admission controls act at create time and cannot see what happens inside a running container.
</details>

---

### Question 9
**Scenario:** A default-deny egress NetworkPolicy is applied to a namespace and every pod immediately fails to resolve service names.

A. NetworkPolicies do not support egress
B. DNS was blocked; allow egress to kube-dns on UDP and TCP port 53
C. CoreDNS crashed
D. The CNI does not support the policy

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Default-deny egress blocks DNS along with everything else, and almost every workload resolves names before it connects. The fix is an explicit egress rule to the kube-dns pods or namespace on port 53, both UDP and TCP. This is the single most common self-inflicted outage when adopting egress policy.
</details>

---

### Question 10
**Scenario:** You want stronger workload isolation for an untrusted tenant than a shared kernel provides.

A. A separate namespace
B. A RuntimeClass backed by gVisor or Kata Containers
C. A PodDisruptionBudget
D. A dedicated ServiceAccount

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Namespaces are an API-level boundary, not a kernel boundary: pods in different namespaces still share the node's kernel. A RuntimeClass lets you schedule the workload onto a sandboxed runtime that intercepts syscalls (gVisor) or runs a lightweight VM (Kata). Service accounts and PDBs are unrelated to isolation.
</details>

---

### Question 11
**Scenario:** Secrets in etcd are stored unencrypted. What is the correct remediation?

A. Base64-encode the values twice
B. Configure an `EncryptionConfiguration` on the API server and re-write existing secrets
C. Move secrets to ConfigMaps
D. Restrict `kubectl get secrets` with RBAC

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Encryption at rest is an API server configuration pointing at a provider such as KMS or `aescbc`. The step teams forget is that enabling it does not re-encrypt existing data, so you must rewrite every secret (for example `kubectl get secrets -A -o json | kubectl replace -f -`). Base64 is encoding, not encryption. ConfigMaps are worse. RBAC is necessary but does not protect the etcd data files or backups.
</details>

---

### Question 12
**Scenario:** You want to reduce the attack surface of a container image before it ships.

A. Use a minimal or distroless base, run a vulnerability scan in CI, and fail the build on critical findings
B. Add a shell for debugging
C. Run the scan after deployment
D. Use `latest` tags so fixes arrive automatically

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Fewer packages means fewer CVEs, and gating the build turns scanning into a control rather than a report. Adding a shell expands the surface. Scanning after deployment finds problems too late. `latest` makes deployments unreproducible and can silently change what runs, which is a supply chain risk rather than a fix.
</details>

---

### Question 13
**Scenario:** Audit logging is enabled but every request is recorded at `RequestResponse` level and the log volume is unmanageable.

A. Disable audit logging
B. Write an audit policy with per-resource rules: `Metadata` for most traffic, `RequestResponse` only for sensitive resources such as secrets
C. Increase disk size
D. Sample the log randomly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The audit policy file matches rules in order and assigns a level per rule, so you keep full fidelity where it matters and drop to metadata elsewhere. Common practice is `None` for high-volume read traffic from system components. Disabling loses the control entirely, and random sampling destroys the evidentiary value of the log.
</details>

---

### Question 14
**Scenario:** A ServiceAccount token should be short-lived and audience-bound rather than a permanent secret.

A. Use a projected service account token volume with `audience` and `expirationSeconds`
B. Rotate the secret manually every month
C. Use a static token file on the API server
D. Use basic auth

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Projected tokens are issued by the TokenRequest API, expire, are bound to a specific audience, and are invalidated when the pod goes away. This is the default for the automounted token in modern clusters. Manual rotation is error-prone, and static token files and basic auth are deprecated mechanisms with no expiry at all.
</details>

---

### Question 15
**Scenario:** You need to confirm that a running cluster's node OS is not exposing the kubelet read-only port.

A. Check `--read-only-port=0` in the kubelet configuration and verify port 10255 is closed
B. Check the API server flags
C. Check the Service definitions
D. Check the CNI configuration

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The kubelet's read-only port 10255 serves unauthenticated pod and node information and should be disabled. It is a kubelet setting, not an API server one, and `kube-bench` flags it. Services and CNI configuration are not involved in exposing the kubelet.
</details>

---

## Where to go deeper

- [CKS cert page](../../exams/kubernetes/cks/) - notes, practice plan, strategy
- [KCSA practice questions](./cncf-kcsa.md) - the knowledge-based security counterpart
- [CKA practice questions](./kubernetes-cka.md) - the prerequisite
- [Kubernetes security guide](../../topics/kubernetes.md) - cross-pillar index
- **[📖 Kubernetes security documentation](https://kubernetes.io/docs/concepts/security/)** - allowed during the exam
