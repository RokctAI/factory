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

# Band-layout whiteboard scene for "Conservation of Energy and Power"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only; slide and ramp sketches hand-built from
# Dot/Line/Arrow/Square/Tex. Write-only reveals.
# Subtopic durations 235/235/240/240/195/195/195 of 1535 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ConservationEnergyPowerSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): conservative vs non-conservative ---
        title = Tex("Conservation of Energy and Power").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("CONSERVATIVE: work independent of path").scale(1.0).shift(UP * 1.1)
        b0_l2 = Tex("gravity — charges height, repays in full").scale(0.95).shift(UP * 0.3)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("NON-CONSERVATIVE: work depends on path").scale(1.0).shift(DOWN * 0.7)
        b0_l4 = Tex("friction — bills every metre, no refunds").scale(0.95).shift(DOWN * 1.5)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_eq = MathTex(r"E_{mech} = E_k + E_p").scale(1.1).shift(DOWN * 2.6)
        self.play(Write(b0_eq))
        self.play(Create(SurroundingRectangle(b0_eq, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the principle, stone dropped from 4,9 m ---
        self.next_band(1)
        b1_title = Tex("Only conservative forces: $E_{mech}$ constant").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"mgh = \tfrac{1}{2}mv^2").scale(1.1).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("mass cancels — every mass falls alike").scale(0.95).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"v^2 = 2 \times 9{,}8 \times 4{,}9 = 96{,}04").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        b1_l4 = MathTex(r"v = 9{,}8\ \text{m·s}^{-1}").scale(1.05).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l3))
        self.wait(2.5)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the bookkeeping identity ---
        self.next_band(2)
        b2_eq = MathTex(r"W_{nc} = \Delta E_k + \Delta E_p").scale(1.2).shift(band_shift(2) + UP * 2.0)
        self.play(Write(b2_eq))
        self.play(Create(SurroundingRectangle(b2_eq, color=GREEN)))
        self.wait(2.5)
        b2_l1 = Tex("1. choose a reference level").scale(0.95).shift(band_shift(2) + UP * 0.9)
        b2_l2 = Tex("2. four numbers: $E_k$, $E_p$ at start and end").scale(0.95).shift(band_shift(2) + UP * 0.1)
        b2_l3 = Tex("3. two changes: final minus initial").scale(0.95).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = Tex("4. add — the sign tells the story").scale(0.95).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l1))
        self.wait(1.5)
        self.play(Write(b2_l2))
        self.wait(1.5)
        self.play(Write(b2_l3))
        self.wait(1.5)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("negative: drained. positive: pumped in.").scale(0.95).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the slide, worked in full ---
        self.next_band(3)
        b3_title = Tex("Slide: 40 kg, 2,5 m high, arrives at 5 m·s$^{-1}$").scale(1.0).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        base3 = band_shift(3) + LEFT * 5.0 + DOWN * 1.2
        slide = Line(base3 + UP * 2.2, base3 + RIGHT * 3.0)
        ground3 = Line(base3, base3 + RIGHT * 3.6)
        kid = Dot(base3 + UP * 2.2, radius=0.12, color=YELLOW)
        self.play(Create(ground3), Create(slide), FadeIn(kid))
        self.wait(2)
        b3_l1 = MathTex(r"E_p^i = 40 \times 9{,}8 \times 2{,}5 = 980\ \text{J}").scale(0.95).shift(band_shift(3) + RIGHT * 2.6 + UP * 1.2)
        b3_l2 = MathTex(r"E_k^f = \tfrac{1}{2} \times 40 \times 25 = 500\ \text{J}").scale(0.95).shift(band_shift(3) + RIGHT * 2.6 + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"W_{nc} = 500 - 980 = -480\ \text{J}").scale(1.0).shift(band_shift(3) + RIGHT * 2.6 + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("frictionless check: $v = \\sqrt{49} = 7$; she arrived at 5").scale(0.9).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): ramp solved to the friction force ---
        self.next_band(4)
        b4_title = Tex("Ramp: 3 kg, 5 m long, 2 m high, arrives at 4 m·s$^{-1}$").scale(0.95).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"E_p^i = 3 \times 9{,}8 \times 2 = 58{,}8\ \text{J}, \;\; E_k^f = 24\ \text{J}").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"W_{nc} = 24 - 58{,}8 = -34{,}8\ \text{J}").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"-f \times 5 = -34{,}8 \Rightarrow f = 6{,}96\ \text{N}").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex("divide by the 5 m PATH — friction bills the surface,").scale(0.9).shift(band_shift(4) + DOWN * 1.9)
        b4_l5 = Tex("never the 2 m height, which belongs to gravity").scale(0.9).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): uphill winch + air resistance twist ---
        self.next_band(5)
        b5_title = Tex("Back up the ramp, constant speed").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"\Delta E_k = 0, \;\; \Delta E_p = +58{,}8\ \text{J}").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"W_{winch} = 58{,}8 + 34{,}8 = 93{,}6\ \text{J}").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("down: friction fights gravity;").scale(0.95).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = Tex("up: EVERYTHING fights the winch").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("ball in air: returns SLOWER — the air billed both legs").scale(0.9).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): power — stairs and borehole ---
        self.next_band(6)
        b6_eq = MathTex(r"P = \frac{W}{\Delta t} \;\; [\text{W} = \text{J·s}^{-1}]").scale(1.1).shift(band_shift(6) + UP * 2.0)
        self.play(Write(b6_eq))
        self.play(Create(SurroundingRectangle(b6_eq, color=GREEN)))
        self.wait(2.5)
        b6_l1 = Tex("Stairs: 55 kg up 3,2 m in 4 s").scale(0.95).shift(band_shift(6) + UP * 0.9)
        b6_l2 = MathTex(r"W = 55 \times 9{,}8 \times 3{,}2 = 1\,724{,}8\ \text{J}").scale(0.95).shift(band_shift(6) + UP * 0.1)
        b6_l3 = MathTex(r"P = 1\,724{,}8 \div 4 = 431{,}2\ \text{W}").scale(0.95).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("Borehole: 150 kg/min from 25 m").scale(0.95).shift(band_shift(6) + DOWN * 1.7)
        b6_l5 = MathTex(r"P_{min} = \frac{150 \times 9{,}8 \times 25}{60} = 612{,}5\ \text{W}").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): P = Fv at constant speed ---
        self.next_band(7)
        b7_eq = MathTex(r"P = F v \;\; \text{(constant speed)}").scale(1.15).shift(band_shift(7) + UP * 2.0)
        self.play(Write(b7_eq))
        self.play(Create(SurroundingRectangle(b7_eq, color=GREEN)))
        self.wait(2.5)
        b7_l1 = Tex("Bus: 20 m·s$^{-1}$ against 2 500 N").scale(1.0).shift(band_shift(7) + UP * 0.9)
        b7_l2 = MathTex(r"P = 2\,500 \times 20 = 50\,000\ \text{W} = 50\ \text{kW}").scale(1.0).shift(band_shift(7) + UP * 0.0)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("'minimum' power: gravity's bill alone —").scale(0.95).shift(band_shift(7) + DOWN * 1.0)
        b7_l4 = Tex("real machines also pay pipe and air friction").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the energy toll road ---
        self.next_band(8)
        b8_title = Tex("Banker or toll collector?").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Swing: height-money $\\leftrightarrow$ speed-money").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Gravity: honest banker — full refunds, any route").scale(0.95).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("Friction: toll collector — pays nothing back, burns it").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Real swing rises less each pass:").scale(0.95).shift(band_shift(8) + DOWN * 1.7)
        b8_l5 = Tex("the missing cents are the toll collector's take").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): friction's receipt ---
        self.next_band(9)
        b9_title = Tex("Friction's receipt").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Wallet in: 980 J. Wallet out: 500 J.").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"\text{receipt: } W_{nc} = -480\ \text{J}").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex("negative: collected. positive: paid in. zero: perfect swing.").scale(0.85).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("friction bills the PATH; gravity bills the HEIGHT").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): rich against fast ---
        self.next_band(10)
        b10_title = Tex("Rich against fast").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_wrong = Tex("Running upstairs does more work").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_wrong))
        self.play(Create(strike(b10_wrong)))
        self.wait(2)
        b10_l1 = Tex("same work — ten times the POWER in a tenth of the time").scale(0.9).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("charger: $\\sim$20 W. kettle: $\\sim$2 000 W.").scale(0.95).shift(band_shift(10) + DOWN * 0.7)
        b10_l3 = Tex("you on the stairs: a few hundred watts").scale(0.95).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("work and time: $P = W/t$. cruising: $P = Fv$.").scale(0.95).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(4)
