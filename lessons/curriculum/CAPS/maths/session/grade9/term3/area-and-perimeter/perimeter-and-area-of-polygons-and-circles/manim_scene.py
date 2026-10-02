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


def rect(origin, w, h, color=WHITE):
    o = origin
    return Polygon(o, o + RIGHT * w, o + RIGHT * w + UP * h, o + UP * h, color=color, stroke_width=4)


def trap(origin, bottom, top, h, color=WHITE):
    o = origin
    off = (bottom - top) / 2
    return Polygon(o, o + RIGHT * bottom, o + RIGHT * (off + top) + UP * h, o + RIGHT * off + UP * h, color=color, stroke_width=4)


def dashed_height(p, h, color=YELLOW):
    return DashedLine(p, p + UP * h, color=color, stroke_width=3)


def lshape(origin, w, h, cw, ch, color=WHITE):
    """A w-by-h rectangle with a cw-by-ch corner removed at top right."""
    o = origin
    return Polygon(o, o + RIGHT * w, o + RIGHT * w + UP * (h - ch), o + RIGHT * (w - cw) + UP * (h - ch),
                   o + RIGHT * (w - cw) + UP * h, o + UP * h, color=color, stroke_width=4)


class PerimeterAreaSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): polygon formulas
        title = Tex("Perimeter adds the sides; area uses the perpendicular height").scale(0.95).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        r = rect(np.array([-6.4, -2.4, 0]), 2.4, 1.4)
        t = trap(np.array([-3.4, -2.4, 0]), 2.5, 1.5, 1.4)
        self.play(Create(r), Create(t))
        self.play(Create(dashed_height(np.array([-2.9, -2.4, 0]), 1.4)))
        f1 = MathTex(r"P = 2(l + b),\quad A = lb:\quad 12 \times 7 \Rightarrow 38\ \text{cm},\ 84\ \text{cm}^2").scale(0.72).shift(UP * 2.1 + RIGHT * 1.6)
        f2 = MathTex(r"A_{\triangle} = \tfrac{1}{2} b h:\ \tfrac{1}{2}(10)(6) = 30\ \text{cm}^2").scale(0.75).shift(UP * 1.3 + RIGHT * 1.6)
        f3 = MathTex(r"A_{\text{parallelogram}} = bh = 8 \times 5 = 40\ \text{cm}^2").scale(0.75).shift(UP * 0.5 + RIGHT * 1.6)
        f4 = MathTex(r"A_{\text{trapezium}} = \tfrac{1}{2}(a + b)h = \tfrac{1}{2}(6 + 10)(4) = 32\ \text{cm}^2").scale(0.72).shift(DOWN * 0.3 + RIGHT * 1.6)
        f5 = MathTex(r"A_{\text{rhombus/kite}} = \tfrac{1}{2} d_1 d_2 = \tfrac{1}{2}(6)(8) = 24\ \text{cm}^2").scale(0.72).shift(DOWN * 1.1 + RIGHT * 1.6)
        for m in (f1, f2, f3, f4, f5):
            self.play(Write(m))
            self.wait(2.4)
        self.wait(4)

        # --- Band 1 (subtopic_2): circle
        self.next_band(1)
        h1 = Tex("The circle: radius first").scale(1.05).move_to(band_shift(1) + UP * 3.2)
        self.play(Write(h1))
        c = Circle(radius=1.4, color=WHITE, stroke_width=4).move_to(band_shift(1) + LEFT * 5.0 + DOWN * 0.6)
        self.play(Create(c))
        self.play(Create(Line(c.get_center(), c.get_center() + RIGHT * 1.4, color=YELLOW, stroke_width=3)))
        self.play(Write(MathTex("r").scale(0.7).move_to(c.get_center() + RIGHT * 0.7 + UP * 0.3)))
        c1 = MathTex(r"C = 2\pi r,\quad A = \pi r^2").scale(0.9).move_to(band_shift(1) + UP * 2.2 + RIGHT * 2.0)
        c2 = Tex("$r = 7$: $C \\approx 44.0$ cm, $A \\approx 153.9$ cm$^2$").scale(0.75).move_to(band_shift(1) + UP * 1.3 + RIGHT * 2.0)
        c3 = Tex("$d = 20$: $r = 10$, $A = \\pi(100) \\approx 314.2$; NOT $\\pi(400)$").scale(0.72).move_to(band_shift(1) + UP * 0.4 + RIGHT * 2.0)
        c4 = Tex("Semicircle $r = 10$: $A \\approx 157.1$; $P = 31.42 + 20 \\approx 51.4$").scale(0.72).move_to(band_shift(1) + DOWN * 0.5 + RIGHT * 2.0)
        c5 = Tex("Ring 10 and 6: $\\pi(100) - \\pi(36) \\approx 201.1$. Pond $50.27$: $r^2 = 16$, $r = 4$.").scale(0.68).move_to(band_shift(1) + DOWN * 1.4 + RIGHT * 2.0)
        for m in (c1, c2, c3, c4, c5):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(c3, color=YELLOW)))
        self.wait(3)

        # --- Band 2 (subtopic_3): units
        self.next_band(2)
        h2 = Tex("Area units: the factor squared").scale(1.05).move_to(band_shift(2) + UP * 3.2)
        self.play(Write(h2))
        big = rect(np.array([-6.4, -2.2, 0]) + band_shift(2), 2.4, 2.4)
        self.play(Create(big))
        for i in range(1, 4):
            self.play(Create(Line(big.get_vertices()[0] + RIGHT * 0.6 * i, big.get_vertices()[3] + RIGHT * 0.6 * i, color=GREY, stroke_width=1)),
                      Create(Line(big.get_vertices()[0] + UP * 0.6 * i, big.get_vertices()[1] + UP * 0.6 * i, color=GREY, stroke_width=1)), run_time=0.3)
        u1 = MathTex(r"1\ \text{m} = 100\ \text{cm} \Rightarrow 1\ \text{m}^2 = 100 \times 100 = 10\,000\ \text{cm}^2").scale(0.75).move_to(band_shift(2) + UP * 2.1 + RIGHT * 1.8)
        u2 = MathTex(r"1\ \text{cm}^2 = 100\ \text{mm}^2,\quad 1\ \text{ha} = 10\,000\ \text{m}^2,\quad 1\ \text{km}^2 = 10^6\ \text{m}^2").scale(0.7).move_to(band_shift(2) + UP * 1.2 + RIGHT * 1.8)
        u3 = Tex("Floor $2.5 \\times 1.6 = 4$ m$^2 = 40\\,000$ cm$^2$. Field $250 \\times 400 = 10$ ha.").scale(0.7).move_to(band_shift(2) + UP * 0.3 + RIGHT * 1.8)
        u4 = Tex("Tiles 300 mm $= 0.3$ m, $0.09$ m$^2$ each; floor $13.5$ m$^2$: $13.5 \\div 0.09 = 150$.").scale(0.68).move_to(band_shift(2) + DOWN * 0.6 + RIGHT * 1.8)
        u5 = Tex("Carpet R145/m$^2$, room $5 \\times 3.6 = 18$ m$^2$: R2 610.").scale(0.72).move_to(band_shift(2) + DOWN * 1.5 + RIGHT * 1.8)
        for m in (u1, u2, u3, u4, u5):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(u1, color=YELLOW)))
        self.wait(3)

        # --- Band 3 (subtopic_4): composite
        self.next_band(3)
        h3 = Tex("Composite shapes: split, name, combine").scale(1.05).move_to(band_shift(3) + UP * 3.2)
        self.play(Write(h3))
        base = np.array([-6.6, -1.8, 0]) + band_shift(3)
        rr = rect(base, 3.0, 1.8)
        self.play(Create(rr))
        semi = Arc(radius=0.9, start_angle=-PI / 2, angle=PI, color=WHITE, stroke_width=4).move_arc_center_to(base + RIGHT * 3.0 + UP * 0.9)
        self.play(Create(semi))
        self.play(Create(DashedLine(base + RIGHT * 3.0, base + RIGHT * 3.0 + UP * 1.8, color=GREY, stroke_width=2)))
        p1 = MathTex(r"A = 10 \times 6 + \tfrac{1}{2}\pi(3)^2 = 60 + 14.14 \approx 74.1\ \text{cm}^2").scale(0.75).move_to(band_shift(3) + UP * 2.1 + RIGHT * 2.0)
        p2 = MathTex(r"P = 10 + 6 + 10 + \tfrac{1}{2}(2\pi \cdot 3) = 26 + 9.42 \approx 35.4\ \text{cm}").scale(0.75).move_to(band_shift(3) + UP * 1.2 + RIGHT * 2.0)
        p3 = Tex("The joined 6 cm side is inside: not perimeter.").scale(0.72).move_to(band_shift(3) + UP * 0.3 + RIGHT * 2.0)
        ls = lshape(np.array([-6.6, -4.0, 0]) + band_shift(3) + UP * 0.6, 3.0, 2.0, 1.0, 1.25)
        p4 = Tex("L-shape from $12 \\times 8$ minus $4 \\times 5$: $A = 76$ cm$^2$, $P$ still 40 cm.").scale(0.7).move_to(band_shift(3) + DOWN * 0.7 + RIGHT * 2.0)
        p5 = Tex("Track: $200 + 2\\pi(31.83) \\approx 400$ m.").scale(0.72).move_to(band_shift(3) + DOWN * 1.6 + RIGHT * 2.0)
        for m in (p1, p2, p3, p4, p5):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(p4, color=YELLOW)))
        self.wait(3)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        h4 = Tex("Error museum").scale(1.05).move_to(band_shift(4) + UP * 3.2)
        self.play(Write(h4))
        e1 = MathTex(r"A = \pi d^2").scale(0.9).move_to(band_shift(4) + UP * 1.8)
        e2 = MathTex(r"1\ \text{m}^2 = 100\ \text{cm}^2").scale(0.9).move_to(band_shift(4) + UP * 0.6)
        e3 = Tex("Semicircle perimeter $= \\tfrac{1}{2}(2\\pi r)$ only").scale(0.8).move_to(band_shift(4) + DOWN * 0.6)
        for m in (e1, e2, e3):
            self.play(Write(m))
            self.wait(1.5)
            self.play(Create(strike(m)))
            self.wait(1.5)
        fix = Tex("Radius first, factor squared, add the diameter, square the unit.").scale(0.75).move_to(band_shift(4) + DOWN * 2.2)
        self.play(Write(fix))
        self.play(Create(SurroundingRectangle(fix, color=GREEN)))
        self.wait(5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): fence and carpet
        self.next_band(5)
        h5 = Tex("Fence and carpet").scale(1.05).move_to(band_shift(5) + UP * 3.2)
        self.play(Write(h5))
        g = rect(np.array([-6.2, -1.6, 0]) + band_shift(5), 3.6, 2.1, color=GREEN)
        self.play(Create(g))
        for i in range(1, 6):
            self.play(Create(Line(g.get_vertices()[0] + RIGHT * 0.6 * i, g.get_vertices()[3] + RIGHT * 0.6 * i, color=GREY, stroke_width=1)), run_time=0.2)
        for j in range(1, 4):
            self.play(Create(Line(g.get_vertices()[0] + UP * 0.6 * j, g.get_vertices()[1] + UP * 0.6 * j, color=GREY, stroke_width=1)), run_time=0.2)
        s1 = Tex("Fence: add the sides, metres. Carpet: formula, square metres.").scale(0.72).move_to(band_shift(5) + UP * 2.0 + RIGHT * 2.2)
        s2 = Tex("$12 \\times 7$: fence 38 cm, carpet 84 cm$^2$.").scale(0.75).move_to(band_shift(5) + UP * 1.1 + RIGHT * 2.2)
        s3 = Tex("Triangle: half of base times straight-up height. Never the slope.").scale(0.7).move_to(band_shift(5) + UP * 0.2 + RIGHT * 2.2)
        s4 = Tex("Trapezium: average of top and bottom, times height: $8 \\times 4 = 32$.").scale(0.7).move_to(band_shift(5) + DOWN * 0.7 + RIGHT * 2.2)
        for m in (s1, s2, s3, s4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(s3, color=YELLOW)))
        self.wait(3)

        # --- Band 6 (subtopic_6): pizza
        self.next_band(6)
        h6 = Tex("Pizza and pie").scale(1.05).move_to(band_shift(6) + UP * 3.2)
        self.play(Write(h6))
        bigp = Circle(radius=1.6, color=ORANGE, stroke_width=4).move_to(band_shift(6) + LEFT * 4.6 + DOWN * 0.4)
        smallp = Circle(radius=0.8, color=ORANGE, stroke_width=4).move_to(band_shift(6) + LEFT * 1.8 + DOWN * 0.4)
        self.play(Create(bigp), Create(smallp))
        z1 = Tex("30 cm pizza: $\\pi(15)^2 \\approx 707$. 15 cm pizza: $\\pi(7.5)^2 \\approx 177$.").scale(0.7).move_to(band_shift(6) + UP * 2.0 + RIGHT * 2.0)
        z2 = Tex("Big one is FOUR small ones: doubling the radius squares to 4.").scale(0.7).move_to(band_shift(6) + UP * 1.1 + RIGHT * 2.0)
        z3 = Tex("Half a pie: half the carpet, but the fence has crust AND the straight cut.").scale(0.68).move_to(band_shift(6) + UP * 0.2 + RIGHT * 2.0)
        z4 = Tex("Ring: big carpet minus small carpet, never radii first.").scale(0.72).move_to(band_shift(6) + DOWN * 0.7 + RIGHT * 2.0)
        for m in (z1, z2, z3, z4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(z2, color=YELLOW)))
        self.wait(3)

        # --- Band 7 (subtopic_7): tiles
        self.next_band(7)
        h7 = Tex("A floor covered in tiles").scale(1.05).move_to(band_shift(7) + UP * 3.2)
        self.play(Write(h7))
        fl = rect(np.array([-6.4, -2.0, 0]) + band_shift(7), 4.5 * 0.7, 3.0 * 0.7)
        self.play(Create(fl))
        for i in range(1, 15):
            self.play(Create(Line(fl.get_vertices()[0] + RIGHT * 0.21 * i, fl.get_vertices()[3] + RIGHT * 0.21 * i, color=GREY, stroke_width=1)), run_time=0.08)
        for j in range(1, 10):
            self.play(Create(Line(fl.get_vertices()[0] + UP * 0.21 * j, fl.get_vertices()[1] + UP * 0.21 * j, color=GREY, stroke_width=1)), run_time=0.08)
        y1 = Tex("Length jump 100; area jump $100^2 = 10\\,000$. Hectare: $100 \\times 100$ m.").scale(0.7).move_to(band_shift(7) + UP * 2.0 + RIGHT * 2.2)
        y2 = Tex("Tile 300 mm $= 0.3$ m $= 0.09$ m$^2$; $13.5 \\div 0.09 = 150$, or $15 \\times 10$.").scale(0.68).move_to(band_shift(7) + UP * 1.1 + RIGHT * 2.2)
        y3 = Tex("Carpet: $18 \\times$ R145 $=$ R2 610.").scale(0.75).move_to(band_shift(7) + UP * 0.2 + RIGHT * 2.2)
        y4 = Tex("L-shape: less carpet, same fence of 40.").scale(0.75).move_to(band_shift(7) + DOWN * 0.7 + RIGHT * 2.2)
        y5 = Tex("Fence or carpet, radius first, jump squared.").scale(0.8).move_to(band_shift(7) + DOWN * 2.3 + RIGHT * 1.0)
        for m in (y1, y2, y3, y4, y5):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(y5, color=YELLOW)))
        self.wait(6)
