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

# Band-layout whiteboard scene for "Dynamic Equilibrium and Le Chatelier"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only; the concentration-time graph is hand-built
# from Arrow axes and Line segments. Write-only reveals.
# Subtopic durations 240/245/240/250/195/200/200 of 1570 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DynamicEquilibriumLeChatelierSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the definitions ---
        title = Tex("Dynamic Equilibrium and Le Chatelier").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Open: exchanges matter AND energy").scale(1.0).shift(UP * 1.3)
        b0_l2 = Tex("Closed: energy only — equilibrium needs this").scale(1.0).shift(UP * 0.5)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("Equilibrium: forward rate $=$ reverse rate,").scale(1.0).shift(DOWN * 0.4)
        b0_l4 = Tex("concentrations constant (NOT equal!)").scale(1.0).shift(DOWN * 1.2)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2.5)
        b0_wrong = Tex("``The reaction has stopped''").scale(1.05).shift(DOWN * 2.2)
        self.play(Write(b0_wrong))
        self.play(Create(strike(b0_wrong)))
        self.wait(2)
        b0_l5 = Tex("DYNAMIC: both reactions run at full tilt").scale(1.0).shift(DOWN * 3.1)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_2): Le Chatelier — concentration + temperature ---
        self.next_band(1)
        b1_title = Tex("Le Chatelier: oppose the disturbance").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_eq = MathTex(r"N_2 + 3H_2 \rightleftharpoons 2NH_3 + \text{heat}").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_eq))
        self.wait(2.5)
        b1_l1 = Tex("Add $N_2$: system consumes it — forward").scale(1.0).shift(band_shift(1) + UP * 0.2)
        b1_l2 = Tex("Remove $NH_3$: system remakes it — forward").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Heat it: endothermic reverse favoured,").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        b1_l4 = Tex("yield falls (and $K_c$ itself changes)").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): pressure + catalyst ---
        self.next_band(2)
        b2_title = Tex("Pressure and the catalyst").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Count gas moles: 4 left, 2 right").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("Squeeze: shifts to FEWER moles — forward").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("Equal moles both sides: pressure does nothing").scale(0.95).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("Catalyst: speeds BOTH equally —").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        b2_l5 = Tex("equilibrium sooner, yield unchanged").scale(1.05).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): concentration-time graph, hand-built ---
        self.next_band(3)
        b3_title = Tex("Add $N_2$ at time $t$: the graph").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        o3 = band_shift(3) + LEFT * 4.8 + DOWN * 1.6
        ax3_t = Arrow(o3 + LEFT * 0.2, o3 + RIGHT * 7.6, buff=0, stroke_width=3)
        ax3_c = Arrow(o3 + DOWN * 0.2, o3 + UP * 3.6, buff=0, stroke_width=3)
        lab3_t = Tex("$t$").scale(0.9).shift(o3 + RIGHT * 7.8 + DOWN * 0.3)
        lab3_c = Tex("conc.").scale(0.85).shift(o3 + UP * 3.6 + LEFT * 0.7)
        self.play(Create(ax3_t), Create(ax3_c))
        self.play(Write(lab3_t), Write(lab3_c))
        self.wait(1.5)
        n2_flat = Line(o3 + UP * 1.5, o3 + RIGHT * 2.0 + UP * 1.5, color=YELLOW)
        n2_jump = Line(o3 + RIGHT * 2.0 + UP * 1.5, o3 + RIGHT * 2.0 + UP * 2.8, color=RED)
        self.play(Create(n2_flat))
        self.play(Create(n2_jump))
        lab_jump = Tex("jump $=$ injection").scale(0.8).shift(o3 + RIGHT * 3.6 + UP * 3.1)
        self.play(Write(lab_jump))
        self.wait(2)
        n2_curve = VGroup(
            Line(o3 + RIGHT * 2.0 + UP * 2.8, o3 + RIGHT * 3.2 + UP * 2.2, color=YELLOW),
            Line(o3 + RIGHT * 3.2 + UP * 2.2, o3 + RIGHT * 4.4 + UP * 2.0, color=YELLOW),
            Line(o3 + RIGHT * 4.4 + UP * 2.0, o3 + RIGHT * 7.0 + UP * 2.0, color=YELLOW),
        )
        self.play(Create(n2_curve), run_time=2)
        lab_n2 = MathTex(r"N_2").scale(0.8).shift(o3 + RIGHT * 7.3 + UP * 2.0)
        self.play(Write(lab_n2))
        self.wait(1.5)
        nh3_line = VGroup(
            Line(o3 + UP * 0.7, o3 + RIGHT * 2.0 + UP * 0.7, color=BLUE),
            Line(o3 + RIGHT * 2.0 + UP * 0.7, o3 + RIGHT * 3.2 + UP * 1.0, color=BLUE),
            Line(o3 + RIGHT * 3.2 + UP * 1.0, o3 + RIGHT * 4.4 + UP * 1.2, color=BLUE),
            Line(o3 + RIGHT * 4.4 + UP * 1.2, o3 + RIGHT * 7.0 + UP * 1.2, color=BLUE),
        )
        self.play(Create(nh3_line), run_time=2)
        lab_nh3 = MathTex(r"NH_3").scale(0.8).shift(o3 + RIGHT * 7.4 + UP * 1.2)
        self.play(Write(lab_nh3))
        self.wait(2)
        b3_note = Tex("New flat levels: a NEW equilibrium").scale(1.0).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_note))
        self.wait(3)

        # --- Band 4 (subtopic_3): identify the disturbance ---
        self.next_band(4)
        b4_title = Tex("Identify the disturbance at time $t$").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("ONE line jumps: concentration change").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex("ALL lines jump: volume or pressure").scale(1.05).shift(band_shift(4) + UP * 0.2)
        b4_l3 = Tex("No jump, curves bend: temperature").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex("Both rates leap together: catalyst").scale(1.05).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2.5)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): K_c worked calculation ---
        self.next_band(5)
        b5_title = MathTex(r"H_2 + I_2 \rightleftharpoons 2HI \;\; (2\ \text{dm}^3)").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("In: 1,0 mol each. At eq: 1,6 mol $HI$").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("Change: $-0,8$ and $-0,8$; remain 0,2 each").scale(1.0).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\div 2\ \text{dm}^3: \; 0{,}1; \;\; 0{,}1; \;\; 0{,}8").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"K_c = \frac{[HI]^2}{[H_2][I_2]} = \frac{0{,}64}{0{,}01}").scale(1.05).shift(band_shift(5) + DOWN * 1.7)
        b5_l5 = MathTex(r"K_c = 64").scale(1.15).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l4))
        self.wait(2.5)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): interpreting K_c ---
        self.next_band(6)
        b6_title = Tex("Reading $K_c$").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Large $K_c$: equilibrium far toward products").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("Small $K_c$: mostly reactants remain").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Solids and pure liquids: never written").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("ONLY temperature changes $K_c$").scale(1.1).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the shop with the steady crowd ---
        self.next_band(7)
        b7_title = Tex("The shop where the crowd never changes").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("40 in per minute, 40 out per minute:").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("crowd constant, doorway churning").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("Steady crowd can be 20 or 2 000:").scale(1.05).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = Tex("constant does not mean equal").scale(1.05).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("A missing back wall (open system):").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        b7_l6 = Tex("no balance can ever form").scale(1.0).shift(band_shift(7) + DOWN * 3.4)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(3)

        # --- Band 8 (subtopic_6): the stubborn see-saw ---
        self.next_band(8)
        b8_title = Tex("The stubborn see-saw").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Push it, and it leans back against you").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Partly undone, never fully undone").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("Trick: write HEAT into the equation").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = Tex("Exothermic: heat sits on the product side").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Catalyst greases the pivot: sooner,").scale(1.0).shift(band_shift(8) + DOWN * 2.6)
        b8_l6 = Tex("never more product").scale(1.0).shift(band_shift(8) + DOWN * 3.4)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_7): the referee with the scoreboard ---
        self.next_band(9)
        b9_title = Tex("The referee's scoreboard: $K_c$").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Huge score: nearly all products").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("Tiny score: barely left the start. 64: product-side").scale(0.95).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Four lines: IN, CHANGE, REMAIN, DIVIDE").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("The referee only accepts concentrations!").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("And he is loyal only to temperature").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(4)
