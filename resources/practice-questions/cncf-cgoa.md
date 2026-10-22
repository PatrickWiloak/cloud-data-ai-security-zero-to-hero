# Certified GitOps Associate (CGOA) - Practice Questions

30 questions for CGOA prep. Principles, terminology, and patterns are 70% of the exam; tooling is only 14%.

> **Cert page:** [exams/kubernetes/cgoa/](../../exams/kubernetes/cgoa/)

---

### Question 1
**Scenario:** A team stores all manifests in Git. On merge, a CI workflow authenticates with a stored kubeconfig and runs `kubectl apply`. Is this GitOps?

A. Yes, because manifests are declarative and version controlled, which are the only requirements
B. No: it violates the pulled-automatically and continuously-reconciled principles
C. Yes, if the pipeline also runs on a schedule so that drift is corrected between merges
D. No, because Kubernetes manifests are not a valid state store for a declarative desired state

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** It satisfies declarative and versioned-and-immutable but pushes rather than pulls, and does nothing between merges, so drift persists undetected. A scheduled pipeline is still push-based and still not an in-cluster agent reconciling continuously.
</details>

---

### Question 2
**Scenario:** Which of the following do the four OpenGitOps principles require?

A. Git specifically as the state store
B. A versioned, immutable state store with full history, whatever the technology
C. Automatic correction of all drift on every resource
D. Kubernetes as the target platform, because the principles are defined in terms of its API objects

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The principles say "stored in a way that enforces immutability, versioning, and retains a complete version history". They name neither Git nor Kubernetes. Principle four says agents observe and *attempt to apply*, so alerting on drift for some resources remains a valid policy choice.
</details>

---

### Question 3
**Scenario:** A platform team manages dev, staging, and production for 40 services. Which environment model is generally recommended?

A. One repository per service per environment, so 40 services give 120 repositories
B. Branch per environment, with promotion done by merging from dev toward production
C. One repository per environment, holding the manifests for all 40 services
D. Directory per environment with a shared base and overlays, so each promotion is an explicit, reviewable change

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Directories make configuration differences visible side by side, make promotion an explicit reviewable change, and support per-directory access control. Branches diverge over time and turn promotion into a merge exercise carrying unintended changes.
</details>

---

### Question 4
**Scenario:** An agent with self-heal enabled keeps reverting a Deployment's replica count from 12 to 3 while an HPA scales it back up.

A. Remove the HPA and manage capacity by editing the committed replica count by hand whenever load changes
B. Disable self-heal entirely, so the agent stops correcting any drift on any resource in the cluster
C. Remove `replicas` from the committed manifest, or have the agent ignore that field
D. Set the manifest replicas to 12, which matches the current value so the agent stops reverting it

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Only declare what you intend to own. Another legitimate controller owns that field, so declaring it creates a fight loop. Disabling self-heal loses drift correction everywhere else. A fixed value of 12 repeats the fight at the next scaling event.
</details>

---

### Question 5
**Scenario:** A team needs database credentials available to workloads. The config repository is readable by all engineers.

A. Base64-encode the Secret manifest and commit it, since base64 hides the value from readers
B. Apply the secret manually outside GitOps with kubectl, and keep the value out of the repository
C. Use Sealed Secrets, SOPS, or the External Secrets Operator
D. Make the repository private so that only the engineers who administer the cluster can read it

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Encrypted values may be committed; plaintext may not, and base64 is encoding rather than encryption. A private repository is access control, not confidentiality, and history is permanent. Manual application creates permanent drift and breaks the model.
</details>

---

### Question 6
**Scenario:** What is the correct rollback procedure in a GitOps model?

A. Revert the commit in the state store and let the agent reconcile the cluster back
B. `kubectl rollout undo` against the Deployment, which restores the previous ReplicaSet at once
C. Re-run the previous CI pipeline to push the older build
D. Pause the agent and fix the cluster by hand

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Any change made directly to the cluster is drift that the next reconciliation will erase. Reverting the state store is auditable, reviewable, and leaves the store accurate, which matters because the store is what the next reconciliation applies.
</details>

---

### Question 7
**Scenario:** Where does CI end and GitOps begin?

A. They are the same process, since each runs on every merge
B. CI deploys to dev and test environments; GitOps takes over only for the production environment, after sign-off
C. CI builds, tests, and publishes an artifact; GitOps starts at the config repository commit
D. GitOps replaces CI entirely, because the agent builds the images

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** GitOps is a continuous delivery approach; CI still builds and tests. The handover is a commit updating an image tag in the config repository, either made by CI or by an image update controller watching the registry.
</details>

---

### Question 8
**Scenario:** Which security property does the pull model provide that a push model does not?

A. Encrypted manifests, because the agent encrypts every file in the repository
B. Faster deployments, because the agent applies changes the moment a commit appears
C. No external system holds cluster credentials, and no inbound cluster access is required
D. Automatic secret rotation, because the agent regenerates every credential

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** In a push model a compromised CI system has full cluster access. In a pull model the agent uses in-cluster identity, so a compromised CI system can at most propose a commit, which is reviewable and revertable.
</details>

---

### Question 9
**Scenario:** What distinguishes continuous reconciliation from self-healing?

A. Reconciliation applies only to new resources, while existing resources are left alone once they have been created in the cluster
B. Nothing; they are synonyms, and every agent must automatically revert every drifted field it finds on any resource
C. Self-healing runs on a schedule and reconciliation does not
D. Reconciliation observes and attempts to apply; self-healing is the configurable behavior of correcting drift

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The principle mandates continuous observation and attempted application. Whether the agent automatically corrects a given resource, or alerts instead, is a design decision, and legitimate designs exclude fields another controller owns.
</details>

---

### Question 10
**Scenario:** Why is a mutable image tag such as `latest` discouraged in a GitOps state store?

A. It slows down image pulls, because the node must revalidate the tag with the registry each time the pod starts a container
B. Registries reject mutable tags, so a push to a tag name that already exists fails with an error in most registries
C. Agents cannot resolve it, because they only accept image digests and fail on any tag at all
D. It breaks immutability: one desired state can yield two different running systems, so rollback is ambiguous

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The second principle requires that a stored state be immutable. A tag that resolves to different bytes over time means the recorded desired state no longer identifies what actually runs, which defeats both reproducibility and rollback.
</details>

---

### Question 11
**Scenario:** Which is the recommended repository structure?

A. Separate application and configuration repositories
B. Manifests committed into the application source repository
C. One repository per environment per service
D. Manifests generated at deploy time and not stored in any repository

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Separation avoids the CI loop where a pipeline commits an image tag into the repository that triggers it, and allows different access controls and reviewers for code and for deployment configuration.
</details>

---

### Question 12
**Scenario:** An organization runs 30 clusters and needs a common baseline plus per-cluster application sets, without duplicating the baseline.

A. One manifest set applied identically everywhere, with the per-cluster differences handled by hand later on each cluster
B. Generators such as ApplicationSets driven by cluster metadata, over a shared base that every cluster inherits
C. Thirty repositories, one per cluster, each holding its own copy of the baseline and its apps
D. Copy the baseline into each cluster directory and update the copies whenever the baseline changes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Generators render one definition across many clusters using cluster metadata, which is the pattern that avoids duplication. Copying drifts the moment one copy is updated. A single identical manifest set allows no per-cluster variation.
</details>

---

### Question 13
**Scenario:** How does GitOps affect the DORA metric "time to restore service"?

A. It generally improves it, because rollback is a revert of the state store rather than a manual intervention
B. It worsens it, because every change must pass review before reaching the cluster
C. It affects only deployment frequency, because recovery is still manual
D. It has no effect, since recovery speed depends only on the on-call engineer

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Rollback becomes a single reviewed commit rather than a pipeline re-run or manual intervention, which shortens recovery. GitOps typically improves all four DORA metrics, which is a common exam framing for why organizations adopt it.
</details>

---

### Question 14
**Scenario:** Which safety net prevents a bad commit from deploying a non-compliant resource, given that the agent applies whatever is committed?

A. Policy as code enforced at admission, with Kyverno or OPA Gatekeeper
B. A longer reconciliation interval, so the agent has more time to catch the bad commit before applying
C. The agent's own validation, which blocks any resource that breaks the organization's compliance rules
D. Branch protection alone, with required reviewers on every merge into the main branch

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The agent faithfully applies the state store, so the enforcement point must be admission control, which everything reaching the cluster passes through. Branch protection helps but depends on reviewers noticing. A longer interval simply delays the bad apply.
</details>

---

### Question 15
**Scenario:** Which pair are both CNCF graduated GitOps agents implementing the same principles?

A. Argo CD with Jenkins X pipelines and plugins
B. Argo CD with the Flux project
C. Helm and Kustomize
D. Flux with Terraform Cloud workspaces

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Argo CD is application-centric with a strong UI; Flux is a set of composable controllers. Both are CNCF graduated and both implement the OpenGitOps principles. Helm and Kustomize compose manifests, Terraform is IaC, and Jenkins is a CI system.
</details>

---

### Question 16
**Scenario:** A team keeps its desired state as a single YAML file in an object storage bucket. Each change overwrites the file in place, with no history kept.

A. Declarative, because a YAML file overwritten in place no longer describes a desired state
B. Pulled automatically, because objects in a bucket cannot be fetched by an agent
C. Continuously reconciled, because overwriting the file stops the agent comparing states
D. Versioned and immutable, because the store keeps no history and allows changes in place

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The Versioned and Immutable principle requires desired state stored in a way that enforces immutability and versioning and keeps a complete version history. An overwritten file with no history fails it. The file is still declarative. Agents can pull from buckets. Reconciliation can still run; it just has no history to roll back to.
</details>

---

### Question 17
**Scenario:** A repository holds a shell script with a sequence of `helm upgrade` and `kubectl patch` commands that bring the system to the right state. Which principle does this miss?

A. Declarative, because it describes steps to perform rather than the desired end state
B. Versioned and immutable, because scripts cannot be stored in version control
C. Pulled automatically, because shell scripts can only run from a CI runner
D. Continuously reconciled, because scripts finish faster than reconciliation intervals

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Declarative principle requires the system's desired state to be expressed declaratively, as what should exist, not a procedure for getting there. A command sequence is imperative. Scripts can be version-controlled, and the other principles concern how state is fetched and reconciled, not the format.
</details>

---

### Question 18
**Scenario:** Under the OpenGitOps principles, how does desired state get from the state store into the running system?

A. A CI pipeline pushes it to the cluster after each merge, using credentials stored in CI
B. Software agents pull the desired state declarations from the source automatically
C. An operator applies it by hand after reviewing each change in the state store
D. The state store pushes it to every cluster through a webhook on each commit

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Pulled Automatically principle says software agents automatically pull the desired state declarations from the source. CI pushes and manual applies are push models. Webhooks can tell an agent to fetch sooner, but the agent still pulls, and the store does not push state into clusters.
</details>

---

### Question 19
**Scenario:** An agent applies new commits when they arrive but never compares the live system with the desired state between commits. Which principle is not fully met?

A. Declarative, because the agent applies the commits as they arrive
B. Versioned and immutable, because the agent only reads the latest commit
C. Continuously reconciled, because actual state is not observed between changes
D. Pulled automatically, because the agent applies commits on its own schedule

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The Continuously Reconciled principle requires agents to continuously observe actual system state and attempt to apply the desired state, which catches drift between commits. Applying on change only misses drift. The other principles are about the format, storage, and retrieval of desired state, which this agent satisfies.
</details>

---

### Question 20
**Scenario:** A team stores its desired state as signed, versioned OCI artifacts in a container registry instead of a Git repository. Can this still be GitOps?

A. No, because the principles require Git specifically, as the name of the practice suggests
B. No, because registries cannot be read by agents that continuously reconcile a cluster
C. Yes, but only if a CI pipeline copies each artifact back into a Git repository nightly
D. Yes, because the principles require a versioned, immutable state store, not Git itself

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** OpenGitOps describes a state store, which must be versioned and immutable with full history, and Git is the common example rather than a requirement. Agents such as Flux can pull from OCI repositories. Copying artifacts into Git is unnecessary.
</details>

---

### Question 21
**Scenario:** Someone scales a Deployment by hand with kubectl, so the live replica count no longer matches the desired state in the state store. What is this called?

A. Drift
B. Rollback
C. Promotion
D. Reconciliation

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Drift is any difference between the actual state of the system and the desired state. Reconciliation is the process that detects and corrects drift. Rollback returns to an earlier desired state. Promotion moves a change from one environment to the next.
</details>

---

### Question 22
**Scenario:** In GitOps terminology, what is the "desired state"?

A. The state the system was in at its most recent successful deployment, as reported by the cluster
B. The aggregate of all configuration data that is enough to recreate the system
C. The set of commands a CI pipeline runs to bring the system to its target configuration
D. The live configuration that the agent reads from the cluster at each reconciliation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OpenGitOps defines desired state as the aggregate of all configuration data that is sufficient to recreate the system so that its instances are indistinguishable in behavior. What the cluster reports is actual state. Commands are procedure, not state. Live configuration is what reconciliation compares against desired state.
</details>

---

### Question 23
**Scenario:** Which term describes the cycle in which an agent observes actual state, compares it with desired state, and acts to remove differences?

A. A promotion pipeline, which moves changes between environments
B. A blue-green deployment, which swaps traffic between versions
C. A reconciliation loop, which repeats observe, compare, and act
D. A merge queue, which orders commits before they reach the main branch

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Reconciliation is the repeated process of ensuring actual state matches desired state, by observing, diffing, and acting, and it runs continuously. Promotion pipelines and merge queues manage changes to desired state. Blue-green is a release strategy.
</details>

---

### Question 24
**Scenario:** A team wants new versions to receive a small share of traffic first and to be rolled back automatically if metrics degrade, while Git stays the source of truth.

A. Commit each traffic percentage to Git by hand every few minutes, then revert if alerts fire
B. Disable reconciliation during releases so that the team can shift traffic with kubectl
C. Deploy every version to all users at once, since GitOps does not allow partial releases
D. Progressive delivery with a controller such as Argo Rollouts or Flagger, declared in Git

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Progressive delivery controllers read a declared strategy (steps, weights, analysis) from the desired state and shift traffic and roll back automatically within the reconciled system. Manual commits for each percentage are slow and error-prone. Disabling reconciliation breaks GitOps. GitOps is fully compatible with partial releases.
</details>

---

### Question 25
**Scenario:** CI builds and pushes a new image. The team wants the new tag written into the state store automatically so that deployment still flows through Git.

A. Have CI run `kubectl set image` on the cluster right after the push
B. Use image update automation that commits the new tag to the repository
C. Use the `latest` tag so the cluster always pulls the newest image
D. Configure the agent to ignore image fields so CI can change them freely

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Image update automation, such as Flux's image automation controllers or Argo CD Image Updater with Git write-back, detects new tags and commits them to the repository, keeping Git as the record of what runs. `kubectl set image` bypasses the state store. `latest` is mutable and hides which version runs. Ignoring image fields gives up control of what is deployed.
</details>

---

### Question 26
**Scenario:** An organization compares one central management cluster whose agent deploys to 50 workload clusters with an agent installed in each workload cluster. What is a key trade-off?

A. Central agents cannot reconcile continuously, so drift is caught only on the next commit
B. Per-cluster agents cannot read from a shared repository, so each needs its own copy
C. Central management is easier to view but holds credentials to every cluster, a larger blast radius
D. Per-cluster agents require the clusters to push their state back to the management cluster

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A hub-and-spoke model gives one place to view and manage everything, but the hub holds credentials to all clusters and is a single point of failure. Per-cluster agents keep credentials local and keep reconciling if the hub is lost, at the cost of more agents to run. Central agents do reconcile continuously, and per-cluster agents can share repositories.
</details>

---

### Question 27
**Scenario:** A team wants cloud databases and buckets managed the same GitOps way as their Kubernetes applications, reconciled from Git.

A. Run Terraform from a laptop after each merge and commit the state file to Git
B. Create the resources by hand in the console and record them in a wiki page
C. Use a CI job that runs cloud CLI commands on a schedule to recreate everything
D. Use a Kubernetes-native controller such as Crossplane, with resources declared in Git

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Controllers such as Crossplane (or a Terraform controller) represent cloud resources as declarative Kubernetes objects that a GitOps agent syncs and that are continuously reconciled against the cloud. Laptop runs and scheduled CLI jobs are push-based and do not reconcile continuously. Console changes are not declarative or versioned.
</details>

---

### Question 28
**Scenario:** An attacker with write access to the repository could commit malicious manifests. The team wants the agent to apply only commits from trusted authors.

A. Require signed commits and configure the agent to verify signatures before applying
B. Make the repository private, which prevents any unauthorized commits being applied
C. Turn off self-heal, so that the agent stops applying commits from untrusted authors
D. Give the agent cluster-admin, so it can detect and refuse malicious manifests

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Signed commits, verified by the agent (both Flux and Argo CD support signature verification), mean only changes signed by trusted keys are applied. A private repository limits readers, but anyone with write access can still commit. Self-heal concerns drift correction, not author trust. More privilege for the agent increases risk.
</details>

---

### Question 29
**Scenario:** Several environments share the same base manifests and differ only by a few fields, such as replica counts and resource limits. The team wants plain YAML without a templating language.

A. Helm charts with a values file per environment
B. Kustomize with a base and per-environment overlays that patch fields
C. Jsonnet libraries that generate each environment's manifests
D. Copies of the full manifests for every environment, edited by hand

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Kustomize layers overlays that patch a base of plain YAML, with no templating language. Helm uses Go templates, and Jsonnet is a programming language. Full copies drift over time and multiply review work.
</details>

---

### Question 30
**Scenario:** In Flux, which controller fetches artifacts from Git repositories, Helm repositories, OCI registries, and buckets for the other controllers to use?

A. The kustomize-controller
B. The helm-controller
C. The notification-controller
D. The source-controller

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Flux's source-controller acquires artifacts from sources such as Git, Helm and OCI repositories, and buckets, and makes them available to the other controllers. The kustomize-controller and helm-controller reconcile Kustomizations and HelmReleases from those artifacts. The notification-controller handles events and alerts.
</details>

---

## Scoring guide

- **26-30 correct (85%+):** Ready. 75% is the pass mark.
- **20-25 correct (67-83%):** Re-read [opengitops.dev](https://opengitops.dev/) directly; the exam uses its exact vocabulary.
- **Below 20:** Work the [scenarios](../../exams/kubernetes/cgoa/scenarios.md), particularly the "is this GitOps" pattern.
