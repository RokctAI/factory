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

# Band-layout whiteboard scene for pandemics-spanish-flu-and-covid-19 (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/170/180/170/90/90/90 of 950 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class PandemicsSpanishFluAndCovid19Session(MovingCameraScene):
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
        # --- Band 0: Epidemics and Pandemics
        self.write_rows(0, "Epidemics and Pandemics", [
            "Epidemic: many cases in one area",
            "Pandemic: spreads across continents",
            "Endemic: always present at a steady level",
            "Pandemics cause spikes in death rates",
        ], scale=0.86, box=1)
        # --- Band 1: The Spanish Flu, 1918 to 1920
        self.next_band(1)
        self.write_rows(1, "The Spanish Flu, 1918 to 1920", [
            "Influenza pandemic, 1918 to 1920",
            "Name from Spanish newspapers, not origin",
            "About 500 million infected",
            "Deaths: about 20 to 50 million or more",
        ], scale=0.86, box=3)
        # --- Band 2: Black October in South Africa
        self.next_band(2)
        self.write_rows(2, "Black October in South Africa", [
            "Arrived September 1918 on troopships",
            "Spread along railway lines",
            "Black October: about 300 000 deaths",
            "1919: Public Health Act",
        ], scale=0.86, box=3)
        # --- Band 3: Comparing with COVID-19
        self.next_band(3)
        self.write_rows(3, "Comparing with COVID-19", [
            "COVID-19: coronavirus, pandemic from 2020",
            "Both spread through the air; came in waves",
            "COVID-19: tests and vaccines within a year",
            "Spanish flu: no vaccine, no antibiotics",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: What Is a Pandemic?
        self.next_band(4)
        self.write_rows(4, "What Is a Pandemic?", [
            "Epidemic: one area",
            "Pandemic: the whole world",
            "Death rates jump",
        ], scale=0.86, box=0)
        # --- Band 5: The Spanish Flu
        self.next_band(5)
        self.write_rows(5, "The Spanish Flu", [
            "1918 to 1920; no vaccine",
            "Came on ships, spread by railway",
            "Black October: about 300 000 SA deaths",
        ], scale=0.86, box=0)
        # --- Band 6: COVID-19 Compared
        self.next_band(6)
        self.write_rows(6, "COVID-19 Compared", [
            "Both: new viruses, waves, masks",
            "COVID-19: tests and vaccines",
            "Planes spread COVID-19 faster",
        ], scale=0.86, box=0)
        self.wait(4)
