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

# Band-layout whiteboard scene for the Building Plans and Models session duo.
# Part 1 — Expert: subtopics 1-4 (floor plan, elevations, quantities & cost,
# packing models). Part 2 — Simplifier: subtopics 5-7 re-teach the same maths
# with the builder's-bakkie framing. Subtopic durations (subtopics.json):
# 215/225/225/225/195/195/200 of 1480 s — simplifier bands get longer waits.
# Exporter-safe mobjects only; add-only lifecycle; camera moves between bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BuildingPlansAndModelsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(15)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the floor plan's language ---
        title = Tex("Building Plans and Models").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Floor plan: the view from above, roof off").scale(1.1).shift(UP * 1.1)
        b0_l2 = Tex("Door: gap in the wall + quarter-circle swing").scale(1.1).shift(UP * 0.2)
        b0_l3 = Tex("Window: thin triple line in the wall").scale(1.1).shift(DOWN * 0.7)
        b0_l4 = MathTex(r"\text{Scale } 1:50 \;\Rightarrow\; 1\text{ mm} = 50\text{ mm real}").scale(0.9).shift(DOWN * 1.7)
        self.play(Write(b0_l1)); self.wait(2)
        self.play(Write(b0_l2)); self.wait(2)
        self.play(Write(b0_l3)); self.wait(2)
        self.play(Write(b0_l4)); self.wait(3)

        # --- Band 1 (subtopic_1): the study plan, measured and converted ---
        self.next_band(1)
        b1_title = Tex("The new study, measured off the plan").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        # Plan sketch: room outline, door gap with swing line, window line
        room = Rectangle(width=4.0, height=3.2).shift(band_shift(1) + LEFT * 3.6 + DOWN * 0.4)
        self.play(Create(room))
        door = Line(room.get_corner(DR) + LEFT * 1.4, room.get_corner(DR) + LEFT * 0.5,
                    color=YELLOW, stroke_width=8)
        swing = Line(room.get_corner(DR) + LEFT * 1.4, room.get_corner(DR) + LEFT * 1.4 + UP * 0.9,
                     color=YELLOW)
        window = Line(room.get_corner(UL) + RIGHT * 0.9, room.get_corner(UL) + RIGHT * 2.4,
                      color=BLUE, stroke_width=8)
        self.play(Create(door), Create(swing))
        self.play(Create(window))
        w_lab = Tex("80 mm").scale(0.9).next_to(room, DOWN, buff=0.15)
        h_lab = Tex("64 mm").scale(0.9).next_to(room, LEFT, buff=0.15)
        self.play(Write(w_lab), Write(h_lab))
        self.wait(2)
        b1_l1 = MathTex(r"80 \times 50 = 4\;000\text{ mm} = 4,0\text{ m}").scale(1.05).shift(band_shift(1) + RIGHT * 2.9 + UP * 1.0)
        b1_l2 = MathTex(r"64 \times 50 = 3\;200\text{ mm} = 3,2\text{ m}").scale(1.05).shift(band_shift(1) + RIGHT * 2.9 + UP * 0.1)
        b1_l3 = MathTex(r"\text{Door: } 18 \to 900\text{ mm}").scale(1.05).shift(band_shift(1) + RIGHT * 2.9 + DOWN * 0.8)
        b1_l4 = MathTex(r"\text{Window: } 24 \to 1,2\text{ m}").scale(1.05).shift(band_shift(1) + RIGHT * 2.9 + DOWN * 1.7)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3)); self.wait(1.5)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(VGroup(b1_l1, b1_l2), color=GREEN)))
        b1_note = Tex("Inside faces = room; outside = footprint").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_note))
        self.wait(3)

        # --- Band 2 (subtopic_2): elevations carry the heights ---
        self.next_band(2)
        b2_title = Tex("Elevations: the house from the side").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex("North elevation = the face LOOKING north").scale(1.1).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("Elevations hold heights; plans hold layout").scale(1.1).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"\text{Walls: } 2,5\text{ m} \quad \text{sill: } 1\;000\text{ mm}").scale(1.1).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l1)); self.wait(2.5)
        self.play(Write(b2_l2)); self.wait(2.5)
        self.play(Write(b2_l3)); self.wait(3)

        # --- Band 3 (subtopic_2): matching plan to elevation ---
        self.next_band(3)
        b3_title = Tex("Which elevation is which?").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("1. Count the openings on that side").scale(1.1).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("2. Check widths against the scale").scale(1.1).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex("3. Check heights for reasonableness").scale(1.1).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex("Mind the mirror: plan's west = your right").scale(1.05).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = Tex("Tallest features identify the face fastest").scale(1.05).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l1)); self.wait(2)
        self.play(Write(b3_l2)); self.wait(2)
        self.play(Write(b3_l3)); self.wait(2)
        self.play(Write(b3_l4)); self.wait(2.5)
        self.play(Write(b3_l5)); self.wait(3)

        # --- Band 4 (subtopic_3): flooring — area, waste, boxes, rands ---
        self.next_band(4)
        b4_title = Tex("Flooring is area").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"4,0 \times 3,2 = 12,8\text{ m}^2").scale(1.1).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"12,8 \times 1,10 = 14,08\text{ m}^2 \;\text{(waste)}").scale(1.1).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"14,08 \div 2,5 = 5,63 \to 6\text{ boxes}").scale(1.1).shift(band_shift(4) + DOWN * 0.8)
        b4_l4 = MathTex(r"6 \times \text{R}429 = \text{R2 574}").scale(1.15).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l1)); self.wait(2)
        self.play(Write(b4_l2)); self.wait(2)
        self.play(Write(b4_l3)); self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        b4_note = Tex("Round UP whatever is sold in wholes").scale(1.0).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_note))
        self.wait(3)

        # --- Band 5 (subtopic_3): skirting — perimeter minus the door ---
        self.next_band(5)
        b5_title = Tex("Skirting is perimeter").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"2 \times (4,0 + 3,2) = 14,4\text{ m}").scale(1.1).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"14,4 - 0,9 = 13,5\text{ m} \;\text{(no door)}").scale(1.1).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"13,5 \div 3 = 4,5 \to 5\text{ lengths}").scale(1.1).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = MathTex(r"5 \times \text{R}95 = \text{R}475").scale(1.15).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.wait(2)
        self.play(Write(b5_l3)); self.wait(2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_3): paint — wall area, two coats, total ---
        self.next_band(6)
        b6_title = Tex("Paint is wall area").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"14,4 \times 2,5 = 36\text{ m}^2").scale(1.05).shift(band_shift(6) + UP * 1.2)
        b6_l2 = MathTex(r"36 - 1,8 - 1,8 = 32,4\text{ m}^2").scale(1.05).shift(band_shift(6) + UP * 0.4)
        b6_l3 = MathTex(r"\text{Two coats: } 32,4 \times 2 = 64,8\text{ m}^2").scale(1.05).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = MathTex(r"64,8 \div 9 = 7,2 \to \text{two 5-litre tins}").scale(1.05).shift(band_shift(6) + DOWN * 1.2)
        b6_l5 = MathTex(r"\text{Paint R}978; \;\; \text{total R4 027}").scale(1.1).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l1)); self.wait(2)
        self.play(Write(b6_l2)); self.wait(2)
        self.play(Write(b6_l3)); self.wait(2)
        self.play(Write(b6_l4)); self.wait(2)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): cans into boxes — counting, not dividing ---
        self.next_band(7)
        b7_title = Tex("Packing: count cans, don't divide volumes").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"\text{Length: } 48 \div 6 = 8\text{ cans}").scale(1.1).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{Width: } 30 \div 6 = 5 \;\Rightarrow\; 8 \times 5 = 40").scale(1.1).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"\text{Height: } 20 \div 10 = 2\text{ layers}").scale(1.1).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = MathTex(r"40 \times 2 = 80\text{ cans}").scale(1.15).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l1)); self.wait(2)
        self.play(Write(b7_l2)); self.wait(2)
        self.play(Write(b7_l3)); self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        b7_note = MathTex(r"23 \div 10 = 2,3 \to 2 \;\text{(round DOWN)}").scale(1.0).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_note))
        self.wait(3)

        # --- Band 8 (subtopic_4): wasted space and cardboard ---
        self.next_band(8)
        b8_title = Tex("How much of the box is air?").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"\text{Box: } 48 \times 30 \times 20 = 28\;800\text{ cm}^3").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"\text{Can: } 3,14 \times 3^2 \times 10 = 282,6").scale(1.05).shift(band_shift(8) + UP * 0.2)
        b8_l3 = MathTex(r"80 \times 282,6 = 22\;608\text{ cm}^3").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = MathTex(r"28\;800 - 22\;608 = 6\;192\text{ cm}^3").scale(1.05).shift(band_shift(8) + DOWN * 1.6)
        b8_l5 = Tex("Volume for what fits, surface area for what wraps").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l1)); self.wait(2)
        self.play(Write(b8_l2)); self.wait(2)
        self.play(Write(b8_l3)); self.wait(2)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b8_l5)); self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): the roof comes off ---
        self.next_band(9)
        b9_title = Tex("The roof comes off").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = Tex("Drone view: double lines are walls").scale(1.1).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("1 : 50 — halve it, then add two zeros").scale(1.1).shift(band_shift(9) + UP * 0.2)
        b9_l3 = MathTex(r"80\text{ mm} \to 4\;000\text{ mm} = 4,0\text{ m}").scale(1.1).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = MathTex(r"18\text{ mm} \to 900\text{ mm door}").scale(1.1).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l1)); self.wait(3)
        self.play(Write(b9_l2)); self.wait(3)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(3)
        self.play(Write(b9_l4)); self.wait(3)
        b9_l5 = Tex("Say WHICH lines you measured between").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l5)); self.wait(3.5)

        # --- Band 10 (subtopic_6): four faces of one house ---
        self.next_band(10)
        b10_title = Tex("Four faces of one house").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = Tex("Play detective: count openings first").scale(1.1).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("Then sizes by scale, then heights by sense").scale(1.1).shift(band_shift(10) + UP * 0.2)
        b10_l3 = Tex("Faces mirror: plan's west sits on your right").scale(1.05).shift(band_shift(10) + DOWN * 0.8)
        b10_l4 = Tex("Follow the chimney — landmarks name the face").scale(1.05).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l1)); self.wait(3)
        self.play(Write(b10_l2)); self.wait(3)
        self.play(Write(b10_l3)); self.wait(3.5)
        self.play(Write(b10_l4)); self.wait(3.5)

        # --- Band 11 (subtopic_7): buying the room ---
        self.next_band(11)
        b11_title = Tex("Buying the room: scale it, measure it, shop it").scale(1.05).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2.5)
        b11_l1 = MathTex(r"\text{Floor: } 5,63 \to 6\text{ boxes} = \text{R2 574}").scale(1.05).shift(band_shift(11) + UP * 1.1)
        b11_l2 = MathTex(r"\text{Skirting: } 4,5 \to 5\text{ lengths} = \text{R}475").scale(1.05).shift(band_shift(11) + UP * 0.2)
        b11_l3 = MathTex(r"\text{Paint: } 7,2 \to 2\text{ tins} = \text{R}978").scale(1.05).shift(band_shift(11) + DOWN * 0.8)
        b11_l4 = MathTex(r"\text{Total: R4 027 before labour}").scale(1.1).shift(band_shift(11) + DOWN * 1.8)
        self.play(Write(b11_l1)); self.wait(3)
        self.play(Write(b11_l2)); self.wait(3)
        self.play(Write(b11_l3)); self.wait(3)
        self.play(Write(b11_l4))
        self.play(Create(SurroundingRectangle(b11_l4, color=GREEN)))
        self.wait(3.5)

        # --- Band 12 (subtopic_7): packing the van ---
        self.next_band(12)
        b12_title = Tex("Packing the van: cans refuse to squash").scale(1.1).shift(band_shift(12) + UP * 2.2)
        self.play(Write(b12_title))
        self.wait(2.5)
        b12_l1 = MathTex(r"8 \times 5 = 40\text{, then } \times 2 = 80\text{ cans}").scale(1.1).shift(band_shift(12) + UP * 1.1)
        b12_l2 = Tex("Round DOWN per direction, then multiply").scale(1.1).shift(band_shift(12) + UP * 0.2)
        b12_l3 = MathTex(r"\text{Air: } 28\;800 - 22\;608 = 6\;192\text{ cm}^3").scale(1.05).shift(band_shift(12) + DOWN * 0.8)
        b12_l4 = Tex("Shopping rounds UP, packing rounds DOWN").scale(1.05).shift(band_shift(12) + DOWN * 1.8)
        self.play(Write(b12_l1))
        self.play(Create(SurroundingRectangle(b12_l1, color=GREEN)))
        self.wait(3)
        self.play(Write(b12_l2)); self.wait(3)
        self.play(Write(b12_l3)); self.wait(3)
        self.play(Write(b12_l4)); self.wait(4)
