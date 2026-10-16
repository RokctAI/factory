#!/usr/bin/env python3
"""Copy an app template into a target directory, substituting {{TOKENS}}.

Two template layouts are supported:

- **Per-stack** (the current `templates/app/`): a `common/` subdirectory
  holding the files every app gets, plus optional sibling overlay directories
  named after stacks (`nextjs/`, `flutter/`, `frappe/`). Seeding copies
  `common/` first, then — when `--stack` is given — the overlay on top, with
  overlay files winning on collision.
- **Flat** (the historical layout): no `common/` subdirectory. The template
  directory is copied as-is, exactly as before. `--stack` is meaningless
  here and rejected loudly rather than silently ignored.

Dotfiles are stored without the leading dot (`gitignore`) so they do not act
on the factory's own tree; RENAMES puts the dot back on the way out.

Usage: seed_app_repo.py --template templates/app --dest <dir> \
         --name <slug> --description <text> --spec-file <path> \
         --owner <login> --visibility <private|public> --issue <url> \
         [--stack {nextjs,flutter,frappe}]
"""
import argparse
import os
import re
import shutil

RENAMES = {"gitignore": ".gitignore"}
TOKEN_RE = re.compile(r"\{\{([A-Z_]+)\}\}")
BINARY_SUFFIXES = (".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf", ".zip")
STACKS = ("nextjs", "flutter", "frappe")


def substitute(text, values):
    return TOKEN_RE.sub(lambda m: values.get(m.group(1), m.group(0)), text)


def app_slug(name):
    """Lowercase `name`, turn spaces/underscores into hyphens, keep [a-z0-9-].

    Consecutive separators collapse to one hyphen and the ends are trimmed,
    so "My Cool_App!" -> "my-cool-app".
    """
    slug = re.sub(r"[ _]+", "-", name.lower())
    slug = re.sub(r"[^a-z0-9-]", "", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug


def copy_tree(template, dest, values):
    """Copy one template tree into dest, substituting tokens.

    Files already present in dest are overwritten — that is what lets a stack
    overlay win over `common/`. Returns the number of files written.
    """
    written = 0
    for root, _dirs, files in os.walk(template):
        rel_dir = os.path.relpath(root, template)
        out_dir = dest if rel_dir == "." else os.path.join(dest, rel_dir)
        os.makedirs(out_dir, exist_ok=True)
        for name in files:
            src = os.path.join(root, name)
            out = os.path.join(out_dir, RENAMES.get(name, name))
            if name.lower().endswith(BINARY_SUFFIXES):
                shutil.copy2(src, out)
            else:
                with open(src, "r", encoding="utf-8") as f:
                    body = substitute(f.read(), values)
                with open(out, "w", encoding="utf-8") as f:
                    f.write(body)
                if out.endswith(".sh"):
                    os.chmod(out, 0o755)
            written += 1
            print(f"[seed] {os.path.relpath(out, dest)}")
    return written


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
    ap.add_argument("--stack", choices=STACKS, default="")
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
        "APP_SLUG": app_slug(args.name),
        "SOURCE_ISSUE": args.issue or "(none)",
    }

    common = os.path.join(args.template, "common")
    if os.path.isdir(common):
        written = copy_tree(common, args.dest, values)
        if args.stack:
            overlay = os.path.join(args.template, args.stack)
            if not os.path.isdir(overlay):
                raise SystemExit(
                    f"[seed] no overlay for stack '{args.stack}' in {args.template}"
                )
            written += copy_tree(overlay, args.dest, values)
    elif args.stack:
        raise SystemExit(
            f"[seed] --stack {args.stack} given, but {args.template} has no "
            "common/ subdirectory (flat legacy template) — refusing to guess"
        )
    else:
        written = copy_tree(args.template, args.dest, values)

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
