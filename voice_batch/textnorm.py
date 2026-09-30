"""Text handling shared by the renderer and the QC gate.

* split_sentences: a line is rendered one sentence at a time.
* speak_text: punctuation-only changes for the TTS prompt (a spaced hyphen
  or dash is a pause, never "minus"; a colon is a comma). Words never change.
* norm_words / word_errors: the word-exact ASR check. Numbers and a few
  spelling variants are normalised; everything else must match exactly.
"""
from __future__ import annotations

import difflib
import re

_SENT_RE = re.compile(r"(?<=[.!?])\s+")


def split_sentences(text: str) -> list[str]:
    return [s.strip() for s in _SENT_RE.split(" ".join(text.split())) if s.strip()]


def speak_text(sentence: str) -> str:
    s = sentence.replace("’", "'")
    s = s.replace(" — ", ", ").replace("—", ", ").replace(" – ", ", ")
    s = s.replace(" - ", ", ")
    s = re.sub(r":\s+", ", ", s)
    return " ".join(s.split())


_ONES = ("zero one two three four five six seven eight nine ten eleven twelve "
         "thirteen fourteen fifteen sixteen seventeen eighteen nineteen").split()
_TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def _n2w(n: int) -> str:
    if n < 20:
        return _ONES[n]
    if n < 100:
        return _TENS[n // 10] + ("" if n % 10 == 0 else " " + _ONES[n % 10])
    if n < 1000:
        rest = n % 100
        return _ONES[n // 100] + " hundred" + ("" if rest == 0 else " and " + _n2w(rest))
    return str(n)


# British/American spelling pairs the ASR model may pick either way.
_SPELLING = {"practice": "practise", "factorize": "factorise", "factorizing": "factorising",
             "factorized": "factorised", "recognize": "recognise", "organize": "organise",
             "okay": "ok"}


def norm_words(text: str) -> list[str]:
    s = text.lower().replace("’", "'").replace("'", "")
    s = s.replace("×", " times ").replace("²", " squared ").replace("−", "-")
    s = re.sub(r"(^|[\s(=,])-\s*(?=\d)", r"\1 minus ", s)
    s = re.sub(r"(\d)([a-z])", r"\1 \2", s)
    s = re.sub(r"\d+", lambda m: " " + _n2w(int(m.group())) + " ", s)
    s = re.sub(r"[^a-z ]", " ", s)
    return [_SPELLING.get(w, w) for w in s.split()]


def word_errors(reference: str, hypothesis: str) -> int:
    a, b = norm_words(reference), norm_words(hypothesis)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    return sum(max(i2 - i1, j2 - j1) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal")
