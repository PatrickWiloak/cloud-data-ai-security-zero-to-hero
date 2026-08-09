---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 8 min
---

# 03 - Techniques to improve generative AI output

---

## The cost and effort ladder

```
Prompt engineering  →  Grounding / RAG  →  Function calling  →  Fine-tuning
     cheapest                                                     most expensive
```

Work down it. Most quality problems are solved on the first two rungs, and the exam's wrong answers usually skip to the last.

---

## Prompt engineering

| Technique | What it is | Use when |
|---|---|---|
| **Zero-shot** | Instruction only | The task is simple and familiar to the model |
| **Few-shot** | Include worked examples | Output format or style needs demonstrating |
| **Chain-of-thought** | Ask for step-by-step reasoning before the answer | Multi-step reasoning or arithmetic |
| **System instructions** | Set role, tone, and constraints for the whole session | Consistent behavior across a conversation |
| **Role prompting** | "You are a financial analyst..." | Framing the perspective |

A well-structured prompt: clear role, explicit task, constraints, the input clearly delimited, and the required output format stated.

Few-shot prompting is often the cheapest large quality gain available, and it is the correct answer far more often than fine-tuning.

---

## Model parameters

| Parameter | Effect | Set it |
|---|---|---|
| **Temperature** | Randomness of token selection. Low is near-deterministic | Low for factual and extraction tasks, higher for creative ones |
| **Top-k** | Sample from the k most likely tokens | To constrain variety |
| **Top-p** | Sample from the smallest set of tokens reaching cumulative probability p | Usually preferred to top-k |
| **Output token limit** | Caps response length | For cost and latency control |
| **Safety settings** | Thresholds for filtering harmful content | Per application risk tolerance |

For "the answers vary too much between runs", the answer is **lower the temperature**.

---

## Grounding

**Grounding** connects the model to authoritative information so it answers from evidence rather than from memory.

Two forms on Google Cloud:
- **Grounding with Google Search** - for public, current information, addressing the knowledge cutoff
- **Grounding with your own data** - through Vertex AI Search or a vector store, for enterprise content

Grounding is the primary mitigation for **hallucination**, and it also enables **citations**, which let a human verify the answer.

---

## Retrieval-augmented generation

RAG is grounding on your own data, done systematically:

1. Split source documents into chunks
2. Embed each chunk and store the vectors
3. Embed the user's question and retrieve the most similar chunks
4. Place those chunks in the prompt with the question
5. Generate an answer from them, with citations

Why it usually beats fine-tuning for knowledge:
- Documents can be updated instantly; fine-tuned knowledge is frozen at training time
- Answers can cite sources
- Far cheaper
- Access control can be applied at retrieval time, per user

**The rule: knowledge problems are RAG problems; behavior problems are fine-tuning problems.**

---

## Function calling and extensions

**Function calling** lets a model request that your code be run: check inventory, look up an order, create a ticket, calculate a quote. The model produces a structured call; your application executes it and returns the result.

This is what turns an assistant that can only talk into one that can **do**, and it is the answer whenever a scenario requires live data or an action rather than information.

The business consideration the exam raises: an agent that can act needs bounded permissions and, for consequential actions, human confirmation. See [agent and tool security](../../../../resources/ai-security/agent-security.md) for the engineering treatment.

---

## Fine-tuning

Further training on your own examples to change **behavior**: tone, format, structure, or domain phrasing.

Appropriate when:
- Prompting and few-shot examples have been tried and are not enough
- The behavior must be consistent across very high volume, where a long prompt would be expensive
- You have a good, consistent dataset of examples

Inappropriate when:
- The requirement is knowledge, especially knowledge that changes
- The dataset is small or inconsistent
- Prompting has not been genuinely exhausted

**Parameter-efficient fine-tuning** trains a small set of additional weights rather than the whole model, making it far cheaper than full fine-tuning.

---

## Evaluation

You cannot manage what you do not measure, and the exam treats evaluation as a business discipline rather than a technical afterthought.

Approaches:
- **Automated metrics** against reference answers, where a correct answer exists
- **Model-based evaluation**, using a model to score outputs against criteria at scale
- **Human evaluation**, the ground truth for subjective quality
- **A/B testing** against the current process or an earlier version

Define success criteria **before** building. For a RAG application, evaluate **retrieval** and **answer quality** separately, because they fail for different reasons.

Track cost and latency alongside quality, because a system that is excellent and unaffordable is not shippable.

---

## Guardrails

- **Safety filters** on input and output, with configurable thresholds
- **Grounding and citation requirements** so claims are checkable
- **Human review** for high-stakes output
- **Scope limits** so the assistant declines topics outside its purpose
- **Monitoring** for drift in quality, cost, and refusal rate

---

## Key terms

- **Zero-shot prompting** - prompting with an instruction and no examples
- **Few-shot prompting** - including worked examples in the prompt, often the cheapest quality gain
- **Chain-of-thought prompting** - requesting step-by-step reasoning before the final answer
- **System instructions** - persistent instructions setting role, tone, and constraints for a session
- **Temperature** - the parameter controlling randomness in generation
- **Top-p** - sampling from the smallest set of tokens reaching a cumulative probability threshold
- **Grounding** - connecting a model to authoritative sources so it answers from evidence
- **Grounding with Google Search** - grounding on public, current web information
- **RAG** - retrieval-augmented generation, retrieving relevant enterprise content into the prompt
- **Function calling** - the mechanism by which a model requests that application code be executed
- **Parameter-efficient fine-tuning** - tuning a small set of added weights rather than the whole model
- **Model-based evaluation** - using a model to score outputs against defined criteria at scale
- **Safety filter** - configurable thresholds blocking harmful input or output
- **Human in the loop** - requiring human review or approval before a consequential output is acted on

---

## Related

- [Notes 04: business strategy](./04-business-strategy.md)
- [Fine-tuning vs RAG](../../../../learn/concepts/fine-tuning-vs-rag.md)
- [Evals for LLMs](../../../../learn/concepts/evals-for-llms.md)
