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
        title = Tex("The Electromagnetic Spectrum").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("born from an ACCELERATING charge").scale(1.0).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("two fields, at right angles, regenerate").scale(0.95).shift(UP * 0.4)
        b0_l3 = Tex("each other — so NO MEDIUM needed").scale(0.95).shift(DOWN * 0.3)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2)
        b0_l4 = MathTex(r"c = 3 \times 10^{8}\;\text{m·s}^{-1}\ \text{for every member}").scale(0.95).shift(DOWN * 1.4)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the wave sketch + dual nature ---
        self.next_band(1)
        b1_t = Tex("Transverse fields, and a dual nature").scale(1.1).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_t))
        self.wait(1.5)
        travel = Arrow(band_shift(1) + LEFT * 3.5 + UP * 1.0, band_shift(1) + RIGHT * 3.5 + UP * 1.0, buff=0, color=YELLOW)
        travel_lab = Tex("direction of travel").scale(0.8).shift(band_shift(1) + RIGHT * 2.0 + UP * 1.5)
        e_ar = Arrow(band_shift(1) + LEFT * 1.0 + UP * 1.0, band_shift(1) + LEFT * 1.0 + UP * 2.0, buff=0, color=BLUE)
        e_lab = Tex("electric field").scale(0.75).shift(band_shift(1) + LEFT * 2.4 + UP * 1.9)
        m_dot = Dot(band_shift(1) + LEFT * 1.0 + UP * 1.0, color=RED)
        m_lab = Tex("magnetic field, out of the board").scale(0.75).shift(band_shift(1) + LEFT * 0.6 + UP * 0.4)
        self.play(Create(travel), Write(travel_lab))
        self.play(Create(e_ar), Write(e_lab), Create(m_dot), Write(m_lab))
        self.wait(2.5)
        b1_l1 = Tex("wave model: reflection, refraction,").scale(0.9).shift(band_shift(1) + DOWN * 0.8)
        b1_l2 = Tex("diffraction, interference").scale(0.9).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("particle model: photons — fixed packets").scale(0.9).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the seven bands in order ---
        self.next_band(2)
        b2_t = Tex("The seven bands, in order").scale(1.15).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("radio — microwave — infrared —").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("visible — ultraviolet — X-rays — gamma").scale(1.0).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(VGroup(b2_l1, b2_l2), color=GREEN)))
        self.wait(2.5)
        freq_ar = Arrow(band_shift(2) + LEFT * 3.5 + DOWN * 0.6, band_shift(2) + RIGHT * 3.5 + DOWN * 0.6, buff=0, color=YELLOW)
        freq_lab = Tex("frequency rises this way").scale(0.85).shift(band_shift(2) + DOWN * 1.2)
        self.play(Create(freq_ar), Write(freq_lab))
        wav_ar = Arrow(band_shift(2) + RIGHT * 3.5 + DOWN * 1.9, band_shift(2) + LEFT * 3.5 + DOWN * 1.9, buff=0, color=BLUE)
        wav_lab = Tex("wavelength grows this way").scale(0.85).shift(band_shift(2) + DOWN * 2.5)
        self.play(Create(wav_ar), Write(wav_lab))
        self.wait(3)

        # --- Band 3 (subtopic_2): energy and penetration rise together ---
        self.next_band(3)
        b3_t = Tex("Along the spectrum, two things climb").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("energy per photon rises with frequency").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("penetrating ability rises with energy").scale(0.95).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("visible: 400 nm violet to 700 nm red").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("ionising: UV, X-rays, gamma —").scale(0.95).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = Tex("energetic enough to strip electrons").scale(0.95).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(VGroup(b3_l4, b3_l5), color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): c = f lambda, two-way radio worked ---
        self.next_band(4)
        b4_t = MathTex(r"c = f\lambda").scale(1.4).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.play(Create(SurroundingRectangle(b4_t, color=GREEN)))
        self.wait(2)
        b4_l1 = MathTex(r"150\;\text{MHz} = 1{,}5 \times 10^{8}\;\text{Hz}").scale(1.0).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\lambda = \frac{3 \times 10^{8}}{1{,}5 \times 10^{8}} = 2\;\text{m}").scale(1.05).shift(band_shift(4) + DOWN * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)
        b4_l3 = Tex("hence the metre-long aerial;").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        b4_l4 = Tex("oven waves 0,12 m — trapped by the mesh").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): E = hf, UV photon worked ---
        self.next_band(5)
        b5_t = MathTex(r"E = hf, \quad h = 6{,}63 \times 10^{-34}\;\text{J·s}").scale(1.0).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.play(Create(SurroundingRectangle(b5_t, color=GREEN)))
        self.wait(2)
        b5_l1 = MathTex(r"300\;\text{nm} = 3 \times 10^{-7}\;\text{m}").scale(0.95).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"f = \frac{3 \times 10^{8}}{3 \times 10^{-7}} = 1 \times 10^{15}\;\text{Hz}").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"E = (6{,}63 \times 10^{-34})(1 \times 10^{15}) = 6{,}63 \times 10^{-19}\;\text{J}").scale(0.9).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = Tex("radio photon: nearly seven million times weaker").scale(0.85).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): uses and dangers from photon energy ---
        self.next_band(6)
        b6_t = Tex("Uses and dangers follow the photon").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("radio: signals — harmless").scale(0.9).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex("microwave: cooking, links — heats tissue").scale(0.9).shift(band_shift(6) + UP * 0.6)
        b6_l3 = Tex("infrared: remotes, heaters — burns").scale(0.9).shift(band_shift(6) + DOWN * 0.1)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("UV: steriliser, vitamin D — skin cancer").scale(0.9).shift(band_shift(6) + DOWN * 0.9)
        b6_l5 = Tex("X-rays: bones, welds — cell damage").scale(0.9).shift(band_shift(6) + DOWN * 1.6)
        b6_l6 = Tex("gamma: radiotherapy — most ionising").scale(0.9).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the named traps ---
        self.next_band(7)
        b7_t = Tex("The five traps").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"300\;\text{nm} = 3 \times 10^{-7}\;\text{m, never } 300").scale(0.9).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("gamma rays travel faster than radio").scale(0.95).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l2))
        self.play(Create(strike(b7_l2)))
        self.wait(2)
        b7_l3 = Tex("exponent key for powers of ten").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        b7_l4 = MathTex(r"E = \frac{hc}{\lambda}\ \text{wants metres}").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l4))
        b7_l5 = Tex("photon energy answers in JOULES").scale(0.95).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): one family, same speed ---
        self.next_band(8)
        b8_t = Tex("One family, same speed").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("all cross empty space at 300 million m/s").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.play(Create(SurroundingRectangle(b8_l1, color=GREEN)))
        self.wait(2)
        b8_l2 = Tex("only difference: how tightly packed").scale(0.95).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("radio, microwave, infrared, visible,").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = Tex("ultraviolet, X-rays, gamma").scale(0.95).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("infra-red: below red; ultra-violet: beyond violet").scale(0.85).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the see-saw and the punch ---
        self.next_band(9)
        b9_t = Tex("The see-saw and the punch").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("speed bolted down: shorter waves,").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("more arrivals per second — always").scale(0.95).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"150\ \text{million/s} \to 2\;\text{m each}").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("punch: shorter wave, harder packet —").scale(0.95).shift(band_shift(9) + DOWN * 1.5)
        b9_l5 = Tex("UV lands seven million times a radio tap").scale(0.9).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): sunscreen, remote, lead apron ---
        self.next_band(10)
        b10_t = Tex("Sunscreen, the remote, the lead apron").scale(1.05).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("radio wakes you; microwave heats breakfast").scale(0.9).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex("infrared presses the remote; light shows it all").scale(0.9).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("UV outside: vitamin D, but hat and sunscreen").scale(0.9).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("X-rays at the dentist: through cheek, stopped by teeth").scale(0.85).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(b10_l4))
        b10_l5 = Tex("gamma at the hospital: aimed to kill tumours").scale(0.9).shift(band_shift(10) + DOWN * 2.3)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
