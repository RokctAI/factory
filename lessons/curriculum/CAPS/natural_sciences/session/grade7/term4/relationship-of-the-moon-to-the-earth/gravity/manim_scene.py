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

# Band-layout whiteboard scene for gravity (Part 1 Expert
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


class GravitySession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What gravity is
        self.write_rows(0, "What gravity is", [
            "Gravity: pull between all objects with mass",
            "Mass: amount of matter (kg)",
            "Non-contact; acts across space",
            "Newton: falling apple = orbiting Moon",
        ], scale=0.88, box=1)

        # --- Band 1 (subtopic_2): Mass and distance
        self.next_band(1)
        self.write_rows(1, "Mass and distance", [
            "More mass: stronger pull",
            "More distance: weaker pull (double distance, ¼ force)",
            "Mass (kg) stays the same; weight (N) changes",
            "Moon: hammer and feather land together",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Orbits
        self.next_band(2)
        self.write_rows(2, "Orbits", [
            "Sideways motion + gravity = curved orbit",
            "The Moon is always falling and missing",
            "String and stopper: let go, it flies straight",
            "Sun holds the planets; Moon drifts away slowly",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``No gravity in space''",
            "``Mass and weight are the same''",
            "``Heavy things always fall faster''",
            "``The Moon is not falling''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): The invisible pull
        self.next_band(4)
        self.write_rows(4, "The invisible pull", [
            "Gravity: pull between things with mass",
            "Everything pulls; big things pull strongly",
            "Works without touching",
            "Works across space",
        ], scale=0.88, box=1)

        # --- Band 5 (subtopic_5): Bigger is stronger, further is weaker
        self.next_band(5)
        self.write_rows(5, "Bigger is stronger, further is weaker", [
            "More mass: stronger pull",
            "Further away: weaker pull",
            "Mass stays; weight changes",
            "Moon: one sixth the pull",
        ], scale=0.88, box=2)

        # --- Band 6 (subtopic_6): Falling around
        self.next_band(6)
        self.write_rows(6, "Falling around", [
            "Sideways speed + pull = orbit",
            "String and stopper",
            "Sun holds the Earth",
            "Further away: weaker",
        ], scale=0.88, box=1)

        last = Tex("More mass, more pull; more distance, less pull: gravity holds orbits.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
