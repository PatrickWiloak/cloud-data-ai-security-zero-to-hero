---
last-updated: 2026-10-22
applies-to: CompTIA Cloud+ CV0-004 exam objectives v2.0, checked 2026-10-22
difficulty: intermediate
---

# Domain 4: Security (19%)

This note covers objectives 4.1 to 4.6: vulnerability management, compliance and regulation, identity and access management, security best practices, security controls, and monitoring for common attacks.

**[📖 CompTIA Cloud+ CV0-004 Exam Objectives v2.0 (PDF)](https://comptiacdn.azureedge.net/webcontent/docs/default-source/exam-objectives/comptia-cloud-cv0-004-exam-objectives-%282-0%29.pdf)** - the official topic list this note follows.

Security is tied with Deployment as the second-largest domain. It is also the domain that bleeds into everything else: a troubleshooting question about a 403 error is really an IAM question, and a backup question about ransomware is really a security question. The exam is vendor neutral, so learn the concept first and the provider names second.

## 4.1 Explain vulnerability management concepts

Vulnerability management is a repeating cycle, not a one-off scan.

- **Scanning scope** - deciding what to scan: which accounts, networks, hosts, container images, code repositories and managed services. A scan that misses a forgotten subnet gives false comfort. Scope also has a legal side: scanning provider infrastructure you do not own may break the provider's terms, so check their penetration testing policy.
- **Identification** - running the scanners (authenticated host scanners, image scanners in the registry, dependency scanners in the pipeline, cloud configuration scanners) and collecting findings.
- **Assessment** - deciding which findings matter. Severity scores are a start, but context decides priority: is the system internet facing, is there a known exploit, does it hold sensitive data, is there a compensating control?
- **Remediation** - fixing the issue (patch, upgrade, configuration change) or, when a fix is not possible yet, mitigating it (block the port, add a WAF rule) and accepting the remaining risk formally. Then rescan to confirm.

- **Common Vulnerabilities and Exposures (CVE)** - the public catalogue of known vulnerabilities, each with an ID such as CVE-2021-44228 (Log4Shell). Scanners report findings by CVE ID.
- **Common Vulnerability Scoring System (CVSS)** - the 0 to 10 severity score attached to a CVE. 9.0 and above is critical.
- **Common Weakness Enumeration (CWE)** - the catalogue of weakness types (for example SQL injection, CWE-89) that cause vulnerabilities. CVE is a specific instance; CWE is the class.

**Exam trap:** A critical CVSS score on an isolated test box with no data can rank below a medium score on an internet-facing payment server. Assessment is about risk in context, not just the number.

## 4.2 Compare and contrast aspects of compliance and regulation

### Data concepts

- **Data sovereignty** - data is subject to the laws of the country where it is stored or processed. A government may be able to demand access to data held in its territory.
- **Data ownership** - who is accountable for a dataset and decides how it is used, classified and shared. Usually a business owner, not IT. In cloud, the customer owns its data; the provider is a processor.
- **Data locality (residency)** - where data physically sits. Regulations or contracts may require that data stays in a country or region, which you meet by choosing regions and restricting replication and backup copies.
- **Data classification** - labelling data by sensitivity (for example public, internal, confidential, restricted) so the right controls apply. Classification drives encryption, access and DLP rules.
- **Data retention** - how long data must be kept and when it must be deleted.
- **Litigation hold (legal hold)** - an instruction to preserve data relevant to a lawsuit or investigation, overriding normal deletion schedules. Object lock or legal hold features in cloud storage enforce it.
- **Contractual retention** - retention required by agreements with customers or partners.
- **Regulatory retention** - retention required by law or regulation, such as financial records rules.

**Exam trap:** Sovereignty is about **whose laws apply**; locality is about **where the bytes are**. A question about a foreign government's legal reach is sovereignty. A question about keeping data inside the EU is locality or residency.

### Industry standards

- **SOC 2 (System and Organization Controls 2)** - an independent auditor's report on a service organization's controls against the trust services criteria: security, availability, processing integrity, confidentiality and privacy. A Type I report covers design at a point in time; a Type II report covers how controls operated over a period, usually 6 to 12 months. Customers ask providers for SOC 2 Type II reports.
- **PCI DSS (Payment Card Industry Data Security Standard)** - required for anyone who stores, processes or transmits payment card data. Scope reduction (segmenting the cardholder data environment, or using a payment provider's hosted page so card numbers never touch your systems) is the main design lever.
- **ISO/IEC 27001** - the international standard for an information security management system (ISMS). Organizations are certified against it by an accredited body after an audit.
- **Cloud Security Alliance (CSA)** - a non-profit that publishes the Cloud Controls Matrix (CCM), the Consensus Assessments Initiative Questionnaire (CAIQ) and the STAR registry, where providers publish their security self-assessments and certifications.

**[📖 Cloud Security Alliance](https://cloudsecurityalliance.org/)** - home of the Cloud Controls Matrix and the STAR registry.

The exam may also mention regulations that are not on the objective list but appear in scenarios: GDPR for EU personal data, HIPAA for US health information, and FedRAMP for US federal cloud use. Match the framework to the data: card numbers mean PCI DSS, health records mean HIPAA, EU residents' personal data means GDPR.

## 4.3 Implement identity and access management

IAM answers three questions: who are you (authentication), what may you do (authorization), and what did you do (accounting). Together they are often called AAA.

### Secure access to the management environment

The management environment is the provider's control plane: creating, changing and deleting resources.

- **Programmatic access** - automation and code calling the provider's APIs.
  - **API** - direct HTTPS calls, signed with keys or tokens.
  - **SDK** - language libraries (Python, Java, .NET, Go) that wrap the API and handle signing and retries.
  - **CLI** - command-line tools such as the AWS CLI, Azure CLI and gcloud. (CompTIA's acronym list expands CLI as "Common Language Infrastructure", which is a quirk; in this context it means the command-line interface.)
- **Web portal** - the browser console. It should require MFA and, for admins, ideally single sign-on through the corporate identity provider.

Prefer short-lived credentials for programmatic access: roles assumed by workloads, workload identity federation for pipelines, and temporary tokens. Long-lived access keys in code are the classic leak.

### Secure access to cloud resources

This is access to the workloads themselves, the data plane.

- **API** - applications calling your services, protected with authentication tokens, API keys and gateways.
- **Secure Shell (SSH)** - encrypted remote shell for Linux, using key pairs rather than passwords.
- **Remote Desktop Protocol (RDP)** - graphical remote access to Windows on TCP 3389.
- **Bastion host (jump box)** - a hardened host in a public subnet that admins connect to first, then hop to private instances. It narrows the exposed surface to one well-monitored machine. Managed equivalents (Azure Bastion, AWS Systems Manager Session Manager, Google IAP TCP forwarding) remove the need to open SSH or RDP to the internet at all.

**Exam trap:** Opening SSH or RDP from 0.0.0.0/0 is always wrong. The right answer is a bastion or managed session service, with source IP restrictions.

### Authentication models

- **Local users** - accounts created directly in the cloud account or on the server. Simple but hard to manage at scale, and they are not removed when someone leaves the company unless a person remembers.
- **Federation** - trusting an external identity provider (IdP) so users sign in with their corporate identity. Joiners and leavers are handled once, centrally.
- **SAML (Security Assertion Markup Language)** - an XML-based federation standard. The IdP sends a signed assertion to the service provider. Common for enterprise single sign-on to consoles and SaaS.
- **Token-based** - after authentication the client gets a token (often a JSON Web Token) and presents it with each request. Tokens expire, which limits the damage if one leaks.
- **Directory-based** - authentication against a directory service such as Active Directory or LDAP. Microsoft Entra ID is the cloud directory behind Azure and Microsoft 365.
- **Multifactor authentication (MFA)** - two or more different factor types: something you know (password), something you have (authenticator app, hardware key) or something you are (biometric). Two passwords is not MFA. Phishing-resistant MFA uses hardware security keys or passkeys (FIDO2).
- **OpenID Connect (OIDC)** - an identity layer on top of OAuth 2.0 using JSON tokens. Common for modern web and mobile sign-in and for letting CI/CD pipelines obtain cloud credentials without stored secrets.

### Authorization models

- **Role-based access control (RBAC)** - permissions are attached to roles (for example "network admin" or "read-only auditor") and users or workloads take on roles. Scales well and maps to job functions.
- **Group-based access control** - permissions attached to groups and users added to groups. In practice groups are often mapped to roles.
- **OAuth 2.0** - a delegated authorization framework. A user lets an application act on their behalf with limited scopes ("read calendar") without giving the application their password. OAuth is authorization; OIDC adds authentication on top.
- **Discretionary access control (DAC)** - the owner of a resource decides who gets access, as with file permissions or sharing a document. Flexible but hard to govern.

Attribute-based access control (ABAC), which decides on tags and attributes such as department or environment, is not listed in v2.0 but appears in provider IAM through condition keys and resource tags.

### Accounting

- **Audit trail** - an immutable record of who did what, when, from where. Control-plane audit logs (AWS CloudTrail, Azure Activity Log, Google Cloud Audit Logs) are the cloud's audit trail. Protect them by sending them to a separate, locked-down account.

**Exam trap:** SAML versus OIDC versus OAuth. SAML is XML and enterprise SSO. OIDC is JSON tokens and modern sign-in. OAuth 2.0 alone is delegated authorization, not a login protocol.

## 4.4 Apply security best practices

- **Zero Trust** - never trust based on network location; verify every request using identity, device health and context, grant the least access needed, and assume breach. In practice: strong identity with MFA, micro-segmentation, encryption everywhere, continuous monitoring.
- **Benchmark** - a published, consensus secure-configuration baseline. **CIS Benchmarks** from the Center for Internet Security cover operating systems, Kubernetes and each major cloud provider. **Vendor-specific** benchmarks come from the provider, such as the AWS Foundational Security Best Practices standard or the Microsoft cloud security benchmark. Cloud security posture tools check accounts against these automatically.
- **Hardening** - reducing attack surface: remove unused software and accounts, close unused ports, disable default credentials, apply benchmark settings, and build from a hardened golden image.
- **Patching** - applying security fixes promptly. Covered in Operations; from a security view the point is speed for exploited vulnerabilities.
- **Encryption of data in transit** - TLS 1.2 or 1.3 for web and API traffic, IPsec for site-to-site VPNs, SSH for admin sessions.
- **Encryption of data at rest** - AES-256 for disks, databases, object storage and backups. Keys live in a key management service (AWS KMS, Azure Key Vault, Google Cloud KMS) or a hardware security module. Customer-managed keys give you control of rotation and revocation.
- **Secrets management** - store passwords, API keys and certificates in a secrets manager (AWS Secrets Manager, Azure Key Vault, Google Secret Manager, HashiCorp Vault), fetch them at runtime, rotate them automatically, and never commit them to source control.
- **API security** - authenticate every call, authorize per resource, validate input, rate limit, use TLS, and log access. An API gateway centralizes these controls. The OWASP API Security Top 10 lists common mistakes such as broken object-level authorization.
- **Principle of least privilege** - give each identity only the permissions it needs, for only as long as it needs them. Start with nothing and add; review and remove unused permissions.
- **Container security** - run containers as **unprivileged** (non-root) users; avoid **privileged** mode, which gives the container near-host-level access to the kernel and devices. Set file access permissions tightly inside the image, use read-only root file systems where possible, scan images for CVEs and use minimal base images.
- **Storage security** - for **object storage**, block public access at the account level, use bucket policies and encryption, enable versioning and object lock against deletion. For **file storage**, restrict network access to known subnets, use share and file permissions and encrypt.

**[📖 CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)** - free consensus hardening baselines for operating systems, Kubernetes and cloud providers.

**[📖 OWASP](https://owasp.org/)** - the Open Worldwide Application Security Project, home of the OWASP Top 10 and API Security Top 10.

**Exam trap:** "The container must run as root to bind port 80" is not a reason to use privileged mode. Map a high host port to the container, or grant only the specific capability needed.

## 4.5 Apply security controls in the cloud

- **Endpoint protection** - anti-malware and endpoint detection and response (EDR) agents on VMs and workstations. They catch malware and suspicious process behaviour that network controls cannot see.
- **Data loss prevention (DLP)** - tools that discover and classify sensitive data (card numbers, health records, personal data) and block or alert when it moves where it should not, such as to a public bucket or a personal email.
- **Intrusion detection system (IDS)** - watches traffic or host activity and alerts on attacks. Passive.
- **Intrusion prevention system (IPS)** - sits inline and blocks attacks as well as detecting them. Active, so a false positive can block legitimate traffic.
- **DDoS protection** - absorbs and filters floods of traffic. Providers include basic protection for free and sell advanced tiers (AWS Shield Advanced, Azure DDoS Protection, Google Cloud Armor) with application-layer mitigation and response support.
- **IAM policies** - JSON (or similar) documents that grant or deny actions on resources. An explicit deny overrides any allow.
- **Firewall** - filtering traffic by rules, in several forms:
  - **Network access control list (ACL)** - subnet-level, **stateless** rules evaluated in number order, with both allow and deny. Because it is stateless you must allow return traffic (often the ephemeral port range 1024-65535) explicitly.
  - **Network security group** - instance or interface level, **stateful** rules. Return traffic is allowed automatically. AWS calls these security groups (allow rules only); Azure network security groups support both allow and deny with priorities.
  - **Web application firewall (WAF)** - Layer 7 inspection of HTTP requests that blocks SQL injection, cross-site scripting, bad bots and abusive rates. It sits in front of a load balancer, application gateway, API gateway or CDN.

| Control | Layer | State | Typical use |
|---|---|---|---|
| Network ACL | Subnet | Stateless | Coarse allow and deny for a whole subnet, block a known bad range |
| Network security group | Instance or NIC | Stateful | Allow only required ports between tiers |
| WAF | Application (Layer 7) | Inspects requests | Block injection and bot attacks on web apps |
| IPS | Network or host | Inline | Block known attack signatures |

**Exam trap:** "Return traffic is being dropped although the inbound rule allows the request" is a stateless network ACL missing an outbound rule for ephemeral ports. Security groups would not cause this.

## 4.6 Monitor suspicious activities to identify common attacks

### Detection techniques

- **Event monitoring** - collecting and correlating security events (logins, IAM changes, API calls, firewall denies) in a SIEM or the provider's threat detection service (Amazon GuardDuty, Microsoft Defender for Cloud and Sentinel, Google Security Command Center).
- **Deviation from the baseline** - spotting activity outside normal patterns: API calls from a new country, a spike in outbound data, an admin logging in at 03:00, a sudden surge of CPU on idle machines.
- **Unnecessary open ports** - any listening port that is not needed is attack surface. Regular port scans and configuration checks find SSH, RDP, database ports or management interfaces exposed by mistake.

### Attack types

- **Vulnerability exploitation through human error** - misconfigurations such as a public storage bucket, an over-permissive security group or a disabled log. Most cloud breaches start here.
- **Vulnerability exploitation through outdated software** - attackers use known CVEs in unpatched systems. Signs include unusual processes and outbound connections from a server running an old version.
- **Social engineering: phishing** - tricking users into giving up credentials or running malware, often through fake login pages. Signs include logins from unusual locations right after a phishing campaign. Phishing-resistant MFA is the strongest defence.
- **Malware: ransomware** - encrypts data and demands payment, and increasingly steals data first. Signs include mass file changes, deletion of snapshots and backups, and new encryption keys. Defences are immutable, off-site backups and least privilege on backup deletion.
- **DDoS** - floods of traffic that exhaust bandwidth, connections or application resources. Signs are sudden traffic spikes from many sources and rising error rates.
- **Cryptojacking** - attackers run cryptocurrency miners on your compute, often after stealing keys. Signs are sustained high CPU or GPU on instances that should be idle, unexpected instances in unused regions, and a surprise bill.
- **Zombie instances** - forgotten, unmanaged resources that keep running unpatched and unmonitored. They are an easy foothold. Inventory, tagging and decommissioning fix them.
- **Metadata service abuse** - every cloud VM can query a local instance metadata service (169.254.169.254) for information including temporary role credentials. A server-side request forgery (SSRF) flaw in a web app can trick the server into fetching those credentials for the attacker. Defences are enforcing the session-token version of the metadata service (IMDSv2 on AWS), least-privilege instance roles and fixing SSRF.

**Exam trap:** A large unexpected bill plus high CPU on unknown instances in a region you never use is cryptojacking after credential compromise. The response is to revoke the leaked credentials first, then terminate the instances and investigate.

---

## Key takeaways

1. Vulnerability management cycles through scope, identify, assess, remediate. CVE is the ID, CVSS the score, context the priority.
2. Sovereignty is whose laws; locality is where the data sits. Litigation hold overrides deletion.
3. SOC 2 is an audit report, PCI DSS is for card data, ISO 27001 is an ISMS certification, CSA publishes the CCM and STAR.
4. SAML is XML SSO, OIDC is JSON identity, OAuth 2.0 is delegated authorization.
5. Bastion or managed session access, never SSH or RDP open to the internet.
6. Least privilege, secrets in a vault, unprivileged containers, encrypted everything.
7. Network ACLs are stateless and subnet level; security groups are stateful and instance level; WAF inspects HTTP.
8. Know the signs: CPU spike on idle boxes (cryptojacking), mass file changes (ransomware), credential calls to 169.254.169.254 (metadata abuse).
