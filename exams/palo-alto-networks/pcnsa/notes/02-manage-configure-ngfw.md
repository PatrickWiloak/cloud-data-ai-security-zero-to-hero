---
last-updated: 2026-07-29
---

# PCNSA Domain 2 - Manage and Configure the NGFW

Day-to-day administration: configuration management, updates, administrators, high
availability, and logging.

## Configuration management

- **Candidate configuration** - your pending edits.
- **Running configuration** - what is being enforced now.
- **Commit** - activates the candidate. Partial commit lets you push only selected administrators' changes.
- **Commit lock and config lock** - prevent other administrators from committing or editing while you work.
- **Revert to running configuration** - discards candidate changes.
- **Configuration snapshot** - a saved named configuration, stored locally.
- **Export and import named configuration** - the backup and restore mechanism. Snapshots on the device do not survive device loss, so exported backups matter.
- **Audit log / config log** - records who changed what and when.

Validate before commit on a production firewall: validation catches errors without
applying them.

## Administrators and access

- **Role-based administration** - dynamic roles (superuser, device admin, read-only) or custom admin roles restricting access to specific tabs and functions.
- **Authentication profile** - how administrators authenticate: local, RADIUS, TACACS+, LDAP, SAML, or Kerberos.
- **Authentication sequence** - an ordered list of profiles tried in turn.
- **Management interface restriction** - permitted IP addresses for management access. An open management interface is a standard finding.
- **Service routes** - which interface the firewall uses for outbound management services such as updates and DNS. By default management traffic uses the management interface; service routes redirect it.

## Content and software updates

- **Dynamic updates** - the signature and category feeds:
  - **Antivirus** - daily.
  - **Applications and Threats** - weekly (App-ID and threat signatures together).
  - **WildFire** - as often as every minute with a subscription.
  - **URL filtering** - cloud-based lookups.
- **Update scheduling** - download and install can be separated, with a threshold delay so brand-new signatures are not applied instantly to a critical network.
- **PAN-OS upgrade path** - you must step through major versions in order rather than jumping. Check the release notes for required intermediate versions.
- **Content version requirement** - a minimum content version is often required before a PAN-OS upgrade.

Application and Threats updates can change App-ID behavior, which can change which rules
match. This is why a review period before installing is a real operational control.

## High availability

- **Active/passive HA** - one firewall processes traffic, the peer stands by synchronized. The most common deployment.
- **Active/active HA** - both process traffic; used for asymmetric routing environments, and more complex.
- **HA1 link** - control link, exchanging hellos, heartbeats, and configuration sync.
- **HA2 link** - data link, synchronizing sessions so failover does not drop established connections.
- **HA3 link** - packet forwarding link, active/active only.
- **Backup HA links** - avoid a single point of failure in the HA path itself.
- **Heartbeat polling and hello messages** - failure detection.
- **Link and path monitoring** - triggers failover when a monitored interface or destination becomes unreachable, catching failures the device itself would not notice.
- **Preemption** - whether the higher-priority device reclaims active status after recovering. Disabled by default in many designs to avoid a second disruption.
- **Split brain** - both peers believe they are active, usually caused by HA1 failure. Backup HA1 links prevent it.

## Logging and monitoring

**Log types**

- **Traffic** - session start and end. The default is end-of-session logging; log at session start only when troubleshooting, because it doubles volume.
- **Threat** - detections from security profiles.
- **URL filtering** - web category decisions.
- **WildFire submissions** - files sent for analysis and their verdicts.
- **Data filtering** - matches on sensitive data patterns.
- **System** - device events.
- **Configuration** - administrative changes.
- **Authentication** - user authentication events.

- **Log forwarding profile** - sends logs to Panorama, syslog, email, SNMP, or HTTP. Attached to security rules, so a rule without a log forwarding profile forwards nothing.
- **Log storage quotas** - allocate space per log type; when full, oldest entries are overwritten.
- **Panorama log collection** - centralizes logs for correlation and longer retention.

**Monitoring tools**

- **Application Command Center (ACC)** - interactive visibility into applications, users, threats, and URLs. The starting point for "what is happening on my network."
- **Session browser** - live sessions currently on the device.
- **Reports** - predefined and custom, scheduled or on demand.
- **Packet capture** - on-device capture across the receive, transmit, drop, and firewall stages.

## Certificates and decryption basics

- **Certificate management** - the firewall needs certificates for management access, GlobalProtect, and decryption.
- **Forward trust certificate** - presented to internal clients when decrypting outbound traffic to sites with valid certificates. Must be trusted by clients, usually by distributing the CA via group policy.
- **Forward untrust certificate** - presented when the destination's certificate is itself untrusted, so users still see a warning.
- **SSL Forward Proxy** - decrypts outbound traffic so Content-ID can inspect it.
- **SSL Inbound Inspection** - decrypts traffic to your own servers using their private keys.
- **Decryption exclusions** - traffic that must not be decrypted for legal, privacy, or technical reasons, for example banking and health categories, and applications using certificate pinning.

Without decryption, App-ID and threat inspection see far less of encrypted traffic. The
trade-off between visibility and privacy is a legitimate exam theme.

## Exam pointers

- Traffic logs default to end-of-session. Session-start logging is a troubleshooting choice, not a default.
- A security rule with no log forwarding profile sends nothing to Panorama or syslog, even though it logs locally.
- HA1 is control, HA2 is session sync, HA3 is packet forwarding in active/active.
- Path and link monitoring exist to detect failures upstream of the device.
- Certificate pinning breaks SSL Forward Proxy, so those applications need decryption exclusions.

## Official documentation

**[📖 PAN-OS Administrator's Guide](https://docs.paloaltonetworks.com/pan-os)** - configuration reference
**[📖 PAN-OS upgrade guidance](https://docs.paloaltonetworks.com/pan-os/upgrade)** - supported upgrade paths
**[📖 High availability](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/high-availability)** - HA modes and link roles
