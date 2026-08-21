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

# Band-layout whiteboard scene for "Series and Parallel Circuits" (Part 1
# Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe
# mobjects only; write-only reveals; camera moves down band by band. Band
# time apportioned to subtopics.json (220/230/230/270/180/180/180 of 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SeriesParallelSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): charge, energy, the three quantities ---
        title = Tex("Series and Parallel Circuits").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"I = \frac{Q}{\Delta t}").scale(1.0).shift(UP * 0.9 + LEFT * 3)
        b0_l2 = MathTex(r"V = \frac{W}{Q}").scale(1.0).shift(UP * 0.9 + RIGHT * 3)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("current: rate of charge flow — amperes").scale(0.9).shift(DOWN * 0.2)
        b0_l4 = Tex("potential difference: joules per coulomb — volts").scale(0.9).shift(DOWN * 1.0)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex("charge circulates; ENERGY is what gets spent").scale(0.9).shift(DOWN * 2.0)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): resistance + the two instrument rules ---
        self.next_band(1)
        b1_t = Tex("Resistance, and the two instruments").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("R in ohms: electrons collide with the lattice").scale(0.9).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("longer = more; thicker = less; hotter = more").scale(0.9).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("ammeter: in SERIES, low resistance").scale(0.9).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l3))
        b1_l4 = Tex("voltmeter: in PARALLEL, high resistance").scale(0.9).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): Ohm's law + the series circuit, drawn ---
        self.next_band(2)
        b2_t = MathTex(r"V = I R").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.play(Create(SurroundingRectangle(b2_t, color=GREEN)))
        self.wait(2)
        # simple series loop sketch: battery left, two resistors on top rail
        rail_y = band_shift(2) + UP * 0.6
        b2_w1 = Line(rail_y + LEFT * 4, rail_y + LEFT * 1.5, color=BLUE)
        b2_r1 = Rectangle(width=1.0, height=0.5, color=YELLOW).move_to(rail_y + LEFT * 1.0)
        b2_w2 = Line(rail_y + LEFT * 0.5, rail_y + RIGHT * 1.0, color=BLUE)
        b2_r2 = Rectangle(width=1.0, height=0.5, color=YELLOW).move_to(rail_y + RIGHT * 1.5)
        b2_w3 = Line(rail_y + RIGHT * 2.0, rail_y + RIGHT * 4.0, color=BLUE)
        self.play(Create(b2_w1), Create(b2_r1), Create(b2_w2), Create(b2_r2), Create(b2_w3))
        b2_lbl = Tex(r"18 V battery; 3 $\Omega$ then 6 $\Omega$ — one loop, no junctions").scale(0.8).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_lbl))
        self.wait(2)
        b2_l1 = Tex("one path: same current everywhere;").scale(0.9).shift(band_shift(2) + DOWN * 1.5)
        b2_l2 = Tex("volts add to the emf; resistances add").scale(0.9).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(3)

        # --- Band 3 (subtopic_2): the series numbers, line by line ---
        self.next_band(3)
        b3_t = Tex("Series, worked").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"R_s = 3 + 6 = 9\ \Omega").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"I = \frac{18}{9} = 2\ \text{A everywhere}").scale(1.0).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"V_1 = 2 \times 3 = 6\ \text{V}; \quad V_2 = 2 \times 6 = 12\ \text{V}").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("check: 6 + 12 = 18 — the full emf accounted for").scale(0.9).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the parallel circuit, drawn ---
        self.next_band(4)
        b4_t = Tex("The parallel circuit").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        # junction sketch: split into two branches
        jL = band_shift(4) + UP * 0.6 + LEFT * 3
        jR = band_shift(4) + UP * 0.6 + RIGHT * 3
        b4_d1 = Dot(jL, color=YELLOW)
        b4_d2 = Dot(jR, color=YELLOW)
        b4_top = Line(jL, jL + UP * 0.8, color=BLUE)
        b4_topr = Line(jL + UP * 0.8, jR + UP * 0.8, color=BLUE)
        b4_topd = Line(jR + UP * 0.8, jR, color=BLUE)
        b4_bot = Line(jL, jL + DOWN * 0.8, color=BLUE)
        b4_botr = Line(jL + DOWN * 0.8, jR + DOWN * 0.8, color=BLUE)
        b4_botd = Line(jR + DOWN * 0.8, jR, color=BLUE)
        self.play(Create(b4_d1), Create(b4_d2))
        self.play(Create(b4_top), Create(b4_topr), Create(b4_topd))
        self.play(Create(b4_bot), Create(b4_botr), Create(b4_botd))
        b4_lbl = Tex(r"3 $\Omega$ on top, 6 $\Omega$ below — same pair of junctions").scale(0.8).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_lbl))
        self.wait(2)
        b4_l1 = Tex("both branches feel the FULL 18 volts").scale(0.9).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): reciprocal formula, the invert step ---
        self.next_band(5)
        b5_t = Tex("Reciprocals add — then INVERT").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"\frac{1}{R_p} = \frac{1}{3} + \frac{1}{6} = \frac{2}{6} + \frac{1}{6} = \frac{1}{2}").scale(0.95).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"R_p = 2\ \Omega").scale(1.15).shift(band_shift(5) + DOWN * 0.1)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2)
        b5_l3 = Tex("2 is LESS than both 3 and 6 — the parallel signature:").scale(0.85).shift(band_shift(5) + DOWN * 1.1)
        b5_l4 = Tex("total always below the smallest branch").scale(0.9).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_3): the parallel currents ---
        self.next_band(6)
        b6_t = Tex("The currents divide").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"I_{tot} = \frac{18}{2} = 9\ \text{A}").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"I_3 = \frac{18}{3} = 6\ \text{A}; \quad I_6 = \frac{18}{6} = 3\ \text{A}").scale(0.95).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("check: 6 + 3 = 9 — junctions lose nothing").scale(0.9).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex("smaller resistance, larger current").scale(0.9).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): the two rule sets, side by side ---
        self.next_band(7)
        b7_t = Tex("The two rule sets").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("SERIES: same I; V's add; R's add;").scale(0.85).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("total larger than any one; one break kills all").scale(0.85).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("PARALLEL: same V; I's add; reciprocals add;").scale(0.85).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("total below smallest; one break spares the rest").scale(0.85).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("same PATH = same I; same JUNCTIONS = same V").scale(0.9).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): error museum + the house ---
        self.next_band(8)
        b8_t = Tex("Error museum, and your walls").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = Tex("1. forgetting to invert the reciprocal").scale(0.85).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("2. swapping the two SAME quantities").scale(0.85).shift(band_shift(8) + UP * 0.5)
        b8_l3 = Tex("3. milliamps into an amp formula  4. missing units").scale(0.85).shift(band_shift(8) + DOWN * 0.2)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("homes wire in PARALLEL: full 230 V per branch;").scale(0.85).shift(band_shift(8) + DOWN * 1.2)
        b8_l5 = Tex("each extra appliance raises the total current").scale(0.85).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): one road through town ---
        self.next_band(9)
        b9_t = Tex("One road through town").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("taxis = charge; 18 joules loaded per coulomb").scale(0.9).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("one road: same traffic at every point").scale(0.9).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex(r"roughness adds: 3 + 6 = 9 $\Omega$; traffic 2 A").scale(0.9).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("energy split by roughness: 6 V and 12 V").scale(0.9).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_6): two roads, two queues ---
        self.next_band(10)
        b10_t = Tex("Two roads, two queues").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("every route drops the FULL eighteen").scale(0.9).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.play(Create(SurroundingRectangle(b10_l1, color=GREEN)))
        self.wait(2)
        b10_l2 = Tex("traffic splits: 6 A on the easy road, 3 A on the rough").scale(0.85).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("upside-down sum: a third + a sixth = a half").scale(0.9).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex(r"FLIP it back: 2 $\Omega$ — check 18/2 = 9 A").scale(0.9).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l4))
        self.wait(3)

        # --- Band 11 (subtopic_7): why your house is wired the clever way ---
        self.next_band(11)
        b11_t = Tex("Why your house is wired the clever way").scale(1.05).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = Tex("series house: shared volts, all dark from one globe").scale(0.85).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11_l1))
        self.wait(2)
        b11_l2 = Tex("parallel house: full volts per branch,").scale(0.9).shift(band_shift(11) + UP * 0.4)
        b11_l3 = Tex("kettle off, lights on").scale(0.9).shift(band_shift(11) + DOWN * 0.3)
        self.play(Write(b11_l2))
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(2)
        b11_l4 = Tex("price: every branch raises the amps — the trip switch counts").scale(0.8).shift(band_shift(11) + DOWN * 1.3)
        self.play(Write(b11_l4))
        self.wait(2)
        b11_l5 = Tex("wall switch: in series with its light, on purpose").scale(0.85).shift(band_shift(11) + DOWN * 2.2)
        self.play(Write(b11_l5))
        self.wait(4)
