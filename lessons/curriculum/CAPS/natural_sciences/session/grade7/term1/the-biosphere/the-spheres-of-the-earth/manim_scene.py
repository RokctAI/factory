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

# Band-layout whiteboard scene for the-spheres-of-the-earth (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/180/160/130/120/120/120 of 1010 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TheSpheresOfTheEarthSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The three non-living spheres
        self.write_rows(0, "The three non-living spheres", [
            "Lithosphere: rock, mountains, ocean floor, soil",
            "Hydrosphere: oceans, rivers, groundwater, ice, clouds",
            "Atmosphere: about 78\\% nitrogen, 21\\% oxygen, a little CO2",
            "Spheres overlap: water in soil, air in water",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): The biosphere
        self.next_band(1)
        self.write_rows(1, "The biosphere", [
            "Bios = life: the zone where life exists",
            "Living organisms + dead organic matter",
            "Thin film: roots below, birds above, sunlit sea",
            "A handful of soil holds all four spheres",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Spheres in conversation
        self.next_band(2)
        self.write_rows(2, "Spheres in conversation", [
            "Water: evaporate, transpire, condense, rain, run off",
            "Carbon: plants take CO2 in; respiration gives it back",
            "Weathering: rain and wind break rock into soil",
            "Overgrazing: bare soil, eroded, silted dams",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_4): Exam layout
        self.next_band(3)
        self.write_rows(3, "Exam layout", [
            "Definition: name + root word + what it contains",
            "Example: something specific, like the Vaal River",
            "Interaction: name both spheres and the process",
            "Pond test: water, mud, bubbles, frogs and reeds",
        ], scale=0.82, box=2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        em = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``The biosphere is a layer above the air''",
            "``Dead leaves are not part of the biosphere''",
            "``The hydrosphere is only the oceans''",
            "``Air is mostly oxygen''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.78).shift(band_shift(4) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): One handful, four spheres
        self.next_band(5)
        self.write_rows(5, "One handful, four spheres", [
            "Grains of sand and clay: lithosphere",
            "Water when you squeeze: hydrosphere",
            "Air in the gaps: atmosphere",
            "Roots, worms, fungus, rotting leaves: biosphere",
        ], scale=0.82, box=3)

        # --- Band 6 (subtopic_6): The planet sandwich
        self.next_band(6)
        self.write_rows(6, "The planet sandwich", [
            "Rock is the bread, water the filling, air the cover",
            "Life lives where the layers touch",
            "Thinner than an apple's skin",
            "Dead leaves get recycled into plant food",
        ], scale=0.82, box=1)

        # --- Band 7 (subtopic_7): Everything is connected
        self.next_band(7)
        self.write_rows(7, "Everything is connected", [
            "Water: sea, air, cloud, rain, river, roots",
            "Gases: plants give oxygen, animals give CO2",
            "Rock to soil; bare soil to muddy dams",
            "Change one sphere and the others feel it",
        ], scale=0.88, box=3)

        last = Tex("Land, water, air and life: the biosphere is where they meet.").scale(0.9).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
