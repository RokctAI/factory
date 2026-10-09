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

# Band-layout whiteboard scene for analysing-and-summarising-data (Part 1 Expert
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


class AnalysingAndSummarisingDataSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Asking Questions of the Data
        self.write_rows(0, "Asking Questions of the Data", [
            "Most: Maths 11",
            "Fewest: Social Sciences 3",
            "Maths or Natural Sciences: 20",
            "20 is more than half of 36",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Summarising Data in Words
        self.next_band(1)
        self.write_rows(1, "Summarising Data in Words", [
            "What the data is about",
            "Biggest and smallest with numbers",
            "One interesting fact",
            "Check every sentence",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Making Predictions
        self.next_band(2)
        self.write_rows(2, "Making Predictions", [
            "Friday busiest, so bake more Fridays",
            "Probably about 30 to 35",
            "Not a promise",
            "More data, better prediction",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Summary repeats every number''",
            "``The data says why''",
            "``Exactly 34 next Friday''",
            "``One week proves it''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Ask the Data
        self.next_band(4)
        self.write_rows(4, "Ask the Data", [
            "Most and fewest",
            "More: subtract",
            "Altogether: add",
            "Why? Needs more data",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Say It in Sentences
        self.next_band(5)
        self.write_rows(5, "Say It in Sentences", [
            "Few sentences",
            "Biggest and smallest",
            "Use the numbers",
            "Check every sentence",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): What Will Happen Next?
        self.next_band(6)
        self.write_rows(6, "What Will Happen Next?", [
            "Sensible guess from data",
            "Probably, about",
            "Things can change",
            "More data, stronger guess",
        ], scale=0.9, box=1)

        last = Tex("Ask the data questions, sum it up in a few checked sentences, and predict with probably and about.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
