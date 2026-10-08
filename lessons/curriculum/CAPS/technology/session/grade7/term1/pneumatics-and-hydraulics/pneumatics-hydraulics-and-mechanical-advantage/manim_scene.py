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

# Band-layout whiteboard scene for pneumatics-hydraulics-and-mechanical-advantage (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (220/150/170/110/110/110 of 870 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PneumaticsHydraulicsAndMechanicalAdvantageSession(MovingCameraScene):
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
        self.wait(47)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Fluids that carry a push
        self.write_rows(0, "Fluids that carry a push", [
            "Pneumatics: air. Hydraulics: liquid",
            "Pressure is force spread over area",
            "Bus door hisses: pneumatic",
            "Trolley jack lifts a taxi: hydraulic",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Small push, big push
        self.next_band(1)
        self.write_rows(1, "Small push, big push", [
            "Same pressure on a bigger face",
            "Four times the area: four times the force",
            "Big piston moves a quarter as far",
            "Reverse it to magnify movement",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Air is springy, water is not
        self.next_band(2)
        self.write_rows(2, "Air is springy, water is not", [
            "Air compresses and bounces back",
            "Water will not budge",
            "Firm, heavy, exact: hydraulic",
            "Light, fast, soft: pneumatic",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Hydraulics and pneumatics are the same''",
            "``The fluid creates the force''",
            "``Both pistons move the same distance''",
            "``Air is always the worse choice''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Pushing through a pipe
        self.next_band(4)
        self.write_rows(4, "Pushing through a pipe", [
            "Air: pneumatics",
            "Liquid: hydraulics",
            "Pressure travels along the pipe",
            "Doors, pumps, jacks, brakes",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Small piston in, big piston out
        self.next_band(5)
        self.write_rows(5, "Small piston in, big piston out", [
            "Two syringes and a tube of water",
            "Bigger face, bigger force",
            "Bigger force, shorter move",
            "Pump many times to lift a little",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Air squashes, water does not
        self.next_band(6)
        self.write_rows(6, "Air squashes, water does not", [
            "Blocked air syringe: squashes",
            "Blocked water syringe: stuck",
            "Oil for the Jaws of Life",
            "Water for our syringes",
        ], scale=0.9, box=1)

        last = Tex("Pressure travels through a fluid; a bigger piston face means a bigger force and a shorter move.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
