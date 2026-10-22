---
last-updated: 2026-10-22
difficulty: beginner
---

# Linux Foundation Certified System Administrator (LFCS) - Practice Questions

30 questions for LFCS prep, weighted toward essential commands (20%) and service configuration (20%), with users, running systems, networking, and storage at 15% each.

LFCS is performance-based on a live system. These reinforce which tool to reach for and why.

> **Cert page:** [exams/linux-foundation/lfcs/](../../exams/linux-foundation/lfcs/)

---

### Question 1
**Scenario:** A directory must let any user create files but only allow the file's owner to delete their own file.

A. `chmod 1777 /shared` (sticky bit)
B. `chmod 2775 /shared` (setgid), so new files inherit the group and group members can manage them
C. `chmod 777 /shared`, giving read, write, and execute on the directory to owner, group, and others
D. `chattr +i /shared`, which sets the immutable flag so that nothing in the directory can be changed

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The sticky bit on a directory restricts deletion and renaming to the file's owner, the directory's owner, or root. This is exactly how `/tmp` works. Plain 777 lets anyone delete anyone's file. Setgid makes new files inherit the directory's group, which is a different requirement. `chattr +i` makes something immutable.
</details>

---

### Question 2
**Scenario:** A service should start automatically at boot and start now.

A. `systemctl status nginx`
B. `systemctl enable --now nginx`, which enables the unit at boot and starts it
C. `systemctl start nginx`, which keeps the unit enabled
D. `service nginx restart`, which stops and starts the daemon and also enables it for the next boot

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `enable` creates the symlink that makes it start at boot, `start` runs it right now, and `--now` does both in one command. `start` alone does not survive a reboot, which is the classic exam trap where the grader reboots the machine.
</details>

---

### Question 3
**Scenario:** You need to find which process is listening on TCP port 8080.

A. `top`, sorted by network usage, to see which process is bound to the port
B. `ps aux | grep 8080`, which searches each process's command line for the port number
C. `ss -tlnp | grep 8080`, which lists listening TCP sockets with numeric ports and the owning process
D. `df -h`, which lists mounted filesystems and the processes that have files open on them

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `ss` lists sockets, and `-tlnp` gives TCP, listening only, numeric ports, with the owning process (which needs root to show for other users' processes). `ps | grep` finds a port only if it happens to be on the command line. `top` shows resource use and `df` shows disk.
</details>

---

### Question 4
**Scenario:** A logical volume must be extended by 5 GB and its ext4 filesystem grown to match, online.

A. `pvcreate` on the logical volume, then `mount -o remount` to make the kernel see the extra 5 GB
B. `lvextend -L +5G /dev/vg/lv` then `resize2fs /dev/vg/lv`
C. `fdisk` to delete and recreate the partition, then reboot so that the filesystem grows by itself
D. `mkfs.ext4` on the volume, which formats it at the new size and brings the old files back from the journal

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** LVM grows the block device and the filesystem is grown separately, which is why `lvextend -r` (or `--resizefs`) exists as a shortcut. `resize2fs` handles ext2/3/4 online; XFS uses `xfs_growfs` and cannot shrink at all. `mkfs` would destroy the data.
</details>

---

### Question 5
**Scenario:** A user should run one specific command as root without a password.

A. `chmod u+s /usr/bin/systemctl`, so the binary runs as root for every user who calls it
B. Add them to the `wheel` group, which grants sudo rights for all commands after a password prompt
C. Give them the root password and ask them to use it only for that one command
D. Add a sudoers rule with `visudo` limited to one command: `alice ALL=(root) NOPASSWD: /usr/bin/systemctl restart nginx`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A targeted sudoers entry grants exactly one command. Use `visudo` because it validates syntax before saving, and a broken sudoers file can lock you out. Group membership grants far more. Setting setuid on `systemctl` would let anyone control every service, which is a serious hole.
</details>

---

### Question 6
**Scenario:** A filesystem must mount automatically at boot and survive device renaming.

A. Add `mount` to `.bashrc`
B. Add an `/etc/fstab` entry using `/dev/sdb1`, the device name that the kernel assigns today
C. Mount it by hand after every boot, using the same command each time
D. Add an `/etc/fstab` entry using `UUID=`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Device names such as `/dev/sdb1` can change when hardware is added or the kernel enumerates differently, so UUID (or LABEL) is the stable identifier. Always test with `mount -a` before rebooting, because a bad fstab entry can drop the system into emergency mode.
</details>

---

### Question 7
**Scenario:** You need the last 50 lines of the systemd journal for a unit, following new output.

A. `journalctl -u nginx -n 50 -f`
B. `dmesg`
C. `systemctl status nginx`, which prints the unit's state together with its most recent log lines
D. `tail -f /var/log/messages`, which follows the traditional syslog file for every service on the host machine

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `journalctl -u` filters to a unit, `-n 50` sets the line count, and `-f` follows. `systemctl status` shows only the last handful of lines. `dmesg` is the kernel ring buffer, and a plain text log may not exist on a journald-only system.
</details>

---

### Question 8
**Scenario:** Replace every occurrence of `old.example.com` with `new.example.com` in a config file, keeping a backup.

A. `sed -i.bak 's/old\.example\.com/new.example.com/g' file.conf`
B. `grep -r old.example.com`, which searches every file under the directory for the old name and rewrites each match
C. `awk '{print $1}' file.conf`, which prints the first field of each line to the terminal
D. `tr old new < file.conf`, which swaps each character in the first set for the one in the second set

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `sed -i.bak` edits in place and writes the original to `file.conf.bak`. Escaping the dots matters because an unescaped `.` matches any character. `grep` only finds, `awk '{print $1}'` prints a field, and `tr` translates characters one for one rather than strings.
</details>

---

### Question 9
**Scenario:** SSH password authentication must be disabled so only keys work.

A. Set `PermitRootLogin no` in `/etc/ssh/sshd_config` and reload sshd, which blocks every password login on the host
B. Set `PermitEmptyPasswords no` in `/etc/ssh/sshd_config` and restart the server
C. Set `PasswordAuthentication no` in `/etc/ssh/sshd_config` and reload sshd
D. Change the SSH port in `sshd_config` to a high number, so password logins are no longer reachable

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** That directive is the control, and the change takes effect on `systemctl reload sshd`. Confirm you can log in with a key from a second session before closing the first, because locking yourself out of a remote box is unrecoverable without console access. Changing the port is obscurity, and `PermitRootLogin` covers only root.
</details>

---

### Question 10
**Scenario:** A job must run at 02:30 every weekday.

A. `* * 2 30 1-5`
B. `30 2 * * 0-4`, Monday as day 0
C. `30 2 * * 1-5` in a crontab, minute first and hour second
D. `2 30 * * 1-5`, which reads the hour first and the minute second on Monday to Friday

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cron fields are minute, hour, day of month, month, day of week, in that order, so 02:30 is `30 2`. Day of week runs 0-7 with both 0 and 7 meaning Sunday, so Monday to Friday is `1-5`. Option B would be Sunday to Thursday.
</details>

---

### Question 11
**Scenario:** A process is consuming CPU and must be stopped gracefully first, forcibly only if it ignores that.

A. `renice`, raising the niceness to 19 so that the process gives up CPU time to everything else and then waits
B. `kill -HUP <pid>`, a clean shutdown
C. `kill -9` immediately
D. `kill <pid>` (SIGTERM), then `kill -9 <pid>` if it does not exit

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** SIGTERM is catchable, so the process can flush buffers and clean up. SIGKILL cannot be caught and risks corrupt state or orphaned files, so it is the escalation, not the opener. SIGHUP usually means "reload config" for daemons. `renice` changes priority without stopping anything.
</details>

---

### Question 12
**Scenario:** A firewall must permit inbound HTTPS permanently on a firewalld system.

A. `iptables -A INPUT -p tcp --dport 443 -j ACCEPT`, which opens the port directly in the netfilter table and bypasses firewalld
B. `firewall-cmd --permanent --add-service=https` then `firewall-cmd --reload`
C. `systemctl stop firewalld`
D. `firewall-cmd --add-service=https` only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Without `--permanent` the rule is lost on reload or reboot, and `--permanent` alone does not affect the running configuration until you reload. Raw iptables rules are also not persistent by default on a firewalld system and can conflict with it. Stopping the firewall is not a fix.
</details>

---

### Question 13
**Scenario:** You must give a group read and write access to a directory tree without changing individual ownership everywhere.

A. `chgrp -R devs /srv/app && chmod -R g+rw /srv/app && chmod g+s /srv/app`, so new files inherit the `devs` group
B. `umask 000` set in `/etc/profile`, so new files created by anybody are read-write for every user
C. `chown -R root /srv/app` so the files have a single owner and the group can reach them through root
D. `chmod -R 777 /srv/app`, giving full access to the group and to everyone else

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Setting the group, granting group rw, and adding setgid to the directory means new files inherit the `devs` group so the arrangement keeps working. 777 grants everyone including other users. Changing owner to root does not help the group. A global `umask 000` weakens permissions system-wide.
</details>

---

### Question 14
**Scenario:** The system boots but one service failed. You need a list of failed units.

A. `journalctl -b`
B. `ls /etc/systemd/system/*.service`
C. `systemctl --failed`
D. `systemctl list-units --all`

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `systemctl --failed` gives exactly the failed units in one line each, which is the fastest first step. `journalctl -b` shows the whole boot log and is the natural follow-up once you know which unit to investigate. Listing all units or the unit directory buries the signal.
</details>

---

### Question 15
**Scenario:** An NFS export must be available to a subnet with read and write access.

A. `chmod 777 /srv/share` so every client can read and write
B. Add `/srv/share 10.0.0.0/24(rw,sync,no_subtree_check)` to `/etc/exports`, then run `exportfs -ra`
C. Start Samba with `systemctl start smb` and define a `[share]` section for the path in `smb.conf`, so clients can mount it
D. Add it to `/etc/fstab` on the server with the `rw` option so that the subnet can mount it at boot, after a reboot

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `/etc/exports` defines what the server offers and to whom, and `exportfs -ra` re-reads it without a restart. `/etc/fstab` is the client side. Samba is SMB rather than NFS. Loosening permissions does not export anything, and the firewall plus `nfs-server` service still need to be in place.
</details>

---

### Question 16
**Scenario:** Disk space is running out. You need every regular file under `/var` larger than 100 MB that was modified in the last 7 days.

A. `find /var -type f -size -100M -mtime +7`
B. `find /var -type f -size +100M -mtime -7`
C. `du -sh /var/* | sort -h | tail -7`
D. `ls -lR /var | grep 100M`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** In `find`, `+100M` means larger than 100 MiB and `-mtime -7` means modified less than 7 days ago. Flipping the signs, as in the other `find` command, selects small files older than a week. `du | sort` ranks directories by total size but ignores modification time, and grepping `ls` output for "100M" matches text, not sizes.

**Key Concept:** [find(1) manual page](https://man7.org/linux/man-pages/man1/find.1.html)
</details>

---

### Question 17
**Scenario:** Before an upgrade, `/etc` must be saved as a single gzip-compressed archive named `etc-backup.tar.gz`.

A. `tar -xzf etc-backup.tar.gz /etc`
B. `gzip -r /etc > etc-backup.tar.gz`
C. `tar -tzf etc-backup.tar.gz /etc`
D. `tar -czf etc-backup.tar.gz /etc`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `-c` creates an archive, `-z` filters it through gzip, and `-f` names the output file. `-x` extracts and `-t` lists the contents of an existing archive, so neither creates a backup. `gzip -r` compresses each file in place, one by one, and does not produce a tar archive.

**Key Concept:** [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html)
</details>

---

### Question 18
**Scenario:** A link is needed at `/home/app/logs` pointing to `/data/logs`, which is on a different filesystem.

A. `ln -s /data/logs /home/app/logs`
B. `ln /data/logs /home/app/logs`
C. `cp -a /data/logs /home/app/logs`
D. `mv /data/logs /home/app/logs`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A symbolic link stores a path, so it can cross filesystems and point at directories. A hard link (plain `ln`) references an inode and cannot span filesystems or, normally, link to a directory. `cp -a` makes an independent copy that drifts out of date, and `mv` relocates the data rather than linking to it.

**Key Concept:** [ln(1) manual page](https://man7.org/linux/man-pages/man1/ln.1.html)
</details>

---

### Question 19
**Scenario:** A new user `maria` was created with a temporary password. She must be forced to choose a new password the first time she logs in.

A. `usermod -L maria`
B. `chage -M 0 maria`
C. `chage -d 0 maria`
D. `userdel -f maria`

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `chage -d 0` sets the last password change date to the epoch, which marks the password as expired and forces a change at next login. `chage -M 0` sets the maximum password age to zero days, which is a policy change rather than a one-time reset. `usermod -L` locks the account, and `userdel` deletes it.

**Key Concept:** [chage(1) manual page](https://man7.org/linux/man-pages/man1/chage.1.html)
</details>

---

### Question 20
**Scenario:** User `alice` already belongs to several supplementary groups. She must be added to the `docker` group without losing any of them.

A. `usermod -G docker alice`
B. `usermod -aG docker alice`
C. `groupmod -n docker alice`
D. `useradd -G docker alice`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `-a` (append) with `-G` adds the group to her existing list. Without `-a`, `usermod -G` replaces the whole supplementary group list, silently removing her from the others. `groupmod -n` renames a group, and `useradd` fails because the user already exists.

**Key Concept:** [usermod(8) manual page](https://man7.org/linux/man-pages/man8/usermod.8.html)
</details>

---

### Question 21
**Scenario:** A server boots into a graphical desktop. It must boot to a text-only, multi-user environment by default from now on.

A. `systemctl isolate multi-user.target`
B. `systemctl enable multi-user.target`
C. `systemctl start multi-user.target`
D. `systemctl set-default multi-user.target`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `set-default` changes the `default.target` symlink, which is what the system boots into. `isolate` switches the running system to that target now but does not persist across a reboot. `start` only pulls the target in for the current boot, and `enable` is for units with an install section, not for choosing the boot target.

**Key Concept:** [systemctl manual](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html)
</details>

---

### Question 22
**Scenario:** A running report job (PID 4182) is slowing interactive users. It should keep running but get less CPU when there is contention.

A. `renice -n 10 -p 4182`
B. `renice -n -10 -p 4182`
C. `kill -STOP 4182`
D. `nice -n 10 4182`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `renice` changes the priority of a process that is already running, and a higher nice value (up to 19) means a lower scheduling priority. A negative value raises its priority, the opposite of what is wanted. `nice` only applies when starting a new command, and `SIGSTOP` pauses the job entirely instead of letting it continue.

**Key Concept:** [renice(1) manual page](https://man7.org/linux/man-pages/man1/renice.1.html)
</details>

---

### Question 23
**Scenario:** IPv4 forwarding must be enabled on a router host now and must stay enabled after reboots.

A. `echo 1 > /proc/sys/net/ipv4/ip_forward` and nothing else
B. Add `ip_forward=1` to `/etc/fstab` and run `mount -a`
C. Put `net.ipv4.ip_forward = 1` in `/etc/sysctl.d/` and run `sysctl --system`
D. Run `sysctl -w net.ipv4.ip_forward=1` and nothing else

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A file in `/etc/sysctl.d/` is applied at every boot, and `sysctl --system` loads it immediately, so both requirements are met. Writing to `/proc` or using `sysctl -w` changes only the running kernel and is lost at reboot. `/etc/fstab` describes filesystems to mount and has nothing to do with kernel parameters.

**Key Concept:** [sysctl.d manual](https://www.freedesktop.org/software/systemd/man/latest/sysctl.d.html)
</details>

---

### Question 24
**Scenario:** On a NetworkManager host, connection `ens3` must use static address 10.0.0.20/24 with gateway 10.0.0.1, persistently.

A. `ip addr add 10.0.0.20/24 dev ens3` and `ip route add default via 10.0.0.1`, applied directly to the live kernel tables
B. `nmcli con mod ens3 ipv4.method manual ipv4.addresses 10.0.0.20/24 ipv4.gateway 10.0.0.1`, then `nmcli con up ens3`
C. `ifconfig ens3 10.0.0.20 netmask 255.255.255.0` and add the gateway in `/etc/hosts`
D. `hostnamectl set-hostname 10.0.0.20` and restart NetworkManager

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `nmcli con mod` writes the settings into the saved connection profile, and `con up` reactivates it so they take effect now. The `ip` commands work immediately but are lost at reboot or when NetworkManager reapplies the profile. `/etc/hosts` maps names to addresses and never holds a gateway, and `hostnamectl` sets the hostname, not an address.

**Key Concept:** [nmcli reference](https://networkmanager.dev/docs/api/latest/nmcli.html)
</details>

---

### Question 25
**Scenario:** Users report that `app.internal` does not resolve. You need to query the internal DNS server at 10.0.0.53 directly for that name, bypassing the local resolver configuration.

A. `ping -c 1 app.internal`
B. `host -l app.internal`
C. `cat /etc/resolv.conf | grep app.internal`
D. `dig @10.0.0.53 app.internal`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `dig @server name` sends the query straight to the named server and shows its full answer, which isolates whether that server or the client configuration is at fault. `ping` goes through the normal resolver and mixes in reachability. `host -l` requests a zone transfer, and `resolv.conf` lists resolvers but holds no records.

**Key Concept:** [BIND 9 manual pages: dig](https://bind9.readthedocs.io/en/latest/manpages.html)
</details>

---

### Question 26
**Scenario:** A host with no spare partitions needs 2 GB of extra swap, active now and after reboot.

A. Create the file with `fallocate`, `chmod 600`, `mkswap`, `swapon`, and add an `/etc/fstab` entry
B. Create the file with `fallocate`, format it with `mkfs.ext4`, mount it at `/swap`, and add that mount to `/etc/fstab`
C. Run `swapon -a` so the kernel creates any missing swap space
D. Create the file with `fallocate` and run `swapon` on it immediately

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A swap file must be secured, formatted as swap with `mkswap`, activated with `swapon`, and listed in `/etc/fstab` to survive reboot. Skipping `mkswap` makes `swapon` fail because the file has no swap signature. Formatting it as ext4 makes a filesystem, not swap, and `swapon -a` only enables swap already listed in fstab.

**Key Concept:** [mkswap(8) manual page](https://man7.org/linux/man-pages/man8/mkswap.8.html)
</details>

---

### Question 27
**Scenario:** `umount /mnt/data` fails with "target is busy". You need to identify which processes are holding the filesystem open.

A. `df -h /mnt/data`
B. `mount | grep /mnt/data`
C. `fuser -vm /mnt/data`
D. `blkid /mnt/data`

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `fuser -m` reports every process using the mounted filesystem, and `-v` shows the user, PID, and access type so you can stop the right one (`lsof` on the mount point works too). `df` shows space usage, `mount` confirms the filesystem is mounted, and `blkid` prints device attributes such as UUID and type.

**Key Concept:** [fuser(1) manual page](https://man7.org/linux/man-pages/man1/fuser.1.html)
</details>

---

### Question 28
**Scenario:** You edited an nginx site configuration and want to confirm the syntax is valid before reloading, so a typo does not take the site down.

A. `systemctl restart nginx`
B. `nginx -t`
C. `nginx -s stop`
D. `journalctl -u nginx`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `nginx -t` parses the configuration and reports errors without changing the running server, so you reload only after it passes. Restarting with a broken file can leave the service down. `nginx -s stop` shuts the server off, and the journal shows past errors but does not test new configuration.

**Key Concept:** [nginx command-line parameters](https://nginx.org/en/docs/switches.html)
</details>

---

### Question 29
**Scenario:** A systemd-based server's clock has drifted, breaking TLS and log correlation. Network time synchronization must be turned on.

A. `timedatectl set-ntp true`
B. `date -s "12:00"` once a day by cron
C. `hwclock --systohc` after every boot
D. `timedatectl set-timezone UTC`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `timedatectl set-ntp true` enables the configured NTP client (systemd-timesyncd or chrony) so the clock is continuously disciplined. Setting the time by hand with `date` drifts again between runs. `hwclock --systohc` copies the already-wrong system time to the hardware clock, and the time zone does not fix drift.

**Key Concept:** [timedatectl manual](https://www.freedesktop.org/software/systemd/man/latest/timedatectl.html)
</details>

---

### Question 30
**Scenario:** An application listens on 127.0.0.1:3000. nginx must accept requests on port 80 and forward them to it.

A. A `return 301 http://127.0.0.1:3000;` line in the server block
B. A `root /var/www/127.0.0.1:3000;` line in the server block
C. A `listen 3000;` line added to the existing server block
D. A `proxy_pass http://127.0.0.1:3000;` line in a location block

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `proxy_pass` makes nginx act as a reverse proxy, forwarding each request to the backend and relaying its response. A `return 301` sends the browser a redirect to a loopback address it cannot reach. `root` serves static files from a directory, and `listen 3000` would make nginx compete with the application for its own port.

**Key Concept:** [nginx ngx_http_proxy_module](https://nginx.org/en/docs/http/ngx_http_proxy_module.html)
</details>

---

## Where to go deeper

- [LFCS cert page](../../exams/linux-foundation/lfcs/) - notes, practice plan, strategy
- [LFCA practice questions](./linux-foundation-lfca.md) - the entry-level sibling
- [File permissions](../../learn/day-one/file-permissions.md) - plain-English primer
- [Reading error messages](../../learn/day-one/reading-error-messages.md) - useful under exam pressure
- **[📖 LFCS exam page](https://training.linuxfoundation.org/certification/linux-foundation-certified-sysadmin-lfcs/)** - official domains and logistics
