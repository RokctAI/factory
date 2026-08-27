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

# Band-layout whiteboard scene for Plans, Elevations and Packaging Models.
# One band per teaching beat; camera moves down, earlier work stays on the
# canvas. Exporter-supported mobjects only (Tex/MathTex/Line/Arrow/Dot/
# Circle/Rectangle); every working line is its own single-string Tex/MathTex
# revealed with Write. No transforms, no FadeOut.
#
# Subtopic time shares (subtopics.json, total 1545 s):
# 235/240/235/255/185/195/200 -> bands 0-1 / 2-3 / 4-5 / 6-8 / 9 / 10 / 11.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PlansElevationsPackagingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the plan's language and its scale
        title = Tex("Plans, Elevations and Packaging Models").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"\text{Scale } 1:100: \; 1 \text{ mm paper} = 100 \text{ mm real}").scale(0.98).shift(UP * 1.2)
        b0_l2 = Tex("So every centimetre is one metre").scale(1.1).shift(UP * 0.3)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2.5)
        b0_l3 = Tex("Walls: thick parallel lines (gap = thickness)").scale(1.0).shift(DOWN * 0.7)
        b0_l4 = Tex("Door: gap plus quarter-circle swing arc").scale(1.0).shift(DOWN * 1.5)
        b0_l5 = Tex("Window: thin double lines; WC, WHB, stove").scale(1.0).shift(DOWN * 2.3)
        b0_l6 = Tex("Plus the north arrow and the title block").scale(1.0).shift(DOWN * 3.1)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.wait(2)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): plan millimetres into real metres
        self.next_band(1)
        b1_t = Tex("Plan to building, and back again").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"50 \text{ mm} \times 100 = 5\;000 \text{ mm} = 5 \text{ m}").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"40 \text{ mm} \times 100 = 4\;000 \text{ mm} = 4 \text{ m}").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"\text{Floor area: } 5 \times 4 = 20 \text{ m}^2").scale(1.1).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = MathTex(r"\text{Reverse: 1,8 m bookshelf} = 1\;800 \div 100 = 18 \text{ mm}").scale(0.9).shift(band_shift(1) + DOWN * 1.8)
        b1_l5 = Tex("Sanity: rooms run 2 m to 8 m — else a slip").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l4))
        self.wait(2.5)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): views, and the matching detective work
        self.next_band(2)
        b2_t = Tex("Floor plan looks down; elevations look across").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("Floor plan: layout, walls, swings — no heights").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("Elevations: heights, roof pitch, window tops").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("Matching: list what the east wall holds").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex("One door, one wide window: the east view").scale(1.0).shift(band_shift(2) + DOWN * 1.3)
        b2_l5 = Tex("Mind the mirror: outside view flips left-right").scale(1.0).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=YELLOW)))
        self.wait(3)

        # --- Band 3 (subtopic_2): combining views, and drawing to scale
        self.next_band(3)
        b3_t = Tex("Two drawings size the glass together").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("Plan: width 1 500 mm; elevation: height 1 200 mm").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"1{,}5 \times 1{,}2 = 1{,}8 \text{ m}^2 \text{ of glass}").scale(1.1).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("Drawing a 3 m by 2,5 m laundry at 1 : 100:").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        room = Rectangle(width=3.0, height=2.5).scale(0.6).shift(band_shift(3) + LEFT * 3.4 + DOWN * 2.2)
        self.play(Create(room))
        door = Line(room.get_corner(DL) + RIGHT * 0.5, room.get_corner(DL) + RIGHT * 0.5 + UP * 0.45)
        self.play(Create(door))
        b3_l4 = Tex("30 mm by 25 mm, door gap 8 mm").scale(1.0).shift(band_shift(3) + RIGHT * 2.6 + DOWN * 1.8)
        b3_l5 = Tex("Ratios, symbols, labels — never art").scale(1.0).shift(band_shift(3) + RIGHT * 2.6 + DOWN * 2.7)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the exploded view and the inventory habit
        self.next_band(4)
        b4_t = Tex("Assembly diagrams: the exploded view").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("Parts float apart along their joining lines").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("Parts list: 2 sides, 4 shelves, 14 screws S").scale(1.0).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex("Inventory check BEFORE assembly starts").scale(1.0).shift(band_shift(4) + DOWN * 0.4)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"\text{14 screws, packets of 4: } 14 \div 4 = 3{,}5 \Rightarrow 4 \text{ packets}").scale(0.82).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)
        b4_l5 = Tex("Packets are sold whole — round UP, 2 spare").scale(1.0).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): sequence and orientation
        self.next_band(5)
        b5_t = Tex("Numbered steps carry real constraints").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("Shelf slides in BEFORE the back board closes").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("Screw on a dotted line: washer, shelf, side panel").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("Name the failure: blocked groove,").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("unreachable hole — never a vague `it breaks'").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2.5)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex("Orientation: arrows, THIS SIDE UP, L and R").scale(1.0).shift(band_shift(5) + DOWN * 2.1)
        b5_l6 = Tex("Mirrored twins differ only in their holes").scale(1.0).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.wait(2)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): packaging counted axis by axis
        self.next_band(6)
        b6_t = Tex("Packing the crate: axis by axis").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("Boxes 8 by 5 by 12 cm; crate 40 by 25 by 24 cm").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = MathTex(r"40 \div 8 = 5; \quad 25 \div 5 = 5; \quad 5 \times 5 = 25 \text{ per layer}").scale(0.87).shift(band_shift(6) + UP * 0.3)
        b6_l3 = MathTex(r"24 \div 12 = 2 \text{ layers}; \quad 25 \times 2 = 50 \text{ boxes}").scale(1.01).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = MathTex(r"\text{Volume check: } 24\;000 \div 480 = 50 \;\checkmark").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("A perfect fit — no wasted air this time").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): the volume trap, and scale models
        self.next_band(7)
        b7_t = Tex("Volume promises; the axis count delivers").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{9 cm long: } 40 \div 9 = 4 \text{ whole, 4 cm left over}").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("The leftover slice ships nothing but air").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"\text{Model at } 1:20: \; 3 \text{ m} \rightarrow 15 \text{ cm}, \; 1{,}2 \text{ m} \rightarrow 6 \text{ cm}").scale(0.8).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = MathTex(r"\text{Areas scale by the SQUARE: } \tfrac{1}{20^2} = \tfrac{1}{400}").scale(0.9).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l3))
        self.wait(2.5)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): material estimates — tiles and paint
        self.next_band(8)
        b8_t = Tex("The builder's estimate: tiles and paint").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = MathTex(r"\text{Tiles: } 20 \div 0{,}04 = 500; \; +10\% = 550").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = MathTex(r"550 \div 20 = 27{,}5 \;\Rightarrow\; \text{buy } 28 \text{ boxes}").scale(0.97).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = MathTex(r"\text{Walls: } 2 \times (5 + 4) \times 2{,}6 = 46{,}8 \text{ m}^2").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = MathTex(r"46{,}8 - 1{,}8 - 1{,}8 = 43{,}2; \;\; \times 2 \text{ coats} = 86{,}4 \text{ m}^2").scale(0.94).shift(band_shift(8) + DOWN * 1.6)
        b8_l5 = MathTex(r"86{,}4 \div 9 = 9{,}6 \;\Rightarrow\; \text{buy } 10 \text{ litres}").scale(1.0).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l3))
        self.wait(2.5)
        self.play(Write(b8_l4))
        self.wait(2.5)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): the drawing that speaks builder
        self.next_band(9)
        b9_t = Tex("The drawing that speaks builder").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(1.5)
        b9_l1 = Tex("Fat lines: walls; quarter-moon: door swing").scale(1.05).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("At 1 : 100 every centimetre is a metre").scale(1.05).shift(band_shift(9) + UP * 0.3)
        b9_l3 = MathTex(r"\text{Ruler: } 50 \times 40 \text{ mm} \rightarrow 5 \times 4 \text{ m room}").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("1,8 m bookshelf = 18 mm: park it with a pencil").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        b9_l5 = Tex("Rooms are people-sized: 2 m to 8 m").scale(1.05).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l4))
        self.wait(2.5)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_6): walking around the paper house
        self.next_band(10)
        b10_t = Tex("Walking around the paper house").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(1.5)
        b10_l1 = Tex("Four elevations, named for the wall they face").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("Detective: door plus wide window = east view").scale(1.0).shift(band_shift(10) + UP * 0.4)
        b10_l3 = Tex("Outside looking in, left and right swap").scale(1.05).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=YELLOW)))
        self.wait(2.5)
        b10_l4 = MathTex(r"\text{Glass: } 1{,}5 \text{ m wide} \times 1{,}2 \text{ m tall} = 1{,}8 \text{ m}^2").scale(0.92).shift(band_shift(10) + DOWN * 1.5)
        b10_l5 = Tex("The floor plan is silent about UP").scale(1.05).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l4))
        self.wait(2.5)
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (subtopic_7): crates, shelves and the hardware list
        self.next_band(11)
        b11_t = Tex("Crates, shelves and the hardware list").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(1.5)
        b11_l1 = Tex("Count the parts first; 14 screws needs 4 packets").scale(1.0).shift(band_shift(11) + UP * 1.2)
        b11_l2 = MathTex(r"\text{Tiles: } 500 \rightarrow 550 \rightarrow 28 \text{ boxes (UP)}").scale(1.0).shift(band_shift(11) + UP * 0.3)
        b11_l3 = MathTex(r"\text{Paint: } 46{,}8 - 3{,}6 = 43{,}2; \; \times 2 = 86{,}4; \; \div 9 \Rightarrow 10 \ell").scale(0.9).shift(band_shift(11) + DOWN * 0.6)
        self.play(Write(b11_l1))
        self.wait(2.5)
        self.play(Write(b11_l2))
        self.wait(2.5)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(2.5)
        b11_l4 = Tex("50 rooibos boxes: five along, five across, two layers").scale(1.0).shift(band_shift(11) + DOWN * 1.6)
        b11_l5 = Tex("Count whole boxes per side; volume only checks").scale(1.0).shift(band_shift(11) + DOWN * 2.5)
        self.play(Write(b11_l4))
        self.wait(2.5)
        self.play(Write(b11_l5))
        self.wait(4)
