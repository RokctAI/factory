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

# Band-layout whiteboard scene for inherited-variation-in-humans (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/140/150/120/120/120 of 810 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class InheritedVariationInHumansSession(MovingCameraScene):
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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Inherited features in humans
        self.write_rows(0, "Inherited features in humans", [
            "Genes on chromosomes, from both parents",
            "46 chromosomes in 23 pairs",
            "Height, eye colour, hair type, blood group",
            "Tongue rolling, earlobes, dimples, thumbs",
        ], scale=0.88, box=1)

        # --- Band 1 (subtopic_2): Planning a survey
        self.next_band(1)
        self.write_rows(1, "Planning a survey", [
            "Clear question; clear definitions",
            "Height: shoes off, back to wall, read at eye level",
            "Ethics: permission, codes not names, no teasing",
            "Record in a table with headings and units",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Graphs and conclusions
        self.next_band(2)
        self.write_rows(2, "Graphs and conclusions", [
            "Group heights: 140 to 144, 145 to 149 cm",
            "Histogram: bars touch; bar graph: gaps",
            "21/30 = 0,7 = 70\\%; range = 165 - 138 = 27 cm",
            "Conclusion: answer the question, stay with the data",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Histogram bars should have gaps''",
            "``Blood group bars should touch''",
            "``One class tells us about all humans''",
            "``Results can be used to tease people''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Your family recipe
        self.next_band(4)
        self.write_rows(4, "Your family recipe", [
            "Half from mother, half from father",
            "Each child: a different shuffle",
            "Tongue rolling, earlobes, dimples, blood group",
            "All humans share almost all their genes",
        ], scale=0.82, box=0)

        # --- Band 5 (subtopic_5): The measuring wall
        self.next_band(5)
        self.write_rows(5, "The measuring wall", [
            "Question: how does height vary in our class?",
            "Shoes off, back to wall, book on head",
            "Permission, numbers not names, no teasing",
            "Table with headings and centimetres",
        ], scale=0.88, box=1)

        # --- Band 6 (subtopic_6): Drawing the picture
        self.next_band(6)
        self.write_rows(6, "Drawing the picture", [
            "Height groups: bars touch, hill shape",
            "Can or cannot: separate bars",
            "21 / 30 = 0,7 = 70\\%",
            "Conclusion: only what the data show",
        ], scale=0.88, box=0)

        last = Tex("Measure carefully, record honestly, and let the data speak.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
