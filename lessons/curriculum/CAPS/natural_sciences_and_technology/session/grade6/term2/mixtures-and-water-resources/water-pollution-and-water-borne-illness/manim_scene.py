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

# Band-layout whiteboard scene for water-pollution-and-water-borne-illness (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (210/120/130/110/110/110 of 790 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class WaterPollutionAndWaterBorneIllnessSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.15).shift(band_shift(k) + UP * 2.4)
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
        self.wait(42)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Insoluble Pollution
        self.write_rows(0, "Insoluble Pollution", [
            "Pollution: water made unsafe",
            "Insoluble: can be seen",
            "Plastic, litter, oil, mud",
            "Removed by picking or filtering",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Soluble Pollution
        self.next_band(1)
        self.write_rows(1, "Soluble Pollution", [
            "Soluble: dissolved, invisible",
            "Fertiliser feeds algae",
            "Poisons, mine water, salts",
            "Cannot be filtered out",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Germs and Water-Borne Illnesses
        self.next_band(2)
        self.write_rows(2, "Germs and Water-Borne Illnesses", [
            "Germs from sewage and faeces",
            "Water-borne illnesses",
            "Cholera, typhoid, diarrhoea",
            "Toilets, clean water, handwashing",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Clear water is always clean''",
            "``Litter is the only pollution''",
            "``Filtering removes all pollution''",
            "``Washing in the river is harmless''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Pollution You Can See
        self.next_band(4)
        self.write_rows(4, "Pollution You Can See", [
            "Pollution you can see",
            "Plastic",
            "Oil",
            "Mud",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Pollution You Can't See
        self.next_band(5)
        self.write_rows(5, "Pollution You Can't See", [
            "Pollution you can't see",
            "Fertiliser",
            "Poison",
            "Soap and salt",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Germs in the Water
        self.next_band(6)
        self.write_rows(6, "Germs in the Water", [
            "Germs in the water",
            "Sewage",
            "Cholera",
            "Wash your hands",
        ], scale=0.9, box=3)

        last = Tex("Water can be polluted by insoluble substances, soluble substances and germs, and dirty water causes water-borne illnesses.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
