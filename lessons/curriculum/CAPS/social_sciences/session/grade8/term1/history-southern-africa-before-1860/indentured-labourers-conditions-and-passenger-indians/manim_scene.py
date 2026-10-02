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

# Band-layout whiteboard scene for indentured-labourers-conditions-and-passenger-indians (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (280/220/270/210/150/150/150 of 1430 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class IndenturedLabourersConditionsAndPassengerIndiansSession(MovingCameraScene):
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
        # --- Band 0: Life on the estates
        self.write_rows(0, "Life on the estates", [
            "Barracks: crowded, poor sanitation",
            "Dawn to dusk; longer in crushing season",
            "Passes; desertion a crime",
            "10 to 14 shillings a month plus rations",
        ], scale=0.86, box=1)
        # --- Band 1: Women and resistance
        self.next_band(1)
        self.write_rows(1, "Women and resistance", [
            "Women: lower pay and a double burden",
            "Complaints, desertion, work refusals",
            "India suspends emigration 1866 to 1874",
            "Wragg Commission 1885 to 1887",
        ], scale=0.86, box=2)
        # --- Band 2: Passenger Indians
        self.next_band(2)
        self.write_rows(2, "Passenger Indians", [
            "Traders from the 1870s, many from Gujarat",
            "Free Indians: gardeners, fishermen, workers",
            "1895: three-pound tax; 1896: vote removed",
            "1894: Natal Indian Congress",
        ], scale=0.86, box=1)
        # --- Band 3: Sources and legacy
        self.next_band(3)
        self.write_rows(3, "Sources and legacy", [
            "Protector's registers and ships' lists",
            "Commission testimony and petitions",
            "1913 strikes; tax ends 1914",
            "16 November remembered",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: A day on the estate
        self.next_band(4)
        self.write_rows(4, "A day on the estate", [
            "Barracks before sunrise",
            "Cane knives until dark",
            "Jail for leaving without a pass",
        ], scale=0.86, box=2)
        # --- Band 5: Pushing back
        self.next_band(5)
        self.write_rows(5, "Pushing back", [
            "Complaints and refusals",
            "Temples and festivals",
            "India stops emigration in 1866",
        ], scale=0.86, box=2)
        # --- Band 6: Traders, taxes and Gandhi
        self.next_band(6)
        self.write_rows(6, "Traders, taxes and Gandhi", [
            "Passenger Indians open shops",
            "The three-pound tax",
            "Gandhi and the Natal Indian Congress",
        ], scale=0.86, box=1)
        self.wait(4)
