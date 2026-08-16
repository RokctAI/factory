# Agent build brief — {{APP_NAME}}

You are the first agent on this repository. It contains a brief and nothing
else. Your job is to turn the brief into a working application.

## What this is

**{{APP_NAME}}** — {{APP_DESCRIPTION}}

Repo: `{{APP_REPO}}` ({{APP_VISIBILITY}})
Accepted from: {{SOURCE_ISSUE}}

## Read first

1. [`docs/spec.md`](docs/spec.md) — the accepted brief, verbatim. It is the
   only statement of intent that exists. Where it is silent, decide, and
   record the decision in `.rokct/decision_log.md`.
2. The open **Build v0** issue — your entry point.

## Protocol bootstrap

This repo ships the Rokct agent protocol as a bootstrap only. Run it once
before your first commit:

```bash
bash .rokct/bootstrap.sh
```

That fetches `initiate.py` from `RokctAI/The-Rokct-Protocol` and runs it,
installing skills, session workflows and `sync_workspace` into `.rokct/`.

This repo is **standalone**: `.rokct/.workspace_config.json` ships with an
empty `parent_repo`, so working files (`memory.md`, `decision_log.md`,
`project_map.md`) stay here and sync to no parent workspace. Run
`bootstrap.sh` in a normal session, not under CI — `initiate.py` skips
installing the session workflows whenever `CI` is set.

## How to work

- Pick the stack yourself unless `docs/spec.md` names one. Justify it in
  `README.md`.
- Ship a v0 that a person can actually run: entry point, install steps, and
  one command in the README that starts it.
- Commit in small, reviewable steps against `main`.
- Keep `docs/spec.md` unedited — it is the accepted brief. New decisions go in
  `.rokct/decision_log.md`, new scope goes in new issues.
