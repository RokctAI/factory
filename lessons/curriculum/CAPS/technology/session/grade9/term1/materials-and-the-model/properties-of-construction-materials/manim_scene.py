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

# Band-layout whiteboard scene for properties-of-construction-materials (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/170/170/120/110/90 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PropertiesOfConstructionMaterialsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Density, Hardness and Stiffness
        self.write_rows(0, "Density, Hardness and Stiffness", [
            "Density: kg per m3; steel 7 800, concrete 2 400",
            "Hardness: resists scratch and dent; nosings",
            "Stiffness: resists bending; rail flex",
            "Stiff is not strong: rubber band, biscuit",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Flexibility, Brittleness and Toughness
        self.next_band(1)
        self.write_rows(1, "Flexibility, Brittleness and Toughness", [
            "Flexible: bends and recovers; rubber",
            "Brittle: snaps; glass, chalk, plain concrete",
            "Tough: dents, survives; mild steel, timber",
            "Hard often means brittle: choose",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Corrosion: How Metals Rot and How to Stop It
        self.next_band(2)
        self.write_rows(2, "Corrosion: How Metals Rot and How to Stop It", [
            "Rust = iron + oxygen + water; salt speeds it",
            "Paint: barrier, scratches, repaint",
            "Galvanise: zinc protects even scratched",
            "Cap tube ends; drain; keep off copper",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Bare mild steel outdoors''",
            "``Paint is permanent''",
            "``Stiffness is strength''",
            "``Tube ends left open''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Heavy, Hard or Stiff: Three Different Things
        self.next_band(4)
        self.write_rows(4, "Heavy, Hard or Stiff: Three Different Things", [
            "Heavy for its size",
            "Scratches or not",
            "Bends or not",
            "Strong is a different question",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Bends, Snaps or Takes a Knock
        self.next_band(5)
        self.write_rows(5, "Bends, Snaps or Takes a Knock", [
            "Bends back: flexible",
            "Snaps: brittle",
            "Dents: tough",
            "Mesh makes concrete tough",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Rust and Its Enemies
        self.next_band(6)
        self.write_rows(6, "Rust and Its Enemies", [
            "Iron, air, water",
            "Paint fails at scratches",
            "Zinc sacrifices itself",
            "Cap the ends",
        ], scale=0.9, box=2)

        last = Tex("Density, hardness, stiffness, flexibility, brittleness and toughness pick the material for each part, and galvanising plus good drainage keep the steel from rusting.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
