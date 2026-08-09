---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 8 min
---

# 03 - Generative AI and large language models

---

## Generative versus discriminative

A **discriminative** model learns the boundary between classes: given an email, is it spam? A **generative** model learns the distribution of the data well enough to produce new samples from it: given a prompt, write an email.

**Large language models** are generative models trained on very large text corpora to predict the next token.

---

## How an LLM works

**Tokens** are the units the model processes: roughly a word or a word fragment. Text is tokenized on the way in and detokenized on the way out, and both cost and context limits are measured in tokens rather than words.

**Embeddings** map tokens (and larger spans of text) into high-dimensional vectors where semantic similarity corresponds to geometric closeness. This is what makes semantic search possible.

**Attention** lets the model weigh the relevance of every other token when processing each token, which is how it handles long-range dependencies. It is the mechanism at the heart of the transformer.

**Generation** is autoregressive: predict the next token, append it, repeat. **Temperature** controls randomness in that choice, with lower values more deterministic and higher values more varied.

---

## Training stages

| Stage | What happens | Cost |
|---|---|---|
| **Pre-training** | Learn language from a very large corpus by predicting the next token | Enormous; done by model providers |
| **Fine-tuning** | Further training on a smaller, task-specific dataset to change behavior | Moderate |
| **Instruction tuning** | Fine-tuning specifically to follow instructions | Part of producing a chat model |
| **RLHF** | Reinforcement learning from human feedback, aligning outputs to preferences | Done by providers |

**Parameter-efficient fine-tuning** methods such as **LoRA** train a small number of additional parameters rather than the whole model, which is far cheaper and is what OCI Generative AI's custom model support uses.

---

## Prompting

- **Zero-shot**: instruction only, no examples
- **Few-shot**: include a handful of worked examples in the prompt
- **Chain-of-thought**: ask the model to reason step by step before answering, which improves multi-step tasks
- **System prompt**: instructions setting role, tone, and constraints for the whole conversation

**Context window** is the maximum number of tokens the model can consider at once, covering the system prompt, the conversation, retrieved documents, and the response. Exceeding it means something must be dropped or summarized.

---

## Hallucination and grounding

**Hallucination** is confident, plausible, incorrect output. It happens because the model predicts likely text rather than retrieving verified facts.

Mitigations:
- **Grounding**: supply authoritative source text in the prompt and instruct the model to answer only from it
- **Citations**: require the answer to reference the supplied sources so a reader can check
- **Escape hatch**: instruct the model to say it does not know when the context lacks the answer
- **Lower temperature** for factual tasks
- **Human review** where the cost of being wrong is high

---

## Retrieval-augmented generation

RAG combines retrieval with generation:

1. **Index**: split source documents into chunks, embed each chunk, store the vectors
2. **Retrieve**: embed the user's question, find the most similar chunks
3. **Augment**: place those chunks in the prompt alongside the question
4. **Generate**: the model answers using the supplied context

Why it usually beats fine-tuning for knowledge: source documents can be updated instantly, answers can cite sources, it is far cheaper, and access control can be applied at retrieval time.

**Fine-tune to change behavior. Use RAG to change knowledge.**

**Vector databases** store embeddings and perform similarity search. In the Oracle ecosystem, **AI Vector Search** in Autonomous Database provides this natively, which means the vectors can live beside the relational data rather than in a separate system.

---

## Agents

An **agent** is an LLM in a loop with **tools**: it decides which tool to call, reads the result, and continues until the task is complete. Tools might be a search index, a database query, an API call, or a calculation.

**OCI Generative AI Agents** provides this as a managed service, with retrieval over enterprise data sources.

Agents introduce risks proportional to their permissions, which is the subject of the repo's [agent and tool security](../../../../resources/ai-security/agent-security.md) material.

---

## Key terms

- **Generative model** - a model that produces new content rather than only classifying existing content
- **Discriminative model** - a model that distinguishes between classes rather than generating data
- **Large language model** - a generative model trained on large text corpora to predict the next token
- **Token** - the unit of text a model processes, roughly a word or word fragment
- **Embedding** - a vector representation of text where semantic similarity corresponds to closeness
- **Attention** - the mechanism weighing the relevance of other tokens when processing each token
- **Temperature** - the parameter controlling randomness in token selection during generation
- **Context window** - the maximum number of tokens a model can consider in a single request
- **Pre-training** - the initial large-scale training that teaches a model language
- **Fine-tuning** - additional training on task-specific data to change model behavior
- **Instruction tuning** - fine-tuning specifically to make a model follow instructions
- **RLHF** - reinforcement learning from human feedback, used to align model outputs to preferences
- **LoRA** - a parameter-efficient fine-tuning method training a small set of additional weights
- **Zero-shot prompting** - prompting with an instruction and no examples
- **Few-shot prompting** - prompting with a small number of worked examples
- **Chain-of-thought prompting** - asking the model to reason step by step before answering
- **Hallucination** - confident but incorrect model output
- **Grounding** - supplying authoritative source text so the model answers from it rather than from memory
- **RAG** - retrieval-augmented generation, retrieving relevant text into the prompt before generating
- **Vector database** - a store for embeddings supporting similarity search
- **AI Vector Search** - Oracle Autonomous Database's native vector storage and similarity search capability
- **Agent** - an LLM operating in a loop with tools to complete a multi-step task

---

## Related

- [Notes 04: OCI AI services](./04-oci-ai-services.md)
- [RAG explained](../../../../learn/concepts/rag-explained.md)
- [Fine-tuning vs RAG](../../../../learn/concepts/fine-tuning-vs-rag.md)
