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

# Band-layout whiteboard scene for tswana-trade-on-the-southern-borders (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/170/170/180/90/90/90 of 950 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TswanaTradeOnTheSouthernBordersSession(MovingCameraScene):
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
        # --- Band 0: The Tswana World
        self.write_rows(0, "The Tswana World", [
            "Batswana: Sotho-Tswana-speaking farmers",
            "Kgosi and the kgotla assembly",
            "Large towns: Dithakong, Kaditshwene",
            "Fields near towns; distant cattle posts",
        ], scale=0.86, box=1)
        # --- Band 1: Tswana Products and Crafts
        self.next_band(1)
        self.write_rows(1, "Tswana Products and Crafts", [
            "Ivory, hides, skins, furs, ostrich feathers",
            "Karosses: fine fur cloaks",
            "Iron hoes and spears; copper beads",
            "Sebilo: sparkling iron powder",
        ], scale=0.86, box=2)
        # --- Band 2: Trade with the Kora and Griqua
        self.next_band(2)
        self.write_rows(2, "Trade with the Kora and Griqua", [
            "Tswana gave: ivory, skins, karosses, metal",
            "Received: beads, tobacco, cloth, later guns",
            "Dithakong: Batlhaping trading capital",
            "Kgosi Mothibi encouraged trade",
        ], scale=0.86, box=3)
        # --- Band 3: Changes on the Southern Tswana Borders
        self.next_band(3)
        self.write_rows(3, "Changes on the Southern Tswana Borders", [
            "New goods; chiefs gain wealth",
            "Guns: elephants hunted heavily",
            "1816: mission among the Batlhaping",
            "1885: British Bechuanaland",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: The Tswana
        self.next_band(4)
        self.write_rows(4, "The Tswana", [
            "Lived north of the Orange River",
            "Chiefs and the kgotla",
            "Big towns like Dithakong",
        ], scale=0.86, box=0)
        # --- Band 5: What They Made
        self.next_band(5)
        self.write_rows(5, "What They Made", [
            "Ivory, hides, skins, furs",
            "Karosses",
            "Iron and copper work",
        ], scale=0.86, box=0)
        # --- Band 6: Trading
        self.next_band(6)
        self.write_rows(6, "Trading", [
            "Gave: ivory, skins, metal",
            "Got: beads, tobacco, cloth, guns",
            "Wealth and new dangers",
        ], scale=0.86, box=0)
        self.wait(4)
