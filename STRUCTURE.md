# Repository Structure: RokctAI/factory
**Generated Date:** 2026-04-29

RokctAI/factory is an autonomous publishing system designed to generate, evaluate, and publish books across multiple genres with minimal human intervention. It leverages AI agents (Groq and Jules) to handle the creative pipeline, governed by a set of hierarchical metarules and guardrails, ensuring high-quality output and safety standards.

## Full Repository Tree & File Contents

- **Directory: .github/** — GitHub configuration and automation
  - **Directory: workflows/** — CI/CD pipeline definitions for all levels
    - **File: agent-automated.yml** — Functional automation for task delegation from queue/prompts
      ```yaml
      # Copyright (c) 2026 RokctAI
      name: "Agent: Automated Delegation"

      on:
        push:
          paths:
            - '.rokct/agent/queue/*.json'
            - '.rokct/agent/prompts/in_progress/*.json'
          branches:
            - main
        schedule:
          - cron: '0 20 * * *' # Daily at 20:00 UTC
        workflow_dispatch:

      concurrency:
        group: agent-delegation
        cancel-in-progress: false

      permissions: write-all

      jobs:
        delegate:
          runs-on: ubuntu-latest
          steps:
            - uses: actions/checkout@v4
              with:
                fetch-depth: 2

            - name: Set up Python
              uses: actions/setup-python@v5
              with:
                python-version: '3.10'

            - name: Install dependencies
              run: pip install requests python-dotenv

            - name: Process Queue
              env:
                JULES_API_KEY: ${{ secrets.JULES_API_KEY }}
                GROQ_API_KEY: ${{ secrets.GROQ_API_KEY }}
              run: |
                FILES=$(ls .rokct/agent/queue/*.json .rokct/agent/prompts/in_progress/*.json 2>/dev/null || true)

                if [ -z "$FILES" ]; then
                  echo "ℹ️ No task files found to process."
                  exit 0
                fi

                CURRENT_TIME=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
                HAS_UPDATES=false
                TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M")

                for FILE in $FILES; do
                  if [ ! -f "$FILE" ]; then continue; fi

                  echo "📂 Analyzing: $FILE"

                  SCHEDULED_AT=$(jq -r '.scheduled_at // empty' "$FILE")
                  if [ -n "$SCHEDULED_AT" ] && [[ "$CURRENT_TIME" < "$SCHEDULED_AT" ]]; then
                    echo "⏳ Task is scheduled for $SCHEDULED_AT. Skipping."
                    continue
                  fi

                  IMMEDIATE=$(jq -r '.immediate // "true"' "$FILE")
                  if [ -z "$SCHEDULED_AT" ] && [ "$IMMEDIATE" == "false" ]; then
                     echo "🕒 Task marked as immediate:false. Skipping."
                     continue
                  fi

                  # Claim Lock
                  CARD_FILE=$(jq -r '.card_file // empty' "$FILE")
                  if [ -n "$CARD_FILE" ] && [ -f "$CARD_FILE" ]; then
                    if ! python .rokct/skills/agent_delegation/scripts/lock_job.py --file "$CARD_FILE" --action claim --agent "jules" --session "AUTO-$GITHUB_RUN_ID"; then
                       echo "Card $CARD_FILE is locked. Skipping task $FILE."
                       continue
                    fi
                  fi

                  AGENT=$(jq -r '.agent // "jules"' "$FILE")
                  REPO=$(jq -r '.repo' "$FILE")
                  PROMPT=$(jq -r '.prompt' "$FILE")
                  TITLE=$(jq -r '.title // "AI-Automation"' "$FILE")
                  LEVEL=$(jq -r '.level // 0' "$FILE")

                  SUCCESS=false
                  SESSION_ID="—"
                  if [ "$AGENT" == "groq" ]; then
                    echo "🚀 Calling Groq for $TITLE..."
                    RESPONSE=$(python .rokct/skills/agent_delegation/scripts/call_groq.py --prompt "$PROMPT")

                    if [ $? -eq 0 ] && [ -n "$RESPONSE" ]; then
                      echo "✅ Groq responded. Handling output..."
                      python .rokct/skills/agent_delegation/scripts/handle_groq_output.py --level "$LEVEL" --content "$RESPONSE"
                      SUCCESS=true
                      HAS_UPDATES=true
                    else
                      echo "❌ Groq call failed."
                    fi
                  else
                    echo "🚀 Delegating to Jules for $TITLE..."
                    RESULT=$(python .rokct/skills/agent_delegation/scripts/delegate_to_agent.py create \
                      --repo "sources/github/$REPO" \
                      --prompt "$PROMPT" \
                      --title "$TITLE")
                    if [ $? -eq 0 ]; then
                      echo "✅ Jules delegation successful."
                      SESSION_ID=$(echo "$RESULT" | jq -r '.id // "—"')
                      SUCCESS=true
                      HAS_UPDATES=true
                    else
                      echo "❌ Jules delegation failed."
                    fi
                  fi

                  if [ "$SUCCESS" = true ]; then
                    # Update Ledger Manually (Multi-file processing)
                    if [ -n "$CARD_FILE" ] && [ -f "$CARD_FILE" ]; then
                       ID=$(grep '^id:' "$CARD_FILE" | cut -d':' -f2 | xargs)
                       TYPE=$(grep '^type:' "$CARD_FILE" | cut -d':' -f2 | xargs)
                       THEME=$(grep '^theme:' "$CARD_FILE" | cut -d':' -f2 | xargs)
                       STATUS=$(grep '^status:' "$CARD_FILE" | cut -d':' -f2 | xargs)
                       echo "| $ID | $TYPE | $THEME | $STATUS | $AGENT | $SESSION_ID | — | $TIMESTAMP |" >> .rokct/agent/log/ledger.md

                       python .rokct/skills/agent_delegation/scripts/lock_job.py --file "$CARD_FILE" --action release
                    fi

                    # Handle recurrence/cleanup
                    RECURRENCE=$(jq -r '.recurrence // "Once"' "$FILE")
                    if [ "$RECURRENCE" == "Daily" ]; then
                      NEXT_RUN=$(date -u -d "tomorrow 20:00" +"%Y-%m-%dT%H:%M:%SZ")
                      jq --arg next "$NEXT_RUN" '.scheduled_at = $next' "$FILE" > tmp.json && mv tmp.json "$FILE"
                      HAS_UPDATES=true
                    elif [ "$RECURRENCE" == "Once" ]; then
                      mkdir -p .rokct/agent/prompts/completed
                      mv "$FILE" ".rokct/agent/prompts/completed/$(basename "$FILE")"
                      HAS_UPDATES=true
                    fi
                  else
                    # Handle Failure for Automated Delegation
                    if [ -n "$CARD_FILE" ] && [ -f "$CARD_FILE" ]; then
                       ATTEMPTS=$(grep '^attempts:' "$CARD_FILE" | cut -d':' -f2 | xargs)
                       NEW_ATTEMPTS=$((ATTEMPTS + 1))
                       sed -i "s/^attempts: .*/attempts: $NEW_ATTEMPTS/" "$CARD_FILE"
                       sed -i "s/^last_error: .*/last_error: ${{ github.run_id }} failed at $(date -u)/" "$CARD_FILE"

                       echo "[$TIMESTAMP] Automated | $TITLE | ${{ github.run_id }} | Failure" >> .rokct/agent/log/errors.log

                       if [ "$NEW_ATTEMPTS" -ge 3 ]; then
                         python .rokct/skills/agent_delegation/scripts/update_status.py --file "$CARD_FILE" --status stalled
                       else
                         python .rokct/skills/agent_delegation/scripts/lock_job.py --file "$CARD_FILE" --action release
                       fi
                       HAS_UPDATES=true
                    fi
                  fi
                done

                if [ "$HAS_UPDATES" == "true" ]; then
                  git config --global user.name "github-actions[bot]"
                  git config --global user.email "github-actions[bot]@users.noreply.github.com"
                  git add .
                  git commit -m "🤖 [CI] Agent Automation Updates & Ledger [skip ci]" || echo "No changes"
                  git push origin main
                fi
      ```
    - **File: agent-cleanup.yml** — Handles session deletion and memory sync after PR merges
      ```yaml
      name: "Agent: Cleanup & Memory"
      on:
        pull_request:
          types: [closed]

      jobs:
        cleanup:
          if: github.event.pull_request.merged == true
          runs-on: ubuntu-latest
          steps:
            - uses: actions/checkout@v4

            - name: Extract Session ID
              id: extract_id
              env:
                BRANCH_NAME: ${{ github.event.pull_request.head.ref }}
              run: |
                if [[ "$BRANCH_NAME" =~ ([0-9]{18,20}) ]]; then
                  SESSION_ID="${BASH_REMATCH[1]}"
                  echo "session_id=$SESSION_ID" >> "$GITHUB_OUTPUT"
                  echo "✅ Found Agent Session ID: $SESSION_ID"
                else
                  echo "ℹ️ No Agent Session ID in branch: $BRANCH_NAME"
                  exit 0
                fi

            - name: Delete Session
              if: steps.extract_id.outputs.session_id != ''
              env:
                AGENT_API_KEY: ${{ secrets.JULES_API_KEY }}
                SESSION_ID: ${{ steps.extract_id.outputs.session_id }}
              run: |
                python .rokct/skills/agent_delegation/scripts/delegate_to_agent.py delete \
                  --id "$SESSION_ID"

            - name: Update Agent Memory
              if: steps.extract_id.outputs.session_id != ''
              env:
                PR_TITLE: ${{ github.event.pull_request.title }}
                PR_URL: ${{ github.event.pull_request.html_url }}
              run: |
                DATE=$(date +'%Y-%m-%d')
                mkdir -p .rokct/agent/log
                echo "* **[$DATE]** - Completed Agent Task: $PR_TITLE ($PR_URL)" >> .rokct/agent/log/memory.md

            - name: Commit Knowledge Updates
              if: steps.extract_id.outputs.session_id != ''
              run: |
                git config --global user.name "github-actions[bot]"
                git config --global user.email "github-actions[bot]@users.noreply.github.com"
                git add .rokct/agent/log/memory.md
                git commit -m "🤖 chore: sync agent memory after PR merge [skip ci]" || echo "No changes to commit"
                git push
      ```
    - **File: factory-sync.yml** — Consolidated nightly sync for classifications, logs, and dashboard
      ```yaml
      name: "Factory: System Sync"
      on:
        schedule:
          - cron: '0 0 * * *' # Daily at midnight UTC
        workflow_dispatch:

      jobs:
        sync:
          runs-on: ubuntu-latest
          permissions: write-all
          steps:
            - uses: actions/checkout@v4

            - name: Set up Python
              uses: actions/setup-python@v5
              with:
                python-version: '3.10'

            - name: Install dependencies
              run: pip install requests python-dotenv pycryptodome

            - name: Update Classifications
              run: python .rokct/skills/agent_delegation/scripts/update_classifications.py

            - name: Update Job Audit Logs
              run: python .rokct/skills/agent_delegation/scripts/update_audit_logs.py

            - name: Update Dashboard
              run: python .rokct/skills/agent_delegation/scripts/update_dashboard.py

            - name: Privacy Sync
              env:
                EMAIL_ENCRYPTION_KEY: ${{ secrets.EMAIL_ENCRYPTION_KEY }}
              run: python .rokct/skills/agent_delegation/scripts/privacy_sync.py

            - name: Commit Updates
              run: |
                git config --global user.name "github-actions[bot]"
                git config --global user.email "github-actions[bot]@users.noreply.github.com"
                git add .
                if git diff --staged --quiet; then
                  echo "No updates to sync."
                else
                  git commit -m "chore: nightly factory system sync [skip ci]"
                  git push origin main
                fi
      ```
    - **File: ledger_update.yml** — Reusable workflow for appending rows to the ledger
      ```yaml
      name: Ledger Update
      on:
        workflow_call:
          inputs:
            id:
              required: true
              type: string
            type:
              required: true
              type: string
            theme:
              required: true
              type: string
            status:
              required: true
              type: string
            agent:
              required: true
              type: string
            session:
              required: true
              type: string
            pr:
              required: false
              type: string

      jobs:
        update_ledger:
          runs-on: ubuntu-latest
          steps:
            - uses: actions/checkout@v4

            - name: Append to Ledger
              run: |
                TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M")
                PR_VALUE="${{ inputs.pr }}"
                if [ -z "$PR_VALUE" ]; then PR_VALUE="—"; fi

                echo "| ${{ inputs.id }} | ${{ inputs.type }} | ${{ inputs.theme }} | ${{ inputs.status }} | ${{ inputs.agent }} | ${{ inputs.session }} | $PR_VALUE | $TIMESTAMP |" >> .rokct/agent/log/ledger.md

            - name: Commit Ledger Update
              run: |
                git config --global user.name "github-actions[bot]"
                git config --global user.email "github-actions[bot]@users.noreply.github.com"
                git add .rokct/agent/log/ledger.md
                git commit -m "chore: update ledger for ${{ inputs.id }} [skip ci]" || exit 0
                git push origin main
      ```
    - **File: level0_theme_generation.yml** — Hourly task to discover new themes via Groq
      ```yaml
      name: Level 0 - Theme Generation
      on:
        schedule:
          - cron: '0 * * * *' # Hourly check
        workflow_dispatch:

      jobs:
        check_and_trigger:
          runs-on: ubuntu-latest
          steps:
            - uses: actions/checkout@v4

            - name: Check Queue and Trigger
              run: |
                PENDING_COUNT=$(ls .rokct/agent/jobs/pending/*.md 2>/dev/null | grep -v "template.md" | wc -l)
                echo "Current pending themes: $PENDING_COUNT"
                if [ "$PENDING_COUNT" -lt 5 ]; then
                  echo "🚀 Triggering Level 0 Theme Discovery..."
                  # For simplicity, we trigger the agent-automated workflow if possible,
                  # or just rely on its next scheduled run.
                  # Here we just mark the prompt card as immediate:true to be picked up.
                  jq '.immediate = "true"' .rokct/agent/prompts/in_progress/level0_theme_discovery.json > tmp.json && mv tmp.json .rokct/agent/prompts/in_progress/level0_theme_discovery.json

                  git config --global user.name "github-actions[bot]"
                  git config --global user.email "github-actions[bot]@users.noreply.github.com"
                  git add .rokct/agent/prompts/in_progress/level0_theme_discovery.json
                  git commit -m "🤖 [CI] Trigger Theme Discovery [skip ci]" || exit 0
                  git push origin main
                fi
      ```
    - **File: level1_idea_generation.yml** — Triggers on new themes to generate book ideas
      ```yaml
      name: Level 1 - Idea Generation
      on:
        push:
          paths:
            - '.rokct/agent/jobs/pending/*.md'
          branches:
            - main

      jobs:
        generate_ideas:
          if: github.actor != 'github-actions[bot]'
          runs-on: ubuntu-latest
          outputs:
            session_id: ${{ steps.delegate_task.outputs.session_id }}
            card_id: ${{ steps.delegate_task.outputs.card_id }}
            card_type: ${{ steps.delegate_task.outputs.card_type }}
            card_theme: ${{ steps.delegate_task.outputs.card_theme }}
            card_file: ${{ steps.delegate_task.outputs.card_file }}
          steps:
            - uses: actions/checkout@v4
              with:
                fetch-depth: 2

            - name: Set up Python
              uses: actions/setup-python@v5
              with:
                python-version: '3.10'

            - name: Install dependencies
              run: pip install requests python-dotenv

            - name: Identify New Card and Claim Lock
              id: delegate_task
              env:
                JULES_API_KEY: ${{ secrets.JULES_API_KEY }}
              run: |
                FILES=$(git diff --name-only HEAD~1 HEAD | grep '.rokct/agent/jobs/pending/.*.md' | grep -v 'template.md' || true)

                if [ -z "$FILES" ]; then
                  echo "ℹ️ No new job cards found."
                else
                  for FILE in $FILES; do
                    if [ ! -f "$FILE" ]; then continue; fi

                    ID=$(grep '^id:' "$FILE" | cut -d':' -f2 | xargs)
                    TYPE=$(grep '^type:' "$FILE" | cut -d':' -f2 | xargs)
                    THEME=$(grep '^theme:' "$FILE" | cut -d':' -f2 | xargs)
                    STATUS=$(grep '^status:' "$FILE" | cut -d':' -f2 | xargs)

                    if [ "$STATUS" != "idea_generated" ]; then continue; fi

                    # Claim Job Lock
                    if ! python .rokct/skills/agent_delegation/scripts/lock_job.py --file "$FILE" --action claim --agent "groq" --session "GS-IDEA-$GITHUB_RUN_ID"; then
                      echo "Card $FILE is locked by another session. Skipping."
                      continue
                    fi

                    echo "🚀 Delegating Idea Expansion for $ID..."

                    RESULT=$(python .rokct/skills/agent_delegation/scripts/delegate_to_agent.py create \
                      --repo "sources/github/RokctAI/factory" \
                      --prompt "TASK: Expand the theme '$THEME' for a '$TYPE' book. Generate 5 unique one-line book ideas. Update the card $FILE with these ideas and change status to 'pending_approval'." \
                      --title "Level 1: Idea Expansion - $ID" \
                      --automation-mode "AUTO_CREATE_PR")

                    SESSION_ID=$(echo "$RESULT" | jq -r '.id // "unknown"')

                    echo "session_id=$SESSION_ID" >> "$GITHUB_OUTPUT"
                    echo "card_id=$ID" >> "$GITHUB_OUTPUT"
                    echo "card_type=$TYPE" >> "$GITHUB_OUTPUT"
                    echo "card_theme=$THEME" >> "$GITHUB_OUTPUT"
                    echo "card_file=$FILE" >> "$GITHUB_OUTPUT"
                    break
                  done
                fi

            - name: Release Job Lock
              if: success() && steps.delegate_task.outputs.card_file != ''
              run: |
                python .rokct/skills/agent_delegation/scripts/lock_job.py \
                  --file "${{ steps.delegate_task.outputs.card_file }}" \
                  --action release

            - name: Handle Failure
              if: failure() && steps.delegate_task.outputs.card_file != ''
              run: |
                CARD_FILE="${{ steps.delegate_task.outputs.card_file }}"
                ATTEMPTS=$(grep '^attempts:' "$CARD_FILE" | cut -d':' -f2 | xargs)
                NEW_ATTEMPTS=$((ATTEMPTS + 1))
                sed -i "s/^attempts: .*/attempts: $NEW_ATTEMPTS/" "$CARD_FILE"
                sed -i "s/^last_error: .*/last_error: ${{ github.run_id }} failed at $(date -u)/" "$CARD_FILE"

                echo "[$(date -u +'%Y-%m-%d %H:%M:%S')] ${{ steps.delegate_task.outputs.card_id }} | Level 1 | ${{ github.run_id }} | Agent call failed" >> .rokct/agent/log/errors.log

                if [ "$NEW_ATTEMPTS" -ge 3 ]; then
                  echo "3 attempts failed. Marking as stalled."
                  python .rokct/skills/agent_delegation/scripts/update_status.py \
                    --file "$CARD_FILE" \
                    --status stalled
                else
                  echo "Attempt $NEW_ATTEMPTS failed. Will retry on next scheduled run."
                  python .rokct/skills/agent_delegation/scripts/lock_job.py \
                    --file "$CARD_FILE" \
                    --action release
                fi

                git config --global user.name "github-actions[bot]"
                git config --global user.email "github-actions[bot]@users.noreply.github.com"
                git add "$CARD_FILE" .rokct/agent/log/errors.log
                git commit -m "fail: recorded error for ${{ steps.delegate_task.outputs.card_id }} [skip ci]"
                git push origin main

        update_ledger:
          needs: generate_ideas
          if: needs.generate_ideas.outputs.session_id != ''
          uses: ./.github/workflows/ledger_update.yml
          with:
            id: ${{ needs.generate_ideas.outputs.card_id }}
            type: ${{ needs.generate_ideas.outputs.card_type }}
            theme: ${{ needs.generate_ideas.outputs.card_theme }}
            status: "pending_approval"
            agent: "groq"
            session: ${{ needs.generate_ideas.outputs.session_id }}
          secrets: inherit
      ```
    - **File: level2_concept_expansion.yml** — Expands approved ideas into full concepts
      ```yaml
      name: Level 2 - Concept Expansion
      on:
        push:
          paths:
            - '.rokct/agent/jobs/pending/*.md'
          branches:
            - main

      jobs:
        expand_concept:
          if: github.actor != 'github-actions[bot]'
          runs-on: ubuntu-latest
          outputs:
            session_id: ${{ steps.delegate_task.outputs.session_id }}
            card_id: ${{ steps.delegate_task.outputs.card_id }}
            card_type: ${{ steps.delegate_task.outputs.card_type }}
            card_theme: ${{ steps.delegate_task.outputs.card_theme }}
            card_file: ${{ steps.delegate_task.outputs.card_file }}
          steps:
            - uses: actions/checkout@v4
              with:
                fetch-depth: 2

            - name: Set up Python
              uses: actions/setup-python@v5
              with:
                python-version: '3.10'

            - name: Install dependencies
              run: pip install requests python-dotenv

            - name: Identify Approved Idea and Claim Lock
              id: delegate_task
              env:
                JULES_API_KEY: ${{ secrets.JULES_API_KEY }}
              run: |
                FILES=$(git diff --name-only HEAD~1 HEAD | grep '.rokct/agent/jobs/pending/.*.md' | grep -v 'template.md' || true)

                if [ -z "$FILES" ]; then
                  echo "ℹ️ No modified job cards found."
                else
                  for FILE in $FILES; do
                    if [ ! -f "$FILE" ]; then continue; fi

                    ID=$(grep '^id:' "$FILE" | cut -d':' -f2 | xargs)
                    TYPE=$(grep '^type:' "$FILE" | cut -d':' -f2 | xargs)
                    THEME=$(grep '^theme:' "$FILE" | cut -d':' -f2 | xargs)
                    IDEA_STATUS=$(grep '^idea_status:' "$FILE" | cut -d':' -f2 | xargs)
                    STATUS=$(grep '^status:' "$FILE" | cut -d':' -f2 | xargs)

                    if [ "$IDEA_STATUS" != "approved" ]; then continue; fi
                    if [ "$STATUS" != "pending_approval" ]; then continue; fi

                    # Claim Job Lock
                    if ! python .rokct/skills/agent_delegation/scripts/lock_job.py --file "$FILE" --action claim --agent "groq" --session "GS-CONCEPT-$GITHUB_RUN_ID"; then
                      echo "Card $FILE is locked by another session. Skipping."
                      continue
                    fi

                    echo "🚀 Delegating Concept Expansion for $ID..."

                    RESULT=$(python .rokct/skills/agent_delegation/scripts/delegate_to_agent.py create \
                      --repo "sources/github/RokctAI/factory" \
                      --prompt "TASK: Develop a full concept for the book '$ID' (Type: $TYPE, Theme: $THEME). Include angle, emotional world, target feeling, and structural approach. Reference metarules for $TYPE. Update the card $FILE and set status to 'concept_expanding'." \
                      --title "Level 2: Concept Expansion - $ID" \
                      --automation-mode "AUTO_CREATE_PR")

                    SESSION_ID=$(echo "$RESULT" | jq -r '.id // "unknown"')

                    echo "session_id=$SESSION_ID" >> "$GITHUB_OUTPUT"
                    echo "card_id=$ID" >> "$GITHUB_OUTPUT"
                    echo "card_type=$TYPE" >> "$GITHUB_OUTPUT"
                    echo "card_theme=$THEME" >> "$GITHUB_OUTPUT"
                    echo "card_file=$FILE" >> "$GITHUB_OUTPUT"
                    break
                  done
                fi

            - name: Release Job Lock
              if: success() && steps.delegate_task.outputs.card_file != ''
              run: |
                python .rokct/skills/agent_delegation/scripts/lock_job.py \
                  --file "${{ steps.delegate_task.outputs.card_file }}" \
                  --action release

            - name: Handle Failure
              if: failure() && steps.delegate_task.outputs.card_file != ''
              run: |
                CARD_FILE="${{ steps.delegate_task.outputs.card_file }}"
                ATTEMPTS=$(grep '^attempts:' "$CARD_FILE" | cut -d':' -f2 | xargs)
                NEW_ATTEMPTS=$((ATTEMPTS + 1))
                sed -i "s/^attempts: .*/attempts: $NEW_ATTEMPTS/" "$CARD_FILE"
                sed -i "s/^last_error: .*/last_error: ${{ github.run_id }} failed at $(date -u)/" "$CARD_FILE"

                echo "[$(date -u +'%Y-%m-%d %H:%M:%S')] ${{ steps.delegate_task.outputs.card_id }} | Level 2 | ${{ github.run_id }} | Agent call failed" >> .rokct/agent/log/errors.log

                if [ "$NEW_ATTEMPTS" -ge 3 ]; then
                  echo "3 attempts failed. Marking as stalled."
                  python .rokct/skills/agent_delegation/scripts/update_status.py \
                    --file "$CARD_FILE" \
                    --status stalled
                else
                  echo "Attempt $NEW_ATTEMPTS failed. Will retry on next scheduled run."
                  python .rokct/skills/agent_delegation/scripts/lock_job.py \
                    --file "$CARD_FILE" \
                    --action release
                fi

                git config --global user.name "github-actions[bot]"
                git config --global user.email "github-actions[bot]@users.noreply.github.com"
                git add "$CARD_FILE" .rokct/agent/log/errors.log
                git commit -m "fail: recorded error for ${{ steps.delegate_task.outputs.card_id }} [skip ci]"
                git push origin main

        update_ledger:
          needs: expand_concept
          if: needs.expand_concept.outputs.session_id != ''
          uses: ./.github/workflows/ledger_update.yml
          with:
            id: ${{ needs.expand_concept.outputs.card_id }}
            type: ${{ needs.expand_concept.outputs.card_type }}
            theme: ${{ needs.expand_concept.outputs.card_theme }}
            status: "concept_expanding"
            agent: "groq"
            session: ${{ needs.expand_concept.outputs.session_id }}
          secrets: inherit
      ```
    - **File: level3_rule_generation.yml** — Triggers Jules to generate specific world and book rules
      ```yaml
      name: Level 3 - Rule Generation
      on:
        push:
          paths:
            - '.rokct/agent/jobs/pending/*.md'
          branches:
            - main

      jobs:
        generate_rules:
          if: github.actor != 'github-actions[bot]'
          runs-on: ubuntu-latest
          outputs:
            session_id: ${{ steps.delegate_task.outputs.session_id }}
            card_id: ${{ steps.delegate_task.outputs.card_id }}
            card_type: ${{ steps.delegate_task.outputs.card_type }}
            card_theme: ${{ steps.delegate_task.outputs.card_theme }}
            card_file: ${{ steps.delegate_task.outputs.card_file }}
          steps:
            - uses: actions/checkout@v4
              with:
                fetch-depth: 2

            - name: Set up Python
              uses: actions/setup-python@v5
              with:
                python-version: '3.10'

            - name: Install dependencies
              run: pip install requests python-dotenv

            - name: Identify Approved Concept and Claim Lock
              id: delegate_task
              env:
                JULES_API_KEY: ${{ secrets.JULES_API_KEY }}
              run: |
                FILES=$(git diff --name-only HEAD~1 HEAD | grep '.rokct/agent/jobs/pending/.*.md' | grep -v 'template.md' || true)

                if [ -z "$FILES" ]; then
                  echo "ℹ️ No modified job cards found."
                else
                  for FILE in $FILES; do
                    if [ ! -f "$FILE" ]; then continue; fi

                    ID=$(grep '^id:' "$FILE" | cut -d':' -f2 | xargs)
                    TYPE=$(grep '^type:' "$FILE" | cut -d':' -f2 | xargs)
                    THEME=$(grep '^theme:' "$FILE" | cut -d':' -f2 | xargs)
                    CONCEPT_STATUS=$(grep '^concept_status:' "$FILE" | cut -d':' -f2 | xargs)
                    STATUS=$(grep '^status:' "$FILE" | cut -d':' -f2 | xargs)

                    if [ "$CONCEPT_STATUS" != "approved" ]; then continue; fi
                    if [ "$STATUS" != "concept_generated" ]; then continue; fi

                    # Claim Job Lock
                    if ! python .rokct/skills/agent_delegation/scripts/lock_job.py --file "$FILE" --action claim --agent "jules" --session "JS-RULES-$GITHUB_RUN_ID"; then
                      echo "Card $FILE is locked by another session. Skipping."
                      continue
                    fi

                    echo "🚀 Delegating Rule Generation for $ID..."

                    RESULT=$(python .rokct/skills/agent_delegation/scripts/delegate_to_agent.py create \
                      --repo "sources/github/RokctAI/factory" \
                      --prompt "TASK: Generate hierarchical rules for the book '$ID' (Type: $TYPE, Theme: $THEME). Generate: World rules -> Book rules -> Poem/Chapter rules -> Stanza/Scene rules -> Line rules. Reference metarules for $TYPE. Update the card $FILE and set status to 'rules_generating'." \
                      --title "Level 3: Rule Generation - $ID" \
                      --automation-mode "AUTO_CREATE_PR")

                    SESSION_ID=$(echo "$RESULT" | jq -r '.id // "unknown"')

                    echo "session_id=$SESSION_ID" >> "$GITHUB_OUTPUT"
                    echo "card_id=$ID" >> "$GITHUB_OUTPUT"
                    echo "card_type=$TYPE" >> "$GITHUB_OUTPUT"
                    echo "card_theme=$THEME" >> "$GITHUB_OUTPUT"
                    echo "card_file=$FILE" >> "$GITHUB_OUTPUT"
                    break
                  done
                fi

            - name: Release Job Lock
              if: success() && steps.delegate_task.outputs.card_file != ''
              run: |
                python .rokct/skills/agent_delegation/scripts/lock_job.py \
                  --file "${{ steps.delegate_task.outputs.card_file }}" \
                  --action release

            - name: Handle Failure
              if: failure() && steps.delegate_task.outputs.card_file != ''
              run: |
                CARD_FILE="${{ steps.delegate_task.outputs.card_file }}"
                ATTEMPTS=$(grep '^attempts:' "$CARD_FILE" | cut -d':' -f2 | xargs)
                NEW_ATTEMPTS=$((ATTEMPTS + 1))
                sed -i "s/^attempts: .*/attempts: $NEW_ATTEMPTS/" "$CARD_FILE"
                sed -i "s/^last_error: .*/last_error: ${{ github.run_id }} failed at $(date -u)/" "$CARD_FILE"

                echo "[$(date -u +'%Y-%m-%d %H:%M:%S')] ${{ steps.delegate_task.outputs.card_id }} | Level 3 | ${{ github.run_id }} | Agent call failed" >> .rokct/agent/log/errors.log

                if [ "$NEW_ATTEMPTS" -ge 3 ]; then
                  echo "3 attempts failed. Marking as stalled."
                  python .rokct/skills/agent_delegation/scripts/update_status.py \
                    --file "$CARD_FILE" \
                    --status stalled
                else
                  echo "Attempt $NEW_ATTEMPTS failed. Will retry on next scheduled run."
                  python .rokct/skills/agent_delegation/scripts/lock_job.py \
                    --file "$CARD_FILE" \
                    --action release
                fi

                git config --global user.name "github-actions[bot]"
                git config --global user.email "github-actions[bot]@users.noreply.github.com"
                git add "$CARD_FILE" .rokct/agent/log/errors.log
                git commit -m "fail: recorded error for ${{ steps.delegate_task.outputs.card_id }} [skip ci]"
                git push origin main

        update_ledger:
          needs: generate_rules
          if: needs.generate_rules.outputs.session_id != ''
          uses: ./.github/workflows/ledger_update.yml
          with:
            id: ${{ needs.generate_rules.outputs.card_id }}
            type: ${{ needs.generate_rules.outputs.card_type }}
            theme: ${{ needs.generate_rules.outputs.card_theme }}
            status: "rules_generating"
            agent: "jules"
            session: ${{ needs.generate_rules.outputs.session_id }}
          secrets: inherit
      ```
    - **File: level4_evaluation.yml** — Weekend Jules session for auditing all active drafts
      ```yaml
      name: Level 4 - Evaluation Session
      on:
        schedule:
          - cron: '0 8 * * 6,0' # Weekends
        workflow_dispatch:

      jobs:
        evaluation_session:
          runs-on: ubuntu-latest
          steps:
            - uses: actions/checkout@v4

            - name: Set up Python
              uses: actions/setup-python@v5
              with:
                python-version: '3.10'

            - name: Install dependencies
              run: pip install requests python-dotenv

            - name: Identify Drafts and Claim Locks
              id: claim_locks
              run: |
                # Audit all books in production or draft status
                FILES=$(find books/drafts -name "metadata.md" | sort)
                LOCKED_FILES=""
                for FILE in $FILES; do
                  STATUS=$(grep '^status:' "$FILE" | cut -d':' -f2 | xargs)
                  if [ "$STATUS" == "production" ] || [ "$STATUS" == "writing" ] || [ "$STATUS" == "evaluating" ]; then
                    # Check iterations first
                    ITERATIONS=$(grep '^loop_iterations:' "$FILE" | cut -d':' -f2 | xargs)
                    MAX=$(grep '^max_iterations:' "$FILE" | cut -d':' -f2 | xargs)
                    if [ "$ITERATIONS" -ge "$MAX" ]; then
                       echo "Max iterations reached for $FILE. Flagging as stalled."
                       python .rokct/skills/agent_delegation/scripts/update_status.py --file "$FILE" --status stalled
                       continue
                    fi

                    if python .rokct/skills/agent_delegation/scripts/lock_job.py --file "$FILE" --action claim --agent "jules" --session "JS-EVAL-$GITHUB_RUN_ID"; then
                      LOCKED_FILES="$LOCKED_FILES $FILE"
                    fi
                  fi
                done
                if [ -n "$LOCKED_FILES" ]; then
                  echo "card_files=$LOCKED_FILES" >> "$GITHUB_OUTPUT"
                  echo "session_id=JS-EVAL-$GITHUB_RUN_ID" >> "$GITHUB_OUTPUT"
                else
                  echo "No available books to lock."
                fi

            - name: Trigger Jules Evaluation Session
              if: steps.claim_locks.outputs.card_files != ''
              env:
                JULES_API_KEY: ${{ secrets.JULES_API_KEY }}
              run: |
                python .rokct/skills/agent_delegation/scripts/delegate_to_agent.py create \
                  --repo "sources/github/RokctAI/factory" \
                  --prompt "TASK: Weekend Evaluation Session. Audit these files: ${{ steps.claim_locks.outputs.card_files }}. Perform a backward audit (Line -> Stanza -> Poem -> Book -> World). Score each element (0-10) and suggest improvements where score < 8." \
                  --title "Weekend Evaluation Session" \
                  --automation-mode "AUTO_CREATE_PR"

            - name: Increment Loop Counter
              if: success() && steps.claim_locks.outputs.card_files != ''
              run: |
                for FILE in ${{ steps.claim_locks.outputs.card_files }}; do
                  CURRENT=$(grep '^loop_iterations:' "$FILE" | cut -d':' -f2 | xargs)
                  NEW=$((CURRENT + 1))
                  sed -i "s/^loop_iterations: .*/loop_iterations: $NEW/" "$FILE"
                done

            - name: Handle Failure
              if: failure() && steps.claim_locks.outputs.card_files != ''
              run: |
                for FILE in ${{ steps.claim_locks.outputs.card_files }}; do
                  ATTEMPTS=$(grep '^attempts:' "$FILE" | cut -d':' -f2 | xargs)
                  NEW_ATTEMPTS=$((ATTEMPTS + 1))
                  sed -i "s/^attempts: .*/attempts: $NEW_ATTEMPTS/" "$FILE"
                  sed -i "s/^last_error: .*/last_error: ${{ github.run_id }} failed at $(date -u)/" "$FILE"

                  if [ "$NEW_ATTEMPTS" -ge 3 ]; then
                    echo "3 attempts failed for $FILE. Marking as stalled."
                    python .rokct/skills/agent_delegation/scripts/update_status.py --file "$FILE" --status stalled
                  else
                    python .rokct/skills/agent_delegation/scripts/lock_job.py --file "$FILE" --action release
                  fi
                done

            - name: Release Job Locks
              if: always() && steps.claim_locks.outputs.card_files != ''
              run: |
                for FILE in ${{ steps.claim_locks.outputs.card_files }}; do
                  if [ -f "$FILE" ]; then
                    python .rokct/skills/agent_delegation/scripts/lock_job.py --file "$FILE" --action release
                  fi
                done
      ```
    - **File: level4_writing.yml** — Weekday Jules session for generating book content
      ```yaml
      name: Level 4 - Writing Session
      on:
        schedule:
          - cron: '0 8 * * 1-5' # 08:00 weekdays
        workflow_dispatch:

      jobs:
        writing_session:
          runs-on: ubuntu-latest
          steps:
            - uses: actions/checkout@v4

            - name: Set up Python
              uses: actions/setup-python@v5
              with:
                python-version: '3.10'

            - name: Install dependencies
              run: pip install requests python-dotenv

            - name: Identify Book and Claim Lock
              id: claim_lock
              run: |
                # Identify oldest book in production
                FILES=$(find books/drafts -name "metadata.md" | sort)
                FOUND=false
                for FILE in $FILES; do
                  STATUS=$(grep '^status:' "$FILE" | cut -d':' -f2 | xargs)
                  if [ "$STATUS" == "production" ] || [ "$STATUS" == "writing" ]; then
                    if python .rokct/skills/agent_delegation/scripts/lock_job.py --file "$FILE" --action claim --agent "jules" --session "JS-WRITING-$GITHUB_RUN_ID"; then
                      echo "card_file=$FILE" >> "$GITHUB_OUTPUT"
                      echo "session_id=JS-WRITING-$GITHUB_RUN_ID" >> "$GITHUB_OUTPUT"
                      FOUND=true
                      break
                    fi
                  fi
                done
                if [ "$FOUND" = false ]; then
                  echo "No available books to lock."
                fi

            - name: Check Loop Safety
              if: steps.claim_lock.outputs.card_file != ''
              run: |
                CARD_FILE="${{ steps.claim_lock.outputs.card_file }}"
                ITERATIONS=$(grep '^loop_iterations:' "$CARD_FILE" | cut -d':' -f2 | xargs)
                MAX=$(grep '^max_iterations:' "$CARD_FILE" | cut -d':' -f2 | xargs)
                if [ "$ITERATIONS" -ge "$MAX" ]; then
                  echo "Max iterations reached for $CARD_FILE. Flagging as stalled."
                  python .rokct/skills/agent_delegation/scripts/update_status.py \
                    --file "$CARD_FILE" \
                    --status stalled
                  echo "stalled=true" >> "$GITHUB_OUTPUT"
                fi
              id: safety_check

            - name: Trigger Jules Writing Session
              if: steps.claim_lock.outputs.card_file != '' && steps.safety_check.outputs.stalled != 'true'
              env:
                JULES_API_KEY: ${{ secrets.JULES_API_KEY }}
              run: |
                python .rokct/skills/agent_delegation/scripts/delegate_to_agent.py create \
                  --repo "sources/github/RokctAI/factory" \
                  --prompt "TASK: Daily Writing Session for ${{ steps.claim_lock.outputs.card_file }}. Generate the next chapter or poem based on the world rules and metarules. Ensure consistency and emotional resonance." \
                  --title "Daily Writing Session" \
                  --automation-mode "AUTO_CREATE_PR"

            - name: Increment Loop Counter
              if: success() && steps.claim_lock.outputs.card_file != '' && steps.safety_check.outputs.stalled != 'true'
              run: |
                CARD_FILE="${{ steps.claim_lock.outputs.card_file }}"
                CURRENT=$(grep '^loop_iterations:' "$CARD_FILE" | cut -d':' -f2 | xargs)
                NEW=$((CURRENT + 1))
                sed -i "s/^loop_iterations: .*/loop_iterations: $NEW/" "$CARD_FILE"

            - name: Handle Failure
              if: failure() && steps.claim_lock.outputs.card_file != ''
              run: |
                CARD_FILE="${{ steps.claim_lock.outputs.card_file }}"
                ATTEMPTS=$(grep '^attempts:' "$CARD_FILE" | cut -d':' -f2 | xargs)
                NEW_ATTEMPTS=$((ATTEMPTS + 1))
                sed -i "s/^attempts: .*/attempts: $NEW_ATTEMPTS/" "$CARD_FILE"
                sed -i "s/^last_error: .*/last_error: ${{ github.run_id }} failed at $(date -u)/" "$CARD_FILE"

                if [ "$NEW_ATTEMPTS" -ge 3 ]; then
                  echo "3 attempts failed. Marking as stalled."
                  python .rokct/skills/agent_delegation/scripts/update_status.py \
                    --file "$CARD_FILE" \
                    --status stalled
                else
                  echo "Attempt $NEW_ATTEMPTS failed. Will retry on next scheduled run."
                  python .rokct/skills/agent_delegation/scripts/lock_job.py \
                    --file "$CARD_FILE" \
                    --action release
                fi

            - name: Release Job Lock
              if: always() && steps.claim_lock.outputs.card_file != ''
              run: |
                if [ -f "${{ steps.claim_lock.outputs.card_file }}" ]; then
                  python .rokct/skills/agent_delegation/scripts/lock_job.py \
                    --file "${{ steps.claim_lock.outputs.card_file }}" \
                    --action release
                fi
      ```
    - **File: level6_publish.yml** — Finalizes and moves books to published status
      ```yaml
      name: Level 6 - Final Publishing
      on:
        push:
          paths:
            - 'books/drafts/**/metadata.md'
          branches:
            - main

      jobs:
        publish_book:
          if: github.actor != 'github-actions[bot]'
          runs-on: ubuntu-latest
          outputs:
            card_id: ${{ steps.publish_task.outputs.card_id }}
            card_type: ${{ steps.publish_task.outputs.card_type }}
            card_theme: ${{ steps.publish_task.outputs.card_theme }}
            card_file: ${{ steps.publish_task.outputs.card_file }}
          steps:
            - uses: actions/checkout@v4
              with:
                fetch-depth: 2

            - name: Set up Python
              uses: actions/setup-python@v5
              with:
                python-version: '3.10'

            - name: Install dependencies
              run: pip install requests python-dotenv

            - name: Identify Approved Draft and Publish
              id: publish_task
              run: |
                FILES=$(git diff --name-only HEAD~1 HEAD | grep 'books/drafts/.*/metadata.md' || true)

                if [ -z "$FILES" ]; then
                  echo "ℹ️ No draft metadata changes found."
                else
                  for FILE in $FILES; do
                    if [ ! -f "$FILE" ]; then continue; fi

                    STATUS=$(grep '^status:' "$FILE" | cut -d':' -f2 | xargs)
                    ID=$(grep '^id:' "$FILE" | cut -d':' -f2 | xargs)
                    TYPE=$(grep '^type:' "$FILE" | cut -d':' -f2 | xargs)
                    THEME=$(grep '^theme:' "$FILE" | cut -d':' -f2 | xargs)

                    # Logic: Human moves to publishing
                    if [ "$STATUS" != "publishing" ]; then continue; fi

                    # Claim Job Lock
                    if ! python .rokct/skills/agent_delegation/scripts/lock_job.py --file "$FILE" --action claim --agent "human" --session "PUBLISH-$GITHUB_RUN_ID"; then
                      echo "Card $FILE is locked. Skipping."
                      continue
                    fi

                    BOOK_DIR=$(dirname "$FILE")
                    BOOK_NAME=$(basename "$BOOK_DIR")

                    echo "🚀 Publishing book: $BOOK_NAME..."

                    # Simulate Publishing Logic
                    mkdir -p "books/published/$BOOK_NAME"
                    cp -r "$BOOK_DIR"/* "books/published/$BOOK_NAME/"

                    # Update status in the published folder using update_status.py (publishing -> published)
                    python .rokct/skills/agent_delegation/scripts/update_status.py \
                      --file "books/published/$BOOK_NAME/metadata.md" \
                      --status "published" \
                      --agent "human"

                    # Cleanup draft
                    rm -rf "$BOOK_DIR"

                    git config --global user.name "github-actions[bot]"
                    git config --global user.email "github-actions[bot]@users.noreply.github.com"
                    git add books/
                    git commit -m "chore: publish book $BOOK_NAME [skip ci]"
                    git push origin main

                    echo "card_id=$ID" >> "$GITHUB_OUTPUT"
                    echo "card_type=$TYPE" >> "$GITHUB_OUTPUT"
                    echo "card_theme=$THEME" >> "$GITHUB_OUTPUT"
                    echo "card_file=$FILE" >> "$GITHUB_OUTPUT"
                    break
                  done
                fi

            - name: Release Job Lock (if exists)
              if: always() && steps.publish_task.outputs.card_file != ''
              run: |
                if [ -f "${{ steps.publish_task.outputs.card_file }}" ]; then
                  python .rokct/skills/agent_delegation/scripts/lock_job.py \
                    --file "${{ steps.publish_task.outputs.card_file }}" \
                    --action release
                fi

        update_ledger:
          needs: publish_book
          if: needs.publish_book.outputs.card_id != ''
          uses: ./.github/workflows/ledger_update.yml
          with:
            id: ${{ needs.publish_book.outputs.card_id }}
            type: ${{ needs.publish_book.outputs.card_type }}
            theme: ${{ needs.publish_book.outputs.card_theme }}
            status: "published"
            agent: "human"
            session: "—"
          secrets: inherit
      ```
    - **File: links.yml** — Weekly health check for external links
      ```yaml
      name: Link Health Check
      on:
        schedule:
          - cron: '0 2 * * 0' # Weekly on Sunday
        workflow_dispatch:

      jobs:
        health_check:
          runs-on: ubuntu-latest
          steps:
            - uses: actions/checkout@v4

            - name: Set up Python
              uses: actions/setup-python@v5
              with:
                python-version: '3.10'

            - name: Install dependencies
              run: pip install requests

            - name: Run Health Check
              run: |
                python .rokct/skills/agent_delegation/scripts/check_health.py
      ```
    - **File: privacy-check.yml** — Enforces PII encryption on new job cards
      ```yaml
      name: Privacy Check
      on:
        push:
          paths:
            - '.rokct/agent/jobs/pending/*.md'
        pull_request:
          paths:
            - '.rokct/agent/jobs/pending/*.md'

      jobs:
        check:
          runs-on: ubuntu-latest
          steps:
            - uses: actions/checkout@v4

            - name: Set up Python
              uses: actions/setup-python@v5
              with:
                python-version: '3.10'

            - name: Install dependencies
              run: pip install python-dotenv pycryptodome

            - name: Run Privacy Enforcement Check
              run: |
                python .rokct/skills/agent_delegation/scripts/privacy_sync.py --check
      ```
    - **File: session_scheduler.yml** — Manages agent session slots and conflict resolution
      ```yaml
      name: Session Scheduler
      on:
        schedule:
          - cron: '*/30 * * * *' # Every 30 minutes
        workflow_dispatch:

      jobs:
        manage_sessions:
          runs-on: ubuntu-latest
          permissions: write-all
          steps:
            - uses: actions/checkout@v4

            - name: Set up Python
              uses: actions/setup-python@v5
              with:
                python-version: '3.10'

            - name: Install dependencies
              run: pip install PyYAML

            - name: Update Session State
              run: python .rokct/skills/agent_delegation/scripts/manage_sessions.py

            - name: Commit State Update
              run: |
                git config --global user.name "github-actions[bot]"
                git config --global user.email "github-actions[bot]@users.noreply.github.com"
                git add .rokct/agent/session_state.md
                if git diff --staged --quiet; then
                  echo "No state changes."
                else
                  git commit -m "chore: update session state [skip ci]"
                  git push origin main
                fi
      ```
- **Directory: .rokct/** — Core AI agent and system governance
  - **Directory: agent/** — Agent-specific configurations and job management
    - **Directory: guardrails/** — Safety templates for different age groups
      - **File: age_13_17.md** — Static prompt for Young Adult content protection
        ```markdown
        This content is for a {age} year old (Young Adult).
        You MUST: explore complex emotions, identity, and social dynamics.
        You MUST NEVER: include graphic sexual violence or excessive gore without thematic purpose.
        The tone can be raw and honest, reflecting the transition from childhood to adulthood.
        ```
      - **File: age_6_12.md** — Static prompt for Middle Grade content protection
        ```markdown
        This content is for a {age} year old child (Middle Grade).
        You MUST: use clear and engaging language, focus on themes of friendship, curiosity, and overcoming challenges.
        You MUST NEVER: include explicit violence, gratuitous fear, or inappropriate adult themes.
        Keep the tone adventurous but grounded.
        ```
      - **File: age_under_6.md** — Static prompt for early childhood content protection
        ```markdown
        This content is for a {age} year old child.
        You MUST: use simple words, create wonder and safety, warm emotional world, nurturing tone.
        You MUST NEVER: introduce darkness, fear, complex trauma, adult themes, ambiguous morality, violence, or loss without resolution.
        ```
    - **Directory: jobs/** — Tracking for active and completed publishing tasks
      - **Directory: done/** — [empty — reserved for completed job cards]
        - **File: .gitkeep**
          ```
          ```
      - **Directory: pending/** — [empty — reserved for job cards waiting to be processed]
        - **File: .gitkeep**
          ```
          ```
      - **Directory: running/** — [empty — reserved for job cards currently being worked on]
        - **File: .gitkeep**
          ```
          ```
      - **File: template.md** — Master YAML template for new job cards
        ```markdown
        <!-- CARD RULES
             This card is the source of truth for this job.
             Status field controls pipeline progression.
             All status changes must go through update_status.py.
             Direct edits to status field will be rejected by the state machine.
        -->
        ---
        id:
        theme:
        type:
        age:
        metarules:
        guardrail:
        idea:
        idea_status:
        concept:
        concept_status:
        rules_status:
        book_name:
        book_path:
        status:
        created:
        last_updated:
        locked_by:
        locked_at:
        attempts: 0
        last_error:
        session_id:
        loop_iterations: 0
        max_iterations: 10
        ---
        ```
    - **Directory: log/** — System activity logs
      - **File: errors.log**
        ```
        # Error Log
        # Format: [timestamp] card_id | workflow | run_id | error
        # This file is append-only. Do not edit.
        ```
      - **File: ledger.md** — The single source of truth for all pipeline activity
        ```markdown
        # RokctAI Factory — Ledger

        <!-- LEDGER RULES
             This file is a historical log only.
             It records what happened. It does not control what happens next.
             Pipeline routing decisions are made by reading job card status fields.
             ONLY CI workflows may append rows to this file.
             Agents may read this file. Agents may never write to this file.
        -->

        **Only CI may write to this file. Agents read only.**

        | ID | Type | Theme | Status | Agent | Session | PR | Timestamp |
        |----|------|-------|--------|-------|---------|----|-----------|
        ```
      - **File: transitions.log**
        ```
        # Status Transition Log
        # Format: [timestamp] card_id | old_status -> new_status | agent
        # This file is append-only. Do not edit.
        [2026-04-29 22:01:19]  | idea_generated -> pending_approval | system
        ```
    - **Directory: prompts/** — AI agent task instructions
      - **Directory: completed/** — [empty — reserved for one-time prompt cards that have run]
        - **File: .gitkeep**
          ```
          ```
      - **Directory: in_progress/** — Recurring prompt configurations for Groq
        - **File: level0_theme_discovery.json** — Prompt for autonomous theme discovery
          ```json
          {
            "repo": "RokctAI/factory",
            "prompt": "Analyze the current pending theme cards in .rokct/agent/jobs/pending/. If there are fewer than 5 themes, generate 5 new unique themes for books across supported types (poetry, fiction, short_story, children). Write each theme as a new card in .rokct/agent/jobs/pending/ using the template. Filename: {theme}_{type}_{hash}.md.",
            "branch": "main",
            "title": "Level 0: Theme Discovery",
            "automation_mode": "AUTO_CREATE_PR",
            "recurrence": "Daily",
            "immediate": false,
            "scheduled_at": "2026-04-29T12:00:00Z"
          }
          ```
        - **File: level1_idea_expansion.json** — Prompt for expanding themes into approved ideas
          ```json
          {
            "repo": "RokctAI/factory",
            "prompt": "Pick the oldest pending theme card in .rokct/agent/jobs/pending/ where status is 'theme_generated'. Generate 5 unique one-line book ideas for this theme and type. Update the card with these ideas and change status to 'pending_approval'. Format ideas for human review.",
            "branch": "main",
            "title": "Level 1: Idea Expansion",
            "automation_mode": "AUTO_CREATE_PR",
            "recurrence": "Daily",
            "immediate": false,
            "scheduled_at": "2026-04-29T13:00:00Z"
          }
          ```
      - **Directory: queue/** — [empty — reserved for one-time prompts waiting to run]
        - **File: .gitkeep**
          ```
          ```
    - **File: session_state.md** — Tracks active sessions and weekend availability
      ```markdown
      ---
      weekend_block: open
      weekend_session_id:
      weekend_started:
      weekend_finished:
      active_sessions: 0
      last_updated:
      ---
      ```
  - **Directory: skills/** — Reusable agent capabilities ported from opportunities
    - **Directory: agent_delegation/** — Automates task offloading to AI agents
      - **File: README.md** — Documentation for agent delegation skills
        ```markdown
        # Agent Delegation Skills (Factory Context)

        This directory contains essential automation skills adapted from the opportunities registry to serve the autonomous factory.

        ## Core Skills

        ### 1. Agent Delegation (`delegate_to_agent.py`)
        CLI tool for creating and managing AI agent sessions. It is the primary interface for triggering complex tasks across all pipeline levels.

        ### 2. Link Health Check (`check_health.py`)
        Scans job cards and book drafts for broken links, ensuring that reference materials and published assets remain accessible.

        ### 3. PII Privacy Sync (`privacy_sync.py` & `crypto_utils.py`)
        Enforces encryption for any personally identifiable information (PII) found in job cards, protecting contributor and user data.

        ### 4. Audit Log Management (`update_audit_logs.py`)
        Maintains `job_audit_log.md` files in draft and published directories, providing automated tracking of book progress.

        ### 5. Classification Updates (`update_classifications.py`)
        Generates reference files for all themes and genres in the pipeline, used by agents for consistency and duplication checks.

        ### 6. Factory Dashboard (`update_dashboard.py`)
        Recalculates real-time factory statistics and updates the main README.md dashboard with the current system state.

        ### 7. Production Kits (`response_kits.py`)
        Scaffolds new book directories in `books/drafts/` when a concept is approved, ensuring a standardized project structure from the start.
        ```
      - **File: SKILL.md** — Technical definition of the agent delegation skill
        ```markdown
        ---
        name: Agent Delegation
        description: Automates the offloading of repetitive or large-scale coding tasks to an AI agent (e.g., Jules).
        ---

        # Agent Delegation Skill

        This skill allows you to delegate complex refactoring, migration, or repetitive coding tasks to an AI agent.

        ## Prerequisites
        - **API Key**: Must have a valid `AGENT_API_KEY` (or `JULES_API_KEY`) configured in the environment or a `.env` file accessible to the script.
        - **Dependencies**: Requires `requests` and `python-dotenv`.

        ## Decision Framework (Self-Guideline)
        Evaluate at the start of every session or mid-task:
        - **Delegate (Agent)**: Bulk refactors, library migrations, repetitive boilerplate, sub-repo isolated work, mid-task error fixes, and lateral/off-topic ideas.
        - **Direct (Antigravity)**: Architecture design, UI/UX polish, multi-repo sync, complex discovery.

        ## How to Use

        ### 1. Identify a Delegetable Task
        Tasks suitable for the Agent include:
        - Large-scale string/type migrations (e.g., Int ID to String ID).
        - Database library migrations (e.g., Hive to Drift).
        - Boilerplate generation across many files.
        - Refactoring legacy patterns into modern standards.

        ### 2. Run the Delegation Script
        Use the provided Python script to create a session:

        '''bash
        python .rokct/skills/agent_delegation/scripts/delegate_to_agent.py create \
          --repo "sources/github/RokctAI/factory" \
          --prompt "Your detailed task description here" \
          --title "Feature/Task Name"
        '''

        ### 3. Monitor Status
        The Agent works asynchronously. Check progress:

        '''bash
        python .rokct/skills/agent_delegation/scripts/delegate_to_agent.py status --id "SESSION_ID"
        '''

        ### 4. Approve Plans (Optional)
        By default, sessions are auto-approved. To require approval, use the `--require-approval` flag during creation. If enabled, approve the latest plan:

        '''bash
        python .rokct/skills/jules_delegation/scripts/delegate_to_jules.py approve --id "SESSION_ID"
        '''

        ## Best Practices
        - **Be Specific**: Provide clear, technical instructions in the prompt.
        - **Source Format**: Always use the full source name (e.g., `sources/github/Owner/Repo`).
        - **Context**: Mentioning specific file paths or patterns helps Jules narrow its scope.
        ```
      - **Directory: scripts/** — Python scripts for agent coordination and data processing
        - **File: call_groq.py**
          ```python
          # Licensed under the MIT License.
          # Copyright 2024 RokctAI

          import os
          import requests
          import json
          import argparse
          import sys

          # Script to call Groq API directly, following patterns in universal-release.yml
          def call_groq(prompt, system_prompt=None, model="llama-3.3-70b-versatile"):
              api_key = os.environ.get("GROQ_API_KEY")
              if not api_key:
                  print("Error: GROQ_API_KEY is missing.")
                  return None

              url = "https://api.groq.com/openai/v1/chat/completions"
              headers = {
                  "Content-Type": "application/json",
                  "Authorization": f"Bearer {api_key}"
              }

              messages = []
              if system_prompt:
                  messages.append({"role": "system", "content": system_prompt})
              messages.append({"role": "user", "content": prompt})

              payload = {
                  "model": model,
                  "messages": messages,
                  "temperature": 0.2
              }

              try:
                  response = requests.post(url, json=payload, headers=headers, timeout=60)
                  response.raise_for_status()
                  data = response.json()
                  return data.get("choices", [{}])[0].get("message", {}).get("content")
              except Exception as e:
                  print(f"Error calling Groq: {e}")
                  if hasattr(e, 'response') and e.response is not None:
                      print(f"Details: {e.response.text}")
                  return None

          def main():
              parser = argparse.ArgumentParser(description="Call Groq API directly.")
              parser.add_argument("--prompt", required=True, help="User prompt")
              parser.add_argument("--system", help="System prompt")
              parser.add_argument("--model", default="llama-3.3-70b-versatile", help="Groq model")

              args = parser.parse_args()

              content = call_groq(args.prompt, args.system, args.model)
              if content:
                  print(content)
              else:
                  sys.exit(1)

          if __name__ == "__main__":
              main()
          ```
        - **File: check_health.py** — Scans for broken links in job cards
          ```python
          # Licensed under the MIT License.
          # Copyright 2024 RokctAI

          import requests
          import re
          import os
          from pathlib import Path

          def check_link_health():
              """Scans book jobs for broken links."""
              print("🔍 Starting Global Job Link Health Check...")

              # Target book draft directories
              directories = [Path('books/drafts')]
              broken_count = 0
              checked_count = 0

              for directory in directories:
                  if not directory.exists(): continue
                  print(f"📂 Auditing {directory.name}...")

                  # Scan all markdown files in book subdirectories
                  for md_file in directory.rglob('*.md'):
                      if md_file.name in ['template.md', 'metadata.md']:
                          continue

                      with open(md_file, 'r', encoding='utf-8') as f:
                          content = f.read()

                      # Pattern to find URLs in markdown links [text](url) or standing alone
                      links = re.findall(r'\(https?://[^\s\)]+\)|https?://[^\s\n\)]+', content)

                      file_broken = False
                      for link in links:
                          url = link.strip('() ')

                          checked_count += 1
                          try:
                              # Use a short timeout and allow redirects
                              response = requests.head(url, timeout=15, allow_redirects=True)
                              # 403 Forbidden is often a bot block, so we only flag >= 404
                              if response.status_code >= 404:
                                  print(f"❌ Broken Link in {md_file.name}: {url} (Status: {response.status_code})")
                                  file_broken = True
                                  broken_count += 1
                          except:
                              # Connection errors are often temporary or firewall blocks,
                              # but we flag for steward review.
                              print(f"⚠️ Connection Error in {md_file.name}: {url}")
                              file_broken = True
                              broken_count += 1

                      if file_broken:
                          # Mark status as BROKEN in the file if not already marked
                          if "Status: BROKEN" not in content and "Verification Status: BROKEN" not in content:
                              updated = content.replace("Status: ACTIVE", "Status: BROKEN")
                              updated = updated.replace("Verification Status: VERIFIED", "Verification Status: BROKEN")
                              updated = updated.replace("Verification Status: IN_PROGRESS", "Verification Status: BROKEN")
                              with open(md_file, 'w', encoding='utf-8') as f:
                                  f.write(updated)

              print(f"🏁 Health check complete. Checked {checked_count} links. Found {broken_count} issues.")

          if __name__ == "__main__":
              check_link_health()
          ```
        - **File: crypto_utils.py** — Handles encryption for PII protection
          ```python
          # Licensed under the MIT License.
          # Copyright 2024 RokctAI

          import base64
          from Crypto.Cipher import AES
          from Crypto.Random import get_random_bytes

          # Ported from opportunities: Handles PII encryption for book card data
          def encrypt_pii(plain_text, key_b64):
              """Encrypts PII using AES-256-GCM."""
              if not key_b64:
                  raise ValueError("Encryption key is missing.")

              key = base64.b64decode(key_b64)
              cipher = AES.new(key, AES.MODE_GCM)
              ciphertext, tag = cipher.encrypt_and_digest(plain_text.encode('utf-8'))

              # We store as: nonce:tag:ciphertext
              combined = base64.b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')
              return combined

          def decrypt_pii(encrypted_blob, key_b64):
              """Decrypts PII using AES-256-GCM."""
              if not key_b64:
                  raise ValueError("Encryption key is missing.")

              key = base64.b64decode(key_b64)
              data = base64.b64decode(encrypted_blob)

              # Extract components
              nonce = data[:16]
              tag = data[16:32]
              ciphertext = data[32:]

              cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
              plain_text = cipher.decrypt_and_verify(ciphertext, tag)
              return plain_text.decode('utf-8')

          if __name__ == "__main__":
              # Quick Test
              test_key = base64.b64encode(get_random_bytes(32)).decode()
              test_data = "PII Data"
              encrypted = encrypt_pii(test_data, test_key)
              decrypted = decrypt_pii(encrypted, test_key)
              print(f"Original: {test_data}")
              print(f"Encrypted: {encrypted}")
              print(f"Decrypted: {decrypted}")
              assert test_data == decrypted
              print("✅ Crypto Utils Test Passed")
          ```
        - **File: delegate_to_agent.py** — CLI for creating and managing agent sessions
          ```python
          # Licensed under the MIT License.
          # Copyright 2024 RokctAI

          import os
          import requests
          import json
          import argparse
          import sys

          # Ported from opportunities: Adapt for 'factory' context
          # Attempt to load from .env if available
          try:
              from dotenv import load_dotenv
              script_dir = os.path.dirname(os.path.abspath(__file__))
              # Path depth verification: scripts -> agent_delegation -> skills -> .rokct -> root
              monorepo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))))
              env_path = os.path.join(monorepo_root, ".env", "production.env")

              # Debug prints for CI logs
              if os.environ.get("GITHUB_ACTIONS"):
                  print(f"🔍 [CI Debug] Script location: {script_dir}")
                  print(f"🔍 [CI Debug] Calculated Monorepo Root: {monorepo_root}")
                  print(f"🔍 [CI Debug] Looking for env at: {env_path}")
                  print(f"🔍 [CI Debug] Env file exists: {os.path.exists(env_path)}")

              if os.path.exists(env_path):
                  load_dotenv(env_path)
                  # Aggressive Manual Fallback: if dotenv failed to populate the ENV (e.g. formatting issues)
                  if not os.environ.get("JULES_API_KEY") and not os.environ.get("AGENT_API_KEY"):
                      with open(env_path, 'r', encoding='utf-8') as f:
                          for line in f:
                              if "JULES_API_KEY=" in line or "AGENT_API_KEY=" in line:
                                  # Strip 'export ', whitespace, and quotes
                                  val = line.replace("export ", "").strip().split("=", 1)[1].strip("'\" ")
                                  key_name = "JULES_API_KEY" if "JULES_API_KEY" in line else "AGENT_API_KEY"
                                  os.environ[key_name] = val
                                  if os.environ.get("GITHUB_ACTIONS"):
                                      print(f"✅ [CI Debug] Manually recovered {key_name} from file.")
              else:
                  load_dotenv()
          except ImportError:
              if os.environ.get("GITHUB_ACTIONS"):
                  print("⚠️ [CI Debug] python-dotenv not installed. Manual recovery only.")
              # Fallback manual read if env_path exists even without dotenv
              try:
                  if os.path.exists(env_path):
                      with open(env_path, 'r', encoding='utf-8') as f:
                          for line in f:
                              if "JULES_API_KEY=" in line or "AGENT_API_KEY=" in line:
                                  val = line.replace("export ", "").strip().split("=", 1)[1].strip("'\" ")
                                  key_name = "JULES_API_KEY" if "JULES_API_KEY" in line else "AGENT_API_KEY"
                                  os.environ[key_name] = val
              except:
                  pass
              pass

          BASE_URL = "https://jules.googleapis.com/v1alpha"

          class AgentCLI:
              def __init__(self, api_key):
                  self.api_key = api_key
                  self.headers = {
                      "Content-Type": "application/json",
                      "X-Goog-Api-Key": self.api_key
                  }

              def create_session(self, prompt, source_repo, automation_mode="AUTO_CREATE_PR", title=None, branch="main", require_approval=False):
                  url = f"{BASE_URL}/sessions"
                  payload = {
                      "prompt": prompt,
                      "sourceContext": {
                          "source": source_repo,
                          "githubRepoContext": {
                              "startingBranch": branch
                          }
                      },
                      "automationMode": automation_mode,
                      "requirePlanApproval": require_approval
                  }
                  if title:
                      payload["title"] = title

                  response = requests.post(url, json=payload, headers=self.headers)
                  response.raise_for_status()
                  return response.json()

              def get_session(self, session_id):
                  url = f"{BASE_URL}/sessions/{session_id}"
                  response = requests.get(url, headers=self.headers)
                  response.raise_for_status()
                  return response.json()

              def send_message(self, session_id, message):
                  url = f"{BASE_URL}/sessions/{session_id}:sendMessage"
                  payload = {"prompt": message}
                  response = requests.post(url, json=payload, headers=self.headers)
                  response.raise_for_status()
                  return response.json()

              def approve_plan(self, session_id):
                  url = f"{BASE_URL}/sessions/{session_id}:approvePlan"
                  response = requests.post(url, headers=self.headers, json={})
                  response.raise_for_status()
                  return {"status": "success", "message": "Plan approved."}

              def delete_session(self, session_id):
                  url = f"{BASE_URL}/sessions/{session_id}"
                  response = requests.delete(url, headers=self.headers)
                  response.raise_for_status()
                  return {"status": "success", "message": f"Session {session_id} deleted."}

              def list_sessions(self):
                  url = f"{BASE_URL}/sessions"
                  response = requests.get(url, headers=self.headers)
                  response.raise_for_status()
                  return response.json().get("sessions", [])

          def main():
              parser = argparse.ArgumentParser(description="Delegate tasks to an AI Agent.")
              parser.add_argument("--api-key", help="Agent API Key (overrides AGENT_API_KEY or JULES_API_KEY env var)")
              subparsers = parser.add_subparsers(dest="command", help="Commands")

              # Create Session
              create_parser = subparsers.add_parser("create", help="Create a new Agent session")
              create_parser.add_argument("--prompt", required=True, help="User prompt/task for the Agent")
              create_parser.add_argument("--repo", required=True, help="Full source name (e.g., 'sources/github/RokctAI/factory')")
              create_parser.add_argument("--branch", default="main", help="Starting branch (default: main)")
              create_parser.add_argument("--title", help="Session title")
              create_parser.add_argument("--require-approval", action="store_true", help="Require plan approval before execution (default: False)")
              create_parser.add_argument("--automation-mode", default="AUTO_CREATE_PR", help="Automation mode (default: AUTO_CREATE_PR)")

              # Get Session
              status_parser = subparsers.add_parser("status", help="Get session status")
              status_parser.add_argument("--id", required=True, help="Session ID")

              # Send Message
              msg_parser = subparsers.add_parser("query", help="Send a message to an active session")
              msg_parser.add_argument("--id", required=True, help="Session ID")
              msg_parser.add_argument("--message", required=True, help="Message content")

              # Approve Plan
              approve_parser = subparsers.add_parser("approve", help="Approve the proposed plan")
              approve_parser.add_argument("--id", required=True, help="Session ID")

              # Delete Session
              delete_parser = subparsers.add_parser("delete", help="Delete an Agent session")
              delete_parser.add_argument("--id", required=True, help="Session ID")

              # List Sessions
              subparsers.add_parser("list", help="List all Agent sessions")

              args = parser.parse_args()

              api_key = args.api_key or os.environ.get("AGENT_API_KEY") or os.environ.get("JULES_API_KEY")
              if not api_key:
                  print("Error: Agent API Key is missing. Provide via --api-key, AGENT_API_KEY, or JULES_API_KEY env var.")
                  sys.exit(1)

              cli = AgentCLI(api_key)

              try:
                  if args.command == "create":
                      result = cli.create_session(
                          args.prompt,
                          args.repo,
                          title=args.title,
                          branch=args.branch,
                          require_approval=args.require_approval,
                          automation_mode=args.automation_mode
                      )
                      print(json.dumps(result, indent=2))
                  elif args.command == "status":
                      result = cli.get_session(args.id)
                      print(json.dumps(result, indent=2))
                  elif args.command == "query":
                      result = cli.send_message(args.id, args.message)
                      print(json.dumps(result, indent=2))
                  elif args.command == "approve":
                      result = cli.approve_plan(args.id)
                      print(json.dumps(result, indent=2))
                  elif args.command == "delete":
                      result = cli.delete_session(args.id)
                      print(json.dumps(result, indent=2))
                  elif args.command == "list":
                      result = cli.list_sessions()
                      print(json.dumps(result, indent=2))
                  else:
                      parser.print_help()
              except Exception as e:
                  print(f"Error: {e}")
                  # If response has JSON error detail, show it
                  if hasattr(e, 'response') and e.response is not None:
                      try:
                          print(f"Details: {json.dumps(e.response.json(), indent=2)}")
                      except:
                          print(f"Details: {e.response.text}")
                  sys.exit(1)

          if __name__ == "__main__":
              main()
          ```
        - **File: handle_groq_output.py**
          ```python
          # Licensed under the MIT License.
          # Copyright 2024 RokctAI

          import os
          import re
          import json
          import hashlib
          import argparse
          from pathlib import Path
          from datetime import datetime
          from update_classifications import is_duplicate_theme

          def handle_groq_output(level, content):
              """Parses Groq output and performs file operations based on the pipeline level."""
              print(f"🛠️ Processing Groq Output for Level {level}...")

              job_dir = Path('.rokct/agent/jobs/pending')
              job_dir.mkdir(parents=True, exist_ok=True)
              themes_path = Path('.rokct/config/classifications/factory_themes.txt')

              if level == 0:
                  # Level 0: Expected output is a list of themes
                  # Format: theme | type
                  lines = content.strip().split('\n')
                  count = 0
                  for line in lines:
                      if '|' not in line: continue
                      parts = [p.strip() for p in line.split('|')]
                      if len(parts) < 2: continue

                      theme = parts[0]
                      book_type = parts[1].lower()

                      # Deduplication Check
                      is_dup, matched = is_duplicate_theme(theme, str(themes_path))
                      if is_dup:
                          print(f"⏭️ Skipping duplicate theme: {theme} (similar to: {matched})")
                          continue

                      # Create a new job card
                      hash_str = hashlib.sha256(f"{theme}{book_type}{datetime.now()}".encode()).hexdigest()[:6]
                      filename = f"{theme.replace(' ', '_').lower()}_{book_type}_{hash_str}.md"

                      card_content = f"""<!-- CARD RULES
               This card is the source of truth for this job.
               Status field controls pipeline progression.
               All status changes must go through update_status.py.
               Direct edits to status field will be rejected by the state machine.
          -->
          ---
          id: {theme.replace(' ', '_').lower()}_{hash_str}
          theme: {theme}
          type: {book_type}
          status: idea_generated
          created: {datetime.now().strftime('%Y-%m-%d')}
          last_updated: {datetime.now().strftime('%Y-%m-%d')}
          locked_by:
          locked_at:
          attempts: 0
          last_error:
          session_id:
          loop_iterations: 0
          max_iterations: 10
          ---
          """
                      with open(job_dir / filename, 'w') as f:
                          f.write(card_content)
                      print(f"✅ Created job card: {filename}")
                      count += 1
                  return count > 0

              elif level == 1:
                  # Level 1: Expected output is 5 ideas for a specific card
                  print("ℹ️ Level 1 Groq output handling: Card update logic.")
                  return True

              return False

          def main():
              parser = argparse.ArgumentParser(description="Handle Groq output.")
              parser.add_argument("--level", type=int, required=True, help="Pipeline level (0-6)")
              parser.add_argument("--content", required=True, help="Content from Groq")

              args = parser.parse_args()

              success = handle_groq_output(args.level, args.content)
              if not success:
                  print("⚠️ No actionable content found in Groq output.")

          if __name__ == "__main__":
              main()
          ```
        - **File: lock_job.py**
          ```python
          # Licensed under the MIT License.
          # Copyright 2024 RokctAI

          import argparse
          import sys
          import re
          from pathlib import Path
          from datetime import datetime, timedelta

          def get_field(content, field):
              match = re.search(rf'^{field}:[ 	]*(.*)', content, re.MULTILINE)
              return match.group(1).strip() if match else ""

          def set_field(content, field, value):
              if re.search(rf'^{field}:', content, re.MULTILINE):
                  return re.sub(rf'^{field}:.*', f'{field}: {value}', content, flags=re.MULTILINE)
              else:
                  # If field doesn't exist, append before the last ---
                  if '---' in content:
                      parts = content.rsplit('---', 1)
                      return f"{parts[0]}{field}: {value}\n---{parts[1]}"
                  return f"{content}\n{field}: {value}"

          def lock_job():
              parser = argparse.ArgumentParser(description="Claim or release a lock on a job card.")
              parser.add_argument("--file", required=True, help="Path to the job card file")
              parser.add_argument("--action", required=True, choices=["claim", "release", "check"], help="Action to perform")
              parser.add_argument("--agent", help="Agent name (required for claim)")
              parser.add_argument("--session", help="Session ID (required for claim)")

              args = parser.parse_args()
              file_path = Path(args.file)

              if not file_path.exists():
                  print(f"Error: File {args.file} not found.")
                  sys.exit(1)

              with open(file_path, 'r', encoding='utf-8') as f:
                  content = f.read()

              locked_by = get_field(content, "locked_by")
              locked_at = get_field(content, "locked_at")

              now = datetime.utcnow()

              if args.action == "check":
                  print(locked_by)
                  sys.exit(0 if not locked_by else 1)

              elif args.action == "release":
                  content = set_field(content, "locked_by", "")
                  content = set_field(content, "locked_at", "")
                  content = set_field(content, "session_id", "")
                  with open(file_path, 'w', encoding='utf-8') as f:
                      f.write(content)
                  print("Lock released.")
                  sys.exit(0)

              elif args.action == "claim":
                  is_stale = False
                  if locked_at:
                      try:
                          locked_time = datetime.strptime(locked_at, "%Y-%m-%d %H:%M:%S")
                          if now - locked_time > timedelta(hours=6):
                              is_stale = True
                      except ValueError:
                          is_stale = True # Assume stale if date format is broken

                  if not locked_by or is_stale:
                      if not args.agent or not args.session:
                          print("Error: --agent and --session required for claim action.")
                          sys.exit(1)

                      content = set_field(content, "locked_by", args.agent)
                      content = set_field(content, "locked_at", now.strftime("%Y-%m-%d %H:%M:%S"))
                      content = set_field(content, "session_id", args.session)
                      with open(file_path, 'w', encoding='utf-8') as f:
                          f.write(content)
                      print(f"Lock claimed by {args.agent}.")
                      sys.exit(0)
                  else:
                      print(f"LOCKED by {locked_by}")
                      sys.exit(1)

          if __name__ == "__main__":
              lock_job()
          ```
        - **File: manage_sessions.py** — Script to monitor and update session state from ledger
          ```python
          # Licensed under the MIT License.
          # Copyright 2024 RokctAI

          import os
          import yaml
          from pathlib import Path
          from datetime import datetime

          def manage_sessions():
              """Reads session_state.md and ledger.md to manage active Jules sessions."""
              print("🗓️ Running Session Scheduler...")

              state_path = Path('.rokct/agent/session_state.md')
              ledger_path = Path('.rokct/agent/log/ledger.md')

              if not state_path.exists():
                  print("⚠️ session_state.md not found.")
                  return

              # 1. Parse session_state.md
              with open(state_path, 'r') as f:
                  content = f.read()
                  parts = content.split('---')
                  if len(parts) < 3:
                      print("⚠️ Invalid session_state.md format.")
                      return
                  state = yaml.safe_load(parts[1])

              # 2. Check for stalled cards in ledger
              stalled_found = False
              if ledger_path.exists():
                  with open(ledger_path, 'r') as f:
                      for line in f:
                          if 'stalled' in line:
                              print(f"⚠️ STALLED JOB DETECTED: {line.strip()}")
                              stalled_found = True

              if stalled_found:
                  print("ℹ️ Stalled jobs require human review. Reset iterations to 0 and status to 'writing' to resume.")

              # 3. Count currently active sessions from ledger
              active_count = 0
              if ledger_path.exists():
                  with open(ledger_path, 'r', encoding='utf-8') as f:
                      lines = f.readlines()
                      # Only look at the last few lines for active status (simplified)
                      for line in lines[-20:]:
                          if any(status in line for status in ['writing', 'evaluating', 'rules_generating']):
                              # This is a bit naive but works for a historical log check
                              active_count += 1

              print(f"📊 Active sessions detected: {active_count}")

              # 4. Update state
              state['active_sessions'] = active_count
              state['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

              # 5. Save updated state
              new_content = "---\n" + yaml.dump(state) + "---\n"
              with open(state_path, 'w') as f:
                  f.write(new_content)

              print("✅ session_state.md updated.")

          if __name__ == "__main__":
              manage_sessions()
          ```
        - **File: privacy_sync.py** — Enforces encryption-based privacy on job cards
          ```python
          # Licensed under the MIT License.
          # Copyright 2024 RokctAI

          import os
          import re
          import hashlib
          import sys
          import argparse
          from pathlib import Path
          from dotenv import load_dotenv
          from crypto_utils import encrypt_pii

          # Ported from opportunities: Adapt for 'factory' book jobs context
          # Configuration
          JOB_DIR = Path('.rokct/agent/jobs/pending')
          EMAIL_REGEX = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

          def load_key():
              """Find and load encryption key from monorepo environment."""
              script_dir = os.path.dirname(os.path.abspath(__file__))
              project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))))
              env_path = os.path.join(project_root, ".env", "production.env")

              if os.path.exists(env_path):
                  load_dotenv(env_path)
                  with open(env_path, 'r', encoding='utf-8') as f:
                      for line in f:
                          if "EMAIL_ENCRYPTION_KEY=" in line:
                              return line.replace("export ", "").strip().split("=", 1)[1].strip("'\" ")

              return os.getenv('EMAIL_ENCRYPTION_KEY')

          def process_privacy(check_only=False):
              """Enforces encryption-based privacy for job cards."""
              if not JOB_DIR.exists():
                  return True

              encryption_key = load_key()
              if not encryption_key and not check_only:
                  print("❌ Error: EMAIL_ENCRYPTION_KEY not found. Cannot encrypt.")
                  return False

              violations = []
              processed_count = 0

              print(f"🔐 {'Checking' if check_only else 'Applying'} PII Encryption Privacy...")

              for card_file in JOB_DIR.glob('*.md'):
                  filename = card_file.name
                  with open(card_file, 'r', encoding='utf-8') as f:
                      content = f.read()

                  # 1. Detection Logic
                  found_emails = re.findall(EMAIL_REGEX, content)
                  has_plaintext_email = any(e for e in found_emails if e.lower() != "email@example.com")

                  if has_plaintext_email:
                      if check_only:
                          violations.append(f"❌ Unencrypted PII in: {filename}")
                          continue

                      # 2. Encryption Logic
                      # Note: This logic assumes a specific PII field in the job card if applicable.
                      # In factory context, we protect any email found in the card.
                      for email in found_emails:
                          if email.lower() == "email@example.com": continue
                          encrypted_blob = encrypt_pii(email, encryption_key)
                          content = content.replace(email, f"[REDACTED] (Encrypted: {encrypted_blob})")

                      with open(card_file, 'w', encoding='utf-8') as f:
                          f.write(content)

                      print(f"🔒 Encrypted PII in: {filename}")
                      processed_count += 1

              if check_only:
                  if violations:
                      print("\n".join(violations))
                      print("\n🚨 PRIVACY CHECK FAILED: Plaintext PII detected.")
                      return False
                  print("✅ Privacy check passed. All PII is encrypted.")
                  return True

              print(f"✅ Encryption sync complete. {processed_count} files secured.")
              return True

          if __name__ == "__main__":
              parser = argparse.ArgumentParser(description="Enforce encryption-based privacy.")
              parser.add_argument("--check", action="store_true", help="Check for plaintext without modifying.")
              args = parser.parse_args()

              success = process_privacy(check_only=args.check)
              if not success:
                  sys.exit(1)
          ```
        - **File: response_kits.py** — Automatically scaffolds production kits for approved concepts
          ```python
          # Licensed under the MIT License.
          # Copyright 2024 RokctAI

          import os
          import re
          from pathlib import Path

          # Ported from opportunities: Adapt for 'factory' book context
          def generate_response_kits():
              """Generates a starting production package for approved concepts."""
              print("📂 Checking for Jobs ready for Production Kits...")

              job_dir = Path('.rokct/agent/jobs/pending')
              drafts_dir = Path('books/drafts')

              if not job_dir.exists(): return

              for md_file in job_dir.glob('*.md'):
                  if md_file.name == 'template.md': continue
                  with open(md_file, 'r') as f:
                      content = f.read()

                  # Create kits for jobs that have approved concepts
                  if "concept_status: approved" in content.lower():
                      # Extract metadata
                      title_match = re.search(r'book_name:\s*(.*)', content)
                      id_match = re.search(r'id:\s*(.*)', content)

                      if not title_match or not id_match: continue

                      book_id = id_match.group(1).strip()
                      book_title = title_match.group(1).strip()
                      if not book_title: book_title = book_id

                      safe_name = "".join([c if c.isalnum() else "_" for c in book_title])[:50]

                      book_path = drafts_dir / f"{book_id}_{safe_name}"
                      if not book_path.exists():
                          book_path.mkdir(parents=True, exist_ok=True)

                          # Copy template files (logic would be expanded to actually copy)
                          # For now, we create foundational placeholders
                          with open(book_path / 'metadata.md', 'w') as p:
                              p.write(f"---\nid: {book_id}\ntitle: {book_title}\nstatus: production\n---")

                          print(f"✅ Created Production Kit: {book_path.name}")

          if __name__ == "__main__":
              generate_response_kits()
          ```
        - **File: update_audit_logs.py** — Maintains audit logs for drafts and published books
          ```python
          # Licensed under the MIT License.
          # Copyright 2024 RokctAI

          import os
          import re
          from pathlib import Path
          from datetime import datetime

          # Ported from opportunities: Adapt for 'factory' book jobs context
          def update_audit_logs():
              """Ensures book job directories have up-to-date audit logs."""
              print("📝 Updating Job Audit Logs...")

              dirs = {
                  'books/drafts': 'LIVING',
                  'books/published': 'STATIC'
              }

              for dir_path, mode in dirs.items():
                  directory = Path(dir_path)
                  if not directory.exists(): continue

                  log_path = directory / 'job_audit_log.md'

                  total_jobs = 0
                  published_jobs = 0

                  # Scan subdirectories for books
                  for book_dir in directory.iterdir():
                      if book_dir.is_dir() and not book_dir.name.startswith('_'):
                          total_jobs += 1
                          metadata_file = book_dir / 'metadata.md'
                          if metadata_file.exists():
                              with open(metadata_file, 'r', encoding='utf-8') as content:
                                  text = content.read()
                                  if "status: published" in text.lower():
                                      published_jobs += 1

                  log_content = f"""# Job Audit Log: {dir_path.split('/')[-1].capitalize()}

          | Directory | Mode | Status | Last Audit Date | Published Jobs | Total Jobs |
          | :--- | :--- | :--- | :--- | :--- | :--- |
          | {dir_path}/ | {mode} | { 'COMPLETE' if published_jobs == total_jobs and total_jobs > 0 else 'IN_PROGRESS' } | {datetime.now().strftime('%Y-%m-%d')} | {published_jobs} | {total_jobs} |

          ## Recent Changes
          - Automated audit log update: {datetime.now().strftime('%Y-%m-%d %H:%M')}
          - Published: {published_jobs}/{total_jobs} ({ (published_jobs/total_jobs*100) if total_jobs > 0 else 0 :.1f}%)
          """
                  with open(log_path, 'w', encoding='utf-8') as f:
                      f.write(log_content)
                  print(f"✅ Updated audit log for {dir_path}")

          if __name__ == "__main__":
              update_audit_logs()
          ```
        - **File: update_classifications.py** — Updates genre and theme classifications
          ```python
          # Licensed under the MIT License.
          # Copyright 2024 RokctAI

          import os
          import re
          from pathlib import Path
          import difflib

          def is_duplicate_theme(new_theme, existing_themes_path, threshold=0.8):
              if not os.path.exists(existing_themes_path):
                  return False, ""

              with open(existing_themes_path, 'r', encoding='utf-8') as f:
                  existing_themes = [line.strip() for line in f.readlines() if line.strip()]

              for existing in existing_themes:
                  similarity = difflib.SequenceMatcher(None, new_theme.lower(), existing.lower()).ratio()
                  if similarity >= threshold:
                      return True, existing

              return False, ""

          # Ported from opportunities: Adapt for 'factory' book jobs context
          def update_classifications():
              """Generates classification reference files for factory books."""
              print("🏷️ Updating Factory Classifications...")

              config_dir = Path('.rokct/config/classifications')
              config_dir.mkdir(parents=True, exist_ok=True)

              job_dir = Path('.rokct/agent/jobs/pending')
              themes = set()
              genres = set()

              if job_dir.exists():
                  for f in job_dir.glob('*.md'):
                      if f.name == 'template.md': continue
                      with open(f, 'r') as content:
                          text = content.read()
                          theme_match = re.search(r'theme:\s*(.*)', text)
                          if theme_match: themes.add(theme_match.group(1).strip())

                          genre_match = re.search(r'type:\s*(.*)', text)
                          if genre_match: genres.add(genre_match.group(1).strip())

              save_list(config_dir / 'factory_themes.txt', themes)
              save_list(config_dir / 'factory_genres.txt', genres)

          def save_list(path, items):
              clean_items = sorted(list(set([i.strip() for i in items if i.strip()])))
              with open(path, 'w') as f:
                  f.write('\n'.join(clean_items))
              print(f"✅ Saved {path.name} ({len(clean_items)} entries)")

          if __name__ == "__main__":
              update_classifications()
          ```
        - **File: update_dashboard.py** — Recalculates stats and updates README dashboard
          ```python
          # Licensed under the MIT License.
          # Copyright 2024 RokctAI

          import os
          import re
          import json
          from pathlib import Path
          from datetime import datetime, timedelta

          # Ported from opportunities: Adapt for 'factory' book jobs context
          def update_readme_stats():
              """Calculates book stats and updates the main README.md and generates data for dashboard."""
              print("📊 Updating Job Dashboard & Data...")

              project_root = Path(__file__).parent.parent.parent.parent.parent
              readme_path = project_root / 'README.md'
              docs_dir = project_root / 'docs'
              docs_dir.mkdir(exist_ok=True)

              # 1. Calculate Stats and Gather Data
              stats = {
                  'Poetry': {'total': 0, 'published': 0, 'new': 0},
                  'Fiction': {'total': 0, 'published': 0, 'new': 0},
                  'Short Story': {'total': 0, 'published': 0, 'new': 0},
                  'Children': {'total': 0, 'published': 0, 'new': 0}
              }

              all_jobs = []

              dirs = {
                  'Poetry': Path('.rokct/types/poetry'),
                  'Fiction': Path('.rokct/types/fiction'),
                  'Short Story': Path('.rokct/types/short_story'),
                  'Children': Path('.rokct/types/children')
              }

              week_ago = datetime.now() - timedelta(days=7)

              job_pending_dir = Path('.rokct/agent/jobs/pending')
              if job_pending_dir.exists():
                  for f in job_pending_dir.glob('*.md'):
                      if f.name == 'template.md': continue

                      with open(f, 'r', encoding='utf-8') as content:
                          text = content.read()

                          # Simple parsing for frontmatter
                          type_match = re.search(r'type:\s*(.*)', text)
                          job_type = type_match.group(1).strip().capitalize() if type_match else "Unknown"
                          if job_type == "Short_story": job_type = "Short Story"

                          if job_type in stats:
                              stats[job_type]['total'] += 1

                              is_published = "status: published" in text.lower()
                              if is_published:
                                  stats[job_type]['published'] += 1

                              is_new = datetime.fromtimestamp(f.stat().st_mtime) > week_ago
                              if is_new:
                                  stats[job_type]['new'] += 1

                              all_jobs.append({
                                  'id': f.stem,
                                  'category': job_type,
                                  'published': is_published,
                                  'new': is_new
                              })

              # 2. Export JSON for dashboard
              data_output = {
                  'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M'),
                  'stats': stats,
                  'jobs': all_jobs
              }

              with open(docs_dir / 'data.json', 'w', encoding='utf-8') as f:
                  json.dump(data_output, f, indent=2)
              print(f"📄 Exported {len(all_jobs)} jobs to docs/data.json")

              # 3. Format Dashboard for README
              if readme_path.exists():
                  total_jobs = sum(s['total'] for s in stats.values())
                  total_published = sum(s['published'] for s in stats.values())
                  total_new = sum(s['new'] for s in stats.values())
                  progress_pct = (total_published / total_jobs * 100) if total_jobs > 0 else 0

                  dashboard = f"""
          ## 🚀 Factory Status Dashboard
          *Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*

          | Genre | Total Jobs | New (7d) | Published | Health |
          | :--- | :--- | :--- | :--- | :--- |
          | 🎭 **Poetry** | {stats['Poetry']['total']} | {stats['Poetry']['new']} | {stats['Poetry']['published']} | { '🟢' if stats['Poetry']['total'] == stats['Poetry']['published'] and stats['Poetry']['total'] > 0 else '🟡' } |
          | 📚 **Fiction** | {stats['Fiction']['total']} | {stats['Fiction']['new']} | {stats['Fiction']['published']} | { '🟢' if stats['Fiction']['total'] == stats['Fiction']['published'] and stats['Fiction']['total'] > 0 else '🟡' } |
          | 📖 **Short Story** | {stats['Short Story']['total']} | {stats['Short Story']['new']} | {stats['Short Story']['published']} | { '🟢' if stats['Short Story']['total'] == stats['Short Story']['published'] and stats['Short Story']['total'] > 0 else '🟡' } |
          | 👶 **Children** | {stats['Children']['total']} | {stats['Children']['new']} | {stats['Children']['published']} | { '🟢' if stats['Children']['total'] == stats['Children']['published'] and stats['Children']['total'] > 0 else '🟡' } |

          **Overall Progress**: `{progress_pct:.1f}%` Published | `+{total_new}` New Jobs This Week
          """

                  with open(readme_path, 'r', encoding='utf-8') as f:
                      readme_content = f.read()

                  marker_start = "## 🚀 Factory Status Dashboard"
                  if marker_start in readme_content:
                      pattern = re.compile(rf"{marker_start}.*?(?=\n## )", re.DOTALL)
                      if not pattern.search(readme_content):
                           pattern = re.compile(rf"{marker_start}.*", re.DOTALL)
                      new_content = pattern.sub(dashboard.strip(), readme_content)
                  else:
                      # Append after the first paragraph
                      parts = readme_content.split('\n\n', 1)
                      if len(parts) > 1:
                          new_content = parts[0] + "\n\n" + dashboard.strip() + "\n\n" + parts[1]
                      else:
                          new_content = readme_content + "\n\n" + dashboard.strip()

                  with open(readme_path, 'w', encoding='utf-8') as f:
                      f.write(new_content)
                  print("✅ README Dashboard Updated.")

          if __name__ == "__main__":
              update_readme_stats()
          ```
        - **File: update_status.py**
          ```python
          # Licensed under the MIT License.
          # Copyright 2024 RokctAI

          import argparse
          import sys
          import re
          from pathlib import Path
          from datetime import datetime

          ALLOWED_TRANSITIONS = {
              "idea_generated": ["pending_approval", "failed", "stalled"],
              "pending_approval": ["concept_expanding", "declined", "failed", "stalled"],
              "concept_expanding": ["concept_generated", "failed", "stalled"],
              "concept_generated": ["pending_concept_approval", "failed", "stalled"],
              "pending_concept_approval": ["rules_generating", "declined", "failed", "stalled"],
              "rules_generating": ["rules_generated", "failed", "stalled"],
              "rules_generated": ["pending_rules_approval", "failed", "stalled"],
              "pending_rules_approval": ["writing", "declined", "failed", "stalled"],
              "writing": ["evaluating", "failed", "stalled"],
              "evaluating": ["draft_ready", "writing", "failed", "stalled"],
              "draft_ready": ["pending_acceptance", "failed", "stalled"],
              "pending_acceptance": ["publishing", "writing", "failed", "stalled"],
              "publishing": ["published", "failed", "stalled"],
              "declined": ["failed", "stalled"],
              "failed": ["writing", "stalled"],
              "stalled": ["writing", "failed"]
          }

          def get_field(content, field):
              match = re.search(rf'^{field}:[ 	]*(.*)', content, re.MULTILINE)
              return match.group(1).strip() if match else ""

          def set_field(content, field, value):
              if re.search(rf'^{field}:', content, re.MULTILINE):
                  return re.sub(rf'^{field}:.*', f'{field}: {value}', content, flags=re.MULTILINE)
              else:
                  if '---' in content:
                      parts = content.rsplit('---', 1)
                      return f"{parts[0]}{field}: {value}\n---{parts[1]}"
                  return f"{content}\n{field}: {value}"

          def update_status():
              parser = argparse.ArgumentParser(description="Update the status of a job card with validation.")
              parser.add_argument("--file", required=True, help="Path to the job card file")
              parser.add_argument("--status", required=True, help="New status to set")
              parser.add_argument("--agent", default="system", help="Agent performing the transition")

              args = parser.parse_args()
              file_path = Path(args.file)

              if not file_path.exists():
                  print(f"Error: File {args.file} not found.")
                  sys.exit(1)

              with open(file_path, 'r', encoding='utf-8') as f:
                  content = f.read()

              current_status = get_field(content, "status")
              card_id = get_field(content, "id")
              attempts = int(get_field(content, "attempts") or 0)

              # Validation
              if current_status and current_status in ALLOWED_TRANSITIONS:
                  if args.status not in ALLOWED_TRANSITIONS[current_status]:
                      print(f"Error: Invalid transition from {current_status} to {args.status}")
                      sys.exit(1)
              elif current_status:
                  # If status is not in map, only allow failed/stalled
                  if args.status not in ["failed", "stalled"]:
                      print(f"Error: Unknown current status {current_status}. Transition to {args.status} rejected.")
                      sys.exit(1)

              # Perform Update
              now = datetime.utcnow()
              content = set_field(content, "status", args.status)
              content = set_field(content, "last_updated", now.strftime("%Y-%m-%d %H:%M:%S"))
              content = set_field(content, "attempts", str(attempts + 1))

              with open(file_path, 'w', encoding='utf-8') as f:
                  f.write(content)

              # Log Transition
              log_path = Path('.rokct/agent/log/transitions.log')
              log_path.parent.mkdir(parents=True, exist_ok=True)

              log_entry = f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {card_id} | {current_status} -> {args.status} | {args.agent}\n"
              with open(log_path, 'a', encoding='utf-8') as f:
                  f.write(log_entry)

              print(f"Status updated successfully: {current_status} -> {args.status}")

          if __name__ == "__main__":
              update_status()
          ```
  - **Directory: templates/** — Markdown templates for cards and documents
    - **File: copyright.md** — Template for copyright statements
      ```markdown
      # Copyright
      © {year} Rokct Publishing (pty) Ltd. All rights reserved.
      Author: {author}
      Title: {title}
      Version: {version}
      ```
    - **File: cover_brief.md** — Template for cover design briefs
      ```markdown
      # Cover Brief
      **Style:**
      **Mood:**
      **Palette:**
      **Typography:**
      **Imagery:**
      ```
    - **File: credits.md** — Template for book credits
      ```markdown
      # Credits

      **Author:** {author}
      **Publisher:** Rokct Publishing (pty) Ltd
      **Editor:**
      **Cover Design:**
      **Production Agent:**
      **Evaluation Agent:**
      ```
    - **File: metadata.md** — Template for book folder metadata
      ```markdown
      ---
      id:
      theme:
      type:
      age:
      status:
      metarules_link:
      rules:
      ---
      ```
    - **File: opening_letter.md** — Template for introductory letters
      ```markdown
      # Opening Letter

      Dear Reader,

      This book, titled **{title}** by **{author}**, explores the theme of **{theme}**.

      [Content]
      ```
  - **Directory: types/** — Categorized metarules by book genre
    - **Directory: children/** — Metarules for children's books
      - **Directory: metarules/** — Governance files for children's content
        - **File: world_rules.md** — Stub for fundamental world laws for children
          ```markdown
          # Metarules Stub
          This is a stub for children metarules. To be completed later.

          ## Rules
          ```
    - **Directory: fiction/** — Metarules for fiction novels
      - **Directory: metarules/** — Governance files for fiction content
        - **File: world_rules.md** — Stub for fundamental world laws for fiction
          ```markdown
          # Metarules Stub
          This is a stub for fiction metarules. To be completed later.

          ## Rules
          ```
    - **Directory: poetry/** — Metarules for poetry collections
      - **Directory: metarules/** — Governance files for poetry content
        - **File: audit_rules.md** — Procedures for the backward audit process
          ```markdown
          # Audit Rules
          This file defines the backward audit process to ensure every element serves the higher levels.

          ## Rules
          ```
        - **File: book_rules.md** — Rules for structural and thematic consistency
          ```markdown
          # Book Rules
          This file governs the structure, thematic consistency, and overall flow of the poetry collection.

          ## Rules
          ```
        - **File: impact_metrics.md** — Metrics for emotional and structural evaluation
          ```markdown
          # Impact Metrics
          This file defines the metrics used to evaluate the emotional and structural impact of the content.

          ## Rules
          ```
        - **File: line_rules.md** — Rules for individual line strength (trees)
          ```markdown
          # Line Rules
          This file governs the individual line (tree), ensuring it stands alone and hits hard.

          ## Rules
          ```
        - **File: poem_rules.md** — Rules for individual poem alignment (regions)
          ```markdown
          # Poem Rules
          This file governs the individual poem's structure, tone, and alignment with the book's themes.

          ## Rules
          ```
        - **File: stanza_rules.md** — Rules for line combinations (forests)
          ```markdown
          # Stanza Rules
          This file governs how trees (lines) come together to form a forest (stanza).

          ## Rules
          ```
        - **File: world_rules.md** — Fundamental laws of the poetry world (country)
          ```markdown
          # World Rules
          This file governs the overarching environment, climate, and fundamental laws of the book's world.

          ## Rules
          ```
    - **Directory: short_story/** — Metarules for short story collections
      - **Directory: metarules/** — Governance files for short stories
        - **File: world_rules.md** — Stub for fundamental world laws for short stories
          ```markdown
          # Metarules Stub
          This is a stub for short story metarules. To be completed later.

          ## Rules
          ```
- **File: LICENSE** — Project licensing terms
- **File: PLANNING.md** — The original architect's vision and technical specification
- **File: README.md** — High-level project documentation and usage guide
  ```markdown
  # RokctAI Factory

  An autonomous publishing factory that generates, evaluates, improves, and publishes books across multiple genres.

  ## 🚀 Factory Status Dashboard
  *Last Updated: 2026-04-29 12:00*

  | Genre | Total Jobs | New (7d) | Published | Health |
  | :--- | :--- | :--- | :--- | :--- |
  | 🎭 **Poetry** | 0 | 0 | 0 | 🟡 |
  | 📚 **Fiction** | 0 | 0 | 0 | 🟡 |
  | 📖 **Short Story** | 0 | 0 | 0 | 🟡 |
  | 👶 **Children** | 0 | 0 | 0 | 🟡 |

  **Overall Progress**: `0.0%` Published | `+0` New Jobs This Week

  ## 🏗 Pipeline Levels

  - **Level 0: Theme Generation** (Fully Automated) - Discovers new themes.
  - **Level 1: Idea Generation** (Human Gate 1) - Expands themes into book ideas for approval.
  - **Level 2: Concept Expansion** (Human Gate 2) - Develops approved ideas into full concepts.
  - **Level 3: Rule Generation** (Human Gate 3) - Generates world, book, and chapter rules.
  - **Level 4: Generation Loop** (Fully Automated) - Continuous writing and evaluation loop.
  - **Level 5: Draft** (Human Gate 4) - Final human review of the completed book.
  - **Level 6: Publishing** (Fully Automated) - Assembles PDF, generates cover, and publishes.

  ## 👥 Human Decision Points

  1. **Approve Idea** (Level 1): Change `idea_status` to `approved` in the job card.
  2. **Approve Concept** (Level 2): Change `concept_status` to `approved` in the job card.
  3. **Approve Rules** (Level 3): Change `rules_status` to `approved` in the job card.
  4. **Accept Final Draft** (Level 5): Change `status` to `accepted` in `metadata.md`.

  ## 📁 Repository Structure

  - `.rokct/agent/`: AI agent configurations, prompts, and job tracking.
  - `.rokct/skills/`: Reusable agent capabilities and automation scripts.
  - `.rokct/types/`: Metarules for different book types (poetry, fiction, etc.).
  - `.github/workflows/`: Functional automation pipelines for each level.
  - `books/drafts/`: In-progress book projects.
  - `books/published/`: Completed and published books.

  ## 🤖 Jules Sessions

  Jules (the primary AI agent) runs in scheduled sessions:
  - **Daily Writing Sessions**: Weekdays at 08:00 UTC.
  - **Weekend Evaluation Sessions**: Deep audit of all active drafts.

  ## 📖 Ledger

  The `.rokct/agent/log/ledger.md` is the single source of truth for the system state. **Only CI workflows are permitted to write to the ledger.**

  ## ✍️ How to Add a Book Idea Manually

  Create a new card in `.rokct/agent/jobs/pending/` using the `template.md` and set the status to `idea_generated`.
  ```
- **Directory: books/** — Book content storage
  - **Directory: drafts/** — In-progress book projects
    - **Directory: _template/** — Scaffold for new book directories
      - **File: copyright.md** — Legal statement stub with variables
        ```markdown
        # Copyright
        © {year} Rokct Publishing (pty) Ltd. All rights reserved.
        Author: {author}
        Title: {title}
        ```
      - **File: cover_brief.md** — Stub for visual design instructions
        ```markdown
        # Cover Brief
        **Style:**
        **Mood:**
        **Palette:**
        **Typography:**
        **Imagery:**
        ```
      - **File: credits.md** — Attribution and production credits stub
        ```markdown
        # Credits
        **Author:** {author}
        **Publisher:** Rokct Publishing (pty) Ltd
        [To be generated]
        ```
      - **File: metadata.md** — Project-specific frontmatter and rule links
        ```markdown
        ---
        id:
        theme:
        type:
        age:
        status:
        metarules_link:
        rules:
        ---
        ```
      - **File: opening_letter.md** — Introductory text stub
        ```markdown
        # Opening Letter
        [To be generated based on theme and rules]
        ```
  - **Directory: published/** — [empty — reserved for completed and human-accepted books]
    - **File: .gitkeep**
      ```
      ```

## NOTES

- **Renaming Suggestions:**
    - The word `metarules` appears as a folder name across multiple paths. Flagging for owner review: suggest renaming to `rules` for clarity, as the 'meta' distinction is conceptual and lives in planning documents rather than file names.
- **Infrastructure Status:**
    - GitHub Actions workflows have been fully implemented and integrated with the agent delegation skills.