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

# Band-layout whiteboard scene for hemispheres (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (290/210/200/240/150/150/150 of 1390 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class HemispheresSession(MovingCameraScene):
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
        # --- Band 0: The four hemispheres
        self.write_rows(0, "The four hemispheres", [
            "Equator: Northern and Southern Hemispheres",
            "Prime meridian + 180\\textdegree{} meridian: Eastern and Western",
            "Johannesburg 26\\textdegree{}12'S 28\\textdegree{}03'E: Southern and Eastern",
            "0\\textdegree{} latitude, 0\\textdegree{} longitude: Gulf of Guinea",
        ], scale=0.8, box=1)
        # --- Band 1: Continents and oceans
        self.next_band(1)
        self.write_rows(1, "Continents and oceans", [
            "Africa: crossed by equator and prime meridian, all four",
            "Australia: south and east. South America: mostly south and west",
            "Pacific Ocean spans all four hemispheres",
            "Atlantic meets Indian Ocean at Cape Agulhas, about 20\\textdegree{}E",
        ], scale=0.72, box=0)
        # --- Band 2: Unequal halves
        self.next_band(2)
        self.write_rows(2, "Unequal halves", [
            "North: about two-thirds of the land",
            "North: about nine in ten people",
            "South: about four-fifths ocean",
            "Heat zones: tropical, temperate, frigid",
        ], scale=0.86, box=2)
        # --- Band 3: Opposite seasons
        self.next_band(3)
        self.write_rows(3, "Opposite seasons", [
            "January: summer in Johannesburg, winter in London",
            "Southern Cross points to the south",
            "Southern cyclones rotate clockwise",
            "Basins draining backwards: a myth",
        ], scale=0.8, box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Cut the orange two ways
        self.next_band(4)
        self.write_rows(4, "Cut the orange two ways", [
            "Around the middle: north and south",
            "Pole to pole, both sides: east and west",
            "Johannesburg: S and E",
        ], scale=0.86, box=2)
        # --- Band 5: Which halves hold what
        self.next_band(5)
        self.write_rows(5, "Which halves hold what", [
            "Africa: the only continent in all four",
            "North: most land, most people",
            "Atlantic west, Indian Ocean east, meeting at Cape Agulhas",
        ], scale=0.8, box=0)
        # --- Band 6: Christmas in summer
        self.next_band(6)
        self.write_rows(6, "Christmas in summer", [
            "Same day, opposite seasons",
            "Southern Cross in our sky",
            "Big storms spin clockwise here",
        ], scale=0.86, box=0)
        self.wait(4)
