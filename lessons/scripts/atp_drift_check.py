#!/usr/bin/env python3
# Licensed under the MIT License.
# Copyright 2026 RokctAI
"""Verify caps_seed.json term placements against the DBE ATP source PDFs.

The DBE reissues Annual Teaching Plans every school year, and a topic's term
placement can shift between editions. This maintenance tool re-verifies the
seed's `term` column against the ATP documents recorded in the seed file's
`_sources` map:

    pip install pypdf requests
    python lessons/scripts/atp_drift_check.py            # verify all
    python lessons/scripts/atp_drift_check.py --subject "Maths" --grade 11
    python lessons/scripts/atp_drift_check.py --sources-dir <dir-of-pdfs>

For each seed entry it reports:
    CONFIRMED   the topic's words appear in the stated term's section
    DRIFT       the topic's words appear only in a DIFFERENT term's section
                (exit code 1 — update the seed or the source URL)
    UNVERIFIED  the extractor could not locate the topic in any term
                (PDF text extraction is imperfect; check by hand)

It never rewrites the seed — term data is only ever changed by a human
looking at the actual document, matching the project's no-guessed-terms rule.
When the DBE publishes a new ATP edition, update the URLs in `_sources`
(and `atp_edition`) and re-run.
"""

import argparse
import io
import json
import re
import sys
import urllib.request
from pathlib import Path

SEED_PATH = Path("lessons/curriculum/caps_seed.json")

STOPWORDS = {
    "and", "the", "of", "in", "for", "with", "other", "basic", "grade",
    "south", "africa", "african", "aspects", "dynamics", "growth", "decay",
}


def fetch_pdf(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def term_buckets(pdf_bytes):
    """Split ATP text into {term: text} using the '(TERM n' page headers."""
    from pypdf import PdfReader
    reader = PdfReader(io.BytesIO(pdf_bytes))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    buckets = {}
    current = None
    for line in text.split("\n"):
        m = re.search(r"\(TERM (\d)", line)
        if m:
            current = m.group(1)
            buckets.setdefault(current, [])
            continue
        if current:
            buckets[current].append(line)
    return {t: "\n".join(lines).lower() for t, lines in buckets.items()}


def _sig_words(text):
    return [w for w in re.findall(r"[a-zA-Z]{4,}", text.lower()) if w not in STOPWORDS]


def entry_word_sets(entry):
    """Two independent identifying word sets: the CAPS topic name and the
    subtopic's content words. Topic names sometimes appear only in page
    headers (which the bucket splitter consumes), so the subtopic's words
    are an equally valid locator."""
    return [ws for ws in (_sig_words(entry["topic"]), _sig_words(entry["subtopic"])) if ws]


def terms_containing(words, buckets):
    """Terms whose text contains at least half of the topic's words."""
    if not words:
        return []
    hits = []
    threshold = max(1, (len(words) + 1) // 2)
    for term, text in buckets.items():
        if sum(1 for w in words if w in text) >= threshold:
            hits.append(term)
    return hits


def main():
    parser = argparse.ArgumentParser(description="ATP term drift check for caps_seed.json")
    parser.add_argument("--subject", help="Only check this subject")
    parser.add_argument("--grade", help="Only check this grade")
    parser.add_argument("--sources-dir", help="Read '<Subject> Grade <n>.pdf' files from this directory instead of downloading")
    args = parser.parse_args()

    seed = json.loads(SEED_PATH.read_text(encoding="utf-8"))
    sources = seed.get("_sources", {}).get("documents", {})
    if not sources:
        print("Error: no _sources.documents map in the seed file.")
        return 2

    entries = seed["entries"]
    if args.subject:
        entries = [e for e in entries if e["subject"].lower() == args.subject.lower()]
    if args.grade:
        entries = [e for e in entries if str(e["grade"]) == str(args.grade)]

    needed = sorted({f"{e['subject']} Grade {e['grade']}" for e in entries})
    buckets_by_doc = {}
    for doc in needed:
        if args.sources_dir:
            path = Path(args.sources_dir) / f"{doc}.pdf"
            if not path.exists():
                print(f"[skip] no local file for {doc} ({path})")
                continue
            data = path.read_bytes()
        else:
            url = sources.get(doc)
            if not url:
                print(f"[skip] no source URL recorded for {doc}")
                continue
            try:
                data = fetch_pdf(url)
            except Exception as e:
                print(f"[skip] could not download {doc}: {e}")
                continue
        try:
            buckets_by_doc[doc] = term_buckets(data)
        except Exception as e:
            print(f"[skip] could not parse {doc}: {e}")

    confirmed = drift = unverified = 0
    for e in entries:
        doc = f"{e['subject']} Grade {e['grade']}"
        buckets = buckets_by_doc.get(doc)
        if buckets is None:
            continue
        stated = str(e["term"]).lower()
        found = sorted({t for ws in entry_word_sets(e) for t in terms_containing(ws, buckets)})
        label = f"{doc} | {e['topic']} / {e['subtopic']} (term {stated})"
        if stated in ("all", "unknown"):
            # 'all' and 'unknown' are deliberate; report where the topic shows up
            print(f"INFO       {label} -> appears in terms {found or ['none found']}")
            continue
        if stated in found:
            confirmed += 1
        elif found:
            drift += 1
            print(f"DRIFT      {label} -> found only in term(s) {found}")
        else:
            unverified += 1
            print(f"UNVERIFIED {label}")

    print(f"\nchecked {confirmed + drift + unverified} entries: "
          f"{confirmed} confirmed, {drift} drift, {unverified} unverified "
          f"(ATP edition {seed.get('_sources', {}).get('atp_edition', '?')})")
    return 1 if drift else 0


if __name__ == "__main__":
    sys.exit(main())
