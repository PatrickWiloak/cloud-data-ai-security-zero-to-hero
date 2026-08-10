---
last-updated: 2026-08-09
difficulty: advanced
---

# Claude Architect Advanced (Self-Directed Track) - Practice Questions

15 questions for the Claude Architect Advanced track, weighted toward advanced and multi-agent architectures (22%), context engineering (18%), tool use and MCP at scale (17%), then evaluation and safety, cost and latency, and enterprise deployment.

This is a self-directed study track rather than an Anthropic exam. Verify API details against the current documentation.

> **Cert page:** [exams/anthropic/claude-certified-architect-advanced/](../../exams/anthropic/claude-certified-architect-advanced/)

---

### Question 1
**Scenario:** A research task splits into six independent sub-questions, each requiring heavy reading.

A. One long single-threaded loop
B. Delegate each sub-question to a subagent so each gets a fresh context window and only the reports return to the coordinator
C. Increase the context window
D. Run six separate applications

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Fan-out is the case delegation is for: parallel threads, independent contexts, and a coordinator whose context stays small because it reads reports rather than raw material. The cost is a round trip and a re-briefing per delegation, so it is wrong for a task you could finish in a few tool calls.
</details>

---

### Question 2
**Scenario:** A coordinator delegates reading-heavy work while keeping planning and synthesis.

A. Every agent should use the same model
B. Put the reading-heavy work on a smaller, cheaper model and keep the large model for planning, verification, and synthesis
C. Only the largest model can be a subagent
D. Model choice does not matter

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Delegated research is mostly search, read, and extract: many input tokens, little hard reasoning. Each agent bills at its own model's rates, so this split is one of the largest cost levers available in a multi-agent design.
</details>

---

### Question 3
**Scenario:** A subagent needs information the coordinator discovered.

A. It inherits the coordinator's conversation
B. Threads share the container filesystem but not conversation history, so every delegated task must carry the paths, constraints, and expected report format it needs
C. It can query the coordinator's context
D. Context is automatic

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Assuming shared context is the most common multi-agent design error. The brief has to be self-contained, which is also why briefing precisely the first time beats launching, waiting, and re-briefing.
</details>

---

### Question 4
**Scenario:** Prompt caching is designed for an agent whose model must change mid-session for a cheap sub-task.

A. Switch the model on the same conversation
B. Caches are model-scoped, so switching invalidates everything; spawn a subagent on the cheaper model and keep the main loop on one model
C. Add a breakpoint before the switch
D. Use a longer TTL

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Three things invalidate the whole prefix: changing the tool set, changing the model, and editing the system prompt. Each has a workaround: tool search appends rather than swaps, a subagent isolates the model change, and a system-role message in `messages` leaves the cached history intact.
</details>

---

### Question 5
**Scenario:** An agent has 200 tools available but only a few are relevant per request.

A. Load every schema on every request
B. Tool search with deferred loading, so only relevant schemas enter context and discovered tools are appended rather than swapped
C. Split into 200 agents
D. Shorten the descriptions

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The appended-not-swapped property is what preserves the prompt cache, which is why tool search is the scaling answer rather than rebuilding the tool array per request. Note the search tool itself must not be deferred, and at least one tool must remain non-deferred.
</details>

---

### Question 6
**Scenario:** Claude chains five tool calls, each returning a large payload that is filtered and discarded.

A. Accept the token cost
B. Programmatic tool calling: Claude writes a script in the code execution container that invokes the tools, processes results with normal control flow, and returns only the final output to context
C. Use a bigger context window
D. Batch the calls

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** With standard tool use every intermediate result lands in context and costs tokens forever after. PTC keeps the intermediate data in the running script, so token cost scales with the final output rather than with everything the tools returned.
</details>

---

### Question 7
**Scenario:** An indirect prompt injection arrives in a document the agent retrieved.

A. Filter the input for suspicious phrases
B. Assume it may succeed: scope each tool's credential narrowly, check authorization against the calling user in code at the tool boundary, require confirmation for irreversible actions, and treat model output as untrusted downstream
C. Instruct the model to ignore instructions in documents
D. Use a larger model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** No classifier reliably separates instructions from data in natural language, so the design goal is bounding the consequence. The tool boundary is the last non-model control that can refuse, which is why authorization belongs there rather than in the prompt.
</details>

---

### Question 8
**Scenario:** An agent's behavior must be debuggable three days after a bad run.

A. The final output
B. Full tracing: every prompt, tool call with arguments, observation, and decision, correlated by a trace ID
C. Ask the model to explain what happened
D. Application logs only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A wrong answer is usually a retrieval or observation problem, invisible from the output. A post-hoc explanation from the model is a plausible narrative reconstructed from the same context, not a record of what happened.
</details>

---

### Question 9
**Scenario:** An agent must be evaluated before production.

A. Final-answer accuracy
B. Trajectory-level evaluation: task success, tool-call correctness, steps to completion, and cost, plus adversarial and injection cases, run on every prompt or model change
C. Latency only
D. Published benchmark scores

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Final-answer accuracy hides agents that reach the right answer through unsafe or wasteful paths. Running the suite on prompt edits as well as model upgrades matters because both change behavior, and injection resistance in particular regresses silently.
</details>

---

### Question 10
**Scenario:** Cost per task is far higher than modeled.

A. Use a smaller model everywhere
B. Measure tokens per step, cache the stable prefix, cap loop iterations, route simple steps to cheaper models, and check whether context has grown with stale tool results
C. Reduce the user base
D. Increase the context window

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Agent cost is loop length multiplied by per-step context size, so both need attention. The system prompt and tool definitions repeat on every step, which is why prefix caching is usually the single largest saving, and context editing is what stops the per-step size growing unbounded.
</details>

---

### Question 11
**Scenario:** A long conversation approaches the context window limit.

A. Truncate the oldest messages
B. Server-side compaction, appending the full response content back on every turn so the compaction blocks are preserved
C. Start a new conversation
D. Increase `max_tokens`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The trap is appending only the extracted text: the compaction block is what the API uses to replace the compacted history on the next request, so dropping it silently loses the state. Arbitrary truncation additionally breaks tool-use pairing.
</details>

---

### Question 12
**Scenario:** An enterprise requires that model inference run on their cloud provider's infrastructure.

A. Only the first-party API is available
B. Claude is available on Amazon Bedrock, Google Vertex AI, and Microsoft Foundry, each with its own client class and its own feature availability
C. All platforms are identical
D. Only Bedrock exists

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Availability differs per feature and per platform, so the architecture question is which capabilities the design depends on. Model IDs also differ: Bedrock prefixes them, Vertex uses bare IDs with its own version separator for dated snapshots.
</details>

---

### Question 13
**Scenario:** An agent should persist learnings across sessions.

A. Longer context windows
B. A memory surface it can read and write, with guidance on what to record and what not to duplicate
C. Compaction
D. A larger system prompt

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Memory is the cross-session mechanism; context editing and compaction operate within one. The design detail that matters is telling it *when* to consult and write memory: agents under-reach for capabilities that need an explicit decision to use them.
</details>

---

### Question 14
**Scenario:** The team wants Anthropic to run the agent loop and host the tool-execution sandbox.

A. That is not offered
B. Managed Agents: a persisted, versioned agent config plus sessions that each get a container, with an event stream you drive
C. The Tool Runner does this
D. The Agent SDK does this

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Tool Runner and the Agent SDK both supply a harness and leave hosting to you; Managed Agents supplies both. The versioning is the reason agents are separate objects: sessions pin to a version, so you can iterate without breaking runs in flight.
</details>

---

### Question 15
**Scenario:** A safety layer must constrain what the agent will do.

A. A word blocklist
B. Layered controls with measurement of both violation rate and false refusal rate
C. Lower temperature
D. Shorter responses

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Safety is a trade-off curve, so measuring only violations optimizes toward an over-blocking product that fails a different way. Blocklists sit badly on both axes: trivially evaded, and prone to catching benign text.
</details>

---

## Where to go deeper

- [Claude Architect Advanced track page](../../exams/anthropic/claude-certified-architect-advanced/) - notes, practice plan, strategy
- [Claude Architect Foundations practice questions](./anthropic-claude-architect-foundations.md) - the level below
- [Agent and tool security](../ai-security/agent-security.md) - question 7 in depth
- [Prompt injection defense](../ai-security/prompt-injection-defense.md) - the attack and the controls
- **[📖 Claude agents and tools documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)** - primary source
