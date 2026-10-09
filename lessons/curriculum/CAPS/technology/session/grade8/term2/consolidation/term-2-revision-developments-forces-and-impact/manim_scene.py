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

# Band-layout whiteboard scene for term-2-revision-developments-forces-and-impact (Part 1 Expert
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


class Term2RevisionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Developments: Nets of Containers Revisited
        self.write_rows(0, "Developments: Nets of Containers Revisited", [
            "Base, four sides, lid, flaps",
            "Dashed folds, solid cuts, labelled flaps",
            "Six faces; matching edges",
            "Tray is a cross; prism adds triangles",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Forces on Materials and the Shapes That Resist Them
        self.next_band(1)
        self.write_rows(1, "Forces on Materials and the Shapes That Resist Them", [
            "What is the load doing to the part?",
            "Chain: tension; seat: bending; spindle: torsion",
            "Steel near the stretched face; plywood crossed",
            "I for bending; tubes for squash and twist",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Impact of Materials on the Environment: Weighing Both Sides
        self.next_band(2)
        self.write_rows(2, "Impact of Materials on the Environment: Weighing Both Sides", [
            "Material and use; one good; one bad at its stage; a fix",
            "Plastic for ivory; bagasse for polystyrene",
            "Thin bags, then thickness and levy",
            "Command word; instruments; both sides; no blanks",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Net with a missing or colliding face''",
            "``'Bending' for a chain or cable''",
            "``One-sided impact answer''",
            "``Sketching when told to draw''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Unfold the Box
        self.next_band(4)
        self.write_rows(4, "Unfold the Box", [
            "Unfold it flat",
            "Hang sides off the base",
            "Fold it in your head",
            "Count six",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Five Forces, Three Letters, Two Composites
        self.next_band(5)
        self.write_rows(5, "Five Forces, Three Letters, Two Composites", [
            "Pull, squash, bend, twist, cut",
            "Concrete squashed, steel pulled",
            "Bottom between walls, top over columns",
            "Ruler on edge: depth",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Good, Bad and What to Do
        self.next_band(6)
        self.write_rows(6, "Good, Bad and What to Do", [
            "Name it, one good, one bad, one fix",
            "Three sentences can do it",
            "Where in its life is the harm?",
            "Draw means ruler",
        ], scale=0.9, box=1)

        last = Tex("Unfold the box with instruments, ask what the load does to the part, and weigh good against bad before you propose the fix.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
