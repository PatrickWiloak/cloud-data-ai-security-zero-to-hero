---
last-updated: 2026-07-29
---

# OSCP 04 - Privilege Escalation (Linux and Windows)

Turning a low-privilege foothold into full control of the host. Like enumeration, this is
mostly a search problem: the escalation path is usually present and the work is finding it.

> Authorised testing only. Methodology as taught in PEN-200, for the exam, your lab, or
> authorised engagements.

## The universal method

1. **Establish who you are** - current user, groups, and privileges.
2. **Enumerate the system systematically** - OS and kernel version, running processes and services, scheduled tasks, installed software, network connections, and file permissions.
3. **Look for the misconfiguration** - escalation almost always comes from a misconfiguration or a vulnerable component, not a zero-day.
4. **Verify before exploiting** - confirm the finding is real and applies.

Run enumeration scripts, but also read their output rather than trusting a summary. The
path is often in a line the script did not flag.

## Linux privilege escalation

**Enumeration targets**

- **Kernel version** - a vulnerable kernel may allow a public local exploit. High reward, but kernel exploits can crash the box, so treat as a later option.
- **sudo rights** - `sudo -l` shows what you may run as another user. Misconfigured sudo entries are the most common escalation path. Cross-reference against known techniques for abusing specific binaries.
- **SUID and SGID binaries** - executables running with the owner's privileges. A SUID binary owned by root that can spawn a shell or write files is a direct path.
- **Cron jobs** - scheduled tasks running as a privileged user. A writable script or a script called without an absolute path can be hijacked.
- **Writable files and directories** - world-writable scripts run by root, writable `/etc/passwd`, or writable service configuration.
- **Capabilities** - Linux capabilities on binaries can grant specific privileges without full SUID.
- **Environment and PATH** - a program calling another without an absolute path, combined with a writable PATH entry, allows substitution.
- **Credentials on disk** - configuration files, history files, backups, and scripts frequently contain passwords.
- **NFS no_root_squash** - a remote share mounted where root on the client maps to root on the server allows planting a SUID binary.

**Common paths, in rough order of preference**

1. Reused or discovered credentials tried with `su` and `sudo`.
2. `sudo -l` misconfigurations.
3. Abusable SUID binaries.
4. Writable cron jobs or service files.
5. Kernel exploit, as a later resort.

## Windows privilege escalation

**Enumeration targets**

- **Current privileges** - `whoami /priv`. Tokens such as SeImpersonatePrivilege and SeBackupPrivilege each enable specific, well-documented escalation techniques.
- **OS version and patch level** - missing patches may enable a public local exploit.
- **Service misconfigurations**:
  - **Unquoted service paths** - a service path with spaces and no quotes lets you plant a binary earlier in the path.
  - **Weak service permissions** - a service you can reconfigure to run your binary, or restart.
  - **Writable service binary** - replace the executable a privileged service runs.
- **Scheduled tasks** - running as a privileged account with a modifiable action.
- **AlwaysInstallElevated** - a registry setting causing MSI packages to install as SYSTEM.
- **Stored credentials** - the registry, unattended install files, saved credentials, the Windows Credential Manager, and configuration files.
- **DLL hijacking** - a service or application loading a DLL from a writable location.
- **Token impersonation** - SeImpersonatePrivilege enables a family of well-known techniques to obtain a SYSTEM token from a service account.

**Common paths**

1. Token privileges from `whoami /priv`, especially SeImpersonate.
2. Service misconfigurations (unquoted path, weak permissions, writable binary).
3. Stored credentials.
4. Missing-patch local exploit.

## Working the escalation

- **Automated enumeration** - scripts collect the data quickly. Read the raw output, not just the highlights, because the winning line is often unflagged.
- **Manual verification** - confirm permissions and paths yourself before spending time.
- **One change at a time** - so you can tell what worked, and can undo it.
- **Stable shell first** - do not attempt escalation from a fragile shell that dies on a syntax error.

## Post-escalation

- **Confirm** - verify you are root or SYSTEM.
- **Collect proof** - the exam requires specific proof files; read the exam guide for exactly what and where.
- **Loot for lateral movement** - credentials, hashes, and keys usable against other hosts.
- **Document** - commands, output, and screenshots for the report.

## Exam pointers

- Enumerate systematically; the path is nearly always a misconfiguration you can find.
- On Linux, start with credentials, `sudo -l`, and SUID binaries before kernel exploits.
- On Windows, start with `whoami /priv` and service misconfigurations before local exploits.
- Kernel and OS exploits carry crash risk and limited resets; prefer misconfigurations first.
- Read raw enumeration output; scripts miss things.
- Collect the exact proof files the exam specifies, and screenshot everything.

## Official documentation

**[📖 OffSec PEN-200 syllabus](https://www.offsec.com/courses/pen-200/)** - authoritative content list
**[📖 OSCP exam guide - proof requirements](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide)** - what to submit
**[📖 GTFOBins](https://gtfobins.github.io/)** and **[📖 LOLBAS](https://lolbas-project.github.io/)** - abusable binaries on Linux and Windows
