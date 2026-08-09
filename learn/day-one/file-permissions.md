---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 8 min
---

# Linux File Permissions

> **8-minute read. Assumes you've read [Terminal basics](./terminal-basics.md).**

## Why this page exists

Sooner or later something fails with "Permission denied", you search for it, and the internet tells you to run `chmod 777`. That makes the error go away and makes the file readable and writable by everyone on the system, which is how a surprising number of real security incidents start.

Permissions take fifteen minutes to understand properly. This is that fifteen minutes.

## Reading the output

```bash
$ ls -l
-rw-r--r--  1 alice  staff   1024 Aug  9 10:14 notes.txt
drwxr-xr-x  3 alice  staff     96 Aug  9 10:12 projects
-rwxr-xr-x  1 alice  staff   2048 Aug  9 10:10 deploy.sh
```

The first column is the interesting one. Take `-rw-r--r--` and split it:

```
-        rw-        r--        r--
type     owner      group      everyone else
```

- **Position 1** is the type: `-` is a regular file, `d` is a directory, `l` is a symbolic link.
- **Positions 2-4** are what the **owner** can do.
- **Positions 5-7** are what members of the **group** can do.
- **Positions 8-10** are what **everyone else** can do.

Each group of three is always in the order **read, write, execute**, and a dash means "not permitted".

| Letter | On a file | On a directory |
|---|---|---|
| **r** (read) | View the contents | List the names inside |
| **w** (write) | Modify the contents | Create, delete, or rename entries inside |
| **x** (execute) | Run it as a program | Enter it, and access things inside |

The directory column is the part that surprises people. **`x` on a directory means you can traverse into it.** A directory with `r` but no `x` lets you list the names and not read any of the files. A directory with `x` but no `r` lets you open a file whose exact name you already know, without being able to list what is there.

Also note: **deleting a file is a write to its directory**, not to the file. You can delete a read-only file if you can write to the folder containing it.

## Numbers

The same permissions are written as three digits, which is what `chmod` usually takes:

| Number | Meaning | Letters |
|---:|---|---|
| 4 | read | `r--` |
| 2 | write | `-w-` |
| 1 | execute | `--x` |

Add them together for each group of three:

| Digit | Letters | Means |
|---:|---|---|
| 7 | `rwx` | read, write, execute |
| 6 | `rw-` | read and write |
| 5 | `r-x` | read and execute |
| 4 | `r--` | read only |
| 0 | `---` | nothing |

So `644` is `rw-r--r--`: owner can read and write, everyone else can only read. And `755` is `rwxr-xr-x`: owner can do everything, everyone else can read and execute.

## The four you actually need

| Setting | Use for |
|---|---|
| `644` | Ordinary files: documents, source code, configuration |
| `755` | Directories, and scripts you want to run |
| `600` | Private files: credentials, private keys, anything sensitive |
| `700` | Private directories |

That covers almost everything. `chmod 600 ~/.ssh/id_ed25519` matters because SSH will refuse to use a private key that others can read, which is a good default and a useful reminder.

## Changing things

```bash
chmod 644 notes.txt          # numeric
chmod 755 deploy.sh
chmod +x deploy.sh           # symbolic: add execute for everyone
chmod u+x deploy.sh          # add execute for the user (owner) only
chmod go-w notes.txt         # remove write from group and others
chmod -R 755 projects/       # recursive, through a directory tree
```

Symbolic form uses `u` (user/owner), `g` (group), `o` (others), `a` (all), with `+` to add, `-` to remove, and `=` to set exactly.

Changing ownership requires `sudo`:

```bash
sudo chown alice notes.txt         # change owner
sudo chown alice:staff notes.txt   # change owner and group
sudo chgrp staff notes.txt         # change group only
```

## Why not 777

`chmod 777` grants read, write, and execute to **every user on the system**. On your own laptop that mostly means you have stopped getting a useful error. On a shared server, a container image, or anything internet-facing, it means any process running as any user can modify that file, including replacing a script that something else runs.

When you hit "Permission denied", the productive questions are:

1. Who owns the file? `ls -l`
2. Who am I? `whoami` and `id`
3. Which permission is actually missing?
4. Do I need `x` on a **parent directory** to reach it?

Then grant the narrowest thing that fixes it, usually with `chmod u+x` or by changing ownership.

## The bits you will meet later

- **`umask`** sets the default permissions for newly created files. A umask of `022` produces `644` files and `755` directories, which is the common default.
- **The sticky bit** on a directory (`chmod +t`, shown as `t`) means only a file's owner can delete it, even if others can write to the directory. This is why `/tmp` is `drwxrwxrwt`.
- **setuid and setgid** (shown as `s`) make a program run as its owner or group rather than as the person invoking it. Powerful, occasionally necessary, and a classic privilege escalation route when misused.

## Practice

```bash
mkdir perms-test && cd perms-test
echo "hello" > file.txt
ls -l                      # note the default permissions your umask produced
chmod 600 file.txt && ls -l
chmod 644 file.txt && ls -l

printf '#!/bin/sh\necho it ran\n' > run.sh
./run.sh                   # Permission denied: no execute bit
chmod +x run.sh
./run.sh                   # now it runs

mkdir sub && chmod 600 sub  # read and write but no execute
ls sub                      # permission denied: no x means no traversal
chmod 700 sub && ls sub     # works
cd .. && rm -rf perms-test
```

That last pair is the lesson most worth keeping: **on a directory, `x` is the permission that lets you in.**

## What to look at next

- **[Terminal basics](./terminal-basics.md)** - navigating and manipulating files
- **[SSH basics](./ssh-basics.md)** - where `600` on a private key becomes mandatory
- **[What is a server?](./what-is-a-server.md)** - the machines these permissions protect
- **[IAM explained](../concepts/iam-explained.md)** - the same ideas at cloud scale
