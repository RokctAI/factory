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

# Band-layout whiteboard scene for worm-gears (Part 1 Expert
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


class WormGearsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The Worm and Wheel: A Screw That Drives a Gear
        self.write_rows(0, "The Worm and Wheel: A Screw That Drives a Gear", [
            "Worm: screw-threaded shaft; wheel: curved teeth",
            "Shafts at right angles",
            "One worm turn = one wheel tooth",
            "Worm drives wheel; not the reverse",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Large Speed Reduction and Force Increase in One Step
        self.next_band(1)
        self.write_rows(1, "Large Speed Reduction and Force Increase in One Step", [
            "Ratio = wheel teeth (single thread)",
            "40 teeth: 40:1; 1200 in -> 30 out",
            "~40x turning force, less large friction",
            "Efficiency 50-90\\%",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Self-Locking, Applications and Evaluation
        self.next_band(2)
        self.write_rows(2, "Self-Locking, Applications and Evaluation", [
            "Self-locking: load stays put",
            "Pegs, winches, gate motors, hoists, winders",
            "Draw: toothed circle, threaded cylinder across",
            "Evaluate: compact and holding; slow and lossy",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Either gear thought able to drive''",
            "``Ratio taken from worm diameter''",
            "``Friction loss ignored''",
            "``Worm gear expected to be fast''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Screw Turning a Wheel
        self.next_band(4)
        self.write_rows(4, "A Screw Turning a Wheel", [
            "A screw turning a wheel",
            "One turn, one tooth",
            "Shallow thread: wheel cannot push back",
            "Small pair, big reduction",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): One Turn, One Tooth
        self.next_band(5)
        self.write_rows(5, "One Turn, One Tooth", [
            "Ratio is the tooth count",
            "40 turns in, 1 out",
            "Slow and strong",
            "Friction eats a chunk",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Slow, Strong and Stays Put
        self.next_band(6)
        self.write_rows(6, "Slow, Strong and Stays Put", [
            "Stays in tune, stays wound, stays shut",
            "Circle plus cylinder, label ratio",
            "Grease it, guard it",
            "Slow, strong, stays put",
        ], scale=0.9, box=3)

        last = Tex("A worm gear advances its wheel one tooth per turn, giving a large reduction and force increase in one self-locking pair.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
