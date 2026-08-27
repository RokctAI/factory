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

# Band-layout whiteboard scene for "Sound in Practice: Echoes, Sonar and
# Ultrasound" (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe mobjects only; write-only reveals; camera moves down band by
# band. Band time apportioned to subtopics.json
# (230/235/235/240/175/180/185 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SoundInPracticeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): who owns each symbol ---
        title = Tex("Echoes, Sonar and Ultrasound").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"v = f\lambda").scale(1.3).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=GREEN)))
        self.wait(2)
        b0_l2 = Tex("v: owned by the MEDIUM").scale(0.95).shift(UP * 0.2)
        b0_l3 = Tex("f: owned by the SOURCE").scale(0.95).shift(DOWN * 0.5)
        b0_l4 = MathTex(r"\lambda = \frac{v}{f}\ \text{— the outcome}").scale(0.95).shift(DOWN * 1.3)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = MathTex(r"\lambda = \frac{340}{250} = 1{,}36\;\text{m}").scale(1.0).shift(DOWN * 2.4)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): crossing into water ---
        self.next_band(1)
        b1_t = Tex("Crossing from air into water").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("frequency CANNOT change: 250 in, 250 on").scale(0.95).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)
        b1_l2 = MathTex(r"\text{air: } \lambda = \frac{340}{250} = 1{,}36\;\text{m}").scale(1.0).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"\text{water: } \lambda = \frac{1\,500}{250} = 6\;\text{m}").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = Tex("frequency stays; speed and wavelength").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        b1_l5 = Tex("change together").scale(0.95).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): sonar drawn + depth calculation ---
        self.next_band(2)
        b2_t = Tex("Sonar: time the sea's reply").scale(1.15).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_t))
        self.wait(1.5)
        boat = Rectangle(width=1.6, height=0.5).shift(band_shift(2) + UP * 1.4)
        sea = Line(band_shift(2) + LEFT * 4.2 + UP * 1.15, band_shift(2) + RIGHT * 4.2 + UP * 1.15)
        floor = Line(band_shift(2) + LEFT * 4.2 + DOWN * 1.6, band_shift(2) + RIGHT * 4.2 + DOWN * 1.6)
        down_ar = Arrow(band_shift(2) + LEFT * 0.4 + UP * 1.0, band_shift(2) + LEFT * 0.4 + DOWN * 1.5, buff=0, color=YELLOW)
        up_ar = Arrow(band_shift(2) + RIGHT * 0.4 + DOWN * 1.5, band_shift(2) + RIGHT * 0.4 + UP * 1.0, buff=0, color=BLUE)
        self.play(Create(boat), Create(sea), Create(floor))
        self.play(Create(down_ar), Create(up_ar))
        self.wait(2)
        b2_l1 = MathTex(r"d = \frac{v \times \Delta t}{2} = \frac{1\,500 \times 1{,}2}{2}").scale(1.0).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l1))
        b2_l2 = MathTex(r"= \frac{1\,800}{2} = 900\;\text{m}").scale(1.0).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): wavelength of the pulse — different logic ---
        self.next_band(3)
        b3_t = Tex("Same pulse, other tool").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"25\;\text{kHz} = 25\,000\;\text{Hz}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"\lambda = \frac{1\,500}{25\,000} = 0{,}06\;\text{m}").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = Tex("no factor of two in a wavelength").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("timing line and wave-equation line:").scale(0.95).shift(band_shift(3) + DOWN * 1.8)
        b3_l5 = Tex("label each — never blend the logics").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the bat ---
        self.next_band(4)
        b4_t = Tex("The bat: nature's sonar in air").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"\lambda = \frac{340}{85\,000} = 0{,}004\;\text{m}").scale(1.05).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(2)
        b4_l2 = Tex("four millimetres: moth-sized waves").scale(0.95).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"\text{round trip: } 2 \times 2{,}55 = 5{,}1\;\text{m}").scale(0.95).shift(band_shift(4) + DOWN * 1.0)
        b4_l4 = MathTex(r"t = \frac{5{,}1}{340} = 0{,}015\;\text{s}").scale(0.95).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex("echolocation: flying by ear").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): the dolphin ---
        self.next_band(5)
        b5_t = Tex("The dolphin: same programme, wet").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"\lambda = \frac{1\,500}{50\,000} = 0{,}03\;\text{m}").scale(1.05).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2)
        b5_l2 = Tex("three centimetres: one fish at a time").scale(0.95).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("bonus of the medium: answers return").scale(0.95).shift(band_shift(5) + DOWN * 1.0)
        b5_l4 = Tex("over four times sooner than in air").scale(0.95).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("ship, bat, dolphin: one physics").scale(0.95).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the ear's limits + the scanner ---
        self.next_band(6)
        b6_t = Tex("The ear stops; the scanner continues").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{hearing: } 20\;\text{Hz} - 20\,000\;\text{Hz}").scale(0.95).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("most sensitive mid-range; the top erodes first").scale(0.9).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("scanner: pulses in, echoes timed,").scale(0.95).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = Tex("depths stacked into a picture").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = MathTex(r"t = \frac{2 \times 0{,}045}{1\,500} = 0{,}000\,06\;\text{s}").scale(0.95).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): why sound and not X-rays ---
        self.next_band(7)
        b7_t = Tex("Why sound and not X-rays").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("ultrasound: mechanical pressure wave").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("X-rays: ionising — strip electrons,").scale(0.95).shift(band_shift(7) + UP * 0.2)
        b7_l3 = Tex("damage cells").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.play(Create(strike(b7_l3)))
        self.wait(2)
        b7_l4 = Tex("so the baby is scanned safely, repeatedly").scale(0.95).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("also: kidney stones, cleaning, crack-hunting").scale(0.9).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): counting the storm ---
        self.next_band(8)
        b8_t = Tex("Counting the storm").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("flash instant; thunder slogs at 340").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"340 \times 5 = 1\,700\;\text{m}").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2)
        b8_l3 = Tex("one-way trip: halve NOTHING").scale(0.95).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("the deciding question: did the sound").scale(0.95).shift(band_shift(8) + DOWN * 1.7)
        b8_l5 = Tex("come back to where it started?").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): shopping with 4 mm waves ---
        self.next_band(9)
        b9_t = Tex("Shopping with four-millimetre waves").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("waves bounce off things their own size or bigger").scale(0.9).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("swell slides past the pole; ripples scatter").scale(0.9).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"85\,000\ \text{per s} \to 4\;\text{mm waves}").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("smaller target, shorter wave, higher pitch").scale(0.95).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        b9_l5 = Tex("return in 0,015 s: moth at 2,55 m").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): seeing with echoes ---
        self.next_band(10)
        b10_t = Tex("Seeing with echoes").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("a torch made of sound, shone through skin").scale(0.95).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex("every tissue boundary splashes an echo back").scale(0.9).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = MathTex(r"0{,}000\,06\;\text{s} \to 4{,}5\;\text{cm deep}").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2)
        b10_l4 = Tex("gentle pushes, no cell damage —").scale(0.95).shift(band_shift(10) + DOWN * 1.6)
        b10_l5 = Tex("safe for the baby, repeat at will").scale(0.95).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
