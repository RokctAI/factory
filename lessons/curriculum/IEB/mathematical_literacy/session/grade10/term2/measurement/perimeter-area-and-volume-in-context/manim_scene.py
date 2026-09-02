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
# exporter-supported mobjects (Tex/MathTex, Line, Rectangle/
# SurroundingRectangle) with write-only reveals — no sub-part transforms.
# Every calculation is built line by line in SA units and currency format.
#
# Mirrors script.md across the seven subtopics of the duo (Part 1 — Expert:
# subtopics 1-4; Part 2 — Simplifier: 5-7); band time proportional to
# subtopics.json.

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


class PerimeterAreaVolumeContextSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): convert first ---
        title = Tex("Perimeter, Area and Volume in Context").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Convert to ONE unit before any formula").scale(1.0).shift(UP * 1.3)
        self.play(Write(l01))
        self.wait(2)
        l02 = MathTex(r"1 \text{ m}^2 = 100 \times 100 = 10\,000 \text{ cm}^2").scale(1.0).shift(UP * 0.4)
        l03 = MathTex(r"1 \text{ m}^3 = 1\,000\,000 \text{ cm}^3").scale(1.0).shift(DOWN * 0.5)
        l04 = MathTex(r"1 \text{ m}^3 = 1\,000 \text{ litres}").scale(1.05).shift(DOWN * 1.4)
        self.play(Write(l02))
        self.wait(2)
        self.play(Write(l03))
        self.wait(2)
        self.play(Write(l04))
        self.play(Create(SurroundingRectangle(l04, color=GREEN)))
        self.wait(2)
        l05 = Tex("Lengths once, areas squared, volumes cubed").scale(0.95).shift(DOWN * 2.4)
        self.play(Write(l05))
        self.wait(3)

        # --- Band 1 (subtopic_1): the two habits ---
        self.next_band(1)
        b1_t = Tex("The two habits that hold the marks").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("1. The unit goes on EVERY line of working").scale(1.0).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"4{,}2 \text{ m} = 420 \text{ cm}; \;\; 1\,750 \text{ mm} = 1{,}75 \text{ m}").scale(0.95).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("2. Never round mid-journey —").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        b1_l4 = Tex("carry the full value, round ONCE at the end").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): fencing the garden ---
        self.next_band(2)
        b2_t = Tex("Fencing: perimeter as a shopping list").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        garden = Rectangle(width=5.6, height=3.6).shift(band_shift(2) + DOWN * 0.4)
        self.play(Create(garden))
        self.wait(1.5)
        b2_l1 = MathTex(r"P = 2 \times (14 + 9) = 46 \text{ m}").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2)
        b2_l2 = MathTex(r"\text{Mesh: } 44 \div 25 = 1{,}76 \to 2 \text{ rolls} = 1\,498").scale(0.85).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"\text{Poles: } 46 \div 2 = 23 \to 1\,656; \;\; \text{total } 3\,154").scale(0.85).shift(band_shift(2) + DOWN * 3.2)
        self.play(Write(b2_l3))
        self.wait(3)

        # --- Band 3 (subtopic_3): tiling the floor ---
        self.next_band(3)
        b3_t = Tex("Tiling: area, coverage and waste").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Floor: } 4{,}0 \times 3{,}6 = 14{,}4 \text{ m}^2").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"+10\%: \; 14{,}4 \times 1{,}10 = 15{,}84 \text{ m}^2").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"15{,}84 \div 1{,}8 = 8{,}8 \to 9 \text{ boxes}").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = MathTex(r"9 \times 289{,}90 = 2\,609{,}10").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Waste first, divide second, round up last").scale(0.95).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): painting the walls ---
        self.next_band(4)
        b4_t = Tex("Painting: perimeter $\\times$ height, minus openings").scale(1.0).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"15{,}2 \times 2{,}6 = 39{,}52 \text{ m}^2").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"39{,}52 - 1{,}89 - 1{,}68 = 35{,}95 \text{ m}^2").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)
        b4_l3 = MathTex(r"\text{Two coats: } 71{,}90 \div 8 = 8{,}99 \text{ litres}").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"\to \text{two } 5\,\ell \text{ tins} = 790{,}00").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("The subtraction line earns its own mark").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): the water tank's volume ---
        self.next_band(5)
        b5_t = Tex("The tank: a circle pushed upward").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("1,2 m across $\\Rightarrow$ radius 0,6 m — HALVE IT").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"V = 3{,}142 \times 0{,}6^2 \times 1{,}8").scale(1.0).shift(band_shift(5) + UP * 0.3)
        b5_l3 = MathTex(r"= 3{,}142 \times 0{,}36 \times 1{,}8 = 2{,}036 \text{ m}^3").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = MathTex(r"2{,}036 \times 1\,000 = 2\,036 \text{ litres}").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Skip the halving: answer 4$\\times$ too big").scale(0.95).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): days of supply, and the roof ---
        self.next_band(6)
        b6_t = Tex("Days of supply — and the roof").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"4 \times 85 = 340 \text{ litres a day}").scale(1.0).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"2\,036 \div 340 = 5{,}99 \to 5 \text{ full days}").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)
        b6_l3 = Tex("Supplies round DOWN — the 6th day runs dry").scale(0.95).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"\text{Roof: } 75 \times 0{,}008 = 0{,}6 \text{ m}^3 = 600\,\ell").scale(0.95).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("8 mm of rain = 0,008 m — convert first").scale(0.95).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): walk around, cover, fill ---
        self.next_band(7)
        b7_t = Tex("Walk around it, cover it, fill it").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("How far around? PERIMETER — 46 m of wire").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("How much to cover? AREA — counting squares").scale(0.95).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("How much to fill? VOLUME — stacked cubes").scale(0.95).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = MathTex(r"1 \text{ m}^2 = 10\,000 \text{ cm}^2; \; 1 \text{ m}^3 = 1\,000\,000 \text{ cm}^3").scale(0.85).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("More dimensions = more conversion").scale(0.95).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): the shopping list ---
        self.next_band(8)
        b8_t = Tex("Buying enough without buying too much").scale(1.05).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = MathTex(r"\text{Mesh: } 2 \text{ rolls } (1\,498) + 6 \text{ m spare}").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"\text{Tiles: } 8{,}8 \to 9 \text{ boxes} = 2\,609{,}10").scale(0.95).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Walls: use perimeter, never floor area").scale(0.95).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = MathTex(r"\text{Paint: } 8{,}99\,\ell \to \text{two tins} = 790{,}00").scale(0.95).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = Tex("Materials: whatever the decimal, go UP").scale(0.95).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): how many days the tank gives ---
        self.next_band(9)
        b9_t = Tex("How many days does the tank give you").scale(1.05).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = MathTex(r"3{,}142 \times 0{,}36 \times 1{,}8 = 2{,}036 \text{ m}^3").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"= 2\,036 \text{ litres}; \;\; 2\,036 \div 340 = 5{,}99").scale(0.95).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("NOT 6 — the sixth day dies before supper").scale(0.95).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("Materials UP; days and whole items DOWN").scale(0.95).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Finish with a sentence a family can act on").scale(0.95).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l5))
        self.wait(4)
