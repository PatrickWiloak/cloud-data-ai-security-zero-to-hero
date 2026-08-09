---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 7 min
---

# JSON and YAML

> **7-minute read. Assumes you've read [Terminal basics](./terminal-basics.md).**

## Why this page exists

Almost every configuration file, API response, and infrastructure definition you will meet is JSON or YAML. They describe the same kinds of data in different syntax, and most of the frustration people have with them comes from three or four specific gotchas rather than from the formats being hard.

## The shapes

Both formats build everything from four things:

- **Scalars**: a string, number, boolean, or null
- **Lists** (arrays): an ordered sequence
- **Maps** (objects, dictionaries): named keys with values
- **Nesting**: lists and maps containing more lists and maps

That is the whole data model. Once you can see those four in a file, the syntax is just punctuation.

## JSON

```json
{
  "name": "web-server",
  "port": 8080,
  "enabled": true,
  "replicas": null,
  "tags": ["production", "eu-west"],
  "resources": {
    "cpu": "500m",
    "memory": "512Mi"
  }
}
```

Rules that trip people up:

- **Keys must be double-quoted strings.** Single quotes are invalid.
- **No trailing comma** after the last item. This is the single most common JSON error.
- **No comments.** There is no comment syntax in JSON at all.
- Strings use double quotes; numbers, `true`, `false`, and `null` are bare.

JSON is strict and unambiguous, which makes it excellent for machines and slightly tedious for humans.

## YAML

The same data:

```yaml
name: web-server
port: 8080
enabled: true
replicas: null
tags:
  - production
  - eu-west
resources:
  cpu: 500m
  memory: 512Mi
```

Rules:

- **Indentation defines structure**, and it must be **spaces, never tabs**. A tab is a syntax error.
- A key-value pair is `key: value`, with a space after the colon.
- A list item starts with `- `.
- Comments start with `#`.
- Quotes are optional for most strings and required when the value would otherwise be parsed as something else.

YAML is a superset of JSON, so valid JSON is valid YAML. That is occasionally useful when you need to embed one in the other.

## The YAML gotchas worth memorizing

**1. Tabs are illegal.** Configure your editor to insert spaces in `.yaml` files. Most "invalid YAML" errors on a file that looks fine are a stray tab.

**2. Indentation must be consistent.** Two spaces is conventional. What matters is that sibling keys line up exactly.

**3. Some bare words are not strings.**

```yaml
version: 1.10        # the number 1.1, because trailing zeros are dropped
port: "8080"         # a string
enabled: yes         # older YAML parsers read this as boolean true
country: NO          # Norway, or boolean false, depending on the parser
time: 12:30          # may parse as a sexagesimal number
```

The fix is always the same: **quote it** when you mean a string. `version: "1.10"` is unambiguous.

**4. Multi-line strings have two forms:**

```yaml
literal: |
  line one
  line two
  # keeps the newlines

folded: >
  this is all
  one long line
  # newlines become spaces
```

**5. A colon inside an unquoted value breaks parsing.**

```yaml
message: Error: something failed     # invalid
message: "Error: something failed"   # fine
```

## Reading them from the terminal

`jq` for JSON and `yq` for YAML are worth installing on day one.

```bash
# Pretty-print and inspect
cat config.json | jq .
cat config.json | jq '.resources.cpu'
cat config.json | jq '.tags[]'
cat config.json | jq '.items[] | select(.status == "active") | .name'

# The same for YAML
yq '.resources.cpu' config.yaml

# Convert between them
yq -o json config.yaml
```

Validating before you deploy something saves a lot of time:

```bash
jq empty config.json      # prints nothing if valid, an error if not
yq '.' config.yaml > /dev/null
python3 -c 'import json,sys; json.load(open("config.json"))'
```

## Which format where

| You will see | Format |
|---|---|
| REST API requests and responses | JSON |
| `package.json`, `tsconfig.json` | JSON |
| Kubernetes manifests | YAML |
| GitHub Actions workflows | YAML |
| Docker Compose | YAML |
| Ansible playbooks | YAML |
| CloudFormation | Either |
| Terraform | HCL, which is a third thing but reads similarly |

The rough rule: **machines talk JSON to each other, humans write YAML for machines.**

## A note on YAML in the age of infrastructure as code

Because YAML has no types beyond the basics and no validation of its own, a manifest can be perfectly valid YAML and completely wrong for the system consuming it. That is why tools ship schemas and validators, and why editors with schema support for Kubernetes or GitHub Actions catch far more mistakes than a YAML linter alone.

Turn on schema validation in your editor. It is the single highest-value setup step for anyone writing these files daily.

## Practice

```bash
cat > test.yaml <<'YAML'
service:
  name: api
  port: 8080
  tags:
    - web
    - public
YAML

yq '.service.name' test.yaml
yq -o json test.yaml
yq -o json test.yaml | jq '.service.tags[]'
rm test.yaml
```

Then deliberately break it: add a tab, remove the space after a colon, add a trailing comma to the JSON output. Reading the resulting error messages is the fastest way to learn to recognize them later.

## What to look at next

- **[HTTP and APIs](./http-and-apis.md)** - where the JSON you meet usually comes from
- **[What is an API call?](./what-is-an-api-call.md)**
- **[Terminal basics](./terminal-basics.md)**
- **[Terraform explained](../concepts/terraform-explained.md)** - configuration as code
- **[Kubernetes in 10 minutes](../concepts/kubernetes-in-10-minutes.md)** - the largest consumer of YAML you will meet
