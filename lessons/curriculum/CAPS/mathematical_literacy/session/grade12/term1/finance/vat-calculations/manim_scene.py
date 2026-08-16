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

# Band-layout whiteboard scene for the VAT Calculations session duo.
# Part 1 — Expert: subtopics 1-4 (how VAT works, adding VAT, removing VAT,
# zero-rated items and the till slip). Part 2 — Simplifier: subtopics 5-7
# retell the loaf-and-slice picture, the backwards trap and the till-slip
# detective work. Durations 215/215/225/230/195/195/195 of 1470 s.
# Exporter-safe mobjects only (till slip as Rectangle + Tex rows);
# add-only lifecycle; camera moves down one band per teaching beat.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class VatCalculationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): how VAT works ---
        title = Tex("VAT Calculations").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Indirect tax: 15\\%, collected inside the price").scale(1.0).shift(UP * 1.1)
        b0_l2 = Tex("Excl.\\ VAT: before tax — quotes, wholesale").scale(1.0).shift(UP * 0.2)
        b0_l3 = Tex("Incl.\\ VAT: tax inside — shelves, till slips").scale(1.0).shift(DOWN * 0.7)
        b0_l4 = MathTex(r"\text{Exclusive} = 100\% \;\Rightarrow\; \text{Inclusive} = 115\%").scale(0.91).shift(DOWN * 1.7)
        b0_l5 = MathTex(r"\times 1,15 \text{ forward}; \quad \div 1,15 \text{ back}").scale(1.05).shift(DOWN * 2.6)
        self.play(Write(b0_l1)); self.wait(2)
        self.play(Write(b0_l2)); self.wait(2)
        self.play(Write(b0_l3)); self.wait(2)
        self.play(Write(b0_l4)); self.wait(2)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): adding VAT to the builder's quote ---
        self.next_band(1)
        b1_title = Tex("Adding VAT: the friendly direction").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{Quote: R14 800 excl.\ VAT}").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"14\;800 \times 0,15 = \text{R2 220,00}").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"14\;800 + 2\;220 = \text{R17 020,00}").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = MathTex(r"\text{One step: } 14\;800 \times 1,15 = 17\;020").scale(1.05).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b1_l4)); self.wait(3)

        # --- Band 2 (subtopic_2): the backpack, and the disciplines ---
        self.next_band(2)
        b2_title = Tex("Same machine at till-slip scale").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"480 \times 0,15 = 72; \quad 480 + 72 = \text{R}552").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("Say which price you were GIVEN").scale(1.05).shift(band_shift(2) + UP * 0.1)
        b2_l3 = Tex("Adding VAT to an inclusive price taxes the tax").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        b2_l4 = Tex("Round only at the end, to the cent").scale(1.05).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2)
        self.play(Write(b2_l2)); self.wait(2)
        self.play(Write(b2_l3)); self.wait(2.5)
        self.play(Write(b2_l4)); self.wait(3)

        # --- Band 3 (subtopic_3): removing VAT — the R299 shoes ---
        self.next_band(3)
        b3_title = Tex("Removing VAT: R299 on the shelf").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_wrong = MathTex(r"299 - 44,85 = 254,15 \;\text{(15\% off)}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l1 = Tex("The 15\\% was charged on the SMALLER price").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3_l2 = MathTex(r"299 \div 1,15 = \text{R}260,00").scale(1.1).shift(band_shift(3) + DOWN * 0.8)
        b3_l3 = MathTex(r"\text{VAT inside: } 299 - 260 = \text{R}39,00").scale(1.05).shift(band_shift(3) + DOWN * 1.7)
        b3_l4 = MathTex(r"\text{Check: } 260 \times 1,15 = 299").scale(1.05).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l1)); self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        self.play(Write(b3_l3)); self.wait(2)
        self.play(Write(b3_l4)); self.wait(3)

        # --- Band 4 (subtopic_3): the 15 over 115 fraction ---
        self.next_band(4)
        b4_title = Tex("The direct fraction for the VAT inside").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{VAT} = \text{inclusive} \times \tfrac{15}{115}").scale(1.1).shift(band_shift(4) + UP * 1.0)
        b4_l2 = MathTex(r"299 \times 15 \div 115 = \text{R}39,00").scale(1.1).shift(band_shift(4) + UP * 0.0)
        b4_l3 = Tex("15 parts of every 115 parts are tax").scale(1.05).shift(band_shift(4) + DOWN * 1.0)
        b4_l4 = Tex("Label the price first: 100\\% or 115\\%?").scale(1.05).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l1)); self.wait(2.5)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)
        self.play(Write(b4_l3)); self.wait(2.5)
        self.play(Write(b4_l4)); self.wait(3)

        # --- Band 5 (subtopic_4): the Saturday till slip ---
        self.next_band(5)
        b5_title = Tex("Zero-rated basics and the till slip").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        slip = Rectangle(width=8.0, height=3.4).shift(band_shift(5) + DOWN * 0.3)
        self.play(Create(slip))
        s_l1 = Tex("Zero-rated: maize meal, brown bread,").scale(0.95).shift(band_shift(5) + UP * 0.9)
        s_l2 = MathTex(r"\text{milk, eggs, oranges: R187,40}").scale(0.95).shift(band_shift(5) + UP * 0.1)
        s_l3 = MathTex(r"\text{Starred (VAT) goods: R412,85 incl.}").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        s_l4 = MathTex(r"412,85 \times 15 \div 115 = \text{R}53,85").scale(1.0).shift(band_shift(5) + DOWN * 1.5)
        self.play(Write(s_l1)); self.wait(2)
        self.play(Write(s_l2)); self.wait(2)
        self.play(Write(s_l3)); self.wait(2)
        self.play(Write(s_l4))
        self.play(Create(SurroundingRectangle(s_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = MathTex(r"\text{Trolley } 600,25 \text{: only R53,85 is tax}").scale(1.0).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the reverse trap and the famous pairs ---
        self.next_band(6)
        b6_title = Tex("Sort before any percentage moves").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_wrong = MathTex(r"600,25 \times 15 \div 115 \;\text{(whole slip)}").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        self.wait(2)
        b6_l1 = Tex("Part of the slip carries no VAT at all").scale(1.05).shift(band_shift(6) + UP * 0.1)
        b6_l2 = Tex("Brown bread free; white bread taxed").scale(1.05).shift(band_shift(6) + DOWN * 0.9)
        b6_l3 = Tex("Zero-rated $\\neq$ exempt (rent, school fees)").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l1)); self.wait(2.5)
        self.play(Write(b6_l2)); self.wait(2.5)
        self.play(Write(b6_l3)); self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the loaf and the slice ---
        self.next_band(7)
        b7_title = Tex("The fifteen percent that follows you").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2.5)
        b7_l1 = Tex("Plain loaf: 100\\%. Add the slice: 115\\%").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"14\;800 \times 1,15 = \text{R17 020}").scale(1.1).shift(band_shift(7) + UP * 0.1)
        b7_l3 = Tex("Shelf price: slice already inside, by law").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        b7_l4 = Tex("Circle `excl.\\ VAT' before you calculate").scale(1.05).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l1)); self.wait(3)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(3)
        self.play(Write(b7_l3)); self.wait(3)
        self.play(Write(b7_l4)); self.wait(3.5)

        # --- Band 8 (subtopic_6): the backwards trap ---
        self.next_band(8)
        b8_title = Tex("The backwards trap").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_wrong = MathTex(r"15\% \text{ off } 299 \to 254,15").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_wrong))
        self.play(Create(strike(b8_wrong)))
        self.wait(2.5)
        b8_l1 = Tex("You sliced the bigger loaf — too thick").scale(1.05).shift(band_shift(8) + UP * 0.2)
        b8_l2 = MathTex(r"299 \div 1,15 = \text{R}260; \;\; \text{VAT R}39").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        b8_l3 = MathTex(r"\text{Prove it: } 260 \times 1,15 = 299").scale(1.05).shift(band_shift(8) + DOWN * 1.8)
        b8_l4 = Tex("ON: multiply. OUT: divide. Never subtract").scale(1.05).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l1)); self.wait(3)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(3)
        self.play(Write(b8_l3)); self.wait(3)
        self.play(Write(b8_l4)); self.wait(3.5)

        # --- Band 9 (subtopic_7): reading the slip like a detective ---
        self.next_band(9)
        b9_title = Tex("Reading the till slip like a detective").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = Tex("The star is the story: starred = taxed").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"\text{Zero pile R187,40: not one cent of tax}").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_l3 = MathTex(r"\text{Starred pile: } 412,85 \times 15 \div 115 = 53,85").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = Tex("Fresh vegetables free; frozen chips taxed").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        b9_l5 = Tex("Sort, then slice — in that order, always").scale(1.05).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l1)); self.wait(3)
        self.play(Write(b9_l2)); self.wait(3)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(3)
        self.play(Write(b9_l4)); self.wait(3)
        self.play(Write(b9_l5)); self.wait(4)
