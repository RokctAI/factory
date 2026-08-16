#!/usr/bin/env python3
# Licensed under the MIT License.
# Copyright 2026 RokctAI
"""Unit tests for .github/scripts/owners.py and the owner field of
parse_app_idea.py (stdlib unittest).

The bug these pin down is silent: `initiate.py` gates the `.rok` skill, the
Protocol workflow deploy and the workspace route on a case-sensitive
`RokctAI/` substring of the git origin URL, while GitHub itself is
case-insensitive about logins. A repo spawned under `rokctai` therefore lands
in exactly the right org, reports success, and loses all three — nothing
errors anywhere. So the tests run in both directions:

  1. Every casing of a KNOWN owner must come back canonically spelled.
  2. Every other owner must come back byte-for-byte as given — a blanket
     `.lower()` or `.title()` would break personal accounts the same silent
     way, just pointing the other direction.

Run from the repo root:
    python3 -m unittest discover -s .github/scripts/tests -v
"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import owners  # noqa: E402
import parse_app_idea  # noqa: E402

# Casings of the known org that all have to resolve to owners.DEFAULT_OWNER.
KNOWN_ORG_CASINGS = ["rokctai", "ROKCTAI", "RokctAI", "RoKcTaI", "rokctAI"]

# Owners the factory does not know. Their casing is theirs to keep.
FOREIGN_OWNERS = [
    "RendaniSinyage",  # the personal account apps get promoted out to
    "rendanisinyage",  # ...which is a different string, and must stay one
    "SomeOtherOrg",
    "someotherorg",
    "aB-cD",
    "x",
]

BODY_TEMPLATE = """### App name

receipt-splitter

### One-line description

Splits a photographed till slip between people.

### Rationale

Ray photographs slips and splits them by hand.

### Visibility

private

### Target owner

{owner}
"""


def parsed_owner(owner_field, default_owner=""):
    """Round-trip an issue body through the real parser, return `owner`."""
    body = BODY_TEMPLATE.format(owner=owner_field)
    fields = parse_app_idea.parse(body)
    errors = parse_app_idea.validate(fields, default_owner)
    if errors:
        raise AssertionError(f"unexpected validation errors: {errors}")
    return fields["owner"]


class CanonicalTests(unittest.TestCase):
    """owners.canonical() in isolation."""

    def test_known_org_any_casing_becomes_canonical(self):
        for given in KNOWN_ORG_CASINGS:
            with self.subTest(given=given):
                self.assertEqual(owners.canonical(given), "RokctAI")

    def test_canonical_spelling_is_a_fixed_point(self):
        for known in owners.KNOWN_OWNERS:
            with self.subTest(known=known):
                self.assertEqual(owners.canonical(known), known)
                self.assertEqual(owners.canonical(owners.canonical(known)), known)

    def test_foreign_owner_keeps_its_casing(self):
        for given in FOREIGN_OWNERS:
            with self.subTest(given=given):
                self.assertEqual(owners.canonical(given), given)

    def test_foreign_owners_are_not_collapsed_into_each_other(self):
        # The failure mode a blanket .lower() would introduce.
        self.assertNotEqual(
            owners.canonical("RendaniSinyage"), owners.canonical("rendanisinyage")
        )

    def test_whitespace_is_trimmed(self):
        self.assertEqual(owners.canonical("  rokctai\t"), "RokctAI")
        self.assertEqual(owners.canonical(" RendaniSinyage "), "RendaniSinyage")

    def test_blank_and_none_canonicalise_to_empty(self):
        for given in ("", "   ", "\n", None):
            with self.subTest(given=given):
                self.assertEqual(owners.canonical(given), "")

    def test_resolve_falls_back_to_the_default(self):
        self.assertEqual(owners.resolve(""), owners.DEFAULT_OWNER)
        self.assertEqual(owners.resolve(None), owners.DEFAULT_OWNER)
        self.assertEqual(owners.resolve("   "), owners.DEFAULT_OWNER)
        # A caller-supplied default is canonicalised too — the repo variable
        # FACTORY_TARGET_OWNER is typed by a human just like the form field.
        self.assertEqual(owners.resolve("", "rokctai"), "RokctAI")
        self.assertEqual(owners.resolve("", "RendaniSinyage"), "RendaniSinyage")
        self.assertEqual(owners.resolve("", ""), owners.DEFAULT_OWNER)

    def test_default_owner_is_itself_canonical(self):
        self.assertEqual(owners.canonical(owners.DEFAULT_OWNER), owners.DEFAULT_OWNER)
        self.assertIn(owners.DEFAULT_OWNER, owners.KNOWN_OWNERS)

    def test_canonical_spelling_lives_in_exactly_one_place(self):
        # Guards the "one-line change to add an org" property: the parser
        # must not carry its own copy of the literal.
        source = (Path(owners.__file__).parent / "parse_app_idea.py").read_text(
            encoding="utf-8"
        )
        code = "\n".join(
            line for line in source.splitlines() if not line.lstrip().startswith("#")
        )
        self.assertNotIn(f'"{owners.DEFAULT_OWNER}"', code)
        self.assertNotIn(f"'{owners.DEFAULT_OWNER}'", code)


class ParsedOwnerTests(unittest.TestCase):
    """The owner as it comes out of a real issue-form body."""

    def test_known_org_any_casing_becomes_canonical(self):
        for given in KNOWN_ORG_CASINGS:
            with self.subTest(given=given):
                self.assertEqual(parsed_owner(given), "RokctAI")

    def test_foreign_owner_keeps_its_casing(self):
        for given in FOREIGN_OWNERS:
            with self.subTest(given=given):
                self.assertEqual(parsed_owner(given), given)

    def test_absent_field_falls_back_to_the_default(self):
        body = BODY_TEMPLATE.replace("### Target owner\n\n{owner}\n", "")
        fields = parse_app_idea.parse(body)
        self.assertEqual(parse_app_idea.validate(fields, ""), [])
        self.assertEqual(fields["owner"], owners.DEFAULT_OWNER)

    def test_no_response_falls_back_to_the_default(self):
        self.assertEqual(parsed_owner("_No response_"), owners.DEFAULT_OWNER)

    def test_blank_field_honours_a_lowercase_repo_variable(self):
        # vars.FACTORY_TARGET_OWNER reaches the parser unmodified, so a
        # lowercase variable used to poison every spawn.
        self.assertEqual(parsed_owner("_No response_", "rokctai"), "RokctAI")

    def test_invalid_login_still_errors(self):
        fields = parse_app_idea.parse(BODY_TEMPLATE.format(owner="not a login!"))
        errors = parse_app_idea.validate(fields, "")
        self.assertTrue(any("Target owner" in e for e in errors), errors)

    def test_app_name_slug_is_untouched(self):
        # Slugs are validated, not normalised; nothing here should change that.
        fields = parse_app_idea.parse(BODY_TEMPLATE.format(owner="rokctai"))
        self.assertEqual(parse_app_idea.validate(fields, ""), [])
        self.assertEqual(fields["name"], "receipt-splitter")


class EmittedOutputTests(unittest.TestCase):
    """What actually reaches $GITHUB_OUTPUT, which is what builds the remote."""

    def _emit(self, owner_field, default_owner=""):
        fields = parse_app_idea.parse(BODY_TEMPLATE.format(owner=owner_field))
        self.assertEqual(parse_app_idea.validate(fields, default_owner), [])
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "out"
            with path.open("w", encoding="utf-8") as f:
                parse_app_idea.emit(fields, f)
            return path.read_text(encoding="utf-8")

    def test_owner_line_is_canonical(self):
        self.assertIn("owner=RokctAI\n", self._emit("ROKCTAI"))

    def test_foreign_owner_line_is_verbatim(self):
        self.assertIn("owner=RendaniSinyage\n", self._emit("RendaniSinyage"))


if __name__ == "__main__":
    unittest.main()
