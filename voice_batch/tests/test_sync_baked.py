"""ci/sync_baked_to_agent.py on temp checkouts. Model-free.

    python -m pytest voice_batch/tests/test_sync_baked.py
"""
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE / "ci"))
sys.path.insert(0, str(HERE))
import sync_baked_to_agent as sb  # noqa: E402

V = "voices/team/tutors/CAPS"
A = "lms/team/tutors/CAPS"


def put(p: Path, data: bytes = b"x"):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)


class SyncBaked(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = Path(self.tmp.name)
        self.voices, self.agent = d / "lessons", d / "agent"
        put(self.voices / V / "tutor_001/samples/sample_line.m4a", b"new")
        put(self.voices / V / "tutor_002/samples/sample_line.m4a", b"two")
        put(self.voices / V / "tutor_004/samples/sample_line.m4a", b"four")  # not baked
        put(self.voices / V / "tutor_001/greetings/01.m4a", b"g")  # downloaded, not baked
        put(self.agent / A / "tutor_001/samples/sample_line.m4a", b"old")
        put(self.agent / A / "tutor_003/samples/gone.m4a", b"gone")
        put(self.agent / A / "tutor_001/greetings/01.m4a", b"keep")

    def tearDown(self):
        self.tmp.cleanup()

    def test_only_first_three_tutors_samples(self):
        r = sb.sync(self.voices, self.agent)
        self.assertEqual(r["added"], ["tutor_002/samples/sample_line.m4a"])
        self.assertEqual(r["updated"], ["tutor_001/samples/sample_line.m4a"])
        self.assertEqual(r["removed"], ["tutor_003/samples/gone.m4a"])
        self.assertEqual((self.agent / A / "tutor_001/samples/sample_line.m4a").read_bytes(), b"new")
        self.assertFalse((self.agent / A / "tutor_004").exists())
        # Files outside the baked sample folders are never touched.
        self.assertEqual((self.agent / A / "tutor_001/greetings/01.m4a").read_bytes(), b"keep")

    def test_check_changes_nothing(self):
        r = sb.sync(self.voices, self.agent, check=True)
        self.assertEqual(len(r["added"]) + len(r["updated"]) + len(r["removed"]), 3)
        self.assertEqual((self.agent / A / "tutor_001/samples/sample_line.m4a").read_bytes(), b"old")
        self.assertTrue((self.agent / A / "tutor_003/samples/gone.m4a").exists())

    def test_second_run_is_a_no_op(self):
        sb.sync(self.voices, self.agent)
        r = sb.sync(self.voices, self.agent)
        self.assertEqual(r, {"added": [], "updated": [], "removed": []})

    def test_refuses_empty_voice_checkout(self):
        empty = Path(self.tmp.name) / "empty"
        empty.mkdir()
        with self.assertRaises(SystemExit):
            sb.sync(empty, self.agent)
        self.assertTrue((self.agent / A / "tutor_003/samples/gone.m4a").exists())


if __name__ == "__main__":
    unittest.main()
