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


def dot_square(n, origin, gap=0.32):
    g = VGroup()
    for i in range(n):
        for j in range(n):
            g.add(Dot(origin + RIGHT * i * gap + UP * j * gap, radius=0.06))
    return g


def dot_staircase(n, origin, gap=0.32):
    g = VGroup()
    for row in range(n):
        for i in range(row + 1):
            g.add(Dot(origin + RIGHT * i * gap + DOWN * row * gap, radius=0.06))
    return g


class BeyondConstantPatternsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): second differences
        title = Tex("Patterns Beyond Constant Difference").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"1,\; 4,\; 9,\; 16,\; 25 \qquad \text{1st: } 3, 5, 7, 9 \qquad \text{2nd: } 2, 2, 2").scale(0.95).shift(UP * 1.3)
        l2 = MathTex(r"2,\; 5,\; 10,\; 17 = (1, 4, 9, 16) + 1 \;\Rightarrow\; T_n = n^2 + 1").scale(0.95).shift(UP * 0.3)
        l3 = MathTex(r"0,\; 3,\; 8,\; 15 \Rightarrow n^2 - 1 \qquad 2,\; 8,\; 18,\; 32 \Rightarrow 2n^2 \;(\text{2nd diff } 4)").scale(0.9).shift(DOWN * 0.7)
        l4 = MathTex(r"1,\; 9,\; 25,\; 49 \Rightarrow T_n = (2n - 1)^2").scale(1.0).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): triangular and recursive
        self.next_band(1)
        b1_title = Tex("Triangular numbers; rules from previous terms").scale(1.05).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        stair = dot_staircase(4, band_shift(1) + UP * 1.4 + LEFT * 5.5)
        self.play(Create(stair))
        self.wait(1.5)
        b1_l1 = MathTex(r"1,\; 3,\; 6,\; 10,\; 15 \qquad T_n = \frac{n(n+1)}{2},\; T_{10} = 55").scale(0.95).shift(band_shift(1) + UP * 1.0 + RIGHT * 1.5)
        b1_l2 = MathTex(r"1, 1, 2, 3, 5, 8, 13: \quad T_n = T_{n-1} + T_{n-2},\; T_1 = T_2 = 1").scale(0.95).shift(band_shift(1) + DOWN * 0.1)
        b1_l3 = MathTex(r"\text{Same recipe from 2 and 5: } 2, 5, 7, 12, 19").scale(0.95).shift(band_shift(1) + DOWN * 1.0)
        b1_l4 = MathTex(r"1, -2, 4, -8, 16: \quad T_n = (-2)^{n-1}").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): identifying
        self.next_band(2)
        b2_title = Tex("Run the tests in order").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        rows = [
            r"\text{1. First differences constant? } dn + c",
            r"\text{2. Ratios constant? } T_1 r^{\,n-1}",
            r"\text{3. Second differences constant? } n^2 \text{ involved}",
            r"\text{4. Built from previous terms? Recursive rule + start}",
            r"\text{5. Famous sequence? Name it}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.85).shift(band_shift(2) + UP * (1.4 - 0.7 * i))
            self.play(Write(m))
            self.wait(1.8)
        b2_l6 = MathTex(r"1, 2, 4 \to 8 \text{ or } 7: \text{ three terms never decide}").scale(0.9).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_3): worked identifications
        self.next_band(3)
        b3_title = Tex("Worked identifications").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"2, 6, 12, 20, 30: \;\text{2nd diff } 2,\; T_n = n^2 + n").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"1, 8, 27, 64, 125: \; T_n = n^3").scale(0.95).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"4, 7, 12, 19, 28: \;\text{2nd diff } 2,\; T_n = n^2 + 3").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = MathTex(r"1, 2, 4, 7, 11, 16: \;\text{1st diffs } 1, 2, 3, 4, 5").scale(0.95).shift(band_shift(3) + DOWN * 1.8)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): creating, and the error museum
        self.next_band(4)
        b4_title = Tex("Create your own; error museum").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"T_n = 3n^2 - 1: \; 2, 11, 26, 47, 74 \quad \text{2nd diff } 6").scale(0.95).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"\text{Border dots: } 4n - 4").scale(0.95).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex(r"``Add more each time''").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = Tex(r"Recursive rule with no starting terms").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        for m in (b4_l1, b4_l2):
            self.play(Write(m))
            self.wait(2.2)
        for m in (b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): staircases and squares
        self.next_band(5)
        b5_title = Tex("Staircases and squares").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        s1 = dot_square(1, band_shift(5) + UP * 0.6 + LEFT * 5.5)
        s2 = dot_square(2, band_shift(5) + UP * 0.6 + LEFT * 4.6)
        s3 = dot_square(3, band_shift(5) + UP * 0.6 + LEFT * 3.4)
        s4 = dot_square(4, band_shift(5) + UP * 0.6 + LEFT * 1.9)
        for s in (s1, s2, s3, s4):
            self.play(Create(s))
            self.wait(0.8)
        b5_l1 = Tex(r"Layers 3, 5, 7, 9: differences grow by 2").scale(0.95).shift(band_shift(5) + UP * 1.2 + RIGHT * 2.6)
        b5_l2 = MathTex(r"2, 5, 10, 17 \text{ against } 1, 4, 9, 16: \; n^2 + 1").scale(0.9).shift(band_shift(5) + UP * 0.2 + RIGHT * 2.6)
        b5_l3 = MathTex(r"\text{Staircase } 1, 3, 6, 10, 15: \; \tfrac{n(n+1)}{2}").scale(0.95).shift(band_shift(5) + DOWN * 1.2)
        for m in (b5_l1, b5_l2, b5_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 6 (subtopic_6): rabbits
        self.next_band(6)
        b6_title = Tex("Rabbits: add the two before").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"1,\; 1,\; 2,\; 3,\; 5,\; 8,\; 13,\; 21").scale(1.1).shift(band_shift(6) + UP * 1.3)
        b6_l2 = MathTex(r"1 + 1 = 2,\quad 1 + 2 = 3,\quad 2 + 3 = 5,\quad 8 + 13 = 21").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("Say where it starts, or it is not a description").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = MathTex(r"1, -2, 4, -8: \text{ multiplier } -2 \text{ flips the sign}").scale(0.95).shift(band_shift(6) + DOWN * 1.5)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): make your own
        self.next_band(7)
        b7_title = Tex("Make your own pattern").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        rows = [
            r"\text{1. Pick a rule: } n^2 + 3",
            r"\text{2. Five terms: } 4, 7, 12, 19, 28",
            r"\text{3. Check the fingerprint: } 3, 5, 7, 9",
            r"\text{4. Words and algebra: square the position, add 3}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.9).shift(band_shift(7) + UP * (1.3 - 0.75 * i))
            self.play(Write(m))
            self.wait(1.8)
        b7_l5 = Tex("Taxi, chain, squares, rabbits. Use every term.").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=YELLOW)))
        self.wait(4)
