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

from manim import *

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Rectangles and triangles are drawn from
# plain line segments. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json
# (220/230/230/230/190/190/180 of 1470 s).

BAND = config.frame_height
U = 0.4  # one centimetre of the figures in scene units


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def rect(corner, w, h, color=YELLOW):
    """Rectangle w by h (in cm) with bottom-left corner at the scene point corner."""
    a = corner
    b = corner + RIGHT * w * U
    c = b + UP * h * U
    d = corner + UP * h * U
    return VGroup(*[Line(p, q, color=color, stroke_width=3) for p, q in ((a, b), (b, c), (c, d), (d, a))])


def unit_grid(corner, w, h, cell, color=GREY):
    """Faint lines splitting a w by h rectangle into cells of size cell."""
    g = VGroup()
    x = cell
    while x < w:
        g.add(Line(corner + RIGHT * x * U, corner + RIGHT * x * U + UP * h * U, color=color, stroke_width=1))
        x += cell
    y = cell
    while y < h:
        g.add(Line(corner + UP * y * U, corner + UP * y * U + RIGHT * w * U, color=color, stroke_width=1))
        y += cell
    return g


class EnlargementSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def notes(self, k, lines, x=2.6, top=1.6, step=0.75, scale=0.7, wait=2.4):
        out = []
        for i, n in enumerate(lines):
            m = Tex(n).scale(scale).shift(band_shift(k) + RIGHT * x + UP * (top - step * i))
            self.play(Write(m))
            self.wait(wait)
            out.append(m)
        return out

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): similar rectangles, scale factor
        h0 = Tex("Enlargement: every length times $k$").scale(1.0).shift(band_shift(0) + UP * 3.1)
        self.play(Write(h0))
        c0 = band_shift(0) + LEFT * 6 + DOWN * 2
        self.play(Create(rect(c0, 4, 3)))
        self.play(Create(rect(c0 + RIGHT * 2.2, 8, 6, color=BLUE)), run_time=1.5)
        self.wait(1.5)
        n0 = self.notes(0, ["4 by 3 becomes 8 by 6: $k = 2$",
                            "$k > 1$ enlarges; $0 < k < 1$ reduces",
                            "$k$ = image length $\\div$ original length",
                            "Angles unchanged: similar figures",
                            "Adding 2 gives 6 by 5: not similar"])
        self.play(Create(strike(n0[-1])))
        self.wait(2)

        # --- Band 1 (subtopic_2): perimeter times k
        self.next_band(1)
        h1 = Tex("Perimeter is multiplied by $k$").scale(1.0).shift(band_shift(1) + UP * 3.1)
        self.play(Write(h1))
        self.notes(1, ["4 by 3: perimeter 14", "8 by 6: perimeter 28, which is $2 \\times 14$",
                       "Sides 3, 4, 5 times 3: 9, 12, 15", "Perimeter 12 becomes 36",
                       "Perimeters 20 and 50: $k = 2.5$"], x=0, top=1.9)
        r1 = MathTex(r"ka + kb + kc = k(a + b + c)").scale(0.9).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(r1))
        self.play(Create(SurroundingRectangle(r1, color=YELLOW)))
        self.wait(3)

        # --- Band 2 (subtopic_3): area times k squared
        self.next_band(2)
        h2 = Tex("Area is multiplied by $k^2$").scale(1.0).shift(band_shift(2) + UP * 3.1)
        self.play(Write(h2))
        c2 = band_shift(2) + LEFT * 6 + DOWN * 2
        big = rect(c2, 8, 6, color=BLUE)
        self.play(Create(big))
        self.play(Create(unit_grid(c2, 8, 6, 4, color=YELLOW)), run_time=1.0)
        self.play(Create(unit_grid(c2, 8, 6, 3, color=YELLOW)), run_time=1.0)
        self.wait(1.5)
        self.notes(2, ["Area 12 becomes 48: four copies fit",
                       "$k l \\times k b = k^2 \\, l b$",
                       "Triangle area 6 times 9 is 54",
                       "Areas 20 and 180: $k^2 = 9$, $k = 3$",
                       "Map 1 : 50 000: 1 cm$^2$ is 0.25 km$^2$"])

        # --- Band 3 (subtopic_4): proportion problems
        self.next_band(3)
        h3 = Tex("Length or area?").scale(1.1).shift(band_shift(3) + UP * 3.1)
        self.play(Write(h3))
        self.notes(3, ["Mural 30 by 20 cm on a 6 m by 4 m wall: $k = 20$",
                       "Border tape: 100 cm becomes 20 m",
                       "Paint: $20^2 = 400$ times, 10 ml becomes 4 litres",
                       "Pizza 20 cm to 30 cm: area times 2.25",
                       "Plan at $\\frac{1}{100}$: 20 m$^2$ room is 20 cm$^2$"], x=0, top=1.9)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        errs = ["Double the sides: area 12 becomes 24",
                "Perimeter times $k^2$",
                "Enlarge by adding 2 to each side",
                "Areas times 9, so sides times 9",
                "Reduce by $\\frac{1}{3}$: area divided by 3"]
        for i, e in enumerate(errs):
            m = Tex(e).scale(0.8).shift(band_shift(4) + UP * (1.5 - 0.9 * i))
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.6)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): same shape, different size
        self.next_band(5)
        b5 = Tex("Same shape, bigger or smaller").scale(1.2).shift(band_shift(5) + UP * 2.8)
        self.play(Write(b5))
        s = self.notes(5, ["Multiply every side by $k$", "6, 8, 10 times $\\frac{1}{2}$ gives 3, 4, 5",
                           "Find $k$: new side $\\div$ old side", "Adding is not enlarging"], x=0, top=1.4, scale=0.85)
        self.play(Create(SurroundingRectangle(s[0], color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): fence times k
        self.next_band(6)
        b6 = Tex("Fence times $k$").scale(1.2).shift(band_shift(6) + UP * 2.8)
        self.play(Write(b6))
        s = self.notes(6, ["Fence 14 around 4 by 3; fence 28 around 8 by 6",
                           "Bed 12 by 9 m: 42 m; plan at $\\frac{1}{3}$: 14",
                           "Fence 20 to 50: $k = 2.5$",
                           "Edging, skirting, piping: times $k$"], x=0, top=1.4, scale=0.85)
        self.play(Create(SurroundingRectangle(s[0], color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): carpet times k squared
        self.next_band(7)
        b7 = Tex("Carpet times $k^2$").scale(1.2).shift(band_shift(7) + UP * 2.8)
        self.play(Write(b7))
        self.notes(7, ["Carpet 12 becomes 48: four times", "Half size: a quarter of the carpet",
                       "Carpet times 9: sides times 3"], x=0, top=1.5, scale=0.85, wait=2.2)
        t5 = Tex("Fence times $k$; carpet times $k^2$.").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(t5))
        self.play(Create(SurroundingRectangle(t5, color=YELLOW)))
        self.wait(4)
