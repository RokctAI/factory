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

# Band-layout whiteboard scene. One band per teaching beat, camera moves down,
# nothing is ever removed. Covers all seven subtopics of the session duo:
# Part 1 — Expert (subtopics 1-4), Part 2 — Simplifier (subtopics 5-7),
# band time apportioned to subtopics.json (210/240/220/260/190/190/210 of 1520 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FormalDefinitionAndInversesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the formal definition
        title = Tex("Functions and Inverses").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Function: every input has EXACTLY one output").scale(1.05).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2)
        d2 = MathTex(r"y = 3x - 5: \; 2 \mapsto 1 \;\text{only} \;\checkmark").scale(1.05).shift(DOWN * 0.1)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"y^2 = x: \; 16 \mapsto 4 \;\text{and}\; -4").scale(1.05).shift(DOWN * 1.1)
        self.play(Write(d3))
        self.play(Create(strike(d3)))
        self.wait(2)
        d4 = Tex("Vertical line test: cut twice $=$ not a function").scale(1.0).shift(DOWN * 2.1)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): many-to-one is legal
        self.next_band(1)
        b1_title = Tex("What the definition does NOT forbid").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"y = x^2: \; 4 \mapsto 16 \;\text{and}\; -4 \mapsto 16").scale(1.05).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Two inputs may SHARE an output").scale(1.05).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Many-to-one: legal. One-to-many: illegal.").scale(1.05).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): swap and solve
        self.next_band(2)
        b2_title = Tex("Build the inverse: swap, then solve").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"y = 3x - 5 \;\xrightarrow{\text{swap}}\; x = 3y - 5").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"y = \frac{x + 5}{3}").scale(1.15).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = MathTex(r"\text{Check: } 2 \mapsto 1, \text{ so } 1 \mapsto \tfrac{1+5}{3} = 2 \;\checkmark").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"y = 2x + 8 \;\Rightarrow\; y = \tfrac{1}{2}x - 4 \;\text{(reciprocal gradient)}").scale(0.95).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex(r"$f^{-1}$ is a label, NOT a power").scale(1.05).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_3): the reflection picture
        self.next_band(3)
        b3_title = Tex("The mirror on the diagonal").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"(2; 1) \;\mapsto\; (1; 2)").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("Swapping coordinates reflects across $y = x$").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = MathTex(r"y = 2x + 8: \; (0; 8), (-4; 0) \;\mapsto\; (8; 0), (0; -4)").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("Domain and range trade places").scale(1.05).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_4): restriction
        self.next_band(4)
        b4_title = Tex(r"Inverting $y = x^2$").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"x = y^2 \;\Rightarrow\; y = \pm\sqrt{x}").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.play(Create(strike(b4_l1)))
        self.wait(2)
        b4_l2 = Tex("Two outputs per input — NOT a function").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("Horizontal line test on the original predicts it").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"\text{Restrict } x \geq 0: \; f^{-1}(x) = \sqrt{x}").scale(1.05).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = MathTex(r"y = 3x^2, \; x \leq 0: \; f^{-1}(x) = -\sqrt{\tfrac{x}{3}}").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): one ticket, one prize
        self.next_band(5)
        b5_title = Tex("One code, one snack").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("A working vending machine IS a function").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"y^2 = x: \text{ code } 16 \text{ drops } 4 \text{ AND } -4").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.play(Create(strike(b5_l2)))
        self.wait(2.5)
        b5_l3 = Tex("Slide a vertical line: one input at a time").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex("Two codes, same snack? Still working.").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_6): running the machine backwards
        self.next_band(6)
        b6_title = Tex("Running the machine backwards").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"y = 3x - 5: \;\times 3, \text{ then } -5").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"\text{Reverse: } +5, \text{ then } \div 3").scale(1.05).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"f^{-1}(x) = \frac{x + 5}{3}").scale(1.1).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = MathTex(r"\text{Trial: snack } 1 \to \text{code } 2 \;\checkmark").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_7): the machine that cannot decide
        self.next_band(7)
        b7_title = Tex("The machine that cannot decide").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"\text{Snack } 16: \text{ code } 4 \text{ or } -4?").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex("Horizontal line touches twice: reverse will stall").scale(1.0).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"\text{Keep } x \geq 0: \; f^{-1}(x) = \sqrt{x}").scale(1.05).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = MathTex(r"\text{Keep } x \leq 0: \; f^{-1}(x) = -\sqrt{x}").scale(1.05).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("One arm at a time, the parabola reverses").scale(1.0).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5))
        self.wait(4)
