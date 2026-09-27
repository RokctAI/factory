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

"""Build `{subject}/syllabus/grade{10,11,12}.json` for the FET subjects listed
in `fet_sources.json` from their DBE Annual Teaching Plan PDFs.

Every 2023/24 FET ATP is the same landscape grid: a header row of weeks
(TERM n | WEEK 1 .. WEEK 11, in the plan's own language), then rows labelled
in the left column (CAPS topics, concepts/skills, requisite pre-knowledge,
resources, informal assessment, SBA). The extractor works on pdfplumber's
table cells, not on text order:

- week spans come from where a cell sits under the header's week columns;
- a row's role comes from its left-column label, matched against the label
  words the ATPs use in all eleven languages (LABELS below);
- content subjects: each CAPS-topic cell is a topic, and the concept cells
  under the same weeks become its subtopics (one per bullet point);
- languages have no topic row: each two-week skills cell is split on its
  bold headings (Listening for comprehension, Literature study, ...), each
  heading a topic and its bullet lines the subtopics; "Duration: n hours"
  lines become `hours`.

Output files carry `"pipeline_enabled": false`, `parse_status: "extracted"`
(mechanical, spot-checked; not the line-by-line curation the original six
had) and a `pathway` block. Existing syllabus JSON is never overwritten unless
--force is given.

    python3 extract_fet_syllabus.py                 # all subjects in fet_sources.json
    python3 extract_fet_syllabus.py life_sciences   # one subject
    python3 extract_fet_syllabus.py --dump PATH.pdf # print what one PDF yields
"""
import argparse
import datetime
import json
import re
import sys
from pathlib import Path

import pdfplumber

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fet_pathways import PATHWAYS, SUBJECT_NAMES  # noqa: E402

CAPS_DIR = Path(__file__).resolve().parents[2] / "curriculum" / "CAPS"
# Syllabus JSON is built for these; the other eight official languages have
# their CAPS and ATP PDFs on file (fet_sources.json) but no JSON yet, because
# their plans' layouts vary too much for this extractor to read unreviewed.
BUILD_SUBJECTS = {
    "english_home_language", "english_first_additional_language",
    "afrikaans_home_language", "afrikaans_first_additional_language",
    "isizulu_home_language", "isizulu_first_additional_language",
    "life_sciences", "agricultural_sciences", "history", "business_studies",
    "life_orientation", "computer_applications_technology", "information_technology",
    "tourism", "consumer_studies", "engineering_graphics_and_design", "visual_arts",
    "religion_studies",
}
MANIFEST = CAPS_DIR / "fet_sources.json"

# Left-column row labels, in every language DBE writes the FET ATPs in.
# Order matters: the first role whose pattern matches wins.
LABELS = [
    ("ignore", r"INFORMAL|INFORMELE|NGAMISEL|OKUNGANISEL|YEO E SEGO|E SE SONG|NKAMAFUNDZA|"
               r"LE SENG|RESOURCE|BRONNE|IZINSIZA|DITLABAKELO|DIDIRI|SWIPFUNO|OKUNYE OKUBALULEKILE|"
               r"DATE|DATUM|COVERAGE|DEKKING|ACTIVIT|AKTIWITEIT|INVESTIGATION|EXPERIMENT|"
               r"TEACHING TIME|SIGNATURE|HANDTEKENING|REMEDIATION|REMEDI[EË]RING"),
    ("prior", r"PRE-|PRE -|KNOWLEDGE|VOORKENNIS|LWANGAPHAMBILI|LWAPHAMBILI|TSEBO YA PELE|"
              r"VUTIVI BYO RHANGELA|SWILAVEKO SWA VUTIVI|DINYAKE|DINYAKWA|TSEBO E|NDIVHO|"
              r"LWAZI LWA|KWATI|LWATI"),
    ("sba", r"SBA|SGA|FORMAL|FORMELE|OKUMISELWE|OKUBEKELWE|SEMMU|MAKAMBELELO|TEKANYETSO|"
            r"TLHATLHOBO|KUHLOLA|U LINGA|NDINGO|KELO YA"),
    ("topic", r"TOPIC|ONDERWERP|IZIHLOKO|DIHLOGO|TINHLOKOMHAKA|THOHO|SIHLOKO|DITLHOGO|"
              r"SEPHOLEKE|XIPHOKHAMA"),
    ("concept", r"CONCEPT|SKILL|CONTENT|VAARDIGHED|KABV|AMAKHONO|MABOKGONI|VUSWIKOTI|"
                r"BOKGONI|MAKONE|LUSWIKOTI|MAKHONO|LIKHONO|TIKHONO|ZWIKILI|ZWIKILA|"
                r"MANONG|MAKGONI|TOPIC|CAPS"),
]
LABEL_RES = [(role, re.compile(pat)) for role, pat in LABELS]

BULLET_RE = re.compile(r"^\s*(?:[•●▪◦■□➢➤►\-–]|\d{1,2}[.)]\s|[a-z][.)]\s)\s*")
CAPS_REF_RE = re.compile(r"\s*\(?\s*CAPS\s*(?:P(?:AGE|G)?S?\.?|PAGES?|BLADSY|B[LS]\.?)\s*[\d\s,.\-–&]+\)?", re.I)
DURATION_RE = re.compile(r"^(?:Duration|Tydsduur|Duur|Isikhathi|Nako|Nakgwana|Nkarhi|Tshifhinga|Sikhatsi)"
                         r"\s*[:\-]?\s*(\d+(?:[.,]\d+)?)\s*(?:hours?|hrs?|h\b|ure|uur|amahora|diiri|tiawara|"
                         r"iawara|awara|tihora|ihora|mahora)", re.I)
DURATION_ANY_RE = re.compile(DURATION_RE.pattern.lstrip("^"), re.I)
EXAM_RE = re.compile(r"(?i)exam|eksamen|study leave|studieverlof")
WEEK_NUM_RE = re.compile(r"(\d{1,2})(?:\s*[-–&]\s*(\d{1,2}))?")


def clean(text):
    text = (text or "").replace("­", "").replace("", "•").replace("", "•")
    text = re.sub(r"\s+", " ", text)
    return text.strip(" ;,")


def is_bold(word):
    return bool(re.search(r"Bold|Black|Heavy|Semibold|,B\b", word.get("fontname", ""), re.I))


SPLIT_CAP_RE = re.compile(r"^([B-HJ-Z]) ([a-z]{2,})")
_FITZ = {}


def rotated_text(page, bbox):
    """Text of a cell written sideways (the ATPs' vertical 'Revision' columns)."""
    import pymupdf
    path = page.pdf.stream.name
    if path not in _FITZ:
        _FITZ.clear()
        _FITZ[path] = pymupdf.open(path)
    fpage = _FITZ[path][page.page_number - 1]
    return clean(fpage.get_text("text", clip=pymupdf.Rect(*bbox)))


def cell_lines(page, bbox):
    """[(text, bold, x0)] lines inside a cell, top to bottom. A line whose
    leading words are bold and end in ':' is split into a bold heading line
    and a plain line."""
    x0, top, x1, bottom = bbox
    try:
        crop = page.crop((x0 + 0.5, top + 0.5, x1 - 0.5, bottom - 0.5))
    except ValueError:
        return []
    words = crop.extract_words(extra_attrs=["fontname", "size"], keep_blank_chars=False,
                               use_text_flow=False, x_tolerance=1.5)
    words = [w for w in words if w.get("upright", True)]
    lines = []
    for w in sorted(words, key=lambda w: (round(w["top"]), w["x0"])):
        if lines and abs(lines[-1]["top"] - w["top"]) <= 2.5:
            lines[-1]["words"].append(w)
        else:
            lines.append({"top": w["top"], "words": [w]})
    if len(lines) >= 4 and sum(len(" ".join(w["text"] for w in ln["words"])) <= 3
                               for ln in lines) >= 0.7 * len(lines):
        text = rotated_text(page, bbox)
        return [(text, False, x0)] if text else []
    out = []
    for ln in lines:
        ws = sorted(ln["words"], key=lambda w: w["x0"])
        text = clean(" ".join(w["text"] for w in ws))
        if not text:
            continue
        nbold = sum(len(w["text"]) for w in ws if is_bold(w))
        if nbold >= 0.6 * sum(len(w["text"]) for w in ws):
            out.append((text, True, ws[0]["x0"]))
            continue
        lead = 0
        while lead < len(ws) and is_bold(ws[lead]):
            lead += 1
        if 0 < lead < len(ws) and ws[lead - 1]["text"].endswith(":"):
            out.append((clean(" ".join(w["text"] for w in ws[:lead])), True, ws[0]["x0"]))
            out.append((clean(" ".join(w["text"] for w in ws[lead:])), False, ws[lead]["x0"]))
        else:
            out.append((text, False, ws[0]["x0"]))
    return out


def cell_text(page, bbox):
    return clean(" ".join(t for t, _, _ in cell_lines(page, bbox)))


def label_role(label):
    squashed = re.sub(r"\s+", "", label.upper())
    for role, rx in LABEL_RES:
        if rx.search(label.upper()) or rx.search(squashed):
            return role
    return None


def row_role(page, cell, labels, cache):
    """Role of a content cell: the labelled row it overlaps most. Label text is
    often split over several stacked cells, so fragments without a role of
    their own count only when no fragment has one."""
    weight, texts = {}, []
    for lb in sorted(labels, key=lambda b: (b[1], b[0])):
        overlap = min(lb[3], cell[3]) - max(lb[1], cell[1])
        if overlap <= 2:
            continue
        if lb not in cache:
            txt = cell_text(page, lb)
            if not re.search(r"\w", txt):
                txt = ""  # bullets only: a blank label
            cache[lb] = (txt, label_role(txt) if txt else None)
        txt, role = cache[lb]
        if txt:
            texts.append(txt)
        if role:
            weight[role] = weight.get(role, 0) + overlap
    # a cell running down past its own row belongs to the row it starts in
    starts = [cache[lb][1] for lb in labels
              if lb in cache and cache[lb][1] and lb[1] - 1 <= cell[1] + 2 < lb[3]]
    if starts and starts[0] != "ignore":
        return starts[0]
    if weight:
        return max(weight, key=weight.get)
    if texts:
        return label_role(" ".join(texts))
    # only blank label cells beside it: the label printed above runs on
    above = []
    for lb in labels:
        if lb[3] <= cell[1] + 2 and lb in cache and cache[lb][1]:
            above.append(lb)
    if above:
        return cache[max(above, key=lambda b: b[3])][1]
    return "blank"


def header_weeks(page, table):
    """-> (term or None, [(week, x0, x1)], body_start) from the week header
    (the first, second or third table row), or None."""
    for i, row in enumerate(table.rows[:3]):
        hdr = _header_row(page, table, row)
        if hdr:
            return hdr + (i + 1,)
    return None


def _header_row(page, table, row):
    numbered = []
    for c in row.cells:
        if not c:
            continue
        txt = cell_text(page, c)
        m = WEEK_NUM_RE.search(txt)
        if m:
            numbered.append((c, txt, int(m.group(1)), int(m.group(2) or m.group(1))))
    if len(numbered) < 3:
        return None
    # weeks: the longest run at the end whose numbers keep increasing
    start = len(numbered) - 1
    while start > 0 and numbered[start - 1][2] < numbered[start][2]:
        start -= 1
    weeks = numbered[start:]
    if len(weeks) < 3:
        return None
    term = numbered[start - 1][2] if start > 0 else None
    cols = []
    for i, (c, _, a, b) in enumerate(weeks):
        x1 = weeks[i + 1][0][0] if i + 1 < len(weeks) else table.bbox[2]
        span = list(range(a, b + 1))
        width = (x1 - c[0]) / len(span)
        for j, w in enumerate(span):
            cols.append((w, c[0] + j * width, c[0] + (j + 1) * width))
    return term, cols


def weeks_of(bbox, cols):
    x0, _, x1, _ = bbox
    out = []
    for w, a, b in cols:
        overlap = min(x1, b) - max(x0, a)
        if overlap > 0.45 * (b - a):
            out.append(w)
    return sorted(set(out))


def page_term(page):
    """Term number from the page title, e.g. '(TERM 2)', '(KWARTAAL 2)',
    '(IKOTA YOKU-2)', '(KOTARA YA 2)'."""
    head = (page.extract_text() or "")[:500]
    m = re.search(r"\(\s*[A-Za-zÀ-ž]{3,12}(?:\s+(?:YA|YOKU|LA|WA|YE|YO))?[\s\-]*([1-4])\s*\)", head, re.I)
    return int(m.group(1)) if m else None


def extract(pdf_path):
    """-> {term: {"topic": [...], "concept": [...], "prior": [...], "sba": [...]}}"""
    terms = {}
    cur_term, cols = None, None
    page_bottom = None
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page = page.dedupe_chars()  # some plans print each cell's text twice, offset
            pt = page_term(page)
            if pt:
                cur_term = pt
            page_labels = []  # a table split mid-page loses its left column
            carry_role = page_bottom[1] if page_bottom else None
            page_bottom = [0, None]
            for table in page.find_tables():
                if len(table.rows) < 2 or len(table.rows[0].cells) < 6:
                    continue
                hdr = header_weeks(page, table)
                if hdr:
                    t, cols, start = hdr
                    cur_term = pt or t or cur_term
                    body = table.rows[start:]
                elif cols is None:
                    continue
                else:
                    body = table.rows
                if cur_term is None:
                    cur_term = pt or 1
                first_x = cols[0][1]
                label_cache = {}
                cells = []
                seen = set()
                for r in body:
                    for c in r.cells:
                        if c and c not in seen:
                            seen.add(c)
                            cells.append(c)
                labels = [c for c in cells if c[2] <= first_x + 3]
                page_labels.extend(lb for lb in labels if lb not in page_labels)
                labels = page_labels
                content = [c for c in cells if c[2] > first_x + 10]
                for c in content:
                    role = row_role(page, c, labels, label_cache)
                    if role == "blank":
                        # label column left blank: the row carries on from the
                        # bottom row of the page before
                        role = carry_role
                    if role and c[3] >= page_bottom[0]:
                        page_bottom[:] = [c[3], role]
                    if role in (None, "ignore"):
                        continue
                    wks = weeks_of(c, cols)
                    if not wks:
                        continue
                    lines = cell_lines(page, c)
                    if not lines:
                        continue
                    terms.setdefault(cur_term, {"topic": [], "concept": [], "prior": [], "sba": []})
                    terms[cur_term][role].append({"weeks": wks, "lines": lines, "top": c[1], "bottom": c[3],
                                                  "page": page.page_number})
    return terms


JOIN_END_RE = re.compile(
    r"(?i)(?:\b(?:of|the|and|or|to|for|a|an|in|on|with|by|from|at|as|into|refer|e\.g\.|"
    r"van|die|en|om|vir|na|op|met|te|oor|deur|'n|ka|kwa|nga|ukuthi|le|la|ya|wa)|[,/&–-])$")


def items_from_lines(lines):
    """Cell lines -> list of items: a bullet or a new heading starts an item,
    wrapped lines (lower-case start, or a bold heading run over two lines)
    join the item above."""
    items = []
    prev_bold = False
    for text, bold, x0 in lines:
        bullet = BULLET_RE.match(text)
        body = clean(BULLET_RE.sub("", text, count=1)) if bullet else text
        body = clean(body.rstrip("•"))
        if not body:
            continue
        cont = not body[:1].isupper() and not body[:1].isdigit()
        if items and not bullet and (JOIN_END_RE.search(items[-1])
                                     or items[-1].count("(") > items[-1].count(")")):
            cont = True  # the line above stops mid-phrase: "Consolidation of | Grade 9 work"
        if items and not bullet and items[-1].endswith(":") and len(items[-1]) < 40:
            cont = True  # a short lead-in: "Vocabulary: | technical terms ..."
        if bullet or not items:
            new = True
        elif bold and prev_bold:
            new = not cont
        elif bold != prev_bold:
            new = not (cont and not items[-1].endswith((":", ".")))
        else:
            new = not cont
        if new:
            items.append(body)
        else:
            items[-1] = clean(items[-1] + " " + body)
        prev_bold = bold
    return [SPLIT_CAP_RE.sub(r"\1\2", i) for i in items if len(i) > 1]


# Names the PDFs garble (two text runs printed over each other), read by eye
# off the rendered page.
NAME_FIXES = {
    "PRESERN TATION OF BUSINESCSO INNFTORROMLLA TION": "PRESENTATION OF BUSINESS INFORMATION",
    "Domestic, regional Daonmde isnttiecr,n raetgioionnaal l tourism":
        "Domestic, regional and international tourism",
    "THE CONSUMER T": "THE CONSUMER",
    "Map. work and tour planning": "Map work and tour planning",
}


def topic_name(text):
    name = re.sub(r"^[a-z] (?=[A-Z])", "", clean(text))  # stray letter of a sideways cell
    name = CAPS_REF_RE.sub("", name)
    name = re.sub(r"\s*\([^()]*\b(?:PG|P|PAGE|PAGES|BLADSY)\.?\s*\d+[^()]*\)", "", name, flags=re.I)
    name = re.sub(r"\s*\((?:P|p)\.?\s*\d+[\d\s\-–,]*\)", "", name)
    name = clean(name).rstrip(":")
    if re.fullmatch(r"(?:[A-Z] ){3,}[A-Z]", name):
        name = name.replace(" ", "")
    return NAME_FIXES.get(name, name)


def _hours(value):
    return int(value) if value == int(value) else value


def _prior_text(cell):
    txt = clean(" ".join(t for t, _, _ in cell["lines"]))
    txt = re.sub(r"^[•\-\s]+", "", txt).replace(" • ", "; ").replace("•", ";")
    return clean(txt)


def _topic_cells(cells):
    """Topic cells -> [{"name", "weeks"}], merging the pieces pdfplumber splits
    one printed cell into (a truncated copy beside it, a second line below)."""
    topics = []
    for tc in sorted(cells, key=lambda c: (c["weeks"][0], c["page"], c["top"])):
        lines, sub = tc["lines"], []
        if len(" ".join(t for t, _, _ in lines)) > 150 and len(lines) > 3:
            # the topic cell carries the content too (History): the leading
            # bold line(s) name the topic, the rest are its subtopics
            n = 1
            while n < len(lines) and lines[n][1] and lines[0][1] and not lines[n][0][:1].isupper():
                n += 1
            lines, sub = lines[:n], items_from_lines(lines[n:])
        name = topic_name(" ".join(t for t, _, _ in lines))
        if not name:
            continue
        if any(set(t["weeks"]) & set(tc["weeks"]) and name.upper() in t["name"].upper()
               for t in topics[-4:]) and not sub:
            continue  # a clipped copy or a wrapped line of a cell already read
        if topics:
            prev = topics[-1]
            pu, nu = prev["name"].upper(), name.upper()
            touching = set(tc["weeks"]) & set(prev["weeks"]) or tc["weeks"][0] == prev["weeks"][-1] + 1
            if touching and (pu.startswith(nu) or nu.startswith(pu) or pu.endswith(nu)):
                prev["weeks"] = sorted(set(prev["weeks"]) | set(tc["weeks"]))
                if len(name) > len(prev["name"]):
                    prev["name"] = name
                continue
            if tc["weeks"] == prev["weeks"] and tc["page"] == prev["page"] \
                    and 0 <= tc["top"] - prev["bottom"] < 4:
                prev["name"] = clean(prev["name"] + " " + name)
                prev["bottom"] = tc["bottom"]
                continue
        topics.append({"name": name, "weeks": list(tc["weeks"]), "page": tc["page"],
                       "bottom": tc["bottom"], "_sub": sub})
    return topics


def _finish_topic(t):
    subs = list(dict.fromkeys(s for s in t.get("_sub", []) if s))
    hours = None
    keep = []
    for s in subs:
        m = DURATION_RE.match(s)
        if m:
            hours = (hours or 0) + float(m.group(1).replace(",", "."))
        else:
            keep.append(s)
    topic = {"name": t["name"]}
    if keep and not EXAM_RE.search(t["name"]):  # exam blocks list paper tables, not content
        topic["subtopics"] = keep
    if t.get("prior_knowledge"):
        topic["prior_knowledge"] = t["prior_knowledge"]
    topic["weeks"] = t["weeks"]
    if hours:
        topic["hours"] = _hours(hours)
    return topic


def build_content_terms(raw):
    """Topics from the CAPS-topic row, subtopics from the concept cells under them."""
    out = []
    for term in sorted(raw):
        r = raw[term]
        topics = _topic_cells(r["topic"])
        if not topics:
            # no CAPS-topic row this term: read its cells like a language plan
            out.extend(build_language_terms({term: r}))
            continue
        extra = []
        for cc in r["concept"]:
            owners = [t for t in topics if set(cc["weeks"]) & set(t["weeks"])]
            items = items_from_lines(cc["lines"])
            if not owners:
                # a cell under no topic (a revision/exam column): its own entry
                if items:
                    extra.append({"name": topic_name(items[0]), "weeks": list(cc["weeks"]),
                                  "_sub": items[1:]})
                continue
            owner = max(owners, key=lambda t: (len(set(cc["weeks"]) & set(t["weeks"])),
                                               -abs(t["weeks"][0] - cc["weeks"][0])))
            owner.setdefault("_sub", []).extend(items)
        for pc in r["prior"]:
            owners = [t for t in topics if set(pc["weeks"]) & set(t["weeks"])]
            txt = _prior_text(pc)
            if not owners or not txt:
                continue
            owner = max(owners, key=lambda t: len(set(pc["weeks"]) & set(t["weeks"])))
            if txt not in owner.get("prior_knowledge", ""):
                owner["prior_knowledge"] = clean(
                    (owner.get("prior_knowledge", "") + "; " + txt).strip("; "))
        allt = sorted(topics + extra, key=lambda t: t["weeks"][0])
        term_obj = {"term": term, "topics": tidy_topics([_finish_topic(t) for t in allt if t["name"]])}
        sba = sba_items(r["sba"])
        if sba:
            term_obj["sba"] = sba
        out.append(term_obj)
    return out


def is_legend(cell):
    text = " ".join(t for t, _, _ in cell["lines"])
    if len(text) >= 200:
        return False
    if len(cell["weeks"]) >= 8 and len(text) < 150:
        return True
    return len(cell["weeks"]) >= 3 and len(text) < 120 \
        and len(re.findall(r"(?:^|\s)[1-4]\s*\.", text)) >= 2


def skills_legend(raw):
    """{1: 'Listening and speaking', ...} from the plan's legend row(s)."""
    legend = {}
    for term in sorted(raw):
        for cc in raw[term]["concept"] + raw[term]["topic"]:
            text = " ".join(t for t, _, _ in cc["lines"])
            if is_legend(cc):
                for n, name in re.findall(r"([1-4])\s*\.\s*(.+?)(?=\s+[1-4]\s*\.|$)", text):
                    legend.setdefault(int(n), clean(name))
    return legend


def build_language_terms(raw, legend=None):
    """Skills cells split on their bold headings: each heading is a topic."""
    legend = skills_legend(raw) if legend is None else legend
    out = []
    for term in sorted(raw):
        r = raw[term]
        cells = sorted(r["concept"] + r["topic"], key=lambda c: (c["weeks"][0], c["page"], c["top"]))
        topics = []
        for cc in cells:
            if is_legend(cc):
                continue  # the skills legend row ("1. Listening ... 4. Language")
            first = cc["lines"][0][0] if cc["lines"] else ""
            m = re.match(r"^\s*([1-4])\s*\.\s*(.*)$", first)
            if m and int(m.group(1)) in legend:
                # skill cells numbered as in the legend row; one cell may hold
                # several numbered skills one under the other
                topic = None
                for text, bold, x0 in cc["lines"]:
                    m = re.match(r"^\s*([1-4])\s*\.\s*(.*)$", text)
                    if m and int(m.group(1)) in legend:
                        skill = legend[int(m.group(1))]
                        topic = {"name": skill, "weeks": list(cc["weeks"]), "_lines": []}
                        topics.append(topic)
                        text = re.sub(r"\s*\d\s*\.\s*$", "", m.group(2))
                        if clean(text).lower().rstrip(":") == skill.lower() or not clean(text):
                            continue
                    dur = DURATION_ANY_RE.search(text)
                    if dur:
                        topic["hours"] = topic.get("hours", 0) + float(dur.group(1).replace(",", "."))
                        text = clean(DURATION_ANY_RE.sub("", text))
                    if clean(text):
                        topic["_lines"].append((text, bold, x0))
                continue
            cur, prev_bold = None, False
            for text, bold, x0 in cc["lines"]:
                dur = DURATION_ANY_RE.search(text)
                if dur:
                    if cur is not None:
                        cur["hours"] = cur.get("hours", 0) + float(dur.group(1).replace(",", "."))
                    text = clean(DURATION_ANY_RE.sub("", text))
                    if not re.sub(r"[•\-\s]", "", text):
                        prev_bold = False
                        continue
                bullet = BULLET_RE.match(text)
                body = clean(BULLET_RE.sub("", text, count=1)) if bullet else text
                if not body:
                    continue
                if bold and not bullet and cur is not None and prev_bold \
                        and not body[:1].isupper() and not body[:1].isdigit():
                    # a bold line wrapped onto the next line
                    if cur["_lines"]:
                        t0, b0, x00 = cur["_lines"][-1]
                        cur["_lines"][-1] = (clean(t0 + " " + body), b0, x00)
                    else:
                        cur["name"] = clean(cur["name"] + " " + body)
                    continue
                prev_bold = bold
                if bold and not bullet:
                    head, _, tail = body.partition(":")
                    split = bool(tail.strip()) and len(head) < 60
                    name = clean(head) if split else body.rstrip(":")
                    if cur is not None and not cur["_lines"] and not cur.get("hours") \
                            and cur["weeks"] == list(cc["weeks"]):
                        # a heading with nothing under it introduces the next one
                        cur["name"] = f"{cur['name']}: {name}"
                    else:
                        cur = {"name": name, "weeks": list(cc["weeks"]), "_lines": []}
                        topics.append(cur)
                    if split:
                        cur["_lines"].append((clean(tail), False, x0))
                    continue
                if cur is None:
                    cur = {"name": body.rstrip(":"), "weeks": list(cc["weeks"]), "_lines": []}
                    topics.append(cur)
                    continue
                cur["_lines"].append((text, bold, x0))
        prior = {}
        for pc in r["prior"]:
            txt = _prior_text(pc)
            if txt:
                prior.setdefault(tuple(pc["weeks"]), []).append(txt)
        term_obj = {"term": term, "topics": []}
        for t in topics:
            topic = {"name": topic_name(t["name"])}
            if not topic["name"]:
                continue
            subs = items_from_lines(t["_lines"])
            if subs:
                topic["subtopics"] = list(dict.fromkeys(subs))
            pk = [v for k, vs in prior.items() if set(k) & set(t["weeks"]) for v in vs]
            if pk:
                topic["prior_knowledge"] = "; ".join(dict.fromkeys(pk))
            topic["weeks"] = t["weeks"]
            if t.get("hours"):
                topic["hours"] = _hours(t["hours"])
            term_obj["topics"].append(topic)
        term_obj["topics"] = tidy_topics(term_obj["topics"], merge_repeats=False)
        sba = sba_items(r["sba"])
        if sba:
            term_obj["sba"] = sba
        out.append(term_obj)
    return out


def tidy_topics(topics, merge_repeats=True):
    """Rule-based clean-up of what the grid yields: bullet fragments and
    'OR' lines that pdfplumber split off a topic cell rejoin the topic above,
    over-long names keep their first clause (the rest become subtopics), and
    repeated cells (same name, same weeks) collapse."""
    out = []
    for t in topics:
        name = t["name"]
        if out and (name[:1] in "•[(" or name[:1].islower() or name.upper() in ("OR", "AND", "EN", "OF")):
            prev = out[-1]
            extra = [clean(x) for x in name.split("•") if clean(x) and clean(x).upper() != "OR"]
            prev.setdefault("subtopics", []).extend(extra + t.get("subtopics", []))
            continue
        if len(name) > 110:
            parts = [clean(x) for x in name.split("•") if clean(x)]
            head, rest = parts[0], parts[1:]
            if len(head) > 110:
                m = re.search(r"^(.{12,110}?)(?::|\.|;| – | - )\s+(.*)$", head)
                if m:
                    head, rest = m.group(1), [m.group(2)] + rest
                else:
                    cut = head.rfind(" ", 0, 110)
                    head, rest = head[:cut], [head[cut + 1:]] + rest
            t["name"] = head
            if rest:
                t["subtopics"] = rest + t.get("subtopics", [])
        dup = next((o for o in out if o["weeks"] == t["weeks"]
                    and (o["name"].upper() in t["name"].upper() or t["name"].upper() in o["name"].upper())
                    and not t.get("subtopics")), None)
        if dup:
            continue
        out.append(t)
    merged = []
    for t in out:
        prev = merged[-1] if merged else None
        if merge_repeats and prev and prev["name"].upper() == t["name"].upper() \
                and t["weeks"][0] <= prev["weeks"][-1] + 1:
            # the plan repeats one topic week by week: one topic over the span
            prev["weeks"] = sorted(set(prev["weeks"]) | set(t["weeks"]))
            if t.get("subtopics"):
                prev.setdefault("subtopics", []).extend(t["subtopics"])
            if t.get("hours"):
                prev["hours"] = prev.get("hours", 0) + t["hours"]
            if t.get("prior_knowledge") and t["prior_knowledge"] not in prev.get("prior_knowledge", ""):
                prev["prior_knowledge"] = clean(
                    (prev.get("prior_knowledge", "") + "; " + t["prior_knowledge"]).strip("; "))
            continue
        merged.append(t)
    out = merged
    for t in out:
        if "subtopics" in t:
            t["subtopics"] = list(dict.fromkeys(t["subtopics"]))
            # keep key order: name, subtopics, prior_knowledge, weeks, hours
            order = ["name", "subtopics", "prior_knowledge", "weeks", "hours"]
            items = sorted(t.items(), key=lambda kv: order.index(kv[0]) if kv[0] in order else 9)
            t.clear()
            t.update(items)
    return out


def sba_items(cells):
    """SBA cells grouped by the weeks they sit under, read top to bottom."""
    groups = {}
    for sc in sorted(cells, key=lambda c: (c["page"], c["weeks"][0], c["top"])):
        txt = clean(" ".join(t for t, _, _ in sc["lines"]))
        txt = clean(txt.replace(" • ", "; ").replace("•", " ").strip("; "))
        if txt:
            groups.setdefault((sc["page"], tuple(sc["weeks"])), []).append(txt)
    items = []
    for parts in groups.values():
        txt = ""
        for part in parts:
            if part not in txt:
                txt = clean(txt + " " + part)
        if len(txt) > 2 and txt not in items:
            items.append(txt)
    return items



def build(subject_folder, grade, entry, today):
    pdf = CAPS_DIR / entry["path"]
    raw = extract(pdf)
    language = subject_folder.endswith("_language")
    terms = build_language_terms(raw) if language else build_content_terms(raw)
    data = {
        "subject": SUBJECT_NAMES[subject_folder],
        "grade": grade,
        "curriculum": "CAPS",
        "phase": "FET",
        "atp_edition": entry.get("edition") or "2023/24",
        "source_verified": today,
        "source_url": entry["source_url"],
        "source_path": [f"lessons/curriculum/CAPS/{entry['path']}"],
        "parse_status": "extracted",
        "pipeline_enabled": False,
        "pathway": PATHWAYS[subject_folder](grade),
        "terms": terms,
    }
    return data


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("subjects", nargs="*")
    ap.add_argument("--force", action="store_true", help="overwrite existing syllabus JSON")
    ap.add_argument("--dump", type=Path, help="print the raw extraction of one PDF")
    args = ap.parse_args()
    if args.dump:
        raw = extract(args.dump)
        for term in sorted(raw):
            for role, cells in raw[term].items():
                for c in cells:
                    print(term, role, c["weeks"], " | ".join(("*" if b else "") + t for t, b, _ in c["lines"])[:300])
        return 0
    man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    today = datetime.date.today().isoformat()
    for entry in man["files"]:
        if entry["kind"] != "atp" or entry["subject"] not in BUILD_SUBJECTS \
                or (args.subjects and entry["subject"] not in args.subjects):
            continue
        target = CAPS_DIR / entry["subject"] / "syllabus" / f"grade{entry['grade']}.json"
        if target.exists() and not args.force:
            continue
        data = build(entry["subject"], entry["grade"], entry, today)
        target.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        ntop = sum(len(t["topics"]) for t in data["terms"])
        nsub = sum(len(tp.get("subtopics", [])) for t in data["terms"] for tp in t["topics"])
        print(f"{target.relative_to(CAPS_DIR)}: {len(data['terms'])} terms, {ntop} topics, {nsub} subtopics")
    return 0


if __name__ == "__main__":
    sys.exit(main())
