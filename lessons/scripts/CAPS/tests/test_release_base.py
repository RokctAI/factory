#!/usr/bin/env python3
# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""release_on_complete's empty tag base: every lesson tag is cut at one
empty commit on the release repo (so the release's auto "Source code"
archive is empty), the base is created on first use, and an existing base
is reused. gh is mocked at subprocess.run — no network.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/CAPS/tests -v
"""

import json
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import release_on_complete as roc  # noqa: E402

REPO = "RokctAI/agent"
BASE = "b" * 40
OTHER = "c" * 40


class FakeGh:
    """Minimal stand-in for the GitHub git-data API behind `gh api`."""

    def __init__(self, refs=None, reject_empty_tree=False):
        self.refs = dict(refs or {})  # "tags/<name>" -> sha
        self.reject_empty_tree = reject_empty_tree
        self.calls = []

    def __call__(self, cmd, input=None, capture_output=False, text=False,
                 check=False):
        body = json.loads(input) if input else None
        self.calls.append((cmd, body))
        if cmd[:2] == ["gh", "release"]:
            return subprocess.CompletedProcess(cmd, 0, "", "")
        method, path = cmd[3], cmd[4]
        prefix = f"repos/{REPO}/git/"
        assert path.startswith(prefix), path
        path = path[len(prefix):]
        if method == "GET" and path.startswith("ref/"):
            name = path[len("ref/"):]
            if name not in self.refs:
                return self._out(1, err="HTTP 404: Not Found")
            return self._out(0, {"object": {"type": "commit",
                                            "sha": self.refs[name]}})
        if method == "POST" and path == "commits":
            if self.reject_empty_tree and body["tree"] == roc.EMPTY_TREE_SHA:
                return self._out(1, err="HTTP 422: Tree SHA does not exist")
            return self._out(0, {"sha": BASE, "tree": {"sha": body["tree"]}})
        if method == "POST" and path == "trees":
            assert body == {"tree": []}
            return self._out(0, {"sha": "e" * 40})
        if method == "POST" and path == "refs":
            name = body["ref"][len("refs/"):]
            if name in self.refs:
                return self._out(1, err="HTTP 422: Reference already exists")
            self.refs[name] = body["sha"]
            return self._out(0, {"ref": body["ref"]})
        raise AssertionError(f"unexpected gh call {cmd}")

    @staticmethod
    def _out(code, data=None, err=""):
        return subprocess.CompletedProcess(
            [], code, json.dumps(data) if data is not None else "", err)

    def posts(self, suffix):
        return [b for c, b in self.calls
                if c[:2] == ["gh", "api"] and c[3] == "POST"
                and c[4].endswith(suffix)]


class ReleaseBaseTests(unittest.TestCase):
    def run_with(self, fake, fn, *args):
        with mock.patch.object(roc.subprocess, "run", fake):
            return fn(*args)

    def test_base_missing_is_created_and_tagged(self):
        fake = FakeGh()
        sha = self.run_with(fake, roc.ensure_release_base, REPO)
        self.assertEqual(sha, BASE)
        (commit,) = fake.posts("git/commits")
        self.assertEqual(commit["tree"], roc.EMPTY_TREE_SHA)
        self.assertEqual(commit["parents"], [])
        self.assertEqual(commit["message"], roc.RELEASE_BASE_MESSAGE)
        self.assertEqual(fake.refs, {f"tags/{roc.RELEASE_BASE_TAG}": BASE})

    def test_base_present_is_reused(self):
        fake = FakeGh(refs={f"tags/{roc.RELEASE_BASE_TAG}": OTHER})
        sha = self.run_with(fake, roc.ensure_release_base, REPO)
        self.assertEqual(sha, OTHER)
        self.assertEqual(fake.posts("git/commits"), [])
        self.assertEqual(fake.posts("git/refs"), [])

    def test_empty_tree_rejected_falls_back_to_created_tree(self):
        fake = FakeGh(reject_empty_tree=True)
        sha = self.run_with(fake, roc.ensure_release_base, REPO)
        self.assertEqual(sha, BASE)
        self.assertEqual(fake.posts("git/trees"), [{"tree": []}])
        self.assertEqual(fake.posts("git/commits")[-1]["tree"], "e" * 40)
        self.assertEqual(fake.posts("git/commits")[-1]["parents"], [])

    def test_lesson_tag_created_at_base_then_released_on_it(self):
        fake = FakeGh(refs={f"tags/{roc.RELEASE_BASE_TAG}": BASE})
        ident = {"id": "maths_g10_t1_x_y"}
        self.run_with(fake, roc.create_release, "lesson-x", REPO, ident,
                      Path("/out"), BASE)
        self.assertEqual(fake.refs["tags/lesson-x"], BASE)
        release = [c for c, _ in fake.calls if c[:2] == ["gh", "release"]]
        self.assertEqual(len(release), 1)
        cmd = release[0]
        self.assertEqual(cmd[2:4], ["create", "lesson-x"])
        self.assertIn("--verify-tag", cmd)
        self.assertNotIn("--target", cmd)
        # tag ref is created before the release
        kinds = [c[1] for c, _ in fake.calls]
        self.assertLess(max(i for i, k in enumerate(kinds) if k == "api"),
                        kinds.index("release"))

    def test_existing_lesson_tag_at_base_is_reused(self):
        fake = FakeGh(refs={"tags/lesson-x": BASE})
        self.run_with(fake, roc.create_release, "lesson-x", REPO,
                      {"id": "x"}, Path("/out"), BASE)
        self.assertEqual(fake.posts("git/refs"), [])

    def test_stray_lesson_tag_elsewhere_refuses_to_release(self):
        fake = FakeGh(refs={"tags/lesson-x": OTHER})
        with self.assertRaises(roc.ReleaseError):
            self.run_with(fake, roc.create_release, "lesson-x", REPO,
                          {"id": "x"}, Path("/out"), BASE)
        self.assertFalse([c for c, _ in fake.calls
                          if c[:2] == ["gh", "release"]])


if __name__ == "__main__":
    unittest.main()
