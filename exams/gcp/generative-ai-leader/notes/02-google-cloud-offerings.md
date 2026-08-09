---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 8 min
---

# 02 - Google Cloud's generative AI offerings

The main memorization load. Learn each product by the problem it solves.

---

## The adoption ladder

| Rung | What you use | Effort | Fits |
|---|---|---|---|
| **Applied assistants** | Gemini for Google Workspace, Gemini for Google Cloud | Lowest, no build | Productivity gains across an organization |
| **Pre-built products** | Vertex AI Search, Conversational Agents, NotebookLM | Low, configure not code | A common capability delivered quickly |
| **Build on the platform** | Vertex AI with Gemini, grounding, function calling | Medium | A differentiated product experience |
| **Customize a model** | Fine-tuning on Vertex AI | High | Consistent specialized behavior at scale |
| **Train from scratch** | Custom foundation model | Very high | Effectively never |

Start at the top. The exam consistently rewards the lowest rung that solves the stated problem.

---

## Vertex AI

The unified platform for AI on Google Cloud.

- **Model Garden** - the catalog of available models: Google's own, open models, and third-party
- **Vertex AI Studio** - a console for prompt design, testing, and comparison without writing code
- **Training and tuning** - fine-tuning and custom training
- **Prediction and endpoints** - serving models
- **Evaluation** - measuring model and application quality
- **Pipelines** - orchestrating ML workflows
- **Feature Store, Model Registry, Model Monitoring** - the MLOps surfaces
- **Vector Search** - similarity search over embeddings at scale
- **Agent Builder** - building agents and search experiences

---

## Models

| Model | Type | Used for |
|---|---|---|
| **Gemini** | Multimodal foundation model family | General generation, reasoning, and multimodal understanding across text, image, audio, video, and code |
| **Gemma** | Open models | Running yourself, on your own infrastructure or at the edge, where openness or control matters |
| **Imagen** | Image generation and editing | Creating and editing images from text |
| **Veo** | Video generation | Creating video from text or images |
| **Chirp** | Speech | Speech recognition and transcription |
| **Embeddings models** | Vector representations | Semantic search, RAG, clustering, recommendation |

Model families come in size tiers, trading capability against cost and latency. Matching the model to the task, rather than defaulting to the largest, is a recurring exam theme.

---

## Pre-built products

**Vertex AI Search** - grounded enterprise search over your own content, with generative summaries and citations. The answer when the requirement is "let employees or customers ask questions about our documents".

**Vertex AI Agent Builder / Conversational Agents** - building conversational agents that can answer questions, take actions through tools, and hand off to humans. The answer for a customer-facing assistant or an internal helpdesk bot.

**NotebookLM** - grounded research over sources you supply, producing summaries, briefings, and question answering restricted to those sources. The answer for individual or small-team research over a document set.

**BigQuery generative AI functions** - calling models directly from SQL, so text generation, summarization, and embedding happen next to the data without building a pipeline. The answer when the data is already in BigQuery and the task is analytical.

---

## Applied assistants

**Gemini for Google Workspace** brings generative AI into Docs, Gmail, Sheets, Slides, and Meet: drafting, summarizing, and meeting notes. It is the fastest path to organization-wide productivity gains, with no build at all.

**Gemini for Google Cloud** assists engineering work: code assistance, cloud operations, and troubleshooting inside the console and IDEs.

These matter on the exam because many scenarios describing a productivity problem are answered by an applied assistant rather than by a project.

---

## Infrastructure

- **AI Hypercomputer** - Google's integrated architecture of hardware, software, and consumption models for large-scale AI
- **TPUs** - Google's purpose-built AI accelerators, designed for large-scale training and inference
- **GPUs** - the alternative accelerator, familiar and broadly compatible
- **Cloud Storage and BigQuery** - where training and grounding data usually lives

Most business-level scenarios do not reach infrastructure. What matters is recognizing that Google offers it and that infrastructure choice is a cost and scale decision, not a capability decision, for most adopters.

---

## Enterprise controls

Frequently the deciding factor in a business scenario:

- **Data governance**: customer data submitted to Vertex AI is not used to train Google's foundation models
- **Data residency** and regional endpoints for regulatory requirements
- **VPC Service Controls and Private Service Connect** for private access
- **CMEK** for customer-managed encryption keys
- **IAM** for access control, and audit logging for accountability
- **Safety filters** configurable per application

When a scenario names a regulated industry or a data residency requirement, these are the differentiators to reach for.

---

## Key terms

- **Vertex AI** - Google Cloud's unified platform for building, tuning, deploying, and evaluating AI
- **Model Garden** - the Vertex AI catalog of Google, open, and third-party models
- **Vertex AI Studio** - the console surface for designing and testing prompts without code
- **Gemini** - Google's multimodal foundation model family
- **Gemma** - Google's family of open models intended to be run by the user
- **Imagen** - Google's image generation and editing model
- **Veo** - Google's video generation model
- **Chirp** - Google's speech recognition model
- **Vertex AI Search** - grounded enterprise search with generative summaries and citations
- **Vertex AI Agent Builder** - the product for building conversational agents and search experiences
- **NotebookLM** - grounded research and question answering over sources the user supplies
- **BigQuery generative AI functions** - calling models directly from SQL inside the data warehouse
- **Gemini for Google Workspace** - generative AI applied inside Docs, Gmail, Sheets, Slides, and Meet
- **Gemini for Google Cloud** - generative AI assistance for engineering and cloud operations
- **AI Hypercomputer** - Google's integrated architecture for large-scale AI workloads
- **TPU** - Google's purpose-built accelerator for AI training and inference
- **VPC Service Controls** - the perimeter control restricting data movement out of a defined boundary

---

## Related

- [Notes 03: improving generative AI output](./03-improving-output.md)
- [Service comparison: GenAI platforms](../../../../resources/service-comparison-genai-platforms.md)
