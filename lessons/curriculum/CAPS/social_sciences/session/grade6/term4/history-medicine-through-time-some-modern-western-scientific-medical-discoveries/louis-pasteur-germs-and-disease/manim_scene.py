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

# Band-layout whiteboard scene for louis-pasteur-germs-and-disease (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/150/140/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class LouisPasteurGermsAndDiseaseSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Old Ideas About Disease
        self.write_rows(0, "Old Ideas About Disease", [
            "Germs: too small to see",
            "Miasma: bad air",
            "Spontaneous generation",
            "Semmelweis: wash hands",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Pasteur Proves Germ Theory
        self.next_band(1)
        self.write_rows(1, "Pasteur Proves Germ Theory", [
            "Chemist, born 1822",
            "Microbes spoil drinks",
            "Gentle heating: pasteurisation",
            "Swan-neck flask",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Vaccines and Pasteur's Legacy
        self.next_band(2)
        self.write_rows(2, "Vaccines and Pasteur's Legacy", [
            "Weakened germs",
            "Anthrax test, 1881",
            "Rabies: Joseph Meister, 1885",
            "Pasteur Institute, 1888",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Pasteur was a doctor''",
            "``Germs come from nothing''",
            "``Pasteurisation ruins food''",
            "``Pasteur made the first vaccine''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Bad Air and Magic Maggots
        self.next_band(4)
        self.write_rows(4, "Bad Air and Magic Maggots", [
            "Microbes",
            "Miasma",
            "Maggots",
            "Hands",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): The Swan-Neck Flask
        self.next_band(5)
        self.write_rows(5, "The Swan-Neck Flask", [
            "Wine",
            "Heat",
            "Flask",
            "Theory",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Weakened Germs Protect
        self.next_band(6)
        self.write_rows(6, "Weakened Germs Protect", [
            "Chickens",
            "Sheep",
            "Rabies",
            "Institute",
        ], scale=0.9, box=1)

        last = Tex("Louis Pasteur proved that invisible germs cause decay and disease, and his discovery led to safer food, better hygiene and new vaccines.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
