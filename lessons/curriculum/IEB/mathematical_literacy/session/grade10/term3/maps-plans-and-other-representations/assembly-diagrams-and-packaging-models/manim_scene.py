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

# Band-layout whiteboard scene for the Assembly Diagrams and Packaging Models
# session duo. One band per teaching beat, camera moves down between bands,
# add-only lifecycle. Exporter-supported mobjects only; every working line is
# a single-string Tex/MathTex revealed with Write. Band time apportioned to
# subtopics.json (220/220/230/260/190/180/180 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AssemblyDiagramsAndPackagingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the parts list ---
        title = Tex("Assembly Diagrams and Packaging").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_h = Tex("The parts list — check it first").scale(1.1).shift(UP * 1.4)
        self.play(Write(b0_h))
        self.wait(1.5)
        b0_l1 = Tex("A: side panel $\\times$2 \\quad B: shelf $\\times$3").scale(1.0).shift(UP * 0.5)
        b0_l2 = Tex("C: bracket $\\times$6 \\quad D: screw $\\times$24").scale(1.0).shift(DOWN * 0.4)
        b0_l3 = Tex("E: back board $\\times$1").scale(1.0).shift(DOWN * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Count the contents against the list before starting").scale(0.95).shift(DOWN * 2.2)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): symbols of the diagram ---
        self.next_band(1)
        b1_t = Tex("The diagram's language").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("Numbered circle: a step — follow in order").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("Curved arrow: turn to tighten").scale(1.0).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex("Magnified circle: the detail everyone gets wrong").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = Tex("Crossed-out picture: the mistake to avoid").scale(1.0).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_rule = Tex("Step 3: fix C to A = a bracket to a side panel").scale(0.95).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_rule))
        self.play(Create(SurroundingRectangle(b1_rule, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the quantity chain ---
        self.next_band(2)
        b2_t = Tex("The quantity chain").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"3 \text{ shelves} \times 2 = 6 \text{ brackets}").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"6 \text{ brackets} \times 4 = 24 \text{ screws}").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("The list interlocks — every screw has a bracket").scale(0.95).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the short packet ---
        self.next_band(3)
        b3_t = Tex("Only 21 screws in the packet").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"21 \div 4 = 5 \text{ complete brackets, 1 left over}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"\text{Missing: } 24 - 21 = 3 \text{ screws}").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("Packets of 8 at R22: buy 1 packet — round UP").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex("Misprint check: 20 screws listed? Chain says 24").scale(0.95).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): packing the small box ---
        self.next_band(4)
        b4_t = Tex("Jars of 8 cm in a 32 $\\times$ 24 $\\times$ 10 box").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_t))
        self.wait(1.5)
        grid = Rectangle(width=6.4, height=4.8).shift(band_shift(4) + DOWN * 0.4 + LEFT * 2.8)
        self.play(Create(grid))
        self.wait(1)
        b4_l1 = MathTex(r"32 \div 8 = 4 \text{ along}").scale(0.95).shift(band_shift(4) + UP * 1.3 + RIGHT * 3.4)
        b4_l2 = MathTex(r"24 \div 8 = 3 \text{ across}").scale(0.95).shift(band_shift(4) + UP * 0.4 + RIGHT * 3.4)
        b4_l3 = MathTex(r"4 \times 3 = 12 \text{ per layer}").scale(0.95).shift(band_shift(4) + DOWN * 0.5 + RIGHT * 3.4)
        b4_l4 = MathTex(r"10 \div 10 = 1 \text{ layer}").scale(0.95).shift(band_shift(4) + DOWN * 1.4 + RIGHT * 3.4)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_ans = Tex("Capacity: 12 jars").scale(1.05).shift(band_shift(4) + DOWN * 2.6 + RIGHT * 3.4)
        self.play(Write(b4_ans))
        self.play(Create(SurroundingRectangle(b4_ans, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the big box and the rules ---
        self.next_band(5)
        b5_t = Tex("The 40 $\\times$ 32 $\\times$ 20 box").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"40 \div 8 = 5 \quad 32 \div 8 = 4 \quad 20 \div 10 = 2").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"5 \times 4 \times 2 = 40 \text{ jars}").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_wrong = Tex("Box volume $\\div$ jar volume").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l3 = Tex("35 cm long? Still 4 jars — fitting rounds DOWN").scale(0.95).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l3))
        self.wait(3)

        # --- Band 6 (subtopic_4): cost per jar ---
        self.next_band(6)
        b6_t = Tex("Cost per jar").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Small: R}6{,}00 \div 12 = 50 \text{ c per jar}").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"\text{Large: R}14{,}00 \div 40 = 35 \text{ c per jar}").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_ans = Tex("Per jar, the large box wins by 15 cents").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_ans))
        self.play(Create(SurroundingRectangle(b6_ans, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): cost for the job ---
        self.next_band(7)
        b7_t = Tex("But the job is 15 jars this week").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("One large box: R14,00 — 25 empty spots").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{Two small boxes: } 2 \times 6{,}00 = \text{R}12{,}00").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_ans = Tex("For THIS job the small boxes win by R2,00").scale(1.0).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_ans))
        self.play(Create(SurroundingRectangle(b7_ans, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex("Cheapest per unit $\\ne$ cheapest for the job").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l3))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the recipe picture ---
        self.next_band(8)
        b8_t = Tex("The instruction sheet is a recipe").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Parts list = ingredients — count them first").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Numbered steps = the method — order matters").scale(1.0).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("Zoom circle = pay attention here").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = Tex("Crossed-out picture = the burnt version").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l1, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): eggs in an egg box ---
        self.next_band(9)
        b9_t = Tex("Eggs in an egg box").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Spots along $\\times$ spots across $\\times$ storeys").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"4 \times 3 \times 1 = 12 \qquad 5 \times 4 \times 2 = 40").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Leftover space is nothing — round DOWN").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("BUYING rounds up; FITTING rounds down").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): best box for the job ---
        self.next_band(10)
        b10_t = Tex("Big box, small box, best box").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Per jar: 50 c vs 35 c — big box wins").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("For 15 jars: R12,00 vs R14,00 — small boxes win").scale(1.0).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Bulk is only a deal if you use the bulk").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2)
        b10_l4 = Tex("Practical factor: weight, and rattling empty spots").scale(0.95).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l4))
        self.wait(4)
