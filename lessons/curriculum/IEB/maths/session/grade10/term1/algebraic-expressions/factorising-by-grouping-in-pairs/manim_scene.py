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

# Band-layout whiteboard scene: one band per teaching beat, camera moves down
# to fresh space, nothing removed. Write-only reveals on single-string
# Tex/MathTex keep the export clean. Bands cover all seven subtopics
# (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7), dwell time proportional
# to subtopics.json (200/250/250/260/170/170/170 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GroupingInPairsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): four terms, a different tool
        title = Tex("Factorising by Grouping in Pairs").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l01 = MathTex(r"3mp + 3mq - np - nq").scale(1.2).shift(UP * 0.9)
        self.play(Write(l01))
        self.wait(2)
        l02 = Tex(r"Four terms $\Rightarrow$ grouping in pairs").scale(1.05).shift(UP * 0.0)
        self.play(Write(l02))
        self.wait(2)
        l03 = Tex(r"No overall common factor; no identity fits").scale(1.0).shift(DOWN * 1.0)
        self.play(Write(l03))
        self.wait(2)
        l04 = Tex(r"But each PAIR shares: $3m$ in the first, $n$ in the second").scale(0.95).shift(DOWN * 2.0)
        self.play(Write(l04))
        self.play(Create(SurroundingRectangle(l04, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): factor each pair
        self.next_band(1)
        b1_title = Tex("Factor each pair").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"3mp + 3mq = 3m(p + q)").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_wrong = MathTex(r"-np - nq = n(-p - q)").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        b1_flag = Tex(r"Brackets do not match — dead end").scale(0.95).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_flag))
        self.wait(2)
        b1_right = MathTex(r"-np - nq = -n(p + q)").scale(1.1).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_right))
        self.play(Create(SurroundingRectangle(b1_right, color=GREEN)))
        b1_rule = Tex(r"Leading minus $\Rightarrow$ take out a NEGATIVE factor").scale(0.95).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_rule))
        self.wait(2.5)

        # --- Band 2 (subtopic_3): the common bracket
        self.next_band(2)
        b2_title = Tex("Factor out the shared bracket").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"3m(p + q) - n(p + q)").scale(1.1).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{Let } B = (p+q): \;\; 3mB - nB = B(3m - n)").scale(1.0).shift(band_shift(2) + UP * 0.1)
        b2_l3 = MathTex(r"= (p + q)(3m - n)").scale(1.15).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = Tex(r"Verify: expand — all four terms return").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): rearrangement rescue
        self.next_band(3)
        b3_title = Tex("When the order refuses to pair").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"3mp - nq - np + 3mq").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex(r"First pair shares nothing useful").scale(0.95).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"\text{Reshuffle: } 3mp + 3mq - np - nq").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex(r"Kin beside kin, then group as before").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_4): full method + bonus example
        self.next_band(4)
        b4_title = Tex(r"Bonus: $2cd + 6c - d - 3$").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"2cd + 6c = 2c(d + 3)").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"-d - 3 = -1(d + 3)").scale(1.05).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"= (d + 3)(2c - 1)").scale(1.1).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_m1 = Tex(r"1. Common factor \; 2. Pair (reshuffle if needed)").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        b4_m2 = Tex(r"3. Factor pairs (minus rule) \; 4. Shared bracket \; 5. Verify").scale(0.9).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_m1))
        self.wait(1.5)
        self.play(Write(b4_m2))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): two bags
        self.next_band(5)
        b5_title = Tex("Sorting the shopping into two bags").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"Bag one: $3mp,\; 3mq$ — both carry $3m$").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"Bag two: $-np,\; -nq$ — both carry $n$").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"3mp + 3mq = 3m(p + q)").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        b5_l4 = Tex(r"The bracket holds the leftovers").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_6): the minus that must come out
        self.next_band(6)
        b6_title = Tex("The minus that must come out").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_wrong = MathTex(r"n(-p - q) \;\;\text{vs}\;\; 3m(p + q)").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        self.wait(2)
        b6_right = MathTex(r"-n(p + q) \;\;\text{— twins at last}").scale(1.05).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_right))
        self.play(Create(SurroundingRectangle(b6_right, color=GREEN)))
        self.wait(2)
        b6_l3 = Tex(r"Bag starts with a minus? Take out a negative.").scale(1.0).shift(band_shift(6) + DOWN * 1.0)
        b6_l4 = Tex(r"Never erase signs inside a bracket for free").scale(0.95).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2.5)

        # --- Band 7 (subtopic_7): the same bracket in both hands
        self.next_band(7)
        b7_title = Tex("The same bracket in both hands").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"3m(p+q) - n(p+q)").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"= (p + q)(3m - n)").scale(1.1).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex(r"Multiply back: $3mp + 3mq - np - nq$ \; ✓").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex(r"Four items, two bags, one shared bracket").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.wait(4)
