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

# Band-layout whiteboard scene for making-and-assembling-packaging-safely (Part 1 Expert
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


class MakingAssemblingPackagingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): From Development to Flat Blank
        self.write_rows(0, "From Development to Flat Blank", [
            "Mark out directly or trace a template",
            "Folds along the grain or flutes",
            "Cut only cut lines; never a fold line",
            "Mat, steel ruler, light passes, hand back",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Scoring, Folding and Gluing
        self.next_band(1)
        self.write_rows(1, "Scoring, Folding and Gluing", [
            "Score with a blunt tool on the outside",
            "Score all, set each, then tube, tab, base, lid",
            "Thin even glue, hold square, wipe squeeze-out",
            "Tab inside, edges meeting, box square",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Checking the Finished Package
        self.next_band(2)
        self.write_rows(2, "Checking the Finished Package", [
            "Product in: shake, drop, stack, open, close",
            "Diagonals equal, folds crisp, seams hold",
            "Skew: base glued first; crack: wrong side",
            "Less material? One material? Recyclable?",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Cut the fold lines''",
            "``Score on the inside of the fold''",
            "``A blob of glue''",
            "``Finished without testing with the product''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Marking Out and Cutting
        self.next_band(4)
        self.write_rows(4, "Marking Out and Cutting", [
            "Trace or measure onto the card",
            "Grain first",
            "Only the outside edge and slots",
            "Dashed means fold, do not cut",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Crisp Folds and Clean Seams
        self.next_band(5)
        self.write_rows(5, "Crisp Folds and Clean Seams", [
            "Butter knife along every fold",
            "Bend once to set",
            "Tube, tab, hold square, glue thin",
            "Base next, lid last",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Does It Do Its Job?
        self.next_band(6)
        self.write_rows(6, "Does It Do Its Job?", [
            "Real product inside",
            "Shake, drop, stack",
            "Diagonals equal, lid tucks",
            "Find the cause, fix it, judge the material",
        ], scale=0.9, box=2)

        last = Tex("Mark out along the grain, cut only the cut lines, score and fold in order, glue thin and square, then test with the product inside.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
