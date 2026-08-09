---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 4 min
---

# OCI AI Foundations Study Strategy

## Calibrate to the exam

40 questions, 60 minutes, 65% to pass. That is 26 correct answers and 90 seconds per question. It is a recognition exam, not a reasoning exam.

The implication: breadth beats depth. Knowing what every OCI AI service does is worth more than understanding any one of them deeply.

## Two categories of question

**1. Concept definitions.** Textbook definitions of standard AI and ML terms. The exam is vendor-flavoured but the concepts are universal, so any solid ML introduction prepares you.

The pairs that recur:
- Supervised versus unsupervised versus reinforcement learning
- Classification versus regression
- Overfitting versus underfitting
- Precision versus recall
- Generative versus discriminative
- Pre-training versus fine-tuning
- Parameters versus hyperparameters

**2. Service selection.** "A company wants to do X. Which OCI service?" These are pure recall, and they are the fastest marks on the paper. Memorize the [service selection table](./fact-sheet.md#the-service-selection-table).

## The distinctions worth getting exactly right

**Precision versus recall.** Precision asks: of the things I flagged, how many were right? Recall asks: of the things I should have found, how many did I find? Fraud detection usually favours recall (missing fraud is worse than a false alarm); spam filtering usually favours precision (blocking real mail is worse than letting spam through). **Accuracy misleads on imbalanced data**: a model that always predicts "not fraud" on a dataset that is 99.9% legitimate scores 99.9% accuracy and is useless.

**Overfitting versus underfitting.** Overfitting means the model memorized the training data and performs badly on new data: high training accuracy, low test accuracy. Underfitting means it never learned the pattern: poor on both. Overfitting is addressed with more data, regularization, simpler models, or early stopping.

**Supervised versus unsupervised.** Supervised learning uses **labeled** data. Unsupervised finds structure in unlabeled data. If the scenario says "we have historical outcomes", it is supervised.

**Fine-tuning versus RAG.** Fine-tuning changes the model's **behavior** by further training. RAG changes what the model **knows for this request** by retrieving relevant text into the prompt. For "the model needs access to our internal documents", RAG is the answer.

## The OCI portfolio, organized

Group the services by layer, which makes recall easier than a flat list:

| Layer | Services | You provide |
|---|---|---|
| **Ready-made AI services** | Language, Speech, Vision, Document Understanding | Data; the model is pre-trained |
| **Generative AI** | OCI Generative AI, Generative AI Agents | Prompts, or documents for grounding |
| **ML platform** | OCI Data Science, Data Labeling | Your own model and code |
| **Infrastructure** | GPU shapes, bare metal, RDMA cluster networking | Everything; you run the stack |

The question "which layer" usually resolves the answer before you get to the specific service: if the scenario says "without machine learning expertise", it is a ready-made service; if it says "train a custom model", it is Data Science.

## Common traps

| Trap | Reality |
|---|---|
| Choosing Data Science for a pre-built capability | If a ready-made service does it, that is the answer |
| Assuming accuracy is always the right metric | Imbalanced data needs precision, recall, or F1 |
| Confusing parameters with hyperparameters | Parameters are learned; hyperparameters are set before training |
| Answering fine-tuning for a knowledge problem | Knowledge problems are RAG problems |
| Overthinking | This is a foundations exam; the textbook answer is correct |

## Exam day

- 60 minutes for 40 questions.
- 65% to pass, which is 26 correct. You can miss 14.
- Multiple choice, no penalty for guessing, leave nothing blank.
- Oracle re-versions the exam annually; make sure you booked the current code.

## After this

[OCI Generative AI Professional](../oci-generative-ai-professional/) is the direct next step and goes considerably deeper on LLM applications, RAG, and the OCI Generative AI service.

## Related

- [Practice plan](./practice-plan.md)
- [Fact sheet](./fact-sheet.md)
- [AI from scratch](../../../learn/ai-from-scratch.md)
- [Fine-tuning vs RAG](../../../learn/concepts/fine-tuning-vs-rag.md)
