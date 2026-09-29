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
points the viewer at the description for the link. The domain never
appears in the video; the brand name does.

The palette and background motif rotate by date, so consecutive days do
not look like one template (Meta limits reach and monetisation on
repetitive, templated content).
"""

import math
import re
import subprocess
from pathlib import Path

W, H, FPS = 1080, 1920, 30
BRAND = "ROKCT"
CLOSE_LINE = "Link in the description"

# (background, glow, accent, text) - rotated by day.
PALETTES = [
    ((12, 12, 16), (255, 196, 0), (255, 196, 0), (245, 245, 245)),
    ((8, 16, 28), (0, 170, 255), (90, 210, 255), (240, 246, 252)),
    ((20, 10, 24), (255, 70, 140), (255, 120, 170), (250, 242, 246)),
    ((6, 20, 14), (0, 220, 130), (80, 240, 170), (238, 250, 244)),
    ((24, 14, 6), (255, 120, 20), (255, 160, 70), (252, 246, 240)),
]


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


_NUMBER = re.compile(r"\d[\d,\s]*(?:\.\d+)?")


def counting(text, progress):
    """The headline with its first number counted up to `progress` of its
    value, formatted the way the card writes it. At progress 1 the text is
    exactly the card's text - the count only ever lands on the real figure."""
    m = _NUMBER.search(text)
    if not m or progress >= 1:
        return text
    raw = m.group(0).rstrip()
    digits = re.sub(r"[,\s]", "", raw)
    try:
        value = float(digits)
    except ValueError:
        return text
    now = value * _ease(progress)
    decimals = len(digits.split(".")[1]) if "." in digits else 0
    shown = f"{now:,.{decimals}f}" if "," in raw else f"{now:.{decimals}f}"
    return text[: m.start()] + shown + text[m.start() + len(raw):]


def _glow(color, radius):
    from PIL import Image, ImageDraw, ImageFilter

    size = radius * 4
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    ImageDraw.Draw(img).ellipse(
        [radius, radius, size - radius, size - radius], fill=color + (90,)
    )
    return img.filter(ImageFilter.GaussianBlur(radius // 2))


class Scene:
    def __init__(self, opp, headline, days_left, seed, duration):
        from PIL import Image

        self.opp = opp
        self.headline = headline
        self.days_left = days_left
        self.duration = duration
        self.bg, glow, self.accent, self.ink = PALETTES[seed % len(PALETTES)]
        self.motif = seed % 3
        self.glows = [_glow(glow, 260), _glow(self.accent, 200)]
        self.base = Image.new("RGB", (W, H), self.bg)
        self.f_brand = _font(54)
        self.f_brand_big = _font(150)
        self.f_kind = _font(42)
        self.f_head = _font(96)
        self.f_title = _font(48, bold=False)
        self.f_date = _font(54)
        self.f_days = _font(170)
        self.f_small = _font(44, bold=False)
        self.f_cta = _font(58)

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
        end_start = self.duration - 3.2

        def text(xy, s, font, fill, alpha=1.0):
            # ImageDraw ignores fill alpha for text, so fades go through a mask.
            alpha = max(0.0, min(1.0, alpha))
            if alpha < 0.01 or not s:
                return
            left, top, right, bottom = d.textbbox((0, 0), s, font=font)
            mask = Image.new("L", (right - left, bottom - top), 0)
            ImageDraw.Draw(mask).text((-left, -top), s, font=font, fill=int(255 * alpha))
            img.paste(fill, (int(xy[0] + left), int(xy[1] + top)), mask)

        # Brand, top-left, drops in.
        p = _back(_phase(t, 0.0, 0.6))
        if t < end_start:
            text((margin, 110 - 80 * (1 - p)), BRAND, self.f_brand, self.accent, p)

        if t < end_start:
            fade = 1 - _ease(_phase(t, end_start - 0.5, 0.5))

            # Kind badge slides in from the left.
            p = _ease(_phase(t, 0.3, 0.6))
            label = self.opp["kind"].upper()
            bw = d.textlength(label, font=self.f_kind) + 56
            x = margin - (bw + margin) * (1 - p)
            y = 440
            d.rounded_rectangle([x, y, x + bw, y + 78], radius=39, fill=self.accent + (int(255 * fade),))
            text((x + 28, y + 14), label, self.f_kind, self.bg, fade)

            # Headline figure scales in and counts up to the exact value.
            p = _phase(t, 0.8, 2.0)
            shown = counting(self.headline, p)
            lines = _wrap(d, self.headline, self.f_head, inner, 3)
            live = _wrap(d, shown, self.f_head, inner, 3) if p < 1 else lines
            y = 580
            pop = _back(_phase(t, 0.8, 0.5))
            for line in live:
                text((margin, y + 40 * (1 - pop)), line, self.f_head, self.ink, min(pop, fade))
                y += 112

            # Title rises line by line.
            y += 30
            for i, line in enumerate(_wrap(d, self.opp["title"], self.f_title, inner, 4)):
                p = _ease(_phase(t, 2.6 + i * 0.25, 0.6))
                text((margin, y + 50 * (1 - p)), line, self.f_title, self.ink, min(p * 0.8, fade))
                y += 64

            # Deadline block: date + live days-left counter.
            y = max(y + 90, 1320)
            p = _back(_phase(t, 4.6, 0.6))
            if p > 0.01:
                w = (W - 2 * margin) * min(1, p)
                d.rounded_rectangle(
                    [margin, y, margin + w, y + 330], radius=34, fill=(255, 255, 255, int(22 * fade))
                )
                d.rectangle([margin, y, margin + 12, y + 330], fill=self.accent + (int(255 * fade),))
                count = int(round(self.days_left * _ease(_phase(t, 4.9, 1.4))))
                pulse = 1 + 0.04 * math.sin(max(0, t - 6.3) * 6) * (t > 6.3)
                days_font = _font(int(170 * pulse))
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
            p = _ease(_phase(t, 7.2, 0.7))
            who = self.opp.get("who") or ""
            y2 = y + 400
            for line in _wrap(d, who, self.f_small, inner, 2):
                text((margin, y2 + 30 * (1 - p)), line, self.f_small, self.ink, min(p * 0.85, fade))
                y2 += 58
        else:
            # Close: big brand + pointer to the description.
            p = _back(_phase(t, end_start, 0.7))
            bw = d.textlength(BRAND, font=self.f_brand_big)
            text(((W - bw) / 2, H * 0.36 + 60 * (1 - p)), BRAND, self.f_brand_big, self.accent, p)
            p2 = _ease(_phase(t, end_start + 0.5, 0.6))
            cw = d.textlength(CLOSE_LINE, font=self.f_cta)
            text(((W - cw) / 2, H * 0.52), CLOSE_LINE, self.f_cta, self.ink, p2)
            bounce = abs(math.sin((t - end_start) * 5)) * 30
            ax, ay = W / 2, H * 0.60 + bounce
            d.polygon(
                [(ax - 40, ay), (ax + 40, ay), (ax, ay + 50)],
                fill=self.accent + (int(255 * p2),),
            )

        # Progress bar along the foot.
        d.rectangle([0, H - 14, W * t / self.duration, H], fill=self.accent + (220,))
        return img


def render_motion(opp, headline, days_left, seed, duration, out: Path):
    """Write the animated clip to `out` (mp4, no audio)."""
    scene = Scene(opp, headline, days_left, seed, duration)
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
