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

# Band-layout whiteboard scene for who-uses-south-africas-water (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/160/180/170/90/90/90 of 970 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class WhoUsesSouthAfricasWaterSession(MovingCameraScene):
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
        # --- Band 0: Reading and Drawing a Pie Chart
        self.write_rows(0, "Reading and Drawing a Pie Chart", [
            "Whole circle: 100 percent, 360 degrees",
            "Angle = percentage x 3.6",
            "50 percent = 180 degrees",
            "Title, key, labels and source",
        ], scale=0.86, box=1)
        # --- Band 1: South Africa's Water Users
        self.next_band(1)
        self.write_rows(1, "South Africa's Water Users", [
            "Irrigation: about 60 percent",
            "Municipal: about 27 percent",
            "Industry, mining, power: about 8 percent",
            "Forestry and livestock: about 5 percent",
        ], scale=0.86, box=2)
        # --- Band 2: Comparing the Users
        self.next_band(2)
        self.write_rows(2, "Comparing the Users", [
            "Irrigation: food, jobs, exports",
            "Drip irrigation saves water",
            "Free Basic Water: 6000 litres a month",
            "Municipal losses about 40 percent",
        ], scale=0.86, box=2)
        # --- Band 3: Sharing Water Fairly and Wisely
        self.next_band(3)
        self.write_rows(3, "Sharing Water Fairly and Wisely", [
            "1998 National Water Act: water belongs to all",
            "Reserve: basic human needs and ecology",
            "Other users need a licence",
            "Fix leaks, reuse, harvest rain",
        ], scale=0.8, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Pie Charts
        self.next_band(4)
        self.write_rows(4, "Pie Charts", [
            "Whole circle: 100 percent",
            "Bigger slice: bigger share",
            "Half = 180 degrees",
        ], scale=0.86, box=0)
        # --- Band 5: Who Uses the Water?
        self.next_band(5)
        self.write_rows(5, "Who Uses the Water?", [
            "Farming: about 60 percent",
            "Towns and cities: about 27 percent",
            "Others: the rest",
        ], scale=0.86, box=0)
        # --- Band 6: Sharing and Saving
        self.next_band(6)
        self.write_rows(6, "Sharing and Saving", [
            "Water belongs to everyone",
            "Basic needs and rivers first",
            "Fix leaks, short showers",
        ], scale=0.86, box=0)
        self.wait(4)
