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

"""Report-only maths correctness verifier: MCQ keys and the maths we teach.

lesson_pipeline.py's verify_answer_keys recognises a handful of regex forms
(discriminant, rational roots, factor/expand strings, numeric "value of")
and so only reaches a few questions. This module recomputes the answer with
sympy wherever the stem carries a formalisable piece of maths:

  solve        an equation or inequality in one unknown (assignments such as
               "a = 2" in the stem are substituted first)
  factorise    options equivalent to the stem expression, preferring the
               fully factorised one
  equivalence  expand / simplify / "equivalent to" / exponent laws, checked
               with simplify(a - b) == 0 (random-point pre-filter first)
  evaluate     a stem expression with no unknowns ("evaluates to", "value of")
  substitute   "for y = 2x², the value of y when x = 3", f(x) and T_n forms
  percent      "25% of R480", "15% off R7 200", "increase R400 by 10%"
  ratio        "simplest form of 250 : 1000", "share R2 400 in the ratio 5 : 3 : 2"

Each MCQ gets one verdict:

  verified          the keyed option is the unique correct option
  MISMATCH          the keyed option is wrong and exactly one other option
                    is right
  MULTIPLE_CORRECT  more than one option equals the true answer
  NO_CORRECT        no option equals the true answer (or correct_index is out
                    of range)
  UNPARSEABLE       the maths in the text is malformed (unbalanced brackets,
                    an expression sympy cannot read)
  SKIPPED           a word or concept question that cannot be formalised

It is deliberately conservative: anything ambiguous is SKIPPED, never
guessed at. The checker is REPORT-ONLY — it always exits 0 unless it crashes
(CI: .github/workflows/math_verify.yml).

Step checks — what we TEACH, not only what we ask (--steps / --steps-only)
-------------------------------------------------------------------------
The same sympy core reads:

  script          lesson scripts (spoken maths: "three x plus one equals
                  seven, so x equals two") under */session/**/script.md
  knowledge_bite  past-paper worked solutions, memo working and answers
                  (*/knowledge_bites/**/question.md)
  animation       the on-screen maths of each lesson (MathTex/Tex strings in
                  manim_scene.py); one animation can carry several tutors'
                  narration, so it is checked once, on its own
  consistency     narration vs screen: script.md "## Subtopic" N is paired
                  with the manim band marked "(subtopic_N)"

It finds derivation chains ("x² − 5x + 6 = 0 → (x−2)(x−3) = 0 → x = 2 or
x = 3", "a = b = c", "so"/"gives" links, and consecutive lines of one
worked solution or screen band), standalone identities ("a^m × a^n =
a^(m+n)") and numeric facts, and gives each one a verdict:

  STEP_OK       the step is true
  STEP_WRONG    the step is false (the step index is reported)
  ANSWER_WRONG  the stated final answer is not a solve of the original
  WARNING       a step legitimately loses or gains roots (dividing by an
                expression in the unknown, squaring both sides, a root
                rejected by context) or holds only after unstated rounding
  UNPARSEABLE   maths-looking text that is malformed (unbalanced brackets,
                garbled operators)
  SKIPPED       prose, or maths that cannot be formalised with certainty
  CONSISTENT / CONTRADICTS_SCREEN  (consistency only)

It CHECKS TRUTH, NOT METHOD. A tutor may simplify, jump several steps at
once, work in a non-textbook order, guess and check, or take any other valid
route: only whether each stated step is mathematically true is judged
(expressions equivalent, solution set preserved, numeric fact correct).
A step that cannot be verified is SKIPPED, never wrong; a root-losing or
root-gaining step is a WARNING that says why, never STEP_WRONG; an arrow
between plain values ("5 → 10 → 20", "x² → 2x") may mean "maps to" and is
never judged. Deliberate error examples ("the error museum", struck-out
screen lines) are never flagged. Spoken maths is read under every plausible
bracketing and is flagged only if false under all of them and free of
vocabulary the reader does not formalise (sine, half of, percent, ...).

Narration-vs-screen is anchored on the equation, never on wording: a
narrated "equation → x = v" is compared only when the same equation (same
solution set, any route) is on screen in that subtopic, and is flagged only
when v is none of the values the screen states.

Private tutor content (RokctAI/agent) is LOCAL ONLY: --agent reads the tutor
snippets (lms/team/tutors/CAPS/*/samples.json, samples/*.md) and whiteboard
animations (animations.json) through the GitHub REST API with MONOREPO_PAT,
GH_TOKEN or GITHUB_TOKEN, writes nothing to disk and prints only
"path:line — verdict". It is never run in the public CI.

Usage (repo root):
    python3 lessons/scripts/CAPS/math_verify.py \\
        --json math_verify_report.json --md math_verify_report.md
    python3 lessons/scripts/CAPS/math_verify.py path/to/mcq.json ...
    python3 lessons/scripts/CAPS/math_verify.py --steps-only \\
        --steps-json math_steps_report.json --steps-md math_steps_report.md
    python3 lessons/scripts/CAPS/math_verify.py --steps-only --content script
    MONOREPO_PAT=... python3 lessons/scripts/CAPS/math_verify.py --agent
"""

import argparse
import json
import math
import random
import re
import signal
import sys
from collections import Counter, defaultdict
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

import sympy as sp
from sympy.parsing.sympy_parser import (
    convert_xor,
    implicit_multiplication_application,
    parse_expr,
    rationalize,
    standard_transformations,
)

REPO_ROOT = Path(__file__).resolve().parents[3]
CURRICULUM_ROOT = REPO_ROOT / "lessons" / "curriculum" / "CAPS"
SUBJECTS = ("maths", "mathematical_literacy")

VERDICTS = ("verified", "MISMATCH", "MULTIPLE_CORRECT", "NO_CORRECT",
            "UNPARSEABLE", "SKIPPED")
FLAGGED = ("MISMATCH", "MULTIPLE_CORRECT", "NO_CORRECT", "UNPARSEABLE")

TIMEOUT_SECONDS = 4

_TRANSFORMS = standard_transformations + (
    implicit_multiplication_application, convert_xor, rationalize)

# Every single letter is a plain symbol: sympy would otherwise read E, I, N,
# O, Q and S as constants/functions.
_LOCALS = {c: sp.Symbol(c) for c in
           "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
for _name in ("alpha", "beta", "theta", "gamma", "phi"):
    _LOCALS[_name] = sp.Symbol(_name)
_LOCALS.update({"pi": sp.pi, "sqrt": sp.sqrt, "cbrt": sp.cbrt,
                "sin": sp.sin, "cos": sp.cos, "tan": sp.tan,
                "log": sp.log, "ln": sp.log, "rad": lambda d: d * sp.pi / 180})

FUNCS = {"sin", "cos", "tan", "sqrt", "cbrt", "log", "ln", "pi", "rad",
         "alpha", "beta", "theta", "gamma", "phi"}
# Two-letter runs that are English or units, never a product of symbols.
_NOT_PRODUCTS = {"to", "of", "or", "in", "is", "by", "at", "an", "as", "if",
                 "on", "no", "st", "nd", "rd", "th", "cm", "mm", "km", "kg",
                 "ml", "kl", "am", "pm", "ha", "be", "it", "so", "up", "we",
                 "do", "go", "me", "my", "us", "he", "id"}


class Timeout(Exception):
    pass


@contextmanager
def time_limit(seconds):
    """SIGALRM guard so one pathological simplify() cannot hang a run."""
    if not hasattr(signal, "SIGALRM"):
        yield
        return

    def _raise(signum, frame):
        raise Timeout()

    old = signal.signal(signal.SIGALRM, _raise)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)


# --- text normalisation ---

_SUPERSCRIPT = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5",
                "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁻": "-", "ˣ": "x",
                "ⁿ": "n", "⁺": "+"}
_SUP_RUN = re.compile("[" + "".join(_SUPERSCRIPT) + "]+")
_GREEK = {"α": " alpha", "β": " beta", "θ": " theta", "γ": " gamma",
          "φ": " phi", "π": " pi "}


def normalise(text):
    """Unicode maths text -> sympy-friendly ASCII (keeps the em dash)."""
    s = str(text)
    s = s.replace(" ", " ").replace(" ", " ").replace(" ", " ")
    s = s.replace("−", "-").replace("–", "-").replace("‒", "-")
    for a in ("×", "·", "⋅", "∙"):
        s = s.replace(a, "*")
    s = s.replace("÷", "/").replace("½", "(1/2)").replace("¼", "(1/4)")
    s = s.replace("≤", "<=").replace("≥", ">=").replace("≠", "!=")
    s = s.replace("’", "'").replace("‘", "'")
    s = _SUP_RUN.sub(
        lambda m: "^(" + "".join(_SUPERSCRIPT[c] for c in m.group()) + ")", s)
    for g, name in _GREEK.items():
        s = s.replace(g, name)
    s = s.replace("∛", "cbrt")
    s = re.sub(r"√\s*\(", "sqrt(", s)
    s = re.sub(r"√\s*(\d+(?:[.,]\d+)?|[A-Za-z])", r"sqrt(\1)", s)
    s = s.replace("√", "sqrt")
    # 1,85 -> 1.85 (a list comma is always followed by a space)
    s = re.sub(r"(?<=\d),(?=\d)", ".", s)
    # 4 000 000 -> 4000000
    s = re.sub(r"(?<![\d.])(\d{1,3})((?: \d{3})+)(?![\d.]*\d)",
               lambda m: m.group(1) + m.group(2).replace(" ", ""), s)
    s = re.sub(r"(?<![\d.])(\d{1,3})((?: \d{3})+)(?=\.\d)",
               lambda m: m.group(1) + m.group(2).replace(" ", ""), s)
    # currency: R4 840 -> 4840
    s = re.sub(r"(?<![A-Za-z])R\s?(?=\d)", "", s)
    # trig in degrees: sin 52° -> sin(rad(52)); sin(180° + x) -> sin(rad(180) + x)
    s = re.sub(r"\b(sin|cos|tan)\^\((\d)\)\s*(\w+)", r"\1(\3)^(\2)", s)
    s = re.sub(r"\b(sin|cos|tan)\s*(\([^()]*\))",
               lambda m: m.group(1) + re.sub(r"(\d+(?:\.\d+)?)\s*°",
                                             r"rad(\1)", m.group(2)), s)
    s = re.sub(r"\b(sin|cos|tan)\s*(-?\d+(?:\.\d+)?)\s*°", r"\1(rad(\2))", s)
    s = s.replace("°", "")
    s = re.sub(r"\b(sin|cos|tan)\s*(\d*\s*(?:alpha|beta|theta|gamma|phi|[a-z]))\b",
               r"\1(\2)", s)
    # log_2 8 -> log(8, 2); log 100 -> log(100, 10)
    s = re.sub(r"\blog_\(?(\w+)\)?\s*\(?\s*([\w.]+)\s*\)?", r"log(\2, \1)", s)
    s = re.sub(r"\blog\s+([\d.]+|[a-z])\b", r"log(\1, 10)", s)
    return s


def strip_explanation(option):
    """'R4 840 — because ...' -> 'R4 840'."""
    s = re.split(r"\s*—\s*|\s+because\b|\s+since\b|,\s+so\b|\s+so\s+|,\s+with\b"
                 r"|,\s+after\b|,\s+by\b|,\s+which\b|\s+\(with\b",
                 str(option), maxsplit=1)[0]
    s = re.sub(r"\s+(only|both)\s*$", "", s.strip(), flags=re.I)
    return s.strip().rstrip(".")


# --- parsing ---

class ParseFailure(Exception):
    """The text is maths-shaped but sympy cannot read it."""


def _balanced(s):
    depth = 0
    for ch in s:
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def parse_math(s):
    """Parse one normalised expression; raises ParseFailure."""
    s = s.strip().rstrip(".:;,?")
    if not s:
        raise ParseFailure("empty")
    if not _balanced(s):
        raise ParseFailure("unbalanced brackets")
    if re.search(r"[+*/^]\s*[*/^)]|\(\s*[*/^)]|[+\-*/^]\s*$", s):
        raise ParseFailure("dangling operator")
    s = s.replace("[", "(").replace("]", ")")
    try:
        with time_limit(TIMEOUT_SECONDS):
            e = parse_expr(s, local_dict=dict(_LOCALS),
                           transformations=_TRANSFORMS, evaluate=True)
    except Timeout:
        raise ParseFailure("timeout")
    except Exception as exc:  # TokenError, SyntaxError, TypeError, ...
        raise ParseFailure(f"{type(exc).__name__}: {exc}")
    if not isinstance(e, sp.Expr):
        raise ParseFailure(f"not an expression: {type(e).__name__}")
    return e


def _over(s):
    """'A over B' -> '(A)/(B)'."""
    parts = re.split(r"\s+over\s+", s)
    if len(parts) == 2:
        return f"({parts[0]})/({parts[1]})"
    return s


def parse_relation(s):
    """'lhs = rhs' / 'a < x <= b' / expression -> (kind, payload)."""
    s = _over_sides(s)
    ops = re.findall(r"<=|>=|!=|=|<|>", s)
    if not ops:
        return "expr", parse_math(s)
    parts = re.split(r"<=|>=|!=|=|<|>", s)
    sides = [parse_math(p) for p in parts]
    if ops == ["="]:
        try:
            return "eq", sp.Eq(sides[0], sides[1], evaluate=False)
        except Exception as exc:
            raise ParseFailure(str(exc))
    if "=" in ops or "!=" in ops:
        raise ParseFailure("mixed relation")
    rel = {"<": sp.Lt, ">": sp.Gt, "<=": sp.Le, ">=": sp.Ge}
    try:
        conds = [rel[o](sides[i], sides[i + 1], evaluate=False)
                 for i, o in enumerate(ops)]
    except Exception as exc:
        raise ParseFailure(str(exc))
    return "ineq", conds


def _over_sides(s):
    pieces = re.split(r"(<=|>=|!=|=|<|>)", s)
    return "".join(p if i % 2 else _over(p) for i, p in enumerate(pieces))


# --- locating maths inside prose ---

_TOKEN_OK = re.compile(r"^[0-9A-Za-z.+\-*/^=<>!()\[\]'_]+$")


def _mathy(tok):
    if not tok or not _TOKEN_OK.match(tok):
        return False
    if tok == "over":
        return True
    runs = re.findall(r"[A-Za-z]+", tok)
    for r in runs:
        if len(r) == 1:
            continue
        if r in FUNCS:
            continue
        if len(r) == 2 and r.islower() and r not in _NOT_PRODUCTS:
            continue
        if re.fullmatch(r"(sqrt|cbrt|log|sin|cos|tan|rad|pi)+[a-z]?", r):
            continue
        return False
    if tok.isalpha() and len(tok) == 1 and tok in "aAI":
        return False  # articles
    if tok.isalpha() and len(tok) == 2 and tok in _NOT_PRODUCTS:
        return False
    return True


def math_spans(text):
    """Maximal runs of maths-looking tokens in normalised prose."""
    spans, cur = [], []
    raws = text.split()
    ops = {"+", "-", "=", "*", "/", "<", ">", "<=", ">="}
    for n, raw in enumerate(raws):
        end = False
        tok = raw
        if tok in ("a", "A") and (n + 1 < len(raws) and raws[n + 1] in ops
                                  or cur and cur[-1] in ops):
            cur.append(tok)  # the symbol a, not the article
            continue
        if tok and tok[-1] in ":;,?!":
            tok, end = tok[:-1], True
        elif tok.endswith(".") and not re.search(r"\d\.$", tok[:-1] + "0"):
            tok, end = tok[:-1], True
        if _mathy(tok):
            cur.append(tok)
        else:
            if cur:
                spans.append(" ".join(cur))
            cur = []
        if end and cur:
            spans.append(" ".join(cur))
            cur = []
    if cur:
        spans.append(" ".join(cur))
    out = []
    for sp_ in spans:
        sp_ = re.sub(r"^(over\s+)+|(\s+over)+$", "", sp_).strip()
        if re.search(r"[+\-*/^=<>()]|sqrt|log|sin|cos|tan|\d[A-Za-z]|[A-Za-z]\d",
                     sp_) and re.search(r"[0-9A-Za-z]", sp_):
            if re.fullmatch(r"-?\d+(\.\d+)?\s*-\s*\d+(\.\d+)?", sp_):
                continue  # a range such as 10-20
            if re.fullmatch(r"[A-Za-z]-[A-Za-z]+", sp_):
                continue
            out.append(sp_)
    return out


# --- comparing values ---

def _is_number(e):
    try:
        return e is not None and not e.free_symbols and e.is_number
    except Exception:
        return False


def to_float(e):
    try:
        with time_limit(TIMEOUT_SECONDS):
            v = complex(sp.N(e, 30))
    except Exception:
        return None
    if abs(v.imag) > 1e-9 * max(1.0, abs(v.real)):
        return None
    return v.real


def equivalent(a, b):
    """True / False / None (unknown) for symbolic equivalence a == b."""
    syms = sorted(a.free_symbols | b.free_symbols, key=str)
    rng = random.Random(7)
    diff = a - b
    checked = 0
    for _ in range(6):
        pts = {s: sp.Rational(rng.randint(13, 97), rng.randint(11, 37))
               for s in syms}
        try:
            with time_limit(TIMEOUT_SECONDS):
                va = complex(sp.N(a.subs(pts), 20))
                vb = complex(sp.N(b.subs(pts), 20))
        except Exception:
            continue
        if any(v != v or abs(v) == float("inf") for v in (va, vb)):
            continue
        checked += 1
        if abs(va - vb) > 1e-8 * max(1.0, abs(va), abs(vb)):
            return False
    if checked == 0:
        return None
    try:
        with time_limit(TIMEOUT_SECONDS):
            if sp.simplify(diff) == 0:
                return True
    except Exception:
        pass
    return True  # agreed at every sample point; simplify merely inconclusive


def _decimals(text):
    m = re.search(r"\d\.(\d+)", text)
    return len(m.group(1)) if m else 0


def numeric_option(opt):
    """Option text -> (value, decimals, is_percent) or None."""
    s = normalise(strip_explanation(opt))
    if "=" in s:
        s = s.split("=")[-1]
    s = s.strip()
    pct = "%" in s
    s = s.replace("%", "").replace("°", "").strip()
    # trailing unit / noun words: at most two, never maths names (pi) and
    # never prose such as "which cannot be simplified"
    upow = None
    for _ in range(2):
        m = re.search(r"(?:(?<=\d)|\s+)([A-Za-z][A-Za-z\-']*)(\^\((\d)\))?\s*$", s)
        if not m or m.group(1) in FUNCS or re.fullmatch(
                r"which|is|cannot|not|be|only|the|and|so|or|because|than|of|[a-z]",
                m.group(1)) and m.group(1) not in ("m", "g", "l", "h", "s"):
            break
        if upow is None and re.fullmatch(r"(mm|cm|m|km)", m.group(1)):
            upow = int(m.group(3) or 1)
        s = s[:m.start()].rstrip()
    if re.search(r"\d\s+[A-Za-z]+\s+[A-Za-z]+", re.sub(r"\bpi\b", "", s)):
        return None
    s = s.strip()
    if not s or not re.search(r"\d", s) or re.search(r"[A-Za-z]{2,}", re.sub(
            r"sqrt|pi|log|sin|cos|tan|rad", "", s)):
        return None
    if re.search(r"(?<![a-z])[a-zA-Z](?![a-z])", re.sub(
            r"sqrt|pi|log|sin|cos|tan|rad", "", s)):
        return None
    try:
        e = parse_math(s)
    except ParseFailure:
        return None
    if not _is_number(e):
        return None
    v = to_float(e)
    if v is None:
        return None
    return v, _decimals(s), pct, upow


_APPROX = re.compile(r"about|approx|≈|nearest|round|correct to|decimal",
                     re.I)


def match_numeric(target, options, approx=False, dim=None):
    """Return (strict_idx, loose_idx, unparsed_idx) against a float target."""
    strict, loose, unparsed = [], [], []
    for i, opt in enumerate(options):
        nv = numeric_option(opt)
        if nv is None:
            unparsed.append(i)
            continue
        v, dp, _, upow = nv
        if dim is not None and upow is not None and upow != dim:
            unparsed.append(i)  # a length answer in m² is not the answer
            continue
        tol = 0.5 * 10 ** (-dp) + 1e-9 * max(1.0, abs(target)) if dp else \
            1e-9 * max(1.0, abs(target))
        if abs(v - target) <= tol * 1.0001:
            strict.append(i)
            loose.append(i)
            continue
        # looser only when the stem itself says the answer is approximate
        ltol = max(2 * tol, 0.005 * abs(target)) if approx else tol
        if approx and dp == 0:
            ltol = max(ltol, 0.5 + 1e-9)
        if abs(v - target) <= ltol:
            loose.append(i)
    return strict, loose, unparsed


def decide(key, correct, candidates=None, parsed=None, n_options=4,
           allow_no_correct=True):
    """Map the set of correct option indexes to a verdict.

    correct:    options that equal the true answer
    candidates: looser matches (rounding); the key being one of these is
                accepted but never counts toward MISMATCH/MULTIPLE_CORRECT
    parsed:     options that could be compared at all
    """
    candidates = candidates if candidates is not None else correct
    parsed = parsed if parsed is not None else list(range(n_options))
    if key in correct:
        if len(correct) > 1:
            return "MULTIPLE_CORRECT", correct
        return "verified", correct
    if key in candidates:
        if len(correct) == 1:
            # the key is only near the answer while another option is exact
            return "MISMATCH", correct
        return "verified", [key]
    if key not in parsed:
        return "SKIPPED", correct
    if len(correct) == 1 and len(candidates) == 1:
        return "MISMATCH", correct
    if len(correct) > 1:
        return "MULTIPLE_CORRECT", correct
    if not candidates and allow_no_correct and len(parsed) == n_options:
        return "NO_CORRECT", []
    return "SKIPPED", correct


# --- question handlers ---

_SKIP_WORDS = re.compile(
    r"\bstep\b|\bsteps\b|\bwhy\b|mistake|\berror\b|\bwrong\b|\bfirst\b|\bnext\b"
    r"|\bmethod\b|\breason|\bmeans?\b|\bcalled\b|\bterms?\b|coefficient"
    r"|\bdegree\b|\blaw\b|property|\bsign\b|\bcheck\b|restriction|undefined"
    r"|domain|\brange\b|graph|turning|asymptote|y-intercept|discriminant"
    r"|how many|number of|nature|\bproof\b|\bpicture\b|\bline\b|begins?\b"
    r"|\bdivid\w* by\b|\bfeature|\bgap\b|\bstands?\b|built from|\bcase\b"
    r"|\bfails?\b|\bvalid\b|\binstead\b|\bstructure\b"
    r"|\bbracket\b|\bsketch|\bshape|\bpattern\b|\bdifference\b(?! f)"
    r"|\bgradient|\bslope|\bderivative|\bdy/dx|limit|\bamplitude|\bperiod"
    r"|\bmaximum|\bminimum|\binverse|\bquadrant|\bsequence|\bseries"
    r"|numerator|denominator|\bLCD\b|\bpower\b|\braise|\bsame\b",
    re.I)
_NOT = re.compile(r"\bNOT\b|\bnot equivalent|\bnot equal|\bexcept\b")


def _stem_spans(stem_n):
    return [s for s in math_spans(stem_n)]


def _parse_spans(spans):
    """-> list of (span, kind, payload) and list of (span, error)."""
    good, bad = [], []
    for s in spans:
        try:
            kind, payload = parse_relation(s)
        except ParseFailure as exc:
            bad.append((s, str(exc)))
            continue
        good.append((s, kind, payload))
    return good, bad


def _free(kind, payload):
    if kind == "ineq":
        out = set()
        for c in payload:
            out |= c.free_symbols
        return out
    return payload.free_symbols


def _assignments(parsed):
    """'x = 3' style spans -> {x: 3}."""
    out = {}
    for s, kind, p in parsed:
        if kind == "eq" and isinstance(p.lhs, sp.Symbol) and _is_number(p.rhs):
            if p.lhs in out and out[p.lhs] != p.rhs:
                return None  # "gives k = 1 and k = 9": not an assignment
            out[p.lhs] = p.rhs
    return out


def _option_solution_set(opt, var):
    """Option text -> sympy Set of values for var, or None."""
    raw = strip_explanation(opt)
    low = raw.lower()
    if re.search(r"no (real )?(solution|roots?)|no value|none", low):
        return sp.S.EmptySet
    if re.search(r"all real|every real|any real", low):
        return sp.S.Reals
    s = normalise(raw)
    s = re.sub(r"\b(only|both|and also)\b", "", s)
    pieces = re.split(r"\bor\b|\band\b|;|,\s", s)
    result = sp.S.EmptySet
    name = str(var)
    for piece in pieces:
        piece = piece.strip()
        if not piece:
            continue
        if re.search(r"[A-Za-z]{3,}", re.sub(r"sqrt|pi|log", "", piece)):
            return None
        variants = [piece]
        if "±" in piece:
            variants = [piece.replace("±", "+"), piece.replace("±", "-")]
        for v in variants:
            try:
                kind, p = parse_relation(v)
            except ParseFailure:
                return None
            if kind == "expr":
                if not _is_number(p):
                    return None
                result = result | sp.FiniteSet(p)
            elif kind == "eq":
                if p.lhs == var and _is_number(p.rhs):
                    result = result | sp.FiniteSet(p.rhs)
                elif isinstance(p.lhs, sp.Symbol) and str(p.lhs) != name:
                    return None
                else:
                    return None
            else:
                if _free(kind, p) != {var}:
                    return None
                part = sp.S.Reals
                try:
                    for c in p:
                        part = part & sp.solveset(c, var, sp.S.Reals)
                except Exception:
                    return None
                result = result | part
    return result


def _sets_equal(a, b):
    """Solution-set equality; decimal options match roots to rounding."""
    if a == b:
        return True
    if isinstance(a, sp.FiniteSet) and isinstance(b, sp.FiniteSet):
        fa = [to_float(x) for x in a]
        fb = [to_float(x) for x in b]
        if None in fa or None in fb:
            return False
        ua = sorted(set(round(x, 9) for x in fa))
        ub = sorted(set(round(x, 9) for x in fb))
        if len(ua) != len(ub):
            return False
        return all(abs(x - y) <= 0.0051 * max(1, abs(x)) for x, y in zip(ua, ub))
    try:
        with time_limit(TIMEOUT_SECONDS):
            return bool(sp.simplify(a.symmetric_difference(b)) == sp.S.EmptySet)
    except Exception:
        return False


def _is_subset(a, b):
    if not (isinstance(a, sp.FiniteSet) and isinstance(b, sp.FiniteSet)):
        return False
    if not a or len(a) >= len(b):
        return False
    fb = [to_float(x) for x in b]
    return all(any(y is not None and abs(to_float(x) - y) < 1e-6 for y in fb)
               for x in a if to_float(x) is not None)


def handle_solve(stem, stem_n, parsed, options, key):
    xint = re.search(r"\bx-intercepts? of\b", stem, re.I)
    if not xint and not re.search(r"\bsolv|solution|\broots?\b|\bsatisf|\bzeros?\b"
                                  r"|value of [a-z]\b|\bgives\b", stem, re.I):
        return None
    assign = _assignments(parsed)
    if assign is None:
        return None
    rels = [(s, k, p) for s, k, p in parsed
            if k in ("eq", "ineq") and not (
                k == "eq" and isinstance(p.lhs, sp.Symbol) and _is_number(p.rhs))]
    if len(rels) != 1:
        return None
    s, kind, p = rels[0]
    if "_" in s or re.match(r"\s*[+*/^=]", s):
        return None  # T_n relations; a span that lost its first term
    # CAPS defines rational exponents for positive bases only, so
    # x^(2/3) = 9 has the single answer x = 27
    domain = sp.Interval.open(0, sp.oo) if re.search(
        r"[a-z]\^\(?-?\d+/\d+\)?", s) else sp.S.Reals
    if xint:
        if kind != "eq" or p.lhs != sp.Symbol("y"):
            return None
        p = sp.Eq(p.rhs, 0)
    if kind == "eq":
        p = sp.Eq(p.lhs.subs(assign), p.rhs.subs(assign))
        free = p.free_symbols
    else:
        p = [c.subs(assign) for c in p]
        free = _free("ineq", p)
    if len(free) != 1:
        return None
    var = next(iter(free))
    if re.search(r"sin|cos|tan", s):
        return None
    try:
        with time_limit(TIMEOUT_SECONDS):
            if kind == "eq":
                truth = sp.solveset(sp.Eq(p.lhs, p.rhs), var, domain)
            else:
                truth = domain
                for c in p:
                    truth = truth & sp.solveset(c, var, domain)
    except Exception:
        return None
    if isinstance(truth, (sp.ConditionSet, sp.ImageSet)) or truth.has(sp.ImageSet):
        return None
    if isinstance(truth, sp.FiniteSet) and len(truth) > 6:
        return None
    exact, partial, parsed_opts = [], [], []
    for i, opt in enumerate(options):
        if xint:  # (3; 0) -> 3
            opt = re.sub(r"\(\s*([^;()]+?)\s*;\s*0\s*\)", r"\1", opt)
        os_ = _option_solution_set(opt, var)
        if os_ is None:
            continue
        parsed_opts.append(i)
        if _sets_equal(os_, truth):
            exact.append(i)
        elif _is_subset(os_, truth):
            partial.append(i)
    if key not in parsed_opts:
        return None
    detail = {"type": "substitute" if assign and kind == "eq" and p.lhs == var
              else "solve", "target": s, "truth": str(truth)}
    if domain is not sp.S.Reals and key not in exact:
        # the positive-base convention is not universal (x = ±27 for
        # x^(2/3) = 9 over the reals): a key matching the real-line answer
        # is accepted, never flagged
        try:
            with time_limit(TIMEOUT_SECONDS):
                real = sp.solveset(sp.Eq(p.lhs, p.rhs), var, sp.S.Reals) \
                    if kind == "eq" else None
            os_ = _option_solution_set(options[key], var)
            if real is not None and os_ is not None and _sets_equal(os_, real):
                return "verified", dict(detail, truth=str(real),
                                        reason="real-line convention"), [key]
        except Exception:
            pass
    if key in exact:
        verdict = "MULTIPLE_CORRECT" if len(exact) > 1 else "verified"
        return verdict, detail, exact
    context = str(var) == "n" or re.search(
        r"natural|positive|length|width|side|\bage\b|time|number|valid|reject"
        r"|domain|term|area|distance|price|cost|real-world|final answer", stem, re.I)
    if key in partial and context:
        # a context rule (natural numbers, lengths) may reject a root
        return ("verified" if not exact else "SKIPPED"), detail, [key]
    if not context:
        partial = []
    if len(parsed_opts) < 3:
        return None
    if len(exact) == 1:
        return "MISMATCH", detail, exact
    if len(exact) > 1:
        return "MULTIPLE_CORRECT", detail, exact
    if not exact and not partial and len(parsed_opts) == len(options):
        return "NO_CORRECT", detail, []
    return "SKIPPED", detail, exact


def _span_symbols(span):
    """Free symbols of a span before evaluation cancels any of them."""
    try:
        with time_limit(TIMEOUT_SECONDS):
            e = parse_expr(_over_sides(span).split("=")[-1].replace("[", "(")
                           .replace("]", ")"), local_dict=dict(_LOCALS),
                           transformations=_TRANSFORMS, evaluate=False)
        return e.free_symbols
    except Exception:
        return set()


def _pick_target(stem_n, parsed, trigger, option_symbols=None):
    """The symbolic expression the question is about."""
    cands = []
    for s, kind, p in parsed:
        if kind == "expr" and p.free_symbols:
            cands.append((s, p))
        elif kind == "eq" and p.free_symbols:
            if p.rhs == 0:
                cands.append((s, p.lhs))
            elif isinstance(p.lhs, (sp.Symbol, sp.Function)) or \
                    re.match(r"^\s*[a-zA-Z](\([a-z]\))?\s*=", s):
                cands.append((s, p.rhs))
    if len(cands) == 1:
        return cands[0]
    if option_symbols is not None:
        fit = [c for c in cands if _span_symbols(c[0]) == option_symbols]
        if len(fit) == 1:
            return fit[0]
    if trigger:
        pos = trigger.end()
        after = [c for c in cands if stem_n.find(c[0], pos) >= 0]
        if len(after) == 1:
            return after[0]
    return None


def _option_expr(opt):
    s = normalise(strip_explanation(opt))
    if re.search(r"[A-Za-z]{3,}", re.sub(r"sqrt|cbrt|pi|log|sin|cos|tan|over"
                                          r"|alpha|beta|theta|gamma|phi|rad",
                                          "", s)):
        return None
    if s.count("=") > 1 or "_" in s:
        return None
    if "=" in s:
        parts = s.split("=")
        if parts[-1].strip() in ("0",):
            s = parts[0]
        else:
            s = parts[-1]
    s = _over(s)
    try:
        return parse_math(s)
    except ParseFailure:
        return None


def _fully_factored(e):
    """An (unevaluated) product of primitive factors, as many as factor() finds."""
    def n_factors(x):
        return sum(1 for f in sp.Mul.make_args(x) if not f.is_number)
    def primitive(f):
        base = f.base if f.is_Pow else f
        try:
            return abs(sp.Poly(base).content()) == 1  # (3x - 6) still hides a 3
        except Exception:
            return True
    try:
        with time_limit(TIMEOUT_SECONDS):
            factors = [f for f in sp.Mul.make_args(e) if not f.is_number]
            return n_factors(e) >= n_factors(sp.factor(e)) and all(
                primitive(f) for f in factors)
    except Exception:
        return False


def handle_equivalence(stem, stem_n, parsed, options, key):
    trig = re.search(r"factoris|factoriz|factors? (as|to)|expand|expanding"
                     r"|expansion|simplif|equivalent|multiply out|identical"
                     r"|a face of|rewrit|written as|equals|becomes|in the form",
                     stem_n, re.I)
    if not trig:
        return None
    exprs = [_option_expr(o) for o in options]
    osyms = set()
    for e in exprs:
        if e is not None:
            osyms |= e.free_symbols
    target = _pick_target(stem_n, parsed, trig, osyms)
    if target is None:
        return None
    span, expr = target
    if not expr.free_symbols or "_" in span:
        return None
    if "÷" in stem and span.count("/") > 1:
        return None  # "a/b ÷ c/d": grouping is ambiguous once flattened
    if span.startswith("(") and re.search(r"[A-Za-z]+\s+of\s*$", stem_n[:stem_n.find(span)]):
        return None  # "Sine of (alpha + beta)": the function is in prose
    parsed_opts = [i for i, e in enumerate(exprs) if e is not None]
    if key not in parsed_opts or len(parsed_opts) < 3:
        return None
    # options must speak about the same unknowns as the target
    tsyms = expr.free_symbols | _span_symbols(span)
    if any(not exprs[i].free_symbols <= tsyms for i in parsed_opts):
        return None
    if sum(1 for i in parsed_opts if exprs[i].free_symbols) * 2 < len(parsed_opts):
        return None
    equiv = []
    for i in parsed_opts:
        r = equivalent(expr, exprs[i])
        if r is None:
            return None
        if r:
            equiv.append(i)
    kind = "factorise" if re.search(r"factor", trig.group(), re.I) else (
        "exponent_laws" if re.search(r"\^|sqrt", span)
        and not re.search(r"\s[+-]\s", re.sub(r"\([^()]*\)", "", span))
        else "equivalence")
    detail = {"type": kind, "target": span}
    if _NOT.search(stem):
        non = [i for i in parsed_opts if i not in equiv]
        if len(parsed_opts) != len(options):
            return None
        if key in non and len(non) == 1:
            return "verified", detail, non
        if key in non:
            return "MULTIPLE_CORRECT", detail, non
        if len(non) == 1:
            return "MISMATCH", detail, non
        return "SKIPPED", detail, non
    if kind == "factorise" and len(equiv) > 1:
        # keep the fully factorised ones (2(x² - 4) is not "fully" factorised)
        full = []
        for i in equiv:
            raw = _over(normalise(strip_explanation(options[i])).split("=")[0])
            try:
                ue = parse_expr(raw.replace("[", "(").replace("]", ")"),
                                local_dict=dict(_LOCALS),
                                transformations=_TRANSFORMS, evaluate=False)
            except Exception:
                ue = exprs[i]
            if _fully_factored(ue):
                full.append(i)
        if full:
            equiv = full
    verdict, idx = decide(key, equiv, parsed=parsed_opts,
                          n_options=len(options))
    return verdict, detail, idx


def handle_evaluate(stem, stem_n, parsed, options, key):
    if not re.search(r"value|evaluat|calculat|equals|equal to|simplif|gives"
                     r"|works out|comes to|\bis\s*[:?]?\s*$|=\s*[:?]?\s*$",
                     stem_n, re.I):
        return None
    ops = r"[+*/^]|(?<!^)-|sqrt|log|sin|cos|tan"
    nums = []
    for s, kind, p in parsed:
        if kind == "expr" and _is_number(p) and re.search(ops, s.strip()):
            nums.append((s, p))
        elif kind == "eq" and _is_number(p.rhs) and isinstance(p.lhs, sp.Symbol) \
                and re.search(ops, s.split("=", 1)[1].strip()):
            nums.append((s, p.rhs))
    if len(nums) != 1:
        return None
    span, expr = nums[0]
    if "÷" in stem and span.count("/") > 1:
        return None
    # the expression must BE the question: "<expr> evaluates to:",
    # "the value of <expr> is:", "evaluate <expr>"
    pos = stem_n.find(span)
    before = stem_n[:pos].lower()
    after = stem_n[pos + len(span):].strip().lower()
    lead = re.search(r"(value of|evaluate|calculate|simplify|work out|expression)\s*$",
                     before)
    if re.match(r"in (?:its )?(?:simplest |exact )?(?:surd |exponential )?form\s+is", after):
        lead = True
    after = re.sub(r"^in (?:its )?(?:simplest |exact )?(?:surd |exponential )?form\s+", "", after)
    tail = re.fullmatch(r"[,)]?\s*(?:which\s+)?(?:evaluates to|equals|simplifies to"
                        r"|is equal to|is|=|works out to|comes to|gives|expands and "
                        r"simplifies to)?\s*[:?.]?", after)
    if not tail or not (lead or re.match(r"\s*(which\s+)?(evaluates|equals|simplifies"
                                         r"|is equal|works out|comes to|=|expands)",
                                         after)):
        return None
    target = to_float(expr)
    if target is None:
        return None
    kind = "exponent_laws" if re.search(r"\^|sqrt", span) else "evaluate"
    detail = {"type": kind, "target": span, "truth": str(sp.nsimplify(expr))
              if expr.is_Rational else f"{target:.6g}"}
    return _numeric_verdict(target, options, key, detail,
                            approx=bool(_APPROX.search(stem)),
                            symbolic=expr,
                            exact=bool(re.search(r"\bexact|surd form", stem, re.I)))


def _numeric_verdict(target, options, key, detail, approx=False, symbolic=None,
                     exact=False, dim=None):
    strict, loose, unparsed = match_numeric(target, options, approx, dim)
    if exact:
        # "the exact value": a rounded decimal such as 0,26 is not it
        for i in list(strict):
            nv = numeric_option(options[i])
            if nv and nv[1] and abs(nv[0] - target) > 1e-9 * max(1, abs(target)):
                strict.remove(i)
    parsed_opts = [i for i in range(len(options)) if i not in unparsed]
    if symbolic is not None:
        # exact options like 2√2 or (√6 − √2)/4 compared exactly as well
        for i in list(unparsed):
            e = _option_expr(options[i])
            if e is not None and _is_number(e):
                parsed_opts.append(i)
                if equivalent(symbolic, e):
                    strict.append(i)
                    loose.append(i)
    if key not in parsed_opts or len(parsed_opts) < 3:
        return None
    verdict, idx = decide(key, sorted(set(strict)), candidates=sorted(set(loose)),
                          parsed=sorted(set(parsed_opts)), n_options=len(options))
    return verdict, detail, idx


_SUB_TRIGGER = re.compile(
    r"\b(?:if|when|for|given|where|at|with)\s+([a-z])\s*=\s*(-?[\d.]+(?:/\d+)?)",
    re.I)


def handle_substitute(stem, stem_n, parsed, options, key):
    assign = _assignments(parsed)
    if not assign or not _SUB_TRIGGER.search(stem_n) or not re.search(
            r"\bvalue\b|\bgives? [a-z] =\s*[:?]?$|evaluat|\bequals?\s*[:?]?$",
            stem_n, re.I):
        return None
    targets = []
    for s, kind, p in parsed:
        if kind == "expr" and p.free_symbols and p.free_symbols <= set(assign):
            targets.append((s, p))
        elif kind == "eq" and not (isinstance(p.lhs, sp.Symbol) and _is_number(p.rhs)):
            if isinstance(p.lhs, sp.Symbol) and p.rhs.free_symbols \
                    and p.rhs.free_symbols <= set(assign):
                targets.append((s, p.rhs))
    if len(targets) != 1:
        return None
    span, expr = targets[0]
    val = expr.subs(assign)
    if not _is_number(val):
        return None
    target = to_float(val)
    if target is None:
        return None
    detail = {"type": "substitute", "target": span,
              "assign": {str(k): str(v) for k, v in assign.items()},
              "truth": str(val)}
    return _numeric_verdict(target, options, key, detail,
                            approx=bool(_APPROX.search(stem)), symbolic=val)


def handle_function_value(stem, stem_n, parsed, options, key):
    """f(x) = ... ; f(3)  and  T_n = ... ; T_50."""
    m = re.search(r"\b([a-zA-Z])\(([a-z])\)\s*=\s*([^,;:]+?)(?:,|;|:|\s+the\b|\s+then\b|$)",
                  stem_n)
    m2 = re.search(r"\bT_\(?n\)?\s*=\s*([^,;:]+?)(?:,|;|:|\s+the\b|$)", stem_n)
    if m:
        fname, var, body = m.group(1), m.group(2), m.group(3)
        calls = re.findall(r"\b" + fname + r"\((-?[\d.]+(?:/\d+)?)\)", stem_n)
    elif m2:
        var, body = "n", m2.group(1)
        calls = re.findall(r"\bT_\(?(\d+)\)?|\bterm (\d+)\b", stem_n)
        calls = [a or b for a, b in calls]
    else:
        return None
    if len(set(calls)) != 1:
        return None
    try:
        expr = parse_math(body)
        arg = parse_math(calls[0])
    except ParseFailure:
        return None
    if expr.free_symbols != {sp.Symbol(var)}:
        return None
    val = expr.subs(sp.Symbol(var), arg)
    target = to_float(val)
    if target is None:
        return None
    detail = {"type": "substitute", "target": body.strip(),
              "assign": {var: str(arg)}, "truth": str(val)}
    return _numeric_verdict(target, options, key, detail, symbolic=val)


_NUM = r"(\d+(?:\.\d+)?)"


_PCT_GUARD = re.compile(
    r"further|\bthen\b|\beach\b|per month|monthly|\byears?\b|compound|interest"
    r"|simple|p\.a\.|annum|\bwhy\b|because|wrong|instead|reverse|check|\bstep"
    r"|found by|\bhow\b|\bwhich\b|\bper\b|percentage|still|remain|twice|double")


def _numbers(s):
    """Numbers in normalised text as (value, is_percent)."""
    out = []
    for m in re.finditer(r"(?<![\w.])(\d+(?:\.\d+)?)(\s*%)?", s):
        out.append((float(m.group(1)), bool(m.group(2))))
    return out


def handle_percent(stem, stem_n, parsed, options, key):
    s = re.sub(r"\s+", " ", stem_n.strip().lower())
    if _PCT_GUARD.search(s):
        return None
    nums = _numbers(s)
    pcts = [v for v, is_pct in nums if is_pct]
    others = [v for v, is_pct in nums if not is_pct]
    if len(others) != 1 or len(pcts) > 1:
        return None
    y = others[0]
    x = pcts[0] if pcts else None
    asks_price = re.search(r"(sale|new|final|till|selling|total) price|leaves|sells"
                           r"|\bpay\b|\bcosts?\b|price is|becomes", s)
    value = None
    if "vat" in s:
        if x not in (None, 15.0):
            return None
        if re.search(r"before vat|excluding vat|excl\.? vat|excl\.? of vat", s) \
                and re.search(r"with (15% )?vat|including vat|incl\.? vat|plus vat"
                              r"|till price|selling price|for\s*[:?]?$", s):
            value = y * 1.15
        elif re.search(r"includ\w* vat|incl\.? vat|vat[- ]inclusive", s) \
                and re.search(r"(price|amount) (before|excluding|without) vat", s):
            value = y / 1.15
        elif re.search(r"\bthe vat(?: amount)?(?: at 15%)?(?: on [^:?]*)? is\s*[:?]?$", s):
            value = y * 0.15
        else:
            return None
    elif x is None:
        return None
    elif re.search(r"\boff\b|discount|reduc|decreas|\bless\b|\bsale\b", s):
        if re.search(r"(discount|saving|amount off)(?: amount)? is\s*[:?]?$", s):
            value = y * x / 100
        elif asks_price or re.search(r"decreas\w* [\d.]+ by [\d.]+ ?%", s):
            value = y * (1 - x / 100)
        else:
            return None
    elif re.search(r"increas|\brises?\b|\braised?\b|mark-?up|\bplus\b", s):
        if asks_price or re.search(r"increas\w* [\d.]+ by [\d.]+ ?%", s):
            value = y * (1 + x / 100)
        else:
            return None
    elif re.search(r"%(?: [a-z]+){0,3} (?:of|on)\b", s) and re.search(
            r"(?:\bis|equals|which is|amounts to|comes to)\s*[:?]?$", s):
        value = y * x / 100
    if value is None:
        return None
    detail = {"type": "percent", "target": stem.strip(), "truth": f"{value:.2f}"}
    return _numeric_verdict(value, options, key, detail,
                            approx=bool(_APPROX.search(stem)))


_WORD_NUM = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
             "seven": 7, "eight": 8, "nine": 9, "ten": 10, "twelve": 12}
_PERIODS = {"annually": 1, "yearly": 1, "half-yearly": 2, "semi-annually": 2,
            "quarterly": 4, "monthly": 12, "weekly": 52, "daily": 365}


def handle_finance(stem, stem_n, parsed, options, key):
    """Simple / compound growth and nominal-to-effective rates."""
    s = re.sub(r"\s+", " ", stem_n.strip().lower())
    for w, n in _WORD_NUM.items():
        s = re.sub(r"\b" + w + r" years?\b", f"{n} years", s)
    if re.search(r"deposit|instal|hire|inflation|depreciat|\bwhy\b|because|wrong"
                 r"|instead|\bstep|formula|found by|\bhow\b|which|principal must"
                 r"|\brate is\b|each year|year (one|two|three)|in year|months'", s):
        return None
    comp = re.search(r"compounded (annually|yearly|half-yearly|semi-annually|quarterly"
                     r"|monthly|weekly|daily)", s)
    rates = re.findall(r"(\d+(?:\.\d+)?)\s*%", s)
    if len(rates) != 1:
        return None
    i = float(rates[0]) / 100
    if "effective" in s:
        if not comp:
            return None
        m = _PERIODS[comp.group(1)]
        value = ((1 + i / m) ** m - 1) * 100
        detail = {"type": "finance", "target": "effective rate",
                  "truth": f"{value:.4f}%"}
        return _numeric_verdict(value, options, key, detail,
                                approx=bool(_APPROX.search(stem)))
    kind = "simple" if "simple" in s else ("compound" if comp or "compound" in s
                                           else None)
    if kind is None:
        return None
    years = re.findall(r"(\d+(?:\.\d+)?) years?\b", s)
    money = [float(v) for v, pct in _numbers(s) if not pct]
    if len(years) != 1:
        return None
    n = float(years[0])
    money = [v for v in money if v != n]
    if len(money) != 1:
        return None
    p = money[0]
    if kind == "simple":
        amount = p * (1 + i * n)
    else:
        m = _PERIODS[comp.group(1)] if comp else 1
        amount = p * (1 + i / m) ** (m * n)
    if re.search(r"(grows|accumulates|amounts) to|is worth|becomes|final amount"
                 r"|accumulated amount|future value", s):
        value = amount
    elif re.search(r"interest (earned|is|amounts)|the interest\s*[:?]?$", s):
        value = amount - p
    else:
        return None
    detail = {"type": "finance", "target": f"{kind} P={p} i={i} n={n}",
              "truth": f"{value:.2f}"}
    return _numeric_verdict(value, options, key, detail,
                            approx=bool(_APPROX.search(stem)))


def _number_list(s):
    """'5; 8; 11; 14' / '4, 6, 7, 9, 14' -> [Rational, ...] (3+ items)."""
    m = re.search(r"(-?\d+(?:\.\d+)?(?:\s*[;,]\s*-?\d+(?:\.\d+)?){2,})"
                  r"(\s*[;,]\s*\.\.\.)?", s)
    if not m:
        return None, None
    vals = [sp.Rational(v) for v in re.split(r"\s*[;,]\s*", m.group(1))]
    return vals, m


def handle_sequence(stem, stem_n, parsed, options, key):
    s = re.sub(r"\s+", " ", stem_n.strip())
    low = s.lower()
    if re.search(r"\bwhy\b|because|picture|found by|\bstep|means|\bhow\b", low):
        return None
    vals, m = _number_list(s)
    series = re.search(r"(-?\d+(?:\.\d+)?(?:\s*\+\s*-?\d+(?:\.\d+)?){2,})\s*\+\s*\.\.\.", s)
    if series:
        vals = [sp.Rational(v) for v in re.split(r"\s*\+\s*", series.group(1))]
    if not vals or len(vals) < 3:
        return None
    diffs = [b - a for a, b in zip(vals, vals[1:])]
    arith = len(set(diffs)) == 1
    ratios = [b / a for a, b in zip(vals, vals[1:])] if all(vals) else []
    geom = bool(ratios) and len(set(ratios)) == 1
    detail = {"type": "sequence", "target": "; ".join(str(v) for v in vals)}
    if series:
        mm = re.search(r"sum of the first (\d+|[a-z]+) terms", low)
        if not mm:
            return None
        n = int(mm.group(1)) if mm.group(1).isdigit() else _WORD_NUM.get(mm.group(1))
        if not n:
            return None
        a = vals[0]
        if arith:
            total = sp.Rational(n, 2) * (2 * a + (n - 1) * diffs[0])
        elif geom:
            r = ratios[0]
            total = a * (r ** n - 1) / (r - 1)
        else:
            return None
        detail["truth"] = str(total)
        return _numeric_verdict(float(total), options, key, detail)
    if not re.search(r"sequence|pattern|terms?\b", low):
        return None
    if re.search(r"(common|constant) difference|\bd\b is|\bd\s*[:?]?$", low) \
            and "second" not in low:
        if not arith:
            return None
        truth = diffs[0]
    elif re.search(r"(common )?ratio|\br\b is", low):
        if not geom:
            return None
        truth = ratios[0]
    elif re.search(r"general term|t_\(?n\)?\s*=?\s*[:?]?$|formula for", low):
        # each option T_n = ... must reproduce the listed terms
        n = sp.Symbol("n")
        hits, parsed_opts = [], []
        for idx, o in enumerate(options):
            on = normalise(strip_explanation(o))
            on = re.sub(r"^\s*T_\(?n\)?\s*=\s*", "", on)
            try:
                e = parse_math(on)
            except ParseFailure:
                continue
            if not e.free_symbols <= {n}:
                continue
            parsed_opts.append(idx)
            if all(sp.simplify(e.subs(n, k + 1) - v) == 0
                   for k, v in enumerate(vals)):
                hits.append(idx)
        if len(parsed_opts) < 3 or key not in parsed_opts:
            return None
        verdict, idx = decide(key, hits, parsed=parsed_opts,
                              n_options=len(options))
        detail["type"] = "sequence"
        return verdict, detail, idx
    else:
        return None
    detail["truth"] = str(truth)
    return _numeric_verdict(float(truth), options, key, detail, symbolic=truth)


def handle_sum(stem, stem_n, parsed, options, key):
    s = re.sub(r"\s+", " ", stem_n.strip())
    m = re.search(r"sum of \((.+?)\) (?:for|from) ([a-z]) = (-?\d+) to (-?\d+)", s)
    if not m:
        return None
    try:
        body = parse_math(m.group(1))
    except ParseFailure:
        return None
    k = sp.Symbol(m.group(2))
    if not body.free_symbols <= {k}:
        return None
    total = sp.summation(body, (k, int(m.group(3)), int(m.group(4))))
    detail = {"type": "sequence", "target": m.group(0), "truth": str(total)}
    return _numeric_verdict(float(total), options, key, detail, symbolic=total)


def handle_statistics(stem, stem_n, parsed, options, key):
    s = re.sub(r"\s+", " ", stem_n.strip())
    low = s.lower()
    m = re.search(r"\b(mean|median|range|variance|standard deviation) of "
                  r"(?:the (?:data|values|marks|scores) )?(-?\d)", low)
    if not m or re.search(r"\band\b (the )?(mean|median|mode|range|variance)"
                          r"|\bwhy\b|because|means|deviations", low):
        return None
    vals, lm = _number_list(s[m.start(2):])
    if not vals or lm.start() != 0:
        return None
    stat = m.group(1)
    nvals = len(vals)
    mean = sum(vals) / nvals
    ordered = sorted(vals)
    if stat == "mean":
        truth, alt = mean, None
    elif stat == "median":
        mid = nvals // 2
        truth = ordered[mid] if nvals % 2 else (ordered[mid - 1] + ordered[mid]) / 2
        alt = None
    elif stat == "range":
        truth, alt = ordered[-1] - ordered[0], None
    else:
        ss = sum((v - mean) ** 2 for v in vals)
        pop, samp = ss / nvals, ss / (nvals - 1)
        if stat == "variance":
            truth, alt = pop, samp
        else:
            truth, alt = sp.sqrt(pop), sp.sqrt(samp)
    detail = {"type": "statistics", "target": f"{stat} of {vals}",
              "truth": f"{float(truth):.6g}"}
    res = _numeric_verdict(float(truth), options, key, detail,
                           approx=bool(_APPROX.search(stem)))
    if res and res[0] != "verified" and alt is not None:
        # CAPS uses the population formula; a sample-formula key is not flagged
        alt_res = _numeric_verdict(float(alt), options, key, detail,
                                   approx=bool(_APPROX.search(stem)))
        if alt_res and alt_res[0] == "verified":
            return "SKIPPED", dict(detail, reason="sample vs population"), []
    return res


def _ratio_tuple(text):
    s = normalise(strip_explanation(text))
    parts = re.split(r"\s*:\s*", s.strip())
    if len(parts) < 2:
        return None
    vals = []
    for p in parts:
        p = re.sub(r"\s*[A-Za-z]+\s*$", "", p.strip())
        try:
            vals.append(sp.Rational(p))
        except Exception:
            return None
    return tuple(vals)


def handle_ratio(stem, stem_n, parsed, options, key):
    s = re.sub(r"\s+", " ", stem_n.strip())
    m = re.search(r"(?:simplif\w*|simplest form)[^:]*?" + _NUM
                  + r"\s*:\s*" + _NUM + r"(?:\s*:\s*" + _NUM + r")?", s, re.I)
    if m and re.search(r"simplest|simplif", s, re.I) and re.search(
            r"ratio", s, re.I):
        nums = [sp.Rational(x) for x in m.groups() if x]
        g = sp.gcd_list(nums)
        truth = tuple(n / g for n in nums)
        hits, parsed_opts = [], []
        for i, o in enumerate(options):
            t = _ratio_tuple(o)
            if t is None:
                continue
            parsed_opts.append(i)
            if t == truth:
                hits.append(i)
        if key not in parsed_opts or len(parsed_opts) < 3:
            return None
        detail = {"type": "ratio", "target": m.group(0),
                  "truth": " : ".join(str(x) for x in truth)}
        verdict, idx = decide(key, hits, parsed=parsed_opts,
                              n_options=len(options))
        return verdict, detail, idx
    m = re.search(r"(?:shar\w*|divid\w*|split\w*) " + _NUM
                  + r" in the ratio ((?:\d+\s*:\s*)+\d+)", s, re.I) or \
        re.search(r"of " + _NUM + r" are shared in the ratio ((?:\d+\s*:\s*)+\d+)",
                  s, re.I)
    if not m:
        return None
    total = sp.Rational(m.group(1))
    parts = [sp.Rational(x) for x in re.split(r"\s*:\s*", m.group(2))]
    shares = [total * p / sum(parts) for p in parts]
    rest = s[m.end():].lower()
    if re.search(r"one part|each part", rest):
        target = total / sum(parts)
    elif re.search(r"middle share", rest) and len(shares) == 3:
        target = shares[1]
    elif re.search(r"(largest|biggest|greatest) share", rest):
        target = max(shares)
    elif re.search(r"(smallest|least) share", rest):
        target = min(shares)
    else:
        return None
    detail = {"type": "ratio", "target": m.group(0), "truth": str(target)}
    return _numeric_verdict(float(target), options, key, detail)


_ANGLE_VAR = r"(?:theta|alpha|beta|x|A|B|C|P|Q|R)"


def handle_trig_angle(stem, stem_n, parsed, options, key):
    """'cos θ = 2/5, so θ is' -> the acute angle, in degrees."""
    s = re.sub(r"\s+", " ", stem_n.strip())
    m = re.search(r"\b(sin|cos|tan)\s*\(?\s*(" + _ANGLE_VAR + r")\s*\)?\s*=\s*"
                  r"(\d+(?:\.\d+)?(?:\s*/\s*\d+(?:\.\d+)?)?)\b(?!\s*[*/^])", s)
    if not m:
        return None
    rest = s[m.end():]
    if not re.search(r"(?:so|then|,)?\s*(?:the angle\s*)?\b" + m.group(2)
                     + r"\b\s*(?:is|=|equals)\s*(?:about|approximately)?\s*[:?]?\s*$",
                     rest):
        return None
    if re.search(r"360|180|general|second|all solutions|obtuse|reflex|quadrant", s):
        return None
    try:
        v = parse_math(m.group(3))
    except ParseFailure:
        return None
    fv = to_float(v)
    if fv is None or fv <= 0 or (m.group(1) != "tan" and fv > 1):
        return None
    inv = {"sin": sp.asin, "cos": sp.acos, "tan": sp.atan}[m.group(1)]
    deg = to_float(inv(v) * 180 / sp.pi)
    detail = {"type": "trig_angle", "target": m.group(0), "truth": f"{deg:.4f}"}
    return _numeric_verdict(deg, options, key, detail, approx=True)


_POINT = r"\(\s*(-?\d+(?:\.\d+)?)\s*;\s*(-?\d+(?:\.\d+)?)\s*\)"


def _line_option(opt):
    """'y = −4/3 x + 1/3' -> sympy expr in x, or None."""
    s = normalise(strip_explanation(opt))
    m = re.fullmatch(r"\s*y\s*=\s*(.+)", s)
    if not m:
        return None
    try:
        e = parse_math(m.group(1))
    except ParseFailure:
        return None
    return e if e.free_symbols <= {sp.Symbol("x")} else None


def _point_option(opt):
    m = re.fullmatch(r"\s*[A-Z]?\s*" + _POINT + r"\s*", normalise(strip_explanation(opt)))
    if not m:
        return None
    return sp.Rational(m.group(1)), sp.Rational(m.group(2))


def handle_analytic(stem, stem_n, parsed, options, key):
    """Gradient, midpoint, distance and line through two points."""
    s = re.sub(r"\s+", " ", stem_n.strip())
    low = s.lower()
    pts = [(sp.Rational(a), sp.Rational(b)) for a, b in re.findall(_POINT, s)]
    if len(pts) != 2 or re.search(r"\bwhy\b|because|\bstep|formula|found by"
                                  r"|perpendicular|parallel|\bhow\b|inclination|angle", low):
        return None
    (x1, y1), (x2, y2) = pts
    x = sp.Symbol("x")
    detail = {"type": "analytic", "target": f"{pts}"}
    if re.search(r"\b(the )?line (through|joining)\b.*\bis\s*[:?]?$|equation of the line", low):
        if x1 == x2:
            return None
        grad = (y2 - y1) / (x2 - x1)
        truth = grad * (x - x1) + y1
        hits, parsed_opts = [], []
        for i, o in enumerate(options):
            e = _line_option(o)
            if e is None:
                continue
            parsed_opts.append(i)
            if sp.simplify(e - truth) == 0:
                hits.append(i)
        if key not in parsed_opts or len(parsed_opts) < 3:
            return None
        detail["truth"] = f"y = {sp.expand(truth)}"
        verdict, idx = decide(key, hits, parsed=parsed_opts, n_options=len(options))
        return verdict, detail, idx
    if re.search(r"\b(?:the )?midpoint(?: m)?(?: of [a-z]+)?(?: is| are)\s*[:?]?$"
                 r"|coordinates of (?:the )?midpoint(?: m)?(?: of [a-z]+)? (?:is|are)\s*[:?]?$",
                 low):
        truth = ((x1 + x2) / 2, (y1 + y2) / 2)
        hits, parsed_opts = [], []
        for i, o in enumerate(options):
            pt = _point_option(o)
            if pt is None:
                continue
            parsed_opts.append(i)
            if pt == truth:
                hits.append(i)
        if key not in parsed_opts or len(parsed_opts) < 3:
            return None
        detail["truth"] = f"({truth[0]}; {truth[1]})"
        verdict, idx = decide(key, hits, parsed=parsed_opts, n_options=len(options))
        return verdict, detail, idx
    if re.search(r"\bgradient\b", low) and re.search(r"(is|equals)\s*[:?]?$", low):
        if x1 == x2:
            return None
        truth = (y2 - y1) / (x2 - x1)
    elif re.search(r"\b(distance|length)\b", low) and re.search(r"(is|equals)\s*[:?]?$", low):
        truth = sp.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    else:
        return None
    detail["truth"] = str(truth)
    return _numeric_verdict(to_float(truth), options, key, detail,
                            approx=bool(_APPROX.search(stem)), symbolic=truth)


_UNITS = {"mm": ("length", sp.Rational(1, 1000)), "cm": ("length", sp.Rational(1, 100)),
          "m": ("length", 1), "km": ("length", 1000),
          "ml": ("volume", sp.Rational(1, 1000)), "l": ("volume", 1),
          "kl": ("volume", 1000), "mg": ("mass", sp.Rational(1, 1000000)),
          "g": ("mass", sp.Rational(1, 1000)), "kg": ("mass", 1), "t": ("mass", 1000)}
_UNIT_WORDS = {"millimetres": "mm", "centimetres": "cm", "metres": "m",
               "kilometres": "km", "millilitres": "ml", "litres": "l",
               "kilolitres": "kl", "grams": "g", "kilograms": "kg", "tonnes": "t"}


def _unit(tok):
    tok = tok.lower().replace("ℓ", "l").rstrip(".")
    tok = _UNIT_WORDS.get(tok, _UNIT_WORDS.get(tok + "s", tok))
    return tok if tok in _UNITS else None


def handle_units(stem, stem_n, parsed, options, key):
    """'4 500 mm expressed in metres is' -> 4,5."""
    s = re.sub(r"\s+", " ", stem_n.strip())
    m = re.search(r"(\d+(?:\.\d+)?)\s*([a-zA-Zℓ]+)\b.*?\b(?:in|into|to|as)\s+([a-zA-Zℓ]+)"
                  r"(?:\s+(?:that|this|it))?\s*(?:is|equals|gives)?\s*[:?]?\s*$", s)
    if not m or len(_numbers(s)) != 1:
        return None
    u1, u2 = _unit(m.group(2)), _unit(m.group(3))
    if not u1 or not u2 or u1 == u2 or _UNITS[u1][0] != _UNITS[u2][0]:
        return None
    truth = sp.Rational(m.group(1)) * _UNITS[u1][1] / _UNITS[u2][1]
    detail = {"type": "units", "target": f"{m.group(1)} {u1} -> {u2}",
              "truth": str(truth)}
    return _numeric_verdict(float(truth), options, key, detail, symbolic=truth)


def handle_probability(stem, stem_n, parsed, options, key):
    """'Of 60 learners, 36 ride taxis. P(taxi) is' -> 36/60."""
    s = re.sub(r"\s+", " ", stem_n.strip())
    low = s.lower()
    if not re.search(r"probability|\bp\(|proportion|relative frequency|percentage", low):
        return None
    if re.search(r"\bnot\b|\bno\b|\bwhy\b|because|\bboth\b|\band\b.*\band\b"
                 r"|\bor\b|\bthen\b|replace|\bafter\b|\btwo\b|\bstep", low):
        return None
    m = re.search(r"\bof (?:the |these |those )?(\d+) ([a-z\-]+)(?: [a-z\-]+){0,4}, (\d+) "
                  r"((?:[a-z\-]+ ){0,2}[a-z\-]+)", low)
    if not m or len(_numbers(low)) != 2:
        return None
    n, k = int(m.group(1)), int(m.group(3))
    if not 0 <= k <= n or n == 0:
        return None
    event_words = [w for w in m.group(4).split() if len(w) >= 4]
    tail = low[m.end():]
    if not event_words or not any(w[:4] in tail for w in event_words):
        return None
    truth = sp.Rational(k, n)
    if "percentage" in low:
        truth *= 100
    detail = {"type": "probability", "target": m.group(0), "truth": str(truth)}
    res = _numeric_verdict(float(truth), options, key, detail,
                           approx=bool(_APPROX.search(stem)), symbolic=truth)
    if res is None and "percentage" not in low and "proportion" in low:
        return _numeric_verdict(float(truth) * 100, options, key, detail,
                                approx=bool(_APPROX.search(stem)))
    return res


def handle_rate(stem, stem_n, parsed, options, key):
    """'At a tariff of R2,80 per unit, what did June's 480 units cost?'"""
    s = re.sub(r"\s+", " ", stem_n.strip())
    low = s.lower()
    m = re.search(r"(\d+(?:\.\d+)?) (?:rand )?per ([a-z]+)", low)
    nums = _numbers(low)
    if not m or len(nums) != 2 or any(p for _, p in nums):
        return None
    if not re.search(r"(costs?|pay|charged?|price|bill)\s*[:?]?$", low) or re.search(
            r"\bwhy\b|because|\bstep|\beach\b|plus|fixed|basic|\bfee\b|vat"
            r"|discount|\bhow many\b|\bper\b.*\bper\b", low):
        return None
    unit = m.group(2)
    other = [v for v, _ in nums if v != float(m.group(1))]
    if len(other) != 1:
        return None
    q = re.search(re.escape(f"{other[0]:g}") + r"\s*([a-z]+)", low)
    if not q or q.group(1)[:4] != unit[:4]:
        return None
    value = float(m.group(1)) * other[0]
    detail = {"type": "rate", "target": f"{m.group(1)} per {unit} x {other[0]:g}",
              "truth": f"{value:.2f}"}
    return _numeric_verdict(value, options, key, detail)


def handle_mensuration(stem, stem_n, parsed, options, key):
    """Circle, rectangle, triangle and cylinder area / perimeter / volume."""
    s = re.sub(r"\s+", " ", stem_n.strip())
    low = s.lower()
    if re.search(r"\bwhy\b|because|\bstep|instead|formula|twice|double|\bhow many\b"
                 r"|remov|excluding|minus|\bless\b|paint|tiles?\b|\bcost|\bboxes"
                 r"|\bbags|doubl|\bk\b|scale|multipl", low):
        return None
    pi = sp.pi
    mp = re.search(r"(?:pi|π) (?:as|=|of) (\d+\.\d+)", low)
    nums = [v for v, pct in _numbers(low) if not pct]
    if mp:
        pi = sp.Rational(mp.group(1))
        nums.remove(float(mp.group(1)))
    frac = 1
    if "semicircular" in low or "semicircle" in low or "half" in low:
        frac = sp.Rational(1, 2)
    elif "quarter" in low:
        frac = sp.Rational(1, 4)
    target, dim = None, None
    if re.search(r"sphere|cone|prism|cube|pyramid|surface", low):
        return None
    r = re.search(r"radius(?: of)?(?:-| )(\d+(?:\.\d+)?)", low)
    d = re.search(r"diameter(?: of)?(?:-| )(\d+(?:\.\d+)?)", low)
    h = re.search(r"height(?: of)? (\d+(?:\.\d+)?)", low)
    if "cylinder" in low and r and h and len(nums) == 2 and re.search(r"\bvolume\b", low) \
            and "surface" not in low:
        target, dim = pi * sp.Rational(r.group(1)) ** 2 * sp.Rational(h.group(1)), 3
    elif (r or d) and len(nums) == 1 and "cylinder" not in low and not h:
        rad = sp.Rational(r.group(1)) if r else sp.Rational(d.group(1)) / 2
        if re.search(r"\barea\b", low):
            target, dim = frac * pi * rad ** 2, 2
        elif re.search(r"circumference", low) and frac == 1:
            target, dim = 2 * pi * rad, 1
    elif re.search(r"triang", low) and len(nums) == 2 and re.search(r"\barea\b", low):
        b = re.search(r"base(?: of)? (\d+(?:\.\d+)?)", low)
        if b and h:
            target, dim = sp.Rational(b.group(1)) * sp.Rational(h.group(1)) / 2, 2
    else:
        m = re.search(r"(\d+(?:\.\d+)?) ?(?:m|cm|mm|km)? (?:by|x|\*) (\d+(?:\.\d+)?)", low)
        if m and len(nums) == 2 and re.search(r"rectang|room|plot|floor|garden|yard"
                                               r"|field|wall|lawn|stoep|slab", low):
            a, b = sp.Rational(m.group(1)), sp.Rational(m.group(2))
            if re.search(r"\barea\b", low) and not re.search(r"perimeter", low):
                target, dim = a * b, 2
            elif re.search(r"perimeter", low) and not re.search(r"\barea\b", low):
                target, dim = 2 * (a + b), 1
    if target is None or not re.search(r"(is|has area|area of|equals|about)\s*[:?]?$", low):
        return None
    detail = {"type": "mensuration", "target": s[:80], "truth": f"{float(target):.4f}"}
    return _numeric_verdict(to_float(target), options, key, detail, approx=True,
                            symbolic=target if pi is sp.pi else None, dim=dim)


def _claims(text):
    """'42 678 + 26% × 72 900 = 61 632' -> [(lhs_text, rhs_text, approx)]."""
    n = normalise(text)
    n = re.sub(r"(\d+(?:\.\d+)?)\s*%", r"(\1/100)", n)
    out = []
    for m in re.finditer(r"([0-9().+\-*/^ ]*[0-9)][0-9().+\-*/^ ]*?)\s*(=|≈)\s*"
                         r"(-?\s*\d[\d.]*(?:\s*/\s*\d+)?)(?![\d.]*\s*[*/^(])", n):
        lhs = m.group(1).strip()
        if not re.search(r"\d\s*[+\-*/^]\s*[\d(]|\)\s*[*/^+\-]", lhs):
            continue
        # the claim's left side must start the maths run, not end a word
        before = n[:m.start(1)]
        if re.search(r"[A-Za-z_]\s*$", before) and not re.search(
                r"(?:gives|is|as|so|and|then|:|,)\s*$", before):
            continue
        out.append((lhs, m.group(3), m.group(2) == "≈"))
    return out


def check_keyed_working(options, key, stem=""):
    """A false arithmetic claim inside the keyed option ('… = 61 632')."""
    for lhs, rhs, approx in _claims(options[key]):
        try:
            lv = to_float(parse_math(lhs))
            rv = to_float(parse_math(rhs))
        except ParseFailure:
            continue
        if lv is None or rv is None:
            continue
        dp = _decimals(rhs)
        tol = 0.5 * 10 ** (-dp) * 1.0001 + 1e-9 * max(1, abs(lv))
        if approx or dp == 0 and abs(lv) >= 1000 and "about" in stem:
            tol = max(tol, 0.01 * abs(lv))
        if abs(lv - rv) > tol and abs(lv - rv) > 0.001 * max(1.0, abs(lv)) \
                and not re.search(r"[<>]", options[key]):
            return {"type": "keyed_working", "target": f"{lhs} = {rhs}",
                    "truth": f"{lv:.6g}",
                    "reason": "the keyed option's own arithmetic is false"}
    return None


HANDLERS = (handle_ratio, handle_finance, handle_percent, handle_statistics,
            handle_sequence, handle_sum, handle_trig_angle, handle_analytic,
            handle_units, handle_probability, handle_rate, handle_mensuration,
            handle_function_value, handle_solve,
            handle_substitute, handle_equivalence, handle_evaluate)


# --- per-question driver ---

def _malformed(text):
    """Bracket imbalance or garbage operators in a stem/option."""
    n = normalise(text)
    if not _balanced(n):
        return "unbalanced brackets"
    if re.search(r"(?<![<>!=])==(?!=)|[+*/^]\s*[*/^]|\(\s*\)", n):
        return "malformed operator sequence"
    return None


def verify_question(q):
    """-> dict(verdict, type, detail, correct) for one MCQ dict."""
    stem = str(q.get("question", ""))
    options = [str(o) for o in q.get("options", [])]
    key = q.get("correct_index")
    out = {"verdict": "SKIPPED", "type": None, "detail": {}, "correct": []}
    if not isinstance(key, int) or not (0 <= key < len(options)):
        out.update(verdict="NO_CORRECT", type="structure",
                   detail={"reason": f"correct_index {key!r} out of range"})
        return out
    for label, text in [("question", stem)] + [
            (f"option {i}", o) for i, o in enumerate(options)]:
        why = _malformed(text)
        if why:
            out.update(verdict="UNPARSEABLE", type="malformed",
                       detail={"where": label, "reason": why, "text": text})
            return out
    stem_n = normalise(stem)
    spans = _stem_spans(stem_n)
    parsed, bad = _parse_spans(spans)
    for handler in HANDLERS:
        try:
            with time_limit(TIMEOUT_SECONDS * 4):
                res = handler(stem, stem_n, parsed, options, key)
        except Timeout:
            res = None
        if res is None:
            continue
        verdict, detail, correct = res
        if verdict != "verified" and handler in (
                handle_solve, handle_substitute, handle_equivalence,
                handle_evaluate) and _SKIP_WORDS.search(stem):
            out.update(verdict="SKIPPED", type=detail.get("type"),
                       detail=dict(detail, reason="process/concept wording"))
            return out
        out.update(verdict=verdict, type=detail.get("type"), detail=detail,
                   correct=correct)
        break
    if out["verdict"] in ("verified", "SKIPPED"):
        bad_work = check_keyed_working(options, key, stem)
        if bad_work:
            out.update(verdict="MISMATCH", type=bad_work["type"], detail=bad_work,
                       correct=[])
            return out
    if out["type"] is not None:
        return out
    for s, err in bad:
        # a self-contained stem span (balanced, no prose quotes) that sympy
        # rejects as a syntax error is garbled maths, not a concept question
        if err.startswith(("SyntaxError", "TokenError")) and "'" not in s \
                and _balanced(s) and re.search(r"[+\-*/^=]", s) \
                and re.search(r"[()]|\^|sqrt", s):
            out.update(verdict="UNPARSEABLE", type="malformed",
                       detail={"where": "question", "reason": err, "text": s})
            return out
    return out


# --- corpus walk + report ---

def iter_mcq_files(root=CURRICULUM_ROOT, subjects=SUBJECTS):
    for subject in subjects:
        base = Path(root) / subject
        if base.is_dir():
            yield from sorted(base.rglob("mcq.json"))


def _meta(path):
    parts = Path(path).as_posix().split("/")
    subject = next((p for p in parts if p in SUBJECTS), "unknown")
    grade = next((p for p in parts if re.fullmatch(r"grade\w+", p)), "unknown")
    variant = "overlay" if "overlays" in parts else "base"
    return subject, grade, variant


def verify_file(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    for sub in data.get("subtopics", []) or []:
        for q in sub.get("questions", []) or []:
            res = verify_question(q)
            res["id"] = q.get("id")
            res["question"] = q.get("question")
            res["options"] = q.get("options")
            res["correct_index"] = q.get("correct_index")
            yield res


def run(paths):
    results = []
    for path in paths:
        subject, grade, variant = _meta(path)
        try:
            rel = Path(path).resolve().relative_to(REPO_ROOT).as_posix()
        except ValueError:
            rel = str(path)
        for res in verify_file(path):
            res.update(path=rel, subject=subject, grade=grade, variant=variant)
            results.append(res)
    return results


def summarise(results):
    by_subject = defaultdict(Counter)
    by_grade = defaultdict(Counter)
    by_type = defaultdict(Counter)
    total = Counter()
    for r in results:
        total[r["verdict"]] += 1
        by_subject[f"{r['subject']} ({r['variant']})"][r["verdict"]] += 1
        by_grade[f"{r['subject']} {r['grade']} ({r['variant']})"][r["verdict"]] += 1
        if r["type"]:
            by_type[r["type"]][r["verdict"]] += 1
    flagged = [{k: r[k] for k in ("path", "id", "subject", "grade", "variant",
                                  "verdict", "type", "detail", "question",
                                  "options", "correct_index", "correct")}
               for r in results if r["verdict"] in FLAGGED]
    return {
        "total_questions": len(results),
        "totals": {v: total.get(v, 0) for v in VERDICTS},
        "by_subject": {k: {v: c.get(v, 0) for v in VERDICTS}
                       for k, c in sorted(by_subject.items())},
        "by_grade": {k: {v: c.get(v, 0) for v in VERDICTS}
                     for k, c in sorted(by_grade.items())},
        "by_type": {k: {v: c.get(v, 0) for v in VERDICTS}
                    for k, c in sorted(by_type.items())},
        "flagged": flagged,
    }


def _table(rows):
    head = "| | " + " | ".join(VERDICTS) + " |\n|---|" + "---|" * len(VERDICTS)
    lines = [head]
    for name, counts in rows.items():
        lines.append(f"| {name} | " + " | ".join(str(counts[v]) for v in VERDICTS)
                     + " |")
    return "\n".join(lines)


def to_markdown(summary):
    out = ["# Maths answer-key verification (report only)", "",
           f"{summary['total_questions']} MCQs checked. Findings never fail "
           "the build.", "", "## By subject", "", _table(summary["by_subject"]),
           "", "## By grade", "", _table(summary["by_grade"]), "",
           "## By question type (formalised questions only)", "",
           _table(summary["by_type"]), "", "## Flagged items", ""]
    if not summary["flagged"]:
        out.append("None.")
    for f in summary["flagged"]:
        key = f["correct_index"]
        opts = f["options"] or []
        keyed = opts[key] if isinstance(key, int) and 0 <= key < len(opts) else "?"
        right = "; ".join(str(opts[i]) for i in f["correct"] if i < len(opts))
        out.append(f"- **{f['verdict']}** `{f['path']}` `{f['id']}` "
                   f"({f['type']}): {f['question']}")
        out.append(f"  - keyed [{key}]: {keyed}")
        if right:
            out.append(f"  - computed match: {right}")
        if f["detail"]:
            det = ", ".join(f"{k}={v}" for k, v in f["detail"].items()
                            if k in ("target", "truth", "reason", "where"))
            if det:
                out.append(f"  - {det}")
    return "\n".join(out) + "\n"


# ===========================================================================
# Step checking: what we TEACH, not only what we ask
# ===========================================================================
#
# The same sympy core checks derivation chains, identities and numeric claims
# in lesson scripts (spoken prose), knowledge-bite worked solutions, the
# on-screen maths of each lesson animation (manim_scene.py), and whether the
# narration contradicts the step on screen. It judges TRUTH, NEVER METHOD:
# see the module docstring.

STEP_VERDICTS = ("STEP_OK", "STEP_WRONG", "ANSWER_WRONG", "WARNING",
                 "UNPARSEABLE", "SKIPPED")
STEP_FLAGGED = ("STEP_WRONG", "ANSWER_WRONG", "UNPARSEABLE")

# Words that mark a deliberately wrong example ("the error museum"): maths
# stated inside such a clause is never flagged.
_ERROR_CONTEXT = re.compile(
    r"\bwrong|\berror|mistake|\btrap\b|\bexhibit|misconception|\bincorrect"
    r"|\bfalse\b|\bnot\b|\bnever\b|n't\b|\binstead\b|\bforget|\bforgot"
    r"|\btempt|\bbroken\b|\bbreaks?\b|\bslip\b|\bcareless|\blearners? who\b"
    r"|\bmight write\b|\bwould write\b|\bwrites?\b|\bclaims?\b|\bsuppose"
    r"|\bpretend|\bimagine|\bmisread|\bconfus|\bloses?\b|\bdrops?\b|\breject"
    r"|\bcheck\b|\binvalid|≠|!=|\bunless\b|\bwhat if\b|\bif\b|✗|✘",
    re.I)

# Instruction verbs that make the next sentence the next step of the same
# derivation ("Rearrange: x^2 + 6x = 0").
_STEP_CUE = re.compile(
    r"^\s*(?:(?:and|then|now|next)\s+)?(?:square|rearrang|factoris|factoriz"
    r"|simplif|expand|divid|multipl|subtract|add\b|isolat|collect|raise"
    r"|so\b|then\b|therefore|hence|thus|this gives|which gives|giving"
    r"|equate|cross-multipl|take)", re.I)

# Chain links inside one clause.
_ARROW = re.compile(r"\s*(?:->|→|⇒|=>|⟹)\s*")
_WORD_LINK = re.compile(r"(?:,\s*|\s+)(?:so|which gives|this gives|giving|gives"
                        r"|therefore|hence|thus|and so)\s+", re.I)

_MARK_CODES = re.compile(
    r"\(\s*\d*\s*(?:M|A|CA|MA|RT|RG|RM|S|R|J|D|F|O|P|C|AO|MCA|SF|SR|NP)"
    r"(?:\b[^()]*)?\)|\bAO\b|✓|✔|\\checkmark")

_UNITS_ALL = (r"km/h|m/s|l/min|c/kWh|kWh|kW|mm|cm|km|kg|mg|ml|kl|m|g|l|ℓ|h|hrs?"
               r"|hours?|min|mins|minutes?|s|seconds?|days?|weeks?|months?"
               r"|years?|units?|people|learners|rand|cents?|litres?|liters?"
               r"|metres?|meters?|degrees|feet|foot|inch(?:es)?|miles?|W")
_UNITS_MATHS = (r"km/h|m/s|mm|cm|km|kg|ml|kl|min|mins|minutes?|hours?|seconds?"
                r"|units?|people|learners|rand|cents?|degrees|litres?|metres?")
_NOT_UNIT = {"and", "or", "the", "per", "of", "for", "to", "is", "are", "was",
             "which", "with", "from", "by", "into", "than", "times", "gives",
             "so", "then", "plus", "minus", "over", "divided", "multiplied",
             "because", "since", "each", "rounded", "correct", "decimal",
             "percent", "out", "more", "less", "equals", "after", "before",
             "at", "in", "on", "as", "if", "not", "all", "both", "only"}

@dataclass
class Item:
    """One formalised piece of a chain.

    kind  'expr' | 'eq' | 'sol'
    alts  alternative readings (spoken maths is ambiguous): Expr, or
          (lhs, rhs), or (var, FiniteSet)
    """
    kind: str
    alts: list
    text: str = ""
    approx: bool = False
    decimals: int = 0
    clean: bool = True


def _finding(verdict, line, step=None, reason="", text="", kind=""):
    return {"verdict": verdict, "line": line, "step": step, "reason": reason,
            "text": text, "kind": kind}


# --- written maths (knowledge bites, animations) ---

def _unit_tag(s, lit):
    """Mark unit words glued to numbers ('1 200 mm' -> '1200 @mm'), so a
    conversion such as '1 m = 1 000 mm' is never read as 1 = 1000."""
    units = _UNITS_ALL if lit else _UNITS_MATHS
    s = re.sub(r"(?<=[\d)])\s*(" + units + r")(?:\s*\^\s*\(?\d\)?)?(?![\w(])",
               lambda m: " @" + m.group(1).replace("/", "per") + " ", s)
    if lit:
        # Maths Lit: any noun after a number is a unit ('36 tags')
        s = re.sub(r"(?<=\d)\s+([A-Za-z][a-z]{2,})\b",
                   lambda m: m.group(0) if m.group(1).lower() in _NOT_UNIT
                   else " @" + m.group(1).lower() + " ", s)
    return s


def written_normalise(text, lit=False):
    """Knowledge-bite / animation text -> normalised maths text."""
    s = _MARK_CODES.sub(" ", str(text))
    s = re.sub(r"\*{3,}", " ", s)  # redacted values on a slip
    s = s.replace("≈", " ~= ")
    # 4 629 629,63 -> 4629629,63 (before the comma decimal is read)
    s = re.sub(r"(?<![\d.,])\d{1,3}(?: \d{3})+(?=,\d|\b)(?! \d)",
               lambda m: m.group().replace(" ", ""), s)
    s = normalise(s)
    s = _unit_tag(s, lit)
    # 'x' / 'X' used as a times sign: '1,2 m x 1 000', 'a x c = 2 x 3'
    tsign = r"(?<=[\d)])(\s*@\w+)?\s*[xX]\s*(?=[\d(])" if lit else \
        r"(?<=[\d)])(\s*@\w+)?\s+[xX]\s+(?=[\d(])" \
        r"|(?<=\b[a-z])\s+x\s+(?=[a-z]\b(?!\s*[\^(]))"
    s = re.sub(tsign, lambda m: (m.group(1) or "") + " * ", s)
    s = re.sub(r"(\d(?:[\d.]*\d)?)\s*%", r"(\1/100)", s)
    return s


_PROSE_SMALL = {"of", "is", "a", "an", "to", "in", "on", "at", "by", "so",
                "the", "and", "or", "for", "we", "it", "as", "with", "from",
                "into", "then", "gives", "get", "use", "via"}


def _clean_part(p, index=0):
    """One side of a relation -> (kind, Expr|None, units, dropped_lead)

    kind: 'expr' | 'label' | 'prose' | 'bad'; units: the unit tags on the
    side; dropped_lead: leading prose words were removed ('Mean 55').
    """
    p = p.strip().strip(",;:").strip()
    units = frozenset(u.lower().rstrip("s") for u in re.findall(r"@(\w+)", p))
    p = re.sub(r"\s*@\w+\s*", " ", p).strip()
    colon = False
    if "?" in p:
        return "prose", None, units, False  # a question, not a claim
    if ":" in p:
        head, tail = p.rsplit(":", 1)
        if index > 0:
            return "prose", None, units, False  # a new statement starts
        if re.search(r"[A-Za-z]{3,}", head):
            p, colon = tail.strip(), True
    if re.match(r"^\s*[+*/^]", p) or re.search(
            r"\bd\s*/\s*d[a-z]|\(d\)/\(d[a-z]\)|\blim\b|\bxbar\b|'", p):
        return "prose", None, units, False  # a continuation line; calculus
    toks = p.split()
    dropped = False
    while toks:
        t = toks[0].rstrip(":?,")
        nxt = toks[1] if len(toks) > 1 else ""
        if re.fullmatch(r"\(?[A-Za-z][A-Za-z'\-]*", t) and t.lstrip("(") \
                not in FUNCS and (len(t) >= 3 or t.lower() in _PROSE_SMALL) \
                and not re.match(r"^[+\-*/^]", nxt):
            toks.pop(0)
            dropped = True
            continue
        break
    p = " ".join(toks).strip().rstrip(".,;:?")
    p = re.sub(r"\.{3,}|…", "", p).strip()
    if dropped and colon:
        dropped = False
    if not p:
        return "label", None, units, dropped
    core = re.sub(r"sqrt|cbrt|pi|log|sin|cos|tan|rad|alpha|beta|theta|gamma|phi",
                  "", p)
    if re.search(r"[A-Za-z]{3,}", core) or re.search(r"[A-Z]", core) or any(
            t in _NOT_PRODUCTS or t in _PROSE_SMALL
            for t in re.findall(r"(?<![A-Za-z])[a-z]{2}(?![A-Za-z(])", core)):
        return "prose", None, units, dropped
    if re.search(r",\s", core):
        return "prose", None, units, dropped  # a list, not one value
    if re.search(r"[^\x00-\x7f]", core):  # T̂, Ô, ∈, ∪ ...
        return "prose", None, units, dropped
    if "_" in core or ";" in core or "'" in core or re.search(r"\|", core):
        return "prose", None, units, dropped  # T_n, (3 ; 0), f'(x), |x|
    if re.search(r"\d\s+\(?\d", core) or not _balanced(core):
        return "prose", None, units, dropped  # '20 h 40 min', a cut bracket
    if re.search(r"(?<![A-Za-z])[a-z]\s*\(\s*[^()]*\)", p) and not re.search(
            r"\d\s*\(", p):
        # f(x), g(1 - m): a function name, not a product
        if re.fullmatch(r"[a-z]\s*\([^()]*\)", p):
            return "label", None, units, dropped
        return "prose", None, units, dropped
    try:
        return "expr", parse_math(_over(p)), units, dropped
    except ParseFailure as exc:
        return "bad", str(exc), units, dropped


def _is_label_text(p):
    p = p.strip()
    return bool(re.fullmatch(r"[A-Za-z]{1,3}\d?|[a-z]\([^()]*\)|T_?\(?\w+\)?"
                             r"|[A-Z]\w*\([^()]*\)", p)) or bool(
        re.search(r"[^\x00-\x7f]", p) and not re.search(r"[\d+\-*/^]", p))


_NUMTOK = r"[+-]?\s*(?:\d+(?:\.\d+)?(?:\s*/\s*\d+(?:\.\d+)?)?|\(\d+/\d+\))"


def _parse_solution(s):
    """'x = 7/2 or x = 1' / 'x = ±3' / 'x = -1 or 2' -> Item('sol') or None."""
    s = s.strip().rstrip(".").strip()
    s = re.sub(r"^(?:so|then|and|hence|therefore|thus|giving|gives)\s+", "", s,
               flags=re.I)
    m = re.match(r"^([a-z])\s*=\s*(.+)$", s)
    if not m:
        return None
    var, rest = m.group(1), m.group(2)
    pieces = re.split(r"\s+(?:or|and)\s+|\s*;\s*|\s*,\s+", rest)
    vals = []
    for pc in pieces:
        pc = re.sub(r"^" + var + r"\s*=\s*", "", pc.strip())
        pc = re.sub(r"\s*\((?:valid|n/a|rejected|reject|accept|accepted)\)", "",
                    pc, flags=re.I)
        variants = [pc]
        if pc.startswith("±"):
            variants = [pc[1:], "-(" + pc[1:] + ")"]
        for v in variants:
            v = v.strip()
            if not v or re.search(r"[A-Za-z]", re.sub(r"sqrt|pi", "", v)):
                return None
            try:
                e = parse_math(v)
            except ParseFailure:
                return None
            if not _is_number(e):
                return None
            vals.append(e)
    if not vals:
        return None
    return Item("sol", [(sp.Symbol(var), sp.FiniteSet(*vals))], s,
                decimals=_decimals(rest))


def _written_relation(seg):
    """One clause -> (Item or None, parts).

    parts are the cleaned '=' sides for chain checking:
    [(kind, expr_or_None, raw, approx_link_before, units)].
    """
    seg = seg.strip()
    sol = _parse_solution(seg)
    if sol is not None:
        return sol, []
    if re.search(r"<|>|!=|\bnot\b", seg):
        return None, []
    raw_parts = re.split(r"(~=|(?<![<>!~])=(?!=))", seg)
    parts = []
    approx = False
    for i, rp in enumerate(raw_parts):
        if i % 2:
            approx = rp == "~="
            continue
        kind, e, units, dropped = _clean_part(rp, i // 2)
        if kind == "expr" and i == 0 and (dropped or _is_label_text(
                re.sub(r"@\w+", "", rp).split(":")[-1])):
            kind, e = "label", None  # 'Quartile 3 = ...', 'Mean = ...'
        elif kind == "expr" and dropped:
            kind, e = "prose", None
        if re.search(r"\.{3,}|…", rp):
            approx = True
        parts.append((kind, e, re.sub(r"\s*@\w+", "", rp).strip(), approx,
                      units))
        approx = False
    item = None
    if len(parts) == 1 and parts[0][0] == "expr":
        item = Item("expr", [parts[0][1]], seg)
    elif len(parts) == 2 and all(p[0] == "expr" for p in parts) and \
            parts[0][4] == parts[1][4]:
        item = Item("eq", [(parts[0][1], parts[1][1])], seg)
    return item, parts


def _num_close(lv, rv, rtext, approx, ctx):
    dp = _decimals(rtext)
    tol = 0.5 * 10 ** (-dp) * 1.0001 + 1e-9 * max(1.0, abs(lv))
    if abs(lv - rv) <= tol:
        return "ok"
    if approx or re.search(r"approx|about|round|nearest|correct to|decimal"
                           r"|≈|~=", ctx, re.I):
        if abs(lv - rv) <= max(tol * 2, 0.01 * max(abs(lv), abs(rv))):
            return "ok"
    if abs(lv - rv) <= 0.005 * max(abs(lv), abs(rv)):
        return "rounded"
    return "wrong"


def _equal_step(a, b, btext, approx, ctx):
    """'ok' | 'wrong' | 'rounded' | None for expression a == expression b."""
    if _is_number(a) and _is_number(b):
        lv, rv = to_float(a), to_float(b)
        if lv is None or rv is None:
            return None
        return _num_close(lv, rv, btext, approx, ctx)
    r = equivalent(a, b)
    if r is None:
        return None
    return "ok" if r else "wrong"


def check_equals_chain(parts, ctx, line, error_ctx):
    """'a = b = c' chains: every consecutive pair of formal parts must be
    equal. The first part may be a label ('Mean', 'f(3)', 'y')."""
    out = []
    # a leading lone symbol or label names the chain, it is not a claim
    start = 0
    if parts and (parts[0][0] in ("label", "prose") or (
            parts[0][0] == "expr" and isinstance(parts[0][1], sp.Symbol)
            and len(parts) > 2)):
        start = 1
    exprs = parts[start:]
    if len(exprs) < 2:
        return out
    if len(parts) == 2 and start == 0:
        # a lone 'lhs = rhs': identity or numeric fact, never an equation
        a, b = parts[0][1], parts[1][1]
        if parts[0][0] != "expr" or parts[1][0] != "expr":
            return out
        if not (_is_number(a) and _is_number(b)):
            return out  # handled by check_identity
    for k in range(1, len(exprs)):
        (ka, a, ra, _, ua), (kb, b, rb, apx, ub) = exprs[k - 1], exprs[k]
        if ka != "expr" or kb != "expr":
            continue
        if ua != ub and (ua or not re.search(r"[+\-*/^]", ra.strip().lstrip("-"))
                         or _power_of_ten(a, b)):
            # a conversion ('1 m = 1 000 mm', '45 min = 45/60', '4 rolls =
            # R1 400'); only 'arithmetic = value unit' is compared
            continue
        if a.free_symbols != b.free_symbols and not (
                _is_number(a) or _is_number(b)):
            continue  # a named quantity substituted ('-cos α/4 = -p/4')
        if "°" in ctx and re.search(r"sin|cos|tan", ra + rb):
            continue  # degree/radian reading of the text is not reliable
        pct = [bool(re.fullmatch(r"\s*\(\d[\d.]*/100\)\s*", x)) for x in (ra, rb)]
        if pct[0] and not pct[1]:
            continue  # '1% = R30': a percentage OF an amount
        if (ua or ub) and (a == 1 or b == 1):
            continue  # '1 cm = 50 cm': a scale statement
        if (_is_number(a) != _is_number(b)):
            continue  # 'x^2 - 4 = 0' style; not a rewrite
        res = _equal_step(a, b, rb, apx, ctx)
        if res != "ok" and re.search(r"/100\)", ra + rb):
            # '34/60 × 100 = 56,67%': the % sign as a label, not ÷ 100
            try:
                a2 = parse_math(_over(re.sub(r"\((\d[\d.]*)/100\)", r"\1", ra)))
                b2 = parse_math(_over(re.sub(r"\((\d[\d.]*)/100\)", r"\1", rb)))
                if _equal_step(a2, b2, rb, apx, ctx) == "ok":
                    res = "ok"
            except ParseFailure:
                pass
        if res is None:
            out.append(_finding("SKIPPED", line, k, "could not decide", ctx,
                                "equals-chain"))
        elif res == "ok":
            out.append(_finding("STEP_OK", line, k, "", ctx, "equals-chain"))
        elif res == "rounded":
            out.append(_finding("WARNING", line, k,
                                f"'{ra} = {rb}' holds only after rounding "
                                "that is not stated", ctx, "equals-chain"))
        elif error_ctx:
            out.append(_finding("SKIPPED", line, k,
                                "false on purpose? (error-example wording)",
                                ctx, "equals-chain"))
        elif _run_on(a, rb):
            out.append(_finding("WARNING", line, k,
                                "run-on '=': the next part continues the "
                                "calculation from the previous result", ctx,
                                "equals-chain"))
        else:
            out.append(_finding("STEP_WRONG", line, k,
                                f"'{ra}' is not equal to '{rb}'", ctx,
                                "equals-chain"))
    return out


def _power_of_ten(a, b):
    va, vb = to_float(a), to_float(b)
    if not va or not vb:
        return False
    r = abs(math.log10(abs(vb / va)))
    return r > 0.5 and abs(r - round(r)) < 0.01


def _run_on(a, btext):
    """'40 ÷ 2 = 20 × R65 = R1 300': b starts from a's value and goes on."""
    m = re.match(r"\s*\(?\s*(-?\d+(?:\.\d+)?)\s*\)?\s*[+\-*/^]", btext)
    if not m or not _is_number(a):
        return False
    va = to_float(a)
    return va is not None and abs(va - float(m.group(1))) <= 0.005 * max(1, abs(va))


_IDENTITY_CUE = re.compile(r"identit|\blaws?\b|\balways\b|factoris"
                           r"|factoriz|expand|expansion|multipl\w* out"
                           r"|simplif|\bsum of (two )?cubes|difference of"
                           r"|equivalent", re.I)


def check_identity(item, ctx, line, error_ctx, cue_ctx=None):
    """A lone 'lhs = rhs' with symbols: a TRUE identity is STEP_OK; a false
    one is flagged only when the wording says it is an identity/law/
    factorisation (otherwise it is an equation to solve)."""
    if item is None or item.kind != "eq":
        return []
    cue = _IDENTITY_CUE.search(cue_ctx if cue_ctx is not None else ctx)
    results = []
    for lhs, rhs in item.alts:
        if _is_number(lhs) and _is_number(rhs):
            return []
        if not (lhs.free_symbols and rhs.free_symbols):
            results.append(None)
            continue
        results.append(equivalent(lhs, rhs))
    if any(r is True for r in results):
        return [_finding("STEP_OK", line, 1, "identity holds", ctx, "identity")]
    if not results or any(r is None for r in results):
        return []
    lhs, rhs = item.alts[0]
    symbolic_power = any(
        isinstance(x, sp.Pow) and x.exp.free_symbols
        for side in (lhs, rhs) for x in sp.preorder_traversal(side))
    product_side = any(
        isinstance(side, sp.Mul) and sum(1 for f in side.args
                                         if f.free_symbols) >= 2
        for side in (lhs, rhs))
    same_syms = lhs.free_symbols == rhs.free_symbols and not (
        isinstance(lhs, sp.Symbol) or isinstance(rhs, sp.Symbol))
    if not (symbolic_power and same_syms and len(lhs.free_symbols) >= 2
            or cue and product_side and same_syms):
        return [_finding("SKIPPED", line, None, "an equation, not a claim",
                         ctx, "identity")]
    if error_ctx:
        return [_finding("SKIPPED", line, None,
                         "false on purpose? (error-example wording)", ctx,
                         "identity")]
    return [_finding("STEP_WRONG", line, 1,
                     "stated identity/factorisation is not an identity", ctx,
                     "identity")]


def _solution_set(item):
    """-> list of (var, Set) readings for an eq/sol item (single unknown)."""
    out = []
    for alt in item.alts:
        if item.kind == "sol":
            out.append(alt)
            continue
        lhs, rhs = alt
        free = (lhs - rhs).free_symbols
        if len(free) != 1:
            out.append(None)
            continue
        v = next(iter(free))
        try:
            with time_limit(TIMEOUT_SECONDS):
                s = sp.solveset(sp.Eq(lhs, rhs), v, sp.S.Reals)
        except Exception:
            out.append(None)
            continue
        if isinstance(s, (sp.ConditionSet, sp.ImageSet)) or s.has(sp.ImageSet) \
                or s.has(sp.ConditionSet):
            out.append(None)
            continue
        out.append((v, s))
    return out


def _set_relation(a, b):
    """'equal' | 'lost' (b ⊂ a) | 'gained' (a ⊂ b) | 'different' | None."""
    try:
        if _sets_equal(a, b):
            return "equal"
        with time_limit(TIMEOUT_SECONDS):
            if isinstance(a, sp.FiniteSet) and isinstance(b, sp.FiniteSet):
                fa = [to_float(x) for x in a]
                fb = [to_float(x) for x in b]
                if None in fa or None in fb:
                    return None

                def within(xs, ys):
                    return all(any(abs(x - y) <= 0.0051 * max(1, abs(x))
                                   for y in ys) for x in xs)
                if within(fb, fa):
                    return "lost"
                if within(fa, fb):
                    return "gained"
                return "different"
            if b.is_subset(a):
                return "lost"
            if a.is_subset(b):
                return "gained"
            return "different"
    except Exception:
        return None


def _why_changed(prev, nxt, rel):
    ptxt, ntxt = prev.text, nxt.text
    if rel == "gained":
        if re.search(r"sqrt|√", ptxt) and not re.search(r"sqrt|√", ntxt):
            return "roots gained: squaring both sides can add extraneous roots"
        return ("roots gained: typical of squaring or multiplying by an "
                "expression in the unknown; check in the original")
    if nxt.kind == "sol":
        return ("roots lost from the stated answer: dividing by an "
                "expression in the unknown, or a root rejected by context")
    return ("roots lost: typical of dividing by an expression in the "
            "unknown")


def _rewrite_like(a, b):
    """Both sides polynomials in the same unknowns and of the same degree:
    an expand / factorise / simplify arrow, not a mapping."""
    try:
        if _is_number(a) or _is_number(b) or a.free_symbols != b.free_symbols:
            return False
        syms = sorted(a.free_symbols, key=str)
        with time_limit(TIMEOUT_SECONDS):
            pa, pb = sp.Poly(sp.expand(a), *syms), sp.Poly(sp.expand(b), *syms)
        return pa.total_degree() == pb.total_degree()
    except Exception:
        return False


def check_step(prev, nxt, line, step, ctx, error_ctx, final=False):
    """One arrow/'so' step between two items -> finding or None."""
    if prev.kind == "expr" and nxt.kind == "expr":
        results = []
        for a in prev.alts:
            for b in nxt.alts:
                results.append(_equal_step(a, b, nxt.text, nxt.approx, ctx))
        if "ok" in results:
            return _finding("STEP_OK", line, step, "", ctx, "rewrite")
        if not _rewrite_like(prev.alts[0], nxt.alts[0]):
            # an arrow between values can mean 'maps to', 'next term',
            # 'derivative', 'limit' or 'on the ground': never judged
            return _finding("SKIPPED", line, step, "arrow is not a rewrite",
                            ctx, "rewrite")
        if None in results or not results:
            return _finding("SKIPPED", line, step, "could not decide", ctx,
                            "rewrite")
        if "rounded" in results:
            return _finding("WARNING", line, step, "equal only after rounding",
                            ctx, "rewrite")
        if error_ctx:
            return _finding("SKIPPED", line, step,
                            "false on purpose? (error-example wording)", ctx,
                            "rewrite")
        return _finding("STEP_WRONG", line, step,
                        "expression is not equivalent to the previous one", ctx,
                        "rewrite")
    if prev.kind == "eq" and nxt.kind in ("eq", "sol"):
        ps, ns = _solution_set(prev), _solution_set(nxt)
        rels = []
        for p in ps:
            for n in ns:
                if p is None or n is None or p[0] != n[0]:
                    continue
                rels.append(_set_relation(p[1], n[1]))
        if not rels:
            if nxt.kind == "eq" and prev.kind == "eq":
                return _multivar_step(prev, nxt, line, step, ctx)
            return _finding("SKIPPED", line, step, "not a one-unknown step", ctx,
                            "transform")
        if "equal" in rels:
            return _finding("STEP_OK", line, step, "", ctx, "transform")
        if None in rels:
            return _finding("SKIPPED", line, step, "could not decide", ctx,
                            "transform")
        for rel in ("gained", "lost"):
            if rel in rels:
                return _finding("WARNING", line, step, _why_changed(prev, nxt, rel),
                                ctx, "transform")
        if error_ctx:
            return _finding("SKIPPED", line, step,
                            "false on purpose? (error-example wording)", ctx,
                            "transform")
        verdict = "ANSWER_WRONG" if nxt.kind == "sol" and final else "STEP_WRONG"
        return _finding(verdict, line, step,
                        "solution set changes: the step does not follow" if
                        verdict == "STEP_WRONG" else
                        "stated answer is not the solution of the equation",
                        ctx, "transform")
    return _finding("SKIPPED", line, step, f"{prev.kind} -> {nxt.kind}", ctx,
                    "transform")


def _multivar_step(prev, nxt, line, step, ctx):
    """Several unknowns: accept a rearrangement (same relation up to a
    nonzero constant factor); anything else is SKIPPED, never wrong."""
    for pl, pr in prev.alts:
        for nl, nr in nxt.alts:
            a, b = pl - pr, nl - nr
            try:
                with time_limit(TIMEOUT_SECONDS):
                    if b == 0 or a == 0:
                        continue
                    ratio = sp.simplify(a / b)
                    if ratio.is_number and ratio != 0:
                        return _finding("STEP_OK", line, step, "", ctx,
                                        "transform")
            except Exception:
                continue
    return _finding("SKIPPED", line, step, "several unknowns", ctx, "transform")


def _malformed_line(text):
    """Unbalanced brackets or garbled operator runs in a written maths line."""
    n = _MARK_CODES.sub(" ", str(text))
    n = re.sub(r"\*{3,}", " ", n)  # redacted values on a slip
    n = re.sub(r"\((?:[a-z]|\d+(?:\.\d+)?|[ivx]+)\)(?=\s)", " ", n)  # (a) (i)
    n = normalise(n)
    n = re.sub(r"\[\s*-?[\d.∞oo]+\s*;\s*-?[\d.∞oo]+\s*\)|\(\s*-?[\d.∞oo]+\s*;"
               r"\s*-?[\d.∞oo]+\s*\]", "", n)  # half-open intervals
    if not _balanced(n):
        return "unbalanced brackets"
    if re.search(r"(?<![<>!=~])==(?!=)|[+*/^]\s*[*/^](?!\()|\(\s*\)|\+\s*\+|--\s*-", n):
        return "malformed operator sequence"
    return None


def _clauses(sentence):
    """Split a sentence into chain pieces on arrows and 'so' links."""
    pieces = []
    for chunk in _ARROW.split(sentence):
        sub = _WORD_LINK.split(chunk)
        pieces.extend(sub)
    return [p for p in pieces if p.strip()]


def _sentences(line):
    """Sentence split that keeps decimals and coordinates together."""
    # '(Memo alternative: ...)' asides are sentences of their own
    line = re.sub(r"(^|\s)\((?=(?:Memo|Alternative|Or|OR|Note|See)\b)", r"\1", line)
    parts = re.split(r"(?<=[.?!])\s+(?=[A-Z0-9(\"'])|(?<=[.?!])\s*$|;\s+(?=[A-Za-z]"
                     r"[A-Za-z]{2,}\b|[A-Z])", line)
    return [p for p in parts if p and p.strip()]


def _split_top(s):
    """Split on ': ' / '; ' outside brackets (coordinates keep their ';')."""
    out, depth, cur, i = [], 0, [], 0
    while i < len(s):
        ch = s[i]
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        if ch in ":;" and depth == 0 and (i + 1 == len(s) or s[i + 1] == " ") \
                and not (i > 0 and s[i - 1] == " " and ch == ":"):
            out.append("".join(cur))
            cur = []
            i += 1
            continue
        cur.append(ch)
        i += 1
    out.append("".join(cur))
    return out


def check_written_line(text, line, lit=False, prev_item=None, link_prev=False):
    """Malformed-maths gate, then every chain and claim in the line."""
    why = _malformed_line(text)
    if why:
        return [_finding("UNPARSEABLE", line, None, why, text, "malformed")], None
    return check_written_text(text, line, lit=lit, prev_item=prev_item,
                              link_prev=link_prev)


def check_written_text(text, line, lit=False, prev_item=None, ctx_extra="",
                       link_prev=False):
    """All chains/claims in one written line -> (findings, last_item)."""
    findings = []
    last = prev_item
    segments = []
    for sent in _sentences(text):
        # a colon or semicolon starts a new statement ('Factorise: ...',
        # 'try x = 2: 4 - 10 + 6 = 0'); prose before it is the step's cue
        segs = [g for g in _split_top(sent) if g.strip()]
        pending_cue = False
        for g in segs:
            segments.append((g, sent, pending_cue))
            pending_cue = bool(_STEP_CUE.search(g)) and not re.search(
                r"[=]", g)
    for sent, whole, carried in segments:
        s_norm = written_normalise(sent, lit)
        error_ctx = bool(_ERROR_CONTEXT.search(sent))
        worded = bool(_STEP_CUE.search(sent) or carried)
        cue = worded or (link_prev and last is prev_item)
        chain_items = []
        pieces = _clauses(s_norm)
        for idx, piece in enumerate(pieces):
            item, parts = _written_relation(piece)
            if parts and len(parts) >= 2:
                findings.extend(check_equals_chain(
                    parts, sent, line, error_ctx))
                if len(parts) == 2 and item is not None:
                    findings.extend(check_identity(item, sent, line, error_ctx,
                                                   cue_ctx=piece + " " + sent))
            if item is None:
                chain_items.append(None)
                continue
            chain_items.append(item)
        # consecutive formal items in one sentence form a chain
        n_steps = 0
        for k in range(1, len(chain_items)):
            a, b = chain_items[k - 1], chain_items[k]
            if a is None or b is None:
                continue
            if a.kind == "sol":
                continue  # 'x = 0 gives √4 − 0 = 2': a check, not a step
            if a.kind == "expr" and b.kind != "expr":
                continue
            if a.kind == "eq" and b.kind == "expr":
                continue
            n_steps += 1
            final = k == len(chain_items) - 1
            findings.append(check_step(a, b, line, n_steps, sent, error_ctx,
                                       final=final))
        # a step cue links this sentence's first equation to the last one
        first = next((c for c in chain_items if c is not None), None)
        if cue and last is not None and first is not None and \
                last.kind == "eq" and first.kind in ("eq", "sol") and len(
                    (last.alts[0][0] - last.alts[0][1]).free_symbols) == 1:
            f = check_step(last, first, line, 0, sent, error_ctx, final=False)
            if f["verdict"] == "STEP_WRONG" or (
                    f["verdict"] == "WARNING" and not worded):
                # across sentences / screen lines we cannot be sure the
                # equation is the same one being transformed (a zero-product
                # branch, a new example): never flag, only skip
                f.update(verdict="SKIPPED", reason="cross-line mismatch "
                         "(may be a new equation or a branch)")
            findings.append(f)
        formal = [c for c in chain_items if c is not None]
        if formal:
            last = formal[-1]
    return findings, last


# --- spoken maths (lesson scripts, tutor snippets) ---

_ONES = {"nought": 0, "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
         "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
         "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
         "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19}
_TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
         "seventy": 70, "eighty": 80, "ninety": 90}
_SCALES = {"hundred": 100, "thousand": 1000, "million": 10 ** 6}


def _read_number(words, i):
    """Spoken number at words[i:] -> (value_str, next_index) or None."""
    total, cur, j, seen = 0, 0, i, False
    while j < len(words):
        w = words[j]
        if w in _ONES:
            if seen and cur % 10 and cur < 100 and cur % 100 != 0 and \
                    not words[j - 1] in _TENS:
                break
            if seen and words[j - 1] in _ONES:
                break
            cur += _ONES[w]
        elif w in _TENS:
            if seen and cur % 100 and words[j - 1] not in _SCALES \
                    and words[j - 1] != "and":
                break
            cur += _TENS[w]
        elif w in _SCALES and seen:
            if w == "hundred":
                cur *= 100
            else:
                total += cur * _SCALES[w]
                cur = 0
        elif w == "and" and seen and j + 1 < len(words) and (
                words[j + 1] in _ONES or words[j + 1] in _TENS) and \
                words[j - 1] in _SCALES:
            pass
        elif w == "point" and seen and j + 1 < len(words) and words[j + 1] in _ONES:
            digits = []
            k = j + 1
            while k < len(words) and words[k] in _ONES and _ONES[words[k]] < 10:
                digits.append(str(_ONES[words[k]]))
                k += 1
            return f"{total + cur}.{''.join(digits)}", k
        else:
            break
        seen = True
        j += 1
    if not seen:
        return None
    return str(total + cur), j


_SPOKEN_STOP = {"equals", ",", "and", "or", "which", "so", "then"}
_LETTERS = set("bcdfghjkmnpqrtuvwxyz")  # 'a' only next to an operator


def _spoken_tokens(sentence):
    s = re.sub(r"(?<![\w'])(?!A\b)[A-Z](?![\w'])", " POINTNAME ", sentence)
    s = s.lower()
    s = re.sub(r"(?<=\d),(?=\d)", ".", s)
    s = re.sub(r"(?<![\d.])\d{1,3}(?: \d{3})+\b(?!\.\d*\s\d)",
               lambda m: m.group().replace(" ", ""), s)
    s = s.replace("—", " , ").replace("–", " , ").replace(";", " , ")
    s = re.sub(r"[“”\"():!?]", " ", s)
    s = re.sub(r"(\w)-(\w)", r"\1 \2", s)
    s = re.sub(r"([a-z])'s\b", r"\1", s)
    s = s.replace(",", " , ")
    s = re.sub(r"\.(?!\d)", " ", s)
    return s.split()


_SPOKEN_BOUND_BEFORE = {
    "", ",", "and", "so", "which", "because", "but", "then", "that", "means",
    "gives", "giving", "since", "now", "here", "check", "answer", "result",
    "therefore", "hence", "thus", "is", "as", "get", "becomes", "leaves",
    "makes", "write", "rewrite", "say", "solve", "simplify", "expand",
    "factorise", "calculate", "compute", "confirm", "verify", "reads", "read",
    "try", "gets", "got", "exactly", "just", "yes", "right", "see", "equation",
    "expression", "sum", "product", "was", "were", "be"}
_SPOKEN_BOUND_AFTER = {
    "", ",", "and", "so", "which", "because", "but", "then", "that", "since",
    "now", "here", "the", "a", "exactly", "again", "too", "as", "for", "when",
    "with", "every", "each", "is", "was", "correct", "confirmed", "true",
    "yes", "right", "checks", "holds", "works", "done", "both", "also"}
# maths vocabulary the spoken reader does not formalise: a claim touching it
# is never flagged
_SPOKEN_UNHANDLED = re.compile(
    r"\b(half|halves|quarter|third|thirds|fifths?|tenths?|of|percent|per|cent"
    r"|sine|cosine|tangent|sin|cos|tan|log|base|root|roots|by|cubic|square"
    r"|degrees?|factorial|pi|rand|doubled|twice|triple|jumps?|term|terms"
    r"|bracket|brackets|point|dot|th|nd|rd|st|mod|modulus|absolute|choose"
    r"|metres?|units?|cm|mm|km|kg|hours?|minutes?|seconds?|litres?"
    r"|grade|page|question|mark|marks|step|row|column|number|cent|r"
    r"|between|halfway|average|mean|median|mode|pointname|log|ln"
    r"|probability|chance|out)\b")


_OPS_WORDS = {"plus": "+", "minus": "-", "times": "*", "over": "/"}


def spoken_to_math(sentence):
    """Spoken maths in one sentence -> list of spans; each span is a list of
    alternative ASCII readings (exponent/root/'over' scope is ambiguous in
    speech, so every plausible bracketing is kept)."""
    w = _spoken_tokens(sentence)
    spans, cur, i = [], [], 0
    n_words = len(w)

    def is_var(k):
        if k >= n_words:
            return False
        t = w[k]
        if t in _LETTERS:
            return True
        if t == "a":
            prev_ = w[k - 1] if k else ""
            nxt_ = w[k + 1] if k + 1 < n_words else ""
            return prev_ in ("plus", "minus", "times", "over", "equals") or \
                nxt_ in ("plus", "minus", "times", "squared", "cubed", "over",
                         "equals") or nxt_ in _LETTERS
        return False

    start = [0]

    def add(tok):
        if not cur:
            start[0] = i
        cur.append(tok)

    def flush():
        if cur:
            spans.append((list(cur), start[0], i))
            cur.clear()

    while i < n_words:
        t = w[i]
        nxt = w[i + 1] if i + 1 < n_words else ""
        num = _read_number(w, i) if (t in _ONES or t in _TENS) else None
        if num:
            add(("num", num[0]))
            i = num[1]
            continue
        if re.fullmatch(r"\d+(?:[.,]\d+)?", t):
            add(("num", t.replace(",", ".")))
            i += 1
            continue
        if is_var(i):
            add(("var", t))
            i += 1
            continue
        if t in ("plus", "times", "over"):
            add(("op", _OPS_WORDS[t]))
            i += 1
            continue
        if t in ("minus", "negative"):
            add(("neg" if t == "negative" else "op", "-"))
            i += 1
            continue
        if t in ("multiplied", "divided") and nxt == "by":
            add(("op", "*" if t == "multiplied" else "/"))
            i += 2
            continue
        if t == "squared":
            add(("pow", "2"))
            i += 1
            continue
        if t == "cubed":
            add(("pow", "3"))
            i += 1
            continue
        if t == "all" and nxt in ("squared", "cubed"):
            add(("allpow", "2" if nxt == "squared" else "3"))
            i += 2
            continue
        if t == "to" and nxt == "the" and i + 2 < n_words:
            k = i + 2
            if w[k] == "power":
                k += 1
                if k < n_words and w[k] == "of":
                    k += 1
            if k < n_words and (w[k] in _ONES or w[k] in _TENS or w[k] in
                                ("negative", "minus") or is_var(k)
                                or re.fullmatch(r"\d+", w[k])):
                add(("to", None))
                i = k
                continue
        if t == "equals" or (t == "is" and nxt == "equal" and i + 2 < n_words
                             and w[i + 2] == "to"):
            add(("eq", "="))
            i += 1 if t == "equals" else 3
            continue
        if t == "is" and cur and nxt != "not":
            add(("is", "="))
            i += 1
            continue
        if t == "the" and nxt == "quantity":
            add(("open", "("))
            i += 2
            continue
        if t == "open" and nxt == "bracket":
            add(("lp", "("))
            i += 2
            continue
        if t in ("close", "closed") and nxt == "bracket":
            add(("rp", ")"))
            i += 2
            continue
        if t in ("square", "cube") and nxt == "root" and i + 2 < n_words \
                and w[i + 2] == "of":
            add(("root", "sqrt" if t == "square" else "cbrt"))
            i += 3
            continue
        if t == "," and cur:
            add(("comma", ","))
            i += 1
            continue
        flush()
        i += 1
    flush()
    out = []
    for span, w0, w1 in spans:
        before = w[w0 - 1] if w0 > 0 else ""
        after = w[w1] if w1 < n_words else ""
        clean = (before in _SPOKEN_BOUND_BEFORE) and (
            after in _SPOKEN_BOUND_AFTER) and not _SPOKEN_UNHANDLED.search(
            " ".join(w[max(0, w0 - 2):w1 + 2]))
        # leading minus is a sign, not an operator
        lead_neg = bool(span) and span[0] == ("op", "-")
        if span and (span[0][0] in ("op", "is", "eq", "pow", "allpow", "to")
                     and not lead_neg or span[-1][0] in ("op", "is", "eq",
                                                         "open", "to", "root",
                                                         "neg")):
            clean = False  # a running total or a cut-off expression
        if any(a[0] == "num" and b[0] == "num" for a, b in zip(span, span[1:])):
            clean = False  # '11:45 is 12:25', '1,539 58'
        if before == "and" and w0 >= 2 and (re.fullmatch(r"[\d.]+", w[w0 - 2])
                                             or w[w0 - 2] in _ONES
                                             or w[w0 - 2] in _TENS):
            clean = False  # 'the mean of 4 and 10 is 7'
        if _SPOKEN_UNHANDLED.search(" ".join(w)):
            clean = False
        while span and span[-1][0] in ("comma", "is", "eq", "op", "open", "to",
                                       "root", "neg"):
            span.pop()
        while span and span[0][0] in ("comma", "is", "eq", "op", "pow", "allpow",
                                      "to"):
            span.pop(0)
        if lead_neg and span and span[0][0] in ("num", "var"):
            span.insert(0, ("neg", "-"))
        # a comma inside a span: the grouping is only trusted around
        # 'the quantity' and ', times'; other pieces are never flagged
        has_comma = any(t[0] == "comma" for t in span)
        pieces, piece = [], []
        for k, tok in enumerate(span):
            if tok[0] == "comma":
                nxt_ = span[k + 1] if k + 1 < len(span) else None
                if nxt_ and (nxt_[0] in ("op", "eq") or any(
                        p[0] == "open" for p in piece)):
                    piece.append(tok)
                    continue
                pieces.append(piece)
                piece = []
                continue
            piece.append(tok)
        pieces.append(piece)
        if len(pieces) > 1:
            clean = False
        for p in pieces:
            kinds = [t[0] for t in p]
            operands = sum(1 for k in kinds if k in ("num", "var"))
            if operands < 2 or not any(k in ("op", "eq", "is", "pow", "to",
                                             "allpow", "root") for k in kinds):
                continue
            if "comma" in kinds and ("is" in kinds or "eq" in kinds) and not (
                    "open" in kinds or any(
                        p[k][0] == "comma" and k + 1 < len(p) and
                        p[k + 1] == ("op", "*") for k in range(len(p)))):
                continue  # '72, over 120, which is 0,6': grouping unclear
            if "is" in kinds and ("eq" in kinds or "var" in kinds):
                # 'is' reads as '=' only between plain numbers
                cut = kinds.index("is")
                if "eq" in kinds[:cut] or "var" in kinds[:cut]:
                    p = p[:cut]
                else:
                    continue
                if sum(1 for t in p if t[0] in ("num", "var")) < 2:
                    continue
            readings = _render_span(p)
            if readings:
                out.append((readings, clean and not has_comma or clean and
                            "open" in kinds))
    return out


def _render_span(tokens):
    """Tokens -> up to 8 alternative ASCII strings."""
    results = []

    def emit(toks, choices):
        s, stack, i = [], [], 0
        side_start = 0
        pending_close = []   # for 'the quantity' groups
        choice_i = 0
        while i < len(toks):
            kind, val = toks[i]
            if kind == "num":
                s.append(val)
            elif kind == "var":
                s.append(" " + val + " ")
            elif kind == "op":
                if kind == "op" and val == "-" and (not s or s[-1].strip() in
                                                    ("", "=", "(", "+", "-", "*", "/")):
                    s.append(" -")
                else:
                    if val == "/" and choice_i < len(choices) and choices[choice_i] == "wide":
                        choice_i += 1
                        left = "".join(s[side_start:])
                        s[side_start:] = ["((" + left + ")/("]
                        stack.append("wide_over")
                    elif val == "/":
                        choice_i += 1
                        s.append(" / ")
                    else:
                        s.append(f" {val} ")
            elif kind == "neg":
                s.append(" -")
            elif kind == "pow":
                s.append(f"^({val})")
            elif kind == "allpow":
                while stack:
                    s.append(")" if stack.pop() != "wide_over" else "))")
                left = "".join(s[side_start:])
                s[side_start:] = [f"({left})^({val})"]
            elif kind == "to":
                wide = choice_i < len(choices) and choices[choice_i] == "wide"
                choice_i += 1
                j = i + 1
                expo = []
                if wide:
                    while j < len(toks) and toks[j][0] not in ("eq", "is", "comma"):
                        expo.append(toks[j])
                        j += 1
                else:
                    if j < len(toks) and toks[j][0] in ("neg",) or (
                            j < len(toks) and toks[j] == ("op", "-")):
                        expo.append(("neg", "-"))
                        j += 1
                    if j < len(toks) and toks[j][0] in ("num", "var"):
                        expo.append(toks[j])
                        j += 1
                sub = emit(expo, [])
                if sub is None:
                    return None
                s.append(f"^({sub})")
                i = j
                continue
            elif kind == "root":
                wide = choice_i < len(choices) and choices[choice_i] == "wide"
                choice_i += 1
                j = i + 1
                arg = []
                if wide:
                    while j < len(toks) and toks[j][0] not in ("eq", "is", "comma"):
                        arg.append(toks[j])
                        j += 1
                elif j < len(toks) and toks[j][0] in ("num", "var"):
                    arg.append(toks[j])
                    j += 1
                sub = emit(arg, [])
                if sub is None:
                    return None
                s.append(f" {val}({sub}) ")
                i = j
                continue
            elif kind in ("eq", "is"):
                while pending_close:
                    pending_close.pop()
                    s.append(")")
                while stack:
                    s.append(")" if stack.pop() != "wide_over" else "))")
                s.append(" = ")
                side_start = len(s)
            elif kind == "open":
                s.append(" (")
                pending_close.append(True)
            elif kind == "lp":
                s.append(" (")
            elif kind == "rp":
                s.append(") ")
            elif kind == "comma":
                if pending_close:
                    pending_close.pop()
                    s.append(")")
                # ', times ...' groups the left side as one factor
                nxt = toks[i + 1] if i + 1 < len(toks) else None
                if nxt and nxt[0] == "op" and nxt[1] in "*/":
                    left = "".join(s[side_start:])
                    s[side_start:] = ["(" + left + ")"]
                    s.append(f" {nxt[1]} (")
                    stack.append("group")
                    i += 2
                    continue
            i += 1
        while pending_close:
            pending_close.pop()
            s.append(")")
        while stack:
            s.append(")" if stack.pop() != "wide_over" else "))")
        return re.sub(r"\s+", " ", "".join(s)).strip()

    n_choice = sum(1 for k, v in tokens if k in ("to", "root") or
                   (k == "op" and v == "/"))
    n_choice = min(n_choice, 3)
    import itertools
    for combo in itertools.product(("narrow", "wide"), repeat=n_choice):
        r = emit(tokens, list(combo))
        if r and r not in results:
            results.append(r)
    extra = []
    for r in results:
        # 'minus two squared' is usually (-2)^2 when spoken
        v = re.sub(r"(?<![\w)])-\s*(\d+(?:\.\d+)?|[a-z])\s*\^", r"(-\1)^", r)
        # 'x minus four times x plus one' is usually (x - 4)(x + 1)
        sides = v.split(" = ")
        new_sides = []
        for side in sides:
            if side.count(" * ") == 1 and "(" not in side:
                left, right = side.split(" * ")
                if re.search(r"[+-]", left.strip().lstrip("-")) or re.search(
                        r"[+-]", right.strip().lstrip("-")):
                    side = f"({left})*({right})"
            new_sides.append(side)
        v2 = " = ".join(new_sides)
        for cand in (v, v2):
            if cand not in results and cand not in extra:
                extra.append(cand)
    return (results + extra)[:12]


def _spoken_item(readings):
    """Alternative readings -> (Item or None, parts_by_reading)."""
    alts_items = []
    for r in readings:
        if r.count("=") == 0:
            try:
                alts_items.append(("expr", parse_math(r), [r]))
            except ParseFailure:
                continue
        else:
            parts = [p.strip() for p in r.split("=")]
            try:
                exprs = [parse_math(p) for p in parts]
            except ParseFailure:
                continue
            alts_items.append(("rel", exprs, parts))
    return alts_items


def check_spoken_text(text, line, prev_item=None, pairs=None):
    """Spoken maths in one script/snippet paragraph -> (findings, last_item).

    pairs, when a list, collects (line, equation Item, solution Item) for
    the narration-vs-screen consistency check.
    """
    findings = []
    last = prev_item
    for sent in _sentences(text):
        if not re.search(r"\b(plus|minus|times|equals|squared|cubed|over|power"
                         r"|divided|multiplied|root|is)\b", sent, re.I):
            continue
        clauses = re.split(r"\s*(?:—|–|;|:(?=\s)|\bso\b|\bwhich gives\b|\bgives\b"
                           r"|\bgiving\b|\btherefore\b|\bhence\b|\bthen\b)\s*",
                           sent, flags=re.I)
        chain = []
        for clause in clauses:
            error_ctx = bool(_ERROR_CONTEXT.search(clause)) or bool(
                re.search(r"\b(wrong|error|mistake|trap|museum|exhibit|not"
                          r"|never|instead|broken)\b", sent, re.I))
            spans = spoken_to_math(clause)
            merged = _merge_spoken_solutions(spans, clause)
            if merged is not None:
                chain.append(merged)
                continue
            if len(spans) != 1:
                if spans:
                    chain.append(None)
                for readings, clean in spans:
                    findings.extend(_spoken_claims(readings, clause, line,
                                                   error_ctx or not clean)[0])
                continue
            f, item = _spoken_claims(spans[0][0], clause, line,
                                     error_ctx or not spans[0][1])
            findings.extend(f)
            if item is not None:
                item.clean = spans[0][1] and not error_ctx
            chain.append(item)
        steps = 0
        for k in range(1, len(chain)):
            a, b = chain[k - 1], chain[k]
            if a is None or b is None or a.kind != "eq" or b.kind not in ("eq", "sol"):
                continue
            steps += 1
            error_ctx = bool(_ERROR_CONTEXT.search(sent)) or not (
                a.clean and b.clean)
            findings.append(check_step(a, b, line, steps, sent, error_ctx,
                                       final=k == len(chain) - 1))
            if pairs is not None and b.kind == "sol" and a.clean and b.clean:
                pairs.append((line, a, b))
        formal = [c for c in chain if c is not None]
        if formal:
            last = formal[-1]
    return findings, last


def _merge_spoken_solutions(spans, clause):
    """'x equals zero or x equals five' / 'x equals zero or five' -> one
    solution Item; None when the clause is anything else."""
    low = clause.lower()
    m = re.search(r"\b([b-z]) equals ([\w\- ]+?) or (?:\1 equals )?"
                  r"((?:minus |negative )?[\w\-]+)\s*[.,]?\s*$", low)
    if not m:
        return None
    var = sp.Symbol(m.group(1))
    vals = []
    for chunk in (m.group(2), m.group(3)):
        words = chunk.replace("-", " ").split()
        neg = bool(words) and words[0] in ("minus", "negative")
        words = words[1:] if neg else words
        num = _read_number(words, 0) if words else None
        if not num or num[1] != len(words):
            if len(words) == 1 and re.fullmatch(r"\d+(?:[.,]\d+)?", words[0]):
                num = (words[0].replace(",", "."), 1)
            else:
                return None
        vals.append(sp.Rational(num[0]) * (-1 if neg else 1))
    clean = not _SPOKEN_UNHANDLED.search(low)
    return Item("sol", [(var, sp.FiniteSet(*vals))], clause, clean=clean)


def _spoken_claims(readings, clause, line, error_ctx):
    """One spoken span (several readings) -> (findings, Item for chaining)."""
    alts = _spoken_item(readings)
    if not alts:
        return [_finding("SKIPPED", line, None, "spoken maths not formalised",
                         clause, "spoken")], None
    rels = [a for a in alts if a[0] == "rel"]
    if not rels:
        return [], Item("expr", [a[1] for a in alts], clause)
    nparts = {len(a[1]) for a in rels}
    if len(nparts) != 1:
        return [_finding("SKIPPED", line, None, "ambiguous", clause, "spoken")], None
    n = nparts.pop()
    numeric = all(_is_number(e) for a in rels for e in a[1])
    if numeric or n >= 3:
        # every '=' in every reading must hold in at least one reading
        oks = []
        for _, exprs, parts in rels:
            good = True
            for k in range(1, len(exprs)):
                a, b = exprs[k - 1], exprs[k]
                if _is_number(a) != _is_number(b):
                    if k == 1 and isinstance(a, sp.Symbol):
                        continue
                    good = None
                    break
                r = _equal_step(a, b, parts[k], False, clause)
                if r != "ok":
                    good = False if r in ("wrong", "rounded") and good else None
                    if good is None:
                        break
            oks.append(good)
        if True in oks:
            return [_finding("STEP_OK", line, None, "", clause, "spoken-claim")], \
                _eq_item(rels, clause)
        if None in oks or error_ctx:
            return [_finding("SKIPPED", line, None,
                             "could not decide" if not error_ctx else
                             "false on purpose? (error-example wording)",
                             clause, "spoken-claim")], None
        return [_finding("STEP_WRONG", line, 1,
                         "spoken claim is false under every reading", clause,
                         "spoken-claim")], None
    item = _eq_item(rels, clause)
    if item is None:
        return [], None
    if item.kind == "sol":
        return [], item
    return check_identity(item, clause, line, error_ctx), item


def _eq_item(rels, clause):
    alts = []
    sol = []
    for _, exprs, parts in rels:
        if len(exprs) != 2:
            continue
        lhs, rhs = exprs
        if isinstance(lhs, sp.Symbol) and _is_number(rhs):
            sol.append((lhs, sp.FiniteSet(rhs)))
        alts.append((lhs, rhs))
    if sol and len(sol) == len(alts):
        return Item("sol", sol, clause)
    if alts:
        return Item("eq", alts, clause)
    return None


# --- LaTeX (animations) ---

def latex_to_plain(tex):
    s = str(tex)
    s = re.sub(r"\^\s*(?:\{\s*\\circ\s*\}|\\circ)", "°", s)
    s = re.sub(r"\\times\s*(?=\\;|\\quad|\\qquad|$|\})", " ✗ ", s)  # a cross mark
    s = s.replace(r"\ell", " ℓ ").replace(r"\bar{x}", " xbar ")
    s = re.sub(r"\\(?:text|mathrm|textbf|mathbf|operatorname)\{([^{}]*)\}",
               r" \1 ", s)
    for a, b in ((r"\left", ""), (r"\right", ""), (r"\,", " "), (r"\;", " "),
                 (r"\!", ""), (r"\quad", " ; "), (r"\qquad", " ; "),
                 (r"\times", "×"), (r"\cdot", "·"), (r"\div", "÷"),
                 (r"\pm", "±"), (r"\leq", "≤"), (r"\geq", "≥"), (r"\le", "≤"),
                 (r"\ge", "≥"), (r"\neq", "≠"), (r"\ne", "≠"),
                 (r"\approx", "≈"), (r"\Rightarrow", " → "),
                 (r"\rightarrow", " → "), (r"\Longrightarrow", " → "),
                 (r"\implies", " → "), (r"\to", " → "), (r"\therefore", " so "),
                 (r"\checkmark", " ✓ "), (r"\circ", "°"), (r"\%", "%"),
                 (r"\pi", "π"), (r"\theta", "θ"), (r"\alpha", "α"),
                 (r"\beta", "β"), (r"\{", "("), (r"\}", ")"), (r"\ldots", "..."),
                 (r"\cdots", "..."), ("{,}", ","), (r"\infty", "∞")):
        s = s.replace(a, b)
    for _ in range(4):
        s = re.sub(r"\\[dt]?frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}", r"((\1)/(\2))", s)
        s = re.sub(r"\\[dt]?frac\s*(\d)(\d)", r"(\1/\2)", s)
        s = re.sub(r"\\sqrt\s*\[([^\]]+)\]\s*\{([^{}]*)\}", r"((\2)^(1/(\1)))", s)
        s = re.sub(r"\\sqrt\s*\{([^{}]*)\}", r"sqrt(\1)", s)
        s = re.sub(r"\^\s*\{([^{}]*)\}", r"^(\1)", s)
        s = re.sub(r"_\s*\{([^{}]*)\}", r"_\1", s)
    s = re.sub(r"\\(sin|cos|tan|log|ln)\b", r"\1", s)
    s = re.sub(r"\\hat\{([^{}]*)\}", r"\1̂", s)
    s = re.sub(r"\\[A-Za-z]+", " Sym ", s)  # an unknown command is prose
    s = s.replace("{", "(").replace("}", ")")
    return re.sub(r"\s+", " ", s).strip()


def manim_math(path):
    """manim_scene.py -> [(line, plain_text, subtopic_ref)] of on-screen maths."""
    import ast
    src = Path(path).read_text(encoding="utf-8")
    lines = src.splitlines()
    bands = []
    for i, l in enumerate(lines, 1):
        m = re.search(r"#\s*---\s*Band\s*\d+\s*\((subtopic_\d+)", l)
        if m:
            bands.append((i, m.group(1)))
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None
    out = []
    assigned = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and \
                isinstance(node.targets[0], ast.Name):
            for sub in ast.walk(node.value):
                if isinstance(sub, ast.Call):
                    assigned[id(sub)] = node.targets[0].id
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func.id if isinstance(node.func, ast.Name) else (
            node.func.attr if isinstance(node.func, ast.Attribute) else "")
        if fn not in ("MathTex", "Tex"):
            continue
        strs = [a.value for a in node.args
                if isinstance(a, ast.Constant) and isinstance(a.value, str)]
        if not strs:
            continue
        raw = " ".join(strs) if fn == "MathTex" else " ".join(strs)
        if fn == "Tex":
            segs = re.findall(r"\$([^$]+)\$", raw)
            if not segs:
                continue
            texts = [latex_to_plain(x) for x in segs]
        else:
            texts = [latex_to_plain(raw)]
        ref = None
        for ln, r in bands:
            if ln <= node.lineno:
                ref = r
        wrong = any(isinstance(k, ast.keyword) and k.arg == "color" and
                    "RED" in ast.unparse(k.value) for k in node.keywords)
        target = assigned.get(id(node))
        if target and re.search(r"strike\(\s*" + re.escape(target) + r"\b|"
                                + re.escape(target) + r"\b[^\n]*color\s*=\s*RED"
                                r"|Cross\(\s*" + re.escape(target) + r"\b", src):
            wrong = True
        for t in texts:
            out.append((node.lineno, t + (" ✗" if wrong else ""), ref, raw))
    out.sort(key=lambda x: x[0])
    return out


def _latex_malformed(raw):
    depth = 0
    for ch in raw.replace(r"\{", "").replace(r"\}", ""):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                return "unbalanced braces"
    return "unbalanced braces" if depth else None


# --- content walkers ---

def _grade_of(path):
    m = re.search(r"grade(\d+)", str(path))
    return f"grade{m.group(1)}" if m else "unknown"


def _subject_of(path):
    p = str(path)
    return "mathematical_literacy" if "mathematical_literacy" in p else (
        "maths" if "/maths/" in p or p.startswith("maths/") else "unknown")


def _rel(path):
    try:
        return Path(path).resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(path)


def check_question_md(path):
    """Knowledge-bite question.md: worked solution chains + final answer."""
    text = Path(path).read_text(encoding="utf-8")
    lit = "mathematical_literacy" in str(path)
    findings = []
    section = None
    question_lines, answer_lines = [], []
    last = None
    for ln, raw in enumerate(text.splitlines(), 1):
        if raw.startswith("## "):
            section = raw[3:].lower()
            last = None
            continue
        if not raw.strip() or raw.startswith("#") or raw.startswith("**"):
            continue
        if section is None or section.startswith("method"):
            continue
        if section.startswith("question"):
            why = _malformed_line(raw)
            if why:
                findings.append(_finding("UNPARSEABLE", ln, None, why, raw,
                                         "malformed"))
                continue
            question_lines.append((ln, raw))
            continue
        if section.startswith("answer"):
            answer_lines.append((ln, raw))
        f, last = check_written_line(raw, ln, lit=lit, prev_item=last)
        findings.extend(f)
    findings.extend(_answer_check(question_lines, answer_lines, lit))
    return findings


def _answer_check(question_lines, answer_lines, lit):
    """'Solve for x: <one equation>' vs the stated answer."""
    qtext = " ".join(t for _, t in question_lines)
    if not re.search(r"\bsolve\b", qtext, re.I) or re.search(
            r"simultaneous|inequalit|<|>|≤|≥|\bsin|\bcos|\btan|log|interval"
            r"|domain|\bif\b|graph", qtext, re.I):
        return []
    eqs = []
    for _, t in question_lines:
        for sent in _sentences(t):
            for piece in re.split(r":\s+|\s{2,}", written_normalise(sent, lit)):
                item, parts = _written_relation(piece)
                if item is not None and item.kind == "eq":
                    eqs.append(item)
    if len(eqs) != 1:
        return []
    eq = eqs[0]
    for ln, t in answer_lines:
        sols = [s for s in (_parse_solution(p) for p in re.split(
            r"\s+OR\s+|\s*;\s*", written_normalise(t, lit)))]
        if not sols or any(s is None for s in sols):
            continue
        var = sols[0].alts[0][0]
        vals = set()
        for s in sols:
            if s.alts[0][0] != var:
                return []
            vals |= set(s.alts[0][1])
        stated = Item("sol", [(var, sp.FiniteSet(*vals))], t,
                      decimals=_decimals(t))
        f = check_step(eq, stated, ln, None, t, False, final=True)
        f["kind"] = "answer"
        if f["verdict"] == "STEP_OK":
            f["reason"] = "answer matches a solve of the question"
        return [f]
    return []


def check_script_md(path):
    text = Path(path).read_text(encoding="utf-8")
    findings = []
    for ln, raw in enumerate(text.splitlines(), 1):
        if not raw.strip() or raw.startswith("#"):
            continue
        if "open bracket" in raw and "close bracket" in raw and \
                raw.count("open bracket") != raw.count("close bracket"):
            findings.append(_finding("UNPARSEABLE", ln, None,
                                     "unbalanced spoken brackets", raw,
                                     "malformed"))
            continue
        f, _ = check_spoken_text(raw, ln)
        findings.extend(f)
    return findings


def check_manim(path):
    items = manim_math(path)
    if items is None:
        return [_finding("SKIPPED", 1, None, "manim_scene.py does not parse",
                         "", "animation")]
    lit = "mathematical_literacy" in str(path)
    findings = []
    last, last_ref = None, None
    for ln, plain, ref, raw in items:
        why = _latex_malformed(raw) or _malformed_line(plain)
        if why:
            findings.append(_finding("UNPARSEABLE", ln, None, why, raw,
                                     "malformed"))
            continue
        # consecutive lines of one band are the next step of the derivation
        # (a mismatch across lines is only ever SKIPPED: it may be a new
        # example)
        f, last = check_written_text(plain, ln, lit=lit,
                                     prev_item=last if ref == last_ref else None,
                                     link_prev=True)
        last_ref = ref
        findings.extend(f)
    return findings


def _script_subtopics(path):
    """script.md -> {subtopic_N: [(line, text)]} in heading order."""
    out, cur, n = defaultdict(list), None, 0
    for ln, raw in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if raw.startswith("## Subtopic"):
            n += 1
            cur = f"subtopic_{n}"
            continue
        if raw.startswith("# "):
            continue
        if cur and raw.strip():
            out[cur].append((ln, raw))
    return out


def _screen_by_band(items):
    """{subtopic: {'eqs': [Item], 'vals': {var: set(floats)}}} of the maths
    shown on screen in each subtopic band."""
    bands = defaultdict(lambda: {"eqs": [], "vals": defaultdict(set)})
    for ln, plain, ref, raw in items:
        if ref is None or "✗" in plain:
            continue
        for piece in _clauses(written_normalise(plain)):
            item, parts = _written_relation(piece)
            if item is None and len(parts) >= 3 and parts[0][0] == "expr" \
                    and isinstance(parts[0][1], sp.Symbol) and all(
                        p[0] == "expr" and _is_number(p[1]) for p in parts[1:]):
                # 'n = 98/3 = 32,67...'
                item = Item("sol", [(parts[0][1], sp.FiniteSet(parts[1][1]))],
                            piece)
            if item is None:
                continue
            if item.kind == "eq":
                bands[ref]["eqs"].append(item)
            elif item.kind == "sol":
                var, fs = item.alts[0]
                for v in fs:
                    f = to_float(v)
                    if f is not None:
                        bands[ref]["vals"][var].add(round(f, 4))
    return bands


def check_consistency(script_path, manim_path):
    """Narration vs the on-screen step of the same subtopic band.

    Anchored on the equation, never on wording: a narration chain
    'equation -> x = v' is compared only when the SAME equation (same
    solution set, any route) is on screen in that subtopic's band, and it
    is flagged only when the narrated value is none of the values the
    screen states for that unknown.
    """
    items = manim_math(manim_path)
    if items is None:
        return []
    screen = _screen_by_band(items)
    spoken = _script_subtopics(script_path)
    findings = []
    for ref, band in screen.items():
        if not band["eqs"] or not band["vals"]:
            continue
        pairs = []
        for ln, raw in spoken.get(ref, []):
            check_spoken_text(raw, ln, pairs=pairs)
        for ln, eq, sol in pairs:
            nsets = [x for x in _solution_set(eq) if x is not None]
            var, said = sol.alts[0]
            shown = band["vals"].get(var)
            if not nsets or not shown:
                continue
            same = False
            for seq in band["eqs"]:
                for sset in _solution_set(seq):
                    if sset is None or sset[0] != var:
                        continue
                    stated = {round(to_float(v), 4) for v in sset[1]
                              if to_float(v) is not None} if isinstance(
                        sset[1], sp.FiniteSet) else set()
                    if not stated & shown:
                        continue  # the screen never states this one's answer
                    if any(n[0] == var and _set_relation(n[1], sset[1]) ==
                           "equal" for n in nsets):
                        same = True
            if not same:
                continue
            said_f = {round(to_float(v), 4) for v in said
                      if to_float(v) is not None}
            if said_f & shown:
                findings.append(_finding("CONSISTENT", ln, None,
                                         f"{ref} {var}", "", "consistency"))
            else:
                findings.append(_finding(
                    "CONTRADICTS_SCREEN", ln, None,
                    f"{ref}: narration gives {var} = "
                    f"{', '.join(f'{x:g}' for x in sorted(said_f))}; the screen "
                    f"shows {var} = {', '.join(f'{x:g}' for x in sorted(shown))} "
                    "for the same equation", "", "consistency"))
    return findings


def iter_step_content(root=CURRICULUM_ROOT):
    """(content_type, path) for every factory item the step checker reads."""
    for subject in SUBJECTS:
        base = Path(root) / subject
        for p in sorted((base / "session").rglob("script.md")) if (
                base / "session").is_dir() else []:
            if "overlays" in p.parts:
                continue
            yield "script", p
            m = p.with_name("manim_scene.py")
            if m.exists():
                yield "animation", m
                yield "consistency", (p, m)
        kb = base / "knowledge_bites"
        for p in sorted(kb.rglob("question.md")) if kb.is_dir() else []:
            yield "knowledge_bite", p


_CHECKERS = {"script": check_script_md, "knowledge_bite": check_question_md,
             "animation": check_manim}


def run_steps(items):
    rows = []
    for ctype, path in items:
        try:
            with time_limit(TIMEOUT_SECONDS * 60):
                if ctype == "consistency":
                    found = check_consistency(*path)
                    path = path[0]
                else:
                    found = _CHECKERS[ctype](path)
        except Timeout:
            found = [_finding("SKIPPED", 1, None, "timeout", "", ctype)]
        for f in found:
            f.update(content_type=ctype, path=_rel(path),
                     subject=_subject_of(_rel(path)), grade=_grade_of(path))
            rows.append(f)
    return rows


def summarise_steps(rows):
    by = defaultdict(Counter)
    for r in rows:
        by[f"{r['content_type']} | {r['subject']} {r['grade']}"][r["verdict"]] += 1
    flagged = [r for r in rows if r["verdict"] in STEP_FLAGGED + (
        "CONTRADICTS_SCREEN",)]
    warnings = [r for r in rows if r["verdict"] == "WARNING"]
    return {"by_type_grade": {k: dict(v) for k, v in sorted(by.items())},
            "totals": dict(Counter(r["verdict"] for r in rows)),
            "flagged": flagged, "warnings": warnings}


def steps_markdown(summary):
    cols = STEP_VERDICTS + ("CONSISTENT", "CONTRADICTS_SCREEN")
    out = ["# Maths step verification (report only)", "",
           "Checks truth, not method: every stated step must be true "
           "(equivalent, solution set preserved, numeric fact correct); "
           "route, order and shortcuts are never judged. Findings never "
           "fail the build.", "",
           "| content \\| grade | " + " | ".join(cols) + " |",
           "|---|" + "---|" * len(cols)]
    for k, c in summary["by_type_grade"].items():
        out.append(f"| {k} | " + " | ".join(str(c.get(v, 0)) for v in cols) + " |")
    out += ["", "## Flagged", ""]
    if not summary["flagged"]:
        out.append("None.")
    for f in summary["flagged"]:
        step = f" step {f['step']}" if f.get("step") else ""
        out.append(f"- **{f['verdict']}**{step} `{f['path']}:{f['line']}` — "
                   f"{f['reason']}")
        if f.get("text"):
            out.append(f"  - {str(f['text'])[:300]}")
    out += ["", "## Warnings (roots lost/gained, unstated rounding)", ""]
    for f in summary["warnings"]:
        out.append(f"- `{f['path']}:{f['line']}` — {f['reason']}")
    return "\n".join(out) + "\n"


# --- private tutor content (local CLI only) ---

def _agent_get(repo, path, ref, token):
    import urllib.request
    url = f"https://api.github.com/repos/{repo}/contents/{path}?ref={ref}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.raw",
        "X-GitHub-Api-Version": "2022-11-28"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def _agent_tree(repo, ref, token):
    import urllib.request
    url = f"https://api.github.com/repos/{repo}/git/trees/{ref}?recursive=1"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return [t["path"] for t in json.loads(r.read())["tree"]
                if t["type"] == "blob"]


def check_agent(repo="RokctAI/agent", ref="main", token=None):
    """Tutor snippets and whiteboard animations in the PRIVATE agent repo,
    read through the REST API only (nothing is cloned or written to disk).

    Returns rows WITHOUT any text: path, line, verdict, step, content_type.
    """
    import os
    token = token or os.environ.get("MONOREPO_PAT") or os.environ.get(
        "GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("--agent needs MONOREPO_PAT, GH_TOKEN or GITHUB_TOKEN")
    paths = _agent_tree(repo, ref, token)
    rows = []
    wanted = [p for p in paths if re.search(
        r"^lms/team/tutors/CAPS/[^/]+/(samples\.json|samples/[^/]+\.md)$", p)]
    wanted += [p for p in paths if re.search(r"(^|/)animations\.json$", p)]
    for p in sorted(wanted):
        raw = _agent_get(repo, p, ref, token)
        lines = raw.splitlines()
        found, ctype = [], "tutor_snippet"
        if p.endswith("samples.json"):
            try:
                data = json.loads(raw)
            except ValueError:
                continue
            for s in data.get("samples", []) or []:
                script = s.get("script") or ""
                if not script:
                    continue
                # the JSON line that holds this sample's script
                key = json.dumps(script, ensure_ascii=False)[1:41]
                ln = next((i for i, l in enumerate(lines, 1)
                           if '"script"' in l and key in l), 1)
                f, _ = check_spoken_text(script, ln)
                f += _spoken_task_answer(script, ln)
                for x in f:
                    x["grade"] = f"grade{s.get('grade')}" if s.get("grade") \
                        else "unknown"
                found += f
        elif p.endswith(".md"):
            for ln, l in enumerate(lines, 1):
                if l.strip() and not l.startswith("#"):
                    f, _ = check_spoken_text(l, ln)
                    found += f + _spoken_task_answer(l, ln)
        else:
            ctype = "animation"
            try:
                data = json.loads(raw)
            except ValueError:
                continue
            last = None
            for prim in sorted(data.get("primitives", []) or [],
                               key=lambda x: x.get("time", 0)):
                if prim.get("primitive") == "camera_move":
                    last = None  # a new board region
                t = prim.get("text")
                if not t:
                    continue
                ln = next((i for i, l in enumerate(lines, 1)
                           if json.dumps(t)[1:-1][:40] in l), 1)
                why = _malformed_line(t)
                if why:
                    found.append(_finding("UNPARSEABLE", ln, None, why, "",
                                          "malformed"))
                    continue
                f, last = check_written_text(latex_to_plain(t), ln,
                                             prev_item=last, link_prev=True)
                found += f
        for x in found:
            x.update(content_type=ctype, path=p, text="",
                     subject="agent", grade=x.get("grade", "unknown"))
            x["reason"] = ""  # never carry private wording out
            rows.append(x)
    return rows


def _spoken_task_answer(text, line):
    """'Factorise <E>. ... <product>.' -> the product must equal E."""
    m = re.search(r"\bfactori[sz]e\s+([^.]+)\.", text, re.I)
    if not m:
        return []
    task = spoken_to_math(m.group(1))
    if len(task) != 1:
        return []
    try:
        targets = [parse_math(r) for r in task[0][0] if "=" not in r]
    except ParseFailure:
        return []
    if not targets:
        return []
    rest = text[m.end():]
    answers = []
    for sent in _sentences(rest):
        for readings, _clean in spoken_to_math(sent):
            for r in readings:
                if "=" in r:
                    continue
                try:
                    e = parse_math(r)
                except ParseFailure:
                    continue
                if isinstance(e, sp.Mul) and sum(
                        1 for f in e.args if f.free_symbols) >= 2 and \
                        e.free_symbols == targets[0].free_symbols:
                    answers.append((readings, sent))
                    break
    if not answers:
        return []
    readings, sent = answers[-1]
    ok = any(equivalent(t, parse_math(r)) for t in targets for r in readings
             if "=" not in r)
    if ok:
        return [_finding("STEP_OK", line, None, "factorised answer expands back",
                         sent, "answer")]
    if _ERROR_CONTEXT.search(sent):
        return [_finding("SKIPPED", line, None, "error-example wording", sent,
                         "answer")]
    return [_finding("ANSWER_WRONG", line, None,
                     "factorised answer does not expand to the task", sent,
                     "answer")]


def _step_counts_line(name, c):
    checked = sum(c.get(v, 0) for v in ("STEP_OK", "STEP_WRONG", "ANSWER_WRONG",
                                        "WARNING", "CONSISTENT",
                                        "CONTRADICTS_SCREEN"))
    flagged = sum(c.get(v, 0) for v in STEP_FLAGGED + ("CONTRADICTS_SCREEN",))
    ok = c.get("STEP_OK", 0) + c.get("CONSISTENT", 0)
    return (f"  {name}: checked {checked}, OK {ok}, flagged {flagged}, "
            f"warnings {c.get('WARNING', 0)}, skipped {c.get('SKIPPED', 0)}")


def _main_steps(args):
    items = [x for x in iter_step_content(Path(args.root))
             if not args.content or x[0] in args.content]
    rows = run_steps(items)
    summary = summarise_steps(rows)
    if args.steps_json:
        Path(args.steps_json).write_text(
            json.dumps(summary, indent=2, ensure_ascii=False, default=str) + "\n",
            encoding="utf-8")
    md = steps_markdown(summary)
    if args.steps_md:
        Path(args.steps_md).write_text(md, encoding="utf-8")
    print("Step checks (truth, not method):")
    by_type = defaultdict(Counter)
    for k, c in summary["by_type_grade"].items():
        by_type[k.split(" | ")[0]].update(c)
        print(_step_counts_line(k, c))
    for k, c in sorted(by_type.items()):
        print(_step_counts_line("TOTAL " + k, c))
    for f in summary["flagged"]:
        step = f" step {f['step']}" if f.get("step") else ""
        print(f"  {f['verdict']}{step} {f['path']}:{f['line']} — {f['reason']}")
    return summary


def _main_agent(args):
    rows = check_agent(args.agent_repo, args.agent_ref)
    counts = defaultdict(Counter)
    for r in rows:
        counts[f"{r['content_type']} {r['grade']}"][r["verdict"]] += 1
        if r["verdict"] != "SKIPPED":
            step = f" (step {r['step']})" if r.get("step") else ""
            print(f"{r['path']}:{r['line']} — {r['verdict']}{step}")
    for k, c in sorted(counts.items()):
        print(_step_counts_line(k, c))
    return 0  # report-only


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paths", nargs="*",
                    help="mcq.json files (default: every maths and Maths Lit mcq.json)")
    ap.add_argument("--json", dest="json_out", help="write the JSON report here")
    ap.add_argument("--md", dest="md_out", help="write the markdown summary here")
    ap.add_argument("--steps", action="store_true",
                    help="also step-check what we teach: lesson scripts, "
                         "knowledge-bite worked solutions, lesson animations "
                         "and narration-vs-screen consistency")
    ap.add_argument("--steps-only", action="store_true",
                    help="step checks only (skip the MCQ answer keys)")
    ap.add_argument("--steps-json", help="write the step-check JSON report here")
    ap.add_argument("--steps-md", help="write the step-check markdown here")
    ap.add_argument("--content", action="append",
                    choices=("script", "knowledge_bite", "animation",
                             "consistency"),
                    help="limit step checks to these content types")
    ap.add_argument("--agent", action="store_true",
                    help="LOCAL ONLY: step-check the private agent repo's tutor "
                         "snippets and animations through the GitHub REST API "
                         "(token: MONOREPO_PAT / GH_TOKEN / GITHUB_TOKEN). "
                         "Prints only 'path:line — verdict'; never text.")
    ap.add_argument("--root", default=str(CURRICULUM_ROOT),
                    help="curriculum root for the step checks")
    ap.add_argument("--agent-repo", default="RokctAI/agent")
    ap.add_argument("--agent-ref", default="main")
    args = ap.parse_args(argv)
    if args.agent:
        return _main_agent(args)
    if args.steps or args.steps_only:
        _main_steps(args)
        if args.steps_only:
            return 0
    paths = [Path(p) for p in args.paths] or list(iter_mcq_files())
    summary = summarise(run(paths))
    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8")
    md = to_markdown(summary)
    if args.md_out:
        Path(args.md_out).write_text(md, encoding="utf-8")
    t = summary["totals"]
    print(f"{summary['total_questions']} MCQs: "
          + ", ".join(f"{v} {t[v]}" for v in VERDICTS))
    for name, counts in summary["by_subject"].items():
        print(f"  {name}: " + ", ".join(f"{v} {counts[v]}" for v in VERDICTS))
    return 0  # report-only: findings never fail the build


if __name__ == "__main__":
    sys.exit(main())
