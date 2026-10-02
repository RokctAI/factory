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

# Band-layout whiteboard scene for urbanisation-and-working-class-living-conditions (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (220/180/180/280/150/150/150 of 1310 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class UrbanisationAndWorkingClassLivingConditionsSession(MovingCameraScene):
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
        # --- Band 0: Overcrowded housing
        self.write_rows(0, "Overcrowded housing", [
            "Towns grew fast; no building rules",
            "Back-to-back houses: windows on one side only",
            "Courts, cellars and lodging houses",
            "Coal smoke and soot over everything",
        ], scale=0.86, box=1)
        # --- Band 1: Dirt, water and disease
        self.next_band(1)
        self.write_rows(1, "Dirt, water and disease", [
            "One privy for 20 households; shared pumps",
            "Cholera and typhoid: dirty water. Typhus: lice",
            "Tuberculosis: damp crowded rooms",
            "Chadwick 1842, Manchester: professionals 38, labourers 17",
        ], scale=0.8, box=3)
        # --- Band 2: Public health reform
        self.next_band(2)
        self.write_rows(2, "Public health reform", [
            "1848 Public Health Act: permissive",
            "1854 John Snow: the Broad Street pump",
            "1858 Great Stink: Bazalgette's sewers",
            "1875 Public Health Act: compulsory",
        ], scale=0.86, box=1)
        # --- Band 3: Poverty and the workhouse
        self.next_band(3)
        self.write_rows(3, "Poverty and the workhouse", [
            "1834 Poor Law Amendment Act",
            "Less eligibility: worse than the poorest worker outside",
            "Families separated, uniforms, stone breaking, oakum",
            "Feared and shamed: Oliver Twist",
        ], scale=0.8, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Twelve people, one room
        self.next_band(4)
        self.write_rows(4, "Twelve people, one room", [
            "Back to back, no fresh air",
            "Lodgers to pay the rent",
            "Cellars for the poorest",
        ], scale=0.86)
        # --- Band 5: Dirty water, deadly disease
        self.next_band(5)
        self.write_rows(5, "Dirty water, deadly disease", [
            "One toilet, one tap, one river",
            "Cholera killed more than 50 000 in 1848 to 1849",
            "Snow's map: the pump was the killer",
        ], scale=0.86, box=2)
        # --- Band 6: The house nobody wanted to enter
        self.next_band(6)
        self.write_rows(6, "The house nobody wanted to enter", [
            "No pension, no unemployment pay",
            "The workhouse: worse than any job outside",
            "Families split at the door",
        ], scale=0.86, box=1)
        self.wait(4)
