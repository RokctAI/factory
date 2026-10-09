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

# Band-layout whiteboard scene for single-movable-pulley (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/180/160/120/110/90 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SingleMovablePulleySession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): A Pulley That Rides on the Rope
        self.write_rows(0, "A Pulley That Rides on the Rope", [
            "Block on the load; rope fixed above",
            "Pulley rides up the rope",
            "Scaffold buckets, dinghies, crane hooks",
            "Alone: pull upward, awkward",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Two Rope Sections, Half the Effort
        self.next_band(1)
        self.write_rows(1, "Two Rope Sections, Half the Effort", [
            "Two sections support the load",
            "One rope, one tension: each carries half",
            "Effort = load / 2; MA = 2",
            "MA = number of supporting sections",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Measuring the Movable Pulley and Its Trade-Off
        self.next_band(2)
        self.write_rows(2, "Measuring the Movable Pulley and Its Trade-Off", [
            "Fixed: 20 N, 300 mm, down; movable: ~10 N, 600 mm, up",
            "Measured ~1.8: block weight + friction",
            "Actual / ideal = efficiency",
            "Heavier load, closer to 2",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Effort rope over a fixed pulley counted as supporting''",
            "``Block weight forgotten''",
            "``Load rises as far as rope is pulled''",
            "``Movable pulley changes direction alone''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): The Wheel Goes Up With the Load
        self.next_band(4)
        self.write_rows(4, "The Wheel Goes Up With the Load", [
            "Pulley moves with the bucket",
            "Tie, round, up to your hand",
            "Mortar, boats, crane hooks",
            "Pull up for now",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Two Strings Share the Weight
        self.next_band(5)
        self.write_rows(5, "Two Strings Share the Weight", [
            "Count: two strings",
            "Each holds half",
            "Pull half: MA 2",
            "Rope pulled: double",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Half the Pull, Twice the Rope
        self.next_band(6)
        self.write_rows(6, "Half the Pull, Twice the Rope", [
            "Table both pulleys",
            "A bit under 2 is honest",
            "Efficiency about 90\\%",
            "Fixed pulley on top next",
        ], scale=0.9, box=1)

        last = Tex("A movable pulley hangs the load from two rope sections, halving the effort for twice the rope: mechanical advantage 2, found by counting supporting sections.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
