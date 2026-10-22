---
last-updated: 2026-10-22
applies-to: SOA-C03 exam guide v1.1
---

# Domain 4: Security and Compliance

Domain 4 carries **16%** of the scored content, the smallest weight on the exam. **Task 4.1** is implementing and managing security and compliance tools and policies: IAM, access troubleshooting, multi-account controls, Trusted Advisor, and continuous compliance. **Task 4.2** is protecting data and infrastructure: classification, encryption at rest and in transit, secrets, and acting on security findings.

The exam guide is clear that **defining** security, compliance and governance requirements (and ransomware defense strategy) is out of scope. Your job as a CloudOps engineer is to **implement and operate** controls that someone else has decided on, and to troubleshoot them when they block legitimate work. Network protection services (WAF, Shield, Network Firewall, DNS Firewall) are audited in Domain 5, Task 5.1.3, in [note 05](./05-networking.md#513-audit-network-protection-services-in-a-single-account).

---

## Task 4.1 - Implement and manage security and compliance tools and policies

### 4.1.1 Implement IAM features

**Identities.** Prefer **roles** with temporary credentials over IAM users with long-term keys. Humans should sign in through **IAM Identity Center** or another identity provider (federation); workloads use instance profiles, Lambda execution roles, ECS task roles and EKS pod identities. The **root user** should have MFA, no access keys, and be used only for the few tasks that require it.

**Password policies** set length, complexity, rotation and reuse rules for IAM users' console passwords (account-wide). **MFA** can be required in policies with the condition key `aws:MultiFactorAuthPresent`, for example denying sensitive actions unless the session used MFA.

**Roles and federation.** A role has a **trust policy** (who may assume it - an AWS service, another account, a SAML or OIDC identity provider) and **permissions policies** (what it can do). Cross-account access is a role in the target account whose trust policy names the source account, plus permission in the source account to call `sts:AssumeRole`. Add an **external ID** condition when a third party assumes the role. Federation types: **SAML 2.0** for enterprise directories, **OIDC** for web identity and CI systems such as GitHub Actions.

**Policy types and evaluation.**

| Policy type | Attached to | Effect |
|---|---|---|
| Identity-based | User, group, role | Grants permissions |
| Resource-based | S3 bucket, KMS key, SQS queue, SNS topic, Lambda function and more | Grants access to principals, including other accounts |
| Permissions boundary | User or role | Caps the maximum an identity policy can grant |
| Service control policy (SCP) | Organization root, OU, account | Caps what principals in member accounts can do |
| Resource control policy (RCP) | Organization root, OU, account | Caps what can be done to resources in member accounts |
| Session policy | Passed when assuming a role | Caps that session |

Evaluation in one account: everything starts **implicitly denied**; an **explicit deny** anywhere wins; otherwise an **allow** is needed and it must survive every applicable cap (SCP, RCP, boundary, session policy). For cross-account access, both sides must allow: the identity policy in the caller's account and the resource policy (or role trust) in the target account.

**Policy conditions** make policies precise: `aws:SourceIp`, `aws:SourceVpce` and `aws:SourceVpc` (restrict to a network path), `aws:RequestedRegion`, `aws:PrincipalOrgID` (allow only principals in your organization), `aws:SecureTransport` (require TLS), `aws:PrincipalTag` and `aws:ResourceTag` (attribute-based access control, ABAC), and `aws:MultiFactorAuthPresent`.

**[📖 Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)** - roles, MFA, least privilege
**[📖 Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)** - how allow and deny combine
**[📖 AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)** - condition keys
**[📖 Set an account password policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)** - password rules
**[📖 Identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html)** - SAML and OIDC

### 4.1.2 Troubleshoot and audit access (CloudTrail, IAM Access Analyzer, IAM policy simulator)

When someone reports "Access Denied", work through these tools in order.

1. **The error message.** Many services now say which policy type denied the request (for example "with an explicit deny in a service control policy"). Some return an **encoded authorization message**; decode it with `aws sts decode-authorization-message` (the caller needs `sts:DecodeAuthorizationMessage`) to see the action, resource and conditions evaluated.
2. **CloudTrail.** Find the event with `errorCode` `AccessDenied` or `UnauthorizedOperation`: it shows the exact principal (often a role session, not the person you expected), action, resource, source IP and Region. CloudTrail is also the audit answer for "who changed this policy and when".
3. **IAM policy simulator.** Test whether a given user, group or role would be allowed a specific action on a specific resource, with chosen context keys, without making the real call. It evaluates identity policies, permissions boundaries, and (for principals in an organization) SCPs, and it can include a resource policy you paste in. Use it to prove a fix before applying it.
4. **IAM Access Analyzer**, which has several features:
   - **External access findings** - resources (S3 buckets, IAM roles, KMS keys, Lambda functions, SQS queues, Secrets Manager secrets and more) shared with principals **outside your zone of trust** (the account or the organization).
   - **Internal access findings** - which principals inside your organization can reach critical resources.
   - **Unused access findings** - unused roles, unused access keys and passwords, and unused permissions, to drive least privilege.
   - **Policy validation** - over a hundred checks for errors, security warnings and best-practice suggestions as you write a policy; **custom policy checks** can block policies that grant new access or specific actions in a pipeline.
   - **Policy generation** - build a least-privilege policy from the role's actual CloudTrail activity.
5. **Last accessed information** (access advisor) shows when each service was last used by a principal, which supports removing unused permissions.

**[📖 Troubleshoot access denied error messages](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html)** - reading the error
**[📖 Testing IAM policies with the policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html)** - simulator usage and limits
**[📖 Using IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)** - external, internal and unused access; validation
**[📖 decode-authorization-message](https://docs.aws.amazon.com/STS/latest/APIReference/API_DecodeAuthorizationMessage.html)** - decoding encoded errors

### 4.1.3 Implement multi-account strategies (Organizations, SCPs, IAM Identity Center)

**AWS Organizations** groups accounts under a **management account** in a tree of **organizational units (OUs)**. It enables consolidated billing, policy types (SCPs, RCPs, tag policies, backup policies, and others), and organization-wide integration for services such as CloudTrail, Config, GuardDuty and Security Hub, usually through a **delegated administrator** member account so that day-to-day security work does not happen in the management account.

**Service control policies** set the **maximum** permissions for IAM users and roles in member accounts:

- They **never grant** permissions; an action still needs an identity or resource policy allow.
- They **do not affect the management account**, and they do not restrict service-linked roles.
- With the default `FullAWSAccess` policy attached, you write **deny list** SCPs (deny specific actions). If you remove `FullAWSAccess`, you must explicitly allow everything that should work (allow list).
- Inheritance flows down the tree: an action must be allowed at every level from root to account, and a deny at any level applies.

Common SCPs: deny actions outside approved Regions (`aws:RequestedRegion`, exempting global services), deny `cloudtrail:StopLogging`/`DeleteTrail`, deny leaving the organization, deny disabling GuardDuty or Config, deny root user actions in member accounts.

**IAM Identity Center** is the recommended way to give people access to many accounts. Connect an identity source (the built-in directory, Active Directory, or an external IdP such as Okta or Microsoft Entra ID via SAML and SCIM provisioning). Define **permission sets** (collections of policies) and **assign** a user or group plus a permission set to one or more accounts; Identity Center creates the matching role in each account. Users sign in once to the access portal and choose an account and role, and the CLI uses `aws configure sso` for short-lived credentials. Troubleshooting: a user who cannot see an account has no assignment for it; a user who sees it but gets denied has a permission set (or an SCP) that does not allow the action; changes to a permission set must be **provisioned** to the accounts.

**AWS Control Tower** sets up and governs a multi-account landing zone on top of Organizations, with an account factory and **controls** (preventive ones implemented as SCPs or RCPs, detective ones as Config rules, proactive ones as CloudFormation hooks), including a Region deny control.

**[📖 Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)** - effects, inheritance and examples
**[📖 Resource control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html)** - resource-side guardrails
**[📖 What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)** - identity sources, permission sets, assignments
**[📖 What is AWS Control Tower?](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)** - landing zones and controls

### 4.1.4 Remediate based on AWS Trusted Advisor security checks

**Trusted Advisor** inspects your account and flags issues across cost optimization, performance, security, fault tolerance, service limits and operational excellence. On the **Basic** support plan you see all **service limits** checks and a selected set of **security** and **fault tolerance** checks (security checks must be refreshed manually); the full set of checks and the API are available on higher support plans. Results can be sent to EventBridge (and so to SNS or automation), and an organizational view aggregates them across accounts.

Security checks the exam expects you to act on, and the operational fix:

| Check | Remediation |
|---|---|
| Security groups with unrestricted access (0.0.0.0/0) to specific ports such as 22 or 3389 | Restrict sources; use Session Manager instead of SSH and RDP |
| Amazon S3 bucket permissions (open access) | Turn on **S3 Block Public Access** at account and bucket level; fix bucket policies and ACLs |
| MFA on root account | Enable MFA on the root user |
| IAM use / IAM password policy | Create admin roles or Identity Center access; set a password policy |
| Exposed access keys | Deactivate and rotate the key immediately; investigate usage in CloudTrail |
| AWS CloudTrail logging | Create a multi-Region trail (or organization trail) |
| EBS or RDS snapshots marked public | Make them private |

Automate where possible: a Trusted Advisor or Config finding in EventBridge can invoke an Automation runbook that closes the security group rule or blocks public access.

**[📖 AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)** - plans, categories and access
**[📖 Trusted Advisor check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html)** - every check
**[📖 Monitoring Trusted Advisor results with EventBridge](https://docs.aws.amazon.com/awssupport/latest/user/cloudwatch-events-ta.html)** - automating responses

### 4.1.5 Enforce compliance and continuous monitoring (Regions, services, Config conformance packs)

**Region and service selection.** Data residency and attack-surface rules usually translate to: deny unapproved Regions with an SCP on `aws:RequestedRegion` (or the Control Tower Region deny control); disable Regions you do not use (opt-in Regions are disabled by default); restrict which services can be used with an SCP allow list. Remember global services (IAM, Organizations, Route 53, CloudFront, Support) are called through us-east-1 endpoints, so Region-deny SCPs must exempt them.

**AWS Config** records resource configurations and their history and evaluates them against **rules**:

- **Managed rules** such as `restricted-ssh`, `s3-bucket-public-read-prohibited`, `encrypted-volumes`, `rds-storage-encrypted`, `cloudtrail-enabled`, `required-tags`.
- **Custom rules** written in Lambda or in **Guard** (policy-as-code DSL).
- Rules run on **configuration change** or **periodically**, and resources are `COMPLIANT` or `NON_COMPLIANT`.
- **Remediation** attaches an Automation runbook to a rule, manual or **automatic**, with retries.
- **Aggregators** collect compliance data from many accounts and Regions into one view.

A **conformance pack** is a collection of Config rules and remediation actions deployed as one unit, from a YAML template. AWS provides sample packs mapped to frameworks (for example operational best practices for CIS, NIST, PCI DSS, HIPAA). Deploy them to every account with **organization conformance packs** from the management or delegated administrator account. A pack gives one compliance score you can track over time.

Config needs a **configuration recorder** (all or selected resource types) and a **delivery channel** (S3, optionally SNS). If rules show no results, check that the recorder is on and records the resource type.

**[📖 What is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)** - recorder, rules, history
**[📖 Conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html)** - templates and organization deployment
**[📖 Remediating noncompliant resources](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html)** - automatic remediation with Automation
**[📖 SCP syntax and condition examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html)** - includes a deny-outside-approved-Regions example

---

## Task 4.2 - Implement strategies to protect data and infrastructure

### 4.2.1 Implement and enforce a data classification scheme

A classification scheme labels data by sensitivity (for example public, internal, confidential, restricted) so that the right controls apply automatically. In AWS that usually means:

- **Tag** resources (and S3 objects where useful) with the classification, for example `DataClassification=confidential`.
- **Enforce tagging** with **tag policies** (standardize keys and allowed values across the organization), the Config `required-tags` rule, and SCPs or IAM conditions that deny creating resources without the tag (`aws:RequestTag`, `aws:TagKeys`).
- **Drive controls from the tag**: ABAC policies that only let principals with a matching `aws:PrincipalTag` reach resources with that `aws:ResourceTag`; AWS Backup plans selected by tag; Config rules scoped to tagged resources.
- **Discover** sensitive data you did not label: **Amazon Macie** uses managed and custom data identifiers to find PII, financial data and credentials in S3, reports sensitive data findings and bucket-level security posture (public, unencrypted, shared), and sends findings to Security Hub and EventBridge.

The exam angle: classification is operational when it is **enforced and audited automatically**, not when it is a spreadsheet.

**[📖 Data classification whitepaper](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification.html)** - AWS guidance on classification schemes
**[📖 Tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html)** - standardizing tags
**[📖 What is Amazon Macie?](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)** - sensitive data discovery
**[📖 ABAC for AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html)** - tag-based authorization

### 4.2.2 Implement encryption at rest (AWS KMS)

**Key types.** **AWS owned keys** (used invisibly by services), **AWS managed keys** (`aws/s3`, `aws/ebs`; visible but you cannot change their policies; rotated yearly), and **customer managed keys** (you control the key policy, grants, rotation, enable/disable and deletion). Choose customer managed keys when you need cross-account use, custom rotation, separation of duties or the ability to disable access.

**Access control.** Every KMS key has a **key policy**; it is the primary control. IAM policies only work for a key if the key policy allows the account to delegate to IAM (the default key policy does). **Grants** give temporary, narrowly scoped use of a key to a principal (services such as EBS use them). Deleting a key has a mandatory **waiting period of 7 to 30 days**; disable it first if you are unsure.

**Rotation.** Automatic rotation for symmetric customer managed keys is optional and the period is configurable (the default is one year); you can also rotate on demand. Old key material is kept, so existing data still decrypts.

**Envelope encryption.** Services encrypt data with a data key and encrypt the data key with your KMS key, so large data never travels to KMS.

**Operational patterns:**

- **EBS encryption by default** - an account and Region setting so every new volume and snapshot copy is encrypted.
- **Encrypting an existing unencrypted EBS volume or RDS instance** - you cannot flip it in place. Snapshot it, **copy the snapshot with encryption enabled**, then create a volume or restore a DB instance from the encrypted copy.
- **Cross-Region** - a KMS key is Regional; copying an encrypted snapshot to another Region re-encrypts with a key in that Region. **Multi-Region keys** share key material across Regions for applications that need it.
- **S3** - SSE-S3 (default for all new objects), **SSE-KMS** (audit key use in CloudTrail; use **S3 Bucket Keys** to cut KMS request volume and cost), DSSE-KMS, and SSE-C.
- **Throttling** - heavy SSE-KMS use can hit KMS request quotas; Bucket Keys help.

**[📖 AWS KMS concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)** - key types, key material, envelope encryption
**[📖 Key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html)** - default policy and delegation
**[📖 Rotating AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)** - automatic and on-demand rotation
**[📖 Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html)** - encryption by default and encrypting existing data
**[📖 Protecting data with server-side encryption in S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html)** - SSE options and Bucket Keys

### 4.2.3 Implement encryption in transit (AWS Certificate Manager)

**ACM** issues and manages TLS certificates for AWS integrated services: **Elastic Load Balancing, CloudFront, API Gateway, App Runner** and others.

- **Public certificates** from ACM are free and **renew automatically**, as long as validation still works. **DNS validation** (a CNAME record in your zone) is preferred because renewal is then fully automatic; **email validation** needs a human to click each time.
- **Imported certificates** (from a third-party CA) are **not renewed** by ACM. You must import the new one before expiry. ACM publishes the `DaysToExpiry` metric and sends expiry events through EventBridge and AWS Health, so you can alarm on it; the AWS Config managed rule `acm-certificate-expiration-check` also catches them.
- **CloudFront** requires the certificate in **us-east-1**; for a load balancer it must be in the load balancer's Region.
- **AWS Private CA** issues private certificates for internal services.
- Enforce TLS: HTTPS listeners with a modern **security policy** on ALB/NLB, HTTP-to-HTTPS redirects, CloudFront viewer protocol policy "redirect HTTP to HTTPS", and bucket policies denying requests where `aws:SecureTransport` is false. RDS and other databases support TLS connections, which you can require through parameters.

**[📖 What is AWS Certificate Manager?](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html)** - public and private certificates
**[📖 Managed certificate renewal in ACM](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html)** - what renews automatically
**[📖 Requirements for using SSL/TLS certificates with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.html)** - us-east-1 rule

### 4.2.4 Securely store secrets

| | **AWS Secrets Manager** | **Systems Manager Parameter Store** |
|---|---|---|
| Purpose | Secrets: database credentials, API keys | Configuration values and secrets (`SecureString`) |
| Rotation | **Built-in automatic rotation** with Lambda; managed rotation for RDS, Aurora, Redshift, DocumentDB | No built-in rotation |
| Cross-Region | **Replicates** secrets to other Regions | No |
| Cost | Per secret per month plus API calls | Standard tier free; advanced tier paid |
| Cross-account | Resource policy on the secret | Advanced tier parameters can be shared via RAM |

Rule of thumb: credentials that must **rotate** belong in **Secrets Manager**; plain configuration (and non-rotating secrets on a budget) can live in Parameter Store as `SecureString` encrypted with KMS. Both integrate with CloudFormation dynamic references (`{{resolve:secretsmanager:...}}`, `{{resolve:ssm-secure:...}}`), ECS task definitions and Lambda. RDS can also **manage the master user password in Secrets Manager** for you.

Never put secrets in user data, environment variables in plain text, AMIs or Git. If a key leaks, deactivate and rotate it first, then investigate.

**[📖 What is AWS Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)** - storage, rotation, replication
**[📖 Rotate Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)** - managed and Lambda rotation
**[📖 Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)** - tiers and SecureString

### 4.2.5 Implement reports and remediate findings (Security Hub, GuardDuty, Config, Inspector, AWS Security Agent)

| Service | What it finds |
|---|---|
| **Amazon GuardDuty** | Threats from analysis of CloudTrail management and data events, VPC Flow Logs and DNS logs, with optional protection plans (S3, EKS, runtime monitoring, malware protection, RDS login activity, Lambda). Examples: compromised instance talking to a known command-and-control IP, credentials used from an unusual location, crypto mining |
| **Amazon Inspector** | Software vulnerabilities (CVEs) and unintended network exposure in **EC2 instances, ECR container images and Lambda functions**, with a risk-adjusted score; rescans automatically when new CVEs are published |
| **AWS Config** | Configuration non-compliance against rules and conformance packs |
| **Amazon Macie** | Sensitive data and S3 bucket posture |
| **AWS Security Hub** | **Aggregates** findings from the services above and partners in a standard format, runs **security standards** checks (AWS Foundational Security Best Practices, CIS, PCI DSS, NIST), and gives a cross-account, cross-Region view through a delegated administrator |
| **AWS Security Agent** | AI-driven application security across the development lifecycle (see below) |

**Remediation flow.** Findings from all of these reach **EventBridge**. Rules route them to SNS (notify), Lambda or Systems Manager Automation (fix: isolate an instance by swapping its security group, disable an access key, block public access), or to a ticketing system. Security Hub **automation rules** can update or suppress findings as they arrive, and **custom actions** let an analyst send a chosen finding to EventBridge for a one-click response. Typical incident steps for a compromised instance: isolate it with a restrictive security group, snapshot its volumes for forensics, detach it from the ASG, then replace it from a clean image.

**AWS Security Agent** (in scope from guide v1.1; AWS documentation now describes it as part of AWS Continuum) is a frontier AI agent that secures applications throughout development. Security teams define organizational requirements once (approved authorization libraries, logging standards, data access policies). The agent then performs **design security reviews** of architecture documents, **code security reviews** of repositories and pull requests (posting findings as comments and proposing fixes as pull requests), **threat modeling** (a system overview with threats classified by STRIDE category), and **on-demand penetration testing** against verified target domains, executing multi-step attack scenarios to discover and validate vulnerabilities and documenting reproducible attack paths. For the exam, place it next to Inspector: **Inspector scans deployed resources for known CVEs and exposure; Security Agent tests and reviews your application itself for exploitable flaws**, and both produce findings you must triage and remediate.

**[📖 What is Amazon GuardDuty?](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)** - data sources and protection plans
**[📖 What is Amazon Inspector?](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)** - EC2, ECR and Lambda scanning
**[📖 What is AWS Security Hub?](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)** - aggregation and standards
**[📖 What is AWS Security Agent?](https://docs.aws.amazon.com/securityagent/latest/userguide/what-is.html)** - reviews, threat modeling, penetration testing

---

## Exam traps

- **SCPs never grant** and **do not apply to the management account**.
- **Explicit deny wins** over any allow, wherever it is.
- **Policy simulator** to test a principal's access; **Access Analyzer** to find external, internal and unused access and to validate policies; **CloudTrail** to see what actually happened.
- **Identity Center**: no account visible means no assignment; visible but denied means the permission set or an SCP.
- **Trusted Advisor on Basic support** gives only service limits plus selected security and fault tolerance checks.
- **Encrypt an existing EBS volume or RDS instance** via an encrypted snapshot copy.
- **Imported ACM certificates do not auto-renew**; CloudFront certificates must be in **us-east-1**.
- **Rotation needed: Secrets Manager.** Plain config: Parameter Store.
- **Security Hub aggregates; GuardDuty detects threats; Inspector finds CVEs; Macie finds sensitive data; Config checks configuration; Security Agent reviews and pen-tests the application.**
- Network protection auditing (WAF, Shield, Network Firewall, DNS Firewall) is in Domain 5.

## Key terms

- **Service control policy** - Organizations policy that caps permissions in member accounts; it never grants and skips the management account
- **Permissions boundary** - managed policy that sets the maximum permissions an identity policy can grant a user or role
- **IAM policy simulator** - tests whether a principal would be allowed an action on a resource without making the real call
- **IAM Access Analyzer** - finds external, internal and unused access, validates policies and generates least-privilege policies
- **Permission set** - IAM Identity Center template of policies that becomes a role in each account it is assigned to
- **Conformance pack** - collection of AWS Config rules and remediation actions deployed and scored as a single unit
- **Config remediation** - links a Config rule to a Systems Manager Automation runbook that fixes noncompliant resources
- **Tag policy** - Organizations policy that standardizes tag keys and allowed values across accounts
- **Amazon Macie** - discovers sensitive data such as PII in S3 and reports bucket security posture
- **Customer managed key** - KMS key whose policy, rotation and lifecycle you control; needed for cross-account sharing
- **KMS key policy** - resource policy on a KMS key and the primary control over who can use or manage it
- **Envelope encryption** - encrypting data with a data key and protecting that data key with a KMS key
- **ACM DNS validation** - proves domain ownership with a CNAME record so ACM can renew the certificate automatically
- **Secrets Manager rotation** - built-in scheduled rotation of secrets such as database credentials using Lambda or managed rotation
- **AWS Security Agent** - AI agent that performs design and code security reviews, threat modeling and on-demand penetration testing

## Vendor documentation

**[📖 SOA-C03 Domain 4 in the exam guide](https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/sysops-administrator-associate-03-domain4.html)** - official task statements
**[📖 IAM user guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)** - identities and policies
**[📖 AWS Organizations user guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)** - accounts, OUs and policies
