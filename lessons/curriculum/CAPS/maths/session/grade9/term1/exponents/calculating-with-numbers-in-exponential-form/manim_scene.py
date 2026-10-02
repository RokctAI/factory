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


class ExponentCalculationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): adding and subtracting
        title = Tex("Calculating with Powers").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"2^3 + 2^4 = 8 + 16 = 24 \;\text{(no law)}").scale(1.05).shift(UP * 1.3)
        l2 = MathTex(r"5^2 - 3^2 = 16 \qquad (5 - 3)^2 = 4").scale(1.05).shift(UP * 0.3)
        l3 = MathTex(r"2^5 + 2^5 = 2 \times 2^5 = 2^6 \qquad 3^4 + 3^4 + 3^4 = 3^5").scale(0.95).shift(DOWN * 0.7)
        l4 = MathTex(r"3 \times 2^4 - 2^5 = 48 - 32 = 16").scale(1.0).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): multiplying and dividing
        self.next_band(1)
        b1_title = Tex("Same base, same exponent, or neither").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"2^3 \times 5^3 = (2 \times 5)^3 = 10^3 = 1\,000").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"6^4 \div 3^4 = 2^4 = 16 \qquad 2^3 \times 3^2 = 72").scale(1.0).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"2^5 \times 3^2 \div 2^3 = 2^2 \times 9 = 36").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"12^2 = (2^2 \times 3)^2 = 2^4 \times 3^2 = 144").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): order of operations
        self.next_band(2)
        b2_title = Tex("Brackets, powers and roots, then multiply, then add").scale(1.0).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"2 + 3 \times 2^3 = 26 \qquad (2 + 3) \times 2^3 = 40").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = MathTex(r"2 \times 3^2 = 18 \qquad (2 \times 3)^2 = 36 \qquad -3^2 + (-3)^2 = 0").scale(0.95).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"\sqrt{2^4} + \sqrt[3]{2^6} = 2^2 + 2^2 = 8").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = MathTex(r"2^3 \times 2^2 + 2^5 \div 2^3 = 32 + 4 = 36").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): powers of ten
        self.next_band(3)
        b3_title = Tex("Scientific notation: fronts and powers separately").scale(1.05).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"(3 \times 10^4)(2 \times 10^5) = 6 \times 10^9").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"(8 \times 10^6) \div (4 \times 10^2) = 2 \times 10^4").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"(4 \times 10^3)(5 \times 10^2) = 20 \times 10^5 = 2 \times 10^6").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = MathTex(r"3 \times 10^5 + 2 \times 10^4 = 30 \times 10^4 + 2 \times 10^4 = 3{,}2 \times 10^5").scale(0.9).shift(band_shift(3) + DOWN * 1.8)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"2^3 + 2^4 = 2^7 \qquad 5^2 - 3^2 = 2^2").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"2^3 \times 5^3 = 10^6").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"3 \times 10^5 + 2 \times 10^4 = 5 \times 10^9").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"2 \times 3^2 = 36").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): bags of marbles
        self.next_band(5)
        b5_title = Tex("Adding is not a law: tip out the bags").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        bag1 = Rectangle(width=1.6, height=1.2, color=BLUE).shift(band_shift(5) + UP * 0.9 + LEFT * 2.5)
        bag2 = Rectangle(width=1.6, height=1.2, color=BLUE).shift(band_shift(5) + UP * 0.9 + LEFT * 0.3)
        lab1 = MathTex(r"2^3 = 8").scale(0.8).move_to(bag1)
        lab2 = MathTex(r"2^4 = 16").scale(0.8).move_to(bag2)
        total = MathTex(r"= 24").scale(1.1).shift(band_shift(5) + UP * 0.9 + RIGHT * 2.0)
        self.play(Create(bag1), Write(lab1))
        self.play(Create(bag2), Write(lab2))
        self.wait(1.5)
        self.play(Write(total))
        self.wait(2)
        b5_l3 = MathTex(r"\text{Identical bags: } 2^5 + 2^5 = 2 \times 2^5 = 2^6").scale(0.95).shift(band_shift(5) + DOWN * 0.6)
        b5_l4 = Tex("Powers first, then multiply, then add: $3 \\times 2^4 - 2^5 = 16$").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        for m in (b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 6 (subtopic_6): what matches
        self.next_band(6)
        b6_title = Tex("Same base? Same exponent? Neither?").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        rows = [
            r"\text{Same base: } 2^5 \div 2^3 = 2^2",
            r"\text{Same exponent: } 2^3 \times 5^3 = 10^3 = 1\,000",
            r"\text{Neither: } 2^3 \times 3^2 = 8 \times 9 = 72",
            r"\text{Never both: } 2^3 \times 5^3 \neq 10^6",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.95).shift(band_shift(6) + UP * (1.3 - 0.85 * i))
            self.play(Write(m))
            self.wait(2.2)
        b6_l5 = MathTex(r"12^2 = 2^4 \times 3^2 = 144").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l5))
        self.wait(2.5)

        # --- Band 7 (subtopic_7): BODMAS and big numbers
        self.next_band(7)
        b7_title = Tex("Kitchen order, and the shelves").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"2 + 3 \times 2^3 = 26 \qquad 2 \times 3^2 = 18").scale(1.0).shift(band_shift(7) + UP * 1.3)
        b7_l2 = MathTex(r"\sqrt{2^4} + \sqrt[3]{2^6} = 4 + 4 = 8").scale(1.0).shift(band_shift(7) + UP * 0.4)
        b7_l3 = MathTex(r"(3 \times 10^4)(2 \times 10^5) = 6 \times 10^9").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = MathTex(r"3 \times 10^5 + 2 \times 10^4 \to 30 \times 10^4 + 2 \times 10^4 = 3{,}2 \times 10^5").scale(0.85).shift(band_shift(7) + DOWN * 1.4)
        b7_l5 = Tex("Plus sign: count. Times sign: match, then shortcut.").scale(0.95).shift(band_shift(7) + DOWN * 2.3)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=YELLOW)))
        self.wait(4)
