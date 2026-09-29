---
last-updated: 2026-09-28
---

# CompTIA A+ (220-1201 and 220-1202) - High-Yield Scenarios and Patterns

These are original help desk scenarios written to match the style of the objectives. Each one walks through the analysis a technician should do, then the fix, then how to prevent it. They are not vendor exam questions.

## Core 1: Hardware Scenarios

### New Drive Not Showing Up
**Scenario**: A technician installs a second SSD in a desktop for extra storage. The drive appears in UEFI, but not in File Explorer.

**Analysis**:
- **Domain**: Core 1 Hardware and Troubleshooting, Core 2 OS tools
- **Clue**: UEFI sees it, so power and data cables are fine
- **Cause**: A new disk is not initialized and has no volume or drive letter

**Response**:
1. Open Disk Management (`diskmgmt.msc`)
2. Initialize the disk as GPT
3. Create a new simple volume, format NTFS, assign a drive letter

**Prevention**:
- Add "initialize and format" to the SOP for drive installs

### Laptop Clock Wrong Every Morning
**Scenario**: A user's older laptop shows the wrong date and time every time it is fully powered off. Web pages show certificate errors until the clock is fixed.

**Analysis**:
- **Clue**: Time resets after power loss
- **Cause**: The CMOS battery (coin cell) is dead
- **Side effect**: Certificates look invalid when the clock is far off

**Response**:
- Replace the CMOS battery (usually a CR2032) following the service manual
- Reset date and time in UEFI, confirm Windows time syncs with NTP

**Prevention**:
- Replace CMOS batteries during hardware refreshes of older machines

### Choosing a RAID Level
**Scenario**: A small office wants a four-drive NAS for shared files. It must survive the loss of any two drives at once, and capacity matters less than safety.

**Analysis**:
- **Requirement**: Two-drive fault tolerance, four drives
- **Options**: RAID 5 survives one failure. RAID 10 survives one per mirror pair, not any two. RAID 6 survives any two

**Response**:
- Configure **RAID 6**. Usable space is two drives' worth
- Keep a separate backup. RAID does not protect against deletion or ransomware

**Prevention**:
- Monitor drive health and replace failed drives quickly

### Ghosting on Laser Prints
**Scenario**: Every page from a department laser printer shows a faint copy of the previous image lower down the page.

**Analysis**:
- **Symptom**: Double/echo images (ghosting)
- **Cause**: The drum is not fully cleaned or discharged between rotations, or the imaging unit is worn

**Response**:
- Replace the toner/drum cartridge (or imaging unit)
- If it continues, check the cleaning blade and apply the maintenance kit

**Prevention**:
- Follow the maintenance kit schedule the printer reports

## Core 1: Networking Scenarios

### Users Cannot Get Online After a Power Cut
**Scenario**: After a power outage, several wired users in a small office report "no internet." `ipconfig` on their PCs shows addresses starting 169.254.

**Analysis**:
- **Clue**: 169.254.x.x is APIPA
- **Cause**: Clients cannot reach a DHCP server. The router or server providing DHCP may not have restarted correctly

**Response**:
1. Check the router or DHCP server is powered and running
2. Check the switch between users and the router
3. Run `ipconfig /release` then `ipconfig /renew` on a client
4. Confirm a valid address and test the gateway with `ping`

**Prevention**:
- Put network gear on a UPS so brief outages do not reboot it

### Slow and Dropping Wi-Fi
**Scenario**: Staff on the second floor complain Wi-Fi drops several times an hour. A Wi-Fi analyzer shows the office AP on 2.4 GHz channel 6 with 40 MHz width, and five neighboring networks on channels 4 to 8.

**Analysis**:
- **Cause**: Channel overlap and interference on a crowded 2.4 GHz band, made worse by a wide channel

**Response**:
- Set 2.4 GHz to 20 MHz width on channel 1 or 11 (whichever is least used)
- Steer capable clients to 5 GHz or 6 GHz
- Consider a second AP for coverage

**Prevention**:
- Survey with a Wi-Fi analyzer before and after changes

### Cable Run Through the Ceiling
**Scenario**: A contractor needs to run Ethernet above a drop ceiling that is used as an air return, to reach an access point 70 m from the switch. The AP has no power outlet nearby.

**Analysis**:
- **Clue**: Air-handling space means plenum-rated cable is required
- **Distance**: 70 m is within the 100 m limit for copper
- **Power**: No outlet means PoE

**Response**:
- Use plenum-rated Cat 6 (or Cat 6a) cable
- Power the AP from a PoE switch or a PoE injector matched to the AP's power class
- Terminate at a patch panel, test with a cable tester

**Prevention**:
- Label both ends and record the run in network documentation

## Core 2: Operating System Scenarios

### Feature Missing on a New Laptop
**Scenario**: A new hire's laptop came with Windows 11 Home. IT cannot join it to the domain, and BitLocker is missing.

**Analysis**:
- **Cause**: Home edition does not support domain join, Group Policy Editor, BitLocker, or hosting RDP

**Response**:
- Upgrade the license to Windows 11 Pro (in-place, keeps apps and files)
- Join the domain, then enable BitLocker and store the recovery key in the directory

**Prevention**:
- Specify Pro or Enterprise in procurement

### Mapped Drive Missing
**Scenario**: A user says their S: drive disappeared after a password change. Other users are fine.

**Analysis**:
- **Clue**: One user, after a password change
- **Cause**: Saved credentials for the mapped drive are stale, or the log-in script failed

**Response**:
1. Update stored credentials in Credential Manager
2. Remap with `net use S: \\fileserver\shared`
3. Run `gpupdate /force` if the drive is mapped by policy, then check `gpresult /r`

**Prevention**:
- Map drives by Group Policy using the signed-in user's credentials

### Linux Web Server Full Disk
**Scenario**: A small Linux server stops accepting uploads. Users see "no space left on device."

**Analysis**:
- **Tools**: `df -h` shows which filesystem is full. `du -sh /var/*` finds the large directories

**Response**:
- Find and rotate or remove old logs, clear package caches (`apt clean` or `dnf clean all`)
- Confirm free space with `df -h`

**Prevention**:
- Configure log rotation and disk space alerts

## Core 2: Security Scenarios

### Browser Hijack
**Scenario**: A user's browser home page changed to an unfamiliar search engine. Pop-ups appear even on trusted sites, and a new toolbar was installed with free PDF software.

**Analysis**:
- **Cause**: A PUP or adware bundled with the download, installing a browser hijacker and extension

**Response (follow the 10 steps)**:
1. Verify the symptoms
2. Quarantine the PC from the network
3. Disable System Restore (Windows Home)
4. Remove the bundled program and malicious extensions, reset the browser
5. Update anti-malware, scan in Safe Mode
6. Schedule scans, re-enable System Restore, create a restore point
7. Educate the user on trusted download sources

**Prevention**:
- Standard user accounts, application allow lists, and browser extension policies

### Files Renamed and Unreadable
**Scenario**: A user calls because their documents now have a strange extension and a text file on the desktop demands payment.

**Analysis**:
- **Cause**: Ransomware
- **Urgency**: It may be encrypting network shares right now

**Response**:
- Disconnect the PC from the network immediately (unplug the cable, turn off Wi-Fi)
- Escalate to security or management following the incident response plan
- Preserve evidence, do not wipe until told to
- Restore files from clean offline backups after the system is rebuilt

**Prevention**:
- 3-2-1 backups with one offline or immutable copy
- Least privilege on shares, EDR, user training

### Disposing of Old Drives
**Scenario**: A clinic is replacing 20 PCs. The old HDDs and SSDs held patient records.

**Analysis**:
- **Regulation**: Healthcare data, so destruction must be documented
- **Media**: Mixed HDD and SSD. Degaussing does not work on SSDs

**Response**:
- Use a certified third-party destruction vendor to shred all drives, or drill and shred in-house
- Get a certificate of destruction listing each asset tag
- Update the asset inventory

**Prevention**:
- Include disposal in the asset life cycle policy

### Securing a New SOHO Router
**Scenario**: A two-person accounting firm installs a new wireless router.

**Response**:
- Change the default admin password and disable remote administration
- Update firmware
- Set WPA3 (or WPA2-AES if older devices need it) with a long passphrase
- Change the default SSID, create a separate guest network
- Disable UPnP and WPS, and forward only needed ports

## Core 2: Operational Procedure Scenarios

### A Change That Went Wrong
**Scenario**: A technician pushes a new printer driver to all PCs at 10:00 on a Tuesday without approval. Half the PCs can no longer print.

**Analysis**:
- **Failures**: No change request, no testing, no approval, no maintenance window, no rollback plan

**Response**:
- Roll back to the previous driver
- Document the incident
- Submit the change properly: sandbox test, risk analysis, CAB approval, maintenance window, rollback plan, and end-user acceptance

**Prevention**:
- Enforce change management for every non-standard change

### Restoring After a Failure
**Scenario**: Backups run a full every Sunday and an incremental every other night. The server fails on Friday morning.

**Analysis**:
- **Incremental restore needs**: The last full plus every incremental since

**Response**:
- Restore Sunday's full, then Monday, Tuesday, Wednesday, and Thursday incrementals in order

**Prevention**:
- Consider synthetic fulls to shorten restores, and test restores regularly

### Prohibited Content Found During Repair
**Scenario**: While fixing a laptop, a technician sees files that appear to be illegal content.

**Response**:
- Stop working on the device and do not open more files
- Report to management (and law enforcement as policy requires)
- Preserve the device as-is and start a chain of custody record
- Document what was seen and when

### Frustrated Executive
**Scenario**: An executive interrupts the technician, complains the laptop has "always been useless," and demands a new one today.

**Response**:
- Stay calm, do not argue or become defensive
- Listen, then clarify with open-ended questions ("What happens when it slows down?")
- Restate the issue and set clear expectations: what you can do now, and what needs approval
- Offer repair or replacement options within policy, then follow up later

## Scenario Analysis Framework

When you meet any scenario question, run through these:

1. **Which domain is this?** It tells you which vocabulary the answer uses.
2. **What changed?** New hardware, update, password, location, or power event.
3. **What is the scope?** One user, one device, or everyone. Scope points to local vs shared causes.
4. **What is the least disruptive fix that addresses the cause?**
5. **Is there a safety, security, or legal angle?** Those override convenience every time.

### Common Exam Keywords and Their Meaning

| Keyword | Meaning |
|---------|---------|
| **FIRST** | The initial step, usually gather information or check the obvious |
| **NEXT** | The step after the one described, follow the methodology order |
| **BEST** | Several work, pick the most complete and appropriate |
| **MOST likely** | The most common cause of that symptom |
| **LEAST** | Pick the weakest, cheapest, or least disruptive option depending on context |

## Related Pages

- [Fact Sheet](fact-sheet.md) - Tables behind these answers
- [05 - Hardware and Network Troubleshooting](notes/05-hardware-network-troubleshooting.md) - Core 1 symptom tables
- [08 - Software Troubleshooting](notes/08-software-troubleshooting.md) - Core 2 symptom tables
- [Practice Questions](../../../resources/practice-questions/comptia-a-plus-220-1201-1202.md) - Test yourself
