---
last-updated: 2026-08-11
---

# CCDV-F - Exam Strategy

The Claude Certified Developer - Foundations exam tests whether you can write correct Claude code, debug it, and make sound implementation choices across eight domains. Many questions take the form of a code snippet plus "what is wrong?" or a scenario plus "which approach fits?". It is 53 questions in 120 minutes, multiple-choice and multiple-response, passing score 720 on a 100-1000 scale. Time pressure is manageable if you can read Python or TypeScript fluently.

Weight your preparation by the blueprint: Applications and Integration is 33.1% of the exam; Claude Code (3.1%) and Eval, Testing, and Debugging (2.6%) together are under 6%. An hour on streaming events is worth more than an hour on hooks.

---

## 3-Phase Preparation

### Phase 1 - Build Fluency (Weeks 1-2)

Write code with the API daily. Use both Python and TypeScript SDKs at least once. Trace every byte of streaming events. Run a tool loop by hand without the SDK helpers so you understand what they do for you.

### Phase 2 - Production Patterns (Weeks 3-4)

Layer in caching, batches, files, retries, model routing, agent guardrails, and security. Build something you would not be embarrassed to deploy. Feel each rate limit, each cache hit, each refused request.

### Phase 3 - Drill (Week 5)

Run timed scenarios and the practice question bank. Do the free Partner Academy prep courses. Re-read the fact sheet. Sleep before the exam.

---

## Time Management

53 questions in 120 minutes: about 2 minutes 15 seconds per question with a small buffer.

| Time Elapsed | Question # |
|---|---|
| 30 min | 14 |
| 60 min | 27 |
| 90 min | 41 |
| 110 min | 53 (done, review) |

First pass: answer fast, flag the slow ones. Second pass: spend the buffer on flags. Third pass: review only with concrete reasons to change. Multiple-response questions say how many options to pick; read that line first.

---

## Reading Code Snippets Fast

Train yourself to scan for these markers:

- `messages.create` vs `messages.stream` vs `messages.batches.create` - tells you the API surface
- `tool_choice` value - tells you if the question is about forcing tool use
- `cache_control` placement - tells you the question is about caching
- `tool_result` in user message - tells you the question is about the tool loop
- `system` field vs `messages` array - tells you if the snippet has a system prompt mistake
- A loop with no iteration cap - tells you the question is about agent reliability
- A hardcoded API key or a key in frontend code - tells you the question is about security

Most questions hinge on a single line. Find it, then read the rest only if needed.

---

## Common Code Bugs to Spot

1. System prompt placed as a user message
2. `tool_result` placed in the assistant message instead of user
3. Missing `max_tokens`
4. `cache_control` on the request instead of a content block
5. Stream not consumed to completion
6. Hardcoded API key in source, or an API key shipped to the browser
7. 400 errors retried in a backoff loop
8. Tool result that omits the `tool_use_id`
9. Agent loop with no iteration cap or budget
10. Model output executed or rendered without validation

---

## Answer Selection Heuristics

- Prefer SDK helpers (e.g., `messages.stream`) over manual SSE parsing when both work.
- Prefer Anthropic's documented patterns over clever workarounds.
- Prefer the cheapest model that meets the quality bar; prefer routing over one-model-for-everything.
- Prefer a code-orchestrated workflow over an agent when the steps are fixed.
- Prefer correct error categorization (retryable vs not) over universal retry.
- For structured output, prefer schema-constrained output over prompting Claude to "respond in JSON."
- For RAG with attribution, prefer the citations feature over post-hoc parsing.
- For bulk async work, prefer the Batch API over your own queue.
- For security questions, prefer architectural controls (least-privilege tools, approval gates, server-side keys) over prompt-level pleading.

---

## Domain-Specific Tactics

### Applications and Integration (33.1%)

The core. Trace streaming event order by heart: `message_start` -> per content block (`content_block_start` -> deltas -> `content_block_stop`) -> `message_delta` -> `message_stop`. System prompt in the `system` field. The API is stateless: resend full history. Honor `retry-after`; retry 429/500/529, never plain 400/401/403/404. Files: upload once, reference by `file_id`. Batch: 50% off, 24h SLA, correlate by `custom_id`.

### Model Selection and Optimization (16.8%)

Capability, latency, cost - in that order. Cache writes cost more (~1.25x, ~2x for 1-hour TTL), reads much less (~0.1x), break-even ~2 reads. Thinking spends output tokens. Token counting is model-specific and done via the API. Levers combine: caching + routing + batching + truncation.

### Agents and Workflows (14.7%)

Workflow = code decides; agent = model decides. Know prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer by name. Reliability answers mention iteration caps, budgets, circuit breakers, human approval. If the scenario has fixed steps, the answer is a workflow, not an agent.

### Prompt and Context Engineering (11.0%)

Clear instructions beat clever tricks. Stable content first (cache-friendly), volatile content last. Tool descriptions are prompts. Examples steer format. Long histories get truncated or summarized.

### Tools and MCPs (10.6%)

`tool_use` in assistant message; `tool_result` in user message, always with `tool_use_id`, all results in one user turn. `is_error: true` for failures. `tool_choice` modes: auto, any, specific tool, none. MCP is the open protocol for connecting models to external tools and data; servers expose tools, clients (like Claude Code) consume them.

### Security and Safety (8.1%)

Keys server-side in env vars or secret managers. Injection: untrusted content is data; least-privilege tools; approval gates. Validate at boundaries. Handle `refusal` before reading content. Keep PII out of prompts, metadata, and logs where possible.

### Claude Code (3.1%)

CLAUDE.md = persistent project context. settings.json = permissions. Hooks = deterministic shell commands on lifecycle events. MCP servers add tools. `claude -p` = headless. Do not over-study; this is one or two questions.

### Eval, Testing, and Debugging (2.6%)

Exact match for labels, code graders for checkable properties, LLM-as-judge (with a rubric, validated) for subjective quality. Evals run as regression suites on every prompt or model change. Tool-call debugging: check descriptions, schemas, and `tool_use_id` pairing.

---

## The 24 Hours Before

- Re-read the fact sheet
- Re-read this strategy
- Run one of your own Claude apps end to end as muscle memory
- Check current model names and pricing on docs.anthropic.com
- Sleep
- Have ID ready; for online proctoring, test your webcam, network, and room setup per Pearson VUE's requirements

---

## During the Exam

- Read the entire question; the constraint is often in the last sentence
- Skim the code; find the diff vs idiomatic
- Eliminate two answers fast
- Choose the most documented pattern between the remaining
- On multiple-response items, the required number of selections is stated; do not over- or under-select

---

## If You Fail

Score reports show domain-level performance. Rebuild the weakest domain, respecting the retake waits (14 days after attempt 1, 30 after attempt 2, 90 after attempt 3; max 4 attempts per rolling 12 months). Failing once at the edge of competence is normal.
