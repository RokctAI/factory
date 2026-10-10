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

# Band-layout whiteboard scene for revision-of-term-4-and-year-fundamentals (Part 1 Expert
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


class RevisionOfTerm4AndYearFundamentalsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Mass, Capacity and Time
        self.write_rows(0, "Mass, Capacity and Time", [
            "2,5 kg is 2 500 g",
            "20 000 ml in 200 ml cups: 100 cups",
            "08:45 to 14:15: 5 hours 30 minutes",
            "1 minute 25 seconds is 85 seconds",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Data Handling
        self.next_band(1)
        self.write_rows(1, "Data Handling", [
            "Votes: 10, 16, 8 and 6 make 40",
            "Sack race: 16 of 40 is 40 per cent",
            "In order: 12, 14, 15, 16, 18, 18, 20",
            "Median 16, mode 18",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Number Fundamentals
        self.next_band(2)
        self.write_rows(2, "Number Fundamentals", [
            "R12 485 to the nearest 1 000: R12 000",
            "R12 485 minus R4 790 is R7 695",
            "One fifth of R7 695 is R1 539",
            "One fifth is 0,2 or 20 per cent",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``2,5 kg as 250 g''",
            "``08:45 to 14:15 as 5 hours 70 minutes''",
            "``Median of the unordered times: 15''",
            "``R12 485 rounded to R13 000''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Weigh, Pour and Time
        self.next_band(4)
        self.write_rows(4, "Weigh, Pour and Time", [
            "Weigh, pour and time",
            "Times 1 000 for grams",
            "Times 1 000 for millilitres",
            "Count on for time",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Read the Data
        self.next_band(5)
        self.write_rows(5, "Read the Data", [
            "Read the data",
            "Tally and total",
            "Order the data",
            "Median 16",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Number Know-How
        self.next_band(6)
        self.write_rows(6, "Number Know-How", [
            "Number know-how",
            "Round with place value",
            "Check with inverses",
            "Write the unit",
        ], scale=0.9, box=3)

        last = Tex("Know the key facts, use a clear method, check with the inverse, and always write the unit.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
