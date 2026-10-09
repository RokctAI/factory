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

# Band-layout whiteboard scene for textiles-for-fire-fighters-and-nsri-crews (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/220/260/100/100/100 of 950 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TextilesForFireFightersAndNsriSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Hazards first, then properties
        self.write_rows(0, "Hazards first, then properties", [
            "Fire: flame, heat, steam, debris, sweat",
            "Sea: cold water, waves, dark, salt",
            "Each hazard asks for a property",
            "Two columns per job",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Fibres, fabrics, properties
        self.next_band(1)
        self.write_rows(1, "Fibres, fabrics, properties", [
            "Cotton soaks and burns; wool chars",
            "Polyester, nylon melt; aramids do not",
            "Weave, knit, felt; coat, laminate",
            "Test: drop, tear, flame, torch",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Layering
        self.next_band(2)
        self.write_rows(2, "Layering", [
            "Shell, moisture barrier, thermal liner",
            "Base, fleece, coated outer, life jacket",
            "Outer, middle, inner, sealed seams",
            "Same for the shelter",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Polyester fire shell''",
            "``Waterproof with no breathability''",
            "``Cotton jersey in cold water''",
            "``Fluorescent but no reflective tape''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Start with the danger
        self.next_band(4)
        self.write_rows(4, "Start with the danger", [
            "Flame, cold sea, sparks, rock, dark",
            "Property beats hazard",
            "Comfort for hours",
            "The table is the spec",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Fibres and fabrics
        self.next_band(5)
        self.write_rows(5, "Fibres and fabrics", [
            "Natural: cotton, wool",
            "Synthetic: polyester, nylon, aramid",
            "PVC out; membrane breathes",
            "Write the swatch table",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Build it in layers
        self.next_band(6)
        self.write_rows(6, "Build it in layers", [
            "Three layers, one jacket",
            "Wick, insulate, shed, float",
            "Seams must not leak",
            "No single fabric does it all",
        ], scale=0.9, box=3)

        last = Tex("Start with the hazard, choose fibres and fabrics for the properties it demands, test them, and layer them so each layer does one job.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
