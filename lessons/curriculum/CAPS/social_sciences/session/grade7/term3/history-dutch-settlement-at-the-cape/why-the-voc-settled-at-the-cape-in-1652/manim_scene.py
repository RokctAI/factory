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

# Band-layout whiteboard scene for why-the-voc-settled-at-the-cape-in-1652 (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/170/180/210/90/90/90 of 990 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class WhyTheVocSettledAtTheCapeIn1652Session(MovingCameraScene):
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
        # --- Band 0: The Dutch East India Company
        self.write_rows(0, "The Dutch East India Company", [
            "VOC founded 1602; owned by shareholders",
            "Monopoly on Dutch trade with Asia",
            "Could build forts, keep armies, govern",
            "Aim: profit from spices; base at Batavia",
        ], scale=0.86, box=1)
        # --- Band 1: Why the VOC Needed a Station
        self.next_band(1)
        self.write_rows(1, "Why the VOC Needed a Station", [
            "Voyage of six months or more",
            "Scurvy: lack of vitamin C",
            "Halfway station for fresh food and water",
            "1647 wreck; 1649 report recommends Cape",
        ], scale=0.86, box=2)
        # --- Band 2: Why the Cape, and the First Years
        self.next_band(2)
        self.write_rows(2, "Why the Cape, and the First Years", [
            "Halfway point; Table Bay; fresh water",
            "6 April 1652: three ships arrive",
            "Fort, later the Castle of Good Hope",
            "Company's Garden for vegetables",
        ], scale=0.86, box=2)
        # --- Band 3: The Impact on the Khoikhoi
        self.next_band(3)
        self.write_rows(3, "The Impact on the Khoikhoi", [
            "Trade became unequal",
            "1657: farms on the Liesbeek River",
            "1659 to 1660: First Khoikhoi-Dutch War",
            "Doman resisted; Krotoa interpreted",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: The VOC
        self.next_band(4)
        self.write_rows(4, "The VOC", [
            "Dutch trading company, 1602",
            "Aim: profit from spices",
            "Base at Batavia",
        ], scale=0.86, box=0)
        # --- Band 5: A Halfway Station
        self.next_band(5)
        self.write_rows(5, "A Halfway Station", [
            "Long voyage; scurvy",
            "Halfway stop for food and water",
            "6 April 1652: Van Riebeeck",
        ], scale=0.86, box=0)
        # --- Band 6: The Khoikhoi Lose Land
        self.next_band(6)
        self.write_rows(6, "The Khoikhoi Lose Land", [
            "1657: land along the Liesbeek taken",
            "1659 to 1660: war; Doman",
            "Krotoa: interpreter",
        ], scale=0.86, box=0)
        self.wait(4)
