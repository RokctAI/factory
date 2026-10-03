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

# Band-layout whiteboard scene for invertebrates-arthropods-and-molluscs (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (120/170/200/120/120/120 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class InvertebratesArthropodsAndMolluscsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Invertebrates and arthropods
        self.write_rows(0, "Invertebrates and arthropods", [
            "Invertebrates: no backbone, about 95\\% of animals",
            "Arthropods: exoskeleton, jointed legs, segments",
            "Exoskeleton of chitin: support, protection, no drying",
            "To grow, they moult",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Insects, arachnids, crustaceans
        self.next_band(1)
        self.write_rows(1, "Insects, arachnids, crustaceans", [
            "Insects: 3 parts, 6 legs, 1 pair antennae, often wings",
            "Arachnids: 2 parts, 8 legs, no antennae",
            "Crustaceans: 2 parts, 10+ legs, 2 pairs antennae, gills",
            "Bee and beetle; spider and scorpion; crab and prawn",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Molluscs
        self.next_band(2)
        self.write_rows(2, "Molluscs", [
            "Soft body, muscular foot, mantle makes a shell",
            "Gastropods: snails, limpets, perlemoen",
            "Bivalves: mussels, oysters (two shells)",
            "Cephalopods: octopus and squid, clever hunters",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A spider is an insect''",
            "``A crab is a mollusc''",
            "``An octopus is not a mollusc''",
            "``Invertebrates are rare''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Armour on the outside
        self.next_band(4)
        self.write_rows(4, "Armour on the outside", [
            "No backbone: invertebrates, about 95 in 100",
            "Arthropods wear armour: an exoskeleton",
            "Legs bend at joints",
            "Too small? Moult and grow a new one",
        ], scale=0.88, box=1)

        # --- Band 5 (subtopic_5): Count the legs
        self.next_band(5)
        self.write_rows(5, "Count the legs", [
            "Six legs, three parts, feelers: insect",
            "Eight legs, two parts: arachnid (spider)",
            "Ten or more legs, gills: crustacean (crab)",
            "Woodlice are land crustaceans",
        ], scale=0.88, box=1)

        # --- Band 6 (subtopic_6): Soft bodies in shells
        self.next_band(6)
        self.write_rows(6, "Soft bodies in shells", [
            "Mollusc = soft body + muscly foot",
            "Snail: one shell; mussel: two shells",
            "Octopus: no outside shell, very clever",
            "Crab: jointed legs, so arthropod",
        ], scale=0.88, box=3)

        last = Tex("Jointed legs or a soft body: most animals have no backbone at all.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
