#!/usr/bin/env bash
# One line's face pictures: portrait + voice line + its text -> a folder of
# pictures and a timing file the app plays with the line's audio (no video).
# Steps: align the text to the voice; LivePortrait draws the face with the head
# still (jaw and lips from the voice); MuseTalk redraws the lips; GFPGAN sharpens
# the mouth; face_pack.py keeps the distinct mouth pictures, eye pictures for
# blinks, and the timing. The voice file is only read, never changed.
# Needs LP_SRC, MUSE_SRC and GFPGAN_WEIGHTS (setup.sh).
# Usage: make_face_pack.sh <portrait> <voice audio> <text file> <out dir> [normal|clear]
# 'clear' = the Grade R-3 mouth: wider, rounder, held longer.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
portrait=$(realpath "$1"); voice=$(realpath "$2"); text=$(realpath "$3"); out=$(realpath -m "$4"); style=${5:-normal}
work=$(mktemp -d); trap 'rm -rf "$work"' EXIT
ffmpeg -v error -y -i "$voice" -ac 1 -ar 16000 "$work/voice16k.wav"
python "$here/align.py" "$work/voice16k.wav" "$text" "$work/letters.json"
python "$here/still_head.py" --portrait "$portrait" --letters "$work/letters.json" --wav "$work/voice16k.wav" --style "$style" --out "$work/frames"
ffmpeg -v error -y -framerate 25 -i "$work/frames/f_%05d.png" -c:v libx264 -pix_fmt yuv420p -crf 14 "$work/face.mp4"
printf 'task_0:\n  video_path: "%s"\n  audio_path: "%s"\n' "$work/face.mp4" "$work/voice16k.wav" > "$work/muse.yaml"
( cd "$MUSE_SRC" && python -m scripts.inference --inference_config "$work/muse.yaml" --result_dir "$work/muse" \
    --unet_model_path models/musetalkV15/unet.pth --unet_config models/musetalkV15/musetalk.json \
    --version v15 --batch_size 4 --output_vid_name lips.mp4 ) > "$work/muse.log" 2>&1 || true
lips="$work/muse/v15/lips.mp4"
if [ ! -s "$lips" ]; then tail -20 "$work/muse.log"; echo "MuseTalk pass failed" >&2; exit 1; fi
python "$here/sharpen.py" "$lips" "$work/sharp.mp4"
rm -rf "$out"; python "$here/face_pack.py" "$work/sharp.mp4" "$out" --params "$work/frames/params.npy"
