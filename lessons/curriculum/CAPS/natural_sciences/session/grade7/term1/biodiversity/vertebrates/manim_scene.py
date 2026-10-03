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

# Band-layout whiteboard scene for vertebrates (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (130/150/200/120/120/120 of 840 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class VertebratesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Vertebrates and fish
        self.write_rows(0, "Vertebrates and fish", [
            "Backbone protects the spinal cord; inner skeleton",
            "Classify by: covering, breathing, temperature, reproduction",
            "Fish: scales, gills, fins, ectothermic",
            "External fertilisation; coelacanth, East London 1938",
        ], scale=0.76, box=1)

        # --- Band 1 (subtopic_2): Amphibians and reptiles
        self.next_band(1)
        self.write_rows(1, "Amphibians and reptiles", [
            "Amphibians: moist skin, no scales, gills then lungs",
            "Jelly eggs in water; tadpole metamorphosis",
            "Reptiles: dry scales, lungs, internal fertilisation",
            "Shelled eggs on land: reptiles can live in deserts",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Birds and mammals
        self.next_band(2)
        self.write_rows(2, "Birds and mammals", [
            "Endothermic: constant temperature, lots of food",
            "Birds: feathers, beak, wings, hard-shelled eggs",
            "Mammals: hair, milk, mostly live birth",
            "Bat and whale: mammals; ostrich: a bird",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A whale is a fish''",
            "``A bat is a bird''",
            "``A crocodile is an amphibian''",
            "``All birds can fly''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Five visitors at the river
        self.next_band(4)
        self.write_rows(4, "Five visitors at the river", [
            "Yellowfish: fish",
            "Frog: amphibian",
            "Crocodile: reptile",
            "Fish eagle: bird; impala: mammal",
        ], scale=0.88, box=4)

        # --- Band 5 (subtopic_5): Four questions
        self.next_band(5)
        self.write_rows(5, "Four questions", [
            "Covering: scales, wet skin, dry scales, feathers, fur",
            "Breathing: gills or lungs",
            "Warm-blooded: birds and mammals only",
            "Babies: jelly eggs, shelled eggs or live birth",
        ], scale=0.82, box=2)

        # --- Band 6 (subtopic_6): Tricky customers
        self.next_band(6)
        self.write_rows(6, "Tricky customers", [
            "Whale: lungs and milk, so mammal",
            "Bat: fur and milk, so mammal",
            "Penguin: feathers, so bird; crocodile: reptile",
            "Ignore where it lives; check the four questions",
        ], scale=0.82, box=3)

        last = Tex("Fish, amphibians, reptiles, birds, mammals: one backbone, five plans.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
