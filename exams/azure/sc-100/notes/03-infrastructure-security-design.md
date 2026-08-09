---
last-updated: 2026-08-09
difficulty: advanced
reading-time: 14 min
---

# 03 - Infrastructure security design

**Domain 3: Design security solutions for infrastructure (20-25%)**

Posture management, workload protection, network segmentation, and hybrid and multicloud coverage.

---

## Defender for Cloud

Two halves, and the exam tests whether you know which one you need.

### CSPM: Cloud Security Posture Management

Configuration and posture. Largely free at the Foundational tier.

- **Secure score** - weighted measure of recommendation compliance
- **Recommendations** - misconfiguration findings mapped to MCSB controls
- **Regulatory compliance dashboard** - control state against assigned initiatives
- **Defender CSPM** (paid) adds attack path analysis, the cloud security explorer graph, agentless scanning, data-aware posture, and permissions management

### CWP: Cloud Workload Protection

Runtime threat detection, priced per resource per plan.

| Plan | Protects | Notable capability |
|---|---|---|
| Defender for Servers P1 | VMs, Arc servers | Defender for Endpoint integration, licensing included |
| Defender for Servers P2 | VMs, Arc servers | Adds vulnerability assessment, file integrity monitoring, JIT VM access, agentless scanning |
| Defender for Containers | AKS, Arc-enabled Kubernetes, ACR, other clouds | Registry scanning, runtime threat detection, Kubernetes hardening |
| Defender for Storage | Storage accounts | Malware scanning on upload, sensitive data threat detection |
| Defender for SQL | SQL on Azure, on VMs, Arc | Vulnerability assessment, anomalous access detection |
| Defender for App Service | Web apps | Detection of web shell and exploitation attempts |
| Defender for Key Vault | Key vaults | Unusual access detection |
| Defender for Resource Manager | Control plane | Suspicious management operations |
| Defender for APIs | API Management APIs | Discovery, posture, and runtime detection |
| Defender for AI Services | Azure AI workloads | Prompt injection and abuse detection signals |

**Rule of thumb**: if the requirement mentions misconfiguration, compliance, or hardening, it is CSPM. If it mentions detection, alerts, malware, or exploitation, it is a workload plan.

### Just-in-time VM access

Closes management ports and opens them on request for a limited window and source range. It is a Defender for Servers P2 feature and a common answer to "reduce exposure of RDP/SSH without a VPN project". Azure Bastion is the alternative when the requirement is "no public IP at all".

---

## Hybrid and multicloud

**Azure Arc** projects non-Azure resources into Azure Resource Manager so that Policy, Defender for Cloud, Monitor, and RBAC apply to them.

- Arc-enabled servers: on-premises and other-cloud VMs
- Arc-enabled Kubernetes: any CNCF-conformant cluster
- Arc-enabled data services and SQL Server

**Native cloud connectors** bring AWS accounts and GCP projects into Defender for Cloud agentlessly for CSPM, with the option of deploying workload protection through Arc.

Design consequence: whenever a scenario includes non-Azure infrastructure and a single-pane-of-glass requirement, Arc and the connectors are part of the answer.

---

## Network segmentation

### Topology

- **Hub-and-spoke** - shared services and inspection in the hub, workloads in spokes. The default answer.
- **Virtual WAN** - Microsoft-managed hub for large-scale branch and global connectivity. Choose when the scenario has many branches or regions and operational simplicity is prioritized.
- **Subscription and management group alignment** - compliance boundaries should coincide with subscription boundaries so policy, RBAC, and audit scope are clean.

### Controls

| Control | Layer | Use for |
|---|---|---|
| Network security group | 3-4 | Subnet and NIC allow/deny by IP, port, protocol, service tag |
| Application security group | 3-4 | Grouping NICs by role so rules reference roles, not IPs |
| Azure Firewall Standard | 3-4 plus FQDN | Centralized egress control, threat intelligence filtering |
| Azure Firewall Premium | 7 | TLS inspection, IDPS, URL filtering, web category filtering |
| Web Application Firewall | 7 | OWASP rule sets on Application Gateway or Front Door |
| DDoS Protection | 3-4 | Network and IP protection tiers with mitigation guarantees |
| Route tables with forced tunneling | 3 | Preventing direct internet egress from a subnet |

**Premium is the discriminator** for TLS inspection and IDPS. If either appears in the requirements, Standard is wrong.

### Private connectivity

| Option | What it does | Limitation |
|---|---|---|
| **Service endpoint** | Routes traffic to a PaaS service over the Microsoft backbone from a subnet | Resource keeps a public IP; does not extend to on-premises |
| **Private endpoint** | Gives the PaaS resource a private IP inside your VNet | Requires private DNS zone configuration |
| **Private Link service** | Exposes your own service privately to consumers | Requires a standard load balancer |

Private endpoint questions almost always include a DNS component. The pattern: a `privatelink.<service>.<suffix>` private DNS zone linked to the VNet, plus conditional forwarders from on-premises DNS so ExpressRoute or VPN clients resolve to the private IP rather than the public one.

Disable public network access on the resource when the requirement says "must not be reachable from the internet". A private endpoint alone does not remove the public endpoint.

---

## Endpoint and server hardening

- **Defender for Endpoint** for detection and response, deployed through Intune, Configuration Manager, or Arc
- **Intune compliance policies** feeding Conditional Access device controls
- **Azure Update Manager** for patch orchestration across Azure, Arc, and on-premises
- **Machine configuration** (formerly guest configuration) in Azure Policy for in-guest baseline auditing and remediation
- **Attack surface reduction rules**, application control, and credential guard as endpoint hardening measures

---

## OT and IoT

**Defender for IoT** covers OT networks through passive network sensors, discovering devices and detecting anomalous industrial protocol behavior without agents. Appears in manufacturing, utilities, and healthcare scenarios. The design point is that OT networks cannot usually take agents, so passive monitoring plus segmentation from IT is the answer.

---

## Key terms

- **CSPM** - Cloud Security Posture Management, the configuration and compliance half of Defender for Cloud
- **CWP** - Cloud Workload Protection, the runtime threat detection half, licensed per resource plan
- **Secure score** - Defender for Cloud's weighted measure of how many security recommendations are satisfied
- **Attack path analysis** - Defender CSPM feature that chains findings into exploitable routes to a critical asset
- **Just-in-time VM access** - Defender for Servers feature that keeps management ports closed and opens them on approved request for a limited time
- **Azure Arc** - service that projects non-Azure servers, Kubernetes clusters, and data services into Azure Resource Manager for governance
- **Service endpoint** - subnet configuration routing PaaS traffic over the Microsoft backbone while the resource retains a public IP
- **Private endpoint** - a network interface giving a PaaS resource a private IP inside a VNet, requiring matching private DNS
- **Application security group** - a logical grouping of NICs so NSG rules can reference workload roles instead of IP ranges
- **Azure Firewall Premium** - the tier adding TLS inspection, IDPS, URL filtering, and web categories
- **Forced tunneling** - route table configuration sending all outbound traffic through an inspection appliance rather than directly to the internet
- **Machine configuration** - Azure Policy capability auditing and remediating settings inside the guest operating system
- **Defender for IoT** - agentless passive monitoring of OT and IoT networks through network sensors

---

## Related

- [Notes 04: application and data security](./04-application-and-data-security.md)
- [Scenarios](../scenarios.md) - scenarios 4, 5, and 8 exercise this domain
- [Networking deep dives](../../../../resources/networking-deep-dives/)
- [Service comparison: networking](../../../../resources/service-comparison-networking.md)
- [AZ-700 Azure Network Engineer](../../az-700/)
