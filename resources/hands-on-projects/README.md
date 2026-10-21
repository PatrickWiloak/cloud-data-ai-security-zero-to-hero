---
last-updated: 2026-05-03
---

# Hands-on projects

Fifteen guided builds: ten cloud, five AI. Each has an estimated time, a goal you can articulate to an interviewer, and inline code or commands. Most run on free-tier accounts; the AI builds list cheap cloud-GPU options where local hardware isn't enough.

## Cloud builds (10)

| Build | Time | What you'll have at the end |
|---|---|---|
| [Deploy a 3-tier app](./deploy-3-tier-app.md) | 3-4 hours | LB → app servers → DB on AWS, Azure, or GCP |
| [Build a CI/CD pipeline](./build-ci-cd-pipeline.md) | 4-5 hours | Auto-build, test, and deploy on commit |
| [Set up a monitoring stack](./setup-monitoring-stack.md) | 3-4 hours | Prometheus + Grafana + alertmanager wired end-to-end |
| [Implement zero-trust security](https://security.noblerworks.com/resources/hands-on-projects/implement-zero-trust/) | 4-5 hours | Identity-aware access, no-implicit-trust networking |
| [Build a data pipeline](https://data.noblerworks.com/resources/hands-on-projects/build-data-pipeline/) | 4-5 hours | Ingest → transform → load with scheduled runs |
| [Deploy an ML model](https://ai.noblerworks.com/build/projects/deploy-ml-model/) | 3-4 hours | Trained model behind an API endpoint |
| [Set up a Kubernetes cluster](./kubernetes-cluster-setup.md) | 4-5 hours | Production-shaped cluster, ingress, observability |
| [Build infra with Terraform](./terraform-infrastructure.md) | 3-4 hours | VPC + compute + DB declared as code, with state |
| [Build a serverless app](./serverless-application.md) | 3-4 hours | API + queue + function + storage, event-driven |
| [Run a DR drill](./disaster-recovery-drill.md) | 4-6 hours | Tested failover, measured RTO/RPO |

## AI builds (5)

| Build | Time | What you'll have at the end |
|---|---|---|
| [Build a RAG pipeline](https://ai.noblerworks.com/build/projects/build-rag-pipeline/) | ~30 min | Docs → chunks → pgvector → Claude with retrieval + evals |
| [Build a Claude agent with MCP](https://ai.noblerworks.com/build/projects/build-claude-agent-with-mcp/) | ~30 min | Agent SDK + custom MCP server reading files + SQLite |
| [Run Llama on a single GPU](https://ai.noblerworks.com/build/projects/run-llama-on-single-gpu/) | ~45 min | Open-weights model serving locally or on a cheap rented GPU |
| [Set up an eval harness](https://ai.noblerworks.com/build/projects/set-up-eval-harness/) | ~30 min | Reproducible eval suite for prompt and model comparisons |
| [Fine-tune with LoRA](https://ai.noblerworks.com/build/projects/fine-tune-with-lora/) | 1-2 hours | LoRA-trained small model, merged + served + benchmarked |

## How to pick

- **First-ever cloud build:** [Deploy a 3-tier app](./deploy-3-tier-app.md). Touches networking, compute, identity, and storage in one project.
- **First-ever AI build:** [Build a RAG pipeline](https://ai.noblerworks.com/build/projects/build-rag-pipeline/). Most hireable AI pattern in 2026.
- **Interview prep:** [Set up a Kubernetes cluster](./kubernetes-cluster-setup.md), [Build infra with Terraform](./terraform-infrastructure.md), [Build a CI/CD pipeline](./build-ci-cd-pipeline.md). These map to the most common practitioner questions.
- **Cheapest to run:** the five AI builds (under $5 each on rented GPUs); serverless and Terraform on the cloud side (free-tier friendly).
- **Most production-shaped:** [Implement zero-trust](https://security.noblerworks.com/resources/hands-on-projects/implement-zero-trust/), [Run a DR drill](./disaster-recovery-drill.md), [Set up a monitoring stack](./setup-monitoring-stack.md).

## Related

- [Concepts](../../learn/concepts/) - the "why" behind each pattern
- [Architecture patterns](../architecture-patterns/) - reference designs each build follows
- [Topic indexes](../../topics/) - all four pillars per subject

## Which lab for which cert

Each lab maps to the certs it exercises. The reverse index lives in [labs-by-cert.md](./labs-by-cert.md).

<!-- BEGIN GENERATED: lab-cert-map - run .github/scripts/build-lab-map.py -->

| Lab | Certs it supports |
|------|-------------------|
| [Hands-On Project: Build a CI/CD Pipeline](./build-ci-cd-pipeline.md) | [GitHub Actions Certification](../../exams/github/actions/), [AZ-400](../../exams/azure/az-400/), [DOP-C02](../../exams/aws/professional/devops-engineer-pro-dop-c02/), [Google Cloud Professional Cloud DevOps Engineer Certification](../../exams/gcp/cloud-devops-engineer/) |
| [Hands-On Project: Build a Serverless Application](./serverless-application.md) | [DVA-C02](../../exams/aws/associate/developer-dva-c02/), [AZ-204](../../exams/azure/az-204/), [Google Cloud Professional Cloud Developer Certification](../../exams/gcp/cloud-developer/) |
| [Hands-On Project: Build Infrastructure with Terraform](./terraform-infrastructure.md) | [Terraform Associate (003)](../../exams/hashicorp/terraform-associate/), [HashiCorp Terraform Authoring and Operations Professional Certification](../../exams/hashicorp/terraform-authoring-operations-pro/) |
| [Hands-On Project: Deploy a 3-Tier Application](./deploy-3-tier-app.md) | [SAA-C03](../../exams/aws/associate/solutions-architect-saa-c03/), [AZ-104](../../exams/azure/az-104/), [Associate Cloud Engineer](../../exams/gcp/cloud-engineer/), [CV0-004](../../exams/comptia/cloud-plus/) |
| [Hands-On Project: Disaster Recovery Drill](./disaster-recovery-drill.md) | [SAP-C02](../../exams/aws/professional/solutions-architect-pro-sap-c02/), [AZ-305](../../exams/azure/az-305/), [Professional Cloud Architect](../../exams/gcp/cloud-architect/), [CV0-004](../../exams/comptia/cloud-plus/) |
| [Hands-On Project: Set Up a Monitoring Stack](./setup-monitoring-stack.md) | [PCA](../../exams/kubernetes/pca/), [SOA-C03](../../exams/aws/associate/cloudops-engineer-soa-c03/), [Google Cloud Professional Cloud DevOps Engineer Certification](../../exams/gcp/cloud-devops-engineer/) |
| [Hands-On Project: Set Up a Production-Like Kubernetes Cluster](./kubernetes-cluster-setup.md) | [CKA](../../exams/kubernetes/cka/), [CKAD](../../exams/kubernetes/ckad/), [EX280](../../exams/redhat/openshift-administrator-ex280/) |

<!-- END GENERATED: lab-cert-map -->
