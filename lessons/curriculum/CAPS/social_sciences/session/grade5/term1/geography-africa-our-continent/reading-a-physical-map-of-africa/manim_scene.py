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

# Band-layout whiteboard scene for reading-a-physical-map-of-africa (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/170/210/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ReadingAPhysicalMapOfAfricaSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Political and Physical Maps
        self.write_rows(0, "Political and Physical Maps", [
            "Political map: countries",
            "Physical map: natural features",
            "Mountains, rivers, lakes",
            "Read the title first",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Sea Level and Height
        self.next_band(1)
        self.write_rows(1, "Sea Level and Height", [
            "Sea level: zero metres",
            "Height above sea level",
            "Spot height: 5895",
            "Higher is usually colder",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Colours, Rivers and Lakes
        self.next_band(2)
        self.write_rows(2, "Colours, Rivers and Lakes", [
            "Colours show height",
            "Green low, brown high",
            "Rivers: blue lines",
            "Lakes: blue shapes",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Physical maps show countries''",
            "``Height from your feet''",
            "``Green means grass''",
            "``Rivers flow uphill''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Two Kinds of Map
        self.next_band(4)
        self.write_rows(4, "Two Kinds of Map", [
            "Political",
            "Countries",
            "Physical",
            "Land",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): How High?
        self.next_band(5)
        self.write_rows(5, "How High?", [
            "Sea level",
            "Zero metres",
            "Above sea level",
            "Metres",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Green Low, Brown High
        self.next_band(6)
        self.write_rows(6, "Green Low, Brown High", [
            "Green: low",
            "Yellow: higher",
            "Brown: highest",
            "Blue: water",
        ], scale=0.9, box=0)

        last = Tex("A physical map uses colours to show height above sea level, with rivers and lakes in blue.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
