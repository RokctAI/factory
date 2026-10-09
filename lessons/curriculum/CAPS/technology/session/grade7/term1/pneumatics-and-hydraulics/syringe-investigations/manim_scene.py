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

# Band-layout whiteboard scene for syringe-investigations (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (220/170/170/110/110/110 of 890 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SyringeInvestigationsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Equal syringes: air then water
        self.write_rows(0, "Equal syringes: air then water", [
            "Air: far plunger lags, feels spongy",
            "Fill and connect under water",
            "Water: same instant, same distance",
            "Equal force, MA = 1",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Unequal syringes
        self.next_band(1)
        self.write_rows(1, "Unequal syringes", [
            "Small pushes big: half distance, double force",
            "Big pushes small: double distance, half force",
            "Air version: late and soft again",
            "Record every run in the table",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Explaining and using the results
        self.next_band(2)
        self.write_rows(2, "Explaining and using the results", [
            "Pressure spreads; bigger face, bigger force",
            "Water incompressible, air compressible",
            "Rescue device: water, no bubbles, short tube",
            "Write up: aim, diagram, table, conclusion",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Trapped bubble means water compresses''",
            "``The air test was a failure''",
            "``Both plungers move the same distance''",
            "``Results can stay in your head''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Same size, air then water
        self.next_band(4)
        self.write_rows(4, "Same size, air then water", [
            "Air: late and lazy, like a pillow",
            "Water: instant and firm",
            "4 cm in, 4 cm out",
            "Water acts like a solid rod",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Small into big, big into small
        self.next_band(5)
        self.write_rows(5, "Small into big, big into small", [
            "Push small: big moves 2 cm, double force",
            "Push big: small moves 4 cm, half force",
            "MA of 2 from the sizes alone",
            "Table: fluid, sizes, in, out, force",
        ], scale=0.85, box=2)

        # --- Band 6 (subtopic_6): What it means for our device
        self.next_band(6)
        self.write_rows(6, "What it means for our device", [
            "Use water, fill under the surface",
            "Small syringe pushes, big one grips",
            "Swap them for a wide quick opening",
            "Honest results, explained, earn marks",
        ], scale=0.9, box=1)

        last = Tex("Water moves it now and fully; air moves it late and softly; the faces set force and distance.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
