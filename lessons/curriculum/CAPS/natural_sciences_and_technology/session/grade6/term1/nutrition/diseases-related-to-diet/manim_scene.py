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

# Band-layout whiteboard scene for diseases-related-to-diet (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (210/120/150/110/110/110 of 810 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DiseasesRelatedToDietSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Too Little Food and Protein
        self.write_rows(0, "Too Little Food and Protein", [
            "Malnutrition: bad nutrition",
            "Kwashiorkor: too little protein",
            "Marasmus: too little food",
            "Stunting: too short for age",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Missing Vitamins and Minerals
        self.next_band(1)
        self.write_rows(1, "Missing Vitamins and Minerals", [
            "Scurvy: no vitamin C",
            "Rickets: no vitamin D or calcium",
            "Anaemia: no iron",
            "Night blindness: no vitamin A",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Too Much Sugar, Salt and Fat
        self.next_band(2)
        self.write_rows(2, "Too Much Sugar, Salt and Fat", [
            "Obesity: too much energy food",
            "Type 2 diabetes: blood sugar",
            "High blood pressure: salt",
            "Tooth decay: sugar",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A big belly means well fed''",
            "``Only poor people get diet diseases''",
            "``Vitamins come only from tablets''",
            "``Only old people get diabetes''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Not Enough Food
        self.next_band(4)
        self.write_rows(4, "Not Enough Food", [
            "Not enough food",
            "Kwashiorkor",
            "Marasmus",
            "Protein and energy",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Missing Vitamins
        self.next_band(5)
        self.write_rows(5, "Missing Vitamins", [
            "Missing vitamins",
            "Scurvy",
            "Rickets",
            "Anaemia",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Too Much of a Good Thing
        self.next_band(6)
        self.write_rows(6, "Too Much of a Good Thing", [
            "Too much of a good thing",
            "Sugar",
            "Salt",
            "Fat",
        ], scale=0.9, box=0)

        last = Tex("A diet lacking nutrients causes deficiency diseases, and too much sugar, salt and fat can cause other diseases.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
