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

# Band-layout whiteboard scene for the session duo "Chords and Angles at the
# Centre" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics
# 5-7). One band per teaching beat, add-only lifecycle, camera moves down.
# Only exporter-supported mobjects; write-only reveals. Band dwell times
# follow subtopics.json (235/255/220/250/190/195/195 of 1540 s); Level 6
# rescales to real audio, so proportion is what matters.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ChordsAnglesAtCentreSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): vocabulary and the chord family
        title = Tex("Chords and Angles at the Centre").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        d1 = Tex("All radii of a circle are equal").scale(1.05).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2)
        d2 = Tex(r"Perpendicular from centre to chord \emph{bisects} it").scale(1.0).shift(DOWN * 0.1)
        d3 = Tex(r"Centre-to-midpoint meets the chord at $90^\circ$").scale(1.0).shift(DOWN * 1.0)
        d4 = Tex(r"Perpendicular bisector of a chord passes through centre").scale(0.95).shift(DOWN * 1.9)
        self.play(Write(d2))
        self.wait(2.5)
        self.play(Write(d3))
        self.wait(2)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the chord-distance triangle
        self.next_band(1)
        b1_title = Tex("Chord 24, radius 13: distance to centre?").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_c = Circle(radius=2.2, color=BLUE).shift(band_shift(1) + DOWN * 0.6)
        b1_ch = Line(b1_c.get_center() + 2.2 * LEFT * 0.92 + 0.85 * DOWN,
                     b1_c.get_center() + 2.2 * RIGHT * 0.92 + 0.85 * DOWN, color=YELLOW)
        self.play(Create(b1_c))
        self.play(Create(b1_ch))
        self.wait(2)
        b1_l1 = MathTex(r"\text{Half-chord} = 12, \; r = 13").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"d^2 = 13^2 - 12^2 = 25 \;\Rightarrow\; d = 5").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): centre is double — the theorem
        self.next_band(2)
        b2_title = Tex("Angle at centre $=$ twice angle at circumference").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\hat{AOB} = 2 \times \hat{ACB} \;\; \text{(same arc } AB\text{)}").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = Tex(r"Proof: line $C$ through $O$; radii $\Rightarrow$ isosceles").scale(0.95).shift(band_shift(2) + UP * 0.2)
        b2_l3 = Tex(r"Exterior angle: $\hat{AOD} = 2x$, $\hat{BOD} = 2y$").scale(0.95).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"\hat{AOB} = 2x + 2y, \quad \hat{ACB} = x + y").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l2))
        self.wait(2.5)
        self.play(Write(b2_l3))
        self.wait(2.5)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): using it, reflex arcs, semicircle
        self.next_band(3)
        b3_title = Tex("Halve the correct centre angle").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"120^\circ \text{ at centre} \Rightarrow 60^\circ \text{ at circumference}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"\text{Reflex } 200^\circ \Rightarrow 100^\circ \text{ on the major arc}").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("Shade the arc both angles stand on before halving").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = MathTex(r"\text{Diameter: } 180^\circ \Rightarrow 90^\circ \text{ — angle in semicircle}").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l3))
        self.wait(2.5)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): angles in the same segment
        self.next_band(4)
        b4_title = Tex("Angles in the same segment").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Same chord $AB$, same side: $\hat{ACB} = \hat{ADB}$").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(2.5)
        b4_l2 = Tex("Proof in one line: both are half of the same centre angle").scale(0.95).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"\hat{ACB} = 47^\circ \Rightarrow \hat{ADB} = 47^\circ \; \text{(same segment)}").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l2))
        self.wait(2.5)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex("Opposite sides = different segments: NOT equal").scale(0.95).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): the worked rider
        self.next_band(5)
        b5_title = Tex(r"Rider: $O$ centre, $\hat{AOB} = 80^\circ$ (minor arc)").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"1.\; \hat{ACB} = 40^\circ \;\; \text{(centre = twice circumference)}").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"2.\; OA = OB \;\; \text{(radii)}").scale(0.95).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"3.\; \hat{A} = \hat{B} \;\; \text{(base angles, isosceles)}").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        b5_l4 = MathTex(r"4.\; \hat{A} = \hat{B} = \tfrac{180 - 80}{2} = 50^\circ \;\; \text{(angle sum)}").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): extending the chain
        self.next_band(6)
        b6_title = Tex("Extend the chain: let $BC$ be a diameter").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\hat{BAC} = 90^\circ \;\; \text{(angle in semicircle)}").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"\hat{ABC} = 180^\circ - 90^\circ - 40^\circ = 50^\circ").scale(1.0).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex("Every new line spends a result from an earlier line").scale(0.95).shift(band_shift(6) + DOWN * 0.9)
        b6_l4 = Tex("Claim $+$ reason, or the line earns nothing").scale(0.95).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l3))
        self.wait(2.5)
        self.play(Write(b6_l4))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): folding the circle
        self.next_band(7)
        b7_title = Tex("Folding the circle").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_c = Circle(radius=1.8, color=BLUE).shift(band_shift(7) + DOWN * 1.3)
        self.play(Create(b7_c))
        self.wait(2)
        b7_l1 = Tex("Fold endpoint onto endpoint: the crease bisects at $90^\\circ$").scale(0.95).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("Every crease passes through the centre — two folds find it").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the stadium
        self.next_band(8)
        b8_title = Tex("The whole stadium sees the same game").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Every seat on the same arc: same viewing angle").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"\text{Centre } 120^\circ \Rightarrow \text{seats } 60^\circ").scale(1.05).shift(band_shift(8) + UP * 0.2)
        b8_l3 = MathTex(r"\text{Goal-chord a diameter} \Rightarrow \text{every seat } 90^\circ").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Shade the arc between the posts before halving").scale(0.95).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_7): the case file
        self.next_band(9)
        b9_title = Tex("Solving a rider like a case file").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("1. Darken the radii — isosceles triangles volunteer angles").scale(0.9).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("2. Hunt the diameter — a free $90^\\circ$ on the circle").scale(0.9).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("3. Shade the arc — halve on the correct side").scale(0.9).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"80^\circ \to 40^\circ \to 50^\circ, 50^\circ \;\; \text{— certainty by certainty}").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("A claim without a reason is a case without evidence").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(4)
