#!/usr/bin/env python3
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

"""Fetch the Grade 10-12 (FET) CAPS documents and Annual Teaching Plans for
the subjects added beside the original six, straight from education.gov.za.

Links are resolved by label from the two DBE index pages every time, so a
reissued document is picked up without editing this file:

- CAPS FET page (tabid 570): one module per group, Home Languages (mid 1555),
  First Additional Languages (mid 1556), English subjects (mid 1558).
- National ATP index (tabid 3205): per grade, Home Languages,
  First Additional Languages and Content Subjects.

Output follows the Grades R-9 layout (`GET_SOURCES.md`):
`{subject}/curriculum/caps_gr10-12.pdf` and `{subject}/syllabus/grade{N}_atp.pdf`,
with each file's source URL, edition, size and sha256 in `fet_sources.json`.

    python3 fetch_fet_sources.py            # fetch missing files, rewrite the manifest
    python3 fetch_fet_sources.py --verify   # re-hash committed files against the manifest
"""
import argparse
import datetime
import hashlib
import html
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

CAPS_DIR = Path(__file__).resolve().parents[2] / "curriculum" / "CAPS"
MANIFEST = CAPS_DIR / "fet_sources.json"
BASE = "https://www.education.gov.za"
CAPS_PAGE = BASE + "/Curriculum/CurriculumAssessmentPolicyStatements(CAPS)/CAPSFET.aspx"
ATP_PAGE = BASE + "/Default.aspx?tabid=3205"
UA = {"User-Agent": "Mozilla/5.0 (rokct factory CAPS fetch)"}

# History's English CAPS is not linked from the CAPS FET page (only the
# Afrikaans one is); DBE hosts the amended edition directly.
HISTORY_CAPS = (BASE + "/Portals/0/CD/National%20Curriculum%20Statements%20and%20Vocational/"
                "AMENDED%20CAPS%20DOC%20HISTORY%20GRADE%2010%20-12.pdf")

LANGUAGES = {
    # folder prefix: label on both DBE pages
    "english": "English",
    "afrikaans": "Afrikaans",
    "isizulu": "IsiZulu",
    "isixhosa": "IsiXhosa",
    "isindebele": "IsiNdebele",
    "sepedi": "Sepedi",
    "sesotho": "Sesotho",
    "setswana": "Setswana",
    "siswati": "Siswati",
    "tshivenda": "Tshivenda",
    "xitsonga": "Xitsonga",
}

# folder: (label on the CAPS FET page, label on the ATP index)
CONTENT = {
    "life_sciences": ("Life Sciences", "Life Sciences"),
    "agricultural_sciences": ("Agricultural Science", "Agricultural Sciences"),
    "history": (None, "History"),
    "business_studies": ("Business Studies", "Business Studies"),
    "life_orientation": ("Life Orientation", "Life Orientation"),
    "computer_applications_technology": ("Computer Applications Technology", "CAT"),
    "information_technology": ("Information Technology", "IT"),
    "tourism": ("Tourism", "Tourism"),
    "consumer_studies": ("Consumer Studies", "Consumer Studies"),
    "engineering_graphics_and_design": ("Engineering Graphics and Design",
                                        "Engineering Graphics and Design"),
    "visual_arts": ("Visual Arts", "Visual Arts"),
    "religion_studies": ("Religion Studies", "Religion Studies"),
}

# 2024 CAPS amendments (Section 3 replaced) published beside the CAPS documents.
AMENDMENTS = {
    "computer_applications_technology": "Amendment: CAT CAPS 2024 -Section 3",
    "information_technology": "Amendment: IT CAPS 2024 -Section 3",
}


def get(url, tries=5):
    """GET with retries: education.gov.za resets connections under load."""
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=180) as r:
                return r.read()
        except OSError:
            if attempt == tries - 1:
                raise
            time.sleep(5 * (attempt + 1))


def links(page_html):
    """[(module_heading, label, absolute_url)] in page order."""
    out, heading = [], None
    pat = re.compile(r'<span class="Head"[^>]*>(.*?)</span>|<h[1-4][^>]*>(.*?)</h[1-4]>|'
                     r'<a[^>]+href="([^"]*)"[^>]*>(.*?)</a>', re.S)
    for m in pat.finditer(page_html):
        if m.group(3) is None:
            text = html.unescape(re.sub("<[^>]+>", "", m.group(1) or m.group(2) or "")).strip()
            if text:
                heading = text
            continue
        url = html.unescape(m.group(3))
        if "LinkClick" not in url or "forcedownload" in url:
            continue
        label = html.unescape(re.sub("<[^>]+>", "", m.group(4))).strip()
        out.append((heading, label, url if url.startswith("http") else BASE + url))
    return out


def caps_url(caps_links, mid, label):
    for _, lab, url in caps_links:
        if f"mid={mid}" in url and lab.lower() == label.lower():
            return url
    return None


def atp_url(atp_links, grade, group, label):
    """group: 'Home Languages' | 'First Additional Languages' | 'Content Subjects'."""
    want = {label.lower(), label.lower() + " hl"}
    for head, lab, url in atp_links:
        if head and head.lower() == f"grade {grade} {group}".lower() and lab.lower() in want:
            return url
    return None


def plan():
    caps_links = links(get(CAPS_PAGE).decode("utf-8", "replace"))
    atp_links = links(get(ATP_PAGE).decode("utf-8", "replace"))
    items = []
    for prefix, label in LANGUAGES.items():
        for kind, mid, group in (("home_language", 1555, "Home Languages"),
                                 ("first_additional_language", 1556, "First Additional Languages")):
            folder = f"{prefix}_{kind}"
            name = f"{'Home Languages' if mid == 1555 else 'First Additional Language'} / {label}"
            items.append(("caps", folder, None, caps_url(caps_links, mid, label), name))
            for g in (10, 11, 12):
                items.append(("atp", folder, g, atp_url(atp_links, g, group, label),
                              f"Grade {g}: {group} / {label}"))
    for folder, (caps_label, atp_label) in CONTENT.items():
        url = caps_url(caps_links, 1558, caps_label) if caps_label else HISTORY_CAPS
        items.append(("caps", folder, None, url, caps_label or "History (amended CAPS)"))
        if folder in AMENDMENTS:
            items.append(("caps_amendment", folder, None,
                          caps_url(caps_links, 1208, AMENDMENTS[folder]), AMENDMENTS[folder]))
        for g in (10, 11, 12):
            items.append(("atp", folder, g, atp_url(atp_links, g, "Content Subjects", atp_label),
                          f"Grade {g}: Content Subjects / {atp_label}"))
    return items


def rel_path(kind, folder, grade):
    if kind == "caps":
        return f"{folder}/curriculum/caps_gr10-12.pdf"
    if kind == "caps_amendment":
        return f"{folder}/curriculum/caps_gr10-12_amendment_2024_section3.pdf"
    return f"{folder}/syllabus/grade{grade}_atp.pdf"


def edition_of(pdf_bytes):
    """Edition as printed on the ATP's first pages (e.g. 2023/24), else None."""
    try:
        import pymupdf
    except ImportError:
        return None
    try:
        doc = pymupdf.open(stream=pdf_bytes, filetype="pdf")
        text = " ".join(doc[i].get_text() for i in range(min(3, doc.page_count)))
    except Exception:
        return None
    m = re.search(r"20(2)0?(\d)\s*[/-]\s*(?:20)?(2\d)", text)  # also DBE's "20203/24" typo
    if m:
        return f"20{m.group(1)}{m.group(2)}/{m.group(3)}"
    m = re.search(r"\b(202\d)\b", text)
    return m.group(1) if m else None


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--verify", action="store_true", help="re-hash files against the manifest")
    ap.add_argument("--dest", type=Path, default=CAPS_DIR)
    args = ap.parse_args()

    if args.verify:
        man = json.loads(MANIFEST.read_text(encoding="utf-8"))
        bad = [f["path"] for f in man["files"]
               if hashlib.sha256((CAPS_DIR / f["path"]).read_bytes()).hexdigest() != f["sha256"]]
        print("\n".join(bad) or f"ok: {len(man['files'])} files match")
        return 1 if bad else 0

    today = datetime.date.today().isoformat()
    old = {}
    if MANIFEST.exists():
        old = {f["path"]: f for f in json.loads(MANIFEST.read_text(encoding="utf-8"))["files"]}
    files, missing = [], []
    for kind, folder, grade, url, label in plan():
        path = rel_path(kind, folder, grade)
        if not url:
            missing.append(f"{path}: no '{label}' link on the DBE page")
            continue
        target = args.dest / path
        if target.exists() and path in old and old[path]["source_url"] == url:
            files.append(old[path])
            continue
        data = get(url)
        if not data.startswith(b"%PDF"):
            missing.append(f"{path}: {url} did not return a PDF")
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        entry = {"kind": kind, "subject": folder}
        entry.update({"grade": grade} if grade else {"grades": "10-12"})
        entry.update({"path": path, "source_url": url, "label": label})
        if kind == "atp":
            entry["edition"] = edition_of(data)
        entry.update({"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                      "fetched": today})
        files.append(entry)
        print(f"fetched {path} ({len(data)} bytes)")
    manifest = {
        "version": 1,
        "curriculum": "CAPS",
        "scope": "Grades 10-12 (FET band), subjects beyond the original six",
        "fetched": today,
        "language": "Content subjects in English; languages in their own language",
        "files": files,
        "gaps": missing,
    }
    if args.dest == CAPS_DIR:
        MANIFEST.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n",
                            encoding="utf-8")
    for m in missing:
        print("MISSING", m, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
