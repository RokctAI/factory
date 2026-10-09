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

# Band-layout whiteboard scene for ratchet-and-pawl (Part 1 Expert
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


class RatchetAndPawlSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Ratchet and Pawl Is and How It Allows Motion One Way
        self.write_rows(0, "What a Ratchet and Pawl Is and How It Allows Motion One Way", [
            "Saw teeth: long slope, short steep face",
            "Pawl: spring-pressed arm",
            "Free way: ride and click; back: jam",
            "Control, not drive",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Where Ratchets Control Machines: Winches, Jacks, Spanners and Ties
        self.next_band(1)
        self.write_rows(1, "Where Ratchets Control Machines: Winches, Jacks, Spanners and Ties", [
            "Boat winch: holds drum; lift pawl to release",
            "Ratchet spanner: drive push, freewheel return",
            "Scissor jack handle",
            "Cable tie, strap, handbrake, turnstile",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Designing, Drawing and Evaluating a Ratchet
        self.next_band(2)
        self.write_rows(2, "Designing, Drawing and Evaluating a Ratchet", [
            "Draw: teeth, pawl, spring, arrows",
            "Pivot so load pushes pawl in",
            "Evaluate: purpose, safety, ergonomics, cost",
            "Holds only at a tooth",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Symmetrical teeth drawn''",
            "``Pawl pivoted so load lifts it out''",
            "``Ratchet said to increase force''",
            "``No release in the design''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Toothed Wheel and a Finger
        self.next_band(4)
        self.write_rows(4, "A Toothed Wheel and a Finger", [
            "Toothed wheel and a finger",
            "Click one way, jam the other",
            "Decides direction only",
            "Card and rubber band",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): One Way Only
        self.next_band(5)
        self.write_rows(5, "One Way Only", [
            "Winch: handle stays put",
            "Spanner: socket stays on",
            "Cable ties and handbrakes",
            "One way only",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Click, Hold, Release
        self.next_band(6)
        self.write_rows(6, "Click, Hold, Release", [
            "Arrow free, crossed arrow blocked",
            "Hard steel pawl",
            "Must release",
            "Fine teeth for fine holding",
        ], scale=0.9, box=2)

        last = Tex("A ratchet and pawl lets a wheel turn one way and locks it the other: a control that governs direction, used in winches, jacks, spanners and ties.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
