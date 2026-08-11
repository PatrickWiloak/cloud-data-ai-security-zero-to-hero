---
last-updated: 2026-08-11
---

# CCDV-F - 5-Week Practice Plan

Daily commitment: 1.5-2 hours weekdays, 3-4 hours one weekend day. Total: ~55 hours.

This plan is hands-on. Every week ends with code you can run. Weeks are ordered by the exam blueprint: Applications and Integration (33.1%) gets the most time, Claude Code and evals (under 6% combined) get a focused day, not a week.

---

## Week 1 - Messages API and Streaming (Domain 1)

- [ ] Read `notes/01-claude-api-fundamentals.md` and `notes/02-messages-api-and-streaming.md`
- [ ] Set up `ANTHROPIC_API_KEY` in your environment
- [ ] Install the Python SDK and TypeScript SDK
- [ ] Send a basic Messages request from both SDKs
- [ ] Inspect the response: content blocks, usage, stop_reason
- [ ] Implement streaming. Print tokens as they arrive.
- [ ] Catch and reassemble all SSE event types: message_start, content_block_start/delta/stop, message_delta, message_stop
- [ ] Handle a `pause_turn` scenario by logging it
- [ ] Write a 30-line CLI that takes a prompt and streams the response

Deliverable: a CLI that streams from the current Sonnet model.

---

## Week 2 - Tool Use and MCP (Domains 5 and 3)

- [ ] Read `notes/03-tool-use-function-calling.md`
- [ ] Define a single tool (e.g., `get_weather`) and call it via `auto` choice
- [ ] Walk through the tool_use / tool_result lifecycle by hand
- [ ] Implement parallel tool use: define two independent tools and confirm Claude calls both in one turn
- [ ] Use structured output (schema-constrained) for JSON extraction
- [ ] Implement an agent loop that runs until `end_turn` with an iteration cap
- [ ] Add a structured error response (`is_error: true`) and observe Claude recovering
- [ ] Try `tool_choice: any` and `tool_choice: {type: "tool", name: "X"}`
- [ ] Connect one MCP server (local or remote) and call one of its tools; skim the MCP architecture at modelcontextprotocol.io

Deliverable: a tool-use agent with at least 3 tools, including one error path and one MCP-sourced tool.

---

## Week 3 - Caching, Batch API, Files, Model Selection (Domains 2 and 1)

- [ ] Read `notes/04-prompt-caching-and-batch-api.md`, `notes/05-files-api-citations-and-pdfs.md`, and `notes/08-model-selection-and-optimization.md`
- [ ] Add `cache_control` to a 30K-token system prompt; verify `cache_creation_input_tokens` and `cache_read_input_tokens` in usage
- [ ] Compute cache ROI on a synthetic 100-request workload
- [ ] Try the 1-hour cache TTL and reason about when it beats the 5-minute default
- [ ] Submit a batch of 100 requests via the Batch API; poll until complete; retrieve results by `custom_id`
- [ ] Handle per-item batch errors gracefully
- [ ] Upload a PDF via the Files API and reference it by file_id in two requests
- [ ] Enable citations on a multi-document request and inspect the citation spans
- [ ] Run the same classification task on Haiku, Sonnet, and Opus; compare cost, latency, and accuracy
- [ ] Build a tiny model router: cheap model for easy inputs, capable model for hard ones
- [ ] Use the token counting endpoint to pre-price a large prompt

Deliverable: a "doc Q&A" app with cached system prompt, PDF input, citations, and a cost comparison table across model tiers.

---

## Week 4 - Agents, Error Handling, Security (Domains 3, 6, and 1)

- [ ] Read `notes/09-agents-and-workflows.md` and `notes/06-error-handling-rate-limits-retries.md`
- [ ] Implement two workflow patterns by hand: prompt chaining and routing
- [ ] Extend your Week 2 agent: iteration cap, token budget ceiling, circuit breaker on repeated identical tool calls
- [ ] Add a human-in-the-loop gate on one destructive tool
- [ ] Implement exponential backoff with jitter for 429, 500, 529; honor `retry-after`
- [ ] Distinguish retryable from non-retryable errors with typed SDK exceptions
- [ ] Read the security half of `notes/10-security-safety-claude-code-and-evals.md`
- [ ] Red-team your own agent: put an injection instruction inside a tool result and watch what happens; then add defenses
- [ ] Validate one tool's model-supplied path/parameter as untrusted input
- [ ] Add structured logging: model, tokens, latency, stop_reason, tool calls

Deliverable: a hardened agent with retries, budgets, an approval gate, and a documented injection test.

---

## Week 5 - Claude Code, Evals, Review (Domains 7, 8, and review)

- [ ] Read the Claude Code and evals parts of `notes/10-security-safety-claude-code-and-evals.md` and `notes/07-sdks-python-typescript-and-cli.md`
- [ ] Use Claude Code on a real repo: write a CLAUDE.md, adjust permissions in settings, add one hook, configure one MCP server
- [ ] Run Claude Code headless (`claude -p`) once
- [ ] Build a 20-case eval set for your Week 3 app: exact-match grader for the classification path, LLM-as-judge with a rubric for one open-ended path
- [ ] Run the eval suite before and after a prompt change; record the score delta
- [ ] Compare Python sync, Python async, and TypeScript SDK ergonomics for the same feature
- [ ] Re-read all notes and the fact sheet
- [ ] Walk through every scenario in `scenarios.md` under timed conditions
- [ ] Work the [practice questions](../../../resources/practice-questions/anthropic-claude-developer-foundations.md)
- [ ] Re-read `strategy.md` the night before
- [ ] Verify current model IDs, pricing, and your Pearson VUE appointment logistics

Deliverable: ready to sit the exam.

---

## Hands-On Project Ideas (Pick One)

1. PDF Q&A bot: upload via Files API, cache system prompt, citations enabled, streaming UI.
2. Structured extractor: read invoices/contracts and produce schema-validated JSON.
3. Backfill enrichment job: 10K records via Batch API with cache, idempotent retries.
4. Customer support agent: 5-tool agent with routing, parallel tool use, approval gate, hardened retries.
5. Eval harness: version-controlled test set with exact-match, code, and LLM-judge graders wired into CI.

---

## Red Flags - Do Not Sit the Exam Yet If

- You cannot describe every SSE event type and its payload
- You have never used `cache_control` and verified the `usage` accounting
- You have never run a tool loop end to end
- You have never used the Batch API
- You cannot name the five workflow patterns or say when an agent is the wrong choice
- You cannot explain the cache write/read economics or the model-routing cost lever
- You cannot describe two prompt-injection defenses beyond "tell the model to be careful"
- Your retry logic does not honor `retry-after`
- You do not know what CLAUDE.md, hooks, and an LLM-as-judge grader are
