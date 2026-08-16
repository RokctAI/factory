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
        title = Tex("Echoes, Sonar and Ultrasound").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"v = f\lambda").scale(1.3).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex(r"$v$ belongs to the MEDIUM: air 340 m·s$^{-1}$").scale(1.0).shift(UP * 0.0)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex(r"$f$ belongs to the SOURCE").scale(1.0).shift(DOWN * 0.9)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = MathTex(r"\lambda = \frac{v}{f} = \frac{340}{500} = 0{,}68\;\text{m}").scale(1.05).shift(DOWN * 2.0)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): crossing into water ---
        self.next_band(1)
        b1_t = Tex("500 Hz sound crosses from air to water").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("frequency CANNOT change: 500 in, 500 on").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"v: 340 \to 1\,500\;\text{m·s}^{-1}").scale(1.05).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"\lambda = \frac{1\,500}{500} = 3\;\text{m}").scale(1.1).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = Tex(r"new medium: $f$ stays, $v$ and $\lambda$ change").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = MathTex(r"68\;\text{kHz} = 68\,000\;\text{Hz first}").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): sonar drawn + depth calculation ---
        self.next_band(2)
        b2_t = Tex("Sonar off Durban: echo after 1,6 s").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        # ship, pulse down, seabed
        ship = Rectangle(width=1.8, height=0.5).shift(band_shift(2) + UP * 1.2 + LEFT * 2.5)
        ship_lab = Tex("ship").scale(0.8).shift(band_shift(2) + UP * 1.2 + LEFT * 2.5)
        self.play(Create(ship), Write(ship_lab))
        seabed = Line(band_shift(2) + DOWN * 1.6 + LEFT * 4.5, band_shift(2) + DOWN * 1.6 + LEFT * 0.2)
        self.play(Create(seabed))
        down_p = Arrow(band_shift(2) + UP * 0.9 + LEFT * 2.9, band_shift(2) + DOWN * 1.5 + LEFT * 2.9,
                       buff=0, color=YELLOW)
        up_p = Arrow(band_shift(2) + DOWN * 1.5 + LEFT * 2.1, band_shift(2) + UP * 0.9 + LEFT * 2.1,
                     buff=0, color=BLUE)
        self.play(Create(down_p))
        self.play(Create(up_p))
        self.wait(2)
        b2_l1 = MathTex(r"d = \frac{v \times \Delta t}{2}").scale(1.1).shift(band_shift(2) + UP * 1.0 + RIGHT * 2.6)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"d = \frac{1\,500 \times 1{,}6}{2} = \frac{2\,400}{2}").scale(1.0).shift(band_shift(2) + DOWN * 0.2 + RIGHT * 2.6)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"d = 1\,200\;\text{m}").scale(1.1).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): wavelength of the pulse — different logic ---
        self.next_band(3)
        b3_t = Tex("Same pulse, second question: wavelength").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"30\;\text{kHz} = 30\,000\;\text{Hz}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"\lambda = \frac{v}{f} = \frac{1\,500}{30\,000}").scale(1.05).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"\lambda = 0{,}05\;\text{m}").scale(1.1).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex("timing logic halves; wave equation never does").scale(1.0).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("short wavelengths see small things").scale(1.0).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the bat ---
        self.next_band(4)
        b4_t = Tex("A bat calling at 68 kHz").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"\lambda = \frac{340}{68\,000} = 0{,}005\;\text{m}").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(2)
        b4_l2 = Tex("five millimetres: moth-sized waves").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex(r"Moth 1,7 m away: round trip $2 \times 1{,}7 = 3{,}4$ m").scale(1.0).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"t = \frac{3{,}4}{340} = 0{,}01\;\text{s}").scale(1.05).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex("echolocation: steering by ears in the dark").scale(1.0).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): the dolphin ---
        self.next_band(5)
        b5_t = Tex("A dolphin clicking at 75 kHz").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"\lambda = \frac{1\,500}{75\,000} = 0{,}02\;\text{m}").scale(1.05).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2)
        b5_l2 = Tex("two centimetres — picks out a single fish").scale(1.0).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex(r"water at 1 500 m·s$^{-1}$: answers return").scale(1.0).shift(band_shift(5) + DOWN * 1.0)
        b5_l4 = Tex(r"over $4\times$ sooner than a bat's").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("ship, bat, dolphin: same three moves").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the ear's limits + the scanner ---
        self.next_band(6)
        b6_t = Tex("The ear's limits, the scanner's trick").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("Hearing: about 20 Hz to 20 000 Hz").scale(1.0).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("most sensitive in the middle — speech").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Scanner: echoes off every tissue boundary").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"t = \frac{2 \times 0{,}06}{1\,500} = 0{,}000\,08\;\text{s}").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex("eighty millionths of a second, routinely").scale(1.0).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): why sound and not X-rays ---
        self.next_band(7)
        b7_t = Tex("Why sound, not X-rays, for a baby").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("Ultrasound: mechanical pressure wave").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("NOT ionising — no cell damage, repeatable").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex("X-rays strip electrons and damage cells").scale(1.0).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("also: kidney stones, cleaning, crack-finding").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): counting the storm ---
        self.next_band(8)
        b8_t = Tex("Counting the storm").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("flash now, bang later: sound trudges").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"340 \times 3 = 1\,020\;\text{m — about 1 km}").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2)
        b8_l3 = Tex("ONE-WAY trip: no halving here").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("halving belongs to echoes — round trips").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("ask first: did the sound come back?").scale(1.0).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): shopping with 5 mm waves ---
        self.next_band(9)
        b9_t = Tex("Shopping with five-millimetre waves").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("waves only bounce off things their own size").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("swells slide past the jetty pole;").scale(1.0).shift(band_shift(9) + UP * 0.3)
        b9_l3 = Tex("tiny ripples scatter off it").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("5 mm waves make a moth a wall").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("smaller target: shorter wave, higher $f$").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): seeing with echoes ---
        self.next_band(10)
        b10_t = Tex("Seeing with echoes").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("a torch made of sound, shone through skin").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex("every tissue boundary splashes an echo back").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("timed, halved: six centimetres deep").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("only pushes and squashes — safe for a baby").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("bonus: shattering kidney stones, no cut").scale(1.0).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l5))
        self.wait(4)
