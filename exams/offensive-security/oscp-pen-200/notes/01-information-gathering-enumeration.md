---
last-updated: 2026-07-29
---

# OSCP 01 - Information Gathering and Enumeration

The phase that decides whether the rest of the exam goes well. Most failed OSCP attempts
are enumeration failures, not exploitation failures: the path was there and the candidate
did not find it.

> This material is for authorised testing only: the OSCP exam environment, your own lab, or
> engagements with written permission. Everything below is methodology, of the kind Offensive
> Security's own course teaches.

## The governing principle

**Enumerate until you find something, then enumerate the something.** When you are stuck,
the answer is almost always that you have not enumerated thoroughly enough, not that you
need a more exotic exploit.

Keep notes as you go. The exam requires a professional report, and reconstructing what you
did hours later costs more time than recording it at the time.

## Passive information gathering

- **OSINT** - gathering from public sources without touching the target: DNS records, certificate transparency logs, job postings, and code repositories.
- **WHOIS and DNS records** - registration data, name servers, and mail servers.
- **Certificate transparency** - public CT logs frequently reveal subdomains that DNS enumeration misses.
- **Google dorking** - targeted search operators (`site:`, `filetype:`, `inurl:`) to find exposed documents and directories.

In the OSCP exam, passive gathering matters less than in a real engagement, because the
scope is given. The skill still appears in the reporting expectations.

## Active host and service discovery

- **Host discovery** - identifying live hosts in scope, typically with ICMP, ARP on a local segment, or TCP probes when ICMP is filtered.
- **Port scanning** - identifying open TCP and UDP ports. Nmap is the standard tool.
- **Service and version detection** - `-sV` identifies the software and version behind a port, which is what drives the search for known vulnerabilities.
- **OS detection** - `-O`, useful but frequently wrong; treat it as a hint.
- **Default scripts** - `-sC` runs the safe script category and often surfaces immediately useful detail.
- **Full port scan** - scanning all 65535 TCP ports. Non-standard ports host the interesting services more often than not, and skipping the full scan is a common cause of a missed path.
- **UDP scanning** - slow and unreliable, but SNMP, TFTP, and DNS live there. Scan the common UDP ports at minimum.

A workable pattern: a fast full TCP port sweep to find open ports, then a targeted
version-and-script scan against only those ports. This is much faster than a full scan with
all options enabled.

## Service-specific enumeration

The heart of the phase. For each open port, ask what the service is, what version, and what
that version allows.

- **HTTP/HTTPS (80, 443, 8080, 8443)** - the richest attack surface. Enumerate directories and files, identify the application and its version, review page source and comments, check for default credentials, and examine any login or upload functionality.
- **SMB (139, 445)** - enumerate shares, null sessions, users, and the SMB version. Misconfigured shares are a frequent entry point.
- **FTP (21)** - check for anonymous login, and whether the directory is writable and web-accessible.
- **SSH (22)** - version identification; rarely the entry point itself, but useful once you have credentials.
- **SMTP (25)** - user enumeration via VRFY and RCPT TO on older configurations.
- **DNS (53)** - attempt a zone transfer, which occasionally succeeds on lab targets.
- **SNMP (161/UDP)** - default community strings such as `public` can reveal running processes, installed software, users, and network configuration.
- **Databases (1433, 3306, 5432, 1521)** - default or weak credentials, and version-specific weaknesses.
- **RDP (3389) and WinRM (5985/5986)** - remote access once credentials are known.
- **NFS (2049)** - exported shares, sometimes with weak permissions.

## Web enumeration in more depth

Because it is where most footholds come from:

- **Directory and file discovery** - brute-forcing paths against a wordlist. Vary the extensions to match the technology (`.php`, `.aspx`, `.jsp`, `.txt`, `.bak`).
- **Virtual host discovery** - a single IP may serve several sites by hostname.
- **Technology fingerprinting** - server headers, framework signatures, cookie names, and error pages.
- **Application version** - once identified, search for known vulnerabilities in that specific version.
- **Parameters and input** - every parameter is a candidate for injection testing.
- **robots.txt, sitemap.xml, backup files, and source repositories** - frequently left exposed.

## Vulnerability identification

- **Searchsploit / Exploit-DB** - offline searchable copy of public exploits, mapped to software versions.
- **Version-to-vulnerability mapping** - the core skill: identify exact version, find whether a known issue exists, and confirm it applies to this configuration.
- **Reading exploit code before running it** - mandatory. Understand what it does, fix hard-coded addresses or ports, and never run something you have not read on a system you care about.
- **Manual verification** - a scanner claim is a hypothesis. Confirm it manually before committing time.

## Note-taking and organisation

- Keep a per-host record: open ports, service versions, findings, credentials, and what you have already tried.
- Record every credential found. Credential reuse across hosts is the single most productive lateral movement technique in lab environments.
- Screenshot as you go. The exam report requires evidence, and re-obtaining it later wastes time you will not have.

## Exam pointers

- Run a full TCP port scan on every target. Missing a high port is the most common self-inflicted failure.
- Enumerate UDP at least for the common ports.
- When stuck, go back to enumeration rather than reaching for a new exploit.
- Read every exploit before you run it.
- Credential reuse is the first thing to try after obtaining any password or hash.
- Take notes and screenshots continuously; the report is part of the exam.

## Official documentation

**[📖 OffSec PEN-200 course syllabus](https://www.offsec.com/courses/pen-200/)** - authoritative content list
**[📖 OSCP exam guide](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide)** - rules, restrictions, and reporting requirements
**[📖 Nmap reference guide](https://nmap.org/book/man.html)** - scanning options
