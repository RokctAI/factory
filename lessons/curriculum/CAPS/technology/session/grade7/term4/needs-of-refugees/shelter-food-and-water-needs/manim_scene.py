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

# Band-layout whiteboard scene for shelter-food-and-water-needs (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/220/250/100/100/100 of 960 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ShelterFoodAndWaterNeedsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Water
        self.write_rows(0, "Water", [
            "15 to 20 litres each per day",
            "Drink 3, cook 3 to 6, wash 6 to 7",
            "Boil, chlorine, or filter then chlorine",
            "Covered storage; tap within 500 m",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Food
        self.next_band(1)
        self.write_rows(1, "Food", [
            "2 100 kilocalories each per day",
            "Staple, protein, fat, vegetables",
            "Adjust for babies, the sick, culture",
            "Big pots, little fuel, no fridge",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Shelter
        self.next_band(2)
        self.write_rows(2, "Shelter", [
            "3.5 square metres each; 21 for six",
            "Weatherproof for place and season",
            "Up in an hour; carried by two",
            "A month; door; 2 m fire gap",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Only 3 litres of drinking water''",
            "``Formula without safe water''",
            "``2 square metres per person''",
            "``Highveld shelter in Limpopo heat''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Water by the bucket
        self.next_band(4)
        self.write_rows(4, "Water by the bucket", [
            "One bucket each per day",
            "Hands, pots, bodies",
            "Three ways to make it safe",
            "250 people per tap at most",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Food that can be cooked there
        self.next_band(5)
        self.write_rows(5, "Food that can be cooked there", [
            "Four groups and salt",
            "Breast milk, soft porridge, rehydration",
            "No pork for Muslim families",
            "No ovens, no raw meat kept",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Shelter for six for a month
        self.next_band(6)
        self.write_rows(6, "Shelter for six for a month", [
            "About 4 by 5 metres",
            "Rain, wind, cold or sun, heat",
            "Ventilation for a stove",
            "Two adults, one hammer, one hour",
        ], scale=0.9, box=0)

        last = Tex("Water 15 to 20 litres treated and stored; food 2 100 kilocalories balanced and adjusted; shelter 3.5 square metres, weatherproof, quick, lasting a month.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
