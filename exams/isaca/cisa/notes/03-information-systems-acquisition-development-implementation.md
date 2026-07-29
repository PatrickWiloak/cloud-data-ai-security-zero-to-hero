---
last-updated: 2026-07-29
---

# CISA Domain 3 - IS Acquisition, Development, and Implementation (12%)

Project governance, the development lifecycle, and the controls that must exist before a
system goes live. The auditor's angle is whether controls were built in, not bolted on.

## Project governance

- **Business case** - the justification: expected benefits, costs, risks, and alternatives. Approved before funding.
- **Feasibility study** - assesses whether the proposal is achievable technically, economically, operationally, and legally.
- **Project sponsor** - the business owner accountable for benefits. A project without an engaged sponsor is a standard finding.
- **Project steering committee** - approves scope, budget, and major changes.
- **Critical path** - the longest sequence of dependent tasks; it determines the minimum project duration. Slippage on the critical path slips the project.
- **Function point analysis** - sizing software by delivered functionality rather than lines of code, used for effort estimation.
- **Earned value analysis** - compares planned versus actual cost and schedule progress.

The auditor's involvement should begin early. Reviewing controls only at go-live is too
late to influence design, which is a recurring exam theme.

## Development methodologies

- **Waterfall** - sequential phases with formal sign-off between them. Suits stable, well-understood requirements; expensive to change late.
- **Agile** - iterative delivery in short increments with continuous stakeholder involvement. Suits evolving requirements. Documentation is lighter, which is an audit consideration rather than an excuse for none.
- **Prototyping** - building a working model to clarify requirements. Risk: the prototype is promoted to production without proper controls.
- **RAD (Rapid Application Development)** - compressed timelines with heavy user involvement.
- **DevOps** - development and operations integration with automated pipelines. See [CI/CD explained](../../../../learn/concepts/cicd-explained.md).
- **Reverse engineering** - deriving design from an existing system, often for replacement.

## SDLC phases and the controls in each

1. **Feasibility** - business case and alternatives.
2. **Requirements definition** - functional and control requirements. Security and audit requirements belong here, not later.
3. **Design** - architecture, data model, interfaces, and control design.
4. **Development** - coding against standards, with code review and version control.
5. **Testing** - unit, integration, system, and acceptance.
6. **Implementation** - conversion, go-live, and handover.
7. **Post-implementation review** - did it deliver the expected benefits?

- **User acceptance testing (UAT)** - performed by business users against business requirements. Users, not developers, must sign off.
- **Regression testing** - confirms existing functionality still works after a change.
- **Parallel testing** - old and new systems run together and results are compared.
- **Pilot testing** - deployment to a limited group before full rollout.
- **Test data** - must be representative. Using live production data in test raises a privacy exposure; it should be masked or anonymized.

## Implementation and conversion

- **Direct (big bang) cutover** - old system off, new system on. Cheapest, riskiest, no fallback.
- **Parallel changeover** - both systems run; highest cost, lowest risk, allows result comparison.
- **Phased changeover** - implemented in stages by module or location.
- **Pilot changeover** - one site or group first.
- **Data conversion controls** - record counts, control totals, and reconciliation before and after migration. Conversion is where data integrity is most often lost.
- **Fallback / rollback plan** - how to return to the previous state. Required before go-live.
- **Post-implementation review (PIR)** - conducted after the system has stabilized, comparing actual benefits to the business case.

Parallel running is the lowest-risk conversion and direct cutover the highest. Questions
about a critical system with no tolerance for failure point to parallel.

## Application controls

- **Input controls** - validation, edit checks, range checks, check digits, sequence checks, and batch totals. Preventing bad data entry is cheaper than correcting it later.
- **Processing controls** - run-to-run totals, reasonableness checks, and reconciliation.
- **Output controls** - distribution restrictions, reconciliation of totals, and error reporting.
- **Check digit** - a calculated digit appended to a number to detect transcription errors.
- **Hash total** - a meaningless-but-verifiable sum used to confirm nothing changed in transit.
- **Audit trail** - a record of transactions sufficient to reconstruct what happened and who did it.

## Change and release management

- **Change management** - request, assess, approve, test, implement, review. Emergency changes still need retrospective approval and documentation.
- **Configuration management** - controlling and recording versions of code and configuration.
- **Version control** - the authoritative history of source code.
- **Library control** - separation of development, test, and production libraries.
- **Migration to production** - performed by someone independent of the developer. Developers with production migration rights is one of the most common CISA findings.
- **Emergency change (firecall) access** - temporary elevated access, logged, time-limited, and reviewed afterwards.

## Acquisition of third-party systems

- **Request for proposal (RFP)** - documented requirements issued to vendors for comparable bids.
- **Vendor evaluation criteria** - defined and weighted before proposals arrive, to keep selection objective.
- **Escrow agreement** - source code held by a third party and released if the vendor fails. The control for vendor viability risk in critical bespoke software.
- **Contractual right to audit** - retained access to assess the vendor's controls.
- **Acceptance criteria** - objective tests the delivered system must pass before payment or go-live.

## Exam pointers

- Security and control requirements must be defined in the requirements phase. Retrofitting is the wrong answer.
- UAT is signed off by users. Developer sign-off is a finding.
- Production data used in testing without masking is a privacy exposure.
- The developer must not migrate their own code to production. Look for segregation of duties.
- Source code escrow addresses vendor failure risk specifically, not quality or support.
- A post-implementation review measures benefits against the business case, not technical success alone.

## Official documentation

**[📖 ISACA CISA exam content outline](https://www.isaca.org/credentialing/cisa)** - authoritative domain list
**[📖 COBIT framework](https://www.isaca.org/resources/cobit)** - build, acquire, and implement objectives
