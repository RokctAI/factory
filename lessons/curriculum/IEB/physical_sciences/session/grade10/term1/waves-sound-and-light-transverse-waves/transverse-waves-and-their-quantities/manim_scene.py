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

# Band-layout whiteboard scene for "Transverse Waves and Their Quantities"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe mobjects only; write-only reveals; camera moves down band by
# band. Band time apportioned to subtopics.json
# (215/225/250/220/180/190/190 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TransverseWavesQuantitiesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): pulse to wave ---
        title = Tex("Transverse Waves and Their Quantities").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("one snap: a PULSE — a single disturbance").scale(1.0).shift(UP * 1.4)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("steady snapping: a WAVE — a train of pulses").scale(1.0).shift(UP * 0.6)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("medium moves at right angles to travel").scale(1.0).shift(DOWN * 0.4)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2)
        b0_l4 = Tex("energy is transferred, the rope stays —").scale(1.0).shift(DOWN * 1.5)
        b0_l5 = Tex("overlaps add, then pulses continue unchanged").scale(1.0).shift(DOWN * 2.3)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_2): the labelled wave picture ---
        self.next_band(1)
        b1_t = Tex("Crest, trough, amplitude, wavelength").scale(1.1).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_t))
        self.wait(1.5)
        rest = DashedLine(band_shift(1) + LEFT * 4.2 + UP * 0.3, band_shift(1) + RIGHT * 4.2 + UP * 0.3)
        self.play(Create(rest))
        wave = VGroup(
            Line(band_shift(1) + LEFT * 4.0 + UP * 0.3, band_shift(1) + LEFT * 3.0 + UP * 1.3, color=BLUE),
            Line(band_shift(1) + LEFT * 3.0 + UP * 1.3, band_shift(1) + LEFT * 1.0 + DOWN * 0.7, color=BLUE),
            Line(band_shift(1) + LEFT * 1.0 + DOWN * 0.7, band_shift(1) + RIGHT * 1.0 + UP * 1.3, color=BLUE),
            Line(band_shift(1) + RIGHT * 1.0 + UP * 1.3, band_shift(1) + RIGHT * 3.0 + DOWN * 0.7, color=BLUE),
            Line(band_shift(1) + RIGHT * 3.0 + DOWN * 0.7, band_shift(1) + RIGHT * 4.0 + UP * 0.3, color=BLUE),
        )
        self.play(Create(wave))
        crest_d = Dot(band_shift(1) + LEFT * 3.0 + UP * 1.3, color=YELLOW)
        crest_lab = Tex("crest").scale(0.8).shift(band_shift(1) + LEFT * 3.0 + UP * 1.8)
        trough_d = Dot(band_shift(1) + LEFT * 1.0 + DOWN * 0.7, color=RED)
        trough_lab = Tex("trough").scale(0.8).shift(band_shift(1) + LEFT * 1.0 + DOWN * 1.2)
        self.play(Create(crest_d), Write(crest_lab), Create(trough_d), Write(trough_lab))
        self.wait(2)
        amp = Arrow(band_shift(1) + RIGHT * 1.0 + UP * 0.3, band_shift(1) + RIGHT * 1.0 + UP * 1.3,
                    buff=0, color=GREEN)
        amp_lab = MathTex(r"A = 0{,}08\;\text{m}").scale(0.85).shift(band_shift(1) + RIGHT * 2.3 + UP * 0.8)
        self.play(Create(amp), Write(amp_lab))
        self.wait(2)
        b1_l1 = Tex("crest to trough is TWO amplitudes").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l1))
        self.play(Create(strike(b1_l1)))
        b1_l2 = MathTex(r"\lambda:\ \text{crest to the very next crest}").scale(0.95).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l2))
        self.wait(3)

        # --- Band 2 (subtopic_2): in phase, out of phase ---
        self.next_band(2)
        b2_t = Tex("In phase, out of phase").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("IN PHASE: same displacement AND").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("same direction — whole wavelengths apart").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(VGroup(b2_l1, b2_l2), color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex("OUT OF PHASE: opposite jobs —").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"\tfrac{1}{2}\lambda,\ 1\tfrac{1}{2}\lambda,\ 2\tfrac{1}{2}\lambda\ \text{apart}").scale(1.0).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("amplitude: up-down and energy; wavelength: along and spacing").scale(0.85).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_3): period, frequency, cork example ---
        self.next_band(3)
        b3_t = Tex("Period and frequency: reciprocals").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("T: time for ONE wave to pass (s)").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("f: waves passing PER SECOND (Hz)").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"f = \frac{1}{T} \qquad T = \frac{1}{f}").scale(1.1).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = MathTex(r"f = \frac{10}{4} = 2{,}5\;\text{Hz}").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        b3_l5 = MathTex(r"T = \frac{1}{2{,}5} = 0{,}4\;\text{s}").scale(1.0).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the wave equation, both ways ---
        self.next_band(4)
        b4_t = MathTex(r"v = f\lambda").scale(1.4).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.play(Create(SurroundingRectangle(b4_t, color=GREEN)))
        self.wait(2)
        b4_l1 = Tex("one period on, one wavelength gained").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"v = (25)(0{,}02) = 0{,}5\;\text{m·s}^{-1}").scale(1.05).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)
        b4_l3 = MathTex(r"f = \frac{1}{0{,}8} = 1{,}25\;\text{Hz}").scale(1.0).shift(band_shift(4) + DOWN * 1.0)
        b4_l4 = MathTex(r"\lambda = \frac{2{,}4}{1{,}25} = 1{,}92\;\text{m}").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex("formula, substitution, answer with unit").scale(0.95).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): the four traps ---
        self.next_band(5)
        b5_t = Tex("The four traps").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"2\;\text{cm} \to 0{,}02\;\text{m};\ 40\;\text{ms} \to 0{,}04\;\text{s}").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"2\;\text{kHz} \to 2\,000\;\text{Hz}").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("amplitude from crest to trough").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l3))
        self.play(Create(strike(b5_l3)))
        self.wait(2)
        b5_l4 = MathTex(r"T = 0{,}2\;\text{s} \iff f = 5\;\text{Hz}").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l4))
        b5_l5 = Tex("write the unit next to every number").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): graphs and the speed misconception ---
        self.next_band(6)
        b6_t = Tex("Read the horizontal axis FIRST").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("vs POSITION: snapshot — repeat = wavelength").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("vs TIME: one particle — repeat = period").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(VGroup(b6_l1, b6_l2), color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex("higher frequency = faster wave").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l3))
        self.play(Create(strike(b6_l3)))
        self.wait(2)
        b6_l4 = Tex("source sets f, medium sets v,").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        b6_l5 = Tex("wavelength adjusts to balance").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the wave in the stands ---
        self.next_band(7)
        b7_t = Tex("The wave in the stands").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("people go UP and DOWN into the same seat").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("the wave goes SIDEWAYS around the ground").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex("right angles = transverse").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("what travels: the ENERGY of standing,").scale(1.0).shift(band_shift(7) + DOWN * 1.7)
        b7_l5 = Tex("handed block to block — never the people").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): the skipping rope measurements ---
        self.next_band(8)
        b8_t = Tex("Measuring with a skipping rope").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("amplitude: flat line up to hump-top").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("wavelength: hump-top to next hump-top").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("double your rhythm: humps half as long").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = MathTex(r"5\ \text{humps/s} \iff 0{,}2\;\text{s each}").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = Tex("flip one number and the other appears").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): one sum that does everything ---
        self.next_band(9)
        b9_t = Tex("One sum that does everything").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("humps per second, times length of each").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"25 \times 0{,}02 = 0{,}5\;\text{m per second}").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2)
        b9_l3 = MathTex(r"\frac{1}{0{,}8} = 1{,}25\ \text{per s};\ \ \frac{2{,}4}{1{,}25} = 1{,}92\;\text{m}").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("convert first, multiply second,").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        b9_l5 = Tex("and read the bottom axis before measuring").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(4)
