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

# Band-layout whiteboard scene for trekboers-moving-inland (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/160/170/190/90/90/90 of 960 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TrekboersMovingInlandSession(MovingCameraScene):
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
        # --- Band 0: Who Were the Trekboers?
        self.write_rows(0, "Who Were the Trekboers?", [
            "Trekboer: travelling stock farmer",
            "1714: loan farm system",
            "Large families needed land",
            "Escape from Company control",
        ], scale=0.86, box=1)
        # --- Band 1: Trekboer Lifestyle
        self.next_band(1)
        self.write_rows(1, "Trekboer Lifestyle", [
            "Wagons and simple clay houses",
            "Wealth in sheep, cattle and horses",
            "Self-sufficient: soap, candles, leather",
            "Bible central; schooling limited",
        ], scale=0.86, box=2)
        # --- Band 2: Slaves, Servants and Labour
        self.next_band(2)
        self.write_rows(2, "Slaves, Servants and Labour", [
            "Few slaves; many Khoikhoi servants",
            "Khoikhoi lost land, worked as herders",
            "Inboekstelsel: indenture to age 25",
            "Commandos: armed farmer groups",
        ], scale=0.86, box=3)
        # --- Band 3: Conflict and Stories
        self.next_band(3)
        self.write_rows(3, "Conflict and Stories", [
            "San resisted; commandos killed thousands",
            "1779: first frontier war with the Xhosa",
            "1795: Graaff-Reinet and Swellendam revolt",
            "Many stories: pioneers and dispossessed",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Travelling Farmers
        self.next_band(4)
        self.write_rows(4, "Travelling Farmers", [
            "Farmers with wagons and livestock",
            "Loan farms from 1714",
            "Big families needed land",
        ], scale=0.86, box=0)
        # --- Band 5: Life on the Move
        self.next_band(5)
        self.write_rows(5, "Life on the Move", [
            "Wagons and clay houses",
            "Self-made soap and shoes",
            "Khoikhoi servants did much of the work",
        ], scale=0.86, box=0)
        # --- Band 6: Conflict
        self.next_band(6)
        self.write_rows(6, "Conflict", [
            "San resisted; commandos attacked",
            "1779: first frontier war",
            "Tell all the stories",
        ], scale=0.86, box=0)
        self.wait(4)
