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

# Band-layout whiteboard scene for "Balancing Chemical Equations" (Part 1
# Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe
# mobjects only; write-only reveals; camera moves down band by band. Band
# time apportioned to subtopics.json (220/250/230/280/160/160/170 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class BalancingEquationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the equation that lies ---
        title = Tex("Balancing Chemical Equations").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"\mathrm{C_3H_8 + O_2 \to CO_2 + H_2O}").scale(1.05).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("left: 3 C, 8 H, 2 O — right: 1 C, 2 H, 3 O").scale(0.95).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("atoms vanished, atoms invented — the line lies").scale(0.95).shift(DOWN * 0.9)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("conservation of mass: atoms are only REARRANGED").scale(0.9).shift(DOWN * 1.9)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): the one commandment ---
        self.next_band(1)
        b1_t = Tex("The one commandment").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("coefficients: yours to change — multipliers of the whole formula").scale(0.8).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("subscripts: locked — they ARE the substance").scale(0.9).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = Tex(r"H$_2$O is water; H$_2$O$_2$ is peroxide — identity theft").scale(0.9).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex(r"4 H$_2$O = 8 H + 4 O; 5 O$_2$ = 10 O").scale(0.95).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the C, H, O order ---
        self.next_band(2)
        b2_t = Tex("Balance in the order C, H, O").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("carbon: one destination — settles instantly").scale(0.95).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("hydrogen: one destination — settles instantly").scale(0.95).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("oxygen: in BOTH products, alone as O$_2$ —").scale(0.95).shift(band_shift(2) + DOWN * 0.6)
        b2_l4 = Tex("dependent on everyone: balance it LAST").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = Tex("oxygen first = the tail-chase loop").scale(0.9).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_3): propane balanced step by step ---
        self.next_band(3)
        b3_t = Tex("Propane, worked in order").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex(r"C: 3 carbons $\to$ 3 CO$_2$").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex(r"H: 8 hydrogens $\to$ 4 H$_2$O").scale(0.95).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex(r"O demand: 6 + 4 = 10 atoms $\to$ 5 O$_2$").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"\mathrm{C_3H_8 + 5\,O_2 \to 3\,CO_2 + 4\,H_2O}").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the audit ---
        self.next_band(4)
        b4_t = Tex("The audit — never optional").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("C: 3 left, 3 right — match").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(1.5)
        b4_l2 = Tex("H: 8 left, 8 right — match").scale(0.95).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l2))
        self.wait(1.5)
        b4_l3 = Tex("O: 10 left, 6 + 4 = 10 right — match").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("three matches: the law PROVEN, not assumed").scale(0.95).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): butane and the fraction ---
        self.next_band(5)
        b5_t = Tex("When oxygen lands on a fraction").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex(r"butane: C$_4$H$_{10}$ $\to$ 4 CO$_2$ + 5 H$_2$O").scale(0.95).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex(r"O demand: 8 + 5 = 13 atoms = $\frac{13}{2}$ O$_2$").scale(0.95).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("cure: double EVERY coefficient").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(1.5)
        b5_l4 = MathTex(r"\mathrm{2\,C_4H_{10} + 13\,O_2 \to 8\,CO_2 + 10\,H_2O}").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): smallest set + the road ahead ---
        self.next_band(6)
        b6_t = Tex("Final form: the smallest set").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex(r"4 H$_2$ + 2 O$_2$ $\to$ 4 H$_2$O balances, but halves:").scale(0.9).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex(r"2 H$_2$ + O$_2$ $\to$ 2 H$_2$O — final").scale(0.95).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("check: does one number divide all coefficients?").scale(0.9).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("next term: 1, 5, 3, 4 become MOLE RATIOS").scale(0.95).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): nothing goes missing at the braai ---
        self.next_band(7)
        b7_t = Tex("Nothing goes missing at the braai").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("weigh gas in + oxygen in = weigh smoke + steam out").scale(0.85).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("carbons leave as CO$_2$, hydrogens leave as steam").scale(0.9).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("3 C in, 3 C out; 8 H in, 8 H out — nobody slips away").scale(0.85).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex("everything collected must be delivered").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (subtopic_6): buy more packets ---
        self.next_band(8)
        b8_t = Tex("Buy more packets, don't repack them").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("big number in front = packets bought — change freely").scale(0.85).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("little number inside = the label — LOCKED").scale(0.9).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2)
        b8_l3 = Tex(r"5 O$_2$ = ten atoms; 4 H$_2$O = 8 H + 4 O").scale(0.9).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("no number in front = an invisible one").scale(0.9).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_7): easy ones first ---
        self.next_band(9)
        b9_t = Tex("Easy ones first, then the awkward one").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("C settles, H settles, O squeezes in last").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("one propane + five oxygen").scale(0.95).shift(band_shift(9) + UP * 0.3)
        b9_l3 = Tex(r"$\to$ three carbon dioxide + four water").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("count out loud: 3 and 3, 8 and 8, 10 and 10").scale(0.9).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("halves? double the list. divisible? reduce it.").scale(0.9).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l5))
        self.wait(4)
