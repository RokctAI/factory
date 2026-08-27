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
        d5 = Tex("Fixed slice of the ORIGINAL, or shrinking slice of the CURRENT").scale(0.9).shift(DOWN * 2.5)
        self.play(Write(d5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the minibus, both ways
        self.next_band(1)
        b1_title = Tex(r"Minibus: R360\,000 at 12\% p.a. over 5 years").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"\text{Straight line: } A = 360\,000(1 - 0{,}12 \times 5)").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"= 360\,000 \times 0{,}4 = \text{R}144\,000").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = MathTex(r"\text{Reducing balance: } A = 360\,000 \times 0{,}88^5").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"= 360\,000 \times 0{,}52773 = \text{R}189\,983{,}49").scale(0.95).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l3))
        self.wait(2.5)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex("Straight line hits zero at 8⅓ years; reducing balance never does").scale(0.85).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): compounding periods
        self.next_band(2)
        b2_title = Tex(r"R15\,000 at 8\% p.a. compounded quarterly, 3 years").scale(1.0).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\text{Convert: } i = \frac{0{,}08}{4} = 0{,}02, \; n = 12").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"A = 15\,000 \times 1{,}02^{12} = \text{R}19\,023{,}63").scale(1.0).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = MathTex(r"\text{Annually: } 15\,000 \times 1{,}08^3 = \text{R}18\,895{,}68").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("Quarterly pays R128 more — interest earns interest sooner").scale(0.95).shift(band_shift(2) + DOWN * 1.8)
        b2_l5 = Tex("Never mix clocks: write the conversion line first").scale(0.95).shift(band_shift(2) + DOWN * 2.7)
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
        b3_l2 = MathTex(r"\text{One rand, one year: } 1{,}02^{4} = 1{,}08243").scale(1.0).shift(band_shift(3) + DOWN * 0.2)
        b3_l3 = MathTex(r"8\% \text{ nominal quarterly} = 8{,}24\% \text{ effective}").scale(1.05).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Effective $>$ nominal whenever $m > 1$ — else inverted!").scale(0.95).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the bank contest
        self.next_band(4)
        b4_title = Tex(r"Bank X: 8,3\% yearly vs Bank Y: 8,1\% monthly").scale(1.0).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\text{X effective: } 8{,}3\%").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"\text{Y: } (1 + \tfrac{0{,}081}{12})^{12} = 1{,}08408").scale(0.95).shift(band_shift(4) + UP * 0.1)
        b4_l3 = MathTex(r"\text{Y effective: } 8{,}41\% \;\text{ — Y wins}").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex("The smaller headline wins — frequency closes the gap").scale(0.9).shift(band_shift(4) + DOWN * 1.9)
        b4_l5 = Tex("Backwards questions: same law, roots instead of powers").scale(0.9).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): exchange rates
        self.next_band(5)
        b5_title = Tex(r"Exchange rates: R17,60 per dollar").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\$650 \text{ camera: } 650 \times 17{,}60 = \text{R}11\,440").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"\text{Rand weakens to } 18{,}40: \; 650 \times 18{,}40 = \text{R}11\,960").scale(0.95).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("R520 more, same dollar price — imports feed inflation").scale(0.9).shift(band_shift(5) + DOWN * 0.9)
        b5_l4 = Tex("Flip side: exports and tourism become cheaper for foreigners").scale(0.85).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l3))
        self.wait(2.5)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the chained timeline
        self.next_band(6)
        b6_title = Tex(r"R9\,000 at 7\% p.a. compounded quarterly, 4 years").scale(0.95).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"\text{Conversion line: } i = 0{,}0175 \text{ per quarter}, \; n = 16").scale(0.95).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"A = 9\,000 \times 1{,}0175^{16} = 9\,000 \times 1{,}31993").scale(1.0).shift(band_shift(6) + UP * 0.1)
        b6_l3 = MathTex(r"A = \text{R}11\,879{,}36").scale(1.1).shift(band_shift(6) + DOWN * 0.9)
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
        b7_l1 = Tex(r"Ruler: R43\,200 of the ORIGINAL gone each year,").scale(0.95).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"5 \times 43\,200 = 216\,000 \Rightarrow \text{R}144\,000 \text{ left}").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"Photocopy at 88\%: each copy keeps 88\% of the LAST —").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = MathTex(r"360\,000 \to 316\,800 \to 278\,784 \to 245\,329{,}92 \to \ldots \to 189\,983{,}49").scale(0.75).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l3))
        self.wait(2.5)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)
        b7_l5 = Tex("A photocopy never comes out blank").scale(0.85).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): interest paydays
        self.next_band(8)
        b8_title = Tex("Interest paydays").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("One December payday, or four small quarterly ones?").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Quarterly wins: March's interest earns from April").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"\text{R}19\,024 \text{ vs } \text{R}18\,896 \text{ — R128 apart}").scale(0.95).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Clock conversion: slice the rate, count the paydays").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        b8_l5 = Tex("Each extra slicing helps a little less").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l4))
        self.wait(2.5)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): the headline and the till slip
        self.next_band(9)
        b9_title = Tex("The headline and the till slip").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Headline: 8,1\% monthly. Till slip: push one rand through —").scale(0.9).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"1{,}00675^{12} = 1{,}08408 \;\Rightarrow\; 8{,}41\% \text{ really}").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex(r"Headlines cannot be compared; till slips can:").scale(0.95).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = MathTex(r"\text{X: } 8{,}3\% \text{ vs Y: } 8{,}41\% \text{ — Y wins}").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("Convert every offer to effective before you choose").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(4)
