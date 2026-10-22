# Cloud Native Platform Engineering Associate (CNPA) - Practice Questions

30 questions for CNPA prep. The organizing idea: a platform is a product whose users can choose not to use it.

> **Cert page:** [exams/kubernetes/cnpa/](../../exams/kubernetes/cnpa/)

---

### Question 1
**Scenario:** A platform team spent a year building a deployment system. Six months post-launch, 4 of 40 teams use it. Leadership proposes mandating it.

A. Mandate it to drive adoption
B. Build a portal on top to improve discoverability, since teams that cannot find the platform will never adopt it, and discovery is the main barrier
C. Run user research with the 36 non-adopting teams and make the golden path easier than their current approach
D. Add more features

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Low voluntary adoption is a product signal. A mandate hides the signal and creates resentment without fixing the cause. More features rarely address it, because the problem is usually onboarding friction, a missing escape hatch, or solving a problem teams do not have. A portal is a nicer front door to something people do not want.
</details>

---

### Question 2
**Scenario:** A platform hosts 40 trusted internal teams, a regulated payments division, and an external partner running code the company does not control.

A. Namespaces for internal teams, dedicated nodes or a cluster for payments, and a sandboxed dedicated cluster for the partner
B. One shared cluster for all three groups, separated only by node labels and taints
C. Namespace isolation for all three groups on the same shared nodes, with network policies, resource quotas, and Pod Security Standards enforced between them
D. Virtual control planes for all three, on one shared node pool

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Match isolation to trust level and compliance boundary. Namespace isolation shares a kernel and control plane, so it is not a boundary against untrusted code. Virtual control planes on shared nodes (D) still share the kernel. One shared cluster separated only by labels and taints (B) gives no real isolation boundary at all.
</details>

---

### Question 3
**Scenario:** A team needs a GPU workload with a custom scheduler that the golden path does not support.

A. Refuse the exception to keep the platform consistent, since supporting one-off schedulers would fragment the golden path
B. Grant it while keeping the thin conformance layer (policy, telemetry, supply chain), and record it as input
C. Immediately build GPU support into the golden path
D. Grant the exception with no guardrails or conformance checks, and let the team run its own scheduler however it likes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Golden paths are the easiest route, not the only route. Refusing drives shadow platforms and loses visibility. What must never be optional is the conformance layer. Building GPU support for one team is premature; wait for the pattern to repeat.
</details>

---

### Question 4
**Scenario:** Developers wait five days for a database because they file a ticket and the platform team runs Terraform manually. Self-service is required without giving developers cloud credentials.

A. Expose the full cloud resource as a custom resource, with every provider field and option editable by developers
B. Give developers Terraform and tightly scoped cloud credentials, with remote state, locking, and a pull request approval step
C. A control plane pattern: a composite resource definition, a composition, and a policy-constrained claim
D. A web form that files the ticket automatically, with the platform team still running Terraform by hand afterwards

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Expose a simple claim, hide the composition, constrain with policy. The abstraction stays stable while the implementation changes underneath. Handing over credentials abandons the guardrails. A faster ticket is still ticket-driven. Exposing the full resource leaks the complexity the abstraction exists to hide.
</details>

---

### Question 5
**Scenario:** A platform team is asked to justify its budget and proposes reporting features shipped, lines of platform code, and tickets closed.

A. Add uptime as a fourth measure and keep the rest, since availability shows the platform is reliable for users
B. Report only cost savings
C. These are reasonable measures of team output, and finance teams generally accept them as evidence of value
D. Replace them with DORA metrics, adoption, time to first deployment, satisfaction, and platform SLOs

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** All three proposed measures are vanity metrics. Tickets closed is actively misleading, because a successful self-service platform drives the ticket count down. Uptime is necessary but not sufficient: a reliable platform nobody uses has still failed.
</details>

---

### Question 6
**Scenario:** Leadership asks the team to "build an IDP" and points at Backstage. Three months after installing it and importing a catalog, developers report no improvement.

A. The capability layer was never built; a portal without a platform behind it is a catalog of links
B. Install more Backstage plugins for CI status, Kubernetes views, and cost, so the portal shows more of each service
C. The catalog metadata is incomplete, so owners, lifecycle and dependencies are missing for many components
D. Abandon the portal

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** An Internal Developer Platform is the capability layer; an Internal Developer Portal is an interface onto it. The ordering was wrong. Build self-service provisioning, a golden path, and delivery automation, then use the portal for discovery and scaffolding.
</details>

---

### Question 7
**Scenario:** Security requires signed images, no critical CVEs, declared resource limits, and non-root execution in production, without the platform team becoming a review bottleneck.

A. Manual security review per release
B. A check in the CI pipeline that fails the build when an image is unsigned, vulnerable, or missing limits
C. Documentation and training
D. Policy as code enforced at admission, rolled out in audit mode first, with a compliant golden path

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Admission control is the enforcement point because everything reaching the cluster passes through it; a CI-only check is bypassable by anyone deploying outside the pipeline. Audit mode first prevents breaking delivery on day one, and a compliant golden path makes the right thing the easiest thing.
</details>

---

### Question 8
**Scenario:** Which best describes a golden path?

A. A set of approved tools teams may choose from
B. A document describing best practices
C. An opinionated, supported, documented route that is the easiest option, with escape hatches
D. The only permitted way to deploy, enforced by blocking any workload that does not use the standard template

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A path that forbids alternatives is a gate, not a paved road, and teams route around gates. A document is not a path because it does not make anything easier. A list of tools is not opinionated enough to reduce cognitive load.
</details>

---

### Question 9
**Scenario:** What is the central justification for platform engineering?

A. Centralizing control of production
B. Reducing extraneous cognitive load so teams spend capacity on their own domain
C. Standardizing tooling across the organization
D. Reducing infrastructure cost

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cognitive load reduction is the stated purpose in the CNCF Platforms White Paper and in Team Topologies. Standardization, cost, and control may follow, but a platform that standardizes tooling while adding concepts developers must learn has made things worse.
</details>

---

### Question 10
**Scenario:** An organization has a recognized platform team that responds to requests through a ticket queue, with some standardization but little self-service. Which maturity level does this describe?

A. Scalable, where the platform is self-service and managed as a product
B. Provisional, where work is ad hoc and depends on individual effort
C. Optimizing, where decisions are driven by continuous measurement
D. Operational, where a team works reactively

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Provisional is ad hoc individual effort. Operational means a team exists but works reactively, typically through tickets. Scalable adds self-service and product management. Optimizing means decisions are driven by measurement. The ticket queue is the operational-level tell.
</details>

---

### Question 11
**Scenario:** Which measure best captures whether a platform is succeeding with its users?

A. Number of clusters managed
B. Voluntary adoption rate and time to first deployment
C. Platform team headcount
D. Number of policies enforced

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Voluntary adoption is the honest signal because users could choose otherwise, and time to first deployment is a direct proxy for the cognitive load the platform removed. The other three measure scale or effort, not outcome.
</details>

---

### Question 12
**Scenario:** What is the "thinnest viable platform" idea?

A. Building the least that delivers value, and buying managed services over building
B. Keeping the platform team small, ideally one team of under ten people who own every capability
C. Running the platform on minimal infrastructure, with the smallest cluster and node sizes that work
D. Supporting only one programming language and framework, so that every team builds the same way

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A wiki page and two scripts can be a legitimate first platform. Every capability is a permanent operational commitment, so capability should follow demonstrated demand. Rebuilding what a managed service already provides is a named anti-pattern.
</details>

---

### Question 13
**Scenario:** Which isolation model gives many tenants cluster-level API access without provisioning a full cluster each?

A. Virtual control plane per tenant
B. Cluster per tenant
C. Node pool per tenant
D. Namespace per tenant

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A virtual control plane gives each tenant its own API server on shared infrastructure, so tenants can create cluster-scoped objects without affecting each other. Namespaces do not offer cluster-level API access, and a cluster each is the expensive option this pattern exists to avoid.
</details>

---

### Question 14
**Scenario:** Why is the Kubernetes API a common foundation for platform APIs, even for capabilities unrelated to containers?

A. It requires no schema
B. It is the fastest API server available, since it serves reads from memory and handles higher request rates than any database-backed API
C. Custom resources inherit RBAC, admission control, audit logging, kubectl, GitOps, and reconciliation
D. It is the only API that supports YAML, so every tool that reads YAML configuration can only talk to Kubernetes

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Extending an existing, well-understood API server means every surrounding capability already works against your new type. That reuse, rather than raw performance, is why platform capabilities are typically exposed as custom resources.
</details>

---

### Question 15
**Scenario:** Which best describes how a platform should produce compliance evidence?

A. Teams submit screenshots of their dashboards and settings during an audit, collected by the platform team
B. The platform generates it as a by-product: policy decisions, admission denials, and provenance
C. Auditors are given read access to the clusters so that they can look at the configuration themselves
D. The platform team compiles a report each quarter manually from tickets, pipeline logs, and interviews with each team

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Uniform enforcement at the platform layer means evidence is produced automatically for every workload. Auditors query the platform rather than asking teams for artifacts, which is a recurring argument for platform investment and a repeated exam theme.
</details>

---

### Question 16
**Scenario:** Using Team Topologies vocabulary, how should a platform team usually interact with the stream-aligned teams that consume its platform?

A. X-as-a-Service, where teams consume the platform through clear interfaces with little coordination
B. Permanent collaboration, where platform engineers join every stream-aligned team's sprint work
C. Facilitating, where the platform team writes the stream-aligned teams' code for them
D. Gatekeeping, where every deployment needs the platform team's approval before release

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The default interaction for a mature platform is X-as-a-Service: the platform is consumed through APIs, templates, and documentation with minimal hand-offs. Collaboration is useful for limited periods, such as discovering a new capability, but not permanently. Facilitating means helping teams learn, not doing their work. Gatekeeping is not a Team Topologies interaction mode and creates bottlenecks.
</details>

---

### Question 17
**Scenario:** Application developers spend much of their time learning Kubernetes networking, certificate management, and cloud IAM before they can ship a simple service. What is the platform's main goal here?

A. Train every developer to expert level in each infrastructure tool before they ship anything
B. Reduce the cognitive load on developers by providing paved, self-service capabilities
C. Move all infrastructure work into a central operations team that takes tickets
D. Ban direct use of infrastructure tools, so that developers only work on application code

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Platform engineering aims to cut the extraneous cognitive load on application teams, so they can focus on their domain, by offering self-service capabilities with sensible defaults. Training everyone to expert level does not scale. A ticket-driven ops team creates waiting. Outright bans remove the escape hatch that advanced teams need.
</details>

---

### Question 18
**Scenario:** A platform team decides each quarter's work by what its own engineers find interesting. Adoption is flat. What would most help?

A. Adopt the newest CNCF projects each quarter so the platform stays current and attractive
B. Freeze new work until adoption grows, so the team can concentrate on stability
C. A platform product manager who runs user research and builds a roadmap from user needs
D. Ask leadership to set adoption targets for every application team in the company

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Treating the platform as a product means someone owns understanding users, prioritizing their problems, and shaping a roadmap from evidence. Chasing new tools solves the platform team's interests, not users' problems. A freeze does not address fit. Targets push adoption without making the platform more valuable.
</details>

---

### Question 19
**Scenario:** Application teams keep asking for small platform features faster than the platform team can build them, and several teams have the skills to build them.

A. Reject the requests, since only the platform team may change the platform
B. Let each team fork the platform and maintain its own copy with the feature
C. Hire contractors to clear the backlog, then reduce the team after the backlog is gone
D. Accept contributions through an inner source model with clear guidelines and code owners

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Inner source lets consuming teams contribute to the platform under guidelines, review, and ownership by the platform team, which scales capacity and keeps one platform. Rejecting requests leaves needs unmet. Forks fragment the platform. Contractors clear a backlog once without changing the dynamic.
</details>

---

### Question 20
**Scenario:** An application team uses the platform's deployment pipeline. Their service crashes in production because of a bug in the application code. Who owns the incident?

A. The platform team, since the service was deployed with the platform
B. The application team, while the platform team owns platform capabilities and their SLOs
C. A central operations team, since neither team should be on call
D. Whichever team notices the incident first, regardless of the cause

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Platforms keep "you build it, you run it" for applications. The application team owns its service, and the platform team owns the platform's capabilities and the SLOs it publishes for them. Making the platform team own every app incident makes it a bottleneck. Separate ops teams and "first to notice" both blur accountability.
</details>

---

### Question 21
**Scenario:** A platform provisions resources with imperative scripts. Over time, environments diverge from what was requested and nobody notices until something breaks.

A. Run the scripts twice each time, so that missed steps are applied by the second run
B. Add more logging to the scripts, so that every change they make is recorded
C. Declarative APIs with controllers that continuously reconcile actual state toward desired state
D. Have engineers review each environment by hand once a month and fix differences

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Declarative resource management with continuous reconciliation, the Kubernetes controller model, detects and corrects drift automatically. Running scripts twice and adding logs do not detect drift made outside the scripts. Monthly manual reviews leave long windows of divergence.
</details>

---

### Question 22
**Scenario:** The platform team wants every service on the golden path to emit traces, metrics, and logs in a vendor-neutral way, so the observability backend can change later.

A. OpenTelemetry instrumentation and the OpenTelemetry Collector, built into the templates
B. Each team's choice of vendor agent, with dashboards rebuilt whenever the vendor changes
C. Only application logs written to disk, collected later if an incident needs investigating
D. A proprietary SDK from the current vendor, embedded in every service at build time

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** OpenTelemetry provides vendor-neutral APIs, SDKs, and a collector for traces, metrics, and logs, and building it into golden path templates gives consistent telemetry by default with a swappable backend. Per-team vendor agents and proprietary SDKs create lock-in and inconsistency. Logs alone miss traces and metrics.
</details>

---

### Question 23
**Scenario:** Auditors ask the platform to prove what each deployed image contains and how it was built.

A. A spreadsheet maintained by each team listing the libraries they remember using
B. Images rebuilt from source at deploy time, so their contents always match the code
C. Scanning running containers once a year and keeping the scan output as evidence
D. Generate an SBOM and signed build provenance (for example SLSA) in the pipeline

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A software bill of materials lists the components in each artifact, and signed provenance, as described by SLSA, records how and where it was built. Generated automatically in the pipeline and stored with the artifact, they give auditors verifiable evidence. Spreadsheets are unreliable. Rebuilding at deploy time breaks reproducibility. Annual scans miss most of the lifecycle.
</details>

---

### Question 24
**Scenario:** Applications need secrets from a central vault, and developers must not paste secret values into Kubernetes manifests in Git.

A. Base64-encode the secrets in the manifests, since encoding protects them in the repository
B. External Secrets Operator syncing values from the vault into Kubernetes Secrets at runtime
C. A shared password file in the repository, readable only by members of the platform team
D. Environment variables typed by hand into each Deployment by the on-call engineer

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** External Secrets Operator lets manifests reference secrets by name while the controller fetches the values from the external store and creates Kubernetes Secrets, so no secret value is committed. Base64 is encoding, not encryption. Files in the repository leak to anyone with access. Hand-typed values are error-prone and unaudited.
</details>

---

### Question 25
**Scenario:** A platform team wants deployments to every cluster to be auditable, reversible with a revert, and corrected automatically if someone changes resources by hand.

A. A CI job that runs `kubectl apply` after each merge, with credentials for every cluster
B. Engineers apply changes by hand during a weekly maintenance window, following a runbook
C. GitOps, with an in-cluster agent reconciling cluster state from a Git repository
D. A nightly script that redeploys everything from the latest container images available

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** GitOps keeps desired state in Git, giving an audit trail and revert-based rollback, while an agent continuously reconciles and corrects manual drift. A CI push does not correct drift between runs and spreads cluster credentials. Manual windows are slow and error-prone. Redeploying the latest images ignores what was approved.
</details>

---

### Question 26
**Scenario:** Test passes in staging, but production behaves differently because the pipeline rebuilds the container image separately for each environment.

A. Build the artifact once, then promote the same immutable image through each environment
B. Rebuild the image in production with the same Dockerfile, but pin the base image tag
C. Skip staging and test in production only, so the build is done for one environment
D. Use the `latest` tag in every environment, so that each one runs the newest build

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Building once and promoting the same immutable artifact, ideally referenced by digest, ensures that what was tested is what runs, with configuration supplied per environment. Rebuilding can pull different dependencies even with a pinned base tag. Skipping staging removes testing. `latest` is mutable and hides what runs.
</details>

---

### Question 27
**Scenario:** Developers should request a "PostgreSQL database" with a size and a backup policy through a Kubernetes API, while the platform decides the cloud resources behind it.

A. Give developers cloud console access and a wiki page on how to create a database correctly
B. A Crossplane composite resource definition with compositions that map to the cloud resources
C. A ConfigMap per database request, which the platform team reads and fulfills by hand
D. A Helm chart that installs PostgreSQL in the developer's namespace with no options exposed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Crossplane lets the platform define its own API (a composite resource definition) with a small developer-facing schema, and compositions translate each request into the underlying managed cloud resources. Console access exposes complexity and credentials. ConfigMaps read by hand reintroduce ticket ops. A fixed Helm chart ignores the request parameters and the cloud service.
</details>

---

### Question 28
**Scenario:** A platform team wants to extend Kubernetes with a new resource type, `Tenant`, that automatically creates namespaces, quotas, and policies when one is created.

A. Write a shell script that a cron job runs every hour to create any missing tenant objects
B. Store each tenant as a row in a database and have engineers apply the YAML by hand
C. Use an admission webhook alone, which creates the namespace and quota objects itself
D. Define a CustomResourceDefinition for `Tenant` and a controller that reconciles it

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The operator pattern pairs a CRD, which adds the new API type, with a controller that watches it and reconciles the namespaces, quotas, and policies it implies, including repairing drift. Cron scripts and database rows are not Kubernetes APIs and do not reconcile. Admission webhooks validate or mutate requests and are not meant to create and maintain other resources.
</details>

---

### Question 29
**Scenario:** Creating a new service takes two weeks of tickets for a repository, CI pipeline, catalog entry, and baseline monitoring. The platform team wants this to take minutes.

A. A wiki page listing each step, so that developers can file the tickets in the right order
B. A software template in the developer portal that scaffolds the repository, CI, catalog entry, and monitoring
C. A shared repository that every new service copies, with the setup steps done later by hand
D. A monthly onboarding session in which the platform team creates services for teams in a batch

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Software templates, such as Backstage scaffolder templates, generate a new service with its repository, pipeline, catalog registration, and observability wiring in one self-service action, encoding the golden path. A wiki keeps the tickets. Copying a repository leaves manual setup. Batch onboarding still makes teams wait.
</details>

---

### Question 30
**Scenario:** Which four metrics make up the DORA software delivery performance measures commonly used to assess a platform's effect on delivery?

A. Lines of code, story points completed, number of commits, and code review comments
B. Platform uptime, number of platform features, ticket count, and cloud spend for the quarter
C. Deployment frequency, lead time for changes, change failure rate, and time to restore service
D. Developer satisfaction, onboarding time, number of templates, and number of catalog entries

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The DORA four key metrics are deployment frequency, lead time for changes, change failure rate, and time to restore service (also called failed deployment recovery time). Output measures such as lines of code, features, and tickets do not show outcomes. Satisfaction and onboarding time are useful, for example in SPACE-style measures, but they are not the DORA four.
</details>

---

## Scoring guide

- **26-30 correct (85%+):** Ready. 75% is the pass mark.
- **20-25 correct (67-83%):** Re-read the CNCF Platforms White Paper and the Maturity Model; the exam follows their vocabulary closely.
- **Below 20:** Work the [scenarios](../../exams/kubernetes/cnpa/scenarios.md), watching for the product-framing pattern in each.
