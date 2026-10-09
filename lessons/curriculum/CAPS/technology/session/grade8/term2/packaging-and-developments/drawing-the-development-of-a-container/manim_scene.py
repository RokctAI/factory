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

# Band-layout whiteboard scene for drawing-the-development-of-a-container (Part 1 Expert
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


class DevelopmentOfContainerSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Development Is
        self.write_rows(0, "What a Development Is", [
            "Flat pattern of every face, joined at folds",
            "Sheet material can only be cut and folded",
            "Cereal box: four sides, flaps, glue tab",
            "Eleven cube nets; test by folding",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Drawing the Development of a Box
        self.next_band(1)
        self.write_rows(1, "Drawing the Development of a Box", [
            "Sides in a row: 80, 40, 80, 40 by 120",
            "Top and bottom on an 80 side",
            "Cuts dark, folds dashed, mm and scale",
            "Every face once; neighbours match",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Tabs, Folds and Other Shapes
        self.next_band(2)
        self.write_rows(2, "Tabs, Folds and Other Shapes", [
            "Glue tab 10 to 15 mm on the last edge",
            "Glue flaps, tuck lid, dust flaps, angled corners",
            "Tray, prism, cylinder: same rule",
            "Nesting on the sheet; die-cut and crease",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Folds drawn as dark outlines''",
            "``No glue tab''",
            "``Flap on an edge of the wrong length''",
            "``A face drawn twice or missed''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Unfolding the Box
        self.next_band(4)
        self.write_rows(4, "Unfolding the Box", [
            "Open the glued edge, unfold",
            "Four sides, flaps, a tab",
            "Six squares in a cross",
            "Fold a copy to check",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Six Squares in a Cross
        self.next_band(5)
        self.write_rows(5, "Six Squares in a Cross", [
            "Side, end, side, end",
            "Top and bottom on the long side",
            "Dashed folds, dark cuts",
            "Six faces once; neighbours match",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Glue Flaps and Lids
        self.next_band(6)
        self.write_rows(6, "Glue Flaps and Lids", [
            "Tab down the last edge",
            "Lid with tongue, dust flaps",
            "Nick the corners",
            "Rectangle plus two circles",
        ], scale=0.9, box=0)

        last = Tex("A development lays every face flat, joined at dashed folds with dark cuts, true sizes in millimetres and tabs to hold it closed.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
