---
last-updated: 2026-08-11
difficulty: intermediate
---

# Claude Certified Architect - Foundations (CCAR-F)

Anthropic's first official Claude certification, launched March 12, 2026. It validates the foundational knowledge needed to design and build production Claude systems: agentic architecture, Claude Code configuration, prompt engineering, tool design, Model Context Protocol (MCP) integration, and context and reliability patterns.

It targets solution architects, AI engineers, and developers who have hands-on experience building with the Claude API, Claude Code, and MCP. Anthropic positions it as the entry point of the Architect track; [Claude Certified Architect - Professional](../claude-certified-architect-professional/) sits above it.

---

## Exam Overview

| Detail | Info |
|---|---|
| **Exam Code** | CCAR-F |
| **Full Name** | Claude Certified Architect - Foundations |
| **Provider** | Anthropic |
| **Level** | Foundational |
| **Duration** | 120 minutes |
| **Questions** | 60 multiple-choice and multiple-response, scenario-based |
| **Passing Score** | 720 / 1000 |
| **Cost** | $125 USD |
| **Delivery** | Pearson VUE (online proctored or test center) |
| **Validity** | 12 months, free non-proctored on-time renewal |
| **Prerequisites** | None (6+ months hands-on Claude experience recommended) |
| **Launched** | March 12, 2026 |

Registration goes through the **[📖 Anthropic Partner Academy](https://anthropic-partners.skilljar.com/page/partner-certifications)** - membership in the (free) **[📖 Claude Partner Network](https://claude.com/partners)** is required, and a personal email address is blocked at checkout. Exams are scheduled with **[📖 Pearson VUE](https://www.pearsonvue.com/us/en/anthropic.html)**; badges are issued via Credly. Retakes: 14-day wait after attempt 1, 30 days after attempt 2, 90 days after attempt 3, maximum 4 attempts in a rolling 12 months.

---

## Exam Domains

| # | Domain | Weight |
|---|---|---|
| 1 | Agentic Architecture | 27% |
| 2 | Claude Code Configuration | 20% |
| 3 | Prompt Engineering & Structured Output | 20% |
| 4 | Tool Design & MCP Integration | 18% |
| 5 | Context & Reliability | 15% |

---

## Domain Breakdown

### 1 - Agentic Architecture (27%)

The highest-weighted domain. You should understand how to design agentic systems with Claude, including when to use agents vs simple prompts, multi-agent orchestration, and production reliability patterns.

**Key Concepts:**
- Agentic design patterns (tool use loops, multi-step reasoning, orchestration)
- Agent architectures (single agent, multi-agent, supervisor/worker patterns)
- Agentic workflows (plan-execute-reflect loops)
- Error handling and recovery in agentic systems
- Decision criteria for agents vs simple prompt chains
- Production considerations (cost management, latency, reliability)
- Claude's extended thinking in agentic contexts

### 2 - Claude Code Configuration (20%)

Claude Code is Anthropic's official CLI and IDE integration for Claude. This domain covers configuring, customizing, and managing Claude Code for individual and team development workflows.

**Key Concepts:**
- Claude Code CLI setup, installation, and configuration
- CLAUDE.md file hierarchy (project-level, user-level, enterprise-level)
- Settings and permissions model
- Hooks system (pre-tool and post-tool execution hooks)
- Custom slash commands
- IDE integrations (VS Code extension, JetBrains plugin)
- MCP server configuration within Claude Code
- Team workflow configuration

### 3 - Prompt Engineering & Structured Output (20%)

The art and science of crafting effective prompts for Claude, plus extracting structured data from responses.

**Key Concepts:**
- Prompt engineering best practices specific to Claude
- System prompts vs user prompts and their roles
- Chain-of-thought and reasoning techniques
- Structured output extraction (JSON mode, tool use for structured data)
- XML tags for prompt organization and clarity
- Few-shot and many-shot prompting techniques
- Prompt caching for cost optimization
- Multimodal prompting (vision, PDF processing)

### 4 - Tool Design & MCP Integration (18%)

The Model Context Protocol (MCP) is a core part of Claude's extensibility story. This domain covers designing tools, building MCP servers, and integrating external capabilities into Claude workflows.

**Key Concepts:**
- Model Context Protocol (MCP) architecture and fundamentals
- MCP components (clients, servers, transports - stdio, SSE, streamable HTTP)
- Building MCP servers (tools, resources, prompts)
- Tool design best practices (naming conventions, descriptions, JSON schemas)
- Claude API tool use (function calling)
- Tool choice modes (auto, any, specific tool forcing)
- Parallel tool use
- Error handling in tool calls

### 5 - Context & Reliability (15%)

Managing Claude's context window effectively, implementing reliability patterns, and building production-grade applications.

**Key Concepts:**
- Context window management
- Long context best practices and strategies
- Prompt caching for performance and cost
- Extended thinking (Claude's reasoning mode)
- Reliability patterns (retries, fallbacks, validation loops)
- Token counting and budget management
- Streaming and real-time response handling
- Rate limiting, error handling, and API best practices

---

## Study Approach

### Recommended Path

1. **Start with the official prep courses** - The Anthropic Partner Academy hosts free preparation courses and the official exam guide. Complete those first; they define the exam scope.

2. **Read the documentation** - The official docs at docs.anthropic.com are the primary source of truth. Focus on the API reference, guides, and cookbooks.

3. **Build hands-on projects** - This is applied material. You need practical experience building with the Claude API, Claude Code, and MCP to internalize it.

4. **Practice with scenarios** - Work through the scenario-based questions in this guide. The goal is applied judgment, not memorization.

5. **Review and fill gaps** - Use the fact sheet and notes in this guide to identify and fill knowledge gaps.

### Time Investment

- **4 weeks** is the recommended study period for someone with existing Claude experience
- **6-8 weeks** for those newer to Claude but with general AI/ML background
- **2-3 hours per day** of focused study is ideal

### Key Study Resources

| Resource | URL | Notes |
|---|---|---|
| Anthropic Partner Academy | https://anthropic-partners.skilljar.com | Official prep courses and exam guide |
| Anthropic Academy | https://anthropic.skilljar.com | Free public Claude courses |
| Anthropic Docs | https://docs.anthropic.com | Primary documentation |
| MCP Specification | https://modelcontextprotocol.io | MCP protocol details |
| Claude Code Docs | https://docs.anthropic.com/en/docs/claude-code | CLI and IDE docs |
| Anthropic Cookbook | https://github.com/anthropics/anthropic-cookbook | Code examples |
| Pearson VUE | https://www.pearsonvue.com/us/en/anthropic.html | Scheduling and retake policy |

---

## Study Materials in This Guide

| File | Description |
|---|---|
| [fact-sheet.md](fact-sheet.md) | Deep reference with documentation links, domain breakdowns, and exam tips |
| [notes/01-agentic-architecture.md](notes/01-agentic-architecture.md) | Domain 1 - Agentic Architecture (27%) |
| [notes/02-claude-code-configuration.md](notes/02-claude-code-configuration.md) | Domain 2 - Claude Code Configuration (20%) |
| [notes/03-prompt-engineering-structured-output.md](notes/03-prompt-engineering-structured-output.md) | Domain 3 - Prompt Engineering & Structured Output (20%) |
| [notes/04-tool-design-mcp-integration.md](notes/04-tool-design-mcp-integration.md) | Domain 4 - Tool Design & MCP Integration (18%) |
| [notes/05-context-reliability.md](notes/05-context-reliability.md) | Domain 5 - Context & Reliability (15%) |
| [notes/06-exam-tips-prep-strategy.md](notes/06-exam-tips-prep-strategy.md) | Exam tips, official courses, and preparation strategy |
| [practice-plan.md](practice-plan.md) | 4-week study plan with checkboxes |
| [scenarios.md](scenarios.md) | Exam-style scenarios with solutions |
| [strategy.md](strategy.md) | 3-phase study approach, resources, and exam tactics |
| [flashcards.csv](flashcards.csv) | Importable flashcard deck |

Practice questions: [resources/practice-questions/anthropic-claude-architect-foundations.md](../../../resources/practice-questions/anthropic-claude-architect-foundations.md)

---

## Exam Tips

1. **Read every word** - Scenario questions have important details buried in the context. Skim at your peril.
2. **Eliminate first** - Most questions have 1-2 obviously wrong answers. Eliminate those, then reason through the remaining options.
3. **Think production** - Favor production-ready, reliable, cost-effective solutions over clever hacks.
4. **Watch for "most appropriate"** - Many questions ask for the BEST answer, not just a correct one. Multiple options may work, but one is better.
5. **Time management** - 120 minutes for 60 questions is 2 minutes each. Flag and move on.
6. **Agentic Architecture is king** - At 27% weighting, prioritize it.

---

## The Anthropic Certification Track

CCAR-F is one of four official Claude certifications:

| Certification | Code | Level | Guide |
|---|---|---|---|
| Claude Certified Associate - Foundations | CCAO-F | Foundational | [guide](../claude-certified-associate-foundations/) |
| Claude Certified Developer - Foundations | CCDV-F | Foundational | [guide](../claude-certified-developer-foundations/) |
| Claude Certified Architect - Foundations | CCAR-F | Foundational | this guide |
| Claude Certified Architect - Professional | CCAR-P | Professional | [guide](../claude-certified-architect-professional/) |

A typical architect path: CCAR-F first, then [CCAR-P](../claude-certified-architect-professional/) once you have production experience. Developers shipping Claude apps usually sit [CCDV-F](../claude-certified-developer-foundations/) instead. The [Prompt Engineering Specialist](../claude-prompt-engineering-specialist/) guide in this repo remains a self-directed deep-dive that supports all four exams.
