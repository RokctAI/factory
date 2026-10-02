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

# Band-layout whiteboard scene for useful-micro-organisms (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (230/240/230/220/180/190/180 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class UsefulMicroOrganismsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): decomposers
        self.write_rows(0, "Decomposers: bacteria and fungi", [
            "Dead material $\\rightarrow$ carbon dioxide + water + minerals",
            "Need moisture, warmth, oxygen, food",
            "Compost heap: centre near 60$^\\circ$C from respiration",
            "Sewage works; biogas digesters make methane",
        ], box=0)

        # --- Band 1 (subtopic_2): food
        self.next_band(1)
        self.write_rows(1, "Fermentation in food", [
            "Yoghurt: lactose $\\rightarrow$ lactic acid; thick, sour, preserved",
            "Heat 85$^\\circ$C, cool 43$^\\circ$C, add starter, keep warm 4 to 8 h",
            "Amasi and mageu: lactic acid bacteria",
            "Bread: yeast makes carbon dioxide bubbles",
        ], scale=0.78, box=1)

        # --- Band 2 (subtopic_3): medicine
        self.next_band(2)
        self.write_rows(2, "Penicillin and beyond", [
            "1928: Fleming, Penicillium mould, clear ring",
            "Florey and Chain about 1940; mass-produced by 1944",
            "Stops bacterial cell walls forming; no effect on viruses",
            "Vaccines; insulin from modified bacteria; resistance",
        ], scale=0.8, box=2)

        # --- Band 3 (subtopic_4): more helpers
        self.next_band(3)
        self.write_rows(3, "More useful microbes", [
            "Root nodules of legumes: nitrogen from the air",
            "Rumen microbes digest cellulose for cattle",
            "Gut bacteria: digestion and vitamin K",
            "Bioremediation: bacteria break down oil",
        ], scale=0.85, box=0)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        errs = [
            "``All bacteria are harmful''",
            "``Yeast makes bread rise with oxygen''",
            "``Penicillin comes from a bacterium''",
            "``Decomposers destroy nutrients''",
        ]
        for i, e in enumerate(errs):
            m = Tex(e).scale(0.9).shift(band_shift(4) + UP * (1.3 - 1.0 * i))
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): clean-up crew
        self.next_band(5)
        self.write_rows(5, "The clean-up crew", [
            "No rotting: dead leaves pile up, soil runs empty",
            "Rot returns carbon dioxide to air, minerals to soil",
            "Water, warmth, air: compost gets hot",
        ], scale=0.85, box=1)

        # --- Band 6 (subtopic_6): tiny cooks
        self.next_band(6)
        self.write_rows(6, "The tiny cooks", [
            "Heat, cool, add bacteria, keep warm, fridge",
            "Amasi in a pot; mageu from maize porridge",
            "Yeast: carbon dioxide bubbles lift the dough",
        ], scale=0.85, box=0)

        # --- Band 7 (subtopic_7): the mould
        self.next_band(7)
        self.write_rows(7, "The mould that saved millions", [
            "1928: a clear ring around the mould",
            "Breaks bacterial walls; viruses have none",
            "Bean root bumps feed the soil nitrogen",
        ], scale=0.85)
        last = Tex("Most microbes are helpers.").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
