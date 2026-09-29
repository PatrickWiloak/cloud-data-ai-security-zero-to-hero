---
last-updated: 2026-09-28
difficulty: beginner
reading-time: 25 min
---

# Core 2 Domain 1: Operating Systems (28%)

## Overview

Operating Systems ties with Security as the largest Core 2 domain. It is mostly Windows: editions, installation, GUI tools, the command line, settings, and networking. It also covers macOS and Linux at a "know the tool and what it does" level, plus application requirements and cloud productivity tools. The PBQs here often show a problem and ask which tool or command fixes it, so learn every tool by its run name and purpose.

The objectives are:

- **1.1** Explain common OS types and their purposes.
- **1.2** Given a scenario, perform OS installations and upgrades in a diverse environment.
- **1.3** Compare and contrast basic features of Microsoft Windows editions.
- **1.4** Given a scenario, use Microsoft Windows OS features and tools.
- **1.5** Given a scenario, use the appropriate Microsoft command-line tools.
- **1.6** Given a scenario, configure Microsoft Windows settings.
- **1.7** Given a scenario, configure Microsoft Windows networking features on a client/desktop.
- **1.8** Explain common features and tools of the macOS/desktop OS.
- **1.9** Identify common features and tools of the Linux client/desktop OS.
- **1.10** Given a scenario, install applications according to requirements.
- **1.11** Given a scenario, install and configure cloud-based productivity tools.

**A note on Windows versions:** the objectives say Windows versions not past end of mainstream support, up to and including Windows 11, are in scope, and they still list Windows 10 editions. Microsoft ended support for most Windows 10 editions on October 14, 2025. Expect Windows 10 content to appear mainly as upgrade and end-of-life scenarios.

## 1.1 OS Types and Filesystems

### Operating systems

| Category | Examples | Notes |
|----------|----------|-------|
| **Workstation** | Windows, macOS, Linux, ChromeOS | ChromeOS is browser-centric, cloud-first, and runs Android and Linux apps |
| **Mobile** | iOS, iPadOS, Android | iOS/iPadOS are Apple only. Android is open source with vendor versions |

### Filesystems

| Filesystem | Used by | Key facts |
|------------|---------|-----------|
| **NTFS** | Windows | Permissions, encryption (EFS), compression, quotas, journaling. Default for Windows system drives |
| **ReFS** | Windows Server, Windows Pro for Workstations | Resilient File System. Built for large volumes and integrity, used with Storage Spaces |
| **FAT32** | Everything | Universal compatibility. **4 GB maximum file size.** No permissions |
| **exFAT** | Flash drives, SD cards | No 4 GB file limit, works on Windows and macOS. No permissions or journaling |
| **ext4** | Linux | Default on many Linux distributions. Journaling |
| **XFS** | Linux (Red Hat default) | High-performance, large files |
| **APFS** | macOS, iOS | Apple File System. Snapshots, encryption, optimized for SSDs |

**Compatibility concerns:** macOS reads NTFS but does not write it by default. Windows does not read APFS or ext4 without third-party tools. For a drive shared between Windows and Mac, use **exFAT**.

### Vendor life cycle

- **End of life (EOL)** - No more security updates. EOL systems are a security risk and fail compliance checks.
- **Update limitations** - Old hardware may not meet new OS requirements (Windows 11 needs TPM 2.0), so the device is stuck on an EOL OS.

## 1.2 Installations and Upgrades

### Boot methods

| Method | Use |
|--------|-----|
| **USB** | Most common. Bootable flash drive made with the Media Creation Tool or similar |
| **Network** (PXE) | Boot from the network to deploy images at scale |
| **Solid-state/flash drives** | External SSDs as installers or portable OSs |
| **Internet-based** | Download and install directly (macOS Recovery, some Linux netinstall) |
| **External/hot-swappable drive** | Install media on an external drive |
| **Internal hard drive (partition)** | A recovery partition that holds a reinstall image |
| **Multiboot** | Several OSs on one machine, choose at startup |

### Types of installation

| Type | What happens |
|------|--------------|
| **Clean install** | Wipe and install fresh. Best for performance and removing problems. Back up data first |
| **Upgrade** (in-place) | Keeps files, settings, and apps. Faster for users, but carries old problems forward |
| **Image deployment** | Apply a prepared, standard image to many machines |
| **Remote network installation** | Install over the network from a deployment server |
| **Zero-touch deployment** | Device ships straight to the user and configures itself when they sign in (Windows Autopilot, Apple Automated Device Enrollment) |
| **Recovery partition** | Restores the factory image from a hidden partition |
| **Repair installation** | Reinstalls Windows over itself, keeping files and apps, to fix corrupted system files |
| **Third-party drivers** | Storage controller (RAID/NVMe) drivers may need loading during setup or the installer cannot see the disk |

### Partitioning: GPT vs MBR

| | MBR | GPT |
|-|-----|-----|
| **Firmware** | Legacy BIOS | UEFI |
| **Max disk size** | 2 TB | Effectively unlimited (9.4 ZB) |
| **Partitions** | 4 primary (or 3 plus an extended partition with logical drives) | 128 on Windows |
| **Resilience** | One partition table | Backup copy of the table at the end of the disk, CRC checks |
| **Windows 11** | Not supported for the boot disk | Required (UEFI boot) |

**Drive format** - The installer formats the system partition NTFS. Choose quick format for a known good disk, full format to check for bad sectors.

### Upgrade considerations

- **Back up files and user preferences** before any upgrade.
- **Application and driver support** - Confirm apps and drivers work on the new version (backward compatibility).
- **Hardware compatibility** - Check CPU, TPM, RAM, and storage against requirements.
- **Feature updates and product life cycle** - Windows gets an annual feature update. Each version has its own support end date.

## 1.3 Windows Editions

| Feature | Home | Pro | Pro for Workstations | Enterprise |
|---------|------|-----|----------------------|------------|
| **Domain join** | No (workgroup only) | Yes | Yes | Yes |
| **Group Policy Editor (gpedit.msc)** | No | Yes | Yes | Yes |
| **BitLocker** | No (device encryption on supported hardware) | Yes | Yes | Yes |
| **Host RDP** | No (can connect out only) | Yes | Yes | Yes |
| **Max RAM (64-bit)** | 128 GB | 2 TB | 6 TB | 6 TB |
| **Other** | Consumer | Business basics, Hyper-V | ReFS, server-grade CPUs, up to 4 CPUs | Volume licensing, AppLocker, advanced security and management |

- **N versions** ship without media playback apps (for European regulations). Users can add the Media Feature Pack.
- **Domain vs workgroup** - A workgroup has local accounts on each PC. A domain has central accounts and policy in Active Directory.
- **32-bit Windows** can use only 4 GB RAM. Windows 11 is 64-bit only.
- **Upgrade paths** - Home to Pro is an in-place license upgrade. Moving to a different architecture (32-bit to 64-bit) needs a clean install.

**Windows 11 hardware requirements:** 1 GHz or faster, 2+ core 64-bit compatible processor, 4 GB RAM, 64 GB storage, UEFI with Secure Boot capability, TPM 2.0, DirectX 12 graphics.

**[📖 Windows 11 Specifications and System Requirements](https://learn.microsoft.com/en-us/windows/whats-new/windows-11-requirements)** - Microsoft's requirements list

## 1.4 Windows Features and Tools

### Task Manager (Ctrl+Shift+Esc)

| Tab | Use |
|-----|-----|
| **Processes** | CPU, memory, disk, network per app. End a hung task |
| **Performance** | Live graphs, uptime, memory in use |
| **Users** | Who is signed in and what they use |
| **Startup** | Enable or disable startup apps to speed boot |
| **Services** | Start and stop services, open Services console |

### MMC snap-ins

The Microsoft Management Console hosts admin tools as snap-ins. You can build a custom console with `mmc.exe`.

| Tool | Command | Use it when |
|------|---------|-------------|
| **Event Viewer** | `eventvwr.msc` | Finding why something crashed. System, Application, and Security logs |
| **Disk Management** | `diskmgmt.msc` | Initializing a new disk, creating, extending, or shrinking volumes, changing drive letters |
| **Task Scheduler** | `taskschd.msc` | Running scripts or tasks at a time or trigger |
| **Device Manager** | `devmgmt.msc` | Updating, rolling back, or disabling drivers. Yellow triangle means a problem |
| **Certificate Manager** | `certmgr.msc` | Viewing and importing user certificates |
| **Local Users and Groups** | `lusrmgr.msc` | Managing local accounts (not on Home) |
| **Performance Monitor** | `perfmon.msc` | Recording counters over time, building baselines |
| **Group Policy Editor** | `gpedit.msc` | Setting local policy (not on Home) |

### Additional tools

| Tool | Command | Use |
|------|---------|-----|
| **System Information** | `msinfo32.exe` | Full hardware and software inventory |
| **Resource Monitor** | `resmon.exe` | Which process is using disk, network, or a locked file |
| **System Configuration** | `msconfig.exe` | Boot options such as Safe Boot, services, diagnostic startup |
| **Disk Cleanup** | `cleanmgr.exe` | Delete temp files, update leftovers, Recycle Bin |
| **Disk Defragment** | `dfrgui.exe` | Defragment HDDs, run TRIM on SSDs |
| **Registry Editor** | `regedit.exe` | Edit the registry directly. Export a backup before changing anything |

## 1.5 Windows Command Line

**[📖 Windows Commands Reference](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)** - Microsoft's documentation for every command in this section

### Navigation and file management

| Command | Example | Does |
|---------|---------|------|
| `cd` | `cd C:\Users\Public` | Change directory. `cd ..` goes up one level |
| `dir` | `dir /a` | List files. `/a` includes hidden and system files |
| `md` | `md Reports` | Make a directory |
| `rmdir` | `rmdir /s Reports` | Remove a directory. `/s` removes its contents too |
| `robocopy` | `robocopy C:\Data \\srv\backup /mir` | Robust copy. Retries, preserves attributes, `/mir` mirrors (and deletes extras at the destination) |

### Disk management

| Command | Does |
|---------|------|
| `chkdsk` | Checks a volume. `/f` fixes errors, `/r` finds bad sectors and recovers readable data |
| `format` | Formats a volume, such as `format E: /fs:ntfs` |
| `diskpart` | Interactive disk tool: `list disk`, `select disk 1`, `clean`, `create partition primary`, `convert gpt` |

### Network

| Command | Does |
|---------|------|
| `ipconfig` | Shows IP settings. `/all` adds MAC, DHCP, and DNS details. `/release` and `/renew` refresh DHCP. `/flushdns` clears the DNS cache |
| `ping` | Tests reachability with ICMP echo. `-t` pings until stopped |
| `netstat` | Shows connections and listening ports. `-a` all, `-n` numeric, `-o` process ID, `-b` executable (needs admin) |
| `nslookup` | Queries DNS for a name or record |
| `net use` | Maps a network drive, such as `net use Z: \\server\share` |
| `tracert` | Lists every router hop to a destination |
| `pathping` | Combines `tracert` and `ping`, measuring loss at each hop over time |

### Informational and OS management

| Command | Does |
|---------|------|
| `hostname` | Shows the computer name |
| `net user` | Lists, creates, or changes local accounts. `net user jsmith /domain` queries a domain user |
| `winver` | Shows the Windows version and build |
| `whoami` | Shows the signed-in user. `/groups` lists group memberships |
| `[command] /?` | Help for any command |
| `gpupdate` | Refreshes Group Policy. `/force` reapplies every setting |
| `gpresult` | Shows which policies applied. `/r` for a summary |
| `sfc` | System File Checker. `sfc /scannow` repairs protected system files. Run as administrator |

Many commands need an **elevated** prompt: right-click Terminal or Command Prompt and choose Run as administrator.

## 1.6 Windows Settings

Windows 10 and 11 split settings between the **Settings** app and the older **Control Panel**. The exam lists both.

### Control Panel utilities

| Utility | Use |
|---------|-----|
| **Internet Options** | Proxy settings, security zones, clear browsing data (legacy IE settings still used by some apps) |
| **Devices and Printers** | Add and manage printers and devices |
| **Programs and Features** | Uninstall programs, turn Windows features on or off (Hyper-V, .NET) |
| **Network and Sharing Center** | Adapter settings, sharing options, network profile |
| **System** | Computer name, domain join, remote settings, advanced system settings (virtual memory, performance) |
| **Windows Defender Firewall** | Allow apps, inbound/outbound rules |
| **Mail** | Outlook profiles |
| **Sound** | Playback and recording devices |
| **User Accounts** | Local accounts, credential manager |
| **Device Manager** | Drivers |
| **Indexing Options** | What Windows Search indexes. Rebuild the index when search is broken |
| **Administrative Tools** | Shortcuts to the MMC tools (now "Windows Tools" in Windows 11) |
| **File Explorer Options** | View hidden files, hide or show file extensions, general and view options |
| **Power Options** | Power plans, hibernate, sleep/suspend, standby, lid close action, fast startup, USB selective suspend |
| **Ease of Access** | Accessibility (now "Accessibility" in Settings) |

**Power terms:**
- **Sleep/suspend/standby** - Keeps RAM powered, resumes in seconds, uses a little battery.
- **Hibernate** - Writes RAM to disk (`hiberfil.sys`) and powers off. Slower to resume, no battery use.
- **Fast startup** - A partial hibernate of the kernel at shutdown. Can hide driver problems and block dual-boot access to the disk. Turn it off when troubleshooting.
- **USB selective suspend** - Powers down idle USB devices. Disable it when USB devices disconnect randomly.

**Showing file extensions** is a security habit: `invoice.pdf.exe` looks like `invoice.pdf` when extensions are hidden.

### Settings app categories

Time and Language, Update and Security (Windows Update, recovery, activation), Personalization, Apps (default apps, optional features), Privacy (camera, microphone, location permissions), System (display, storage, notifications), Devices (Bluetooth, printers), Network and Internet, Gaming, and Accounts (sign-in options, work or school accounts).

## 1.7 Windows Networking

### Domain joined vs workgroup

| | Workgroup | Domain |
|-|-----------|--------|
| **Accounts** | Local on each PC | Central in Active Directory |
| **Management** | Per machine | Group Policy |
| **Scale** | Small offices (under about 20 PCs) | Any size |
| **Needs** | Any edition | Pro or higher, plus a domain controller |

### Shared resources

- **Printers** - Add by IP, by share name, or through a print server.
- **File servers and mapped drives** - Map with File Explorer (Map network drive) or `net use`. The path format is a **UNC path**: `\\server\share`.
- **Administrative shares** such as `C$` and `ADMIN$` exist by default and require admin rights.

### Local firewall

- Allow or block specific **applications** and **ports**. Create exceptions only for what is needed.
- Profiles apply by network type: **Domain**, **Private**, **Public**.

### Client network configuration

- **IP addressing scheme**, **subnet mask**, **gateway**, and **DNS settings** set in adapter properties (IPv4 properties) or Settings.
- **Static vs dynamic** - Static for servers and printers, DHCP for clients.
- **Alternate configuration** - A fallback static address when DHCP is unavailable.

### Connection types

- **VPN** - Built-in client (IKEv2, SSTP, L2TP) or a vendor client.
- **Wireless**, **wired**, and **WWAN/cellular** (built-in LTE/5G modems or USB dongles).

### Other settings

- **Proxy settings** - Manual proxy or automatic configuration script (PAC). A wrong proxy setting breaks web browsing while ping still works.
- **Public vs private network** - Public hides the PC and blocks discovery. Private allows discovery and sharing. Choose public for coffee shops.
- **Metered connections** - Windows limits background downloads and updates. Useful on cellular and hotspots.
- **File Explorer network paths** - Type `\\server\share` in the address bar.

## 1.8 macOS

| Area | What to know |
|------|--------------|
| **App file types** | **.dmg** (disk image, mount it and drag the app to Applications), **.pkg** (installer package that runs a setup wizard), **.app** (the application bundle itself) |
| **App Store** | Apple's store. Apps are sandboxed and reviewed |
| **Uninstall** | Drag the .app to the Trash. Some apps include an uninstaller for leftover files in Library folders |
| **System folders** | `/Applications` (apps), `/Users` (home folders), `/Library` (system-wide support files), `/System` (the OS, protected), `/Users/<name>/Library` (per-user preferences and caches) |
| **Apple ID and corporate restrictions** | Personal Apple IDs on corporate Macs may be restricted by MDM. Managed Apple IDs are available for business |
| **Best practices** | Backups (Time Machine), antivirus, updates and patches, **Rapid Security Response (RSR)**, which delivers urgent security fixes between full updates |
| **System Preferences** (System Settings since macOS Ventura) | Displays, Networks, Printers, Scanners, Privacy, Accessibility, Time Machine |

### macOS features and tools

| Feature | What it does |
|---------|--------------|
| **Multiple desktops / Mission Control** | Virtual desktops (Spaces) and an overview of all open windows |
| **Keychain** | Stores passwords, certificates, and keys |
| **Spotlight** | System-wide search (Cmd+Space) |
| **iCloud** | Sync for iMessage, FaceTime, Drive, photos, and more |
| **Gestures** | Multi-touch trackpad shortcuts |
| **Finder** | The file manager |
| **Dock** | App launcher and running apps bar |
| **Continuity** | Handoff, Universal Clipboard, AirDrop, and phone calls between Apple devices |
| **Disk Utility** | Format, partition, repair (First Aid), and create disk images |
| **FileVault** | Full-disk encryption |
| **Terminal** | Command line (zsh by default) |
| **Force Quit** | Cmd+Option+Esc, ends a hung app |
| **Time Machine** | Built-in backup to an external or network drive |

**[📖 macOS User Guide](https://support.apple.com/guide/mac-help/welcome/mac)** - Apple's documentation for every feature above

## 1.9 Linux

### Commands

| Category | Command | Does |
|----------|---------|------|
| **File management** | `ls` | List directory contents (`ls -l` long format, `ls -a` hidden files) |
| | `pwd` | Print the working directory |
| | `mv` | Move or rename |
| | `cp` | Copy (`cp -r` for directories) |
| | `rm` | Remove (`rm -r` for directories, no Recycle Bin) |
| | `chmod` | Change permissions, such as `chmod 755 script.sh` or `chmod u+x script.sh` |
| | `chown` | Change owner, such as `chown alice:staff report.txt` |
| | `grep` | Search inside files for text |
| | `find` | Search for files by name, size, date |
| **Filesystem** | `fsck` | Check and repair a filesystem (unmounted) |
| | `mount` | Attach a filesystem to a directory |
| **Administrative** | `su` | Switch to another user (root by default) |
| | `sudo` | Run one command as root, logged and controlled by `/etc/sudoers` |
| **Packages** | `apt` | Debian and Ubuntu package manager |
| | `dnf` | Fedora and Red Hat package manager |
| **Network** | `ip` | Show and set addresses and routes (`ip addr`, `ip route`). Replaces `ifconfig` |
| | `ping`, `traceroute` | Reachability and path |
| | `curl` | Fetch a URL, test web services |
| | `dig` | Query DNS |
| **Informational** | `man` | Manual page for a command |
| | `cat` | Show a file's contents |
| | `top` | Live process and resource view |
| | `ps` | Snapshot of processes (`ps aux`) |
| | `du` | Disk usage of files and directories |
| | `df` | Free space per filesystem (`df -h`) |
| **Text editors** | `nano` | Simple terminal editor |

**Permissions in `chmod` numbers:** read = 4, write = 2, execute = 1. `755` means owner rwx, group r-x, others r-x.

### Configuration files

| File | Holds |
|------|-------|
| `/etc/passwd` | User account list (no passwords despite the name) |
| `/etc/shadow` | Password hashes, readable only by root |
| `/etc/hosts` | Static name-to-IP mappings, checked before DNS |
| `/etc/fstab` | Filesystems to mount at boot |
| `/etc/resolv.conf` | DNS server settings |

### OS components

- **Kernel** - The core that manages hardware, memory, and processes.
- **Bootloader** - Loads the kernel at startup (GRUB is common).
- **systemd** - The init system and service manager on most distributions. Manage services with `systemctl start|stop|status|enable <service>`.
- **Root account** - The superuser. Avoid logging in as root. Use `sudo` for single commands.

**[📖 Linux man-pages Project](https://man7.org/linux/man-pages/)** - Reference manual pages for Linux commands and files

## 1.10 Installing Applications

| Requirement | Check |
|-------------|-------|
| **32-bit vs 64-bit** | 64-bit Windows runs most 32-bit apps. 32-bit Windows cannot run 64-bit apps |
| **Graphics** | Dedicated vs integrated GPU, and VRAM for CAD, video editing, and games |
| **RAM** | Minimum and recommended |
| **CPU** | Speed, cores, architecture (x64 vs ARM) |
| **External hardware tokens** | Some licensed software needs a USB dongle |
| **Storage** | Free space for install and working data |
| **App to OS compatibility** | Supported OS versions |

**Distribution methods:** physical media vs a mountable **ISO** file (Windows mounts ISOs natively with a double-click), downloadable package (MSI, EXE, MSIX, DMG, PKG, DEB, RPM), and image deployment.

**Impact considerations:** consider the effect of a new app on the **device** (performance, storage), the **network** (bandwidth, firewall rules), **operation** (support load, training), and the **business** (licensing cost, compliance, security).

## 1.11 Cloud-Based Productivity Tools

| Area | What to configure |
|------|-------------------|
| **Email systems** | Microsoft 365/Exchange Online or Google Workspace mailboxes, mail clients, mobile mail |
| **Storage** | OneDrive, Google Drive, SharePoint. **Sync/folder settings** such as Files On-Demand and which folders sync |
| **Collaboration tools** | Spreadsheets, videoconferencing, presentation tools, word processing, instant messaging (Teams, Google Meet, Slack, Zoom) |
| **Identity synchronization** | Syncing on-premises Active Directory accounts to the cloud identity provider (Microsoft Entra Connect), so users have one set of credentials |
| **Licensing assignment** | Users need a license assigned before the service works. "Mailbox not found" for a new starter is often a missing license |

## Exam Tips and Traps

1. **FAT32 cannot store files over 4 GB.** Use exFAT for large files on removable drives.
2. **Home edition cannot join a domain, run gpedit, use BitLocker, or host RDP.**
3. **MBR is limited to 2 TB and 4 primary partitions.** GPT needs UEFI.
4. **Repair installation** keeps files and apps while fixing Windows.
5. **Know the .msc names**: eventvwr, diskmgmt, taskschd, devmgmt, certmgr, lusrmgr, perfmon, gpedit.
6. **`sfc /scannow` fixes system files. `chkdsk /f` fixes the filesystem.**
7. **`gpupdate /force` applies policy. `gpresult /r` reports it.**
8. **`robocopy /mir` deletes files at the destination** that are not at the source.
9. **Public network profile** for untrusted Wi-Fi.
10. **Force Quit is Cmd+Option+Esc** on macOS.
11. **`sudo` runs one command as root.** `su` switches user.
12. **`/etc/shadow` holds hashes. `/etc/passwd` lists accounts.**

## Related Notes

- [07 - Security](07-security.md#22-windows-security-settings) - BitLocker, Defender, NTFS permissions, Active Directory
- [08 - Software Troubleshooting](08-software-troubleshooting.md) - Using these tools to fix problems
- [09 - Operational Procedures](09-operational-procedures.md#48-scripting-basics) - Scripting on Windows, macOS, and Linux
- [Fact Sheet](../fact-sheet.md#windows-command-line-core-2-objective-15) - Command tables for review
