#!/usr/bin/env python3
# Copyright (c) 2026 RokctAI
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Fetch-and-record step for the US curriculum tree.

Stdlib only. Polite by construction: honest User-Agent with a contact route,
robots.txt respected, 2 second spacing, exponential backoff. It does NOT spoof
a browser - if a rights holder's front end refuses this client, the answer is a
manual browser session and `register`, not evasion.

The important behaviour is the refusal. Every subcommand reads
../RIGHTS.json first, and any framework whose gate is
`blocked_pending_written_permission` is refused outright - the script will not
fetch College Board material even if asked directly. Clearing that gate is an
edit to RIGHTS.json by the owner, backed by a recorded permission, not a flag
on this script. There is deliberately no --force.

Subcommands:
    probe                 read robots.txt + terms pages for every framework and
                          report what they actually say (the check SOURCES.md
                          is currently missing)
    fetch <framework>     download the recorded primary sources
    register <framework> <file> --url <url>
                          record a browser-downloaded file with real URL +
                          sha256 provenance
    verify [framework]    re-hash the manifest; --refetch to detect upstream
                          edition changes

Usage:
    python3 lessons/scripts/US/fetch_us_sources.py probe
    python3 lessons/scripts/US/fetch_us_sources.py fetch COMMON_CORE
    python3 lessons/scripts/US/fetch_us_sources.py verify NGSS
"""

import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
US_ROOT = os.path.join(REPO_ROOT, "lessons", "curriculum", "US")

CONTACT = "curriculum-bot (RokctAI factory; contact: repository owner)"
USER_AGENT = "RokctAI-curriculum-bot/1.0 (+educational curriculum indexing; {})".format(CONTACT)
SPACING_SECONDS = 2.0
MAX_RETRIES = 4

BLOCKED_GATE = "blocked_pending_written_permission"


def load_rights():
    with open(os.path.join(US_ROOT, "RIGHTS.json"), encoding="utf-8") as fh:
        return json.load(fh)


def gate_check(rights, framework):
    """Refuse outright if the framework's gate is closed. No override."""
    block = rights["frameworks"].get(framework)
    if block is None:
        sys.exit("unknown framework: {}".format(framework))
    if block.get("gate") == BLOCKED_GATE:
        print("REFUSED: {} is gated '{}'.".format(framework, BLOCKED_GATE))
        print()
        print("  Rights holder : {}".format(block["rights_holder"]))
        print("  Why           : {}".format(block.get("commercial_reproduction_detail")
                                            or block.get("verdict")))
        if block.get("ai_use") == "expressly_prohibited":
            print("  AI clause     : {}".format(block.get("ai_use_detail", "expressly prohibited")))
        print("  Unblock via   : {}".format(
            block["primary_sources"].get("permission_request_form", "the rights holder")))
        print()
        print("This script has no --force. Record written permission in "
              "RIGHTS.json and change the gate there.")
        sys.exit(2)
    return block


def robots_allows(url):
    parsed = urllib.parse.urlparse(url)
    robots_url = "{}://{}/robots.txt".format(parsed.scheme, parsed.netloc)
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
    except Exception as exc:  # noqa: BLE001
        return None, "robots.txt unreadable ({})".format(exc)
    return rp.can_fetch(USER_AGENT, url), "robots.txt read"


def http_get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    delay = 2
    last = None
    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read(), resp.status, dict(resp.headers)
        except urllib.error.HTTPError as exc:
            # 4xx other than 429 is a decision, not a transient failure.
            if exc.code != 429 and 400 <= exc.code < 500:
                return None, exc.code, {}
            last = exc
        except Exception as exc:  # noqa: BLE001
            last = exc
        if attempt < MAX_RETRIES - 1:
            time.sleep(delay)
            delay *= 2
    return None, None, {"error": str(last)}


def manifest_path(framework):
    return os.path.join(US_ROOT, framework, "sources_manifest.json")


def load_manifest(framework):
    p = manifest_path(framework)
    if os.path.exists(p):
        with open(p, encoding="utf-8") as fh:
            return json.load(fh)
    return {"framework": framework, "documents": []}


def save_manifest(framework, manifest):
    p = manifest_path(framework)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print("manifest: {}".format(os.path.relpath(p, US_ROOT)))


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def source_urls(block):
    """Every fetchable URL recorded for a framework."""
    out = []
    for key, value in block.get("primary_sources", {}).items():
        if isinstance(value, str) and value.startswith("http") and key != "mirror_note":
            out.append((key, value))
    return out


# ---------------------------------------------------------------------------

def cmd_probe(args, rights):
    print("Probing the recorded sources for every framework.")
    print("This is the first-hand terms check SOURCES.md currently lacks -")
    print("run it from a network-enabled machine and fold the results back in.")
    print()
    for framework in ("COMMON_CORE", "NGSS", "AP", "SAT"):
        block = rights["frameworks"][framework]
        gate = block.get("gate")
        print("=" * 70)
        print("{}  (gate: {})".format(framework, gate))
        print("=" * 70)
        if gate == BLOCKED_GATE:
            print("  Gate closed - probing terms pages only (reading a public")
            print("  terms page is not reproduction), no document fetches.")
        seen_hosts = set()
        for key, url in source_urls(block):
            host = urllib.parse.urlparse(url).netloc
            if host not in seen_hosts:
                allowed, note = robots_allows(url)
                print("  robots [{}]: {} ({})".format(
                    host, {True: "allows", False: "DISALLOWS", None: "unknown"}[allowed], note))
                seen_hosts.add(host)
                time.sleep(SPACING_SECONDS)
            if gate == BLOCKED_GATE and not any(
                    t in key for t in ("terms", "copyright", "permission")):
                continue
            body, status, _ = http_get(url)
            print("    {:<28} {:<6} {}".format(
                key, status if status is not None else "ERR", url))
            if body and status == 200:
                print("      {} bytes retrieved".format(len(body)))
            time.sleep(SPACING_SECONDS)
        print()
    print("Record what this reports in SOURCES.md and set")
    print("RIGHTS.json.verification_method to 'first_hand' with the date.")
    return 0


def cmd_fetch(args, rights):
    framework = args.framework
    block = gate_check(rights, framework)
    manifest = load_manifest(framework)
    dest_root = os.path.join(US_ROOT, framework, "source")
    os.makedirs(dest_root, exist_ok=True)

    fetched = 0
    for key, url in source_urls(block):
        if not url.lower().endswith(".pdf"):
            continue
        allowed, note = robots_allows(url)
        if allowed is False:
            print("SKIP {} - robots.txt disallows ({})".format(url, note))
            continue
        print("GET  {}".format(url))
        body, status, headers = http_get(url)
        if body is None or status != 200:
            print("     failed (status={}). If the front end blocks scripted "
                  "fetching, download in a browser and use `register`."
                  .format(status))
            time.sleep(SPACING_SECONDS)
            continue
        name = os.path.basename(urllib.parse.urlparse(url).path) or (key + ".pdf")
        dest = os.path.join(dest_root, name)
        with open(dest, "wb") as fh:
            fh.write(body)
        digest = sha256_bytes(body)
        manifest["documents"] = [d for d in manifest["documents"] if d.get("url") != url]
        manifest["documents"].append({
            "id": key,
            "url": url,
            "local_path": os.path.relpath(dest, US_ROOT),
            "sha256": digest,
            "bytes": len(body),
            "content_type": headers.get("Content-Type"),
            "fetched": time.strftime("%Y-%m-%d"),
            "method": "scripted_fetch",
        })
        print("     {} bytes, sha256={}".format(len(body), digest[:16]))
        fetched += 1
        time.sleep(SPACING_SECONDS)

    if fetched:
        manifest["attribution_notice"] = block["attribution_notice"]
        manifest["license"] = block.get("license_name")
        save_manifest(framework, manifest)
    print("fetched {} document(s). PDFs stay local - ../.gitignore blocks "
          "*.pdf; commit the manifest only.".format(fetched))
    return 0


def cmd_register(args, rights):
    framework = args.framework
    block = gate_check(rights, framework)
    path = args.file
    if not os.path.exists(path):
        sys.exit("no such file: {}".format(path))
    with open(path, "rb") as fh:
        body = fh.read()
    manifest = load_manifest(framework)
    manifest["documents"] = [d for d in manifest["documents"] if d.get("url") != args.url]
    manifest["documents"].append({
        "id": args.id or os.path.splitext(os.path.basename(path))[0],
        "url": args.url,
        "local_path": os.path.relpath(os.path.abspath(path), US_ROOT),
        "sha256": sha256_bytes(body),
        "bytes": len(body),
        "fetched": time.strftime("%Y-%m-%d"),
        "method": "browser_download_registered",
    })
    manifest["attribution_notice"] = block["attribution_notice"]
    manifest["license"] = block.get("license_name")
    save_manifest(framework, manifest)
    print("registered {} ({} bytes)".format(path, len(body)))
    return 0


def cmd_verify(args, rights):
    frameworks = [args.framework] if args.framework else ["COMMON_CORE", "NGSS", "AP", "SAT"]
    problems = 0
    for framework in frameworks:
        p = manifest_path(framework)
        if not os.path.exists(p):
            print("{}: no manifest (nothing fetched yet)".format(framework))
            continue
        manifest = load_manifest(framework)
        for doc in manifest.get("documents", []):
            local = os.path.join(US_ROOT, doc["local_path"])
            if not os.path.exists(local):
                print("{}: MISSING local file {}".format(framework, doc["local_path"]))
                problems += 1
                continue
            with open(local, "rb") as fh:
                digest = sha256_bytes(fh.read())
            state = "ok" if digest == doc["sha256"] else "HASH MISMATCH"
            if state != "ok":
                problems += 1
            print("{}: {} {}".format(framework, doc["id"], state))
            if args.refetch and doc.get("url"):
                body, status, _ = http_get(doc["url"])
                if body and status == 200:
                    upstream = sha256_bytes(body)
                    if upstream != doc["sha256"]:
                        print("    UPSTREAM CHANGED - a new edition was published; "
                              "re-ingest and re-curate.")
                        problems += 1
                time.sleep(SPACING_SECONDS)
    return 1 if problems else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("probe", help="read robots.txt + terms pages first-hand")

    f = sub.add_parser("fetch", help="download recorded primary sources")
    f.add_argument("framework")

    r = sub.add_parser("register", help="record a browser-downloaded file")
    r.add_argument("framework")
    r.add_argument("file")
    r.add_argument("--url", required=True, help="the real URL it came from")
    r.add_argument("--id")

    v = sub.add_parser("verify", help="re-hash the manifest")
    v.add_argument("framework", nargs="?")
    v.add_argument("--refetch", action="store_true",
                   help="also re-download to detect upstream edition changes")

    args = ap.parse_args()
    rights = load_rights()
    return {
        "probe": cmd_probe, "fetch": cmd_fetch,
        "register": cmd_register, "verify": cmd_verify,
    }[args.cmd](args, rights)


if __name__ == "__main__":
    sys.exit(main())
