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
# dwell time proportional to subtopics.json (290/240/220/210/290/220/200 of
# 1670 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MissingLengthSurdsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Hypotenuse or Leg
        t0 = Tex(r"Hypotenuse or Leg").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"c^2 = 2^2 + 3^2 = 13 \Rightarrow c = \sqrt{13}").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"a^2 = 10^2 - 6^2 = 100 - 36 = 64 \Rightarrow a = 8").scale(1.1).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"a^2 = 7^2 - 4^2 = 49 - 16 = 33 \Rightarrow a = \sqrt{33}").scale(1.1).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Hypotenuse missing: add. Leg missing: subtract from the hypotenuse squared.").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): Simplifying Surds
        self.next_band(1)
        t1 = Tex(r"Simplifying Surds").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"\sqrt{50} = \sqrt{25 \times 2} = 5\sqrt{2} \qquad \sqrt{72} = \sqrt{36 \times 2} = 6\sqrt{2}").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"\sqrt{48} = 4\sqrt{3} \qquad \sqrt{20} = 2\sqrt{5} \qquad \sqrt{200} = 10\sqrt{2}").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"Take out the largest square factor: 4, 9, 16, 25, 36, 49, 64, 81, 100").scale(1.05).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"No square factor: leave it. Decimal only when asked, with the rounding stated.").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Diagonals and Heights
        self.next_band(2)
        t2 = Tex(r"Diagonals and Heights").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"d^2 = 3^2 + 5^2 = 34 \Rightarrow d = \sqrt{34} \qquad d = 80\sqrt{2} \approx 113{,}1").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"h^2 = 13^2 - 5^2 = 144 \Rightarrow h = 12").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"h^2 = 80^2 - 40^2 = 4\,800 \Rightarrow h = \sqrt{4\,800} = 40\sqrt{3} \approx 69{,}3").scale(1.1).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Drop a perpendicular from the apex: two congruent right-angled triangles").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Problems in Context
        self.next_band(3)
        t3 = Tex(r"Problems in Context").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"h^2 = 5^2 - 1{,}5^2 = 22{,}75 \Rightarrow h \approx 4{,}77 \text{ m}").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"12^2 + 9^2 = 225 \Rightarrow 15 \text{ km} \qquad 60^2 + 80^2 = 10\,000 \Rightarrow 100 \text{ m}").scale(1.1).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"100^2 - 80^2 = 3\,600 \Rightarrow 60 \text{ cm} \qquad 2^2 + 1^2 = 5 \Rightarrow \sqrt{5} \text{ m}").scale(1.1).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"Draw the triangle; exact surd unless told to round; decimal for cutting and buying").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m16))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m16, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): The Glazier's Two Lengths
        self.next_band(4)
        t4 = Tex(r"The Glazier's Two Lengths").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"d^2 = 80^2 + 80^2 = 12\,800 \Rightarrow d = 80\sqrt{2} \approx 113{,}1").scale(1.1).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"h^2 = 80^2 - 40^2 = 4\,800 \Rightarrow h = 40\sqrt{3} \approx 69{,}3").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"80 + 69{,}3 = 149{,}3 \qquad \sqrt{149{,}28^2 + 40^2} \approx 154{,}5").scale(1.1).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"Exact surds first, decimals second").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m20))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m20, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): The Ladder on Paper
        self.next_band(5)
        t5 = Tex(r"The Ladder on Paper").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m21 = MathTex(r"h^2 = 5^2 - 1{,}25^2 = 23{,}4375 \Rightarrow h \approx 4{,}84").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m21))
        self.wait(2)
        m22 = MathTex(r"h^2 = 6^2 - 1{,}5^2 = 33{,}75 \Rightarrow h \approx 5{,}81 \qquad h^2 = 25 - 9 = 16 \Rightarrow h = 4").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"h^2 = 8^2 - 2^2 = 60 \Rightarrow h = 2\sqrt{15} \approx 7{,}75").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m23))
        self.wait(2)
        m24 = Tex(r"Reach is a leg: always less than the ladder; the angle decides").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
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
        m25 = MathTex(r"c^2 = 5^2 + 5^2 = 50 \Rightarrow c = 5\sqrt{2} \qquad a^2 = 9^2 - 6^2 = 45 \Rightarrow a = 3\sqrt{5}").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m25))
        self.wait(2)
        m26 = MathTex(r"h^2 = 10^2 - 6^2 = 64 \Rightarrow h = 8").scale(1.1).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m26))
        self.wait(2)
        m27 = Tex(r"Add for the hypotenuse, subtract for a leg; three lines; simplify the surd").scale(1.05).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m27))
        self.wait(2)
        m28 = Tex(r"Create the right angle: diagonal, perpendicular from the apex, half-diagonals").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m28))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m28, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
