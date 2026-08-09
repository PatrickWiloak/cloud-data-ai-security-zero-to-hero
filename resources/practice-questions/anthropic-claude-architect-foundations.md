---
last-updated: 2026-08-09
difficulty: intermediate
---

# Claude Architect Foundations (Self-Directed Track) - Practice Questions

15 questions for the Claude Architect Foundations track, weighted toward agentic architecture (27%), Claude Code configuration (20%), prompt engineering and structured output (20%), tool design and MCP (18%), and context and reliability (15%).

This is a self-directed study track rather than an Anthropic exam. Verify API details against the current documentation.

> **Cert page:** [exams/anthropic/claude-certified-architect-foundations/](../../exams/anthropic/claude-certified-architect-foundations/)

---

### Question 1
**Scenario:** A team wants to know whether their task warrants an agent.

A. Always build an agent
B. Check four things: is the task multi-step and hard to specify in advance, does the outcome justify higher cost and latency, is the model capable at it, and can errors be caught and recovered
C. Build an agent if the task uses tools
D. Agents are for chat only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Complexity, value, viability, and cost of error are the four gates. A "no" on any of them means staying at a simpler tier: a single call for classification or extraction, or a code-controlled workflow where you own the branching.
</details>

---

### Question 2
**Scenario:** Which describes the tiers from simplest to most complex?

A. Agent, workflow, single call
B. Single LLM call, workflow with code-controlled logic, agent with a model-driven loop
C. They are equivalent
D. Workflow, agent, single call

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Default to the simplest tier that meets the need. The distinction between a workflow and an agent is who decides the next step: your code in a workflow, the model in an agent. Model-driven control flow is what buys adaptability and what costs predictability.
</details>

---

### Question 3
**Scenario:** A custom-tool agent is being built and the team is writing the request-execute-loop by hand.

A. That is the only option
B. The SDK's tool runner drives the loop for you and still exposes per-turn hooks for approval gates, error interception, result modification, and retries
C. Hand-writing the loop gives more control in every case
D. Loops are not needed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** "I need control" is rarely a reason to hand-roll: the runner yields the assistant message before tools execute, so approval gating and interception fit inside it. Write the loop yourself only for control the runner genuinely does not expose.
</details>

---

### Question 4
**Scenario:** The team confuses the Tool Runner with the Claude Agent SDK.

A. They are the same
B. The Tool Runner is a helper in the regular API SDK that loops over tools you define; the Claude Agent SDK is a separate library packaging the Claude Code harness with built-in file, bash, and search tools
C. The Agent SDK has no tools
D. The Tool Runner hosts your compute

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Both supply a harness and leave deployment to you; the difference is scope. The Tool Runner has no built-in tools and no filesystem access. Managed Agents is the third option, where Anthropic runs both the loop and a per-session sandbox.
</details>

---

### Question 5
**Scenario:** Should an action be a bash command or a dedicated tool?

A. Always bash for flexibility
B. Start with bash for breadth; promote to a dedicated tool when you need to gate, render, audit, or parallelize that specific action
C. Always dedicated tools
D. It makes no difference

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A bash tool gives your harness one opaque string for every action, so it cannot tell a parallel-safe search from a destructive push. A dedicated tool gives typed arguments the harness can intercept, confirm, or run concurrently.
</details>

---

### Question 6
**Scenario:** A tool description is one vague sentence and its parameters have no descriptions.

A. Fine, the schema is enough
B. Under-described: tool descriptions are the biggest factor in tool performance, so write several sentences covering what it does, when to use it, when not to, and what each parameter means
C. Shorter is always better
D. Add urgent capitalized instructions

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Under-description is the more common failure than over-description, and being prescriptive about *when* to call a tool measurably improves selection. What does not belong in a description is behavioral steering or worked examples; those go in the system prompt or a skill.
</details>

---

### Question 7
**Scenario:** MCP in one sentence.

A. A model architecture
B. An open protocol for exposing tools, prompts, and resources to a model through a standard server interface
C. A prompt format
D. A hosting platform

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** MCP standardizes the integration surface so a tool written once works across clients. The API's MCP connector requires two halves together: `mcp_servers` declaring the connection, and a matching `mcp_toolset` entry in `tools` referencing it by name.
</details>

---

### Question 8
**Scenario:** A prompt must produce guaranteed-valid JSON.

A. Prefill the assistant turn with an opening brace
B. Structured outputs with a JSON schema
C. Ask politely and retry on parse failure
D. A stop sequence

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Prefilling was the older technique and now returns a 400 on current models. When migrating a prompt off it, the surrounding machinery goes too: the stop sequences, the regex extraction, and the retry-on-parse-failure loop all existed to serve the old mechanism.
</details>

---

### Question 9
**Scenario:** A system prompt carried over from an older model is full of "CRITICAL: You MUST" instructions and the model now overtriggers a tool.

A. Add more emphasis
B. Dial the language back to plain statements; current models follow the system prompt closely, so emphasis written to overcome older reluctance now over-applies
C. Remove the tool
D. Lower the temperature

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** When every instruction is marked critical, the markers stop carrying information, and an anxious prompt produces a hedging model. Emphasis is a tested fix for one demonstrably underweighted instruction, not a default register.
</details>

---

### Question 10
**Scenario:** Where should thinking depth be controlled?

A. By instructing "think step by step" in the prompt
B. Through configuration: adaptive thinking plus the effort parameter
C. By raising `max_tokens`
D. It cannot be controlled

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** On thinking models the prose incantation is redundant, and instructions to think or not to think are prompt cruft worth deleting. Effort is the configured control, and it also affects tool-use rate and how far the model scopes its work.
</details>

---

### Question 11
**Scenario:** A long-running agent's context window fills with old tool results.

A. Restart the conversation
B. Context editing to clear stale tool results, compaction to summarize when near the limit, and memory for state that must survive the session
C. Raise `max_tokens`
D. Delete the oldest messages arbitrarily

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The three operate at different scopes: editing prunes within a session, compaction summarizes within a session, memory persists across sessions. Many long-running agents use all three. Arbitrary truncation breaks tool-use pairing and thinking-block ordering.
</details>

---

### Question 12
**Scenario:** An agent's prompt cache keeps missing after the team added a mode switch that edits the system prompt mid-session.

A. Accept the cost
B. Editing the system prompt changes the front of the prefix and invalidates everything; on supporting models, append a system-role message to `messages` instead so the cached history survives
C. Disable caching
D. Add more breakpoints

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Render order is tools, then system, then messages, so anything appended after the cached history leaves it intact. Changing the tool set or the model invalidates the cache in the same way; use tool search or a subagent respectively to avoid it.
</details>

---

### Question 13
**Scenario:** An agent loop must not run forever.

A. Trust the model to stop
B. Bound it: maximum iterations, a wall-clock timeout, a token budget, and detection of repeated states
C. Increase the context window
D. Use a larger model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Non-termination is the default failure mode of an agent loop, and the model's own judgment about being finished is not a control. Server-side tool loops add a related case: a turn can stop with `pause_turn`, which you resume by re-sending rather than treating as complete.
</details>

---

### Question 14
**Scenario:** A repository uses a `CLAUDE.md` and skill files.

A. They are documentation for humans only
B. They are context loaded into the model's working set, so every paragraph is paid for on use and should carry information only the author knows
C. Longer is always better
D. They replace the system prompt

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The deletion test is whether the model could already know it. Keep the audience, environment facts, quality bar, and tool contracts; remove restatements of trained defaults and workarounds for failures the current model no longer has.
</details>

---

### Question 15
**Scenario:** A tool with side effects, such as sending email, is exposed to an agent.

A. Trust the loop
B. Validate inputs and gate destructive or irreversible actions behind confirmation, whether you use the tool runner or a manual loop
C. Add a warning to the system prompt
D. Log the calls and review later

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The tool executes automatically whenever the model requests it, so the gate has to be in code. With the runner you gate inside the tool function or intervene on the yielded message before it executes; the system prompt is advisory and injected content can compete with it.
</details>

---

## Where to go deeper

- [Claude Architect Foundations track page](../../exams/anthropic/claude-certified-architect-foundations/) - notes, practice plan, strategy
- [Claude Architect Advanced practice questions](./anthropic-claude-architect-advanced.md) - the next level
- [Agentic loops](../../learn/concepts/agentic-loops.md) - the loop in plain English
- [MCP explained](../../learn/concepts/mcp-explained.md) - the protocol
- **[📖 Claude agents and tools documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)** - primary source
