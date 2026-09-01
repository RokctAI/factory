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

# Band-layout whiteboard scene for "Paper One Physics Essentials" (Part 1 —
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
        title = Tex("Physics Essentials: The Final Sweep").scale(1.2).to_edge(UP)
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
        b0_l5 = Tex("Bare statements are worth marks: word-perfect").scale(0.95).shift(DOWN * 2.3)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the crate, and the incline split
        self.next_band(1)
        b1_title = Tex("The force story, run once").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"F_{net} = 100 - 28 = 72\ \text{N}").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"a = \frac{72}{8} = 9\ \text{m}\cdot\text{s}^{-2}").scale(1.05).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("On an incline, split the weight first:").scale(1.0).shift(band_shift(1) + DOWN * 1.0)
        b1_l4 = MathTex(r"mg\sin\theta\ \text{along},\quad mg\cos\theta\ \text{into}").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_1): impulse with sign discipline
        self.next_band(2)
        b2_title = Tex("Impulse: declare the positive direction").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("0,4 kg ball: in at 12, back at 9 m·s$^{-1}$").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"\Delta p = 0{,}4(-9 - 12) = -8{,}4\ \text{kg}\cdot\text{m}\cdot\text{s}^{-1}").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"F_{net} = \frac{-8{,}4}{0{,}05} = -168\ \text{N}").scale(1.05).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = Tex("168 N away from the wall — direction included").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_1): conservation and the elastic test
        self.next_band(3)
        b3_title = Tex("Coupling: 3 kg at 4 meets 1 kg at rest").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"p = 12 \Rightarrow v = \frac{12}{4} = 3\ \text{m}\cdot\text{s}^{-1}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"E_k: \ 24\ \text{J} \rightarrow 18\ \text{J}").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("Energy lost: INELASTIC — decided by arithmetic").scale(1.0).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_2): the standard vertical flight
        self.next_band(4)
        b4_title = Tex("Up at 24,5 m·s$^{-1}$ — the standard flight").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"t_{top} = \frac{24{,}5}{9{,}8} = 2{,}5\ \text{s}").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"\Delta y = \frac{24{,}5^2}{2 \times 9{,}8} = \frac{600{,}25}{19{,}6} = 30{,}63\ \text{m}").scale(1.0).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"v(4) = 24{,}5 - 9{,}8 \times 4 = -14{,}7\ \text{m}\cdot\text{s}^{-1}").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("At the top: $v = 0$, but $a$ is still 9,8 down").scale(0.95).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_2): energy budgets and power
        self.next_band(5)
        b5_title = Tex("The energy budget on the rough ramp").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"E_p\ \text{spent}: 2 \times 9{,}8 \times 4 = 78{,}4\ \text{J}").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"E_k\ \text{banked}: \tfrac{1}{2} \times 2 \times 49 = 49\ \text{J}").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"W_{friction} = 49 - 78{,}4 = -29{,}4\ \text{J}").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = MathTex(r"\text{Pump: } P = \frac{29\,400}{14} = 2\,100\ \text{W}").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_3): Coulomb and the field
        self.next_band(6)
        b6_title = Tex("Coulomb: inverse square, always").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"F = \frac{kQ_1Q_2}{r^2} = \frac{9 \times 10^9 \times 4 \times 10^{-6} \times 2 \times 10^{-6}}{(0{,}2)^2}").scale(0.85).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"F = \frac{7{,}2 \times 10^{-2}}{4 \times 10^{-2}} = 1{,}8\ \text{N}").scale(1.0).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex("Fields: away from $+$, toward $-$,").scale(1.0).shift(band_shift(6) + DOWN * 1.1)
        b6_l4 = Tex("added as vectors, contribution by contribution").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_3): the circuit staple, books balanced
        self.next_band(7)
        b7_title = Tex(r"emf 12 V, $r = 0{,}5\ \Omega$: outside-in").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"4 \| 4 = 2\ \Omega,\ \ R_{ext} = 3{,}5\ \Omega,\ \ R_{tot} = 4\ \Omega").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"I = \frac{12}{4} = 3\ \text{A},\quad V_{term} = 12 - 1{,}5 = 10{,}5\ \text{V}").scale(0.95).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"V_{pair} = 6\ \text{V} \Rightarrow 1{,}5\ \text{A per branch}").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Audit: $1{,}5 + 1{,}5 = 3$ A — books balanced").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): electrodynamics and rms
        self.next_band(8)
        b8_title = Tex("Generators, motors, and rms").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("AC: slip rings, sine-wave output").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("DC: split-ring commutator, one polarity").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"V_{rms} = \frac{V_{max}}{\sqrt{2}} = \frac{311}{1{,}41} \approx 220\ \text{V}").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("rms: the AC value matching DC energy delivery").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_4): the photoelectric close
        self.next_band(9)
        b9_title = Tex(r"Photoelectric: $E = W_0 + E_{k,max}$").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(1.5)
        b9_l1 = MathTex(r"E = hf = 6{,}63 \times 10^{-34} \times 7{,}5 \times 10^{14}").scale(0.95).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"E = 4{,}97 \times 10^{-19}\ \text{J}").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"E_{k,max} = 4{,}97 - 3{,}7 = 1{,}27 \times 10^{-19}\ \text{J}").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Intensity counts photons; frequency sizes them").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 10 (subtopic_5): the syllabus as a map
        self.next_band(10)
        b10_title = Tex("Three territories").scale(1.2).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_title))
        self.wait(1.5)
        r1 = Rectangle(width=5.2, height=1.0).shift(band_shift(10) + UP * 1.2)
        t1 = Tex("Mechanics — the broadest").scale(0.9).shift(band_shift(10) + UP * 1.2)
        r2 = Rectangle(width=4.4, height=1.0).shift(band_shift(10) + UP * 0.0)
        t2 = Tex("Electricity and magnetism").scale(0.9).shift(band_shift(10) + UP * 0.0)
        r3 = Rectangle(width=3.6, height=1.0).shift(band_shift(10) + DOWN * 1.2)
        t3 = Tex("Doppler and photoelectric").scale(0.9).shift(band_shift(10) + DOWN * 1.2)
        self.play(Create(r1), Write(t1))
        self.wait(1.5)
        self.play(Create(r2), Write(t2))
        self.wait(1.5)
        self.play(Create(r3), Write(t3))
        self.wait(2)
        b10_l1 = Tex("Border control: definitions, word for word").scale(0.95).shift(band_shift(10) + DOWN * 2.4)
        b10_l2 = Tex("Currency: choosing the equation before the calculator").scale(0.95).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(3)

        # --- Band 11 (subtopic_6): force stories and energy budgets
        self.next_band(11)
        b11_title = Tex("Two stories, three ledgers").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(1.5)
        b11_l1 = Tex("Force story: instants — dot, arrows, $F_{net} = ma$").scale(0.95).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11_l1))
        self.wait(2)
        b11_l2 = Tex("Energy budget: journeys — joules in, joules out,").scale(0.95).shift(band_shift(11) + UP * 0.3)
        b11_l3 = Tex("friction takes its cut as heat").scale(0.95).shift(band_shift(11) + DOWN * 0.4)
        self.play(Write(b11_l2))
        self.play(Write(b11_l3))
        self.wait(2.5)
        b11_l4 = Tex("Momentum ledger: crashes — before equals after").scale(0.95).shift(band_shift(11) + DOWN * 1.3)
        self.play(Write(b11_l4))
        self.wait(2)
        b11_l5 = Tex("Instants, journeys, crashes — pick first, then compute").scale(0.95).shift(band_shift(11) + DOWN * 2.2)
        self.play(Write(b11_l5))
        self.play(Create(SurroundingRectangle(b11_l5, color=GREEN)))
        self.wait(3)

        # --- Band 12 (subtopic_7): the four traps and the sweep
        self.next_band(12)
        b12_title = Tex("Four traps, named").scale(1.15).shift(band_shift(12) + UP * 2.4)
        self.play(Write(b12_title))
        self.wait(1.5)
        b12_l1 = Tex("1. Top of flight: $v = 0$, $a$ still 9,8").scale(0.95).shift(band_shift(12) + UP * 1.4)
        b12_l2 = Tex("2. Declare the positive direction first").scale(0.95).shift(band_shift(12) + UP * 0.6)
        b12_l3 = Tex("3. Under load: terminal V $=$ emf $-$ $Ir$").scale(0.95).shift(band_shift(12) + DOWN * 0.2)
        b12_l4 = Tex("4. Brighter $\\neq$ faster electrons").scale(0.95).shift(band_shift(12) + DOWN * 1.0)
        self.play(Write(b12_l1))
        self.wait(2)
        self.play(Write(b12_l2))
        self.wait(2)
        self.play(Write(b12_l3))
        self.wait(2)
        self.play(Write(b12_l4))
        self.wait(2.5)
        b12_l5 = Tex("Units on every answer; audit every circuit").scale(0.95).shift(band_shift(12) + DOWN * 2.0)
        self.play(Write(b12_l5))
        self.play(Create(SurroundingRectangle(b12_l5, color=GREEN)))
        self.wait(4)
