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

# Band-layout whiteboard scene for underground-railroad-and-harriet-tubman (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/190/190/230/90/90/120 of 1100 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class UndergroundRailroadAndHarrietTubmanSession(MovingCameraScene):
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
        # --- Band 0: Escaping to Freedom
        self.write_rows(0, "Escaping to Freedom", [
            "North and Canada meant freedom",
            "On foot, at night, hunted by slave catchers",
            "Follow the North Star",
            "Douglass 1838; Henry Box Brown 1849",
        ], scale=0.86, box=1)
        # --- Band 1: How the Underground Railroad Worked
        self.next_band(1)
        self.write_rows(1, "How the Underground Railroad Worked", [
            "Not underground, not a railroad: a secret network",
            "Conductors, stations, passengers",
            "Free Black communities did much of the work",
            "William Still kept records; Quaker allies",
        ], scale=0.8, box=2)
        # --- Band 2: Harriet Tubman's Escape
        self.next_band(2)
        self.write_rows(2, "Harriet Tubman's Escape", [
            "Born about 1822 in Maryland as Araminta Ross",
            "Head injury; faith and visions",
            "Escaped to Pennsylvania, 1849",
            "Free, but her family was not",
        ], scale=0.86, box=2)
        # --- Band 3: Moses of Her People
        self.next_band(3)
        self.write_rows(3, "Moses of Her People", [
            "About 13 trips; about 70 people led to freedom",
            "Winter nights, Saturday starts, disguises",
            "1850 Fugitive Slave Act: on to Canada",
            "1863 Combahee River Raid: over 700 freed",
        ], scale=0.8, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Running North
        self.next_band(4)
        self.write_rows(4, "Running North", [
            "North and Canada: no slavery",
            "Walking at night, hunted",
            "Follow the North Star",
        ], scale=0.86, box=0)
        # --- Band 5: A Secret Network
        self.next_band(5)
        self.write_rows(5, "A Secret Network", [
            "Not under the ground, not a railway",
            "Conductors, stations, passengers",
            "Free Black people and Quakers helped",
        ], scale=0.86, box=0)
        # --- Band 6: Harriet Tubman
        self.next_band(6)
        self.write_rows(6, "Harriet Tubman", [
            "Escaped 1849",
            "About 13 trips, about 70 people",
            "Never lost a passenger",
        ], scale=0.86, box=0)
        self.wait(4)
