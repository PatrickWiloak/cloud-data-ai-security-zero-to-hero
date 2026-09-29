---
last-updated: 2026-09-28
difficulty: beginner
---

# CompTIA A+ (220-1201 and 220-1202) - Practice Questions

20 original scenario questions for A+ prep. Questions 1-10 cover Core 1 (mobile devices, networking, hardware, virtualization and cloud, hardware and network troubleshooting). Questions 11-20 cover Core 2 (operating systems, security, software troubleshooting, operational procedures).

> **Cert page:** [exams/comptia/a-plus/](../../exams/comptia/a-plus/)

---

### Question 1
**Scenario:** A user replaced their laptop's display assembly at a repair shop. Since then, Wi-Fi signal is very weak even next to the access point, but a USB Wi-Fi adapter works fine.

A. Replace the wireless card
B. Check that the Wi-Fi antenna leads in the display lid were reconnected to the wireless card
C. Update the wireless driver
D. Change the router to 2.4 GHz

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Laptop Wi-Fi antennas run through the display lid, so a screen replacement is the classic moment for a lead to be left unplugged or pinched. The timing points to the repair, not the card or driver. A USB adapter working proves the network itself is fine.
</details>

---

### Question 2
**Scenario:** A company lets staff read work email on personal phones. When someone leaves, IT must remove company data without touching personal photos.

A. Full remote wipe through MDM
B. MDM with a work profile or container and a selective wipe
C. Ask the employee to delete the mail app
D. Disable the user's cellular data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** BYOD management separates business apps and data into a managed container or work profile. A selective wipe removes only that container. A full wipe would destroy personal data on a device the company does not own, and asking the user relies on trust rather than control.
</details>

---

### Question 3
**Scenario:** A user wants to read the same mailbox on a phone, a laptop, and a tablet, with read status and folders staying in sync.

A. POP3 on port 110
B. IMAP on port 143 (or IMAPS on 993)
C. SMTP on port 25
D. LDAP on port 389

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** IMAP keeps mail on the server and syncs state to every client. POP3 downloads messages and usually removes them from the server, so other devices miss them. SMTP sends mail between servers, and LDAP queries directories.
</details>

---

### Question 4
**Scenario:** Several PCs on one floor suddenly cannot browse the web. `ipconfig` shows addresses in the 169.254.0.0/16 range and no default gateway.

A. The DNS server is down
B. The PCs cannot reach a DHCP server
C. The proxy settings are wrong
D. The NIC drivers are corrupt on every PC

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A 169.254.x.x address is APIPA, which Windows assigns itself when no DHCP server answers. Because it affects a whole floor, check the DHCP server, its scope, or the switch and VLAN serving that floor. A DNS failure would leave a valid IP address in place.
</details>

---

### Question 5
**Scenario:** A new access point must be mounted on a warehouse ceiling 60 m from the network closet. There is no power outlet at the mounting point, and the cable will run through an air-handling space.

A. Cat 5 UTP and an extension cord
B. Plenum-rated Cat 6 with PoE from the switch or an injector
C. Multimode fiber with a power adapter
D. Direct burial Cat 6a

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Air-handling spaces require plenum-rated cable for fire safety, 60 m is within copper's 100 m limit, and PoE delivers power over the same cable. Fiber carries no power, and direct burial cable is for underground runs, not plenum spaces.
</details>

---

### Question 6
**Scenario:** A small office wants a NAS with four drives. It must keep working if any two drives fail at the same time.

A. RAID 0
B. RAID 1
C. RAID 5
D. RAID 6

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** RAID 6 uses double parity and survives any two drive failures, with at least four drives. RAID 5 survives only one. RAID 0 has no redundancy at all. RAID 10 would also use four drives, but it survives two failures only if they are in different mirror pairs, not any two.
</details>

---

### Question 7
**Scenario:** A technician tries to create a 64-bit virtual machine in a Type 2 hypervisor on a new desktop. The hypervisor reports that hardware virtualization is unavailable.

A. Install more RAM
B. Enable Intel VT-x or AMD-V in the UEFI settings
C. Switch to a Type 1 hypervisor
D. Convert the disk from MBR to GPT

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hardware virtualization support is often disabled by default in firmware. Enabling it in UEFI is the fix. Changing the hypervisor type does not help, because both types need the CPU feature, and neither RAM nor the partition style affects this error.
</details>

---

### Question 8
**Scenario:** A startup wants to deploy its web application without managing operating systems, patches, or runtime versions. It only wants to upload code.

A. IaaS
B. PaaS
C. SaaS
D. Private cloud

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PaaS provides the OS and runtime, and the customer supplies the application and data. IaaS would leave the team patching VMs. SaaS is a finished application that the customer uses, not a platform for their own code. Private cloud is a deployment model, not a service model.
</details>

---

### Question 9
**Scenario:** An office desktop loses the correct date and time whenever it is unplugged overnight. Several websites then show certificate warnings.

A. Replace the power supply
B. Replace the CMOS battery
C. Reinstall Windows
D. Replace the network card

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The coin-cell CMOS battery keeps the real-time clock running without mains power. When it dies, the clock resets. A clock far in the past or future makes valid certificates appear expired or not yet valid, which explains the browser warnings.
</details>

---

### Question 10
**Scenario:** Pages from a laser printer show toner that smears and rubs off when touched.

A. Low toner
B. A failing fuser assembly
C. Wrong printer driver
D. A worn pickup roller

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The fuser uses heat and pressure to bond toner to the paper. If it fails, toner sits loose on the page and smears. Low toner causes faded prints, a wrong driver causes garbled output, and worn pickup rollers cause feeding problems.
</details>

---

### Question 11
**Scenario:** A technician needs to copy a 7 GB video file to a USB flash drive that must work on both Windows and macOS. The copy fails with "file too large."

A. Reformat the drive as NTFS
B. Reformat the drive as exFAT
C. Reformat the drive as APFS
D. Compress the file

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The drive is almost certainly FAT32, which has a 4 GB maximum file size. exFAT removes that limit and is read-write on both Windows and macOS. macOS cannot write NTFS by default, and Windows cannot read APFS without extra software.
</details>

---

### Question 12
**Scenario:** A domain user's newly assigned drive mappings and desktop settings have not appeared, although other users in the same OU have them. The technician wants to apply the policy immediately and then confirm which policies applied.

A. `sfc /scannow`, then `chkdsk`
B. `gpupdate /force`, then `gpresult /r`
C. `ipconfig /renew`, then `nslookup`
D. `net user`, then `whoami`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `gpupdate /force` reapplies all Group Policy settings, and `gpresult /r` reports which policies applied to the user and computer. The other commands repair files, check disks, or deal with networking and accounts, not policy.
</details>

---

### Question 13
**Scenario:** A Linux administrator must let the owner read, write, and execute a script, while the group and everyone else can only read and execute it.

A. `chmod 777 script.sh`
B. `chmod 755 script.sh`
C. `chown 755 script.sh`
D. `chmod 644 script.sh`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Read is 4, write is 2, and execute is 1. Owner rwx is 7, and group and others r-x is 5 each, so 755. 777 gives everyone write access, 644 removes execute, and `chown` changes ownership rather than permissions.
</details>

---

### Question 14
**Scenario:** A shared folder grants Everyone "Full Control" at the share level. The NTFS permissions give the Sales group "Read." A Sales user tries to save a file to the share over the network.

A. The save succeeds because share permissions allow Full Control
B. The save fails because the most restrictive permission applies
C. The save succeeds because NTFS permissions only apply locally
D. The save fails because Everyone overrides group permissions

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Network access passes through both share and NTFS permissions, and the effective permission is the more restrictive of the two. Read beats Full Control here. NTFS permissions apply both locally and over the network.
</details>

---

### Question 15
**Scenario:** A technician has confirmed that a home user's PC shows malware symptoms and has disconnected it from the network. What should happen next in CompTIA's malware removal procedure?

A. Educate the end user
B. Disable System Restore in Windows
C. Reimage the PC
D. Schedule scans and run updates

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The order is investigate and verify, quarantine, disable System Restore, remediate (update anti-malware, scan and remove, reimage if needed), schedule scans and updates, re-enable System Restore and create a restore point, then educate the user. System Restore is disabled so infected restore points cannot bring the malware back.
</details>

---

### Question 16
**Scenario:** A clinic is retiring laptops with SSDs that held patient data. It needs a method that makes the data unrecoverable and gives auditors proof.

A. Degauss the SSDs
B. Standard format each drive
C. Use a certified vendor to shred the drives and issue a certificate of destruction
D. Delete the patient folders and empty the Recycle Bin

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Shredding destroys any media, and the certificate is the audit evidence. Degaussing works only on magnetic media, so it does nothing to SSDs. A standard format or deleting files leaves data recoverable.
</details>

---

### Question 17
**Scenario:** Right after a graphics driver update, a Windows PC shows a blue screen during every normal startup. It starts normally in Safe Mode.

A. Reinstall Windows
B. Boot into Safe Mode and roll back the driver in Device Manager
C. Replace the graphics card
D. Run `chkdsk /r`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The timing points to the driver, and Safe Mode loads only basic drivers, which is why it boots there. Rolling back the driver is the least disruptive fix that addresses the cause. Reinstalling Windows or replacing hardware is premature.
</details>

---

### Question 18
**Scenario:** A user's phone suddenly shows many full-screen ads, uses far more mobile data than usual, and the battery drains quickly. The user recently installed a flashlight app from a website link rather than the official store.

A. Replace the battery
B. Remove the sideloaded app, scan the device, and factory reset if the symptoms continue
C. Turn off location services
D. Reset network settings

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An app from an unofficial source, along with ads, high data use, and battery drain, points to adware or other malware. Remove the app first, then scan. A factory reset (after backing up data) is the fallback. The battery and network settings are symptoms, not the cause.
</details>

---

### Question 19
**Scenario:** A company runs a full backup on Sunday and differential backups Monday through Saturday. The server fails on Thursday morning.

A. Sunday's full only
B. Sunday's full plus Monday, Tuesday, and Wednesday differentials
C. Sunday's full plus Wednesday's differential
D. Wednesday's differential only

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Each differential contains every change since the last full, so only the latest differential is needed with the full. If these had been incrementals, every one since Sunday would be required, in order.
</details>

---

### Question 20
**Scenario:** A help desk technician wants to paste a user's error log, which includes the user's name, email, and an internal server password, into a free public AI chatbot to get help diagnosing it.

A. Paste it, because AI tools are accurate
B. Paste it, but ask the chatbot not to store it
C. Do not paste sensitive data into a public AI tool. Remove the personal and secret data or use an approved private AI tool, and verify any answer before acting
D. Email the log to a personal account and use the chatbot from home

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Public AI tools may keep or train on what is entered, so pasting PII and credentials is a data security and privacy failure. Organizational AI policy and approved private tools exist for this reason. AI output can also be inaccurate or hallucinated, so any suggested fix must be checked before it is used.
</details>

---

## Where to go deeper

- [A+ cert page](../../exams/comptia/a-plus/) - notes, fact sheet, practice plan, strategy, scenarios
- [Network+ practice questions](./comptia-network-plus.md) - the natural next step
- [Security+ practice questions](./comptia-security-plus.md) - the security baseline after A+
- **[📖 CompTIA A+](https://www.comptia.org/en-us/certifications/a/)** - official exam details and objectives
