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

# Band-layout whiteboard scene: sequential vertical bands, one per teaching
# beat, camera moves down between bands, add-only lifecycle. Exporter-safe
# mobjects only (Tex/MathTex/Line/Rectangle); every working line is a
# single-string MathTex revealed with Write. Covers all seven subtopics of
# the duo (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7); band time
# apportioned to subtopics.json (225/240/230/255/195/210/225 of 1580 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FundamentalCountingPrincipleSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the principle — choices multiply
        title = Tex("The Fundamental Counting Principle").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex(r"Task 1 in $m$ ways, task 2 in $n$ ways for EACH:").scale(1.05).shift(UP * 0.9)
        s0_l2 = MathTex(r"\text{together: } m \times n \text{ ways}").scale(1.2).shift(UP * 0.0)
        self.play(Write(s0_l1))
        self.play(Write(s0_l2))
        self.wait(2.5)
        s0_l3 = MathTex(r"5 \text{ shirts} \times 2 \text{ jeans} = 10 \text{ outfits}").scale(1.1).shift(DOWN * 1.1)
        s0_l4 = MathTex(r"\times\, 3 \text{ caps} = 30 \text{ complete outfits}").scale(1.1).shift(DOWN * 2.0)
        self.play(Write(s0_l3))
        self.wait(2)
        self.play(Write(s0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the slot method; multiply along, add across
        self.next_band(1)
        b1_title = Tex("Draw the slots").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        slot_xs = [-1.6, 0.0, 1.6]
        slot_ns = ["4", "6", "3"]
        slot_lines = [Line(band_shift(1) + UP * 0.8 + RIGHT * (x - 0.45),
                           band_shift(1) + UP * 0.8 + RIGHT * (x + 0.45),
                           stroke_width=4) for x in slot_xs]
        slot_nums = [MathTex(n).scale(1.2).move_to(band_shift(1) + UP * 1.3 + RIGHT * x)
                     for x, n in zip(slot_xs, slot_ns)]
        self.play(Create(slot_lines[0]), Create(slot_lines[1]), Create(slot_lines[2]))
        self.play(Write(slot_nums[0]), Write(slot_nums[1]), Write(slot_nums[2]))
        self.wait(2)
        b1_l2 = MathTex(r"4 \times 6 \times 3 = 72 \text{ meals}").scale(1.15).shift(band_shift(1) + DOWN * 0.2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex(r"Multiply along a sequence of decisions").scale(1.05).shift(band_shift(1) + DOWN * 1.2)
        b1_l4 = Tex(r"Add only across exclusive cases (bus OR cycle)").scale(1.05).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): arrangements and the factorial
        self.next_band(2)
        b2_title = Tex("Five debaters take their seats in a row").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        p_xs = [-2.4, -1.2, 0.0, 1.2, 2.4]
        p_ns = ["5", "4", "3", "2", "1"]
        p_lines = [Line(band_shift(2) + UP * 0.8 + RIGHT * (x - 0.4),
                        band_shift(2) + UP * 0.8 + RIGHT * (x + 0.4),
                        stroke_width=4) for x in p_xs]
        p_nums = [MathTex(n).scale(1.1).move_to(band_shift(2) + UP * 1.3 + RIGHT * x)
                  for x, n in zip(p_xs, p_ns)]
        self.play(Create(p_lines[0]), Create(p_lines[1]), Create(p_lines[2]),
                  Create(p_lines[3]), Create(p_lines[4]))
        self.play(Write(p_nums[0]), Write(p_nums[1]), Write(p_nums[2]),
                  Write(p_nums[3]), Write(p_nums[4]))
        self.wait(2)
        b2_l2 = MathTex(r"5! = 5 \times 4 \times 3 \times 2 \times 1 = 120").scale(1.1).shift(band_shift(2) + DOWN * 0.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex(r"$n$ distinct objects: $n!$ arrangements").scale(1.1).shift(band_shift(2) + DOWN * 1.2)
        b2_l4 = Tex(r"Options shrink — arrangement forbids reuse").scale(1.05).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): restrictions — forced, glued, complement
        self.next_band(3)
        b3_title = Tex("Fussy first, glue for together, complement for apart").scale(1.0).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\text{Right end forced: } 1 \times 4! = 24").scale(1.1).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"\text{Two together (glue): } 4! \times 2 = 48").scale(1.1).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{Two apart: } 120 - 48 = 72").scale(1.1).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex(r"The complement is often the fastest route").scale(1.05).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): codes — ask about repetition first
        self.next_band(4)
        b4_title = Tex("Codes: may symbols repeat?").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{5-digit code, repetition allowed: } 10^5 = 100\,000").scale(1.05).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"\text{Repetition forbidden: } 10 \times 9 \times 8 \times 7 \times 6 = 30\,240").scale(1.0).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex(r"Same slots, different discipline —").scale(1.05).shift(band_shift(4) + DOWN * 1.2)
        b4_l4 = Tex(r"over two thirds of the codes gone").scale(1.05).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): restricted slots first; letters of a word
        self.next_band(5)
        b5_title = Tex("Restricted slots are filled first").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{Non-zero digit + 2 different letters: } 9 \times 26 \times 25 = 5\,850").scale(0.95).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex(r"May not start with 0: first slot drops to 9").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\text{STAR: 4 distinct letters} \Rightarrow 4! = 24").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = MathTex(r"\text{Begins with S: } 1 \times 3! = 6").scale(1.05).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): probability by counting — the code case
        self.next_band(6)
        b6_title = Tex("Probability by counting").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"P(\text{event}) = \frac{\text{favourable}}{\text{total}}").scale(1.15).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=YELLOW)))
        self.wait(2.5)
        b6_l2 = Tex(r"Random code: all five digits different?").scale(1.05).shift(band_shift(6) + DOWN * 0.2)
        b6_l3 = MathTex(r"P = \frac{30\,240}{100\,000} = 0{,}3024").scale(1.15).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex(r"Under a third — repeats sneak in easily").scale(1.05).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): cousins together; STAR begins with S
        self.next_band(7)
        b7_title = Tex("The same machine, run twice").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"P(\text{cousins together}) = \frac{48}{120} = \frac{2}{5}").scale(1.1).shift(band_shift(7) + UP * 1.0)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"P(\text{separated}) = 1 - \frac{2}{5} = \frac{3}{5}").scale(1.1).shift(band_shift(7) + UP * 0.0)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"P(\text{STAR begins with S}) = \frac{6}{24} = 0{,}25").scale(1.05).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex(r"Shortcut view: one fair pick among 4 letters").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): outfits from a small cupboard
        self.next_band(8)
        b8_title = Tex("Outfits from a small cupboard").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_wrong = MathTex(r"5 \text{ shirts} + 2 \text{ jeans} = 7?").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_wrong))
        self.play(Create(strike(b8_wrong)))
        self.wait(2)
        b8_l1 = MathTex(r"5 \times 2 = 10 \text{ outfits}, \;\; \times 3 \text{ caps} = 30").scale(1.05).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l1))
        self.play(Create(SurroundingRectangle(b8_l1, color=GREEN)))
        self.wait(2.5)
        b8_l2 = MathTex(r"\text{Canteen: } 4 \times 6 \times 3 = 72 \text{ lunches}").scale(1.05).shift(band_shift(8) + DOWN * 1.0)
        b8_l3 = MathTex(r"\text{Combo OR lunchbox: } 72 + 4 = 76").scale(1.05).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(3)

        # --- Band 9 (subtopic_6): the class photo and the glued friends
        self.next_band(9)
        b9_title = Tex("The class photo and the glued friends").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"5 \times 4 \times 3 \times 2 \times 1 = 5! = 120").scale(1.1).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\text{Captain at right end: } 1 \times 4! = 24").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\text{Invisible string: } 4! \times 2 = 48").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"\text{Kept apart: } 120 - 48 = 72").scale(1.05).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        b9_l5 = Tex(r"Fussy first, string for together, subtract for apart").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): what are the chances, counted
        self.next_band(10)
        b10_title = Tex("What are the chances, counted").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"P(\text{code, all different}) = \frac{30\,240}{100\,000} = 0{,}3024").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"P(\text{cousins together}) = \frac{48}{120} = \frac{2}{5}").scale(1.05).shift(band_shift(10) + UP * 0.0)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"P(\text{apart}) = \frac{3}{5}, \quad P(\text{S first}) = 0{,}25").scale(1.0).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"Count the world, count your wish, divide").scale(1.1).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(4)
