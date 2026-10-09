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

# Band-layout whiteboard scene for revision-mechanical-advantage-and-strengthening-frames (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/210/210/100/100/100 of 900 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RevisionMechanicalAdvantageAndFramesSession(MovingCameraScene):
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
        self.wait(60)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Mechanical advantage revisited
        self.write_rows(0, "Mechanical advantage revisited", [
            "MA = load over effort; costs distance",
            "Lever, crank, wheel, pulley, gear",
            "Crane: crank six, pulley one",
            "Movable pulley: twelve",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Strengthening frames revisited
        self.next_band(1)
        self.write_rows(1, "Strengthening frames revisited", [
            "Bend: tube, L, U, box",
            "Fold: diagonal or gusset",
            "Tip: wide base, weight at back",
            "Joints: overlap, tab, sleeve",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Apply both to the sketch
        self.next_band(2)
        self.write_rows(2, "Apply both to the sketch", [
            "Load path: magnet to base",
            "Effort path: hand to magnet",
            "Numbers one side, stiffeners the other",
            "Rubric rewards both",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Tip pulley multiplies the crank''",
            "``Flat strip mast''",
            "``Rectangles with no diagonals''",
            "``Cells up the mast''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Advantage, again
        self.next_band(4)
        self.write_rows(4, "Advantage, again", [
            "Load over effort",
            "Handle over drum; count the ropes",
            "Crane total: six",
            "Write the chain",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Frames, again
        self.next_band(5)
        self.write_rows(5, "Frames, again", [
            "Bend, fold, tip",
            "Tube, triangle, base",
            "Cells at the back",
            "Sleeve the arm joint",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Walk the sketch
        self.next_band(6)
        self.write_rows(6, "Walk the sketch", [
            "Backwards: will it hold?",
            "Forwards: what is the advantage?",
            "Second colour for stiffeners",
            "Mechanism and structure",
        ], scale=0.9, box=3)

        last = Tex("Advantage is load over effort and multiplies along the chain; frames are strengthened by shape, triangles and a weighted base; the crane needs both.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
