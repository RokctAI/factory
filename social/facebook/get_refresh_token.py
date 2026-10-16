# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""One-time sign-in that prints a refresh token for TikTok or YouTube.

Run it on your own machine, sign in with the account the daily Reel posts
as, and paste the address the browser lands on back here. The refresh token
it prints goes into Occultation .env/production.env (below the END_FLUTTER
marker) - never into a repo, a chat or an Actions secret.

    python social/facebook/get_refresh_token.py youtube
    python social/facebook/get_refresh_token.py tiktok

The app's client id/key and secret are asked for at the prompt.
"""

import getpass
import secrets
import sys
import urllib.parse

import requests

PLATFORMS = {
    "youtube": {
        "authorize": "https://accounts.google.com/o/oauth2/v2/auth",
        "token": "https://oauth2.googleapis.com/token",
        "id_param": "client_id",
        # Desktop OAuth clients accept the loopback address without registering it.
        "redirect": "http://localhost",
        "extra": {
            "scope": "https://www.googleapis.com/auth/youtube.upload",
            "access_type": "offline",
            "prompt": "consent",
        },
    },
    "tiktok": {
        "authorize": "https://www.tiktok.com/v2/auth/authorize/",
        "token": "https://open.tiktokapis.com/v2/oauth/token/",
        "id_param": "client_key",
        # Must match a Redirect URI registered on the TikTok app (Login Kit).
        "redirect": "https://rokct.ai/",
        "extra": {"scope": "user.info.basic,video.publish"},
    },
}


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1 or argv[0] not in PLATFORMS:
        sys.exit(f"usage: get_refresh_token.py {'|'.join(PLATFORMS)}")
    cfg = PLATFORMS[argv[0]]
    client_id = input(f"{cfg['id_param']}: ").strip()
    client_secret = getpass.getpass("client secret: ").strip()
    redirect = input(f"redirect URI [{cfg['redirect']}]: ").strip() or cfg["redirect"]
    state = secrets.token_urlsafe(16)
    query = {cfg["id_param"]: client_id, "redirect_uri": redirect, "response_type": "code", "state": state}
    query.update(cfg["extra"])
    print("\nOpen this, sign in and allow access:\n")
    print(cfg["authorize"] + "?" + urllib.parse.urlencode(query))
    landed = input("\nPaste the full address the browser landed on: ").strip()
    params = urllib.parse.parse_qs(urllib.parse.urlparse(landed).query)
    if params.get("state", [""])[0] != state:
        sys.exit("That address is not from this sign-in (state mismatch).")
    if "code" not in params:
        sys.exit(f"No code in that address: {params.get('error', ['unknown error'])[0]}")
    resp = requests.post(
        cfg["token"],
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            cfg["id_param"]: client_id,
            "client_secret": client_secret,
            "code": params["code"][0],
            "grant_type": "authorization_code",
            "redirect_uri": redirect,
        },
        timeout=60,
    )
    body = resp.json()
    token = body.get("refresh_token")
    if not token:
        sys.exit(f"No refresh token returned ({resp.status_code}): {body.get('error_description') or body}")
    print(f"\n{argv[0].upper()}_REFRESH_TOKEN (put it in Occultation, then clear this screen):\n{token}")


if __name__ == "__main__":
    main()
