---
last-updated: 2026-09-28
---

# CompTIA A+ (220-1201 and 220-1202) Study Strategy

## Study Approach

### Which exam first?

CompTIA lets you take the two cores in any order. Most people take **Core 1 first** because its hardware and networking basics make Core 2's OS and security content easier to follow. Take Core 2 first only if you already work with Windows and security daily and want an early win.

Whatever the order, sit both exams from the **same series**. CompTIA's FAQ states that if a series retires before you pass the second core, your first result no longer counts toward the certification.

### Phase 1: Core 1 Foundation (3 weeks)
1. **Mobile Devices and Networking**
   - Laptop parts and mobile connectivity
   - The 14 ports, Wi-Fi standards, DNS and DHCP
   - SOHO addressing and networking hardware
2. **Hardware**
   - Cables and connectors, RAM, storage, RAID
   - Motherboards, CPUs, UEFI, power supplies
   - Printers and printer maintenance

### Phase 2: Core 1 Depth and Exam (2 weeks)
1. **Virtualization and Cloud**
2. **Hardware and Network Troubleshooting** - the heaviest Core 1 domain at 28%
3. **Practice exams and PBQs, then sit Core 1**

### Phase 3: Core 2 Foundation (3 weeks)
1. **Operating Systems** - Windows tools and commands, then macOS and Linux
2. **Security** - Windows security, malware removal, hardening, data destruction

### Phase 4: Core 2 Depth and Exam (2 weeks)
1. **Software Troubleshooting**
2. **Operational Procedures**
3. **Practice exams and PBQs, then sit Core 2**

## Study Resources

### Free Resources (Highly Recommended)
- **[📖 Professor Messer: 220-1101 vs 220-1201 Differences](https://www.professormesser.com/free-a-plus-training/a-plus-articles/differences-between-220-1101-and-220-1201/)** - What changed in Core 1, useful if you have older study material
- **[📖 Professor Messer: 220-1102 vs 220-1202 Differences](https://www.professormesser.com/free-a-plus-training/a-plus-articles/differences-between-220-1102-and-220-1202/)** - What changed in Core 2
- **[📖 Windows Commands Reference](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)** - Official docs for every Windows command on the exam
- **[📖 macOS User Guide](https://support.apple.com/guide/mac-help/welcome/mac)** - Apple's guide to Finder, Time Machine, FileVault, and more
- **[📖 Linux man-pages Project](https://man7.org/linux/man-pages/)** - Manual pages for the Linux commands

Professor Messer also publishes a free video course for each V15 core on the same site.

### Official CompTIA Resources
- **[📖 CompTIA A+ Certification](https://www.comptia.org/en-us/certifications/a/)** - Certification overview
- **[📖 A+ Core 1 V15 (220-1201)](https://www.comptia.org/en-us/certifications/a/core-1-v15/)** - Exam details, domain weights, and FAQ
- **[📖 A+ Core 2 V15 (220-1202)](https://www.comptia.org/en-us/certifications/a/core-2-v15/)** - Exam details and domain weights
- **[📖 A+ 220-1202 Exam Objectives (PDF)](https://assets.ctfassets.net/82ripq7fjls2/6I8WL66IBa1AUovioDGrnM/f74a7eca336fd4e4c8e723a1f893086d/CompTIA-A-220-1202-Exam-Objectives-3.0.pdf)** - The full Core 2 objectives. Download the Core 1 objectives from the Core 1 page

CompTIA also sells CertMaster Learn, Labs, and Practice for each core. Check the product pages for what is included.

### Paid Courses and Practice Exams
1. **Professor Messer 220-1201/220-1202 course notes and practice exams** - Low cost, closely follows the objectives
2. **Mike Meyers A+ (Total Seminars)** - Video courses, books, and TotalTester practice exams
3. **Jason Dion A+ practice exams** (Udemy) - Large question banks with PBQ-style items
4. **CompTIA CertMaster Practice** - Official adaptive practice questions

Make sure any material you buy is labeled 220-1201/220-1202 or V15. Older 1101/1102 material covers most of the same ground but misses the AI objective and some reorganized content.

## Exam Tactics

### Question Strategy
1. **Read the last sentence first** - It tells you what is actually being asked.
2. **Spot the qualifier** - "BEST", "FIRST", "MOST likely", "NEXT". They change the answer.
3. **Eliminate the clearly wrong** - Usually two options go quickly.
4. **Least disruptive fix first** - For "first" or "next step" questions, pick the gentle, non-destructive option (check the cable, restart the service) over reimaging.
5. **Look for the obvious** - Many scenarios hide a simple answer: wrong input source, Wi-Fi turned off, USB stick left in.

### Time Management
- **Up to 90 questions in 90 minutes** per exam, so about one minute per question.
- **PBQs usually come first.** Skip them, answer the multiple choice, then come back. They take 3-5 minutes each.
- **Flag and move** - Never spend more than 2 minutes on a multiple choice question.
- **Keep 10 minutes** at the end for flagged questions.

### Performance-Based Questions (PBQs)
Expect a few PBQs per exam. Common types:
- **Drag and drop matching** - Ports to protocols, cables to connectors, tools to tasks, RAID levels to requirements.
- **Ordering** - Laser printing steps, malware removal steps, Bluetooth pairing steps.
- **Simulated configuration** - SOHO router settings, Windows tools, command-line output interpretation.
- **Troubleshooting** - Pick the cause and fix from a set of symptoms.

Tips: read every instruction, check whether an item can be used more than once, and answer every part. Partial credit is generally believed to apply, so never leave a PBQ blank.

### Keyword Decision Matrix

| Keyword in the question | Usually points to |
|-------------------------|-------------------|
| "Drop ceiling" / "air handling" | Plenum-rated cable |
| "169.254" | APIPA, DHCP failure |
| "Most restrictive" / "over the network" | Share plus NTFS permissions |
| "Keep files and apps" + "fix Windows" | Repair install or Reset (keep files) |
| "Pre-approved" / "routine" | Standard change |
| "Carbon copies" / "multipart forms" | Impact printer |
| "Ghost image" | Laser drum or cleaning |
| "Wrong date after power loss" | CMOS battery |
| "Tailgating" | Access control vestibule |
| "Magnetic media only" | Degaussing |
| "Remote PowerShell" | WinRM |
| "Confident but wrong" | AI hallucination |

## Common Pitfalls

### Conceptual Pitfalls
- Confusing **incremental** and **differential** restore requirements.
- Thinking **RAID is a backup**.
- Thinking **hiding the SSID** is security.
- Mixing up **POP3** (download) and **IMAP** (sync).
- Forgetting that **Windows Home** lacks domain join, gpedit, BitLocker, and RDP hosting.

### Technical Pitfalls
- Degaussing an **SSD** (does nothing).
- Using **FAT32** for a 6 GB video file (4 GB limit).
- Wearing an **ESD strap** near high voltage.
- Choosing **Telnet** or **FTP** where a secure protocol is needed.
- Initializing disks when a **RAID array is missing**.

### Exam Pitfalls
- Spending 10 minutes on the first PBQ.
- Changing answers without a clear reason. First instincts are usually right unless you misread.
- Picking the most technical answer when the question is about **professionalism**. On behavior questions, choose the customer-focused option.

## Domain-Specific Tips

### Core 1
- **Mobile Devices (13%)** - Know SODIMM, swollen battery handling, NFC vs Bluetooth range, BYOD selective wipe.
- **Networking (23%)** - Ports cold, Wi-Fi bands and standards, DHCP terms, private and APIPA ranges.
- **Hardware (25%)** - RAID and cable tables, UEFI settings, PSU voltages, laser steps.
- **Virtualization and Cloud (11%)** - Type 1 vs Type 2, containers vs VMs, IaaS/PaaS/SaaS, elasticity.
- **HW and Network Troubleshooting (28%)** - Learn symptom-to-cause pairs. This is where Core 1 is won or lost.

### Core 2
- **Operating Systems (28%)** - Every .msc and command by name. Editions. GPT vs MBR. macOS and Linux tools.
- **Security (28%)** - Malware removal order, NTFS vs share, WPA3, destruction methods, SOHO settings.
- **Software Troubleshooting (23%)** - The repair ladder. Safe Mode, System Restore, sfc.
- **Operational Procedures (21%)** - Backup types, change types, safety, professionalism, script extensions, remote access, AI terms.

## Important Acronyms to Memorize

### Hardware and Networking
- **APIPA** - Automatic Private IP Addressing
- **DHCP** - Dynamic Host Configuration Protocol
- **ONT** - Optical Network Terminal
- **PoE** - Power over Ethernet
- **SODIMM** - Small Outline Dual In-line Memory Module
- **NVMe** - Non-volatile Memory Express
- **TPM / HSM** - Trusted Platform Module / Hardware Security Module
- **UEFI** - Unified Extensible Firmware Interface

### Security and Operations
- **MDM** - Mobile Device Management
- **EDR / MDR / XDR** - Endpoint / Managed / Extended Detection and Response
- **SAE** - Simultaneous Authentication of Equals (WPA3)
- **MSDS** - Material Safety Data Sheet
- **CMDB** - Configuration Management Database
- **RMM** - Remote Monitoring and Management
- **SPICE** - Simple Protocol for Independent Computing Environments
- **GFS** - Grandfather-Father-Son

Download the acronym list at the end of each objectives PDF and review it the week before each exam.

## Pre-Exam Checklist

### One Week Before
- [ ] Two full practice exams at 85%+
- [ ] Every table in the [fact sheet](fact-sheet.md) from memory
- [ ] Acronym list reviewed
- [ ] Testing center or online proctoring requirements confirmed

### Day Before
- [ ] Light review only
- [ ] ID ready, check-in time confirmed
- [ ] For online testing: run the system test, clear the desk, close other apps
- [ ] Sleep

### Exam Day
- [ ] Arrive or log in 30 minutes early
- [ ] Skip PBQs first, come back to them
- [ ] Watch the qualifiers: BEST, FIRST, MOST likely
- [ ] Use every minute, review flagged questions

## Related Pages

- [README](README.md) - Exam overview
- [Practice Plan](practice-plan.md) - The 10-week schedule
- [Scenarios](scenarios.md) - Worked help desk cases
- [Network+](../network-plus/README.md) - The next certification
