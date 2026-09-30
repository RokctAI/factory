#!/usr/bin/env python3
"""Record one engine's regression-baseline render as a manifest fragment.

    record.py run      --engine E --step NAME [--cwd DIR] [--no-tail] -- CMD ARGS...
    record.py finalize --engine E --out DIR [--source NAME=CHECKOUT ...]
                       [--input NAME=FILE ...] [--fixture KEY=VALUE ...]
                       [--withhold GLOB ...] [--f0 GLOB ...] [--note TEXT ...]
    record.py skip     --engine E --reason TEXT [--fixture KEY=VALUE ...]

`run` executes one step of the old engine, streams its output, and appends
the command, exit code and wall time to the fragment. `finalize` lists every
file the engine wrote under --out with its sha256, size and cheap media
metrics (ffprobe: duration, streams, frame count; ffmpeg ebur128:
integrated loudness and true peak; librosa pyin median F0 when asked and
installed), then sets the engine status: baselined when every step exited 0
and at least one file was written, failed otherwise. `skip` records an
engine that could not be baselined, with the reason.

Files matching --withhold are measured and hashed, then moved out of the
upload folder: this repository is public, so its Actions artifacts are
public too, and cloned-voice audio never goes into them. When the optional
secret BASELINE_ARTIFACT_KEY is set, the withheld files are uploaded as one
AES-256 encrypted tarball instead (openssl enc -aes-256-cbc -pbkdf2).

Fragments are written to $BASELINE_FRAGMENTS (default baseline_fragments/)
as <engine>.json; merge.py folds them into baseline_manifest.json.
"""
from __future__ import annotations

import argparse
import collections
import fnmatch
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

FRAG_DIR = Path(os.environ.get("BASELINE_FRAGMENTS", "baseline_fragments"))
AUDIO_EXT = {".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg", ".opus"}
VIDEO_EXT = {".mp4", ".mov", ".webm", ".mkv"}
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp"}
# Environment names the posting code reads. None may be present in a
# baseline job: their absence is part of the proof that nothing can post.
POSTING_ENV = re.compile(r"^(FACEBOOK_|TIKTOK_|YOUTUBE_|GRAPH_|META_)")


def now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def frag_path(engine: str) -> Path:
    return FRAG_DIR / f"{engine}.json"


def load(engine: str) -> dict:
    p = frag_path(engine)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {"engine": engine, "status": "pending", "steps": [], "outputs": [], "notes": []}


def save(frag: dict) -> None:
    FRAG_DIR.mkdir(parents=True, exist_ok=True)
    frag_path(frag["engine"]).write_text(json.dumps(frag, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def kv(pairs: list[str] | None) -> dict:
    out = {}
    for p in pairs or []:
        k, _, v = p.partition("=")
        out[k] = v
    return out


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def posting_env_present() -> list[str]:
    return sorted(k for k in os.environ if POSTING_ENV.match(k))


# ------------------------------------------------------------------ steps


def cmd_run(a) -> int:
    frag = load(a.engine)
    bad = posting_env_present()
    if bad:
        frag["steps"].append({"name": a.step, "command": a.cmd, "exit_code": 97, "duration_s": 0,
                              "error": f"posting credentials present in the environment: {bad}"})
        save(frag)
        print(f"::error::refusing to run: posting credentials present in the environment ({bad})")
        return 97
    tail: collections.deque = collections.deque(maxlen=15)
    started = time.time()
    print(f"::group::{a.engine} / {a.step}: {' '.join(a.cmd)}", flush=True)
    try:
        proc = subprocess.Popen(a.cmd, cwd=a.cwd or None, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                text=True, errors="replace", bufsize=1)
        for line in proc.stdout:
            sys.stdout.write(line)
            tail.append(line.rstrip("\n"))
        rc = proc.wait()
    except OSError as exc:
        rc, tail = 127, collections.deque([str(exc)])
    print("::endgroup::", flush=True)
    step = {"name": a.step, "command": a.cmd, "cwd": a.cwd or ".", "started_at": time.strftime(
        "%Y-%m-%dT%H:%M:%SZ", time.gmtime(started)), "exit_code": rc, "duration_s": round(time.time() - started, 1)}
    if rc != 0:
        step["error"] = ("see the job log (output not copied: private inputs)" if a.no_tail
                         else "\n".join(tail))
    frag["steps"].append(step)
    save(frag)
    return rc


# ---------------------------------------------------------------- metrics


def run_json(cmd: list[str]) -> dict:
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        return json.loads(r.stdout or "{}")
    except (OSError, ValueError, subprocess.TimeoutExpired):
        return {}


def probe(p: Path) -> dict:
    ext = p.suffix.lower()
    if ext not in AUDIO_EXT | VIDEO_EXT | IMAGE_EXT:
        return {}
    extra = ["-count_packets"] if ext in VIDEO_EXT else []
    d = run_json(["ffprobe", "-v", "error", *extra, "-show_entries",
                  "format=duration,format_name:stream=codec_type,codec_name,width,height,r_frame_rate,"
                  "nb_frames,nb_read_packets,sample_rate,channels,sample_fmt,bits_per_sample,pix_fmt",
                  "-of", "json", str(p)])
    if not d:
        return {"probe": "ffprobe unavailable or failed"}
    m: dict = {}
    dur = (d.get("format") or {}).get("duration")
    if dur and ext not in IMAGE_EXT:
        m["duration_s"] = round(float(dur), 4)
    for s in d.get("streams", []):
        t = s.get("codec_type")
        if t == "video":
            if ext in IMAGE_EXT:
                m.update(width=s.get("width"), height=s.get("height"), codec=s.get("codec_name"))
            else:
                num, _, den = (s.get("r_frame_rate") or "0/1").partition("/")
                fps = float(num) / float(den or 1) if float(den or 1) else 0.0
                frames = s.get("nb_read_packets") or s.get("nb_frames")
                m["video"] = {"codec": s.get("codec_name"), "width": s.get("width"), "height": s.get("height"),
                              "fps": round(fps, 3), "frames": int(frames) if frames else None,
                              "pix_fmt": s.get("pix_fmt")}
        elif t == "audio":
            m["audio"] = {"codec": s.get("codec_name"), "sample_rate": int(s.get("sample_rate") or 0),
                          "channels": s.get("channels"), "sample_fmt": s.get("sample_fmt")}
    if ext in VIDEO_EXT and "audio" not in m:
        m["audio"] = None  # no audio stream at all (a silent render)
    return m


def loudness(p: Path) -> dict:
    try:
        r = subprocess.run(["ffmpeg", "-nostats", "-hide_banner", "-i", str(p), "-map", "0:a:0",
                            "-filter_complex", "ebur128=peak=true", "-f", "null", "-"],
                           capture_output=True, text=True, timeout=600)
    except (OSError, subprocess.TimeoutExpired):
        return {}
    summary = r.stderr.rpartition("Summary:")[2]
    out = {}
    m = re.search(r"I:\s*(-?[\d.]+|-inf)\s*LUFS", summary)
    if m:
        out["integrated_lufs"] = None if m.group(1) == "-inf" else float(m.group(1))
    m = re.search(r"True peak:\s*Peak:\s*(-?[\d.]+|-inf)\s*dBFS", summary, re.S)
    if m:
        out["true_peak_dbtp"] = None if m.group(1) == "-inf" else float(m.group(1))
    m = re.search(r"LRA:\s*(-?[\d.]+)\s*LU", summary)
    if m:
        out["lra_lu"] = float(m.group(1))
    return out


def median_f0(p: Path) -> dict:
    try:
        import librosa
        import numpy as np
    except ImportError:
        return {"median_f0_hz": None, "f0_note": "librosa not installed in this job"}
    try:
        y, sr = librosa.load(str(p), sr=16000, mono=True)
        f0, voiced, _ = librosa.pyin(y, fmin=50, fmax=400, sr=sr)
        v = f0[voiced & ~np.isnan(f0)]
        return {"median_f0_hz": round(float(np.median(v)), 2) if v.size else None,
                "voiced_fraction": round(float(voiced.mean()), 3) if voiced.size else None}
    except Exception as exc:  # measurement only; never fail the record
        return {"median_f0_hz": None, "f0_note": f"pyin failed: {exc}"}


def measure(p: Path, f0: bool) -> dict:
    m = probe(p)
    has_audio = p.suffix.lower() in AUDIO_EXT or bool(m.get("audio"))
    if has_audio:
        m.update(loudness(p))
        if f0:
            m.update(median_f0(p))
    return m


def source_info(name: str, path: str) -> dict:
    info = {"name": name, "path": path}
    try:
        info["sha"] = subprocess.run(["git", "-C", path, "rev-parse", "HEAD"], capture_output=True,
                                     text=True, check=True).stdout.strip()
        url = subprocess.run(["git", "-C", path, "remote", "get-url", "origin"], capture_output=True,
                             text=True).stdout.strip()
        m = re.search(r"github\.com[/:]([^/]+/[^/.]+)", url)
        info["repo"] = m.group(1) if m else url
        # No credentials may be left in the checkout: without them nothing
        # here can push, whatever token the checkout step used.
        cfg = subprocess.run(["git", "-C", path, "config", "--get-regexp", r"^http\..*\.extraheader$"],
                             capture_output=True, text=True).stdout.strip()
        info["credentials_in_git_config"] = bool(cfg)
    except (OSError, subprocess.CalledProcessError) as exc:
        info["error"] = str(exc)
    return info


def tool_versions(pkgs: list[str]) -> dict:
    from importlib import metadata
    out = {"python": sys.version.split()[0]}
    for pkg in pkgs:
        try:
            out[pkg] = metadata.version(pkg)
        except metadata.PackageNotFoundError:
            out[pkg] = None
    try:
        first = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True).stdout.splitlines()
        out["ffmpeg"] = first[0] if first else None
    except OSError:
        out["ffmpeg"] = None
    return out


def cmd_finalize(a) -> int:
    frag = load(a.engine)
    out = Path(a.out)
    frag["fixture"] = {**frag.get("fixture", {}), **kv(a.fixture)}
    frag["sources"] = [source_info(n, p) for n, p in kv(a.source).items()]
    frag["inputs"] = [{"name": n, "path": p, "sha256": sha256(Path(p)) if Path(p).is_file() else None}
                      for n, p in kv(a.input).items()]
    frag["notes"] = list(dict.fromkeys(frag.get("notes", []) + (a.note or [])))
    withheld_dir = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "baseline_withheld" / a.engine
    outputs = []
    files = sorted(p for p in out.rglob("*") if p.is_file()) if out.is_dir() else []
    for p in files:
        rel = p.relative_to(out).as_posix()
        withhold = any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(p.name, g) for g in a.withhold or [])
        f0 = any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(p.name, g) for g in a.f0 or [])
        row = {"path": rel, "sha256": sha256(p), "bytes": p.stat().st_size, "uploaded": not withhold,
               "metrics": measure(p, f0)}
        if withhold:
            dst = withheld_dir / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(p), dst)
        outputs.append(row)
    frag["outputs"] = outputs
    if any(not o["uploaded"] for o in outputs):
        key = os.environ.get("BASELINE_ARTIFACT_KEY", "")
        if key:
            enc = out / "withheld.tar.gz.enc"
            tar = subprocess.run(["tar", "czf", "-", "-C", str(withheld_dir), "."], capture_output=True, check=True)
            subprocess.run(["openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-salt", "-pass", "env:BASELINE_ARTIFACT_KEY",
                            "-out", str(enc)], input=tar.stdout, check=True)
            frag["withheld"] = {"policy": "cloned-voice audio is not uploaded in the clear (public repo)",
                                "encrypted_tarball": enc.name, "sha256": sha256(enc)}
        else:
            frag["withheld"] = {"policy": "cloned-voice audio is not uploaded (public repo artifacts are public); "
                                          "sha256 and metrics above are the baseline, renders are deterministic"}
    steps = frag.get("steps", [])
    frag["duration_s"] = round(sum(s.get("duration_s", 0) for s in steps), 1)
    if not steps and frag.get("status") == "not_baselined":
        pass  # recorded by `skip` before anything could run; keep its reason
    elif not steps:
        frag["status"], frag["error"] = "failed", "no render step ran (see the job log)"
    elif any(s.get("exit_code") for s in steps):
        bad = next(s for s in steps if s.get("exit_code"))
        frag["status"] = "failed"
        frag["error"] = f"step '{bad['name']}' exited {bad['exit_code']}: {bad.get('error', '')}".strip()
    elif not outputs:
        frag["status"], frag["error"] = "failed", "every step exited 0 but the engine wrote no file"
    else:
        frag["status"] = "baselined"
        frag.pop("error", None)
    if a.status_override:
        frag["status"], frag["reason"] = a.status_override, a.reason
    frag["tools"] = tool_versions(a.pkg or [])
    frag["posting_env_present"] = posting_env_present()
    frag["recorded_at"] = now()
    save(frag)
    print(f"{a.engine}: {frag['status']} ({len(outputs)} file(s), {sum(not o['uploaded'] for o in outputs)} withheld)")
    return 0


def cmd_skip(a) -> int:
    frag = load(a.engine)
    frag.update(status="not_baselined", reason=a.reason, recorded_at=now())
    frag["fixture"] = {**frag.get("fixture", {}), **kv(a.fixture)}
    frag["inputs"] = frag.get("inputs", []) + [
        {"name": n, "path": p, "sha256": sha256(Path(p)) if Path(p).is_file() else None,
         "metrics": measure(Path(p), False) if Path(p).is_file() else {}}
        for n, p in kv(a.input).items()]
    frag["sources"] = [source_info(n, p) for n, p in kv(a.source).items()]
    save(frag)
    print(f"{a.engine}: not baselined - {a.reason}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--engine", required=True)
    r.add_argument("--step", required=True)
    r.add_argument("--cwd")
    r.add_argument("--no-tail", action="store_true", help="never copy output lines into the fragment")
    r.add_argument("command", nargs=argparse.REMAINDER)
    f = sub.add_parser("finalize")
    f.add_argument("--engine", required=True)
    f.add_argument("--out", required=True)
    f.add_argument("--source", action="append")
    f.add_argument("--input", action="append")
    f.add_argument("--fixture", action="append")
    f.add_argument("--withhold", action="append")
    f.add_argument("--f0", action="append")
    f.add_argument("--note", action="append")
    f.add_argument("--pkg", action="append", help="Python distribution whose version to record")
    f.add_argument("--status-override", choices=["not_baselined"])
    f.add_argument("--reason")
    s = sub.add_parser("skip")
    s.add_argument("--engine", required=True)
    s.add_argument("--reason", required=True)
    s.add_argument("--fixture", action="append")
    s.add_argument("--input", action="append")
    s.add_argument("--source", action="append")
    a = ap.parse_args()
    if a.cmd == "run":
        a.cmd = a.command[1:] if a.command[:1] == ["--"] else a.command
        if not a.cmd:
            ap.error("run needs a command after --")
        return cmd_run(a)
    return cmd_finalize(a) if a.cmd == "finalize" else cmd_skip(a)


if __name__ == "__main__":
    sys.exit(main())
