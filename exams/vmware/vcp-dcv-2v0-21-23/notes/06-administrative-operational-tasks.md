---
last-updated: 2026-07-29
---

# VCP-DCV Section 6 - Administrative and Operational Tasks

The routine work: VM lifecycle, permissions, monitoring, security hardening, and
automation.

## VM lifecycle

- **Create** - from scratch, from a template, by cloning, or by deploying an OVF/OVA.
- **Template** - a master image that cannot be powered on. Convert to template or clone to template.
- **Guest customization specification** - applies hostname, IP, domain join, and SID regeneration during deployment. Without it, cloned Windows machines share identities.
- **Clone** - a copy taken now. Cloning a running VM produces a crash-consistent copy unless quiesced.
- **Instant Clone** - a running clone sharing memory and disk state with its parent, used for rapid provisioning such as VDI.
- **Snapshot** - a point-in-time state, comprising memory (optional) and delta disks. **Not a backup.** Delete or consolidate promptly.
- **Migrate** - compute, storage, or both, hot or cold.
- **Remove from inventory versus Delete from disk** - the first unregisters and leaves files in place; the second destroys them. Confusing these is a genuine data-loss risk and a plausible exam distractor.

## Permissions and roles in practice

- **Role** - a set of privileges, cloned from a sample role and edited rather than modifying the built-ins.
- **Permission** - user or group, plus role, applied to an inventory object, optionally propagating.
- **Least privilege** - assign the narrowest role at the lowest object that satisfies the need.
- **Global permissions** - apply across all inventory hierarchies and all linked vCenters.
- **No cryptography administrator** - a role variant excluding encryption privileges, used where administrators should not access encrypted VM keys.

## Monitoring and alarms

- **Alarm** - a definition with a trigger (condition or event), plus actions.
- **Alarm actions** - send email, send SNMP trap, or run a script.
- **Alarm scope** - defined at a parent object and inherited by children, so a datacenter-level alarm covers all hosts within it.
- **Acknowledge versus reset** - acknowledging silences the alarm and records who saw it, but leaves it triggered; resetting returns it to normal.
- **Events and tasks** - the audit record of what happened and who did it.
- **Syslog and SNMP** - external monitoring integration.
- **Performance charts** - real-time (20 seconds, retained one hour) and historical rollups (daily, weekly, monthly, yearly).

Acknowledging an alarm does not clear the underlying condition. That difference is
examined.

## Security and hardening

- **Lockdown mode** - normal permits DCUI for exception users; strict disables the DCUI. Both push administration through vCenter.
- **ESXi firewall** - service-based rules with allowed IP ranges.
- **ESXi Shell and SSH** - disabled by default and should stay disabled, enabled temporarily with a timeout when needed.
- **Certificate management** - VMCA acts as an internal CA, or you install custom or enterprise CA certificates.
- **VM encryption** - encrypts VM files using a key provider (a standard key provider with an external KMS, or the native key provider). Requires the appropriate license and a configured key provider.
- **vMotion encryption** - opportunistic, required, or disabled, per VM.
- **Virtual TPM (vTPM)** - a virtual Trusted Platform Module for guests requiring it, such as Windows 11. Depends on VM encryption being available.
- **UEFI Secure Boot** - for hosts and for VMs.
- **Host profiles** - capture a reference host's configuration and apply it to others, with compliance checking. The standard answer for enforcing consistent host configuration at scale.

## Automation and APIs

- **PowerCLI** - the PowerShell module for vSphere, and the automation tool most likely to appear.
  - `Connect-VIServer` opens a session.
  - `Get-VM`, `Get-VMHost`, `Get-Datastore` retrieve inventory.
  - `New-VM`, `Set-VM`, `Remove-VM` manage VMs.
  - `Move-VM` performs migrations.
  - `Get-Help <cmdlet> -Examples` is the discovery route.
- **vSphere REST API** - the modern programmatic interface.
- **vSphere Automation SDKs** - language bindings.
- **Scheduled tasks** - run operations such as power actions or snapshots at defined times.

## Content Library operations

- **Local library** - stores templates, ISOs, and other files.
- **Published library** - shares content with subscribers.
- **Subscribed library** - consumes published content, either downloading immediately or on demand.
- **Versioning** - templates can be checked out, updated, and checked in.

## Capacity and reporting

- **Datastore usage alarms** - warn before a datastore fills.
- **Storage reports and views** - capacity and usage.
- **Aria Operations** - capacity forecasting and right-sizing.
- **Licensing view** - assigned versus available capacity, and expiry.

## Exam pointers

- Remove from inventory keeps the files; Delete from disk destroys them.
- Guest customization prevents duplicate identities on cloned Windows VMs.
- Alarms defined at a parent object propagate to children.
- Acknowledging an alarm is not the same as resolving or resetting it.
- Host profiles enforce configuration consistency across hosts.
- vTPM depends on VM encryption and a configured key provider.
- PowerCLI starts with `Connect-VIServer`.

## Official documentation

**[📖 vSphere security](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere.html)** - hardening, encryption, lockdown
**[📖 vSphere VM administration](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere.html)** - VM lifecycle operations
**[📖 PowerCLI documentation](https://developer.broadcom.com/powercli)** - cmdlet reference
