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
