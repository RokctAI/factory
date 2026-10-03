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

# Band-layout whiteboard scene for community-conservation-and-eco-tourism (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/170/160/180/90/90/90 of 950 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CommunityConservationAndEcoTourismSession(MovingCameraScene):
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
        # --- Band 0: What Is Community Conservation?
        self.write_rows(0, "What Is Community Conservation?", [
            "Communities manage and benefit",
            "Past: people removed and excluded",
            "Ownership, decisions, shared benefits",
            "Respect local and scientific knowledge",
        ], scale=0.86, box=1)
        # --- Band 1: Community Conservation Examples
        self.next_band(1)
        self.write_rows(1, "Community Conservation Examples", [
            "Makuleke: removed 1969, land won back 1998",
            "Kept land wild; eco-tourism lodges",
            "Working for Water: clears alien plants",
            "Food gardens, recycling, small-scale fishing",
        ], scale=0.86, box=2)
        # --- Band 2: What Is Eco-Tourism?
        self.next_band(2)
        self.write_rows(2, "What Is Eco-Tourism?", [
            "Eco-tourism: responsible travel to nature",
            "Minimise impact; support conservation",
            "Benefit and respect local people",
            "Beware greenwashing",
        ], scale=0.86, box=2)
        # --- Band 3: Eco-Tourism Examples
        self.next_band(3)
        self.write_rows(3, "Eco-Tourism Examples", [
            "Makuleke lodges pay the community",
            "Wild Coast community trails",
            "Hermanus whale watching, June to November",
            "Khwa ttu San Heritage Centre",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Communities as Protectors
        self.next_band(4)
        self.write_rows(4, "Communities as Protectors", [
            "Past: people moved off land",
            "Now: communities share benefits",
            "Benefit means protection",
        ], scale=0.86, box=0)
        # --- Band 5: Examples
        self.next_band(5)
        self.write_rows(5, "Examples", [
            "Makuleke: land back, kept wild",
            "Working for Water: remove alien trees",
            "Food gardens and recycling",
        ], scale=0.86, box=0)
        # --- Band 6: Eco-Tourism
        self.next_band(6)
        self.write_rows(6, "Eco-Tourism", [
            "Protects nature, helps locals",
            "Wild Coast trails, Hermanus whales",
            "Check it is truly green",
        ], scale=0.86, box=0)
        self.wait(4)
