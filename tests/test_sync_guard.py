import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import sync_guard  # noqa: E402


def sh(cwd, *args):
    subprocess.run(args, cwd=cwd, check=True, capture_output=True)


class SyncGuardTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = self.d = self.tmp.name
        sh(d, "git", "init", "-q")
        sh(d, "git", "config", "user.email", "t@t")
        sh(d, "git", "config", "user.name", "t")
        os.makedirs(os.path.join(d, ".rokct", "workflows"))
        for name, body in {
            ".rokct/memory.md": "## Safe ID\nsinyage.f74d39\n",
            ".rokct/decision_log.md": "ADR-001\n",
            ".rokct/workflows/forget_repos.py": "print(1)\n",
            ".rokct/.sync_ready": "",
        }.items():
            with open(os.path.join(d, name), "w") as f:
                f.write(body)
        sh(d, "git", "add", "-A")
        sh(d, "git", "commit", "-qm", "base")

    def tearDown(self):
        self.tmp.cleanup()

    def test_bot_safe_id_is_dropped(self):
        p = os.path.join(self.d, ".rokct", "memory.md")
        with open(p, "a") as f:
            f.write("\n## Safe ID\n\n41898282+github-actions[bot].0b4d71\n")
        self.assertEqual(sync_guard.main(self.d), 0)
        with open(p) as f:
            self.assertNotIn("github-actions", f.read())

    def test_deleted_tracked_files_are_restored(self):
        os.remove(os.path.join(self.d, ".rokct", "decision_log.md"))
        os.remove(os.path.join(self.d, ".rokct", "workflows", "forget_repos.py"))
        self.assertEqual(sync_guard.main(self.d), 0)
        self.assertTrue(os.path.exists(os.path.join(self.d, ".rokct", "decision_log.md")))
        self.assertTrue(
            os.path.exists(os.path.join(self.d, ".rokct", "workflows", "forget_repos.py"))
        )

    def test_unrestorable_loss_fails(self):
        os.remove(os.path.join(self.d, ".rokct", "decision_log.md"))
        orig = sync_guard.git

        def no_checkout(repo, *args):
            if args and args[0] == "checkout" and "decision_log" in args[-1]:
                return ""
            return orig(repo, *args)

        sync_guard.git = no_checkout
        try:
            self.assertEqual(sync_guard.main(self.d), 1)
        finally:
            sync_guard.git = orig

    def test_marker_removal_is_allowed(self):
        os.remove(os.path.join(self.d, ".rokct", ".sync_ready"))
        self.assertEqual(sync_guard.main(self.d), 0)


if __name__ == "__main__":
    unittest.main()
