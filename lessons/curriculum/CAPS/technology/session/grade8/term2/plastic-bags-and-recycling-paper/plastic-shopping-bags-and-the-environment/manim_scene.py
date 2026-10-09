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

# Band-layout whiteboard scene for plastic-shopping-bags-and-the-environment (Part 1 Expert
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


class PlasticBagsEnvironmentSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The Problem With Plastic Shopping Bags
        self.write_rows(0, "The Problem With Plastic Shopping Bags", [
            "Thin polythene film, almost free, 8 billion a year",
            "Free, light, never rots",
            "Fences, drains, rivers, turtles, cattle",
            "Same material, different use, different impact",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): South Africa's Response: Thicker Bags and the Levy
        self.next_band(1)
        self.write_rows(1, "South Africa's Response: Thicker Bags and the Levy", [
            "2003: thin bags banned, minimum thickness",
            "Charge per bag plus levy",
            "Use fell up to 80 percent, then crept back",
            "Starch, oxo-degradable, paper, woven reusable",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Writing a Case-Study Report
        self.next_band(2)
        self.write_rows(2, "Writing a Case-Study Report", [
            "Introduction, background, findings, discussion",
            "Recommendation follows findings; sources",
            "Evidence with source and date, both sides",
            "Table across source, manufacture, use, disposal",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Write a story, not a report''",
            "``Opinions without evidence''",
            "``One side only''",
            "``Recommendation unrelated to findings''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Why the Bag Became a Problem
        self.next_band(4)
        self.write_rows(4, "Why the Bag Became a Problem", [
            "A few grams of polythene",
            "Thrown away at once, blows for kilometres",
            "Never rots, so it stays",
            "The national flower",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): What the Country Did About It
        self.next_band(5)
        self.write_rows(5, "What the Country Did About It", [
            "Thicker bags, pay per bag",
            "Litter fell; use came back",
            "Levy money wandered",
            "Woven reusable bag works best",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Putting the Report Together
        self.next_band(6)
        self.write_rows(6, "Putting the Report Together", [
            "Six headings, short paragraphs",
            "Facts not feelings",
            "Both sides, numbers with sources",
            "Recommendation from findings",
        ], scale=0.9, box=1)

        last = Tex("Free, light and everlasting made the bag a problem; thicker bags and a levy helped for a while; a report gives both sides and a recommendation that follows.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
