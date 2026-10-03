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

# Band-layout whiteboard scene for types-of-revolutions-and-the-economy-before-industrialisation (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/200/190/320/150/150/150 of 1350 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TypesOfRevolutionsAndTheEconomyBeforeIndustrialisationSession(MovingCameraScene):
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
        # --- Band 0: Kinds of revolution
        self.write_rows(0, "Kinds of revolution", [
            "Revolution: fundamental change in how things are done",
            "Political: America 1775, France 1789, Haiti 1791 to 1804",
            "Economic: agricultural, industrial; today digital",
            "Haiti 1804: enslaved people create a free nation",
        ], scale=0.8, box=3)
        # --- Band 1: The agricultural revolution
        self.next_band(1)
        self.write_rows(1, "The agricultural revolution", [
            "Open fields: strips, a fallow field, the common",
            "Seed drill; four-field rotation; selective breeding",
            "Enclosure: Acts of Parliament, about 1750 to 1850",
            "More food; poor villagers lose land and move to towns",
        ], scale=0.8, box=3)
        # --- Band 2: The domestic system
        self.next_band(2)
        self.write_rows(2, "The domestic system", [
            "Merchant puts out wool or cotton to families",
            "Spin and weave at home; paid by the piece",
            "Own hours, but low pay and the merchant's power",
            "Spinning was the bottleneck",
        ], scale=0.86, box=3)
        # --- Band 3: Before industry
        self.next_band(3)
        self.write_rows(3, "Before industry", [
            "Power: muscles, water, wind, wood",
            "Slow transport: packhorse, wagon, river",
            "England and Wales about 6 million in 1750, mostly rural",
            "Trade and merchant wealth growing",
        ], scale=0.8, box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Big change, short time
        self.next_band(4)
        self.write_rows(4, "Big change, short time", [
            "Who is in charge: America, France, Haiti",
            "How people live: farming, industry, digital",
            "Not always fighting in the streets",
        ], scale=0.86)
        # --- Band 5: Smarter farming, fewer farmers
        self.next_band(5)
        self.write_rows(5, "Smarter farming, fewer farmers", [
            "Strips, fallow fields and the common",
            "New methods; fences go up",
            "More food, but families lose land",
        ], scale=0.86, box=2)
        # --- Band 6: The spinning wheel by the fire
        self.next_band(6)
        self.write_rows(6, "The spinning wheel by the fire", [
            "Merchant brings wool; family spins and weaves",
            "Together at home, but slow and poorly paid",
            "The waiting weaver needs a faster spinner",
        ], scale=0.86, box=2)
        self.wait(4)
