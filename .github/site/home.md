<!--
  Site-only landing page. Rendered over the staged copy of README.md by
  .github/scripts/build-site.py; the repo's own README.md is never touched.

  The two pages have different jobs. README.md is a repo front page: badges,
  repository structure, contributing, "star this repo". This is a website
  landing page: what the site is, who it is for, and the four or five links a
  first-time visitor actually needs.

  Never hard-code a count here. Every number is a double-braced token filled from
  docs/certs.json and from check-readme-counts.py's gather(), which is the same
  counting code CI runs against the README - so a number on this page cannot
  drift away from the tree. Adding a new number means adding a token, not
  typing a figure.

  No `hide: toc` here. With toc.integrate the page's headings fold into the left
  sidebar, and hiding them would make Home the one page whose sections do not
  appear where every other page's do.
-->
<!-- markdownlint-disable MD030 -->
<!-- Material's card grids use `-   ` (three spaces) so the card body lines up at
     a four-space indent and stays part of the list item. MD030 wants one. -->


# Cloud, Data, AI, and Security - From Zero to Hero { .home-title }

<p class="home-intro">Plain-English concepts, hands-on builds, deep references, and the most comprehensive certification library on GitHub.</p>

<p class="home-sub">Free, no signup, nothing gated. Never opened a terminal, or chasing your fifth cert - both start here. Press <kbd>/</kbd> to search all {{words}} words.</p>

[Start from zero](learn/day-one/){ .md-button .md-button--primary }
[Browse {{certifications}} certifications](STUDY-HUB.md){ .md-button }
[Look up a concept](learn/concepts/){ .md-button }

<div class="stat-strip" markdown>

- **{{certifications}}** certifications
- **{{providers}}** providers
- **{{words}}** words
- **{{doc_links}}** vendor doc links
- **{{concept_pages}}** concept pages
- **{{hands_on_projects}}** hands-on builds

</div>

## Four ways in

<div class="grid cards" markdown>

-   :material-book-open-variant:{ .lg .middle } **Learn**

    ---

    Plain English, no exam scaffolding. A strict-beginner on-ramp, {{concept_pages}} bite-size concept pages, and two structured paths through cloud and AI.

    [:octicons-arrow-right-24: Start learning](learn/)

-   :material-hammer-wrench:{ .lg .middle } **Build**

    ---

    {{hands_on_projects}} guided builds with inline code and time estimates, {{architecture_patterns}} architecture patterns, {{cli_cheat_sheets}} CLI cheat sheets.

    [:octicons-arrow-right-24: Build something](resources/hands-on-projects/)

-   :material-certificate-outline:{ .lg .middle } **Certify**

    ---

    {{certifications}} cert guides across {{providers}} providers, each with a fact sheet, practice plan, scenarios, and exam-day strategy.

    [:octicons-arrow-right-24: Find your cert](STUDY-HUB.md)

-   :material-book-search-outline:{ .lg .middle } **Reference**

    ---

    {{service_comparisons}} cross-cloud service comparisons, {{roadmaps}} career roadmaps, plus compliance, FinOps, migration and troubleshooting deep dives.

    [:octicons-arrow-right-24: Browse reference](resources/)

</div>

## Jump to what you need

<div class="home-links" markdown>

- [Day One](learn/day-one/) - terminal, git, HTTP and servers, assuming nothing
- [Cloud from Scratch](learn/cloud-from-scratch.md) - compute, storage, networking, identity
- [AI from Scratch](learn/ai-from-scratch.md) - LLMs, RAG, agents, evals, fine-tuning
- [Concepts](learn/concepts/) - {{concept_pages}} five-minute explainers, one idea each
- [Topic indexes](topics/) - {{topic_indexes}} subjects tied across all four pillars
- [Glossary](learn/glossary.md) - the vocabulary, defined once
- [Hands-on projects](resources/hands-on-projects/) - {{hands_on_projects}} builds you can finish in a sitting
- [Labs by certification](resources/hands-on-projects/labs-by-cert.md) - which build backs which exam
- [Practice questions](resources/practice-questions/) - scenario banks with explained answers
- [Interview prep](resources/interview-prep/) - {{interview_prep}} role-specific guides
- [Freshness ledger](docs/freshness.md) - what was last verified, and when
- [Curated YouTube](learn/youtube.md) - the videos worth your time

</div>

## Certifications by provider

<div class="provider-grid" markdown>

{{provider_chips}}

</div>

[Full per-provider breakdown](STUDY-HUB.md#-certifications-by-provider){ .md-button }

## What's new

{{whats_new}}

## Who made this

Built by **[Patrick Wiloak](https://patrickwiloak.com)** - ex-AWS Solutions Architect, 10 years in tech, 60 certifications and accreditations, 18x multi-cloud certified.
[YouTube](https://youtube.com/@patrickwiloak) · [LinkedIn](https://www.linkedin.com/in/patricklukewilson/) · [Blog](https://patrickwiloak.com/blog/aws-certification-study-framework-how-to-prepare-pass-certifications) · [Source on GitHub](https://github.com/PatrickWiloak/cloud-data-ai-security-zero-to-hero)

We build custom software and products at **[Nobler Works](https://noblerworks.com/)**. Open-source training like this is how we give back - we are nothing without the community that supports us. If you need software built, [get in touch](https://noblerworks.com/).

!!! tip "Want the reps as well as the material?"

    [![gitGood.dev - training platform for software engineers and architects](assets/brand/gitgood-banner.png){ width="420" }](https://gitgood.dev)

    This site gives you the material. **[gitGood](https://gitgood.dev)** gives you the reps, and tells you whether you actually know it: 1,000+ practice questions, coding challenges with worked explanations, AI mock interviews, certification deep dives, resume review, and a live job-market pulse.

    10 days free, then $5/month or $40/year. The free tier needs no card.

## Fine print

Free for educational use with attribution. Every technical claim links to the vendor's own documentation - {{doc_links}} links across the site.

This is an independent educational resource. It is not affiliated with, endorsed by, or sponsored by AWS, Microsoft, Google, Oracle, IBM, or any other vendor referenced. All trademarks belong to their respective owners.

Found something wrong or out of date? [Contributions welcome](CONTRIBUTING.md).
