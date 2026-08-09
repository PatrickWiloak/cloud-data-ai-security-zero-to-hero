---
last-updated: 2026-08-09
difficulty: intermediate
---

# GitHub Advanced Security (GHAS) - Practice Questions

15 questions for the GHAS exam, weighted toward code scanning and CodeQL (25%), secret scanning and push protection (20%), and dependency review and Dependabot (20%).

> **Cert page:** [exams/github/advanced-security/](../../exams/github/advanced-security/)

---

### Question 1
**Scenario:** A developer tries to push a commit containing an API key.

A. The push succeeds and an alert is raised later
B. With push protection enabled, the push is blocked and the developer is prompted to remove the secret or provide a bypass reason
C. The key is encrypted automatically
D. Nothing happens

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Push protection stops the secret before it enters history, which is the only outcome that avoids rotation. Once a secret is pushed, treat it as compromised and rotate it: removing the commit does not undo the exposure, especially in a public repository.
</details>

---

### Question 2
**Scenario:** CodeQL must find injection vulnerabilities in application code.

A. It matches patterns of bad strings
B. It builds a queryable database of the code and runs semantic queries, including data flow analysis from sources to sinks
C. It runs the application
D. It checks dependencies only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Taint tracking is what distinguishes CodeQL from a regular-expression scanner: it follows untrusted input through the code to a dangerous sink, which finds real vulnerabilities and suppresses cases where the input is sanitized on the way.
</details>

---

### Question 3
**Scenario:** A code scanning alert is a false positive.

A. Delete the code
B. Dismiss the alert with a reason (false positive, used in tests, or won't fix), which is recorded and auditable
C. Disable code scanning
D. Ignore it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Dismissing with a reason keeps the alert list meaningful while preserving the decision and who made it. Disabling scanning to silence one finding removes coverage everywhere, and an unmanaged backlog quickly makes the whole tool ignored.
</details>

---

### Question 4
**Scenario:** Dependabot must open pull requests for vulnerable dependencies.

A. Dependabot alerts only
B. Enable Dependabot security updates, which open pull requests upgrading to a patched version, alongside alerts
C. Manual dependency review
D. Secret scanning

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Alerts tell you; security updates act. Version updates are the separate feature that keeps dependencies current regardless of vulnerabilities, configured in `dependabot.yml` with a schedule and grouping.
</details>

---

### Question 5
**Scenario:** A pull request adds a dependency with a known critical vulnerability.

A. It merges normally
B. Dependency review on the pull request surfaces it, and can be enforced as a required check that blocks the merge
C. Nothing detects it
D. Only after merge

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Catching it at review time is far cheaper than after merge, and the dependency review action can fail the build on a severity threshold or a disallowed license. That turns policy into a gate rather than a report.
</details>

---

### Question 6
**Scenario:** Code scanning must run on a schedule as well as on pull requests.

A. Pull requests only
B. Configure the workflow with `pull_request`, `push` to the default branch, and a `schedule` trigger, since new queries can find issues in unchanged code
C. Manual runs only
D. Once at setup

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The CodeQL query pack is updated over time, so a scheduled scan finds newly discoverable issues in code that has not changed. Pull request scanning gives fast feedback on new code; the schedule covers the rest of the repository.
</details>

---

### Question 7
**Scenario:** A monorepo has code in several languages.

A. CodeQL scans all languages automatically in one run
B. Configure a matrix with one analysis per supported language, since CodeQL databases are per-language
C. Only one language can be scanned
D. Use secret scanning instead

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Each language gets its own database and query suite, which is why the default workflow uses a matrix. Compiled languages may also need a build step, either autobuild or explicit build commands, for the database to be complete.
</details>

---

### Question 8
**Scenario:** Scanning results from a third-party tool must appear in the GitHub security tab.

A. It is not possible
B. Upload results in SARIF format, which the code scanning API accepts from any tool
C. Only CodeQL is supported
D. Paste them into an issue

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SARIF is the interoperability format, so linters, SAST tools, and container scanners can all feed the same alert experience with deduplication and pull request annotations. This is what makes code scanning a hub rather than a single tool.
</details>

---

### Question 9
**Scenario:** A secret was pushed and is now in git history.

A. Delete the commit and consider it resolved
B. Rotate the credential first, then optionally rewrite history; assume it was harvested
C. Make the repository private
D. Add it to `.gitignore`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Automated scrapers find secrets in public repositories within minutes, so rotation is the only reliable remediation and it comes first. History rewriting is cleanup; it does not recall what was already cloned or indexed.
</details>

---

### Question 10
**Scenario:** GHAS must be rolled out across a large enterprise without overwhelming teams.

A. Enable everything everywhere at once
B. Phase it: start with secret scanning and push protection, then dependency management, then code scanning per language, with an owner for triage at each stage
C. Enable code scanning only
D. Leave it to individual teams

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Secret scanning has the highest signal-to-noise ratio and needs the least developer effort, which builds credibility. Turning on everything at once produces a backlog nobody triages, and an ignored alert list is worse than no scanning because it looks like coverage.
</details>

---

### Question 11
**Scenario:** Which explains secret scanning's partner program?

A. Secrets are shared with partners
B. When a partner's credential pattern is detected in a public repository, GitHub notifies the provider so they can revoke it
C. Partners write the scanner
D. It applies only to private repositories

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Provider notification means many leaked tokens are revoked before an attacker uses them, which is a meaningful safety net. It applies to public repositories, so private repository scanning depends on your own alerting and response.
</details>

---

### Question 12
**Scenario:** A custom CodeQL query must encode an organization-specific rule.

A. Not supported
B. Write a custom query or query pack in QL and include it in the code scanning configuration
C. Use a regular expression in CI
D. Ask GitHub

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Custom queries let you encode internal rules such as banned APIs or required wrappers, with the same data flow capability as the built-in suites. Query packs make them distributable across repositories.
</details>

---

### Question 13
**Scenario:** A vulnerability is found in a repository's own code and must be fixed privately.

A. Open a public issue
B. A private repository security advisory, with a temporary private fork for collaboration, then publish a CVE when the fix is released
C. Fix it silently
D. Email everyone

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Advisories provide private collaboration space until a fix is available, and publishing adds the advisory to the GitHub Advisory Database so downstream consumers get Dependabot alerts. A public issue tells attackers before users can patch.
</details>

---

### Question 14
**Scenario:** Alert volume from code scanning is high on a legacy codebase.

A. Dismiss everything
B. Focus on new alerts introduced by pull requests, set a severity threshold for blocking, and burn down the historical backlog on a plan
C. Disable scanning
D. Fix all alerts before merging anything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Blocking on pre-existing findings stops all delivery and gets the tool turned off. Preventing new issues while scheduling the backlog is what teams actually sustain, and it means the trend improves from day one.
</details>

---

### Question 15
**Scenario:** GHAS licensing is described.

A. It is free for all repositories
B. Advanced Security features are free on public repositories; private repositories require licensing, historically committer-based and now also available as separate Code Security and Secret Protection products
C. It is per repository
D. It is included in all plans

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The distinction between public and private licensing is examinable, and the packaging has changed, so verify current terms before planning a rollout budget. Active committer counting is what drives cost in the committer-based model.
</details>

---

## Where to go deeper

- [GHAS cert page](../../exams/github/advanced-security/) - notes, practice plan, strategy
- [GitHub Actions practice questions](./github-actions.md) - where scanning runs
- [GitHub Administration practice questions](./github-administration.md) - enterprise rollout
- [Model supply chain security](../ai-security/model-supply-chain.md) - the same reasoning applied to AI artifacts
- **[📖 GitHub Certifications](https://resources.github.com/learn/certifications/)** - official exam pages
