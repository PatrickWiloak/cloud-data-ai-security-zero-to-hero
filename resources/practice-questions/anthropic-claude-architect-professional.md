---
last-updated: 2026-08-11
difficulty: advanced
---

# Claude Certified Architect - Professional (CCAR-P) - Practice Questions

15 questions for the Claude Certified Architect - Professional (CCAR-P) exam, weighted toward the heavier blueprint domains: Integration (19%), Solution Design and Architecture (17%), Evaluation, Testing and Optimization (16%), Governance, Safety and Risk Management (14%), Stakeholder Communication and Lifecycle Management (14%), Claude Models, Prompting and Context Engineering (13%), and Developer Productivity and Operational Enablement (7%).

These are practice questions written for this repo, not real exam items. Verify API details against the current documentation.

> **Cert page:** [exams/anthropic/claude-certified-architect-professional/](../../exams/anthropic/claude-certified-architect-professional/)

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
**Scenario:** A production claims agent is pinned to a dated model snapshot. The provider announces that snapshot's deprecation with a six-month window. An engineer proposes switching to an auto-updating model alias so migrations stop being necessary.

A. Accept: auto-updating aliases eliminate migration work
B. Keep pinning; run the full eval and red-team suite on the successor snapshot, fix prompt regressions, phase it in with the old snapshot held for rollback, and notify stakeholders of behavior changes
C. Wait until the deprecation date and let the cutover happen
D. Move to a cloud platform where snapshots are never retired

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A model version change is a behavior change to the product, so it goes through the same gate as a code release: eval diff, phased rollout, rollback path, stakeholder notice. An auto-updating alias trades scheduled migrations for silent, unreviewed behavior changes, and cloud platforms retire model versions on their own schedules too.
</details>

---

### Question 3
**Scenario:** A healthcare enterprise requires that prompts and completions are never retained after the response is served, and that the deployment is covered for PHI under HIPAA.

A. Set a retention flag on each API request
B. Sign a BAA, use a HIPAA-eligible endpoint, and put a contractual zero-data-retention arrangement in place; verify the posture separately for each deployment path
C. Retention is already zero by default, so only the BAA is needed
D. Strip PHI client-side; then retention and BAA no longer matter

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ZDR is a contractual arrangement for qualified customers, not a request-time flag, and default handling permits short-term retention for abuse detection. HIPAA coverage requires a signed BAA on a HIPAA-eligible endpoint. Minimization (D) is good practice but does not satisfy a hard requirement on its own, since PHI can still reach the model in a clinical workload.
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
**Scenario:** A pilot's exit gate requires a 90% task-success score before general rollout. The pilot lands at 84%, and the executive sponsor pushes to launch anyway because a competitor just shipped.

A. Launch; the gate was only a guideline
B. Hold the pre-agreed gate: present the evidence, diagnose the top failure categories, propose a bounded remediation phase with a re-test date, and offer a narrower interim launch only if a segment already clears the gate
C. Lower the gate to 84% so the pilot passes
D. Escalate to the sponsor's manager

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Go/no-go gates exist precisely for the moment pressure and sunk cost argue for launching; agreeing on thresholds before the phase is what makes the decision evidence-based rather than political. Moving the goalposts (A, C) destroys the gate's value for every future launch. Offering a scoped alternative keeps the conversation constructive without shipping a known-failing experience.
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

- [Claude Certified Architect - Professional cert page](../../exams/anthropic/claude-certified-architect-professional/) - notes, practice plan, strategy
- [Claude Architect Foundations practice questions](./anthropic-claude-architect-foundations.md) - the level below
- [Agent and tool security](../ai-security/agent-security.md) - question 7 in depth
- [Prompt injection defense](../ai-security/prompt-injection-defense.md) - the attack and the controls
- **[📖 Claude agents and tools documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)** - primary source
