---
last-updated: 2026-08-09
difficulty: intermediate
---

# Claude Prompt Engineering Specialist (Self-Directed Track) - Practice Questions

15 questions for the Claude Prompt Engineering Specialist track, weighted toward prompt fundamentals (18%), system prompts and role (16%), reasoning elicitation (16%), then structure, examples, and evaluation.

This is a self-directed study track rather than an Anthropic exam. Prompting guidance shifts between model generations, so verify against current documentation.

> **Cert page:** [exams/anthropic/claude-prompt-engineering-specialist/](../../exams/anthropic/claude-prompt-engineering-specialist/)

---

### Question 1
**Scenario:** What belongs in a prompt, in one principle?

A. Everything that might be relevant
B. What only you know: the audience, the product, environment facts, the quality bar, constraints and their reasons
C. As few words as possible
D. Restatements of good behavior

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Context is never cruft; restating trained defaults is. "Be accurate and helpful" adds nothing, while "this goes to compliance reviewers who need the source cited" changes the output. Too-short prompts produce generic results because the model fills gaps with safe defaults.
</details>

---

### Question 2
**Scenario:** A prompt reads "CRITICAL: You MUST ALWAYS verify before answering. NEVER guess. IMPORTANT: be thorough."

A. Well-calibrated emphasis
B. Over-emphasized: when everything is marked critical the markers carry no information, and an anxious prompt produces a hedging, over-cautious model
C. Needs more emphasis
D. Correct for all models

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Forcefulness was genuinely needed on older, less steerable models. Current models follow the system prompt closely, so the same text over-applies. Emphasis is a tested, scoped fix for one demonstrably underweighted instruction, not a default register.
</details>

---

### Question 3
**Scenario:** A prompt says "try to include a summary if possible" for a summary that is actually required.

A. Fine, it is polite
B. Hedges are now read literally as permission to skip; state the requirement plainly
C. Add emphasis
D. Repeat it three times

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Over-emphasis and under-emphasis are the same defect from opposite directions, and both come from writing for a model with different steerability. Say exactly what you mean at normal volume.
</details>

---

### Question 4
**Scenario:** A prompt contains "think step by step" and instructions to use `<scratchpad>` tags.

A. Keep them for reliability
B. On thinking models these are redundant at best; control reasoning depth through adaptive thinking and the effort parameter instead
C. Add more reasoning instructions
D. They improve output on every model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** These are idioms from an era before reasoning was natively trained and configurable. Instructions telling the model *not* to reason are worse still: they can increase leakage of internal markup into the visible response rather than suppressing it.
</details>

---

### Question 5
**Scenario:** A prompt uses XML tags to delimit a document and the instructions.

A. Unnecessary
B. Useful: explicit delimiters make it unambiguous which text is data and which is instruction, especially with long inputs
C. XML tags are deprecated
D. Only JSON works

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Structural delimiting remains sound practice for separating content from instruction. What has been superseded is using tags to *force output shape*, which structured outputs now handles as a decoding constraint rather than a prompting convention.
</details>

---

### Question 6
**Scenario:** A prompt embeds one gold-standard output example.

A. Ideal
B. Risky: examples are the strongest signal in a prompt, so one example freezes its length, tone, and structure; use several deliberately varied examples labeled illustrative
C. Add more examples of the same shape
D. Examples never matter

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The model matches what it sees, so a single example becomes a template rather than an illustration. Examples written for an older model are worse: they freeze that model's behavior into the new one. Keep examples that pin a genuinely format-sensitive output.
</details>

---

### Question 7
**Scenario:** A prompt has fifteen "do not" lines.

A. Comprehensive coverage
B. Describing success beats enumerating failure, and a prohibition against a failure the model was not going to make can anchor it toward that failure
C. Add more prohibitions
D. Prohibitions are always wrong

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The test for each line is provenance: does it encode a real constraint with a reason, or is it a workaround for an older model's habit? Keep prohibitions whose failure reproduces on the current model; rewrite the rest as positive statements.
</details>

---

### Question 8
**Scenario:** A system prompt runs to 4,000 words of numbered steps for a judgment task.

A. More detail is better
B. Over-prescriptive: prompts written for prior models are often too prescriptive for current ones and reduce output quality; state outcomes, constraints, and how to verify, keeping numbered steps only where order truly matters
C. Convert it to bullets
D. Split it into two prompts

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Prompting effort should scale with how far the task is from what the model does naturally. Fragile operations where exactly one sequence is safe keep their exact scripts; open-ended judgment work does better with the goal and the constraints.
</details>

---

### Question 9
**Scenario:** A prompt says "you will be graded on completeness; there are hidden tests."

A. Effective motivation
B. It describes the scoring apparatus instead of the requirement, and pushes effort toward appearing watched; state every requirement the grader checks and never describe the grader
C. Add the rubric
D. Remove all quality language

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** If a requirement matters, say it as a requirement. Grader vocabulary is a proxy that the model optimizes toward instead of the underlying goal, which is exactly the substitution you do not want.
</details>

---

### Question 10
**Scenario:** How should a prompt change be validated?

A. Read the new output and judge it
B. An evaluation set with defined metrics, run before and after, ideally changing one thing at a time
C. Ask the model whether the prompt is good
D. Ship it and watch for complaints

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Prompting is empirical and intuitions about what helps are unreliable. Asking the model to assess its own prompt is self-report, not measurement. Changing one thing at a time is what lets a regression be attributed to its cause.
</details>

---

### Question 11
**Scenario:** A prompt embeds "current date: {today}" at the top of the system prompt.

A. Good practice for temporal grounding
B. It sits at the front of the cached prefix and invalidates everything after it on every request; inject dynamic context later in the messages instead
C. Dates cannot be provided
D. Move it to the end of the system prompt

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Caching is a prefix match, and the render order is tools, then system, then messages. Anything varying per request belongs after the last breakpoint. A message at turn five invalidates nothing before turn five.
</details>

---

### Question 12
**Scenario:** A prompt contains lines nobody can justify, added after specific incidents on a retired model.

A. Keep them, they are harmless
B. Treat them as removal candidates: prompts accumulate the union of every generation's workarounds, and specific outdated instructions actively degrade behavior
C. Add a comment explaining each
D. Rewrite them more forcefully

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The question for every emphatic line is which failure, on which model, it prevented, and whether that failure still reproduces. Removal is a hypothesis to test, not a conclusion: probe behavior before and after, and re-add in minimal form if a cut regresses.
</details>

---

### Question 13
**Scenario:** A skill's frontmatter description carries urgent language about when to invoke it.

A. Same problem as an over-emphatic system prompt
B. Different: text whose job is routing may legitimately carry calibrated urgency, since skills currently under-trigger; text whose job is behavior should explain rather than shout
C. All urgency should be removed
D. Descriptions should be one word

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Trigger text and behavioral text look identical to a search, so classify by function before editing. Ideally the trigger wording is tuned against a trigger evaluation rather than intuition.
</details>

---

### Question 14
**Scenario:** A response is longer than the product wants.

A. Add "be concise" and hope
B. Give a concrete instruction about what to include and what to drop, and prefer positive examples of the desired concision over telling the model what not to do
C. Cap the output tokens
D. Lower the effort setting

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Numeric output caps tuned against an older model's verbosity starve reasoning on hard problems, and truncate rather than shorten. Lowering effort changes reasoning depth without reliably changing visible length. Selectivity is the lever: drop what would not change what the reader does next.
</details>

---

### Question 15
**Scenario:** A prompt is being written for a new model generation.

A. Reuse the old prompt unchanged
B. Re-baseline in both directions: remove workarounds the new model no longer needs, and add guidance for its new behaviors, since prompts are per-model artifacts
C. Always shorten
D. Always lengthen

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Matching a prompt to a new model sometimes means adding text, not only cutting it. A line that is load-bearing on one generation is cruft on the next, and the reverse, which is why each model release is a trigger to re-audit rather than a reason to reuse.
</details>

---

## Where to go deeper

- [Claude Prompt Engineering Specialist track page](../../exams/anthropic/claude-prompt-engineering-specialist/) - notes, practice plan, strategy
- [Claude Architect Foundations practice questions](./anthropic-claude-architect-foundations.md) - the architecture track
- [Prompt engineering](../../learn/concepts/prompt-engineering.md) - plain-English primer
- [Structured outputs](../../learn/concepts/structured-outputs.md) - the replacement for format-forcing prompts
- **[📖 Claude prompt engineering documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)** - primary source
