---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 5 min
---

# OCI Generative AI Professional Study Strategy

## Three decision axes

Most questions reduce to one of three decisions. Get these right and the exam is largely handled.

**1. Customization approach.** In order of preference:

```
Prompting  →  Few-shot  →  RAG  →  Fine-tuning (T-Few / LoRA)  →  Full fine-tuning
   cheap                                                              expensive
```

The rule: **knowledge problems are RAG problems, behavior problems are fine-tuning problems.**

- "The model does not know about our products" → RAG
- "The model will not consistently produce the JSON format we need" → try prompting and structured output first, then fine-tuning
- "The model must adopt our house tone across thousands of responses" → fine-tuning
- "Our documentation changes weekly" → RAG, because fine-tuned knowledge is frozen at training time

**2. On-demand or dedicated cluster.**

| | On-demand | Dedicated AI cluster |
|---|---|---|
| Billing | Per request, by tokens | Reserved capacity, by cluster unit hours |
| Throughput | Shared, variable | Predictable and isolated |
| Custom models | Not supported | **Required** |
| Fine-tuning | Not supported | **Required** |
| Fits | Development, spiky or low volume | Production with steady load, or any custom model |

Two things force a cluster: **fine-tuning** and **hosting a custom model**.

**3. Where retrieval quality comes from.** When a scenario says "the answers are wrong or irrelevant", the cause is usually retrieval, not the model. Check chunking, the embedding model, the number of chunks retrieved, and whether the right chunk was in the context at all.

## Decoding parameters

Directly testable, and easy marks.

| Parameter | Effect | Set it when |
|---|---|---|
| **Temperature** | Scales the randomness of token selection. 0 is near-deterministic | Low for factual and extraction tasks, higher for creative ones |
| **Top-k** | Sample only from the k most likely tokens | Constraining variety without going fully deterministic |
| **Top-p (nucleus)** | Sample from the smallest set of tokens whose cumulative probability reaches p | Usually preferred over top-k; adapts to the distribution |
| **Frequency penalty** | Reduces likelihood of tokens already used often | Repetition in long output |
| **Presence penalty** | Reduces likelihood of tokens that have appeared at all | Encouraging topic variety |
| **Max tokens** | Caps output length | Cost and latency control |
| **Stop sequences** | Ends generation at a marker | Structured output |

For reproducibility, set **temperature to 0**. That is the single most likely parameter question.

## Chunking

The lever with the largest effect on RAG quality.

- **Too small**: each chunk lacks context, so retrieval finds the right words but the model cannot ground itself
- **Too large**: the embedding represents too many ideas at once and becomes imprecise, and retrieved context wastes the window
- **Reasonable default**: a few hundred tokens with modest overlap, split on structural boundaries such as paragraphs or headings rather than at fixed character counts
- **Overlap** prevents information that straddles a boundary from being lost
- Carry **metadata** on each chunk: source document, section, and any access-control attributes

## Diagnosing a RAG application

The exam likes scenarios where answers are poor. Work down the pipeline:

1. **Was the right chunk retrieved at all?** Log the retrieved chunks. If not, it is a retrieval problem: chunking, embedding model, or query phrasing
2. **Was it in the prompt?** Context window truncation, or too many chunks retrieved
3. **Did the model use it?** If the right chunk was present and the answer ignored it, the prompt needs a stronger grounding instruction, or the chunk was buried among many others
4. **Is the model inventing?** Add an explicit escape hatch and require citations

## Common traps

| Trap | Reality |
|---|---|
| Fine-tuning to add knowledge | Fine-tuning changes behavior; RAG changes knowledge |
| Fine-tuning on frequently changing data | Frozen at training time; RAG updates instantly |
| Raising temperature to improve accuracy | Higher temperature increases variety, not correctness |
| Assuming on-demand can serve a custom model | Custom models require a dedicated AI cluster |
| Retrieving more chunks to fix bad answers | Often makes it worse by burying the relevant one |
| Ignoring chunk metadata | Provenance and access control both depend on it |
| Treating embeddings as anonymized | Source text can be substantially reconstructed from vectors |

## Exam day

- 90 minutes for 60 questions, 68% to pass, which is 41 correct.
- Multiple choice, no penalty for guessing.
- The service changes quickly; if a question describes a capability you do not recognize, answer from the principle rather than from memory of the console.
- Oracle re-versions annually, so confirm you registered for the current code.

## Related

- [Practice plan](./practice-plan.md)
- [Scenarios](./scenarios.md)
- [Fact sheet](./fact-sheet.md)
- [RAG explained](../../../learn/concepts/rag-explained.md)
- [Prompt injection defense](../../../resources/ai-security/prompt-injection-defense.md)
