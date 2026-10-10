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

# Band-layout whiteboard scene for edward-jenner-and-the-smallpox-vaccine (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (260/130/140/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EdwardJennerAndTheSmallpoxVaccineSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Smallpox: A Deadly Disease
        self.write_rows(0, "Smallpox: A Deadly Disease", [
            "Smallpox: fever and blisters",
            "About 3 in 10 died",
            "The Cape, 1713",
            "Inoculation: risky",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Jenner's Experiment
        self.next_band(1)
        self.write_rows(1, "Jenner's Experiment", [
            "Milkmaids and cowpox",
            "Sarah Nelmes, 1796",
            "James Phipps, aged 8",
            "Vacca means cow",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): From Opposition to Eradication
        self.next_band(2)
        self.write_rows(2, "From Opposition to Eradication", [
            "Cartoons of cow heads",
            "WHO campaign, 1967",
            "Last case, 1977",
            "Eradicated, 1980",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Jenner was the first to protect''",
            "``The vaccine used smallpox''",
            "``Smallpox still exists''",
            "``Such tests are allowed today''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Terrible Disease
        self.next_band(4)
        self.write_rows(4, "A Terrible Disease", [
            "Fever",
            "Blisters",
            "Scars",
            "Epidemic",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Cowpox Protects
        self.next_band(5)
        self.write_rows(5, "Cowpox Protects", [
            "Cowpox",
            "Milkmaid",
            "Boy",
            "Vaccine",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Smallpox Is Gone
        self.next_band(6)
        self.write_rows(6, "Smallpox Is Gone", [
            "Doubt",
            "Spread",
            "Campaign",
            "Gone",
        ], scale=0.9, box=3)

        last = Tex("Edward Jenner's cowpox experiment in 1796 began the age of vaccines, and in 1980 smallpox became the first human disease wiped off the Earth.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
