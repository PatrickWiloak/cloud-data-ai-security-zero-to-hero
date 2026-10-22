---
last-updated: 2026-10-22
applies-to: CompTIA Cloud+ CV0-004 exam objectives v2.0, checked 2026-10-22
difficulty: intermediate
---

# CompTIA Cloud+ (CV0-004) Fact Sheet

## Quick Reference

**Exam Code:** CV0-004
**Duration:** 90 minutes
**Questions:** Maximum of 90 (multiple choice and performance-based)
**Passing Score:** 750 (on a scale of 100-900)
**Cost:** $369 USD
**Validity:** 3 years
**Delivery:** Pearson VUE (testing center or online proctored)

Launched December 18, 2024. Recommended experience: 2-3 years as a systems administrator or cloud engineer, plus Network+ and Server+ level knowledge.

**[📖 CV0-004 Exam Objectives v2.0 (PDF)](https://comptiacdn.azureedge.net/webcontent/docs/default-source/exam-objectives/comptia-cloud-cv0-004-exam-objectives-%282-0%29.pdf)** - the authoritative domain and objective list.

**[📖 CompTIA Cloud+ certification page](https://www.comptia.org/en-us/certifications/cloud/)** - exam details and official training.

## Exam Domain Breakdown

| # | Domain | Weight | Objectives | Notes |
|---|---|---|---|---|
| 1 | Cloud Architecture | 23% | 1.1-1.11 | [01-cloud-architecture](notes/01-cloud-architecture.md) |
| 2 | Deployment | 19% | 2.1-2.5 | [02-deployment](notes/02-deployment.md) |
| 3 | Operations | 17% | 3.1-3.4 | [03-operations](notes/03-operations.md) |
| 4 | Security | 19% | 4.1-4.6 | [04-security](notes/04-security.md) |
| 5 | DevOps Fundamentals | 10% | 5.1-5.4 | [05-devops-fundamentals](notes/05-devops-fundamentals.md) |
| 6 | Troubleshooting | 12% | 6.1-6.3 | [06-troubleshooting](notes/06-troubleshooting.md) |

## Domain 1: Cloud Architecture

### Service models and shared responsibility

| Model | Provider runs | You run | Examples |
|---|---|---|---|
| **IaaS** | Hardware, network, hypervisor | OS, runtime, apps, data | EC2, Azure VMs, Compute Engine |
| **PaaS** | IaaS plus OS, middleware, runtime | Apps, data | App Service, Elastic Beanstalk, App Engine |
| **SaaS** | Whole application | Configuration, users, data | Microsoft 365, Salesforce |
| **FaaS** | Everything but the function | Function code, triggers | Lambda, Azure Functions |

- Provider: security **of** the cloud. Customer: security **in** the cloud. Data and identity are always the customer's.
- IaaS guest OS patching is the customer's job.

### Availability and DR

- **Region** - geographic area. **AZ** - isolated data centre(s) inside a region.
- **Cloud bursting** - overflow from private to public cloud at peak.
- **Edge computing** - compute near users or devices for low latency.
- **RTO** - max downtime. **RPO** - max data loss, in time.

| DR site | State | Recovery time | Cost |
|---|---|---|---|
| **Hot** | Fully running, current data | Minutes or less | Highest |
| **Warm** | Partly running, recent data | Hours | Medium |
| **Cold** | Space and power, restore from backup | Days | Lowest |

### Networking

| Item | Remember |
|---|---|
| **VPN** | Encrypted over internet, quick, cheap, variable latency |
| **Dedicated connection** | Private circuit (Direct Connect, ExpressRoute, Cloud Interconnect), steady latency, weeks to provision, not encrypted by default |
| **Application load balancer** | Layer 7, routes by path or host, terminates TLS |
| **Network load balancer** | Layer 4, TCP and UDP, very high throughput, static IP |
| **Application gateway** | Layer 7 proxy, often with WAF |
| **CDN** | Edge caching for static content, lower latency, DDoS absorption |
| **VPC peering** | One-to-one, **not transitive**, no overlapping CIDRs |
| **Transit gateway** | Hub and spoke for many VPCs and on-premises links, transitive |
| **VLAN** | Layer 2 segmentation by 802.1Q tag |
| **SDN** | Central software control plane; every cloud VPC is SDN |
| **BGP** | Dynamic route exchange, automatic failover on dedicated links |
| **Route table** | Longest prefix match wins |

### Storage

| Tier | Access | Store cost | Retrieval |
|---|---|---|---|
| **Hot** | Frequent | Highest | Cheapest, instant |
| **Warm** | Monthly | Lower | Per-access fee |
| **Cold** | Rare | Lower again | Higher fee |
| **Archive** | Compliance, almost never | Lowest | Hours, highest fee |

- **Block** - VM disks, lowest latency (EBS, Managed Disks). **File** - shared NFS or SMB mounts (EFS, Azure Files). **Object** - HTTP API, buckets, massive scale (S3, Blob, Cloud Storage).
- **SSD** - high IOPS, databases and boot. **HDD** - cheap, sequential throughput.
- **IOPS** - small random operations. **Throughput** - MB per second for large sequential transfers.

### Cloud-native, containers, virtualization

- **Microservices**, **loose coupling** (queues and events), **fan-out** (one message to many consumers), **service discovery** (registry or DNS instead of hard-coded IPs).
- **Stand-alone container** - one host, no self-healing. **Orchestration** - Kubernetes schedules, heals, scales.
- **Port mapping** - host port to container port. **Persistent volume** survives restarts; **ephemeral storage** does not.
- **Image registry** - public (Docker Hub) or private (ECR, ACR, Artifact Registry).
- **Clustering** - hosts pooled, live migration. **Cloning** - copy a VM. **Host affinity / anti-affinity** - keep VMs together or apart. **Hardware pass-through** - direct GPU or NIC access, blocks live migration.
- **Overlay network** - virtual L2 over L3 (VXLAN). **SAN** - block over Fibre Channel or iSCSI. **NAS** - file over NFS or SMB.

### Cost

| Model | Best for | Watch out |
|---|---|---|
| **Pay-as-you-go** | New, short or unpredictable | Highest unit price |
| **Reserved** | Steady baseload, 1 or 3 years | Commitment; rightsize first |
| **Spot** | Batch, CI, rendering | Reclaimed at short notice |
| **Dedicated host** | Per-core licensing, compliance | Most expensive |

- **Metering** - usage measured per resource. **Tagging** - cost allocation by team or project. **Rightsizing** - match size to real use.

### Databases, workloads, evolving tech

- **Relational** - SQL, schema, ACID transactions. **Non-relational** - key-value, document, wide-column, graph; scale out.
- **Self-managed** - full control, you patch and back up. **Provider-managed** - DBaaS, less effort.
- **VM** for full control, **container** for density and portability, **serverless** for spiky event-driven work.
- **Workflow** services coordinate multi-step processes with retries (Step Functions, Logic Apps).
- AI services: text recognition (OCR), translation, visual recognition, sentiment analysis, speech-to-text, text-to-speech, generative AI.
- IoT: sensors, gateways (edge processing, protocol translation), communication (Wi-Fi, cellular, LoRaWAN), protocols (MQTT, CoAP, AMQP).

## Domain 2: Deployment

- **Public / private (on premises or hosted) / hybrid / community.** A VPC is still public cloud.

| Strategy | Downtime | Extra cost | Rollback |
|---|---|---|---|
| **Blue-green** | None | High | Instant switch back |
| **Canary** | None | Low | Route canary traffic back |
| **Rolling** | None | None | Roll old version back out |
| **In-place** | Yes | None | Reinstall |

- Migration types: **on-premises to cloud**, **cloud to on-premises** (repatriation), **cloud to cloud**.
- Considerations: storage, platform compatibility, compute, cost (egress), networking, management overhead, service availability, vendor lock-in, power and cooling, regulatory and compliance.
- **Rehost** (lift and shift) / **replatform** (managed services, minimal code change) / **refactor** (code changes) / **re-architect** (redesign, microservices) / **retain** / **retire**.
- **IaC** builds infrastructure (Terraform, CloudFormation, Bicep). **CaC** configures inside it (Ansible, Chef, Puppet).
- Scripting: variables, conditionals, operators, data types (string, integer, boolean, list, map), functions.
- **Drift** - manual change not in code; find it with `terraform plan` or drift detection.
- **JSON** - braces, quoted keys, no comments. **YAML** - indentation is syntax, `#` comments, dashes for lists.

### Uptime math

| SLA | Per year | Per 30-day month |
|---|---|---|
| 99% | 3.65 days | 7.2 hours |
| 99.9% | 8.77 hours | 43.8 minutes |
| 99.95% | 4.38 hours | 21.9 minutes |
| 99.99% | 52.6 minutes | 4.4 minutes |
| 99.999% | 5.26 minutes | 26 seconds |

Series: multiply availabilities. Parallel redundant: 1 - (product of failure rates).

## Domain 3: Operations

- **Logs** (what happened) - collect, aggregate, retain. **Metrics** (how much) - dashboards and alarms. **Traces** (where in the call path) - spans with a trace ID.
- **Alerting** - triage by severity and owner, respond with runbooks or automation. Alert on symptoms.

### Scaling

| Approach | Trigger |
|---|---|
| **Trend** | Predicted from history (predictive scaling) |
| **Load** | Live metric threshold (CPU, queue depth) |
| **Event** | A message, file or webhook arrives |
| **Scheduled** | Calendar time |
| **Manual** | Operator |

- **Horizontal** - add instances, needs stateless app. **Vertical** - bigger instance, ceiling and restart.

### Backup types

| Type | Copies | Backup speed | Restore needs |
|---|---|---|---|
| **Full** | Everything | Slowest | One set |
| **Incremental** | Changes since last backup of any type | Fastest | Full plus every incremental |
| **Differential** | Changes since last full | Medium, grows daily | Full plus latest differential |

- **On-site** - fast restore, same disaster. **Off-site** - survives site loss.
- Schedule set by RPO. Retention set by law, contract and policy. Encrypt backups. Replication is not a backup.
- Test **recoverability** (can it restore, within RTO) and **integrity** (is the data correct).
- **In-place** - overwrite original. **Parallel** - restore alongside. **Bulk** - whole system. **Granular** - one file, mailbox or table.
- 3-2-1: three copies, two media, one off site; add an immutable copy against ransomware.

### Life cycle

- **Patch** - urgent fix. **Minor update** - compatible. **Major update** - may break, plan and test.
- **Ephemeral data** - dies with the resource. **Persistent data** - survives, must be deleted deliberately.
- **End of life** - no longer sold or developed. **End of support** - no more patches.

## Domain 4: Security

- Vulnerability management: **scope, identify, assess, remediate**, then rescan. **CVE** - ID. **CVSS** - 0-10 score. **CWE** - weakness type.
- **Sovereignty** - whose laws apply. **Locality** - where data sits. **Ownership** - who decides. **Classification** - sensitivity labels. **Litigation hold** - overrides deletion.
- **SOC 2** - audit report (Type II covers a period). **PCI DSS** - card data. **ISO 27001** - ISMS certification. **CSA** - Cloud Controls Matrix and STAR registry.

### IAM

| Term | Meaning |
|---|---|
| **API / SDK / CLI** | Programmatic access to the management plane; prefer short-lived credentials |
| **Bastion host** | Hardened jump box; never open SSH (22) or RDP (3389) to the world |
| **Federation** | Trust an external IdP |
| **SAML** | XML assertions, enterprise SSO |
| **OIDC** | JSON tokens, identity on top of OAuth 2.0 |
| **OAuth 2.0** | Delegated authorization with scopes |
| **MFA** | Two different factor types |
| **RBAC** | Permissions by role |
| **DAC** | Owner decides access |
| **Audit trail** | CloudTrail, Activity Log, Cloud Audit Logs |

### Best practices and controls

- Zero Trust, CIS and vendor benchmarks, hardening, patching, encryption in transit (TLS 1.2+) and at rest (AES-256), secrets manager, API security, least privilege, unprivileged containers, block public object storage.

| Control | Layer | State |
|---|---|---|
| **Network ACL** | Subnet | Stateless, allow and deny, numbered order |
| **Network security group** | Instance or NIC | Stateful |
| **WAF** | Layer 7 | Blocks SQL injection, XSS, bots |
| **IDS / IPS** | Network or host | Detect only / inline block |
| **DLP** | Data | Stops sensitive data leaving |

### Attack signs

| Sign | Attack |
|---|---|
| High CPU on idle instances, unknown regions, surprise bill | Cryptojacking |
| Mass file changes, deleted snapshots | Ransomware |
| Logins from new locations after suspicious email | Phishing |
| Credential requests to 169.254.169.254 via the web app | Metadata service abuse (SSRF) |
| Old unmanaged instances still running | Zombie instances |
| Traffic flood from many sources | DDoS |

## Domain 5: DevOps Fundamentals

- **Commit** (local snapshot), **push** (to remote), **branch** (isolated line of work), **pull request** (ask to merge), **code review**, **merge**.
- **CI** - integrate and test every change. **Continuous delivery** - ready to release, manual approval. **Continuous deployment** - automatic to production.
- Pipeline: build, test, security scan, publish artifact, deploy, monitor. Build once, promote the same artifact.
- Artifacts: VM images, container images, packages (**RPM**, **Debian**, **ZIP**, **tar**), flat files. Repositories: public or private.

### Integration styles

| Style | Use it when |
|---|---|
| **Event-driven** | Many consumers react independently; loose coupling |
| **REST** | Resource URLs and HTTP verbs, JSON, stateless |
| **SOAP** | Strict XML contract, WS-Security, legacy enterprise |
| **RPC (gRPC)** | Fast typed service-to-service calls |
| **WebSockets** | Two-way real-time push |
| **GraphQL** | Client asks for exactly the fields it needs |

### DevOps tools

| Tool | Purpose |
|---|---|
| **Terraform** | Declarative multi-cloud IaC with state |
| **Ansible** | Agentless configuration management, YAML playbooks over SSH |
| **Docker** | Build and run container images |
| **Kubernetes** | Orchestrate containers at scale |
| **Git** | Distributed version control |
| **GitHub Actions** | CI/CD workflows in GitHub, YAML |
| **Jenkins** | Self-hosted CI/CD server, plugins, Jenkinsfile |
| **ELK** | Elasticsearch store and search, Logstash ingest, Kibana dashboards |
| **Grafana** | Dashboards and alerts across many data sources |

## Domain 6: Troubleshooting

### Methodology

1. Identify the problem
2. Establish a theory of probable cause
3. Test the theory
4. Establish a plan of action
5. Implement the solution or escalate
6. Verify full functionality and add preventive measures
7. Document findings

### Deployment

- **403 / AccessDenied** - permissions. **429 / Rate exceeded** - API throttling, use backoff. **LimitExceeded** - service quota, request increase.
- **Oversubscription** - high steal time or storage latency. **Sizing** - wrong instance or volume size.
- **Outdated definitions** and **deprecation** - old images, runtimes, API versions fail.
- **Regional availability** - service or instance type missing in that region.
- **ImagePullBackOff** - wrong image or registry auth. **CrashLoopBackOff** - app exits, read logs. **Pending** - no capacity.

### Network

| Symptom | Likely cause |
|---|---|
| 169.254.x.x address | DHCP failure |
| "Could not resolve host" | DNS record, resolver or zone association |
| Auth fails, "request expired" | NTP clock skew |
| Private subnet cannot reach internet | NAT gateway or its route |
| Cannot peer or route two networks | Overlapping CIDR |
| New instances fail, no free IPs | Scope exhaustion |
| VPN up, no traffic | Missing route |
| VMs on one VLAN lost after port change | Access port or VLAN not allowed on trunk |
| Old clients fail TLS after update | Protocol or cipher suite deprecation |

### HTTP status codes

- **401** unauthenticated, **403** forbidden, **404** not found, **429** throttled.
- **500** app error, **502** bad response from backend, **503** no healthy backend, **504** backend timeout.

### Security

- **Leaked credentials** - revoke first, then investigate the audit trail.
- **Privilege escalation** - remove self-granting permissions, use permission boundaries.
- **Unauthorized access** - remove public exposure, revoke sessions, add guardrails.
- **Cipher suite deprecation** - upgrade the client, do not weaken the server.
- **Unauthorized software** - remove, find the entry point, enforce allow-lists.

## Further reading

**[📖 NIST SP 800-145 - The NIST Definition of Cloud Computing](https://csrc.nist.gov/pubs/sp/800/145/final)** - service and deployment model definitions.

**[📖 CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)** - hardening baselines for OS, Kubernetes and cloud accounts.

**[📖 Cloud Security Alliance](https://cloudsecurityalliance.org/)** - Cloud Controls Matrix and STAR registry.

**[📖 OWASP](https://owasp.org/)** - Top 10 web and API security risks.
