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

# Band-layout whiteboard scene for design-brief-for-stairs-and-a-wheelchair-ramp (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/190/150/120/110/90 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DesignBriefForStairsAndAWheelchairRampSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Why a School Needs Both Stairs and a Ramp
        self.write_rows(0, "Why a School Needs Both Stairs and a Ramp", [
            "Raised floor: stairs for speed, ramp for access",
            "Accessibility is required by law",
            "Team = building firm bidding for the job",
            "Investigate the users first",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): The Numbers in a Design Brief: Steps, Risers, Width and Gradient
        self.next_band(1)
        self.write_rows(1, "The Numbers in a Design Brief: Steps, Risers, Width and Gradient", [
            "Rise 600; riser 150 to 180; equal risers",
            "600 / 150 = 4 steps; tread 250; width 1 200",
            "Ramp 1 in 12 or gentler: 7 200 long",
            "Specifications vs constraints",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Handrails, Landings and the Rules That Protect Users
        self.next_band(2)
        self.write_rows(2, "Handrails, Landings and the Rules That Protect Users", [
            "Handrails both sides, 900 to 1 000 high",
            "Landings at turns, ends, every 10 m",
            "Top landing clear of the door swing",
            "Non-slip surfaces for rain",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Steep ramp to save space''",
            "``Unequal risers to use up the height''",
            "``Handrail as decoration''",
            "``No landing at the top''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Two Ways Up to the Same Door
        self.next_band(4)
        self.write_rows(4, "Two Ways Up to the Same Door", [
            "Door 600 mm up",
            "Stairs: fast for most",
            "Ramp: access for all",
            "Ask who uses it",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Riser, Tread, Width and Slope
        self.next_band(5)
        self.write_rows(5, "Riser, Tread, Width and Slope", [
            "Riser 150, four equal steps",
            "Tread 250, width 1 200",
            "1 in 12: one up, twelve along",
            "Specs = must be; constraints = limits",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Rails and Rests
        self.next_band(6)
        self.write_rows(6, "Rails and Rests", [
            "Rails 900 to 1 000, both sides",
            "Kerb along the ramp",
            "Landings to rest",
            "Flat at the door",
        ], scale=0.9, box=3)

        last = Tex("Stairs for speed, a ramp at 1 in 12 for access, equal risers, rails at hand height and landings to rest: every number protects a user.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
