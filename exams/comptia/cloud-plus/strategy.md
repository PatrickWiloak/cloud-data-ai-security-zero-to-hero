---
last-updated: 2026-10-22
applies-to: CompTIA Cloud+ CV0-004 exam objectives v2.0, checked 2026-10-22
difficulty: intermediate
---

# CompTIA Cloud+ (CV0-004) Study Strategy

## How the weights should shape your study

CV0-004 has six domains. Two facts drive the plan:

- **Cloud Architecture is 23%**, the single largest domain, with eleven objectives. It is broad rather than deep: networking, storage, containers, virtualization, cost, databases, AI and IoT all live here. Budget the most time for it.
- **DevOps Fundamentals (10%) is new.** Material written for the old exam does not cover it. Learn what each named tool is for and the integration styles, and you will collect most of these points cheaply.

| Domain | Weight | Share of a 40-hour plan | Notes |
|---|---|---|---|
| 1. Cloud Architecture | 23% | about 10 hours | [01-cloud-architecture](notes/01-cloud-architecture.md) |
| 2. Deployment | 19% | about 7.5 hours | [02-deployment](notes/02-deployment.md) |
| 3. Operations | 17% | about 7 hours | [03-operations](notes/03-operations.md) |
| 4. Security | 19% | about 7.5 hours | [04-security](notes/04-security.md) |
| 5. DevOps Fundamentals | 10% | about 4 hours | [05-devops-fundamentals](notes/05-devops-fundamentals.md) |
| 6. Troubleshooting | 12% | about 4 hours | [06-troubleshooting](notes/06-troubleshooting.md) |

## Study approach

### Phase 1: Foundation (2 weeks)
Read Domain 1 end to end, then Domain 2. Architecture first, because every other domain assumes its vocabulary: you cannot troubleshoot a transit gateway route or choose a deployment strategy without it. Use the [fact sheet](fact-sheet.md) tables as a check after each objective.

### Phase 2: Operate and secure (2 weeks)
Domains 3 and 4, then 5. Operations and Security are scenario heavy ("Given a scenario..."), so after each section work through the matching entries in [scenarios.md](scenarios.md). Get hands on if you can: a free-tier account where you create a VPC with public and private subnets, a NAT gateway, a security group and a load balancer will teach more networking than any reading.

### Phase 3: Troubleshoot and practise (1-2 weeks)
Domain 6 last, because it draws on everything else. Then full timed practice exams. Review every wrong answer back to the objective number it came from, and re-read that section of the notes.

## Exam tactics

### Question strategy
1. **Find the constraint.** Most questions have one deciding phrase: "least cost", "minimal downtime", "fewest changes", "must not traverse the internet", "small team". Underline it mentally before reading the options.
2. **Eliminate.** Two options are usually clearly wrong. Decide between the remaining two by the constraint.
3. **Vendor neutral.** Answers use generic names (dedicated connection, not Direct Connect; network security group or security group, not a product name).
4. **Best practice over workaround.** "Open the port to everyone" or "give the pipeline admin rights" fixes the symptom and is never the answer.
5. **Watch the order words.** "First", "next" and "best" questions about troubleshooting follow the CompTIA methodology. Containment comes before investigation for security incidents; testing a theory comes before implementing a fix.

### Time management
- A maximum of 90 questions in 90 minutes is about 1 minute each, with PBQs taking 3 to 6 minutes.
- PBQs usually appear first. Read each one; if it will clearly take more than 5 minutes, flag it, answer the multiple choice, and come back.
- Do not leave anything blank. There is no penalty for guessing.
- Keep 10 minutes at the end for flagged questions.

### Performance-based questions (PBQs)
PBQs are small simulations: drag and drop, matching, filling in a configuration, or picking the faulty line in output. Likely shapes for CV0-004:

- **Match requirements to resources** (objective 2.5): a list of requirements and a set of storage, compute and network options to place. Check every requirement is met and none violated.
- **Read a template** (2.4): spot the mis-indented YAML line or the trailing comma in JSON; fill in a variable or conditional.
- **Order a process**: troubleshooting methodology, vulnerability management steps (scope, identify, assess, remediate), or a CI/CD pipeline (build, test, scan, publish, deploy).
- **Fix connectivity** (6.2): a route table missing a peering route, a private subnet routed to an internet gateway instead of NAT, a stateless network ACL missing an outbound rule, or a trunk port missing a VLAN.
- **Choose backup and restore** (3.3): pick full, incremental or differential for a given window and RPO, and in-place or parallel, bulk or granular for a given incident.
- **Match tools** (5.4): pair Terraform, Ansible, Docker, Kubernetes, Jenkins, GitHub Actions, ELK, Grafana and Git with their purposes.

Partial credit is generally believed to apply to multi-part PBQs, so complete every part you can.

### Keyword decision matrix

| Keyword in question | Points to |
|---|---|
| "Most cost-effective", steady load | Reserved capacity after rightsizing |
| "Interruptible", "batch", "can tolerate termination" | Spot instances |
| "Per-core licensing", "no shared hardware" | Dedicated host |
| "Spiky", "idle most of the day", "event triggered" | Serverless (FaaS) |
| "Small team", "no patching", "focus on code" | PaaS or managed services |
| "Many VPCs", "hub", "transitive" | Transit gateway |
| "Consistent latency", "must not use internet" | Dedicated connection |
| "Route by URL path", "Layer 7" | Application load balancer |
| "TCP/UDP", "extreme throughput", "static IP" | Network load balancer |
| "Zero downtime, instant rollback" | Blue-green |
| "Small percentage of users first" | Canary |
| "No extra infrastructure, no downtime" | Rolling |
| "Fastest migration, no changes" | Rehost |
| "Managed database, little code change" | Replatform |
| "Shortest backup window" | Incremental |
| "Fastest restore" | Full (or differential) |
| "One deleted file" | Granular restore, ideally parallel |
| "Data lost on container restart" | Persistent volume |
| "Real-time push to browser" | WebSockets |
| "Exactly the fields the client needs" | GraphQL |
| "Provision across clouds" | Terraform |
| "Configure existing servers, agentless" | Ansible |
| "HTTP 429", "Rate exceeded" | API throttling, add backoff |
| "LimitExceeded" | Service quota increase |
| "169.254.x.x address" | DHCP failure |
| "Leaked keys" | Revoke first |

## Domain-specific tips

### 1. Cloud Architecture (23%)
- Memorize the shared responsibility table; data and identity are always the customer's.
- RTO is downtime, RPO is data loss. Do not over-buy a hot site when the RTO is hours.
- VPC peering is not transitive and cannot join overlapping CIDRs.
- SAN is block, NAS is file. Object storage is not mountable as a normal disk.
- Know the tiers (hot, warm, cold, archive) and that archive retrieval takes hours.
- For AI services, match the verb in the scenario (extract text, translate, detect objects, judge sentiment, transcribe, speak, generate).
- IoT questions: sensor, gateway (edge), protocol (MQTT), cloud hub. Each device needs its own identity.

### 2. Deployment (19%)
- A VPC is public cloud, not private cloud.
- Learn the deployment strategy table by heart: downtime, cost, rollback.
- Know all six Rs on the objective list and which is "fastest" (rehost) and which "modernizes most" (re-architect).
- Repatriation (cloud to on-premises) is a real migration type; power and cooling become your problem.
- Read YAML and JSON comfortably. YAML indentation errors are a favourite.
- IaC versus CaC: Terraform builds, Ansible configures.

### 3. Operations (17%)
- Logs, metrics, traces: what, how much, where.
- Logs written only to an auto-scaled instance's disk are lost; aggregate centrally.
- Scaling triggers: trend, load, event, scheduled, manual. Horizontal needs stateless design.
- Backup types are almost guaranteed: practise the restore-set question until it is automatic.
- In-place versus parallel recovery, bulk versus granular.
- End of support means no security patches; plan upgrades before the date.

### 4. Security (19%)
- Vulnerability management order: scope, identify, assess, remediate.
- Sovereignty (whose laws) versus locality (where data is).
- SAML is XML SSO; OIDC is JSON identity on OAuth 2.0; OAuth 2.0 alone is authorization.
- Network ACLs are stateless and subnet level; security groups are stateful.
- Privileged containers are almost never the right answer.
- Know the attack signatures: cryptojacking (CPU and bill), ransomware (mass changes, deleted backups), metadata abuse (169.254.169.254).

### 5. DevOps Fundamentals (10%)
- Commit is local, push is remote, pull request is the review gate.
- Continuous delivery has a manual approval; continuous deployment does not.
- Build the artifact once and promote it. Know RPM, Debian, ZIP and tar as package formats.
- REST, SOAP, RPC, WebSockets, GraphQL and event-driven: one line each on when to use it.
- Nine named tools: one sentence each on what they do.

### 6. Troubleshooting (12%)
- Follow the methodology in order, and answer "what next" questions from it.
- 4xx is client side (401 unauthenticated, 403 forbidden, 429 throttled); 5xx is server side (502, 503, 504 at the load balancer).
- DHCP failure gives 169.254.x.x. NTP skew breaks authentication and signed API calls.
- Missing routes after peering or VPN setup are the most common connectivity fault.
- Access ports carry one VLAN; trunks carry many tagged VLANs.
- Leaked credentials: revoke first. Deprecated ciphers: upgrade the client.

## Common pitfalls

- Studying from material written for the previous exam version: it has five domains, no DevOps domain, and the old weights.
- Confusing HA (prevent downtime) with DR (recover after it).
- Mixing up RTO and RPO.
- Picking the most powerful answer instead of the one that fits the constraint (hot site, multi-region, dedicated host when not needed).
- Confusing incremental and differential restore sets.
- Treating replication as a backup.
- Treating SOC 2, PCI DSS and ISO 27001 as interchangeable.
- Thinking Docker and Kubernetes do the same job.

## Pre-exam checklist

### One week before
- [ ] Scoring 80% or more consistently on timed practice exams
- [ ] Every note read at least twice, with weak objectives re-read
- [ ] [Scenarios](scenarios.md) worked through for all six domains
- [ ] Fact sheet tables can be reproduced from memory

### Day before
- [ ] Light review of the [fact sheet](fact-sheet.md) only
- [ ] Confirm appointment, ID and (for online) the room and system check
- [ ] Sleep

### Exam day
- [ ] Arrive 15 minutes early, or start online check-in early
- [ ] Skim PBQs first, flag long ones
- [ ] Read every option before choosing
- [ ] Review flagged questions at the end; change an answer only with a clear reason
