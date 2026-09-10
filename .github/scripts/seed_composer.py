#!/usr/bin/env python3
"""Write a seeded Next.js shell's composer.json from the Protocol, at spawn.

Ray, 2026-09-10: a composer.json that is empty "is same as not being
there", and a new repo needs the SDK versions current at the time of its
creation - read from the file that already gets updated on every SDK
change, the SDK consumers index in RokctAI/The-Rokct-Protocol. So the
spawn ships no static pins. After seed_app_repo.py has laid the overlay
down, this script rewrites <dest>/composer.json from the protocol's main,
read over HTTPS (raw.githubusercontent.com; the protocol repo is public,
GH_TOKEN is sent when set), taking the first source that knows the app:

  1. core/utils/frappe/composer/<app_type>.json - the product template
     `scripts/compose.sh refresh` composes from - when it exists and carries
     enabled `sdks` (entries copied verbatim).
  2. sdk_consumers.json - the consumers index (SDK_CONSUMERS.md is rendered
     from it) - when it lists the shell as a consumer: its SDKs with a
     Next.js half, kernel (telemetry_sdk, base_sdk) first, each entry built
     from the index's repo, path, version and pin. The index records no
     home SDK, so none is flagged and the log says so.
  3. nextjs_compose_example.json - the generic Next.js shell composition the
     protocol generates from that index (its sdks[]: the kernel, enabled,
     pinned, versioned) - for a brand-new app_type.
  4. Only when the protocol cannot be read at all: the overlay's own
     telemetry_sdk + base_sdk default already in <dest>/composer.json,
     logged loudly as a fallback (its pins are as old as the template).

Whichever source wins, every git-sourced entry is then re-pinned live:
`sha256` becomes the SHA-256 of that SDK's install.py at the entry's ref,
read from the SDK repo now (GH_TOKEN - the spawn passes FACTORY_PAT - for
the private repos), computed exactly as compose.sh's sha256_file() and the
composer's enforce_sdk_pin() compute it (CRLF folded to LF), so
`scripts/compose.sh refresh` accepts the file as written. A pin that cannot
be fetched keeps the source's pin with a warning; an entry left with no pin
at all is fatal. Finally every entry is checked against the index: an SDK
the index places in another repo or at another path is drift and stops the
spawn; an SDK the index does not list yet is only warned about.

The result is always a real composition - at least one enabled, pinned SDK -
or this exits non-zero and the spawn fails loudly rather than pushing a
shell that cannot compose.

Usage: seed_composer.py --dest <seeded dir> --app-type <slug> --name <text>
         [--protocol-ref main] [--protocol-dir <local checkout>]
"""
import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request

PROTOCOL_REPO = "RokctAI/The-Rokct-Protocol"
REGISTRY_DIR = "core/utils/frappe/composer"
CONSUMERS_JSON = "sdk_consumers.json"
EXAMPLE_JSON = "nextjs_compose_example.json"
KERNEL_SDKS = ("telemetry_sdk", "base_sdk")
API = "https://api.github.com"
RAW = "https://raw.githubusercontent.com"
USER_AGENT = "rokct-factory-seed-composer"
GITHUB = "https://github.com/"


class ProtocolUnreachable(Exception):
    """The protocol's main could not be read over HTTPS."""


def log(msg):
    print(f"[composer] {msg}")


def warn(msg):
    print(f"[composer] WARNING: {msg}", file=sys.stderr)


def sha256_lf(data):
    """SHA-256 with CRLF folded to LF - compose.sh sha256_file() and the
    composer's enforce_sdk_pin() normalise the same way, so a pin computed
    here verifies against a checkout on a core.autocrlf machine too."""
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def _request(url, token, accept):
    headers = {"Accept": accept, "User-Agent": USER_AGENT}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def fetch_raw(owner_repo, path, ref, token=None):
    """Bytes of <path> in <owner_repo> at <ref> via the contents API (works
    for private repos with a token), or None when it does not exist there
    (404). Other failures propagate."""
    url = f"{API}/repos/{owner_repo}/contents/{path}?ref={ref}"
    try:
        return _request(url, token, "application/vnd.github.raw+json")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def fetch_protocol(path, ref="main", token=None):
    """Bytes of a protocol file over plain HTTPS from raw main - the repo is
    public, so no token is sent there (raw.githubusercontent.com answers 404
    to a token it does not accept). A 404 from raw is retried once through
    the contents API with the token, which also serves a private fork.
    None when neither has the file; ProtocolUnreachable on anything else."""
    url = f"{RAW}/{PROTOCOL_REPO}/{ref}/{path}"
    try:
        return _request(url, None, "*/*")
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise ProtocolUnreachable(f"{url}: HTTP {e.code}")
    except (urllib.error.URLError, OSError) as e:
        raise ProtocolUnreachable(f"{url}: {e}")
    try:
        return fetch_raw(PROTOCOL_REPO, path, ref, token)
    except urllib.error.HTTPError as e:
        raise ProtocolUnreachable(f"{API} {PROTOCOL_REPO}/{path}@{ref}: HTTP {e.code}")
    except (urllib.error.URLError, OSError) as e:
        raise ProtocolUnreachable(f"{API} {PROTOCOL_REPO}/{path}@{ref}: {e}")


def fetch_head(owner_repo, ref, token=None):
    """Commit SHA <ref> resolves to in <owner_repo>, or None (informational
    only - it goes into a comment)."""
    url = f"{API}/repos/{owner_repo}/commits/{ref}"
    try:
        return _request(url, token, "application/vnd.github.sha").decode("ascii").strip()
    except (urllib.error.HTTPError, urllib.error.URLError, ValueError, OSError):
        return None


def repo_name(git_url):
    url = git_url.rstrip("/")
    if url.endswith(".git"):
        url = url[:-4]
    return url.rsplit("/", 1)[-1]


def owner_repo_of(git_url):
    """'RokctAI/core' from 'https://github.com/RokctAI/core[.git]'."""
    m = re.match(r"^https?://github\.com/([^/]+)/([^/]+?)(?:\.git)?/?$", git_url.strip())
    if not m:
        raise ValueError(f"not a GitHub repo URL: {git_url}")
    return f"{m.group(1)}/{m.group(2)}"


def sdk_subpath(entry):
    """'telemetry/nextjs' from path '../core/telemetry/nextjs' - the
    composer's own get_subpath_in_repo() rule: the path is relative to a
    sibling checkout named after the repo."""
    path = (entry.get("path") or "").replace("\\", "/").strip("/")
    name = repo_name(entry["git"])
    parts = [p for p in path.split("/") if p and p != ".."]
    if parts and parts[0].lower() == name.lower():
        parts = parts[1:]
    if not parts:
        raise ValueError(f"{entry.get('name')}: path {entry.get('path')!r} names no SDK directory")
    return "/".join(parts)


class Protocol:
    """The protocol's main, read lazily over HTTPS (or from a local
    checkout for tests and offline runs)."""

    def __init__(self, ref="main", local_dir=None, token=None):
        self.ref = ref
        self.local_dir = local_dir
        self.token = token
        self.head = None
        self._json = {}

    def read(self, rel):
        if self.local_dir:
            path = os.path.join(self.local_dir, *rel.split("/"))
            if not os.path.exists(path):
                return None
            with open(path, "rb") as f:
                return f.read()
        if self.head is None:
            self.head = fetch_head(PROTOCOL_REPO, self.ref, self.token) or self.ref
        return fetch_protocol(rel, self.ref, self.token)

    def read_json(self, rel, fresh=False):
        if fresh and not self.local_dir:
            try:
                raw = fetch_raw(PROTOCOL_REPO, rel, self.ref, self.token)
            except (urllib.error.HTTPError, urllib.error.URLError, OSError) as e:
                warn(f"{rel}: contents API re-read failed ({e}); keeping the raw copy")
                return self._json.get(rel)
            if raw is not None:
                try:
                    self._json[rel] = json.loads(raw.decode("utf-8-sig"))
                except ValueError as e:
                    raise SystemExit(f"[composer] {PROTOCOL_REPO} {rel} is not valid JSON: {e}")
            return self._json.get(rel)
        if rel not in self._json:
            raw = self.read(rel)
            if raw is None:
                self._json[rel] = None
            else:
                try:
                    self._json[rel] = json.loads(raw.decode("utf-8-sig"))
                except ValueError as e:
                    raise SystemExit(f"[composer] {PROTOCOL_REPO} {rel} is not valid JSON: {e}")
        return self._json[rel]

    def describe(self, rel):
        where = f"local checkout {self.local_dir}" if self.local_dir else f"@ {self.head or self.ref}"
        return f"{PROTOCOL_REPO} {rel} ({where})"


def registry_sdks(protocol, app_type):
    """Source 1: the product template's sdks[], or None."""
    template = protocol.read_json(f"{REGISTRY_DIR}/{app_type}.json")
    if template is None:
        return None
    sdks = [s for s in template.get("sdks") or [] if isinstance(s, dict) and s.get("name")]
    if not any(s.get("enabled", True) for s in sdks):
        return None
    return sdks


def index_entry(name, record, enabled=True):
    """One composer entry from an index record's nextjs block."""
    half = record["nextjs"]
    repo = record["repo"]
    return {
        "name": name,
        "enabled": enabled,
        "source": "git",
        "git": GITHUB + repo,
        "path": f"../{repo.split('/', 1)[1]}/{half['path'].strip('/')}",
        "ref": "main",
        "sha256": half.get("install_py_sha256"),
        "version": half.get("version"),
        "home_sdk": False,
        "_comment": (
            f"From {CONSUMERS_JSON} at spawn: {name} {half.get('version') or '?'} in {repo} "
            f"({half['path']}). The index records no home SDK - flag the home SDK by hand, then "
            f"add the registry template {REGISTRY_DIR}/<app_type>.json."
        ),
    }


def index_sdks(protocol, app_type):
    """Source 2: the shell's SDKs per the consumers index, or None when the
    index does not list it. Returns (sdks, index) - the index is also the
    drift-check reference."""
    data = protocol.read_json(CONSUMERS_JSON)
    if data is None:
        return None, None
    index = data.get("sdks") or {}
    if not any(isinstance(r, dict) and "nextjs" in r for r in index.values()):
        # raw.githubusercontent.com caches for a few minutes: an index read
        # right after a protocol merge may still be the old shape (no
        # nextjs blocks). Re-read it through the contents API, which is
        # never stale, before concluding the index knows no Next.js half.
        fresh = protocol.read_json(CONSUMERS_JSON, fresh=True)
        if fresh is not None:
            index = fresh.get("sdks") or index
    shells = {}
    for name, record in index.items():
        for shell in record.get("consumers") or []:
            shells.setdefault(shell.lower(), []).append(name)
    names = shells.get(app_type.lower())
    if names is None:
        return None, index
    ordered = list(KERNEL_SDKS) + [n for n in names if n not in KERNEL_SDKS]
    sdks, skipped = [], []
    for name in ordered:
        record = index.get(name)
        if not record or not record.get("repo") or not record.get("nextjs"):
            skipped.append(name)
            continue
        sdks.append(index_entry(name, record))
    if skipped:
        log(f"index: skipped {', '.join(skipped)} for '{app_type}' - no Next.js half recorded")
    return sdks, index


def example_sdks(protocol):
    """Source 3: the generic composition's sdks[] (the kernel), or None."""
    example = protocol.read_json(EXAMPLE_JSON)
    if example is None:
        return None
    sdks = [s for s in example.get("sdks") or [] if isinstance(s, dict) and s.get("name")]
    for entry in sdks:
        entry.pop("consumers", None)  # informational in the example; not a composer key
    return sdks or None


def check_against_index(sdks, index):
    """Drift check between the generated entries and the consumers index.
    Returns (problems, unknown): problems are fatal contradictions (the
    index places the SDK in another repo or at another path); unknown are
    SDKs the index does not list with a Next.js half yet."""
    problems, unknown = [], []
    for entry in sdks:
        if not entry.get("enabled", True) or entry.get("source", "local") != "git" or not entry.get("git"):
            continue
        name = entry.get("name", "?")
        record = (index or {}).get(name)
        if not record or not record.get("repo") or not record.get("nextjs"):
            unknown.append(name)
            continue
        if owner_repo_of(entry["git"]).lower() != record["repo"].lower():
            problems.append(f"{name}: composer points at {owner_repo_of(entry['git'])} but "
                            f"{CONSUMERS_JSON} says {record['repo']}")
        try:
            sub = sdk_subpath(entry)
        except ValueError as e:
            problems.append(str(e))
            continue
        if sub.lower() != record["nextjs"]["path"].strip("/").lower():
            problems.append(f"{name}: composer path '{entry.get('path')}' but {CONSUMERS_JSON} "
                            f"records {record['nextjs']['path']}")
    return problems, unknown


def pin_sdks(sdks, token=None):
    """Re-pin every enabled git entry in place. Returns the number pinned."""
    pinned = 0
    for entry in sdks:
        if not entry.get("enabled", True):
            continue
        if entry.get("source", "local") != "git" or not entry.get("git"):
            continue  # a local/sibling entry has nothing to pin
        name = entry.get("name", "?")
        ref = entry.get("ref") or "main"
        repo = owner_repo_of(entry["git"])
        installer = f"{sdk_subpath(entry)}/install.py"
        try:
            raw = fetch_raw(repo, installer, ref, token)
        except (urllib.error.HTTPError, urllib.error.URLError, OSError) as e:
            raw = None
            warn(f"{name}: could not read {repo}/{installer}@{ref}: {e}")
        if raw is None:
            if entry.get("sha256"):
                warn(f"{name}: keeping the source's own pin {entry['sha256'][:12]}... "
                     f"({repo}/{installer}@{ref} could not be read now)")
                pinned += 1
                continue
            raise SystemExit(
                f"[composer] {name}: {repo}/{installer}@{ref} is unreadable and the source "
                "carries no sha256 for it - refusing to seed an unpinned SDK "
                "(the composer would refuse it too)."
            )
        digest = sha256_lf(raw)
        head = fetch_head(repo, ref, token)
        at = f"{repo_name(entry['git'])}@{head[:8]}" if head else f"{repo_name(entry['git'])}@{ref}"
        changed = entry.get("sha256") not in (None, "", digest)
        if changed:
            warn(f"{name}: the source pinned {entry['sha256'][:12]}... but {installer} at {at} "
                 f"is {digest[:12]}... - re-pinned to what is on {ref} now")
        entry["sha256"] = digest
        entry["_sha256_comment"] = (
            f"SHA-256 of {installer} at {at} ({len(raw)} bytes), computed at spawn by the "
            "factory's seed_composer.py; required by the composer's unpinned-installer gate. "
            "`scripts/compose.sh refresh` re-pins from the registry."
        )
        log(f"{name:<18} {digest[:12]}  {repo}/{installer}@{ref}" + ("  (re-pinned)" if changed else ""))
        pinned += 1
    return pinned


def build_composer(app_type, app_name, sdks, source):
    slug = re.sub(r"[^a-z0-9]+", "_", app_type.lower()).strip("_") or "app"
    return {
        "name": f"{slug}_composer",
        "version": "1.0.0",
        "description": (
            f"Active Next.js SDK list for the {app_name} shell "
            "(composed by The-Rokct-Protocol core/utils/nextjs/sdk_composer.py)"
        ),
        "_comment": (
            f"Generated at spawn by the factory's seed_composer.py from {source}. "
            f"Registry templates are canonical: when {REGISTRY_DIR}/{app_type}.json carries an "
            "'sdks' array, every compose re-materializes this file from it, and "
            "`scripts/compose.sh refresh` re-pins every entry from the SDK repos. This committed "
            "copy is the offline record of the shell's composition floor (SDK_ECOSYSTEM.md hard "
            "invariant 9). Change the registry template first, then mirror it here."
        ),
        "sdks": sdks,
    }


def resolve_sdks(protocol, app_type, fallback_path):
    """(sdks, source description, index or None) from the first source
    that knows the app - see the module docstring."""
    index = None
    try:
        sdks = registry_sdks(protocol, app_type)
        if sdks is not None:
            source = protocol.describe(f"{REGISTRY_DIR}/{app_type}.json")
            log(f"registry template found: {source}")
            _, index = index_sdks(protocol, app_type)
            return sdks, source, index
        log(f"no registry template {REGISTRY_DIR}/{app_type}.json on the protocol's {protocol.ref}.")
        sdks, index = index_sdks(protocol, app_type)
        if sdks:
            source = protocol.describe(CONSUMERS_JSON) + f" (shell '{app_type}')"
            log(f"resolved {len(sdks)} SDK(s) for '{app_type}' from the consumers index; "
                "no home SDK is recorded there.")
            return sdks, source, index
        log(f"the consumers index lists no shell '{app_type}'." if index is not None
            else f"{CONSUMERS_JSON} is not on the protocol's {protocol.ref}.")
        sdks = example_sdks(protocol)
        if sdks:
            source = protocol.describe(EXAMPLE_JSON)
            log(f"using the generic Next.js shell composition: {source}")
            return sdks, source, index
        raise ProtocolUnreachable(f"{EXAMPLE_JSON} is not on the protocol's {protocol.ref}")
    except ProtocolUnreachable as e:
        warn(f"the protocol could not be read ({e}) - FALLING BACK to the overlay's own "
             "telemetry_sdk + base_sdk default. Its pins are as old as the factory template; "
             "run `scripts/compose.sh refresh` in the new shell as soon as possible.")
        if not os.path.exists(fallback_path):
            raise SystemExit(f"[composer] {fallback_path} is missing - the nextjs overlay did not seed it")
        with open(fallback_path, "r", encoding="utf-8-sig") as f:
            default = json.load(f)
        sdks = [s for s in default.get("sdks") or [] if isinstance(s, dict) and s.get("name")]
        return sdks, "the overlay's telemetry_sdk + base_sdk fallback (the protocol was unreachable)", index


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dest", required=True, help="seeded repo directory")
    ap.add_argument("--app-type", required=True, help="registry template name (.rokct/config/app_type)")
    ap.add_argument("--name", required=True, help="human app name, for the description")
    ap.add_argument("--protocol-ref", default="main")
    ap.add_argument("--protocol-dir", default="", help="local protocol checkout instead of HTTPS")
    args = ap.parse_args()

    token = os.environ.get("GH_TOKEN") or None
    out = os.path.join(args.dest, "composer.json")
    protocol = Protocol(args.protocol_ref, args.protocol_dir or None, token)

    sdks, source, index = resolve_sdks(protocol, args.app_type, out)
    enabled = [s for s in sdks if s.get("enabled", True)]
    if not enabled:
        raise SystemExit("[composer] the SDK list is empty - refusing to seed an empty composer.json")

    if index:
        problems, unknown = check_against_index(sdks, index)
        for name in unknown:
            warn(f"{name}: not in {CONSUMERS_JSON} with a Next.js half yet (the index refreshes "
                 "weekly) - repo/path unverified")
        if problems:
            raise SystemExit("[composer] the composition drifts from " + CONSUMERS_JSON + ":\n  - "
                             + "\n  - ".join(problems))
        log(f"index check: {len(enabled) - len(unknown)} entry/entries match {CONSUMERS_JSON}.")

    pinned = pin_sdks(sdks, token)
    if pinned == 0:
        raise SystemExit("[composer] no SDK could be pinned - refusing to seed an unpinned composer.json")

    composer = build_composer(args.app_type, args.name, sdks, source)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(composer, f, indent=2, ensure_ascii=False)
        f.write("\n")
    homes = [s["name"] for s in enabled if s.get("home_sdk") is True]
    log(f"wrote {os.path.relpath(out)}: {len(enabled)} enabled SDK(s), {pinned} pinned, "
        f"home SDK: {homes[0] if homes else 'none declared'}")


if __name__ == "__main__":
    main()
