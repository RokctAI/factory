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

# Band-layout whiteboard scene for randlords-and-the-chamber-of-mines (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (290/210/220/260/150/150/150 of 1430 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class RandlordsAndTheChamberOfMinesSession(MovingCameraScene):
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
        # --- Band 0: Gold on the Witwatersrand
        self.write_rows(0, "Gold on the Witwatersrand", [
            "1886: Langlaagte",
            "Fine gold in hard conglomerate",
            "Low-grade and deep",
            "Cyanide process, 1890",
        ], scale=0.86, box=2)
        # --- Band 1: The Randlords
        self.next_band(1)
        self.write_rows(1, "The Randlords", [
            "Rhodes, Beit, Wernher, Barnato",
            "Mining houses",
            "Capital from London and Europe",
            "Many began in Kimberley",
        ], scale=0.86, box=1)
        # --- Band 2: Chamber of Mines, 1887
        self.next_band(2)
        self.write_rows(2, "Chamber of Mines, 1887", [
            "Gold price fixed",
            "Cut and cap black wages",
            "Recruiting: Wenela",
            "Lobbying the government",
        ], scale=0.86, box=0)
        # --- Band 3: Profits and politics
        self.next_band(3)
        self.write_rows(3, "Profits and politics", [
            "10 000 $\\times$ 10 = 100 000 g",
            "Costs decide profit",
            "Jameson Raid, 1895 to 1896",
            "Road to war",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Gold in hard rock
        self.next_band(4)
        self.write_rows(4, "Gold in hard rock", [
            "Dig, crush, extract",
        ], scale=0.86, box=0)
        # --- Band 5: The rich men of the Rand
        self.next_band(5)
        self.write_rows(5, "The rich men of the Rand", [
            "Kimberley money moves north",
        ], scale=0.86, box=0)
        # --- Band 6: The owners' club
        self.next_band(6)
        self.write_rows(6, "The owners' club", [
            "Keep costs low",
        ], scale=0.86, box=0)
        self.wait(4)
