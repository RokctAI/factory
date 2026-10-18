# r3_pictures

Draws the kids-mode (Grades R–3) pictures: one hand-built SVG per picture
slug, in one shared style, with every printed word kept inside its shape.
These scripts produced the Grades 1–3 set in RokctAI/agent
`lms/dart/templates/assets/r3_pictures` (agent PR #518).

**This repo is public and holds only the engine**: the drawing library and
the code that draws each object or scene. The lesson side comes in at run
time from the private repos and is never committed here:

| Input | What it is | Where it lives |
|---|---|---|
| `--slugs` | the picture slugs the R-3 packs use | RokctAI/agent `lms/dart/test/r3_pack_picture_slugs.json` |
| `--text` | every word, phrase or sentence a picture prints | RokctAI/lessons `school/r3_pictures/r3_picture_text.json` (private); never in this repo |

## Run

```sh
python3 r3_pictures/build.py \
  --slugs    ../agent/lms/dart/test/r3_pack_picture_slugs.json \
  --text     ../lessons/school/r3_pictures/r3_picture_text.json \
  --existing ../agent/lms/dart/templates/assets/r3_pictures \
  --out      /tmp/r3_pictures_out \
  --manifest /tmp/r3_pictures.json \
  --check
```

- `--slugs` (required): `{grade: [slug]}`, `{slug: [grade]}` or a list.
- `--text`: `{"text": {key: words}}`. Without it the pictures that print
  words are not written; the manifest lists them under `needs_text`.
- `--existing`: a folder of SVGs (or a file of slugs) already drawn; those
  slugs are not written again. Point it at the agent folder as it is on
  `main` to get only the new pictures.
- `--out` (required): the output folder, one `<slug>.svg` per drawing. Copy
  the files you want into the agent's `r3_pictures` folder.
- `--manifest`: JSON with `drawn`, `alias` (slug → drawn slug, for slugs
  whose drawing is identical to another's), `tutor_thing` (tutor slug →
  picture), `needs_text`, `absent_tables` and `problems`.
- `--check`: run the fit and overlap checks on every SVG; exit 1 on any.
- `--only a,b`: write only slugs starting with these prefixes (all are
  still drawn, since scenes reuse one another).
- `--modules`, `--no-fix`: build a subset of modules; skip the fit pass.

Python 3.9+, standard library only. A full run takes about 15 s.

## Layout

- `build.py` — the command above.
- `draw/content.py` — reads the two inputs. Drawing code gets pack slugs
  from `content.pack(pattern)` / `content.SLUGS` and words from
  `words('<module>:<slug>[.<n>]')` or `content.table('<module>:<name>')`.
  A picture whose key is missing is skipped, never drawn with a stand-in.
- `draw/lib.py`, `people.py`, `props.py`, `roles.py` — shapes, outline
  attributes, palette, people. `font.py` — a stroked letter font (no
  system fonts), `text`/`texts`/`boxed` placed by the real ink box.
- `draw/kit.py`, `mkit.py`, `sk.py` — tiles, cards, coins, number lines,
  charts, figures in poses, speech bubbles.
- `draw/animals.py` … `tutor_scenes.py` — the Grade R drawings (already in
  the app); loaded first so later scenes reuse them, never written.
- `draw/g_*.py`, `n0*.py`, `t0*.py` — the Grades 1–3 drawings, in build
  order (`build.MODULES`). `g_*` are rule-driven (numerals, clock times,
  sums, word cards made from the slug), `n0*` new base objects, `t0*`
  scenes; `t09.py` is the tutor-thing map.
- `draw/samples/` — the 11 original hand-drawn SVGs other pictures reuse.

## Shared style

- `viewBox="0 0 200 200"`; one outer `<g fill="none" stroke="#1F2A44"
  stroke-width="6" stroke-linecap="round" stroke-linejoin="round">`.
- Outline colour `#1F2A44` (INK) everywhere. Stroke widths: 6 for outlines,
  3–5 for inner detail; a placed sub-drawing `g(x, y, s, ...)` sets
  `stroke-width = 6/s` so its outline stays 6 on screen. Thick limbs are an
  ink stroke 10 wider than the colour stroke on top.
- Palette (`draw/lib.py`): soft fills Y `#FFE08A`, B `#B8E6FF`, G
  `#C8F2C2`, PK `#FFC9DE`, PU `#E2D4FF`, OR `#FFD2B0`; strong RED `#E8574A`,
  BLUE `#5B8DEF`, GREEN `#6CC46C`, DGREEN `#3E9B4F`, GOLD `#FFD25A`,
  ORANGE `#F2A65A`, ROSE `#E86A8C`, PURPLE `#9B7BE0`, BROWN `#9C6B3C`, TAN
  `#E9B872`, GREY `#E2E3DE`, DGREY `#9AA1AE`, SKY `#7EC8F2`, NIGHT
  `#34416B`, skins `#C68B59` `#8D5A3B` `#F1C27D`. Tiles and cards pick
  their colour from a hash of the label, so the same word always looks the
  same.
- Ground shadow: `<ellipse cx="100" cy="182" rx="60" ry="7" fill="#1F2A44"
  stroke="none" opacity=".12"/>` (`S(cx, cy, rx)`), first in the drawing;
  `body(slug)` drops it when a drawing is reused inside a scene.
- Words are paths from `font.py` in `<g class="w">` groups (stroke
  `max(3, size × .17)`; outlined tile letters add a 6 px ink rim).
- Size budget 6000 bytes per SVG (reported, not fatal; three calendar
  pages are just over).

## Fit and overlap checks (`draw/fitfix.py`)

- **Fit** (`check`, applied by `fix` on every build unless `--no-fix`):
  each word group must sit inside the shape it is on (bubble, card, tile,
  sign) at least 6 px from that shape's inner stroke edge (or a fifth of
  the shape's inner size when smaller), or 4 px inside the canvas when it
  sits on nothing. `fix` shrinks a misfit group (or stack of lines) about
  its centre and moves it toward the shape's centre only as far as needed.
- **Overlap** (`overlaps`): no word group may be covered by a filled shape
  drawn after it, crossed by the edge of a shape under it (other than its
  own container), or touch another word group.
- `--check` runs both on every written SVG. The agent repo's
  `r3_picture_fit_test.dart` checks the same rules on the shipped set.

## Tests

`python -m pytest r3_pictures/tests` — made-up slugs and words only. One
test builds everything with no text file and fails if any picture prints a
word (two or more letters) that did not come from a slug name, i.e. if
lesson words creep back into the code.
