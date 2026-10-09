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

# Band-layout whiteboard scene for painting-and-galvanising (Part 1 Expert
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


class PaintingAndGalvanisingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Why Metals Corrode: Iron, Oxygen and Water
        self.write_rows(0, "Why Metals Corrode: Iron, Oxygen and Water", [
            "Rust: iron oxide; needs oxygen AND water",
            "Salt speeds it; flakes expose fresh metal",
            "Costs billions; hinges, roofs, cars, concrete",
            "Principle: keep oxygen and water off",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Painting: Sealing the Surface and Its Limits
        self.next_band(1)
        self.write_rows(1, "Painting: Sealing the Surface and Its Limits", [
            "Paint: pigment in binder, a barrier skin",
            "Prepare: remove rust, degrease, prime, top coat",
            "Cheap, any colour, on site, any size",
            "Fails at chips; chalks; renew every few years",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Galvanising: Zinc as a Coat and a Sacrifice
        self.next_band(2)
        self.write_rows(2, "Galvanising: Zinc as a Coat and a Sacrifice", [
            "Hot-dip: clean steel in molten zinc, 450 degrees",
            "Barrier plus sacrificial: zinc corrodes first",
            "30 to 50 years inland; less at coast",
            "Limits: grey, factory, repair by zinc paint, cost",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Rust said to need only air or only water''",
            "``Paint applied over rust''",
            "``Scratch on galvanising expected to rust like paint''",
            "``Galvanising called a paint''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Rust Needs Air and Water
        self.next_band(4)
        self.write_rows(4, "Rust Needs Air and Water", [
            "Air and water, both",
            "Dry or oily: no rust",
            "Flakes and keeps going",
            "Keep them off",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): A Skin of Paint
        self.next_band(5)
        self.write_rows(5, "A Skin of Paint", [
            "A skin",
            "Clean first",
            "Chip it, rust creeps",
            "Repaint often",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): A Skin of Zinc That Gives Itself Up
        self.next_band(6)
        self.write_rows(6, "A Skin of Zinc That Gives Itself Up", [
            "Dip in zinc",
            "Zinc gives itself up",
            "Grey, then red when gone",
            "Dearer first, cheaper over life",
        ], scale=0.9, box=1)

        last = Tex("Iron rusts when oxygen and water reach it; paint is a barrier that fails at breaks, while zinc galvanising is a barrier that also sacrifices itself to protect scratched steel.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
