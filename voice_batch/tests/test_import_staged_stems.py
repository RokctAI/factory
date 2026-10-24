"""ci/import_staged_stems.py: staged sandbox records go to lessons main
unless CI has passed lines there the staged record lacks. Model-free.

    python -m unittest voice_batch/tests/test_import_staged_stems.py
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "ci"))
import import_staged_stems as I  # noqa: E402

REL = "maths/session/grade9/term4/topic-a/lesson-b"


def manifest(root: Path, persona: str, keys: list[str]) -> Path:
    d = root / "school/curriculum/CAPS" / REL / "voice" / persona
    d.mkdir(parents=True, exist_ok=True)
    p = d / "manifest.json"
    p.write_text(json.dumps({"lines": [{"key": k, "file": f"{k}.mp3"} for k in keys]}), encoding="utf-8")
    return p


class Import(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.stage, self.main = Path(tmp.name) / "stage", Path(tmp.name) / "main"
        (self.main / "school/curriculum/CAPS" / REL).mkdir(parents=True)

    def run_import(self):
        with mock.patch.object(I.subprocess, "run") as run:
            I.main(["--stage", str(self.stage), "--lessons-root", str(self.main)])
        return run

    def test_staged_record_is_copied_and_pushed(self):
        manifest(self.stage, "tutor_001", ["seg00", "seg01"])
        self.assertEqual(I.staged(self.stage), {"tutor_001": [REL]})
        run = self.run_import()
        self.assertEqual(run.call_count, 1)
        cmd = run.call_args.args[0]
        self.assertIn("push", cmd)
        self.assertEqual(cmd[cmd.index("--lessons") + 1], REL)
        self.assertEqual(cmd[cmd.index("--stems-root") + 1], str(self.stage / I.STEMS_DIR))
        copied = self.main / "school/curriculum/CAPS" / REL / "voice/tutor_001/manifest.json"
        self.assertEqual(I.keys_passed(copied), {"seg00", "seg01"})

    def test_ci_work_on_main_is_never_overwritten(self):
        manifest(self.stage, "tutor_001", ["seg00"])
        theirs = manifest(self.main, "tutor_001", ["seg00", "seg05"])
        run = self.run_import()
        run.assert_not_called()
        self.assertEqual(I.keys_passed(theirs), {"seg00", "seg05"})


if __name__ == "__main__":
    unittest.main()
