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

# Band-layout whiteboard scene for stiffening-by-tubing-and-folding (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (260/160/190/110/110/110 of 940 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class StiffeningByTubingAndFoldingSession(MovingCameraScene):
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
        self.wait(43)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Stability, strength, rigidity
        self.write_rows(0, "Stability, strength, rigidity", [
            "Stable: does not topple",
            "Strong: does not break; rigid: does not bend",
            "Ruler strong not rigid; biscuit rigid not strong",
            "Shape moves material away from the middle",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Investigation: tubing
        self.next_band(1)
        self.write_rows(1, "Investigation: tubing", [
            "Flat sheet: collapses under one coin",
            "Tube: dozens of coins, holds a textbook",
            "Fails by the wall buckling inward",
            "Wider is stiffer until the wall buckles",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Investigation: folding
        self.next_band(2)
        self.write_rows(2, "Investigation: folding", [
            "Pleated sheet carries as much as the tube",
            "Narrow sharp folds are stiffer",
            "Folds across the span: collapses",
            "Corrugated iron, cardboard, car floors",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``The tube is stronger than the sheet''",
            "``Fold across the span''",
            "``Wider tube is always better''",
            "``Stable means rigid''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Three words, not the same
        self.next_band(4)
        self.write_rows(4, "Three words, not the same", [
            "Fall over, break, bend",
            "Ruler versus biscuit",
            "Thicker, more bars, or new shape",
            "Shape is free stiffness",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Roll it into a tube
        self.next_band(5)
        self.write_rows(5, "Roll it into a tube", [
            "One coin flat; dozens as a tube",
            "Caves in at the middle",
            "Fat tube stiffer, wall weaker",
            "Straws, poles, bones, mast legs",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Fold it like a fan
        self.next_band(6)
        self.write_rows(6, "Fold it like a fan", [
            "Zigzag along the length",
            "Sharp narrow folds win",
            "Wrong way: collapses",
            "Roofs, cardboard, tin lids, palm leaves",
        ], scale=0.9, box=2)

        last = Tex("Same material, new shape: tubes and folds move material from the middle and make it rigid for free.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
