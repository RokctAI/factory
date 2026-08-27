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

# Band-layout whiteboard scene for "Paper 1 Physics Essentials" (Part 1 —
# Expert subtopics 1-4, Part 2 — Simplifier subtopics 5-7).
# Exporter-safe mobjects only, write-only reveals, camera moves between bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class Paper1PhysicsEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Newton's three laws, exam-day form
        title = Tex("Paper 1 Physics Essentials").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("1st: rest or constant velocity unless").scale(1.0).shift(UP * 1.3)
        b0_l2 = Tex("a non-zero net force acts").scale(1.0).shift(UP * 0.6)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"2nd: $a \propto F_{net}$, inversely $\propto m$").scale(1.05).shift(DOWN * 0.4)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("3rd: A on B; B on A, equal, opposite").scale(1.05).shift(DOWN * 1.3)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex("Bare statements ARE marks — word-perfect").scale(1.0).shift(DOWN * 2.4)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the crate, and the incline split
        self.next_band(1)
        b1_title = Tex("Free-body first, then $F_{net} = ma$").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("10 kg crate: 80 N pull against 20 N friction").scale(1.0).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"F_{net} = 80 - 20 = 60\ \text{N}").scale(1.1).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"a = \frac{60}{10} = 6\ \text{m}\cdot\text{s}^{-2}").scale(1.1).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = Tex(r"Incline: split weight into $mg\sin\theta$ along,").scale(1.0).shift(band_shift(1) + DOWN * 2.0)
        b1_l5 = Tex(r"$mg\cos\theta$ perpendicular — THE move").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_1): impulse with sign discipline
        self.next_band(2)
        b2_title = Tex("Impulse: declare the positive direction").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("0,5 kg ball: in at 10 m/s, back at 8 m/s").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("Towards the wall $=$ positive").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\Delta p = 0{,}5(-8 - 10) = -9\ \text{kg}\cdot\text{m/s}").scale(1.05).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = MathTex(r"F_{net} = \frac{-9}{0{,}1} = -90\ \text{N}").scale(1.05).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Report: 90 N directed AWAY from the wall").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_1): conservation and the elastic test
        self.next_band(3)
        b3_title = Tex("Coupling: 2 kg at 3 m/s meets 1 kg at rest").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"p_{before} = 2 \times 3 = 6\ \text{kg}\cdot\text{m/s}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"v = \frac{6}{3} = 2\ \text{m/s}").scale(1.1).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = MathTex(r"E_k: \tfrac{1}{2}(2)(9) = 9\ \text{J} \rightarrow \tfrac{1}{2}(3)(4) = 6\ \text{J}").scale(1.0).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex("Energy lost: INELASTIC — decided by").scale(1.0).shift(band_shift(3) + DOWN * 2.1)
        b3_l5 = Tex("arithmetic, never by guess").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_2): the standard vertical flight
        self.next_band(4)
        b4_title = Tex("Projectiles: gravity never switches off").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"At the top: $v = 0$ but $a = 9{,}8$ down — still").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"t_{top} = \frac{19{,}6}{9{,}8} = 2\ \text{s}").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"\Delta y = \frac{(19{,}6)^2}{2 \times 9{,}8} = 19{,}6\ \text{m}").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = MathTex(r"v(3) = 19{,}6 - 9{,}8 \times 3 = -9{,}8\ \text{m/s}").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("v-t graph: one line, gradient $-9{,}8$").scale(1.0).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_2): energy budgets and power
        self.next_band(5)
        b5_title = Tex("The energy budget closes to the joule").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("4 kg box, rough ramp, 5 m high, lands at 8 m/s").scale(0.95).shift(band_shift(5) + UP * 1.3)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"E_p = 4 \times 9{,}8 \times 5 = 196\ \text{J}").scale(1.05).shift(band_shift(5) + UP * 0.4)
        b5_l3 = MathTex(r"E_k = \tfrac{1}{2} \times 4 \times 64 = 128\ \text{J}").scale(1.05).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"W_{friction} = 128 - 196 = -68\ \text{J}").scale(1.05).shift(band_shift(5) + DOWN * 1.5)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)
        b5_l5 = MathTex(r"\text{Pump: } P = \frac{29\,400}{10} = 2\,940\ \text{W}").scale(1.0).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_3): Coulomb and the field
        self.next_band(6)
        b6_title = Tex("Electrostatics: the inverse square").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"F = \frac{kQ_1Q_2}{r^2}").scale(1.2).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"F = \frac{5{,}4 \times 10^{-2}}{10^{-2}} = 5{,}4\ \text{N}").scale(1.05).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = MathTex(r"E = \frac{F}{q}, \qquad E = \frac{kQ}{r^2}").scale(1.1).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Fields add as vectors: away from $+$,").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        b6_l5 = Tex("toward $-$ — directions first, always").scale(1.0).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_3): the circuit staple, books balanced
        self.next_band(7)
        b7_title = Tex(r"18 V, $r = 0{,}5\ \Omega$: 2 $\Omega$ with 4$\parallel$4").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"R_p = \frac{16}{8} = 2\ \Omega, \quad R_{ext} = 4\ \Omega").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"I = \frac{18}{4{,}5} = 4\ \text{A}").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = MathTex(r"V_{term} = 18 - 4 \times 0{,}5 = 16\ \text{V}").scale(1.05).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = MathTex(r"V_p = 16 - 8 = 8\ \text{V}, \quad I_4 = 2\ \text{A each}").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex(r"Audit: $2 + 2 = 4$ A — books closed").scale(1.0).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_4): electrodynamics and rms
        self.next_band(8)
        b8_title = Tex("Electrodynamics in four lines").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("Slip rings: AC; split-ring commutator: DC").scale(1.05).shift(band_shift(8) + UP * 1.4)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Motor $=$ generator run backward").scale(1.05).shift(band_shift(8) + UP * 0.7)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l5 = Tex("rms: same energy as the equivalent DC").scale(1.0).shift(band_shift(8) + UP * 0.0)
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l3a = MathTex(r"V_{rms} = \frac{V_{max}}{\sqrt{2}}").scale(1.1).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3a))
        self.wait(2)
        b8_l3 = MathTex(r"\frac{311}{1{,}41} \approx 220\ \text{V}").scale(1.05).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = MathTex(r"P_{avg} = I_{rms}V_{rms}").scale(1.1).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_4): the photoelectric close
        self.next_band(9)
        b9_title = Tex(r"Photoelectric: $E = W_0 + E_{k(max)}$").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"E = hf = 6{,}63 \times 10^{-34} \times 6{,}0 \times 10^{14}").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"E = 3{,}98 \times 10^{-19}\ \text{J}").scale(1.05).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"E_{k(max)} = (3{,}98 - 3{,}0) \times 10^{-19}").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = MathTex(r"E_{k(max)} = 9{,}8 \times 10^{-20}\ \text{J}").scale(1.05).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("Intensity counts photons; frequency sizes them").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 10 (subtopic_5): the paper as a map
        self.next_band(10)
        b10_title = Tex("The paper as a map of three territories").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("1. Mechanics — largest, highest rent").scale(1.05).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("2. Electricity and magnetism — close behind").scale(1.05).shift(band_shift(10) + UP * 0.4)
        b10_l3 = Tex("3. Doppler and photoelectric — small, predictable").scale(1.0).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("Definitions: the cheapest marks in the paper").scale(1.0).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Name the territory, name the equation,").scale(1.0).shift(band_shift(10) + DOWN * 2.3)
        b10_l6 = Tex("THEN touch the calculator").scale(1.0).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_6): force stories and energy budgets
        self.next_band(11)
        b11_title = Tex("Two stories, three ledgers").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex("Force story (newtons): dot, arrows, $F_{net} = ma$").scale(1.0).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = Tex("Energy budget (joules): height money spent,").scale(1.0).shift(band_shift(11) + UP * 0.4)
        b11_l3 = Tex("speed banked, friction pockets the gap").scale(1.0).shift(band_shift(11) + DOWN * 0.3)
        self.play(Write(b11_l2))
        self.play(Write(b11_l3))
        self.wait(2.5)
        b11_l4 = Tex("Net force for instants, energy for journeys,").scale(1.0).shift(band_shift(11) + DOWN * 1.4)
        b11_l5 = Tex("momentum for crashes").scale(1.05).shift(band_shift(11) + DOWN * 2.2)
        self.play(Write(b11_l4))
        self.play(Write(b11_l5))
        self.play(Create(SurroundingRectangle(b11_l5, color=GREEN)))
        self.wait(3.5)

        # --- Band 12 (subtopic_7): the four traps and the sweep
        self.next_band(12)
        b12_title = Tex("The classic traps, met by name").scale(1.2).shift(band_shift(12) + UP * 2.2)
        self.play(Write(b12_title))
        self.wait(2)
        b12_t1 = Tex(r"Top of flight: $a = 0$").scale(1.0).shift(band_shift(12) + UP * 1.3)
        self.play(Write(b12_t1))
        self.play(Create(strike(b12_t1)))
        b12_c1 = Tex(r"$a = 9{,}8$ down, full shifts").scale(1.0).shift(band_shift(12) + UP * 0.55)
        self.play(Write(b12_c1))
        self.wait(2)
        b12_t2 = Tex("Declare the positive direction FIRST").scale(1.0).shift(band_shift(12) + DOWN * 0.25)
        self.play(Write(b12_t2))
        self.wait(2)
        b12_t3 = Tex(r"Under load the voltmeter reads $\varepsilon - Ir$").scale(1.0).shift(band_shift(12) + DOWN * 1.05)
        self.play(Write(b12_t3))
        self.wait(2)
        b12_t4 = Tex("Brighter: more electrons, never faster ones").scale(1.0).shift(band_shift(12) + DOWN * 1.85)
        self.play(Write(b12_t4))
        self.wait(2)
        b12_l5 = Tex("Units on, directions on, books closed").scale(1.05).shift(band_shift(12) + DOWN * 2.85)
        self.play(Write(b12_l5))
        self.play(Create(SurroundingRectangle(b12_l5, color=GREEN)))
        self.wait(4)
