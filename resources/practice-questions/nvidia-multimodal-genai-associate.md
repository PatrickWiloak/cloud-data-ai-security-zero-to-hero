---
last-updated: 2026-08-09
difficulty: intermediate
---

# NVIDIA Certified Associate - Multimodal Generative AI (NCA-MMGA) - Practice Questions

15 questions for NCA-MMGA prep, weighted toward multimodal fundamentals (25%) and image and video generation (25%), then text and speech (20%), NVIDIA tooling (15%), and applications (15%).

> **Cert page:** [exams/nvidia/multimodal-genai-associate/](../../exams/nvidia/multimodal-genai-associate/)

---

### Question 1
**Scenario:** What makes a model multimodal?

A. It runs on multiple GPUs
B. It accepts or produces more than one modality, such as text and images, in a shared representation
C. It uses multiple prompts
D. It has more parameters

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The defining feature is a shared representation space that lets the model relate content across modalities, so an image and its description land near each other. Multi-GPU execution and parameter count are unrelated properties.
</details>

---

### Question 2
**Scenario:** CLIP-style training aligns images and text. What objective does it use?

A. Next-token prediction
B. Contrastive learning: matching image-text pairs are pulled together and mismatched pairs pushed apart
C. Diffusion denoising
D. Reinforcement learning

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Contrastive pretraining over large image-caption datasets is what produces a joint embedding space, which is what enables zero-shot classification and text-to-image retrieval. Diffusion is the generative mechanism used later, and next-token prediction is the language modeling objective.
</details>

---

### Question 3
**Scenario:** How does a diffusion model generate an image?

A. It predicts pixels left to right
B. It starts from noise and iteratively denoises, guided by the conditioning (such as a text embedding)
C. It retrieves the closest training image
D. It uses a GAN discriminator

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Training teaches the model to reverse a noising process; generation runs that reversal from pure noise. The number of denoising steps is the main quality-versus-speed knob, and latent diffusion runs the process in a compressed latent space to make it affordable.
</details>

---

### Question 4
**Scenario:** A text-to-image model must follow the prompt more closely.

A. Lower the guidance scale
B. Raise the classifier-free guidance scale, accepting reduced diversity and possible artifacts at high values
C. Reduce the number of steps
D. Change the random seed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Guidance scale trades prompt adherence against diversity and naturalness. Pushing it too high produces over-saturated, artifact-heavy output, so there is a usable band rather than a "higher is better" relationship. The seed changes which sample you get, not how closely it follows the prompt.
</details>

---

### Question 5
**Scenario:** A vision-language model must answer questions about a chart in an uploaded image.

A. OCR only
B. A VLM that encodes the image and reasons jointly over the visual and textual content
C. A text-only LLM
D. An embedding model alone

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Chart question answering needs both reading and reasoning over spatial structure, which a VLM does end to end. OCR extracts text but loses the relationships between axes, series, and values. Embeddings support retrieval rather than answering.
</details>

---

### Question 6
**Scenario:** Which NVIDIA product provides speech recognition and text-to-speech services?

A. NVIDIA Riva
B. NVIDIA Merlin
C. NVIDIA Morpheus
D. NVIDIA Clara

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Riva is the speech AI stack, covering ASR, TTS, and translation with GPU-optimized deployment. Merlin targets recommenders, Morpheus is cybersecurity AI, and Clara is healthcare.
</details>

---

### Question 7
**Scenario:** Multimodal RAG must retrieve both diagrams and text for a technical question.

A. Index only the text
B. Embed images and text into a shared or aligned space, or index image captions and metadata alongside text, then retrieve across both
C. Store images as base64 in the prompt
D. Ignore images

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Retrieval requires the images to be searchable, which comes from either a joint embedding model or a generated-caption index. Caption-based indexing is often the pragmatic choice because it also gives you readable evidence of why an image was retrieved.
</details>

---

### Question 8
**Scenario:** Generated video is temporally inconsistent: objects flicker between frames.

A. Increase resolution
B. Temporal coherence is a known challenge; use models with temporal attention or conditioning on prior frames, and evaluate consistency explicitly
C. Change the prompt wording only
D. Reduce the frame rate

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Frame-by-frame generation with no temporal mechanism produces flicker by construction. Video models add temporal layers or condition on preceding frames, and consistency should be measured as its own metric rather than assumed from per-frame quality.
</details>

---

### Question 9
**Scenario:** An image generation feature must not produce content resembling identifiable real people.

A. Rely on the prompt
B. Layered controls: prompt and output classification, restricted model or LoRA selection, and a documented policy with human review for edge cases
C. Add a disclaimer
D. Reduce image resolution

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Likeness and deepfake risk is a real harm and a legal exposure, so it needs enforcement rather than intent. Input filtering catches the obvious requests, output classification catches what slips through, and provenance metadata such as C2PA credentials supports downstream accountability.
</details>

---

### Question 10
**Scenario:** How should a multimodal model's quality be evaluated?

A. Human judgment only
B. Task-appropriate metrics plus human evaluation: for example FID or CLIP score for images, WER for speech recognition, and grounded accuracy for VQA
C. Parameter count
D. Inference latency

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Each modality has its own established metrics, and none of them fully capture perceived quality, which is why human evaluation stays in the loop. Reporting a single number across modalities hides where a system is actually failing.
</details>

---

### Question 11
**Scenario:** An image must be edited so only a specified region changes.

A. Regenerate the whole image
B. Inpainting with a mask, so the model regenerates only the masked region conditioned on the surroundings
C. Increase guidance
D. Use a larger model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Masked inpainting preserves the rest of the image exactly, which is what "edit this part" requires. Regenerating from a modified prompt changes everything, including details the user wanted kept. Outpainting is the same mechanism extended beyond the original boundary.
</details>

---

### Question 12
**Scenario:** A custom style must be applied consistently to generated images with only 20 reference examples.

A. Full fine-tuning
B. LoRA or DreamBooth-style adaptation on the small reference set
C. Train from scratch
D. Prompt engineering alone

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Lightweight adaptation methods learn a style or subject from a handful of images while keeping the base model frozen, which is both feasible and reversible. Full training needs orders of magnitude more data, and prompts alone rarely reproduce a specific visual identity consistently.
</details>

---

### Question 13
**Scenario:** Which describes the trade-off in reducing diffusion sampling steps?

A. No trade-off
B. Fewer steps means faster generation with typically lower fidelity, though distilled or consistency models narrow the gap substantially
C. Fewer steps improves quality
D. Steps affect only memory

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Step count directly sets both latency and cost. Distillation techniques have compressed high-quality generation into very few steps, which is why the naive "more steps is better" rule no longer holds across model families.
</details>

---

### Question 14
**Scenario:** Audio transcription accuracy is poor on domain-specific terminology.

A. Increase the sample rate
B. Adapt the model or use custom vocabulary and language model biasing for the domain terms
C. Use a larger microphone gain
D. Reduce the audio length

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Rare proper nouns and jargon are the standard weakness of general ASR models. Custom vocabulary, phrase boosting, or fine-tuning on domain audio directly targets that failure. Audio quality changes help only when quality is actually the problem.
</details>

---

### Question 15
**Scenario:** A multimodal application must run where data cannot leave the premises.

A. It is not possible
B. Deploy the models on-premises, for example with NIM microservices or NeMo on local GPU infrastructure
C. Anonymize and send to a public API
D. Use a smaller model in the cloud

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Self-hosting is the answer to a data residency constraint, and containerized microservices make it a deployment choice rather than a rewrite. Anonymization is rarely sufficient for images and audio, which carry identifying signal that is hard to remove.
</details>

---

## Where to go deeper

- [NCA-MMGA cert page](../../exams/nvidia/multimodal-genai-associate/) - notes, practice plan, strategy
- [NCA-GENL practice questions](./nvidia-genai-llms-associate.md) - the text-focused sibling
- [Multimodal models](../../learn/concepts/multimodal-models.md) - plain-English primer
- [LLMs and GenAI topic index](../../topics/llms-and-genai.md) - the wider AI stack
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
