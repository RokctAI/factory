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

# Band-layout whiteboard scene for creating-sustainable-job-opportunities (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-5). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (170/180/190/120/110 of 770 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CreatingSustainableJobOpportunitiesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.78, box=None):
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
            self.play(Create(SurroundingRectangle(made[box], color=YELLOW)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1)
        self.write_rows(0, "Sustainable jobs", [
            "Lasts over time",
            "Pays a fair, decent income",
            "Safe working conditions",
            "Does not harm environment or community",
        ], box=0)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Small businesses", [
            "SMMEs: small, medium, micro enterprises",
            "Informal sector: spaza, street trade",
            "Need finance, skills, markets",
            "Government and banks support SMMEs",
        ], box=0)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Partners and green jobs", [
            "Government: growth, infrastructure, skills",
            "Business: invest and employ",
            "Community: buy local, cooperatives",
            "Green jobs: solar, recycling, water",
        ], box=3)


        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Bongani's car wash", [
            "Starts alone with a bucket",
            "Saves, buys a pressure washer",
            "Hires two friends: jobs created",
            "Uses recycled water: green and lasting",
        ], box=2)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Who helps create jobs?", [
            "Government: roads, power, skills",
            "Big business: invest, buy local",
            "Community: support local shops",
            "You: skills and your own ideas",
        ], box=3)

        self.wait(4)
