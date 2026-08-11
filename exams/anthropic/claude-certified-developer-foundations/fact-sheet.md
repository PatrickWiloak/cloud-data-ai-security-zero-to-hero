---
last-updated: 2026-08-11
---

# CCDV-F - Fact Sheet

## Quick Reference

| Detail | Info |
|---|---|
| Exam Code | CCDV-F |
| Full Name | Claude Certified Developer - Foundations |
| Provider | Anthropic |
| Duration | 120 minutes |
| Questions | 53 multiple-choice and multiple-response |
| Passing Score | 720 / 1000 |
| Cost | $125 USD |
| Delivery | Pearson VUE - online proctored or test center |
| Validity | 12 months (free non-proctored renewal via Partner Academy) |
| Prerequisites | None |
| Registration | Anthropic Partner Academy (requires free Claude Partner Network membership) |
| Retakes | 14 days after attempt 1, 30 after attempt 2, 90 after attempt 3; max 4 per rolling 12 months |

---

## Exam Domains (blueprint v1.0, effective July 2026)

| # | Domain | Weight | Focus |
|---|---|---|---|
| 1 | Applications and Integration | 33.1% | Messages API, streaming, files, batching, errors, SDKs |
| 2 | Model Selection and Optimization | 16.8% | Model family, caching economics, cost and latency levers |
| 3 | Agents and Workflows | 14.7% | Workflow patterns, agent loops, Agent SDK, reliability |
| 4 | Prompt and Context Engineering | 11.0% | System prompts, structure, context management |
| 5 | Tools and MCPs | 10.6% | Tool use lifecycle, tool design, Model Context Protocol |
| 6 | Security and Safety | 8.1% | Key handling, prompt injection, validation, moderation |
| 7 | Claude Code | 3.1% | CLAUDE.md, settings, hooks, MCP config, headless use |
| 8 | Eval, Testing, and Debugging | 2.6% | Graders, regression suites, debugging tool calls |

---

## Models (mid-2026)

| Model | Tier | Use |
|---|---|---|
| Claude Opus 5 | Most capable | Deep reasoning, hard agentic and coding work |
| Claude Sonnet 5 | Balanced | Default workhorse for most applications |
| Claude Haiku 4.5 | Fastest, cheapest | Throughput, classification, routing, sub-agents |

Model lineups change. Check current IDs and pricing at https://docs.anthropic.com/en/docs/about-claude/models before the exam. See [notes/08](notes/08-model-selection-and-optimization.md) for selection criteria.

---

## Authentication

- Header: `x-api-key: <key>`
- Header: `anthropic-version: 2023-06-01`
- Beta features: `anthropic-beta: <feature>`

Bedrock and Vertex use IAM and service accounts respectively, not the API key.

---

## Messages API Essentials

### Request Shape (Minimal)

```json
{
  "model": "claude-sonnet-4-6",
  "max_tokens": 1024,
  "messages": [
    {"role": "user", "content": "Hello"}
  ]
}
```

### Required Fields

- `model`
- `max_tokens`
- `messages`

### Optional Fields

- `system` - system prompt (string or array of content blocks)
- `temperature` - 0 to 1
- `top_p`, `top_k`
- `stop_sequences`
- `stream` - boolean
- `tools`, `tool_choice`
- `thinking` - extended thinking config
- `metadata` - user_id for abuse tracking

### Response Shape

```json
{
  "id": "msg_...",
  "type": "message",
  "role": "assistant",
  "model": "claude-sonnet-4-6",
  "content": [{"type": "text", "text": "..."}],
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 12,
    "output_tokens": 30,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0
  }
}
```

### Stop Reasons

- `end_turn` - natural completion
- `max_tokens` - hit max_tokens cap
- `stop_sequence` - hit a stop_sequence
- `tool_use` - Claude wants to call a tool
- `pause_turn` - long-running response paused (rare)
- `refusal` - model declined to respond

---

## Content Block Types

- text
- image (base64 or URL)
- document (PDF, base64 or file_id)
- tool_use (Claude's request to call a tool)
- tool_result (your response to a tool_use)
- thinking (Claude's internal reasoning)

---

## Streaming Events

In order:

1. `message_start` - message metadata
2. For each content block:
   - `content_block_start`
   - `content_block_delta` (one or more)
   - `content_block_stop`
3. `message_delta` - usage and stop_reason updates
4. `message_stop` - end of stream

Delta types:

- `text_delta` - text increments
- `input_json_delta` - tool_use input building
- `thinking_delta` - thinking content
- `signature_delta` - thinking signature

Also: `ping` events for keepalive.

---

## Tool Use Lifecycle

1. Define tools in the request: `tools: [{name, description, input_schema}]`
2. Set `tool_choice`: `auto` (default), `any`, `{type: "tool", name: "..."}`, or `none`
3. Claude responds with `stop_reason: tool_use` and one or more `tool_use` blocks
4. Execute the tool(s) in your code
5. Send a new message with role `user` and a `tool_result` content block per tool_use
6. Continue the loop until `stop_reason: end_turn`

### Forced Structured Output

To guarantee JSON matching a schema:

```python
tools = [{
    "name": "extract_invoice",
    "description": "Extract structured invoice fields.",
    "input_schema": {...JSON schema...}
}]
tool_choice = {"type": "tool", "name": "extract_invoice"}
```

The tool's `input` will be the structured output.

---

## Prompt Caching

- Mark blocks with `cache_control: {"type": "ephemeral"}`
- Default TTL: 5 minutes
- 1-hour TTL: `cache_control: {"type": "ephemeral", "ttl": "1h"}` (where supported)
- Up to 4 cache breakpoints per request
- Minimum cacheable prefix varies by model (roughly 1024-4096 tokens; below the minimum a marker silently does nothing)
- Cache writes ~1.25x input rate
- Cache reads ~0.1x input rate
- `usage.cache_creation_input_tokens` and `usage.cache_read_input_tokens` report per request

### What to Cache (in order)

1. System prompt
2. Tool definitions
3. Stable reference docs
4. Few-shot examples
5. Conversation prefix

---

## Batch API

| Aspect | Value |
|---|---|
| Discount | 50% off real-time |
| SLA | Within 24 hours |
| Max requests per batch | 100,000 |
| Max batch size | 256 MB |

### Workflow

1. Submit batch: `POST /v1/messages/batches` with array of requests
2. Poll: `GET /v1/messages/batches/{id}` for status
3. Retrieve: `GET /v1/messages/batches/{id}/results` (JSONL stream)
4. Each item succeeds or fails independently

### Batch Statuses

- in_progress
- canceling
- ended

Per-item results: `succeeded`, `errored`, `expired`, `canceled`.

---

## Files API

- Upload: `POST /v1/files` (multipart)
- Reference by `file_id` in subsequent messages
- Supported types: PDF, images, plain text, JSON, more
- File size limits and storage TTL per docs
- Use to avoid re-uploading the same artifact across requests

---

## Citations

Enables Claude to cite specific spans of input documents in its response. Wrap source documents in `document` content blocks with `citations: {enabled: true}`. Claude returns `citations` arrays alongside text spans.

Use cases:

- Grounded RAG with source attribution
- Compliance use cases requiring traceability
- UI rendering of "sources" beneath generated answers

---

## Vision and PDF

### Images

```json
{"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": "..."}}
```

Or by URL or `file_id`.

### PDFs

```json
{"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": "..."}}
```

Or by URL or `file_id`. Claude reads text and visual layout.

---

## Error Codes

| Code | Meaning | Action |
|---|---|---|
| 400 | invalid_request_error | Fix request |
| 401 | authentication_error | Check API key |
| 403 | permission_error | Check permissions |
| 404 | not_found_error | Check ID/endpoint |
| 413 | request_too_large | Trim payload |
| 429 | rate_limit_error | Retry with backoff per Retry-After |
| 500 | api_error | Retry with backoff |
| 529 | overloaded_error | Retry with backoff |

### Rate Limit Headers

- `anthropic-ratelimit-requests-limit`
- `anthropic-ratelimit-requests-remaining`
- `anthropic-ratelimit-requests-reset`
- `anthropic-ratelimit-tokens-limit`
- `anthropic-ratelimit-tokens-remaining`
- `anthropic-ratelimit-tokens-reset`
- `retry-after` on 429 / 529

---

## Retry Patterns

- Exponential backoff with jitter
- Cap retries (3-5)
- Honor `retry-after` when present
- Distinguish retryable (429, 500, 529, network) from non-retryable (400, 401, 403, 404)

---

## SDK Highlights

### Python

```python
from anthropic import Anthropic
client = Anthropic()  # reads ANTHROPIC_API_KEY
msg = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hi"}],
)
```

Async: `from anthropic import AsyncAnthropic`.

Streaming helper:

```python
with client.messages.stream(...) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
final = stream.get_final_message()
```

Bedrock: `from anthropic import AnthropicBedrock`.
Vertex: `from anthropic import AnthropicVertex`.

### TypeScript

```ts
import Anthropic from "@anthropic-ai/sdk";
const client = new Anthropic();
const msg = await client.messages.create({
  model: "claude-sonnet-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hi" }],
});
```

Streaming:

```ts
const stream = client.messages.stream({...});
for await (const event of stream) { ... }
const final = await stream.finalMessage();
```

---

## New-Domain Quick Facts

### Model Selection and Optimization (Domain 2, 16.8%)

- Choose by capability need, latency budget, and cost per token: Opus for the hardest reasoning, Sonnet as the default, Haiku for high-volume simple tasks.
- Cost levers in rough order of impact: prompt caching, Batch API (50% off), model routing (cheap model for easy requests), truncating or summarizing history, right-sizing `max_tokens`.
- Extended thinking spends output tokens on reasoning; control the spend with the model's thinking or effort configuration and leave `max_tokens` headroom.
- Count tokens with the token counting endpoint, never a third-party tokenizer.
- Full detail: [notes/08](notes/08-model-selection-and-optimization.md).

### Agents and Workflows (Domain 3, 14.7%)

- Workflow = your code orchestrates fixed steps. Agent = the model decides the next step in a tool-use loop.
- Know the five workflow patterns: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer.
- Agent reliability: iteration caps, budget limits, human-in-the-loop gates for destructive actions.
- The Claude Agent SDK packages the Claude Code harness (tools, loop, permissions) as a library.
- Full detail: [notes/09](notes/09-agents-and-workflows.md).

### Security and Safety (Domain 6, 8.1%)

- API keys live in environment variables or a secrets manager, never in code or client-side bundles.
- Prompt injection: treat all retrieved or user-supplied content as untrusted; least-privilege tools; human approval for irreversible actions.
- Validate tool inputs and model outputs at system boundaries; handle `stop_reason: "refusal"` before reading content.
- Full detail: [notes/10](notes/10-security-safety-claude-code-and-evals.md).

### Claude Code (Domain 7, 3.1%)

- CLAUDE.md = persistent project context; settings.json = permissions and config; hooks = shell commands on lifecycle events; MCP servers configured per project or user.
- Headless mode (`claude -p`) and the Agent SDK enable CI and programmatic use.
- Full detail: [notes/10](notes/10-security-safety-claude-code-and-evals.md).

### Eval, Testing, and Debugging (Domain 8, 2.6%)

- Grader types: exact match / string checks (cheap, rigid), code graders (deterministic properties), LLM-as-judge (subjective quality, needs its own validation).
- Build the eval set before tuning prompts; run it as a regression suite on every prompt or model change.
- Debug tool-call failures by logging full request and response bodies, including `tool_use_id` pairing and `stop_reason`.
- Full detail: [notes/10](notes/10-security-safety-claude-code-and-evals.md).

---

## High-Yield Exam Tips

1. `max_tokens` is required.
2. System prompts go in the `system` field, not as a message.
3. `stop_reason: tool_use` requires you to send `tool_result` next, not a regular user message.
4. Tool results go in a `user` role message with `tool_result` content blocks.
5. `cache_control` belongs on individual content blocks, not on the request.
6. Cache writes cost more; cache reads cost much less; break-even ~2 reads.
7. Batch API is async; poll or use webhooks.
8. The Retry-After header overrides your default backoff.
9. The SDK is thread-safe; reuse the client.
10. Bedrock and Vertex have separate SDK clients but the same Messages interface.

---

## Common Traps

1. Putting the system prompt as a user message (use `system` field).
2. Forgetting to send tool_result and instead sending a fresh user message.
3. Caching content that changes per request.
4. Missing `cache_creation_input_tokens` accounting in cost reports.
5. Treating Batch results as in-order; they are not.
6. Retrying 400 errors blindly.
7. Hardcoding model IDs without env config.
8. Ignoring `pause_turn` stop reason on long responses.
9. Confusing `tool_choice: any` with `tool_choice: {type: "tool", name: ...}`.
10. Streaming without consuming events to completion (resource leak).
