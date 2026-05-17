# Licensed under the MIT License.
# Copyright 2024 RokctAI

import os
import requests
import json
import argparse
import sys

def parse_env_content(content):
    """Parses shell-style exports and returns True if a key was successfully found and set."""
    found = False
    for line in content.splitlines():
        if "JULES_API_KEY=" in line or "AGENT_API_KEY=" in line:
            # Strip 'export ', whitespace, and quotes
            val = line.replace("export ", "").strip().split("=", 1)[1].strip("'\" ")
            key_name = "JULES_API_KEY" if "JULES_API_KEY" in line else "AGENT_API_KEY"
            os.environ[key_name] = val
            found = True
            if os.environ.get("GITHUB_ACTIONS"):
                print(f"✅ [CI Debug] Successfully set {key_name} from content.")
    return found

def load_monorepo_env():
    """Prioritizes the Remote Vault if MONOREPO_PAT is present."""
    pat = os.environ.get("MONOREPO_PAT")
    if not pat:
        return False

    url = "https://raw.githubusercontent.com/RokctAI/monorepo/main/.env/production.env"
    if os.environ.get("GITHUB_ACTIONS"):
        print(f"🔍 [CI Debug] MONOREPO_PAT detected. Dialing home to: {url}")

    try:
        headers = {"Authorization": f"token {pat}"}
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return parse_env_content(response.text)
    except Exception as e:
        if os.environ.get("GITHUB_ACTIONS"):
            print(f"⚠️ [CI Debug] Remote Vault resolution failed: {e}")
        return False

def load_local_env():
    """Fallback to local environment files."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    monorepo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))))
    env_path = os.path.join(monorepo_root, ".env", "production.env")

    # Debug prints for CI logs
    if os.environ.get("GITHUB_ACTIONS"):
        print(f"🔍 [CI Debug] Looking for local env at: {env_path}")

    try:
        if os.path.exists(env_path):
            with open(env_path, 'r', encoding='utf-8') as f:
                return parse_env_content(f.read())

        # Try default .env if production.env doesn't exist
        try:
            from dotenv import load_dotenv
            load_dotenv()
            return os.environ.get("JULES_API_KEY") or os.environ.get("AGENT_API_KEY")
        except ImportError:
            return False
    except Exception as e:
        if os.environ.get("GITHUB_ACTIONS"):
            print(f"⚠️ [CI Debug] Local env resolution failed: {e}")
        return False

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
    # Priority: Remote Vault > Local Env > Local File
    if os.environ.get("MONOREPO_PAT"):
        load_monorepo_env()

    if not os.environ.get("JULES_API_KEY") and not os.environ.get("AGENT_API_KEY"):
        load_local_env()

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
