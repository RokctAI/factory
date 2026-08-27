# From issue to app repo

Ray files an app idea as an issue on this repository, reads it later, and puts
the `approved` label on it. Seconds after that label lands there is a new
GitHub repo under `RokctAI` containing a brief, an agent-facing README and a
bootstrap script, with an open **Build v0** issue waiting for whoever — or
whatever — picks it up. Nothing in between is manual.

This page explains what happens in between, and what does not. For operator
detail — PAT scopes, the `FACTORY_TARGET_OWNER` variable, owner casing, the
roadmap hand-off — see [app-factory.md](app-factory.md), which this page does
not repeat.

## The two labels

The issue form at
[`.github/ISSUE_TEMPLATE/app-idea.yml`](../.github/ISSUE_TEMPLATE/app-idea.yml)
attaches `app-idea` to every idea automatically (`app-idea.yml:4`), and that
label is inert. The spawn workflow fires on
`github.event.label.name == 'approved'` and on nothing else
([`app_spawn.yml:32`](../.github/workflows/app_spawn.yml)). Ray applies
`approved` by hand, and every application of it mints a repo. Ideas accumulate
freely as issues; one label turns one of them into a repository.

The form asks five things, all parsed out of the rendered issue body — there is
no API in between, just markdown headings.

- **App name** (required) — the repo slug, held to
  `^[a-z0-9][a-z0-9-]{0,62}[a-z0-9]$` (`.github/scripts/parse_app_idea.py:24`).
- **One-line description** (required) — becomes the repo description.
- **Rationale** (required, free text) — copied **verbatim** into the new repo's
  `docs/spec.md`, the only statement of intent that repo will ever have. It is
  written for the agent that will build the thing.
- **Visibility** (required dropdown, exactly `private` or `public`, `default: 0`
  so private).
- **Target owner** (optional) — falls back to the `FACTORY_TARGET_OWNER` repo
  variable, then to `RokctAI`.

## Parsing, and the trap in it

[`parse_app_idea.py`](../.github/scripts/parse_app_idea.py) splits the body on
`^###\s+(.+)$`, normalises each heading to lowercase with punctuation flattened
to spaces, and then iterates over its own `FIELDS` map rather than over the
headings it found (`parse_app_idea.py:31-37`, `:58`). **Any heading not in
`FIELDS` is parsed and then silently dropped** — add a field to the form
without adding it to `FIELDS` and no error is raised anywhere; the value just
never reaches the new repo.

`validate()` is strict where it matters and deliberately lenient where it does
not. Missing name, description or rationale is a hard error, as is a bad slug
or a login that cannot be a GitHub account. Visibility does the opposite:
anything unexpected falls back to `private` (`:79-82`), because an unreadable
dropdown means the form has drifted and private is the safe side of that. The
owner goes through `owners.canonical()` (`:86`), which folds any casing of
`RokctAI` to the canonical spelling — `initiate.py` tests the origin URL for
the literal substring `RokctAI/`, case-sensitively — and leaves unknown owners
byte-for-byte as typed. `rationale` is renamed to `spec` on the way out
(`:121`), the name the seeder and the scaffold use.

## The run

```
issue labelled `approved`
   |
   +-- parse job
   |     require `app-idea` label ......... app_spawn.yml:47   fails loudly if absent
   |     parse the issue body ............. parse_app_idea.py
   |     gh api repos/$TARGET ............. app_spawn.yml:74   refuses if it already exists
   |         (any failure -> comment on the issue, remove `approved`)
   |
   +-- create job (app_create.yml, reusable)
   |     check token scopes ............... app_create.yml:85
   |     gh repo create ................... app_create.yml:101
   |     seed templates/app -> seed/ ...... seed_app_repo.py
   |     git init / commit / push main .... app_create.yml:131
   |     gh issue create "Build v0" ....... app_create.yml:145
   |     register with the roadmap ........ app_create.yml:165  optional, continue-on-error
   |
   +-- announce job
         comment the new repo URL on the factory issue, close it  app_spawn.yml:125
```

Three guardrails are worth naming. The `app-idea` requirement is a step inside
the job rather than part of the `if`, so labelling an unrelated issue
`approved` fails visibly — commenting the reason and stripping `approved` —
instead of skipping every job in silence (`app_spawn.yml:47-52`, `:86-99`). The
double-spawn guard asks `gh api repos/$TARGET` before creating anything,
because an existing repo is somebody's work in progress (`:74-84`). And both
parse failures and create failures report back on the originating issue and
remove `approved`, so fixing the issue and re-applying the label is the retry.

## What lands in the new repo

The scaffold is [`templates/app/`](../templates/app): six files in two
directories — `AGENTS.md`, `README.md`, `docs/spec.md`, `.relation` (a literal
`[]`), `.rokct/bootstrap.sh` (mode 755), and `gitignore`, stored dotless and
renamed to `.gitignore` by the seeder. That is the only rename
(`seed_app_repo.py:16`); a live `.gitignore` in `templates/app/` would act on
the factory's own tree.

[`seed_app_repo.py`](../.github/scripts/seed_app_repo.py) copies the tree and
substitutes seven tokens — `{{APP_NAME}}`, `{{APP_DESCRIPTION}}`,
`{{APP_SPEC}}`, `{{APP_OWNER}}`, `{{APP_REPO}}`, `{{APP_VISIBILITY}}`,
`{{SOURCE_ISSUE}}` (`:40-48`). The pattern is `\{\{([A-Z_]+)\}\}` (`:17`):
uppercase and underscores only, no digits. An unknown token is left in place,
and a second walk over the seeded tree then raises `SystemExit` on any survivor
(`:70-79`) — so a typo fails the spawn loudly instead of shipping a literal
`{{...}}` into a new repo. `{{APP_OWNER}}` is defined but used by no template
file today.

The files reach GitHub over plain git, not `gh`. `app_create.yml` builds a
fresh local repo in `seed/` — `git init -q -b main`, `git add -A`, a commit
authored by `rokct-bot` whose message ends `[skip ci]` — then adds a
token-in-URL remote `https://x-access-token:${GH_TOKEN}@github.com/${TARGET}.git`
and pushes (`app_create.yml:131-143`). `gh` does exactly two things:
`repo create` and `issue create`.

All four token-bearing steps use `secrets.FACTORY_PAT`, which `app_spawn.yml`
resolves as `${{ secrets.FACTORY_PAT || secrets.MONOREPO_PAT }}` (`:120`) — so
`MONOREPO_PAT` by default. `GITHUB_TOKEN` never touches the new repo; it only
comments on and closes the factory's own issue. A pre-flight step reads the
live `x-oauth-scopes` header and fails with the missing scope named if a
classic PAT lacks `repo` (`app_create.yml:85-99`); a fine-grained token
advertises no scopes, so that case is only warned about. The scope table is in
[app-factory.md](app-factory.md#which-token-creates-a-repo-where).

After the push, `gh issue create` opens **Build v0** in the new repo pointing
at `docs/spec.md` and `AGENTS.md` and asking for `bash .rokct/bootstrap.sh`
(`app_create.yml:145-157`). Then one optional `continue-on-error` step POSTs
outward to tell the fleet's roadmap module the repo exists (`app_create.yml:165`,
detailed in [app-factory.md](app-factory.md#registering-with-the-roadmap)).
Finally the `announce` job comments the new repo's URL on the factory issue and
closes it.

## What the factory does not do

This is the part most often assumed wrongly. It **never executes anything
inside the spawned repo**: no `gh workflow run`, no `repository_dispatch`, no
branch protection, no topics. Its involvement ends at a pushed `main` and an
open issue. `templates/app/` **ships no `.github/` directory at all**, so a
spawned repo has no workflows of any kind until something else installs them.
And `.rokct/bootstrap.sh` ships but **is never invoked by the factory** — its
only mention anywhere under `.github/` is prose in the Build v0 issue body
asking the agent to run it (`app_create.yml:155`). That last one is deliberate:
`initiate.py` skips deploying the session workflows when `CI` is set, so
bootstrapping from inside a workflow would install half the protocol and look
finished; see
[app-factory.md](app-factory.md#why-the-scaffold-ships-no-workspace_configjson).
There is also **no stack, framework or language field** anywhere in the form.

One honest gap: because the scaffold contains no `.github/workflows/`, the
factory has never pushed a workflow file. Doing so over a PAT needs `workflow`
scope on a classic token, or Workflows: write on a fine-grained one, and this
repo documents neither — only `repo` scope and `Administration: write`. Whether
`MONOREPO_PAT` could push a workflow is **unverified**, and nothing here should
be read as claiming it can.

## Proposal, not built: a stack field

`AGENTS.md` already defers to a stack the spec is meant to name. It tells the
agent to "Pick the stack yourself unless `docs/spec.md` names one"
(`templates/app/AGENTS.md:90`), and it gates its whole SDK-fleet section on
whether the spec puts the app on the fleet stack, Flutter plus Frappe
(`templates/app/AGENTS.md:42-44`). Nothing ever names one, because there is no
field to name it in.

Closing that is ten edits and no new machinery: a Stack dropdown on the form
(`agent-decides` / `flutter` / `nextjs` / `frappe` / `flutter+frappe`,
defaulting to `agent-decides` so today's behaviour is unchanged), a `FIELDS`
entry, a membership check in `validate()` with a safe default copying the
visibility pattern, the value threaded through `parse.outputs` → the reusable
workflow's `with:` → `workflow_call.inputs` → a `--stack` flag on the seeder →
the `values` dict, and a `**Stack:** {{APP_STACK}}` line in
`templates/app/docs/spec.md`. **Ray has not approved this.** It is recorded
here so the shape of it exists, not because it is queued.

## Test coverage

[`unit_tests.yml`](../.github/workflows/unit_tests.yml) triggers only on paths
`lessons/scripts/**` and `.github/scripts/**` (`unit_tests.yml:6-14`), so a
change confined to `templates/app/` or `.github/ISSUE_TEMPLATE/` does not run
the suite at all. Within the suite, `.github/scripts/tests/` covers `owners.py`
and `register_roadmap.py` but has no coverage for `seed_app_repo.py` — the
token substitution and the unsubstituted-token guard are untested.
