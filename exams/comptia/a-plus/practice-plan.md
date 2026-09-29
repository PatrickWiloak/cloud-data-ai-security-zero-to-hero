---
last-updated: 2026-09-28
---

# CompTIA A+ (220-1201 and 220-1202) Study Plan

## 10-Week Schedule for Both Exams

This plan takes Core 1 at the end of week 5 and Core 2 at the end of week 10. Book both exams on day one: a date on the calendar keeps the plan honest. Both exams must come from the same series (V15), so do not leave a long gap between them. CompTIA estimates V15 retirement in 2028, so this is only a risk if you stall for years, but a Core 1 pass does not carry over to a new series.

Budget about 10-12 hours a week. Increase it if you are new to IT, shorten it if you already work in support.

### Week 1: Mobile Devices and Networking Foundations

#### Day 1-2: Mobile Devices
- [ ] Laptop replaceable parts: battery, keyboard, SODIMM, SSD, wireless card, antenna, webcam
- [ ] Connection methods: USB-C, microUSB, Lightning, NFC, Bluetooth, tethering, hotspot
- [ ] Docking station vs port replicator
- [ ] Review Notes: `01-mobile-devices.md`

#### Day 3-4: Mobile Connectivity and MDM
- [ ] Cellular data, SIM vs eSIM, hotspot
- [ ] Bluetooth pairing steps in order
- [ ] Location services, MDM, BYOD vs corporate-owned, synchronization and data caps
- [ ] Review Notes: `01-mobile-devices.md`

#### Day 5-6: Ports and Protocols
- [ ] Memorize the 14 ports in objective 2.1 both directions
- [ ] TCP vs UDP
- [ ] POP3 vs IMAP, Telnet vs SSH, HTTP vs HTTPS
- [ ] Review Notes: `02-networking.md`

#### Day 7: Week 1 Review
- [ ] Port flashcards until 100% from memory
- [ ] 20 practice questions on mobile and ports (target: 70%+)

### Week 2: Networking

#### Day 8-9: Wireless and Services
- [ ] 2.4, 5, 6 GHz trade-offs, channels 1/6/11, channel widths
- [ ] 802.11a/b/g/n/ac/ax/be table
- [ ] Server roles, spam gateway, UTM, load balancer, proxy, SCADA, IoT
- [ ] Review Notes: `02-networking.md`

#### Day 10-11: Configuration and Hardware
- [ ] DNS records: A, AAAA, CNAME, MX, TXT, and SPF/DKIM/DMARC
- [ ] DHCP scope, lease, reservation, exclusion
- [ ] Routers, managed vs unmanaged switches, AP, patch panel, firewall, PoE standards, ONT, cable modem, DSL
- [ ] Review Notes: `02-networking.md`

#### Day 12-13: SOHO and Connection Types
- [ ] Private ranges, APIPA, loopback, IPv6 basics
- [ ] Configure a SOHO router in a lab (DHCP reservation, WPA3, guest network)
- [ ] Internet connection types and network types
- [ ] Networking tools: crimper, punchdown, toner probe, cable tester, loopback, tap
- [ ] Review Notes: `02-networking.md`

#### Day 14: Week 2 Review
- [ ] 30 networking practice questions (target: 70%+)
- [ ] Draw the SOHO network from memory

### Week 3: Hardware

#### Day 15-16: Displays and Cables
- [ ] LCD types (IPS, TN, VA), OLED, Mini-LED, attributes
- [ ] Cat 5e to Cat 8 table, T568A/B, plenum, direct burial
- [ ] Fiber: single-mode vs multimode, ST/SC/LC
- [ ] Video: HDMI, DisplayPort, DVI, VGA, USB-C. Peripheral: USB versions, Thunderbolt, serial
- [ ] Review Notes: `03-hardware.md`

#### Day 17-18: RAM, Storage, RAID
- [ ] DIMM vs SODIMM, DDR generations, ECC, channels
- [ ] HDD speeds and sizes, SATA vs NVMe vs SAS, M.2 keying, mSATA
- [ ] RAID 0/1/5/6/10: minimum drives, fault tolerance, usable capacity
- [ ] Review Notes: `03-hardware.md`

#### Day 19-20: Motherboards, CPUs, Power
- [ ] ATX, microATX, ITX. PCIe lanes, headers, M.2
- [ ] Sockets, x64 vs ARM, cores, virtualization support
- [ ] UEFI settings: boot options, Secure Boot, TPM, passwords, USB permissions
- [ ] PSU: input voltage, rails, 20+4, modular, redundant, wattage, efficiency
- [ ] Hands-on: take apart and rebuild a PC
- [ ] Review Notes: `03-hardware.md`

#### Day 21: Week 3 Review
- [ ] 30 hardware practice questions (target: 70%+)
- [ ] Drill the RAID and cable tables from memory

### Week 4: Printers, Virtualization, Cloud

#### Day 22-23: Printers
- [ ] MFD deployment: drivers (PCL vs PostScript), connectivity, sharing, security, scan services
- [ ] Laser 7 steps in order
- [ ] Maintenance for laser, inkjet, thermal, impact
- [ ] Review Notes: `03-hardware.md`

#### Day 24-25: Virtualization and Cloud
- [ ] VM purposes, Type 1 vs Type 2, containers, VDI, requirements
- [ ] Cloud models: public, private, hybrid, community. IaaS, PaaS, SaaS
- [ ] Characteristics: metered, ingress/egress, elasticity, multitenancy
- [ ] Hands-on: build a VM in VirtualBox or Hyper-V
- [ ] Review Notes: `04-virtualization-cloud.md`

#### Day 26-27: Hardware and Network Troubleshooting
- [ ] Troubleshooting methodology (competency, not tested as an objective)
- [ ] Symptom tables for 5.1 to 5.6
- [ ] Review Notes: `05-hardware-network-troubleshooting.md`

#### Day 28: Week 4 Review
- [ ] 40 troubleshooting practice questions (target: 75%+)

### Week 5: Core 1 Exam Week

#### Day 29-31: Full Practice Exams
- [ ] Full-length Core 1 practice exam #1 (target: 80%+)
- [ ] Review every wrong answer and the objective behind it
- [ ] Full-length Core 1 practice exam #2 (target: 85%+)
- [ ] PBQ practice: cable to port matching, RAID selection, printer fault ordering

#### Day 32-34: Final Core 1 Review
- [ ] Reread the [fact sheet](fact-sheet.md) tables
- [ ] Final pass through `05-hardware-network-troubleshooting.md`
- [ ] Rest the day before

#### Day 35: Sit Core 1 (220-1201), passing score 675

### Week 6: Operating Systems

#### Day 36-37: OS Types and Installation
- [ ] Filesystems: NTFS, ReFS, FAT32, exFAT, ext4, XFS, APFS
- [ ] Boot methods, install types, GPT vs MBR, upgrade considerations
- [ ] Windows editions and Windows 11 requirements
- [ ] Review Notes: `06-operating-systems.md`

#### Day 38-39: Windows Tools and Commands
- [ ] Task Manager tabs, every MMC snap-in by .msc name
- [ ] msinfo32, resmon, msconfig, cleanmgr, dfrgui, regedit
- [ ] Every command in objective 1.5, run in a VM
- [ ] Review Notes: `06-operating-systems.md`

#### Day 40-41: Settings and Networking
- [ ] Control Panel and Settings items, power options, File Explorer options
- [ ] Domain vs workgroup, mapped drives, firewall, proxy, public vs private, metered
- [ ] Review Notes: `06-operating-systems.md`

#### Day 42: Week 6 Review
- [ ] 30 OS practice questions (target: 70%+)

### Week 7: macOS, Linux, Apps, Cloud Tools

#### Day 43-44: macOS
- [ ] .dmg, .pkg, .app, system folders, Time Machine, FileVault, Keychain, Spotlight, Force Quit, Disk Utility
- [ ] Review Notes: `06-operating-systems.md`

#### Day 45-46: Linux
- [ ] Every command in objective 1.9, practiced in a VM or WSL
- [ ] chmod numbers, config files, systemd, sudo vs su
- [ ] Review Notes: `06-operating-systems.md`

#### Day 47-48: Applications and Cloud Productivity
- [ ] App requirements, distribution methods, impact considerations
- [ ] Email, storage sync, collaboration, identity sync, licensing
- [ ] Review Notes: `06-operating-systems.md`

#### Day 49: Week 7 Review
- [ ] 30 OS practice questions including macOS and Linux (target: 75%+)

### Week 8: Security

#### Day 50-51: Controls and Windows Security
- [ ] Physical and logical controls, MFA methods
- [ ] Defender, firewall, users and groups, UAC, BitLocker, EFS
- [ ] NTFS vs share permissions, inheritance, move vs copy
- [ ] Active Directory tasks
- [ ] Review Notes: `07-security.md`

#### Day 52-53: Wireless, Malware, Social Engineering
- [ ] WPA2 vs WPA3, TKIP vs AES, RADIUS vs TACACS+ vs Kerberos
- [ ] Malware types and tools (EDR, MDR, XDR)
- [ ] Social engineering, threats, vulnerabilities
- [ ] Malware removal 10 steps in order
- [ ] Review Notes: `07-security.md`

#### Day 54-55: Hardening and Disposal
- [ ] Workstation and mobile hardening
- [ ] Data destruction methods and when each works
- [ ] SOHO router and browser security
- [ ] Review Notes: `07-security.md`

#### Day 56: Week 8 Review
- [ ] 40 security practice questions (target: 75%+)

### Week 9: Software Troubleshooting and Operational Procedures

#### Day 57-58: Software Troubleshooting
- [ ] Windows symptoms and the repair ladder
- [ ] Mobile OS, app, and mobile security symptoms
- [ ] PC and browser security symptoms
- [ ] Review Notes: `08-software-troubleshooting.md`

#### Day 59-61: Operational Procedures
- [ ] Ticketing, asset management, documents
- [ ] Change management elements and change types
- [ ] Backup types, GFS, 3-2-1, recovery options
- [ ] Safety, environment, MSDS, power protection
- [ ] Incident response, licensing, regulated data
- [ ] Professionalism, scripting file types, remote access, AI basics
- [ ] Review Notes: `09-operational-procedures.md`

#### Day 62-63: Week 9 Review
- [ ] 40 practice questions on troubleshooting and procedures (target: 75%+)

### Week 10: Core 2 Exam Week

#### Day 64-66: Full Practice Exams
- [ ] Full-length Core 2 practice exam #1 (target: 80%+)
- [ ] Review every wrong answer
- [ ] Full-length Core 2 practice exam #2 (target: 85%+)
- [ ] PBQ practice: command selection, malware removal ordering, permissions

#### Day 67-69: Final Core 2 Review
- [ ] Fact sheet command and tool tables
- [ ] [Scenarios](scenarios.md) end to end
- [ ] Rest the day before

#### Day 70: Sit Core 2 (220-1202), passing score 700

## Compressed Plan (Experienced Technicians)

If you already work in desktop support, try four to six weeks:

| Week | Focus |
|------|-------|
| 1 | Core 1 domains 1-3, focusing on tables you do not use daily (Wi-Fi standards, RAID, printers) |
| 2 | Core 1 domains 4-5, two practice exams, sit Core 1 |
| 3 | Core 2 domains 1-2, especially macOS and Linux if you are Windows-only |
| 4 | Core 2 domains 3-4, two practice exams, sit Core 2 |

## Tracking Progress

| Area | Practice score 1 | Practice score 2 | Confident? |
|------|------------------|------------------|------------|
| Core 1 - Mobile Devices | | | |
| Core 1 - Networking | | | |
| Core 1 - Hardware | | | |
| Core 1 - Virtualization and Cloud | | | |
| Core 1 - HW/Network Troubleshooting | | | |
| Core 2 - Operating Systems | | | |
| Core 2 - Security | | | |
| Core 2 - Software Troubleshooting | | | |
| Core 2 - Operational Procedures | | | |

Aim for 85% or better on practice exams before booking the real one. Practice banks vary in difficulty, but consistent 85%+ across two different sources is a good sign.

## Related Pages

- [README](README.md) - Exam overview and domains
- [Fact Sheet](fact-sheet.md) - Tables to memorize
- [Strategy](strategy.md) - Exam-day tactics
- [Practice Questions](../../../resources/practice-questions/comptia-a-plus-220-1201-1202.md) - 20 original questions
