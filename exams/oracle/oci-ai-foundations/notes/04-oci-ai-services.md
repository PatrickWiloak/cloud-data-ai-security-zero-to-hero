---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 8 min
---

# 04 - OCI AI services and infrastructure

The service selection questions are the fastest marks on the exam.

---

## The four layers

| Layer | Services | You bring | You need ML skills? |
|---|---|---|---|
| **Ready-made AI services** | Language, Speech, Vision, Document Understanding | Your data | No |
| **Generative AI** | OCI Generative AI, Generative AI Agents | Prompts, or documents to ground on | No |
| **ML platform** | Data Science, Data Labeling | Your model and code | Yes |
| **AI infrastructure** | GPU shapes, bare metal, RDMA cluster networking | Everything | Yes |

Identifying the layer usually resolves the question. "Without machine learning expertise" points at a ready-made service; "train a custom model" points at Data Science; "distributed training across many GPUs" points at infrastructure.

---

## Ready-made AI services

**OCI Language**
- Sentiment analysis, at document and aspect level
- Named entity recognition
- Key phrase extraction
- Language detection
- Text classification
- Translation
- **PII detection and redaction**
- Custom models for classification and entity recognition

**OCI Speech**
- Speech to text transcription, batch and real time
- Multiple languages, punctuation, and profanity filtering
- Speaker diarization

**OCI Vision**
- Image classification and object detection
- Text detection in images (OCR)
- Face detection
- Custom models trained on your own labeled images

**OCI Document Understanding**
- Extraction from forms, invoices, receipts, and identity documents
- Table extraction, key-value extraction, document classification

---

## Generative AI

**OCI Generative AI** provides managed access to foundation models through an API and console:
- **On-demand inference** for variable workloads
- **Dedicated AI clusters** for predictable throughput and isolation
- **Custom models** through parameter-efficient fine-tuning on your own data
- Embedding models for semantic search and RAG
- Content moderation controls

**OCI Generative AI Agents** provides retrieval-augmented agents over enterprise data sources, so users can ask questions in natural language and get answers grounded in company documents, with citations.

**AI Vector Search** in Autonomous Database stores embeddings alongside relational data and performs similarity search in SQL, which removes the need for a separate vector store.

**Select AI** lets users query the database in natural language, with the model generating the SQL.

---

## ML platform

**OCI Data Science** is the environment for building your own models:
- **Notebook sessions** - managed JupyterLab with GPU options
- **Model catalog** - versioned model storage with metadata and provenance
- **Model deployment** - models served as HTTP endpoints with autoscaling
- **Jobs** - repeatable training or processing runs
- **Pipelines** - orchestrated multi-step ML workflows
- **AI Quick Actions** - deploy, fine-tune, and evaluate foundation models without writing serving code
- Feature store and model monitoring capabilities

**OCI Data Labeling** creates labeled datasets for supervised training, supporting images, text, and documents.

---

## AI infrastructure

- **GPU shapes** on virtual machines and bare metal for training and inference
- **Bare metal** where you need the full device without virtualization overhead
- **RDMA cluster networking** for low-latency, high-throughput communication between nodes during distributed training. This is the differentiator for large-scale training, because the interconnect is the bottleneck once you exceed one node
- **Storage**: Object Storage for datasets, File Storage for shared access during training, Block Volumes for attached performance

---

## Responsible AI in OCI

- Data used with OCI AI services is not used to train Oracle's base models
- Dedicated AI clusters provide isolation for sensitive workloads
- Content moderation controls in Generative AI
- PII detection in OCI Language supports privacy workflows
- Standard OCI controls apply: IAM policy, compartments, private endpoints, encryption, and audit logging

---

## Service selection drill

| Requirement | Service |
|---|---|
| Sentiment across product reviews | OCI Language |
| Redact personal data from support tickets | OCI Language (PII detection) |
| Transcribe recorded support calls | OCI Speech |
| Detect defects in production line photos | OCI Vision, custom model |
| Extract totals and dates from scanned invoices | OCI Document Understanding |
| Chatbot answering from internal policy documents | OCI Generative AI Agents |
| Summarize text through an API | OCI Generative AI |
| Adapt a foundation model to a domain vocabulary | OCI Generative AI custom model (fine-tuning) |
| Semantic search over data already in the database | AI Vector Search |
| Ask questions of a database in plain English | Select AI |
| Train a custom model in a notebook | OCI Data Science |
| Create labeled training data | OCI Data Labeling |
| Serve a trained model as an endpoint | OCI Data Science model deployment |
| Distributed training across many GPUs | AI infrastructure with RDMA cluster networking |

---

## Key terms

- **OCI Language** - the ready-made service for sentiment, entities, key phrases, translation, and PII detection
- **OCI Speech** - the ready-made service converting speech to text
- **OCI Vision** - the ready-made service for image classification, object detection, and OCR
- **OCI Document Understanding** - the service extracting structured data from forms and documents
- **OCI Generative AI** - the managed service providing foundation model inference, embeddings, and fine-tuning
- **Dedicated AI cluster** - isolated capacity for predictable generative AI throughput
- **OCI Generative AI Agents** - the managed service providing retrieval-augmented agents over enterprise data
- **AI Vector Search** - Autonomous Database's native vector storage and similarity search
- **Select AI** - the capability translating natural language questions into SQL against the database
- **OCI Data Science** - the platform for building, training, deploying, and monitoring custom models
- **Model catalog** - the versioned store for models with metadata and provenance in OCI Data Science
- **Model deployment** - serving a catalogued model as a scalable HTTP endpoint
- **AI Quick Actions** - OCI Data Science capability for deploying and fine-tuning foundation models without custom serving code
- **OCI Data Labeling** - the service for creating labeled datasets for supervised training
- **Bare metal GPU shape** - a compute shape providing direct access to GPUs without virtualization overhead

---

## Related

- [Notes 01: AI and ML fundamentals](./01-ai-and-ml-fundamentals.md)
- [OCI Generative AI Professional](../../oci-generative-ai-professional/)
- [Service comparison: AI and ML](../../../../resources/service-comparison-ai-ml.md)
