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
        # --- Band 0 (subtopic_1): Sharing Money and Measurement
        self.write_rows(0, "Sharing Money and Measurement", [
            "R936 among 8: 936 divided by 8",
            "800 plus 136: 100 plus 17 is 117",
            "684 metres in 6s: 114 gaps",
            "What kind of thing is the answer?",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): What the Remainder Means
        self.next_band(1)
        self.write_rows(1, "What the Remainder Means", [
            "125 divided by 15 is 8 remainder 5",
            "Minibuses for everyone: round up to 9",
            "Full bags for sale: round down to 8",
            "What is left over? Report 5",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Rate and Ratio by Division
        self.next_band(2)
        self.write_rows(2, "Rate and Ratio by Division", [
            "480 km in 6 hours: 80 km per hour",
            "R280 for 8 boxes: R35 per box",
            "24 to 16 simplifies to 3 to 2",
            "R100 in 3 to 2: R60 and R40",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``8 minibuses is enough''",
            "``The leftover sweets make a bag''",
            "``Divide one side of the ratio''",
            "``3 to 2 of R100 is R30 and R20''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Share It Out
        self.next_band(4)
        self.write_rows(4, "Share It Out", [
            "Shared equally: divide",
            "936 divided by 8 is 117",
            "684 divided by 6 is 114",
            "Rands, or a count?",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): What Happens to the Leftover
        self.next_band(5)
        self.write_rows(5, "What Happens to the Leftover", [
            "8 remainder 5",
            "Everyone must go: 9 buses",
            "Full bags only: 8",
            "Read the question again",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Per One, and Fair Shares
        self.next_band(6)
        self.write_rows(6, "Per One, and Fair Shares", [
            "480 divided by 6: 80 per hour",
            "280 divided by 8: R35 per box",
            "Divide both parts: 3 to 2",
            "5 parts of R20: R60 and R40",
        ], scale=0.9, box=0)

        last = Tex("Divide to share or group, read the story for the remainder, and divide to find a rate or simplify a ratio.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
