---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 10 min
---

# 01 - Large language model fundamentals

---

## Architecture

**Transformers** process a whole sequence in parallel using **attention**, which computes how relevant every other token is to each token. This replaced recurrent architectures because it removes the sequential bottleneck and handles long-range dependencies better.

Three variants:
- **Encoder-only** (BERT-style): produces representations. Used for classification and **embeddings**
- **Decoder-only** (GPT-style): predicts the next token. Used for generation. Most chat models
- **Encoder-decoder** (T5-style): reads an input and produces an output. Translation and summarization

---

## Tokens

Text is split into **tokens**, roughly a word or word fragment. Everything meaningful is measured in tokens:

- **Cost** is per input and output token, usually priced differently
- **Context window** is a token limit covering the system prompt, conversation, retrieved documents, and the response
- Token counts vary by language and by content; code and non-English text often tokenize less efficiently than English prose

---

## Embeddings

An **embedding** maps text to a vector where semantic similarity corresponds to geometric closeness. Two sentences meaning the same thing land near each other even with no shared words.

Similarity metrics:
- **Cosine similarity** - the angle between vectors, ignoring magnitude. The usual default for text
- **Dot product** - considers magnitude as well as direction
- **Euclidean distance** - straight-line distance

Practical points: the embedding model used to index documents must be the **same model** used to embed queries, and dimensionality affects both storage cost and retrieval quality.

---

## Decoding parameters

How the model chooses each next token. Directly testable.

| Parameter | What it does |
|---|---|
| **Temperature** | Scales the probability distribution. Near 0 selects the most likely token almost always; higher values flatten the distribution and increase variety |
| **Top-k** | Restricts sampling to the k most likely tokens |
| **Top-p (nucleus)** | Restricts sampling to the smallest set of tokens whose cumulative probability reaches p. Adapts to the distribution, so it is generally preferred to top-k |
| **Frequency penalty** | Reduces the probability of tokens in proportion to how often they have already appeared |
| **Presence penalty** | Reduces the probability of tokens that have appeared at all |
| **Max tokens** | Caps the length of the generated output |
| **Stop sequences** | Ends generation when a specified string is produced |

**Greedy decoding** always picks the highest-probability token, which is what temperature 0 approximates. **Sampling** introduces controlled randomness.

For extraction, classification, and any task feeding a downstream system, use **temperature 0**. For creative writing, raise it.

---

## Prompting

- **Zero-shot**: instruction only
- **Few-shot**: include worked examples, which is often the cheapest large quality gain
- **Chain-of-thought**: ask for step-by-step reasoning before the answer, which helps on multi-step problems
- **System prompt**: role, tone, and constraints applying to the whole conversation

Prompt structure that works: clear role, explicit task, the constraints, the input delimited unambiguously, and the required output format.

**Prompt injection** is the risk that text inside the input is treated as instruction. It matters here because a deployed application's prompt is assembled from user input, retrieved documents, and tool output, any of which an attacker may influence. See [prompt injection defense](../../../../resources/ai-security/prompt-injection-defense.md).

---

## The customization spectrum

| Approach | Changes | Relative cost | Fits |
|---|---|---|---|
| **Prompt engineering** | Nothing | Lowest | Always the starting point |
| **Few-shot prompting** | Nothing; supplies examples in context | Low | The task needs demonstration |
| **RAG** | What the model knows for this request | Low to medium | The model needs your data, especially changing data |
| **PEFT: T-Few, LoRA** | A small set of added parameters | Medium | Consistent behavior, tone, or format at scale |
| **Full fine-tuning** | All weights | High | Large, stable, domain-specific dataset |
| **Pre-training** | Builds a model from scratch | Very high | Effectively never outside model providers |

**T-Few** is the parameter-efficient fine-tuning method OCI Generative AI uses. It updates a fraction of the weights, which makes fine-tuning far cheaper and faster than full fine-tuning and reduces the amount of training data needed.

The decision rule the exam applies: **knowledge problems are RAG problems, behavior problems are fine-tuning problems.**

---

## Evaluation

- **Loss** and **perplexity** measure how well a model predicts held-out text during training. Lower perplexity means the model is less surprised by the data
- **Task accuracy** on a held-out set measures whether the model does the job
- **LLM-as-judge** uses a model to score outputs against criteria, which scales better than human review and needs its own validation
- **Human evaluation** remains the ground truth for subjective quality

For an application rather than a model, evaluate **retrieval quality** and **answer quality** separately, because they fail for different reasons and need different fixes.

---

## Key terms

- **Transformer** - the attention-based architecture underlying modern language models
- **Attention** - the mechanism computing the relevance of every token to every other token
- **Decoder-only model** - the generative architecture used by most chat models
- **Encoder-only model** - the architecture producing representations, used for embeddings and classification
- **Token** - the unit of text a model processes, the basis for cost and context limits
- **Context window** - the total token budget for a request, spanning prompt, history, retrieved text, and output
- **Embedding** - a vector representation of text where semantic similarity is geometric closeness
- **Cosine similarity** - the angle-based similarity metric commonly used for text embeddings
- **Temperature** - the decoding parameter scaling randomness in token selection
- **Top-k sampling** - restricting token selection to the k most probable candidates
- **Top-p sampling** - restricting token selection to the smallest set of tokens reaching cumulative probability p
- **Frequency penalty** - a decoding parameter discouraging tokens already used often
- **Presence penalty** - a decoding parameter discouraging tokens that have appeared at all
- **Greedy decoding** - always selecting the highest-probability token
- **Stop sequence** - a string that terminates generation when produced
- **Few-shot prompting** - including worked examples in the prompt to demonstrate the task
- **Chain-of-thought prompting** - requesting step-by-step reasoning before the final answer
- **T-Few** - the parameter-efficient fine-tuning method used by OCI Generative AI
- **LoRA** - low-rank adaptation, a parameter-efficient fine-tuning technique
- **Perplexity** - a measure of how well a model predicts held-out text, where lower is better
- **LLM-as-judge** - using a language model to evaluate the outputs of another model against criteria

---

## Related

- [Notes 02: the OCI Generative AI service](./02-oci-generative-ai-service.md)
- [LLM basics](../../../../learn/concepts/llm-basics.md)
- [Transformer architecture](../../../../learn/concepts/transformer-architecture.md)
