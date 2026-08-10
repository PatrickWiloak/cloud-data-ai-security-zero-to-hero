---
last-updated: 2026-08-09
difficulty: intermediate
---

# Claude Application Developer (Self-Directed Track) - Practice Questions

15 questions for the Claude Application Developer track, weighted toward the Messages API and streaming (22%), tool use (20%), prompt caching and the Batch API (16%), then files and multimodal, and error handling.

This is a self-directed study track rather than an Anthropic exam. Verify API details against the current documentation, which changes faster than any study guide.

> **Cert page:** [exams/anthropic/claude-application-developer/](../../exams/anthropic/claude-application-developer/)

---

### Question 1
**Scenario:** A conversation must continue across several turns. What does the application send on each request?

A. Only the newest user message; the API remembers the rest
B. The full conversation history, since the Messages API is stateless
C. A session ID
D. A conversation token

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Messages API holds no server-side conversation state, so the client sends the entire `messages` array every time. The first message must be from the user, and the practical consequences are that history length drives cost and that prompt caching is what makes resending affordable.
</details>

---

### Question 2
**Scenario:** A response comes back with `stop_reason: "max_tokens"`.

A. The model refused
B. The output hit the `max_tokens` ceiling and is truncated; raise the limit or stream
C. The context window was exceeded
D. A stop sequence matched

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `max_tokens` is a hard cap on generated output, so a response ending this way is incomplete. Distinguish it from `end_turn` (finished naturally), `tool_use` (wants a tool result), `pause_turn` (server-side tool loop paused, re-send to resume), and `refusal`.
</details>

---

### Question 3
**Scenario:** The model returns a `tool_use` block. What must the next request contain?

A. Just the tool's output as plain text
B. The assistant turn including the `tool_use` block, followed by a user turn whose content is a `tool_result` block carrying the matching `tool_use_id`
C. A new conversation
D. The tool definition again only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The `tool_use_id` is what pairs the result to the request, and the assistant turn must be appended intact so the model sees its own call. Dropping the assistant turn or omitting the ID produces an error rather than a graceful recovery.
</details>

---

### Question 4
**Scenario:** One assistant turn contains three `tool_use` blocks.

A. Answer them one at a time in three separate user messages
B. Execute all three and return all three `tool_result` blocks in a single user message
C. Only the first is valid
D. Parallel tool use is not supported

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Parallel tool use is on by default, and results must be returned together in one user turn. Splitting them across messages trains the model away from making parallel calls, which quietly costs you latency later. `disable_parallel_tool_use` turns the behavior off if you need one call per turn.
</details>

---

### Question 5
**Scenario:** A tool execution fails.

A. Omit the result
B. Return a `tool_result` block with `is_error: true` and a message describing the failure
C. Throw an exception to the user
D. Retry silently forever

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Returning the error as a tool result lets the model adapt, either by retrying differently or by explaining to the user. Omitting the result leaves an unanswered `tool_use` block, which the API rejects.
</details>

---

### Question 6
**Scenario:** Prompt caching is enabled but `cache_read_input_tokens` is always zero across identical-looking requests.

A. Caching is broken
B. Something in the prefix changes every request: a timestamp, a UUID, non-deterministic JSON key order, or a varying tool set
C. The model does not support caching
D. The cache TTL is too long

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Caching is a prefix match on exact bytes, so one changed character invalidates everything after it. The render order is tools, then system, then messages, so a per-request value injected into the system prompt destroys the whole cache. Move volatile content after the last breakpoint.
</details>

---

### Question 7
**Scenario:** Where should a `cache_control` breakpoint go when many requests share a long preamble but differ in the final question?

A. On the last block of the whole prompt
B. On the last block of the shared preamble, leaving the varying question uncached
C. On every block
D. On the first block

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A breakpoint after the varying part writes a distinct cache entry per request and is never read. Placing it at the end of the shared portion is what produces hits. A request allows at most four breakpoints.
</details>

---

### Question 8
**Scenario:** The economics of prompt caching.

A. Cache writes are free
B. Cache reads cost about 0.1x base input price; writes cost about 1.25x for the 5-minute TTL and about 2x for the 1-hour TTL
C. Caching always saves money on the first request
D. There is no TTL

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The write premium is why caching a prefix used once loses money. With the 5-minute TTL the break-even is around two requests; the 1-hour TTL costs more to write and needs more reads to pay off, but survives gaps in bursty traffic.
</details>

---

### Question 9
**Scenario:** 50,000 classification requests must run overnight at the lowest cost.

A. Send them in parallel to the Messages API
B. The Message Batches API, which processes asynchronously at 50% of standard pricing
C. One request with all inputs concatenated
D. Reduce `max_tokens`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Batches trade latency for a 50% discount, accepting up to 100,000 requests or 256 MB per batch, usually completing within an hour and always within 24. Poll `processing_status` until `ended`, then stream the results.
</details>

---

### Question 10
**Scenario:** Batch results come back and the application matches them to inputs by position.

A. This is correct
B. Results can arrive in any order; key them by `custom_id`
C. Results are always sorted
D. Position matching is faster

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `custom_id` exists precisely because ordering is not guaranteed. Each result also carries a `result.type` of succeeded, errored, canceled, or expired, so the handler needs a branch for each rather than assuming success.
</details>

---

### Question 11
**Scenario:** The same PDF is queried in twenty separate requests.

A. Base64-encode it into every request
B. Upload it once with the Files API and reference it by `file_id` in a `document` content block
C. Extract the text manually
D. Split it into pages

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Uploading once avoids re-sending the bytes on every call, and the file persists until deleted. Note the tokens are still billed as input each time the document is included, so pair it with prompt caching if the document sits in a stable prefix.
</details>

---

### Question 12
**Scenario:** The application needs guaranteed schema-valid JSON.

A. Ask for JSON in the prompt and parse defensively
B. Use structured outputs via `output_config.format` with a JSON schema, ideally through the SDK's parse helper
C. Prefill the assistant turn with an opening brace
D. Use a regular expression

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Constrained decoding removes the class of failures where the model wraps JSON in prose. Assistant-turn prefilling, the old technique for this, now returns a 400 on current models, so structured outputs is the replacement rather than an alternative.
</details>

---

### Question 13
**Scenario:** A 429 response arrives under load.

A. Fail the request
B. The SDKs retry 429 and 5xx automatically with backoff; honor the `retry-after` header for custom logic, and use the typed `RateLimitError` rather than string-matching the message
C. Retry immediately in a tight loop
D. Switch to a different API key

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Each SDK exposes a typed exception per status code, which is what lets you distinguish retryable failures (429, 5xx, connection errors) from non-retryable ones (400, 404). Immediate retries make an overload worse.
</details>

---

### Question 14
**Scenario:** A long response should appear to the user progressively.

A. Poll for the result
B. Stream the response and consume `content_block_delta` events, using the SDK's final-message helper if you also need the complete object
C. Reduce `max_tokens`
D. Split into several requests

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Streaming also matters operationally: large `max_tokens` values on non-streaming requests risk HTTP timeouts, so streaming is the recommended path for long outputs regardless of whether the UI displays tokens as they arrive.
</details>

---

### Question 15
**Scenario:** A cost estimate is needed before sending a large prompt.

A. Estimate with a character count
B. Call the token counting endpoint with the same model and messages, since token counts are model-specific
C. Use a third-party tokenizer
D. Send it and read the response usage

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Counting must use the model you will actually call, because tokenizers differ between model generations. Third-party tokenizers built for other providers materially undercount Claude tokens, particularly on code and non-English text.
</details>

---

## Where to go deeper

- [Claude Application Developer track page](../../exams/anthropic/claude-application-developer/) - notes, practice plan, strategy
- [Claude Architect Foundations practice questions](./anthropic-claude-architect-foundations.md) - the architecture track
- [Tool use and function calling](../../learn/concepts/tool-use-and-function-calling.md) - the mechanism in plain English
- [Prompt caching](../../learn/concepts/prompt-caching.md) - the cost lever in depth
- **[📖 Claude API documentation](https://platform.claude.com/docs/en/api/overview)** - primary source
