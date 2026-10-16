#!/usr/bin/env python3
"""Canonical spellings for the GitHub owners the protocol treats specially.

`initiate.py` decides whether a repo gets the `.rok` skill, the Protocol
workflow deploy and the shared-workspace route by testing the literal
substring `RokctAI/` against the git origin URL — case-sensitively, in three
places. GitHub logins are case-insensitive, so a repo created under `rokctai`
lands in exactly the right org and nothing errors; the bootstrap just quietly
skips all three. Routing every resolved owner through `canonical()` means any
casing the submitter types comes back spelled the way `initiate.py` expects.

Owners we do not know are returned trimmed but otherwise byte-for-byte:
personal accounts and third-party orgs have no canonical form to impose, and
mangling their casing would be the same silent damage in the other direction.

Adding another known org is one more entry in KNOWN_OWNERS; the spelling
lives here and nowhere else.

Usage from shell: `owners.py <owner>` prints the resolved canonical spelling
(blank input prints DEFAULT_OWNER).
"""
import sys

# The owner new app repos land under when nothing else is specified.
DEFAULT_OWNER = "RokctAI"

# Every owner whose casing is load-bearing. Matched case-insensitively.
KNOWN_OWNERS = (DEFAULT_OWNER,)

_CANONICAL_BY_LOWER = {owner.lower(): owner for owner in KNOWN_OWNERS}


def canonical(owner):
    """Trim `owner`; return the canonical casing if it is a known owner.

    Anything else comes back exactly as given (after trimming), casing and
    all.
    """
    owner = (owner or "").strip()
    return _CANONICAL_BY_LOWER.get(owner.lower(), owner)


def resolve(owner, default=None):
    """Canonicalise `owner`, falling back to `default` when it is blank."""
    if default is None:
        default = DEFAULT_OWNER
    return canonical(owner) or canonical(default) or DEFAULT_OWNER


if __name__ == "__main__":
    print(resolve(sys.argv[1] if len(sys.argv) > 1 else ""))
