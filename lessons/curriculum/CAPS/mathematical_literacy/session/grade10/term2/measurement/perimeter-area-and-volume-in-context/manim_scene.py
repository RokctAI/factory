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
# write-only reveals — no sub-part transforms. Every calculation is built
# line by line with units kept on every line; SA currency format throughout.
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
        title = Tex("Perimeter, Area and Volume in Context").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Convert to ONE unit before any formula").scale(1.05).shift(UP * 1.4)
        self.play(Write(l01))
        self.wait(2)
        l02 = MathTex(r"3{,}5 \text{ m} = 350 \text{ cm}; \quad 2\,400 \text{ mm} = 2{,}4 \text{ m}").scale(0.88).shift(UP * 0.5)
        self.play(Write(l02))
        self.wait(2)
        l03 = MathTex(r"\text{Area factor squared: } 1 \text{ m}^2 = 10\,000 \text{ cm}^2").scale(0.91).shift(DOWN * 0.4)
        l04 = MathTex(r"\text{Volume cubed: } 1 \text{ m}^3 = 1\,000\,000 \text{ cm}^3").scale(0.96).shift(DOWN * 1.3)
        self.play(Write(l03))
        self.wait(2)
        self.play(Write(l04))
        self.wait(2)
        l05 = MathTex(r"1 \text{ m}^3 = 1\,000 \text{ litres}").scale(1.15).shift(DOWN * 2.4)
        self.play(Write(l05))
        self.play(Create(SurroundingRectangle(l05, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the two habits ---
        self.next_band(1)
        b1_t = Tex("Two habits that hold the marks").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("1. Write the unit on EVERY line —").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("a number without a unit earns nothing").scale(1.05).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("2. Round once, at the end:").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = Tex("money to the cent, paint to whole tins,").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        b1_l5 = Tex("days to whole days").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): fencing the garden ---
        self.next_band(2)
        b2_t = Tex("Fencing the 12 m $\\times$ 8 m garden").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"P = 2(12 + 8) = 2 \times 20 = 40 \text{ m}").scale(1.05).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{Gate: } 40 - 2 = 38 \text{ m of mesh}").scale(1.0).shift(band_shift(2) + UP * 0.3)
        b2_l3 = MathTex(r"38 \div 30 = 1{,}27 \to 2 \text{ rolls} = \text{R1 798,00}").scale(0.95).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = MathTex(r"\text{Poles: } 40 \div 2 = 20 \times \text{R65} = \text{R1 300,00}").scale(0.95).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Total materials: R3 098,00").scale(1.05).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        b2_l6 = Tex("Closed boundary: poles = gaps").scale(0.9).shift(band_shift(2) + DOWN * 3.2)
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_3): tiling the floor ---
        self.next_band(3)
        b3_t = Tex("Tiles: area, waste, boxes").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"A = 4{,}2 \times 3{,}5 = 14{,}7 \text{ m}^2").scale(1.05).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"+10\% \text{ waste: } 14{,}7 \times 1{,}10 = 16{,}17 \text{ m}^2").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"16{,}17 \div 1{,}5 = 10{,}78 \to 11 \text{ boxes}").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("$11 \\times$ R249,90 = R2 748,90").scale(1.05).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        b3_l5 = Tex("Area, adjust, divide by coverage, round up").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): painting the walls ---
        self.next_band(4)
        b4_t = Tex("Paint: walls minus openings, two coats").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Walls: } 2(4{,}2 + 3{,}5) \times 2{,}7 = 41{,}58 \text{ m}^2").scale(0.95).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"41{,}58 - 1{,}89 - 1{,}8 = 37{,}89 \text{ m}^2").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{Two coats: } 37{,}89 \times 2 = 75{,}78 \text{ m}^2").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = MathTex(r"75{,}78 \div 8 = 9{,}47 \; \ell \to 2 \times 5\,\ell \text{ tins}").scale(0.95).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("Cost: $2 \\times$ R429,99 = R859,98").scale(1.05).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): the water tank's volume ---
        self.next_band(5)
        b5_t = Tex("The tank: 1,4 m across, 1,6 m tall").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"r = 1{,}4 \div 2 = 0{,}7 \text{ m — HALVE it}").scale(1.05).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"V = 3{,}142 \times 0{,}7^2 \times 1{,}6").scale(1.05).shift(band_shift(5) + UP * 0.3)
        b5_l3 = MathTex(r"= 3{,}142 \times 0{,}49 \times 1{,}6 = 2{,}463 \text{ m}^3").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"2{,}463 \times 1\,000 = 2\,463 \text{ litres}").scale(1.05).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        b5_l5 = Tex("Skip the halving: answer 4$\\times$ too big").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): days of supply, and the roof ---
        self.next_band(6)
        b6_t = Tex("How long does the tank last?").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"5 \times 90 = 450 \; \ell \text{ per day}").scale(1.05).shift(band_shift(6) + UP * 1.2)
        b6_l2 = MathTex(r"2\,463 \div 450 = 5{,}47 \text{ days}").scale(1.05).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Supplies round DOWN: 5 complete days").scale(1.05).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = MathTex(r"\text{Roof: } 60 \times 0{,}012 = 0{,}72 \text{ m}^3 = 720 \; \ell").scale(0.95).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("12 mm = 0,012 m — convert before multiplying").scale(0.9).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): walk around, cover, fill ---
        self.next_band(7)
        b7_t = Tex("Walking around it, covering it, filling it").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("How far around? Perimeter: walk 40 m").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("How much to cover? Area: 14,7 squares").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("How much to fill? Volume — and").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        b7_l4 = MathTex(r"1 \text{ m}^3 = 1\,000 \text{ litres}").scale(1.05).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)
        b7_l5 = Tex("A m$^2$ is a 100-by-100 block: 10 000 cm$^2$").scale(0.95).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): the shopping list ---
        self.next_band(8)
        b8_t = Tex("Buying enough without buying too much").scale(1.05).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Fence: 38 m needs 2 rolls — R1 798,").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("22 m left over — say so in the answer").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Tiles: add 10\\% first, then 11 boxes").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Walls: perimeter $\\times$ height, minus").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        b8_l5 = Tex("door and window, two coats, 2 tins").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex("Materials: whatever the decimal, go UP").scale(1.0).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): how many days the tank gives ---
        self.next_band(9)
        b9_t = Tex("How many days does the tank give you?").scale(1.05).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("A drum is a circle pushed upward").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"3{,}142 \times 0{,}7 \times 0{,}7 \times 1{,}6 \approx 2{,}463 \text{ m}^3").scale(0.95).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"2\,463 \div 450 = 5{,}47 \to 5 \text{ full days}").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Materials up; days and whole items down").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("One shower on a 60 m$^2$ roof: 720 litres").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.wait(4)
