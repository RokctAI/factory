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

# Band-layout whiteboard scene for british-takeover-of-griqualand-west (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (250/200/320/250/150/150/150 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class BritishTakeoverOfGriqualandWestSession(MovingCameraScene):
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
        # --- Band 0: The discovery
        self.write_rows(0, "The discovery", [
            "1867: Eureka diamond near Hopetown",
            "1869: Star of South Africa",
            "1871: dry diggings; Colesberg Kopje",
            "Kimberlite pipes go deep",
        ], scale=0.86, box=3)
        # --- Band 1: Four claimants
        self.next_band(1)
        self.write_rows(1, "Four claimants", [
            "Orange Free State",
            "South African Republic",
            "Waterboer's Griqua, advised by Arnot",
            "Tswana chiefs",
        ], scale=0.86, box=2)
        # --- Band 2: Annexation
        self.next_band(2)
        self.write_rows(2, "Annexation", [
            "Keate Award 1871: against the Transvaal",
            "October 1871: Griqualand West",
            "1876: Free State paid 90 000 pounds",
            "Griqua lose land; rising of 1878",
        ], scale=0.86, box=1)
        # --- Band 3: Interpreting the takeover
        self.next_band(3)
        self.write_rows(3, "Interpreting the takeover", [
            "Protection or seizure?",
            "Arnot's documents: read critically",
            "1 carat = one fifth of a gram",
            "Diamonds pull Britain inland",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: A shiny stone
        self.next_band(4)
        self.write_rows(4, "A shiny stone", [
            "A pebble by the river",
            "Diamonds deep in the ground",
            "A camp of tents and tin",
        ], scale=0.86, box=1)
        # --- Band 5: Who owns the land?
        self.next_band(5)
        self.write_rows(5, "Who owns the land?", [
            "Four claimants",
            "Keate decides against the Transvaal",
            "Britain takes it all",
        ], scale=0.86, box=2)
        # --- Band 6: What Britain gained
        self.next_band(6)
        self.write_rows(6, "What Britain gained", [
            "Diamond wealth and the road north",
            "Free State compensated",
            "Griqua lose their land",
        ], scale=0.86, box=2)
        self.wait(4)
