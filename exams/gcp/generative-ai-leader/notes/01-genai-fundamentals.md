---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 8 min
---

# 01 - Generative AI fundamentals

---

## How the terms nest

**Artificial intelligence** contains **machine learning**, which contains **deep learning**, which contains **generative AI**. Generative AI produces new content: text, images, audio, video, or code.

**Discriminative** models classify or predict from existing data. **Generative** models produce new samples. A spam filter is discriminative; a model writing an email is generative.

---

## Foundation models

A **foundation model** is a large model pre-trained on broad data that can be adapted to many downstream tasks.

Why this changed the economics: previously, every task needed its own model, its own labeled dataset, and its own training run. A foundation model can be adapted with a prompt, which moves the cost of a new capability from months of ML work to an afternoon of prompt iteration.

Consequences the exam draws on:
- Building AI capability no longer requires an ML team for most use cases
- The bottleneck moves from model training to **data readiness**, integration, and evaluation
- The same model serves many use cases, which changes how you think about cost and governance

---

## How language models work

**Tokens** are the units of text a model processes, roughly a word or word fragment. Cost and limits are measured in tokens rather than words.

**Context window** is the maximum tokens a model can consider at once, covering the instructions, any supplied documents, the conversation, and the response. Larger windows allow more supplied context at higher cost.

**Embeddings** map text to vectors where semantic similarity is geometric closeness. This is what makes semantic search possible: a query about "logging in" can find a document about "authentication".

**Generation** is autoregressive: predict the next token, append it, repeat. This is why output is not deterministic by default, and why models can produce fluent text that is factually wrong.

---

## Multimodal models

A **multimodal** model accepts and produces more than one type of content. Gemini is multimodal across text, images, audio, video, and code.

Practically, this means one model can read a screenshot, a spreadsheet, and a paragraph of instructions together, which removes a class of preprocessing that used to require separate specialized models.

---

## Training stages

| Stage | What happens | Who does it |
|---|---|---|
| **Pre-training** | Learn language and world knowledge from a very large corpus | Model providers; enormously expensive |
| **Fine-tuning** | Further training on task-specific data to change behavior | You, when justified |
| **Instruction tuning** | Fine-tuning specifically to follow instructions | Providers, to produce a usable assistant |
| **Alignment** (RLHF and related) | Shaping outputs toward helpful and safe behavior | Providers |

---

## Hallucination

A **hallucination** is confident, plausible, incorrect output. It happens because the model predicts likely text rather than retrieving verified facts, and it is a property of how these models work rather than a bug to be patched.

Mitigations, in order of effectiveness:
- **Grounding**: supply authoritative source text and instruct the model to answer only from it
- **Citations**: require references so a human can verify
- **An escape hatch**: instruct the model to say when it does not know
- **Lower temperature** for factual tasks
- **Human review** where the cost of being wrong is high

**Knowledge cutoff** is a related limit: a model knows nothing after its training data ends, which is why grounding with search matters for current information.

---

## Agents

An **agent** is a model in a loop with **tools**. It decides what to do, calls a tool, reads the result, and continues until the task is complete. Tools might be a search index, a database, a booking API, or a calculation.

Agents extend what a model can do from "produce text" to "take action", which is where both the business value and the risk increase. An agent that can act needs bounded permissions and, for consequential actions, a human confirmation step.

---

## Limitations worth naming

- **Knowledge cutoff** - no awareness of events after training
- **Hallucination** - confident wrong answers
- **Reasoning limits** - multi-step logical and arithmetic reasoning remains imperfect
- **Non-determinism** - the same prompt can produce different output
- **Bias** - models reflect patterns in their training data
- **Context limits** - not everything fits in the window
- **Cost and latency** - larger and better models cost more and respond more slowly

Recognizing these is a business skill, because they determine which use cases are appropriate and where a human must stay in the loop.

---

## Key terms

- **Generative AI** - AI that produces new content rather than only classifying existing data
- **Foundation model** - a large model pre-trained on broad data and adaptable to many tasks
- **Token** - the unit of text a model processes, and the basis for cost and limits
- **Context window** - the maximum tokens a model can consider in one request
- **Embedding** - a vector representation of text where similarity corresponds to closeness
- **Multimodal model** - a model handling more than one content type, such as text and images
- **Pre-training** - the large-scale initial training that gives a model its general capability
- **Fine-tuning** - additional training on specific data to change a model's behavior
- **Instruction tuning** - fine-tuning that makes a model follow instructions reliably
- **Hallucination** - confident but incorrect model output
- **Grounding** - supplying authoritative sources so the model answers from them
- **Knowledge cutoff** - the point after which a model has no training data
- **Agent** - a model operating in a loop with tools to complete multi-step tasks
- **Non-determinism** - the property that the same prompt may produce different outputs

---

## Related

- [Notes 02: Google Cloud's generative AI offerings](./02-google-cloud-offerings.md)
- [LLM basics](../../../../learn/concepts/llm-basics.md)
