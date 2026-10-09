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

# Band-layout whiteboard scene for the-wedge-and-the-wheel-and-axle (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/180/140/120/110/100 of 840 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class WedgeWheelAxleSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The Wedge as a Moving Inclined Plane
        self.write_rows(0, "The Wedge as a Moving Inclined Plane", [
            "Inclined plane driven into a material",
            "Axe: swing down, split sideways",
            "Thinner wedge, greater advantage",
            "Door wedge: small push, strong hold",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): The Wheel and Axle
        self.next_band(1)
        self.write_rows(1, "The Wheel and Axle", [
            "Big wheel fixed to a small axle",
            "MA = wheel radius over axle radius",
            "Tap, screwdriver, steering wheel",
            "Drive the axle for speed: bicycle",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Where Both Are Used
        self.next_band(2)
        self.write_rows(2, "Where Both Are Used", [
            "Wedge: split, cut, lift, hold",
            "Wheel and axle: force, speed, less friction",
            "PAT: wedge foot, crank and axle",
            "Justify the choice",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A wedge pushes where you hit it''",
            "``A blunt knife is safer''",
            "``The axle does the hard work''",
            "``Anything round is a wheel and axle''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Ramp That Moves
        self.next_band(4)
        self.write_rows(4, "A Ramp That Moves", [
            "A ramp that moves",
            "Thin edge goes in, sides push apart",
            "Sharp knife, easy cut",
            "Door wedge jams",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Big Wheel, Thin Rod
        self.next_band(5)
        self.write_rows(5, "Big Wheel, Thin Rod", [
            "Big wheel, thin rod, turn together",
            "Gentle turn, strong force",
            "Bicycle: drive the rod, rim flies",
            "Trolleys roll, not scrape",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Spotting Them Around You
        self.next_band(6)
        self.write_rows(6, "Spotting Them Around You", [
            "Split or hold: wedge",
            "Turn with force: wheel and axle",
            "Speed: drive the axle",
            "PAT: foot and crank",
        ], scale=0.9, box=3)

        last = Tex("A wedge is a moving ramp, a wheel and axle is a spinning lever, and both trade distance for force.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
