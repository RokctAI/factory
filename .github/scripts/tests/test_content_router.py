import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import content_router as cr  # noqa: E402


class Glob(unittest.TestCase):
    def test_star_stays_in_one_folder(self):
        self.assertTrue(cr.path_matches(".rokct/agent/jobs/pending/a.md", [".rokct/agent/jobs/pending/*.md"]))
        self.assertFalse(cr.path_matches(".rokct/agent/jobs/pending/x/a.md", [".rokct/agent/jobs/pending/*.md"]))

    def test_double_star_crosses_folders(self):
        self.assertTrue(cr.path_matches("school/curriculum/CAPS/maths/x.json", ["school/**"]))
        self.assertTrue(cr.path_matches("school/a/b/script.md", ["school/**/script.md"]))

    def test_last_match_wins(self):
        pats = ["school/**", "!school/review_index.json"]
        self.assertFalse(cr.path_matches("school/review_index.json", pats))
        self.assertTrue(cr.path_matches("school/reviews/a.json", pats))


def commit(sha, msg="edit", login="ray", email="ray@example.com"):
    return {"sha": sha, "author": {"login": login},
            "commit": {"message": msg, "author": {"email": email}}}


class Skip(unittest.TestCase):
    def test_skip_ci_and_bot(self):
        self.assertTrue(cr.skipped(commit("a", "x [skip ci]")))
        self.assertTrue(cr.skipped(commit("a", login="github-actions[bot]")))
        self.assertTrue(cr.skipped(commit("a", login="", email="github-actions[bot]@users.noreply.github.com")))
        self.assertFalse(cr.skipped(commit("a")))


class FakeGitHub:
    def __init__(self, head, status="ahead", commits=(), files=None):
        self._head, self.status, self.commits = head, status, list(commits)
        self.files, self.dispatched = files or {}, []

    def head(self, repo):
        return self._head

    def compare(self, repo, base, head):
        return self.status, self.commits

    def commit_files(self, repo, sha):
        return self.files.get(sha, [])

    def dispatch(self, engine, wf, inputs):
        self.dispatched.append((wf, inputs))


ROUTES = [
    {"workflow": "lesson4_evaluation.yml", "paths": [".rokct/agent/jobs/pending/*.md"]},
    {"workflow": "review_index.yml", "paths": ["school/**", "!school/review_index.json"]},
]


class Route(unittest.TestCase):
    def test_first_run_records_head_only(self):
        gh = FakeGitHub("h1")
        self.assertEqual(cr.route_repo(gh, "RokctAI/lessons", ROUTES, None, "E"), ("h1", []))
        self.assertEqual(gh.dispatched, [])

    def test_dispatches_matching_workflows_with_the_range_start(self):
        gh = FakeGitHub("h2", commits=[commit("c1"), commit("c2", "ledger [skip ci]")],
                        files={"c1": [".rokct/agent/jobs/pending/a.md"], "c2": ["school/x.md"]})
        head, hit = cr.route_repo(gh, "RokctAI/lessons", ROUTES, "h1", "E")
        self.assertEqual((head, hit), ("h2", ["lesson4_evaluation.yml"]))
        self.assertEqual(gh.dispatched, [("lesson4_evaluation.yml", {"router_before": "h1"})])

    def test_only_excluded_paths_dispatch_nothing(self):
        gh = FakeGitHub("h2", commits=[commit("c1")], files={"c1": ["school/review_index.json"]})
        self.assertEqual(cr.route_repo(gh, "r", ROUTES, "h1", "E")[1], [])

    def test_rewritten_history_resets_without_dispatch(self):
        gh = FakeGitHub("h2", status="diverged", commits=[commit("c1")], files={"c1": ["school/a"]})
        self.assertEqual(cr.route_repo(gh, "r", ROUTES, "h1", "E"), ("h2", []))
        self.assertEqual(gh.dispatched, [])

    def test_dry_run_dispatches_nothing(self):
        gh = FakeGitHub("h2", commits=[commit("c1")], files={"c1": ["school/a"]})
        self.assertEqual(cr.route_repo(gh, "r", ROUTES, "h1", "E", dry_run=True)[1], ["review_index.yml"])
        self.assertEqual(gh.dispatched, [])


if __name__ == "__main__":
    unittest.main()
