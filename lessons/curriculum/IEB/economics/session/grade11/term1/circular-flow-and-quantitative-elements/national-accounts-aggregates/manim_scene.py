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

# Band-layout whiteboard scene for "National Accounts Aggregates" (IEB).
# (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier subtopics 5-7.)
# Every worked calculation from the script appears line by line in MathTex.
# Exporter-safe primitives only; add-only lifecycle.
# Subtopic durations: 210/240/240/250/180/180/180 of 1480 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class NationalAccountsAggregatesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===================== Part 1 — Expert =====================
        # --- Band 0 (subtopic_1): three doors into one room ---
        title = Tex("National Accounts Aggregates").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0a = Tex("Produced $=$ sold $=$ paid for $=$ earned").scale(1.1).shift(UP * 1.2)
        self.play(Write(b0a))
        self.play(Create(SurroundingRectangle(b0a, color=GREEN)))
        self.wait(2)
        b0b = Tex("Production door: sum each firm's VALUE ADDED").scale(1.0).shift(UP * 0.1)
        b0c = Tex("Expenditure door: spending on FINAL goods only").scale(1.0).shift(DOWN * 0.7)
        b0d = Tex("Income door: wages $+$ operating surplus").scale(1.0).shift(DOWN * 1.5)
        self.play(Write(b0b))
        self.wait(2)
        self.play(Write(b0c))
        self.wait(2)
        self.play(Write(b0d))
        self.wait(2)
        b0e = Tex("Three doors, one room — mismatch printed as residual").scale(0.95).shift(DOWN * 2.5)
        self.play(Write(b0e))
        self.wait(3)

        # --- Band 1 (subtopic_1): three word-pairs ---
        self.next_band(1)
        b1t = Tex("Three word-pairs at your fingertips").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = Tex("Final vs intermediate: sugar to a bottler is").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1a2 = Tex("intermediate; in the trolley, final — purpose decides").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1a))
        self.play(Write(b1a2))
        self.wait(2.5)
        b1b = Tex("Gross vs net: net removes consumption of").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        b1b2 = Tex("fixed capital — only net shows real growth").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1b))
        self.play(Write(b1b2))
        self.wait(2.5)
        b1c = Tex("Domestic asks WHERE: inside the borders;").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        b1c2 = Tex("national asks WHO: residents, wherever").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1c))
        self.play(Write(b1c2))
        self.play(Create(SurroundingRectangle(VGroup(b1c, b1c2), color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): household consumption C ---
        self.next_band(2)
        b2t = Tex("C: the giant of the expenditure side").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex("Roughly sixty cents of every rand of spending").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2a))
        self.wait(2)
        b2b = Tex("Durable (3+ yrs): cars, washing machines, laptops").scale(0.92).shift(band_shift(2) + UP * 0.4)
        b2c = Tex("Semi-durable: uniforms, shoes, curtains").scale(0.95).shift(band_shift(2) + DOWN * 0.3)
        b2d = Tex("Non-durable: maize meal, petrol, medicine").scale(0.95).shift(band_shift(2) + DOWN * 1.0)
        b2e = Tex("Services: transport, school fees, data, insurance").scale(0.92).shift(band_shift(2) + DOWN * 1.7)
        for m in (b2b, b2c, b2d, b2e):
            self.play(Write(m))
            self.wait(1.5)
        b2f = Tex("Durables can be delayed — first casualties of a downturn").scale(0.88).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2f))
        self.play(Create(SurroundingRectangle(b2f, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): G and its two evictions ---
        self.next_band(3)
        b3t = Tex("G: government consumption — two evictions").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("In G: salaries of teachers, doctors, magistrates;").scale(0.95).shift(band_shift(3) + UP * 1.1)
        b3a2 = Tex("textbooks, vaccines, diesel, electricity").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3a))
        self.play(Write(b3a2))
        self.wait(2.5)
        b3w1 = Tex("Social grants sit inside G").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3w1))
        self.play(Create(strike(b3w1)))
        b3r1 = Tex("A transfer buys nothing — counted once, in C").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3r1))
        self.wait(2.5)
        b3w2 = Tex("A new water treatment works sits inside G").scale(1.0).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3w2))
        self.play(Create(strike(b3w2)))
        b3r2 = Tex("An asset was created — record it under I").scale(0.95).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3r2))
        self.play(Create(SurroundingRectangle(b3r2, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): gross fixed capital formation ---
        self.next_band(4)
        b4t = Tex("I: gross fixed capital formation").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("Assets serving in production for over a year").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4a))
        self.wait(2)
        b4b = Tex("Buildings, highways, rail, dams, harbours;").scale(0.95).shift(band_shift(4) + UP * 0.4)
        b4b2 = Tex("machinery, vehicles, ICT, orchards, dairy herds").scale(0.95).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(b4b))
        self.play(Write(b4b2))
        self.wait(2.5)
        b4c = Tex("Existing office block bought: NOT capital formation —").scale(0.9).shift(band_shift(4) + DOWN * 1.2)
        b4c2 = Tex("the asset only changed owners").scale(0.95).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4c))
        self.play(Write(b4c2))
        self.wait(2)
        b4d = Tex("Investors: private firms, public corporations, govt").scale(0.9).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4d))
        self.wait(3)

        # --- Band 5 (subtopic_3): net investment, and the target ---
        self.next_band(5)
        b5t = Tex("Gross to net, in rand billions").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5l1 = MathTex(r"\text{Gross I} = \text{R1 000 bn}, \; \text{depr.} = \text{R620 bn}").scale(0.95).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5l1))
        self.wait(2)
        b5l2 = MathTex(r"\text{Net I} = 1\,000 - 620 = \text{R}380\,\text{bn}").scale(1.1).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5l2))
        self.play(Create(SurroundingRectangle(b5l2, color=GREEN)))
        self.wait(2.5)
        b5a = Tex("Only R380 bn enlarges capacity; R620 bn stood still").scale(0.92).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5a))
        self.wait(2)
        b5l3 = MathTex(r"\frac{1\,000}{6\,700} = 14{,}9\% \quad \text{vs NDP goal} \approx 30\%").scale(0.86).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5l3))
        self.wait(2)
        b5b = Tex("Gross below depreciation $=$ eating your machines").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5b))
        self.wait(3)

        # --- Band 6 (subtopic_4): GNE and GDP ---
        self.next_band(6)
        b6t = Tex("GNE, then GDP (rand billions)").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6l1 = MathTex(r"GNE = C + G + I + \Delta\text{inventories}").scale(1.05).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6l1))
        self.wait(2)
        b6l2 = MathTex(r"= 4\,200 + 1\,500 + 1\,000 - 60 = 6\,640").scale(1.05).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6l2))
        self.play(Create(SurroundingRectangle(b6l2, color=GREEN)))
        self.wait(2.5)
        b6l3 = MathTex(r"GDP = GNE + X - M").scale(1.05).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6l3))
        self.wait(2)
        b6l4 = MathTex(r"= 6\,640 + 2\,100 - 2\,040 = 6\,700").scale(1.05).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6l4))
        self.play(Create(SurroundingRectangle(b6l4, color=GREEN)))
        self.wait(2)
        b6a = Tex("Produce more than you spend: net exports carry it out").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6a))
        self.wait(3)

        # --- Band 7 (subtopic_4): GVA and GNI ---
        self.next_band(7)
        b7t = Tex("GVA and GNI close the chain").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7l1 = MathTex(r"GDP = GVA + \text{taxes on products} - \text{subsidies}").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7l1))
        self.wait(2)
        b7l2 = MathTex(r"6\,000 + 730 - 30 = 6\,700").scale(1.05).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7l2))
        self.wait(2.5)
        b7l3 = MathTex(r"GNI = GDP + \text{income received} - \text{income paid}").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7l3))
        self.wait(2)
        b7l4 = MathTex(r"= 6\,700 + 110 - 290 = 6\,520").scale(1.05).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7l4))
        self.play(Create(SurroundingRectangle(b7l4, color=GREEN)))
        self.wait(2)
        b7a = Tex("GNI $<$ GDP: dividends owed to owners abroad").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7a))
        self.wait(3)

        # ===================== Part 2 — Simplifier =====================
        # --- Band 8 (subtopic_5): the country's till slip ---
        self.next_band(8)
        b8t = Tex("The country's till slip").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Towering pile: households — C, sixty cents in the rand").scale(0.9).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex("Washing machine: durable $\\cdot$ takkies: semi $\\cdot$ oranges: non").scale(0.85).shift(band_shift(8) + UP * 0.4)
        b8b2 = Tex("taxi ride: service — nothing left but having arrived").scale(0.9).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(b8b))
        self.play(Write(b8b2))
        self.wait(2.5)
        b8c = Tex("G: the teacher's salary, vaccines, ambulance diesel").scale(0.95).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8c))
        self.wait(2)
        b8w = Tex("Gogo's grant lands on the G pile").scale(1.0).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8w))
        self.play(Create(strike(b8w)))
        b8r = Tex("Counted once, in C, when she buys bread and tea").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8r))
        self.play(Create(SurroundingRectangle(b8r, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): spending that builds tomorrow ---
        self.next_band(9)
        b9t = Tex("Spending that builds tomorrow").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Flour and packaging get used up; the R500 000 oven").scale(0.92).shift(band_shift(9) + UP * 1.1)
        b9a2 = Tex("still bakes in ten years — that is capital").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9a))
        self.play(Write(b9a2))
        self.wait(2.5)
        b9l1 = MathTex(r"500\,000 - 180\,000 \text{ wear} = 320\,000 \text{ net}").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9l1))
        self.wait(2)
        b9l2 = MathTex(r"\text{Country: } 1\,000 - 620 = \text{R}380\,\text{bn new capacity}").scale(0.9).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9l2))
        self.play(Create(SurroundingRectangle(b9l2, color=GREEN)))
        self.wait(2)
        b9b = Tex("Used oven from a closing caf\\'e: no new oven exists").scale(0.92).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex("The only pile that lengthens NEXT year's slip").scale(1.0).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(b9c))
        self.wait(3)

        # --- Band 10 (subtopic_7): three totals, one country ---
        self.next_band(10)
        b10t = Tex("Three totals, one country").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10l1 = MathTex(r"\text{GNE: } 4\,200 + 1\,500 + 1\,000 - 60 = 6\,640").scale(0.95).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10l1))
        self.wait(2)
        b10l2 = MathTex(r"\text{GDP: } 6\,640 + 2\,100 - 2\,040 = 6\,700").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10l2))
        self.wait(2)
        b10l3 = MathTex(r"\text{GVA: } 6\,000 + 730 - 30 = 6\,700").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10l3))
        self.wait(2)
        b10l4 = MathTex(r"\text{GNI: } 6\,700 + 110 - 290 = 6\,520").scale(0.95).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10l4))
        self.play(Create(SurroundingRectangle(b10l4, color=GREEN)))
        self.wait(2)
        b10a = Tex("Spent $\\cdot$ produced $\\cdot$ maker's price $\\cdot$ kept").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10a))
        self.wait(2)
        b10b = Tex("The R180 bn gap: rent on foreign capital used here").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10b))
        self.wait(4)
