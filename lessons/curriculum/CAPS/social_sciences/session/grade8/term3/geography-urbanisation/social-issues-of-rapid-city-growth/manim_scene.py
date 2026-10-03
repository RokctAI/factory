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

# Band-layout whiteboard scene for social-issues-of-rapid-city-growth (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (290/280/250/220/130/130/130 of 1430 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SocialIssuesOfCityGrowthSession(MovingCameraScene):
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
        # --- Band 0: The housing challenge
        self.write_rows(0, "The housing challenge", [
            "Informal settlements",
            "Floods and fires",
            "Housing backlog",
            "Upgrade in place",
        ], scale=0.86, box=3)
        # --- Band 1: Basic services
        self.next_band(1)
        self.write_rows(1, "Basic services", [
            "Water: shared standpipes",
            "Sanitation and disease",
            "Electricity and paraffin",
            "Refuse removal",
        ], scale=0.86, box=1)
        # --- Band 2: Health and education
        self.next_band(2)
        self.write_rows(2, "Health and education", [
            "TB in crowded homes",
            "Overcrowded clinics",
            "Crowded classrooms",
            "Mobile clinics, school meals",
        ], scale=0.86, box=0)
        # --- Band 3: Measuring pressure
        self.next_band(3)
        self.write_rows(3, "Measuring pressure", [
            "1 500 $\\div$ 30 = 50 per class",
            "30 000 $\\div$ 5 = 6 000 per nurse",
            "Map access",
            "Opportunity and challenge",
        ], scale=0.86, box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Too many, too fast
        self.next_band(4)
        self.write_rows(4, "Too many, too fast", [
            "Not enough houses",
        ], scale=0.86, box=0)
        # --- Band 5: Water, toilets and power
        self.next_band(5)
        self.write_rows(5, "Water, toilets and power", [
            "One tap, many families",
        ], scale=0.86, box=0)
        # --- Band 6: Clinics and classrooms
        self.next_band(6)
        self.write_rows(6, "Clinics and classrooms", [
            "Queues and crowded rooms",
        ], scale=0.86, box=0)
        self.wait(4)
