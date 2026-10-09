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

# Band-layout whiteboard scene for division-problems-sharing-and-remainders (Part 1 Expert
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


class DivisionProblemsSharingAndRemaindersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Sharing and Grouping Problems
        self.write_rows(0, "Sharing and Grouping Problems", [
            "Sharing: R675 for 15 is R45 each",
            "Grouping: 350 rolls in packs of 12",
            "350 divided by 12 is 29 remainder 2",
            "900 cm in 35 cm pieces: 25, 25 cm left",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): What to Do with the Remainder
        self.next_band(1)
        self.write_rows(1, "What to Do with the Remainder", [
            "500 learners, 32 seats: 15 remainder 20",
            "Everyone needs a seat: 16 buses",
            "Only full packs: 29 packs",
            "Money left over: change it and share",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Rates, Ratios and Money with Division
        self.next_band(2)
        self.write_rows(2, "Rates, Ratios and Money with Division", [
            "540 km at 12 km per litre: 45 litres",
            "24 pens for R192: R8 each",
            "Ratio 1 to 2 of 72: 3 parts of 24",
            "Naledi 24, Sipho 48",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``15 buses for 500 learners''",
            "``30 full packs of rolls''",
            "``15 divided by 675''",
            "``1 to 2 of 72 is 36 and 36''",
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
            "Sharing: how much in each group",
            "Grouping: how many groups",
            "R675 for 15: R45 each",
            "350 rolls: 29 packs of 12",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Up, Down or Left Over
        self.next_band(5)
        self.write_rows(5, "Up, Down or Left Over", [
            "Read the question again",
            "Seats for all: round up",
            "Full packs only: round down",
            "Left over: the remainder is the answer",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Price for One
        self.next_band(6)
        self.write_rows(6, "Price for One", [
            "Price for one: divide",
            "R192 for 24 pens: R8",
            "1 to 2 means 3 parts",
            "72 divided by 3 is 24",
        ], scale=0.9, box=2)

        last = Tex("Divide, then read the question again to decide what the remainder means.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
