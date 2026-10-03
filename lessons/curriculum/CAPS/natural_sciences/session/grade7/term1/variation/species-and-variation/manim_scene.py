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

# Band-layout whiteboard scene for species-and-variation (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (120/150/170/120/120/120 of 800 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SpeciesAndVariationSession(MovingCameraScene):
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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): What a species is
        self.write_rows(0, "What a species is", [
            "Species: breed together, fertile offspring",
            "Horse + donkey = mule (infertile): two species",
            "Great Dane and Chihuahua: one species",
            "Population: same species, same place, same time",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Variation
        self.next_band(1)
        self.write_rows(1, "Variation", [
            "Variation: no two individuals alike",
            "Continuous: any value in a range (height, mass)",
            "Discontinuous: distinct groups (blood group A, B, AB, O)",
            "Continuous gives a bell curve; discontinuous, separate bars",
        ], scale=0.76, box=2)

        # --- Band 2 (subtopic_3): Causes of variation
        self.next_band(2)
        self.write_rows(2, "Causes of variation", [
            "Inherited: genes from both parents mix",
            "Environmental: food, climate, exercise, disease",
            "Many features: both (height)",
            "Variation helps a species survive change",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Variation is between species''",
            "``Height is discontinuous''",
            "``All variation is inherited''",
            "``Different breeds are different species''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): One kind, many looks
        self.next_band(4)
        self.write_rows(4, "One kind, many looks", [
            "Nguni cattle: many looks, one species",
            "Species: babies that can have babies",
            "Horse + donkey = mule, which cannot breed",
            "All humans: one species",
        ], scale=0.88, box=1)

        # --- Band 5 (subtopic_5): Smooth or in groups
        self.next_band(5)
        self.write_rows(5, "Smooth or in groups", [
            "Line-up by height: smooth, continuous",
            "Blood group: four groups, discontinuous",
            "Heights graph: a hill shape",
            "Blood groups graph: separate bars",
        ], scale=0.88, box=0)

        # --- Band 6 (subtopic_6): Genes and life
        self.next_band(6)
        self.write_rows(6, "Genes and life", [
            "Genes: half from each parent, a new mix",
            "Life: food, sun, sport, accidents",
            "Many features come from both",
            "Variation helps survival and breeding",
        ], scale=0.88, box=3)

        last = Tex("Same species, never identical: that is variation.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
