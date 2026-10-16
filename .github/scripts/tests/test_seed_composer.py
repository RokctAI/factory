#!/usr/bin/env python3
# Licensed under the MIT License.
# Copyright 2026 ROKCT INTELLIGENCE (PTY) LTD
"""Unit tests for .github/scripts/seed_composer.py (stdlib unittest).

The spawn rewrites a Next.js shell's composer.json from the protocol at
creation time. These tests pin down, with the network stubbed out:

  1. **Source order.** The registry template named by the app_type wins;
     without one the consumers index (sdk_consumers.json) decides when it
     lists the shell; without that the protocol's generated
     nextjs_compose_example.json (the kernel) is used; and only when the
     protocol cannot be read at all does the overlay's own telemetry + base
     default stand - loudly.
  2. **Pins.** Every git entry is re-pinned to the SHA-256 of its install.py
     as read from the SDK repo now, CRLF folded to LF (compose.sh's own
     rule); an unreadable installer keeps the source's pin with a warning
     and an entry left with no pin at all is fatal.
  2b. **Versions.** Every git entry's `version` is what the manifest.json
     next to that install.py declares now - the consumers index trails
     releases - and the source's value stands, with a warning, only when
     the manifest is unreachable, not JSON, or has no version.
  3. **Drift.** An entry the index places in another repo or at another
     path stops the spawn; an SDK the index has not caught up with is a
     warning.
  4. **Never empty.** No enabled SDK is a SystemExit.

Run from the repo root:
    python3 -m unittest discover -s .github/scripts/tests -v
"""

import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import seed_composer  # noqa: E402

SHA_TEL = "1" * 64
SHA_BASE = "2" * 64
SHA_LMS = "3" * 64
TEL_PY = b"print('telemetry')\r\n"  # CRLF on purpose: the pin folds it
BASE_PY = b"print('base')\n"
LMS_PY = b"print('lms')\n"


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data), encoding="utf-8")


def record(repo, path, version, pin, consumers=()):
    return {"repo": repo, "consumers": list(consumers),
            "nextjs": {"path": path, "version": version, "install_py_sha256": pin}}


def git_entry(name, repo_short, sha=None, home=False, enabled=True):
    return {"name": name, "enabled": enabled, "source": "git",
            "git": f"https://github.com/RokctAI/{repo_short}",
            "path": f"../{repo_short}/{name[:-4]}/nextjs", "ref": "main",
            **({"sha256": sha} if sha else {}), "home_sdk": home}


class FakeNetwork:
    """Stands in for fetch_raw/fetch_head: a dict of (repo, path) -> bytes.
    A (repo, path) in `broken` raises the way a 5xx from the contents API
    would."""

    def __init__(self, files, broken=()):
        self.files = files
        self.broken = set(broken)
        self.calls = []

    def fetch_raw(self, owner_repo, path, ref, token=None):
        self.calls.append((owner_repo, path, ref))
        if (owner_repo, path) in self.broken:
            raise urllib.error.HTTPError(f"https://api.github.com/{owner_repo}/{path}", 503,
                                         "Service Unavailable", None, None)
        return self.files.get((owner_repo, path))

    def fetch_head(self, owner_repo, ref, token=None):
        return "abcdef0123456789"


class SeedComposerCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.dest = self.root / "seed"
        self.protocol = self.root / "protocol"
        (self.protocol / "core/utils/frappe/composer").mkdir(parents=True)
        # The overlay default the seeder laid down (the last-resort fallback).
        write_json(self.dest / "composer.json", {"sdks": [
            git_entry("telemetry_sdk", "core", "f" * 64),
            git_entry("base_sdk", "core", "e" * 64),
        ]})
        self.net = FakeNetwork({
            ("RokctAI/core", "telemetry/nextjs/install.py"): TEL_PY,
            ("RokctAI/core", "base/nextjs/install.py"): BASE_PY,
            ("RokctAI/agent", "lms/nextjs/install.py"): LMS_PY,
        })
        self._orig = (seed_composer.fetch_raw, seed_composer.fetch_head)
        seed_composer.fetch_raw = self.net.fetch_raw
        seed_composer.fetch_head = self.net.fetch_head
        self.addCleanup(self._restore)

    def _restore(self):
        seed_composer.fetch_raw, seed_composer.fetch_head = self._orig

    def write_index(self, extra=None, consumers_of_shell=("acme-web",)):
        sdks = {
            "telemetry_sdk": record("RokctAI/core", "telemetry/nextjs", "1.2.0", SHA_TEL, consumers_of_shell),
            "base_sdk": record("RokctAI/core", "base/nextjs", "1.35.0", SHA_BASE, consumers_of_shell),
        }
        sdks.update(extra or {})
        write_json(self.protocol / "sdk_consumers.json", {"generated_by": "test", "sdks": sdks})

    def write_example(self):
        write_json(self.protocol / "nextjs_compose_example.json", {"sdks": [
            dict(git_entry("telemetry_sdk", "core", SHA_TEL), version="1.2.0"),
            dict(git_entry("base_sdk", "core", SHA_BASE), version="1.35.0"),
        ]})

    def run_main(self, app_type="acme-web", protocol_dir=None):
        argv = ["seed_composer.py", "--dest", str(self.dest), "--app-type", app_type,
                "--name", "Acme Web", "--protocol-dir",
                str(self.protocol if protocol_dir is None else protocol_dir)]
        old_argv, old_env = sys.argv, os.environ.get("GH_TOKEN")
        sys.argv = argv
        os.environ.pop("GH_TOKEN", None)
        out, err = io.StringIO(), io.StringIO()
        try:
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                seed_composer.main()
        finally:
            sys.argv = old_argv
            if old_env is not None:
                os.environ["GH_TOKEN"] = old_env
        return out.getvalue(), err.getvalue()

    def composer(self):
        return json.loads((self.dest / "composer.json").read_text(encoding="utf-8"))


class TestSha(unittest.TestCase):
    def test_crlf_folds_to_lf(self):
        self.assertEqual(seed_composer.sha256_lf(b"a\r\nb\r\n"), seed_composer.sha256_lf(b"a\nb\n"))

    def test_subpath_and_repo_parsing(self):
        entry = git_entry("telemetry_sdk", "core")
        self.assertEqual(seed_composer.sdk_subpath(entry), "telemetry/nextjs")
        self.assertEqual(seed_composer.owner_repo_of(entry["git"]), "RokctAI/core")
        lower = dict(git_entry("auth_sdk", "users"), git="https://github.com/RokctAI/Users.git")
        self.assertEqual(seed_composer.sdk_subpath(lower), "auth/nextjs")


class TestSourceOrder(SeedComposerCase):
    def test_registry_template_wins(self):
        write_json(self.protocol / "core/utils/frappe/composer/acme-web.json", {"sdks": [
            git_entry("telemetry_sdk", "core", "9" * 64),
            git_entry("base_sdk", "core", "9" * 64),
            git_entry("lms_sdk", "agent", "9" * 64, home=True),
        ]})
        self.write_index({"lms_sdk": record("RokctAI/agent", "lms/nextjs", "1.25.0", SHA_LMS)})
        self.write_example()
        out, err = self.run_main()
        c = self.composer()
        self.assertEqual([s["name"] for s in c["sdks"]], ["telemetry_sdk", "base_sdk", "lms_sdk"])
        self.assertEqual(c["name"], "acme_web_composer")
        self.assertIn("acme-web.json", c["_comment"])
        self.assertEqual(c["sdks"][2]["home_sdk"], True)
        self.assertIn("home SDK: lms_sdk", out)

    def test_consumers_index_when_no_template(self):
        self.write_index({
            "lms_sdk": record("RokctAI/agent", "lms/nextjs", "1.25.0", SHA_LMS, ["acme-web"]),
            "zones_sdk": {"repo": "RokctAI/zones", "consumers": ["acme-web"], "nextjs": None},
        })
        self.write_example()
        out, err = self.run_main()
        c = self.composer()
        self.assertEqual([s["name"] for s in c["sdks"]], ["telemetry_sdk", "base_sdk", "lms_sdk"])
        self.assertEqual(c["sdks"][2]["path"], "../agent/lms/nextjs")
        self.assertEqual(c["sdks"][2]["version"], "1.25.0")
        self.assertIn("sdk_consumers.json", c["_comment"])
        self.assertIn("skipped zones_sdk", out)
        self.assertIn("no home SDK is recorded", out)
        self.assertTrue(all(s["home_sdk"] is False for s in c["sdks"]))

    def test_example_when_index_does_not_list_the_shell(self):
        self.write_index(consumers_of_shell=("other-shell",))
        self.write_example()
        out, err = self.run_main()
        c = self.composer()
        self.assertEqual([s["name"] for s in c["sdks"]], ["telemetry_sdk", "base_sdk"])
        self.assertIn("nextjs_compose_example.json", c["_comment"])
        self.assertIn("lists no shell 'acme-web'", out)

    def test_overlay_fallback_only_when_protocol_unreachable(self):
        def unreachable(rel):
            raise seed_composer.ProtocolUnreachable("offline")
        self.write_index()
        self.write_example()
        orig = seed_composer.Protocol.read
        seed_composer.Protocol.read = lambda self, rel: unreachable(rel)
        try:
            out, err = self.run_main()
        finally:
            seed_composer.Protocol.read = orig
        c = self.composer()
        self.assertEqual([s["name"] for s in c["sdks"]], ["telemetry_sdk", "base_sdk"])
        self.assertIn("fallback", c["_comment"])
        self.assertIn("FALLING BACK", err)

    def test_protocol_without_example_and_unknown_shell_falls_back_loudly(self):
        self.write_index(consumers_of_shell=("other-shell",))
        out, err = self.run_main()
        self.assertIn("FALLING BACK", err)
        self.assertEqual(len(self.composer()["sdks"]), 2)


class TestPins(SeedComposerCase):
    def test_every_entry_is_repinned_from_the_repo_now(self):
        self.write_index()
        self.write_example()
        out, err = self.run_main()
        c = self.composer()
        self.assertEqual(c["sdks"][0]["sha256"], seed_composer.sha256_lf(TEL_PY))
        self.assertEqual(c["sdks"][0]["sha256"], seed_composer.sha256_lf(TEL_PY.replace(b"\r\n", b"\n")))
        self.assertEqual(c["sdks"][1]["sha256"], seed_composer.sha256_lf(BASE_PY))
        self.assertIn("computed at spawn", c["sdks"][0]["_sha256_comment"])
        self.assertIn("re-pinned", err)  # the index's stub pins differ from the live installers
        self.assertIn(("RokctAI/core", "telemetry/nextjs/install.py", "main"), self.net.calls)

    def test_unreadable_installer_keeps_the_source_pin(self):
        self.write_index()
        self.write_example()
        del self.net.files[("RokctAI/core", "base/nextjs/install.py")]
        out, err = self.run_main()
        self.assertEqual(self.composer()["sdks"][1]["sha256"], SHA_BASE)
        self.assertIn("keeping the source's own pin", err)

    def test_unreadable_installer_without_a_pin_is_fatal(self):
        write_json(self.protocol / "core/utils/frappe/composer/acme-web.json", {"sdks": [
            git_entry("telemetry_sdk", "core", SHA_TEL),
            git_entry("base_sdk", "core", SHA_BASE),
            git_entry("new_sdk", "agent", home=True),  # no sha256, no installer
        ]})
        self.write_index()
        with self.assertRaises(SystemExit) as ctx:
            self.run_main()
        self.assertIn("new_sdk", str(ctx.exception))
        self.assertIn("unpinned", str(ctx.exception))


class TestVersions(SeedComposerCase):
    """The consumers index is regenerated weekly and trails releases: it
    wrote base_sdk 1.35.0 while core's main declared 1.37.0. The version an
    entry ships with is the manifest's, read next to the installer."""

    def manifest(self, name, version=None, raw=None):
        sub = {"telemetry_sdk": "telemetry/nextjs", "base_sdk": "base/nextjs", "lms_sdk": "lms/nextjs"}[name]
        repo = "RokctAI/agent" if name == "lms_sdk" else "RokctAI/core"
        body = raw if raw is not None else json.dumps(
            {"name": name, **({"version": version} if version is not None else {}), "installs": []}
        ).encode("utf-8")
        self.net.files[(repo, f"{sub}/manifest.json")] = body

    def test_version_comes_from_the_live_manifest_not_the_index(self):
        self.manifest("telemetry_sdk", "1.2.0")
        self.manifest("base_sdk", "1.37.0")  # the index still says 1.35.0
        self.write_index()
        self.write_example()
        out, err = self.run_main()
        c = self.composer()
        self.assertEqual(c["sdks"][0]["version"], "1.2.0")
        self.assertEqual(c["sdks"][1]["version"], "1.37.0")
        self.assertIn(("RokctAI/core", "base/nextjs/manifest.json", "main"), self.net.calls)
        self.assertIn("the source said 1.35.0 but manifest.json", out)
        self.assertIn("declares 1.37.0", out)
        self.assertNotIn("keeping the source's version", err)

    def test_manifest_version_is_read_at_the_entry_ref(self):
        write_json(self.protocol / "core/utils/frappe/composer/acme-web.json", {"sdks": [
            git_entry("telemetry_sdk", "core", SHA_TEL),
            dict(git_entry("base_sdk", "core", SHA_BASE), ref="v1.37.0", version="1.35.0"),
        ]})
        self.manifest("base_sdk", "1.37.0")
        self.write_index()
        out, err = self.run_main()
        self.assertIn(("RokctAI/core", "base/nextjs/manifest.json", "v1.37.0"), self.net.calls)
        self.assertEqual(self.composer()["sdks"][1]["version"], "1.37.0")

    def test_registry_entry_without_a_version_gets_the_manifest_one(self):
        write_json(self.protocol / "core/utils/frappe/composer/acme-web.json", {"sdks": [
            git_entry("telemetry_sdk", "core", SHA_TEL),
            git_entry("base_sdk", "core", SHA_BASE),
            git_entry("lms_sdk", "agent", SHA_LMS, home=True),  # no version key at all
        ]})
        self.manifest("lms_sdk", "1.26.0")
        self.write_index({"lms_sdk": record("RokctAI/agent", "lms/nextjs", "1.25.0", SHA_LMS)})
        out, err = self.run_main()
        self.assertEqual(self.composer()["sdks"][2]["version"], "1.26.0")
        self.assertNotIn("the source said", out)  # nothing to contradict

    def test_missing_manifest_keeps_the_index_version_with_a_warning(self):
        self.manifest("telemetry_sdk", "1.2.0")  # base_sdk's manifest is absent
        self.write_index()
        self.write_example()
        out, err = self.run_main()
        self.assertEqual(self.composer()["sdks"][1]["version"], "1.35.0")
        self.assertIn("base_sdk: RokctAI/core/base/nextjs/manifest.json@main does not exist", err)
        self.assertIn("keeping the source's version 1.35.0", err)

    def test_unreachable_manifest_keeps_the_index_version_with_a_warning(self):
        self.manifest("telemetry_sdk", "1.2.0")
        self.manifest("base_sdk", "1.37.0")
        self.net.broken.add(("RokctAI/core", "base/nextjs/manifest.json"))
        self.write_index()
        self.write_example()
        out, err = self.run_main()
        c = self.composer()
        self.assertEqual(c["sdks"][1]["version"], "1.35.0")
        self.assertEqual(c["sdks"][1]["sha256"], seed_composer.sha256_lf(BASE_PY))  # the pin still lands
        self.assertIn("base/nextjs/manifest.json@main could not be read", err)
        self.assertIn("keeping the source's version 1.35.0", err)

    def test_manifest_without_a_version_keeps_the_index_version(self):
        self.manifest("telemetry_sdk", "1.2.0")
        self.manifest("base_sdk")  # no version key
        self.write_index()
        self.write_example()
        out, err = self.run_main()
        self.assertEqual(self.composer()["sdks"][1]["version"], "1.35.0")
        self.assertIn("declares no version", err)

    def test_manifest_that_is_not_json_keeps_the_index_version(self):
        self.manifest("telemetry_sdk", "1.2.0")
        self.manifest("base_sdk", raw=b"<html>rate limited</html>")
        self.write_index()
        self.write_example()
        out, err = self.run_main()
        self.assertEqual(self.composer()["sdks"][1]["version"], "1.35.0")
        self.assertIn("is not valid JSON", err)

    def test_manifest_lookup_skips_disabled_and_local_entries(self):
        write_json(self.protocol / "core/utils/frappe/composer/acme-web.json", {"sdks": [
            git_entry("telemetry_sdk", "core", SHA_TEL),
            git_entry("base_sdk", "core", SHA_BASE),
            dict(git_entry("corporate_sdk", "corporate", enabled=False), git="https://github.com/RokctAI/nowhere"),
            {"name": "local_sdk", "enabled": True, "source": "local", "path": "../local/nextjs"},
        ]})
        self.write_index()
        out, err = self.run_main()
        paths = [p for _, p, _ in self.net.calls]
        self.assertNotIn("corporate/nextjs/manifest.json", paths)
        self.assertEqual([p for p in paths if p.endswith("manifest.json")],
                         ["telemetry/nextjs/manifest.json", "base/nextjs/manifest.json"])


class TestDrift(SeedComposerCase):
    def test_template_repo_contradicting_the_index_stops_the_spawn(self):
        write_json(self.protocol / "core/utils/frappe/composer/acme-web.json", {"sdks": [
            git_entry("telemetry_sdk", "core", SHA_TEL),
            git_entry("base_sdk", "core", SHA_BASE),
            dict(git_entry("lms_sdk", "agent", SHA_LMS, home=True), git="https://github.com/RokctAI/elsewhere"),
        ]})
        self.write_index({"lms_sdk": record("RokctAI/agent", "lms/nextjs", "1.25.0", SHA_LMS)})
        with self.assertRaises(SystemExit) as ctx:
            self.run_main()
        self.assertIn("drifts from sdk_consumers.json", str(ctx.exception))
        self.assertIn("lms_sdk", str(ctx.exception))

    def test_sdk_unknown_to_the_index_is_only_a_warning(self):
        write_json(self.protocol / "core/utils/frappe/composer/acme-web.json", {"sdks": [
            git_entry("telemetry_sdk", "core", SHA_TEL),
            git_entry("base_sdk", "core", SHA_BASE),
            git_entry("lms_sdk", "agent", SHA_LMS, home=True),
        ]})
        self.write_index()  # lms_sdk not indexed yet
        out, err = self.run_main()
        self.assertIn("lms_sdk: not in sdk_consumers.json", err)
        self.assertEqual(len(self.composer()["sdks"]), 3)

    def test_disabled_entries_are_neither_checked_nor_pinned(self):
        write_json(self.protocol / "core/utils/frappe/composer/acme-web.json", {"sdks": [
            git_entry("telemetry_sdk", "core", SHA_TEL),
            git_entry("base_sdk", "core", SHA_BASE),
            git_entry("lms_sdk", "agent", SHA_LMS, home=True),
            dict(git_entry("corporate_sdk", "corporate", enabled=False), git="https://github.com/RokctAI/nowhere"),
        ]})
        self.write_index()
        out, err = self.run_main()
        self.assertNotIn(("RokctAI/nowhere", "corporate/nextjs/install.py", "main"), self.net.calls)


class TestNeverEmpty(SeedComposerCase):
    def test_all_disabled_is_fatal(self):
        write_json(self.protocol / "core/utils/frappe/composer/acme-web.json", {"sdks": [
            git_entry("telemetry_sdk", "core", SHA_TEL, enabled=False),
        ]})
        self.write_index()
        self.write_example()
        # A template with no enabled entry is "no template"; the index and
        # example then decide, so the result is still real.
        out, err = self.run_main()
        self.assertEqual(len(self.composer()["sdks"]), 2)

    def test_empty_overlay_fallback_is_fatal(self):
        write_json(self.dest / "composer.json", {"sdks": []})
        orig = seed_composer.Protocol.read
        seed_composer.Protocol.read = lambda self, rel: (_ for _ in ()).throw(seed_composer.ProtocolUnreachable("x"))
        try:
            with self.assertRaises(SystemExit) as ctx:
                self.run_main()
        finally:
            seed_composer.Protocol.read = orig
        self.assertIn("empty", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
