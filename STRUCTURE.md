# Repository Map — RokctAI Book Factory

This repository contains two parallel content streams managed by the same agent infrastructure.

## 1. Books Stream (`books/`)
Automated publishing factory for poetry, fiction, and children's books.
- **Rules:** `.rokct/types/{book.poetry|book.fiction|book.children|book.short_story}/`
- **Output:** `books/published/`
- **See:** [STRUCTURE_BOOKS.md](STRUCTURE_BOOKS.md)

## 2. Bible Series Stream (`bible/`)
Long-form research series exploring the hidden architecture of scripture.
- **Rules:** `.rokct/types/bible.series/`
- **Output:** `bible/{series_name}/`
- **See:** [STRUCTURE_BIBLE.md](STRUCTURE_BIBLE.md)

---

## Shared Infrastructure (Highlights)

### .rokct/
- **agent/**: Prompts, jobs, ledger, and guardrails.
- **skills/**: Ported skills from RokctAI/opportunities.
- **templates/**: Shared document stubs.

### .github/workflows/
Pipeline levels 0-6 managing the automated creation and publishing loop.

---

## Documentation
- [PLANNING.md](PLANNING.md): Core vision and technical specification.
- [README.md](README.md): Project overview and setup.
