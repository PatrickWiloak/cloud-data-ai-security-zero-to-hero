---
last-updated: 2026-08-09
difficulty: beginner
---

# Linux Foundation Certified System Administrator (LFCS) - Practice Questions

15 questions for LFCS prep, weighted toward essential commands (20%) and service configuration (20%), with users, running systems, networking, and storage at 15% each.

LFCS is performance-based on a live system. These reinforce which tool to reach for and why.

> **Cert page:** [exams/linux-foundation/lfcs/](../../exams/linux-foundation/lfcs/)

---

### Question 1
**Scenario:** A directory must let any user create files but only allow the file's owner to delete their own file.

A. `chmod 777 /shared`
B. `chmod 1777 /shared` (sticky bit)
C. `chmod 2775 /shared` (setgid)
D. `chattr +i /shared`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The sticky bit on a directory restricts deletion and renaming to the file's owner, the directory's owner, or root. This is exactly how `/tmp` works. Plain 777 lets anyone delete anyone's file. Setgid makes new files inherit the directory's group, which is a different requirement. `chattr +i` makes something immutable.
</details>

---

### Question 2
**Scenario:** A service should start automatically at boot and start now.

A. `systemctl enable --now nginx`
B. `systemctl start nginx`
C. `systemctl status nginx`
D. `service nginx restart`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `enable` creates the symlink that makes it start at boot, `start` runs it right now, and `--now` does both in one command. `start` alone does not survive a reboot, which is the classic exam trap where the grader reboots the machine.
</details>

---

### Question 3
**Scenario:** You need to find which process is listening on TCP port 8080.

A. `ps aux | grep 8080`
B. `ss -tlnp | grep 8080`
C. `top`
D. `df -h`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `ss` lists sockets, and `-tlnp` gives TCP, listening only, numeric ports, with the owning process (which needs root to show for other users' processes). `ps | grep` finds a port only if it happens to be on the command line. `top` shows resource use and `df` shows disk.
</details>

---

### Question 4
**Scenario:** A logical volume must be extended by 5 GB and its ext4 filesystem grown to match, online.

A. `lvextend -L +5G /dev/vg/lv` then `resize2fs /dev/vg/lv`
B. `fdisk` then reboot
C. `mkfs.ext4` on the volume
D. `pvcreate` then `mount -o remount`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** LVM grows the block device and the filesystem is grown separately, which is why `lvextend -r` (or `--resizefs`) exists as a shortcut. `resize2fs` handles ext2/3/4 online; XFS uses `xfs_growfs` and cannot shrink at all. `mkfs` would destroy the data.
</details>

---

### Question 5
**Scenario:** A user should run one specific command as root without a password.

A. Add them to the `wheel` group
B. Add a sudoers rule via `visudo`: `alice ALL=(root) NOPASSWD: /usr/bin/systemctl restart nginx`
C. Give them the root password
D. `chmod u+s /usr/bin/systemctl`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A targeted sudoers entry grants exactly one command. Use `visudo` because it validates syntax before saving, and a broken sudoers file can lock you out. Group membership grants far more. Setting setuid on `systemctl` would let anyone control every service, which is a serious hole.
</details>

---

### Question 6
**Scenario:** A filesystem must mount automatically at boot and survive device renaming.

A. Add an `/etc/fstab` entry using `UUID=`
B. Add an `/etc/fstab` entry using `/dev/sdb1`
C. Add a `mount` command to `.bashrc`
D. Mount it manually after each boot

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Device names such as `/dev/sdb1` can change when hardware is added or the kernel enumerates differently, so UUID (or LABEL) is the stable identifier. Always test with `mount -a` before rebooting, because a bad fstab entry can drop the system into emergency mode.
</details>

---

### Question 7
**Scenario:** You need the last 50 lines of the systemd journal for a unit, following new output.

A. `journalctl -u nginx -n 50 -f`
B. `tail -f /var/log/messages`
C. `dmesg`
D. `systemctl status nginx`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `journalctl -u` filters to a unit, `-n 50` sets the line count, and `-f` follows. `systemctl status` shows only the last handful of lines. `dmesg` is the kernel ring buffer, and a plain text log may not exist on a journald-only system.
</details>

---

### Question 8
**Scenario:** Replace every occurrence of `old.example.com` with `new.example.com` in a config file, keeping a backup.

A. `sed -i.bak 's/old\.example\.com/new.example.com/g' file.conf`
B. `grep -r old.example.com`
C. `awk '{print $1}' file.conf`
D. `tr old new < file.conf`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `sed -i.bak` edits in place and writes the original to `file.conf.bak`. Escaping the dots matters because an unescaped `.` matches any character. `grep` only finds, `awk '{print $1}'` prints a field, and `tr` translates characters one for one rather than strings.
</details>

---

### Question 9
**Scenario:** SSH password authentication must be disabled so only keys work.

A. Set `PasswordAuthentication no` in `/etc/ssh/sshd_config` and reload sshd
B. Delete all user passwords
C. Change the SSH port
D. Set `PermitRootLogin no`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** That directive is the control, and the change takes effect on `systemctl reload sshd`. Confirm you can log in with a key from a second session before closing the first, because locking yourself out of a remote box is unrecoverable without console access. Changing the port is obscurity, and `PermitRootLogin` covers only root.
</details>

---

### Question 10
**Scenario:** A job must run at 02:30 every weekday.

A. `30 2 * * 1-5` in a crontab
B. `2 30 * * 1-5`
C. `30 2 * * 0-4`
D. `* * 2 30 1-5`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cron fields are minute, hour, day of month, month, day of week, in that order, so 02:30 is `30 2`. Day of week runs 0-7 with both 0 and 7 meaning Sunday, so Monday to Friday is `1-5`. Option C would be Sunday to Thursday.
</details>

---

### Question 11
**Scenario:** A process is consuming CPU and must be stopped gracefully first, forcibly only if it ignores that.

A. `kill -9` immediately
B. `kill <pid>` (SIGTERM), then `kill -9 <pid>` if it does not exit
C. `kill -HUP <pid>`
D. `renice`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SIGTERM is catchable, so the process can flush buffers and clean up. SIGKILL cannot be caught and risks corrupt state or orphaned files, so it is the escalation, not the opener. SIGHUP usually means "reload config" for daemons. `renice` changes priority without stopping anything.
</details>

---

### Question 12
**Scenario:** A firewall must permit inbound HTTPS permanently on a firewalld system.

A. `firewall-cmd --add-service=https` only
B. `firewall-cmd --permanent --add-service=https` then `firewall-cmd --reload`
C. `iptables -A INPUT -p tcp --dport 443 -j ACCEPT`
D. `systemctl stop firewalld`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Without `--permanent` the rule is lost on reload or reboot, and `--permanent` alone does not affect the running configuration until you reload. Raw iptables rules are also not persistent by default on a firewalld system and can conflict with it. Stopping the firewall is not a fix.
</details>

---

### Question 13
**Scenario:** You must give a group read and write access to a directory tree without changing individual ownership everywhere.

A. `chgrp -R devs /srv/app && chmod -R g+rw /srv/app && chmod g+s /srv/app`
B. `chmod -R 777 /srv/app`
C. `chown -R root /srv/app`
D. `umask 000`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Setting the group, granting group rw, and adding setgid to the directory means new files inherit the `devs` group so the arrangement keeps working. 777 grants everyone including other users. Changing owner to root does not help the group. A global `umask 000` weakens permissions system-wide.
</details>

---

### Question 14
**Scenario:** The system boots but one service failed. You need a list of failed units.

A. `systemctl --failed`
B. `systemctl list-units --all`
C. `ls /etc/systemd/system`
D. `journalctl -b`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `systemctl --failed` gives exactly the failed units in one line each, which is the fastest first step. `journalctl -b` shows the whole boot log and is the natural follow-up once you know which unit to investigate. Listing all units or the unit directory buries the signal.
</details>

---

### Question 15
**Scenario:** An NFS export must be available to a subnet with read and write access.

A. Add `/srv/share 10.0.0.0/24(rw,sync,no_subtree_check)` to `/etc/exports` and run `exportfs -ra`
B. Add it to `/etc/fstab`
C. Start Samba
D. `chmod 777 /srv/share`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `/etc/exports` defines what the server offers and to whom, and `exportfs -ra` re-reads it without a restart. `/etc/fstab` is the client side. Samba is SMB rather than NFS. Loosening permissions does not export anything, and the firewall plus `nfs-server` service still need to be in place.
</details>

---

## Where to go deeper

- [LFCS cert page](../../exams/linux-foundation/lfcs/) - notes, practice plan, strategy
- [LFCA practice questions](./linux-foundation-lfca.md) - the entry-level sibling
- [File permissions](../../learn/day-one/file-permissions.md) - plain-English primer
- [Reading error messages](../../learn/day-one/reading-error-messages.md) - useful under exam pressure
- **[📖 LFCS exam page](https://training.linuxfoundation.org/certification/linux-foundation-certified-sysadmin-lfcs/)** - official domains and logistics
