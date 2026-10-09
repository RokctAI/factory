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

# Band-layout whiteboard scene for measuring-and-recording-length (Part 1 Expert
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


class MeasuringAndRecordingLengthSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Units and Tools
        self.write_rows(0, "Units and Tools", [
            "mm, cm, m and km",
            "Ruler: short things",
            "Tape measure: curves",
            "Trundle wheel: 1 m per click",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Estimating and Measuring
        self.next_band(1)
        self.write_rows(1, "Estimating and Measuring", [
            "Estimate first: desk about 120 cm",
            "Start at the 0 mark",
            "12 cm 4 mm is 124 mm",
            "Book: 297 mm by 210 mm",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Recording, Comparing and Ordering
        self.next_band(2)
        self.write_rows(2, "Recording, Comparing and Ordering", [
            "1 m 98 cm, 2 m 8 cm",
            "2 m 35 cm, 2 m 50 cm",
            "198, 208, 235, 250 cm",
            "Always write the unit",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Starting at the ruler edge''",
            "``2 m 8 cm beats 2 m 35 cm''",
            "``124 with no unit''",
            "``A ruler for the school field''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Pick the Unit, Pick the Tool
        self.next_band(4)
        self.write_rows(4, "Pick the Unit, Pick the Tool", [
            "Pick the unit",
            "mm, cm, m, km",
            "Pick the tool",
            "Ruler to trundle wheel",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Guess, Then Measure
        self.next_band(5)
        self.write_rows(5, "Guess, Then Measure", [
            "Guess, then measure",
            "Start at zero",
            "12 cm 4 mm",
            "124 mm",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Line Them Up
        self.next_band(6)
        self.write_rows(6, "Line Them Up", [
            "Line them up",
            "Metres first",
            "Then centimetres",
            "Shortest: 1 m 98 cm",
        ], scale=0.9, box=2)

        last = Tex("Choose the unit and the tool, estimate first, start at zero, write the unit, and compare the biggest units first.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
