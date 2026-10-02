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

# Band-layout whiteboard scene for from-slave-trade-wealth-to-the-industrial-revolution (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/270/180/250/150/150/150 of 1340 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class FromSlaveTradeWealthToTheIndustrialRevolutionSession(MovingCameraScene):
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
        # --- Band 0: Doing History: sources
        self.write_rows(0, "Doing History: sources", [
            "Primary: made at the time. Secondary: made later",
            "Ask: who, when, why, could they know?",
            "Biased sources still reveal beliefs",
            "Tasks: source-based questions, paragraph, essay",
        ], scale=0.86, box=2)
        # --- Band 1: Wealth from the slave trade
        self.next_band(1)
        self.write_rows(1, "Wealth from the slave trade", [
            "Goods to West Africa; captives across the Atlantic",
            "Middle Passage: about 12,5 million forced onto ships",
            "Sugar, tobacco and cotton back to Liverpool and Bristol",
            "Slave trade abolished 1807; Cape emancipation 1834",
        ], scale=0.8, box=1)
        # --- Band 2: The Industrial Revolution
        self.next_band(2)
        self.write_rows(2, "The Industrial Revolution", [
            "Hand work at home to machines in factories",
            "Spinning jenny, water frame, power loom",
            "Watt's steam engine; coal and iron; railways from 1825",
            "Britain first: a combination of factors",
        ], scale=0.8, box=3)
        # --- Band 3: Reaching southern Africa
        self.next_band(3)
        self.write_rows(3, "Reaching southern Africa", [
            "1860: indentured Indian labour in Natal",
            "1867: diamonds; 1871: British annexation",
            "1886: gold on the Witwatersrand",
            "Colonial rule and controlled black migrant labour",
        ], scale=0.8, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: History as detective work
        self.next_band(4)
        self.write_rows(4, "History as detective work", [
            "Sources are clues",
            "Question every witness",
            "Answer first, then evidence",
        ], scale=0.86)
        # --- Band 5: Following the money
        self.next_band(5)
        self.write_rows(5, "Following the money", [
            "Three journeys, one triangle",
            "Liverpool, banks, canals and factories",
            "One important piece among several",
        ], scale=0.86, box=2)
        # --- Band 6: Machines, coal and a long road south
        self.next_band(6)
        self.write_rows(6, "Machines, coal and a long road south", [
            "Hand to machine, around 1750",
            "Hungry factories need raw materials and minerals",
            "1860, 1867, 1886",
        ], scale=0.86, box=2)
        self.wait(4)
