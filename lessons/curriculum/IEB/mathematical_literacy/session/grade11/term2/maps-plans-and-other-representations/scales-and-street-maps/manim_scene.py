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

# Band layout: one frame-height band per teaching beat; the camera moves down,
# nothing is removed. Exporter-supported mobjects only (Tex/MathTex/Line/
# Rectangle/SurroundingRectangle); single-string Write reveals throughout.
#
# Covers all seven subtopics (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# band time roughly proportional to subtopics.json
# (215/220/225/230/195/195/195 of 1475 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ScalesAndStreetMapsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the number scale ---
        title = Tex("Scales and Street Maps").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l1 = Tex(r"1 : 25\,000 — one map unit is 25\,000 real ones").scale(1.0).shift(UP * 1.1)
        self.play(Write(l1)); self.wait(2)
        l2 = MathTex(r"8 \text{ cm} \times 25\,000 = 200\,000 \text{ cm}").scale(1.1).shift(UP * 0.2)
        l3 = MathTex(r"200\,000 \text{ cm} = 2\,000 \text{ m} = 2 \text{ km}").scale(1.1).shift(DOWN * 0.7)
        self.play(Write(l2)); self.wait(2.5)
        self.play(Write(l3))
        self.play(Create(SurroundingRectangle(l3, color=GREEN)))
        self.wait(2.5)
        l4 = Tex("Measure, multiply, convert — always in that order").scale(0.95).shift(DOWN * 1.8)
        self.play(Write(l4)); self.wait(2.5)

        # --- Band 1 (subtopic_1): the reverse, and the sense test ---
        self.next_band(1)
        b1_title = Tex("Backwards, and the sense test").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"6 \text{ km} = 600\,000 \text{ cm}; \;\; 600\,000 \div 25\,000 = 24 \text{ cm}").scale(0.9).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2.5)
        b1_l2 = Tex("Map to ground: grows. Ground to map: shrinks.").scale(1.0).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2)); self.wait(2.5)
        b1_wrong = Tex("A town route of 20 km? A road in 2 mm? Recheck!").scale(0.95).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2.5)
        b1_l3 = Tex(r"Anchors: 100 cm $=$ 1 m; \; 100\,000 cm $=$ 1 km").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l3)); self.wait(2.5)

        # --- Band 2 (subtopic_2): the bar scale ---
        self.next_band(2)
        b2_title = Tex("The bar scale: distance as a drawing").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        bar = Rectangle(width=6.0, height=0.5).shift(band_shift(2) + UP * 1.1)
        self.play(Create(bar))
        seg1 = Line(band_shift(2) + LEFT * 1.0 + UP * 1.35, band_shift(2) + LEFT * 1.0 + UP * 0.85)
        seg2 = Line(band_shift(2) + RIGHT * 1.0 + UP * 1.35, band_shift(2) + RIGHT * 1.0 + UP * 0.85)
        self.play(Create(seg1), Create(seg2))
        b2_l1 = Tex(r"3 cm of bar $=$ 12 km, so 1 cm $=$ 4 km").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1)); self.wait(2.5)
        b2_l2 = MathTex(r"\text{Route of } 7 \text{ cm}: \; 7 \times 4 = 28 \text{ km}").scale(1.05).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex("No ruler? Tick the route on a paper edge, count stripes").scale(0.9).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l3)); self.wait(2.5)

        # --- Band 3 (subtopic_2): the photocopier problem ---
        self.next_band(3)
        b3_title = Tex("Shrink the map — which scale survives?").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_wrong = Tex(r"The printed 1 : 25\,000 on an 80\% copy — now a lie").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2.5)
        b3_l1 = Tex("The bar shrinks WITH the roads — proportion survives").scale(0.95).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2.5)
        b3_l2 = Tex("Number scale: exact, but only at original size").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        b3_l3 = Tex("Bar scale: robust to resizing, inherits your ruler").scale(0.95).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l2)); self.wait(2.5)
        self.play(Write(b3_l3)); self.wait(2.5)

        # --- Band 4 (subtopic_3): grids and directions ---
        self.next_band(4)
        b4_title = Tex("Finding the place, naming the way").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Grid: library at D2 — column D meets row 2, one block").scale(0.92).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1)); self.wait(2.5)
        b4_l2 = Tex("Compass: north top, east right — White River lies NE").scale(0.92).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2)); self.wait(2.5)
        b4_l3 = Tex("Relative: left and right travel with the traveller").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3)); self.wait(2.5)
        b4_l4 = Tex("Heading south, west is on your RIGHT — orient first!").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): distance, time ---
        self.next_band(5)
        b5_title = Tex(r"Road map 1 : 200\,000 — route 11 cm").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"11 \times 200\,000 = 2\,200\,000 \text{ cm} = 22 \text{ km}").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2.5)
        b5_l2 = MathTex(r"\text{Time: } 22 \div 55 = 0{,}4 \text{ h}").scale(1.05).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2)); self.wait(2.5)
        b5_wrong = Tex(r"0,4 h $=$ 40 minutes?").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l3 = MathTex(r"0{,}4 \times 60 = 24 \text{ minutes}").scale(1.05).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): fuel, rands and the comparison ---
        self.next_band(6)
        b6_title = Tex("Fuel, rands, and who should drive").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"22 \div 100 \times 7{,}5 = 1{,}65 \text{ litres}").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"1{,}65 \times 22{,}80 = R37{,}62; \;\; \text{return } R75{,}24").scale(0.95).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1)); self.wait(2.5)
        self.play(Write(b6_l2)); self.wait(2.5)
        b6_l3 = Tex(r"Minibus: R30 each way — R60 return per person").scale(0.95).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l3)); self.wait(2.5)
        b6_l4 = Tex(r"Four travellers: car R75,24 vs minibus R240 — save R164,76").scale(0.85).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the shrinking machine ---
        self.next_band(7)
        b7_title = Tex("The world through a shrinking machine").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2.5)
        b7_l1 = Tex(r"Everything 25\,000 times smaller — evenly").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1)); self.wait(3)
        b7_l2 = MathTex(r"8 \text{ cm} \to 200\,000 \text{ cm} \to 2\,000 \text{ m} \to 2 \text{ km}").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(3)
        b7_l3 = Tex("Paper to world: balloon. World to paper: collapse.").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3)); self.wait(3)
        b7_l4 = Tex("Ruler first, multiply second, tidy the units last").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4)); self.wait(3.5)

        # --- Band 8 (subtopic_6): the honest little bar ---
        self.next_band(8)
        b8_title = Tex("The little bar that survives the photocopier").scale(1.05).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = Tex(r"One stripe: 3 cm $=$ 12 km, so 1 cm $=$ 4 km").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1)); self.wait(3)
        b8_l2 = MathTex(r"7 \text{ cm route: } 7 \times 4 = 28 \text{ km}").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(3)
        b8_l3 = Tex("Shrunk copy: the ratio lies, the bar shrinks with the roads").scale(0.9).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3)); self.wait(3)
        b8_l4 = Tex("Exact but fragile, or rough but robust — say the trade-off").scale(0.9).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4)); self.wait(3.5)

        # --- Band 9 (subtopic_7): blocks, turns and petrol money ---
        self.next_band(9)
        b9_title = Tex("Block, turns, kilometres, minutes, rands").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = Tex("East along Henshall, left into Brown, library on the right").scale(0.88).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1)); self.wait(3)
        b9_l2 = MathTex(r"22 \text{ km at } 55: \; 0{,}4 \text{ h} = 24 \text{ min, not } 40").scale(0.95).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2)); self.wait(3)
        b9_l3 = MathTex(r"1{,}65 \ell; \; R37{,}62 \text{ there}; \; R75{,}24 \text{ return}").scale(0.95).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3)); self.wait(3)
        b9_l4 = Tex(r"Four in the car: about R18,81 each — the car wins by R164,76").scale(0.85).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(4)
