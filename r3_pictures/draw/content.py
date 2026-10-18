"""The lesson side of the pictures, read from files outside this repo.

This repository is public, so it holds only the engine: the drawing library
and the code that draws each object. Two inputs come from the private
repos at run time (build.py --slugs / --text):

* SLUGS: the picture slugs the R-3 packs use (for example RokctAI/agent
  lms/dart/test/r3_pack_picture_slugs.json). Rules such as "every clock
  time a pack names gets a clock" and "every word_<x> slug gets a word
  card" walk this set.
* TEXT: every word, phrase or sentence a picture prints (word cards,
  sentence strips, speech bubbles, titles, labels), keyed by words('<key>').
  A key looks like '<module>:<slug>' or '<module>:<slug>.<n>'.

A picture that asks for a key the text file does not have is not written;
build.py lists it under "needs text".
"""
import json
import re

SLUGS = set()
TEXT = {}
MISSING = set()   # keys asked for since the last art() call
SKIPPED = {}      # slug -> keys it needed but the text file lacks
ABSENT = set()    # tables the text file lacks (their pictures are not drawn)


def load_slugs(path):
    """A pack slug file: {grade: [slug, ...]}, {slug: [grade, ...]} or [slug, ...]."""
    with open(path, encoding='utf-8') as f:
        d = json.load(f)
    if isinstance(d, list):
        return {s for s in d}
    if all(isinstance(v, list) for v in d.values()) and all(isinstance(x, str) for v in d.values() for x in v):
        # grade -> slugs, or slug -> grades: tell them apart by the keys
        if len(d) <= 12:
            return {s for v in d.values() for s in v}
    return set(d)


def load(slugs_path=None, text_path=None):
    SLUGS.clear()
    TEXT.clear()
    MISSING.clear()
    SKIPPED.clear()
    ABSENT.clear()
    if slugs_path:
        SLUGS.update(load_slugs(slugs_path))
    if text_path:
        with open(text_path, encoding='utf-8') as f:
            d = json.load(f)
        TEXT.update(d.get('text', d))


def pack(pattern, keep=None):
    """The pack slugs matching pattern (whole slug), sorted; keep(match)
    can drop some. Drawing rules walk these instead of a fixed list."""
    rx = re.compile(pattern)
    out = []
    for s in sorted(SLUGS):
        m = rx.fullmatch(s)
        if m and (keep is None or keep(m)):
            out.append(s)
    return out


def words(key, n=None):
    """The words for key: a string, or a list of n lines when n is given.
    When the text file lacks the key, a stand-in of the same shape comes
    back and the picture is not written."""
    if key in TEXT:
        return TEXT[key]
    MISSING.add(key)
    return '?' if n is None else ['?'] * n


def table(key):
    """A {slug: words} table from the text file ({} when absent)."""
    v = TEXT.get(key)
    if v is None:
        ABSENT.add(key)
        return {}
    return v


def uses(slug):
    """Called by lib.body: reusing a skipped picture skips this one too."""
    if slug in SKIPPED:
        MISSING.add('picture:' + slug)


def settle(slug):
    """Called by lib.art: a picture whose words were missing is skipped."""
    SKIPPED.pop(slug, None)
    if MISSING:
        SKIPPED[slug] = sorted(MISSING)
        MISSING.clear()
