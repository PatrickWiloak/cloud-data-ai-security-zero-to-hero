---
last-updated: 2026-10-22
applies-to: CompTIA Cloud+ CV0-004 exam objectives v2.0, checked 2026-10-22
difficulty: intermediate
---

# CompTIA Cloud+ (CV0-004)

> **Outline updated 2026-10-22.** Earlier versions of this folder said CV0-004 but listed CV0-003's five domains (Architecture 13%, Security 20%, Deployment 23%, Operations 22%, Troubleshooting 22%). The real CV0-004 outline has six domains, including a new DevOps Fundamentals domain, and Cloud Architecture is now the heaviest at 23%. The notes were renumbered to match; this page and every file in the folder now follow the official objectives v2.0.

## Exam overview

CompTIA Cloud+ validates the skills to design, deploy, secure, operate and troubleshoot cloud infrastructure. It is vendor neutral: questions describe concepts and scenarios, not one provider's console. It suits cloud engineers, system administrators moving to cloud, and network engineers working with cloud networking. CV0-004 launched on December 18, 2024 and replaced the previous version of the exam.

**Exam details:**
- **Exam Code:** CV0-004
- **Duration:** 90 minutes
- **Questions:** Maximum of 90, multiple choice and performance-based
- **Passing Score:** 750 (on a scale of 100-900)
- **Cost:** $369 USD
- **Language:** English
- **Delivery:** Pearson VUE testing center or online proctoring
- **Validity:** 3 years (renewable through the CompTIA Continuing Education program)
- **Prerequisites:** None required. Recommended: 2-3 years of experience as a systems administrator or cloud engineer, plus CompTIA Network+ and Server+ or equivalent knowledge

**[📖 CompTIA Cloud+ certification page](https://www.comptia.org/en-us/certifications/cloud/)** - official exam details, pricing and training options.

**[📖 CV0-004 Exam Objectives v2.0 (PDF)](https://comptiacdn.azureedge.net/webcontent/docs/default-source/exam-objectives/comptia-cloud-cv0-004-exam-objectives-%282-0%29.pdf)** - the authoritative topic list. Re-check it before you book.

## Exam domains

| # | Domain | Weight | Notes |
|---|---|---|---|
| 1 | Cloud Architecture | 23% | [01-cloud-architecture](notes/01-cloud-architecture.md) |
| 2 | Deployment | 19% | [02-deployment](notes/02-deployment.md) |
| 3 | Operations | 17% | [03-operations](notes/03-operations.md) |
| 4 | Security | 19% | [04-security](notes/04-security.md) |
| 5 | DevOps Fundamentals | 10% | [05-devops-fundamentals](notes/05-devops-fundamentals.md) |
| 6 | Troubleshooting | 12% | [06-troubleshooting](notes/06-troubleshooting.md) |

### What each domain covers

**1. Cloud Architecture (23%, objectives 1.1-1.11).** The broadest domain. Service models (IaaS, PaaS, SaaS, FaaS) and the shared responsibility model; availability (regions, availability zones, cloud bursting, edge, availability monitoring, DR with RTO, RPO and hot, warm and cold sites, multicloud tenancy); networking (VPN and dedicated connections, application and network load balancers, application gateways, CDN, firewalls, VPC peering and transit gateways, subnets, VLAN, SDN, BGP, static routes, route tables); storage tiers, disk types and object, block and file storage; cloud-native design (managed services, microservices, loose coupling, fan-out, service discovery); containers and virtualization; billing models, metering, tagging and rightsizing; relational and non-relational databases; workload optimization; and evolving technology (AI and ML services, generative AI, IoT).

**2. Deployment (19%, objectives 2.1-2.5).** Deployment models (public, private, hybrid, community); deployment strategies (blue-green, canary, rolling, in-place); migration types, considerations and the Rs (rehost, replatform, refactor, re-architect, retain, retire); infrastructure and configuration as code, scripting logic, drift detection, versioning and JSON and YAML; and provisioning resources to meet storage, performance, security, cost, availability, compliance, network and compute requirements.

**3. Operations (17%, objectives 3.1-3.4).** Observability (logging collection, aggregation and retention, tracing, metrics, alerting triage and response); scaling (trend, load, event, scheduled and manual triggers; horizontal and vertical); backup and recovery (full, incremental, differential, on-site and off-site, schedule, retention, replication, encryption, testing, in-place and parallel recovery, bulk and granular restores); and life cycle management (patches, major and minor updates, ephemeral and persistent data, end of life and end of support).

**4. Security (19%, objectives 4.1-4.6).** Vulnerability management and CVEs; compliance (data sovereignty, ownership, locality, classification, retention and litigation hold; SOC 2, PCI DSS, ISO 27001, Cloud Security Alliance); IAM (programmatic and console access, SSH, RDP and bastion hosts, federation, SAML, OIDC, MFA, RBAC, OAuth 2.0, audit trails); best practices (Zero Trust, CIS benchmarks, hardening, encryption, secrets management, least privilege, container and storage security); controls (endpoint protection, DLP, IDS and IPS, DDoS protection, IAM policies, network ACLs, security groups, WAF); and spotting attacks (phishing, ransomware, DDoS, cryptojacking, zombie instances, metadata service abuse).

**5. DevOps Fundamentals (10%, objectives 5.1-5.4).** New as its own domain. Source control (commit, push, branch, pull request, review, merge); CI/CD pipelines (build, test, security, workflow, artifacts such as VM and container images, RPM, Debian, ZIP and tar packages, public and private repositories); integration styles (event-driven, REST, SOAP, RPC, WebSockets, GraphQL); and the purpose of Ansible, Docker, ELK, Git, GitHub Actions, Grafana, Jenkins, Kubernetes and Terraform.

**6. Troubleshooting (12%, objectives 6.1-6.3).** Deployment issues (incompatibility, misconfiguration, oversubscription, sizing, outdated definitions, deprecation, full and partial outages, API throttling, service quotas, regional availability); network issues (DHCP, DNS, NTP, NAT, HTTP status codes, latency, throughput, protocol deprecation, IP scope exhaustion and overlap, routes, VLAN tags, access and trunk ports); and security issues (cipher suite deprecation, privilege escalation, unauthorized access, leaked credentials, vulnerable and unauthorized software).

## Study materials

| Resource | What it is for |
|---|---|
| [Fact sheet](fact-sheet.md) | One-page cram reference across all six domains |
| [Notes](notes/) | In-depth teaching notes, one per domain, organized by objective |
| [Scenarios](scenarios.md) | Scenario patterns with the right answer and common distractors |
| [Flashcards](flashcards.csv) | Question and answer pairs for spaced repetition |
| [Practice plan](practice-plan.md) | Six-week schedule weighted by domain |
| [Strategy](strategy.md) | Exam-day tactics, PBQ advice and domain-specific traps |
| [Practice questions](../../../resources/practice-questions/comptia-cloud-plus.md) | Original practice questions with explanations |

## Recommended training

CompTIA sells official CertMaster Learn (self-paced course), CertMaster Practice (adaptive questions) and CertMaster Labs for Cloud+, linked from the certification page above. Check that any third-party course or book says **CV0-004**; material for the previous version misses the DevOps domain and under-weights architecture.

### Video courses
1. **CompTIA CertMaster Learn for Cloud+** - official self-paced training
2. **ITProTV (ACI Learning) CompTIA Cloud+** - video course with labs
3. **Pluralsight CompTIA Cloud+** - structured learning path
4. **LinkedIn Learning Cloud+ prep** - exam-focused training

### Practice exams
1. **CompTIA CertMaster Practice** - official practice questions
2. **Kaplan IT Training** - practice exams with explanations
3. **Pearson practice tests** - question bank that accompanies the official cert guides

### Books
1. **CompTIA Cloud+ Study Guide: Exam CV0-004** - Sybex/Wiley
2. **CompTIA Cloud+ Certification All-in-One Exam Guide (Exam CV0-004)** - McGraw Hill

## Next steps after certification

### Career paths
- Cloud engineer
- Cloud administrator
- Cloud systems analyst
- Cloud infrastructure specialist
- DevOps engineer

### Further certifications
- **AWS Solutions Architect - Associate** - AWS-specific architecture
- **Azure Administrator Associate (AZ-104)** - Microsoft cloud administration
- **Google Cloud Associate Cloud Engineer** - GCP engineering
- **CompTIA Security+** or **CompTIA CySA+** - deeper security, which builds on Domain 4
- **HashiCorp Terraform Associate** or **CNCF CKA** - deeper DevOps tooling, which builds on Domain 5
