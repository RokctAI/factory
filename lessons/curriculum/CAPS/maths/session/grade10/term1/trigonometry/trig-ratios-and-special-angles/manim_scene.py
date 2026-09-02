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
# band per teaching beat, camera moves down to fresh space, nothing removed.
# Write-only reveals on single-string Tex/MathTex keep the export clean; the
# special triangles are hand-built from Lines + Tex labels (exporter-supported
# shapes only). Bands cover all seven subtopics (Part 1 — Expert: 1-4; Part 2
# — Simplifier: 5-7), dwell time proportional to subtopics.json
# (220/250/230/260/170/170/170 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TrigRatiosAndSpecialAnglesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the three ratios
        title = Tex("Trig Ratios and Special Angles").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1a = MathTex(r"\sin\theta = \frac{O}{H} \quad \cos\theta = \frac{A}{H}").scale(1.0).shift(UP * 1.1)
        l1b = MathTex(r"\tan\theta = \frac{O}{A}").scale(1.0).shift(UP * 0.2)
        self.play(Write(l1a))
        self.play(Write(l1b))
        self.play(Create(SurroundingRectangle(VGroup(l1a, l1b), color=YELLOW)))
        self.wait(2.5)
        l2 = Tex("SOH CAH TOA").scale(1.2).shift(DOWN * 0.8)
        self.play(Write(l2))
        self.wait(2)
        l3 = Tex(r"Same angle, any size: $\tfrac{5}{13} = \tfrac{10}{26}$").scale(1.0).shift(DOWN * 1.7)
        l4 = Tex(r"Opposite and adjacent belong to the ANGLE").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(l3))
        self.wait(2)
        self.play(Write(l4))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): the 60/30 triangle
        self.next_band(1)
        b1_title = Tex(r"Special triangle 1: equilateral, side 2, cut in half").scale(1.0).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        # half-equilateral triangle: base 1, height sqrt3, hyp 2
        A = band_shift(1) + LEFT * 5.4 + DOWN * 1.6
        B = A + RIGHT * 1.4
        C = B + UP * 2.4
        tri = VGroup(Line(A, B), Line(B, C), Line(C, A),
                     Line(B + LEFT * 0.22, B + LEFT * 0.22 + UP * 0.22),
                     Line(B + LEFT * 0.22 + UP * 0.22, B + UP * 0.22))
        self.play(Create(tri))
        lab_base = MathTex(r"1").scale(0.85).next_to(Line(A, B), DOWN, buff=0.15)
        lab_h = MathTex(r"\sqrt{3}").scale(0.85).next_to(Line(B, C), RIGHT, buff=0.15)
        lab_hyp = MathTex(r"2").scale(0.85).shift((A + C) / 2 + LEFT * 0.35)
        lab_60 = MathTex(r"60^\circ").scale(0.7).shift(A + RIGHT * 0.55 + UP * 0.22)
        lab_30 = MathTex(r"30^\circ").scale(0.7).shift(C + DOWN * 0.55 + LEFT * 0.1)
        self.play(Write(lab_base), Write(lab_h), Write(lab_hyp))
        self.play(Write(lab_60), Write(lab_30))
        self.wait(2)
        b1_s60 = MathTex(r"\sin 60^\circ = \tfrac{\sqrt{3}}{2}").scale(0.9).shift(band_shift(1) + RIGHT * 2.2 + UP * 1.4)
        b1_c60 = MathTex(r"\cos 60^\circ = \tfrac{1}{2}").scale(0.9).shift(band_shift(1) + RIGHT * 2.2 + UP * 0.65)
        b1_t60 = MathTex(r"\tan 60^\circ = \sqrt{3}").scale(0.9).shift(band_shift(1) + RIGHT * 2.2 + DOWN * 0.1)
        self.play(Write(b1_s60))
        self.play(Write(b1_c60))
        self.play(Write(b1_t60))
        self.wait(2.5)
        b1_s30 = MathTex(r"\sin 30^\circ = \tfrac{1}{2}").scale(0.9).shift(band_shift(1) + RIGHT * 2.2 + DOWN * 0.9)
        b1_c30 = MathTex(r"\cos 30^\circ = \tfrac{\sqrt{3}}{2}").scale(0.9).shift(band_shift(1) + RIGHT * 2.2 + DOWN * 1.65)
        b1_t30 = MathTex(r"\tan 30^\circ = \tfrac{1}{\sqrt{3}}").scale(0.9).shift(band_shift(1) + RIGHT * 2.2 + DOWN * 2.4)
        self.play(Write(b1_s30))
        self.play(Write(b1_c30))
        self.play(Write(b1_t30))
        self.wait(3)

        # --- Band 2 (subtopic_2): the 45 triangle + the evaluation
        self.next_band(2)
        b2_title = Tex(r"Special triangle 2: legs 1 and 1, hypotenuse $\sqrt{2}$").scale(1.0).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1a = MathTex(r"\sin 45^\circ = \cos 45^\circ = \tfrac{1}{\sqrt{2}}").scale(1.0).shift(band_shift(2) + UP * 1.4)
        b2_l1b = MathTex(r"\tan 45^\circ = 1").scale(1.0).shift(band_shift(2) + UP * 0.7)
        self.play(Write(b2_l1a))
        self.play(Write(b2_l1b))
        self.wait(2.5)
        b2_l2 = MathTex(r"\sin 60^\circ \cos 30^\circ - \tan 45^\circ").scale(1.1).shift(band_shift(2) + DOWN * 0.1)
        b2_l3 = MathTex(r"= \tfrac{\sqrt{3}}{2} \times \tfrac{\sqrt{3}}{2} - 1").scale(1.1).shift(band_shift(2) + DOWN * 1.0)
        b2_l4 = MathTex(r"= \tfrac{3}{4} - 1 = -\tfrac{1}{4}").scale(1.1).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2.5)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        b2_l5 = Tex("No calculator means exact answers — keep the fraction").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): the inverse move
        self.next_band(3)
        b3_title = Tex(r"Hypotenuse 13, opposite 5 — find $x$").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\sin x = \frac{5}{13}").scale(1.1).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex(r"Ratio known, angle wanted: run sine backwards").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"x = \sin^{-1}\!\left(\tfrac{5}{13}\right) = 22{,}6^\circ").scale(1.1).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex(r"Checks: $\tfrac{5}{13} < \tfrac{1}{2}$ so $x < 30^\circ$;").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        b3_l5 = MathTex(r"5, 12, 13: \; 22{,}6^\circ + 67{,}4^\circ = 90^\circ \;\checkmark").scale(0.85).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_4): the choosing routine + variations
        self.next_band(4)
        b4_title = Tex("The choosing routine").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"1. Mark the angle \; 2. Label the sides from it").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"3. Circle known and wanted \; 4. Match the letters").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"\text{Angle and } H: \; O = 13\sin 22{,}6^\circ = 5").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = MathTex(r"O = 5, A = 12: \; x = \tan^{-1}\!\tfrac{5}{12} = 22{,}6^\circ").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex(r"Traps: labels from the wrong angle; radian mode;").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        b4_l6 = Tex(r"inverse used in the wrong direction").scale(0.95).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): where you stand decides the names
        self.next_band(5)
        b5_title = Tex("Where you stand decides the names").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"Ladder, wall, ground — the ladder is the hypotenuse,").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"and it never changes its name").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex(r"Stand at the foot: wall is opposite, ground adjacent").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex(r"Climb to the top: the two swap — angle first, names second").scale(0.95).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex(r"Same slant, any ladder: like price per kilogram").scale(1.0).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5_l5))
        self.wait(2.5)

        # --- Band 6 (subtopic_6): two rebuildable shapes
        self.next_band(6)
        b6_title = Tex("Two triangles you can rebuild anywhere").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Paving slab, sides 2, cut down the middle:").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = MathTex(r"1, \; \sqrt{3}, \; 2 \;\text{ with } 30^\circ \text{ and } 60^\circ").scale(1.05).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"Floor tile, side 1, cut corner to corner:").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = MathTex(r"1, \; 1, \; \sqrt{2} \;\text{ with } 45^\circ").scale(1.05).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = MathTex(r"\tfrac{\sqrt{3}}{2} \times \tfrac{\sqrt{3}}{2} - 1 = \tfrac{3}{4} - 1 = -\tfrac{1}{4}").scale(0.85).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 7 (subtopic_7): forward gear, reverse gear
        self.next_band(7)
        b7_title = Tex("Forward gear, reverse gear").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"Forward: angle in, ratio out. Reverse: ratio in, angle out").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2a = MathTex(r"\sin x = \tfrac{5}{13}").scale(1.0).shift(band_shift(7) + UP * 0.45)
        b7_l2b = MathTex(r"x = \sin^{-1}\!\tfrac{5}{13} = 22{,}6^\circ").scale(1.0).shift(band_shift(7) + DOWN * 0.35)
        self.play(Write(b7_l2a))
        self.play(Write(b7_l2b))
        self.play(Create(SurroundingRectangle(b7_l2b, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex(r"Defend it: under $30^\circ$ since $\tfrac{5}{13} < \tfrac{1}{2}$,").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        b7_l4 = MathTex(r"\text{and } 22{,}6^\circ + 67{,}4^\circ = 90^\circ").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex(r"If $\sin 30^\circ$ shows $-0{,}988$: radian mode — fix the D").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5))
        self.wait(4)
