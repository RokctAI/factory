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

# Band-layout whiteboard scene for "Longitudinal Waves and Sound" (Part 1
# Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe
# mobjects only; write-only reveals; camera moves down band by band. Band
# time apportioned to subtopics.json (225/230/230/240/185/180/190 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class LongitudinalWavesSoundSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the definition + slinky picture ---
        title = Tex("Longitudinal Waves and Sound").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Particles vibrate PARALLEL to the travel").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=GREEN)))
        self.wait(2)
        # slinky: dots bunched (compression) and spread (rarefaction)
        xs = [-4.2, -3.9, -3.6, -3.3, -2.4, -1.4, -0.4, 0.0, 0.3, 0.6, 0.9,
              1.8, 2.8, 3.8]
        coils = VGroup(*[Dot(RIGHT * x + DOWN * 0.2, radius=0.07, color=BLUE) for x in xs])
        self.play(Create(coils))
        trav = Arrow(RIGHT * 4.2 + DOWN * 0.2, RIGHT * 5.4 + DOWN * 0.2, buff=0, color=YELLOW)
        self.play(Create(trav))
        self.wait(1.5)
        comp = Tex("compression").scale(0.9).shift(LEFT * 3.7 + DOWN * 1.1)
        rare = Tex("rarefaction").scale(0.9).shift(LEFT * 1.4 + UP * 0.6)
        self.play(Write(comp))
        self.play(Write(rare))
        self.wait(2)
        b0_l2 = Tex("crowded: pressure high — spread: pressure low").scale(0.95).shift(DOWN * 2.0)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("squash, gap, squash, gap — marching along").scale(0.95).shift(DOWN * 2.8)
        self.play(Write(b0_l3))
        self.wait(3)

        # --- Band 1 (subtopic_1): the carried-over quantities ---
        self.next_band(1)
        b1_t = Tex("Same quantities, new picture").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex(r"$\lambda$: compression to next compression, in m").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Amplitude: max displacement from rest, in m").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Period in s; frequency in Hz").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"f = \frac{1}{T} \qquad v = f\lambda").scale(1.2).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex("travels in solids, liquids AND gases").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): sound needs a medium ---
        self.next_band(2)
        b2_t = Tex("Sound: made by a vibrating object").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("a wave of PRESSURE, not moving air").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("Bell jar: pump the air out, bell falls silent").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("No particles, no compressions, no sound").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = Tex("Audible range: 20 Hz to 20 000 Hz").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): the medium sets the speed ---
        self.next_band(3)
        b3_t = Tex("The medium fixes the speed").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("Fastest in solids, slower in liquids,").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("slowest in gases").scale(1.0).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"\text{steel} \approx 5\,000\;\text{m·s}^{-1}").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l3))
        self.wait(1.5)
        b3_l3b = MathTex(r"\text{water} \approx 1\,500\;\text{m·s}^{-1}").scale(1.0).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3b))
        self.wait(1.5)
        b3_l4 = MathTex(r"\text{air} \approx 340\;\text{m·s}^{-1}").scale(1.05).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex("closer, tighter particles pass it on faster").scale(1.0).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the three dials ---
        self.next_band(4)
        b4_t = Tex("Pitch, loudness, quality").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("PITCH is set by FREQUENCY").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("LOUDNESS is set by AMPLITUDE").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("QUALITY is set by the WAVEFORM").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("pluck harder: same pitch, more loudness").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("waveform is why you know a voice").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): the hooter worked example ---
        self.next_band(5)
        b5_t = Tex(r"Hooter at 850 Hz, air at 340 m·s$^{-1}$").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"v = f\lambda \;\Rightarrow\; \lambda = \frac{v}{f}").scale(1.1).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"\lambda = \frac{340}{850}").scale(1.1).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"\lambda = 0{,}4\;\text{m}").scale(1.15).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = Tex("higher pitch, shorter wavelength —").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        b5_l5 = Tex("the speed cannot change in the same air").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the echo and the factor of two ---
        self.next_band(6)
        b6_t = Tex("Echoes: there AND back").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"d = \frac{v \times \Delta t}{2}").scale(1.2).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"d = 340 \times 1{,}2 = 408\;\text{m} \;\; \text{(forgot the 2)}").scale(1.0).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_l2))
        self.play(Create(strike(b6_l2)))
        self.wait(2)
        b6_l3 = MathTex(r"d = \frac{340 \times 1{,}2}{2} = \frac{408}{2}").scale(1.05).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"d = 204\;\text{m to the cliff}").scale(1.1).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): sonar and ultrasound ---
        self.next_band(7)
        b7_t = Tex("Sonar off Saldanha Bay").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"d = \frac{1\,500 \times 0{,}4}{2} = \frac{600}{2}").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"d = 300\;\text{m deep}").scale(1.1).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex("Ultrasound: above 20 000 Hz — bats, sonar,").scale(0.95).shift(band_shift(7) + DOWN * 0.9)
        b7_l4 = Tex("prenatal scans; NOT ionising radiation").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = MathTex(r"40\;\text{kHz} = 40 \quad \text{(never!)} ").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.play(Create(strike(b7_l5)))
        b7_l6 = MathTex(r"40\;\text{kHz} = 40\,000\;\text{Hz}").scale(1.0).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the taxi queue ---
        self.next_band(8)
        b8_t = Tex("The slinky and the taxi queue").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("A bump travels up the queue —").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("nobody walks to the front").scale(1.0).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("squash = compression, gap = rarefaction").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("people move ALONG the line the squash runs").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = Tex("squash-to-squash: wavelength; shuffle: amplitude").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): sound is a queue of air ---
        self.next_band(9)
        b9_t = Tex("Why sound is a queue of air").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Vibrating thing squashes the air in front").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("No air to squash: silent — space, bell jar").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Tight queue is fast: solid, liquid, gas").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("Thunder trudges at 340 m a second —").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        b9_l5 = Tex("that is why you count the gap").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): high, loud, and the round trip ---
        self.next_band(10)
        b10_t = Tex("High, loud, and the round trip").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Pitch: how FAST the squashes come").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(1.5)
        b10_l2 = Tex("Loudness: how HARD the air was shoved").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = MathTex(r"\text{cliff: } \frac{340 \times 1{,}2}{2} = 204\;\text{m}").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2)
        b10_l4 = MathTex(r"\text{sea floor: } \frac{1\,500 \times 0{,}4}{2} = 300\;\text{m}").scale(1.0).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("every echo answer is HALVED first").scale(1.05).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5))
        self.wait(4)
