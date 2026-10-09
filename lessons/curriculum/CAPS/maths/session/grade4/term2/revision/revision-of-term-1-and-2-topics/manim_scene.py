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

# Band-layout whiteboard scene for revision-of-term-1-and-2-topics (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/160/160/110/110/110 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RevisionOfTerm1And2TopicsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Numbers and the Four Operations
        self.write_rows(0, "Numbers and the Four Operations", [
            "1 248: the 4 is worth 40",
            "1 248 plus 375 is 1 623",
            "8 times 24 is 192",
            "192 divided by 8 is 24",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Sentences, Properties, Multiples, Factors and Patterns
        self.next_band(1)
        self.write_rows(1, "Sentences, Properties, Multiples, Factors and Patterns", [
            "Box plus 375 equals 1 623: box is 1 248",
            "Factors of 24: eight of them",
            "4, 7, 10, 13: add 3",
            "Times 12 then plus 5: 17, 29, 41, 53",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Shapes, Objects and Symmetry
        self.next_band(2)
        self.write_rows(2, "Shapes, Objects and Symmetry", [
            "Polygon: straight sides, named by count",
            "Prism, cylinder, sphere, pyramid",
            "Square: 4 lines, rectangle: 2",
            "Describe by stated properties",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``8 minibuses is enough''",
            "``Rectangle diagonal is symmetric''",
            "``Subtract to find a ratio''",
            "``No need to check''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): At the Gate: Numbers and Sums
        self.next_band(4)
        self.write_rows(4, "At the Gate: Numbers and Sums", [
            "1 248: the 4 is 40",
            "1 248 plus 375 is 1 623",
            "1 623 minus 486 is 1 137",
            "8 times 24 is 192",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): At the Medal Table: Patterns and Rules
        self.next_band(5)
        self.write_rows(5, "At the Medal Table: Patterns and Rules", [
            "Undo the plus to find the box",
            "4, 7, 10, 13: add 3",
            "3, 6, 12, 24: times 2",
            "Backwards: minus 5, divide by 12",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): In the Store: Shapes and Symmetry
        self.next_band(6)
        self.write_rows(6, "In the Store: Shapes and Symmetry", [
            "Prism, cylinder, sphere, pyramid",
            "Count straight sides to name",
            "Square: 4 lines of symmetry",
            "Fold it: halves must match",
        ], scale=0.9, box=3)

        last = Tex("Numbers, operations, patterns, shapes and symmetry: estimate, show working, check, and read to the end.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
