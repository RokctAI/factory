"""Guard for sdk_protocol_sync.yml: stop a sync from losing SDK repo content.

Usage: python3 scripts/sync_guard.py <sdk_clone_dir>

Run after the protocol steps and before the commit. It
  1. restores .rokct/memory.md from HEAD (a sync never edits a repo's memory;
     initiate.py otherwise appends the CI bot as a second "Safe ID"), and
  2. fails the run if any tracked file under .rokct/ or .github/workflows/
     was deleted, other than the files in ALLOWED_DELETIONS.
"""

import subprocess
import sys

ALLOWED_DELETIONS = {".rokct/.sync_ready"}
RESTORE_FROM_HEAD = (".rokct/memory.md",)


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", repo, *args], capture_output=True, text=True, check=True
    ).stdout


def tracked(repo, path):
    return bool(git(repo, "ls-files", "--", path).strip())


def deleted_files(repo):
    out = git(
        repo, "diff", "--name-only", "--diff-filter=D", "HEAD", "--",
        ".rokct", ".github/workflows",
    )
    return [p for p in out.splitlines() if p and p not in ALLOWED_DELETIONS]


def main(repo):
    for path in RESTORE_FROM_HEAD:
        if tracked(repo, path):
            git(repo, "checkout", "HEAD", "--", path)
            print(f"[guard] kept {path} as on main")
    lost = deleted_files(repo)
    if lost:
        print("[guard] Sync would delete repo content; stopping:", file=sys.stderr)
        for p in lost:
            print(f"  - {p}", file=sys.stderr)
        return 1
    print("[guard] No content lost.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
