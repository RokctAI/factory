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

# Band-layout whiteboard scene for "Physics Paper Practice Run" — seven
# question walks through a Paper 1 (this duo's script runs all seven
# subtopics as expert question walks; each gets its own fresh bands).
# Exporter-safe mobjects only, write-only reveals, camera moves between bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class PhysicsPaperPracticeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # --- Band 0 (subtopic_1): Q1 — free-body diagram on the incline
        title = Tex("Physics Paper Practice Run").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Q1: 8 kg block, 30$^\circ$ incline, 80 N up,").scale(1.0).shift(UP * 1.6)
        b0_l2 = Tex("friction 10 N — free-body first").scale(1.0).shift(UP * 0.9)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2)
        # free-body diagram: dot with four labelled arrows
        body = Dot(DOWN * 0.9, radius=0.12)
        self.play(Create(body))
        aW = Arrow(DOWN * 0.9, DOWN * 2.6, buff=0, color=YELLOW)
        lW = MathTex(r"F_g").scale(0.9).shift(DOWN * 2.6 + RIGHT * 0.5)
        self.play(Create(aW), Write(lW))
        aN = Arrow(DOWN * 0.9, DOWN * 0.9 + (UP * 1.4 + LEFT * 0.8), buff=0, color=BLUE)
        lN = MathTex(r"N").scale(0.9).shift(DOWN * 0.9 + UP * 1.6 + LEFT * 1.1)
        self.play(Create(aN), Write(lN))
        aF = Arrow(DOWN * 0.9, DOWN * 0.9 + (RIGHT * 1.6 + UP * 0.9), buff=0, color=GREEN)
        lF = MathTex(r"F = 80\ \text{N}").scale(0.85).shift(DOWN * 0.9 + RIGHT * 2.6 + UP * 1.2)
        self.play(Create(aF), Write(lF))
        af = Arrow(DOWN * 0.9, DOWN * 0.9 + (LEFT * 1.3 + DOWN * 0.75), buff=0, color=RED)
        lf = MathTex(r"f = 10\ \text{N}").scale(0.85).shift(DOWN * 0.9 + LEFT * 2.5 + DOWN * 1.1)
        self.play(Create(af), Write(lf))
        self.wait(2.5)
        b0_l3 = Tex("Four arrows, four labels — that IS the mark").scale(1.0).shift(DOWN * 3.0)
        self.play(Write(b0_l3))
        self.wait(3)

        # --- Band 1 (subtopic_1): the incline calculation
        self.next_band(1)
        b1_title = Tex("Split the weight, sum along the slope").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"F_{g\parallel} = mg\sin\theta = 8 \times 9{,}8 \times 0{,}5").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"F_{g\parallel} = 39{,}2\ \text{N (down the slope)}").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"F_{net} = 80 - 39{,}2 - 10 = 30{,}8\ \text{N}").scale(1.05).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = MathTex(r"a = \frac{F_{net}}{m} = \frac{30{,}8}{8}").scale(1.05).shift(band_shift(1) + DOWN * 1.8)
        b1_l5 = MathTex(r"a = 3{,}85\ \text{m}\cdot\text{s}^{-2}\ \text{up the slope}").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): momentum — the coupling
        self.next_band(2)
        b2_title = Tex("Q2: 5 kg at 4 m/s couples with 3 kg at rest").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex("Total momentum of an ISOLATED system").scale(1.0).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex("remains constant — the word isolated must appear").scale(0.95).shift(band_shift(2) + UP * 0.6)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"p_{before} = 5 \times 4 + 3 \times 0 = 20\ \text{kg}\cdot\text{m/s}").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = MathTex(r"v = \frac{20}{8} = 2{,}5\ \text{m/s to the right}").scale(1.05).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): elastic or not, and the impulse
        self.next_band(3)
        b3_title = Tex("Kinetic energy decides; impulse closes").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"E_{k,before} = \tfrac{1}{2} \times 5 \times 16 = 40\ \text{J}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"E_{k,after} = \tfrac{1}{2} \times 8 \times 6{,}25 = 25\ \text{J}").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex(r"40 J $\rightarrow$ 25 J: INELASTIC — say it from").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex("the numbers, or the conclusion earns nothing").scale(1.0).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = MathTex(r"J_B = \Delta p_B = 3 \times 2{,}5 - 0 = 7{,}5\ \text{N}\cdot\text{s}").scale(1.0).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(2)
        b3_l6 = Tex("A lost exactly 7,5 — third law audit").scale(1.0).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): projectile numbers
        self.next_band(4)
        b4_title = Tex("Q3: ball up at 19,6 m/s — up is positive").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"0 = 19{,}6 - 9{,}8t \Rightarrow t = 2\ \text{s}").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"\Delta y = \frac{(19{,}6)^2}{2 \times 9{,}8} = \frac{384{,}16}{19{,}6}").scale(1.05).shift(band_shift(4) + UP * 0.0)
        b4_l3 = MathTex(r"\Delta y = 19{,}6\ \text{m}").scale(1.1).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l2))
        self.wait(2.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = MathTex(r"v(3) = 19{,}6 - 9{,}8 \times 3 = -9{,}8\ \text{m/s}").scale(1.0).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("Report it: 9,8 m/s DOWNWARD — sign is physics").scale(0.95).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): the velocity-time graph
        self.next_band(5)
        b5_title = Tex("One straight line tells the whole flight").scale(1.15).shift(band_shift(5) + UP * 2.8)
        self.play(Write(b5_title))
        self.wait(1.5)
        ax_y = Arrow(band_shift(5) + LEFT * 3.6 + DOWN * 2.2, band_shift(5) + LEFT * 3.6 + UP * 2.2, buff=0)
        ax_x = Arrow(band_shift(5) + LEFT * 3.6, band_shift(5) + RIGHT * 3.4, buff=0)
        y_lab = Tex("v (m/s)").scale(0.85).shift(band_shift(5) + LEFT * 4.5 + UP * 1.9)
        x_lab = Tex("t (s)").scale(0.85).shift(band_shift(5) + RIGHT * 3.9 + DOWN * 0.4)
        self.play(Create(ax_y), Create(ax_x), Write(y_lab), Write(x_lab))
        self.wait(1.5)
        vline = Line(band_shift(5) + LEFT * 3.6 + UP * 1.8, band_shift(5) + RIGHT * 2.8 + DOWN * 1.8, color=BLUE)
        self.play(Create(vline))
        d0 = Dot(band_shift(5) + LEFT * 3.6 + UP * 1.8, color=YELLOW)
        l0 = MathTex(r"+19{,}6").scale(0.85).shift(band_shift(5) + LEFT * 2.7 + UP * 2.1)
        d2 = Dot(band_shift(5) + LEFT * 0.4, color=YELLOW)
        l2 = MathTex(r"t = 2").scale(0.85).shift(band_shift(5) + LEFT * 0.4 + UP * 0.6)
        d4 = Dot(band_shift(5) + RIGHT * 2.8 + DOWN * 1.8, color=YELLOW)
        l4 = MathTex(r"-19{,}6 \text{ at } t = 4").scale(0.85).shift(band_shift(5) + RIGHT * 1.6 + DOWN * 2.3)
        self.play(Create(d0), Write(l0))
        self.play(Create(d2), Write(l2))
        self.play(Create(d4), Write(l4))
        self.wait(2.5)
        b5_l1 = Tex(r"Gradient $-9{,}8$ throughout; up 2 s, down 2 s").scale(1.0).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l1))
        self.wait(3)

        # --- Band 6 (subtopic_4): work-energy theorem on the crate
        self.next_band(6)
        b6_title = Tex("Q4: crate — energy methods are BINDING").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"F_{net} = 100 - 30 = 70\ \text{N}").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"W_{net} = 70 \times 5 = 350\ \text{J}").scale(1.05).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"350 = \tfrac{1}{2} \times 20 \times v^2").scale(1.05).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = MathTex(r"v^2 = 35 \Rightarrow v = 5{,}92\ \text{m/s}").scale(1.05).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2.5)
        b6_l5 = Tex("Work-energy theorem: net work $= \\Delta E_k$").scale(1.0).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): the motor's power
        self.next_band(7)
        b7_title = Tex("Motor: 300 kg up 12 m in 20 s").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"F = mg = 300 \times 9{,}8 = 2\,940\ \text{N}").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"W = 2\,940 \times 12 = 35\,280\ \text{J}").scale(1.05).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"P = \frac{W}{t} = \frac{35\,280}{20} = 1\,764\ \text{W}").scale(1.05).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("Just under 2 kW for four storeys — plausible").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (subtopic_5): the Doppler effect
        self.next_band(8)
        b8_title = Tex("Q5: siren 800 Hz, source at 30 m/s").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Approach must RAISE $f$: denominator shrinks").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"f_L = \frac{340}{340 - 30} \times 800 = \frac{272\,000}{310}").scale(1.0).shift(band_shift(8) + UP * 0.2)
        b8_l3 = MathTex(r"f_L = 877{,}42\ \text{Hz} > 800").scale(1.05).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = MathTex(r"\text{Receding: } \frac{340}{370} \times 800 = 735{,}14\ \text{Hz}").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Application: blood-flow or foetal heartbeat").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the circuit — outside in
        self.next_band(9)
        b9_title = Tex(r"Q6: 20 V battery, $r = 1\ \Omega$, 5 with 8$\parallel$8").scale(1.0).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"R_p = \frac{8 \times 8}{8 + 8} = \frac{64}{16} = 4\ \Omega").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"R_{ext} = 5 + 4 = 9\ \Omega, \quad R_{tot} = 10\ \Omega").scale(1.0).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"I = \frac{20}{10} = 2\ \text{A}").scale(1.05).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = MathTex(r"V_{term} = 20 - 2 \times 1 = 18\ \text{V}").scale(1.05).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("2 V spent inside the battery as heat").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_6): walk back in, audit, power
        self.next_band(10)
        b10_title = Tex("Walk back into the branches").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(1.5)
        b10_l1 = MathTex(r"V_5 = 2 \times 5 = 10\ \text{V}").scale(1.05).shift(band_shift(10) + UP * 1.2)
        b10_l2 = MathTex(r"V_p = 18 - 10 = 8\ \text{V}").scale(1.05).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = MathTex(r"I_8 = \frac{8}{8} = 1\ \text{A each branch}").scale(1.05).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex(r"Audit: $1 + 1 = 2$ A — the books balance").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = MathTex(r"P_5 = I^2R = 4 \times 5 = 20\ \text{W}").scale(1.05).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): the photoelectric close
        self.next_band(11)
        b11_title = Tex(r"Q7: 400 nm light, $W_0 = 3{,}68 \times 10^{-19}$ J").scale(1.05).shift(band_shift(11) + UP * 2.4)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex("Work function: MINIMUM energy to emit").scale(1.0).shift(band_shift(11) + UP * 1.5)
        self.play(Write(b11_l1))
        self.wait(2)
        b11_l2 = MathTex(r"E = \frac{hc}{\lambda} = \frac{1{,}989 \times 10^{-25}}{4 \times 10^{-7}}").scale(1.0).shift(band_shift(11) + UP * 0.5)
        b11_l3 = MathTex(r"E = 4{,}97 \times 10^{-19}\ \text{J}").scale(1.05).shift(band_shift(11) + DOWN * 0.5)
        self.play(Write(b11_l2))
        self.wait(2.5)
        self.play(Write(b11_l3))
        self.wait(2)
        b11_l4 = MathTex(r"E_{k(max)} = (4{,}97 - 3{,}68) \times 10^{-19}").scale(1.0).shift(band_shift(11) + DOWN * 1.4)
        b11_l5 = MathTex(r"E_{k(max)} = 1{,}29 \times 10^{-19}\ \text{J}").scale(1.05).shift(band_shift(11) + DOWN * 2.3)
        self.play(Write(b11_l4))
        self.wait(2)
        self.play(Write(b11_l5))
        self.play(Create(SurroundingRectangle(b11_l5, color=GREEN)))
        self.wait(2)
        b11_l6 = Tex(r"Double the intensity: $E_{k(max)}$ UNCHANGED").scale(1.0).shift(band_shift(11) + DOWN * 3.1)
        self.play(Write(b11_l6))
        self.wait(4)
