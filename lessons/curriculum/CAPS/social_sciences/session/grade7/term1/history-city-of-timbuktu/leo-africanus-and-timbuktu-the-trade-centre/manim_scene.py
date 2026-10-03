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

# Band-layout whiteboard scene for leo-africanus-and-timbuktu-the-trade-centre (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/170/180/220/90/90/90 of 1010 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class LeoAfricanusAndTimbuktuTheTradeCentreSession(MovingCameraScene):
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
        # --- Band 0: Leo Africanus: The Man and His Book
        self.write_rows(0, "Leo Africanus: The Man and His Book", [
            "Al-Hasan al-Wazzan, born Granada, about 1494",
            "Visited Timbuktu about 1510",
            "Captured and taken to Rome",
            "Description of Africa, published 1550",
        ], scale=0.86, box=1)
        # --- Band 1: What Leo Africanus Saw
        self.next_band(1)
        self.write_rows(1, "What Leo Africanus Saw", [
            "Clay houses, a stone and lime mosque",
            "Weavers, merchants, imported cloth",
            "A rich king who honours scholars",
            "Books earn more than any other goods",
        ], scale=0.86, box=3)
        # --- Band 2: Testing an Eyewitness Source
        self.next_band(2)
        self.write_rows(2, "Testing an Eyewitness Source", [
            "Who: a North African scholar, an outsider",
            "When: about 15 years after the visit",
            "Why and for whom: European readers in Rome",
            "Check against chronicles and manuscripts",
        ], scale=0.86, box=3)
        # --- Band 3: Timbuktu, Port of the Desert
        self.next_band(3)
        self.write_rows(3, "Timbuktu, Port of the Desert", [
            "Founded about 1100 near a well",
            "Camels meet boats at the Niger bend",
            "Salt and cloth in, gold and kola out",
            "Height in the 1400s and 1500s",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: A Traveller Writes a Book
        self.next_band(4)
        self.write_rows(4, "A Traveller Writes a Book", [
            "Born in Granada, grew up in Fez",
            "Visited Timbuktu about 1510",
            "Book published 1550",
        ], scale=0.86, box=0)
        # --- Band 5: What He Saw, and Can We Trust It?
        self.next_band(5)
        self.write_rows(5, "What He Saw, and Can We Trust It?", [
            "Weavers, scholars, a rich king",
            "Books sold for the best profit",
            "Really there, but wrote years later",
        ], scale=0.86, box=0)
        # --- Band 6: Where Camels Meet Boats
        self.next_band(6)
        self.write_rows(6, "Where Camels Meet Boats", [
            "Desert edge, river bend",
            "Camels from the north, boats from the south",
            "A port of the desert",
        ], scale=0.86, box=0)
        self.wait(4)
