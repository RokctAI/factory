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

# Band-layout whiteboard scene for spread-of-islam-into-west-africa (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/180/170/180/90/90/90 of 960 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SpreadOfIslamIntoWestAfricaSession(MovingCameraScene):
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
        # --- Band 0: Islam Spreads Across North Africa
        self.write_rows(0, "Islam Spreads Across North Africa", [
            "Islam: one God, Prophet Muhammad",
            "Quran in Arabic",
            "Five Pillars, including the hajj",
            "North Africa Muslim by about 710",
        ], scale=0.86, box=1)
        # --- Band 1: Traders Carry Islam South
        self.next_band(1)
        self.write_rows(1, "Traders Carry Islam South", [
            "From about the 9th century, with traders",
            "Ghana: a Muslim town with 12 mosques",
            "Shared faith built trust and credit",
            "Towns and kings first, countryside later",
        ], scale=0.86, box=2)
        # --- Band 2: What Islam Brought: Writing, Learning and Law
        self.next_band(2)
        self.write_rows(2, "What Islam Brought: Writing, Learning and Law", [
            "Arabic script: reading and writing",
            "Quranic schools and scholars",
            "Advisers, judges and records",
            "Mud-brick mosques with wooden beams",
        ], scale=0.86, box=1)
        # --- Band 3: African Islam: Blending and Choice
        self.next_band(3)
        self.write_rows(3, "African Islam: Blending and Choice", [
            "Kings balanced Islam and older beliefs",
            "Ibn Battuta: praise and criticism",
            "Accommodation: adopted and adapted",
            "West Africans chose and shaped Islam",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: A Faith From Arabia
        self.next_band(4)
        self.write_rows(4, "A Faith From Arabia", [
            "One God, the Prophet Muhammad",
            "Quran in Arabic",
            "Pray, give, fast, pilgrimage",
        ], scale=0.86, box=0)
        # --- Band 5: Carried by Camel
        self.next_band(5)
        self.write_rows(5, "Carried by Camel", [
            "Traders, not armies",
            "Same faith, more trust",
            "Traders and kings first",
        ], scale=0.86, box=0)
        # --- Band 6: Books, Schools and Mud Mosques
        self.next_band(6)
        self.write_rows(6, "Books, Schools and Mud Mosques", [
            "Writing and schools",
            "Scholars, judges, advisers",
            "Mud mosques with wooden beams",
        ], scale=0.86, box=0)
        self.wait(4)
