import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import leak_guard as lg  # noqa: E402


class Files(unittest.TestCase):
    def test_audio_and_content_fail(self):
        errs = lg.check_files(["social/facebook/assets/voice_open.wav", "school/a.md",
                               "radio_ads/out/x/x.mp3", "voice_batch/run.py"])
        self.assertEqual(len(errs), 3)


class Workflows(unittest.TestCase):
    def test_upload_artifact_fails_unless_allowed(self):
        wf = "      - uses: actions/upload-artifact@v4\n"
        self.assertEqual(len(lg.check_workflow("w", wf)), 1)
        self.assertEqual(lg.check_workflow("w", wf.rstrip() + "  # leak-guard: allow public build log\n"), [])
        self.assertEqual(lg.check_workflow("w", "# - uses: actions/upload-artifact@v4\n"), [])

    def test_cache_paths(self):
        safe = ("      - name: Restore model weights\n"
                "        uses: actions/cache/restore@v4\n"
                "        with:\n"
                "          path: ${{ env.HF_HOME }}/hub\n"
                "          key: k\n")
        self.assertEqual(lg.check_workflow("w", safe), [])
        bad = ("      - name: Restore line cache\n"
               "        uses: actions/cache/restore@v4\n"
               "        with:\n"
               "          path: |\n"
               "            ${{ env.HF_HOME }}/hub\n"
               "            radio_ads/cache/tts\n"
               "          key: k\n")
        errs = lg.check_workflow("w", bad)
        self.assertEqual(len(errs), 1)
        self.assertIn("radio_ads/cache/tts", errs[0])

    def test_pull_request_target_fails(self):
        self.assertEqual(len(lg.check_workflow("w", "on:\n  pull_request_target:\n")), 1)


if __name__ == "__main__":
    unittest.main()
