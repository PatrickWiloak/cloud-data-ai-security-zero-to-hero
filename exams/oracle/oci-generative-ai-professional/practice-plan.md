---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 4 min
---

# OCI Generative AI Professional Study Plan

Five weeks at 5-6 hours per week, assuming [OCI AI Foundations](../oci-ai-foundations/) level knowledge going in.

## Week 1: LLM fundamentals

- [ ] Transformer architecture: attention, encoder and decoder variants
- [ ] Tokenization, and how tokens relate to cost and context limits
- [ ] Embeddings and what makes two texts similar in vector space
- [ ] Decoding parameters: temperature, top-k, top-p, penalties, max tokens, stop sequences
- [ ] Greedy decoding versus sampling, and the effect on reproducibility
- [ ] **Lab**: run the same prompt at temperature 0 and 1 in the playground and compare
- [ ] Review Notes: `notes/01-llm-fundamentals.md`

## Week 2: Prompting and customization

- [ ] Zero-shot, few-shot, chain-of-thought, system prompts
- [ ] Prompt injection at a conceptual level, and why it matters for a deployed application
- [ ] The customization spectrum: prompting, RAG, T-Few and LoRA fine-tuning, full fine-tuning, pre-training
- [ ] When fine-tuning is the right answer and when it is not
- [ ] Evaluation: loss, perplexity, held-out accuracy, LLM-as-judge
- [ ] **Lab**: compare zero-shot, few-shot, and chain-of-thought on the same reasoning task

## Week 3: The OCI Generative AI service

- [ ] Available models: chat and embedding, and their context limits
- [ ] On-demand inference versus dedicated AI clusters, and the billing difference
- [ ] Cluster sizing, hosting clusters versus fine-tuning clusters
- [ ] Creating a custom model and serving it through an endpoint
- [ ] Playground, API, SDK, and CLI
- [ ] Security: compartments, IAM policies, private endpoints, encryption, data isolation
- [ ] Content moderation, limits, and quotas
- [ ] OCI Generative AI Agents
- [ ] **Lab**: call the service from the playground and from the SDK; inspect the request parameters
- [ ] Review Notes: `notes/02-oci-generative-ai-service.md`

## Week 4: Building RAG applications

- [ ] RAG end to end: ingest, chunk, embed, store, retrieve, augment, generate
- [ ] Chunking strategy: size, overlap, and structure-aware splitting
- [ ] Embedding model choice and dimensionality
- [ ] Similarity metrics: cosine, dot product, Euclidean
- [ ] Vector stores, including AI Vector Search in Autonomous Database
- [ ] LangChain: models, prompts, chains, memory, retrievers, document loaders, output parsers
- [ ] Conversation memory and its effect on context and cost
- [ ] **Lab**: build a small RAG pipeline; change the chunk size and observe the effect
- [ ] Review Notes: `notes/03-building-llm-applications.md`

## Week 5: Evaluation, deployment, and review

- [ ] Evaluating retrieval quality separately from answer quality
- [ ] Observability, tracing, and cost management for LLM applications
- [ ] Deployment patterns on OCI and integration with other services
- [ ] Guardrails and content moderation in a production application
- [ ] Work every scenario in [scenarios.md](./scenarios.md)
- [ ] Two timed practice exams

## Readiness check

- [ ] Explain what temperature, top-k, and top-p each do, and which to change for determinism
- [ ] Choose between prompting, RAG, and fine-tuning for a given requirement, and justify it
- [ ] Explain when a dedicated AI cluster is required rather than on-demand
- [ ] Describe the full RAG pipeline in order
- [ ] Explain how chunk size affects retrieval quality in both directions
- [ ] Name three causes of poor RAG answers and say how you would diagnose each
- [ ] Explain how to evaluate a RAG system, distinguishing retrieval from generation
