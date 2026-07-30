# -*- coding: utf-8 -*-
"""Derive every app-side rendition of a tutor/assistant photo from ONE source
image, the way a user profile picture works: drop the generated portrait into
lessons/tutors/<id>/appearance/ (or lessons/assistants/<name>/appearance/) and
this produces the crops the app actually asks for.

Renditions, taken from what the shipped widgets do:
  * card_1080x1440 (3:4) - TutorCard is a FULL-BLEED photo (the mockup card is
    ~340x460), drawn with BoxFit.cover behind a bottom scrim;
  * avatar_512 (1:1)     - tutor profile / detail sheet;
  * avatar_168 (1:1)     - the 56pt session speaker bubble at 3x.

Why cropping needs a focus point: a studio portrait is mostly body, so a
naive centre crop to a square lands on the chest. Each subject may carry
appearance/crop.json - {"focus_x": 0.5, "focus_y": 0.22, "zoom": 1.0} - where
focus is the FACE CENTRE in normalised source coordinates. The default suits
a waist-up studio portrait; if a crop looks wrong, move focus_y rather than
re-generating the image. Portrait framing is deliberate, not centred: the
face sits high in a card (rule of thirds) and near-centred in an avatar.

Runs are idempotent: a subject is skipped when its source image, its crop
settings and the rendition spec are all unchanged since the last run and the
output files are still on disk. Re-running costs nothing, so CI can call it
on every push; replacing a portrait, editing crop.json or changing
RENDITIONS re-renders exactly the subjects affected.

Usage:
  python lessons/scripts/tutor_images.py            # everyone with a source
  python lessons/scripts/tutor_images.py tutor_001  # one subject
  python lessons/scripts/tutor_images.py --check    # report, write nothing
  python lessons/scripts/tutor_images.py --force    # re-render regardless
"""
import hashlib
import json
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is required: python -m pip install Pillow")

LESSONS = Path("lessons")
SUBJECT_DIRS = (LESSONS / "tutors", LESSONS / "assistants")
RASTER = (".png", ".jpg", ".jpeg", ".webp")

# name -> (width, height, focus_at, target_face)
#   focus_at    - where the face sits down the crop, as a fraction of its
#                 height (0.38 on a tall card leaves room for the scrim text)
#   target_face - how much of the crop's HEIGHT the head should occupy. This
#                 is what makes an avatar an avatar: squaring the card
#                 framing gives a full-body thumbnail whose face is a few
#                 pixels at 56pt, so the square crops pull right in.
RENDITIONS = {
    "card_1080x1440": (1080, 1440, 0.38, 0.22),
    "avatar_512": (512, 512, 0.44, 0.52),
    "avatar_168": (168, 168, 0.44, 0.52),
}

# face_height: how much of the SOURCE height the head occupies (hairline to
# chin). 0.25 suits a waist-up studio portrait; a full-length shot is nearer
# 0.12. It is the one measurement the crops derive from, so if every
# rendition of a subject is too tight or too loose, change this - not zoom.
DEFAULT_CROP = {"focus_x": 0.5, "focus_y": 0.22, "face_height": 0.25,
                "zoom": 1.0}

# Onboarding slides are SCENES, not portraits. No face measurement applies -
# the subject is a person in a room - so these crop to the largest fitting box
# around a focus point that sits lower in frame than a headshot's.
ONBOARDING_RENDITIONS = {
    "slide_1080x1920": (1080, 1920, 0.45, None),
    "card_1080x1350": (1080, 1350, 0.45, None),
}
ONBOARDING_CROP = {"focus_x": 0.5, "focus_y": 0.45, "face_height": None,
                   "zoom": 1.0}
ONBOARDING_DIR = LESSONS / "onboarding"


def find_source(appearance: Path):
    """The portrait to derive from: source.* by convention, else the largest
    raster sitting directly in appearance/ (renders/ is never a source)."""
    for ext in RASTER:
        p = appearance / f"source{ext}"
        if p.exists():
            return p
    cands = [p for p in appearance.iterdir()
             if p.is_file() and p.suffix.lower() in RASTER]
    return max(cands, key=lambda p: p.stat().st_size) if cands else None


def load_crop(appearance: Path):
    cfg = dict(DEFAULT_CROP)
    p = appearance / "crop.json"
    if p.exists():
        cfg.update(json.loads(p.read_text(encoding="utf-8")))
    return cfg


def crop_box(src_w, src_h, aspect, focus_x, focus_y, focus_at, zoom,
             face_height=None, target_face=None):
    """A box of [aspect] (w/h) sized so the head fills [target_face] of its
    height, positioned so the face sits at [focus_at] down the box and
    horizontally centred on the focus. Falls back to the largest fitting box
    when no face measurement is given. Clamped to the image."""
    if face_height and target_face:
        box_h = src_h * face_height / target_face
    else:
        box_h = min(src_h, src_w / aspect)
    box_h = min(box_h / max(zoom, 0.01), src_h, src_w / aspect)
    box_w = box_h * aspect
    if box_w > src_w:  # zoom pushed it past the edge
        box_w, box_h = src_w, src_w / aspect
    left = focus_x * src_w - box_w / 2
    top = focus_y * src_h - box_h * focus_at
    left = max(0, min(left, src_w - box_w))
    top = max(0, min(top, src_h - box_h))
    return (round(left), round(top), round(left + box_w), round(top + box_h))


def recipe_of(src: Path, cfg: dict):
    """What the renders depend on: the source bytes, the crop settings and
    the rendition spec. Any of them changing invalidates the output; none of
    them changing means there is nothing to do."""
    h = hashlib.sha1(src.read_bytes()).hexdigest()[:12]
    spec = json.dumps({"crop": cfg, "renditions": RENDITIONS}, sort_keys=True)
    return h, hashlib.sha1(spec.encode()).hexdigest()[:12]


def is_current(out_dir: Path, src_sha1, recipe_sha1):
    """True when the last run used the same source AND the same recipe, and
    every file it claims to have written is still there."""
    man = out_dir / "manifest.json"
    if not man.exists():
        return False
    try:
        prev = json.loads(man.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return False
    if prev.get("source_sha1") != src_sha1 or prev.get("recipe_sha1") != recipe_sha1:
        return False
    return all((out_dir / f"{name}.png").exists() for name in RENDITIONS)


def process(appearance: Path, check_only=False, force=False):
    src = find_source(appearance)
    subject = appearance.parent.name
    if src is None:
        return {"subject": subject, "status": "no source image"}

    cfg = load_crop(appearance)
    out_dir = appearance / "renders"
    src_sha1, recipe_sha1 = recipe_of(src, cfg)
    if not force and is_current(out_dir, src_sha1, recipe_sha1):
        return {"subject": subject, "status": "up to date", "source": src.name}

    img = Image.open(src)
    img = img.convert("RGB")
    w, h = img.size
    results = {}
    for name, (tw, th, focus_at, target_face) in RENDITIONS.items():
        box = crop_box(w, h, tw / th, cfg["focus_x"], cfg["focus_y"],
                       focus_at, cfg["zoom"],
                       cfg.get("face_height"), target_face)
        if not check_only:
            out_dir.mkdir(exist_ok=True)
            img.crop(box).resize((tw, th), Image.LANCZOS).save(
                out_dir / f"{name}.png", "PNG", optimize=True)
        results[name] = {"size": [tw, th], "source_box": list(box)}

    manifest = {
        "subject": subject,
        "source": src.name,
        "source_size": [w, h],
        "source_sha1": src_sha1,
        "recipe_sha1": recipe_sha1,
        "crop": cfg,
        "renditions": results,
        "_comment": [
            "Generated by lessons/scripts/tutor_images.py - do not hand-edit.",
            "One source portrait, every app rendition: the card is full-bleed",
            "3:4, the avatars are square. If a face sits wrong in a crop,",
            "edit appearance/crop.json (focus_y moves the face up/down) and",
            "re-run; never re-generate the portrait for a framing problem.",
        ],
    }
    if not check_only:
        (out_dir / "manifest.json").write_text(
            json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return {"subject": subject, "status": "ok", "source": src.name,
            "source_size": [w, h], "renditions": list(results)}


def process_onboarding(check_only=False):
    """Onboarding slide images live beside their slide JSON, named the same:
    lessons/onboarding/students/01_welcome_1_live_classes.png next to
    ...01_welcome_1_live_classes.json. Renders to renders/<slide>/."""
    rows = []
    if not ONBOARDING_DIR.is_dir():
        return rows
    for branch in sorted(d for d in ONBOARDING_DIR.iterdir() if d.is_dir()):
        for spec in sorted(branch.glob("*.json")):
            src = None
            for ext in RASTER:
                cand = spec.with_suffix(ext)
                if cand.exists():
                    src = cand
                    break
            if src is None:
                continue
            img = Image.open(src).convert("RGB")
            w, h = img.size
            out_dir = branch / "renders" / spec.stem
            results = {}
            for name, (tw, th, focus_at, _face) in ONBOARDING_RENDITIONS.items():
                box = crop_box(w, h, tw / th, ONBOARDING_CROP["focus_x"],
                               ONBOARDING_CROP["focus_y"], focus_at,
                               ONBOARDING_CROP["zoom"])
                if not check_only:
                    out_dir.mkdir(parents=True, exist_ok=True)
                    img.crop(box).resize((tw, th), Image.LANCZOS).save(
                        out_dir / f"{name}.png", "PNG", optimize=True)
                results[name] = {"size": [tw, th], "source_box": list(box)}
            if not check_only:
                (out_dir / "manifest.json").write_text(json.dumps({
                    "slide": spec.stem, "branch": branch.name,
                    "source": src.name, "source_size": [w, h],
                    "source_sha1": hashlib.sha1(src.read_bytes()).hexdigest()[:12],
                    "renditions": results,
                    "_comment": [
                        "Generated by lessons/scripts/tutor_images.py.",
                        "Onboarding slides crop as SCENES - no face logic - to",
                        "the 9:16 phone slide and a 4:5 card.",
                    ],
                }, indent=2) + "\n", encoding="utf-8")
            rows.append({"subject": f"{branch.name}/{spec.stem}",
                         "status": "ok", "source": src.name,
                         "source_size": [w, h],
                         "renditions": list(results)})
    return rows


def main(argv):
    check = "--check" in argv
    force = "--force" in argv
    wanted = [a for a in argv if not a.startswith("--")]
    rows = []
    for root in SUBJECT_DIRS:
        if not root.is_dir():
            continue
        for sub in sorted(root.iterdir()):
            if not sub.is_dir() or (wanted and sub.name not in wanted):
                continue
            appearance = sub / "appearance"
            if appearance.is_dir():
                rows.append(process(appearance, check, force))
    rows += process_onboarding(check)
    if not rows:
        print("No appearance directories found.")
        return 1
    done = 0
    for r in rows:
        if r["status"] == "ok":
            done += 1
            print(f"{r['subject']:<12} {r['source']}  "
                  f"{r['source_size'][0]}x{r['source_size'][1]}  -> "
                  f"{', '.join(r['renditions'])}")
        else:
            print(f"{r['subject']:<12} {r['status']}")
    skipped = sum(1 for r in rows if r["status"] == "up to date")
    print(f"\n{done} rendered, {skipped} already up to date, "
          f"{len(rows) - done - skipped} without a source"
          f"{' (check only, nothing written)' if check else ''}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
