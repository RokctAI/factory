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


def matchstick_squares(n, origin, size=0.6):
    """Row of n unit squares built from shared matchsticks."""
    g = VGroup()
    for i in range(n):
        x = origin[0] + i * size
        bl = np.array([x, origin[1], 0])
        g.add(Line(bl, bl + UP * size, color=ORANGE, stroke_width=5))
        g.add(Line(bl, bl + RIGHT * size, color=ORANGE, stroke_width=5))
        g.add(Line(bl + UP * size, bl + UP * size + RIGHT * size, color=ORANGE, stroke_width=5))
    end = np.array([origin[0] + n * size, origin[1], 0])
    g.add(Line(end, end + UP * size, color=ORANGE, stroke_width=5))
    return g


class ExtendingPatternsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): constant difference
        title = Tex("Extending Patterns").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"5,\; 8,\; 11,\; 14,\; \dots \qquad d = 3").scale(1.05).shift(UP * 1.3)
        l2 = MathTex(r"T_n = dn + c, \quad c = T_1 - d = 2 \;\Rightarrow\; T_n = 3n + 2").scale(1.0).shift(UP * 0.3)
        l3 = MathTex(r"T_{20} = 62 \qquad 3n + 2 = 92 \Rightarrow n = 30").scale(1.0).shift(DOWN * 0.7)
        l4 = MathTex(r"20,\; 17,\; 14,\; 11 \;\Rightarrow\; T_n = 23 - 3n,\; T_{10} = -7").scale(0.95).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): constant ratio
        self.next_band(1)
        b1_title = Tex("Constant ratio: a power").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"3,\; 6,\; 12,\; 24,\; \dots \qquad r = 2").scale(1.05).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"T_n = T_1 \cdot r^{\,n-1} = 3 \times 2^{n-1}").scale(1.1).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"T_1 = 3 \times 2^0 = 3 \qquad T_8 = 3 \times 2^7 = 384").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"2,\; 6,\; 18,\; 54 \Rightarrow 2 \times 3^{n-1},\; T_6 = 486 \qquad 80 \times (\tfrac{1}{2})^{n-1},\; T_5 = 5").scale(0.85).shift(band_shift(1) + DOWN * 1.8)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): diagrams and tables
        self.next_band(2)
        b2_title = Tex("Matchstick squares: 4, 7, 10, ...").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        sq1 = matchstick_squares(1, band_shift(2) + UP * 0.9 + LEFT * 5.0)
        sq2 = matchstick_squares(2, band_shift(2) + UP * 0.9 + LEFT * 3.4)
        sq3 = matchstick_squares(3, band_shift(2) + UP * 0.9 + LEFT * 1.2)
        for s in (sq1, sq2, sq3):
            self.play(Create(s))
            self.wait(1.2)
        b2_l1 = MathTex(r"T_n = 3n + 1 \quad (\text{3 new sticks per square, 1 to close the first})").scale(0.9).shift(band_shift(2) + UP * 0.9 + RIGHT * 3.0)
        b2_l2 = MathTex(r"T_{15} = 46 \qquad 3n + 1 = 31 \Rightarrow n = 10").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        b2_l3 = MathTex(r"\text{L-shapes: } 3,\; 5,\; 7 \Rightarrow T_n = 2n + 1").scale(1.0).shift(band_shift(2) + DOWN * 1.5)
        for m in (b2_l1, b2_l2, b2_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 3 (subtopic_4): the procedure
        self.next_band(3)
        b3_title = Tex("Find the rule, test the rule").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        rows = [
            r"\text{1. Differences constant? } T_n = dn + (T_1 - d)",
            r"\text{2. Ratios constant? } T_n = T_1 \cdot r^{\,n-1}",
            r"\text{3. Test at } n = 1 \text{ and at the last term}",
            r"\text{4. Then use it: } 3 \times 2^{n-1} = 384 \Rightarrow 2^{n-1} = 128 \Rightarrow n = 8",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.9).shift(band_shift(3) + UP * (1.3 - 0.85 * i))
            self.play(Write(m))
            self.wait(2.2)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"T_n = T_1 + dn \;\text{(gives 8 for } T_1\text{)}").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"T_n = 3 \times 2^{n} \;\text{(gives 6 for } T_1\text{)}").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex("Tested on one term only").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"3,\; 6,\; 12 \;\text{read as}\; 3,\; 6,\; 9").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): taxi meter
        self.next_band(5)
        b5_title = Tex("The taxi meter: step and flag fall").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"R2 to get in, R3 per km: 5, 8, 11, 14").scale(1.0).shift(band_shift(5) + UP * 1.3)
        b5_l2 = MathTex(r"T_n = \underbrace{3}_{\text{step}} n + \underbrace{2}_{\text{flag fall}}").scale(1.05).shift(band_shift(5) + UP * 0.2)
        b5_l3 = Tex(r"Flag fall is one step BACK from the first term: $5 - 3 = 2$").scale(0.95).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = Tex(r"R100? $100 - 2 = 98$, not a multiple of 3: never").scale(0.95).shift(band_shift(5) + DOWN * 1.7)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): doubling
        self.next_band(6)
        b6_title = Tex("Doubling patterns: count the jumps").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        dots = VGroup(*[Dot(band_shift(6) + UP * 1.2 + RIGHT * (x - 3.0), radius=0.09) for x in (0, 2, 4, 6)])
        labels = VGroup(*[MathTex(s).scale(0.8).next_to(d, UP, buff=0.15) for s, d in zip(("3", "6", "12", "24"), dots)])
        arrows = VGroup(*[MathTex(r"\times 2").scale(0.7).move_to(band_shift(6) + UP * 0.8 + RIGHT * (x - 2.0)) for x in (0, 2, 4)])
        self.play(Create(dots), Write(labels))
        self.play(Write(arrows))
        self.wait(2)
        b6_l3 = Tex("Four terms, three jumps: the exponent is $n - 1$").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        b6_l4 = MathTex(r"T_n = 3 \times 2^{n-1} \qquad T_8 = 384").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        b6_l5 = Tex(r"Subtract neighbours: step pattern. Divide neighbours: multiplying pattern.").scale(0.85).shift(band_shift(6) + DOWN * 2.1)
        for m in (b6_l3, b6_l4, b6_l5):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 7 (subtopic_7): picture pattern
        self.next_band(7)
        b7_title = Tex("Reading a picture: growing part, fixed part").scale(1.1).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        sq = matchstick_squares(4, band_shift(7) + UP * 0.9 + LEFT * 4.5)
        self.play(Create(sq))
        self.wait(1.5)
        b7_l1 = Tex(r"Grows: 3 sticks per square. Fixed: 1 closing stick.").scale(0.95).shift(band_shift(7) + UP * 0.9 + RIGHT * 2.2)
        b7_l2 = MathTex(r"T_n = 3n + 1 \qquad T_{15} = 46 \qquad 50 \text{ sticks} \Rightarrow 16 \text{ squares, 1 spare}").scale(0.9).shift(band_shift(7) + DOWN * 0.3)
        b7_l3 = Tex("Test on two terms. Then jump.").scale(1.0).shift(band_shift(7) + DOWN * 1.3)
        for m in (b7_l1, b7_l2):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=YELLOW)))
        self.wait(4)
