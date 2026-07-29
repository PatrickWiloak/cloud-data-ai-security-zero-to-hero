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
| [Implement zero-trust security](./implement-zero-trust.md) | 4-5 hours | Identity-aware access, no-implicit-trust networking |
| [Build a data pipeline](./build-data-pipeline.md) | 4-5 hours | Ingest → transform → load with scheduled runs |
| [Deploy an ML model](./deploy-ml-model.md) | 3-4 hours | Trained model behind an API endpoint |
| [Set up a Kubernetes cluster](./kubernetes-cluster-setup.md) | 4-5 hours | Production-shaped cluster, ingress, observability |
| [Build infra with Terraform](./terraform-infrastructure.md) | 3-4 hours | VPC + compute + DB declared as code, with state |
| [Build a serverless app](./serverless-application.md) | 3-4 hours | API + queue + function + storage, event-driven |
| [Run a DR drill](./disaster-recovery-drill.md) | 4-6 hours | Tested failover, measured RTO/RPO |

## AI builds (5)

| Build | Time | What you'll have at the end |
|---|---|---|
| [Build a RAG pipeline](./build-rag-pipeline.md) | ~30 min | Docs → chunks → pgvector → Claude with retrieval + evals |
| [Build a Claude agent with MCP](./build-claude-agent-with-mcp.md) | ~30 min | Agent SDK + custom MCP server reading files + SQLite |
| [Run Llama on a single GPU](./run-llama-on-single-gpu.md) | ~45 min | Open-weights model serving locally or on a cheap rented GPU |
| [Set up an eval harness](./set-up-eval-harness.md) | ~30 min | Reproducible eval suite for prompt and model comparisons |
| [Fine-tune with LoRA](./fine-tune-with-lora.md) | 1-2 hours | LoRA-trained small model, merged + served + benchmarked |

## How to pick

- **First-ever cloud build:** [Deploy a 3-tier app](./deploy-3-tier-app.md). Touches networking, compute, identity, and storage in one project.
- **First-ever AI build:** [Build a RAG pipeline](./build-rag-pipeline.md). Most hireable AI pattern in 2026.
- **Interview prep:** [Set up a Kubernetes cluster](./kubernetes-cluster-setup.md), [Build infra with Terraform](./terraform-infrastructure.md), [Build a CI/CD pipeline](./build-ci-cd-pipeline.md). These map to the most common practitioner questions.
- **Cheapest to run:** the five AI builds (under $5 each on rented GPUs); serverless and Terraform on the cloud side (free-tier friendly).
- **Most production-shaped:** [Implement zero-trust](./implement-zero-trust.md), [Run a DR drill](./disaster-recovery-drill.md), [Set up a monitoring stack](./setup-monitoring-stack.md).

## Related

- [Concepts](../../learn/concepts/) - the "why" behind each pattern
- [Architecture patterns](../architecture-patterns/) - reference designs each build follows
- [Topic indexes](../../topics/) - all four pillars per subject

## Which lab for which cert

Each lab maps to the certs it exercises. The reverse index lives in [labs-by-cert.md](./labs-by-cert.md).

<!-- BEGIN GENERATED: lab-cert-map - run .github/scripts/build-lab-map.py -->

| Lab | Certs it supports |
|------|-------------------|
| [Build a Claude agent with MCP](./build-claude-agent-with-mcp.md) | [CAD](../../exams/anthropic/claude-application-developer/), [AIP-C01](../../exams/aws/professional/genai-developer-aip-c01/), [NCP-AAI](../../exams/nvidia/agentic-ai-professional/) |
| [Build a RAG pipeline](./build-rag-pipeline.md) | [AIP-C01](../../exams/aws/professional/genai-developer-aip-c01/), [AIF-C01](../../exams/aws/foundational/ai-practitioner-aif-c01/), [AI-102](../../exams/azure/ai-102/), [Databricks Certified Generative AI Engineer Associate](../../exams/databricks/genai-engineer-associate/), [CCA-F](../../exams/anthropic/claude-certified-architect-foundations/) |
| [Fine-tune with LoRA](./fine-tune-with-lora.md) | [NCP-GENL](../../exams/nvidia/genai-llms-professional/), [Databricks Certified Machine Learning Professional](../../exams/databricks/ml-professional/), [DP-100](../../exams/azure/dp-100/) |
| [Hands-On Project: Build a CI/CD Pipeline](./build-ci-cd-pipeline.md) | [GitHub Actions Certification](../../exams/github/actions/), [AZ-400](../../exams/azure/az-400/), [DOP-C02](../../exams/aws/professional/devops-engineer-pro-dop-c02/), [Google Cloud Professional Cloud DevOps Engineer Certification](../../exams/gcp/cloud-devops-engineer/) |
| [Hands-On Project: Build a Data Pipeline](./build-data-pipeline.md) | [DEA-C01](../../exams/aws/associate/data-engineer-dea-c01/), [DP-203](../../exams/azure/dp-203/), [Professional Data Engineer](../../exams/gcp/data-engineer/), [Databricks Certified Data Engineer Associate](../../exams/databricks/data-engineer-associate/) |
| [Hands-On Project: Build a Serverless Application](./serverless-application.md) | [DVA-C02](../../exams/aws/associate/developer-dva-c02/), [AZ-204](../../exams/azure/az-204/), [Google Cloud Professional Cloud Developer Certification](../../exams/gcp/cloud-developer/) |
| [Hands-On Project: Build Infrastructure with Terraform](./terraform-infrastructure.md) | [Terraform Associate (003)](../../exams/hashicorp/terraform-associate/), [HashiCorp Terraform Authoring and Operations Professional Certification](../../exams/hashicorp/terraform-authoring-operations-pro/) |
| [Hands-On Project: Deploy a 3-Tier Application](./deploy-3-tier-app.md) | [SAA-C03](../../exams/aws/associate/solutions-architect-saa-c03/), [AZ-104](../../exams/azure/az-104/), [Associate Cloud Engineer](../../exams/gcp/cloud-engineer/), [CV0-004](../../exams/comptia/cloud-plus/) |
| [Hands-On Project: Deploy a Machine Learning Model](./deploy-ml-model.md) | [MLA-C01](../../exams/aws/associate/ml-engineer-mla-c01/), [DP-100](../../exams/azure/dp-100/), [Professional Machine Learning Engineer](../../exams/gcp/machine-learning-engineer/), [Databricks Certified Machine Learning Associate](../../exams/databricks/ml-associate/) |
| [Hands-On Project: Disaster Recovery Drill](./disaster-recovery-drill.md) | [SAP-C02](../../exams/aws/professional/solutions-architect-pro-sap-c02/), [AZ-305](../../exams/azure/az-305/), [Professional Cloud Architect](../../exams/gcp/cloud-architect/), [CV0-004](../../exams/comptia/cloud-plus/) |
| [Hands-On Project: Implement Zero Trust Security](./implement-zero-trust.md) | [CCSK v5 - Certificate of Cloud Security Knowledge](../../exams/cloud-security-alliance/ccsk/), [AZ-500](../../exams/azure/az-500/), [SCS-C02](../../exams/aws/specialty/security-scs-c02/), [Google Cloud Professional Cloud Security Engineer Certification](../../exams/gcp/cloud-security-engineer/), [CKS](../../exams/kubernetes/cks/) |
| [Hands-On Project: Set Up a Monitoring Stack](./setup-monitoring-stack.md) | [PCA](../../exams/kubernetes/pca/), [SOA-C03](../../exams/aws/associate/cloudops-engineer-soa-c03/), [Google Cloud Professional Cloud DevOps Engineer Certification](../../exams/gcp/cloud-devops-engineer/) |
| [Hands-On Project: Set Up a Production-Like Kubernetes Cluster](./kubernetes-cluster-setup.md) | [CKA](../../exams/kubernetes/cka/), [CKAD](../../exams/kubernetes/ckad/), [EX280](../../exams/redhat/openshift-administrator-ex280/) |
| [Run Llama on a single GPU](./run-llama-on-single-gpu.md) | [NCA-AIIO](../../exams/nvidia/ai-infrastructure-operations-associate/), [NCA-GENL](../../exams/nvidia/genai-llms-associate/) |
| [Set up an eval harness](./set-up-eval-harness.md) | [CPES](../../exams/anthropic/claude-prompt-engineering-specialist/), [AIP-C01](../../exams/aws/professional/genai-developer-aip-c01/), [Databricks Certified Generative AI Engineer Associate](../../exams/databricks/genai-engineer-associate/) |

<!-- END GENERATED: lab-cert-map -->
