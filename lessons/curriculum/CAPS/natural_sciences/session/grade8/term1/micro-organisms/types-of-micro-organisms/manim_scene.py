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

# Band-layout whiteboard scene for types-of-micro-organisms (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex/MathTex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (230/240/230/220/180/190/180 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TypesOfMicroOrganismsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): size and microscopes
        self.write_rows(0, "Micro-organisms: seen only with a microscope", [
            "1 mm = 1 000 $\\mu$m; \\ 1 $\\mu$m = 1 000 nm",
            "Bacterium about 2 $\\mu$m: 500 span 1 mm; hair about 70 $\\mu$m",
            "Viruses 20 to 300 nm: electron microscope only",
            "Van Leeuwenhoek, 1670s: animalcules in pond water",
        ], box=0)

        # --- Band 1 (subtopic_2): viruses and bacteria
        self.next_band(1)
        self.write_rows(1, "Viruses and bacteria", [
            "Virus: not a cell; DNA or RNA in a protein coat; copies only in a host",
            "Bacterium: one cell, cell wall, no nucleus, DNA loose",
            "Shapes: cocci (balls), bacilli (rods), spirilla (spirals)",
            "Binary fission every 20 min: 1, 8, 64, 512 after 3 hours",
        ], scale=0.76, box=3)

        # --- Band 2 (subtopic_3): protists and fungi
        self.next_band(2)
        self.write_rows(2, "Protists and fungi", [
            "Protists: single cells with a nucleus",
            "Amoeba pseudopodia; paramecium cilia; euglena flagellum and chloroplasts",
            "Fungi: chitin walls, no chlorophyll, digest outside and absorb",
            "Yeast buds; moulds grow hyphae and release spores",
        ], scale=0.76, box=2)

        # --- Band 3 (subtopic_4): sorting questions
        self.next_band(3)
        self.write_rows(3, "Three sorting questions", [
            "1. Is it a cell? No: virus",
            "2. Has it a nucleus? No: bacterium",
            "3. Threads or budding with chitin: fungus. Otherwise: protist",
            "Antibiotics act on bacteria, never on viruses",
        ], scale=0.82, box=3)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        errs = [
            "``A virus is a tiny bacterium''",
            "``Bacteria have a nucleus''",
            "``All micro-organisms cause disease''",
            "``Antibiotics will cure my flu''",
        ]
        for i, e in enumerate(errs):
            m = Tex(e).scale(0.9).shift(band_shift(4) + UP * (1.3 - 1.0 * i))
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the invisible zoo
        self.next_band(5)
        self.write_rows(5, "The invisible zoo", [
            "One drop of pond water: blobs, hairy slippers, green swimmers",
            "Cut a millimetre into 1 000: one micrometre",
            "Light microscope for cells; electron microscope for viruses",
            "Most microbes are harmless or helpful",
        ], scale=0.82, box=3)

        # --- Band 6 (subtopic_6): four houses
        self.next_band(6)
        self.write_rows(6, "Four families, four houses", [
            "Virus: no house at all, a hijacker",
            "Bacterium: one room, no office",
            "Protist: a room with an office",
            "Fungus: a house of threads, or budding cells",
        ], scale=0.88, box=0)

        # --- Band 7 (subtopic_7): doubling
        self.next_band(7)
        self.write_rows(7, "One becomes a million", [
            "1 hour: 8. \\ 2 hours: 64. \\ 3 hours: 512",
            "20 splits, under 7 hours: 1 048 576",
            "Fridge slows it; cooking kills; drying removes water",
        ], scale=0.88, box=1)
        last = Tex("Antibiotics break bacteria, not viruses.").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
