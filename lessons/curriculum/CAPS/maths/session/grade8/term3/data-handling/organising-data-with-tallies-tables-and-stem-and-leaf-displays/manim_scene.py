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
# dwell time proportional to subtopics.json (250/190/220/240/240/210/220 of
# 1570 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class OrganiseDataSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Tally Marks and Frequency Tables
        t0 = Tex(r"Tally Marks and Frequency Tables").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = Tex(r"One row per category; one mark per form; group marks in fives").scale(1.05).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Frequency: how many times the category occurred").scale(1.05).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"12 + 9 + 6 + 3 = 30").scale(1.1).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Heading, three columns, total row; frequencies must sum to the total").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): Numerical Frequency Tables
        self.next_band(1)
        t1 = Tex(r"Numerical Frequency Tables").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = Tex(r"Few repeating values: one row per value (siblings 0, 1, 2, 3, 4 or more)").scale(1.05).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = Tex(r"Many rarely-repeating values: stem-and-leaf or grouped intervals").scale(1.05).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"Order first: 12, 17, 19, 22, 23, 27, 28, 29, 30, 31, 31, 31, 33, 35, 36, 38, 40, 44, 45, 48").scale(1.05).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Count after ordering: twenty values, twenty forms").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Constructing a Stem-and-Leaf
        self.next_band(2)
        t2 = Tex(r"Constructing a Stem-and-Leaf").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        rows = [("1", "2 7 9"), ("2", "2 3 7 8 9"), ("3", "0 1 1 1 3 5 6 8"), ("4", "0 4 5 8")]
        grp = VGroup(*[Tex(s + r" $\mid$ " + l).scale(1.0) for s, l in rows]).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(band_shift(2) + UP * 0.6)
        self.play(Write(grp), run_time=3)
        key = Tex(r"Key: 2 $\mid$ 3 means 23").scale(0.9).next_to(grp, DOWN, buff=0.4)
        self.play(FadeIn(key))
        self.wait(1.5)
        self.play(FadeOut(grp), FadeOut(key))
        m9 = Tex(r"Leaves in order, one digit each, repeats repeated; count leaves: 3, 5, 8, 4 make 20").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(m9))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m9, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Reading and Grouping
        self.next_band(3)
        t3 = Tex(r"Reading and Grouping").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m10 = Tex(r"Row: stem 4, leaves 0 4 5 8 are 40, 44, 45, 48. Column: longest row shows the bunch.").scale(1.05).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m10))
        self.wait(2)
        m11 = Tex(r"Intervals 10 to 19, 20 to 29, 30 to 39, 40 to 49: frequencies 3, 5, 8, 4").scale(1.05).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m11))
        self.wait(2)
        m12 = MathTex(r"\text{range} = 48 - 12 = 36").scale(1.1).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m12))
        self.wait(2)
        m13 = Tex(r"Equal width, no overlap, every value in exactly one interval; grouping loses detail").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m13))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m13, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): The Cashier Who Counts in Fives
        self.next_band(4)
        t4 = Tex(r"The Cashier Who Counts in Fives").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m14 = Tex(r"Coins by value, stacked in fives, count on a slip, check against takings").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"Categories, tally groups, frequency column, total check").scale(1.05).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m15))
        self.wait(2)
        m16 = MathTex(r"12 + 9 = 21, \quad 21 + 6 = 27, \quad 27 + 3 = 30").scale(1.1).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m16))
        self.wait(2)
        m17 = Tex(r"Never count the heap; sort into rows and check the sum").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m17))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m17, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): Stem-and-Leaf at the Cricket
        self.next_band(5)
        t5 = Tex(r"Stem-and-Leaf at the Cricket").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        rows = [("0", "0 2 4 7 8"), ("1", "1 5 9"), ("2", "3 6"), ("3", "4"), ("4", "~"), ("5", "1")]
        grp = VGroup(*[Tex(s + r" $\mid$ " + l).scale(0.95) for s, l in rows]).arrange(DOWN, aligned_edge=LEFT, buff=0.22).move_to(band_shift(5) + UP * 0.5)
        self.play(Write(grp), run_time=3)
        key = Tex(r"Key: 2 $\mid$ 3 means 23. Eleven leaves, eleven batters.").scale(0.85).next_to(grp, DOWN, buff=0.4)
        self.play(FadeIn(key))
        self.wait(1.5)
        self.play(FadeOut(grp), FadeOut(key))
        m18 = Tex(r"Read across for a score; read down for the shape; keep the empty stem").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(m18))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m18, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_7): Examination Technique
        self.next_band(6)
        t6 = Tex(r"Examination Technique").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m19 = Tex(r"Tally in fives, frequencies sum to the total, order numerical data").scale(1.05).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"Stem-and-leaf: ordered leaves, repeats kept, empty stems kept, key").scale(1.05).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m20))
        self.wait(2)
        m21 = Tex(r"Grouped table: equal width, no overlap, every value in one interval, total checked").scale(1.05).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m21))
        self.wait(2)
        m22 = Tex(r"Above 35 in the display: 36, 38, 40, 44, 45, 48 make six").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m22))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m22, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
