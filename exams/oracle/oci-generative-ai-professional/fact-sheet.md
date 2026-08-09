---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 10 min
---

# Oracle Cloud Infrastructure Generative AI Professional Fact Sheet

## Exam Overview

**Exam Code:** 1Z0-1127-25
**Exam Name:** Oracle Cloud Infrastructure Generative AI Professional
**Level:** Professional
**Duration:** 90 minutes
**Format:** Multiple choice
**Questions:** 60
**Passing Score:** 68%
**Cost:** USD 245 list price; Oracle periodically runs free certification windows
**Valid For:** Re-versioned annually, indicated by the year suffix in the exam code
**Delivery:** Oracle CertView, online proctored
**Prerequisites:** None formally; [OCI AI Foundations](../oci-ai-foundations/) and Python familiarity strongly recommended

> **Verify before booking.** Oracle re-versions this exam annually and the OCI Generative AI service changes quickly. Confirm the current exam code and objectives before building a study plan around this sheet.

**[📖 OCI Generative AI Professional](https://education.oracle.com/oracle-cloud-infrastructure-2025-generative-ai-professional/pexam_1Z0-1127-25)** - exam page and objectives
**[📖 OCI Generative AI documentation](https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm)** - service reference
**[📖 Oracle University free learning path](https://mylearn.oracle.com/)** - the official course, usually free

## What this exam covers

Three areas, roughly equal in weight:

1. **Fundamentals of large language models** - architecture, prompting, fine-tuning, decoding
2. **Using the OCI Generative AI service** - models, inference, dedicated clusters, custom models, security
3. **Building an LLM application** - RAG, LangChain, vector stores, deployment, and evaluation

It is a **builder's exam**. Where [OCI AI Foundations](../oci-ai-foundations/) asks what things are, this asks how you would assemble them, and expects familiarity with code-level concepts even though there is no coding on the exam itself.

## Target Audience

- Developers building generative AI applications on OCI
- Solution architects designing LLM systems
- Data scientists moving into LLM application work
- Anyone who has passed [OCI AI Foundations](../oci-ai-foundations/) and wants depth

## Exam Domains

### Fundamentals of large language models

**Key Concepts:**
- Transformer architecture, attention, encoder and decoder variants
- Tokenization and the relationship between tokens, cost, and context limits
- Embeddings, embedding models, and semantic similarity
- Decoding parameters: temperature, top-k, top-p (nucleus), frequency and presence penalties, max tokens, stop sequences
- Greedy decoding versus sampling, and the effect on determinism
- Prompt engineering: zero-shot, few-shot, chain-of-thought, system prompts
- Prompt injection and mitigation at a conceptual level
- Hallucination, grounding, and citation
- Model customization spectrum: prompting, RAG, parameter-efficient fine-tuning (T-Few, LoRA), full fine-tuning, pre-training
- Evaluation: loss, perplexity, accuracy on held-out sets, and LLM-as-judge

### Using the OCI Generative AI service

**Key Concepts:**
- Available foundation models: chat, embedding, and their context limits
- On-demand inference versus **dedicated AI clusters**, and when each is appropriate
- Cluster unit sizing, hosting versus fine-tuning clusters
- Custom model creation through fine-tuning, and the endpoint that serves it
- The playground, API, SDK, and CLI surfaces
- Security: compartments, IAM policy, private endpoints, encryption, customer data isolation
- Content moderation controls
- Monitoring, limits, and quotas
- OCI Generative AI Agents for retrieval-augmented agents over enterprise data

### Building, deploying, and evaluating LLM applications

**Key Concepts:**
- RAG architecture end to end: ingest, chunk, embed, store, retrieve, augment, generate
- Chunking strategy and its effect on retrieval quality
- Vector stores, including Oracle **AI Vector Search** in Autonomous Database
- Similarity metrics: cosine, dot product, Euclidean
- LangChain concepts: models, prompts, chains, memory, retrievers, document loaders, output parsers
- Conversation memory and its effect on context and cost
- Chatbot design patterns
- Evaluation of RAG: retrieval quality and answer quality
- Observability, tracing, and cost management
- Deployment on OCI and integration with other OCI services

## The customization decision

The most testable decision on the exam.

| Approach | Changes | Cost | Choose when |
|---|---|---|---|
| **Prompt engineering** | Nothing about the model | Lowest | Always start here |
| **Few-shot prompting** | Nothing; supplies examples in context | Low | The task needs demonstration, not new knowledge |
| **RAG** | What the model knows for this request | Low to medium | The model needs access to your data, which changes |
| **Fine-tuning (T-Few / LoRA)** | Model behavior, style, format adherence | Medium | Consistent tone or output format is required, and prompting is not enough |
| **Full fine-tuning** | All model weights | High | Rare; a large, stable, domain-specific dataset |
| **Pre-training** | Builds a model from scratch | Very high | Effectively never, outside model providers |

**Rule the exam applies: knowledge problems are RAG problems; behavior problems are fine-tuning problems.**

## Related repo material

- [Notes](./notes/) - three notes, one per area
- [Practice plan](./practice-plan.md) - 5-week schedule
- [Scenarios](./scenarios.md)
- [Strategy](./strategy.md)
- [OCI AI Foundations](../oci-ai-foundations/) - the prerequisite in practice
- [RAG explained](../../../learn/concepts/rag-explained.md), [Fine-tuning vs RAG](../../../learn/concepts/fine-tuning-vs-rag.md)
- [Build a RAG pipeline](../../../resources/hands-on-projects/build-rag-pipeline.md)
- [AI security](../../../resources/ai-security/) - the risks these applications carry
