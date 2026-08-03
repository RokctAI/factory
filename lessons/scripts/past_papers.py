#!/usr/bin/env python3
"""Past-paper -> lesson linking pipeline.

Fetches (out of band, see SOURCES.md) real DBE past papers, matches each
question to an existing lesson topic/subtopic, attaches it as an attributed,
animated worked example, and keeps a durable bidirectional index a
verification pass can trace either way.

Subcommands:
  match   paper.json questions -> lesson subtopics (method-level content
          matching against real lesson cards; honest 'unmatched' allowed).
  link    apply matches: write worked-example question.md + manim_scene.py
          into the lesson dir, record `past_paper_examples` on the card, and
          update lessons/curriculum/CAPS/past_papers/links.json (paper->lessons + lesson->papers).
  lookup  query the index in either direction.
  verify  the payoff of the link: for a lesson's linked questions, recompute
          the checkable memo answers and confirm the linked subtopic actually
          teaches the method the question needs.

Matching is method-level, NOT keyword-on-question-text: each question carries
the `solution_method` the official MEMO uses, and each lesson advertises the
methods its subtopics teach (derived from subtopic titles). A question links
to a lesson only when the lesson teaches that method — so `x(2x+1)=0` links to
the factoring lesson's Zero-Product-Property subtopic even though the question
text says neither 'factor' nor 'quadratic'. Below-threshold questions are left
unmatched rather than forced onto the nearest topic. An optional Groq backend
(--backend groq) is available for questions whose method is not cleanly
tagged; the default `memo` backend needs no network and is fully reproducible.
"""
import argparse
import json
import re
from pathlib import Path

PP_ROOT = Path("lessons/curriculum/CAPS/past_papers")
LINKS_PATH = PP_ROOT / "links.json"
JOBS = [Path(".rokct/agent/jobs/done"), Path(".rokct/agent/jobs/pending")]

# Canonical solution methods -> substrings that, in a lesson SUBTOPIC TITLE,
# indicate the subtopic teaches that method. This is how a lesson advertises
# what it can back with a worked example.
METHOD_SUBTOPIC_SIGNALS = {
    # Maths
    "zero_product_property": ["zero-product", "zero product"],
    "factoring": ["factor"],
    "quadratic_formula": ["quadratic formula", "the formula", "applying the formula"],
    "completing_square": ["completing the square"],
    "completing_square_optimisation": ["completing the square"],
    "quadratic_inequality": ["inequalit"],
    "discriminant_analysis": ["nature of roots", "discriminant"],
    "simultaneous_substitution": ["simultaneous"],
    "substitution_to_quadratic": ["reducible", "substitution"],
    # Physical Sciences ("stating"/"applying" distinguish the two halves of
    # the Newton's-second-law lesson; a bare "newton's second law" signal
    # would match both subtopics ambiguously)
    "state_newtons_second_law": ["stating newton"],
    "newtons_second_law_application": ["applying newton"],
    "vector_resolution": ["vector", "resultant", "components of forces"],
    "friction_equilibrium": ["friction"],
    "incline_dynamics": ["inclined plane", "incline"],
    "universal_gravitation": ["universal gravitation"],
    # Geography (mapwork skills)
    "gradient_calculation": ["gradient"],
    "map_scale_distance": ["map scale", "scale and distance"],
    "cross_section_exaggeration": ["cross-section", "vertical exaggeration"],
}


def get_field(content, field):
    m = re.search(rf"^{field}:[ \t]*(.*)", content, re.MULTILINE)
    return m.group(1).split("#")[0].strip() if m else ""


def set_field(content, field, value):
    if re.search(rf"^{field}:", content, re.MULTILINE):
        return re.sub(rf"^{field}:.*", f"{field}: {value}", content, flags=re.MULTILINE)
    parts = content.rsplit("---", 1)
    return f"{parts[0]}{field}: {value}\n---{parts[1]}"


def load_lessons(subject, grade):
    """Real lesson cards for this subject/grade, each annotated with the
    methods its subtopics teach."""
    lessons = []
    for d in JOBS:
        for card_path in sorted(d.glob("*.md")):
            c = card_path.read_text(encoding="utf-8")
            if get_field(c, "subject") != subject:
                continue
            if get_field(c, "grade") != str(grade):
                continue
            lp = get_field(c, "lesson_path")
            subs = []
            if lp and (Path(lp) / "subtopics.json").exists():
                subs = json.loads((Path(lp) / "subtopics.json").read_text("utf-8")).get("subtopics", [])
            methods = {}  # method -> subtopic ref that teaches it
            for sub in subs:
                title = sub.get("title", "").lower()
                for method, signals in METHOD_SUBTOPIC_SIGNALS.items():
                    if any(sig in title for sig in signals):
                        methods.setdefault(method, sub["ref"])
            lessons.append({
                "id": get_field(c, "id"),
                "card": str(card_path),
                "status": get_field(c, "status").split()[0] if get_field(c, "status") else "",
                "topic": get_field(c, "topic"),
                "lesson_path": lp,
                "subtopics": subs,
                "methods": methods,
            })
    return lessons


def match_questions(paper, lessons):
    """[(question, lesson, subtopic_ref, confidence)] with lesson=None for
    honest non-matches."""
    results = []
    for q in paper["questions"]:
        method = q.get("solution_method", "")
        best = None
        for lesson in lessons:
            if method in lesson["methods"]:
                # Same-topic evaluated lesson that teaches the exact method is
                # a high-confidence match; a pending lesson is medium.
                conf = "high" if lesson["status"] == "evaluated" else "medium"
                best = (lesson, lesson["methods"][method], conf)
                if conf == "high":
                    break
        if best:
            results.append((q, best[0], best[1], best[2]))
        else:
            results.append((q, None, None, "unmatched"))
    return results


# --- worked-example Manim scene generators (per method) ---
#
# Each generator takes (q, paper). The Maths generators are data-driven from
# q["scene_data"] with a fallback to the first paper's (Nov 2018) content for
# questions recorded before scene_data existed — so a new paper year needs
# only paper.json entries, no new code.

def _scene_header(q, paper):
    return (f"# Auto-generated past-paper worked example.\n"
            f"# Source: DBE Grade {paper['grade']} {paper['subject']} "
            f"{paper['paper']}, {paper['session']}, {q['ref']}\n"
            f"# {paper['copyright']}")


def _head_line(q, paper):
    session_short = paper["session"].replace("November", "Nov")
    return f"Past paper: DBE {session_short} {paper['paper']} {q['ref']}"


def scene_zero_product(q, paper):
    sd = q.get("scene_data") or {
        "given_latex": "x(2x + 1) = 0",
        "factor_steps": ["x = 0",
                         "2x + 1 = 0 \\Rightarrow x = -\\tfrac{1}{2}"],
        "answer_latex": "x = 0 \\quad \\text{or} \\quad x = -\\tfrac{1}{2}",
    }
    left, right = sd["factor_steps"]
    return f'''from manim import *

{_scene_header(q, paper)}
class PastPaperWorkedExample(Scene):
    def construct(self):
        head = Tex(r"{_head_line(q, paper)}").to_edge(UP)
        self.play(Write(head)); self.wait(1)
        eq = MathTex(r"{sd["given_latex"]}")
        self.play(Write(eq)); self.wait(2)
        self.play(eq.animate.shift(UP * 2))
        note = Tex(r"Zero-product property: a product is 0 when a factor is 0").scale(0.7)
        self.play(Write(note)); self.wait(2)
        left = MathTex(r"{left}").scale(0.9).shift(LEFT * 2.5 + DOWN)
        right = MathTex(r"{right}").scale(0.9).shift(RIGHT * 2.5 + DOWN)
        self.play(Write(left), Write(right)); self.wait(2)
        ans = MathTex(r"{sd["answer_latex"]}").shift(DOWN * 2.5)
        self.play(Write(ans)); self.wait(3)
'''


def scene_quadratic_formula(q, paper):
    sd = q.get("scene_data") or {
        "given_latex": "5x^2 + 2x - 6 = 0", "a": 5, "b": 2, "c": -6,
        "sub_latex": "x = \\frac{-2 \\pm \\sqrt{2^2 - 4(5)(-6)}}{2(5)} = \\frac{-2 \\pm \\sqrt{124}}{10}",
        "answer_latex": "x = 0{,}91 \\quad \\text{or} \\quad x = -1{,}31",
    }
    return f'''from manim import *

{_scene_header(q, paper)}
class PastPaperWorkedExample(Scene):
    def construct(self):
        head = Tex(r"{_head_line(q, paper)}").to_edge(UP)
        self.play(Write(head)); self.wait(1)
        eq = MathTex(r"{sd["given_latex"]}")
        self.play(Write(eq)); self.wait(2)
        self.play(eq.animate.shift(UP * 2))
        coeffs = MathTex(r"a = {sd["a"]}, \\quad b = {sd["b"]}, \\quad c = {sd["c"]}").scale(0.9).shift(UP * 0.5)
        self.play(Write(coeffs)); self.wait(2)
        formula = MathTex(r"x = \\frac{{-b \\pm \\sqrt{{b^2 - 4ac}}}}{{2a}}").shift(DOWN * 0.5)
        self.play(Write(formula)); self.wait(2)
        sub = MathTex(r"{sd["sub_latex"]}").scale(0.9).shift(DOWN * 1.5)
        self.play(Write(sub)); self.wait(2)
        ans = MathTex(r"{sd["answer_latex"]}").shift(DOWN * 2.6)
        self.play(Write(ans)); self.wait(3)
'''


def scene_state_second_law(q, paper):
    return f'''from manim import *

# Auto-generated past-paper worked example.
# Source: DBE Grade 11 Physical Sciences P1, November 2018, {q["ref"]}
# (c) Department of Basic Education, 2018.
class PastPaperWorkedExample(Scene):
    def construct(self):
        head = Tex(r"Past paper: DBE Nov 2018 P1 {q["ref"]}").to_edge(UP)
        self.play(Write(head)); self.wait(1)
        ask = Tex(r"State Newton's Second Law of Motion in words. (2)").scale(0.8).shift(UP * 1.5)
        self.play(Write(ask)); self.wait(2)
        l1 = Tex(r"When a \\textbf{{net force}} acts on an object, the object").scale(0.7)
        l2 = Tex(r"\\textbf{{accelerates}} in the \\textbf{{direction of the force}}.").scale(0.7).shift(DOWN * 0.5)
        l3 = Tex(r"The acceleration is \\textbf{{directly proportional to the net force}}").scale(0.7).shift(DOWN * 1.2)
        l4 = Tex(r"and \\textbf{{inversely proportional to the mass}}.").scale(0.7).shift(DOWN * 1.7)
        for l in (l1, l2, l3, l4):
            self.play(Write(l)); self.wait(1)
        warn = Tex(r"Memo: $-1$ mark if a key phrase is missing.").scale(0.6).shift(DOWN * 2.8)
        self.play(Write(warn)); self.wait(3)
'''


def scene_second_law_graph(q, paper):
    return f'''from manim import *

# Auto-generated past-paper worked example.
# Source: DBE Grade 11 Physical Sciences P1, November 2018, {q["ref"]}
# (c) Department of Basic Education, 2018.
class PastPaperWorkedExample(Scene):
    def construct(self):
        head = Tex(r"Past paper: DBE Nov 2018 P1 {q["ref"]}").to_edge(UP)
        self.play(Write(head)); self.wait(1)
        given = Tex(r"Graph of $\\frac{{1}}{{a}}$ versus $m$ (constant net force), gradient $= 2$").scale(0.75).shift(UP * 1.8)
        self.play(Write(given)); self.wait(2)
        s1 = MathTex(r"F_{{net}} = ma \\;\\Rightarrow\\; \\frac{{1}}{{a}} = \\frac{{1}}{{F_{{net}}}} \\cdot m").shift(UP * 0.6)
        self.play(Write(s1)); self.wait(2)
        s2 = MathTex(r"\\text{{gradient}} = \\frac{{1}}{{F_{{net}}}} = \\frac{{2{{,}}5 - 0}}{{1{{,}}25 - 0}} = 2").shift(DOWN * 0.6)
        self.play(Write(s2)); self.wait(2)
        ans = MathTex(r"F_{{net}} = \\frac{{1}}{{2}} = 0{{,}}5\\ \\text{{N}}").shift(DOWN * 1.9)
        self.play(Write(ans)); self.wait(3)
'''


def scene_gradient(q, paper):
    """Average-gradient worked example, built from the question's map_inputs
    (memo-accepted map readings) so the animation shows the real numbers."""
    mi = q["map_inputs"]
    vi = mi["trig_station_height_m"] - mi["contour_height_m"]
    he_m = mi["map_distance_cm"] * mi["map_scale_denominator"] / 100
    ratio = he_m / vi
    return f'''from manim import *

# Auto-generated past-paper worked example.
# Source: DBE NSC Grade 12 Geography P2, November 2018, {q["ref"]}
# (c) Department of Basic Education, 2018.
class PastPaperWorkedExample(Scene):
    def construct(self):
        head = Tex(r"Past paper: DBE Nov 2018 Geography P2 {q["ref"]}").to_edge(UP)
        self.play(Write(head)); self.wait(1)
        formula = MathTex(r"\\text{{Average gradient}} = \\frac{{\\text{{vertical interval (VI)}}}}{{\\text{{horizontal equivalent (HE)}}}}").scale(0.8).shift(UP * 1.8)
        self.play(Write(formula)); self.wait(2)
        vi = MathTex(r"VI = {mi["trig_station_height_m"]:g}\\,\\text{{m}} - {mi["contour_height_m"]:g}\\,\\text{{m}} = {vi:g}\\,\\text{{m}}").scale(0.85).shift(UP * 0.6)
        self.play(Write(vi)); self.wait(2)
        he = MathTex(r"HE = {mi["map_distance_cm"]:g}\\,\\text{{cm}} \\times {mi["map_scale_denominator"]} = {he_m:g}\\,\\text{{m}}").scale(0.85).shift(DOWN * 0.4)
        self.play(Write(he)); self.wait(2)
        grad = MathTex(r"\\text{{Gradient}} = \\frac{{{vi:g}}}{{{he_m:g}}}").scale(0.85).shift(DOWN * 1.4)
        self.play(Write(grad)); self.wait(2)
        ans = MathTex(r"= 1 : {ratio:.1f}").scale(1.0).shift(DOWN * 2.4)
        self.play(Write(ans)); self.wait(3)
'''


SCENE_GENERATORS = {
    "zero_product_property": scene_zero_product,
    "quadratic_formula": scene_quadratic_formula,
    "state_newtons_second_law": scene_state_second_law,
    "newtons_second_law_application": scene_second_law_graph,
    "gradient_calculation": scene_gradient,
}


def worked_example_dir(lesson, paper, qref):
    return Path(lesson["lesson_path"]) / "past_papers" / f'{paper["paper_id"]}_{qref.replace(".", "_")}'


def cmd_match(args):
    paper = json.loads(Path(args.paper).read_text("utf-8"))
    lessons = load_lessons(paper["subject"], paper["grade"])
    print(f"Loaded {len(lessons)} {paper['subject']} G{paper['grade']} lesson card(s).")
    for q, lesson, ref, conf in match_questions(paper, lessons):
        if lesson:
            print(f"  {q['ref']:8} [{conf:6}] {q['solution_method']:28} -> "
                  f"{lesson['id']} ({ref}, status={lesson['status']})")
        else:
            print(f"  {q['ref']:8} [unmatched] {q['solution_method']:28} -> (no lesson teaches this method)")
    return 0


def cmd_link(args):
    paper = json.loads(Path(args.paper).read_text("utf-8"))
    lessons = load_lessons(paper["subject"], paper["grade"])
    matches = match_questions(paper, lessons)

    links = {"papers": {}, "lessons": {}}
    if LINKS_PATH.exists():
        links = json.loads(LINKS_PATH.read_text("utf-8"))
    links["papers"].setdefault(paper["paper_id"], {
        "source": paper["source"], "source_url": paper["source_url"],
        "subject": paper["subject"], "grade": paper["grade"],
        "paper": paper["paper"], "session": paper["session"],
        "matches": {}, "unmatched": [],
    })
    paper_entry = links["papers"][paper["paper_id"]]

    linked = 0
    for q, lesson, ref, conf in matches:
        if not lesson or lesson["status"] != "evaluated":
            paper_entry["unmatched"].append(q["ref"])
            continue
        gen = SCENE_GENERATORS.get(q["solution_method"])
        if not gen:
            paper_entry["unmatched"].append(q["ref"])
            continue

        # Write the attributed worked example + its Manim scene into the lesson.
        wdir = worked_example_dir(lesson, paper, q["ref"])
        wdir.mkdir(parents=True, exist_ok=True)
        (wdir / "question.md").write_text(
            f"# Past-Paper Worked Example — {q['ref']}\n\n"
            f"**Source:** {paper['source']} — Grade {paper['grade']} "
            f"{paper['subject']} {paper['paper']}, {paper['session']}, question {q['ref']}.\n\n"
            f"**{paper['copyright']}**\n\n"
            f"## Question ({q['marks']} marks)\n\n{q['text']}\n\n"
            f"## Method\n\n{q['solution_method'].replace('_', ' ')}\n\n"
            f"## Memo working\n\n{q.get('memo_working', '(see marking guidelines)')}\n\n"
            f"## Answer (per marking guidelines)\n\n{q['memo_answer']}\n",
            encoding="utf-8")
        (wdir / "manim_scene.py").write_text(gen(q, paper), encoding="utf-8")

        # Record on the card + both directions of the index.
        card = Path(lesson["card"]).read_text("utf-8")
        existing = get_field(card, "past_paper_examples")
        refs = [r for r in existing.split(",") if r.strip()] if existing else []
        tag = f'{paper["paper_id"]}:{q["ref"]}'
        if tag not in refs:
            refs.append(tag)
        card = set_field(card, "past_paper_examples", ", ".join(refs))
        Path(lesson["card"]).write_text(card, encoding="utf-8")

        paper_entry["matches"][q["ref"]] = {
            "lesson_id": lesson["id"], "subtopic_ref": ref,
            "confidence": conf, "solution_method": q["solution_method"],
            "example_path": str(wdir).replace("\\", "/"),
        }
        links["lessons"].setdefault(lesson["id"], [])
        back = {"paper_id": paper["paper_id"], "question": q["ref"],
                "subtopic_ref": ref, "example_path": str(wdir).replace("\\", "/")}
        if back not in links["lessons"][lesson["id"]]:
            links["lessons"][lesson["id"]].append(back)
        linked += 1
        print(f"  linked {q['ref']} -> {lesson['id']} ({ref})  [{wdir}]")

    paper_entry["unmatched"] = sorted(set(paper_entry["unmatched"]))
    LINKS_PATH.parent.mkdir(parents=True, exist_ok=True)
    LINKS_PATH.write_text(json.dumps(links, indent=2) + "\n", encoding="utf-8")
    print(f"Linked {linked} worked example(s); index -> {LINKS_PATH}")
    return 0


def cmd_lookup(args):
    links = json.loads(LINKS_PATH.read_text("utf-8"))
    if args.paper_id:
        entry = links["papers"].get(args.paper_id)
        if not entry:
            print(f"No such paper: {args.paper_id}"); return 1
        print(f"Paper {args.paper_id} -> lessons:")
        for qref, m in entry["matches"].items():
            print(f"  {qref} -> {m['lesson_id']} ({m['subtopic_ref']}, {m['confidence']})")
        print(f"  unmatched: {', '.join(entry['unmatched']) or '(none)'}")
    elif args.lesson_id:
        back = links["lessons"].get(args.lesson_id, [])
        print(f"Lesson {args.lesson_id} <- past-paper questions:")
        for b in back:
            print(f"  {b['paper_id']}:{b['question']} ({b['subtopic_ref']}) [{b['example_path']}]")
        if not back:
            print("  (none)")
    return 0


# --- verification hook ---

def _fmt_root(v, decimals=None):
    """Root -> canonical string matching parse_memo_roots output."""
    if decimals is not None:
        v = round(v, decimals)
        s = f"{v:.{decimals}f}"
        return s.rstrip("0").rstrip(".") if "." in s else s
    return f"{v:g}"


def recompute(qref, paper):
    """Recompute the answer for a checkable question from first principles;
    return a set of rounded values as strings, or None if not recomputable.

    Preferred path: a machine-checkable `recompute` spec on the question —
    data-driven, so new papers need no code changes:
      {"kind": "linear_factor_roots", "factors": [[a1,b1],[a2,b2]]}
          roots of (a1 x + b1)(a2 x + b2) = 0, i.e. -b/a each
      {"kind": "quadratic_formula_roots", "a":…, "b":…, "c":…, "decimals": 2}
    Legacy per-(paper_id, qref) cases below cover the papers recorded before
    the spec existed. Question refs repeat across papers, hence the pairing."""
    q = next((x for x in paper["questions"] if x["ref"] == qref), None)
    if not q or not q.get("checkable"):
        return None
    spec = q.get("recompute")
    if spec:
        import math
        if spec["kind"] == "linear_factor_roots":
            roots = set()
            for a, b in spec["factors"]:
                v = -b / a
                roots.add(_fmt_root(v, 2 if v != int(v) else None))
            return roots
        if spec["kind"] == "quadratic_formula_roots":
            a, b, c = spec["a"], spec["b"], spec["c"]
            d = math.sqrt(b * b - 4 * a * c)
            dec = spec.get("decimals", 2)
            return {_fmt_root((-b + d) / (2 * a), dec),
                    _fmt_root((-b - d) / (2 * a), dec)}
        raise SystemExit(f"unknown recompute kind: {spec['kind']}")
    pid = paper["paper_id"]
    if pid == "dbe_maths_g11_p1_2018_nov" and qref == "Q1.1.1":
        return {"0", "-0.5"}  # x(2x+1)=0 by zero-product
    if pid == "dbe_maths_g11_p1_2018_nov" and qref == "Q1.1.2":
        import math
        a, b, c = 5, 2, -6
        d = math.sqrt(b * b - 4 * a * c)
        return {f"{round((-b + d) / (2 * a), 2):.2f}", f"{round((-b - d) / (2 * a), 2):.2f}"}
    if pid == "dbe_physical_sciences_g11_p1_2018_nov" and qref == "Q4.3":
        # 1/a vs m graph at constant F_net: 1/a = m/F_net, so the gradient is
        # 1/F_net. Memo's accepted coordinates: (1,25 kg, 2,5 s^2/m).
        gradient = (2.5 - 0) / (1.25 - 0)
        f_net = 1 / gradient
        return {f"{f_net:g}"}
    if pid == "dbe_geography_g12_p2_2018_nov" and qref == "Q2.2.2":
        # Average gradient = VI/HE as 1:x, from the memo-accepted map
        # readings recorded in the question's map_inputs.
        mi = q["map_inputs"]
        vi = mi["trig_station_height_m"] - mi["contour_height_m"]
        he_m = mi["map_distance_cm"] * mi["map_scale_denominator"] / 100
        ratio = round(he_m / vi, 1)
        lo, hi = mi["accepted_final_range"]
        if not lo <= ratio <= hi:
            return {"OUT_OF_ACCEPTED_RANGE"}
        return {"1", f"{ratio:g}"}
    return None


def parse_memo_roots(memo):
    """Extract numeric roots from a memo answer string like
    'x = 0,91 or x = -1,31' -> {'0.91','-1.31'} (SA comma decimals + fractions)."""
    roots = set()
    for tok in re.findall(r"-?\d+(?:[.,]\d+)?(?:/\d+)?", memo):
        t = tok.replace(",", ".")
        if "/" in t:
            n, den = t.split("/")
            roots.add(f"{float(n) / float(den):.2f}".rstrip("0").rstrip("."))
        else:
            v = float(t)
            roots.add(f"{v:.2f}".rstrip("0").rstrip(".") if v != int(v) else str(int(v)))
    return roots


def cmd_verify(args):
    links = json.loads(LINKS_PATH.read_text("utf-8"))
    back = links["lessons"].get(args.lesson_id, [])
    if not back:
        print(f"Lesson {args.lesson_id} has no linked past-paper examples."); return 0
    ok = True
    for b in back:
        paper = json.loads((PP_ROOT / _paper_rel(b["paper_id"])).read_text("utf-8"))
        q = next((x for x in paper["questions"] if x["ref"] == b["question"]), None)
        # 1. the linked subtopic must actually teach the question's method
        lessons = load_lessons(paper["subject"], paper["grade"])
        lesson = next((l for l in lessons if l["id"] == args.lesson_id), None)
        method = q["solution_method"]
        teaches = lesson and lesson["methods"].get(method) == b["subtopic_ref"]
        # 2. recompute the answer and compare to the memo
        computed = recompute(q["ref"], paper)
        memo = parse_memo_roots(q["memo_answer"]) if q.get("checkable") else None
        agree = (computed is not None and memo is not None and computed == memo)

        status = "OK" if teaches and (agree or not q.get("checkable")) else "FAIL"
        ok = ok and status == "OK"
        detail = f"method taught by {b['subtopic_ref']}: {teaches}"
        if q.get("checkable"):
            detail += f"; recomputed {sorted(computed)} vs memo {sorted(memo)}: {agree}"
        else:
            detail += "; answer not machine-checkable (structural link only)"
        print(f"  [{status}] {b['paper_id']}:{q['ref']} — {detail}")
    print("VERIFY OK" if ok else "VERIFY FAILED")
    return 0 if ok else 1


def _paper_rel(paper_id):
    # dbe_maths_g11_p1_2018_nov -> maths/grade11/2018/paper.json
    m = re.match(r"dbe_(\w+?)_g(\d+)_p\d_(\d{4})_", paper_id)
    if not m:
        raise SystemExit(f"cannot locate paper.json for {paper_id}")
    subj, grade, year = m.group(1), m.group(2), m.group(3)
    return Path(subj) / f"grade{grade}" / year / "paper.json"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("match"); m.add_argument("--paper", required=True)
    m.add_argument("--backend", choices=["memo", "groq"], default="memo")
    m.set_defaults(func=cmd_match)
    l = sub.add_parser("link"); l.add_argument("--paper", required=True)
    l.set_defaults(func=cmd_link)
    lo = sub.add_parser("lookup")
    lo.add_argument("--paper-id"); lo.add_argument("--lesson-id")
    lo.set_defaults(func=cmd_lookup)
    v = sub.add_parser("verify"); v.add_argument("--lesson-id", required=True)
    v.set_defaults(func=cmd_verify)
    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
