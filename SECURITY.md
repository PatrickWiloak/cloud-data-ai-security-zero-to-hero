# Security policy

This repository is study material: markdown, diagrams, and code samples meant to be read and copied into your own environment. It runs no service and holds no user data, so "security issue" here means something different from a normal application repo.

## What is worth reporting

- **A code sample that teaches an insecure practice.** A snippet with a hardcoded credential, an over-permissive IAM policy presented as a good example, a `curl | bash` without comment, a Terraform block that opens a security group to `0.0.0.0/0` without saying why that is wrong. These are the ones that matter most, because people paste them into real accounts.
- **A link to a hijacked or malicious domain.** The repo cites thousands of vendor documentation URLs. Domains get abandoned and re-registered, and a citation that used to point at a vendor doc can end up pointing somewhere hostile.
- **A leaked secret**, in the tree or in its history. Nothing here should ever contain a real key, token, or account identifier.
- **A vulnerability in the automation** under `.github/`, particularly anything in a workflow that could execute attacker-controlled input from a pull request.

## What is not a security issue

A dead link, a stale vendor fact, or an out-of-date exam detail is a content bug. Open a normal issue for those, or a pull request.

## How to report

For anything in the first list, use **[GitHub's private vulnerability reporting](https://github.com/PatrickWiloak/cloud-data-ai-security-zero-to-hero/security/advisories/new)** rather than a public issue, so the fix can land before the detail is public.

Please include the file path, the line, and what a reader would do wrong if they followed it.

Expect an acknowledgement within a week. This repository is maintained around a full-time job, so a fix may take longer than that, but a report will not be ignored.

## Scope of the content itself

Everything here describes how to secure cloud, data, and AI systems. None of it is a substitute for your own organization's review, and vendor defaults change faster than any document. Where a page carries a `last-updated` date, treat that as the date somebody last checked it against the vendor's documentation, not a guarantee that it is current today. The per-certification verification ledger is in [docs/freshness.md](./docs/freshness.md).
