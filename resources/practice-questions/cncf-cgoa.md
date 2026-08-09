# Certified GitOps Associate (CGOA) - Practice Questions

15 questions for CGOA prep. Principles, terminology, and patterns are 70% of the exam; tooling is only 14%.

> **Cert page:** [exams/kubernetes/cgoa/](../../exams/kubernetes/cgoa/)

---

### Question 1
**Scenario:** A team stores all manifests in Git. On merge, a CI workflow authenticates with a stored kubeconfig and runs `kubectl apply`. Is this GitOps?

A. Yes, because manifests are declarative and version controlled
B. No: it violates the pulled-automatically and continuously-reconciled principles
C. Yes, if the pipeline also runs on a schedule
D. No, because Kubernetes manifests are not a valid state store

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** It satisfies declarative and versioned-and-immutable but pushes rather than pulls, and does nothing between merges, so drift persists undetected. A scheduled pipeline is still push-based and still not an in-cluster agent reconciling continuously.
</details>

---

### Question 2
**Scenario:** Which of the following do the four OpenGitOps principles require?

A. Git specifically as the state store
B. Kubernetes as the target
C. A versioned, immutable state store, whatever the technology
D. Automatic correction of all drift

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The principles say "stored in a way that enforces immutability, versioning, and retains a complete version history". They name neither Git nor Kubernetes. Principle four says agents observe and *attempt to apply*, so alerting on drift for some resources remains a valid policy choice.
</details>

---

### Question 3
**Scenario:** A platform team manages dev, staging, and production for 40 services. Which environment model is generally recommended?

A. Branch per environment
B. Directory per environment with a shared base and overlays
C. One repository per environment
D. One repository per service per environment

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Directories make configuration differences visible side by side, make promotion an explicit reviewable change, and support per-directory access control. Branches diverge over time and turn promotion into a merge exercise carrying unintended changes.
</details>

---

### Question 4
**Scenario:** An agent with self-heal enabled keeps reverting a Deployment's replica count from 12 to 3 while an HPA scales it back up.

A. Disable self-heal entirely
B. Set the manifest replicas to 12
C. Remove `replicas` from the committed manifest, or configure the agent to ignore that field
D. Remove the HPA

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Only declare what you intend to own. Another legitimate controller owns that field, so declaring it creates a fight loop. Disabling self-heal loses drift correction everywhere else. A fixed value of 12 repeats the fight at the next scaling event.
</details>

---

### Question 5
**Scenario:** A team needs database credentials available to workloads. The config repository is readable by all engineers.

A. Base64-encode the Secret manifest and commit it
B. Make the repository private
C. Use Sealed Secrets, SOPS, or the External Secrets Operator
D. Apply the secret manually outside GitOps

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Encrypted values may be committed; plaintext may not, and base64 is encoding rather than encryption. A private repository is access control, not confidentiality, and history is permanent. Manual application creates permanent drift and breaks the model.
</details>

---

### Question 6
**Scenario:** What is the correct rollback procedure in a GitOps model?

A. `kubectl rollout undo`
B. Revert the commit in the state store and let the agent reconcile
C. Pause the agent and fix the cluster manually
D. Re-run the previous CI pipeline

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Any change made directly to the cluster is drift that the next reconciliation will erase. Reverting the state store is auditable, reviewable, and leaves the store accurate, which matters because the store is what the next reconciliation applies.
</details>

---

### Question 7
**Scenario:** Where does CI end and GitOps begin?

A. CI deploys to dev; GitOps handles production
B. CI builds, tests, and publishes an immutable artifact; GitOps begins at the commit to the config repository
C. GitOps replaces CI entirely
D. They are the same process

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** GitOps is a continuous delivery approach; CI still builds and tests. The handover is a commit updating an image tag in the config repository, either made by CI or by an image update controller watching the registry.
</details>

---

### Question 8
**Scenario:** Which security property does the pull model provide that a push model does not?

A. Encrypted manifests
B. No external system holds cluster credentials, and no inbound access to the cluster is required
C. Faster deployments
D. Automatic secret rotation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** In a push model a compromised CI system has full cluster access. In a pull model the agent uses in-cluster identity, so a compromised CI system can at most propose a commit, which is reviewable and revertable.
</details>

---

### Question 9
**Scenario:** What distinguishes continuous reconciliation from self-healing?

A. Nothing; they are synonyms
B. Reconciliation observes and attempts to apply; self-healing is the specific behavior of automatically correcting drift, which is configurable
C. Self-healing runs on a schedule and reconciliation does not
D. Reconciliation applies only to new resources

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The principle mandates continuous observation and attempted application. Whether the agent automatically corrects a given resource, or alerts instead, is a design decision, and legitimate designs exclude fields another controller owns.
</details>

---

### Question 10
**Scenario:** Why is a mutable image tag such as `latest` discouraged in a GitOps state store?

A. It slows down image pulls
B. It breaks immutability: the same desired state can produce two different running systems, and rollback becomes ambiguous
C. Registries reject it
D. Agents cannot resolve it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The second principle requires that a stored state be immutable. A tag that resolves to different bytes over time means the recorded desired state no longer identifies what actually runs, which defeats both reproducibility and rollback.
</details>

---

### Question 11
**Scenario:** Which is the recommended repository structure?

A. Manifests committed into the application source repository
B. Separate application and configuration repositories
C. One repository per environment per service
D. Manifests generated at deploy time and not stored

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Separation avoids the CI loop where a pipeline commits an image tag into the repository that triggers it, and allows different access controls and reviewers for code and for deployment configuration.
</details>

---

### Question 12
**Scenario:** An organization runs 30 clusters and needs a common baseline plus per-cluster application sets, without duplicating the baseline.

A. Thirty repositories, one per cluster
B. Copy the baseline into each cluster directory
C. Generators such as ApplicationSets or Kustomization substitution, driven by cluster metadata, over a shared base
D. One manifest set applied identically everywhere

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Generators render one definition across many clusters using cluster metadata, which is the pattern that avoids duplication. Copying drifts the moment one copy is updated. A single identical manifest set allows no per-cluster variation.
</details>

---

### Question 13
**Scenario:** How does GitOps affect the DORA metric "time to restore service"?

A. It has no effect
B. It generally improves it, because rollback is a revert of the state store
C. It worsens it, because changes require review
D. It affects only deployment frequency

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Rollback becomes a single reviewed commit rather than a pipeline re-run or manual intervention, which shortens recovery. GitOps typically improves all four DORA metrics, which is a common exam framing for why organizations adopt it.
</details>

---

### Question 14
**Scenario:** Which safety net prevents a bad commit from deploying a non-compliant resource, given that the agent applies whatever is committed?

A. Branch protection alone
B. Policy as code enforced at admission, with Kyverno or OPA Gatekeeper
C. The agent's own validation
D. A longer reconciliation interval

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The agent faithfully applies the state store, so the enforcement point must be admission control, which everything reaching the cluster passes through. Branch protection helps but depends on reviewers noticing. A longer interval simply delays the bad apply.
</details>

---

### Question 15
**Scenario:** Which pair are both CNCF graduated GitOps agents implementing the same principles?

A. Argo CD and Jenkins
B. Argo CD and Flux
C. Flux and Terraform
D. Helm and Kustomize

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Argo CD is application-centric with a strong UI; Flux is a set of composable controllers. Both are CNCF graduated and both implement the OpenGitOps principles. Helm and Kustomize compose manifests, Terraform is IaC, and Jenkins is a CI system.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready. 75% is the pass mark.
- **10-12 correct (65-80%):** Re-read [opengitops.dev](https://opengitops.dev/) directly; the exam uses its exact vocabulary.
- **Below 10:** Work the [scenarios](../../exams/kubernetes/cgoa/scenarios.md), particularly the "is this GitOps" pattern.
