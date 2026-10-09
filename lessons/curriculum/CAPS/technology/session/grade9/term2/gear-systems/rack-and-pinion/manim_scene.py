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

# Band-layout whiteboard scene for rack-and-pinion (Part 1 Expert
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


class RackAndPinionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Rack and Pinion: Turning Rotation Into Straight-Line Motion
        self.write_rows(0, "Rack and Pinion: Turning Rotation Into Straight-Line Motion", [
            "Rack: straight bar of teeth; pinion: small gear",
            "Rotary <-> linear, no slip, both ways",
            "Fixed rack: pinion travels; fixed pinion: rack travels",
            "Precision, not big force gain",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Automatic Gates and Steering Racks
        self.next_band(1)
        self.write_rows(1, "Automatic Gates and Steering Racks", [
            "Gate: rack on gate, motor pinion, limit switch",
            "Beam or safety edge; manual release",
            "Steering: column pinion, rack, tie rods",
            "Drill head, microscope, sluice, rack railway",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Calculating Rack Travel and Evaluating the Mechanism
        self.next_band(2)
        self.write_rows(2, "Calculating Rack Travel and Evaluating the Mechanism", [
            "Travel per turn = teeth x spacing: 12 x 10 = 120 mm",
            "4000 / 120 = about 33 turns",
            "Steering ratio from pinion size",
            "Evaluate: travel, backlash, guards, release",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Pinion teeth multiplied by rack teeth''",
            "``Mechanism assumed one-way''",
            "``Bigger pinion thought to give more force''",
            "``Gate designed without a manual release''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Gear and a Flat Gear
        self.next_band(4)
        self.write_rows(4, "A Gear and a Flat Gear", [
            "A gear and a flat gear",
            "Turn it, it slides",
            "Push it, it turns",
            "Changes the kind of motion",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Round and Round Becomes Back and Forth
        self.next_band(5)
        self.write_rows(5, "Round and Round Becomes Back and Forth", [
            "Gate: rack, motor, stop, beam, release",
            "Steering: wheel, pinion, rack, rods",
            "Small pinion: light and fine",
            "Drills and microscopes too",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): One Turn, One Tooth Length Each
        self.next_band(6)
        self.write_rows(6, "One Turn, One Tooth Length Each", [
            "One turn = one gap per tooth",
            "12 x 10 = 120",
            "Bigger pinion: further, harder",
            "Clean the grit; keep the release",
        ], scale=0.9, box=1)

        last = Tex("A rack and pinion turns rotation into straight-line motion and back; the rack moves one tooth spacing per pinion tooth per turn.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
