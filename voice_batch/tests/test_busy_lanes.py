import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ci"))
import busy_lanes  # noqa: E402


class BusyLanesTest(unittest.TestCase):
    def test_titles_map_to_lanes(self):
        titles = [
            "Voice batch: voice_batches/inbox/r3_packs_0_gradeR.json",
            "Voice batch: voice_batches/inbox/r3_packs_1_gradeR_kavitha.json",
            "Voice batch: voice_batches/inbox/tutor_011_greetings.json",
            "",
        ]
        self.assertEqual(busy_lanes.busy(titles), ["r3", "voice_batches/inbox/tutor_011_greetings.json"])

    def test_untitled_run_is_unknown(self):
        # scheduled/push runs, and runs started before run-name, carry no batch
        self.assertEqual(busy_lanes.busy(["Voice batch"]), ["*"])

    def test_lane_of_a_batch(self):
        self.assertEqual(busy_lanes.lane("voice_batches/inbox/r3_packs_0_gradeR.json"), "r3")
        self.assertEqual(busy_lanes.lane("voice_batches/inbox/a.json"), "voice_batches/inbox/a.json")


if __name__ == "__main__":
    unittest.main()
