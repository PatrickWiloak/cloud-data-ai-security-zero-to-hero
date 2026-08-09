---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 5 min
---

# OCI Generative AI Professional (1Z0-1127-25)

Building generative AI applications on Oracle Cloud Infrastructure: LLM fundamentals, the OCI Generative AI service, and RAG applications with LangChain and vector search.

Together with [OCI AI Foundations](../oci-ai-foundations/), this closes the gap where the repo carried five Oracle certifications and no Oracle AI ones.

## Exam Details

- **Exam Code:** 1Z0-1127-25
- **Duration:** 90 minutes
- **Questions:** 60, multiple choice
- **Passing Score:** 68%
- **Cost:** USD 245 list; free certification windows appear periodically
- **Prerequisites:** None formal; AI Foundations and Python familiarity recommended

Full detail in the [fact sheet](./fact-sheet.md).

## Notes

| Notes | Covers |
|---|---|
| [01 LLM fundamentals](./notes/01-llm-fundamentals.md) | Transformers, tokens, decoding parameters, prompting, customization spectrum |
| [02 The OCI Generative AI service](./notes/02-oci-generative-ai-service.md) | Models, on-demand versus dedicated clusters, fine-tuning, security |
| [03 Building LLM applications](./notes/03-building-llm-applications.md) | RAG, chunking, vector search, LangChain, evaluation, deployment |

## The three decisions the exam keeps testing

**1. How to customize a model.** Prompting, then RAG, then fine-tuning, in that order of preference. Knowledge problems are RAG problems; behavior and format problems are fine-tuning problems. An answer that reaches for fine-tuning to give a model access to company documents is wrong.

**2. On-demand or dedicated cluster.** On-demand for variable, low-volume, or experimental workloads, billed per use. Dedicated AI clusters for predictable throughput, isolation, and any custom fine-tuned model, billed for the reserved capacity. Fine-tuning itself requires a cluster.

**3. Where retrieval quality comes from.** Chunking strategy, embedding model choice, similarity metric, and how many chunks you retrieve. Most "the answers are bad" scenarios are retrieval problems rather than model problems.

## Hands-on

An OCI free tier account plus the Generative AI playground covers most of this. Worth doing:

- Run the same prompt at temperature 0 and temperature 1 and compare determinism
- Compare zero-shot, few-shot, and chain-of-thought on a reasoning task
- Generate embeddings and compute cosine similarity between related and unrelated sentences
- Build a small RAG pipeline: chunk a document set, embed, store, retrieve, and answer
- Change the chunk size and observe the effect on answer quality
- Set up an OCI Generative AI Agent over a document store

## Study resources

- **[📖 OCI Generative AI documentation](https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm)** - the primary source
- **[📖 Oracle University learning path](https://mylearn.oracle.com/)** - the official course
- **[📖 LangChain documentation](https://python.langchain.com/docs/introduction/)** - the framework the exam references
- [Build a RAG pipeline](../../../resources/hands-on-projects/build-rag-pipeline.md) - a worked build in this repo
- [Practice questions](../../../resources/practice-questions/oracle-oci-generative-ai-professional.md) - question bank in this repo

## Related

- [OCI AI Foundations](../oci-ai-foundations/) - the tier below
- [AWS GenAI Developer Professional](../../aws/professional/genai-developer-aip-c01/) - the AWS equivalent
- [Azure AI-102](../../azure/ai-102/) - the Azure equivalent
- [Databricks GenAI Engineer Associate](../../databricks/genai-engineer-associate/)
- [AI security](../../../resources/ai-security/) - securing what you build here
- [AI/ML Engineer roadmap](../../../resources/certification-roadmap-ai-ml-engineer.md)
