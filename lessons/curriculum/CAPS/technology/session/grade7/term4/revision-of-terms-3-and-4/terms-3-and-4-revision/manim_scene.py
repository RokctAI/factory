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

# Band-layout whiteboard scene for terms-3-and-4-revision (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (200/220/280/100/100/100 of 1000 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class Terms3And4RevisionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Term three
        self.write_rows(0, "Term three", [
            "Ferrous metals; closed circuits",
            "Coil plus core; switch it off",
            "Crank second class; pulley wheel and axle",
            "Oblique at 45; flow chart shapes",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Term four: needs, food, textiles
        self.next_band(1)
        self.write_rows(1, "Term four: needs, food, textiles", [
            "Shelter, water, toilets, food",
            "20 litres; 2 100 kcal; 3.5 square metres",
            "Five questions; processing; fortified",
            "Hazard first; fibres; layers",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Term four: shelters and the process
        self.next_band(2)
        self.write_rows(2, "Term four: shelters and the process", [
            "Four scenarios; cause and cure",
            "Six for a month; vents; spacing",
            "Borrow the dome; test the fabric",
            "Investigate, design, make, evaluate, communicate",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Metal for ferrous metal''",
            "``Specification with no number''",
            "``Specs and constraints in one list''",
            "``Forgetting what harms soonest''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Term three shelf
        self.next_band(4)
        self.write_rows(4, "Term three shelf", [
            "Only ferrous sticks",
            "Symbols with a ruler",
            "Handle over drum; count the ropes",
            "Real sizes once each",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Term four shelf: people, food, cloth
        self.next_band(5)
        self.write_rows(5, "Term four shelf: people, food, cloth", [
            "Border or not",
            "Three figures",
            "Ten for the recipe, times ten",
            "Cotton burns, polyester melts",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Term four shelf: shelter and process
        self.next_band(6)
        self.write_rows(6, "Term four shelf: shelter and process", [
            "Sturdy, waterproof, easy to erect",
            "Not the thatch",
            "Ten lines, two shapes",
            "Four errors to avoid",
        ], scale=0.9, box=3)

        last = Tex("Term three: magnets, circuits, electromagnets, cranks, pulleys, advantage and drawing; term four: ranked needs, camp food, textiles and shelters; through both, the design process.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
