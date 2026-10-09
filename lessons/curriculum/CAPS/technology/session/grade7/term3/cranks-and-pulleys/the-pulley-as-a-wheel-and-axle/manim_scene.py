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

# Band-layout whiteboard scene for the-pulley-as-a-wheel-and-axle (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/220/220/100/100/100 of 920 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ThePulleyAsAWheelAndAxleSession(MovingCameraScene):
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
        self.wait(70)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): A pulley is a wheel and axle
        self.write_rows(0, "A pulley is a wheel and axle", [
            "Grooved wheel on an axle, rope in groove",
            "Guides a rope with little friction",
            "Flagpoles, blinds, lifts, cranes",
            "Fixed pulley: 200 g needs 200 g, MA 1",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Fixed, movable, rope count
        self.next_band(1)
        self.write_rows(1, "Fixed, movable, rope count", [
            "Fixed: direction only",
            "Movable on the load: effort halves",
            "MA = ropes holding the load",
            "Friction: measure, do not assume",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): A pulley at the crane's tip
        self.next_band(2)
        self.write_rows(2, "A pulley at the crane's tip", [
            "Light and grooved: bead or tube",
            "Axle at right angles, held both sides",
            "Optional movable pulley on the hook",
            "Heavy reel tips the crane",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A fixed pulley halves the effort''",
            "``Counting the pulled rope''",
            "``Tip pulley with no groove''",
            "``Cotton reel at the tip''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A wheel for a rope
        self.next_band(4)
        self.write_rows(4, "A wheel for a rope", [
            "Two circles on one centre",
            "Rope round a corner, no rubbing",
            "Pull down to lift up",
            "Advantage one",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Halving the pull
        self.next_band(5)
        self.write_rows(5, "Halving the pull", [
            "Tie, under, over, down to hand",
            "Balance reads 100",
            "Two ropes share the load",
            "Count the ropes",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Fit the crane's pulley
        self.next_band(6)
        self.write_rows(6, "Fit the crane's pulley", [
            "Bead on a wire through the tip",
            "Should turn, not drag",
            "Too heavy? Movable pulley",
            "Write down why",
        ], scale=0.9, box=1)

        last = Tex("A pulley is a wheel and axle that guides a rope; a fixed one changes direction, a movable one halves effort, and advantage equals ropes holding the load.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
