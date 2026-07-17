#!/usr/bin/env python3
"""Level 6 manifest assembler — turns an `evaluated` lesson card into the
finished ReplaySDK asset triple the app downloads: manifest.json, audio.mp3,
animations.json.

This is step 4-7 of supacharge-tech.md §4's production pipeline:
  4. run Manim -> animation JSON      (manim_exporter.py)
  5. VibeVoice generates tutor audio  (audio backend, below)
  6. ManimExporter outputs primitives (manim_exporter.py)
  7. timestamps aligned, manifest assembled

The manifest shape is NOT invented here — it is exactly what
agent/replay/dart .../models/data/manifest.dart `ReplayManifest.fromJson`
parses (version, session_id, subject, grade, topic, lesson_number,
door_close_seconds, scheduled_at, audio{lesson,format,duration_seconds},
assets[], tracks[{time,type,...}]). Track event types (profile,
subtopic_start, subtopic_end, stretch_break, signoff) are the vocabulary in
supacharge-product.md's manifest sample and replay AudioSync's doc comment.

Audio backend (--audio-backend):
  vibevoice : real VibeVoice-1.5B TTS. Requires a CUDA GPU — see the Level 6
              feasibility note; standard GH runners have none, so this runs
              on a GPU runner / on-demand GPU, not ubuntu-latest.
  sapi      : offline OS TTS (pyttsx3 / SAPI5 on Windows, espeak elsewhere)
              used to prove the assembly loop end to end WITHOUT a GPU. The
              audio is a real, playable, correctly-measured file; only the
              voice model differs from production. Clearly flagged in the
              manifest via audio.engine.

Timestamp alignment: subtopics.json describes the INTENDED lesson timeline
(e.g. 900s). The manifest must describe the REAL audio, so subtopic
boundaries and animation-primitive times are scaled by
real_audio_duration / intended_duration. In production VibeVoice reads the
full 15-minute script and the factor is ~1; for the SAPI proof it compresses
to the real (shorter) synthesized length so playback stays coherent.
"""
import argparse
import json
import re
import subprocess
import sys
import wave
from datetime import datetime, timezone
from pathlib import Path

DOOR_CLOSE_SECONDS = 300  # supacharge-product.md late-door policy
PASS_THRESHOLD = 0.80     # per subtopic_end in the product-doc manifest sample
QA_WINDOW_SECONDS = 120


def get_field(content, field):
    m = re.search(rf"^{field}:[ \t]*(.*)", content, re.MULTILINE)
    return m.group(1).split("#")[0].strip() if m else ""


def strip_script_to_narration(script_md):
    """Plain spoken text from script.md: drop headings, bullets, markdown
    emphasis and stage directions in [brackets]/(parens)."""
    lines = []
    for line in script_md.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith(">"):
            continue
        s = re.sub(r"[*_`]", "", s)
        s = re.sub(r"^\-\s*", "", s)
        s = re.sub(r"\[[^\]]*\]", "", s)   # [visual: ...] stage directions
        s = s.strip()
        if s:
            lines.append(s)
    return " ".join(lines)


def synth_audio_sapi(text, out_wav):
    """Offline OS TTS -> wav. Real audio, no GPU.

    Windows: pyttsx3 over SAPI5. Linux (CI): the espeak/espeak-ng CLI
    directly — pyttsx3's espeak driver crashes on hosted runners
    (SetVoiceByName fails for voice 'gmw/en', a pyttsx3/espeak-ng
    mismatch; seen on the first real Level 6 run, 29544575572)."""
    import platform
    import shutil
    if platform.system() != "Windows":
        exe = shutil.which("espeak-ng") or shutil.which("espeak")
        if not exe:
            raise SystemExit("no espeak/espeak-ng CLI on PATH (apt-get install espeak)")
        text_file = Path(str(out_wav) + ".txt")
        text_file.write_text(text, encoding="utf-8")
        subprocess.run([exe, "-v", "en", "-s", "150",
                        "-w", str(out_wav), "-f", str(text_file)], check=True)
        text_file.unlink()
    else:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty("rate", 165)
        engine.save_to_file(text, str(out_wav))
        engine.runAndWait()
    if not Path(out_wav).exists() or Path(out_wav).stat().st_size == 0:
        raise SystemExit("OS TTS synthesis produced no audio")


def synth_audio_vibevoice(text, out_wav, voice_preset):
    """Real VibeVoice-1.5B synthesis (GPU). Imported lazily so the assembler
    still runs in SAPI mode on a machine without torch/CUDA/VibeVoice."""
    from vibevoice.inference import synthesize  # provided on the GPU runner
    synthesize(text=text, speaker=voice_preset, output_path=str(out_wav),
               sample_rate=24000)
    if not Path(out_wav).exists() or Path(out_wav).stat().st_size == 0:
        raise SystemExit("VibeVoice synthesis produced no audio")


def wav_duration_seconds(wav_path):
    with wave.open(str(wav_path), "rb") as w:
        return w.getnframes() / float(w.getframerate())


def to_mp3(wav_path, mp3_path):
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav_path),
         "-codec:a", "libmp3lame", "-qscale:a", "4", str(mp3_path)],
        check=True,
    )


def build_tracks(subtopics, mcq, tutor_label, scale, audio_seconds):
    """Manifest track events from subtopics.json, scaled to real audio.
    profile at 0, subtopic_start/subtopic_end per subtopic (end carries the
    subtopic's MCQ ids as `exercise`), signoff last. All times clamped to the
    audio length so no event lands past the declared audio duration."""
    tutor_slug = tutor_label.split("—")[0].strip().lower().replace(" ", "_")
    mcq_by_ref = {b["ref"]: [q["id"] for q in b.get("questions", [])]
                  for b in mcq.get("subtopics", [])}
    cap = float(int(round(audio_seconds)))  # matches manifest audio duration

    tracks = [{"time": 0, "type": "profile", "tutor": tutor_slug,
               "audio": "audio.mp3"}]
    last_end = 0.0
    for sub in subtopics.get("subtopics", []):
        start = round(min(sub["start_seconds"] * scale, cap), 2)
        end = round(min(sub["end_seconds"] * scale, cap), 2)
        last_end = end
        tracks.append({"time": start, "type": "subtopic_start",
                       "ref": sub["ref"], "title": sub.get("title", "")})
        tracks.append({"time": end, "type": "subtopic_end",
                       "ref": sub["ref"], "qa_window": QA_WINDOW_SECONDS,
                       "exercise": mcq_by_ref.get(sub["ref"], []),
                       "pass_threshold": PASS_THRESHOLD})
    tracks.append({"time": round(last_end, 2), "type": "signoff",
                   "tutor": tutor_slug, "audio": "audio.mp3"})
    tracks.sort(key=lambda t: t["time"])
    return tracks


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--card", required=True, help="evaluated job card path")
    ap.add_argument("--out-dir", required=True, help="asset output directory")
    ap.add_argument("--audio-backend", choices=["vibevoice", "sapi"],
                    default="sapi")
    ap.add_argument("--lesson-number", type=int, default=1)
    ap.add_argument("--max-narration-chars", type=int, default=0,
                    help="truncate narration (proof runs); 0 = full script")
    args = ap.parse_args()

    repo = Path.cwd()
    card = Path(args.card).read_text(encoding="utf-8")
    card_id = get_field(card, "id")
    subject = get_field(card, "subject")
    grade = int(get_field(card, "grade") or 0)
    topic = get_field(card, "topic")
    tutor = get_field(card, "tutor") or "Grandmaster — formal"
    lesson_path = repo / get_field(card, "lesson_path")

    subtopics = json.loads((lesson_path / "subtopics.json").read_text("utf-8"))
    mcq_file = lesson_path / "mcq.json"
    mcq = json.loads(mcq_file.read_text("utf-8")) if mcq_file.exists() else {}
    script_md = (lesson_path / "script.md").read_text("utf-8")

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # --- 5/6. audio ---
    narration = strip_script_to_narration(script_md)
    if args.max_narration_chars and len(narration) > args.max_narration_chars:
        narration = narration[:args.max_narration_chars]
    wav_path = out_dir / "audio.wav"
    print(f"[audio] backend={args.audio_backend} chars={len(narration)}")
    if args.audio_backend == "vibevoice":
        # Voice preset comes from the tutor persona card (documented intent
        # today; Level 6 maps it to a real VibeVoice speaker embedding).
        synth_audio_vibevoice(narration, wav_path, voice_preset=tutor)
    else:
        synth_audio_sapi(narration, wav_path)
    audio_seconds = wav_duration_seconds(wav_path)
    mp3_path = out_dir / "audio.mp3"
    to_mp3(wav_path, mp3_path)
    wav_path.unlink()
    print(f"[audio] {audio_seconds:.1f}s -> {mp3_path.name}")

    # --- 4. animation primitives ---
    sys.path.insert(0, str(repo / "lessons" / "scripts"))
    from manim_exporter import export_scene
    anim_path = out_dir / "animations.json"
    anim = export_scene(str(lesson_path / "manim_scene.py"), str(anim_path))
    manim_duration = anim["duration_seconds"] or 1.0

    # --- 7. align timestamps to the real audio ---
    intended = subtopics["subtopics"][-1]["end_seconds"] if subtopics["subtopics"] else audio_seconds
    subtopic_scale = audio_seconds / intended if intended else 1.0
    anim_scale = audio_seconds / manim_duration
    for p in anim["primitives"]:
        p["time"] = round(p["time"] * anim_scale, 2)
    anim["duration_seconds"] = round(audio_seconds, 2)
    anim_path.write_text(json.dumps(anim, indent=2), encoding="utf-8")
    print(f"[align] subtopic x{subtopic_scale:.3f}  animation x{anim_scale:.3f}")

    tracks = build_tracks(subtopics, mcq, tutor, subtopic_scale, audio_seconds)

    # --- manifest (ReplayManifest.fromJson contract) ---
    manifest = {
        "version": "1",
        "session_id": card_id,
        "subject": subject,
        "grade": grade,
        "topic": topic,
        "lesson_number": args.lesson_number,
        "door_close_seconds": DOOR_CLOSE_SECONDS,
        # Real scheduler overwrites this when the lesson is calendared
        # (production step 9); a valid ISO stamp is required by fromJson.
        "scheduled_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "audio": {
            "lesson": "audio.mp3",
            "format": "mp3",
            "duration_seconds": int(round(audio_seconds)),
            "engine": args.audio_backend,  # provenance; ignored by parser
        },
        "assets": ["animations.json"],
        "tracks": tracks,
    }
    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"[manifest] {len(tracks)} tracks -> {manifest_path}")
    print(json.dumps({"session_id": card_id, "audio_seconds": round(audio_seconds, 1),
                      "tracks": len(tracks), "primitives": len(anim["primitives"])}))


if __name__ == "__main__":
    main()
