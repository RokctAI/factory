"""Resumable renders (resume.py, run.py's chunk driver, merge_manifest's
"remaining") and the scheduled pending scan (pending.py). Model-free.

    python -m pytest voice_batch/tests/test_resume.py
"""
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

try:
    import yaml
except ImportError:  # the workflow checks skip without PyYAML
    yaml = None

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import lines  # noqa: E402
import merge_manifest  # noqa: E402
import pending  # noqa: E402
import qc_failed  # noqa: E402
import resume  # noqa: E402
from test_assistants import AID, make_agent  # noqa: E402

heavy = {m: types.ModuleType(m) for m in ("numpy", "librosa", "soundfile", "faster_whisper", "resemblyzer")
         if importlib.util.find_spec(m) is None}
with mock.patch.dict(sys.modules, heavy):
    import run  # noqa: E402

VOICE = "voice_b_sister"
REF_SHA = "ab" * 32
WORKFLOW = HERE.parent / ".github/workflows/voice_batch.yml"


class Clock:
    def __init__(self):
        self.t = 1000.0

    def __call__(self):
        return self.t


def passing(it, take):
    return {"id": it["id"], "status": "pass", "final_path": str(take), "sha256": run.sha256_file(take),
            "duration_s": 1.0, "seeds": [11], "median_f0_hz": 240.0, "similarity": 0.9,
            "asr_match": True, "similarity_threshold": 0.83, "upward_swings": 0, "rms_dbfs": -20,
            "peak": 0.5, "pauses_ms": [], "tail_db": -60, "seeds_tried": [11],
            "takes": [{"seed": 11} for _ in it["sentences"]]}


def failing(it):
    r = {"id": it["id"], "status": "fail", "seeds_tried": [11, 22, 33, 44, 55], "duration_s": 1.0,
         "median_f0_hz": 150.0, "similarity": 0.7, "similarity_threshold": 0.83, "asr_match": False,
         "gate": {"f0": False, "asr": True}}
    r["rounds"] = [qc_failed.round_record(n, s, r) for n, s in enumerate(run.SEED_ROUNDS, 1)]
    return r


class Budget(unittest.TestCase):
    def test_limit_and_estimate(self):
        c = Clock()
        b = resume.Budget(10, clock=c)
        self.assertTrue(b.allows(100))          # no rate yet: the first round always runs
        c.t += 240
        b.record(4, 240)                        # 60 s a take
        self.assertTrue(b.allows(6))            # 240 + 360 = 600 <= 600
        self.assertFalse(b.allows(7))           # would end past the budget
        c.t += 360
        self.assertFalse(b.allows(0))           # out of time
        self.assertTrue(resume.Budget(0, clock=c).allows(10 ** 6))   # 0 = unlimited

    def test_start_from_job_start(self):
        c = Clock()
        self.assertEqual(resume.Budget(5, start=c.t - 120, clock=c).elapsed(), 120)

    def test_checkpoint_throttle(self):
        c, calls = Clock(), []
        ck = resume.Checkpoint(["push"], every_minutes=15, clock=c, run=lambda cmd: calls.append(cmd) or 0)
        self.assertTrue(ck.push(force=True))
        self.assertFalse(ck.push())             # too soon
        c.t += 15 * 60
        self.assertTrue(ck.push())
        self.assertEqual(len(calls), 2)
        bad = resume.Checkpoint(["push"], clock=c, run=lambda cmd: 1)
        self.assertFalse(bad.push(force=True))  # a failed push is a warning, not fatal


class RenderRoundsBudget(unittest.TestCase):
    """The real render_rounds with the render and QC subprocesses faked: a
    line still failing after round 1 is 'remaining' (not failed) when round 2
    would not fit in the budget; a passed line stays passed."""

    def test_stops_before_a_round_that_does_not_fit(self):
        c = Clock()
        with tempfile.TemporaryDirectory() as d:
            work = Path(d)
            items = [{"id": "a", "render_text": ["One."]}, {"id": "b", "render_text": ["Two."]}]
            calls = []

            def fake_run(cmd, check):
                calls.append(Path(cmd[1]).name)
                if Path(cmd[1]).name == "qc.py":
                    c.t += 600                  # round 1: 6 takes in 600 s
                    (work / "results.json").write_text(json.dumps([
                        {"id": "a", "status": "pass"}, {"id": "b", "status": "fail", "lacking": [{"key": "b#1"}]}]))

            args = types.SimpleNamespace(model_path="m", asr_model="small.en", f0_target=102.0, f0_tolerance=8.0,
                                         language="en", pace_wpm=149, pace_tolerance=15,
                                         budget=resume.Budget(11, clock=c))
            with mock.patch.object(run.subprocess, "run", fake_run), mock.patch.object(run.time, "time", c):
                out = run.render_rounds(items, work, Path("ref.wav"), Path("s"), args, "t")
            # 600 s elapsed + round 2 (1 take at 100 s a take) > 660 s: round 2 never started
            self.assertEqual(calls, ["render_takes.py", "qc.py"])
            self.assertEqual([(r["id"], r["status"]) for r in out], [("a", "pass"), ("b", "remaining")])


class RoundHistory(unittest.TestCase):
    def test_every_round_failing_gates_are_recorded(self):
        with tempfile.TemporaryDirectory() as d:
            work = Path(d)
            items = [{"id": "a", "render_text": ["One."]}]
            rounds = iter([
                {"id": "a", "status": "incomplete", "lacking": [{"key": "a#1", "tier": 0, "heard": ["Won.", "On."]}]},
                {"id": "a", "status": "fail", "lacking": [{"key": "a#1", "tier": 2}], "asr_word_errors": 1,
                 "asr_transcript": "Won.",
                 "gate": {"asr": False, "loudness": False, "f0": True}, "checks": {"integrated_db": -25.5}},
                {"id": "a", "status": "fail", "lacking": [], "gate": {"lead_in": False, "onset": False},
                 "checks": {"lead_in_ms": 20.0, "head_rms_dbfs": -30.0, "onset_rise_ms": 1.0}, "seeds_tried": [11, 22, 33, 44, 55]},
            ])

            def fake_run(cmd, check):
                if Path(cmd[1]).name == "qc.py":
                    (work / "results.json").write_text(json.dumps([next(rounds)]))

            args = types.SimpleNamespace(model_path="m", asr_model="small.en", f0_target=102.0, f0_tolerance=8.0,
                                         language="en", pace_wpm=149, pace_tolerance=15)
            with mock.patch.object(run.subprocess, "run", fake_run):
                (r,) = run.render_rounds(items, work, Path("ref.wav"), Path("s"), args, "t")
        self.assertEqual(r["status"], "fail")
        self.assertEqual([x["round"] for x in r["rounds"]], [1, 2, 3])
        self.assertEqual(r["rounds"][0]["failing"], {"asr": {"sentences_without_word_exact_take": 1,
                                                             "heard": [{"sentence": 1, "heard": ["Won.", "On."]}]}})
        self.assertEqual(r["rounds"][1]["failing"], {"asr": {"asr_word_errors": 1, "asr_transcript": "Won."},
                                                     "loudness": {"integrated_db": -25.5}})
        self.assertEqual(r["rounds"][2]["failing"], {"lead_in": {"lead_in_ms": 20.0},
                                                     "onset": {"head_rms_dbfs": -30.0, "onset_rise_ms": 1.0}})
        self.assertEqual(r["rounds"][2]["seeds"], [55])


class ResumableRun(unittest.TestCase):
    """run_tutor (kind assistant fixture) with the rounds faked and a fake clock."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.d = Path(self.tmp.name)
        make_agent(self.d, {"agreement_in_place": False})
        self.ref = self.d / "ref.wav"
        self.ref.write_bytes(b"ref")
        self.take = self.d / "take.wav"
        self.take.write_bytes(b"audio")
        self.out = self.d / "github_output"
        self.clock = Clock()
        self.rendered = []
        self.fail_ids = set()
        self.pushes = []

    def tearDown(self):
        self.tmp.cleanup()

    def fake_rounds(self, items, *a, **k):
        self.rendered.append([it["id"] for it in items])
        self.clock.t += 100 * 60                # every chunk takes 100 minutes
        return [failing(it) if it["id"] in self.fail_ids else passing(it, self.take) for it in items]

    def run_once(self, budget_minutes=150, series=None):
        self.out.write_text("")
        args = types.SimpleNamespace(kind="assistant", tutor=AID, category="timekeeping", lines="", voice=VOICE,
                                     ref_sha256=REF_SHA, model_path="/m", work=str(self.d / "w"),
                                     asr_model="small.en", language="en", f0_target=241.0, f0_tolerance=25.0,
                                     pace_wpm=149, pace_tolerance=15, chunk_lines=1,
                                     budget=resume.Budget(budget_minutes, clock=self.clock),
                                     checkpoint=resume.Checkpoint(["push"], 15, clock=self.clock,
                                                                  run=lambda c: self.pushes.append(c) or 0))
        env = {"GITHUB_OUTPUT": str(self.out), "RENDER_SERIES": series or ""}
        with mock.patch.object(run, "render_rounds", self.fake_rounds), mock.patch.object(run, "versions", lambda: {}), \
                mock.patch.object(run.pronunciations, "load", lambda: {}), mock.patch.dict(os.environ, env):
            self.assertEqual(run.run_tutor(args, self.d, self.ref, self.d / "lms/team/scripts"), 0)
        outputs = dict(ln.split("=", 1) for ln in self.out.read_text().split())
        return outputs, json.loads((self.d / lines.team_rel(AID) / f"{VOICE}_manifest.timekeeping.json").read_text())

    def ids(self):
        return [f"{AID}/timekeeping/{s}" for s in ("halfway", "five_min_warning", "wrap_up")]

    def test_budget_stop_is_incomplete_then_second_run_skips_pushed_lines(self):
        outputs, m = self.run_once()
        # 0 -> 100 -> 200 min: the third chunk does not start past 150.
        self.assertEqual(outputs, {"incomplete": "true", "remaining": "1"})
        self.assertEqual(len(m["lines"]), 2)
        self.assertEqual(len(self.rendered), 2)
        self.assertEqual(m["remaining"], [i for i in self.ids() if i not in {e["id"] for e in m["lines"]}])
        # one forced push up front (remaining marked), one after each chunk
        self.assertEqual(len(self.pushes), 3)
        # Second run (a continuation): the two installed lines are skipped.
        outputs, m = self.run_once()
        self.assertEqual(len(self.rendered), 3)
        self.assertEqual(len(self.rendered[-1]), 1)
        self.assertNotIn(self.rendered[-1][0], [x for r in self.rendered[:2] for x in r])
        self.assertEqual(outputs, {"incomplete": "false", "remaining": "0"})
        self.assertEqual(len(m["lines"]), 3)
        self.assertNotIn("remaining", m)
        # Third run: nothing to render at all.
        outputs, _ = self.run_once()
        self.assertEqual(len(self.rendered), 3)
        self.assertEqual(outputs, {"incomplete": "false", "remaining": "0"})

    def test_final_failed_lines_are_not_incomplete(self):
        self.fail_ids = {self.ids()[1]}
        outputs, m = self.run_once(budget_minutes=0, series="77")
        self.assertEqual(outputs, {"incomplete": "false", "remaining": "0"})
        self.assertEqual([e["id"] for e in m["failed"]], [self.ids()[1]])
        self.assertEqual(m["failed"][0]["series"], "77")
        self.assertNotIn("remaining", m)
        self.assertEqual(len(self.rendered), 3)                    # one chunk per line
        # A continuation in the same series does not retry it ...
        outputs, _ = self.run_once(budget_minutes=0, series="77")
        self.assertEqual(len(self.rendered), 3)
        self.assertEqual(outputs, {"incomplete": "false", "remaining": "0"})
        # ... a fresh run (new series) does, once.
        self.run_once(budget_minutes=0, series="78")
        self.assertEqual(self.rendered[3:], [[self.ids()[1]]])


    def test_final_failed_line_is_logged_in_qc_failed_then_cleared_when_it_passes(self):
        bad = self.ids()[2]
        self.fail_ids = {bad}
        log = self.d / lines.team_rel(AID) / "timekeeping" / "qc_failed.json"
        with mock.patch.dict(os.environ, {"BATCH_FILE": "voice_batches/inbox/x.json", "GITHUB_RUN_ID": "4242"}):
            self.run_once(budget_minutes=0)
        (e,) = json.loads(log.read_text())["failed"]
        self.assertEqual((e["id"], e["category"], e["attempts"], e["batch"], e["run_id"]),
                         (bad, "timekeeping", 5, "voice_batches/inbox/x.json", "4242"))
        self.assertEqual(e["text"], next(it["text"] for it in lines.build_lines(self.d, AID, ["timekeeping"], kind="assistant")
                                         if it["id"] == bad))
        self.assertRegex(e["date"], r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        self.assertEqual([x["round"] for x in e["rounds"]], [1, 2, 3])
        self.assertEqual(e["rounds"][-1]["failing"], {"f0": {"median_f0_hz": 150.0}})
        self.assertEqual(qc_failed.last_failing(e), "f0")
        # A fresh run (no series) retries it; it passes: the entry, and the empty log, are gone.
        self.fail_ids = set()
        self.run_once(budget_minutes=0)
        self.assertEqual(self.rendered[-1], [bad])
        self.assertFalse(log.exists())


class Continuation(unittest.TestCase):
    def test_cap(self):
        self.assertEqual(resume.next_continuation("0"), 1)
        self.assertEqual(resume.next_continuation(4), 5)
        self.assertIsNone(resume.next_continuation(5))
        self.assertIsNone(resume.next_continuation(9))
        self.assertEqual(resume.CONTINUATION_CAP, 5)
        r = subprocess.run([sys.executable, str(HERE / "resume.py"), "next", "5"], capture_output=True, text=True)
        self.assertEqual(r.stdout.split(), ["dispatch=false"])
        r = subprocess.run([sys.executable, str(HERE / "resume.py"), "next", "2"], capture_output=True, text=True)
        self.assertEqual(r.stdout.split(), ["dispatch=true", "next=3"])

    def test_remaining_counts(self):
        self.assertEqual(resume.count_remaining({"remaining": {"greetings": ["a", "b"], "teaching": ["c"]}},
                                                ["greetings"]), 2)
        self.assertEqual(resume.count_remaining({"remaining": ["a"]}), 1)
        self.assertEqual(resume.count_remaining({}), 0)

    def test_merge_carries_remaining(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "v_manifest.greetings.json").write_text(json.dumps(
                {"category": "greetings", "lines": [{"id": "g1"}], "failed": [], "remaining": ["g2"]}))
            (d / "v_manifest.teaching.json").write_text(json.dumps({"category": "teaching", "lines": [], "failed": []}))
            self.assertEqual(merge_manifest.merge(d, "v")["remaining"], {"greetings": ["g2"]})
            # r3: a part's list is this run's word; an older one is dropped once the line passed or failed.
            (d / "r3_manifest.v.json").write_text(json.dumps(
                {"lines": [], "failed": [{"id": "x"}], "remaining": ["x", "y", "z"]}))
            (d / "r3_manifest.v.part01.json").write_text(json.dumps(
                {"updated_at": "1", "lines": [{"id": "y"}], "failed": [], "remaining": ["w"]}))
            m, _ = merge_manifest.merge_r3(d, "v")
            self.assertEqual(m["remaining"], ["w", "z"])

    @unittest.skipIf(yaml is None, "needs PyYAML")
    def test_workflow_wiring(self):
        wf = yaml.safe_load(WORKFLOW.read_text())
        jobs = wf["jobs"]
        self.assertLess(int(wf["env"]["RENDER_BUDGET_MINUTES"].split("'")[1]), jobs["render"]["timeout-minutes"])
        self.assertLess(jobs["render"]["timeout-minutes"], 360)
        self.assertEqual(jobs["continue"]["permissions"], {"actions": "write"})
        self.assertIn("schedule", wf[True])
        self.assertNotEqual(wf[True]["schedule"][0]["cron"].split()[0], "0")
        self.assertEqual(set(wf[True]["workflow_dispatch"]["inputs"]), {"batch_path", "continuation", "series"})
        text = WORKFLOW.read_text()
        self.assertNotIn("actions/upload-artifact", text)


def make_batches(root: Path, specs: dict) -> list[Path]:
    out = []
    for name, cats in specs.items():
        p = root / f"{name}.json"
        p.write_text(json.dumps({"kind": "assistant", "assistant": AID, "voice": VOICE,
                                 "ref_path": "lms/team/voice_refs/v.wav", "ref_sha256": REF_SHA,
                                 "agent_branch": f"rokct/{name}", "categories": cats}))
        out.append(p)
    return out


def done_manifest(root: Path, category: str, agent: Path, failed: bool = False) -> None:
    """Manifest under root (agent main or an exported branch) with every line
    of the category passed (or failed every round), built from agent."""
    items = lines.build_lines(agent, AID, [category], kind="assistant")
    entries = [{"id": it["id"], "text_sha256": it["text_sha256"], "render_sha256": it["render_sha256"],
                "tail_pad": resume.TAIL_PAD, **({"ref_sha256": REF_SHA} if failed else {})} for it in items]
    m = {"reference": {"sha256": REF_SHA}, "category": category,
         "lines": [] if failed else entries, "failed": entries if failed else []}
    p = root / lines.team_rel(AID) / f"{VOICE}_manifest.{category}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(m))


class PendingScan(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.d = Path(self.tmp.name)
        self.agent = self.d / "agent"
        make_agent(self.agent)
        self.branch = self.d / "branch"
        self.a, self.b = make_batches(self.d, {"a_handover": ["handover"], "b_timekeeping": ["timekeeping"]})

    def tearDown(self):
        self.tmp.cleanup()

    def scan(self):
        lst = self.d / "list.tsv"
        lst.write_text(f"{self.a}\t{self.branch}\n{self.b}\t\n")
        hit = pending.first_pending([(str(self.a), [self.agent, self.branch]), (str(self.b), [self.agent])],
                                    self.agent)
        r = subprocess.run([sys.executable, str(HERE / "pending.py"), "--agent-root", str(self.agent), "--scan", str(lst)],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout.strip(), hit[0] if hit else "")
        return hit

    def test_picks_the_first_pending_batch(self):
        self.assertEqual(self.scan(), (str(self.a), 2))            # nothing rendered: the first batch
        done_manifest(self.branch, "handover", self.agent)                      # a is done on its agent branch
        self.assertEqual(self.scan(), (str(self.b), 3))

    def test_nothing_pending_means_no_matrix(self):
        done_manifest(self.branch, "handover", self.agent)
        done_manifest(self.agent, "timekeeping", self.agent, failed=True)       # all final-failed on main: done
        self.assertIsNone(self.scan())
        if yaml is None:
            return
        # The plan job counts the scan's output lines: 0 -> no render matrix, no merge, no PR.
        plan = yaml.safe_load(WORKFLOW.read_text())["jobs"]
        self.assertEqual(plan["render"]["if"], "needs.plan.outputs.count == '1'")
        self.assertIn("needs.plan.outputs.count == '1'", plan["merge"]["if"])

    def test_changed_text_is_pending_again(self):
        done_manifest(self.branch, "handover", self.agent)
        done_manifest(self.agent, "timekeeping", self.agent)
        self.assertIsNone(self.scan())
        md = self.agent / lines.team_rel(AID) / "timekeeping/halfway.md"
        md.write_text("# halfway\n\nNew words now.\n")
        self.assertEqual(self.scan(), (str(self.b), 1))


if __name__ == "__main__":
    unittest.main()
