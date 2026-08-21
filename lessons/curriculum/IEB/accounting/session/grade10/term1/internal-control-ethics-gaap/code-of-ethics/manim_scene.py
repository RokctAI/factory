# Copyright (c) 2026 RokctAI
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

# Band-layout whiteboard scene for the session duo "Code of Ethics"
# (grade10 term1, internal-control-ethics-gaap). One band per teaching beat,
# camera moves down to fresh space, nothing is ever removed. Exporter-safe
# vocabulary only: Tex/MathTex/Line/Rectangle/SurroundingRectangle/VGroup,
# single-string Tex lines revealed with Write — no sub-part transforms.
#
# Subtopic time shares (subtopics.json, total 1240 s):
# 170/190/190/170/170/180/170 -> bands 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CodeOfEthicsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(13)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): what a code of ethics is ---
        title = Tex("The Code of Ethics").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Money gathers temptation").scale(1.1).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("A formal, written statement of the").scale(1.1).shift(UP * 0.3)
        b0_l3 = Tex("values and standards of behaviour").scale(1.1).shift(DOWN * 0.5)
        b0_l4 = Tex("a business commits itself to").scale(1.1).shift(DOWN * 1.3)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(VGroup(b0_l2, b0_l3, b0_l4), color=GREEN)))
        self.wait(2.5)
        b0_l5 = Tex("Binds ALL parties: owner, managers,").scale(1.05).shift(DOWN * 2.2)
        b0_l6 = Tex("bookkeepers, staff, suppliers, the state").scale(1.05).shift(DOWN * 3.0)
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): trust is the precondition ---
        self.next_band(1)
        b1_title = Tex("Why Accounting insists on it").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Figures have value only if").scale(1.1).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("they can be TRUSTED").scale(1.1).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        box1 = SurroundingRectangle(VGroup(b1_l1, b1_l2), color=YELLOW)
        self.play(Create(box1))
        self.wait(2.5)
        b1_l3 = Tex("Bent records = decoration, not information").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Internal control: dishonesty made difficult").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        b1_l5 = Tex("Ethics: dishonesty made unwanted").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): characteristics 1-4 ---
        self.next_band(2)
        b2_title = Tex("Seven characteristics — first four").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Leadership — the example set from the top").scale(0.95).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex("Discipline — rules followed consistently").scale(0.95).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex("Transparency — records open to those entitled").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex("Accountability — answering for your actions").scale(0.95).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l1))
        self.wait(1.5)
        self.play(Write(b2_l2))
        self.wait(1.5)
        self.play(Write(b2_l3))
        self.wait(1.5)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Definition + one-line example = the marks").scale(0.95).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): characteristics 5-7 and the overlaps ---
        self.next_band(3)
        b3_title = Tex("Last three — and the overlaps").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Fairness — no favouritism, no advantage taken").scale(0.95).shift(band_shift(3) + UP * 1.3)
        b3_l2 = Tex("Sustainability — no profit today that").scale(0.95).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex("destroys profit tomorrow").scale(0.95).shift(band_shift(3) + DOWN * 0.3)
        b3_l4 = Tex("Responsible management — careful stewardship").scale(0.95).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3_l1))
        self.wait(1.5)
        self.play(Write(b3_l2))
        self.play(Write(b3_l3))
        self.wait(1.5)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Leadership breeds discipline;").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        b3_l6 = Tex("transparency enables accountability").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(VGroup(b3_l5, b3_l6), color=YELLOW)))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): scenario one worked in full ---
        self.next_band(4)
        b4_title = Tex("Scenario: hide the Saturday sales").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Mokoena Hardware: owner orders sales").scale(0.95).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("left out of the records to cut tax").scale(0.95).shift(band_shift(4) + UP * 0.6)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("Owner: leadership + fairness breached").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex("Bookkeeper who obeys: discipline,").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        b4_l5 = Tex("accountability — and reliability lost").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l3))
        self.wait(1.5)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2)
        b4_l6 = Tex("False in one corner = suspect in every corner").scale(0.9).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l6, color=RED)))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): scenarios two and three ---
        self.next_band(5)
        b5_title = Tex("Two more scenarios").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Second-hand parts sold as new:").scale(0.95).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("transparency, fairness, responsible mgmt").scale(0.95).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("Runoff piped into the stream:").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("sustainability, first and loudest").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("The pattern: small certain gain now,").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        b5_l6 = Tex("large uncertain loss later").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(VGroup(b5_l5, b5_l6), color=YELLOW)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the four-move method ---
        self.next_band(6)
        b6_title = Tex("The four-move method").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("1. State the issue in plain words").scale(1.0).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex("2. Name the characteristic at stake").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("3. Argue the link: definition to scenario").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("4. Consequence and correction").scale(1.0).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l1))
        self.wait(1.5)
        self.play(Write(b6_l2))
        self.wait(1.5)
        self.play(Write(b6_l3))
        self.wait(1.5)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(VGroup(b6_l1, b6_l2, b6_l3, b6_l4), color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the two mark-losing errors ---
        self.next_band(7)
        b7_title = Tex("Two ways to lose the marks").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("``This is dishonest and wrong''").scale(1.0).shift(band_shift(7) + UP * 1.0)
        self.play(Write(b7_l1))
        self.play(Create(strike(b7_l1)))
        b7_l2 = Tex("Moralising without naming").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("``Transparency, accountability, fairness''").scale(1.0).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.play(Create(strike(b7_l3)))
        b7_l4 = Tex("Naming without applying").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Every name tied to a fact of the scenario").scale(0.95).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the captain picture ---
        self.next_band(8)
        b8_title = Tex("One captain, seven characteristics").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("Trains hardest, asks nothing extra — leadership").scale(0.9).shift(band_shift(8) + UP * 1.4)
        b8_l2 = Tex("On time, every practice — discipline").scale(0.9).shift(band_shift(8) + UP * 0.6)
        b8_l3 = Tex("Explains the line-up openly — transparency").scale(0.9).shift(band_shift(8) + DOWN * 0.2)
        b8_l4 = Tex("Owns the defeat first — accountability").scale(0.9).shift(band_shift(8) + DOWN * 1.0)
        b8_l5 = Tex("Same chance for the new player — fairness").scale(0.9).shift(band_shift(8) + DOWN * 1.8)
        b8_l6 = Tex("Never wins by cheating — sustainability").scale(0.9).shift(band_shift(8) + DOWN * 2.6)
        b8_l7 = Tex("Minds the kit and fixtures — responsible mgmt").scale(0.9).shift(band_shift(8) + DOWN * 3.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3.5)

        # --- Band 9 (subtopic_6): ethics at the till ---
        self.next_band(9)
        b9_title = Tex("Ethics at the till — three moments").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(1.5)
        b9_l1 = Tex("Double-charged loaf, checked and refunded:").scale(0.9).shift(band_shift(9) + UP * 1.4)
        b9_l2 = Tex("accountability, fairness, transparency").scale(0.9).shift(band_shift(9) + UP * 0.6)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("``Cash, no paperwork'' quote:").scale(0.9).shift(band_shift(9) + DOWN * 0.3)
        b9_l4 = Tex("transparency and accountability traded away").scale(0.9).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Half-price stock, no questions asked:").scale(0.9).shift(band_shift(9) + DOWN * 2.0)
        b9_l6 = Tex("sustainability says the real asset is trust").scale(0.9).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=YELLOW)))
        self.wait(2.5)

        # --- Band 10 (subtopic_7): good ethics is good business ---
        self.next_band(10)
        b10_title = Tex("Good ethics is good business").scale(1.2).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_title))
        self.wait(1.5)
        b10_l1 = Tex("Fairness $\\rightarrow$ loyal clients").scale(0.95).shift(band_shift(10) + UP * 1.3)
        b10_l2 = Tex("Transparency $\\rightarrow$ bank credit").scale(0.95).shift(band_shift(10) + UP * 0.5)
        b10_l3 = Tex("Discipline $\\rightarrow$ supplier terms").scale(0.95).shift(band_shift(10) + DOWN * 0.3)
        b10_l4 = Tex("Sustainability $\\rightarrow$ still standing in ten years").scale(0.95).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex("Ethics protects from dishonesty's costs").scale(0.95).shift(band_shift(10) + DOWN * 2.1)
        b10_l6 = Tex("AND earns the profits of being trusted").scale(0.95).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(VGroup(b10_l5, b10_l6), color=GREEN)))
        self.wait(3.5)
