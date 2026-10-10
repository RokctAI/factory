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

# Band-layout whiteboard scene for the-sea-route-to-the-east-around-southern-africa (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/140/150/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TheSeaRouteToTheEastAroundSouthernAfricaSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Step by Step down Africa
        self.write_rows(0, "Step by Step down Africa", [
            "1434: past Cape Bojador",
            "1470s: across the equator",
            "About 1486: Cape Cross",
            "Swing out into the Atlantic",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Rounding the Cape
        self.next_band(1)
        self.write_rows(1, "Rounding the Cape", [
            "Dias left Lisbon, 1487",
            "Storm blew him south, 1488",
            "Landed at Mossel Bay",
            "Cape of Good Hope",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): The Route to the East
        self.next_band(2)
        self.write_rows(2, "The Route to the East", [
            "Lisbon, Cape, East Africa, India",
            "About six months or more",
            "The Cape: halfway stop",
            "Main route until 1869",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``One voyage to the Cape''",
            "``Dias saw the tip going out''",
            "``Dias reached India''",
            "``Cape of Good Hope is most southern''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Little Further Each Time
        self.next_band(4)
        self.write_rows(4, "A Little Further Each Time", [
            "West coast",
            "Step",
            "Step",
            "Namibia",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Blown Past the Tip
        self.next_band(5)
        self.write_rows(5, "Blown Past the Tip", [
            "Storm",
            "Dias",
            "Mossel Bay",
            "Good Hope",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Halfway to India
        self.next_band(6)
        self.write_rows(6, "Halfway to India", [
            "Water",
            "Meat",
            "Repairs",
            "Winds",
        ], scale=0.9, box=0)

        last = Tex("Step by step, Portuguese sailors found the stormy sea route around southern Africa, and the Cape became a halfway stop to the East.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
