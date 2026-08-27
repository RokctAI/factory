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

# Band-layout whiteboard scene for the IEB Grade 12 Geography session duo
# "Economic Sectors and Their Contribution". Bands cover all seven subtopics
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7) with
# dwell time proportional to subtopics.json (235/235/220/230/220/220/220 of
# 1580 s). The wool chain and the GDP-share bar chart are hand-built from
# exporter-safe primitives only (Tex/MathTex/Line/Arrow/Dot/Rectangle/
# VGroup); add-only lifecycle, the camera moves down between bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EconomicSectorsContributionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # --- Band 0 (subtopic_1): the four sectors defined ---
        title = Tex("Economic Sectors and Their Contribution").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Primary: EXTRACT --- wool, fish, timber, ore").scale(1.0).shift(UP * 0.9)
        b0_l2 = Tex(r"Secondary: TRANSFORM --- mills, steelworks, builders").scale(0.95).shift(UP * 0.1)
        b0_l3 = Tex(r"Tertiary: SERVE --- retail, transport, banking").scale(1.0).shift(DOWN * 0.7)
        b0_l4 = Tex(r"Quaternary: KNOW --- research, software, data").scale(1.0).shift(DOWN * 1.5)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(1.9)
        b0_l5 = Tex(r"Keyword of secondary: transformation").scale(1.0).shift(DOWN * 2.5)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the wool chain, drawn link by link ---
        self.next_band(1)
        b1_t = Tex("One fleece, four sectors").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        sc1 = band_shift(1)
        c1 = Tex(r"farm\\shears").scale(0.9).shift(sc1 + UP * 0.8 + LEFT * 4.6)
        c2 = Tex(r"mill\\weaves").scale(0.9).shift(sc1 + UP * 0.8 + LEFT * 1.6)
        c3 = Tex(r"shop, courier\\sell, deliver").scale(0.9).shift(sc1 + UP * 0.8 + RIGHT * 1.6)
        c4 = Tex(r"lab\\breeds finer").scale(0.9).shift(sc1 + UP * 0.8 + RIGHT * 4.6)
        tags = [
            Tex("primary").scale(0.85).shift(sc1 + DOWN * 0.2 + LEFT * 4.6),
            Tex("secondary").scale(0.85).shift(sc1 + DOWN * 0.2 + LEFT * 1.6),
            Tex("tertiary").scale(0.85).shift(sc1 + DOWN * 0.2 + RIGHT * 1.6),
            Tex("quaternary").scale(0.85).shift(sc1 + DOWN * 0.2 + RIGHT * 4.6),
        ]
        self.play(Write(c1), Write(tags[0])); self.wait(1.6)
        self.play(Create(Arrow(sc1 + UP * 0.8 + LEFT * 3.7, sc1 + UP * 0.8 + LEFT * 2.5, color=GREEN, buff=0.1)))
        self.play(Write(c2), Write(tags[1])); self.wait(1.6)
        self.play(Create(Arrow(sc1 + UP * 0.8 + LEFT * 0.7, sc1 + UP * 0.8 + RIGHT * 0.5, color=GREEN, buff=0.1)))
        self.play(Write(c3), Write(tags[2])); self.wait(1.6)
        self.play(Create(Arrow(sc1 + UP * 0.8 + RIGHT * 2.7, sc1 + UP * 0.8 + RIGHT * 3.6, color=GREEN, buff=0.1)))
        self.play(Write(c4), Write(tags[3])); self.wait(1.6)
        b1_l1 = Tex(r"Every worker belongs to exactly one link").scale(1.05).shift(sc1 + DOWN * 1.4)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): GDP versus GNP ---
        self.next_band(2)
        b2_t = Tex("GDP versus GNP --- one letter apart").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex(r"GDP: produced INSIDE the borders,").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex(r"whoever owns the producer").scale(1.05).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1)); self.wait(1.6)
        self.play(Write(b2_l2)); self.wait(2)
        b2_l3 = Tex(r"GNP: produced by the nation's own people").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = Tex(r"and companies, anywhere on earth").scale(1.0).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l3)); self.wait(1.6)
        self.play(Write(b2_l4)); self.wait(2)
        b2_l5 = Tex(r"The ground versus").scale(1.1).shift(band_shift(2) + DOWN * 2.0)
        b2_l6 = Tex(r"the passport").scale(1.1).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l5)); self.wait(1.5)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): GDP shares as a bar chart of rectangles ---
        self.next_band(3)
        b3_t = Tex("How South Africa's GDP is shared").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        sc3 = band_shift(3)
        axis = Line(sc3 + UP * 1.4 + LEFT * 4.6, sc3 + DOWN * 2.0 + LEFT * 4.6, stroke_width=3)
        self.play(Create(axis))
        bars = [
            (r"Agriculture $\pm$3\%", 0.35, 1.0),
            (r"Mining under 10\%", 1.0, 0.1),
            (r"Secondary $\pm$20\%", 2.2, -0.8),
            (r"Tertiary $\pm$66\%", 6.4, -1.7),
        ]
        for label, w, dy in bars:
            bar = Rectangle(width=w, height=0.55, color=YELLOW).shift(
                sc3 + UP * dy + LEFT * 4.6 + RIGHT * (w / 2))
            lab = Tex(label).scale(0.9).shift(sc3 + UP * dy + LEFT * 4.6 + RIGHT * (w + 1.9))
            self.play(Create(bar), Write(lab))
            self.wait(1.7)
        b3_l1 = Tex(r"Developed-economy shape, developing-world jobs shortage").scale(0.85).shift(sc3 + DOWN * 2.8)
        self.play(Write(b3_l1))
        self.wait(3)

        # --- Band 4 (subtopic_3): the money-jobs mismatch and its rule ---
        self.next_band(4)
        b4_t = Tex("Money and jobs disagree").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex(r"Agriculture: jobs share $\approx$ double GDP share").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex(r"Finance: fat GDP slice, few workers").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1)); self.wait(1.8)
        self.play(Write(b4_l2)); self.wait(2)
        b4_l3 = Tex(r"Rule: labour-intensive $\rightarrow$ more jobs than GDP;").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex(r"capital-intensive $\rightarrow$ more GDP than jobs").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l3)); self.wait(1.6)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(VGroup(b4_l3, b4_l4), color=GREEN)))
        self.wait(2)
        b4_l5 = Tex(r"Realities: unemployment above 30\%,").scale(1.0).shift(band_shift(4) + DOWN * 2.1)
        b4_l6 = Tex(r"and the invisible informal economy").scale(1.0).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5)); self.wait(1.6)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_4): the four-step reading order ---
        self.next_band(5)
        b5_t = Tex("Four steps for every data source").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex(r"1. Title, units, date first").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"2. Name the largest and smallest").scale(1.05).shift(band_shift(5) + UP * 0.3)
        b5_l3 = Tex(r"3. Hunt the trend or the contradiction").scale(1.05).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex(r"4. Attach a syllabus reason").scale(1.05).shift(band_shift(5) + DOWN * 1.3)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(1.8)
        b5_l5 = Tex(r"Twin pies: the gap IS the labour rule;").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        b5_l6 = Tex(r"50-year lines: the maturing-economy story").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5)); self.wait(1.5)
        self.play(Write(b5_l6))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the percentage-to-rand calculation ---
        self.next_band(6)
        b6_t = Tex("Percentage into rand").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex(r"GDP $\approx$ R7,5 trillion; agriculture $\approx$ 3\%").scale(1.1).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1)); self.wait(2)
        b6_l2 = MathTex(r"7\,500\,\text{billion} \times \tfrac{3}{100}").scale(1.15).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2)); self.wait(2)
        b6_l3 = MathTex(r"= 225\ \text{billion rand}").scale(1.15).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex(r"Tiny share, mountain of money ---").scale(1.05).shift(band_shift(6) + DOWN * 1.9)
        b6_l5 = Tex(r"write both halves down").scale(1.05).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l4)); self.wait(1.5)
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): one loaf of bread, four kinds of work ---
        self.next_band(7)
        b7_t = Tex("One loaf of bread, four kinds of work").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex(r"Somebody GREW the wheat --- primary").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex(r"Somebody BAKED it into bread --- secondary").scale(1.05).shift(band_shift(7) + UP * 0.3)
        b7_l3 = Tex(r"Somebody MOVED and SOLD it --- tertiary").scale(1.05).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex(r"Somebody BRED better wheat --- quaternary").scale(1.0).shift(band_shift(7) + DOWN * 1.3)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(1.9)
        b7_l5 = Tex(r"Raw in your hands? Then it is primary.").scale(1.0).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5)); self.wait(1.6)
        b7_l6 = Tex(r"Wheat cheap, sliced loaf dear: value added").scale(1.0).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the hundred-rand payout and its corrections ---
        self.next_band(8)
        b8_t = Tex("Sharing one hundred rand").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex(r"Farmer R3, miner under R10,").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"factory $\pm$R20, services $\pm$R66").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1)); self.wait(1.8)
        self.play(Write(b8_l2)); self.wait(2)
        b8_wrong = Tex(r"Small share $=$ small importance").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_wrong))
        self.play(Create(strike(b8_wrong)))
        self.wait(2)
        b8_l3 = Tex(r"The farmer's R3 FEEDS EVERYBODY;").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        b8_l4 = Tex(r"count heads and the shares move").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l3)); self.wait(1.6)
        self.play(Write(b8_l4)); self.wait(1.8)
        b8_l5 = Tex(r"GDP $=$ the ground, GNP $=$ the passport").scale(1.0).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): reading the numbers like a till slip ---
        self.next_band(9)
        b9_t = Tex("Reading the numbers like a till slip").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex(r"Top of the slip: title, units, year").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex(r"Loud things: biggest, smallest slice").scale(1.0).shift(band_shift(9) + UP * 0.5)
        b9_l3 = Tex(r"The story: what changed, where the gap is").scale(1.0).shift(band_shift(9) + DOWN * 0.2)
        b9_l4 = Tex(r"Explain with a reason from the lesson").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        for m in (b9_l1, b9_l2, b9_l3, b9_l4):
            self.play(Write(m))
            self.wait(1.8)
        b9_l5 = MathTex(r"3\% \text{ of } R7,5\,\text{trillion} \approx R225\,\text{billion}").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(2)
        b9_l6 = Tex(r"Honest pair: informal work goes uncounted;").scale(0.95).shift(band_shift(9) + DOWN * 2.4)
        b9_l7 = Tex(r"a percentage is not an importance").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l6)); self.wait(1.5)
        self.play(Write(b9_l7))
        self.wait(4)
