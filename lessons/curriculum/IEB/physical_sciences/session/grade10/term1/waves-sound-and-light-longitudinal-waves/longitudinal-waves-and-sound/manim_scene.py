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
        title = Tex("Longitudinal Waves and Sound").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("particles vibrate PARALLEL to the travel").scale(1.0).shift(UP * 1.4)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=GREEN)))
        self.wait(2)
        # slinky: dots bunched (compression) and spread (rarefaction)
        base = DOWN * 0.2
        comp = VGroup(*[Dot(base + LEFT * (3.4 - 0.22 * i), color=BLUE) for i in range(6)])
        rare = VGroup(*[Dot(base + LEFT * 0.8 + RIGHT * (0.75 * i), color=BLUE) for i in range(4)])
        comp2 = VGroup(*[Dot(base + RIGHT * (2.6 + 0.22 * i), color=BLUE) for i in range(6)])
        self.play(Create(comp), Create(rare), Create(comp2))
        c_lab = Tex("compression: crowded, high pressure").scale(0.8).shift(DOWN * 1.1 + LEFT * 2.4)
        r_lab = Tex("rarefaction: spread, low pressure").scale(0.8).shift(DOWN * 1.9 + RIGHT * 0.6)
        self.play(Write(c_lab))
        self.play(Write(r_lab))
        self.wait(2)
        b0_l2 = Tex("shove along the slinky, not across it").scale(0.95).shift(DOWN * 2.8)
        self.play(Write(b0_l2))
        self.wait(3)

        # --- Band 1 (subtopic_1): the carried-over quantities ---
        self.next_band(1)
        b1_t = Tex("Same toolkit, new picture").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"\lambda:\ \text{compression to next compression}").scale(0.95).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("amplitude: max displacement from rest").scale(0.95).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"f = \frac{1}{T} \qquad v = f\lambda").scale(1.15).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = Tex("works in solids, liquids and gases —").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        b1_l5 = Tex("everything resists being squeezed").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): sound needs a medium ---
        self.next_band(2)
        b2_t = Tex("Sound: made by a vibrating object").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("push: compression; pull back: rarefaction").scale(0.95).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("a pressure pattern travels — air does not").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("bell in an evacuated jar: silent,").scale(0.95).shift(band_shift(2) + DOWN * 0.6)
        b2_l4 = Tex("hammer still striking").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(VGroup(b2_l3, b2_l4), color=GREEN)))
        self.wait(2)
        b2_l5 = Tex("no particles, no compressions, no sound").scale(0.95).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the medium sets the speed ---
        self.next_band(3)
        b3_t = Tex("The medium owns the speed").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{steel} \approx 5\,000\;\text{m·s}^{-1}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"\text{water} \approx 1\,500\;\text{m·s}^{-1}").scale(1.0).shift(band_shift(3) + UP * 0.3)
        b3_l3 = MathTex(r"\text{air} \approx 340\;\text{m·s}^{-1}").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex("solid before liquid before gas, always").scale(0.95).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = MathTex(r"\text{audible range: } 20\;\text{Hz} - 20\,000\;\text{Hz}").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the three dials ---
        self.next_band(4)
        b4_t = Tex("Three dials of hearing").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("PITCH — set by FREQUENCY").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("LOUDNESS — set by AMPLITUDE").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("QUALITY — set by WAVEFORM").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(VGroup(b4_l1, b4_l2, b4_l3), color=GREEN)))
        self.wait(2)
        b4_l4 = Tex("pluck harder: same pitch, more loudness").scale(0.95).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l4))
        b4_l5 = Tex("waveform is the voice's fingerprint").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): the siren worked example ---
        self.next_band(5)
        b5_t = Tex("Pitch meets spacing").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"f = 680\;\text{Hz}, \quad v = 340\;\text{m·s}^{-1}").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"\lambda = \frac{v}{f}").scale(1.1).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"\lambda = \frac{340}{680} = 0{,}5\;\text{m}").scale(1.1).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = Tex("higher pitch, shorter wavelength —").scale(0.95).shift(band_shift(5) + DOWN * 2.0)
        b5_l5 = Tex("the air's speed will not budge").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the echo and the factor of two ---
        self.next_band(6)
        b6_t = Tex("Echoes: there AND back").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"d = \frac{v \times \Delta t}{2}").scale(1.15).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2)
        b6_l2 = MathTex(r"d = \frac{340 \times 0{,}9}{2} = \frac{306}{2}").scale(1.05).shift(band_shift(6) + DOWN * 0.1)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"d = 153\;\text{m}").scale(1.1).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex("forget the 2 and every answer doubles").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): sonar and ultrasound ---
        self.next_band(7)
        b7_t = Tex("Sonar and ultrasound").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"d = \frac{1\,500 \times 0{,}6}{2} = \frac{900}{2} = 450\;\text{m}").scale(1.0).shift(band_shift(7) + UP * 1.0)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(2)
        b7_l2 = Tex("ultrasound: above 20 000 Hz —").scale(0.95).shift(band_shift(7) + UP * 0.0)
        b7_l3 = Tex("bats, dolphins, ships, hospitals").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("not ionising — safe for the unborn baby").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l4))
        b7_l5 = MathTex(r"60\;\text{kHz} = 60\,000\;\text{Hz, never } 60").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the taxi queue ---
        self.next_band(8)
        b8_t = Tex("The slinky and the taxi queue").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("a squash travels the queue —").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("nobody walks to the front").scale(1.0).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2)
        b8_l3 = Tex("squash = compression; gap = rarefaction").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("people rock along the SAME line").scale(0.95).shift(band_shift(8) + DOWN * 1.5)
        b8_l5 = Tex("the squash travels: longitudinal").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): sound is a queue of air ---
        self.next_band(9)
        b9_t = Tex("Sound is a queue of air").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("vibrator pushes: squash; pulls: gap").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("a squash lands on your eardrum: sound").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("tight queue fast, loose queue slow:").scale(0.95).shift(band_shift(9) + DOWN * 0.6)
        b9_l4 = MathTex(r"5\,000 \to 1\,500 \to 340\;\text{m·s}^{-1}").scale(1.0).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("flash instant, thunder at 340 — count the gap").scale(0.9).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): high, loud, and the round trip ---
        self.next_band(10)
        b10_t = Tex("High, loud, and the round trip").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("pitch: how OFTEN — loudness: how HARD").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.play(Create(SurroundingRectangle(b10_l1, color=GREEN)))
        self.wait(2)
        b10_l2 = MathTex(r"340 \times 0{,}9 = 306\;\text{m round trip}").scale(1.0).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = MathTex(r"\text{wall at } \frac{306}{2} = 153\;\text{m}").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2)
        b10_l4 = Tex("lagoon: 900 m journey, floor at 450 m").scale(0.95).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l4))
        b10_l5 = Tex("halve before you write, every time").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l5))
        self.wait(4)
