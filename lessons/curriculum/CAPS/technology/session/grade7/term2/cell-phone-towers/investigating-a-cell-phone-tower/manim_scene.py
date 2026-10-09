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

# Band-layout whiteboard scene for investigating-a-cell-phone-tower (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (220/150/180/110/110/110 of 880 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class InvestigatingACellPhoneTowerSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Reading a cell phone tower
        self.write_rows(0, "Reading a cell phone tower", [
            "Solid foundation, bolted feet",
            "Legs carry weight; horizontals hold them apart",
            "Diagonals zigzag up every face",
            "Antennas on top; wide base, narrow top; guys",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Why triangles
        self.next_band(1)
        self.write_rows(1, "Why triangles", [
            "Rectangle leans into a parallelogram",
            "Diagonal: two triangles, shape locked",
            "Crossing diagonals: one always in tension",
            "Light yet rigid; sloping legs add a big triangle",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Pylons, windmills, headgear
        self.next_band(2)
        self.write_rows(2, "Pylons, windmills, headgear", [
            "Pylon: cable pull and wind",
            "Wind pump: shaking wheel, concrete feet",
            "Headgear: cage and cable, sloping back leg",
            "Triangulated, tapered, anchored",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Horizontals alone stiffen a tower''",
            "``Diagonals are decoration''",
            "``Strong must mean heavy''",
            "``The biggest load is the antennas''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): The parts of a tower
        self.next_band(4)
        self.write_rows(4, "The parts of a tower", [
            "Concrete, bolts, legs",
            "Flat bars across, slanting bars up",
            "Antennas at the top",
            "Wide base, guy wires on thin masts",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): The triangle trick
        self.next_band(5)
        self.write_rows(5, "The triangle trick", [
            "Rectangle leans like a box folding",
            "One slanting bar locks it",
            "A cross: one bar always pulled",
            "Mostly air, still rigid",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Three cousins
        self.next_band(6)
        self.write_rows(6, "Three cousins", [
            "Pylons across the veld",
            "Windmills since the 1870s",
            "Headgear over the mines",
            "Same triangles, same lesson",
        ], scale=0.9, box=3)

        last = Tex("Legs, horizontals, diagonals: triangles lock the frame so a tower can be light, tall and rigid.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
