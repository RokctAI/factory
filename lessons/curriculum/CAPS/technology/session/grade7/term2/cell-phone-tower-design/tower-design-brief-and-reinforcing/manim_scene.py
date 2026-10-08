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

# Band-layout whiteboard scene for tower-design-brief-and-reinforcing (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (250/180/180/110/110/110 of 940 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TowerDesignBriefAndReinforcingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Writing the tower brief
        self.write_rows(0, "Writing the tower brief", [
            "Need and people; model and purpose; user and limit; the view",
            "Stability: returns upright after a 20 mm push",
            "Strength: 200 g on the platform; rigidity: under 10 mm sway",
            "Testable with a ruler, a weight or a push",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Webs, gussets, internal bracing
        self.next_band(1)
        self.write_rows(1, "Webs, gussets, internal bracing", [
            "Webs: card triangles lock corners",
            "Gussets: plates join members over an area",
            "X on faces; string through the inside against twist",
            "Plan on a sketch with a reason for each",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Disguising the tower
        self.next_band(2)
        self.write_rows(2, "Disguising the tower", [
            "Tree, flagpole, windmill, water tower",
            "Slim form, fading colour, siting, sharing",
            "Canopy adds top weight: stronger base",
            "Fit the disguise to the community",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A brief with no community''",
            "``The tower must be strong''",
            "``Add gussets after building''",
            "``A disguise with no structural cost''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): The brief for our tower
        self.next_band(4)
        self.write_rows(4, "The brief for our tower", [
            "Four sentences, plus the view",
            "500 mm tall, 150 by 150 base",
            "200 g held, under 10 mm sway",
            "Could a friend test it?",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Three ways to strengthen it
        self.next_band(5)
        self.write_rows(5, "Three ways to strengthen it", [
            "Webs in the corners",
            "Gussets on the joints",
            "X on each face",
            "String inside against twist",
        ], scale=0.95, box=3)

        # --- Band 6 (subtopic_6): Hiding it in plain sight
        self.next_band(6)
        self.write_rows(6, "Hiding it in plain sight", [
            "Tree, flagpole, wind pump",
            "Slim, painted, behind trees, shared",
            "Pay for it in the base",
            "Make it fit the place",
        ], scale=0.9, box=2)

        last = Tex("A brief with the community in it, specifications with numbers, reinforcement planned, disguise paid for.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
