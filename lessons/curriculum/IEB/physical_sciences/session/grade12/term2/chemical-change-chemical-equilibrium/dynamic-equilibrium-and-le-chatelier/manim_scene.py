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
# Exporter-safe vocabulary only; graphs hand-built from Line/Dot/Tex.
# Write-only reveals.
# Subtopic durations 240/245/240/250/195/200/200 of 1570 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DynamicEquilibriumSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the definitions ---
        title = Tex("Dynamic Equilibrium and Le Chatelier").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("OPEN: exchanges matter and energy").scale(0.95).shift(UP * 1.2)
        b0_l2 = Tex("CLOSED: energy yes, matter no — equilibrium's home").scale(0.9).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2.5)
        b0_l3 = Tex("EQUILIBRIUM: forward rate $=$ reverse rate,").scale(0.9).shift(DOWN * 0.6)
        b0_l4 = Tex("concentrations constant — but traffic never stops").scale(0.9).shift(DOWN * 1.4)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_wrong = Tex("The reaction has stopped").scale(0.95).shift(DOWN * 2.4)
        self.play(Write(b0_wrong))
        self.play(Create(strike(b0_wrong)))
        self.wait(3)

        # --- Band 1 (subtopic_2): Le Chatelier — concentration + temperature ---
        self.next_band(1)
        b1_title = Tex("Oppose the disturbance").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_eq = MathTex(r"2SO_2 + O_2 \rightleftharpoons 2SO_3 \; (+\,\text{heat})").scale(1.0).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_eq))
        self.play(Create(SurroundingRectangle(b1_eq, color=GREEN)))
        self.wait(2.5)
        b1_l1 = Tex("add O$_2$: system consumes it — shift RIGHT").scale(0.9).shift(band_shift(1) + UP * 0.2)
        b1_l2 = Tex("remove SO$_3$: system replaces it — shift RIGHT").scale(0.9).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("heat it: endothermic reverse favoured — yield falls").scale(0.9).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("cool it: exothermic forward favoured — more SO$_3$").scale(0.9).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): pressure + catalyst ---
        self.next_band(2)
        b2_title = Tex("Pressure counts gas moles").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex("left: 3 gas moles; right: 2").scale(0.95).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("squeeze: shift to FEWER moles — right").scale(0.95).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex("equal moles both sides: pressure shifts nothing").scale(0.9).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_wrong = Tex("A catalyst raises the yield").scale(0.95).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l4 = Tex("both directions faster equally: sooner, never more").scale(0.9).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_3): concentration-time graph, hand-built ---
        self.next_band(3)
        b3_title = Tex("Jumps, curves, flats").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        o3 = band_shift(3) + LEFT * 5.0 + DOWN * 2.2
        ax3x = Line(o3, o3 + RIGHT * 8.5)
        ax3y = Line(o3, o3 + UP * 3.8)
        self.play(Create(ax3x), Create(ax3y))
        # O2 line: flat, jump up, curve back down to new flat
        o2a = Line(o3 + UP * 1.2, o3 + RIGHT * 3.0 + UP * 1.2, color=BLUE)
        o2jump = Line(o3 + RIGHT * 3.0 + UP * 1.2, o3 + RIGHT * 3.0 + UP * 2.8, color=BLUE)
        o2b = Line(o3 + RIGHT * 3.0 + UP * 2.8, o3 + RIGHT * 5.5 + UP * 2.2, color=BLUE)
        o2c = Line(o3 + RIGHT * 5.5 + UP * 2.2, o3 + RIGHT * 8.0 + UP * 2.2, color=BLUE)
        self.play(Create(o2a))
        self.wait(1.5)
        self.play(Create(o2jump))
        self.wait(1.5)
        self.play(Create(o2b), Create(o2c))
        self.wait(2)
        # SO3 line: flat, then rises to new flat
        s3a = Line(o3 + UP * 2.0, o3 + RIGHT * 3.0 + UP * 2.0, color=GREEN)
        s3b = Line(o3 + RIGHT * 3.0 + UP * 2.0, o3 + RIGHT * 5.5 + UP * 2.6, color=GREEN)
        s3c = Line(o3 + RIGHT * 5.5 + UP * 2.6, o3 + RIGHT * 8.0 + UP * 2.6, color=GREEN)
        self.play(Create(s3a), Create(s3b), Create(s3c))
        self.wait(2)
        b3_l1 = Tex("one line jumps: concentration disturbance").scale(0.85).shift(band_shift(3) + RIGHT * 2.2 + UP * 1.3)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): identify the disturbance ---
        self.next_band(4)
        b4_title = Tex("Identify the disturbance by its signature").scale(1.0).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex("one line jumps: concentration").scale(0.95).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex("all gas lines jump: volume / pressure").scale(0.95).shift(band_shift(4) + UP * 0.2)
        b4_l3 = Tex("no jump, curves bend: temperature").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex("both RATE lines leap together: catalyst").scale(0.95).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): K_c worked calculation ---
        self.next_band(5)
        b5_title = Tex("$K_c$: H$_2$ + I$_2$ $\\rightleftharpoons$ 2HI, 4 dm$^3$").scale(1.0).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("in: 2,0 and 2,0 mol; at eq: 3,0 mol HI").scale(0.9).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("change: $-$1,5 and $-$1,5; remain: 0,5 each").scale(0.9).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"[H_2] = [I_2] = 0{,}125; \;\; [HI] = 0{,}75").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"K_c = \frac{0{,}75^2}{0{,}125 \times 0{,}125} = 36").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): interpreting K_c ---
        self.next_band(6)
        b6_title = Tex("Reading $K_c$").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("$K_c \\gg 1$: products dominate").scale(0.95).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("$K_c \\ll 1$: mostly reactants remain").scale(0.95).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("solids and pure liquids never enter the expression").scale(0.85).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("only TEMPERATURE changes $K_c$").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the shop with the steady crowd ---
        self.next_band(7)
        b7_title = Tex("The shop where the crowd never changes").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("30 in per minute, 30 out — crowd stuck at 150").scale(0.9).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex("count constant, doors churning: DYNAMIC").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("steady crowd can be 15 or 1 500: constant $\\neq$ equal").scale(0.85).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = Tex("missing back wall $=$ open system: no balance possible").scale(0.85).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (subtopic_6): the stubborn see-saw ---
        self.next_band(8)
        b8_title = Tex("The stubborn see-saw").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        # See-saw sketch
        base8 = band_shift(8) + DOWN * 0.2
        plank = Line(base8 + LEFT * 3.0 + UP * 0.5, base8 + RIGHT * 3.0 + DOWN * 0.1)
        pivot = Dot(base8, radius=0.12)
        self.play(Create(plank), FadeIn(pivot))
        self.wait(2)
        b8_l1 = Tex("every push is answered by a lean the other way").scale(0.9).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("heat is a passenger: write it into the equation").scale(0.9).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("partly undone, never fully undone").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): the referee with the scoreboard ---
        self.next_band(9)
        b9_title = Tex("The referee with the scoreboard").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("score: products over reactants, powers from coefficients").scale(0.85).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("in, change, remain — then DIVIDE by the volume").scale(0.9).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex("huge score: products won. tiny score: barely started.").scale(0.85).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("the referee answers to TEMPERATURE alone").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(4)
