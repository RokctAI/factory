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

# Band-layout whiteboard scene for gravitational-potential-energy
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe mobjects, add-only lifecycle, one band per teaching beat.
# Time apportioned to subtopics.json (225/235/235/250/180/175/175 of 1475 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GravitationalPotentialEnergySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): energy stored by position ---
        title = Tex("Gravitational Potential Energy").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Energy: the capacity to do work — joules (J)").scale(1.0).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2)
        d2 = Tex("Stored by POSITION in the gravitational field").scale(1.0).shift(UP * 0.0)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"E_p = mgh").scale(1.4).shift(DOWN * 1.2)
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(d3, color=GREEN)))
        self.wait(2.5)
        d4 = Tex("$mg$: the weight; $\\times h$: the lifting bill").scale(1.0).shift(DOWN * 2.4)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_2): pricing the 3 m lift ---
        self.next_band(1)
        b1t = Tex("Pricing the lift: 4 kg to 3 m").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = MathTex(r"E_p = 4 \times 9{,}8 \times 3").scale(1.1).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1a))
        self.wait(2)
        b1b = MathTex(r"4 \times 9{,}8 = 39{,}2 \text{ N (the weight)}").scale(1.0).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1b))
        self.wait(2.5)
        b1c = MathTex(r"39{,}2 \times 3 = 117{,}6 \text{ J}").scale(1.15).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1c))
        self.play(Create(SurroundingRectangle(b1c, color=GREEN)))
        self.wait(2.5)
        b1d = Tex("kg $\\times$ m/s$^2$ $\\times$ m $=$ N$\\cdot$m $=$ J").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1d))
        self.wait(3)

        # --- Band 2 (subtopic_2): the second platform ---
        self.next_band(2)
        b2t = Tex("The higher platform: 10 m").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = MathTex(r"E_p(10) = 4 \times 9{,}8 \times 10 = 392 \text{ J}").scale(1.0).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2a))
        self.wait(2.5)
        b2b = MathTex(r"\text{Further gain} = 392 - 117{,}6 = 274{,}4 \text{ J}").scale(1.0).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = MathTex(r"\text{Shorter road: } 39{,}2 \times 7 = 274{,}4 \text{ J}").scale(1.0).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2c))
        self.play(Create(SurroundingRectangle(b2c, color=GREEN)))
        self.wait(2.5)
        b2d = Tex("Only the height CHANGE matters").scale(1.05).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2d))
        self.wait(3)

        # --- Band 3 (subtopic_3): the reference level, drawn ---
        self.next_band(3)
        b3t = Tex("Where zero lives").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        g = band_shift(3) + DOWN * 0.4
        ground = Line(g + LEFT * 4.5, g + RIGHT * 4.5, stroke_width=4)
        self.play(Create(ground))
        cellar = Line(g + LEFT * 4.5 + DOWN * 1.2, g + RIGHT * 0.0 + DOWN * 1.2, stroke_width=3, color=GREY)
        self.play(Create(cellar))
        plat = Line(g + RIGHT * 1.0 + UP * 1.8, g + RIGHT * 3.0 + UP * 1.8, stroke_width=4, color=YELLOW)
        self.play(Create(plat))
        tin = Dot(g + RIGHT * 2.0 + UP * 1.95, radius=0.1)
        self.play(Create(tin))
        self.wait(2)
        l1 = Tex("Ground zero: $h = 3$, $E_p = 117{,}6$ J").scale(0.85).shift(band_shift(3) + UP * 1.6 + LEFT * 2.5)
        self.play(Write(l1))
        self.wait(2.5)
        l2 = Tex("Cellar zero: $h = 5$, $E_p = 196$ J").scale(0.85).shift(band_shift(3) + DOWN * 2.2 + LEFT * 2.0)
        self.play(Write(l2))
        self.wait(3)

        # --- Band 4 (subtopic_3): two bookkeepers agree on differences ---
        self.next_band(4)
        b4t = Tex("Two bookkeepers, one payout").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = MathTex(r"\text{Ground: } 117{,}6 - 0 = 117{,}6 \text{ J}").scale(1.0).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4a))
        self.wait(2.5)
        b4b = MathTex(r"\text{Cellar: } 196 - 78{,}4 = 117{,}6 \text{ J}").scale(1.0).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4b))
        self.play(Create(SurroundingRectangle(b4b, color=GREEN)))
        self.wait(2.5)
        b4c = Tex("Zeros are bookkeeping; differences are physics").scale(1.0).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4c))
        self.wait(2)
        b4d = Tex("Never mix levels inside one problem").scale(1.0).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4d))
        self.wait(3)

        # --- Band 5 (subtopic_4): the four-step method ---
        self.next_band(5)
        b5t = Tex("The method, four steps").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("1. List $m$, $g$, $h$ — converting units as you list").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5b = Tex("2. Declare the reference level").scale(0.95).shift(band_shift(5) + UP * 0.2)
        b5c = Tex("3. Substitute into $E_p = mgh$, carry units").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        b5d = Tex("4. Sense-check; changes use height differences").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        for m in (b5a, b5b, b5c, b5d):
            self.play(Write(m))
            self.wait(2)
        self.wait(2)

        # --- Band 6 (subtopic_4): the traps ---
        self.next_band(6)
        b6t = Tex("The traps").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("Weight fed in as mass: $39{,}2 \\times g$ again").scale(0.95).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6a))
        self.play(Create(strike(b6a)))
        self.wait(2)
        b6b = Tex("Slope length used as height — $h$ is VERTICAL").scale(0.95).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6b))
        self.wait(2)
        b6c = Tex("750 g $=$ 0,75 kg; 320 cm $=$ 3,2 m").scale(0.95).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6c))
        self.wait(2)
        b6d = Tex("`117,6 J downward'").scale(0.95).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6d))
        self.play(Create(strike(b6d)))
        self.wait(2)
        b6e = Tex("Use $g = 9{,}8$, not 10, unless told otherwise").scale(0.95).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6e))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the bank account in the sky ---
        self.next_band(7)
        b7t = Tex("The bank account in the sky").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("Pumping water up: a DEPOSIT of work").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7a))
        self.wait(2.5)
        b7b = Tex("Sitting high: savings, waiting").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7b))
        self.wait(2)
        b7c = Tex("Falling: the withdrawal, paid in speed").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7c))
        self.wait(2)
        b7d = Tex("The bill: weight $\\times$ height").scale(1.05).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7d))
        self.play(Create(SurroundingRectangle(b7d, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the paint tin's bank balance ---
        self.next_band(8)
        b8t = Tex("The paint tin's bank balance").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = MathTex(r"\text{Weight: } 4 \times 9{,}8 = 39{,}2 \text{ N}").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2.5)
        b8b = MathTex(r"\text{Deposit: } 39{,}2 \times 3 = 117{,}6 \text{ J}").scale(1.0).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8b))
        self.wait(2.5)
        b8c = MathTex(r"\text{Top-up: } 39{,}2 \times 7 = 274{,}4 \text{ J}").scale(1.0).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8c))
        self.play(Create(SurroundingRectangle(b8c, color=GREEN)))
        self.wait(2.5)
        b8d = Tex("From 10 m, all 392 J return as speed — hard hats").scale(0.9).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8d))
        self.wait(3)

        # --- Band 9 (subtopic_7): choosing where zero is ---
        self.next_band(9)
        b9t = Tex("Choosing where zero is").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Ground says 3 m; cellar says 5 m — both right").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2.5)
        b9b = Tex("Nature pays only DIFFERENCES").scale(1.05).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9b))
        self.play(Create(SurroundingRectangle(b9b, color=GREEN)))
        self.wait(2.5)
        b9c = Tex("Declare the zero once; keep it to the end").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9c))
        self.wait(2)
        b9d = Tex("Below zero: a negative, overdrawn balance").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9d))
        self.wait(4)
