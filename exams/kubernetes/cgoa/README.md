---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 6 min
---

# Certified GitOps Associate (CGOA)

The vendor-neutral GitOps certification. CGOA tests whether you understand what GitOps actually is: the four OpenGitOps principles, the vocabulary, the repository and environment patterns, and where the model's edges are.

It is **not** an Argo CD exam. Tooling is 14% of the content. Candidates who prepare by learning Argo CD and skip the principles tend to fail.

## Exam Details

- **Exam Code:** CGOA
- **Duration:** 90 minutes
- **Questions:** 60, multiple choice and multiple select
- **Passing Score:** 75%
- **Cost:** USD 250, includes one free retake
- **Validity:** 2 years
- **Prerequisites:** None
- **Format:** Knowledge-based, not hands-on

Full detail in the [fact sheet](./fact-sheet.md).

## Domains

| Domain | Weight | Notes |
|--------|-------:|-------|
| GitOps Principles | 30% | [01](./notes/01-gitops-principles.md) |
| GitOps Terminology | 20% | [02](./notes/02-gitops-terminology.md) |
| GitOps Patterns | 20% | [03](./notes/03-gitops-patterns.md) |
| Related Practices | 16% | [04](./notes/04-related-practices-and-tooling.md) |
| Tooling | 14% | [04](./notes/04-related-practices-and-tooling.md) |

## The definition to memorize

The four **OpenGitOps** principles. The exam uses this wording, so learn it as written:

1. **Declarative** - a system managed by GitOps must have its desired state expressed declaratively.
2. **Versioned and immutable** - desired state is stored in a way that enforces immutability, versioning, and retains a complete version history.
3. **Pulled automatically** - software agents automatically pull the desired state declarations from the source.
4. **Continuously reconciled** - software agents continuously observe actual system state and attempt to apply the desired state.

Notice what the principles do **not** say. They do not say "Git". They do not say "Kubernetes". They do not say "Argo CD". The state store is commonly Git and the target is commonly Kubernetes, but the principles are broader, and the exam tests that distinction.

## The distinction the exam keeps testing

**Automation is not GitOps.** A pipeline that runs `kubectl apply` on every merge is automated, declarative, and version-controlled, and it is still not GitOps: it **pushes** rather than pulls, and it does nothing between runs, so drift persists undetected.

Any question describing a pipeline that pushes to a cluster is describing something that violates principles 3 and 4.

## Study sequence

1. **Principles** - read the OpenGitOps site directly, twice.
2. **Terminology** - the glossary. The exam is literal about these words.
3. **Patterns** - repository strategy, environments, promotion, secrets, drift policy.
4. **Related practices and tooling** - shallow breadth, no configuration depth needed.

Schedule in the [practice plan](./practice-plan.md).

## Hands-on

Not required, but one afternoon with a real agent makes the concepts concrete. Install Argo CD or Flux on a kind cluster and:

- Point it at a repository and watch initial sync
- Change a replica count with `kubectl edit`, then watch drift detection, and see the difference between self-heal on and off
- Revert a commit and watch the rollback happen without touching the cluster
- Add a Kustomize overlay for a second environment
- Try to store a plain Secret in the repository, then fix it properly with Sealed Secrets or the External Secrets Operator

## Study resources

- **[📖 OpenGitOps](https://opengitops.dev/)** - principles and glossary; the primary source
- **[📖 CGOA curriculum](https://github.com/cncf/curriculum)** - published domains
- **[📖 Argo CD documentation](https://argo-cd.readthedocs.io/)** - one reference implementation
- **[📖 Flux documentation](https://fluxcd.io/flux/)** - the other reference implementation
- **[📖 CNCF blog: how to ace the CGOA exam](https://www.cncf.io/blog/2024/10/30/how-to-ace-the-certified-gitops-associate-cgoa-exam/)** - candidate guidance
- [Practice questions](../../../resources/practice-questions/cncf-cgoa.md) - question bank in this repo

## Related

- [CAPA Certified Argo Project Associate](../capa/) - Argo tooling depth
- [CNPA Platform Engineering Associate](../cnpa/) - the platform layer GitOps sits inside
- [CKA](../cka/) - Kubernetes operations
- [CI/CD explained](../../../learn/concepts/cicd-explained.md)
- [Build a CI/CD pipeline](../../../resources/hands-on-projects/build-ci-cd-pipeline.md)
