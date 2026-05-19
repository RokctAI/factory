---
name: Agent Delegation
description: Automates the offloading of repetitive or large-scale coding tasks to an AI agent (Jules) or direct Groq API calls.
---

# Agent Delegation Skill

This skill delegates work to external AI agents (Jules) or the Groq API. It uses a **thin-wrapper → shared-script** architecture.

## Architecture

```
factory .rokct/                          The-Rokct-Protocol/
 └─ skills/agent_delegation/             └─ core/skills/agent_delegation/scripts/
     ├─ scripts/call_jules.py            │    ├─ delegate_to_agent.py   (canonical — excluded from copy)
     ├─ scripts/call_groq.py             │    └─ utils/
     ├─ scripts/handle_groq_output.py    └──►     ├─ call_jules.py
     └─ scripts/update_classifications.py        ├─ call_groq.py
                                                    └─ handle_groq_output.py
```

- **Thin wrappers** (`call_jules.py`, `call_groq.py`) live in `.rokct/skills/agent_delegation/scripts/`. They locate `The-Rokct-Protocol` by walking up the directory tree and redirect to `delegate_to_agent.py`.
- **`delegate_to_agent.py`** is the single canonical implementation in The-Rokct-Protocol. It is **excluded** during `init_protocol` copy.
- **`handle_groq_output.py`** is project-specific — parses Groq LLM output into job cards for `.rokct/agent/jobs/pending/`. Uses `update_classifications.py` from the same scripts directory; reads `.rokct/config/classifications/factory_themes.txt` for deduplication.
- **`update_classifications.py`** is project-specific — generates/exports theme/genre lists for this project's classification files.

## Prerequisites
- **Jules API Key**: `JULES_API_KEY` or `AGENT_API_KEY` (env, `.env`, or remote vault).
- **Groq API Key**: `GROQ_API_KEY` (only needed for `groq` subcommand).
- **Monorepo Access**: `MONOREPO_PAT` (CI / remote vault key resolution).
- **Dependencies**: `requests`, `python-dotenv`, `pyyaml`.

## API Key Resolution (delegate_to_agent.py)

Order of fallback:

1. **Remote Vault** (`MONOREPO_PAT` set) — fetches `.env` from `RokctAI/monorepo` via GitHub API.
2. **Local env file** — `Monorepo/.env/production.env` or `/.env/production.env`.
3. **Explicit** — `--api-key` CLI flag.
4. **Environment** — `JULES_API_KEY` / `AGENT_API_KEY`.
5. **`.env`** — `--env-file` fallback.

## delegate_to_agent.py Subcommands

| Subcommand | Key | Description |
|---|---|---|
| `create` | JULES / AGENT | Create a new Jules session |
| `status` | JULES / AGENT | Fetch session status |
| `query` | JULES / AGENT | Send a follow-up message |
| `approve` | JULES / AGENT | Approve a pending plan |
| `delete` | JULES / AGENT | Cancel/delete a session |
| `list` | JULES / AGENT | List all sessions |
| `groq` | GROQ | Call Groq chat completion |

## Decision Framework
- **Delegate (Agent)**: Bulk refactors, library migrations, boilerplate, sub-repo work, mid-task fixes.
- **Direct (Antigravity)**: Architecture design, UI/UX, multi-repo sync, complex discovery.
- **Groq**: Fast LLM calls without a Jules session (theme generation, structured output).

## How to Use

### 1. Delegate to Jules

```bash
python .rokct/skills/agent_delegation/scripts/call_jules.py create \
  --repo "sources/github/RokctAI/factory" \
  --prompt "Your detailed task description here" \
  --title "Feature/Task Name"
```

Monitor status:

```bash
python .rokct/skills/agent_delegation/scripts/call_jules.py status --id "SESSION_ID"
```

### 2. Call Groq Directly

```bash
python .rokct/skills/agent_delegation/scripts/call_groq.py groq \
  --prompt "Your prompt here" \
  --system "Optional system prompt" \
  --model "llama-3.3-70b-versatile"
```

### 3. Handle Groq Output (Pipeline)

```bash
python .rokct/skills/agent_delegation/scripts/handle_groq_output.py \
  --level 0 \
  --content "$GROQ_RESPONSE"
```

Pipeline levels:
- **Level 0**: Parses `theme | type` lines → creates `.rokct/agent/jobs/pending/` job cards.
- **Level 1**: Parses 5 ideas per card (extension point).

### 4. Manage Sessions

```bash
python .rokct/skills/agent_delegation/scripts/manage_sessions.py
```

Reads `session_state.md` and `ledger.md`, detects stalled cards, reports active Jules sessions.

### 5. Approve Plans (Optional)

```bash
python .rokct/skills/agent_delegation/scripts/call_jules.py approve --id "SESSION_ID"
```

## Best Practices
- **Repo format**: Always use full source name (`sources/github/Owner/Repo`).
- **Context**: Mention specific file paths or patterns to narrow scope.
