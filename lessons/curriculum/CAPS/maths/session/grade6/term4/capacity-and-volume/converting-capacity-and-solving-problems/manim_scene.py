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

# Band-layout whiteboard scene for converting-capacity-and-solving-problems (Part 1 Expert
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


class ConvertingCapacityAndSolvingProblemsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Bigger Units to Smaller Units
        self.write_rows(0, "Bigger Units to Smaller Units", [
            "1 l = 1 000 ml; 1 kl = 1 000 l",
            "1,5 l = 1 500 ml",
            "3/4 l = 750 ml",
            "5 kl = 5 000 l",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Smaller Units to Bigger Units
        self.next_band(1)
        self.write_rows(1, "Smaller Units to Bigger Units", [
            "2 500 ml = 2,5 l",
            "330 ml = 0,33 l",
            "7 500 l = 7,5 kl",
            "600 l = 3/5 kl",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Solving Water Problems
        self.next_band(2)
        self.write_rows(2, "Solving Water Problems", [
            "5 000 l divided by 1 000 l = 5 days",
            "1 500 ml divided by 250 ml = 6 cups",
            "Tap: 5 l times 24 = 120 l a day",
            "Shower 36 l, bath 150 l: save 114 l",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``1,5 l = 150 ml''",
            "``2 500 ml = 25 l''",
            "``3/4 l = 75 ml''",
            "``2 l + 500 ml = 502''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Big to Small: Multiply
        self.next_band(4)
        self.write_rows(4, "Big to Small: Multiply", [
            "Big to small",
            "Multiply by 1 000",
            "1,5 l is 1 500 ml",
            "5 kl is 5 000 l",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Small to Big: Divide
        self.next_band(5)
        self.write_rows(5, "Small to Big: Divide", [
            "Small to big",
            "Divide by 1 000",
            "2 500 ml is 2,5 l",
            "330 ml is 0,33 l",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Save Water
        self.next_band(6)
        self.write_rows(6, "Save Water", [
            "Save water",
            "Tank lasts 5 days",
            "Shower, not bath",
            "114 l saved",
        ], scale=0.9, box=3)

        last = Tex("1 000 ml make 1 litre and 1 000 litres make 1 kilolitre: multiply to go smaller, divide to go bigger.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
