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

# Band-layout whiteboard scene for an-ancient-african-society (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/180/200/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AnAncientAfricanSocietySession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Where and When
        self.write_rows(0, "Where and When", [
            "North-eastern Africa",
            "Along the Nile, flowing north",
            "United about 5,100 years ago",
            "Lasted about 3,000 years",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): An African Society
        self.next_band(1)
        self.write_rows(1, "An African Society", [
            "An African society",
            "Neighbour: Kush",
            "An early civilisation",
            "Pyramids, writing, maths",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): How We Know
        self.next_band(2)
        self.write_rows(2, "How We Know", [
            "Buildings and wall paintings",
            "Writing on stone and papyrus",
            "Objects and mummies",
            "Dry desert preserved them",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Egypt was not in Africa''",
            "``It lasted a few hundred years''",
            "``The Nile flows south''",
            "``Only stories tell us''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Where and When
        self.next_band(4)
        self.write_rows(4, "Where and When", [
            "Africa",
            "Nile",
            "Pharaoh",
            "3,000 years",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): African and Great
        self.next_band(5)
        self.write_rows(5, "African and Great", [
            "African",
            "Kush",
            "Pyramids",
            "Writing",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): How We Know
        self.next_band(6)
        self.write_rows(6, "How We Know", [
            "Walls",
            "Papyrus",
            "Objects",
            "Mummies",
        ], scale=0.9, box=2)

        last = Tex("Ancient Egypt was a great African civilisation along the Nile, and its buildings, writing and objects tell us about it.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
