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

# Band-layout whiteboard scene for "The Electromagnetic Spectrum" (Part 1
# Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe
# mobjects only; write-only reveals; camera moves down band by band. Band
# time apportioned to subtopics.json (225/225/250/230/180/185/185 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ElectromagneticSpectrumSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): what an EM wave is ---
        title = Tex("The Electromagnetic Spectrum").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Made by an ACCELERATING electric charge").scale(1.05).shift(UP * 1.1)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex(r"E-field $\perp$ B-field $\perp$ travel: TRANSVERSE").scale(1.0).shift(UP * 0.2)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("The fields regenerate each other:").scale(1.0).shift(DOWN * 0.7)
        b0_l4 = Tex("NO MEDIUM needed — light crosses vacuum").scale(1.0).shift(DOWN * 1.5)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        b0_l5 = MathTex(r"c = 3 \times 10^8\;\text{m·s}^{-1} \text{ for ALL of them}").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the wave sketch + dual nature ---
        self.next_band(1)
        b1_t = Tex("One wave, two models").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        # transverse wave as a chained polyline
        pts = [LEFT * 3.0 + UP * 0.9, LEFT * 2.0 + UP * 1.7, LEFT * 1.0 + UP * 0.9,
               RIGHT * 0.0 + UP * 0.1, RIGHT * 1.0 + UP * 0.9, RIGHT * 2.0 + UP * 1.7,
               RIGHT * 3.0 + UP * 0.9]
        wave = VGroup(*[Line(band_shift(1) + pts[i], band_shift(1) + pts[i + 1], color=BLUE)
                        for i in range(len(pts) - 1)])
        self.play(Create(wave))
        trav = Arrow(band_shift(1) + RIGHT * 3.3 + UP * 0.9, band_shift(1) + RIGHT * 4.3 + UP * 0.9,
                     buff=0, color=YELLOW)
        self.play(Create(trav))
        self.wait(2)
        b1_l1 = Tex("Wave model: reflection, refraction,").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        b1_l2 = Tex("diffraction, interference").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Particle model: PHOTONS — fixed packets").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_l3))
        b1_l4 = Tex("of energy; both models are needed").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the seven bands in order ---
        self.next_band(2)
        b2_t = Tex("The spectrum in order").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        rail = Arrow(band_shift(2) + LEFT * 4.6 + UP * 0.9, band_shift(2) + RIGHT * 4.8 + UP * 0.9,
                     buff=0, color=WHITE)
        self.play(Create(rail))
        names = ["radio", "micro", "IR", "visible", "UV", "X-ray", "gamma"]
        xs = [-4.0, -2.7, -1.5, -0.2, 1.2, 2.4, 3.8]
        labels = VGroup(*[Tex(n).scale(0.8).shift(band_shift(2) + RIGHT * x + UP * 1.5)
                          for n, x in zip(names, xs)])
        ticks = VGroup(*[Line(band_shift(2) + RIGHT * x + UP * 0.75,
                              band_shift(2) + RIGHT * x + UP * 1.05) for x in xs])
        self.play(Create(ticks), Write(labels))
        self.wait(2.5)
        b2_l1 = Tex(r"left: long $\lambda$, low $f$ — right: short $\lambda$, high $f$").scale(1.0).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex(r"Visible: 400--700 nm, red long, violet short").scale(1.0).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex(r"$f \times \lambda$ must always equal $c$").scale(1.05).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): energy and penetration rise together ---
        self.next_band(3)
        b3_t = Tex("What rises along the spectrum").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("Energy per photon rises with frequency").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("Penetrating ability rises with energy").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("Ionising radiation strips electrons off atoms").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("The ionising three: UV, X-rays, gamma").scale(1.05).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): c = f lambda, FM worked ---
        self.next_band(4)
        b4_t = Tex(r"FM radio at 100 MHz — find $\lambda$").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"c = f\lambda \;\Rightarrow\; \lambda = \frac{c}{f}").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"100\;\text{MHz} = 1 \times 10^8\;\text{Hz}").scale(1.05).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"\lambda = \frac{3 \times 10^8}{1 \times 10^8} = 3\;\text{m}").scale(1.1).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = Tex(r"Oven at $2{,}45 \times 10^9$ Hz: $\lambda \approx 0{,}12$ m").scale(1.0).shift(band_shift(4) + DOWN * 2.1)
        b4_l5 = Tex("door mesh holes are smaller — waves stay in").scale(0.95).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): E = hf, UV photon worked ---
        self.next_band(5)
        b5_t = Tex(r"UV at 250 nm — find $f$ and $E$").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"250\;\text{nm} = 2{,}5 \times 10^{-7}\;\text{m}").scale(1.05).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"f = \frac{3 \times 10^8}{2{,}5 \times 10^{-7}} = 1{,}2 \times 10^{15}\;\text{Hz}").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"E = hf = (6{,}63 \times 10^{-34})(1{,}2 \times 10^{15})").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"E = 7{,}96 \times 10^{-19}\;\text{J}").scale(1.05).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex(r"radio photon: $6{,}63 \times 10^{-26}$ J — 12 million $\times$ less").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): uses and dangers from photon energy ---
        self.next_band(6)
        b6_t = Tex("Uses and dangers follow the energy").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("Radio: broadcasting — harmless").scale(0.95).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(1.5)
        b6_l2 = Tex("Micro: cooking, cell links — heats tissue").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l2))
        self.wait(1.5)
        b6_l3 = Tex("IR: remotes, thermal imaging — burns").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l3))
        self.wait(1.5)
        b6_l4 = Tex("UV: vitamin D, sterilising — skin cancer").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l4))
        self.wait(1.5)
        b6_l5 = Tex("X-rays: imaging bones — cell damage").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l5))
        self.wait(1.5)
        b6_l6 = Tex("Gamma: radiotherapy — most ionising").scale(0.95).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): the named traps ---
        self.next_band(7)
        b7_t = Tex("The traps, named").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"\lambda = 250 \quad \text{(nm left in!)}").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.play(Create(strike(b7_l1)))
        self.wait(2)
        b7_l2 = Tex("``gamma rays travel faster than radio''").scale(1.0).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.play(Create(strike(b7_l2)))
        self.wait(2)
        b7_l3 = Tex("same speed in vacuum — only more energetic").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex(r"$E = \tfrac{hc}{\lambda}$ needs metres; answer in J").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): one family, same speed ---
        self.next_band(8)
        b8_t = Tex("One family, same speed").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("All of them: 300 million metres a second").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Only difference: how tightly packed").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("radio, micro, IR, light, UV, X, gamma").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("Infra-red: below red — braai warmth").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        b8_l5 = Tex("Ultra-violet: beyond violet — sunburn").scale(1.0).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the see-saw and the punch ---
        self.next_band(9)
        b9_t = Tex("The see-saw and the punch").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex(r"Speed is stuck, so $f$ and $\lambda$ trade off").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("FM: 100 million waves a second, 3 m each").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Oven: 2,5 billion a second, 12 cm each").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Shorter wave = harder punch per packet").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex(r"one UV packet $\approx$ 12 million radio packets").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): sunscreen, remote, lead apron ---
        self.next_band(10)
        b10_t = Tex("Sunscreen, the remote, the lead apron").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Radio through walls; microwave shakes water").scale(0.95).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex("IR runs the remote; light runs your eyes").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("UV: vitamin D, but hat and sunscreen —").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        b10_l4 = Tex("cloud does not stop it").scale(0.95).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("X-ray shows bone; apron guards the cells").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l5))
        self.wait(2)
        b10_l6 = Tex("Explain use AND danger from the punch").scale(1.0).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
