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

# Band-layout whiteboard scene for exploded-view-of-the-device (Part 1 Expert
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


class ExplodedViewOfTheDeviceSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What an Exploded View Is and Why Assembly Needs One
        self.write_rows(0, "What an Exploded View Is and Why Assembly Needs One", [
            "Assembled drawing hides inner parts",
            "Exploded: parts separated along an axis, orientation kept",
            "Furniture, manuals, kits",
            "Complements circuit, sketch, orthographic",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Drawing the Device Exploded: Axis, Order and Alignment Lines
        self.next_band(1)
        self.write_rows(1, "Drawing the Device Exploded: Axis, Order and Alignment Lines", [
            "Axis first: vertical for a lift-off lid",
            "Order: base, holder, board, lid, LED, button, screws",
            "Isometric, same scale, 30 degree grid",
            "Thin dashed alignment lines through holes",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Labelling, Parts List and Checking the Exploded Drawing
        self.next_band(2)
        self.write_rows(2, "Labelling, Parts List and Checking the Exploded Drawing", [
            "Balloons numbered from the base up",
            "Parts list: no., name, qty, material, size",
            "Title block: name, Exploded Assembly, NTS, date, team",
            "Checks: all drawn, all numbered, lines real, buildable",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Parts rotated so orientation is lost''",
            "``Parts scattered off the axis with no alignment lines''",
            "``Balloon numbers not matching the parts list''",
            "``Lid-mounted LED or switch left off the list''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Pull It Apart on Paper
        self.next_band(4)
        self.write_rows(4, "Pull It Apart on Paper", [
            "Pull it apart on paper",
            "Still the right way up",
            "Shows order and screws",
            "Assembly plan for making",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Everything in a Line
        self.next_band(5)
        self.write_rows(5, "Everything in a Line", [
            "Faint line, everything on it",
            "Bottom to top",
            "Gaps half a part",
            "Dashes join them",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Number Every Piece
        self.next_band(6)
        self.write_rows(6, "Number Every Piece", [
            "Circle with a number",
            "List matches balloons",
            "Note: solder first",
            "Could a stranger build it?",
        ], scale=0.9, box=3)

        last = Tex("An exploded view separates the parts along an axis in assembly order, in isometric with alignment lines, numbered balloons and a matching parts list.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
