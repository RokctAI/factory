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

# Band-layout whiteboard scene for sketching-a-transportable-emergency-shelter (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (230/260/260/100/100/100 of 1050 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SketchingATransportableShelterSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Two structures, not one
        self.write_rows(0, "Two structures, not one", [
            "Dome: rods in compression, hoops in tension",
            "Ridge: two A's and a pole, guys",
            "Box: diagonals or it folds",
            "21 square metres; 1.8 m; cover and floor",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Annotating for the lists
        self.next_band(1)
        self.write_rows(1, "Annotating for the lists", [
            "Door, two vents, stove place, lamp",
            "Guys at 45; hem pegged; pitch 30",
            "Packed bundle under 25 kg; six steps",
            "Credit hoop tent, hut, crane, thatch",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Checking, choosing, modelling
        self.next_band(2)
        self.write_rows(2, "Checking, choosing, modelling", [
            "Table: tick, cross, question, reason",
            "Fewest crosses on the lines that matter",
            "Straws and tissue: push, blow, pour",
            "Redraw clean; camp plan; steps",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Same tent in two sizes''",
            "``No door, vents or stove place''",
            "``Flat roof''",
            "``Box with no diagonals''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Two shapes
        self.next_band(4)
        self.write_rows(4, "Two shapes", [
            "Dome quick and strong",
            "Ridge flat sheets, low walls",
            "Box roomy, heavy, slow",
            "Fold the page",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Label everything
        self.next_band(5)
        self.write_rows(5, "Label everything", [
            "Door away from the wind",
            "Hooded vent high, vent low",
            "Stove under the peak on a slab",
            "Say where each idea came from",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Check, choose, model
        self.next_band(6)
        self.write_rows(6, "Check, choose, model", [
            "Ticks and crosses",
            "Hybrid with named parents",
            "Flat tissue roof pools",
            "Winner redrawn with every label",
        ], scale=0.9, box=2)

        last = Tex("Two shelters differing in structure, drawn with sizes, cover, floor and every safety feature labelled, checked in a table, tested as straw models, chosen with reasons and redrawn clean.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
