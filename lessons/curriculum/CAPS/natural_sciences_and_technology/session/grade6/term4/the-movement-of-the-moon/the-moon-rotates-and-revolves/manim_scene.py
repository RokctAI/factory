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

# Band-layout whiteboard scene for the-moon-rotates-and-revolves (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/120/130/110/110/110 of 820 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TheMoonRotatesAndRevolvesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The Moon Revolves Around the Earth
        self.write_rows(0, "The Moon Revolves Around the Earth", [
            "Revolves around the Earth",
            "About a month",
            "Phases: how much lit half",
            "New to full and back",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): The Moon Rotates
        self.next_band(1)
        self.write_rows(1, "The Moon Rotates", [
            "Rotates on its axis",
            "About 28 days",
            "Same time as revolving",
            "Same face to Earth",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Together Around the Sun
        self.next_band(2)
        self.write_rows(2, "Together Around the Sun", [
            "Earth and Moon together",
            "Around the Sun in a year",
            "12 to 13 Moon trips",
            "Three movements",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``The Moon does not rotate''",
            "``Earth's shadow causes the phases''",
            "``The Moon changes its real shape''",
            "``The Moon orbits the Sun alone''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Around the Earth
        self.next_band(4)
        self.write_rows(4, "Around the Earth", [
            "Around the Earth",
            "Month",
            "Phases",
            "Gravity",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Same Face
        self.next_band(5)
        self.write_rows(5, "Same Face", [
            "Same face",
            "Spins",
            "28 days",
            "Dark patches",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Together Around the Sun
        self.next_band(6)
        self.write_rows(6, "Together Around the Sun", [
            "Together around the Sun",
            "Moon",
            "Earth",
            "Sun",
        ], scale=0.9, box=0)

        last = Tex("The Moon rotates and revolves in about a month, so it always shows us the same face, and it travels around the Sun with the Earth.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
