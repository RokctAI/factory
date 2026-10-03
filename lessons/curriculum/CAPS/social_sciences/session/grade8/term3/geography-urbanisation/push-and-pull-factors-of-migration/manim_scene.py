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

# Band-layout whiteboard scene for push-and-pull-factors-of-migration (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (300/240/290/230/130/130/130 of 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class PushAndPullFactorsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.1).shift(band_shift(k) + UP * 2.4)
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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0: Urbanisation and migration
        self.write_rows(0, "Urbanisation and migration", [
            "Urban share rises",
            "Natural increase and migration",
            "Internal and international",
            "SA: about two-thirds urban",
        ], scale=0.86, box=0)
        # --- Band 1: Push factors
        self.next_band(1)
        self.write_rows(1, "Push factors", [
            "No jobs, low incomes",
            "Small plots, drought",
            "Few schools and clinics",
            "Conflict and disasters",
        ], scale=0.86, box=0)
        # --- Band 2: Pull factors
        self.next_band(2)
        self.write_rows(2, "Pull factors", [
            "Jobs and higher pay",
            "Education and services",
            "Chain migration",
            "Remittances home",
        ], scale=0.86, box=2)
        # --- Band 3: Measuring urbanisation
        self.next_band(3)
        self.write_rows(3, "Measuring urbanisation", [
            "6 $\\div$ 12 = 0.5, so 50 per cent",
            "Gauteng: 15.1 of 62.0 million",
            "About 24 per cent",
            "Push at home, pull in city",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Why people move
        self.next_band(4)
        self.write_rows(4, "Why people move", [
            "A scale with two pans",
        ], scale=0.86, box=0)
        # --- Band 5: Pushed away
        self.next_band(5)
        self.write_rows(5, "Pushed away", [
            "Many reasons together",
        ], scale=0.86, box=0)
        # --- Band 6: Pulled to the city
        self.next_band(6)
        self.write_rows(6, "Pulled to the city", [
            "Jobs, schools, family",
        ], scale=0.86, box=0)
        self.wait(4)
