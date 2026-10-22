---
last-updated: 2026-10-22
---

# SOA-C03 Study Strategy

SOA-C03 has five domains with three of them tied for the largest share. That shapes the plan: no single domain dominates, so you cannot pass by mastering one area. Breadth with operational depth is what scores.

## Time allocation by weight

| Domain | Weight | Share of study time | Notes |
|---|---|---|---|
| 1. Monitoring, Logging, Analysis, Remediation, and Performance Optimization | 22% | about 25% (it has three tasks and the most services) | [01](./notes/01-monitoring-logging.md), [01b](./notes/01b-performance-optimization.md) |
| 2. Reliability and Business Continuity | 22% | about 20% | [02](./notes/02-reliability-business-continuity.md) |
| 3. Deployment, Provisioning, and Automation | 22% | about 22% | [03](./notes/03-deployment-automation.md) |
| 4. Security and Compliance | 16% | about 15% | [04](./notes/04-security-compliance.md) |
| 5. Networking and Content Delivery | 18% | about 18% | [05](./notes/05-networking.md) |

Domain 1 gets a little more than its weight because Task 1.3 (performance across EC2, EBS, S3, EFS, FSx, S3 Files and RDS) is wide, and because CloudWatch and EventBridge show up inside questions from every other domain too. Domain 2 gets a little less because much of it (Auto Scaling, ELB, Multi-AZ) overlaps with what you learn for Domains 1 and 3.

In exam terms, the 50 scored questions split roughly 11 / 11 / 11 / 8 / 9.

## Study approach

### Phase 1: Foundations (weeks 1-2)

Start with Domain 1, because everything else depends on reading signals. Get hands-on with CloudWatch metrics, the CloudWatch agent, alarms, Logs Insights, CloudTrail and EventBridge. Build one end-to-end loop yourself: an alarm on a custom metric, an EventBridge rule on its state change, and a Systems Manager Automation runbook that fixes the resource. Then work through performance (note 01b) with real EBS and RDS metrics.

### Phase 2: Operating patterns (weeks 3-5)

Domains 2 and 3 together. Build an Auto Scaling group behind an ALB across three AZs, break its health checks on purpose and fix them. Deploy it with CloudFormation, then change it with a change set, cause a rollback, and recover. Create an Image Builder pipeline. Restore an RDS instance to a point in time and notice it is a new endpoint. Set up AWS Backup by tag.

### Phase 3: Security and networking (weeks 5-7)

Domain 4: use the policy simulator and Access Analyzer on a deliberately broken policy; set up Config conformance packs with automatic remediation; encrypt an unencrypted EBS volume via snapshot copy. Domain 5: build public and private subnets with a NAT gateway and a gateway endpoint, break routing and NACLs, use Reachability Analyzer and flow logs to find the fault, and configure Resolver endpoints if you can.

### Phase 4: Practice and review (week 8)

Official practice question set and practice exam on AWS Skill Builder, then third-party practice exams. Review every wrong answer back to the note and the AWS documentation page.

## Per-domain tactics

**Domain 1.** Questions describe a missing or wrong signal. Ask: is the data collected (agent, data events)? Is the alarm evaluating correctly (dimensions, period, missing data)? Can the action run (SNS policy, EventBridge target permission, runbook assume role)? For performance, match the bottleneck metric to the fix: `VolumeQueueLength` to a faster volume or bigger instance, `DatabaseConnections` to RDS Proxy, `CPUCreditBalance` to unlimited mode or a fixed-performance instance.

**Domain 2.** Look for the scaling or resilience mechanism that is **automatic**. Target tracking over manual changes, ELB health checks over EC2 checks, Multi-AZ over single-AZ, AWS Backup over scripts. For restores, match the option to the stated RPO and RTO and remember PITR creates a new resource.

**Domain 3.** Know what each CloudFormation state means and the one action that recovers from it. Prefer managed, repeatable options: Image Builder over hand-built AMIs, StackSets over per-account deploys, RAM sharing over duplication, Systems Manager over SSH scripts. OpsWorks is never the answer.

**Domain 4.** Most questions are "why is this denied?" or "how do we enforce this automatically?". Trace the policy layers (SCP, boundary, identity, resource, session) and pick the tool that answers the question asked: simulator, Access Analyzer or CloudTrail. For findings, the answer is usually EventBridge to an automated fix.

**Domain 5.** Troubleshoot in order: security group, NACL, route table, gateway, DNS. Know the cost-saving moves (gateway endpoints, same-AZ traffic, CloudFront) and the logging specifics (flow log fields, WAF log naming, query logging Regions).

## Exam tactics

- **2 minutes per question** on average (130 minutes, 65 questions). Flag anything over 3 minutes and return.
- **Keywords**: "least operational overhead" (managed, automated), "least privilege", "without downtime", "most cost-effective" (still only within the stated requirements).
- **Eliminate** answers that are manual, use retired services (OpsWorks), or design something the question did not ask for.
- **Multiple response**: the question tells you how many to pick; each must be independently correct.
- There are **no exam labs** on SOA-C03, but practice in a real account anyway: hands-on time is what makes troubleshooting questions easy.

## Resources

- **[📖 SOA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/sysops-administrator-associate-03.html)** - domains, tasks and in-scope services
- **[📖 Official exam page](https://aws.amazon.com/certification/certified-cloudops-engineer-associate/)** - registration and exam prep resources
- **[📖 AWS Skill Builder](https://skillbuilder.aws/)** - official exam prep, question sets and practice exam
- **[📖 AWS Free Tier](https://aws.amazon.com/free/)** - hands-on practice

## Common pitfalls

- Treating the exam as a design exam. It asks how to operate and fix, with the least effort.
- Skipping the CloudWatch agent and EventBridge details; they appear in every domain.
- Studying old SOA-C02 material: it has exam labs, a separate cost domain and OpsWorks, all of which are gone.
- Over-studying billing and TCO, which are out of scope.
- Ignoring the v1.1 additions (Bedrock monitoring, DevOps Agent, Security Agent, Kiro, Health Dashboard, S3 Files). Expect light, "which tool fits" questions on them.
