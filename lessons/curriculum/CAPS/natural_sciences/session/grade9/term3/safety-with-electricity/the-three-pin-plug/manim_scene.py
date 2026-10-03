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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ThreePinPlugSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Live, Neutral and Earth
        title = Tex("Three wires").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Live: brown (old: red), 230 V").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Neutral: blue (old: black), near 0 V").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Earth: green and yellow (old: green)").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Earth normally carries no current").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): How the Earth Wire Protects You
        self.next_band(1)
        b1_title = Tex("How earth protects").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Fault: live touches metal casing").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("No earth: casing stays live").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("With earth: large current to ground").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Breaker and earth leakage switch off").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Switches, Plugs and Double Insulation
        self.next_band(2)
        b2_title = Tex("Plugs and switches").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Switches and fuses in the live wire").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Earth pin longest: in first, out last").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Cord grip; correct terminals; no loose strands").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Double insulated: two pins").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Checking Plugs and the Error Museum
        self.next_band(3)
        b3_title = Tex("Checking plugs").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("No cracks or burn marks").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("No coloured wires showing").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Pull the plug, not the cord").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Keep plugs dry").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Checking Plugs and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Earth carries the return current''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Switch in either wire''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Brown is neutral''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``All pins equal''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Three Wires, Three Jobs
        self.next_band(5)
        b5_title = Tex("Three jobs").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Brown: live, brings it in").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Blue: neutral, takes it back").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Green and yellow: safety").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Never touch bare wires").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Escape Route
        self.next_band(6)
        b6_title = Tex("The escape route").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Cracked insulation").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("No earth: a hidden danger").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Earth: current escapes to ground").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Power switches off").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): The Longest Pin
        self.next_band(7)
        b7_title = Tex("The longest pin").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Earth pin in first, out last").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Switches in the live wire").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Square in a square: two pins").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Check, grip the plug, keep dry").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l1, color=YELLOW)))
        self.wait(4)
