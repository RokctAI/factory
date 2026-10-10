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

# Band-layout whiteboard scene for trade-across-africa-and-the-indian-ocean (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/130/160/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TradeAcrossAfricaAndTheIndianOceanSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): A Network Across the Ocean
        self.write_rows(0, "A Network Across the Ocean", [
            "East African trading towns",
            "Sofala, Kilwa, Mombasa",
            "Dhows with triangular sails",
            "Monsoon winds",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Goods Out and Goods In
        self.next_band(1)
        self.write_rows(1, "Goods Out and Goods In", [
            "Out: gold and ivory",
            "In: glass beads and cloth",
            "Chinese porcelain found",
            "The king controlled trade",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Journeys on Foot and Globalisation
        self.next_band(2)
        self.write_rows(2, "Journeys on Foot and Globalisation", [
            "No wheels, no pack animals",
            "Porters on foot",
            "Weeks to the coast",
            "An early globalisation",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Goods went in wagons''",
            "``Only traded with neighbours''",
            "``Beads were made from local sand''",
            "``Globalisation is only modern''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Ships and Winds
        self.next_band(4)
        self.write_rows(4, "Ships and Winds", [
            "Dhows",
            "Winds",
            "Coast",
            "Sofala",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Out and In
        self.next_band(5)
        self.write_rows(5, "Out and In", [
            "Gold",
            "Ivory",
            "Beads",
            "Cloth",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): On Foot
        self.next_band(6)
        self.write_rows(6, "On Foot", [
            "Porters",
            "Paths",
            "Weeks",
            "Linked",
        ], scale=0.9, box=0)

        last = Tex("Gold and ivory walked to the coast, and beads and cloth sailed back: Mapungubwe was linked to the wider world.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
