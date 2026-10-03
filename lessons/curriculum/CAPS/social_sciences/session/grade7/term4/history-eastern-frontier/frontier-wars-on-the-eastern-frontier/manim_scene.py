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

# Band-layout whiteboard scene for frontier-wars-on-the-eastern-frontier (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/170/210/210/90/90/90 of 1030 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class FrontierWarsOnTheEasternFrontierSession(MovingCameraScene):
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
        # --- Band 0: The Xhosa and the Frontier
        self.write_rows(0, "The Xhosa and the Frontier", [
            "Xhosa: Gcaleka and Rharhabe branches",
            "Leaders: Hintsa, Ngqika, Ndlambe",
            "Zuurveld: Bushmans to Fish River",
            "Same needs: grazing land and water",
        ], scale=0.86, box=1)
        # --- Band 1: Causes of the Wars
        self.next_band(1)
        self.write_rows(1, "Causes of the Wars", [
            "Land: the main cause",
            "Cattle raids and the reprisal system",
            "Different ideas about borders",
            "British policy and chiefs' rivalries",
        ], scale=0.86, box=2)
        # --- Band 2: The Wars of the Early 1800s
        self.next_band(2)
        self.write_rows(2, "The Wars of the Early 1800s", [
            "Nine wars, 1779 to 1879",
            "1819: Makhanda attacks Grahamstown",
            "Ceded Territory: Fish to Keiskamma",
            "1835: Hintsa killed; land later returned",
        ], scale=0.86, box=3)
        # --- Band 3: Later Wars and Consequences
        self.next_band(3)
        self.write_rows(3, "Later Wars and Consequences", [
            "1846: War of the Axe",
            "1850 to 1853: Mlanjeni's War",
            "1856 to 1857: the cattle-killing",
            "Xhosa lost land, cattle and independence",
        ], scale=0.86, box=4)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: The Xhosa
        self.next_band(4)
        self.write_rows(4, "The Xhosa", [
            "Cattle farmers in the Eastern Cape",
            "Chiefs: Hintsa, Ngqika, Ndlambe",
            "Competition for the Zuurveld",
        ], scale=0.86, box=0)
        # --- Band 5: Why the Wars?
        self.next_band(5)
        self.write_rows(5, "Why the Wars?", [
            "Land and cattle",
            "1819: Makhanda attacks Grahamstown",
            "1835: Hintsa killed",
        ], scale=0.86, box=0)
        # --- Band 6: A Hundred Years of War
        self.next_band(6)
        self.write_rows(6, "A Hundred Years of War", [
            "Nine wars, 1779 to 1879",
            "Cattle-killing and famine",
            "Land and independence lost",
        ], scale=0.86, box=0)
        self.wait(4)
