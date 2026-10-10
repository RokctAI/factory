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

# Band-layout whiteboard scene for the-value-of-raw-materials-and-manufactured-goods (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (220/150/160/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TheValueOfRawMaterialsAndManufacturedGoodsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Adding Value
        self.write_rows(0, "Adding Value", [
            "Value: what something is worth",
            "Adding value",
            "Work, skills, machines, energy",
            "Everyone along the chain is paid",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Comparing Values
        self.next_band(1)
        self.write_rows(1, "Comparing Values", [
            "Wheat, flour, bread",
            "Wood, planks, table",
            "Iron ore, steel, car",
            "Raw material prices go up and down",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Why It Matters
        self.next_band(2)
        self.write_rows(2, "Why It Matters", [
            "Raw materials earn less",
            "Manufacturing creates jobs",
            "Process more at home",
            "Many exports are safer",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Raw materials are worth more''",
            "``The shop gets all the money''",
            "``Adding value means raising prices''",
            "``Where goods are made does not matter''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Each Step Adds
        self.next_band(4)
        self.write_rows(4, "Each Step Adds", [
            "Wash",
            "Cook",
            "Bottle",
            "Sell",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Cheap to Dear
        self.next_band(5)
        self.write_rows(5, "Cheap to Dear", [
            "Wheat",
            "Bread",
            "Wood",
            "Table",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Jobs Follow Value
        self.next_band(6)
        self.write_rows(6, "Jobs Follow Value", [
            "Jobs",
            "Money",
            "Skills",
            "Home",
        ], scale=0.9, box=0)

        last = Tex("Every step from raw material to finished product adds value, and the jobs and money stay where the value is added.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
