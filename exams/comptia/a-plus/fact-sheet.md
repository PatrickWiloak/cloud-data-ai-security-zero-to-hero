---
last-updated: 2026-09-28
---

# CompTIA A+ (220-1201 and 220-1202) Fact Sheet

## Quick Reference

**Exam Code:** 220-1201 + 220-1202
**Exams:** Core 1 (220-1201) and Core 2 (220-1202). You must pass both, from the same series.
**Series:** V15, launched March 25, 2025. CompTIA estimates retirement in 2028.
**Duration:** 90 minutes per exam
**Questions:** Maximum of 90 per exam (multiple choice, drag-and-drop, performance-based)
**Passing Score:** Core 1 **675**/900, Core 2 **700**/900
**Cost:** Two vouchers, one per exam. Price not verified on an official page (see below)
**Validity:** 3 years from passing the second exam
**Delivery:** Pearson VUE (testing center or online proctored)
**Languages:** English, German, Japanese

### Verified facts and sources (checked 2026-09-28)

| Fact | Value | Source |
|------|-------|--------|
| Core 1 code, length, questions, passing score, weights | 220-1201, 90 min, max 90, 675 | [CompTIA Core 1 V15 page](https://www.comptia.org/en-us/certifications/a/core-1-v15/) |
| Core 2 code, length, questions, passing score, weights | 220-1202, 90 min, max 90, 700 | [CompTIA Core 2 V15 page](https://www.comptia.org/en-us/certifications/a/core-2-v15/) and the [220-1202 objectives PDF](https://assets.ctfassets.net/82ripq7fjls2/6I8WL66IBa1AUovioDGrnM/f74a7eca336fd4e4c8e723a1f893086d/CompTIA-A-220-1202-Exam-Objectives-3.0.pdf) |
| V15 launch date | March 25, 2025 | CompTIA Core 1 and Core 2 V15 pages |
| V14 (220-1101/1102) retirement | "September 2025" on CompTIA's FAQ; third-party trackers give September 25, 2025 as the last test date | [CompTIA Core 1 V15 FAQ](https://www.comptia.org/en-us/certifications/a/core-1-v15/) |
| Both exams must be the same version | Yes. A Core 1 pass from a retired series no longer counts | CompTIA Core 1 V15 FAQ |
| Price | **Not verified.** CompTIA loads prices per region in its store and no USD figure could be read from an official page. Third-party guides in 2026 quote about $246 to $274 per exam | Check the CompTIA store for your region |

## Exam Domain Breakdown

### Core 1 (220-1201)

| Domain | Weight | Focus |
|--------|--------|-------|
| 1.0 Mobile Devices | 13% | Laptop parts, USB-C/Lightning/NFC/Bluetooth, hotspot, MDM, BYOD |
| 2.0 Networking | 23% | Ports, Wi-Fi, DNS/DHCP, VLAN, VPN, PoE, SOHO IP, tools |
| 3.0 Hardware | 25% | Displays, cables, RAM, storage, RAID, motherboards, CPUs, PSUs, printers |
| 4.0 Virtualization and Cloud Computing | 11% | Hypervisors, containers, VDI, IaaS/PaaS/SaaS, cloud characteristics |
| 5.0 Hardware and Network Troubleshooting | 28% | Symptom to cause for every hardware area plus networks and printers |

### Core 2 (220-1202)

| Domain | Weight | Focus |
|--------|--------|-------|
| 1.0 Operating Systems | 28% | Windows tools and commands, editions, installs, macOS, Linux |
| 2.0 Security | 28% | Controls, Windows security, wireless, malware, hardening, data destruction |
| 3.0 Software Troubleshooting | 23% | Windows, mobile OS, mobile security, PC security symptoms |
| 4.0 Operational Procedures | 21% | Ticketing, change, backup, safety, professionalism, scripting, remote access, AI |

## Ports You Must Know (Core 1 objective 2.1)

| Port | Protocol | Transport | Purpose |
|------|----------|-----------|---------|
| 20-21 | FTP | TCP | File transfer (20 data, 21 control). Cleartext |
| 22 | SSH | TCP | Encrypted remote shell. SFTP also runs here |
| 23 | Telnet | TCP | Cleartext remote shell. Replace with SSH |
| 25 | SMTP | TCP | Sending mail between servers |
| 53 | DNS | UDP and TCP | Name resolution (UDP queries, TCP zone transfers and large replies) |
| 67/68 | DHCP | UDP | Address assignment (67 server, 68 client) |
| 80 | HTTP | TCP | Web, cleartext |
| 110 | POP3 | TCP | Mail download, usually deletes from server |
| 137-139 | NetBIOS/NetBT | UDP and TCP | Legacy Windows name and session services |
| 143 | IMAP | TCP | Mail access, keeps mail on the server and syncs |
| 389 | LDAP | TCP and UDP | Directory queries (Active Directory) |
| 443 | HTTPS | TCP | Web over TLS |
| 445 | SMB/CIFS | TCP | Windows file and printer sharing |
| 3389 | RDP | TCP and UDP | Remote Desktop |

**Handy extras (outside the 2.1 list but seen in Core 2):** RADIUS 1812/1813 UDP, TACACS+ 49 TCP, Kerberos 88, VNC 5900, WinRM 5985/5986, secure mail variants (IMAPS 993, POP3S 995, SMTP submission 587).

**[📖 IANA Service Name and Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)** - The authoritative port list

## Wi-Fi Standards

| Standard | Wi-Fi name | Bands | Max theoretical speed |
|----------|------------|-------|-----------------------|
| 802.11a | - | 5 GHz | 54 Mbps |
| 802.11b | - | 2.4 GHz | 11 Mbps |
| 802.11g | - | 2.4 GHz | 54 Mbps |
| 802.11n | Wi-Fi 4 | 2.4 and 5 GHz | 600 Mbps (MIMO) |
| 802.11ac | Wi-Fi 5 | 5 GHz | About 6.9 Gbps (MU-MIMO) |
| 802.11ax | Wi-Fi 6 / 6E | 2.4, 5 GHz (6E adds 6 GHz) | About 9.6 Gbps (OFDMA) |
| 802.11be | Wi-Fi 7 | 2.4, 5, 6 GHz | About 46 Gbps (320 MHz channels, MLO) |

- **2.4 GHz** - Longer range, better through walls, crowded. Non-overlapping channels 1, 6, 11 in the US.
- **5 GHz** - Faster, shorter range, many more non-overlapping channels.
- **6 GHz** - Wi-Fi 6E and 7 only, very clean spectrum, shortest range, requires WPA3.
- **Channel width** - 20, 40, 80, 160 MHz (320 MHz on Wi-Fi 7). Wider is faster but uses more spectrum and overlaps more.

## Cabling Quick Reference

### Copper twisted pair

| Category | Max speed | Max distance |
|----------|-----------|--------------|
| Cat 5 | 100 Mbps | 100 m |
| Cat 5e | 1 Gbps | 100 m |
| Cat 6 | 1 Gbps (10 Gbps to about 55 m) | 100 m |
| Cat 6a | 10 Gbps | 100 m |
| Cat 8 | 25/40 Gbps | 30 m |

- **T568B pin order:** white-orange, orange, white-green, blue, white-blue, green, white-brown, brown.
- **T568A pin order:** white-green, green, white-orange, blue, white-blue, orange, white-brown, brown.
- **Straight-through** = same standard both ends. **Crossover** = A on one end, B on the other.
- **UTP** is standard. **STP** adds shielding for EMI. **Plenum-rated** jacket is required in air-handling spaces (low smoke, fire resistant). **Direct burial** is for underground runs.
- **Coax** (RG-6) uses the **F-type** connector for cable internet and TV.

### Fiber

| Type | Light source | Distance | Typical use |
|------|-------------|----------|-------------|
| Single-mode | Laser | Kilometers | ISP and campus backbones |
| Multimode | LED or VCSEL | Hundreds of meters | Inside a building or data center |

**Connectors:** ST (round, bayonet twist), SC (square, push-pull), LC (small, latching, common on SFP modules).

### Peripheral and video

| Cable | Notes |
|-------|-------|
| USB 2.0 | 480 Mbps |
| USB 3.0 (3.2 Gen 1) | 5 Gbps, blue insert on Type-A ports |
| USB-C | Reversible connector. Can carry USB 3.x/4, DisplayPort, Thunderbolt, and power |
| Thunderbolt 3/4 | 40 Gbps over USB-C connector |
| Lightning | Apple 8-pin, older iPhones and iPads |
| Serial (DB9) | Legacy RS-232, still used for console ports |
| HDMI | Digital video plus audio |
| DisplayPort | Digital video plus audio, daisy-chaining |
| DVI | Digital (DVI-D), analog (DVI-A), or both (DVI-I). No audio |
| VGA | Analog, DE-15 connector. No audio |
| SATA / eSATA | Internal and external drive data |
| Molex | Legacy 4-pin drive power |
| RJ11 / RJ45 | Phone line (2-4 wires) / Ethernet (8 wires) |

## RAM

| Type | Desktop DIMM pins | Laptop SODIMM pins |
|------|-------------------|--------------------|
| DDR3 | 240 | 204 |
| DDR4 | 288 | 260 |
| DDR5 | 288 (different notch) | 262 |

- **ECC** detects and corrects single-bit errors. Servers and workstations. Board and CPU must support it.
- **Channels** - Dual or quad channel doubles or quadruples bandwidth. Install matched sticks in the color-coded slot pairs.

## Storage and RAID

| RAID | Min drives | Fault tolerance | Usable capacity |
|------|-----------|-----------------|-----------------|
| 0 (striping) | 2 | None, one failure loses everything | 100% |
| 1 (mirroring) | 2 | One drive | 50% |
| 5 (striping with parity) | 3 | One drive | (n-1) drives |
| 6 (double parity) | 4 | Two drives | (n-2) drives |
| 10 (stripe of mirrors) | 4 | One per mirror pair | 50% |

- **HDD spindle speeds:** 5,400 and 7,200 rpm (desktops/laptops), 10,000 and 15,000 rpm (servers).
- **SSD interfaces:** SATA (up to about 600 MB/s) vs NVMe over PCIe (several GB/s).
- **Form factors:** 2.5-inch, 3.5-inch, M.2 (keyed B, M, or B+M), mSATA.

## Motherboards and Power

| Form factor | Size |
|-------------|------|
| ATX | 12 x 9.6 in (305 x 244 mm) |
| microATX | 9.6 x 9.6 in (244 x 244 mm) |
| Mini-ITX | 6.7 x 6.7 in (170 x 170 mm) |

| Power rail / connector | Detail |
|------------------------|--------|
| 3.3 V (orange), 5 V (red), 12 V (yellow) | Main DC outputs. Black is ground |
| 20+4 pin ATX | Main motherboard power |
| 4/8 pin EPS | CPU power |
| 6/8 pin PCIe, 12V-2x6 (16 pin) | Graphics cards |
| 15-pin SATA power | Drives |
| Input | 110-120 VAC (North America) vs 220-240 VAC (most of the world). Most PSUs auto-sense |

## Printer Types

| Type | How it prints | Maintenance |
|------|---------------|-------------|
| Laser | Charged drum, toner fused by heat | Replace toner, apply maintenance kit (fuser, rollers), calibrate, clean |
| Inkjet | Liquid ink sprayed by printhead | Clean printheads, replace cartridges, calibrate/align, clear jams |
| Thermal | Heat on special paper (or ribbon) | Replace paper, clean heating element, remove debris |
| Impact | Pins strike an inked ribbon | Replace ribbon, printhead, and paper. Handles multipart forms |

**Laser imaging steps:** processing, charging, exposing, developing, transferring, fusing, cleaning.

## Windows Command Line (Core 2 objective 1.5)

| Command | Use |
|---------|-----|
| `cd`, `dir` | Navigate and list |
| `md`, `rmdir` | Make and remove directories |
| `robocopy` | Robust copy with retry, mirror, and logging |
| `ipconfig /all`, `/release`, `/renew`, `/flushdns` | View and reset IP config |
| `ping`, `tracert`, `pathping` | Reachability, route, route plus per-hop loss |
| `netstat -ano` | Connections and listening ports with process IDs |
| `nslookup` | Query DNS |
| `net use`, `net user` | Map drives, manage user accounts |
| `chkdsk /f /r` | Fix filesystem errors and find bad sectors |
| `format`, `diskpart` | Format volumes, manage disks and partitions |
| `sfc /scannow` | Repair protected system files |
| `gpupdate /force`, `gpresult /r` | Refresh and report Group Policy |
| `hostname`, `whoami`, `winver` | Computer name, current user, Windows version |
| `[command] /?` | Help for any command |

**[📖 Windows Commands Reference](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)** - Microsoft's reference for every command above

## Windows GUI Tools (Core 2 objective 1.4)

| Tool | Run command | Use |
|------|-------------|-----|
| Event Viewer | `eventvwr.msc` | System, Application, Security logs |
| Disk Management | `diskmgmt.msc` | Partitions, volumes, drive letters |
| Task Scheduler | `taskschd.msc` | Scheduled jobs |
| Device Manager | `devmgmt.msc` | Drivers and hardware status |
| Certificate Manager | `certmgr.msc` | User certificates |
| Local Users and Groups | `lusrmgr.msc` | Local accounts (not on Home editions) |
| Performance Monitor | `perfmon.msc` | Counters and logging over time |
| Group Policy Editor | `gpedit.msc` | Local policy (not on Home editions) |
| System Information | `msinfo32.exe` | Hardware and software inventory |
| Resource Monitor | `resmon.exe` | Live CPU, memory, disk, network per process |
| System Configuration | `msconfig.exe` | Boot options, safe boot, services |
| Disk Cleanup | `cleanmgr.exe` | Remove temp files |
| Defragment and Optimize | `dfrgui.exe` | Defrag HDDs, TRIM SSDs |
| Registry Editor | `regedit.exe` | Edit the registry (back up first) |

## Linux Commands (Core 2 objective 1.9)

| Command | Use |
|---------|-----|
| `ls`, `pwd`, `cd` | List, print working directory, change directory |
| `mv`, `cp`, `rm` | Move/rename, copy, delete |
| `chmod`, `chown` | Change permissions, change owner |
| `grep`, `find` | Search text, search for files |
| `fsck`, `mount` | Check a filesystem, attach a filesystem |
| `su`, `sudo` | Switch user, run one command as root |
| `apt`, `dnf` | Package managers (Debian/Ubuntu, Fedora/RHEL) |
| `ip`, `ping`, `curl`, `dig`, `traceroute` | Network config and testing |
| `man`, `cat`, `top`, `ps`, `du`, `df` | Help, show file, live processes, process list, directory usage, free disk space |
| `nano` | Simple text editor |

**Config files:** `/etc/passwd` (accounts), `/etc/shadow` (password hashes), `/etc/hosts` (static name mapping), `/etc/fstab` (mounts at boot), `/etc/resolv.conf` (DNS servers).

## Windows Editions (Core 2 objective 1.3)

| Feature | Home | Pro | Enterprise |
|---------|------|-----|------------|
| Join a domain | No | Yes | Yes |
| Group Policy Editor | No | Yes | Yes |
| BitLocker | No (device encryption only on some hardware) | Yes | Yes |
| Host RDP sessions | No (client only) | Yes | Yes |
| Max RAM (64-bit) | 128 GB | 2 TB | 6 TB |

**Windows 11 minimums:** 64-bit 1 GHz dual-core CPU on the supported list, 4 GB RAM, 64 GB storage, UEFI with Secure Boot capable, TPM 2.0.

**[📖 Windows 11 Specifications and System Requirements](https://learn.microsoft.com/en-us/windows/whats-new/windows-11-requirements)** - Microsoft's hardware requirements

## Security Quick Reference

| Topic | Remember |
|-------|----------|
| Wireless | WPA3 (SAE) best, WPA2-AES acceptable, TKIP and WEP obsolete |
| RADIUS vs TACACS+ | RADIUS: UDP, combines auth and authz, encrypts only the password. TACACS+: TCP 49, separates AAA, encrypts the whole payload |
| Kerberos | Ticket-based authentication used by Active Directory |
| NTFS + share permissions | Effective access over the network is the **most restrictive** of the two |
| Malware removal | 10 steps - investigate, quarantine, disable System Restore, remediate, update, scan, reimage if needed, schedule scans, re-enable System Restore, educate |
| Data destruction | Drill, shred, degauss (magnetic only), incinerate. Get a certificate of destruction from vendors |

## Backup Types

| Type | Backs up | Clears archive bit | Restore needs |
|------|----------|--------------------|---------------|
| Full | Everything | Yes | Last full |
| Incremental | Changes since last backup of any type | Yes | Last full + every incremental since |
| Differential | Changes since last full | No | Last full + last differential |
| Synthetic full | Built from a full plus incrementals, without re-reading the source | - | The synthetic full |

**3-2-1 rule:** three copies, two different media, one offsite. **GFS:** daily (son), weekly (father), monthly (grandfather) rotation.

## Common Exam Scenarios

1. **"Laptop will not charge"** - Check the adapter wattage and port first, then battery health.
2. **"Users get 169.254.x.x addresses"** - APIPA, the DHCP server is unreachable or out of addresses.
3. **"Can reach IPs but not names"** - DNS problem. Check DNS settings, `ipconfig /flushdns`, `nslookup`.
4. **"Ghost images on laser prints"** - Drum or cleaning issue.
5. **"Clicking noise and slow file access"** - Failing HDD. Back up now, check S.M.A.R.T.
6. **"BSOD after installing a driver"** - Boot to Safe Mode, roll back the driver.
7. **"Browser redirects and new toolbar"** - Adware or browser hijacker. Follow the malware removal steps.
8. **"Need Windows features like domain join and BitLocker"** - Pro or higher, not Home.
9. **"Move a file and keep NTFS permissions"** - Move within the same volume.
10. **"Dispose of drives with sensitive data"** - Physical destruction or certified wipe, with documentation.

---

**Good luck on your exams!** Memorize the port table, the RAID table, and the command lists cold. Most of the rest is recognizing a symptom and matching it to the cause.
