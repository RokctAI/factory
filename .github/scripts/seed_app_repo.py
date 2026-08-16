#!/usr/bin/env python3
"""Copy templates/app into a target directory, substituting {{TOKENS}}.

Dotfiles are stored without the leading dot (`gitignore`) so they do not act
on the factory's own tree; RENAMES puts the dot back on the way out.

Usage: seed_app_repo.py --template templates/app --dest <dir> \
         --name <slug> --description <text> --spec-file <path> \
         --owner <login> --visibility <private|public> --issue <url>
"""
import argparse
import os
import re
import shutil

RENAMES = {"gitignore": ".gitignore"}
TOKEN_RE = re.compile(r"\{\{([A-Z_]+)\}\}")
BINARY_SUFFIXES = (".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf", ".zip")


def substitute(text, values):
    return TOKEN_RE.sub(lambda m: values.get(m.group(1), m.group(0)), text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", default="templates/app")
    ap.add_argument("--dest", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--description", required=True)
    ap.add_argument("--spec-file", required=True)
    ap.add_argument("--owner", required=True)
    ap.add_argument("--visibility", default="private")
    ap.add_argument("--issue", default="")
    args = ap.parse_args()

    with open(args.spec_file, "r", encoding="utf-8") as f:
        spec = f.read().strip()

    values = {
        "APP_NAME": args.name,
        "APP_DESCRIPTION": args.description,
        "APP_SPEC": spec,
        "APP_OWNER": args.owner,
        "APP_REPO": f"{args.owner}/{args.name}",
        "APP_VISIBILITY": args.visibility,
        "SOURCE_ISSUE": args.issue or "(none)",
    }

    written = 0
    for root, _dirs, files in os.walk(args.template):
        rel_dir = os.path.relpath(root, args.template)
        out_dir = args.dest if rel_dir == "." else os.path.join(args.dest, rel_dir)
        os.makedirs(out_dir, exist_ok=True)
        for name in files:
            src = os.path.join(root, name)
            dest = os.path.join(out_dir, RENAMES.get(name, name))
            if name.lower().endswith(BINARY_SUFFIXES):
                shutil.copy2(src, dest)
            else:
                with open(src, "r", encoding="utf-8") as f:
                    body = substitute(f.read(), values)
                with open(dest, "w", encoding="utf-8") as f:
                    f.write(body)
                if dest.endswith(".sh"):
                    os.chmod(dest, 0o755)
            written += 1
            print(f"[seed] {os.path.relpath(dest, args.dest)}")

    leftovers = set()
    for root, _dirs, files in os.walk(args.dest):
        for name in files:
            path = os.path.join(root, name)
            if name.lower().endswith(BINARY_SUFFIXES):
                continue
            with open(path, "r", encoding="utf-8") as f:
                leftovers.update(TOKEN_RE.findall(f.read()))
    if leftovers:
        raise SystemExit(f"[seed] unsubstituted tokens remain: {sorted(leftovers)}")

    print(f"[seed] wrote {written} files to {args.dest}")


if __name__ == "__main__":
    main()
