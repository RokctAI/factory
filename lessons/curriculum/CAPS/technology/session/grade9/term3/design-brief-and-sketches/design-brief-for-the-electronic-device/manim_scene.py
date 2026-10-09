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

# Band-layout whiteboard scene for design-brief-for-the-electronic-device (Part 1 Expert
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


class DesignBriefForTheElectronicDeviceSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): From Investigation to Brief: One Sentence That Names the Need
        self.write_rows(0, "From Investigation to Brief: One Sentence That Names the Need", [
            "One sentence: product, job, user, setting",
            "No circuit named: need, not solution",
            "Each phrase traced to the investigation",
            "Team agrees; interview settles disputes",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Specifications for an Electronic Device
        self.next_band(1)
        self.write_rows(1, "Specifications for an Electronic Device", [
            "Input: detect below 1/5, no opening",
            "Output: visible 10 m daylight; sound switchable",
            "Supply: 4.5-6 V; < 0.5 mA standby; 6 months",
            "Enclosure, use, size: rain, 12 m wire, test button, phone-size",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Constraints, Evaluation Criteria and Team Agreement
        self.next_band(2)
        self.write_rows(2, "Constraints, Evaluation Criteria and Team Agreement", [
            "Constraints: kit + shop, ~80 rand, weeks 3-9, no mains",
            "Criteria written now: test per spec + five headings",
            "One page: sentence, specs, constraints, criteria, names",
            "First Design page of the PAT",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Brief sentence names the circuit''",
            "``Untestable specification such as must work well''",
            "``Budget mixed into specifications''",
            "``Brief written by one member and never read by the team''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Say What, for Whom, Where
        self.next_band(4)
        self.write_rows(4, "Say What, for Whom, Where", [
            "Say what, for whom, where",
            "Cut what you cannot trace",
            "Show clearly: light allowed, sound optional",
            "Everyone reads it",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Rules You Can Measure
        self.next_band(5)
        self.write_rows(5, "Rules You Can Measure", [
            "Rules with numbers",
            "Bright -> 10 m; reliable -> 20 tests",
            "Standby current, not six months",
            "Number them",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Limits You Cannot Move
        self.next_band(6)
        self.write_rows(6, "Limits You Cannot Move", [
            "Limits you cannot move",
            "Tests chosen before the device exists",
            "Purpose, safety, ergonomics, cost, looks",
            "Point at the page",
        ], scale=0.9, box=3)

        last = Tex("A brief states the need in one sentence, sets measurable specifications and fixed constraints, and names the tests before anything is built.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
