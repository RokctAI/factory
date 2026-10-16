#!/usr/bin/env python3
"""Register a freshly spawned app repo as a `Roadmap` on the rlms Frappe site.

The last step of the spawn flow, and the only one that reaches outside GitHub.
Everything before it has already happened — the repo exists, `main` is pushed,
`Build v0` is open — so this step is *advisory*: it hands the new repo to the
fleet's own roadmap machinery and, whatever the answer, never fails the spawn.
A Frappe outage, an expired token or a site that was never configured must not
turn a repo that was created successfully into a red workflow.

What the other side does with it: `Roadmap` is an ordinary DocType, so it is
created through Frappe's generic resource API (`POST /api/resource/Roadmap`).
Inserting one is the whole hand-off: the site fills the document out in the
background afterwards, from what GitHub already knows about the repo. So the
useful half of this hand-off happens on the site, after we hang up.

Deliberately **not** sent: `jules_api_key`. The doctype accepts a per-roadmap
key, but nothing on that path calls an AI service on any key, so there is
nothing here for the factory to supply. Leaving it out means no AI key has to
exist as a factory secret at all.

Usage:
    register_roadmap.py --title <app> --repo-url <url> [--description <text>]
                        [--status <option>] [--timeout <seconds>]

Credentials come from the environment, the same three the rest of this repo
already uses against this site (see lessons/scripts/CAPS/build_skills_index.py):
RLMS_SITE_URL, RLMS_API_KEY, RLMS_API_SECRET. With RLMS_SITE_URL unset the
whole step is a clean no-op — the roadmap hand-off is optional.

Exits 0 in every case a caller can provoke, including refusal by the site.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

RESOURCE_PATH = "/api/resource/Roadmap"

# `status` is reqd on the doctype and is a Select; these are its options, in
# the doctype's own order. Frappe rejects anything else at insert time, so the
# value is checked here instead, where the complaint is readable.
STATUS_OPTIONS = ("Ideas", "Idea Passed", "Bugs", "Doing", "Done", "Archived")

# A spawned repo is an idea that cleared Ray's `approved` gate and now has a
# repo and an open `Build v0` — but that nothing has started building yet.
# "Ideas" would put it back in the unvetted pile it just came out of, and
# "Doing" would claim work is in flight. Overridable with --status.
DEFAULT_STATUS = "Idea Passed"

# Truncation for a site error body echoed into the log. Frappe returns a full
# HTML traceback on some failures; the first line is the useful part.
BODY_EXCERPT = 500


def _log(level, message):
    """One line to stdout, as a GitHub annotation when running in Actions.

    `warning` rather than `error` throughout: nothing this script reports is
    worth colouring a successful spawn red, but all of it is worth seeing.
    """
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::{level}::{message}", flush=True)
    else:
        print(f"{level}: {message}", flush=True)


def credentials(env=None):
    """(site_url, api_key, api_secret) from the environment; blanks included.

    The trailing slash is stripped from the site URL because RESOURCE_PATH
    carries its own leading one.
    """
    env = os.environ if env is None else env
    return (
        env.get("RLMS_SITE_URL", "").strip().rstrip("/"),
        env.get("RLMS_API_KEY", "").strip(),
        env.get("RLMS_API_SECRET", "").strip(),
    )


def auth_header(api_key, api_secret):
    """Frappe token auth — the exact shape build_skills_index.py already sends
    to this site. Not Bearer, not Basic: `token <key>:<secret>`.
    """
    return f"token {api_key}:{api_secret}"


def build_payload(title, repo_url, description="", status=DEFAULT_STATUS):
    """The Roadmap document to insert.

    Field names are the doctype's own: `title` (which is also the autoname
    source, so it becomes the document name), `source_repository` and `status`
    are the three reqd fields; `description` is optional and only sent when we
    have one, since `discover_roadmap_context` fills it in from the repo when
    it is blank. No `jules_api_key` — see the module docstring.
    """
    payload = {
        "title": title,
        "source_repository": repo_url,
        "status": status,
    }
    if description:
        payload["description"] = description
    return payload


def post_roadmap(
    site_url,
    api_key,
    api_secret,
    payload,
    timeout=30.0,
    opener=urllib.request.urlopen,
):
    """POST the document to the resource API and return the response body.

    Raises whatever urllib raises; `register` is the layer that swallows it.
    `opener` is injectable so the tests never touch the network.
    """
    request = urllib.request.Request(
        site_url + RESOURCE_PATH,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": auth_header(api_key, api_secret),
        },
        method="POST",
    )
    with opener(request, timeout=timeout) as response:
        return response.read().decode("utf-8", "replace")


def _excerpt(error):
    """First readable chunk of a Frappe error body, or '' if it will not read."""
    try:
        body = error.read().decode("utf-8", "replace")
    except Exception:
        return ""
    body = " ".join(body.split())
    return body[:BODY_EXCERPT]


def register(
    title,
    repo_url,
    description="",
    status=DEFAULT_STATUS,
    timeout=30.0,
    env=None,
    opener=urllib.request.urlopen,
):
    """Hand the repo to the roadmap. True when a Roadmap was created, False
    when the step skipped or the site refused it. Never raises.

    Every False path logs why, because the alternative — a silent no-op on a
    green workflow — is how a hand-off like this rots unnoticed.
    """
    site_url, api_key, api_secret = credentials(env)

    # The whole step is opt-in. No site configured is the normal state for
    # anyone running the factory without the rlms backend, not a problem.
    if not site_url:
        _log(
            "notice",
            "RLMS_SITE_URL is not set — skipping the roadmap registration. "
            "The new repo and its Build v0 issue are unaffected.",
        )
        return False

    absent = [
        name
        for name, value in (("RLMS_API_KEY", api_key), ("RLMS_API_SECRET", api_secret))
        if not value
    ]
    if absent:
        _log(
            "warning",
            f"RLMS_SITE_URL is set but {' and '.join(absent)} "
            f"{'is' if len(absent) == 1 else 'are'} missing — cannot authenticate, "
            f"so {repo_url} was NOT registered on the roadmap. Add it by hand, or "
            "configure the secret and re-run. The spawn itself succeeded.",
        )
        return False

    if not title or not repo_url:
        _log(
            "warning",
            "register_roadmap.py needs both --title and --repo-url; got "
            f"title={title!r} repo-url={repo_url!r}. Nothing was registered.",
        )
        return False

    if status not in STATUS_OPTIONS:
        _log(
            "warning",
            f"{status!r} is not one of the Roadmap doctype's status options "
            f"({', '.join(STATUS_OPTIONS)}) — the site would reject it. "
            f"{repo_url} was NOT registered.",
        )
        return False

    payload = build_payload(title, repo_url, description, status)

    try:
        post_roadmap(site_url, api_key, api_secret, payload, timeout, opener)
    except urllib.error.HTTPError as err:
        detail = _excerpt(err)
        _log(
            "warning",
            f"The roadmap site refused {title} ({repo_url}): HTTP {err.code} "
            f"{err.reason}." + (f" {detail}" if detail else "") + " The spawn "
            "succeeded; add the Roadmap by hand if it is still missing.",
        )
        return False
    except (urllib.error.URLError, OSError) as err:
        _log(
            "warning",
            f"Could not reach the roadmap site to register {title} ({repo_url}): "
            f"{err}. The spawn succeeded; add the Roadmap by hand if it is still "
            "missing.",
        )
        return False

    print(
        f"Registered {title} -> {repo_url} as a Roadmap ({status}). "
        "The site will classify the repo in the background.",
        flush=True,
    )
    return True


def main():
    ap = argparse.ArgumentParser(
        description="Register a spawned app repo as a Roadmap on the rlms site."
    )
    ap.add_argument("--title", required=True, help="Roadmap title (the app name).")
    ap.add_argument("--repo-url", required=True, help="URL of the new repo.")
    ap.add_argument("--description", default="", help="One-line app description.")
    # Not argparse `choices`: an unknown value is reported by `register` and
    # skipped, rather than exiting 2 and reddening the run.
    ap.add_argument(
        "--status",
        default=DEFAULT_STATUS,
        help=f"Roadmap status, one of: {', '.join(STATUS_OPTIONS)}.",
    )
    ap.add_argument("--timeout", type=float, default=30.0, help="Seconds.")
    args = ap.parse_args()

    register(
        title=args.title,
        repo_url=args.repo_url,
        description=args.description,
        status=args.status,
        timeout=args.timeout,
    )
    # Always. Failing here would fail a spawn that already succeeded.
    return 0


if __name__ == "__main__":
    sys.exit(main())
