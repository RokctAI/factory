#!/usr/bin/env python3
"""Normalise text files under the given paths.

For each tracked-looking text file under the given roots: strip trailing
spaces and tabs, convert CRLF/CR to LF, and ensure exactly one final newline.
Binary files and lock files are skipped. Stdlib only.

Usage: whitespace_fix.py PATH [PATH ...]
"""

import os
import sys

SKIP_NAMES = {"pubspec.lock", "package-lock.json", "yarn.lock", "Podfile.lock"}
SKIP_SUFFIXES = (
    ".lock",
    ".g.dart",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".ico",
    ".pdf",
    ".zip",
    ".gz",
    ".jar",
    ".so",
    ".dll",
    ".exe",
    ".ttf",
    ".otf",
)
SKIP_DIRS = {".git", "node_modules", "vendor", "build", ".dart_tool"}


def is_binary(data: bytes) -> bool:
    return b"\x00" in data[:8192]


def normalise(data: bytes) -> bytes:
    text = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    lines = [line.rstrip(b" \t") for line in text.split(b"\n")]
    while lines and lines[-1] == b"":
        lines.pop()
    return b"\n".join(lines) + b"\n" if lines else b""


def walk(root: str):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name in SKIP_NAMES or name.endswith(SKIP_SUFFIXES):
                continue
            yield os.path.join(dirpath, name)


def main(argv):
    if not argv:
        print("usage: whitespace_fix.py PATH [PATH ...]", file=sys.stderr)
        return 2
    changed = 0
    for root in argv:
        if not os.path.isdir(root):
            continue
        for path in walk(root):
            if os.path.islink(path):
                continue
            with open(path, "rb") as fh:
                data = fh.read()
            if is_binary(data):
                continue
            fixed = normalise(data)
            if fixed != data:
                with open(path, "wb") as fh:
                    fh.write(fixed)
                changed += 1
    print(f"whitespace_fix: normalised {changed} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
