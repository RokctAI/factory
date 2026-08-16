#!/usr/bin/env python3
"""Parse an `app-idea` issue-form body into the fields app_spawn.yml needs.

Issue forms render as `### Heading` followed by the value. Optional fields the
submitter left empty render as `_No response_`. Anything the parser cannot
resolve is a hard error: a half-parsed brief would seed a repo the agent
cannot build from.

Usage: parse_app_idea.py --body-file <path> [--default-owner <login>]
Writes `key=value` lines to $GITHUB_OUTPUT when set, otherwise to stdout.
Multi-line values use the heredoc form so `spec` survives intact.

The resolved owner goes through owners.canonical(), because `initiate.py`
gates the protocol bootstrap on a case-sensitive `RokctAI/` — see owners.py.
"""
import argparse
import os
import re
import sys
import uuid

import owners

SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}[a-z0-9]$")
HEADING_RE = re.compile(r"^###[ \t]+(.+?)[ \t]*$")
NO_RESPONSE = ("_no response_", "_no response_.", "")

# Issue-form label -> output key. Labels are matched case-insensitively with
# punctuation stripped, so "One-line description" still lands if Ray retitles
# it to "One line description".
FIELDS = {
    "app name": "name",
    "one line description": "description",
    "rationale": "rationale",
    "visibility": "visibility",
    "target owner": "owner",
}


def normalise(heading):
    return re.sub(r"[^a-z0-9]+", " ", heading.lower()).strip()


def parse(body):
    sections, current, buf = {}, None, []
    for line in body.replace("\r\n", "\n").split("\n"):
        match = HEADING_RE.match(line)
        if match:
            if current:
                sections[current] = "\n".join(buf).strip()
            current, buf = normalise(match.group(1)), []
        elif current is not None:
            buf.append(line)
    if current:
        sections[current] = "\n".join(buf).strip()

    out = {}
    for label, key in FIELDS.items():
        value = sections.get(label, "").strip()
        out[key] = "" if value.lower() in NO_RESPONSE else value
    return out


def validate(fields, default_owner):
    errors = []
    if not fields["name"]:
        errors.append("**App name** is missing.")
    elif not SLUG_RE.match(fields["name"]):
        errors.append(
            f"**App name** `{fields['name']}` is not a valid slug — "
            "lowercase letters, digits and hyphens only, 2-64 characters, "
            "starting and ending with a letter or digit."
        )
    if not fields["description"]:
        errors.append("**One-line description** is missing.")
    if not fields["rationale"]:
        errors.append("**Rationale** is missing.")

    if fields["visibility"] not in ("private", "public"):
        # Default rather than fail: a missing dropdown is a form drift
        # problem, and private is the safe side of it.
        fields["visibility"] = "private"
    # Canonicalise before validating: `rokctai` and `ROKCTAI` reach the same
    # org on GitHub but only `RokctAI` survives initiate.py's origin test.
    # An owner we do not know keeps its casing exactly.
    fields["owner"] = owners.canonical(fields["owner"])
    if not fields["owner"]:
        fields["owner"] = owners.canonical(default_owner) or owners.DEFAULT_OWNER
    elif not re.match(r"^[A-Za-z0-9][A-Za-z0-9-]{0,38}$", fields["owner"]):
        errors.append(f"**Target owner** `{fields['owner']}` is not a valid GitHub login.")
    return errors


def emit(fields, handle):
    for key, value in fields.items():
        if "\n" in value:
            marker = f"EOF_{uuid.uuid4().hex}"
            handle.write(f"{key}<<{marker}\n{value}\n{marker}\n")
        else:
            handle.write(f"{key}={value}\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--body-file", required=True)
    # Blank is normal: app_spawn.yml passes vars.FACTORY_TARGET_OWNER straight
    # through, and that variable is usually unset.
    ap.add_argument("--default-owner", default="")
    args = ap.parse_args()

    with open(args.body_file, "r", encoding="utf-8") as f:
        fields = parse(f.read())

    errors = validate(fields, args.default_owner)
    if errors:
        print("Could not spawn an app repo from this issue:\n", file=sys.stderr)
        for e in errors:
            print(f"- {e}", file=sys.stderr)
        sys.exit(1)

    fields["spec"] = fields.pop("rationale")
    target = os.environ.get("GITHUB_OUTPUT")
    if target:
        with open(target, "a", encoding="utf-8") as f:
            emit(fields, f)
    else:
        emit(fields, sys.stdout)


if __name__ == "__main__":
    main()
