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

# Band-layout whiteboard scene for indigenous-frame-homes (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/140/170/110/110/110 of 810 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class IndigenousFrameHomesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): A Framework of Poles
        self.write_rows(0, "A Framework of Poles", [
            "Thin poles in a circle",
            "Bent over and tied",
            "Dome frame: strong and stable",
            "Frame first, covering second",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): The Nama Matjieshuis
        self.next_band(1)
        self.write_rows(1, "The Nama Matjieshuis", [
            "Matjieshuis: mat house",
            "Bent sticks and reed mats",
            "Cool when hot, swells in rain",
            "Taken apart and moved",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Zulu and Xhosa Homes
        self.next_band(2)
        self.write_rows(2, "Zulu and Xhosa Homes", [
            "Zulu uguqa: pole frame, thatch",
            "Xhosa rontabile, ungqu-phantsi",
            "Thatch and mud walls",
            "Many crossings: stronger",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Traditional homes were weak''",
            "``The covering holds it up''",
            "``The matjieshuis never moved''",
            "``These homes are only history''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Poles First
        self.next_band(4)
        self.write_rows(4, "Poles First", [
            "Poles first",
            "Push in a circle",
            "Bend and tie",
            "Then cover",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): A House of Mats
        self.next_band(5)
        self.write_rows(5, "A House of Mats", [
            "A house of mats",
            "Reed mats",
            "Cool and dry",
            "Easy to move",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Grass, Mud and Models
        self.next_band(6)
        self.write_rows(6, "Grass, Mud and Models", [
            "Grass, mud and models",
            "Pole frames",
            "Thatch and mud",
            "Still built today",
        ], scale=0.9, box=3)

        last = Tex("Indigenous homes stand on a framework of tied poles, covered with reed mats, thatch or mud.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
