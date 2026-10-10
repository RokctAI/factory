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

# Band-layout whiteboard scene for properties-of-materials (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/150/160/110/110/110 of 790 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PropertiesOfMaterialsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Hard or Soft, Stiff or Flexible
        self.write_rows(0, "Hard or Soft, Stiff or Flexible", [
            "Hard: does not dent or scratch",
            "Soft: foam, wool, cloth",
            "Stiff: wood, glass, stone",
            "Flexible: rubber, cloth",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Strong or Weak, Light or Heavy
        self.next_band(1)
        self.write_rows(1, "Strong or Weak, Light or Heavy", [
            "Strong: rope, metal, leather",
            "Weak: paper tears",
            "Same size blocks: fair test",
            "Light but strong: aluminium",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Waterproof or Absorbent
        self.next_band(2)
        self.write_rows(2, "Waterproof or Absorbent", [
            "Waterproof: plastic, rubber, glass",
            "Absorbent: towel, paper towel",
            "Raincoat: waterproof, flexible",
            "Towel: absorbent, soft",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A cotton raincoat''",
            "``Hard means strong''",
            "``Weigh different sized blocks''",
            "``Light means weak''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Scratch and Bend
        self.next_band(4)
        self.write_rows(4, "Scratch and Bend", [
            "Scratch and bend",
            "Hard and soft",
            "Stiff and flexible",
            "Rubber bends",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Pull and Lift
        self.next_band(5)
        self.write_rows(5, "Pull and Lift", [
            "Pull and lift",
            "Strong and weak",
            "Light and heavy",
            "Paper tears",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Wet or Dry
        self.next_band(6)
        self.write_rows(6, "Wet or Dry", [
            "Wet or dry",
            "Waterproof",
            "Absorbent",
            "Choose for the job",
        ], scale=0.9, box=3)

        last = Tex("Hard or soft, stiff or flexible, strong or weak, light or heavy, waterproof or absorbent: choose the right one for the job.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
