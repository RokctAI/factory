# newfactory — accepted brief

> Copied verbatim from https://github.com/RokctAI/factory/issues/269 at spawn time. Do not edit: this is the
> record of what was accepted. Decisions taken while building belong in
> `.rokct/decision_log.md`.

**One line:** Public CI engine: runs every factory workflow on free public minutes against the private content repos.

## Rationale

Part of the factory split. Today's RokctAI/factory is renamed to RokctAI/lessons (private, history kept). This repo becomes the running engine: it takes all of `.github/` plus the code the workflows run (`voice_batch/`, the radio_ads and social scripts, `templates/app`). It holds no lesson, book, film or voice content; workflows check out the private content repos (lessons, books, bible, film, social, startupos) with MONOREPO_PAT and commit back to them. Named newfactory for now; Ray renames it to `factory` once the old factory has been renamed.

Done means: all workflows run from here, nothing private is printed, uploaded or cached in public runs, and lesson releases land on the private lessons repo.
