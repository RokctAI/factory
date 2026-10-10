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

# Band-layout whiteboard scene for revision-of-term-3-topics (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/160/160/110/110/110 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RevisionOfTerm3TopicsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): 3D Objects and Data
        self.write_rows(0, "3D Objects and Data", [
            "Gift box: rectangular prism",
            "Tin: cylinder, tent: pyramid",
            "Votes: food 15, games 11",
            "Crafts 8, books 6: total 40",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Probability and Length
        self.next_band(1)
        self.write_rows(1, "Probability and Length", [
            "Spinner: 4 equal outcomes",
            "20 spins: 6, 4, 5, 5",
            "1 and 1/2 km is 1 500 m",
            "400 cm divided by 50 is 8",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Perimeter, Area and Volume
        self.next_band(2)
        self.write_rows(2, "Perimeter, Area and Volume", [
            "Cloth 2 m by 1 m: 6 m around",
            "Design 6 by 4: 24 squares",
            "Flag: 3 whole, 2 halves: 4",
            "Box: 6 in a layer, 2 layers: 12",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A tin is a circle''",
            "``Half a star as a whole''",
            "``1 and 1/2 km is 150 m''",
            "``Area of 6 by 4 is 20''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Prizes and Votes
        self.next_band(4)
        self.write_rows(4, "Prizes and Votes", [
            "Prizes and votes",
            "Box, tin, tent",
            "Total votes: 40",
            "Mode: food",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Spin and Measure
        self.next_band(5)
        self.write_rows(5, "Spin and Measure", [
            "Spin and measure",
            "4 outcomes",
            "1 500 m fun walk",
            "8 rosettes",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Around, Inside and Filling
        self.next_band(6)
        self.write_rows(6, "Around, Inside and Filling", [
            "Around, inside, filling",
            "6 m around",
            "24 squares inside",
            "12 cubes filling",
        ], scale=0.9, box=1)

        last = Tex("3D objects, data, chance, length, perimeter, area and volume: look carefully, count well, and use the right unit every time.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
