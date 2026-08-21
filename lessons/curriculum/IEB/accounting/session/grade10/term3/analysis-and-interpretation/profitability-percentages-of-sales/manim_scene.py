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

# Band-layout whiteboard scene for the IEB Grade 10 Accounting session duo
# "Profitability Percentages of Sales". Add-only lifecycle, one band per
# teaching beat, camera moves down between bands. Covers all seven subtopics:
# Part 1 Expert (subtopics 1-4), Part 2 Simplifier (subtopics 5-7) in fresh
# bands. subtopics.json durations 210/220/220/220/180/190/190 of 1430 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ProfitabilityPercentagesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): why percentages, the sales base, the figures
        title = Tex("Profitability Percentages of Sales").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Absolute figures carry no verdict —").scale(1.05).shift(UP * 1.2)
        b0_l2 = Tex("a figure gains meaning against a BASE: sales").scale(1.05).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Sales R60 000; gross profit R20 000").scale(1.0).shift(DOWN * 0.6)
        b0_l4 = Tex("Expenses R15 200; operating R12 000; net R10 500").scale(1.0).shift(DOWN * 1.4)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex("Out of every R100 of sales, how much ended as this?").scale(0.95).shift(DOWN * 2.4)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): formula summary discipline, the wrong-figure trap
        self.next_band(1)
        b1_title = Tex("Your formula summary gives every formula").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = Tex("Tested skills: selection, substitution,").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("interpretation — not memory").scale(1.05).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_wrong = MathTex(r"\text{Net profit \% using } 12\,000 \text{ (operating!)}").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2.5)
        b1_l3 = Tex("Label what you substitute, every time").scale(1.05).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the two gross profit percentages, in full
        self.next_band(2)
        b2_title = Tex("The two gross profit percentages").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\text{On sales: } \frac{20\,000}{60\,000} \times 100 = 33{,}3\%").scale(1.05).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = Tex("The margin the business lives on").scale(1.0).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"\text{On cost: } \frac{20\,000}{40\,000} \times 100 = 50\%").scale(1.05).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("This IS the mark-up — policy confirmed at 50\\%").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        b2_l5 = Tex("Same profit, seen from the two ends of the counter").scale(0.95).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): a gap against the policy is a finding
        self.next_band(3)
        b3_title = Tex("Policy 50\\% — achieved 44\\%: a FINDING").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = Tex("Causes are a short, learnable list:").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("goods sold below full price (markdowns)").scale(1.0).shift(band_shift(3) + UP * 0.3)
        b3_l3 = Tex("stock lost, broken or stolen after costing").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = Tex("recording errors; theft of takings").scale(1.0).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("The percentage raises the alarm and sizes the leak").scale(0.95).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the operating family and net profit on sales
        self.next_band(4)
        b4_title = Tex("The operating family").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\text{Expenses: } \frac{15\,200}{60\,000} \times 100 = 25{,}3\%").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"\text{Operating: } \frac{12\,000}{60\,000} \times 100 = 20\%").scale(1.0).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{Net: } \frac{10\,500}{60\,000} \times 100 = 17{,}5\%").scale(1.0).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex("20 down to 17,5 — the financing bite, isolated").scale(1.0).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): the five-gauge dashboard panel
        self.next_band(5)
        b5_title = Tex("One dashboard, five gauges").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        panel = Rectangle(width=10.5, height=4.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Create(panel))
        b5_r1 = Tex("Mark-up achieved 50\\% \\quad Margin 33,3\\%").scale(1.0).shift(band_shift(5) + UP * 0.6)
        self.play(Write(b5_r1))
        self.wait(2)
        div = Line(LEFT * 5.25, RIGHT * 5.25).shift(band_shift(5) + UP * 0.0)
        self.play(Create(div))
        b5_r2 = Tex("Expenses 25,3\\% \\quad Operations keep 20\\%").scale(1.0).shift(band_shift(5) + DOWN * 0.7)
        b5_r3 = Tex("Owner keeps 17,5\\%").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_r2))
        self.wait(2)
        self.play(Write(b5_r3))
        self.wait(2)
        b5_l1 = Tex("Proportions travel — rand totals are trapped").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l1))
        self.wait(3)

        # --- Band 6 (subtopic_4): the three comparison bases
        self.next_band(6)
        b6_title = Tex("A percentage needs a comparison").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Against LAST YEAR — the trend").scale(1.05).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("Against the POLICY — the control check").scale(1.05).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Against a SIMILAR BUSINESS — competition").scale(1.05).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("The question signals the base by what it supplies").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): the four-move comment anatomy
        self.next_band(7)
        b7_title = Tex("Comment anatomy — four moves").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_wrong = Tex("Only saying: it went down — quarter marks").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(2.5)
        b7_l1 = Tex("STATE: margin fell from 36\\% to 33,3\\%").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("JUDGE: a deterioration").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("EXPLAIN: clearance sale, or losses before sale").scale(1.0).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("RECOMMEND: count stock; review discount depth").scale(1.0).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): following one hundred-rand note
        self.next_band(8)
        b8_title = Tex("Out of every hundred rand").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("R100 crosses the counter").scale(1.05).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("R66,70 goes back to replacing the goods").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("R33,30 margin stays to work with").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("About R25,30 runs the shop; interest nibbles").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("R17,50 remains — the owner's keep").scale(1.05).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the clinic visit — vitals read as a set
        self.next_band(9)
        b9_title = Tex("The health check at the clinic").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Temperature 37 — fine or fever? Compare!").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Margin 33,3\\% vs last year's 36\\%: slipped").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Never read one vital alone — read the SET:").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("margin fine, keep thin: check running costs").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        b9_l5 = Tex("margin down, expenses steady: leak upstream").scale(1.0).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the four-line recipe and gauge matching
        self.next_band(10)
        b10_title = Tex("Saying something that means something").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("WHAT: margin fell, 36 to 33,3 per hundred").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex("SO: nearly three rand less per hundred to work with").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("WHY (from the scenario): the clearance sale").scale(1.0).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("NOW WHAT: count stock; review discount depth").scale(1.0).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2.5)
        b10_l5 = Tex("Match the gauge to the question — always").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l5))
        self.wait(4)
