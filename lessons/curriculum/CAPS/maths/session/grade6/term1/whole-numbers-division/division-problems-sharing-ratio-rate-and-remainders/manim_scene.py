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

# Band-layout whiteboard scene for division-problems-sharing-ratio-rate-and-remainders (Part 1 Expert
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


class DivisionProblemsSharingRatioRateAndRemaindersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Equal Sharing and Grouping with Remainders
        self.write_rows(0, "Equal Sharing and Grouping with Remainders", [
            "Sharing: how many in each?",
            "Grouping: how many groups?",
            "1 350 divided by 65 = 20 remainder 50",
            "Book 21 buses",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Division in Money and Measurement
        self.next_band(1)
        self.write_rows(1, "Division in Money and Measurement", [
            "Share the cost: R4 680 divided by 12 = R390",
            "Unit price: R1 008 divided by 144 = R7",
            "6 for R54 is R9 each",
            "4 for R40 is R10 each",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Ratio and Rate with Division
        self.next_band(2)
        self.write_rows(2, "Ratio and Rate with Division", [
            "Ratio 1 : 3 has 4 parts",
            "R2 400 divided by 4 = R600",
            "R600 and R1 800",
            "450 km in 5 hours = 90 km per hour",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``20 buses for 1 350 learners''",
            "``R2 400 in the ratio 1 : 3 divided by 3''",
            "``Remainder bigger than the divisor''",
            "``One pen costs R144''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Share or Group
        self.next_band(4)
        self.write_rows(4, "Share or Group", [
            "Share or group",
            "20 remainder 50",
            "Nobody left behind",
            "21 buses",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Rand and Metres
        self.next_band(5)
        self.write_rows(5, "Rand and Metres", [
            "Price of one",
            "R7 a pen",
            "R9 a juice",
            "20 pieces of rope",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Per Unit
        self.next_band(6)
        self.write_rows(6, "Per Unit", [
            "Add the parts: 4",
            "R600 a part",
            "90 km per hour",
            "63 litres of petrol",
        ], scale=0.9, box=0)

        last = Tex("Divide to share or to group, let the story decide the remainder, add the parts for a ratio and divide to find a rate.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
