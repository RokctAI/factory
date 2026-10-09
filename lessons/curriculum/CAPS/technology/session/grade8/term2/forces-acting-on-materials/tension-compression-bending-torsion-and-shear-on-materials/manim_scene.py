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

# Band-layout whiteboard scene for tension-compression-bending-torsion-and-shear-on-materials (Part 1 Expert
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


class ForcesOnMaterialsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Five Forces and What They Do to a Material
        self.write_rows(0, "Five Forces and What They Do to a Material", [
            "Tension pulls, compression pushes",
            "Bending stretches one side, squashes the other",
            "Torsion twists; shear slides",
            "Neutral axis does no work",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): How Materials Respond: Strength, Stiffness and Failure
        self.next_band(1)
        self.write_rows(1, "How Materials Respond: Strength, Stiffness and Failure", [
            "Strength names the force",
            "Stiff is not the same as strong",
            "Brittle snaps; tough absorbs",
            "Concrete: compression yes, tension no",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Testing Forces in the Classroom
        self.next_band(2)
        self.write_rows(2, "Testing Forces in the Classroom", [
            "One force at a time, same-size specimens",
            "Chalk twists and breaks at a slant",
            "Corrugated card beats flat card",
            "Eyes covered, fingers clear",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``'Strong' without naming the force''",
            "``Stiffness equals strength''",
            "``Comparing different-sized specimens''",
            "``Buckled straw is weak material''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Pull, Squash, Bend, Twist, Cut
        self.next_band(4)
        self.write_rows(4, "Pull, Squash, Bend, Twist, Cut", [
            "Pull, squash, bend, twist, cut",
            "Bend a ruler: outside stretches",
            "Twist: the skin works, not the core",
            "Five everyday examples",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Strong Is Not One Thing
        self.next_band(5)
        self.write_rows(5, "Strong Is Not One Thing", [
            "Concrete squashed, steel both ways",
            "Wood: along the grain",
            "Breaks at the weakest spot",
            "Paper clip: fatigue",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Try It on the Bench
        self.next_band(6)
        self.write_rows(6, "Try It on the Bench", [
            "Hang, press, pile, twist, cut",
            "Same size, same place, same speed",
            "Straw buckled, did not crush",
            "Write how it broke",
        ], scale=0.9, box=2)

        last = Tex("Five forces, each resisted differently; name the force before you name the strength, and test one force at a time.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
