#!/usr/bin/env python3
# Licensed under the MIT License.
# Copyright 2026 RokctAI
"""Unit tests for .github/scripts/register_roadmap.py (stdlib unittest).

Two properties matter here, and they pull in opposite directions.

  1. When it works, it must send *exactly* what the Roadmap doctype expects —
     the reqd trio `title`/`source_repository`/`status`, a status drawn from
     the doctype's real Select options, and Frappe's `token <key>:<secret>`
     auth rather than Bearer or Basic. A payload the site rejects is a
     hand-off that silently never happens.
  2. When it does *not* work, it must not take the spawn down with it. By the
     time this runs the repo exists, main is pushed and Build v0 is open. So
     every failure path — no secrets at all, half the secrets, a 4xx from the
     site, a dead socket — has to return quietly and say why.

Nothing here touches the network: `register` takes its opener as an argument
and every test passes a recorder or an exploding stub.

Run from the repo root:
    python3 -m unittest discover -s .github/scripts/tests -v
"""

import contextlib
import io
import json
import sys
import unittest
import urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import register_roadmap  # noqa: E402

SITE = "https://rlms.example.com"
FULL_ENV = {
    "RLMS_SITE_URL": SITE,
    "RLMS_API_KEY": "key123",
    "RLMS_API_SECRET": "secret456",
}
TITLE = "receipt-splitter"
REPO_URL = "https://github.com/RokctAI/receipt-splitter"
DESCRIPTION = "Splits a photographed till slip between people."


class FakeResponse:
    """Just enough of an http.client.HTTPResponse for `with ... as r: r.read()`."""

    def __init__(self, body=b'{"data": {"name": "receipt-splitter"}}'):
        self._body = body

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class Recorder:
    """Stands in for urllib.request.urlopen and keeps what it was handed."""

    def __init__(self, error=None):
        self.error = error
        self.request = None
        self.timeout = None
        self.calls = 0

    def __call__(self, request, timeout=None):
        self.calls += 1
        self.request = request
        self.timeout = timeout
        if self.error is not None:
            raise self.error
        return FakeResponse()

    @property
    def payload(self):
        return json.loads(self.request.data.decode("utf-8"))


def http_error(code=417, reason="EXPECTATION FAILED", body=b"Validation failed"):
    return urllib.error.HTTPError(
        SITE + register_roadmap.RESOURCE_PATH, code, reason, {}, io.BytesIO(body)
    )


def run(env, opener, **kwargs):
    """Call register() with the noise captured. Returns (result, stdout)."""
    call = {
        "title": TITLE,
        "repo_url": REPO_URL,
        "description": DESCRIPTION,
        "env": env,
        "opener": opener,
    }
    call.update(kwargs)
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        result = register_roadmap.register(**call)
    return result, buffer.getvalue()


class PayloadTests(unittest.TestCase):
    """Secrets present: the right document, at the right URL, with the right key."""

    def setUp(self):
        self.opener = Recorder()
        self.result, self.output = run(FULL_ENV, self.opener)

    def test_it_posts_once_and_reports_success(self):
        self.assertTrue(self.result)
        self.assertEqual(self.opener.calls, 1)
        self.assertIn("Registered", self.output)

    def test_it_posts_to_the_generic_resource_endpoint(self):
        self.assertEqual(
            self.opener.request.full_url, SITE + "/api/resource/Roadmap"
        )
        self.assertEqual(self.opener.request.get_method(), "POST")

    def test_auth_header_is_frappe_token_key_colon_secret(self):
        # The shape build_skills_index.py already uses against this site.
        self.assertEqual(
            self.opener.request.get_header("Authorization"), "token key123:secret456"
        )
        self.assertEqual(
            self.opener.request.get_header("Content-type"), "application/json"
        )

    def test_payload_carries_the_three_reqd_doctype_fields(self):
        payload = self.opener.payload
        self.assertEqual(payload["title"], TITLE)
        self.assertEqual(payload["source_repository"], REPO_URL)
        self.assertEqual(payload["status"], register_roadmap.DEFAULT_STATUS)
        self.assertEqual(payload["description"], DESCRIPTION)

    def test_default_status_is_a_real_doctype_option(self):
        self.assertIn(register_roadmap.DEFAULT_STATUS, register_roadmap.STATUS_OPTIONS)
        self.assertEqual(register_roadmap.DEFAULT_STATUS, "Idea Passed")

    def test_the_jules_key_is_never_sent(self):
        # It falls back to Roadmap Settings on the site; it must not become a
        # factory secret by the back door.
        self.assertNotIn("jules_api_key", self.opener.payload)

    def test_no_secret_leaks_into_the_log(self):
        self.assertNotIn("secret456", self.output)
        self.assertNotIn("key123", self.output)


class PayloadShapeTests(unittest.TestCase):
    """build_payload on its own — the field names are load-bearing."""

    def test_description_is_omitted_when_blank(self):
        # discover_roadmap_context fills it in from the repo when it is empty.
        payload = register_roadmap.build_payload(TITLE, REPO_URL, "")
        self.assertNotIn("description", payload)
        self.assertEqual(set(payload), {"title", "source_repository", "status"})

    def test_status_options_match_the_doctype(self):
        self.assertEqual(
            register_roadmap.STATUS_OPTIONS,
            ("Ideas", "Idea Passed", "Bugs", "Doing", "Done", "Archived"),
        )

    def test_every_option_is_accepted(self):
        for status in register_roadmap.STATUS_OPTIONS:
            with self.subTest(status=status):
                opener = Recorder()
                result, _ = run(FULL_ENV, opener, status=status)
                self.assertTrue(result)
                self.assertEqual(opener.payload["status"], status)

    def test_trailing_slash_on_the_site_url_does_not_double(self):
        opener = Recorder()
        run({**FULL_ENV, "RLMS_SITE_URL": SITE + "/"}, opener)
        self.assertEqual(opener.request.full_url, SITE + "/api/resource/Roadmap")


class SkipTests(unittest.TestCase):
    """Secrets absent: skip cleanly, say so, post nothing."""

    def test_no_secrets_at_all_is_a_clean_skip(self):
        opener = Recorder()
        result, output = run({}, opener)
        self.assertFalse(result)
        self.assertEqual(opener.calls, 0)
        self.assertIn("RLMS_SITE_URL is not set", output)

    def test_blank_site_url_is_a_clean_skip(self):
        for blank in ("", "   ", "\n"):
            with self.subTest(blank=blank):
                opener = Recorder()
                result, output = run({**FULL_ENV, "RLMS_SITE_URL": blank}, opener)
                self.assertFalse(result)
                self.assertEqual(opener.calls, 0)
                self.assertIn("skipping", output)

    def test_site_url_without_credentials_warns_and_posts_nothing(self):
        # The dangerous middle case: configured enough to look intentional,
        # not enough to authenticate. Must be loud, must not post.
        opener = Recorder()
        result, output = run({"RLMS_SITE_URL": SITE}, opener)
        self.assertFalse(result)
        self.assertEqual(opener.calls, 0)
        self.assertIn("RLMS_API_KEY", output)
        self.assertIn("RLMS_API_SECRET", output)
        self.assertIn("NOT registered", output)

    def test_a_single_missing_secret_is_named(self):
        opener = Recorder()
        result, output = run({**FULL_ENV, "RLMS_API_SECRET": ""}, opener)
        self.assertFalse(result)
        self.assertEqual(opener.calls, 0)
        self.assertIn("RLMS_API_SECRET", output)
        self.assertNotIn("RLMS_API_KEY is", output)

    def test_a_status_off_the_doctype_is_refused_before_posting(self):
        opener = Recorder()
        result, output = run(FULL_ENV, opener, status="Active")
        self.assertFalse(result)
        self.assertEqual(opener.calls, 0)
        self.assertIn("Idea Passed", output)

    def test_missing_arguments_do_not_post(self):
        for kwargs in ({"title": ""}, {"repo_url": ""}):
            with self.subTest(kwargs=kwargs):
                opener = Recorder()
                result, output = run(FULL_ENV, opener, **kwargs)
                self.assertFalse(result)
                self.assertEqual(opener.calls, 0)
                self.assertIn("Nothing was registered", output)


class NonFatalFailureTests(unittest.TestCase):
    """The site is reachable-ish but says no. Log it; never raise."""

    def test_http_error_is_logged_and_swallowed(self):
        result, output = run(FULL_ENV, Recorder(error=http_error()))
        self.assertFalse(result)
        self.assertIn("417", output)
        self.assertIn("EXPECTATION FAILED", output)
        self.assertIn("The spawn succeeded", output)

    def test_the_error_body_is_echoed(self):
        _, output = run(
            FULL_ENV, Recorder(error=http_error(body=b"DuplicateEntryError: Roadmap"))
        )
        self.assertIn("DuplicateEntryError", output)

    def test_a_long_error_body_is_truncated(self):
        _, output = run(
            FULL_ENV, Recorder(error=http_error(body=b"x" * 5000))
        )
        self.assertNotIn("x" * (register_roadmap.BODY_EXCERPT + 1), output)

    def test_common_status_codes_are_all_non_fatal(self):
        for code, reason in ((403, "FORBIDDEN"), (409, "CONFLICT"), (500, "SERVER")):
            with self.subTest(code=code):
                result, output = run(
                    FULL_ENV, Recorder(error=http_error(code=code, reason=reason))
                )
                self.assertFalse(result)
                self.assertIn(str(code), output)

    def test_an_unreadable_error_body_does_not_explode(self):
        class Unreadable(urllib.error.HTTPError):
            def read(self, *a, **kw):
                raise OSError("stream is gone")

        error = Unreadable(SITE, 502, "BAD GATEWAY", {}, None)
        result, output = run(FULL_ENV, Recorder(error=error))
        self.assertFalse(result)
        self.assertIn("502", output)

    def test_an_unreachable_site_is_logged_and_swallowed(self):
        result, output = run(
            FULL_ENV, Recorder(error=urllib.error.URLError("Name or service not known"))
        )
        self.assertFalse(result)
        self.assertIn("Could not reach", output)
        self.assertIn(REPO_URL, output)

    def test_a_timeout_is_logged_and_swallowed(self):
        result, output = run(FULL_ENV, Recorder(error=TimeoutError("timed out")))
        self.assertFalse(result)
        self.assertIn("Could not reach", output)

    def test_the_timeout_is_passed_through(self):
        opener = Recorder()
        run(FULL_ENV, opener, timeout=5.0)
        self.assertEqual(opener.timeout, 5.0)


class NeverFatalTests(unittest.TestCase):
    """The property the whole step rests on, asserted directly."""

    def test_register_never_raises_whatever_the_opener_does(self):
        errors = [
            http_error(),
            urllib.error.URLError("boom"),
            TimeoutError("timed out"),
            ConnectionResetError("reset"),
            OSError("no route to host"),
        ]
        for error in errors:
            with self.subTest(error=type(error).__name__):
                try:
                    result, _ = run(FULL_ENV, Recorder(error=error))
                except Exception as exc:  # pragma: no cover - the failure case
                    self.fail(f"register() raised {exc!r}")
                self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
