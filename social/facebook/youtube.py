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

"""Post the daily clip to YouTube as a Short (Data API v3 videos.insert).

A vertical clip under a minute is filed as a Short automatically; #Shorts in
the title makes it certain. Needs a Google Cloud project with the YouTube
Data API v3 enabled and an OAuth client (Desktop app), published to
production so the refresh token does not expire after 7 days. Until Google
audits the project, uploads from it are locked to private.

Environment (from Occultation .env/production.env, never printed):
    YOUTUBE_CLIENT_ID, YOUTUBE_CLIENT_SECRET, YOUTUBE_REFRESH_TOKEN
"""

import json
import sys
from pathlib import Path

import requests

TOKEN_URL = "https://oauth2.googleapis.com/token"
UPLOAD_URL = "https://www.googleapis.com/upload/youtube/v3/videos"
KEYS = ("YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET", "YOUTUBE_REFRESH_TOKEN")
CATEGORY_EDUCATION = "27"


def _check(resp, what):
    try:
        body = resp.json()
    except ValueError:
        body = {"raw": resp.text[:300]}
    if resp.status_code >= 400 or "error" in body:
        err = body.get("error", body)
        msg = err.get("message") if isinstance(err, dict) else body.get("error_description", err)
        sys.exit(f"YouTube {what} failed ({resp.status_code}): {msg}")
    return body


def access_token(client_id, client_secret, refresh_token):
    return _check(
        requests.post(
            TOKEN_URL,
            data={
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token,
                "grant_type": "refresh_token",
            },
            timeout=60,
        ),
        "token refresh",
    )["access_token"]


def publish(env, mp4: Path, title, description):
    """Resumable upload in one request; returns (video_id, url, privacy)."""
    token = access_token(*(env[k] for k in KEYS))
    data = mp4.read_bytes()
    meta = {
        "snippet": {
            "title": title[:100],
            "description": description[:5000],
            "categoryId": CATEGORY_EDUCATION,
        },
        "status": {"privacyStatus": "public", "selfDeclaredMadeForKids": False},
    }
    start = requests.post(
        UPLOAD_URL,
        params={"uploadType": "resumable", "part": "snippet,status"},
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=UTF-8",
            "X-Upload-Content-Type": "video/mp4",
            "X-Upload-Content-Length": str(len(data)),
        },
        data=json.dumps(meta),
        timeout=60,
    )
    if start.status_code >= 400 or "Location" not in start.headers:
        _check(start, "upload start")
        sys.exit(f"YouTube upload start returned no upload URL ({start.status_code})")
    video = _check(
        requests.put(
            start.headers["Location"],
            headers={"Content-Type": "video/mp4", "Content-Length": str(len(data))},
            data=data,
            timeout=600,
        ),
        "upload",
    )
    video_id = video["id"]
    privacy = (video.get("status") or {}).get("privacyStatus", "public")
    return video_id, f"https://youtube.com/shorts/{video_id}", privacy
