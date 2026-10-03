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

# Band-layout whiteboard scene for map-of-colonising-countries-and-causes (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (270/260/250/230/130/130/130 of 1400 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ColonisingCountriesAndCausesSession(MovingCameraScene):
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
        # --- Band 0: Africa in 1914
        self.write_rows(0, "Africa in 1914", [
            "Britain: Egypt to the Cape",
            "France: north and west",
            "Germany, Belgium, Portugal",
            "Free: Ethiopia, Liberia",
        ], scale=0.86, box=3)
        # --- Band 1: Economic causes
        self.next_band(1)
        self.write_rows(1, "Economic causes", [
            "Raw materials",
            "Markets",
            "Investment, chartered companies",
            "Long Depression",
        ], scale=0.86, box=0)
        # --- Band 2: Other causes
        self.next_band(2)
        self.write_rows(2, "Other causes", [
            "Nationalism and rivalry",
            "Suez and the Cape route",
            "Missionaries, racist ideas",
            "Steamships, quinine, Maxim gun",
        ], scale=0.86, box=2)
        # --- Band 3: Explaining causes
        self.next_band(3)
        self.write_rows(3, "Explaining causes", [
            "0.9 x 30.4 = 27.4 million sq km",
            "27.4 $\\div$ 10 = 2.7 x Europe",
            "Ferry's speech",
            "Weigh the causes",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Seven colours on the map
        self.next_band(4)
        self.write_rows(4, "Seven colours on the map", [
            "A quilt with two free patches",
        ], scale=0.86, box=0)
        # --- Band 5: Money and power
        self.next_band(5)
        self.write_rows(5, "Money and power", [
            "A race for land",
        ], scale=0.86, box=0)
        # --- Band 6: Beliefs and machines
        self.next_band(6)
        self.write_rows(6, "Beliefs and machines", [
            "False ideas, new machines",
        ], scale=0.86, box=0)
        self.wait(4)
