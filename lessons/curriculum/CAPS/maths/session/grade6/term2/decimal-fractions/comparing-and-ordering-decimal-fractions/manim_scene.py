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

# Band-layout whiteboard scene for comparing-and-ordering-decimal-fractions (Part 1 Expert
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


class ComparingAndOrderingDecimalFractionsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Comparing Decimals by Place Value
        self.write_rows(0, "Comparing Decimals by Place Value", [
            "Wholes first, then tenths, then hundredths",
            "34,98 is less than 35,09",
            "35,09 is less than 35,4",
            "0,5 is 0,50 so it beats 0,25",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Ordering Decimals
        self.next_band(1)
        self.write_rows(1, "Ordering Decimals", [
            "Line up the commas, fill with zeros",
            "34,98; 35,09; 35,40; 36,10",
            "Smallest time is fastest",
            "Biggest to smallest: 2,5; 2,45; 2,05",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Number Lines and Rounding Decimals
        self.next_band(2)
        self.write_rows(2, "Number Lines and Rounding Decimals", [
            "Nearest whole: look at the tenths",
            "Nearest tenth: look at the hundredths",
            "5 or more: round up",
            "3,68 rounds to 3,7 and to 4",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``0,25 is bigger than 0,5''",
            "``3,09 is bigger than 3,1''",
            "``4,70 is bigger than 4,7''",
            "``2,45 rounds to 2,4''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Which Is Bigger?
        self.next_band(4)
        self.write_rows(4, "Which Is Bigger?", [
            "Which is bigger?",
            "Start on the left",
            "Wholes, tenths, hundredths",
            "0,5 beats 0,25",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Line Them Up
        self.next_band(5)
        self.write_rows(5, "Line Them Up", [
            "Line them up",
            "Commas under commas",
            "Fill gaps with zeros",
            "Smallest time wins",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Round to the Nearest
        self.next_band(6)
        self.write_rows(6, "Round to the Nearest", [
            "Round to the nearest",
            "Whole: look at tenths",
            "Tenth: look at hundredths",
            "5 or more, round up",
        ], scale=0.9, box=3)

        last = Tex("Compare decimals from the left, one place at a time: more digits does not mean a bigger number.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
