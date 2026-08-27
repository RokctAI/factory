#!/usr/bin/env python3
# Licensed under the MIT License.
# Copyright 2026 RokctAI
"""Unit tests for .github/scripts/seed_app_repo.py (stdlib unittest).

The seeder has two jobs and both are covered here:

  1. **Layouts.** The historical flat template (no `common/` subdirectory)
     must keep seeding exactly as before, while the per-stack layout copies
     `common/` first and the requested stack overlay second, overlay files
     winning on collision. `--stack` against a flat template is a loud
     refusal, not a silent ignore.
  2. **Substitution.** Every `{{TOKEN}}` must resolve — a leftover token is a
     SystemExit, because a pushed repo with `{{APP_NAME}}` in its README is
     a bug nobody re-runs the spawn for. `APP_SLUG` is derived, not passed,
     so its derivation is pinned down here too.

The suite builds throwaway templates under tempfile for the behavioural
tests, and additionally checks the *real* `templates/app/` tree for the two
invariants Ray ruled on: it is layered (has `common/`), and no `.relation`
is seeded into app shells anywhere in it.

Run from the repo root:
    python3 -m unittest discover -s .github/scripts/tests -v
"""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import seed_app_repo  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]


def write(path, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


class SeedRunner:
    """Run seed_app_repo.main() against a template with canned args."""

    def seed(self, template, dest, name="My App", stack=None):
        spec = Path(dest).parent / "spec.txt"
        write(spec, "Do the thing.")
        argv = [
            "seed_app_repo.py",
            "--template", str(template),
            "--dest", str(dest),
            "--name", name,
            "--description", "A test app",
            "--spec-file", str(spec),
            "--owner", "RokctAI",
            "--visibility", "private",
            "--issue", "https://github.com/RokctAI/factory/issues/1",
        ]
        if stack:
            argv += ["--stack", stack]
        old_argv = sys.argv
        sys.argv = argv
        try:
            seed_app_repo.main()
        finally:
            sys.argv = old_argv


class TestAppSlug(unittest.TestCase):
    def test_lowercases(self):
        self.assertEqual(seed_app_repo.app_slug("Supacharge"), "supacharge")

    def test_spaces_and_underscores_become_hyphens(self):
        self.assertEqual(seed_app_repo.app_slug("My Cool_App"), "my-cool-app")

    def test_strips_disallowed_characters(self):
        self.assertEqual(seed_app_repo.app_slug("Bob's App! v2"), "bobs-app-v2")

    def test_collapses_and_trims_separators(self):
        self.assertEqual(seed_app_repo.app_slug("  a  b  "), "a-b")

    def test_hyphens_survive(self):
        self.assertEqual(seed_app_repo.app_slug("supacharge-web"), "supacharge-web")


class SeedTestCase(SeedRunner, unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.dest = self.root / "seed"

    def make_flat_template(self):
        t = self.root / "template"
        write(t / "README.md", "# {{APP_NAME}}\n{{APP_DESCRIPTION}}\n")
        write(t / "gitignore", "node_modules/\n")
        write(t / ".rokct" / "bootstrap.sh", "#!/bin/sh\necho {{APP_REPO}}\n")
        return t

    def make_layered_template(self):
        t = self.root / "template"
        write(t / "common" / "README.md", "# {{APP_NAME}}\n")
        write(t / "common" / "AGENTS.md", "Spec: {{APP_SPEC}}\n")
        write(t / "common" / "gitignore", "node_modules/\n")
        write(t / "common" / ".rokct" / "bootstrap.sh", "#!/bin/sh\n")
        for stack in seed_app_repo.STACKS:
            write(
                t / stack / ".rokct" / "config" / "app_type",
                "{{APP_SLUG}}\n",
            )
        # Collision: the overlay README must win over common's.
        write(t / "nextjs" / "README.md", "# {{APP_NAME}} (nextjs shell)\n")
        write(
            t / "nextjs" / "composer.json",
            '{"name": "{{APP_SLUG}}_composer", "sdks": []}\n',
        )
        return t


class TestFlatLegacyTemplate(SeedTestCase):
    def test_flat_copy_renames_and_substitutes(self):
        self.seed(self.make_flat_template(), self.dest)
        self.assertEqual(
            (self.dest / "README.md").read_text(),
            "# My App\nA test app\n",
        )
        self.assertTrue((self.dest / ".gitignore").is_file())
        self.assertFalse((self.dest / "gitignore").exists())
        bootstrap = self.dest / ".rokct" / "bootstrap.sh"
        self.assertIn("RokctAI/My App", bootstrap.read_text())
        self.assertTrue(os.access(bootstrap, os.X_OK))

    def test_stack_against_flat_template_fails(self):
        template = self.make_flat_template()
        with self.assertRaises(SystemExit) as ctx:
            self.seed(template, self.dest, stack="nextjs")
        self.assertIn("no common/ subdirectory", str(ctx.exception))


class TestLayeredTemplate(SeedTestCase):
    def test_no_stack_seeds_common_only(self):
        self.seed(self.make_layered_template(), self.dest)
        self.assertTrue((self.dest / "README.md").is_file())
        self.assertTrue((self.dest / ".gitignore").is_file())
        self.assertFalse((self.dest / "composer.json").exists())
        self.assertFalse((self.dest / ".rokct" / "config").exists())

    def test_each_stack_overlay_lands_with_slug(self):
        for stack in seed_app_repo.STACKS:
            dest = self.root / f"seed-{stack}"
            self.seed(self.make_layered_template(), dest, stack=stack)
            app_type = dest / ".rokct" / "config" / "app_type"
            self.assertEqual(app_type.read_text(), "my-app\n")

    def test_overlay_wins_on_collision(self):
        self.seed(self.make_layered_template(), self.dest, stack="nextjs")
        self.assertEqual(
            (self.dest / "README.md").read_text(),
            "# My App (nextjs shell)\n",
        )
        composed = json.loads((self.dest / "composer.json").read_text())
        self.assertEqual(composed, {"name": "my-app_composer", "sdks": []})

    def test_missing_overlay_fails(self):
        t = self.root / "template"
        write(t / "common" / "README.md", "# {{APP_NAME}}\n")
        with self.assertRaises(SystemExit) as ctx:
            self.seed(t, self.dest, stack="frappe")
        self.assertIn("no overlay for stack 'frappe'", str(ctx.exception))


class TestLeftoverTokens(SeedTestCase):
    def test_unknown_token_is_fatal(self):
        t = self.root / "template"
        write(t / "README.md", "{{APP_NAME}} uses {{NOT_A_TOKEN}}\n")
        with self.assertRaises(SystemExit) as ctx:
            self.seed(t, self.dest)
        self.assertIn("NOT_A_TOKEN", str(ctx.exception))


class TestRealTemplateTree(unittest.TestCase):
    """Invariants on the committed templates/app/ itself."""

    template = REPO_ROOT / "templates" / "app"

    def test_is_layered(self):
        self.assertTrue((self.template / "common").is_dir())
        for stack in seed_app_repo.STACKS:
            self.assertTrue((self.template / stack).is_dir(), stack)

    def test_no_relation_anywhere(self):
        # Ray's ruling: .relation is an SDK-repo-only marker and must never
        # be seeded into an app shell.
        offenders = [
            str(p) for p in self.template.rglob("*") if p.name == ".relation"
        ]
        self.assertEqual(offenders, [])

    def test_every_stack_ships_app_type_marker(self):
        for stack in seed_app_repo.STACKS:
            marker = self.template / stack / ".rokct" / "config" / "app_type"
            self.assertEqual(marker.read_text(), "{{APP_SLUG}}\n", stack)

    def test_only_nextjs_ships_an_active_composer_json(self):
        # frappe: universal-frappe-ci composes whenever a committed
        # composer.json exists at the repo root, so the frappe overlay must
        # ship the example only. flutter: CI overwrites composer.json from
        # the Protocol registry template, so an active seed is pointless.
        self.assertTrue((self.template / "nextjs" / "composer.json").is_file())
        for stack in ("flutter", "frappe"):
            self.assertFalse(
                (self.template / stack / "composer.json").exists(), stack
            )
            self.assertTrue(
                (self.template / stack / "composer.json.example").is_file(),
                stack,
            )


if __name__ == "__main__":
    unittest.main()
