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

# Band-layout whiteboard scene for the Electric Fields duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell proportional to subtopics.json (235/225/230/240/185/185/190
# of 1490 s). Exporter-safe mobjects only; add-only lifecycle; camera bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ElectricFieldConceptsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the definition ---
        title = Tex("Electric Fields").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("A region of space in which an electric").scale(1.0).shift(UP * 1.1)
        b0_l2 = Tex("charge experiences a force").scale(1.0).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(VGroup(b0_l1, b0_l2), color=BLUE)))
        self.wait(2.5)
        b0_l3 = Tex("Direction: the force on a POSITIVE test charge").scale(0.9).shift(DOWN * 0.7)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Away from positive, toward negative").scale(0.9).shift(DOWN * 1.5)
        self.play(Write(b0_l4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): field-line rules and patterns ---
        self.next_band(1)
        b1_title = Tex("Four rules of field lines").scale(1.1).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Start on positive, end on negative").scale(0.9).shift(band_shift(1) + UP * 1.3)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Never cross — one direction per point").scale(0.9).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Arrows follow the positive probe").scale(0.9).shift(band_shift(1) + DOWN * 0.3)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Crowded lines mean a strong field").scale(0.9).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1_l4))
        self.wait(2)
        centre = Dot(color=YELLOW).shift(band_shift(1) + DOWN * 2.4)
        rays = VGroup(*[
            Line(ORIGIN, 0.7 * np.array([np.cos(a), np.sin(a), 0]), color=BLUE).shift(band_shift(1) + DOWN * 2.4)
            for a in np.linspace(0, TAU, 8, endpoint=False)
        ])
        self.play(Create(centre), Create(rays))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): E = F/q forward ---
        self.next_band(2)
        b2_title = Tex("Field strength from force").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"E = \frac{F}{q} \quad [\text{N}\cdot\text{C}^{-1}]").scale(1.15).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=BLUE)))
        self.wait(2.5)
        b2_l2 = MathTex(r"E = \frac{0{,}02}{4 \times 10^{-6}} = 5\ 000\ \text{N}\cdot\text{C}^{-1}\ \text{north}").scale(0.95).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex("The field belongs to the place, not the visitor").scale(0.9).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l3))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): E = F/q backward, the electron ---
        self.next_band(3)
        b3_l1 = MathTex(r"F = Eq = 5\ 000 \times 1{,}6 \times 10^{-19}").scale(1.0).shift(band_shift(3) + UP * 1.6)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"F = 8 \times 10^{-16}\ \text{N — SOUTH, against the field}").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("Electrons read the map backwards").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("q is the FEELING charge, never the creator").scale(0.95).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): E = kQ/r^2 ---
        self.next_band(4)
        b4_title = Tex("Field of a point charge").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"E = \frac{kQq/r^2}{q} = \frac{kQ}{r^2}").scale(1.1).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=BLUE)))
        self.wait(2.5)
        b4_l2 = Tex("The test charge cancels — source and distance only").scale(0.9).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"E = \frac{9 \times 10^9 \times 8 \times 10^{-6}}{0{,}2^2} = \frac{72\ 000}{0{,}04}").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = MathTex(r"E = 1{,}8 \times 10^6\ \text{N}\cdot\text{C}^{-1}\ \text{away}").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): superposition setup ---
        self.next_band(5)
        b5_title = Tex(r"Two sources: $+4\ \mu$C at A, $-6\ \mu$C at B, P midway").scale(0.9).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"E_A = \frac{36\ 000}{0{,}09} = 4 \times 10^5\ \text{N}\cdot\text{C}^{-1}\ \text{(away from A)}").scale(0.85).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"E_B = \frac{54\ 000}{0{,}09} = 6 \times 10^5\ \text{N}\cdot\text{C}^{-1}\ \text{(toward B)}").scale(0.85).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Both arrows run from A toward B — they agree").scale(0.9).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): superposition result ---
        self.next_band(6)
        b6_l1 = MathTex(r"E_{net} = 4 \times 10^5 + 6 \times 10^5 = 1 \times 10^6\ \text{N}\cdot\text{C}^{-1}").scale(0.95).shift(band_shift(6) + UP * 1.5)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = Tex("Directed from A toward B").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Unlike charges: contributions cooperate between them").scale(0.9).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Like charges: they compete — a zero hides between").scale(0.9).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l4))
        self.wait(2.5)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the invisible cushion ---
        self.next_band(7)
        b7_title = Tex("The invisible cushion").scale(1.15).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(2)
        core = Dot(color=YELLOW).shift(band_shift(7) + UP * 0.6)
        rings = VGroup(*[Circle(radius=r, color=BLUE, stroke_opacity=1.0 - 0.25 * i).shift(band_shift(7) + UP * 0.6)
                         for i, r in enumerate([0.5, 1.0, 1.5, 2.0])])
        self.play(Create(core))
        self.play(Create(rings))
        self.wait(2.5)
        b7_l1 = Tex("Dense up close, fading with distance").scale(0.9).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("A visitor feels the cushion where it stands").scale(0.9).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l2))
        self.wait(3)

        # --- Band 8 (subtopic_6): the unit price ---
        self.next_band(8)
        b8_title = Tex("How hard is the shove at this spot?").scale(1.05).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("The shove depends on the probe —").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("so quote the shove PER COULOMB").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("Rand per litre; newtons per coulomb").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Twice as far from the source: a quarter of the rate").scale(0.9).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_7): two charges vote ---
        self.next_band(9)
        b9_title = Tex("When two charges both have a say").scale(1.05).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Between unlikes: both votes point the same way — add").scale(0.85).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Between likes: the votes clash — somewhere, ZERO").scale(0.85).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex("Thick bundle of lines from positive into negative").scale(0.85).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(3)

        # --- Band 10 (subtopic_7): the dead spot and the bookkeeping ---
        self.next_band(10)
        b10_l1 = Tex("Unequal likes: the dead spot sits nearer the weaker one").scale(0.85).shift(band_shift(10) + UP * 1.8)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Each contribution at its own distance,").scale(0.9).shift(band_shift(10) + UP * 0.7)
        b10_l3 = Tex("add when arrows agree, subtract when they clash").scale(0.9).shift(band_shift(10) + UP * 0.0)
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(VGroup(b10_l2, b10_l3), color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex("One arrow per charge, then let the arrows vote").scale(0.9).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l4))
        self.wait(4)
