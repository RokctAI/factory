# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""The animated visual for a daily opportunity Reel.

Draws every frame with Pillow and pipes them to ffmpeg, producing a
1080x1920 30fps clip that tiktok_render.py then conforms and encodes. The
beats, in order: the brand drops in, the kind badge slides across, the
headline figure counts up to its exact card value, the title rises line
by line, the deadline lands with a live days-left counter, and the close
points the viewer at the first comment for the link. The domain never
appears in the video; the brand name does.

Built for the first second: the money figure is already on screen, big,
in frame one, and the beats land on the music's tempo. Colours are the
brand's; the background motif and the music rotate by date, so consecutive
days do not look like one template (Meta limits reach and monetisation on
repetitive, templated content).
"""

import math
import re
import subprocess
from pathlib import Path

W, H, FPS = 1080, 1920, 30
BRAND = "ROKCT"
CLOSE_LINE = "Link in the comments"
# TikTok and YouTube Shorts do not make links in comments clickable, so
# their cut points at the profile link instead.
CLOSE_LINE_BIO = "Link in bio"

# Brand, from RokctAI_frontend: --primary hsl(48 96% 53%) on the dark
# --background hsl(240 10% 3.9%); the logo tile is the header's dark-mode
# zinc-100 -> zinc-300 gradient carrying logo_dark.svg.
BG = (9, 9, 11)
ACCENT = (250, 204, 21)
INK = (244, 244, 245)
TILE_TOP, TILE_BOTTOM = (244, 244, 245), (212, 212, 216)
ASSETS = Path(__file__).resolve().parent / "assets"
LOGO = ASSETS / "rokct-logo-dark.png"


def _font(size, bold=True):
    from PIL import ImageFont

    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    for base in ("/usr/share/fonts/truetype/dejavu", "/usr/share/fonts/dejavu"):
        if Path(base, name).exists():
            return ImageFont.truetype(str(Path(base, name)), size)
    return ImageFont.load_default()


def _ease(t):
    """Ease-out cubic on 0..1, clamped."""
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def _back(t):
    """Ease-out with a small overshoot, for things that pop."""
    t = max(0.0, min(1.0, t))
    c = 1.70158
    return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2


def _phase(t, start, length):
    return (t - start) / length


def _wrap(draw, text, font, width, max_lines):
    words, lines, line = text.split(), [], ""
    for word in words:
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=font) <= width or not line:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(" ,-") + "..."
    return lines


def _fit(draw, text, size, width, max_lines, floor, bold=True):
    """The largest font from size down to floor that wraps text into
    max_lines without cutting it; floor (cut if it must) when none does."""
    for n in range(size, floor - 1, -4):
        font = _font(n, bold)
        if len(_wrap(draw, text, font, width, 99)) <= max_lines:
            return font
    return _font(floor, bold)


# A tip heading such as "Tender tip: partner to qualify" puts its type on the
# badge and the rest in the headline.
_TIP_TYPE = re.compile(r"^\s*(tender|grant|investor|funding) tip:\s*", re.I)


_NUMBER = re.compile(r"\d[\d,\s]*(?:\.\d+)?")


def _value(text):
    m = _NUMBER.search(text or "")
    try:
        return float(re.sub(r"[,\s]", "", m.group(0))) if m else None
    except ValueError:
        return None


def counting(text, progress, start=0.0):
    """The headline with its first number counted from `start` up to its
    value (`progress` 0..1), formatted the way the card writes it. At
    progress 1 the text is exactly the card's text - the count only ever
    lands on the real figure."""
    m = _NUMBER.search(text)
    if not m or progress >= 1:
        return text
    raw = m.group(0).rstrip()
    digits = re.sub(r"[,\s]", "", raw)
    try:
        value = float(digits)
    except ValueError:
        return text
    now = start + (value - start) * _ease(progress)
    decimals = len(digits.split(".")[1]) if "." in digits else 0
    shown = f"{now:,.{decimals}f}" if "," in raw else f"{now:.{decimals}f}"
    return text[: m.start()] + shown + text[m.start() + len(raw):]


_UNIT = r"(?:\s?(?:million|billion|bn|m|k|lakhs?|crores?)\b)?"
_AMOUNT = re.compile(r"\d[\d,]*(?:\.\d+)?" + _UNIT, re.I)
_RANGE_JOIN = re.compile(r"\s*(?:to|-|–)\s*[^\d\s]{0,3}", re.I)
MIN_AT, HOLD, MAX_FOR = 1.2, 0.6, 1.2  # range: count to min, hold, count to max


def split_figure(text):
    """'Up to $2,000 to $7,500 per project' ->
    ('Up to $2,000 to $7,500', 'per project', index where the minimum ends).
    The index is None for a single figure; None overall when there is no number."""
    m = _AMOUNT.search(text)
    if not m:
        return None
    end, first_end = m.end(), None
    j = _RANGE_JOIN.match(text, end)
    m2 = _AMOUNT.match(text, j.end()) if j else None
    if m2:
        first_end, end = m.end(), m2.end()
    return text[:end].strip(), text[end:].strip(" ,"), first_end


_MULTIPLIER = {"k": 1e3, "m": 1e6, "million": 1e6, "bn": 1e9, "billion": 1e9}


def _unit_of(text):
    return re.search(_UNIT + "$", text.strip(), re.I).group(0).strip().lower()


def _expand(text, value, unit):
    """'€1 million' -> '€1,000,000' so it counts on from a figure in units."""
    m = _AMOUNT.search(text)
    full = value * _MULTIPLIER.get(unit, 1)
    return text[: m.start()] + f"{full:,.0f}" + text[m.end():]


def figure_at(figure, first_end, t):
    """(text to show, finished) at t seconds. A single figure counts up from
    40%. A range shows one amount only: it counts to the minimum, holds, then
    becomes "Up to" and climbs on to the maximum - the climb says there is
    more without printing two numbers."""
    if first_end is None:
        p = 0.4 + 0.6 * _phase(t, 0.0, 1.4)
        return counting(figure, p), p >= 1
    head, tail = figure[:first_end], figure[first_end:]
    top = re.sub(r"^\s*(?:to|-|–)\s*", "", tail, flags=re.I)
    if top[:1].isdigit():  # "€1-2.5 million": the maximum borrows the minimum's symbol
        sym = re.search(r"(\S*?)\d", head)
        top = (sym.group(1) if sym else "") + top
    lo, hi = _value(head), _value(top)
    u_lo, u_hi = _unit_of(head), _unit_of(top)
    if u_hi and not u_lo and lo is not None and lo < 1000:
        head, u_lo = head.rstrip() + " " + u_hi, u_hi  # "€1-2.5 million" -> "€1 million"
    elif u_hi != u_lo and not u_lo and hi is not None:
        top = _expand(top, hi, u_hi)  # "€800,000 to €1 million" -> "... €1,000,000"
        hi, u_hi = _value(top), ""
    if t < MIN_AT + HOLD:
        return counting(head, 0.4 + 0.6 * _phase(t, 0.0, MIN_AT)), False
    start = lo if (lo is not None and hi and u_lo == u_hi and lo < hi) else 0.4 * (hi or 0)
    p = _phase(t, MIN_AT + HOLD, MAX_FOR)
    return "Up to " + counting(top, p, start), p >= 1


def _glow(color, radius):
    from PIL import Image, ImageDraw, ImageFilter

    size = radius * 4
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    ImageDraw.Draw(img).ellipse(
        [radius, radius, size - radius, size - radius], fill=color + (90,)
    )
    return img.filter(ImageFilter.GaussianBlur(radius // 2))


def _logo_tile(size):
    """The header brand mark: rounded gradient tile with the logo inside."""
    from PIL import Image, ImageDraw

    tile = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    grad = Image.new("RGBA", (size, size))
    gd = ImageDraw.Draw(grad)
    for y in range(size):
        k = y / max(1, size - 1)
        gd.line([(0, y), (size, y)], fill=tuple(
            int(TILE_TOP[i] + (TILE_BOTTOM[i] - TILE_TOP[i]) * k) for i in range(3)) + (255,))
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, size - 1, size - 1], radius=size // 5, fill=255)
    tile.paste(grad, (0, 0), mask)
    if LOGO.exists():
        logo = Image.open(LOGO).convert("RGBA")
        h = int(size * 0.66)
        logo = logo.resize((int(logo.width * h / logo.height), h), Image.LANCZOS)
        tile.alpha_composite(logo, ((size - logo.width) // 2, (size - logo.height) // 2))
    return tile


class Scene:
    def __init__(self, opp, headline, days_left, seed, duration, bpm, close_line=CLOSE_LINE):
        from PIL import Image

        self.opp = opp
        self.close_line = close_line
        self.headline = headline
        self.badge = opp["kind"].upper()
        tip = _TIP_TYPE.match(headline) if opp["kind"] == "Funding tip" else None
        if tip:
            self.badge = f"{tip.group(1)} tip".upper()
            rest = headline[tip.end():]
            self.headline = rest[:1].upper() + rest[1:]
        if opp["kind"] == "Funding tip" and opp.get("id"):
            self.badge += f" #{opp['id']}"
        self.fonts = {}
        self.days_left = days_left
        self.duration = duration
        self.beat = 60.0 / bpm
        self.bg, self.accent, self.ink = BG, ACCENT, INK
        self.motif = seed % 3
        self.glows = [_glow(ACCENT, 260), _glow((255, 150, 0), 200)]
        self.base = Image.new("RGB", (W, H), self.bg)
        self.tile_small = _logo_tile(84)
        self.f_brand = _font(58)
        self.f_brand_big = _font(130)
        self.f_kind = _font(42)
        self.f_head = _font(104)
        self.f_rest = _font(58)
        self.f_title = _font(48, bold=False)
        self.f_date = _font(54)
        self.f_small = _font(44, bold=False)
        self.f_cta = _font(62)

    def pulse(self, t):
        """1 on each beat, decaying to 0 before the next - for on-beat hits."""
        return math.exp(-((t % self.beat) / self.beat) * 6)

    # -- background -------------------------------------------------------

    def _background(self, img, t):
        from PIL import ImageDraw

        # Two glows drifting on slow Lissajous paths.
        for i, g in enumerate(self.glows):
            x = W / 2 + math.sin(t * (0.35 + 0.2 * i) + i * 2) * 360 - g.width / 2
            y = H * (0.3 + 0.35 * i) + math.cos(t * (0.3 + 0.15 * i) + i) * 280 - g.height / 2
            img.paste(g, (int(x), int(y)), g)
        d = ImageDraw.Draw(img, "RGBA")
        a = self.accent + (26,)
        if self.motif == 0:  # diagonal lines sliding
            off = (t * 60) % 120
            for k in range(-20, 30):
                x = k * 120 + off
                d.line([(x, 0), (x - 900, H)], fill=a, width=3)
        elif self.motif == 1:  # rising dots
            for k in range(40):
                x = (k * 173) % W
                y = (H - ((t * (40 + k % 5 * 18) + k * 211) % (H + 100)))
                r = 4 + k % 4 * 2
                d.ellipse([x - r, y - r, x + r, y + r], fill=self.accent + (60,))
        else:  # pulsing rings
            for k in range(5):
                r = ((t * 120 + k * 260) % 1300)
                d.ellipse(
                    [W / 2 - r, H * 0.45 - r, W / 2 + r, H * 0.45 + r],
                    outline=self.accent + (int(40 * (1 - r / 1300)),),
                    width=4,
                )

    # -- frame ------------------------------------------------------------

    def frame(self, t):
        from PIL import Image, ImageDraw

        img = self.base.copy()
        self._background(img, t)
        d = ImageDraw.Draw(img, "RGBA")
        margin, inner = 96, W - 2 * 96

        def text(xy, s, font, fill, alpha=1.0):
            # ImageDraw ignores fill alpha for text, so fades go through a mask.
            alpha = max(0.0, min(1.0, alpha))
            if alpha < 0.01 or not s:
                return
            left, top, right, bottom = d.textbbox((0, 0), s, font=font)
            mask = Image.new("L", (right - left, bottom - top), 0)
            ImageDraw.Draw(mask).text((-left, -top), s, font=font, fill=int(255 * alpha))
            img.paste(fill, (int(xy[0] + left), int(xy[1] + top)), mask)

        end_start = self.duration - 2.6
        hit = self.pulse(t)

        # Brand mark, top-left: logo tile + wordmark, drops in.
        if t < end_start:
            p = _back(_phase(t, 0.0, 0.5))
            y = int(100 - 60 * (1 - p))
            if p > 0.05:
                img.paste(self.tile_small, (margin, y), self.tile_small)
            text((margin + 104, y + 8), BRAND, self.f_brand, self.ink, p)

            fade = 1 - _ease(_phase(t, end_start - 0.4, 0.4))

            # Kind badge: already there in frame one, slides the last bit.
            p = _ease(_phase(t, -0.3, 0.6))
            label = self.badge
            bw = d.textlength(label, font=self.f_kind) + 56
            x = margin - 200 * (1 - p)
            y = 420
            d.rounded_rectangle([x, y, x + bw, y + 78], radius=39, fill=self.accent + (int(255 * fade),))
            text((x + 28, y + 14), label, self.f_kind, self.bg, fade)

            # Headline figure: on screen and big from frame one, counting up
            # to the exact card value, kicking on every beat. A grant's
            # figure (a range too) stays on one line, sized to fit; what
            # follows it ("per project") sits underneath.
            kick = 1 + 0.035 * hit
            split = split_figure(self.headline) if self.opp["kind"] == "Grant" else None
            y = 560
            if split:
                figure, rest, first_end = split
                final, _ = figure_at(figure, first_end, self.duration)
                size = min(104, int(104 * inner / max(1, d.textlength(final, font=self.f_head))))
                shown, done = figure_at(figure, first_end, t)
                f_fig = _font(int(size * kick)) if hit > 0.05 else _font(size)
                text((margin, y + (104 - size) * 0.6), shown, f_fig, self.ink if done else self.accent, fade)
                y += 124
                for line in _wrap(d, rest, self.f_rest, inner, 2):
                    text((margin, y), line, self.f_rest, self.ink, fade)
                    y += 70
            else:
                # Shrunk until the whole headline fits in three lines.
                if "head" not in self.fonts:
                    self.fonts["head"] = _fit(d, self.headline, 104, inner, 3, 72)
                size = self.fonts["head"].size
                p = 0.4 + 0.6 * _phase(t, 0.0, 1.4)
                shown = counting(self.headline, p)
                lines = _wrap(d, self.headline, self.fonts["head"], inner, 3)
                live = _wrap(d, shown, self.fonts["head"], inner, 3) if p < 1 else lines
                f_head = _font(int(size * kick)) if hit > 0.05 else self.fonts["head"]
                for line in live:
                    text((margin, y), line, f_head, self.accent if t < 1.4 else self.ink, fade)
                    y += int(size * 1.19)

            # Title rises line by line.
            y += 24
            # A tip's body is the tip itself, so it gets more lines than a title.
            if "title" not in self.fonts:
                rows = 6 if self.opp["kind"] == "Funding tip" else 4
                self.fonts["title"] = _fit(d, self.opp["title"], 48, inner, rows, 40, bold=False)
                self.fonts["rows"] = rows
            f_title = self.fonts["title"]
            for i, line in enumerate(_wrap(d, self.opp["title"], f_title, inner, self.fonts["rows"])):
                p = _ease(_phase(t, 1.0 + i * 0.18, 0.5))
                text((margin, y + 50 * (1 - p)), line, f_title, self.ink, min(p * 0.85, fade))
                y += int(f_title.size * 1.33)

            # Deadline block: live days-left counter, pulsing on the beat.
            # Posts with no deadline (investors, tips) carry a two-line
            # panel instead: opp["panel"] = (big accent line, small line).
            y = max(y + 80, 1320)
            p = _back(_phase(t, 2.2, 0.5))
            panel = self.opp.get("panel")
            if panel and p > 0.01:
                w = (W - 2 * margin) * min(1, p)
                d.rounded_rectangle(
                    [margin, y, margin + w, y + 330], radius=34, fill=(255, 255, 255, int(22 * fade))
                )
                d.rectangle([margin, y, margin + 12, y + 330], fill=self.accent + (int(255 * fade),))
                big = _wrap(d, panel[0], self.f_date, inner - 100, 2)
                yy = y + 40 + (60 if len(big) == 1 else 0)
                for line in big:
                    text((margin + 50, yy), line, self.f_date, self.accent, min(p, fade))
                    yy += 72
                for line in _wrap(d, panel[1], self.f_small, inner - 100, 2):
                    text((margin + 50, yy + 20), line, self.f_small, self.ink, min(p, fade))
                    yy += 56
            elif p > 0.01:
                w = (W - 2 * margin) * min(1, p)
                d.rounded_rectangle(
                    [margin, y, margin + w, y + 330], radius=34, fill=(255, 255, 255, int(22 * fade))
                )
                d.rectangle([margin, y, margin + 12, y + 330], fill=self.accent + (int(255 * fade),))
                count = int(round(self.days_left * _ease(_phase(t, 2.4, 1.0))))
                days_font = _font(int(170 * (1 + 0.05 * hit * (t > 3.4))))
                text((margin + 50, y + 26), f"{count}", days_font, self.accent, min(p, fade))
                nx = margin + 70 + d.textlength(f"{count}", font=days_font)
                text((nx, y + 110), "days left", self.f_date, self.ink, min(p, fade))
                text(
                    (margin + 50, y + 230),
                    f"Closes {self.opp['deadline_text']}",
                    self.f_small,
                    self.ink,
                    min(p, fade),
                )

            # Who it is from.
            p = _ease(_phase(t, 4.0, 0.6))
            y2 = y + 400
            for line in _wrap(d, self.opp.get("who") or "", self.f_small, inner, 2):
                text((margin, y2 + 30 * (1 - p)), line, self.f_small, self.ink, min(p * 0.85, fade))
                y2 += 58
        else:
            # Close: the brand mark (logo at its first-frame size, above the
            # name) and the pointer to the first comment.
            p = _back(_phase(t, end_start, 0.6))
            size = self.tile_small.width
            if p > 0.05:
                img.paste(self.tile_small, (int((W - size) / 2), int(H * 0.36 - 40 * (1 - p))), self.tile_small)
            bw = d.textlength(BRAND, font=self.f_brand_big)
            text(((W - bw) / 2, H * 0.36 + size + 40 + 60 * (1 - p)), BRAND, self.f_brand_big, self.ink, p)
            p2 = _ease(_phase(t, end_start + 0.4, 0.5))
            cw = d.textlength(self.close_line, font=self.f_cta)
            text(((W - cw) / 2, H * 0.62), self.close_line, self.f_cta, self.accent, p2)
            bounce = abs(math.sin((t - end_start) * math.pi / self.beat)) * 30
            ax, ay = W / 2, H * 0.70 + bounce
            d.polygon(
                [(ax - 40, ay), (ax + 40, ay), (ax, ay + 50)],
                fill=self.accent + (int(255 * p2),),
            )

        # Progress bar along the foot.
        d.rectangle([0, H - 14, W * t / self.duration, H], fill=self.accent + (220,))
        return img


def render_motion(opp, headline, days_left, seed, duration, bpm, out: Path, close_line=CLOSE_LINE):
    """Write the animated clip to `out` (mp4, no audio)."""
    scene = Scene(opp, headline, days_left, seed, duration, bpm, close_line)
    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
        "-i", "-",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
        str(out),
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    try:
        for i in range(int(duration * FPS)):
            proc.stdin.write(scene.frame(i / FPS).convert("RGB").tobytes())
    finally:
        proc.stdin.close()
    if proc.wait() != 0:
        raise RuntimeError("ffmpeg failed while encoding the motion clip")
    return out
