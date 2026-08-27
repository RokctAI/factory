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

# Band-layout whiteboard scene for the session duo "Decay and Nominal vs
# Effective Rates" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier:
# subtopics 5-7). One band per teaching beat, add-only lifecycle, camera
# moves down. Only exporter-supported mobjects; write-only reveals.
# SA number format (R1 234,56). Band dwell times follow subtopics.json
# (230/225/230/230/195/190/200 of 1500 s); Level 6 rescales to real audio.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DecayNominalEffectiveSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the four formulae
        title = Tex("Decay and Nominal vs Effective Rates").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        d1 = MathTex(r"\text{Simple growth: } A = P(1 + in)").scale(1.05).shift(UP * 1.0)
        d2 = MathTex(r"\text{Compound growth: } A = P(1 + i)^n").scale(1.05).shift(UP * 0.2)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"\text{Simple decay (straight line): } A = P(1 - in)").scale(1.05).shift(DOWN * 0.7)
        d4 = MathTex(r"\text{Compound decay (reducing balance): } A = P(1 - i)^n").scale(1.0).shift(DOWN * 1.5)
        self.play(Write(d3))
        self.wait(2)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(VGroup(d3, d4), color=GREEN)))
        self.wait(2)
        d5 = Tex("Same slice of the ORIGINAL, or of the CURRENT value").scale(0.95).shift(DOWN * 2.5)
        self.play(Write(d5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the bakkie, both ways
        self.next_band(1)
        b1_title = Tex(r"Bakkie: R240\,000 at 15\% p.a. over 4 years").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"\text{Straight line: } A = 240\,000(1 - 0{,}15 \times 4)").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"= 240\,000 \times 0{,}4 = \text{R}96\,000").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = MathTex(r"\text{Reducing balance: } A = 240\,000 \times 0{,}85^4").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"= 240\,000 \times 0{,}52200625 = \text{R}125\,281{,}50").scale(0.95).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l3))
        self.wait(2.5)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex("Straight line hits zero; reducing balance never does").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): compounding periods
        self.next_band(2)
        b2_title = Tex(r"R10\,000 at 9\% p.a. compounded monthly, 2 years").scale(1.0).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\text{Convert: } i = \frac{0{,}09}{12} = 0{,}0075, \; n = 24").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"A = 10\,000 \times 1{,}0075^{24} = \text{R}11\,964{,}14").scale(1.0).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = MathTex(r"\text{Annually: } 10\,000 \times 1{,}09^2 = \text{R}11\,881").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("Monthly pays R83 more — interest earns interest sooner").scale(0.95).shift(band_shift(2) + DOWN * 1.8)
        b2_l5 = Tex("Never mix periods: write the conversion line first").scale(0.95).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): nominal to effective
        self.next_band(3)
        b3_title = Tex("Nominal is the headline; effective is the truth").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"1 + i_{\text{eff}} = \left(1 + \frac{i_{\text{nom}}}{m}\right)^m").scale(1.1).shift(band_shift(3) + UP * 1.0)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2.5)
        b3_l2 = MathTex(r"\text{One rand, one year: } 1{,}0075^{12} = 1{,}09381").scale(1.0).shift(band_shift(3) + DOWN * 0.2)
        b3_l3 = MathTex(r"9\% \text{ nominal monthly} = 9{,}38\% \text{ effective}").scale(1.05).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Effective $>$ nominal whenever $m > 1$ — else inverted!").scale(0.95).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the bank duel
        self.next_band(4)
        b4_title = Tex(r"Bank A: 9,4\% yearly vs Bank B: 9,3\% quarterly").scale(1.0).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\text{A effective: } 9{,}4\%").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"\text{B: } (1 + \tfrac{0{,}093}{4})^4 = 1{,}09629").scale(0.95).shift(band_shift(4) + UP * 0.1)
        b4_l3 = MathTex(r"\text{B effective: } 9{,}63\% \;\text{ — B wins}").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex("The lower headline wins — compounding makes up the gap").scale(0.9).shift(band_shift(4) + DOWN * 1.9)
        b4_l5 = Tex("Backwards questions: same line, roots instead of powers").scale(0.9).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): exchange rates
        self.next_band(5)
        b5_title = Tex(r"Exchange rates: R18,50 per dollar").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\$800 \text{ laptop: } 800 \times 18{,}50 = \text{R}14\,800").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"\text{Rand weakens to } 19{,}75: \; 800 \times 19{,}75 = \text{R}15\,800").scale(0.95).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("R1 000 more, same dollar price — imports feed inflation").scale(0.9).shift(band_shift(5) + DOWN * 0.9)
        b5_l4 = Tex("Flip side: exports and tourism become cheaper for foreigners").scale(0.85).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l3))
        self.wait(2.5)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the mixed timeline
        self.next_band(6)
        b6_title = Tex(r"R8\,000 at 10\% p.a. compounded half-yearly, 3 years").scale(0.95).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"\text{Conversion line: } i = 0{,}05 \text{ per half-year}, \; n = 6").scale(0.95).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"A = 8\,000 \times 1{,}05^6 = 8\,000 \times 1{,}34010").scale(1.0).shift(band_shift(6) + UP * 0.1)
        b6_l3 = MathTex(r"A = \text{R}10\,720{,}77").scale(1.1).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex("Rate change mid-way? Split the timeline: segment one's").scale(0.95).shift(band_shift(6) + DOWN * 1.9)
        b6_l5 = Tex("output becomes segment two's P — multiply through").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the photocopy and the ruler
        self.next_band(7)
        b7_title = Tex("The photocopy and the ruler").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"Ruler: R36\,000 of the ORIGINAL gone each year,").scale(0.95).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"4 \times 36\,000 = 144\,000 \Rightarrow \text{R}96\,000 \text{ left}").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"Photocopy at 85\%: each copy keeps 85\% of the LAST —").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = MathTex(r"240\,000 \to 204\,000 \to 173\,400 \to 147\,390 \to 125\,281{,}50").scale(0.85).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l3))
        self.wait(2.5)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)
        b7_l5 = Tex("A photocopy never becomes a blank page").scale(0.85).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): interest paydays
        self.next_band(8)
        b8_title = Tex("Interest paydays").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("One December payday, or twelve small monthly ones?").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Monthly wins: January's interest works from February").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"\text{R}11\,964 \text{ vs } \text{R}11\,881 \text{ — R83 apart}").scale(0.95).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Clock conversion: divide the rate, count the paydays").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        b8_l5 = Tex("Each extra step of frequency helps a little less").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l4))
        self.wait(2.5)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): the headline and the till slip
        self.next_band(9)
        b9_title = Tex("The headline and the till slip").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Sticker: 9\% monthly. Till slip: send one rand through —").scale(0.95).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"1{,}0075^{12} = 1{,}09381 \;\Rightarrow\; 9{,}38\% \text{ really}").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex(r"Stickers cannot be compared; till slips can:").scale(0.95).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = MathTex(r"\text{A: } 9{,}4\% \text{ vs B: } 9{,}63\% \text{ — B wins}").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("Convert every offer to effective before you compare").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(4)
