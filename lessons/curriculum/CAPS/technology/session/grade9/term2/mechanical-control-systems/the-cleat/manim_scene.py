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

# Band-layout whiteboard scene for the-cleat (Part 1 Expert
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


class TheCleatSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Cleat Is and How It Holds a Rope Without a Knot
        self.write_rows(0, "What a Cleat Is and How It Holds a Rope Without a Knot", [
            "Holds rope by friction and jamming",
            "Load up, grip up; release instantly",
            "Control: governs whether rope moves",
            "Bolts in shear; backing plate",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Types of Cleat: Horn, Cam and Jam Cleats
        self.next_band(1)
        self.write_rows(1, "Types of Cleat: Horn, Cam and Jam Cleats", [
            "Horn: round turn + figure-of-eights",
            "Cam: spring-loaded toothed jaws, ratchet for rope",
            "Jam: tapered slot, flick to free",
            "Hold vs release trade-offs",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Where Cleats Are Used and How to Evaluate Them
        self.next_band(2)
        self.write_rows(2, "Where Cleats Are Used and How to Evaluate Them", [
            "Pontoons, yachts, flagpoles, lines, tents",
            "Evaluate: purpose, safety, ergonomics, cost",
            "Plank test: wraps, release, wet slip",
            "Recommend for a stated use",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Knot tied so tight it cannot release''",
            "``Rope too thin for the cam teeth''",
            "``Cleat screwed to thin plywood''",
            "``Cleat said to increase force''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Rope Catcher
        self.next_band(4)
        self.write_rows(4, "A Rope Catcher", [
            "No knot: wrap, pinch or jam",
            "Pull harder, holds harder",
            "The boat pulls; the cleat holds",
            "Bolt through, not screw",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Wrap It, Pinch It, Jam It
        self.next_band(5)
        self.write_rows(5, "Wrap It, Pinch It, Jam It", [
            "Horn: figure-of-eight",
            "Cam: toothed jaws",
            "Jam: wedge in a slot",
            "Lift, lift, flick",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Hold Fast, Let Go Fast
        self.next_band(6)
        self.write_rows(6, "Hold Fast, Let Go Fast", [
            "Right rope size, wet or dry",
            "No accidental release",
            "One cold hand",
            "Table then recommend",
        ], scale=0.9, box=1)

        last = Tex("A cleat holds a rope by friction or jamming so that load tightens the grip, and releases it instantly: a control that adds no force.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
