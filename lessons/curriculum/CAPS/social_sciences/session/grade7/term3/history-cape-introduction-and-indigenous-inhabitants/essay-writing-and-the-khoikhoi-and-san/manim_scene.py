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

# Band-layout whiteboard scene for essay-writing-and-the-khoikhoi-and-san (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/160/170/190/90/90/90 of 950 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class EssayWritingAndTheKhoikhoiAndSanSession(MovingCameraScene):
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
        # --- Band 0: Introducing Colonisation
        self.write_rows(0, "Introducing Colonisation", [
            "Colonisation: settle and take control",
            "Sea route to the spices of the East",
            "1652: VOC refreshment station",
            "Most written sources by colonists",
        ], scale=0.86, box=1)
        # --- Band 1: How to Write a History Essay
        self.next_band(1)
        self.write_rows(1, "How to Write a History Essay", [
            "Introduction: answer and line of argument",
            "Body: one main point per paragraph",
            "Topic sentence, evidence, link back",
            "Conclusion: sum up, no new facts",
        ], scale=0.86, box=2)
        # --- Band 2: The San
        self.next_band(2)
        self.write_rows(2, "The San", [
            "Hunter-gatherers in small mobile groups",
            "Men hunted; women gathered most food",
            "Rock art: eland, rain, trance dance",
            "Lost land as colonists spread",
        ], scale=0.86, box=3)
        # --- Band 3: The Khoikhoi
        self.next_band(3)
        self.write_rows(3, "The Khoikhoi", [
            "Khoikhoi: herders of cattle and sheep",
            "Portable reed-mat huts",
            "Autshumato: interpreter for the Dutch",
            "Traded livestock for copper, iron, beads",
        ], scale=0.86, box=4)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: This Term and Essays
        self.next_band(4)
        self.write_rows(4, "This Term and Essays", [
            "Colonisation: settle and take control",
            "1652: VOC at the Cape",
            "Essay: introduction, body, conclusion",
        ], scale=0.86, box=0)
        # --- Band 5: The San
        self.next_band(5)
        self.write_rows(5, "The San", [
            "Hunters and gatherers",
            "Small moving family groups",
            "Rock art",
        ], scale=0.86, box=0)
        # --- Band 6: The Khoikhoi
        self.next_band(6)
        self.write_rows(6, "The Khoikhoi", [
            "Herders of cattle and sheep",
            "Reed-mat huts",
            "Traded with ships",
        ], scale=0.86, box=0)
        self.wait(4)
