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

# Band-layout whiteboard scene for impact-of-migrant-labour-on-families (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (270/220/230/250/150/150/150 of 1420 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ImpactOfMigrantLabourOnFamiliesSession(MovingCameraScene):
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
        # --- Band 0: How the system worked
        self.write_rows(0, "How the system worked", [
            "200 000 workers by 1910",
            "Contracts, compounds, return home",
            "Pushed by land loss and taxes",
            "Wages for a single man",
        ], scale=0.86, box=3)
        # --- Band 1: Women and children
        self.next_band(1)
        self.write_rows(1, "Women and children", [
            "Women: farming, herding, building",
            "Grandmothers raise children",
            "Absent fathers",
            "Strained relationships",
        ], scale=0.86, box=0)
        # --- Band 2: Health, money, long-term effects
        self.next_band(2)
        self.write_rows(2, "Health, money, long-term effects", [
            "Tuberculosis spreads home",
            "Remittances: taxes, food, lobola",
            "Households headed by women",
            "Part of apartheid",
        ], scale=0.86, box=0)
        # --- Band 3: Sources and calculations
        self.next_band(3)
        self.write_rows(3, "Sources and calculations", [
            "120 -- 30 = 90 shillings",
            "90 $\\div$ 2 = 45 shillings",
            "Songs, letters, oral history",
            "Not only suffering: resilience",
        ], scale=0.86, box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Two halves of one family
        self.next_band(4)
        self.write_rows(4, "Two halves of one family", [
            "Mine and village",
        ], scale=0.86, box=0)
        # --- Band 5: Life at home
        self.next_band(5)
        self.write_rows(5, "Life at home", [
            "Women hold it together",
        ], scale=0.86, box=0)
        # --- Band 6: What the mines sent home
        self.next_band(6)
        self.write_rows(6, "What the mines sent home", [
            "Money and sickness",
        ], scale=0.86, box=0)
        self.wait(4)
