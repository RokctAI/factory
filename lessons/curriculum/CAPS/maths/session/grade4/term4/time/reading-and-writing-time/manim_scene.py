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

# Band-layout whiteboard scene for reading-and-writing-time (Part 1 Expert
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


class ReadingAndWritingTimeSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Reading Analogue and Digital Clocks
        self.write_rows(0, "Reading Analogue and Digital Clocks", [
            "Short hand: hours, long hand: minutes",
            "Count minutes in fives",
            "2 marks past the 4: 22 minutes",
            "6:45 is a quarter to seven",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): The 12-Hour Way: a.m. and p.m.
        self.next_band(1)
        self.write_rows(1, "The 12-Hour Way: a.m. and p.m.", [
            "24 hours, clock shows 12",
            "a.m.: midnight to midday",
            "p.m.: midday to midnight",
            "12 noon and 12 midnight",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): The 24-Hour Way
        self.next_band(2)
        self.write_rows(2, "The 24-Hour Way", [
            "Hours numbered 00 to 23",
            "1:30 p.m. is 13:30",
            "15:45 is 3:45 p.m.",
            "Midnight is 00:00",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Hour hand nearly at 7: say 7''",
            "``Minute hand on 9: 9 minutes''",
            "``1:30 p.m. is 01:30''",
            "``15:45 is 5:45 p.m.''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Hands and Numbers
        self.next_band(4)
        self.write_rows(4, "Hands and Numbers", [
            "Short hand: hours",
            "Long hand: minutes in fives",
            "6:15 is a quarter past six",
            "6:45 is a quarter to seven",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Morning or Evening
        self.next_band(5)
        self.write_rows(5, "Morning or Evening", [
            "Clock goes round twice",
            "a.m.: night and morning",
            "p.m.: afternoon and evening",
            "Noon and midnight",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Twenty-Four Hours
        self.next_band(6)
        self.write_rows(6, "Twenty-Four Hours", [
            "00 to 23",
            "p.m.: add 12",
            "13:30 is 1:30 p.m.",
            "20:30 is 8:30 p.m.",
        ], scale=0.9, box=1)

        last = Tex("Short hand for hours, long hand for minutes in fives; a.m. or p.m., or add 12 for the 24-hour way.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
