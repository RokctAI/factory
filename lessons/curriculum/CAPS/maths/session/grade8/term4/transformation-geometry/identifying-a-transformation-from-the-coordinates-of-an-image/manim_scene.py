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
# dwell time proportional to subtopics.json (310/210/250/230/270/230/210 of
# 1710 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class IdentifyTransformationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Signs and Swaps
        t0 = Tex(r"Signs and Swaps").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = Tex(r"y negated: x-axis. x negated: y-axis. Swapped: line y equals x.").scale(1.05).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Both negated: rotation 180. Swapped, new x negated: 90 anticlockwise. Swapped, new y negated: 90 clockwise.").scale(1.05).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"(3;\ 2) \to (7;\ 5): \quad 7 - 3 = 4, \quad 5 - 2 = 3 \quad \text{translation}").scale(1.1).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Write the pairs one above the other; say what happened to x and to y").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): Describing Precisely
        self.next_band(1)
        t1 = Tex(r"Describing Precisely").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = Tex(r"Reflection: name the line. Translation: direction and distance, or the rule. Rotation: centre, angle, direction.").scale(1.05).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"(1;\ -3) \to (-2;\ 4): \quad -2 - 1 = -3, \quad 4 - (-3) = 7").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"Image minus original gives the shift; signs give the direction").scale(1.05).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Full sentence: a rotation of 90 degrees clockwise about the origin").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Checks
        self.next_band(2)
        t2 = Tex(r"Checks").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = Tex(r"Reflection: same distance from the mirror. Rotation: same distance from the centre. Translation: same shift for every point.").scale(1.05).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"3^2 + 2^2 = 13 = (-2)^2 + 3^2 \qquad 7^2 + 5^2 = 74 \neq 13").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = Tex(r"Distance from the origin changed: translation. Unchanged: reflection or rotation, decided by the pattern.").scale(1.05).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Off-origin centre: compare offsets from the centre").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): When One Point Is Not Enough
        self.next_band(3)
        t3 = Tex(r"When One Point Is Not Enough").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = Tex(r"A point on the mirror maps to itself; a point on an axis hides one coordinate's sign").scale(1.05).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"(4;\ 0) \to (-4;\ 0): \text{ y-axis reflection or } 180^\circ \text{ rotation}").scale(1.1).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"A second point off the line decides; translations are never ambiguous").scale(1.05).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"Give both answers if both fit, and say what would decide").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m16))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m16, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): The GPS Log
        self.next_band(4)
        t4 = Tex(r"The GPS Log").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"(3;\ 2) \to (2;\ -3): \text{ swap, new y negated, } 90^\circ \text{ clockwise}").scale(1.1).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"(5;\ -2) \to (1;\ 6): \quad 25 + 4 = 29 \neq 37 \text{: translation } (-4;\ 8)").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = Tex(r"Distance to the depot first; pattern second; a mid-point when the start is on an axis").scale(1.05).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"Compare, check, read, ask for more if needed").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m20))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m20, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): Reading Homework Backwards
        self.next_band(5)
        t5 = Tex(r"Reading Homework Backwards").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m21 = MathTex(r"(4;\ -3) \to (4;\ 3) \text{ is the x-axis reflection; y-axis gives } (-4;\ -3)").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m21))
        self.wait(2)
        m22 = MathTex(r"(-2;\ 5) \to (-5;\ -2) \text{ anticlockwise}; \quad (5;\ 2) \text{ is clockwise}").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"(1;\ 6) \to (6;\ 1): \text{ swap only, line } y = x").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m23))
        self.wait(2)
        m24 = Tex(r"Every written image names a transformation; compare it with the one asked").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m24))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m24, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_7): Examination Technique
        self.next_band(6)
        t6 = Tex(r"Examination Technique").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m25 = MathTex(r"(-3;\ 5) \to (5;\ 3): \text{ swap, new y negated: } 90^\circ \text{ clockwise}").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m25))
        self.wait(2)
        m26 = MathTex(r"(-3;\ 5) \to (3;\ -5): \text{ both negated: } 180^\circ \qquad (-3;\ 5) \to (2;\ 1): \text{ translation } (5;\ -4)").scale(1.1).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m26))
        self.wait(2)
        m27 = Tex(r"Distance first; pattern second; check; complete description").scale(1.05).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m27))
        self.wait(2)
        m28 = Tex(r"Swap only is a reflection; both answers when a point on an axis allows two").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m28))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m28, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
