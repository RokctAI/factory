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

# Band-layout whiteboard scene for regulating-diamond-supply-and-price (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (270/210/240/300/150/150/150 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class RegulatingDiamondSupplyAndPriceSession(MovingCameraScene):
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
        # --- Band 0: One man, one claim
        self.write_rows(0, "One man, one claim", [
            "A diggers' rule, 1870 to 1871",
            "Spread the chance; block speculators",
            "Limit raised to ten in 1876",
            "Then removed: consolidation",
        ], scale=0.86, box=1)
        # --- Band 1: Scarcity, supply and price
        self.next_band(1)
        self.write_rows(1, "Scarcity, supply and price", [
            "More supply, same demand: price falls",
            "Kimberley floods the market",
            "2 000 $\\times$ 3 = 6 000",
            "3 000 $\\times$ 2 = 6 000",
        ], scale=0.86, box=0)
        # --- Band 2: Controlling supply
        self.next_band(2)
        self.write_rows(2, "Controlling supply", [
            "De Beers limits output from 1888",
            "London Diamond Syndicate 1890",
            "Buy up new producers",
            "Compounds and IDB laws stop leaks",
        ], scale=0.86, box=1)
        # --- Band 3: Effects and today
        self.next_band(3)
        self.write_rows(3, "Effects and today", [
            "Winners: shareholders and merchants",
            "Losers: small diggers and workers",
            "Botswana, Namibia, South Africa",
            "Kimberley Process 2003",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: A fair share for each digger
        self.next_band(4)
        self.write_rows(4, "A fair share for each digger", [
            "One small square each",
            "Mostly for white diggers",
            "Limit gone as the mine deepened",
        ], scale=0.86, box=0)
        # --- Band 5: Too many diamonds
        self.next_band(5)
        self.write_rows(5, "Too many diamonds", [
            "Rare means valuable",
            "More digging, lower prices",
        ], scale=0.86, box=1)
        # --- Band 6: One hand on the tap
        self.next_band(6)
        self.write_rows(6, "One hand on the tap", [
            "Dig less, store the rest",
            "Syndicate sells slowly",
            "Owners rich, workers poor",
        ], scale=0.86, box=0)
        self.wait(4)
