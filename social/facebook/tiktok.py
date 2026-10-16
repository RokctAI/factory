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

"""Post the daily clip to TikTok through the Content Posting API (Direct Post).

Needs a TikTok developer app with Login Kit + Content Posting API and the
scope video.publish. Until TikTok audits the app, every post is forced to
private (SELF_ONLY); this reads the privacy options TikTok offers the account
and posts publicly as soon as that option appears.

Environment (from Occultation .env/production.env, never printed):
    TIKTOK_CLIENT_KEY, TIKTOK_CLIENT_SECRET, TIKTOK_REFRESH_TOKEN
"""

import sys
import time
from pathlib import Path

import requests

API = "https://open.tiktokapis.com/v2"
KEYS = ("TIKTOK_CLIENT_KEY", "TIKTOK_CLIENT_SECRET", "TIKTOK_REFRESH_TOKEN")


def _check(resp, what):
    try:
        body = resp.json()
    except ValueError:
        body = {"raw": resp.text[:300]}
    err = body.get("error")
    code = err.get("code") if isinstance(err, dict) else err
    if resp.status_code >= 400 or (code and code != "ok"):
        msg = err.get("message") if isinstance(err, dict) else body.get("error_description", body)
        sys.exit(f"TikTok {what} failed ({resp.status_code}): {code}: {msg}")
    return body


def access_token(client_key, client_secret, refresh_token):
    """A fresh 24 h access token from the long-lived refresh token."""
    body = _check(
        requests.post(
            f"{API}/oauth/token/",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "client_key": client_key,
                "client_secret": client_secret,
                "grant_type": "refresh_token",
                "refresh_token": refresh_token,
            },
            timeout=60,
        ),
        "token refresh",
    )
    return body["access_token"]


def publish(env, mp4: Path, caption):
    """Upload and publish; returns (publish_id, post_id or '', privacy)."""
    token = access_token(*(env[k] for k in KEYS))
    auth = {"Authorization": f"Bearer {token}", "Content-Type": "application/json; charset=UTF-8"}
    creator = _check(
        requests.post(f"{API}/post/publish/creator_info/query/", headers=auth, timeout=60),
        "creator info",
    )["data"]
    options = creator.get("privacy_level_options") or ["SELF_ONLY"]
    privacy = "PUBLIC_TO_EVERYONE" if "PUBLIC_TO_EVERYONE" in options else options[0]

    data = mp4.read_bytes()
    size = len(data)
    init = _check(
        requests.post(
            f"{API}/post/publish/video/init/",
            headers=auth,
            json={
                "post_info": {
                    "title": caption[:2200],
                    "privacy_level": privacy,
                    "disable_comment": False,
                    "disable_duet": False,
                    "disable_stitch": False,
                },
                # The clip is a few MB, well under the 64 MB single-chunk limit.
                "source_info": {
                    "source": "FILE_UPLOAD",
                    "video_size": size,
                    "chunk_size": size,
                    "total_chunk_count": 1,
                },
            },
            timeout=60,
        ),
        "upload init",
    )["data"]
    publish_id = init["publish_id"]
    resp = requests.put(
        init["upload_url"],
        headers={
            "Content-Type": "video/mp4",
            "Content-Length": str(size),
            "Content-Range": f"bytes 0-{size - 1}/{size}",
        },
        data=data,
        timeout=300,
    )
    if resp.status_code >= 400:
        sys.exit(f"TikTok upload failed ({resp.status_code}): {resp.text[:300]}")

    post_id = ""
    for _ in range(30):  # TikTok processes the upload before it is live
        status = _check(
            requests.post(
                f"{API}/post/publish/status/fetch/",
                headers=auth,
                json={"publish_id": publish_id},
                timeout=60,
            ),
            "publish status",
        )["data"]
        phase = status.get("status")
        if phase == "FAILED":
            sys.exit(f"TikTok rejected the post: {status.get('fail_reason')}")
        if phase == "PUBLISH_COMPLETE":
            ids = status.get("publicaly_available_post_id") or status.get("publicly_available_post_id") or []
            post_id = str(ids[0]) if ids else ""
            break
        time.sleep(10)
    return publish_id, post_id, privacy
