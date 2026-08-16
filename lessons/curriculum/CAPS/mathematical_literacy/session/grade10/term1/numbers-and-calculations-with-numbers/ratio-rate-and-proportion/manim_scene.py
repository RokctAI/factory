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

# BAND LAYOUT: sequential vertical bands, one frame-height each; the camera
# moves down between teaching steps and nothing is ever removed. Only
# exporter-supported mobjects (Tex/MathTex, Line, SurroundingRectangle) with
# write-only reveals — no sub-part transforms.
#
# Mirrors script.md across the seven subtopics of the duo (Part 1 — Expert:
# subtopics 1-4; Part 2 — Simplifier: 5-7); band time proportional to
# subtopics.json. All money in SA format (R1 234,56 / decimal comma).

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


def strike(m):
    """Diagonal cancellation stroke through a wrong line, teacher-style."""
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RatioRateProportionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): what a ratio is ---
        title = Tex("Ratio, Rate and Proportion").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Ratio: same kind, same unit, no unit of its own").scale(1.0).shift(UP * 1.2)
        self.play(Write(l01))
        self.wait(2)
        l02 = Tex("Order matters: adults : children $= 3:7$, not $7:3$").scale(1.0).shift(UP * 0.3)
        self.play(Write(l02))
        self.wait(2)
        l03 = Tex("Same unit BEFORE simplifying:").scale(1.0).shift(DOWN * 0.6)
        l04 = MathTex(r"250\text{ g} : 1\text{ kg} = 250 : 1\,000 = 1 : 4").scale(1.05).shift(DOWN * 1.5)
        self.play(Write(l03))
        self.play(Write(l04))
        self.play(Create(SurroundingRectangle(l04, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): sharing R2 400 in 5 : 3 : 2 ---
        self.next_band(1)
        b1_t = Tex("Share R2 400 in the ratio $5:3:2$").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{Parts: } 5 + 3 + 2 = 10").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"\text{One part: } 2\,400 \div 10 = 240").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Lerato: $5 \\times$ R240 = R1 200").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = Tex("Sipho: $3 \\times$ R240 = R720; Mpho: R480").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Check: R1 200 + R720 + R480 = R2 400").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_1): the concrete mix ---
        self.next_band(2)
        b2_t = Tex("Concrete mix $1:3:5$, 27 wheelbarrows").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"1 + 3 + 5 = 9 \text{ parts}").scale(1.1).shift(band_shift(2) + UP * 1.0)
        b2_l2 = MathTex(r"\text{One part: } 27 \div 9 = 3").scale(1.1).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("Cement 3, sand 9, stone 15").scale(1.1).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = MathTex(r"\text{Check: } 3 + 9 + 15 = 27").scale(1.05).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): unit rates — the bakkie ---
        self.next_band(3)
        b3_t = Tex("Rate: keeps its units — ``per'' = for one").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"480 \text{ km on } 40 \ell: \; 480 \div 40 = 12 \text{ km}/\ell").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"300 \text{ km trip: } 300 \div 12 = 25 \ell").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("At R23,40 per litre: $25 \\times$ R23,40").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        b3_l4 = Tex("Trip fuel cost = R585,00").scale(1.1).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_2): the time-unit trap and the tariff ---
        self.next_band(4)
        b4_t = Tex("Speed: 63 km in 45 minutes, in km/h?").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"63 \div 45 = 1{,}4 \text{ km/h}").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.play(Create(strike(b4_l1)))
        self.wait(2)
        b4_l2 = MathTex(r"45 \text{ min} = \frac{45}{60} = 0{,}75 \text{ h}").scale(1.05).shift(band_shift(4) + UP * 0.0)
        b4_l3 = MathTex(r"63 \div 0{,}75 = 84 \text{ km/h}").scale(1.1).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = Tex("Tariff: 18 k$\\ell$ $\\times$ R14,50 = R261,00").scale(1.0).shift(band_shift(4) + DOWN * 2.1)
        b4_l5 = Tex("Cost = rate $\\times$ number of units").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): direct proportion ---
        self.next_band(5)
        b5_t = Tex("Direct proportion: up together").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("6 loaves cost R114,00").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"114 \div 6 = 19 \;\; (\text{R19,00 per loaf})").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("11 loaves: $11 \\times$ R19,00 = R209,00").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = Tex("Unitary method: down to one, up to what").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        b5_l5 = Tex("you want. Test: dividing gives a constant.").scale(1.0).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_3): indirect proportion ---
        self.next_band(6)
        b6_t = Tex("Indirect: one up, the other down").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"4 \text{ painters} \times 15 \text{ days} = 60 \text{ painter-days}").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"6 \text{ painters: } 60 \div 6 = 10 \text{ days}").scale(1.05).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex("Bus at fixed R900: 15 learners pay R60,00;").scale(1.0).shift(band_shift(6) + DOWN * 1.0)
        b6_l4 = Tex("20 pay R45,00 — $15 \\times 60 = 20 \\times 45 = 900$").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Up together: divide. Opposite ways: multiply.").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): best buy ---
        self.next_band(7)
        b7_t = Tex("Best buy: compare the price of ONE kg").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("2,5 kg at R42,99: R42,99 $\\div$ 2,5").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("= R17,196 $\\approx$ R17,20 per kg").scale(1.05).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("10 kg at R159,99: R159,99 $\\div$ 10 = R16,00/kg").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("10 kg bag is the better buy — R16,00/kg").scale(1.05).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("Round at the END; keep units on every line;").scale(0.95).shift(band_shift(7) + DOWN * 2.3)
        b7_l6 = Tex("state the condition: affordability and storage").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): cutting the loaf into shares ---
        self.next_band(8)
        b8_t = Tex("Cutting the loaf into shares").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Cut into the TOTAL number of parts first").scale(1.05).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"5 + 3 + 2 = 10; \quad 2\,400 \div 10 = 240").scale(1.05).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Deal out: R1 200, R720, R480").scale(1.05).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("Add them back: R2 400 exactly").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Same container first: 250 g : 1 000 g = 1 : 4").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): what one costs, what one does ---
        self.next_band(9)
        b9_t = Tex("What ONE costs, what ONE does").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = MathTex(r"480 \div 40 = 12 \text{ km each litre}").scale(1.05).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("300 km needs 25 $\\ell$: $25 \\times$ R23,40 = R585,00").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex("Per HOUR? Time into hours first:").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        b9_l4 = MathTex(r"63 \div 0{,}75 = 84 \text{ km/h}").scale(1.05).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Water: 18 k$\\ell$ $\\times$ R14,50 = R261,00").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): more hands, fewer days; the real price ---
        self.next_band(10)
        b10_t = Tex("More hands, fewer days — and the shelf").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Loaves: R19,00 each, so 11 cost R209,00").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = MathTex(r"4 \times 15 = 60 \text{ painter-days}; \;\; 60 \div 6 = 10").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("Bus R900: 15 pay R60,00; 20 pay R45,00").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("Shelf: R17,20/kg vs R16,00/kg — big bag wins").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("Say the number, then say the condition").scale(1.0).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l5))
        self.wait(4)
