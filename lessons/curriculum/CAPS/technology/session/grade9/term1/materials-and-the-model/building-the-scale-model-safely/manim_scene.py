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

# Band-layout whiteboard scene for building-the-scale-model-safely (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/170/170/120/110/90 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BuildingTheScaleModelSafelySession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Model Materials, Tools and the Conversion Table
        self.write_rows(0, "Model Materials, Tools and the Conversion Table", [
            "1:20: ramp 360, riser 7.5, rail 45",
            "Card = concrete; polystyrene fill; dowel rails",
            "Rule, knife, mat, saw, PVA, glue gun",
            "Conversion table, checked, pinned",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Safe Working Practices with Knives, Glue and Dust
        self.next_band(1)
        self.write_rows(1, "Safe Working Practices with Knives, Glue and Dust", [
            "Knife: mat, fingers back, light passes, cap it",
            "Blunt blades slip; change and bin them",
            "Glue gun on stand; cold water ready",
            "Dust wiped; bench tidy; report injuries",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Building Neatly to the Drawing and Checking as You Go
        self.next_band(2)
        self.write_rows(2, "Building Neatly to the Drawing and Checking as You Go", [
            "Base plan; ramp; check 1 in 12; glue",
            "Steps; check risers equal; landing flat",
            "Posts 75 apart, 45 high; rails; braces",
            "Paint, texture, photos, spec check",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Cut from memory''",
            "``Glued before checking''",
            "``Hot glue blobs everywhere''",
            "``No photos or check sheet''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): What You Build It From and How Big
        self.next_band(4)
        self.write_rows(4, "What You Build It From and How Big", [
            "Divide by 20",
            "Card, foam, dowel, base",
            "Few tools, all sharp",
            "Cut from the table",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Sharp Things, Sticky Things, Tidy Benches
        self.next_band(5)
        self.write_rows(5, "Sharp Things, Sticky Things, Tidy Benches", [
            "Mat, away, cap",
            "Stand, tweezers, water",
            "Wipe, do not blow",
            "Tell the teacher",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Follow the Chart, Check the Sizes
        self.next_band(6)
        self.write_rows(6, "Follow the Chart, Check the Sizes", [
            "Check before glue",
            "Posts upright, rails even",
            "Thin glue, hold square",
            "Photos and ticks",
        ], scale=0.9, box=0)

        last = Tex("A model at 1:20 cut from a checked table, built safely in flow chart order with checks before glue, finished neatly and recorded for the file.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
