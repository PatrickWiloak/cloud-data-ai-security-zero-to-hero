---
last-updated: 2026-10-22
---

# AWS CloudOps Engineer Associate (SOA-C03) Study Plan

## 8-Week Study Schedule

The weeks follow the five exam domains (22 / 22 / 22 / 16 / 18%). Domain 1 gets two weeks because it has three tasks, including performance optimization. Each day assumes 2-3 hours; do the hands-on items in a sandbox account and clean up afterwards.

| Week | Domain and tasks | Notes |
|---|---|---|
| 1 | Domain 1, Tasks 1.1-1.2: monitoring, logging, remediation | [01](./notes/01-monitoring-logging.md) |
| 2 | Domain 1, Task 1.3: performance optimization | [01b](./notes/01b-performance-optimization.md) |
| 3 | Domain 2: scalability, high availability | [02](./notes/02-reliability-business-continuity.md) |
| 4 | Domain 2: backup, restore, DR; Domain 3 begins | [02](./notes/02-reliability-business-continuity.md), [03](./notes/03-deployment-automation.md) |
| 5 | Domain 3: provisioning and automation | [03](./notes/03-deployment-automation.md) |
| 6 | Domain 4: security and compliance | [04](./notes/04-security-compliance.md) |
| 7 | Domain 5: networking and content delivery | [05](./notes/05-networking.md) |
| 8 | Practice exams and review | All notes, [scenarios](./scenarios.md) |

### Week 1: Domain 1 - Monitoring, Logging, Analysis, and Remediation (Tasks 1.1-1.2)

#### Day 1-2: Metrics, logs and the CloudWatch agent (1.1.1, 1.1.2)
- [ ] Read [notes/01-monitoring-logging.md](./notes/01-monitoring-logging.md), Task 1.1.1 and 1.1.2
- [ ] Hands-on: install the CloudWatch agent on an EC2 instance with the configuration stored in Parameter Store; publish memory and disk metrics
- [ ] Hands-on: create a metric filter on application logs and run a Logs Insights query
- [ ] Hands-on: create a multi-Region trail with data events for one S3 bucket and integrity validation
- [ ] Read: Lambda and Bedrock metrics; Amazon Managed Service for Prometheus basics

#### Day 3-4: Alarms, dashboards, SNS (1.1.3-1.1.5)
- [ ] Hands-on: metric alarm with M-of-N datapoints and missing-data treatment; composite alarm over two children
- [ ] Hands-on: EC2 recover action on `StatusCheckFailed_System`
- [ ] Hands-on: dashboard with widgets from two Regions; read about cross-account observability
- [ ] Hands-on: SNS topic encrypted with a customer managed key that a CloudWatch alarm can publish to

#### Day 5-6: EventBridge and Automation (1.2.1-1.2.3)
- [ ] Hands-on: EventBridge rule on EC2 state change with an input transformer to SNS
- [ ] Hands-on: EventBridge rule on an alarm state change that starts an Automation runbook
- [ ] Hands-on: write a custom runbook with `aws:executeScript` and an assume role; run it by tag with rate control
- [ ] Read: AWS Health events in EventBridge; AWS DevOps Agent and Kiro overviews

#### Day 7: Review
- [ ] Domain 1 practice questions (Tasks 1.1-1.2); revisit the exam traps in note 01

### Week 2: Domain 1 - Performance Optimization (Task 1.3)

#### Day 8-9: Compute and EBS (1.3.1, 1.3.2, 1.3.6)
- [ ] Read [notes/01b-performance-optimization.md](./notes/01b-performance-optimization.md)
- [ ] Hands-on: enable Compute Optimizer and review findings
- [ ] Hands-on: change a gp2 volume to gp3 with Elastic Volumes; watch `VolumeQueueLength` under a `fio` load
- [ ] Study: placement group types, enhanced networking, instance EBS limits

#### Day 10-11: S3 and shared storage (1.3.3, 1.3.4)
- [ ] Hands-on: multipart upload with the CLI; enable Transfer Acceleration and test the endpoint
- [ ] Hands-on: S3 Lifecycle rule including abort incomplete multipart uploads
- [ ] Hands-on: EFS with Elastic throughput and a lifecycle policy to IA
- [ ] Read: FSx options and Amazon S3 Files

#### Day 12-13: Databases (1.3.5)
- [ ] Hands-on: RDS instance with Performance Insights (Database Insights) and Enhanced Monitoring; review proactive recommendations
- [ ] Hands-on: put RDS Proxy in front of the instance; change a static parameter and observe `pending-reboot`

#### Day 14: Review
- [ ] Domain 1 practice questions (Task 1.3)

### Week 3: Domain 2 - Scalability and High Availability (Tasks 2.1-2.2)

#### Day 15-16: Scaling (2.1.1)
- [ ] Read [notes/02-reliability-business-continuity.md](./notes/02-reliability-business-continuity.md), Task 2.1
- [ ] Hands-on: ASG with a launch template, target tracking and a scheduled action; lifecycle hook; instance refresh
- [ ] Hands-on: break the launch template and read the ASG activity history

#### Day 17-18: Caching and database scaling (2.1.2, 2.1.3)
- [ ] Hands-on: ElastiCache with lazy loading in a small app; CloudFront in front of an ALB
- [ ] Hands-on: RDS read replica; DynamoDB on-demand vs provisioned with auto scaling

#### Day 19-20: Health checks and Multi-AZ (2.2.1, 2.2.2)
- [ ] Hands-on: ALB health checks; break them with a security group and a bad path, then fix
- [ ] Hands-on: Route 53 failover with an endpoint check and a CloudWatch alarm-based check
- [ ] Hands-on: RDS Multi-AZ reboot with failover

#### Day 21: Review
- [ ] Domain 2 practice questions (Tasks 2.1-2.2)

### Week 4: Domain 2 - Backup and DR (Task 2.3), then Domain 3 begins

#### Day 22-23: Backup and restore (2.3.1-2.3.3)
- [ ] Hands-on: AWS Backup plan assigned by tag with a cross-Region copy; look at Vault Lock settings
- [ ] Hands-on: RDS point-in-time restore (note the new endpoint); DynamoDB PITR restore
- [ ] Hands-on: S3 versioning, delete markers and a noncurrent-version lifecycle rule

#### Day 24-25: DR procedures (2.3.4)
- [ ] Study: backup and restore, pilot light, warm standby, active/active
- [ ] Hands-on: promote a cross-Region read replica; read about Elastic Disaster Recovery drills

#### Day 26-27: Images (3.1.1)
- [ ] Read [notes/03-deployment-automation.md](./notes/03-deployment-automation.md), Task 3.1.1
- [ ] Hands-on: EC2 Image Builder pipeline with a test component and distribution to a second Region
- [ ] Hands-on: share an AMI encrypted with a customer managed key

#### Day 28: Review
- [ ] Domain 2 practice questions (Task 2.3)

### Week 5: Domain 3 - Deployment, Provisioning, and Automation

#### Day 29-30: CloudFormation and CDK (3.1.2, 3.1.3)
- [ ] Hands-on: stack with parameters, conditions and DeletionPolicy; update via change set; drift detection
- [ ] Hands-on: cause `ROLLBACK_COMPLETE` and `UPDATE_ROLLBACK_FAILED`, then recover
- [ ] Hands-on: `cdk bootstrap`, `cdk diff`, `cdk deploy` a small app
- [ ] Study: subnet sizing, `iam:PassRole` errors

#### Day 31-32: Sharing and strategies (3.1.4-3.1.6)
- [ ] Hands-on: share a subnet with RAM; deploy a StackSet to two Regions
- [ ] Hands-on: CodeDeploy or ECS blue/green with an alarm-based rollback
- [ ] Hands-on: Terraform with an S3 backend and state locking; plan and apply from Git

#### Day 33-34: Systems Manager and event-driven automation (3.2)
- [ ] Hands-on: State Manager association, Patch Manager baseline with a maintenance window, Session Manager with logging
- [ ] Hands-on: S3 Event Notification to Lambda (avoid a recursive loop); S3 to EventBridge
- [ ] Read: AWS DevOps Agent investigations

#### Day 35: Review
- [ ] Domain 3 practice questions

### Week 6: Domain 4 - Security and Compliance

#### Day 36-37: IAM and access troubleshooting (4.1.1, 4.1.2)
- [ ] Read [notes/04-security-compliance.md](./notes/04-security-compliance.md)
- [ ] Hands-on: cross-account role with external ID; MFA condition
- [ ] Hands-on: diagnose a denied call with CloudTrail, the policy simulator and `decode-authorization-message`
- [ ] Hands-on: IAM Access Analyzer external and unused access findings; policy validation

#### Day 38-39: Multi-account and compliance (4.1.3-4.1.5)
- [ ] Study: SCPs (deny list, Region restriction), IAM Identity Center permission sets
- [ ] Hands-on: Trusted Advisor security checks; fix one
- [ ] Hands-on: Config conformance pack with automatic remediation

#### Day 40-41: Data protection and findings (4.2)
- [ ] Hands-on: tag-based classification with a tag policy; Macie sensitive data job
- [ ] Hands-on: encrypt an unencrypted EBS volume via snapshot copy; ACM certificate with DNS validation
- [ ] Hands-on: Secrets Manager rotation for an RDS secret
- [ ] Hands-on: GuardDuty and Security Hub finding to EventBridge to SNS; read about AWS Security Agent

#### Day 42: Review
- [ ] Domain 4 practice questions

### Week 7: Domain 5 - Networking and Content Delivery

#### Day 43-44: VPC, endpoints and protection (5.1)
- [ ] Read [notes/05-networking.md](./notes/05-networking.md)
- [ ] Hands-on: public and private subnets, NAT gateway, egress-only IGW, gateway and interface endpoints
- [ ] Hands-on: DNS Firewall rule group, WAF web ACL in Count then Block, Network Firewall routing (read if no budget)
- [ ] Study: network cost levers (NAT processing, cross-AZ, CloudFront)

#### Day 45-46: DNS and content delivery (5.2)
- [ ] Hands-on: private hosted zone; Resolver query logging; Route 53 weighted and failover records
- [ ] Hands-on: CloudFront with OAC to S3; compare with Global Accelerator in the docs

#### Day 47-48: Troubleshooting (5.3)
- [ ] Hands-on: break routing and NACLs, then diagnose with Reachability Analyzer and flow logs
- [ ] Hands-on: read ALB access logs and WAF logs; fix a low CloudFront cache hit ratio with a cache policy
- [ ] Study: VPN and Direct Connect troubleshooting; Network Flow Monitor, Internet Monitor, Network Synthetic Monitor

#### Day 49: Review
- [ ] Domain 5 practice questions

### Week 8: Practice Exams and Final Review

#### Day 50-51: Full practice exams
- [ ] Official practice exam on AWS Skill Builder, timed (130 minutes)
- [ ] Map every wrong answer to a task number and re-read that section

#### Day 52-53: Weak-domain remediation
- [ ] Re-do the hands-on items for the two weakest domains
- [ ] Work through [scenarios.md](./scenarios.md)

#### Day 54-55: Final consolidation
- [ ] Read every note's exam traps and key terms
- [ ] Second timed practice exam; target 80%+

#### Day 56: Pre-exam
- [ ] Light review of the [fact sheet](./fact-sheet.md)
- [ ] Confirm logistics (ID, online proctoring setup)

## Practice Exam Targets

- [ ] End of week 3: 60%+ on Domain 1-2 question sets
- [ ] End of week 6: 70%+ on mixed sets
- [ ] Week 8: 80%+ on full timed practice exams

## Study Resources

- **[📖 SOA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/sysops-administrator-associate-03.html)** - task statements to check coverage against
- **[📖 Official exam page](https://aws.amazon.com/certification/certified-cloudops-engineer-associate/)** - registration
- **[📖 AWS Skill Builder](https://skillbuilder.aws/)** - official prep and practice exam
- **[📖 AWS Free Tier](https://aws.amazon.com/free/)** - hands-on practice

## Exam Day Checklist

- [ ] Log in 30 minutes early for online proctoring, or arrive early at the test center
- [ ] Bring the required identification
- [ ] Pace at about 2 minutes per question; flag and move on
- [ ] Read for "least operational overhead", "automatically" and "least privilege"
