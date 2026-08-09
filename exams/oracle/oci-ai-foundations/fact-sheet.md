---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 9 min
---

# Oracle Cloud Infrastructure AI Foundations Associate Fact Sheet

## Exam Overview

**Exam Code:** 1Z0-1122-25
**Exam Name:** Oracle Cloud Infrastructure AI Foundations Associate
**Level:** Foundational
**Duration:** 60 minutes
**Format:** Multiple choice
**Questions:** 40
**Passing Score:** 65%
**Cost:** USD 245 list price; Oracle frequently runs free certification periods for its AI and OCI foundations exams
**Valid For:** Oracle refreshes these annually with a year suffix in the exam code
**Delivery:** Oracle CertView, online proctored
**Prerequisites:** None

> **Verify before booking.** Oracle re-versions these exams every year (the `-25` suffix), and free certification promotions come and go. Confirm the current exam code, price, and whether a free window is open before you register.

**[📖 Oracle Cloud Infrastructure AI Foundations Associate](https://education.oracle.com/oracle-cloud-infrastructure-ai-foundations-associate/trackp_OCIAIF)** - exam page and preparation track
**[📖 Oracle University free AI learning paths](https://mylearn.oracle.com/)** - the official free training
**[📖 OCI AI services documentation](https://docs.oracle.com/en-us/iaas/Content/ai-services/home.htm)** - product reference

## Why this exam is in this repo

Oracle has five OCI certifications in this repo and, until now, **zero AI ones**, in a repository whose remit is explicitly cloud plus AI. That is the gap this closes.

It also has a practical draw: Oracle regularly makes this exam and its training free, which makes it one of the cheapest ways to get a vendor AI credential.

## Target Audience

- Anyone new to AI who wants a structured, vendor-anchored overview
- OCI practitioners adding AI vocabulary
- Sales, product, and management roles needing credible AI literacy
- A stepping stone to [OCI Generative AI Professional](../oci-generative-ai-professional/)

No coding is required, and no prior AI knowledge is assumed.

## Exam Domains

Oracle publishes this as a topic list rather than weighted domains.

### AI fundamentals

**Key Concepts:**
- What AI is, and how AI, machine learning, and deep learning relate
- AI task categories: language, speech, vision, and decision
- Common applications and their business value
- Responsible AI: fairness, transparency, explainability, accountability, and privacy

### Machine learning fundamentals

**Key Concepts:**
- Supervised learning: classification and regression
- Unsupervised learning: clustering, dimensionality reduction, anomaly detection
- Reinforcement learning at a conceptual level
- The ML workflow: data collection, preparation, feature engineering, training, evaluation, deployment, monitoring
- Training, validation, and test splits
- Overfitting, underfitting, and the bias-variance trade-off
- Evaluation metrics: accuracy, precision, recall, F1, confusion matrix, and why accuracy alone misleads on imbalanced data
- Common algorithms: linear and logistic regression, decision trees, random forests, k-means, support vector machines

### Deep learning fundamentals

**Key Concepts:**
- Neural network structure: neurons, layers, weights, biases, activation functions
- Forward propagation, loss functions, backpropagation, gradient descent
- Hyperparameters: learning rate, epochs, batch size
- Architectures: CNN for images, RNN and LSTM for sequences, transformers for language
- Why GPUs matter for training, and the role of parallelism

### Generative AI and large language models

**Key Concepts:**
- Generative versus discriminative models
- Transformer architecture, attention, tokens, and embeddings
- Pre-training, fine-tuning, and instruction tuning
- Prompt engineering: zero-shot, few-shot, chain-of-thought
- Context window and its limits
- Hallucination and how grounding mitigates it
- Retrieval-augmented generation (RAG)
- Vector databases and semantic search
- Agents and tool use at a conceptual level

### OCI AI services

**Key Concepts:**
- **OCI Generative AI** - managed access to foundation models, with dedicated AI clusters and custom model fine-tuning
- **OCI Generative AI Agents** - retrieval-augmented agents over enterprise data
- **OCI Language** - sentiment, entity recognition, key phrase extraction, translation, PII detection
- **OCI Speech** - speech to text transcription
- **OCI Vision** - image classification, object detection, document AI
- **OCI Document Understanding** - extraction from forms and documents
- **OCI Data Science** - notebooks, model catalog, model deployment, jobs, pipelines
- **OCI Data Labeling**
- **Select AI** and AI Vector Search in Autonomous Database

### OCI AI infrastructure

**Key Concepts:**
- GPU shapes and bare metal compute for AI workloads
- RDMA cluster networking for distributed training
- Storage options for training data
- Where each service sits: infrastructure, platform, or ready-made service

## The service selection table

The most testable content on the exam.

| Requirement | Service |
|---|---|
| Analyze sentiment in customer reviews | OCI Language |
| Transcribe recorded calls | OCI Speech |
| Detect objects in photographs | OCI Vision |
| Extract fields from scanned invoices | OCI Document Understanding |
| Build and train a custom model in a notebook | OCI Data Science |
| Call a foundation model through an API | OCI Generative AI |
| Answer questions grounded in internal documents | OCI Generative AI Agents |
| Run distributed training across many GPUs | OCI AI infrastructure with RDMA cluster networking |
| Query a database with natural language | Select AI in Autonomous Database |

## Related repo material

- [Notes](./notes/) - four notes
- [Practice plan](./practice-plan.md) - 3-week schedule
- [Strategy](./strategy.md)
- [OCI Generative AI Professional](../oci-generative-ai-professional/) - the next step
- [OCI Foundations](../oci-foundations/) - the cloud fundamentals counterpart
- [AI from scratch](../../../learn/ai-from-scratch.md) - the vendor-neutral version of this material
- [LLM basics](../../../learn/concepts/llm-basics.md), [RAG explained](../../../learn/concepts/rag-explained.md)
