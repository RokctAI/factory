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

# Band-layout whiteboard scene for "Physics Paper Practice Run" — seven
# question walks through a full-year physics practice set (this script runs
# all seven subtopics as expert question walks; each gets its own fresh bands).
# Exporter-safe mobjects only, write-only reveals, camera moves between bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PhysicsPaperPracticeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # --- Band 0 (subtopic_1): Q1 — free-body diagram on the incline
        title = Tex("Physics Practice Run").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Q1: 6 kg block, 30$^\\circ$ incline, 70 N up the slope").scale(1.0).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        # incline sketch: slope line, block dot, force arrows
        slope = Line(LEFT * 4.0 + DOWN * 2.2, RIGHT * 2.0 + UP * 0.2)
        base = Line(LEFT * 4.0 + DOWN * 2.2, RIGHT * 2.0 + DOWN * 2.2)
        self.play(Create(slope), Create(base))
        blk = Dot(LEFT * 1.0 + DOWN * 1.0, radius=0.12)
        self.play(Create(blk))
        self.wait(1.5)
        f_app = Arrow(LEFT * 1.0 + DOWN * 1.0, RIGHT * 0.6 + DOWN * 0.36, buff=0, color=GREEN)
        f_fric = Arrow(LEFT * 1.0 + DOWN * 1.0, LEFT * 2.2 + DOWN * 1.48, buff=0, color=RED)
        f_w = Arrow(LEFT * 1.0 + DOWN * 1.0, LEFT * 1.0 + DOWN * 2.4, buff=0, color=BLUE)
        lab_app = Tex("70 N").scale(0.8).shift(RIGHT * 1.2 + DOWN * 0.2)
        lab_fric = Tex("f $=$ 8,6 N").scale(0.8).shift(LEFT * 3.2 + DOWN * 1.2)
        lab_w = Tex("W").scale(0.8).shift(LEFT * 0.6 + DOWN * 2.3)
        self.play(Create(f_app), Write(lab_app))
        self.play(Create(f_fric), Write(lab_fric))
        self.play(Create(f_w), Write(lab_w))
        self.wait(2.5)
        b0_l2 = Tex("Friction points DOWN the slope: motion is up").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(b0_l2))
        self.wait(3)

        # --- Band 1 (subtopic_1): the incline calculation
        self.next_band(1)
        b1_title = Tex("Split the weight, then $F_{net} = ma$").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"mg\sin\theta = 6 \times 9{,}8 \times 0{,}5 = 29{,}4\ \text{N}").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"F_{net} = 70 - 29{,}4 - 8{,}6 = 32\ \text{N}").scale(1.05).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"a = \frac{32}{6} = 5{,}33\ \text{m}\cdot\text{s}^{-2}\ \text{up the slope}").scale(1.05).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = Tex("Audit: positive, and less than the frictionless value").scale(0.95).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): momentum — the coupling
        self.next_band(2)
        b2_title = Tex("Q2: 4 kg at 3 m·s$^{-1}$ couples 2 kg at rest").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex("Isolated system: total momentum constant").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"p_{before} = 4 \times 3 + 2 \times 0 = 12\ \text{kg}\cdot\text{m}\cdot\text{s}^{-1}").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"v = \frac{12}{6} = 2\ \text{m}\cdot\text{s}^{-1}\ \text{to the right}").scale(1.05).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Direction is part of the answer").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): elastic or not, and the impulse
        self.next_band(3)
        b3_title = Tex("Elastic? Compute both sides").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"E_{k,before} = \tfrac{1}{2} \times 4 \times 9 = 18\ \text{J}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"E_{k,after} = \tfrac{1}{2} \times 6 \times 4 = 12\ \text{J}").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("Kinetic energy fell: INELASTIC").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = MathTex(r"\text{Impulse on B} = 2 \times 2 - 0 = 4\ \text{N}\cdot\text{s}").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("A loses the same 4 — equal and opposite").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): projectile numbers
        self.next_band(4)
        b4_title = Tex("Q3: up at 14,7 m·s$^{-1}$, up is positive").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"0 = 14{,}7 - 9{,}8t \Rightarrow t = 1{,}5\ \text{s}").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"\Delta y = \frac{14{,}7^2}{2 \times 9{,}8} = \frac{216{,}09}{19{,}6} = 11{,}03\ \text{m}").scale(1.0).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"v(2{,}5) = 14{,}7 - 9{,}8 \times 2{,}5 = -9{,}8\ \text{m}\cdot\text{s}^{-1}").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("Report: 9,8 m·s$^{-1}$ DOWNWARD").scale(1.0).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): the velocity-time graph
        self.next_band(5)
        b5_title = Tex("One straight line, gradient $-9{,}8$").scale(1.1).shift(band_shift(5) + UP * 2.8)
        self.play(Write(b5_title))
        self.wait(1.5)
        ax_y = Arrow(band_shift(5) + LEFT * 4.0 + DOWN * 2.0, band_shift(5) + LEFT * 4.0 + UP * 2.2, buff=0)
        ax_x = Arrow(band_shift(5) + LEFT * 4.0 + UP * 0.1, band_shift(5) + RIGHT * 3.4 + UP * 0.1, buff=0)
        y_lab = Tex("v").scale(0.85).shift(band_shift(5) + LEFT * 4.5 + UP * 1.9)
        x_lab = Tex("t").scale(0.85).shift(band_shift(5) + RIGHT * 3.0 + DOWN * 0.3)
        self.play(Create(ax_y), Create(ax_x), Write(y_lab), Write(x_lab))
        self.wait(1.5)
        vline = Line(band_shift(5) + LEFT * 4.0 + UP * 1.8, band_shift(5) + RIGHT * 2.4 + DOWN * 1.6, color=YELLOW)
        self.play(Create(vline))
        self.wait(2)
        l_start = Tex("$+14{,}7$").scale(0.8).shift(band_shift(5) + LEFT * 4.7 + UP * 1.8)
        l_cross = Tex("$t = 1{,}5$ s at the top").scale(0.8).shift(band_shift(5) + LEFT * 0.4 + UP * 0.6)
        l_end = Tex("$-14{,}7$ at $t = 3$ s").scale(0.8).shift(band_shift(5) + RIGHT * 1.6 + DOWN * 1.9)
        self.play(Write(l_start))
        self.play(Write(l_cross))
        self.play(Write(l_end))
        self.wait(2.5)
        b5_l1 = Tex("Symmetry is the audit: up 1,5 s, down 1,5 s").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l1))
        self.wait(3)

        # --- Band 6 (subtopic_4): work-energy theorem on the crate
        self.next_band(6)
        b6_title = Tex("Q4: 15 kg crate, 90 N against 30 N, over 8 m").scale(1.0).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"W_{net} = (90 - 30) \times 8 = 480\ \text{J}").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"W_{net} = \Delta E_k: \ 480 = \tfrac{1}{2} \times 15 \times v^2").scale(1.0).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"v^2 = 64 \Rightarrow v = 8\ \text{m}\cdot\text{s}^{-1}").scale(1.05).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex("Energy methods named: the instruction is binding").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): the motor's power
        self.next_band(7)
        b7_title = Tex("Motor: 250 kg through 16 m in 25 s").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"F = mg = 250 \times 9{,}8 = 2\,450\ \text{N}").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"W = 2\,450 \times 16 = 39\,200\ \text{J}").scale(1.0).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"P = \frac{39\,200}{25} = 1\,568\ \text{W}").scale(1.05).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex("Audit: about 1,5 kW — a plausible motor").scale(0.95).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (subtopic_5): the Doppler effect
        self.next_band(8)
        b8_title = Tex("Q5: train at 20 m·s$^{-1}$, horn 900 Hz").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Approach must RAISE $f$: denominator shrinks").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"f_{obs} = \frac{340}{340 - 20} \times 900 = 956{,}25\ \text{Hz}").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = MathTex(r"f_{obs} = \frac{340}{340 + 20} \times 900 = 850\ \text{Hz}").scale(1.0).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Audit: above 900 approaching, below receding").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        b8_l5 = Tex("Application: blood flow by ultrasound").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the circuit — outside in
        self.next_band(9)
        b9_title = Tex(r"Q6: emf 24 V, $r = 2\ \Omega$, 4 $\Omega$ $+$ (12 $\|$ 12)").scale(1.0).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"12 \| 12 = \frac{144}{24} = 6\ \Omega").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"R_{ext} = 4 + 6 = 10\ \Omega,\quad R_{tot} = 10 + 2 = 12\ \Omega").scale(0.95).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"I = \frac{24}{12} = 2\ \text{A}").scale(1.05).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("The internal resistance belongs in the total").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_6): walk back in, audit, power
        self.next_band(10)
        b10_title = Tex("Walk back into the branches").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(1.5)
        b10_l1 = MathTex(r"V_{term} = 24 - 2 \times 2 = 20\ \text{V}").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"V_{4\Omega} = 8\ \text{V} \Rightarrow V_{pair} = 12\ \text{V}").scale(1.0).shift(band_shift(10) + UP * 0.2)
        b10_l3 = MathTex(r"I_{branch} = \frac{12}{12} = 1\ \text{A each}").scale(1.0).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("Audit: $1 + 1 = 2$ A — the books balance").scale(1.0).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = MathTex(r"P_{4\Omega} = I^2R = 4 \times 4 = 16\ \text{W}").scale(1.0).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (subtopic_7): the photoelectric close
        self.next_band(11)
        b11_title = Tex(r"Q7: 450 nm light, $W_0 = 3{,}5 \times 10^{-19}$ J").scale(1.05).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = MathTex(r"E = \frac{hc}{\lambda} = \frac{6{,}63 \times 10^{-34} \times 3 \times 10^8}{4{,}5 \times 10^{-7}}").scale(0.95).shift(band_shift(11) + UP * 1.0)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = MathTex(r"E = 4{,}42 \times 10^{-19}\ \text{J}").scale(1.05).shift(band_shift(11) + UP * 0.0)
        self.play(Write(b11_l2))
        self.play(Create(SurroundingRectangle(b11_l2, color=GREEN)))
        self.wait(2)
        b11_l3 = MathTex(r"E_{k,max} = 4{,}42 - 3{,}5 = 0{,}92 \times 10^{-19}\ \text{J}").scale(1.0).shift(band_shift(11) + DOWN * 1.0)
        self.play(Write(b11_l3))
        self.wait(2.5)
        b11_l4 = Tex("Halve the intensity: HALF the electrons,").scale(0.95).shift(band_shift(11) + DOWN * 1.9)
        b11_l5 = Tex("SAME maximum kinetic energy").scale(0.95).shift(band_shift(11) + DOWN * 2.6)
        self.play(Write(b11_l4))
        self.play(Write(b11_l5))
        self.wait(2)
        b11_l6 = Tex("Light behaves as particles — the closing sentence").scale(0.95).shift(band_shift(11) + DOWN * 3.3)
        self.play(Write(b11_l6))
        self.wait(4)
