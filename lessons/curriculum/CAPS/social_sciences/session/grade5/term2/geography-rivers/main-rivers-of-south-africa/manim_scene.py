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

# Band-layout whiteboard scene for main-rivers-of-south-africa (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/130/210/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MainRiversOfSouthAfricaSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.15).shift(band_shift(k) + UP * 2.4)
        self.play(Write(t))
        self.wait(1.5)
        made = []
        for i, r in enumerate(rows):
            m = Tex(r).scale(scale).shift(band_shift(k) + UP * (1.3 - 0.95 * i))
            self.play(Write(m))
            self.wait(2.3)
            made.append(m)
        if box is not None:
            self.play(Create(SurroundingRectangle(made[box], color=box_color)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(42)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Rivers Flowing West
        self.write_rows(0, "Rivers Flowing West", [
            "Gariep: longest, from Lesotho",
            "Tributaries: Caledon, Vaal",
            "Mouth: Alexander Bay",
            "Berg: to St Helena Bay",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Rivers Flowing East and South
        self.next_band(1)
        self.write_rows(1, "Rivers Flowing East and South", [
            "Thukela: Drakensberg to the east",
            "uMngeni and uMsunduzi",
            "Mzimvubu, Great Fish",
            "Breede: to Witsand",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): The Limpopo and Reading the Map
        self.next_band(2)
        self.write_rows(2, "The Limpopo and Reading the Map", [
            "Limpopo: northern border",
            "Flows east to the Indian Ocean",
            "Escarpment: the main watershed",
            "East short, west long",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``The Vaal reaches the sea''",
            "``The Gariep starts in SA''",
            "``Limpopo to the Atlantic''",
            "``East rivers are long''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): West to the Atlantic
        self.next_band(4)
        self.write_rows(4, "West to the Atlantic", [
            "Gariep",
            "West",
            "Vaal",
            "Atlantic",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): East to the Indian Ocean
        self.next_band(5)
        self.write_rows(5, "East to the Indian Ocean", [
            "Thukela",
            "East",
            "Short",
            "Indian Ocean",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): The Northern Border
        self.next_band(6)
        self.write_rows(6, "The Northern Border", [
            "Limpopo",
            "North",
            "East",
            "Border",
        ], scale=0.9, box=0)

        last = Tex("South Africa's main rivers flow east to the Indian Ocean or west to the Atlantic, divided by the escarpment.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
