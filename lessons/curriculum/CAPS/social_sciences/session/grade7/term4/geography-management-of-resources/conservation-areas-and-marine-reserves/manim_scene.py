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

# Band-layout whiteboard scene for conservation-areas-and-marine-reserves (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/160/180/210/90/90/90 of 980 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ConservationAreasAndMarineReservesSession(MovingCameraScene):
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
        # --- Band 0: Types and Purposes of Conservation Areas
        self.write_rows(0, "Types and Purposes of Conservation Areas", [
            "National parks: run by SANParks",
            "Provincial, private and community reserves",
            "Marine protected areas and peace parks",
            "Purpose: biodiversity, water, tourism, research",
        ], scale=0.8, box=1)
        # --- Band 1: Where Are They?
        self.next_band(1)
        self.write_rows(1, "Where Are They?", [
            "Kruger: Limpopo and Mpumalanga, 1926",
            "Hluhluwe-iMfolozi: saved the white rhino",
            "iSimangaliso: first World Heritage Site",
            "Addo: saved the last Eastern Cape elephants",
        ], scale=0.86, box=4)
        # --- Band 2: Marine Protected Areas
        self.next_band(2)
        self.write_rows(2, "Marine Protected Areas", [
            "Cold Benguela west; warm Agulhas east",
            "MPA: fishing restricted to protect life",
            "No-take zones; spillover to fishers",
            "2019: 20 new MPAs, total 41",
        ], scale=0.86, box=3)
        # --- Band 3: Case Study: Tsitsikamma
        self.next_band(3)
        self.write_rows(3, "Case Study: Tsitsikamma", [
            "1964: Africa's oldest marine protected area",
            "About 60 km of coast, 5 km out to sea",
            "No-take zone: more and larger fish",
            "2016: limited community fishing debated",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Protected Areas
        self.next_band(4)
        self.write_rows(4, "Protected Areas", [
            "Places set aside for nature",
            "National parks run by SANParks",
            "Protect, research, tourism",
        ], scale=0.86, box=0)
        # --- Band 5: Where Are They?
        self.next_band(5)
        self.write_rows(5, "Where Are They?", [
            "Kruger: Big Five",
            "Hluhluwe-iMfolozi: white rhino",
            "Addo: elephants",
        ], scale=0.86, box=0)
        # --- Band 6: Reserves in the Sea
        self.next_band(6)
        self.write_rows(6, "Reserves in the Sea", [
            "No fishing in no-take zones",
            "Fish grow and spread",
            "Tsitsikamma, 1964",
        ], scale=0.86, box=0)
        self.wait(4)
