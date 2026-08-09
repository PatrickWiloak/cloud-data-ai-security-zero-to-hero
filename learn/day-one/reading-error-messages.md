---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 7 min
---

# Reading Error Messages

> **7-minute read. Assumes you've read [Terminal basics](./terminal-basics.md).**

## Why this page exists

The difference between someone who has been doing this for a decade and someone who started last month is only partly knowledge. A lot of it is that the experienced person **reads the error**, and the beginner skims it, feels a flash of dread, and pastes the whole thing into a search box.

Error messages are usually telling you exactly what is wrong. This page is about how to extract that.

## The four questions

For any error, in this order:

1. **What actually failed?** Not what you were trying to do, but the specific operation that returned an error.
2. **Where?** Which file, which line, which host, which service.
3. **What did it expect versus what did it get?** Most errors contain both.
4. **What is the first error?** Not the last one.

Question 4 matters more than people expect.

## Read the first error, not the last

A stack trace or a build log is usually a cascade. One genuine failure causes twenty downstream complaints, and the loudest, longest, most alarming message at the bottom is often a consequence rather than a cause.

Scroll **up** to the first thing that went wrong. Fix that. Frequently the other nineteen disappear.

The same applies to compiler output: fix the first error, recompile, and do not bother reading the rest until you have.

## Reading a stack trace

A stack trace reads **bottom-up in cause, top-down in call order**. The most useful line is usually neither the first nor the last: it is **the deepest line that points at code you wrote**.

```
Traceback (most recent call last):
  File "app.py", line 42, in <module>
    result = process_order(order_id)
  File "app.py", line 28, in process_order
    total = order["items"][0]["price"]      <-- your code, and the real location
  File "lib/parser.py", line 310, in __getitem__
    raise KeyError(key)
KeyError: 'price'
```

The last line is the **error type and value**: a `KeyError` for `'price'`. The framework frames below your code are usually just the machinery that noticed. Line 28 of `app.py` is where you look.

So: find the error type and value at the bottom, then find the last frame in your own code, and start there.

## Errors that mean something specific

These come up constantly, and each has a small set of real causes.

| Message | Usually means |
|---|---|
| **Permission denied** | Missing read, write, or execute; or missing `x` on a parent directory. See [file permissions](./file-permissions.md) |
| **No such file or directory** | A typo, a relative path resolved from a different working directory, or a file that was never created |
| **Command not found** | Not installed, or installed but not on your `PATH` |
| **Connection refused** | You reached the host and nothing is listening on that port. The service is down, or on a different port |
| **Connection timed out** | You did not reach the host at all. Firewall, security group, wrong address, or network route |
| **Name or service not known** | DNS could not resolve the name. A typo, or a name that only resolves inside a particular network |
| **401 Unauthorized** | Authentication failed: the credential is missing, wrong, or expired |
| **403 Forbidden** | Authentication succeeded, authorization failed: you are who you say and are not allowed |
| **404 Not Found** | The path is wrong, or the resource does not exist |
| **409 Conflict** | The resource already exists, or the state changed under you |
| **429 Too Many Requests** | Rate limited. Back off and retry |
| **500 Internal Server Error** | The server broke. The useful log is on the server, not here |
| **502 / 503 / 504** | The proxy could not reach, or was not answered by, the backend |
| **Address already in use** | Something is already listening on that port |
| **Out of memory / OOMKilled** | The process exceeded its memory limit and was terminated |

The distinction between **connection refused** and **connection timed out** is worth internalizing. Refused means you got there and nothing answered, so look at the service. Timed out means you never got there, so look at the network.

The distinction between **401** and **403** is the same shape: 401 is "I do not know who you are", 403 is "I know exactly who you are and no".

## Finding more detail

Most tools have more to say than they showed you:

```bash
command --verbose
command --debug
command -v            # or -vv, -vvv for progressively more
```

For services, the log is somewhere else than your terminal:

```bash
journalctl -u servicename -n 100 --no-pager
docker logs container-name --tail 100
kubectl logs pod-name --previous      # the previous container, for a crash loop
kubectl describe pod pod-name         # events, which often explain more than the logs
```

`kubectl describe` is the specific thing beginners miss: for a pod that will not start, the **Events** section at the bottom usually states the reason in plain language.

## Searching effectively

When you do search, strip the parts unique to you:

- Remove your file paths, hostnames, IDs, and timestamps
- Keep the error type, the library name, and the distinctive phrase
- Add the tool and version: `postgres 16 "could not connect to server"`
- Quote the exact phrase to avoid loosely related results

Searching `Error: connect ECONNREFUSED 127.0.0.1:5432` is better than searching the whole log, and `"ECONNREFUSED" postgres docker-compose` is better still.

## When the message really is useless

Some errors genuinely tell you nothing. Then:

1. **Reproduce it reliably.** An intermittent bug you cannot trigger is very hard to fix.
2. **Reduce it.** Cut away everything that still produces the error, until what remains is small.
3. **Change one thing at a time**, and note what happened.
4. **Check what changed recently.** Most breakages follow a change: a deploy, an upgrade, a config edit, an expired certificate.
5. **Rubber-duck it.** Explaining the problem out loud, in order, solves a genuinely surprising proportion of them.

## The habit worth building

Before reacting to an error, read it once, slowly, all the way through. That single habit will save you more time over a career than any tool.

## What to look at next

- **[Terminal basics](./terminal-basics.md)**
- **[Networking troubleshooting](./networking-troubleshooting.md)** - for the connection errors above
- **[File permissions](./file-permissions.md)** - for permission denied
- **[HTTP and APIs](./http-and-apis.md)** - for the status codes
- **[Observability basics](../concepts/observability-basics.md)** - finding errors before a user reports them
