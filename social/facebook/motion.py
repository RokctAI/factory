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
brand's; each post type has four background motifs of its own, and motif
and music rotate by date, so consecutive days do not look like one template
(Meta limits reach and monetisation on repetitive, templated content).
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

# Backgrounds: four per post type, picked by the day's seed, so each type
# has a look of its own and no type repeats inside a working week. Every
# motif sits at low alpha behind the text and moves slowly; the two soft
# glows under it carry the type's tint next to the brand gold.
MOTIFS = {
    "Grant": ("aurora", "coins", "bars", "horizon"),
    "Tender": ("blueprint", "checklist", "sheets", "ruler"),
    "Investor": ("network", "curve", "orbits", "hexes"),
    "Funding tip": ("notebook", "chevrons", "sparks", "waves"),
}
MOTIF_NAMES = {
    "aurora": "Aurora ribbons", "coins": "Drifting coins", "bars": "Rising bars", "horizon": "Horizon grid",
    "blueprint": "Blueprint grid", "checklist": "Checklist", "sheets": "Floating sheets", "ruler": "Tape measures",
    "network": "Constellation", "curve": "Growth curve", "orbits": "Orbits", "hexes": "Honeycomb",
    "notebook": "Ruled page", "chevrons": "Chevrons", "sparks": "Idea sparks", "waves": "Waves",
}
TINT = {"Grant": (255, 150, 0), "Tender": (150, 160, 185), "Investor": (255, 110, 60), "Funding tip": (255, 228, 170)}


def motif_for(kind, seed):
    names = MOTIFS.get(kind, MOTIFS["Grant"])
    return names[seed % len(names)]


def _noise(k, i=0):
    """A stable pseudo-random 0..1 for particle k, channel i."""
    return (math.sin(k * 127.1 + i * 311.7) * 43758.5453) % 1.0
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
        # A tip's number sits in a second, white pill beside the badge.
        self.tag = f"#{opp['id']}" if opp["kind"] == "Funding tip" and opp.get("id") else ""
        self.fonts = {}
        self.days_left = days_left
        self.duration = duration
        self.beat = 60.0 / bpm
        self.bg, self.accent, self.ink = BG, ACCENT, INK
        self.motif = motif_for(opp["kind"], seed)
        self.glows = [_glow(ACCENT, 260), _glow(TINT.get(opp["kind"], TINT["Grant"]), 200)]
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

        # Two glows drifting on slow Lissajous paths, then the type's motif.
        for i, g in enumerate(self.glows):
            x = W / 2 + math.sin(t * (0.35 + 0.2 * i) + i * 2) * 360 - g.width / 2
            y = H * (0.3 + 0.35 * i) + math.cos(t * (0.3 + 0.15 * i) + i) * 280 - g.height / 2
            img.paste(g, (int(x), int(y)), g)
        getattr(self, f"_m_{self.motif}")(ImageDraw.Draw(img, "RGBA"), t, self.pulse(t))

    # Grants: generous, warm, upward.

    def _m_aurora(self, d, t, hit):
        # Five soft ribbons, each a slow sine band, layered at low alpha.
        for i in range(5):
            base = H * (0.18 + 0.17 * i)
            amp, thick, speed = 90 + 30 * (i % 3), 110 + 40 * (i % 2), 0.25 + 0.07 * i
            top = [(x, base + amp * math.sin(x / 320 + t * speed + i * 1.3)) for x in range(-40, W + 80, 40)]
            bottom = [(x, y + thick + 30 * math.sin(x / 210 - t * speed * 0.7 + i)) for x, y in reversed(top)]
            d.polygon(top + bottom, fill=self.accent + (22 + 6 * (i % 2),))

    def _m_coins(self, d, t, hit):
        # Coins drifting up at three depths: the nearer, the bigger and faster.
        for k in range(26):
            depth = k % 3
            r = 14 + 12 * depth
            x = _noise(k) * W + math.sin(t * 0.6 + k) * (20 + 10 * depth)
            y = H + 100 - ((t * (55 + 30 * depth) + _noise(k, 1) * (H + 200)) % (H + 200))
            a = 40 + 25 * depth
            d.ellipse([x - r, y - r, x + r, y + r], outline=self.accent + (a,), width=3)
            ri = r * 0.62
            d.ellipse([x - ri, y - ri, x + ri, y + ri], outline=self.accent + (a // 2,), width=2)

    def _m_bars(self, d, t, hit):
        # A bar chart along the foot, each bar breathing on its own clock.
        n, gap = 16, 16
        bw = (W - gap * (n + 1)) / n
        for k in range(n):
            base = 140 + 260 * _noise(k, 2)
            h = base * (0.7 + 0.3 * math.sin(t * (0.5 + 0.2 * (k % 4)) + k)) + 40 * hit * (k % 3 == 0)
            x = gap + k * (bw + gap)
            d.rectangle([x, H - h, x + bw, H], fill=self.accent + (30,))
            d.rectangle([x, H - h, x + bw, H - h + 6], fill=self.accent + (60,))

    def _m_horizon(self, d, t, hit):
        # A perspective floor rolling toward the viewer under a horizon line.
        a, hz, vx = self.accent, H * 0.62, W / 2
        d.line([(0, hz), (W, hz)], fill=a + (80,), width=3)
        for k in range(-9, 10):
            d.line([(vx + k * 80, hz), (vx + k * 900, H)], fill=a + (36,), width=2)
        for k in range(14):
            f = ((k + t * 0.35) % 14) / 14  # 0 at the horizon, 1 at the foot
            y = hz + (H - hz) * f * f
            d.line([(0, y), (W, y)], fill=a + (int(16 + 56 * f),), width=2 if f < 0.5 else 3)

    # Tenders: structured, official, measured.

    def _m_blueprint(self, d, t, hit):
        # A drafting grid panning slowly, crosshairs on the major lines, a scan line.
        a, step = self.accent, 96
        ox, oy = (t * 18) % step, (t * 12) % step
        for x in range(-step, W + step, step):
            d.line([(x + ox, 0), (x + ox, H)], fill=a + (24,), width=1)
        for y in range(-step, H + step, step):
            d.line([(0, y + oy), (W, y + oy)], fill=a + (24,), width=1)
        for i in range(-1, W // (step * 4) + 2):
            for j in range(-1, H // (step * 4) + 2):
                x, y = i * step * 4 + ox, j * step * 4 + oy
                d.line([(x - 14, y), (x + 14, y)], fill=a + (70,), width=2)
                d.line([(x, y - 14), (x, y + 14)], fill=a + (70,), width=2)
        sy = (t * 140) % (H + 200) - 100
        d.line([(0, sy), (W, sy)], fill=a + (40,), width=3)

    def _m_checklist(self, d, t, hit):
        # A compliance checklist down the right edge: boxes drifting up, ticks
        # landing one after another, each tick kicking on the beat it lands.
        a = self.accent
        step, size = 150, 46
        off = (t * 22) % step
        for k in range(-1, H // step + 2):
            y = k * step + step - off
            x = W - 150
            d.rounded_rectangle([x, y, x + size, y + size], radius=8, outline=a + (60,), width=3)
            d.line([(x + size + 24, y + size / 2), (x + size + 24 + 60, y + size / 2)], fill=a + (0,), width=2)
            due = 0.8 + (k * 0.47) % 4.0  # when this row's tick lands
            p = _ease(_phase(t, due, 0.3))
            if p > 0:
                pts = [(x + 10, y + 24), (x + 20, y + 34), (x + 36, y + 12)]
                seg = [pts[0], pts[1]] if p < 0.5 else pts
                if p < 0.5:
                    q = p / 0.5
                    seg = [pts[0], (pts[0][0] + (pts[1][0] - pts[0][0]) * q, pts[0][1] + (pts[1][1] - pts[0][1]) * q)]
                else:
                    q = (p - 0.5) / 0.5
                    seg = [pts[0], pts[1], (pts[1][0] + (pts[2][0] - pts[1][0]) * q, pts[1][1] + (pts[2][1] - pts[1][1]) * q)]
                d.line(seg, fill=a + (170,), width=5, joint="curve")
            # a faint text rule to the left of each box, as a list line
            d.line([(x - 300, y + size / 2), (x - 30, y + size / 2)], fill=a + (22,), width=3)

    def _m_sheets(self, d, t, hit):
        # Document sheets drifting and turning slowly, drawn as outlines with rules.
        a = self.accent
        for k in range(7):
            w, h = 260 + 90 * (k % 3), 340 + 110 * (k % 3)
            cx = _noise(k) * W + math.sin(t * 0.2 + k) * 60
            cy = _noise(k, 1) * H + math.cos(t * 0.17 + k * 2) * 80
            ang = math.radians(-14 + 28 * _noise(k, 2)) + math.sin(t * 0.15 + k) * 0.08
            c, s = math.cos(ang), math.sin(ang)

            def at(x, y):
                return (cx + x * c - y * s, cy + x * s + y * c)

            d.polygon([at(-w / 2, -h / 2), at(w / 2, -h / 2), at(w / 2, h / 2), at(-w / 2, h / 2)], outline=a + (36,), width=3)
            for r in range(3):
                y = -h / 2 + 60 + r * 46
                d.line([at(-w / 2 + 40, y), at(w / 2 - 40 - 50 * (r == 2), y)], fill=a + (26,), width=3)

    def _m_ruler(self, d, t, hit):
        # Three tape measures scrolling at their own speeds, a marker pulsing on the beat.
        a = self.accent
        for y, speed in ((H * 0.12, 90), (H * 0.62, -60), (H * 0.94, 120)):
            d.line([(0, y), (W, y)], fill=a + (40,), width=2)
            for k in range(-2, W // 30 + 6):
                x = (k * 30 + t * speed) % (W + 150) - 75
                major = k % 5 == 0
                d.line([(x, y), (x, y - (40 if major else 18))], fill=a + (100 if major else 55,), width=3 if major else 2)
            mx = W * 0.5
            d.polygon([(mx - 12, y + 30), (mx + 12, y + 30), (mx, y + 8)], fill=a + (int(80 + 140 * hit),))

    # Investors: capital, connections, growth.

    def _m_network(self, d, t, hit):
        # Nodes drifting on slow paths, linked while they are near each other.
        pts = []
        for k in range(20):
            x = _noise(k) * W + math.sin(t * (0.18 + 0.05 * (k % 4)) + k) * 90
            y = _noise(k, 1) * H + math.cos(t * (0.14 + 0.04 * (k % 3)) + k * 1.7) * 110
            pts.append((x, y))
        for i in range(20):
            for j in range(i + 1, 20):
                dist = math.hypot(pts[i][0] - pts[j][0], pts[i][1] - pts[j][1])
                if dist < 460:
                    d.line([pts[i], pts[j]], fill=self.accent + (int(70 * (1 - dist / 460)),), width=2)
        for k, (x, y) in enumerate(pts):
            r = 5 + k % 3 * 2 + 3 * hit * (k % 5 == 0)
            d.ellipse([x - r, y - r, x + r, y + r], fill=self.accent + (120,))

    def _m_curve(self, d, t, hit):
        # A growth curve drawing itself up and to the right, glowing, its area shaded.
        a = self.accent
        p = _ease(_phase(t, 0.3, 3.0))
        n = 60
        pts = []
        for i in range(int(n * p) + 1):
            u = i / n
            x = -20 + (W + 10) * u
            y = H * 0.88 - H * 0.36 * u ** 2.2 + 26 * math.sin(u * 9 + t * 0.9)
            pts.append((x, y))
        if len(pts) > 1:
            d.polygon(pts + [(pts[-1][0], H), (pts[0][0], H)], fill=a + (12,))
            for w, al in ((26, 14), (14, 30), (5, 110)):
                d.line(pts, fill=a + (al,), width=w, joint="curve")
            x, y = pts[-1]
            r = 10 + 6 * hit
            d.ellipse([x - r, y - r, x + r, y + r], fill=a + (200,))

    def _m_orbits(self, d, t, hit):
        # Three tilted orbits around one centre, a body on each with a short trail.
        a = self.accent
        cx, cy = W / 2, H * 0.46
        for i in range(3):
            ra, rb = 420 + 170 * i, 150 + 70 * i
            ang = math.radians(-30 + 25 * i)
            c, s = math.cos(ang), math.sin(ang)

            def at(q):
                return (cx + ra * math.cos(q) * c - rb * math.sin(q) * s, cy + ra * math.cos(q) * s + rb * math.sin(q) * c)

            d.line([at(j * math.pi / 45) for j in range(91)], fill=a + (44,), width=2)
            th = t * (0.9 - 0.2 * i) + i * 2.1
            for k in range(6):
                x, y = at(th - k * 0.09)
                r = (10 + 4 * hit) if k == 0 else max(1.5, 5 - k * 0.7)
                d.ellipse([x - r, y - r, x + r, y + r], fill=a + (170 if k == 0 else 60 - k * 8,))

    def _m_hexes(self, d, t, hit):
        # A honeycomb whose cells light up and dim on their own clocks.
        a, R = self.accent, 64
        dx, dy = R * math.sqrt(3), R * 1.5
        for j in range(int(H / dy) + 2):
            for i in range(int(W / dx) + 2):
                cx, cy = i * dx + (dx / 2 if j % 2 else 0), j * dy
                k = i * 31 + j * 17
                lit = max(0.0, math.sin(t * (0.5 + 0.4 * _noise(k)) + _noise(k, 1) * 6.28))
                al = int(10 + 48 * lit)
                if al < 12:
                    continue
                pts = [(cx + (R - 6) * math.cos(math.pi / 6 + q * math.pi / 3), cy + (R - 6) * math.sin(math.pi / 6 + q * math.pi / 3)) for q in range(6)]
                d.polygon(pts, outline=a + (al,), width=2)

    # Tips: friendly, notebook, ideas.

    def _m_notebook(self, d, t, hit):
        # A ruled page drifting up slowly, a margin rule and punched holes.
        a, step = self.accent, 88
        off = (t * 10) % step
        for y in range(-step, H + step, step):
            d.line([(0, y + step - off), (W, y + step - off)], fill=a + (30,), width=2)
        d.line([(64, 0), (64, H)], fill=a + (55,), width=3)
        for k in range(6):
            y = 220 + k * 300
            d.ellipse([32 - 10, y - 10, 32 + 10, y + 10], outline=a + (45,), width=3)

    def _m_chevrons(self, d, t, hit):
        # Rows of chevrons marching up the frame, brighter as they climb: the
        # "next step" of a tip. Each row scrolls sideways at its own pace.
        a = self.accent
        rows, gap = 9, 210
        off_y = (t * 26) % gap
        for r in range(-1, rows + 1):
            y = H - r * gap + off_y
            f = 1 - min(1, max(0, y / H))
            al = int(14 + 44 * f)
            off_x = (t * (30 + 12 * (r % 3)) * (1 if r % 2 else -1)) % 160
            for k in range(-1, W // 160 + 2):
                x = k * 160 + off_x
                d.line([(x - 26, y + 16), (x, y - 12), (x + 26, y + 16)], fill=a + (al,), width=4, joint="curve")

    def _m_sparks(self, d, t, hit):
        # Rays bursting from a point top right, flaring on the beat, inside two rings.
        a = self.accent
        cx, cy = W * 0.78, H * 0.20
        for k in range(18):
            ang = k * math.pi * 2 / 18 + t * 0.12
            ln = 160 + 120 * _noise(k) + 90 * hit + 40 * math.sin(t * 1.5 + k)
            c, s = math.cos(ang), math.sin(ang)
            for seg, al in ((0.0, 90), (0.45, 50), (0.75, 22)):
                x0, y0 = cx + c * (60 + ln * seg), cy + s * (60 + ln * seg)
                x1, y1 = cx + c * (60 + ln * min(1, seg + 0.3)), cy + s * (60 + ln * min(1, seg + 0.3))
                d.line([(x0, y0), (x1, y1)], fill=a + (al,), width=4)
        for i in range(2):
            r = 40 + 30 * i + 12 * hit
            d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=a + (70 - 30 * i,), width=3)

    def _m_waves(self, d, t, hit):
        a = self.accent
        for i in range(4):
            base = H * (0.62 + 0.08 * i + 0.08 * (i == 3))
            pts = [
                (x, base + (30 + 14 * i) * math.sin(x / (170 + 40 * i) + t * (0.8 - 0.12 * i) + i * 1.1) + 14 * math.sin(x / 61 - t * 1.3))
                for x in range(-20, W + 40, 20)
            ]
            d.line(pts, fill=a + (44 + 10 * i,), width=4, joint="curve")

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
            if self.tag:
                tx = x + bw + 20
                tw = d.textlength(self.tag, font=self.f_kind) + 56
                d.rounded_rectangle([tx, y, tx + tw, y + 78], radius=39, fill=self.ink + (int(255 * fade),))
                text((tx + 28, y + 14), self.tag, self.f_kind, self.bg, fade)

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
