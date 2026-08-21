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

# Band-layout whiteboard scene: sequential vertical bands, one per teaching
# beat, camera moves down between bands, add-only lifecycle. Exporter-safe
# mobjects only (Tex/MathTex/Line/Rectangle); every working line is a
# single-string MathTex revealed with Write. Covers all seven subtopics of
# the duo (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7); band time
# apportioned to subtopics.json (225/230/245/240/195/195/200 of 1530 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GrowthAndDecaySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the four formulae
        title = Tex("The four formulae on one timeline").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = MathTex(r"\text{simple growth: } A = P(1 + in)").scale(1.0).shift(UP * 1.0)
        s0_l2 = MathTex(r"\text{compound growth: } A = P(1 + i)^n").scale(1.0).shift(UP * 0.2)
        s0_l3 = MathTex(r"\text{simple decay: } A = P(1 - in)").scale(1.0).shift(DOWN * 0.6)
        s0_l4 = MathTex(r"\text{reducing balance: } A = P(1 - i)^n").scale(1.0).shift(DOWN * 1.4)
        self.play(Write(s0_l1))
        self.play(Write(s0_l2))
        self.play(Write(s0_l3))
        self.play(Write(s0_l4))
        self.wait(2.5)
        s0_l5 = Tex(r"Simple adds; compound multiplies by $1+i$").scale(1.0).shift(DOWN * 2.4)
        self.play(Write(s0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): worked drill + matching i and n
        self.next_band(1)
        b1_title = Tex(r"R20\,000 at 7\% p.a. annually, 6 years").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"A = 20\,000 \times 1{,}07^{6}").scale(1.1).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"1{,}07^{6} = 1{,}500730 \Rightarrow A = \text{R}30\,014{,}61").scale(1.05).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex(r"Match $i$ and $n$: 6\% p.a. monthly $\Rightarrow i = 0{,}005$, months").scale(0.9).shift(band_shift(1) + DOWN * 1.1)
        b1_l4 = Tex(r"Keep every decimal until the final rounding").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): solving for the rate — the van
        self.next_band(2)
        b2_title = Tex(r"Van: R320\,000 $\to$ R135\,000 in 3 years").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"135\,000 = 320\,000(1 - i)^3").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"(1 - i)^3 = 0{,}421875").scale(1.05).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"1 - i = \sqrt[3]{0{,}421875} = 0{,}75").scale(1.05).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"i = 0{,}25 \;\Rightarrow\; 25\% \text{ per annum}").scale(1.1).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the growth twin + disciplines
        self.next_band(3)
        b3_title = Tex("The growth twin").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"8\,000 \to 10\,941{,}05 \text{ in 3 years}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"(1 + i)^3 = 1{,}367631 \Rightarrow 1 + i = 1{,}11").scale(1.0).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex(r"Divide BEFORE rooting: root acts on $A/P$").scale(1.0).shift(band_shift(3) + DOWN * 1.0)
        b3_l4 = Tex(r"Decay factor below one; growth factor above").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): solving for time — enter the logarithm
        self.next_band(4)
        b4_title = Tex("Solving for time — enter the logarithm").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"8\,000 = 4\,000 \times 1{,}075^{n} \Rightarrow 1{,}075^{n} = 2").scale(1.0).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"n = \log_{1{,}075} 2 = \frac{\log 2}{\log 1{,}075}").scale(1.05).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=YELLOW)))
        self.wait(2.5)
        b4_l3 = MathTex(r"n = \frac{0{,}30103}{0{,}031408} = 9{,}58 \text{ years}").scale(1.05).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): interpret against the crediting schedule
        self.next_band(5)
        b5_title = Tex("Round to the crediting schedule").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"1{,}075^{9} \approx 1{,}9172 \; \text{ — not yet doubled}").scale(1.0).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"1{,}075^{10} \approx 2{,}0610 \; \text{ — past double}").scale(1.0).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex(r"Answer: at the END of year 10").scale(1.05).shift(band_shift(5) + DOWN * 1.0)
        b5_l4 = MathTex(r"\text{Inflation at 5\%: } \frac{\log 2}{\log 1{,}05} \approx 14{,}2 \text{ years}").scale(0.95).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): changing conditions — walk the timeline
        self.next_band(6)
        b6_title = Tex("Changing conditions: walk the timeline").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"12\,000 \times 1{,}07^{3} = 14\,700{,}52 \; \xrightarrow{+6\,000} \; 20\,700{,}52").scale(0.9).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"\times\, 1{,}07 = 22\,149{,}55 \text{ at year 4}").scale(0.95).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"\times\, 1{,}08^{2} = 25\,835{,}24 \text{ at year 6}").scale(1.0).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the rules that make timelines safe
        self.next_band(7)
        b7_title = Tex("Timeline rules").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Every amount travels through every period it is present").scale(0.95).shift(band_shift(7) + UP * 1.0)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex(r"Rate changes cut regimes; value carries across the cut").scale(0.95).shift(band_shift(7) + UP * 0.0)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"Withdrawals subtract at their date and stop growing").scale(0.95).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex(r"Draw the line first — bookkeeping, not acrobatics").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): escalator up, escalator down
        self.next_band(8)
        b8_title = Tex("Escalator up, escalator down").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\text{stairs: } +1\,400 \text{ each year on } 20\,000").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"\text{escalator: } \times 1{,}07 \text{ each year} \Rightarrow 30\,014{,}61").scale(1.0).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = MathTex(r"\text{decay escalator: } \times 0{,}88 \text{ — never reaches zero}").scale(0.95).shift(band_shift(8) + DOWN * 1.0)
        b8_l4 = Tex(r"Up or down? Stairs or escalator? Formula chosen.").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): the car lot detective
        self.next_band(9)
        b9_title = Tex("The car lot detective").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_wrong = MathTex(r"\text{shed } 57{,}8\% \div 3 \approx 19\% \text{ a year?}").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_wrong))
        self.play(Create(strike(b9_wrong)))
        self.wait(2)
        b9_l1 = MathTex(r"\frac{135\,000}{320\,000} = 0{,}421875 \text{ kept over 3 years}").scale(0.95).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\sqrt[3]{0{,}421875} = 0{,}75 \Rightarrow \text{shed } 25\% \text{ p.a.}").scale(1.0).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2)
        b9_l3 = Tex(r"Divide end by start, root by the years").scale(1.0).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l3))
        self.wait(3)

        # --- Band 10 (subtopic_7): how long until it doubles
        self.next_band(10)
        b10_title = Tex("How long until it doubles").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"1{,}075^{n} = 2 \Rightarrow n = \frac{\log 2}{\log 1{,}075} \approx 9{,}58").scale(1.0).shift(band_shift(10) + UP * 1.0)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex(r"Banks pay at year ends: crossed at END of year 10").scale(0.95).shift(band_shift(10) + UP * 0.0)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = MathTex(r"\text{Prices at 5\%: double in} \approx 14{,}2 \text{ years}").scale(0.95).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"Unknown exponent calls the logarithm").scale(1.05).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=YELLOW)))
        self.wait(4)
