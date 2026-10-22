---
last-updated: 2026-10-22
---

# AWS Certified CloudOps Engineer - Associate (SOA-C03)

## Exam Overview

The AWS Certified CloudOps Engineer - Associate (SOA-C03) exam validates the ability to deploy, manage and operate workloads on AWS. It replaced the SysOps Administrator - Associate (SOA-C02). The exam is operational: it asks how to monitor, troubleshoot, automate, secure and recover running systems, usually with the least operational overhead.

**Exam Details:**
- **Exam Code:** SOA-C03
- **Duration:** 130 minutes
- **Number of Questions:** 65 (50 scored + 15 unscored)
- **Question Types:** Multiple choice and multiple response (no exam labs)
- **Passing Score:** 720 out of 1000 (scaled, compensatory scoring)
- **Cost:** $150 USD
- **Language:** English, Japanese, Korean, and Simplified Chinese
- **Delivery:** Pearson VUE testing center or online proctoring
- **Validity:** 3 years
- **Prerequisites:** None. AWS recommends 1 year of AWS deployment, management, troubleshooting, networking and security experience and 1 year in an operations role
- **Exam guide:** version 1.1 (2026-06-01)

**Official Resources:**
- **[📖 Official Exam Page](https://aws.amazon.com/certification/certified-cloudops-engineer-associate/)** - Registration and details
- **[📖 SOA-C03 Exam Guide](https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/sysops-administrator-associate-03.html)** - Domains, task statements, in-scope and out-of-scope services
- **[📖 In-scope AWS services](https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/soa-03-in-scope-services.html)** - Service list for the exam
- **[📖 AWS Skill Builder](https://skillbuilder.aws/)** - Official exam prep and practice exam

## Exam Domains

| Domain | Weight | Tasks |
|---|---|---|
| 1. Monitoring, Logging, Analysis, Remediation, and Performance Optimization | 22% | 1.1 Metrics, alarms and filters; 1.2 Identify and remediate issues; 1.3 Performance optimization for compute, storage and databases |
| 2. Reliability and Business Continuity | 22% | 2.1 Scalability and elasticity; 2.2 Highly available and resilient environments; 2.3 Backup and restore |
| 3. Deployment, Provisioning, and Automation | 22% | 3.1 Provision and maintain cloud resources; 3.2 Automate management of existing resources |
| 4. Security and Compliance | 16% | 4.1 Security and compliance tools and policies; 4.2 Protect data and infrastructure |
| 5. Networking and Content Delivery | 18% | 5.1 Networking features and connectivity; 5.2 Domains, DNS and content delivery; 5.3 Troubleshoot network connectivity |

There is no separate cost or performance domain. Performance optimization is Task 1.3, and network cost optimization is Task 5.1.4. Cost and TCO analysis and billing are out of scope. Guide v1.1 added Amazon Bedrock, AWS DevOps Agent, AWS Health Dashboard, Kiro and AWS Security Agent to the in-scope services.

## Study Materials

| Material | Covers |
|---|---|
| [01 - Monitoring, Logging, Analysis, and Remediation](./notes/01-monitoring-logging.md) | Domain 1, Tasks 1.1-1.2: CloudWatch metrics, Logs, agent, alarms, dashboards, SNS, CloudTrail, Managed Prometheus, Bedrock monitoring, EventBridge, Automation runbooks, AWS Health, DevOps Agent, Kiro |
| [01b - Performance Optimization](./notes/01b-performance-optimization.md) | Domain 1, Task 1.3: Compute Optimizer, EBS, S3, EFS, FSx, S3 Files, RDS Performance Insights and RDS Proxy, placement groups |
| [02 - Reliability and Business Continuity](./notes/02-reliability-business-continuity.md) | Domain 2: Auto Scaling, caching, database scaling, ELB and Route 53 health checks, Multi-AZ, AWS Backup, PITR, versioning, DR |
| [03 - Deployment, Provisioning, and Automation](./notes/03-deployment-automation.md) | Domain 3: AMIs and EC2 Image Builder, CloudFormation and CDK, deployment troubleshooting, RAM and StackSets, deployment strategies, Terraform and Git, Systems Manager, event-driven automation |
| [04 - Security and Compliance](./notes/04-security-compliance.md) | Domain 4: IAM, Access Analyzer and policy simulator, Organizations and Identity Center, Trusted Advisor, Config, data classification, KMS, ACM, secrets, security findings, Security Agent |
| [05 - Networking and Content Delivery](./notes/05-networking.md) | Domain 5: VPC, endpoints, network protection audit, network cost, Route 53 Resolver, routing policies, CloudFront, Global Accelerator, troubleshooting, network logs, CloudWatch network monitoring |
| [Fact sheet](./fact-sheet.md) | Exam logistics and high-yield facts per domain |
| [Strategy](./strategy.md) | Time allocation by weight and per-domain tactics |
| [Practice plan](./practice-plan.md) | Eight-week plan mapped to the domains |
| [Scenarios](./scenarios.md) | High-yield scenarios and distractors |

## Study Strategy

### Recommended Timeline: 8 Weeks

- **Weeks 1-2:** Domain 1 - monitoring, logging, remediation, then performance optimization.
- **Weeks 3-4:** Domain 2 - scaling, health checks, Multi-AZ, backup and DR.
- **Weeks 4-5:** Domain 3 - images, infrastructure as code, deployment strategies, Systems Manager.
- **Week 6:** Domain 4 - IAM troubleshooting, multi-account controls, compliance, encryption and findings.
- **Week 7:** Domain 5 - VPC, DNS, CloudFront and Global Accelerator, network troubleshooting.
- **Week 8:** Practice exams and review.

See [practice-plan.md](./practice-plan.md) for the day-by-day version.

## Exam Tips

### Question Strategy
1. **Read for the operational requirement** - fix, monitor, automate, recover, restrict.
2. **Look for keywords:**
   - "Least operational overhead" - managed services and automation
   - "Automatically" - EventBridge, Systems Manager Automation, Config remediation, Auto Scaling
   - "Least privilege" - IAM conditions, permission sets, Access Analyzer
   - "Without downtime" - Multi-AZ, rolling or blue/green deployments, Elastic Volumes
3. **Eliminate** manual, overbuilt or retired options (OpsWorks reached end of life in May 2024).

### Time Management
- 130 minutes for 65 questions = 2 minutes per question.
- Flag uncertain questions and return later; leave about 15 minutes for review.

### Common Pitfalls
- Expecting memory or disk space as standard EC2 metrics (they need the CloudWatch agent).
- Confusing security groups (stateful) with NACLs (stateless).
- Forgetting that PITR creates a new database instance or table.
- Not knowing CloudFormation failure states and how to recover from each.
- Studying SOA-C02 material with exam labs and a separate cost domain.

## Next Steps After Certification

- **[📖 AWS DevOps Engineer - Professional](https://aws.amazon.com/certification/certified-devops-engineer-professional/)** - Advanced automation and operations
- **[📖 AWS Solutions Architect - Professional](https://aws.amazon.com/certification/certified-solutions-architect-professional/)** - Complex architecture design
- **[📖 AWS Security - Specialty](https://aws.amazon.com/certification/certified-security-specialty/)** - Deep security focus
