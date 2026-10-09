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

# Band-layout whiteboard scene for identifying-plastics-by-recycling-codes (Part 1 Expert
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


class IdentifyingPlasticsByRecyclingCodesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What Plastics Are and Why They Must Be Sorted
        self.write_rows(0, "What Plastics Are and Why They Must Be Sorted", [
            "Polymers: long chains from oil and gas",
            "Thermoplastics remould; thermosets do not",
            "Mixed melts: weak lumps; one PVC ruins PET",
            "SA: 1, 2 strong; PS and mixed to landfill",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): The Seven Recycling Codes and the Plastics They Name
        self.next_band(1)
        self.write_rows(1, "The Seven Recycling Codes and the Plastics They Name", [
            "1 PET bottles; 2 HDPE milk, detergent",
            "3 PVC pipes, film; 4 LDPE bags",
            "5 PP tubs, caps; 6 PS cups, foam",
            "7 Other: multi-layer; no code = 7",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Sorting a Bag of Household Plastic for Recycling
        self.next_band(2)
        self.write_rows(2, "Sorting a Bag of Household Plastic for Recycling", [
            "Rinse; caps off; find code; sort piles",
            "Squash; bag by type; 3, 6, 7 out",
            "Traps: clear PVC, black trays, crisp packets",
            "To buy-back or picker, paid per kilogram",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Unrinsed containers contaminating the bag''",
            "``Caps left on bottles''",
            "``All clear plastic assumed to be PET''",
            "``Polystyrene and crisp packets put in the recycling''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Family of Materials, Not One
        self.next_band(4)
        self.write_rows(4, "A Family of Materials, Not One", [
            "A family, not one",
            "Oil and water when melted",
            "Pickers do the recycling",
            "Codes put value where it is collected",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Look for the Triangle and the Number
        self.next_band(5)
        self.write_rows(5, "Look for the Triangle and the Number", [
            "Triangle and a number",
            "1, 2, 5 matter most",
            "4 if clean",
            "3, 6, 7 keep out",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Rinse, Squash, Sort, Bag
        self.next_band(6)
        self.write_rows(6, "Rinse, Squash, Sort, Bag", [
            "Rinse, squash, sort, bag",
            "Cap is a different plastic",
            "Black fools the machine",
            "Weigh the week",
        ], scale=0.9, box=0)

        last = Tex("Plastics are a family that cannot be melted together; the resin code sorts them, and in South Africa codes 1, 2 and 5 are the ones that are recycled.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
