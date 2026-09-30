#!/usr/bin/env python3
"""Pronunciation audition: one short clip per changed word and voice, so
someone can listen to a pronunciations.json entry and adjust it.

    # plan: which words changed, which voices (GitHub step outputs)
    python voice_batch/audition.py plan --before <sha> --after <sha> [--words "Mahikeng,Thendo"]

    # render one voice's clips into the agent checkout
    python voice_batch/audition.py render --agent-root .agent --voice voice_a \
        --ref .agent/<ref> --ref-sha256 <hex> --model-path <snapshot dir> \
        --work $RUNNER_TEMP/audition --words-json words.json --summary summary.md

Changed words: keys added to or changed in "words" (their respelling), and
for an added or changed "ambiguous" entry every listed variant. --words
(a manual run) names entries instead, whatever changed.

Carrier: "<respelling>. <respelling>." rendered as one take: the word said
twice, short enough to judge, and a lone word is where the model is least
stable. Seeds 11, then 22, then 33, until a take passes a light QC (no ASR:
these are odd words): 0.4-8 s long, not silent, speaker similarity >= 0.75,
and the tail check from qc.py (tail_db/tail_ok: last 50 ms at or below
-34 dB of the loudest 10 ms frame). The prompt carries textnorm's tail pad. If none
passes, the best-scoring take is kept and marked passed: false.

Output (agent repo, never this public repo):
lms/team/voices/samples/pronunciation/<voice>/<word>--<respelling>.mp3 plus
audition.json beside them. voices/samples/ is excluded from the app bundle.
Logs and the summary carry words, respellings and paths only: the same text
that is already public in pronunciations.json.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import pronunciations  # noqa: E402
from qc import tail_db, tail_ok  # noqa: E402
from textnorm import speak_text  # noqa: E402

PRON_REL = "voice_batch/pronunciations.json"
INBOX = HERE.parent / "voice_batches" / "inbox"
VOICES = ("voice_a", "voice_b")
BRANCH = "rokct/pronunciation-audition"
OUT_DIR = "lms/team/voices/samples/pronunciation"
SEEDS = (11, 22, 33)
MAX_CLIPS = 30
MIN_SIM, MIN_S, MAX_S, MIN_DBFS = 0.75, 0.4, 8.0, -45.0


class AuditionError(ValueError):
    pass


# ---------------------------------------------------------------------------
# What to render
# ---------------------------------------------------------------------------

def slug(s: str) -> str:
    """ASCII, lower case, [a-z0-9-] only: 'Nkosi’s TEN-doh' -> 'nkosis-ten-doh'."""
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"['’]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:48].strip("-") or "x"


def clip_name(word: str, respelling: str) -> str:
    return f"{slug(word)}--{slug(respelling)}"


def carrier(respelling: str) -> str:
    return f"{respelling}. {respelling}."


def _entry(word: str, respelling: str, kind: str) -> dict:
    return {"word": word, "respelling": respelling, "kind": kind, "clip": clip_name(word, respelling),
            "carrier": carrier(respelling)}


def _dedupe(rows: list[dict]) -> list[dict]:
    seen, out = set(), []
    for r in rows:
        if r["clip"] not in seen:
            seen.add(r["clip"]); out.append(r)
    return out


def changed(old: dict, new: dict) -> list[dict]:
    """Added or changed "words" keys, and every variant of an added or
    changed "ambiguous" entry. Removed entries render nothing."""
    rows = [_entry(w, r, "word") for w, r in new["words"].items() if old["words"].get(w) != r]
    for w, vs in new["ambiguous"].items():
        if old["ambiguous"].get(w) != vs:
            rows += [_entry(w, v, "ambiguous") for v in vs]
    return _dedupe(rows)


def requested(pron: dict, names: list[str]) -> list[dict]:
    """The entries a manual run names (any case)."""
    words = {w.lower(): w for w in pron["words"]}
    amb = {w.lower(): w for w in pron["ambiguous"]}
    rows, unknown = [], []
    for n in names:
        k = " ".join(n.split()).lower()
        if k in words:
            rows.append(_entry(words[k], pron["words"][words[k]], "word"))
        elif k in amb:
            rows += [_entry(amb[k], v, "ambiguous") for v in pron["ambiguous"][amb[k]]]
        else:
            unknown.append(n)
    if unknown:
        raise AuditionError(f"not in pronunciations.json: {unknown}")
    return _dedupe(rows)


def parse_words(arg: str) -> list[str]:
    return [w.strip() for w in arg.split(",") if w.strip()]


def file_at(rev: str, path: str = PRON_REL, cwd: str | Path | None = None, strict: bool = False) -> dict:
    """pronunciations.json at a git revision, validated; empty if it did not
    exist. strict (the new file): an invalid file raises. Otherwise (the old
    file) an invalid one counts as empty, so every entry is new."""
    r = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, text=True, cwd=cwd)
    if r.returncode != 0:
        return pronunciations.empty()
    try:
        return pronunciations.validate(json.loads(r.stdout))
    except json.JSONDecodeError as exc:
        if strict:
            raise pronunciations.PronunciationError(f"pronunciations.json is not valid JSON ({exc.msg})") from None
    except pronunciations.PronunciationError:
        if strict:
            raise
    return pronunciations.empty()


def voices(inbox: Path = INBOX, names: tuple = VOICES) -> list[dict]:
    """Each audition voice's pinned reference, from the batch JSONs that
    render it. Every batch naming a voice must pin the same reference."""
    refs: dict[str, set] = {v: set() for v in names}
    for p in sorted(inbox.glob("*.json")):
        try:
            b = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(b, dict) and b.get("voice") in refs:
            refs[b["voice"]].add((b.get("ref_path"), b.get("ref_sha256")))
    out = []
    for v in names:
        if len(refs[v]) != 1:
            raise AuditionError(f"{v}: expected one pinned reference in {inbox.name}/, found {len(refs[v])}")
        (ref_path, sha), = refs[v]
        if not (isinstance(ref_path, str) and re.fullmatch(r"lms/team/voice_refs/[A-Za-z0-9_]+\.wav", ref_path)
                and isinstance(sha, str) and re.fullmatch(r"[0-9a-f]{64}", sha)):
            raise AuditionError(f"{v}: bad ref_path or ref_sha256")
        out.append({"voice": v, "ref_path": ref_path, "ref_sha256": sha})
    return out


def plan(before: str, after: str, words_arg: str, cwd: str | Path | None = None) -> list[dict]:
    cwd = cwd or HERE.parent
    new = file_at(after, cwd=cwd, strict=True)
    names = parse_words(words_arg)
    if names:
        rows = requested(new, names)
    else:
        # No usable "before" (empty, all zeros, or not in this history after a
        # force push): diff against the previous commit.
        known = before and not re.fullmatch(r"0*", before) and subprocess.run(
            ["git", "cat-file", "-e", f"{before}^{{commit}}"], cwd=cwd, capture_output=True).returncode == 0
        rows = changed(file_at(before if known else f"{after}^", cwd=cwd), new)
    if len(rows) > MAX_CLIPS:
        raise AuditionError(f"{len(rows)} clips per voice; at most {MAX_CLIPS} per run "
                            "(run the workflow by hand with a words list)")
    return rows


# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------

class LightMeter:
    def __init__(self, ref: Path):
        from resemblyzer import VoiceEncoder, preprocess_wav
        self._pre = preprocess_wav
        self.enc = VoiceEncoder("cpu", verbose=False)
        self.R = self.enc.embed_utterance(preprocess_wav(self._r16(ref)))

    @staticmethod
    def _r16(p):
        import librosa
        import soundfile as sf
        w, sr = sf.read(str(p))
        w = w.mean(1) if w.ndim > 1 else w
        return librosa.resample(w, orig_sr=sr, target_sr=16000)

    def measure(self, p: Path) -> dict:
        import numpy as np
        import soundfile as sf
        x, sr = sf.read(str(p))
        x = x.mean(1) if x.ndim > 1 else x
        e = self.enc.embed_utterance(self._pre(self._r16(p)))
        sim = float(np.dot(e, self.R) / np.linalg.norm(e) / np.linalg.norm(self.R))
        m = {"duration_s": round(len(x) / sr, 3), "similarity": round(sim, 4),
             "rms_dbfs": round(float(20 * np.log10(max(float(np.sqrt(np.mean(x ** 2))), 1e-12))), 2)}
        m["tail_db"] = tail_db(x, sr)
        return m

    def passes(self, m: dict) -> bool:
        ok = MIN_S <= m["duration_s"] <= MAX_S and m["rms_dbfs"] > MIN_DBFS and m["similarity"] >= MIN_SIM
        return ok and tail_ok(m["tail_db"])


def render(args) -> int:
    import hashlib
    import mp3
    rows = json.loads(Path(args.words_json).read_text(encoding="utf-8"))
    agent, ref, work = Path(args.agent_root).resolve(), Path(args.ref).resolve(), Path(args.work).resolve()
    if hashlib.sha256(ref.read_bytes()).hexdigest() != args.ref_sha256:
        print("::error::reference sha256 does not match; refusing to render")
        return 1
    out_dir = agent / OUT_DIR / args.voice
    out_dir.mkdir(parents=True, exist_ok=True)
    work.mkdir(parents=True, exist_ok=True)
    scripts = agent / "lms/team/scripts"
    takes: dict[str, dict[int, dict]] = {r["clip"]: {} for r in rows}
    pending = [r for r in rows]
    meter = None
    for seed in SEEDS:
        if not pending:
            break
        jobs = [{"key": r["clip"], "text": speak_text(r["carrier"]), "seed": seed,
                 "out": str(work / f"{r['clip']}_seed{seed}.wav")} for r in pending]
        (work / "jobs.json").write_text(json.dumps(jobs, ensure_ascii=False), encoding="utf-8")
        print(f"::group::{args.voice}: seed {seed}, {len(jobs)} clip(s)", flush=True)
        subprocess.run([sys.executable, str(HERE / "render_takes.py"), "--jobs", str(work / "jobs.json"),
                        "--ref", str(ref), "--scripts-dir", str(scripts), "--model-path", args.model_path],
                       check=False)
        print("::endgroup::", flush=True)
        meter = meter or LightMeter(ref)
        still = []
        for r, j in zip(pending, jobs):
            if not Path(j["out"]).exists():
                still.append(r)
                continue
            m = meter.measure(Path(j["out"]))
            m["passed"] = meter.passes(m)
            takes[r["clip"]][seed] = {**m, "wav": j["out"]}
            print(f"{r['clip']} seed{seed}: {m}", flush=True)
            if not m["passed"]:
                still.append(r)
        pending = still

    index_path = out_dir / "audition.json"
    index = json.loads(index_path.read_text(encoding="utf-8")) if index_path.exists() else {}
    index.update({"voice": args.voice, "reference": {"sha256": args.ref_sha256},
                  "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
    clips = index.setdefault("clips", {})
    lines = [f"### Pronunciation audition `{args.voice}`", "",
             f"Agent branch `{BRANCH}`", "",
             "| word | respelling | file | QC |", "|---|---|---|---|"]
    failed = 0
    for r in rows:
        t = takes[r["clip"]]
        if not t:
            failed += 1
            lines.append(f"| {r['word']} | {r['respelling']} | (render failed) | n/a |")
            continue
        seed, best = min(t.items(), key=lambda kv: (not kv[1]["passed"], -kv[1]["similarity"]))
        rel = f"{OUT_DIR}/{args.voice}/{r['clip']}.mp3"
        encoder = mp3.encode(best["wav"], agent / rel)
        clips[r["clip"]] = {
            "word": r["word"], "respelling": r["respelling"], "kind": r["kind"], "carrier": r["carrier"],
            "file": rel, "seed": seed, "seeds_tried": sorted(t), "encoder": encoder,
            **{k: v for k, v in best.items() if k != "wav"},
            **({"ci_run_id": os.environ["GITHUB_RUN_ID"]} if os.environ.get("GITHUB_RUN_ID") else {}),
        }
        qc = "pass" if best["passed"] else "weak (listen closely)"
        lines.append(f"| {r['word']} | {r['respelling']} | `{rel}` | {qc} |")
    index["clips"] = dict(sorted(clips.items()))
    index_path.write_text(json.dumps(index, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    if args.summary:
        with open(args.summary, "a", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
    print(f"{args.voice}: {len(rows) - failed}/{len(rows)} clip(s) written")
    return 0 if failed < len(rows) else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan")
    p.add_argument("--before", default="")
    p.add_argument("--after", default="HEAD")
    p.add_argument("--words", default="")
    r = sub.add_parser("render")
    for a in ("--agent-root", "--voice", "--ref", "--ref-sha256", "--model-path", "--work", "--words-json"):
        r.add_argument(a, required=True)
    r.add_argument("--summary", default="")
    args = ap.parse_args(argv)
    if args.cmd == "render":
        return render(args)
    try:
        rows = plan(args.before, args.after, args.words)
        vs = voices() if rows else []
    except (AuditionError, pronunciations.PronunciationError) as exc:
        print(f"::error::{exc}", file=sys.stderr)
        return 1
    print(f"count={len(rows)}")
    print("words_json=" + json.dumps(rows, ensure_ascii=False))
    print("voices_json=" + json.dumps(vs))
    print(f"branch={BRANCH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
