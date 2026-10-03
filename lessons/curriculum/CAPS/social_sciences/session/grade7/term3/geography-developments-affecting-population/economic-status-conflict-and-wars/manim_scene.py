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

# Band-layout whiteboard scene for economic-status-conflict-and-wars (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/170/160/180/90/90/90 of 930 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class EconomicStatusConflictAndWarsSession(MovingCameraScene):
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
        # --- Band 0: Economic Status and Development
        self.write_rows(0, "Economic Status and Development", [
            "Economic status: how wealthy",
            "Developed and developing countries",
            "HDI: income, education, life expectancy",
            "Wealthier: lower births and deaths",
        ], scale=0.86, box=1)
        # --- Band 1: How Wealth and Poverty Affect Births and Deaths
        self.next_band(1)
        self.write_rows(1, "How Wealth and Poverty Affect Births and Deaths", [
            "Poverty: poor food, water, health care",
            "More child deaths, so more births",
            "Wealth: smaller families, longer lives",
            "Death rates fall first, then birth rates",
        ], scale=0.86, box=2)
        # --- Band 2: Conflict and War
        self.next_band(2)
        self.write_rows(2, "Conflict and War", [
            "Direct: soldiers and civilians killed",
            "Indirect: famine, disease, destroyed clinics",
            "Births fall in war, may jump after",
            "Missing young men show on pyramids",
        ], scale=0.86, box=2)
        # --- Band 3: Refugees and Displaced People
        self.next_band(3)
        self.write_rows(3, "Refugees and Displaced People", [
            "Refugee: fled across a border",
            "Displaced person: fled within own country",
            "Over 110 million displaced worldwide",
            "Most refugees stay in neighbouring countries",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Rich and Poor
        self.next_band(4)
        self.write_rows(4, "Rich and Poor", [
            "Wealthier: long lives, small families",
            "Poorer: more child deaths, bigger families",
            "Health, water and schools matter",
        ], scale=0.86, box=0)
        # --- Band 5: Wars
        self.next_band(5)
        self.write_rows(5, "Wars", [
            "Killing in fighting",
            "Hunger and disease kill even more",
            "Fewer births in war; baby boom after",
        ], scale=0.86, box=0)
        # --- Band 6: People on the Move
        self.next_band(6)
        self.write_rows(6, "People on the Move", [
            "Refugee: crossed a border",
            "Displaced: still in own country",
            "Over 110 million forced from home",
        ], scale=0.86, box=0)
        self.wait(4)
