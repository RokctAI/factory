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

# Band-layout whiteboard scene for "The Photoelectric Effect and Atomic
# Spectra" (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only; the metal surface, photons and energy
# ladders are hand-built from Rectangles, Circles, Lines and Tex labels.
# Eleven bands; dwell follows subtopics.json (235/240/240/235/190/195/195).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PhotoelectricEffectSpectraSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # --- Band 0 (subtopic_1): the effect and the threshold
        title = Tex("The Photoelectric Effect and Atomic Spectra").scale(1.05).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        # Metal surface with a photon arriving and an electron leaving.
        c0 = DOWN * 1.0
        surface = Rectangle(width=5.0, height=0.8).move_to(c0 + DOWN * 1.2)
        lab_metal = Tex("metal surface").scale(0.7).shift(c0 + DOWN * 2.0)
        self.play(Create(surface), Write(lab_metal))
        photon = Line(c0 + UP * 1.8 + LEFT * 2.6, c0 + DOWN * 0.7 + LEFT * 0.6)
        lab_ph = Tex("photon, $E = hf$").scale(0.7).shift(c0 + UP * 2.0 + LEFT * 2.4)
        self.play(Create(photon), Write(lab_ph))
        electron = Dot(c0 + DOWN * 0.7 + RIGHT * 0.4)
        e_path = Line(c0 + DOWN * 0.7 + RIGHT * 0.4, c0 + UP * 1.6 + RIGHT * 2.2)
        lab_e = Tex("electron out").scale(0.7).shift(c0 + UP * 1.9 + RIGHT * 2.4)
        self.play(Create(electron))
        self.play(Create(e_path), Write(lab_e))
        self.wait(2.5)
        b0_l1 = Tex("Below $f_0$: nothing, at any brightness").scale(0.9).shift(UP * 1.6)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): photons and the work function
        self.next_band(1)
        b1_title = Tex("Photons and the work function").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"E = hf, \quad h = 6,63 \times 10^{-34}\ \text{J·s}").scale(0.95).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex("One photon, one electron: all or nothing").scale(0.95).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("$W_0$: minimum energy to eject an electron").scale(0.95).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"W_0 = h f_0").scale(1.05).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Waves diffract; photons eject:").scale(0.9).shift(band_shift(1) + DOWN * 2.6)
        b1_l6 = Tex("light carries both natures").scale(0.9).shift(band_shift(1) + DOWN * 3.4)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): the photoelectric equation
        self.next_band(2)
        b2_title = Tex("The photoelectric equation").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"E = W_0 + E_{k\,max}").scale(1.15).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = MathTex(r"hf = hf_0 + \tfrac{1}{2}mv_{max}^2").scale(1.0).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("Exit cost first; the change leaves as speed").scale(0.95).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("MAX: surface electrons only —").scale(0.95).shift(band_shift(2) + DOWN * 1.9)
        b2_l5 = Tex("deeper escapes pay extra, emerge slower").scale(0.95).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): full calculation on sodium
        self.next_band(3)
        b3_title = Tex("Worked: 400 nm on sodium").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"f = \frac{c}{\lambda} = \frac{3 \times 10^8}{4,0 \times 10^{-7}} = 7,5 \times 10^{14}\ \text{Hz}").scale(0.9).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"E = hf = 4,97 \times 10^{-19}\ \text{J}").scale(0.95).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"W_0 = 3,65 \times 10^{-19}\ \text{J} < E:\ \text{emission}").scale(0.9).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = MathTex(r"E_{k\,max} = (4,97 - 3,65) \times 10^{-19} = 1,32 \times 10^{-19}\ \text{J}").scale(0.85).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_2): threshold frequency and wavelength conversion
        self.next_band(4)
        b4_title = Tex("Threshold and conversions").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"f_0 = \frac{W_0}{h} = \frac{3,65 \times 10^{-19}}{6,63 \times 10^{-34}} = 5,51 \times 10^{14}\ \text{Hz}").scale(0.85).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex("Sodium ignores anything slower").scale(0.95).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("Given wavelength? Convert FIRST:").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        b4_l4 = MathTex(r"f = \frac{c}{\lambda}").scale(1.05).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)
        b4_l5 = Tex("Three moves: convert, photon energy, subtract $W_0$").scale(0.85).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): the two dials — intensity and frequency
        self.next_band(5)
        b5_title = Tex("Two dials, two jobs").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("INTENSITY: photons per second").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("$\\Rightarrow$ number of electrons per second").scale(0.95).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("FREQUENCY: energy per photon").scale(0.95).shift(band_shift(5) + DOWN * 0.6)
        b5_l4 = Tex("$\\Rightarrow$ kinetic energy per electron").scale(0.95).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)
        b5_l5 = Tex("Below threshold: brightness buys nothing —").scale(0.9).shift(band_shift(5) + DOWN * 2.4)
        b5_l6 = Tex("no electron pools two packets").scale(0.9).shift(band_shift(5) + DOWN * 3.2)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_3): the particle-nature argument
        self.next_band(6)
        b6_title = Tex("The particle-nature argument").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_wrong = Tex("Wave: any frequency works if bright enough").scale(0.9).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        self.wait(2)
        b6_l1 = Tex("Observed: instant response in faint light,").scale(0.9).shift(band_shift(6) + UP * 0.1)
        b6_l2 = Tex("a hard threshold, and $E_k$ that tracks $f$,").scale(0.9).shift(band_shift(6) + DOWN * 0.7)
        b6_l3 = Tex("ignoring brightness").scale(0.9).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("Only whole packets, one per electron,").scale(0.9).shift(band_shift(6) + DOWN * 2.4)
        b6_l5 = Tex("explain all three at once").scale(0.9).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): atomic spectra — the ladder and the lines
        self.next_band(7)
        b7_title = Tex("Atomic spectra: the ladder").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        c7 = band_shift(7) + LEFT * 2.4 + DOWN * 0.8
        rungs = VGroup(
            Line(c7 + LEFT * 1.2 + DOWN * 1.2, c7 + RIGHT * 1.2 + DOWN * 1.2),
            Line(c7 + LEFT * 1.2 + DOWN * 0.2, c7 + RIGHT * 1.2 + DOWN * 0.2),
            Line(c7 + LEFT * 1.2 + UP * 0.5, c7 + RIGHT * 1.2 + UP * 0.5),
            Line(c7 + LEFT * 1.2 + UP * 1.0, c7 + RIGHT * 1.2 + UP * 1.0),
        )
        self.play(Create(rungs))
        drop = Line(c7 + UP * 1.0, c7 + DOWN * 0.2)
        lab_drop = MathTex(r"E = hf = E_2 - E_1").scale(0.8).shift(c7 + RIGHT * 3.4 + UP * 0.4)
        self.play(Create(drop), Write(lab_drop))
        self.wait(2.5)
        b7_l1 = Tex("Emission: bright lines on black").scale(0.9).shift(band_shift(7) + DOWN * 2.4)
        b7_l2 = Tex("Absorption: dark lines on a rainbow — same places").scale(0.85).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_5): the bouncer at the metal's door
        self.next_band(8)
        b8_title = Tex("The bouncer at the metal's door").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Exit fee $=$ work function, fixed per metal").scale(0.9).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Photons are customers; frequency is their cash").scale(0.9).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Single payments only: no pooling, no loans").scale(0.9).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Cash short: nothing happens, ever").scale(0.9).shift(band_shift(8) + DOWN * 1.6)
        b8_l5 = Tex("Cash enough: out instantly, change $=$ speed").scale(0.9).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): ten soft throws never beat one hard throw
        self.next_band(9)
        b9_title = Tex("Ten soft throws never beat one hard throw").scale(1.0).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Strength machine: resets between swings").scale(0.9).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.play(Create(SurroundingRectangle(b9_l1, color=GREEN)))
        self.wait(2.5)
        b9_l2 = Tex("Force of a swing $=$ frequency").scale(0.9).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("Swings per minute $=$ intensity").scale(0.9).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("Soft tempo: silence forever").scale(0.9).shift(band_shift(9) + DOWN * 1.5)
        b9_l5 = Tex("Hard swings: every one rings; surplus $=$ $E_k$").scale(0.9).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(2.5)
        b9_l6 = Tex("Never write: brighter $=$ faster electrons").scale(0.9).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l6))
        self.wait(3)

        # --- Band 10 (subtopic_7): every element signs its light
        self.next_band(10)
        b10_title = Tex("Every element signs its light").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Fixed rungs $\\rightarrow$ fixed drops $\\rightarrow$ fixed colours").scale(0.9).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.play(Create(SurroundingRectangle(b10_l1, color=GREEN)))
        self.wait(2.5)
        b10_l2 = Tex("Hot gas: bright lines. Cool gas: dark lines.").scale(0.9).shift(band_shift(10) + UP * 0.2)
        b10_l3 = Tex("Same positions: one autograph, two inks").scale(0.9).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("Helium: read in sunlight before").scale(0.9).shift(band_shift(10) + DOWN * 1.5)
        b10_l5 = Tex("it was found on Earth").scale(0.9).shift(band_shift(10) + DOWN * 2.3)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2)
        b10_l6 = Tex("Pattern slides red: the star is receding").scale(0.9).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10_l6))
        self.wait(4)
