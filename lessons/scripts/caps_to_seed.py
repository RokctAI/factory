#!/usr/bin/env python3
# Licensed under the MIT License.
# Copyright 2026 RokctAI
"""Point Level 0 at the real syllabus: flatten lessons/curriculum/CAPS/ into
caps_seed.json rows.

lessons/curriculum/CAPS/{subject}/syllabus/{grade}.json (curated from the DBE
ATP PDFs) is the source of truth for what may be taught. caps_seed.json stays
the pipeline-facing artifact Level 0 reads (lesson_pipeline.py cmd_seed), so
this script maps one onto the other instead of rewiring the pipeline:

  CAPS topic            -> seed `topic`
  CAPS subtopic         -> seed `subtopic` (one row per subtopic)
  CAPS prior_knowledge  -> seed `prior_knowledge` (topic-level, copied to rows)
  CAPS term             -> seed `term`
  subject folder        -> seed `type` (lesson.<type>) via TYPE_BY_FOLDER

Policy (deliberate, do not "clean up"):
  - Existing seed entries are preserved byte-for-byte. Open cards and the
    dashboard's opened/remaining counts key off them; rewriting or deleting
    rows mid-flight would orphan both.
  - New rows are appended only when no existing row already covers the same
    content: exact (type, grade, topic, subtopic) match OR fuzzy token overlap
    (Jaccard/containment) within the same (type, grade). The old hand-written
    rows word topics differently from the ATP text ("Quadratic Equations /
    Factoring method" vs "Equations and inequalities / Solve quadratic
    equations by factorisation..."), and Level 0's own duplicate check is
    exact-tuple only, so without the fuzzy gate we would open twin cards.
  - Revision/exam/assessment/consolidation topics never become lesson rows.
  - New rows carry no example_problem/tutor (both optional in cmd_seed;
    Level 1 recommends a tutor and derives the worked example).
  - Each appended row carries source: the CAPS file it came from.

Run --dry-run first; --apply rewrites caps_seed.json in place.
"""

import argparse
import json
import re
from pathlib import Path

CAPS_DIR = Path("lessons/curriculum/CAPS")
SEED_PATH = Path("lessons/curriculum/caps_seed.json")

TYPE_BY_FOLDER = {
    "maths": "lesson.maths",
    "mathematical_literacy": "lesson.maths_literacy",
    "physical_sciences": "lesson.physical_sciences",
    "economics": "lesson.economics",
    "geography": "lesson.geography",
    "accounting": "lesson.accounting",
}

NON_LESSON_TOPIC = re.compile(
    r"(?i)revision|revise|examination|exam\b|control test|controlled test|"
    r"consolidation|assessment|remediation|discussion|admin\b|prior knowledge"
)

STOPWORDS = {
    "the", "a", "an", "of", "and", "or", "to", "in", "on", "for", "with",
    "using", "use", "incl", "including", "etc", "vs", "via", "per", "by",
}


def _stem(w):
    # Light suffix stripping so "completing"/"complete", "equations"/"equation"
    # compare equal. Not linguistic stemming - just enough for dedupe.
    for suf in ("ing", "es", "ed"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            w = w[: -len(suf)]
            break
    if w.endswith("s") and len(w) > 3:
        w = w[:-1]
    if w.endswith("e") and len(w) > 4:
        w = w[:-1]
    return w


def tokens(*parts):
    text = " ".join(str(p) for p in parts).lower()
    return {
        _stem(t)
        for t in re.findall(r"[a-z]+", text)
        if len(t) > 2 and t not in STOPWORDS
    }


def covered(new_row, existing_rows_by_key, existing_tokens):
    key = (new_row["type"], str(new_row["grade"]))
    exact = (
        new_row["type"], str(new_row["grade"]),
        new_row["topic"].strip().lower(), new_row["subtopic"].strip().lower(),
    )
    if exact in existing_rows_by_key:
        return "exact"
    new_toks = tokens(new_row["topic"], new_row["subtopic"])
    if not new_toks:
        return "empty"
    for old_toks in existing_tokens.get(key, []):
        inter = len(new_toks & old_toks)
        union = len(new_toks | old_toks)
        smaller = min(len(new_toks), len(old_toks))
        if union and inter / union >= 0.5:
            return "fuzzy"
        if smaller and inter / smaller >= 0.7:
            return "fuzzy"
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="report only")
    mode.add_argument("--apply", action="store_true", help="rewrite caps_seed.json")
    args = parser.parse_args()

    seed = json.loads(SEED_PATH.read_text(encoding="utf-8"))
    entries = seed.get("entries", [])

    existing_rows_by_key = {}
    existing_tokens = {}
    for e in entries:
        exact = (
            e.get("type", ""), str(e.get("grade", "")),
            str(e.get("topic", "")).strip().lower(),
            str(e.get("subtopic", "")).strip().lower(),
        )
        existing_rows_by_key[exact] = e
        existing_tokens.setdefault((e.get("type", ""), str(e.get("grade", ""))), []).append(
            tokens(e.get("topic", ""), e.get("subtopic", ""))
        )

    added, skipped_exact, skipped_fuzzy, skipped_nonlesson = [], 0, 0, 0
    for folder, lesson_type in sorted(TYPE_BY_FOLDER.items()):
        for grade_file in sorted((CAPS_DIR / folder / "syllabus").glob("grade*.json")):
            data = json.loads(grade_file.read_text(encoding="utf-8"))
            rel = grade_file.as_posix()
            for term in data.get("terms", []):
                for topic in term.get("topics", []):
                    name = topic["name"]
                    subs = topic.get("subtopics") or []
                    if NON_LESSON_TOPIC.search(name) or not subs:
                        if subs:
                            skipped_nonlesson += len(subs)
                        continue
                    for sub in subs:
                        row = {
                            "type": lesson_type,
                            "subject": data["subject"],
                            "grade": data["grade"],
                            "term": str(term["term"]),
                            "topic": name,
                            "subtopic": sub,
                            "source": rel,
                        }
                        pk = topic.get("prior_knowledge")
                        if pk:
                            row["prior_knowledge"] = pk
                        verdict = covered(row, existing_rows_by_key, existing_tokens)
                        if verdict == "exact":
                            skipped_exact += 1
                        elif verdict == "fuzzy":
                            skipped_fuzzy += 1
                        else:
                            added.append(row)
                            key = (row["type"], str(row["grade"]))
                            existing_tokens.setdefault(key, []).append(
                                tokens(row["topic"], row["subtopic"])
                            )

    per_type = {}
    for r in added:
        k = f"{r['type']} g{r['grade']}"
        per_type[k] = per_type.get(k, 0) + 1
    print(f"existing rows: {len(entries)}")
    print(f"rows to add:   {len(added)}")
    print(f"skipped: {skipped_fuzzy} fuzzy-covered, {skipped_exact} exact, "
          f"{skipped_nonlesson} revision/assessment subtopics")
    for k in sorted(per_type):
        print(f"  + {per_type[k]:3d}  {k}")

    if args.apply:
        seed["entries"] = entries + added
        SEED_PATH.write_text(
            json.dumps(seed, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        print(f"written {SEED_PATH} ({len(seed['entries'])} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
