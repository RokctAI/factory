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

# Band-layout whiteboard scene for the-moons-orbit (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (120/160/140/120/120/120 of 780 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TheMoonsOrbitSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The Moon
        self.write_rows(0, "The Moon", [
            "Earth's natural satellite",
            "About 384 000 km away; gravity ⅙ of Earth's",
            "No air, no water; craters and maria",
            "Vredefort Dome: a crater on Earth",
        ], scale=0.88, box=1)

        # --- Band 1 (subtopic_2): The Moon's orbit
        self.next_band(1)
        self.write_rows(1, "The Moon's orbit", [
            "Orbit: 27,3 days; full to full: 29,5 days",
            "Spins once per orbit: same face to Earth",
            "Gravity pulls; sideways motion carries",
            "Rises about 50 min later each night",
        ], scale=0.88, box=3)

        # --- Band 2 (subtopic_3): Moonlight and phases
        self.next_band(2)
        self.write_rows(2, "Moonlight and phases", [
            "Moonlight = reflected sunlight",
            "Half always lit; we see different amounts",
            "New, crescent, quarter, gibbous, full",
            "Waxing grows, waning shrinks",
        ], scale=0.88, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``The Moon makes its own light''",
            "``Phases are Earth's shadow''",
            "``The Moon does not rotate''",
            "``The far side is always dark''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Our Moon
        self.next_band(4)
        self.write_rows(4, "Our Moon", [
            "Natural satellite of Earth",
            "Rock, no air, no water",
            "Craters from space rocks",
            "Weak gravity: astronauts bounce",
        ], scale=0.88, box=1)

        # --- Band 5 (subtopic_5): Round and round
        self.next_band(5)
        self.write_rows(5, "Round and round", [
            "Once around the Earth: about a month",
            "Spins once per trip: same face",
            "Gravity holds it",
            "Month comes from Moon",
        ], scale=0.88, box=2)

        # --- Band 6 (subtopic_6): The changing Moon
        self.next_band(6)
        self.write_rows(6, "The changing Moon", [
            "Moonlight is bounced sunlight",
            "Half always lit",
            "New, crescent, half, full, back again",
            "Waxing grows, waning shrinks",
        ], scale=0.88, box=1)

        last = Tex("The Moon orbits Earth in about a month; sunlight makes its phases.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
