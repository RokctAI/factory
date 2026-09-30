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

"""Report-only maths correctness verifier for maths and Maths Lit MCQs.

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

Usage (repo root):
    python3 lessons/scripts/CAPS/math_verify.py \\
        --json math_verify_report.json --md math_verify_report.md
    python3 lessons/scripts/CAPS/math_verify.py path/to/mcq.json ...
"""

import argparse
import json
import random
import re
import signal
import sys
from collections import Counter, defaultdict
from contextlib import contextmanager
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


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paths", nargs="*",
                    help="mcq.json files (default: every maths and Maths Lit mcq.json)")
    ap.add_argument("--json", dest="json_out", help="write the JSON report here")
    ap.add_argument("--md", dest="md_out", help="write the markdown summary here")
    args = ap.parse_args(argv)
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
