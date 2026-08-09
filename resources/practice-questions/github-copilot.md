---
last-updated: 2026-08-09
difficulty: beginner
---

# GitHub Copilot Certification - Practice Questions

15 questions for the GitHub Copilot exam, weighted toward using Copilot (25%), introduction (20%), then plans and features, developer use cases, responsible use, and prompt engineering.

> **Cert page:** [exams/github/copilot/](../../exams/github/copilot/)

---

### Question 1
**Scenario:** What does Copilot use to generate a suggestion?

A. A search of public repositories at request time
B. A large language model given context from your open files, surrounding code, and prompt
C. A fixed snippet library
D. Your git history only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Suggestions are generated, not retrieved, which is why they are novel and also why they can be confidently wrong. The context sent includes the current file and related open tabs, which is why keeping relevant files open improves suggestions noticeably.
</details>

---

### Question 2
**Scenario:** A suggestion compiles and looks correct.

A. Accept it without review
B. Review it as you would a colleague's code: correctness, security, performance, and whether it fits the codebase
C. Trust it because it compiles
D. Run it in production to test

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The developer who commits the code is responsible for it. Generated code compiles far more reliably than it is correct, and the plausible-but-subtly-wrong case is the one that costs the most to find later.
</details>

---

### Question 3
**Scenario:** An organization is concerned Copilot might suggest code matching public repositories.

A. Nothing can be done
B. Enable the duplication detection filter, which blocks suggestions matching public code
C. Disable Copilot
D. Manually check every suggestion

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The filter suppresses suggestions that match public code above a length threshold, which addresses the licensing concern most legal teams raise. Copilot Business and Enterprise also carry IP indemnification when the filter is enabled, which is examinable.
</details>

---

### Question 4
**Scenario:** Copilot must not use an organization's code to train models.

A. It always trains on your code
B. Copilot Business and Enterprise do not use customer code for model training, and admins control telemetry and data retention settings
C. Only individual plans are safe
D. Training cannot be controlled

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The data handling difference between individual and business plans is a standard exam and procurement question. Knowing that prompts and suggestions are not retained for training on business plans is usually what unblocks adoption.
</details>

---

### Question 5
**Scenario:** A developer wants Copilot to write a function matching a specific behavior.

A. A vague comment
B. A specific comment or docstring stating inputs, outputs, and edge cases, plus a descriptive function name and nearby examples
C. An empty file
D. Random keystrokes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Copilot infers intent from context, so specificity in names, signatures, and comments is the main quality lever. Existing similar code in an open file acts as an implicit style example, which is why suggestions improve as a file develops.
</details>

---

### Question 6
**Scenario:** Copilot Chat is asked to explain unfamiliar code.

A. It cannot explain code
B. Select the code and ask, using slash commands such as `/explain`, `/fix`, and `/tests` for common tasks
C. Only inline completion exists
D. Copy the code to a web search

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Chat with a selection is the fastest way into unfamiliar code, and the slash commands wrap the common intents. Onboarding to a new codebase is one of the strongest documented use cases, ahead of writing brand-new code.
</details>

---

### Question 7
**Scenario:** Which Copilot capability reviews a pull request?

A. There is none
B. Copilot code review, which comments on a pull request with suggested changes
C. Secret scanning
D. Dependabot

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Copilot can review a pull request and leave suggestions, which catches straightforward issues before a human reviewer spends attention on them. It supplements human review rather than replacing the judgment about design and intent.
</details>

---

### Question 8
**Scenario:** Tests must be generated for existing code.

A. Copilot cannot write tests
B. Ask Copilot to generate tests, then review that they assert meaningful behavior and cover edge cases rather than just passing
C. Tests are always correct
D. Only the developer can write tests

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Test generation is a strong use case because the surrounding code supplies clear context. The review that matters is whether the assertions are meaningful: tests generated from an implementation can encode the current behavior, including its bugs.
</details>

---

### Question 9
**Scenario:** Copilot suggests code using a deprecated API.

A. Use it anyway
B. Verify against current documentation, since the model's knowledge has a cutoff and may predate recent changes
C. Assume it is current
D. Report it as a bug

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Training data has a cutoff, and API deprecation is exactly the kind of change that lands after it. Copilot Chat with repository or web context can help, but the documentation remains the authority for what is current.
</details>

---

### Question 10
**Scenario:** An organization wants Copilot to understand its internal codebase and standards.

A. Not possible
B. Copilot Enterprise features such as knowledge bases and repository indexing, plus repository custom instructions
C. Fine-tune the model yourself
D. Paste standards into every prompt

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Custom instructions in the repository apply automatically to Copilot's context, and Enterprise knowledge bases index documentation so chat can answer from internal sources. Both remove the need to restate context on every request.
</details>

---

### Question 11
**Scenario:** Which describes a limitation developers should know?

A. Copilot is always correct
B. It can produce code with bugs, security flaws, or licensing concerns, and it does not know your runtime state or your requirements
C. It cannot generate code
D. It only works on Python

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Being able to state the limitations is explicitly part of the responsible use domain. The one people underweight is that Copilot cannot know your requirements: it produces plausible code for the context, not correct code for your intent.
</details>

---

### Question 12
**Scenario:** Copilot must be disabled for specific file types containing secrets.

A. Not configurable
B. Content exclusions configured at repository or organization level, so Copilot ignores specified paths
C. Delete the files
D. Disable Copilot entirely

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Content exclusions stop configured paths being used as context or receiving completions, which is how you keep `.env` files and key material out of the request. It is a per-repository or organization admin setting rather than a per-developer choice.
</details>

---

### Question 13
**Scenario:** Where can Copilot be used?

A. One IDE only
B. In IDEs (VS Code, Visual Studio, JetBrains, Neovim), on GitHub.com, in the CLI, and in mobile, depending on plan
C. Only in the browser
D. Only on Windows

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Surface coverage differs by plan, and the CLI integration for shell commands plus chat on GitHub.com for pull requests and issues are the two people most often do not realize exist.
</details>

---

### Question 14
**Scenario:** A team wants to measure whether Copilot is helping.

A. Lines of code generated
B. Adoption and acceptance metrics from the Copilot metrics API, alongside outcome measures such as cycle time and developer survey results
C. Count suggestions
D. It cannot be measured

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Lines of code is a famously poor proxy that rewards verbosity. Usage metrics tell you whether people are using it; delivery and satisfaction measures tell you whether it is helping, and only the pair is meaningful.
</details>

---

### Question 15
**Scenario:** Prompt engineering for Copilot in one principle.

A. Write less
B. Give it context and specificity: clear names, a stated goal, relevant files open, and iterative refinement when the first suggestion misses
C. Use single letters
D. Prompting does not matter

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Context and specificity are the levers. Treating a poor suggestion as a signal to add detail, rather than as a failure, is the working habit that separates productive use from frustration.
</details>

---

## Where to go deeper

- [GitHub Copilot cert page](../../exams/github/copilot/) - notes, practice plan, strategy
- [GitHub Foundations practice questions](./github-foundations.md) - the platform fundamentals
- [Prompt engineering](../../learn/concepts/prompt-engineering.md) - the general skill
- [AI security topic index](../../topics/ai-security.md) - responsible use in a wider frame
- **[📖 GitHub Certifications](https://resources.github.com/learn/certifications/)** - official exam pages
