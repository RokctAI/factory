# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

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
        l02 = Tex("Order matters: boys : girls $= 4:5$, not $5:4$").scale(1.0).shift(UP * 0.3)
        self.play(Write(l02))
        self.wait(2)
        l03 = Tex("Same unit BEFORE simplifying:").scale(1.0).shift(DOWN * 0.6)
        l04 = MathTex(r"400\text{ g} : 2\text{ kg} = 400 : 2\,000 = 1 : 5").scale(1.05).shift(DOWN * 1.5)
        self.play(Write(l03))
        self.play(Write(l04))
        self.play(Create(SurroundingRectangle(l04, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): sharing R3 600 in 4 : 3 : 2 ---
        self.next_band(1)
        b1_t = Tex("Share R3 600 in the ratio $4:3:2$").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{Parts: } 4 + 3 + 2 = 9").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"\text{One part: } 3\,600 \div 9 = 400").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Naledi: $4 \\times$ R400 = R1 600").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = Tex("Karabo: $3 \\times$ R400 = R1 200; Anele: R800").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Check: R1 600 + R1 200 + R800 = R3 600").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_1): the concrete mix ---
        self.next_band(2)
        b2_t = Tex("Concrete mix $2:3:4$, 36 wheelbarrows").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"2 + 3 + 4 = 9 \text{ parts}").scale(1.1).shift(band_shift(2) + UP * 1.0)
        b2_l2 = MathTex(r"\text{One part: } 36 \div 9 = 4").scale(1.1).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("Cement 8, sand 12, stone 16").scale(1.1).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = MathTex(r"\text{Check: } 8 + 12 + 16 = 36").scale(1.05).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): unit rates — the trip ---
        self.next_band(3)
        b3_t = Tex("Rate: keeps its units — ``per'' = for one").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"560 \text{ km on } 40 \ell: \; 560 \div 40 = 14 \text{ km}/\ell").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"350 \text{ km trip: } 350 \div 14 = 25 \ell").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("At R22,80 per litre: $25 \\times$ R22,80").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        b3_l4 = Tex("Trip fuel cost = R570,00").scale(1.1).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_2): the time-unit trap and the tariff ---
        self.next_band(4)
        b4_t = Tex("Speed: 54 km in 45 minutes, in km/h?").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"54 \div 45 = 1{,}2 \text{ km/h}").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.play(Create(strike(b4_l1)))
        self.wait(2)
        b4_l2 = MathTex(r"45 \text{ min} = \frac{45}{60} = 0{,}75 \text{ h}").scale(1.05).shift(band_shift(4) + UP * 0.0)
        b4_l3 = MathTex(r"54 \div 0{,}75 = 72 \text{ km/h}").scale(1.1).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = Tex("Tariff: 15 k$\\ell$ $\\times$ R16,80 = R252,00").scale(1.0).shift(band_shift(4) + DOWN * 2.1)
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
        b5_l1 = Tex("5 muffins cost R85,00").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"85 \div 5 = 17 \;\; (\text{R17,00 per muffin})").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("9 muffins: $9 \\times$ R17,00 = R153,00").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
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
        b6_l1 = MathTex(r"6 \text{ workers} \times 20 \text{ days} = 120 \text{ worker-days}").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"8 \text{ workers: } 120 \div 8 = 15 \text{ days}").scale(1.05).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex("Minibus at fixed R1 080: 12 learners pay R90,00;").scale(0.95).shift(band_shift(6) + DOWN * 1.0)
        b6_l4 = Tex("18 pay R60,00 — $12 \\times 90 = 18 \\times 60 = 1\\,080$").scale(0.95).shift(band_shift(6) + DOWN * 1.8)
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
        b7_l1 = Tex("2 kg at R56,99: R56,99 $\\div$ 2").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("= R28,495 $\\approx$ R28,50 per kg").scale(1.05).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("10 kg at R249,99: R249,99 $\\div$ 10 = R25,00/kg").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("10 kg bag is the better buy — R25,00/kg").scale(1.05).shift(band_shift(7) + DOWN * 1.4)
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
        b8_l2 = MathTex(r"4 + 3 + 2 = 9; \quad 3\,600 \div 9 = 400").scale(1.05).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Deal out: R1 600, R1 200, R800").scale(1.05).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("Add them back: R3 600 exactly").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Same container first: 400 g : 2 000 g = 1 : 5").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): what one costs, what one does ---
        self.next_band(9)
        b9_t = Tex("What ONE costs, what ONE does").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = MathTex(r"560 \div 40 = 14 \text{ km each litre}").scale(1.05).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("350 km needs 25 $\\ell$: $25 \\times$ R22,80 = R570,00").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex("Per HOUR? Time into hours first:").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        b9_l4 = MathTex(r"54 \div 0{,}75 = 72 \text{ km/h}").scale(1.05).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Water: 15 k$\\ell$ $\\times$ R16,80 = R252,00").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): more hands, fewer days; the real price ---
        self.next_band(10)
        b10_t = Tex("More hands, fewer days — and the shelf").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Muffins: R17,00 each, so 9 cost R153,00").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = MathTex(r"6 \times 20 = 120 \text{ worker-days}; \;\; 120 \div 8 = 15").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("Minibus R1 080: 12 pay R90,00; 18 pay R60,00").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("Shelf: R28,50/kg vs R25,00/kg — big bag wins").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("Say the number, then say the condition").scale(1.0).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l5))
        self.wait(4)
