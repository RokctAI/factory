# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from manim import *

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (200/250/250/260/170/170/170 of
# 1470 s).

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
        # --- Band 0 (subtopic_1): four terms call for grouping
        title = Tex("Factorising by Grouping in Pairs").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        expr = MathTex(r"2ax + 2ay - bx - by").scale(1.3).shift(UP * 0.9)
        self.play(Write(expr))
        self.wait(2)
        count1 = Tex(r"2 terms: squares / cubes identities").scale(1.1).shift(DOWN * 0.3)
        count2 = Tex(r"3 terms: trinomial method").scale(1.1).shift(DOWN * 1.1)
        count3 = Tex(r"4 terms: grouping in pairs").scale(1.1).shift(DOWN * 1.9)
        self.play(Write(count1))
        self.play(Write(count2))
        self.play(Write(count3))
        self.wait(2)
        nofac = Tex(r"No factor common to ALL four terms").scale(1.1).shift(DOWN * 2.9)
        self.play(Write(nofac))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): pairwise structure and the plan
        self.next_band(1)
        b1_title = Tex("But the PAIRS share plenty").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"2ax + 2ay \;\text{ share }\; 2a").scale(1.15).shift(band_shift(1) + UP * 1.0)
        b1_l2 = MathTex(r"-bx - by \;\text{ share }\; b").scale(1.15).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_plan = Tex(r"Plan: pair up $\rightarrow$ factor each pair").scale(1.1).shift(band_shift(1) + DOWN * 1.2)
        b1_plan2 = Tex(r"$\rightarrow$ factor out the common bracket").scale(1.1).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_plan))
        self.play(Write(b1_plan2))
        self.wait(3)

        # --- Band 2 (subtopic_2): factor each pair — the sign trap
        self.next_band(2)
        b2_title = Tex("Factor each pair — mind the signs").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"2ax + 2ay = 2a(x + y)").scale(1.15).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_wrong = MathTex(r"-bx - by = b(-x - y)").scale(1.1).shift(band_shift(2) + UP * 0.0)
        b2_flag = Tex(r"bracket $\neq (x+y)$ — dead end").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_wrong))
        self.wait(2)
        self.play(Create(strike(b2_wrong)))
        self.play(Write(b2_flag))
        self.wait(2.5)
        b2_right = MathTex(r"-bx - by = -b(x + y)").scale(1.15).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_right))
        self.play(Create(SurroundingRectangle(b2_right, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the negative-factor rule
        self.next_band(3)
        b3_rule1 = Tex("Pair begins with a minus?").scale(1.2).shift(band_shift(3) + UP * 2.2)
        b3_rule2 = Tex("Factor out a NEGATIVE common factor").scale(1.2).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_rule1))
        self.play(Write(b3_rule2))
        self.play(Create(SurroundingRectangle(b3_rule2, color=YELLOW)))
        self.wait(2.5)
        b3_now = Tex("The expression now reads:").scale(1.1).shift(band_shift(3) + DOWN * 0.2)
        b3_l1 = MathTex(r"2a(x + y) - b(x + y)").scale(1.2).shift(band_shift(3) + DOWN * 1.2)
        b3_match = Tex("Matching brackets — move three is open").scale(1.05).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_now))
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_match))
        self.wait(3)

        # --- Band 4 (subtopic_3): factor out the common bracket
        self.next_band(4)
        b4_title = Tex("The bracket is a factor too").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Let } K = x + y").scale(1.1).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"2aK - bK = K(2a - b)").scale(1.15).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"2ax + 2ay - bx - by = (x+y)(2a-b)").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): verify by expansion; rearrange stubborn orders
        self.next_band(5)
        b5_title = Tex("Verify by expanding").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"(x+y)(2a-b) = 2ax - bx + 2ay - by").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"All four terms return, signs correct").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex(r"Order refuses to group? Rearrange:").scale(1.05).shift(band_shift(5) + DOWN * 0.9)
        b5_l4 = MathTex(r"2ax - by - bx + 2ay").scale(1.05).shift(band_shift(5) + DOWN * 1.8)
        b5_l5 = MathTex(r"\Rightarrow\; 2ax + 2ay - bx - by").scale(1.05).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l3))
        self.wait(1.5)
        self.play(Write(b5_l4))
        self.wait(1.5)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the five-step method
        self.next_band(6)
        b6_title = Tex("The full method").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_s1 = Tex("1. Overall common factor first").scale(1.05).shift(band_shift(6) + UP * 1.2)
        b6_s2 = Tex("2. Pair the four terms, signs attached").scale(1.05).shift(band_shift(6) + UP * 0.4)
        b6_s3 = Tex("3. Factor each pair (minus? take out negative)").scale(1.05).shift(band_shift(6) + DOWN * 0.4)
        b6_s4 = Tex("4. Brackets match? Factor the bracket out").scale(1.05).shift(band_shift(6) + DOWN * 1.2)
        b6_s5 = Tex("5. Expand to verify; factorise fully").scale(1.05).shift(band_shift(6) + DOWN * 2.0)
        for m in (b6_s1, b6_s2, b6_s3, b6_s4, b6_s5):
            self.play(Write(m))
            self.wait(1.5)
        self.wait(2)

        # --- Band 7 (subtopic_4): bonus worked example with -1
        self.next_band(7)
        b7_title = Tex(r"Factorise: $3pq + 6p - q - 2$").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"3pq + 6p = 3p(q + 2)").scale(1.1).shift(band_shift(7) + UP * 1.0)
        b7_l2 = MathTex(r"-q - 2 = -1(q + 2)").scale(1.1).shift(band_shift(7) + UP * 0.1)
        b7_l3 = MathTex(r"3p(q+2) - 1(q+2)").scale(1.1).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = MathTex(r"= (q + 2)(3p - 1)").scale(1.15).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        b7_note = Tex(r"Even $-1$ obeys the negative-factor rule").scale(1.05).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_note))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): sorting the shopping into two bags
        self.next_band(8)
        b8_title = Tex("Sorting the shopping into two bags").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"No single bag holds all four items").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"Bag 1: $2ax,\; 2ay$ — both carry $2a$").scale(1.05).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex(r"Bag 2: $-bx,\; -by$ — both carry $b$").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = MathTex(r"2ax + 2ay = 2a(x + y)").scale(1.1).shift(band_shift(8) + DOWN * 1.7)
        b8_l5 = Tex("The bracket holds the leftovers").scale(1.05).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.wait(2.5)

        # --- Band 9 (subtopic_6): the minus that must come out
        self.next_band(9)
        b9_title = Tex("The minus that must come out").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_wrong = MathTex(r"-bx - by = b(-x - y) \;\text{ — not twins}").scale(1.05).shift(band_shift(9) + UP * 1.0)
        self.play(Write(b9_wrong))
        self.play(Create(strike(b9_wrong)))
        self.wait(2.5)
        b9_right = MathTex(r"-bx - by = -b(x + y) \;\text{ — twins!}").scale(1.05).shift(band_shift(9) + UP * 0.0)
        self.play(Write(b9_right))
        self.wait(2.5)
        b9_rule = Tex("Pair starts with a minus? Take out a negative").scale(1.05).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(b9_rule))
        self.play(Create(SurroundingRectangle(b9_rule, color=YELLOW)))
        self.wait(2)
        b9_warn = Tex("Never rub out signs to force a match").scale(1.05).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_warn))
        self.wait(2.5)

        # --- Band 10 (subtopic_7): the same bracket in both hands
        self.next_band(10)
        b10_title = Tex("The same bracket in both hands").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"\text{Nickname it: } K = x + y").scale(1.05).shift(band_shift(10) + UP * 1.1)
        b10_l2 = MathTex(r"2aK - bK = K(2a - b)").scale(1.1).shift(band_shift(10) + UP * 0.2)
        b10_l3 = MathTex(r"= (x + y)(2a - b)").scale(1.15).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2)
        b10_l4 = Tex("Multiply out — every term comes back").scale(1.05).shift(band_shift(10) + DOWN * 1.8)
        b10_l5 = Tex("Wrong queue? Reshuffle: kin with kin").scale(1.05).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l4))
        self.wait(2)
        self.play(Write(b10_l5))
        self.wait(4)
