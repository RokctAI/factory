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
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def box(origin, l=2.0, h=1.0, d=0.6, color=WHITE):
    """Rectangular prism wireframe: front face l by h, depth drawn at 45 degrees."""
    off = np.array([d, d, 0])
    f = [origin, origin + RIGHT * l, origin + RIGHT * l + UP * h, origin + UP * h]
    b = [p + off for p in f]
    g = VGroup()
    for i in range(4):
        g.add(Line(f[i], f[(i + 1) % 4], color=color))
        g.add(Line(b[i], b[(i + 1) % 4], color=color))
        g.add(Line(f[i], b[i], color=color))
    return g


def cylinder(base_centre, r=0.9, h=1.8, tilt=0.35, color=WHITE):
    top = base_centre + UP * h
    return VGroup(
        Ellipse(width=2 * r, height=2 * r * tilt, color=color).move_to(top),
        Ellipse(width=2 * r, height=2 * r * tilt, color=color).move_to(base_centre),
        Line(base_centre + LEFT * r, top + LEFT * r, color=color),
        Line(base_centre + RIGHT * r, top + RIGHT * r, color=color),
    )


class SurfaceAreaVolumeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): surface area of prisms
        title = Tex("Surface area: add every face").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        bx = box(np.array([-6.3, -0.4, 0]), l=2.4, h=1.2, d=0.7)
        self.play(Create(bx), run_time=2)
        bx_lab = Tex("4 by 3 by 2").scale(0.6).move_to(np.array([-5.1, -0.9, 0]))
        self.play(Write(bx_lab))
        rows = [
            r"\text{Cube, side 5: } 6 \times 25 = 150 \text{ cm}^2",
            r"\text{Box: } 2(12 + 8 + 6) = 52 \text{ cm}^2",
            r"\text{3, 4, 5 prism, length 10: } 2 \times 6 + 12 \times 10 = 132 \text{ cm}^2",
            r"\text{Prism: } 2 \times \text{end} + \text{perimeter} \times \text{length}",
            r"\text{Open shoebox: } 540 + 720 + 432 = 1692 \text{ cm}^2",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.7).shift(RIGHT * 1.9 + UP * (1.8 - 0.8 * i))
            self.play(Write(m))
            self.wait(2.1)
        self.wait(2)

        # --- Band 1 (subtopic_2): surface area of cylinders
        self.next_band(1)
        b1_title = Tex("Cylinder: two circles and a rectangle").scale(1.1).shift(band_shift(1) + UP * 3.0)
        self.play(Write(b1_title))
        self.wait(1.5)
        net_rect = Rectangle(width=3.6, height=1.6, color=WHITE).move_to(band_shift(1) + LEFT * 4.3 + UP * 0.3)
        c_top = Circle(radius=0.57, color=GREEN).next_to(net_rect, UP, buff=0)
        c_bot = Circle(radius=0.57, color=GREEN).next_to(net_rect, DOWN, buff=0)
        self.play(Create(net_rect), Create(c_top), Create(c_bot), run_time=2)
        rl = MathTex(r"2\pi r").scale(0.6).next_to(net_rect, DOWN, buff=1.25)
        rh = MathTex("h").scale(0.6).next_to(net_rect, LEFT, buff=0.1)
        self.play(Write(rl), Write(rh))
        cy = [
            r"SA = 2\pi r^2 + 2\pi r h",
            r"r = 3.5,\ h = 10: \ 76.97 + 219.91 \approx 296.88 \text{ cm}^2",
            r"\text{Label only: } 2\pi r h \approx 219.91 \text{ cm}^2",
            r"\text{No lid: } \pi r^2 + 2\pi r h \approx 258.40 \text{ cm}^2",
            r"\text{Tank } r = 1,\ h = 2,\ \text{no base: } 5\pi \approx 15.71 \text{ m}^2",
        ]
        for i, r in enumerate(cy):
            m = MathTex(r).scale(0.68).shift(band_shift(1) + RIGHT * 2.3 + UP * (1.8 - 0.8 * i))
            self.play(Write(m))
            self.wait(2.1)
        self.wait(2)

        # --- Band 2 (subtopic_3): volume and capacity
        self.next_band(2)
        b2_title = Tex("Volume = base area $\\times$ height").scale(1.15).shift(band_shift(2) + UP * 3.0)
        self.play(Write(b2_title))
        self.wait(1.5)
        tin = cylinder(band_shift(2) + LEFT * 5.2 + DOWN * 1.6, r=0.9, h=2.4)
        self.play(Create(tin), run_time=2)
        layers = VGroup(*[Ellipse(width=1.8, height=0.63, color=BLUE, stroke_width=2).move_to(band_shift(2) + LEFT * 5.2 + DOWN * 1.6 + UP * 0.48 * k) for k in range(1, 5)])
        self.play(Create(layers), run_time=1.5)
        vol = [
            r"\text{Cube: } 125 \text{ cm}^3 \qquad \text{Box: } 24 \text{ cm}^3 \qquad \text{Prism: } 6 \times 10 = 60 \text{ cm}^3",
            r"\text{Tin: } \pi \times 3.5^2 \times 10 \approx 384.85 \text{ cm}^3 \approx 385 \text{ ml}",
            r"1 \text{ cm}^3 = 1 \text{ ml} \qquad 1000 \text{ cm}^3 = 1 \ell \qquad 1 \text{ m}^3 = 1000 \ell",
            r"\text{Fish tank: } 60 \times 30 \times 40 = 72\,000 \text{ cm}^3 = 72 \ell",
            r"\text{Rain tank: } \pi \times 0.65^2 \times 1.6 \approx 2.12 \text{ m}^3 \approx 2120 \ell",
        ]
        for i, r in enumerate(vol):
            m = MathTex(r).scale(0.62).shift(band_shift(2) + RIGHT * 1.6 + UP * (1.8 - 0.8 * i))
            self.play(Write(m))
            self.wait(2.2)
        self.wait(2)

        # --- Band 3 (subtopic_4): unit conversions
        self.next_band(3)
        b3_title = Tex("Converting SI units").scale(1.2).shift(band_shift(3) + UP * 3.0)
        self.play(Write(b3_title))
        self.wait(1.5)
        sq = Square(side_length=2.0, color=WHITE).move_to(band_shift(3) + LEFT * 5.0 + UP * 0.2)
        grid = VGroup(*[Line(sq.get_corner(DL) + RIGHT * 0.2 * k, sq.get_corner(UL) + RIGHT * 0.2 * k, color=GREY, stroke_width=1) for k in range(1, 10)],
                      *[Line(sq.get_corner(DL) + UP * 0.2 * k, sq.get_corner(DR) + UP * 0.2 * k, color=GREY, stroke_width=1) for k in range(1, 10)])
        self.play(Create(sq), Create(grid), run_time=2)
        sq_lab = Tex("100 by 100 small squares").scale(0.6).next_to(sq, DOWN, buff=0.2)
        self.play(Write(sq_lab))
        conv = [
            r"1 \text{ m}^2 = 100 \times 100 = 10\,000 \text{ cm}^2",
            r"1 \text{ m}^3 = 100 \times 100 \times 100 = 1\,000\,000 \text{ cm}^3",
            r"\text{Crate: } 120 \times 80 \times 50 = 480\,000 \text{ cm}^3 = 480 \ell",
            r"\text{Pool: } 10 \times 5 \times 1.5 = 75 \text{ m}^3 = 75\,000 \ell",
        ]
        for i, r in enumerate(conv):
            m = MathTex(r).scale(0.72).shift(band_shift(3) + RIGHT * 1.9 + UP * (1.6 - 0.9 * i))
            self.play(Write(m))
            self.wait(2.4)
        tip = Tex("Convert lengths first, then calculate").scale(0.8).shift(band_shift(3) + RIGHT * 1.9 + DOWN * 2.2)
        self.play(Write(tip))
        self.play(Create(SurroundingRectangle(tip, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        e1 = Tex("296.88 cm$^2$ divided by 100 gives m$^2$").scale(0.8).shift(band_shift(4) + UP * 1.5)
        e2 = Tex("1.2 times 80 times 50 (metres with centimetres)").scale(0.8).shift(band_shift(4) + UP * 0.6)
        e3 = Tex("Tin 7 cm across: r = 7 in the formula").scale(0.8).shift(band_shift(4) + DOWN * 0.3)
        e4 = Tex("Volume 24 cm$^2$; surface area 52 cm$^3$").scale(0.8).shift(band_shift(4) + DOWN * 1.2)
        e5 = Tex("A lid counted on an open box").scale(0.8).shift(band_shift(4) + DOWN * 2.1)
        for m in (e1, e2, e3, e4, e5):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.6)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): wrap it
        self.next_band(5)
        b5_title = Tex("Wrap it: add every face").scale(1.2).shift(band_shift(5) + UP * 2.8)
        self.play(Write(b5_title))
        self.wait(2)
        w1 = Tex("Box: pairs 12, 8, 6; add and double: 52").scale(0.85).shift(band_shift(5) + UP * 1.4)
        w2 = Tex("Tent: two triangles 12, strip 120: 132").scale(0.85).shift(band_shift(5) + UP * 0.5)
        w3 = Tex("Tin: two circles and a label, about 296.88").scale(0.85).shift(band_shift(5) + DOWN * 0.4)
        w4 = Tex("Radius, not width. Lid or no lid?").scale(0.85).shift(band_shift(5) + DOWN * 1.3)
        for m in (w1, w2, w3, w4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(w4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): floor times height
        self.next_band(6)
        b6_title = Tex("Floor times height").scale(1.2).shift(band_shift(6) + UP * 2.8)
        self.play(Write(b6_title))
        self.wait(2)
        stack = VGroup(*[Rectangle(width=2.4, height=0.35, color=BLUE).move_to(band_shift(6) + LEFT * 4.8 + DOWN * 1.6 + UP * 0.38 * k) for k in range(6)])
        self.play(Create(stack), run_time=2)
        f1 = Tex("Same layer stacked up: floor area times height").scale(0.8).shift(band_shift(6) + RIGHT * 1.6 + UP * 1.3)
        f2 = Tex("Box 24, prism 60, tin about 385 cubic centimetres").scale(0.8).shift(band_shift(6) + RIGHT * 1.6 + UP * 0.4)
        f3 = Tex("Wrapping: little 2. Space inside: little 3.").scale(0.8).shift(band_shift(6) + RIGHT * 1.6 + DOWN * 0.5)
        f4 = Tex("1 cubic centimetre holds 1 millilitre").scale(0.8).shift(band_shift(6) + RIGHT * 1.6 + DOWN * 1.4)
        for m in (f1, f2, f3, f4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(f1, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): how many litres fit
        self.next_band(7)
        b7_title = Tex("How many litres fit").scale(1.2).shift(band_shift(7) + UP * 2.8)
        self.play(Write(b7_title))
        self.wait(2)
        h1 = Tex("Fish tank: 72 000 cubic centimetres, 72 litres").scale(0.8).shift(band_shift(7) + UP * 1.5)
        h2 = Tex("Rain tank: about 2.12 cubic metres, about 2 120 litres").scale(0.8).shift(band_shift(7) + UP * 0.6)
        h3 = Tex("Square metre: 10 000 cm$^2$. Cubic metre: a million cm$^3$.").scale(0.8).shift(band_shift(7) + DOWN * 0.3)
        h4 = Tex("Crate: 120 by 80 by 50, then multiply: 480 litres").scale(0.8).shift(band_shift(7) + DOWN * 1.2)
        for m in (h1, h2, h3, h4):
            self.play(Write(m))
            self.wait(2.2)
        h5 = Tex("Wrap it. Fill it. Convert it.").scale(0.95).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(h5))
        self.play(Create(SurroundingRectangle(h5, color=YELLOW)))
        self.wait(4)
