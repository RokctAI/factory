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

# Band-layout whiteboard scene for land-dispossession-and-its-consequences (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/160/180/170/90/90/90 of 950 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class LandDispossessionAndItsConsequencesSession(MovingCameraScene):
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
        # --- Band 0: What Is Land Dispossession?
        self.write_rows(0, "What Is Land Dispossession?", [
            "Dispossess: take land away",
            "Khoikhoi: land held in common",
            "San: shared hunting territories",
            "Colonists: private property, fenced and sold",
        ], scale=0.86, box=1)
        # --- Band 1: How the Land Was Taken
        self.next_band(1)
        self.write_rows(1, "How the Land Was Taken", [
            "Settlement on grazing land without consent",
            "Wars: 1659 and 1673 to 1677",
            "Cattle lost through trade and raids",
            "Smallpox, commandos and colonial law",
        ], scale=0.86, box=3)
        # --- Band 2: Consequences for the Khoikhoi and San
        self.next_band(2)
        self.write_rows(2, "Consequences for the Khoikhoi and San", [
            "Chiefdoms broke up; independence lost",
            "Became farm labourers and servants",
            "Passes and indenture restricted freedom",
            "Languages and cultures lost",
        ], scale=0.86, box=2)
        # --- Band 3: Land Then and Now
        self.next_band(3)
        self.write_rows(3, "Land Then and Now", [
            "1913 Natives Land Act",
            "Restitution covers loss after 19 June 1913",
            "1999: Khomani San land claim",
            "2019: Khoi-San leadership recognised",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Different Ideas About Land
        self.next_band(4)
        self.write_rows(4, "Different Ideas About Land", [
            "Dispossession: land taken away",
            "Khoikhoi and San shared land",
            "Colonists: private ownership",
        ], scale=0.86, box=0)
        # --- Band 5: How It Happened
        self.next_band(5)
        self.write_rows(5, "How It Happened", [
            "Farms and wars",
            "Cattle taken; smallpox",
            "Trekboers, commandos and laws",
        ], scale=0.86, box=0)
        # --- Band 6: What It Caused
        self.next_band(6)
        self.write_rows(6, "What It Caused", [
            "Lost independence and cattle",
            "Became farm workers",
            "Restitution only after 1913",
        ], scale=0.86, box=0)
        self.wait(4)
