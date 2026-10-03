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

# Band-layout whiteboard scene for mansa-musas-pilgrimage-and-the-great-mosque (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/180/170/200/90/90/90 of 990 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class MansaMusasPilgrimageAndTheGreatMosqueSession(MovingCameraScene):
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
        # --- Band 0: Why Mansa Musa Went to Mecca
        self.write_rows(0, "Why Mansa Musa Went to Mecca", [
            "Hajj: pilgrimage to Mecca, a pillar of Islam",
            "1324 to 1325: the famous journey",
            "Faith, prestige, diplomacy, learning",
            "Main source: al-Umari in Egypt",
        ], scale=0.86, box=1)
        # --- Band 1: The Journey and Cairo
        self.next_band(1)
        self.write_rows(1, "The Journey and Cairo", [
            "Thousands of followers, camels of gold",
            "Cairo, July 1324: the Mamluk sultan",
            "So much gold that its value fell",
            "On to Mecca and Medina",
        ], scale=0.86, box=2)
        # --- Band 2: Results of the Pilgrimage
        self.next_band(2)
        self.write_rows(2, "Results of the Pilgrimage", [
            "Fame: Mali on European maps",
            "Scholars and books return with Musa",
            "Al-Sahili from Granada, architect",
            "Gao and Timbuktu in the empire",
        ], scale=0.86, box=2)
        # --- Band 3: The Great Mosque of Timbuktu
        self.next_band(3)
        self.write_rows(3, "The Great Mosque of Timbuktu", [
            "Djinguereber, completed about 1327",
            "Banco mud brick and toron beams",
            "Yearly replastering by the community",
            "Not the Great Mosque of Djenne",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: A King Goes on Pilgrimage
        self.next_band(4)
        self.write_rows(4, "A King Goes on Pilgrimage", [
            "Hajj to Mecca in 1324",
            "Faith, fame, friends, books",
            "Stories from Egypt",
        ], scale=0.86, box=0)
        # --- Band 5: Gold in Cairo
        self.next_band(5)
        self.write_rows(5, "Gold in Cairo", [
            "Thousands of people, camels of gold",
            "Gold lost value in Cairo",
            "Borrowed to get home",
        ], scale=0.86, box=0)
        # --- Band 6: The Mud Mosque
        self.next_band(6)
        self.write_rows(6, "The Mud Mosque", [
            "Scholars, books and an architect",
            "Djinguereber, about 1327",
            "Fresh mud every year",
        ], scale=0.86, box=0)
        self.wait(4)
