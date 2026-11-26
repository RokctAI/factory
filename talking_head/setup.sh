#!/usr/bin/env bash
# Fetch the two engines at pinned commits plus their weights, CPU only.
# Usage: source setup.sh <dir>   (exports LP_SRC, MUSE_SRC and GFPGAN_WEIGHTS)
set -euo pipefail
root=$(realpath -m "${1:-$PWD/.talking_head}"); mkdir -p "$root"
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LP_REF=9b294b3d0536135442ea73cb01e6cb3ca7029dd3     # KwaiVGI/LivePortrait
MUSE_REF=2536eaf06b85f775d8e04b7fd81bf6699155a58d   # TMElyralab/MuseTalk
clone() { [ -d "$2/.git" ] || git clone --quiet "$1" "$2"; git -C "$2" checkout --quiet "$3"; }
clone https://github.com/KwaiVGI/LivePortrait.git "$root/LivePortrait" "$LP_REF"
clone https://github.com/TMElyralab/MuseTalk.git "$root/MuseTalk" "$MUSE_REF"
export LP_SRC="$root/LivePortrait" MUSE_SRC="$root/MuseTalk"
# MuseTalk's own face finder needs mmpose/mmcv, which only build against old
# Python/torch; ours uses the insightface detector LivePortrait already ships.
cp "$here/musetalk_preprocessing.py" "$MUSE_SRC/musetalk/utils/preprocessing.py"
python - <<'PY'
import os
from huggingface_hub import snapshot_download as d
lp, mu = os.environ['LP_SRC'], os.environ['MUSE_SRC']
d('KwaiVGI/LivePortrait', local_dir=f'{lp}/pretrained_weights', allow_patterns=['insightface/*', 'liveportrait/*'], ignore_patterns=['*animals*'])
d('TMElyralab/MuseTalk', local_dir=f'{mu}/models', allow_patterns=['musetalkV15/*'])
d('stabilityai/sd-vae-ft-mse', local_dir=f'{mu}/models/sd-vae', allow_patterns=['config.json', 'diffusion_pytorch_model.bin'])
d('openai/whisper-tiny', local_dir=f'{mu}/models/whisper', allow_patterns=['config.json', 'pytorch_model.bin', 'preprocessor_config.json'])
d('ManyOtherFunctions/face-parse-bisent', local_dir=f'{mu}/models/face-parse-bisent', allow_patterns=['79999_iter.pth'])
PY
# The face-parse backbone: torchvision's official ResNet-18 (same weights as
# MuseTalk's link, saved in the format current torch loads safely).
rn="$MUSE_SRC/models/face-parse-bisent/resnet18-5c106cde.pth"
[ -s "$rn" ] || curl -sSL -o "$rn" https://download.pytorch.org/models/resnet18-f37072fd.pth
# GFPGAN v1.4 (Apache-2.0) sharpens the mouth (sharpen.py). The gfpgan package is
# installed --no-deps: only its clean architecture files are used.
export GFPGAN_WEIGHTS="$root/GFPGANv1.4.pth"
[ -s "$GFPGAN_WEIGHTS" ] || curl -sSL -o "$GFPGAN_WEIGHTS" https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/GFPGANv1.4.pth
python -m pip install --quiet --no-deps gfpgan==1.3.8
echo "LP_SRC=$LP_SRC"; echo "MUSE_SRC=$MUSE_SRC"; echo "GFPGAN_WEIGHTS=$GFPGAN_WEIGHTS"
