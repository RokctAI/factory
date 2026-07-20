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
    emphasis, stage directions in [brackets], and any session-framing lines
    (self-intros, platform mentions, host references, goodbyes) that slipped
    into legacy scripts — the player supplies all framing, so produced audio
    must never carry it. Question lead-ins at MCQ subtopic ends are teaching
    flow and stay in (the framing signatures cannot match them)."""
    sys.path.insert(0, str(Path(__file__).parent))
    from lesson_pipeline import verify_no_session_framing
    lines = []
    for line in script_md.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith(">"):
            continue
        if verify_no_session_framing(s):
            continue  # framing line — never reaches the audio
        s = re.sub(r"[*_`]", "", s)
        s = re.sub(r"^\-\s*", "", s)
        s = re.sub(r"\[[^\]]*\]", "", s)   # [visual: ...] stage directions
        s = s.strip()
        if s:
            lines.append(s)
    return " ".join(lines)


def split_script_into_segments(script_md):
    """[(subtopic_index, narration)] — the script split at its
    '## Subtopic: <title>' headings, each block reduced to spoken narration.

    Per-subtopic granularity is deliberate (model (B) production):
      * each segment is synthesized separately, so its duration is MEASURED
        rather than estimated — subtopic boundaries become the exact sum of
        real segment lengths instead of one global proportional stretch;
      * it is the only granularity at which a single corrected subtopic can
        be re-synthesized without redoing the whole lesson's audio;
      * a two-part lesson can synthesize each speaker's own subtopics in
        that speaker's voice.
    Any narration appearing before the first heading is attached to
    segment 0 so nothing is silently dropped.
    """
    blocks, current = [], []
    for line in script_md.splitlines():
        if re.match(r"^\s*##\s*Subtopic\s*:", line, re.IGNORECASE):
            blocks.append(current)
            current = []
        current.append(line)
    blocks.append(current)
    # blocks[0] is any preamble before the first heading
    preamble, *subtopic_blocks = blocks
    segments = []
    if not subtopic_blocks:
        text = strip_script_to_narration("\n".join(preamble))
        return [(0, text)] if text else []
    lead = strip_script_to_narration("\n".join(preamble))
    for i, block in enumerate(subtopic_blocks):
        text = strip_script_to_narration("\n".join(block))
        if i == 0 and lead:
            text = (lead + " " + text).strip()
        if text:
            segments.append((i, text))
    return segments


def concat_wavs(parts, out_wav):
    """Concatenate segment wavs into one track, server-side.

    Client-side gapless playback is NOT achievable on the current stack
    (measured: audioplayers has no queue/gapless API; a segment join leaves
    ~100-150ms of audible silence), so the segments are joined here and the
    lesson ships ONE audio file. Done on raw PCM frames — no re-encode, so
    concatenation is lossless and sample-exact; only the final wav->mp3 step
    encodes, exactly once."""
    with wave.open(str(parts[0]), "rb") as first:
        params = first.getparams()
    with wave.open(str(out_wav), "wb") as out:
        out.setparams(params)
        for p in parts:
            with wave.open(str(p), "rb") as w:
                if w.getparams()[:3] != params[:3]:
                    raise SystemExit(
                        f"segment {p} has mismatched audio params "
                        f"{w.getparams()[:3]} vs {params[:3]}")
                out.writeframes(w.readframes(w.getnframes()))


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


def _ffmpeg_exe():
    """Resolve an ffmpeg binary: PATH first (CI installs it via apt), else
    the one bundled with imageio-ffmpeg if that package is present."""
    import shutil
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        raise SystemExit("ffmpeg not found on PATH and imageio-ffmpeg is not "
                         "installed (pip install imageio-ffmpeg)")


def to_mp3(wav_path, mp3_path):
    subprocess.run(
        [_ffmpeg_exe(), "-y", "-loglevel", "error", "-i", str(wav_path),
         "-codec:a", "libmp3lame", "-qscale:a", "4", str(mp3_path)],
        check=True,
    )


BREAK_DURATION_SECONDS = 300  # replaysdk-spec break_start sample


SECOND_TUTOR_FIELD = "second_tutor_from_subtopic"


def two_part_split(card_text, subtopics):
    """The subtopic ref at which the SECOND tutor takes over, or None for a
    single-voice lesson.

    A lesson is two-part only when its card says so — `second_tutor_from_subtopic:
    subtopic_N`. This is the gate for `second_tutor` and `break_start`: a
    lesson must never announce a tutor who never speaks (single-voice audio
    with a break_start told the client to announce Big John over the
    Grandmaster recording). The field is written by the two-block generation
    path; every legacy/single-voice card simply lacks it."""
    ref = get_field(card_text, SECOND_TUTOR_FIELD)
    if not ref:
        return None
    refs = [s.get("ref") for s in subtopics.get("subtopics", [])]
    if ref not in refs:
        print(f"[warn] {SECOND_TUTOR_FIELD}={ref!r} is not a subtopic ref {refs}; "
              "treating lesson as single-voice")
        return None
    if refs.index(ref) == 0:
        print(f"[warn] {SECOND_TUTOR_FIELD}={ref!r} is the FIRST subtopic — the "
              "lead tutor would never speak; treating lesson as single-voice")
        return None
    return ref


def resolve_tutor_pair(card_text, tutor_label):
    """(first, second) tutor identity dicts for the manifest, derived from
    the tutor roster's paired-duo mapping — roster.json already captures the
    two-tutor-per-lesson design (every subject has an Expert + Simplifier
    duo), so the second tutor needs NO new job-card field: it is simply the
    other member of the card subject's duo. Returns (first, None) when the
    roster cannot resolve a pair (legacy label, missing roster).

    NOTE: resolving a pair does NOT mean the lesson is two-part — see
    two_part_split(); the caller drops `second` for single-voice lessons."""
    sys.path.insert(0, str(Path(__file__).parent))
    from lesson_pipeline import (card_roster_key, load_roster, load_tutor_card,
                                 persona_label)

    def identity(slug):
        text = load_tutor_card(slug)
        label = persona_label(text) if text else slug
        name = label.split("—")[0].strip() if label else slug
        real = get_field(text, "real_name") if text else ""
        return {"id": slug, "display_name": name,
                **({"real_name": real} if real else {})}

    fallback = {"id": tutor_label.split("—")[0].strip().lower().replace(" ", "_"),
                "display_name": tutor_label.split("—")[0].strip()}
    duo = load_roster().get("subjects", {}).get(card_roster_key(card_text), {})
    slugs = [duo.get("expert", ""), duo.get("simplifier", "")]
    if not all(slugs):
        return fallback, None
    name_part = tutor_label.split("—")[0].strip().lower()
    first_slug = next(
        (s for s in slugs
         if persona_label(load_tutor_card(s)).split("—")[0].strip().lower() in name_part
         or name_part in persona_label(load_tutor_card(s)).split("—")[0].strip().lower()),
        None)
    if first_slug is None:
        return fallback, None
    second_slug = slugs[1] if first_slug == slugs[0] else slugs[0]
    return identity(first_slug), identity(second_slug)


MAX_BREAK_QUESTIONS = 4  # client caps at 4 so a break stays a break


def extract_break_questions(transcript_md, limit=MAX_BREAK_QUESTIONS):
    """Student questions from mandy_qa_transcript.md, for the break board.

    Emitted INLINE on break_start (not into a bank): the client's
    BreakQuestion model has no id field, and these are single-use display
    prompts rather than scored items. Only the question is carried — the
    board shows it while Mandy speaks the answer from the audio, so
    ask/answer seconds stay at the client's defaults unless the bridge audio
    gives us real ones."""
    questions = []
    for line in transcript_md.splitlines():
        m = re.match(r"^\*\*Student:\*\*\s*(.+?)\s*$", line.strip())
        if m:
            text = re.sub(r"[*_`]", "", m.group(1)).strip()
            if text:
                questions.append({"question": text})
        if len(questions) >= limit:
            break
    return questions


def build_tracks(subtopics, mcq, comprehension, first_tutor, second_tutor,
                 scale, audio_seconds, topic, topic_display_seconds,
                 split_ref=None, break_questions=None, segment_bounds=None):
    """Manifest track events from subtopics.json, scaled to real audio.

    topic_display at 0 (full-screen topic while the tutor speaks the intro —
    duration computed from when board work actually starts, see main()),
    profile at 0, subtopic_start/subtopic_end per subtopic (end carries the
    subtopic's MCQ ids as `exercise`), a break_start at the subtopic
    boundary nearest the audio midpoint (the bridge between the two tutors'
    parts — Mandy bridges, then the second tutor takes over; the duo comes
    from roster.json), then — when the lesson ships a comprehension check —
    a comprehension_check event at lesson end, signoff last. All times
    clamped to the audio length."""
    mcq_by_ref = {b["ref"]: [q["id"] for q in b.get("questions", [])]
                  for b in mcq.get("subtopics", [])}
    cap = float(int(round(audio_seconds)))  # matches manifest audio duration

    tracks = [
        {"time": 0, "type": "topic_display", "topic": topic,
         "duration_seconds": round(topic_display_seconds, 2)},
        {"time": 0, "type": "profile", "tutor": first_tutor["id"],
         "audio": "audio.mp3"},
    ]
    subs = subtopics.get("subtopics", [])
    # The bridge sits exactly where the card says the second tutor takes
    # over: the END of the subtopic immediately before `split_ref`. It is
    # never guessed from the midpoint — the handover is a content fact, and
    # the break must line up with the actual voice change in the audio.
    break_after_ref = None
    if second_tutor and split_ref:
        refs = [s.get("ref") for s in subs]
        break_after_ref = refs[refs.index(split_ref) - 1]
    last_end = 0.0
    for i, sub in enumerate(subs):
        # EXACT boundaries when per-subtopic segments were measured; the
        # proportional stretch is only the fallback for a script whose
        # headings did not map onto the subtopic list.
        if segment_bounds and i < len(segment_bounds):
            start, end = segment_bounds[i]
            start, end = round(min(start, cap), 2), round(min(end, cap), 2)
        else:
            start = round(min(sub["start_seconds"] * scale, cap), 2)
            end = round(min(sub["end_seconds"] * scale, cap), 2)
        last_end = end
        tracks.append({"time": start, "type": "subtopic_start",
                       "ref": sub["ref"], "title": sub.get("title", "")})
        tracks.append({"time": end, "type": "subtopic_end",
                       "ref": sub["ref"], "qa_window": QA_WINDOW_SECONDS,
                       "exercise": mcq_by_ref.get(sub["ref"], []),
                       "pass_threshold": PASS_THRESHOLD})
        if break_after_ref is not None and sub.get("ref") == break_after_ref:
            tracks.append({"time": round(end, 2), "type": "break_start",
                           "duration_seconds": BREAK_DURATION_SECONDS,
                           "bridge": "mandy",
                           "next_tutor": second_tutor["id"],
                           **({"questions": break_questions} if break_questions else {})})
    cc_ids = [q["id"] for q in comprehension.get("questions", []) if q.get("id")]
    if cc_ids:
        tracks.append({"time": round(last_end, 2), "type": "comprehension_check",
                       "questions": cc_ids, "qa_window": QA_WINDOW_SECONDS})
    tracks.append({"time": round(last_end, 2), "type": "signoff",
                   "tutor": first_tutor["id"], "audio": "audio.mp3"})
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
    cc_file = lesson_path / "comprehension_check.json"
    comprehension = json.loads(cc_file.read_text("utf-8")) if cc_file.exists() else {}
    script_md = (lesson_path / "script.md").read_text("utf-8")

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # --- 5/6. audio ---
    wav_path = out_dir / "audio.wav"

    # --- per-subtopic synthesis, then server-side concatenation ---
    # Each subtopic is synthesized as its own segment (in the voice of the
    # speaker who owns it) and the segments are concatenated here into ONE
    # audio.mp3. Client-side gapless playback of separate files is not
    # achievable on the current stack, so the join happens server-side; the
    # concat is on raw PCM frames, so nothing is re-encoded.
    segments = split_script_into_segments(script_md)
    split_ref_early = two_part_split(card, subtopics)
    sub_refs = [s.get("ref") for s in subtopics.get("subtopics", [])]
    split_index = sub_refs.index(split_ref_early) if (
        split_ref_early and split_ref_early in sub_refs) else None

    print(f"[audio] backend={args.audio_backend} segments={len(segments)} "
          f"chars={sum(len(t) for _, t in segments)}")
    seg_files, seg_durations = [], []
    for idx, text in segments:
        if args.max_narration_chars:
            text = text[:args.max_narration_chars]
        # Segment voice: subtopics from the split onward are the second
        # tutor's block. Only meaningful for a real two-part lesson.
        voice = tutor
        if split_index is not None and idx >= split_index:
            _, second = resolve_tutor_pair(card, tutor)
            if second:
                voice = second["display_name"]
        seg_path = out_dir / f"seg_{idx:02d}.wav"
        if args.audio_backend == "vibevoice":
            # Voice preset comes from the tutor persona card (documented
            # intent today; Level 6 maps it to a VibeVoice speaker embedding).
            synth_audio_vibevoice(text, seg_path, voice_preset=voice)
        else:
            synth_audio_sapi(text, seg_path)
        d = wav_duration_seconds(seg_path)
        seg_files.append(seg_path)
        seg_durations.append(d)
        print(f"  seg {idx:02d} [{voice.split('—')[0].strip()}]: {d:6.1f}s  {len(text)} chars")

    if not seg_files:
        raise SystemExit("script produced no narration segments")
    concat_wavs(seg_files, wav_path)
    audio_seconds = wav_duration_seconds(wav_path)
    drift = abs(audio_seconds - sum(seg_durations))
    if drift > 0.05:
        raise SystemExit(f"concat lost {drift:.3f}s vs the sum of segments")
    for p in seg_files:
        p.unlink()
    mp3_path = out_dir / "audio.mp3"
    to_mp3(wav_path, mp3_path)
    wav_path.unlink()
    print(f"[audio] {len(seg_files)} segment(s) -> {audio_seconds:.1f}s "
          f"(sum {sum(seg_durations):.1f}s, drift {drift:.3f}s) -> {mp3_path.name}")

    # EXACT subtopic boundaries: cumulative measured segment durations, so a
    # boundary is the real moment the narration changes subtopic — not a
    # global proportional stretch of the intended timeline.
    segment_bounds, _cursor = [], 0.0
    for d in seg_durations:
        segment_bounds.append((round(_cursor, 2), round(_cursor + d, 2)))
        _cursor += d

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
    for ev in anim.get("camera", []):
        ev["time"] = round(ev["time"] * anim_scale, 2)
    anim["duration_seconds"] = round(audio_seconds, 2)
    anim_path.write_text(json.dumps(anim, indent=2), encoding="utf-8")
    print(f"[align] subtopic x{subtopic_scale:.3f}  animation x{anim_scale:.3f}")

    # TOPIC-DISPLAY TIMING: the player shows the topic full-screen while the
    # tutor speaks the intro, until board work begins. That duration is
    # COMPUTED here from the real content — the time of the first animation
    # primitive in the rescaled (real-audio) timeline — not left to
    # coincidence: the Level 2 prompt requires scenes to open with a wait
    # beat covering the spoken intro, and this measurement turns that beat
    # into an explicit manifest contract.
    topic_display_seconds = min((p["time"] for p in anim["primitives"]),
                                default=0.0)

    first_tutor, second_tutor = resolve_tutor_pair(card, tutor)
    # GATE: only a lesson whose audio really has a second-tutor block may
    # publish second_tutor / break_start. Without this, the client announces
    # "X has joined" (break_start.time - 60s) and swaps the speaking role
    # over audio in which X never speaks.
    split_ref = two_part_split(card, subtopics)
    if second_tutor and not split_ref:
        print(f"[tutors] roster pair is {first_tutor['id']}+{second_tutor['id']}, but the "
              f"card declares no {SECOND_TUTOR_FIELD} — single-voice audio, so "
              "second_tutor/break_start are suppressed")
        second_tutor = None
    elif second_tutor:
        print(f"[tutors] two-part: {first_tutor['id']} -> {second_tutor['id']} from {split_ref}")
    else:
        print(f"[tutors] first={first_tutor['id']} — no roster pair resolved; single-tutor manifest")

    transcript_file = lesson_path / "mandy_qa_transcript.md"
    break_questions = (extract_break_questions(transcript_file.read_text("utf-8"))
                       if second_tutor and transcript_file.exists() else [])
    if break_questions:
        print(f"[break] {len(break_questions)} question(s) from mandy_qa_transcript.md")

    tracks = build_tracks(subtopics, mcq, comprehension, first_tutor,
                          second_tutor, subtopic_scale, audio_seconds,
                          topic, topic_display_seconds,
                          split_ref=split_ref, break_questions=break_questions,
                          segment_bounds=(segment_bounds
                                          if len(segment_bounds) == len(subtopics.get("subtopics", []))
                                          else None))

    # Manifest-level question bank: subtopic_end `exercise` entries are IDs
    # the app resolves against this map (lms_sdk McqQuestion.fromJson reads
    # mcq.json's field names directly — question/options/correct_index/
    # time_limit_seconds). Without it the exercise moments silently no-op.
    questions = {q["id"]: q
                 for b in mcq.get("subtopics", [])
                 for q in b.get("questions", []) if q.get("id")}

    # Comprehension-check bank, same pattern: Level 3 validates
    # comprehension_check.json but Level 6 never shipped it, while lms_sdk's
    # models already have a comprehension-check concept waiting for content.
    # The comprehension_check track event at lesson end carries the ids;
    # this bank carries the full questions (id/question/expected_answer).
    cc_bank = {q["id"]: q for q in comprehension.get("questions", []) if q.get("id")}

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
        # Second tutor identity for the app's attendee panel
        # (LessonScreenDeps.secondTutor / TutorPersona{id, displayName}) —
        # sourced from roster.json's paired-duo mapping, not a card field.
        **({"second_tutor": second_tutor} if second_tutor else {}),
        "tracks": tracks,
        **({"questions": questions} if questions else {}),
        **({"comprehension_check": cc_bank} if cc_bank else {}),
    }
    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"[manifest] {len(tracks)} tracks -> {manifest_path}")
    print(json.dumps({"session_id": card_id, "audio_seconds": round(audio_seconds, 1),
                      "tracks": len(tracks), "primitives": len(anim["primitives"])}))


if __name__ == "__main__":
    main()
