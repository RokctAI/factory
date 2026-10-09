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

# Band-layout whiteboard scene for multiples-and-factors (Part 1 Expert
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


class MultiplesAndFactorsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Multiples of Two-Digit Numbers
        self.write_rows(0, "Multiples of Two-Digit Numbers", [
            "Multiples: skip-count",
            "Multiples of 12: 12, 24, 36, 48, 60",
            "Multiples of 15: 15, 30, 45, 60, 75, 90",
            "84 is 12 times 7",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Factors of Numbers to 100
        self.next_band(1)
        self.write_rows(1, "Factors of Numbers to 100", [
            "Factors divide in exactly",
            "Find them in pairs",
            "1 and 48, 2 and 24, 3 and 16",
            "4 and 12, 6 and 8",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Common Multiples and Common Factors
        self.next_band(2)
        self.write_rows(2, "Common Multiples and Common Factors", [
            "Packs of 12 and packs of 18",
            "First common multiple: 36",
            "Common factors of 48 and 72",
            "Highest common factor: 24",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``4 is a multiple of 48''",
            "``Factors of 48: 2, 4, 6, 8''",
            "``The number is not its own factor''",
            "``Smallest common multiple: 12 times 18''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Up the Times Table
        self.next_band(4)
        self.write_rows(4, "Up the Times Table", [
            "Multiples go up the times table",
            "12, 24, 36, 48, 60, 72, 84, 96",
            "15, 30, 45, 60, 75, 90",
            "84 is in the 12 times table",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Pairs That Fit
        self.next_band(5)
        self.write_rows(5, "Pairs That Fit", [
            "Factors go into the number",
            "Find them in pairs",
            "48: 1, 2, 3, 4, 6, 8, 12, 16, 24, 48",
            "Stop when the pairs meet",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): When Things Match
        self.next_band(6)
        self.write_rows(6, "When Things Match", [
            "Same number of juices and muffins",
            "First match: 36",
            "3 packs of 12, 2 packs of 18",
            "24 teams: 2 boys and 3 girls each",
        ], scale=0.9, box=1)

        last = Tex("Multiples go up by skip-counting, factors come in pairs that divide exactly, and the first match is the smallest common multiple.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
