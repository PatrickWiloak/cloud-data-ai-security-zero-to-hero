---
last-updated: 2026-10-22
applies-to: CompTIA Cloud+ CV0-004 exam objectives v2.0, checked 2026-10-22
difficulty: intermediate
---

# CompTIA Cloud+ (CV0-004) Study Plan

A six-week plan at about 1.5 to 2 hours a day, built around the six CV0-004 domains and their weights. Each day names the note to read. Practice questions are in [comptia-cloud-plus.md](../../../resources/practice-questions/comptia-cloud-plus.md).

## Time allocation by weight

| Domain | Weight | Study days | Note |
|---|---|---|---|
| 1. Cloud Architecture | 23% | 9 | [01-cloud-architecture.md](notes/01-cloud-architecture.md) |
| 2. Deployment | 19% | 4 plus week 2 review | [02-deployment.md](notes/02-deployment.md) |
| 3. Operations | 17% | 5 | [03-operations.md](notes/03-operations.md) |
| 4. Security | 19% | 6 | [04-security.md](notes/04-security.md) |
| 5. DevOps Fundamentals | 10% | 3 | [05-devops-fundamentals.md](notes/05-devops-fundamentals.md) |
| 6. Troubleshooting | 12% | 3 plus week 5 review | [06-troubleshooting.md](notes/06-troubleshooting.md) |
| Weekly reviews and full practice exams | - | 12 | [fact-sheet.md](fact-sheet.md), [strategy.md](strategy.md) |

## Week 1: Cloud Architecture, part 1

#### Day 1: Service models and shared responsibility (1.1)
- [ ] Read `notes/01-cloud-architecture.md` section 1.1
- [ ] Reproduce the shared responsibility table from memory
- [ ] For IaaS, PaaS, SaaS and FaaS, write one scenario that points to each

#### Day 2: Availability and DR (1.2)
- [ ] Read section 1.2: regions, AZs, cloud bursting, edge, availability monitoring
- [ ] RTO versus RPO; hot, warm and cold sites; multicloud tenancy
- [ ] Work the "Designing for High Availability" entry in [scenarios.md](scenarios.md)

#### Day 3-4: Cloud networking (1.3)
- [ ] Read section 1.3: VPN versus dedicated connection, ALB versus NLB, application gateway, CDN
- [ ] VPC peering (not transitive) versus transit gateway
- [ ] Subnets, VLAN, SDN, BGP, static routes, route tables
- [ ] Hands on if possible: build a VPC with a public and a private subnet, an internet gateway and a NAT gateway, then read the route tables

#### Day 5: Storage (1.4)
- [ ] Read section 1.4: hot, warm, cold, archive; SSD versus HDD
- [ ] Object versus block versus file, with a use case for each
- [ ] IOPS versus throughput; retrieval cost traps

#### Day 6: Cloud-native and containers (1.5, 1.6)
- [ ] Microservices, loose coupling, fan-out, service discovery
- [ ] Stand-alone versus orchestrated containers, port mapping, persistent versus ephemeral storage, registries

#### Day 7: Week 1 review
- [ ] Practice questions for objectives 1.1-1.6 (target 65%+)
- [ ] Re-read every section where you missed a question

## Week 2: Cloud Architecture, part 2, and Deployment begins

#### Day 8: Virtualization (1.7)
- [ ] Clustering, cloning, host affinity and anti-affinity, hardware pass-through
- [ ] Overlay versus VM networks; local storage versus SAN (block) versus NAS (file)

#### Day 9: Cost and databases (1.8, 1.9)
- [ ] Dedicated host, reserved, pay-as-you-go, spot; metering, tagging, rightsizing
- [ ] Relational versus non-relational; self-managed versus provider-managed
- [ ] Work the "Cost Optimization" scenario

#### Day 10: Workload optimization and evolving tech (1.10, 1.11)
- [ ] VM versus container versus serverless; orchestration versus workflow; latency versus throughput; IOPS
- [ ] AI services by what they do; generative AI; IoT sensors, gateways, communication, MQTT

#### Day 11: Deployment models and strategies (2.1, 2.2)
- [ ] Read `notes/02-deployment.md` sections 2.1 and 2.2
- [ ] Learn the blue-green, canary, rolling, in-place table: downtime, cost, rollback

#### Day 12: Migration (2.3)
- [ ] Migration types including cloud to on-premises
- [ ] Considerations: compatibility, cost and egress, vendor lock-in, power and cooling, regulatory
- [ ] Rehost, replatform, refactor, re-architect, retain, retire
- [ ] Work the "Migration Strategy Selection" scenario

#### Day 13: Code to deploy (2.4)
- [ ] IaC versus CaC, declarative versus imperative, idempotency
- [ ] Variables, conditionals, operators, data types, functions
- [ ] Drift detection, versioning, testing, documentation
- [ ] Read and write a short JSON and YAML file describing the same thing

#### Day 14: Week 2 review
- [ ] Practice questions for 1.7-1.11 and 2.1-2.4 (target 70%+)
- [ ] Full Domain 1 review against the [fact sheet](fact-sheet.md)

## Week 3: Deployment ends, Operations

#### Day 15: Provisioning to requirements (2.5)
- [ ] Read section 2.5 and the uptime math table
- [ ] Take three scenarios and list every requirement type they contain before choosing resources

#### Day 16: Observability (3.1)
- [ ] Read `notes/03-operations.md` section 3.1
- [ ] Logging collection, aggregation, retention; tracing; metrics; alert triage and response
- [ ] Work the "Monitoring and Alerting Strategy" scenario

#### Day 17: Scaling (3.2)
- [ ] Trend, load, event, scheduled, manual triggers
- [ ] Horizontal versus vertical; why state breaks scale-in

#### Day 18-19: Backup and recovery (3.3)
- [ ] Full, incremental, differential: what each copies and what a restore needs
- [ ] On-site versus off-site, schedule from RPO, retention, replication, encryption
- [ ] Testing recoverability and integrity
- [ ] In-place versus parallel; bulk versus granular
- [ ] Work the backup and recovery scenarios

#### Day 20: Life cycle (3.4)
- [ ] Patches, minor and major updates, testing
- [ ] Ephemeral versus persistent data; end of life versus end of support; decommissioning steps

#### Day 21: Week 3 review
- [ ] Practice questions for 2.5 and Domain 3 (target 70%+)

## Week 4: Security

#### Day 22: Vulnerability management and compliance (4.1, 4.2)
- [ ] Read `notes/04-security.md` sections 4.1 and 4.2
- [ ] Scope, identify, assess, remediate; CVE, CVSS, CWE
- [ ] Sovereignty, ownership, locality, classification, retention, litigation hold
- [ ] SOC 2, PCI DSS, ISO 27001, Cloud Security Alliance

#### Day 23-24: Identity and access management (4.3)
- [ ] Programmatic access (API, SDK, CLI), web portal, SSH, RDP, bastion hosts
- [ ] Local users, federation, SAML, token-based, directory, MFA, OIDC
- [ ] RBAC, group-based, OAuth 2.0, discretionary; audit trail
- [ ] Work the "Implementing Zero Trust Access" scenario

#### Day 25: Best practices (4.4)
- [ ] Zero Trust, CIS and vendor benchmarks, hardening, encryption, secrets management
- [ ] API security, least privilege, privileged versus unprivileged containers, storage security

#### Day 26: Controls and attacks (4.5, 4.6)
- [ ] Endpoint protection, DLP, IDS versus IPS, DDoS, IAM policies
- [ ] Network ACL versus network security group versus WAF
- [ ] Attack signs: phishing, ransomware, DDoS, cryptojacking, zombie instances, metadata abuse

#### Day 27: Security scenarios
- [ ] Work every Security scenario in [scenarios.md](scenarios.md)

#### Day 28: Week 4 review
- [ ] Practice questions for Domain 4 (target 75%+)

## Week 5: DevOps Fundamentals and Troubleshooting

#### Day 29: Source control and CI/CD (5.1, 5.2)
- [ ] Read `notes/05-devops-fundamentals.md` sections 5.1 and 5.2
- [ ] Commit, push, branch, pull request, review, merge
- [ ] CI versus continuous delivery versus continuous deployment; artifacts and repositories

#### Day 30: Integration and tools (5.3, 5.4)
- [ ] Event-driven, REST, SOAP, RPC, WebSockets, GraphQL
- [ ] One sentence each: Ansible, Docker, ELK, Git, GitHub Actions, Grafana, Jenkins, Kubernetes, Terraform

#### Day 31: DevOps review
- [ ] Practice questions for Domain 5 (target 75%+)
- [ ] Work the DevOps scenarios

#### Day 32: Methodology and deployment issues (6.1)
- [ ] Read `notes/06-troubleshooting.md` methodology and section 6.1
- [ ] Permissions, oversubscription, sizing, deprecation, throttling, quotas, regional availability

#### Day 33: Network issues (6.2)
- [ ] DHCP, DNS, NTP, NAT, HTTP status codes
- [ ] Scope exhaustion, overlap, missing and misconfigured routes, VLAN tags, access versus trunk
- [ ] Run the diagnostic commands in the note on a Linux VM

#### Day 34: Security issues (6.3)
- [ ] Cipher suite deprecation, privilege escalation, unauthorized access, leaked credentials, vulnerable and unauthorized software
- [ ] Work every Troubleshooting scenario

#### Day 35: Week 5 review
- [ ] Mixed practice questions across all six domains (target 75%+)

## Week 6: Full practice exams and final review

#### Day 36-37: Full practice exams
- [ ] Two timed full-length practice exams (90 minutes each)
- [ ] Tag every wrong answer with its objective number

#### Day 38-39: Weak areas
- [ ] Re-read the note sections for your three weakest objectives
- [ ] Redo the matching scenarios

#### Day 40-41: PBQ preparation and final practice exam
- [ ] Review the PBQ shapes in [strategy.md](strategy.md)
- [ ] One more timed full practice exam (target 80%+)

#### Day 42: Final review
- [ ] [Fact sheet](fact-sheet.md) only
- [ ] Exam logistics: ID, time, room or test centre

## Daily routine (about 1.5 to 2 hours)

1. **40 minutes** - read the day's note section
2. **20 minutes** - check yourself against the fact sheet tables and flashcards
3. **30 minutes** - practice questions or scenarios for the same objectives
4. **15 minutes** - review wrong answers and note which objective they map to

## Target scores

- [ ] Week 1: 65%+ on Domain 1 questions
- [ ] Week 2: 70%+ on Domains 1-2
- [ ] Week 3: 70%+ on Domains 2-3
- [ ] Week 4: 75%+ on Domain 4
- [ ] Week 5: 75%+ on mixed questions
- [ ] Week 6: 80%+ consistently on full practice exams

## Resources

**[📖 CV0-004 Exam Objectives v2.0 (PDF)](https://comptiacdn.azureedge.net/webcontent/docs/default-source/exam-objectives/comptia-cloud-cv0-004-exam-objectives-%282-0%29.pdf)** - tick off each objective as you finish it.

**[📖 CompTIA Cloud+ certification page](https://www.comptia.org/en-us/certifications/cloud/)** - official CertMaster Learn, Practice and Labs.

**[📖 NIST SP 800-145](https://csrc.nist.gov/pubs/sp/800/145/final)** - cloud definitions behind 1.1 and 2.1.

**[📖 Terraform documentation](https://developer.hashicorp.com/terraform/docs)** - IaC reference for 2.4 and 5.4.

**[📖 Kubernetes documentation](https://kubernetes.io/docs/home/)** - container orchestration for 1.6 and 5.4.

## Final checklist

- [ ] Every objective in the PDF ticked
- [ ] Can reproduce the fact sheet tables (deployment strategies, backup types, scaling triggers, HTTP codes, DevOps tools) from memory
- [ ] 80%+ on two consecutive full practice exams
- [ ] Exam booked and logistics confirmed
