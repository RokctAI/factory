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

# Band-layout whiteboard scene for goods-and-services-markets (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (260/200/220/160/190/110/120 of 1260 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class GoodsAndServicesMarketsSession(MovingCameraScene):
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
        self.write_rows(0, "Goods and services markets", [
            "Goods: touchable; services: done for you",
            "Non-durable, semi-durable, durable",
            "Consumer goods and capital goods",
            "Durables swing with the economy",
        ], box=1)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Kinds of markets", [
            "Local, national, international",
            "Physical and online",
            "Wholesale and retail",
            "Formal and informal",
        ], box=3)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Demand, supply and price", [
            "Price up: demand down",
            "Price up: supply up",
            "R60: 300 demanded = 300 supplied",
            "Equilibrium price R60",
        ], box=3)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Surpluses and shortages", [
            "R70: 400 - 200 = surplus of 200",
            "R50: 400 - 200 = shortage of 200",
            "Hailstorm: supply down, price up",
            "Prices are signals",
        ], box=2)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Consumers in the market", [
            "Consumer sovereignty",
            "Consumer Protection Act 2008",
            "Defects: return within six months",
            "Competition Commission fights price fixing",
        ], box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "Morning at the produce market", [
            "R40: too many buyers",
            "R80: too many tomatoes",
            "R60: the market clears",
            "Hail: price rises, more sent",
        ], box=2)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "From the stall to the table", [
            "Supermarket: formal retail",
            "Spaza and pavement: informal",
            "App: online market",
            "Know your consumer rights",
        ], box=3)

        self.wait(4)
