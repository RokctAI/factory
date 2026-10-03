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

# Band-layout whiteboard scene for indentured-labour-from-india-for-natal (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (250/250/260/240/150/150/150 of 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class IndenturedLabourFromIndiaForNatalSession(MovingCameraScene):
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
        # --- Band 0: India as a British colony
        self.write_rows(0, "India as a British colony", [
            "East India Company from 1600",
            "Uprising of 1857; direct British rule 1858",
            "Debt, land revenue, famine",
            "Madras and Calcutta: ports of departure",
        ], scale=0.86, box=2)
        # --- Band 1: Sugar and labour in Natal
        self.next_band(1)
        self.write_rows(1, "Sugar and labour in Natal", [
            "Cane cut by hand, crushed quickly",
            "Africans had land; refused low-paid contracts",
            "Mauritius already used Indian labour",
            "1859 laws; Truro arrives November 1860",
        ], scale=0.86, box=1)
        # --- Band 2: The contract and voyage
        self.next_band(2)
        self.write_rows(2, "The contract and voyage", [
            "Five years with one employer",
            "10 shillings a month, plus 1 a year",
            "Free passage home after ten years",
            "Four to eight weeks at sea",
        ], scale=0.86, box=0)
        # --- Band 3: Interpreting indenture
        self.next_band(3)
        self.write_rows(3, "Interpreting indenture", [
            "A contract, wages and an end date",
            "But: passes, punishment, abuse",
            "About 152 000 came by 1911",
            "Most stayed in Natal",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: India under the British
        self.next_band(4)
        self.write_rows(4, "India under the British", [
            "A trading company takes control",
            "Debt and famine in the villages",
        ], scale=0.86, box=1)
        # --- Band 5: Sugar needs hands
        self.next_band(5)
        self.write_rows(5, "Sugar needs hands", [
            "Cane must be cut and crushed fast",
            "Zulu men had their own land",
            "The Truro arrives, 1860",
        ], scale=0.86, box=1)
        # --- Band 6: The contract and the journey
        self.next_band(6)
        self.write_rows(6, "The contract and the journey", [
            "Five years, ten shillings a month",
            "Weeks in crowded ships",
            "Most stayed",
        ], scale=0.86, box=0)
        self.wait(4)
