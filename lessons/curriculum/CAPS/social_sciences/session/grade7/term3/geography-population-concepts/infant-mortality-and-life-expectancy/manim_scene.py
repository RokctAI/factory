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

# Band-layout whiteboard scene for infant-mortality-and-life-expectancy (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/170/190/190/90/90/100 of 1010 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class InfantMortalityAndLifeExpectancySession(MovingCameraScene):
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
        # --- Band 0: The Infant Mortality Rate
        self.write_rows(0, "The Infant Mortality Rate", [
            "Infant deaths under 1, per 1000 live births",
            "100 / 4000 x 1000 = 25",
            "World: about 140 in 1950, about 28 now",
            "SA about 24; Japan about 2",
        ], scale=0.86, box=0)
        # --- Band 1: Why Infants Die and How to Prevent It
        self.next_band(1)
        self.write_rows(1, "Why Infants Die and How to Prevent It", [
            "Causes: birth problems, diarrhoea, pneumonia",
            "Clean water and oral rehydration",
            "Immunisation and breastfeeding",
            "Mothers' education saves lives",
        ], scale=0.86, box=1)
        # --- Band 2: Life Expectancy
        self.next_band(2)
        self.write_rows(2, "Life Expectancy", [
            "Average years a newborn can expect to live",
            "Child deaths pull the average down",
            "World: about 30 in 1900, about 73 now",
            "SA: fell to about 53 with AIDS, then recovered",
        ], scale=0.8, box=3)
        # --- Band 3: Using the Indicators
        self.next_band(3)
        self.write_rows(3, "Using the Indicators", [
            "Developed: low infant deaths, long lives",
            "SA: big differences between rich and poor",
            "UN goals: end preventable child deaths by 2030",
            "Check the date and the source",
        ], scale=0.8, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Babies Under One
        self.next_band(4)
        self.write_rows(4, "Babies Under One", [
            "Deaths before age one",
            "Per 1000 babies born alive",
            "World: 140 then, 28 now",
        ], scale=0.86, box=0)
        # --- Band 5: Keeping Babies Alive
        self.next_band(5)
        self.write_rows(5, "Keeping Babies Alive", [
            "Clean water and toilets",
            "Vaccinations and breastfeeding",
            "Sugar and salt water for diarrhoea",
        ], scale=0.86, box=0)
        # --- Band 6: How Long We Live
        self.next_band(6)
        self.write_rows(6, "How Long We Live", [
            "World: about 30 then, about 73 now",
            "SA: AIDS, then recovery",
            "Numbers show where help is needed",
        ], scale=0.86, box=0)
        self.wait(4)
