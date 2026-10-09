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

# Band-layout whiteboard scene for design-brief-feeding-one-hundred-refugees (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (220/210/220/100/100/100 of 950 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DesignBriefFeedingOneHundredSession(MovingCameraScene):
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
        self.wait(60)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The brief and specifications
        self.write_rows(0, "The brief and specifications", [
            "What, for whom, why",
            "2 100 kcal; four groups daily",
            "400 g staple, 60 g protein, 25 g oil",
            "Soft food; no pork; cooked within 2 h",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): One nutritious, tasty meal
        self.next_band(1)
        self.write_rows(1, "One nutritious, tasty meal", [
            "Pap, pilchard relish, cabbage",
            "Recipe for ten, then times ten",
            "Fits two pots and one hour",
            "Nutrition, flavour, texture",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Costing and checking
        self.next_band(2)
        self.write_rows(2, "Costing and checking", [
            "About R8.35 a plate; R18 a day",
            "Over budget? Beans for fish",
            "Check the mix and the kitchen",
            "One page; the morning cook reads it",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Feed the refugees, no numbers''",
            "``Needs an oven, a fridge, three hours''",
            "``Scaled by guessing''",
            "``Only the main meal costed''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Write the brief
        self.next_band(4)
        self.write_rows(4, "Write the brief", [
            "One or two sentences",
            "Numbers for the food",
            "Limits on the kitchen",
            "Two columns",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Plan the meal
        self.next_band(5)
        self.write_rows(5, "Plan the meal", [
            "Four groups, two pots",
            "12 kg meal, 20 tins, 5 cabbages",
            "Stiff for adults, soft for children",
            "Three criteria",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Cost it and check it
        self.next_band(6)
        self.write_rows(6, "Cost it and check it", [
            "Price list times quantities",
            "Inside R20 a head",
            "Soft, extra, rehydration, no pork, rice",
            "Brief, columns, recipes, cost, criteria",
        ], scale=0.9, box=1)

        last = Tex("A brief with quantified specifications and kitchen constraints, a four-group meal written for ten and scaled to one hundred, costed within budget and judged on nutrition, flavour and texture.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
