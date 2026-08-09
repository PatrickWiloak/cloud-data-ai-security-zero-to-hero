---
last-updated: 2026-08-09
difficulty: advanced
---

# NVIDIA Certified Professional - OpenUSD (NCP-USD) - Practice Questions

15 questions for NCP-USD prep, weighted toward USD fundamentals (25%) and scene composition (25%), then the Omniverse platform (20%), rendering and materials (15%), and collaboration (15%).

> **Cert page:** [exams/nvidia/openusd-professional/](../../exams/nvidia/openusd-professional/)

---

### Question 1
**Scenario:** What is a prim in USD?

A. A file format
B. The primary container object in a scene hierarchy, carrying a type, properties, and metadata
C. A rendering pass
D. A material shader

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Prims are the nodes of the scene graph, identified by a path such as `/World/Vehicle/Wheel`. They have a type (Mesh, Xform, Camera, and so on), attributes, and relationships. Everything in a USD stage is addressed as a prim path.
</details>

---

### Question 2
**Scenario:** What does LIVRPS describe?

A. A rendering pipeline
B. The composition arc strength order: Local, Inherits, VariantSets, References, Payloads, Specializes
C. A file naming convention
D. A material model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** LIVRPS is the order in which USD resolves conflicting opinions about a prim's properties, strongest first. Understanding it is what lets you predict which layer's value wins, which is the single most important concept in USD composition.
</details>

---

### Question 3
**Scenario:** A large asset should not be loaded until it is needed.

A. A reference
B. A payload, which can be loaded and unloaded on demand
C. An inherit
D. A variant

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Payloads are references that are not composed by default, so a stage can be opened with heavy geometry deferred. This is the primary mechanism for working with scenes far larger than memory, and the choice between reference and payload is a scalability decision.
</details>

---

### Question 4
**Scenario:** One asset must be available in three configurations, switchable at runtime.

A. Three separate files with no relationship
B. A variant set with three variants on the prim
C. Three payloads always loaded
D. Three stages

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Variant sets encode alternatives inside a single asset and let a consumer select one by name, which keeps configuration a property of the asset rather than a file-management problem. Nested variant sets handle combinations such as model and trim level.
</details>

---

### Question 5
**Scenario:** Several artists must work on the same scene simultaneously without overwriting each other.

A. One shared file
B. Layer-based workflow: each contributor works in their own layer, composed into the stage by the layer stack
C. Take turns
D. Duplicate the scene per artist

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Non-destructive layering is the collaboration model USD was designed for: lighting, animation, and modeling opinions live in separate layers with defined strength, so nobody edits the same bytes. This is also why USD suits pipelines with many departments touching one asset.
</details>

---

### Question 6
**Scenario:** What is a stage in USD?

A. A single file
B. The composed scene graph resulting from evaluating the root layer and all its composition arcs
C. A rendering device
D. A material library

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The stage is the runtime view, not a file: it is what you get after composition has resolved references, payloads, variants, and layer strength. Distinguishing the authored layer from the composed stage explains most confusion about "why is my edit not showing."
</details>

---

### Question 7
**Scenario:** An edit must be made without modifying the referenced source asset.

A. Edit the source file
B. Author an override in a stronger local layer, so the source remains unchanged
C. Copy the asset
D. Delete the reference

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Non-destructive override is the core USD workflow: your opinion in a stronger layer wins during composition while the upstream asset keeps updating independently. Copying breaks the link and guarantees divergence when the source changes.
</details>

---

### Question 8
**Scenario:** Which describes Omniverse Nucleus?

A. A renderer
B. The collaboration and data service that stores USD content and publishes live change notifications to connected clients
C. A physics engine
D. A file format

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Nucleus is the server component providing versioned storage and the live-sync channel that makes multi-user editing possible. RTX Renderer and Hydra handle rendering, PhysX handles simulation, and Kit is the application framework.
</details>

---

### Question 9
**Scenario:** Materials must be portable across renderers.

A. Renderer-specific shaders only
B. MaterialX and UsdPreviewSurface for portable definitions, with renderer-specific implementations where needed
C. Textures with no material
D. Hard-coded colors

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** UsdPreviewSurface gives a baseline PBR material every USD-aware renderer understands, and MaterialX expresses richer node graphs portably. Authoring only in a renderer-specific language locks the asset to one pipeline, which defeats the interchange purpose of USD.
</details>

---

### Question 10
**Scenario:** Which layer wins when two sublayers in the same layer stack both set a prim's attribute?

A. The last one listed
B. The stronger one, meaning the one earlier in the sublayer list
C. They are averaged
D. It is undefined

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Sublayer order is strength order, strongest first, and the strongest opinion wins with no blending. This is deterministic by design, which is what makes a pipeline reproducible. `usdview`'s composition inspector shows exactly which layer supplied a value.
</details>

---

### Question 11
**Scenario:** Hydra is used in the rendering path. What is its role?

A. It authors USD files
B. It is the scene delegate architecture that decouples the scene description from the renderer, so multiple render delegates can consume the same stage
C. It stores assets
D. It handles physics

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hydra sits between the scene and the renderer so the same USD stage can be drawn by Storm, RTX, or a third-party delegate without changing the data. That separation is what lets a studio switch renderers without reauthoring content.
</details>

---

### Question 12
**Scenario:** A schema must add domain-specific properties to prims consistently.

A. Ad-hoc attributes on each prim
B. A typed or applied API schema defining the properties, so tooling can rely on them
C. Comments in the file
D. External spreadsheets

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Schemas make properties discoverable and validated rather than conventional, which is what allows tools to interoperate. Applied API schemas add capabilities to existing prim types without changing their type, which is the usual choice for domain metadata.
</details>

---

### Question 13
**Scenario:** A scene opens very slowly with high memory use.

A. Buy more RAM
B. Convert heavy references to payloads, use instancing for repeated geometry, and check for unnecessarily deep composition
C. Reduce the screen resolution
D. Disable materials

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Composition cost and geometry duplication are the two usual causes. Point instancers and scenegraph instancing collapse thousands of identical prims into shared data, and payloads defer what is not needed yet. Hardware only postpones the ceiling.
</details>

---

### Question 14
**Scenario:** Assets from several tools must combine into one scene.

A. Convert everything to a proprietary format
B. Use USD as the interchange format, with connectors exporting each tool's data, and validate with the USD validation tooling
C. Rebuild everything in one tool
D. Screenshot each asset

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Interchange is USD's original purpose and the reason it spread beyond film into simulation and industrial digital twins. Validation matters because a syntactically valid file can still violate pipeline conventions, and catching that at export is far cheaper than downstream.
</details>

---

### Question 15
**Scenario:** Time-varying data such as animation is stored how in USD?

A. Only as a single static value
B. As time samples on attributes, evaluated at a given time code against the stage's frame rate
C. In a separate video file
D. As a material property

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Attributes hold either a default value or a set of time samples, and the stage's timeCodesPerSecond relates time codes to seconds. Layer offsets and scales let a referenced animation be retimed without editing the source, which is the composition system applied to time.
</details>

---

## Where to go deeper

- [NCP-USD cert page](../../exams/nvidia/openusd-professional/) - notes, practice plan, strategy
- [NCA-MMGA practice questions](./nvidia-multimodal-genai-associate.md) - generative content for 3D pipelines
- **[📖 OpenUSD documentation](https://openusd.org/release/index.html)** - primary source
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
