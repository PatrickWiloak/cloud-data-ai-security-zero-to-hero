---
last-updated: 2026-08-11
---

# Domain 1 - Output Evaluation and Validation (21%)

## Overview

This is the largest domain on the CCAO-F exam, and that is deliberate. Anthropic's message with this blueprint is clear: the most important skill for a business user of Claude is not writing prompts, it is knowing whether the output is good enough to use, and what to do when it is not.

Everything in this domain flows from one idea: **Claude's output is a draft, not a deliverable.** You review it, verify it, and improve it before it goes anywhere that matters.

---

## Why Validation Matters

Claude is a language model. It produces fluent, confident, well-structured text whether or not the underlying claims are correct. Three properties make validation non-negotiable:

1. **Hallucination** - Claude can state things that are false, invent sources, or misremember details, while sounding completely certain. Fluency is not accuracy.
2. **Training cutoff and staleness** - without web search or provided documents, Claude's knowledge stops at its training cutoff. Recent events, prices, versions, and people's roles may be out of date.
3. **Ambiguity absorption** - if your prompt was vague, Claude fills the gaps with plausible assumptions. The output can be "wrong" simply because it answered a different question than you meant.

The consequence for business users: an unverified Claude output in a client deliverable is your error, not Claude's. The person who ships the work owns its accuracy.

---

## Match Verification Depth to Risk

The exam tests proportionality in both directions. Under-verifying a client report is wrong; running a full fact-check audit on a brainstorm is also wrong (wasted effort is a cost).

| Output use | Risk | Appropriate verification |
|---|---|---|
| Brainstorming ideas, internal draft for your own use | Low | Skim for relevance; no formal check |
| Internal summary shared with your team | Medium | Read fully, spot-check key facts and figures |
| Client deliverable, external publication | High | Verify every checkable claim against sources; human review |
| Legal, financial, medical, HR-decision content | Very high | Expert human review is mandatory; Claude assists, never decides |

A useful exam heuristic: when a scenario mentions "client", "publish", "regulator", or "decision about a person", the correct answer includes verification and human review. When it says "brainstorm" or "rough draft for yourself", heavyweight verification options are distractors.

---

## What to Check First: The Checkables

Some elements of an output carry disproportionate risk because they are specific and falsifiable:

- **Names** - people, companies, products. Claude can misattribute or misspell.
- **Numbers** - statistics, percentages, financial figures, dates. Verify against the source, and re-derive any arithmetic.
- **Quotes** - anything in quotation marks. Claude may paraphrase and present it as verbatim.
- **Citations and URLs** - Claude can produce plausible-looking references to documents or pages that do not exist. Every citation gets clicked or looked up.
- **Claims about the recent past** - anything after the training cutoff needs a live source.
- **Legal, regulatory, and policy statements** - always confirm with the actual text or a qualified person.

Prose, structure, tone, and general explanations are lower risk; the specific falsifiable claims embedded in them are where errors hide.

---

## Grounding: The Best Prevention

The most effective way to reduce fabrication is to give Claude the source material and constrain it to that material.

Practical pattern:

1. Upload or paste the actual documents (report, contract, transcript, data export).
2. Instruct: "Answer using only the provided documents. If the documents do not contain the answer, say so instead of guessing."
3. Ask for support: "For each key claim, quote the passage from the document that supports it."
4. Spot-check the quotes against the source. A quote that is not actually in the document is a red flag for the whole output.

Grounding reduces hallucination substantially, but does not eliminate it. Claude can still misread a table, combine two passages incorrectly, or over-generalize. The quotes give you a fast audit trail.

Web search works the same way for current information: ask Claude to search and cite, then open the cited pages for anything load-bearing.

---

## Techniques for Evaluating an Output

### Ask for the seams

- "List the assumptions you made in this answer."
- "Which parts of this are you least confident about?"
- "What would make this analysis wrong?"

Claude is reasonably good at surfacing its own uncertainty when asked. These questions turn a smooth answer into a reviewable one.

### Cross-examination

- Re-ask the question with different wording, or in a fresh chat, and compare. Consistent answers raise confidence; divergent answers mark exactly what needs external verification.
- Ask Claude to argue the opposite position, then judge which case is stronger.

### Independent re-derivation

- For calculations: ask Claude to show its work step by step, or use the analysis tool (which runs actual code) rather than accepting mental arithmetic in prose. Then spot-check a sample by hand.
- For summaries: pick two or three claims from the summary and find them in the source yourself.

### Self-review, with eyes open

Asking Claude to "review this output for errors" catches real mistakes - format problems, internal contradictions, missed instructions. But it is not independent verification: Claude reviewing Claude shares the same blind spots. Use self-review as a first filter, never as the final sign-off on facts.

---

## Improving an Output That Falls Short

Evaluation feeds directly into iteration (this overlaps with Domain 7):

| Problem found | Fix |
|---|---|
| Factual errors | Provide sources and ask Claude to correct against them |
| Missed part of the task | Point to the specific gap: "You covered X but not Y; add Y" |
| Wrong tone or depth for audience | Name the audience explicitly and give one example paragraph in the right voice |
| Too generic | Add the specific context that was missing from the prompt |
| Structurally messy | Give the exact outline or template to follow |

Specific, targeted feedback in the same conversation almost always beats starting over with a new prompt, because Claude retains the working context.

---

## Validation in Team Workflows

For teams using Claude in delivery work, evaluation should be a process, not a heroic individual habit:

- **Define review gates** - which outputs need peer review, which need expert review, before they leave the team.
- **Label AI-assisted drafts** - so reviewers know to check facts, not just style.
- **Keep the sources attached** - a summary shared without its source documents cannot be verified by the next person.
- **Record what was verified** - for regulated or high-stakes work, note who checked what. This connects to Domain 3 (auditability).

---

## Worked Example

Scenario: an analyst asks Claude to summarize three uploaded customer interview transcripts into key themes for a client readout.

A sound validation pass:

1. Instruct Claude to cite the transcript and speaker for each theme.
2. Check that every quoted line actually appears in a transcript (search the file).
3. Check the counts ("4 of 6 customers mentioned pricing") by scanning the transcripts for the topic.
4. Ask Claude: "Which themes are supported by only one interview?" to catch over-generalization.
5. Human read-through for client sensitivity before the readout.

Time cost: minutes. Risk removed: presenting a fabricated quote to a client.

---

## Key Takeaways

1. Output evaluation is the exam's biggest domain because it is the biggest real-world skill gap.
2. Fluency is not accuracy; confident tone tells you nothing about correctness.
3. Scale verification to stakes - both under- and over-verifying are wrong answers.
4. Names, numbers, quotes, citations, and recent events are the high-risk checkables.
5. Ground Claude in source documents and demand citations; then spot-check the citations.
6. Self-review is a useful filter, never independent verification.
7. The human who ships the output owns its accuracy.

**[📖 Claude Help Center](https://support.claude.com)** - official product guidance, including how file uploads, web search, and the analysis tool work
