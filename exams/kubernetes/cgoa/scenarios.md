---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 9 min
---

# CGOA High-Yield Scenarios

---

## Scenario 1: Is this GitOps?

**Scenario**: A team stores all Kubernetes manifests in Git. On merge to main, a GitHub Actions workflow authenticates to the cluster with a stored kubeconfig and runs `kubectl apply -f manifests/`. Manifests are declarative and every change is reviewed.

**Solution Pattern**:
- **Not GitOps.** It satisfies principles 1 (declarative) and 2 (versioned and immutable), and violates 3 and 4
- **Principle 3 violated**: the pipeline **pushes** to the cluster; no agent pulls
- **Principle 4 violated**: nothing reconciles between merges, so drift introduced by a manual `kubectl edit` persists indefinitely
- Secondary problem: cluster credentials live outside the cluster, in the CI system, which is the security cost of push-based delivery
- To convert: install an agent in the cluster, point it at the repository, and remove cluster credentials from CI

**Common Distractors**:
- "It is GitOps because manifests are in Git" (the state store is necessary, not sufficient)
- "It is GitOps because it is declarative" (one of four principles)
- "It becomes GitOps if the pipeline runs on a schedule" (still push, and scheduled reapplication is not continuous reconciliation by an in-cluster agent)

**Key Takeaway**: Check all four principles, not one. Push-based pipelines fail on pull and continuous reconciliation regardless of how good the rest is.

---

## Scenario 2: Environment modeling

**Scenario**: A platform team must manage dev, staging, and production for 40 services. They are choosing between a branch per environment and a directory per environment in one repository.

**Solution Pattern**:
- **Directory per environment** with a shared base and per-environment overlays (Kustomize) or values files (Helm)
- Promotion becomes an explicit, reviewable change to the target environment's directory, usually an image tag update
- Avoids the branch model's failure modes: long-lived branches diverge, cherry-picking becomes routine, and merges carry unintended changes between environments
- Access control per directory through CODEOWNERS, so production changes require different approvers
- Configuration differences are visible side by side rather than hidden in a diff between branches

**Common Distractors**:
- Branch per environment (intuitive, and the source of most GitOps repository pain in practice)
- One repository per environment (triples maintenance and makes shared bases hard)
- One repository per service per environment (120 repositories)

**Key Takeaway**: Directory per environment with overlays is the recommended pattern. The branch model looks natural to anyone from a feature-branch background and causes divergence and accidental promotion.

---

## Scenario 3: Secrets in the state store

**Scenario**: A team needs database credentials available to workloads. The config repository is internal but readable by all engineers, and they want GitOps to manage everything declaratively.

**Solution Pattern**:
Three valid families, chosen by context:
- **Sealed Secrets**: encrypt with a controller-held public key, commit the SealedSecret, only the in-cluster controller can decrypt. Simple, cluster-scoped keys, awkward for disaster recovery across clusters
- **SOPS** with age or a cloud KMS key: encrypt values in place, the agent decrypts at apply time. Good for multi-cluster, needs key distribution
- **External Secrets Operator**: commit only a reference; the operator fetches the value from Vault, AWS Secrets Manager, Azure Key Vault, or GCP Secret Manager at runtime. The value never enters the repository at all, and rotation happens outside Git

**Common Distractors**:
- Base64-encoded Secret manifests (base64 is encoding, not encryption; anyone with repo access has the credential)
- A private repository (access control is not confidentiality, and history is permanent)
- Applying secrets manually outside GitOps (breaks the model and creates permanent drift)

**Key Takeaway**: Encrypted values may be committed; plaintext and base64 may not. External Secrets is the strongest answer when rotation matters, because the secret never enters version history.

---

## Scenario 4: Drift that should not be corrected

**Scenario**: An agent is configured with self-heal enabled. A HorizontalPodAutoscaler scales a Deployment from 3 to 12 replicas under load. The agent immediately reverts the replica count to 3, the service degrades, and the HPA scales up again. The loop repeats.

**Solution Pattern**:
- The `replicas` field is legitimately owned by the HPA, not by the state store
- **Remove `replicas` from the committed manifest** so the agent does not manage that field, or
- Configure the agent to **ignore differences** on that specific field for that resource
- This is a general principle: a field with another legitimate controller must not also be declared in the desired state
- Other examples: fields mutated by admission webhooks, cloud-assigned load balancer IPs, and injected sidecar containers

**Common Distractors**:
- Disabling self-heal entirely (loses drift correction for everything else)
- Setting the manifest replicas to 12 (fixed value; the next scaling event repeats the fight)
- Removing the HPA (removes the capability rather than the conflict)

**Key Takeaway**: Only declare what you intend to own. Where another controller legitimately owns a field, remove it from the desired state or exclude it from comparison. This is the most practically useful pattern on the exam.

---

## Scenario 5: The CI and CD boundary

**Scenario**: A team asks where image tags should be updated. Their CI pipeline builds an image on every merge. They want the new image deployed to dev automatically and to production after approval.

**Solution Pattern**:
- **CI** builds, tests, scans, and pushes the image to a registry with an immutable tag, ideally a digest or a content-derived tag rather than `latest`
- The handover happens one of two ways:
  - CI **commits an image tag update** to the config repository's dev overlay, which the agent then reconciles
  - An **image update controller** in the cluster watches the registry and commits the change itself
- **Production promotion** is a separate, reviewed change to the production overlay, gated by approval through pull request review or an environment protection rule
- The state store remains the single source of truth for what is deployed where

**Common Distractors**:
- CI deploying directly to dev "because it is only dev" (two delivery models, and dev stops representing production behavior)
- Mutable tags such as `latest` (breaks immutability and makes rollback ambiguous)
- Committing the tag update into the application repository (triggers CI again; keep config separate)

**Key Takeaway**: CI ends at a published immutable artifact. GitOps begins at a commit to the state store. Promotion between environments is a commit, not a pipeline run.

---

## Scenario 6: Rollback

**Scenario**: A release causes elevated errors. The on-call engineer wants the fastest safe rollback.

**Solution Pattern**:
- **Revert the commit** in the state store. The agent reconciles the cluster back to the previous desired state
- This is auditable, reviewable, and leaves the state store accurate, which matters because the next reconciliation will apply whatever the store says
- Faster variants: `git revert` on a release commit, or moving an environment pointer to the previous known-good revision
- Never fix forward by editing the cluster directly. That creates drift, and the agent will undo it at the next reconciliation

**Common Distractors**:
- `kubectl rollout undo` (works momentarily, then the agent reverts it back to the bad state)
- Pausing the agent and fixing the cluster manually (buys time, leaves the store wrong, and is easy to forget)
- Re-running a previous CI pipeline (that is the push model's answer)

**Key Takeaway**: In GitOps, rollback is a state store operation. Any change made directly to the cluster is drift, and continuous reconciliation will erase it, which is exactly the behavior you asked for.

---

## Scenario 7: Multi-cluster at scale

**Scenario**: An organization runs 30 clusters across three regions and two clouds. Each needs a common baseline (policy, monitoring agents, ingress controller) plus per-cluster application sets.

**Solution Pattern**:
- **Hub-and-spoke**: a management cluster running the agent, or an agent per cluster pulling from a shared repository, depending on the tool and the isolation requirement
- **Templated generators** (Argo CD ApplicationSets, Flux Kustomization with substitution) to render the baseline across all clusters from one definition
- **Cluster metadata** driving per-cluster values: region, environment, cloud, size
- **Base plus overlay** so common configuration is defined once
- **Policy as code** with Kyverno or Gatekeeper to enforce the baseline regardless of what a cluster's manifests say
- Separate repositories or directories for platform baseline and application workloads, with different owners

**Common Distractors**:
- Thirty repositories, one per cluster (unmaintainable duplication)
- Copying the baseline into each cluster's directory (drifts the moment one is updated)
- One giant manifest set applied everywhere (no per-cluster variation)

**Key Takeaway**: At scale, generators plus base-and-overlay plus cluster metadata keep one definition serving many clusters. Duplication is the failure mode multi-cluster GitOps exists to avoid.

---

## Related

- [Practice plan](./practice-plan.md)
- [Strategy](./strategy.md)
- [Notes](./notes/)
- [CAPA](../capa/) - the Argo tooling that implements these patterns
- [Practice questions](../../../resources/practice-questions/cncf-cgoa.md)
