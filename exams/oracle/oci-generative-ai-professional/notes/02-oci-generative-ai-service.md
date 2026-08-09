---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 8 min
---

# 02 - The OCI Generative AI service

---

## What the service provides

A managed service offering foundation models through an API, console playground, SDK, and CLI, plus the ability to fine-tune and host custom models.

Model families available:
- **Chat models** for generation, of varying size and context window
- **Embedding models** for semantic search and RAG

Model availability and versions change frequently, so verify the current catalog in the documentation rather than memorizing names. What the exam tests is the **shape** of the service, not the model list.

---

## Inference modes

| | On-demand | Dedicated AI cluster |
|---|---|---|
| **Billing** | Per request, by tokens consumed | Reserved capacity, by cluster unit hours |
| **Throughput** | Shared, variable under load | Dedicated and predictable |
| **Isolation** | Shared infrastructure | Isolated to your tenancy |
| **Base models** | Yes | Yes |
| **Custom fine-tuned models** | **No** | **Yes, required** |
| **Fine-tuning** | **No** | **Yes, required** |
| **Fits** | Development, prototyping, spiky or low-volume workloads | Steady production load, latency commitments, any custom model |

**Two things force a dedicated cluster: fine-tuning, and hosting a custom model.** That is the constraint the exam tests most often.

Cluster types are distinct: a **fine-tuning cluster** runs the training job, and a **hosting cluster** serves the resulting model. Plan for both if you retrain regularly.

---

## Custom models

The fine-tuning flow:

1. Prepare a training dataset in the required format, typically prompt and completion pairs, stored in Object Storage
2. Create a **fine-tuning dedicated AI cluster**
3. Run the fine-tuning job, selecting the base model and method (**T-Few** for parameter-efficient tuning)
4. Review training metrics: loss, and accuracy where applicable
5. Create a **hosting cluster** and an **endpoint** to serve the model
6. Call the endpoint like any other model

Practical guidance the exam reflects:
- Data quality matters more than volume. A few hundred high-quality, consistent examples usually beat thousands of noisy ones
- Fine-tune for **behavior**: tone, format, structure, domain phrasing. Not for knowledge
- Evaluate against a held-out set, not against the training data
- Fine-tuned knowledge is frozen at training time; anything that changes belongs in retrieval

---

## OCI Generative AI Agents

A managed service providing retrieval-augmented agents over enterprise data.

- Connect a data source, typically documents in Object Storage or content in a database
- The service handles ingestion, chunking, embedding, and retrieval
- Users ask questions in natural language and receive grounded answers with citations
- Reduces the work of building a RAG pipeline yourself, at the cost of some control over chunking and retrieval strategy

Choose the agent service when the requirement is a grounded question-answering experience over documents, and build your own pipeline when you need control over retrieval behavior.

---

## Security and governance

The service inherits standard OCI controls, and the exam expects you to know they apply:

- **Compartments** for logical isolation and access boundaries
- **IAM policies** governing who may call the service, create clusters, or fine-tune
- **Private endpoints** so traffic does not traverse the public internet
- **Encryption** at rest and in transit, with customer-managed keys where required
- **Customer data isolation**: data submitted to the service is not used to train Oracle's base models, and dedicated clusters provide infrastructure isolation
- **Content moderation** controls for input and output filtering
- **Audit logging** of API activity

For an application built on the service, the security work does not stop here. Retrieval authorization, output handling, and tool permissions are the application's responsibility, and are covered in the repo's [AI security](../../../../resources/ai-security/) material.

---

## Limits, monitoring, and cost

- **Service limits and quotas** apply per tenancy and per region, and are raised by request
- **Monitoring** through OCI Monitoring for request volume, latency, and errors
- Cost drivers: input tokens, output tokens, and reserved cluster hours
- The largest practical cost levers in an application are the size of retrieved context, how conversation history is carried, and the length of the system prompt

---

## Key terms

- **OCI Generative AI** - the managed service providing foundation model inference, embeddings, and fine-tuning
- **On-demand inference** - per-request access to base models, billed by tokens
- **Dedicated AI cluster** - reserved, isolated capacity required for fine-tuning and for hosting custom models
- **Fine-tuning cluster** - a dedicated cluster that runs a fine-tuning job
- **Hosting cluster** - a dedicated cluster that serves a model through an endpoint
- **Endpoint** - the addressable serving target for a model on a hosting cluster
- **Custom model** - a model fine-tuned on your data, which can only be served from a dedicated cluster
- **T-Few** - the parameter-efficient fine-tuning method offered by the service
- **OCI Generative AI Agents** - the managed retrieval-augmented agent service over enterprise data
- **Compartment** - the OCI construct providing logical isolation and an access boundary
- **Private endpoint** - a private network path to the service, keeping traffic off the public internet
- **Content moderation** - service controls filtering harmful input and output
- **Service limit** - the per-tenancy, per-region quota governing resource consumption

---

## Related

- [Notes 03: building LLM applications](./03-building-llm-applications.md)
- [Scenarios](../scenarios.md) - scenario 2
- [AI security](../../../../resources/ai-security/)
