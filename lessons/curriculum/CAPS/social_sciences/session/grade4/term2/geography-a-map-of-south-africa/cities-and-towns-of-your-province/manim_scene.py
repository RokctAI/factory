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

# Band-layout whiteboard scene for cities-and-towns-of-your-province (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/160/190/110/110/110 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CitiesAndTownsOfYourProvinceSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Main Cities and Towns
        self.write_rows(0, "Main Cities and Towns", [
            "Dots and stars for towns",
            "Gauteng: Johannesburg, Pretoria",
            "KZN: Pietermaritzburg, Durban",
            "Know your own province",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Finding Your Own Settlement on a Map
        self.next_band(1)
        self.write_rows(1, "Finding Your Own Settlement on a Map", [
            "Find your province",
            "Find the capital star",
            "Find your town, or the nearest",
            "Index and grid reference",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Describing Where You Live
        self.next_band(2)
        self.write_rows(2, "Describing Where You Live", [
            "Settlement, province, nearby city",
            "Add a compass direction",
            "North-east of Polokwane",
            "Home, settlement, province, country",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Every village is on the map''",
            "``No province named''",
            "``The capital is always the biggest''",
            "``North-east of nowhere''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Big Places
        self.next_band(4)
        self.write_rows(4, "Big Places", [
            "Capital cities",
            "Big towns",
            "Your province",
            "Stars on the map",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Find Your Place
        self.next_band(5)
        self.write_rows(5, "Find Your Place", [
            "Province",
            "Capital",
            "Your town",
            "Index",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Say Where You Live
        self.next_band(6)
        self.write_rows(6, "Say Where You Live", [
            "Settlement",
            "Province",
            "Big place nearby",
            "Direction",
        ], scale=0.9, box=3)

        last = Tex("Every province has a capital and main towns, and we can find and describe where our own settlement is.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
