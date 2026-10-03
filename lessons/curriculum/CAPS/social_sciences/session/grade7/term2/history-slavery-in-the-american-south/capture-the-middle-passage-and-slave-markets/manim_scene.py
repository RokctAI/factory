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

# Band-layout whiteboard scene for capture-the-middle-passage-and-slave-markets (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/180/190/200/90/90/90 of 1000 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CaptureTheMiddlePassageAndSlaveMarketsSession(MovingCameraScene):
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
        # --- Band 0: Capture and the March to the Coast
        self.write_rows(0, "Capture and the March to the Coast", [
            "War, raids, kidnapping, punishment, debt",
            "Equiano kidnapped as a child",
            "Coffles: tied together, marched for weeks",
            "Sold again and again on the way",
        ], scale=0.86, box=1)
        # --- Band 1: Forts, Factories and Sale on the Coast
        self.next_band(1)
        self.write_rows(1, "Forts, Factories and Sale on the Coast", [
            "Elmina 1482; Cape Coast; Goree Island",
            "Dark, crowded dungeons for weeks",
            "Inspected like livestock; branded",
            "The Door of No Return",
        ], scale=0.86, box=1)
        # --- Band 2: The Middle Passage
        self.next_band(2)
        self.write_rows(2, "The Middle Passage", [
            "6 to 10 weeks across the Atlantic",
            "Chained below deck; disease spread",
            "Brookes plan, 1788",
            "About 1 in 7 or 8 died; revolts on about 1 in 10",
        ], scale=0.8, box=3)
        # --- Band 3: Slave Markets and the Numbers
        self.next_band(3)
        self.write_rows(3, "Slave Markets and the Numbers", [
            "Auctions and scrambles",
            "Families and shipmates separated",
            "About 400 000 directly to North America",
            "Most to the Caribbean and Brazil",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Taken From Home
        self.next_band(4)
        self.write_rows(4, "Taken From Home", [
            "Kidnapped and captured",
            "Tied together, marched for weeks",
            "Dungeons and the Door of No Return",
        ], scale=0.86, box=0)
        # --- Band 5: The Crossing
        self.next_band(5)
        self.write_rows(5, "The Crossing", [
            "Six to ten weeks",
            "Chained in the dark",
            "About 1 in 7 or 8 died",
        ], scale=0.86, box=0)
        # --- Band 6: Sold
        self.next_band(6)
        self.write_rows(6, "Sold", [
            "Auctions and scrambles",
            "Families split forever",
            "Most to the Caribbean and Brazil",
        ], scale=0.86, box=0)
        self.wait(4)
