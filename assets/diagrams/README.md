# Diagrams

PNG diagrams, for the cases where an inline diagram will not do.

**Mermaid is the default in this repo.** Write diagrams inline in the page that uses
them, in a fenced ` ```mermaid ` block. GitHub renders it natively, it stays editable in
the markdown, and it diffs as text in review. See
[docs/ARCHITECTURE.md](../../docs/ARCHITECTURE.md#visual-content-standards) for the full
convention.

Use a PNG here only when the diagram is too dense to read as inline text: large
multi-region topologies, detailed multi-service reference architectures. If you are
unsure, write it in Mermaid first and see whether it reads.

## Layout

Organised by topic. Subdirectories are created lazily as content grows:

```
assets/diagrams/
├── architecture/    # Architecture patterns (3-tier, microservices, event-driven, etc.)
├── ai/              # AI/ML topics (RAG pipelines, attention, agent loops)
├── cloud/           # Cloud primitives (regions, VPC topologies, storage)
├── networking/      # Networking deep dives (DNS flow, BGP, load balancing)
└── security/        # Security and identity flows (OAuth, IAM, zero trust)
```

## Authoring

- Create diagrams in [draw.io](https://app.diagrams.net/) (or the draw.io MCP server when available).
- Export at 2x resolution for retina displays.
- Keep file size under ~200 KB for inline use.
- Commit the editable `.drawio` source alongside the exported `.png` so others can edit it.

## Embedding

```markdown
![Descriptive alt text](../../assets/diagrams/<topic>/<slug>.png)
```

Always include alt text. It matters both when the image fails to render and for
screen-reader users.
