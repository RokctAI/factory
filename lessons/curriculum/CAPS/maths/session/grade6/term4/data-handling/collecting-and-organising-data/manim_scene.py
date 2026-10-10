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

# Band-layout whiteboard scene for collecting-and-organising-data (Part 1 Expert
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


class CollectingAndOrganisingDataSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Asking Questions and Collecting Data
        self.write_rows(0, "Asking Questions and Collecting Data", [
            "Data answers a question",
            "Survey, observation, records",
            "Clear, fair questions with choices",
            "Yes or no: simplest",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Tally Marks and Frequency Tables
        self.next_band(1)
        self.write_rows(1, "Tally Marks and Frequency Tables", [
            "Tally: four lines, fifth across",
            "Walk 15, taxi 9, bus 6, car 4, bicycle 2",
            "Total: 36 learners",
            "Breakfast: yes 27, no 9",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Organising and Ordering Data
        self.next_band(2)
        self.write_rows(2, "Organising and Ordering Data", [
            "Smallest to largest",
            "Bicycle, car, bus, taxi, walk",
            "Intervals: 0 to 9, 10 to 19, 20 to 29",
            "No overlaps",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Five upright lines''",
            "``Total not checked''",
            "``Soccer is the best, isn't it?''",
            "``0 to 10, 10 to 20''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Ask a Clear Question
        self.next_band(4)
        self.write_rows(4, "Ask a Clear Question", [
            "Ask a clear question",
            "Give choices",
            "Do not push",
            "Ask once each",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Tally in Fives
        self.next_band(5)
        self.write_rows(5, "Tally in Fives", [
            "Tally in fives",
            "Four lines, one across",
            "Check the total",
            "36",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Put It in Order
        self.next_band(6)
        self.write_rows(6, "Put It in Order", [
            "Put it in order",
            "Smallest first",
            "Largest last",
            "Walk wins",
        ], scale=0.9, box=1)

        last = Tex("Ask a clear question, tally in fives, check the total, then order the groups from smallest to largest.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
