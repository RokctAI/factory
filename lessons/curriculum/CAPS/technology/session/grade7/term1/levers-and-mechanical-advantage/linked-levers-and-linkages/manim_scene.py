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

# Band-layout whiteboard scene for linked-levers-and-linkages (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (220/170/150/110/110/110 of 870 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class LinkedLeversAndLinkagesSession(MovingCameraScene):
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
        self.wait(44)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Pairs of levers
        self.write_rows(0, "Pairs of levers", [
            "Scissors, pliers, shears: first class",
            "Punch, nutcracker: second class",
            "Stapler, tweezers: third class",
            "Strongest near the pivot",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Linkages with more pivots
        self.next_band(1)
        self.write_rows(1, "Linkages with more pivots", [
            "Folding airer: movement magnified",
            "Bell crank: force around a corner",
            "Scissor jack: force in two stages",
            "More movement means less force",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Designing the rescue jaws
        self.next_band(2)
        self.write_rows(2, "Designing the rescue jaws", [
            "Syringe, rod, two first-class arms, pin",
            "Pin near tips: grip; pin at back: opening",
            "Tight joins pass on movement",
            "Stiff arms: fold or double the card",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Two handles means two machines''",
            "``Force and movement both increase''",
            "``Pin at the back for grip''",
            "``Arm stiffness does not matter''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Tools that come in pairs
        self.next_band(4)
        self.write_rows(4, "Tools that come in pairs", [
            "Find the pivot on each tool",
            "Cut near the screw: easy",
            "Nut near the hinge: cracks",
            "Tweezers: gentle, careful tips",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Chains of levers
        self.next_band(5)
        self.write_rows(5, "Chains of levers", [
            "Airer stretches out long",
            "Jack lifts a car in two stages",
            "Piston pushes the back of the arms",
            "Bigger movement, smaller force",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Building the jaws
        self.next_band(6)
        self.write_rows(6, "Building the jaws", [
            "Water, plunger, rod, arms, tips",
            "Pin position: grip or opening",
            "Double the card so it does not bend",
            "Mock-up first, write it down",
        ], scale=0.9, box=1)

        last = Tex("Linked levers share a pivot; linkages chain them; movement and force trade places at every pin.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
