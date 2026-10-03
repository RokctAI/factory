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


def split_lines(origin, w, h, color=YELLOW):
    """One vertical and one horizontal line cutting a w-by-h rectangle into four."""
    o = origin
    return VGroup(Line(o + RIGHT * w / 2, o + RIGHT * w / 2 + UP * h, color=color, stroke_width=3),
                  Line(o + UP * h / 2, o + RIGHT * w + UP * h / 2, color=color, stroke_width=3))


class DoublingDimensionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): one dimension
        title = Tex("Doubling one dimension").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        u = 0.35
        r0 = rect(np.array([-6.4, -2.2, 0]), 6 * u, 4 * u)
        r1 = rect(np.array([-3.6, -2.2, 0]), 12 * u, 4 * u)
        self.play(Create(r0))
        self.play(Write(Tex("$6 \\times 4$").scale(0.6).next_to(r0, DOWN, buff=0.15)))
        self.play(Create(r1))
        self.play(Write(Tex("$12 \\times 4$").scale(0.6).next_to(r1, DOWN, buff=0.15)))
        a1 = MathTex(r"P = 20,\ A = 24 \quad\to\quad P = 32,\ A = 48").scale(0.85).shift(UP * 2.0)
        a2 = Tex("Area doubles: one factor of the product doubled.").scale(0.75).shift(UP * 1.2)
        a3 = Tex("Perimeter adds twice the stretched side: $20 + 12 = 32$; breadth doubled gives $20 + 8 = 28$.").scale(0.68).shift(UP * 0.4)
        a4 = Tex("Square side 5, one side doubled: a $10 \\times 5$ rectangle, $P = 30$, $A = 50$.").scale(0.7).shift(DOWN * 0.4)
        for m in (a1, a2, a3, a4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(a2, color=YELLOW)))
        self.wait(4)

        # --- Band 1 (subtopic_2): both dimensions
        self.next_band(1)
        h1 = Tex("Doubling all dimensions: $P \\times 2$, $A \\times 4$").scale(1.05).move_to(band_shift(1) + UP * 3.2)
        self.play(Write(h1))
        o2 = np.array([-6.4, -2.4, 0]) + band_shift(1)
        s0 = rect(o2, 6 * u, 4 * u)
        o3 = o2 + RIGHT * 3.0
        s1 = rect(o3, 12 * u, 8 * u)
        self.play(Create(s0), Create(s1))
        self.play(Create(split_lines(o3, 12 * u, 8 * u)))
        self.play(Write(Tex("four copies").scale(0.6).next_to(s1, DOWN, buff=0.15)))
        b1 = MathTex(r"12 \times 8:\quad P = 40 = 2 \times 20,\quad A = 96 = 4 \times 24").scale(0.85).move_to(band_shift(1) + UP * 2.1 + RIGHT * 2.0)
        b2 = Tex("Square 5 to 10: $P$ 20 to 40, $A$ 25 to 100. Tripled: 60 and 225.").scale(0.72).move_to(band_shift(1) + UP * 1.2 + RIGHT * 2.0)
        b3 = Tex("Triangle 6, 8, 10 doubled: $P$ 24 to 48, $A$ 24 to 96.").scale(0.72).move_to(band_shift(1) + UP * 0.3 + RIGHT * 2.0)
        b4 = Tex("Length is one-dimensional; area is two-dimensional, so doubling acts twice.").scale(0.68).move_to(band_shift(1) + DOWN * 0.6 + RIGHT * 2.0)
        for m in (b1, b2, b3, b4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(b1, color=YELLOW)))
        self.wait(4)

        # --- Band 2 (subtopic_3): scale factor k
        self.next_band(2)
        h2 = Tex("Circles and the general scale factor $k$").scale(1.05).move_to(band_shift(2) + UP * 3.2)
        self.play(Write(h2))
        c0 = Circle(radius=0.6, color=WHITE, stroke_width=4).move_to(band_shift(2) + LEFT * 5.6 + DOWN * 0.8)
        c1 = Circle(radius=1.2, color=WHITE, stroke_width=4).move_to(band_shift(2) + LEFT * 3.4 + DOWN * 0.8)
        self.play(Create(c0), Create(c1))
        k1 = MathTex(r"r = 3:\ C \approx 18.85,\ A \approx 28.27;\quad r = 6:\ C \approx 37.70,\ A \approx 113.10").scale(0.7).move_to(band_shift(2) + UP * 2.1 + RIGHT * 1.6)
        k2 = MathTex(r"\text{scale factor } k:\quad P \to kP,\qquad A \to k^2 A").scale(0.9).move_to(band_shift(2) + UP * 1.2 + RIGHT * 1.6)
        k3 = Tex("$k = 3$: area $\\times 9$. $k = 10$: $\\times 100$. $k = \\tfrac{1}{2}$: $\\times \\tfrac{1}{4}$. $k = 1.5$: $\\times 2.25$.").scale(0.7).move_to(band_shift(2) + UP * 0.3 + RIGHT * 1.6)
        k4 = Tex("Trapezium 32 scaled by 1.5: $\\tfrac{1}{2}(9 + 15)(6) = 72 = 32 \\times 2.25$.").scale(0.7).move_to(band_shift(2) + DOWN * 0.6 + RIGHT * 1.6)
        k5 = Tex("Backwards: area $\\times 9 \\Rightarrow k = \\sqrt{9} = 3$. Area $\\times 2 \\Rightarrow k \\approx 1.41$.").scale(0.7).move_to(band_shift(2) + DOWN * 1.5 + RIGHT * 1.6)
        for m in (k1, k2, k3, k4, k5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(k2, color=YELLOW)))
        self.wait(3)

        # --- Band 3 (subtopic_4): applications
        self.next_band(3)
        h3 = Tex("Applications").scale(1.05).move_to(band_shift(3) + UP * 3.2)
        self.play(Write(h3))
        p1 = Tex("Farm $50 \\times 30$: fence 160 m, 1500 m$^2$. Doubled: fence 320 m, 6000 m$^2$.").scale(0.7).move_to(band_shift(3) + UP * 2.1)
        p2 = Tex("At R85/m: R13 600 then R27 200. Twice the money, four times the land.").scale(0.7).move_to(band_shift(3) + UP * 1.2)
        p3 = Tex("Photo $10 \\times 15$ to $20 \\times 30$: four times the paper, twice the frame.").scale(0.7).move_to(band_shift(3) + UP * 0.3)
        p4 = Tex("Pizza 30 cm at R120 vs 15 cm at R45: four smalls cost R180. Large wins.").scale(0.7).move_to(band_shift(3) + DOWN * 0.6)
        p5 = Tex("Map 1 : 50 000: lengths $\\times 50\\,000$, areas $\\times 50\\,000^2$. 2 cm square $=$ 1 km square $=$ 100 ha.").scale(0.65).move_to(band_shift(3) + DOWN * 1.5)
        for m in (p1, p2, p3, p4, p5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(p2, color=YELLOW)))
        self.wait(3)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        h4 = Tex("Error museum").scale(1.05).move_to(band_shift(4) + UP * 3.2)
        self.play(Write(h4))
        e1 = Tex("Double the dimensions, double the area").scale(0.8).move_to(band_shift(4) + UP * 1.8)
        e2 = MathTex(r"k = 3 \Rightarrow \text{area} \times 3").scale(0.9).move_to(band_shift(4) + UP * 0.6)
        e3 = MathTex(r"\text{area} \times 9 \Rightarrow k = 9").scale(0.9).move_to(band_shift(4) + DOWN * 0.6)
        for m in (e1, e2, e3):
            self.play(Write(m))
            self.wait(1.5)
            self.play(Create(strike(m)))
            self.wait(1.5)
        fix = Tex("State $k$; perimeter $\\times k$, area $\\times k^2$; backwards take the square root.").scale(0.72).move_to(band_shift(4) + DOWN * 2.2)
        self.play(Write(fix))
        self.play(Create(SurroundingRectangle(fix, color=GREEN)))
        self.wait(5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): stretch
        self.next_band(5)
        h5 = Tex("Stretch one way, then both ways").scale(1.05).move_to(band_shift(5) + UP * 3.2)
        self.play(Write(h5))
        o5 = np.array([-6.4, -2.4, 0]) + band_shift(5)
        q0 = rect(o5, 6 * u, 4 * u)
        q1 = rect(o5 + RIGHT * 2.6, 12 * u, 4 * u, color=BLUE)
        q2 = rect(o5 + RIGHT * 7.4, 12 * u, 8 * u, color=GREEN)
        self.play(Create(q0))
        self.play(Create(q1))
        self.play(Create(q2))
        self.play(Create(split_lines(o5 + RIGHT * 7.4, 12 * u, 8 * u)))
        g1 = Tex("One way: carpet 24 to 48, fence 20 to 32 (up by twice the stretched side).").scale(0.68).move_to(band_shift(5) + UP * 2.1)
        g2 = Tex("Both ways: fence 20 to 40, carpet 24 to 96. Four copies inside.").scale(0.72).move_to(band_shift(5) + UP * 1.2)
        g3 = Tex("Triangle base 8, height 5: carpet 20; double base 40; double both 80.").scale(0.7).move_to(band_shift(5) + UP * 0.3)
        for m in (g1, g2, g3):
            self.play(Write(m))
            self.wait(2.8)
        self.play(Create(SurroundingRectangle(g2, color=YELLOW)))
        self.wait(4)

        # --- Band 6 (subtopic_6): fence and carpet
        self.next_band(6)
        h6 = Tex("Fence doubles, carpet quadruples").scale(1.05).move_to(band_shift(6) + UP * 3.2)
        self.play(Write(h6))
        f1 = Tex("Fence is made of lengths: each doubled, total doubled.").scale(0.75).move_to(band_shift(6) + UP * 2.0)
        f2 = Tex("Carpet is length times width: both doubled, so $2 \\times 2 = 4$.").scale(0.75).move_to(band_shift(6) + UP * 1.1)
        f3 = Tex("Circle $r$ 3 to 6: fence 18.85 to 37.70, carpet 28.27 to 113.10.").scale(0.72).move_to(band_shift(6) + UP * 0.2)
        f4 = Tex("Triple: fence $\\times 3$, carpet $\\times 9$. Halve: fence $\\times \\tfrac{1}{2}$, carpet $\\times \\tfrac{1}{4}$.").scale(0.72).move_to(band_shift(6) + DOWN * 0.7)
        f5 = Tex("Farm doubled: R13 600 to R27 200 of fence for four times the land.").scale(0.72).move_to(band_shift(6) + DOWN * 1.6)
        for m in (f1, f2, f3, f4, f5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(f2, color=YELLOW)))
        self.wait(3)

        # --- Band 7 (subtopic_7): k
        self.next_band(7)
        h7 = Tex("Scale factor $k$: times $k$, times $k^2$").scale(1.05).move_to(band_shift(7) + UP * 3.2)
        self.play(Write(h7))
        w1 = MathTex(r"k = 2:\ \times 2,\ \times 4 \qquad k = 3:\ \times 3,\ \times 9 \qquad k = 10:\ \times 10,\ \times 100").scale(0.75).move_to(band_shift(7) + UP * 2.0)
        w2 = Tex("Backwards: carpet $\\times 9 \\Rightarrow k = 3$. Fence $\\times 5 \\Rightarrow$ carpet $\\times 25$.").scale(0.72).move_to(band_shift(7) + UP * 1.1)
        w3 = Tex("Double the carpet: $k = \\sqrt{2} \\approx 1.41$, sides up about 41 percent.").scale(0.72).move_to(band_shift(7) + UP * 0.2)
        pz0 = Circle(radius=0.5, color=ORANGE, stroke_width=4).move_to(band_shift(7) + LEFT * 5.4 + DOWN * 1.6)
        pz1 = Circle(radius=1.0, color=ORANGE, stroke_width=4).move_to(band_shift(7) + LEFT * 3.4 + DOWN * 1.6)
        self.play(Create(pz0), Create(pz1))
        w4 = Tex("30 cm pizza is four 15 cm pizzas. Map: lengths $\\times 50\\,000$, areas $\\times 50\\,000^2$.").scale(0.68).move_to(band_shift(7) + DOWN * 0.9 + RIGHT * 1.6)
        w5 = Tex("One way, both ways, $k$ squared.").scale(0.85).move_to(band_shift(7) + DOWN * 2.4 + RIGHT * 1.6)
        for m in (w1, w2, w3, w4, w5):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(w5, color=YELLOW)))
        self.wait(6)
