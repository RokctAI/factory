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

# Band-layout whiteboard scene for refraction-prisms-and-lenses (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (220/230/240/230/180/190/180 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RefractionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1)
        self.write_rows(0, 'What refraction is', [
            'Change of direction at a boundary',
            'Caused by a change of speed',
            'Slows: bends towards the normal',
            'Along the normal: no bending',
        ], scale=0.8, box=0)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, 'Everyday refraction', [
            'Bent pencil in water',
            'Pools look 3/4 of real depth',
            'Mirages on hot roads',
            'Twinkling stars',
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, 'Lenses', [
            'Convex: thick middle, converges',
            'Concave: thin middle, diverges',
            'Focal point and focal length',
            'Glass in veld can start fires',
        ], scale=0.8, box=1)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, 'Uses of lenses', [
            'Short sight: concave lens',
            'Long sight: convex lens',
            'Magnifying glass, camera, projector',
            'Microscope and telescope',
        ], scale=0.8, box=0)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        errs = [
            "``Into air bends towards normal''",
            "``Refraction is bouncing''",
            "``Along the normal it bends''",
            "``Concave converges''",
        ]
        for i, e in enumerate(errs):
            m = Tex(e).scale(0.85).shift(band_shift(4) + UP * (1.3 - 1.0 * i))
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5)
        self.next_band(5)
        self.write_rows(5, 'A pencil in a glass of water', [
            'Light slows in water',
            'Bends at the surface',
            'Brain assumes straight lines',
        ], scale=0.85, box=1)

        # --- Band 6 (subtopic_6)
        self.next_band(6)
        self.write_rows(6, 'Tricks of the water and air', [
            'Pools look shallow',
            'Mirage: sky on the road',
            'Twinkling stars',
        ], scale=0.85, box=2)

        # --- Band 7 (subtopic_7)
        self.next_band(7)
        self.write_rows(7, 'Spectacles, cameras, telescopes', [
            'Convex: brings light together',
            'Concave: spreads it out',
            'Lenses everywhere',
        ], scale=0.85, box=0)

        last = Tex('Change the speed, change the direction.').scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
