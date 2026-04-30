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
