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
# dwell time proportional to subtopics.json (200/210/200/220/200/190/220 of
# 1440 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DivisionByZeroSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Division by Zero
        t0 = Tex(r"Division by Zero").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"12 \div 3 = 4 \quad \text{because} \quad 4 \times 3 = 12").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"a \div b = c \iff c \times b = a").scale(1.1).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex(r"Division asks a multiplication question").scale(1.05).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = MathTex(r"0 \div 12 = 0 \quad \text{because} \quad 0 \times 12 = 0").scale(1.1).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): $12 \div 0$: what times $0$ gives $12$?
        self.next_band(1)
        t1 = Tex(r"$12 \div 0$: what times $0$ gives $12$?").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"4 \times 0 = 0, \quad 100 \times 0 = 0, \quad 1\,000\,000 \times 0 = 0").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = Tex(r"Nothing times zero gives 12").scale(1.05).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"12 \div 0 \;\text{ is UNDEFINED}").scale(1.1).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m7, color=RED)))
        self.wait(1.5)
        m8 = MathTex(r"0 \div 12 = 0 \qquad 12 \div 0 \text{ undefined}").scale(1.1).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_2): $0 \div 0$: too many answers
        self.next_band(2)
        t2 = Tex(r"$0 \div 0$: too many answers").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"4 \times 0 = 0, \quad 7 \times 0 = 0, \quad 1\,000 \times 0 = 0").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = Tex(r"Every number works, so no single value exists").scale(1.05).shift(band_shift(2) + DOWN * 0.85)
        self.play(Write(m10))
        self.wait(2)
        m11 = Tex(r"Grade 8 rule: zero as the DIVISOR is never allowed").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m11))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m11, color=YELLOW)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_3): Shrink the divisor, watch the quotient
        self.next_band(3)
        t3 = Tex(r"Shrink the divisor, watch the quotient").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m12 = MathTex(r"12 \div 4 = 3, \quad 12 \div 2 = 6, \quad 12 \div 1 = 12").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m12))
        self.wait(2)
        m13 = MathTex(r"12 \div 0{,}1 = 120, \quad 12 \div 0{,}01 = 1\,200").scale(1.1).shift(band_shift(3) + UP * 0.18)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"12 \div 0{,}001 = 12\,000 \quad \ldots").scale(1.1).shift(band_shift(3) + DOWN * 0.85)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"Grows without limit — no value at zero").scale(1.05).shift(band_shift(3) + DOWN * 1.87)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"Calculator: Math Error. You write: undefined").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m16))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_4): Where the zero divisor hides
        self.next_band(4)
        t4 = Tex(r"Where the zero divisor hides").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"\frac{6}{x} \quad \Rightarrow \quad x \neq 0").scale(1.1).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"\text{speed} = \frac{120 \text{ km}}{0 \text{ h}} \quad \text{undefined}").scale(1.1).shift(band_shift(4) + UP * 0.18)
        self.play(Write(m18))
        self.wait(2)
        m19 = Tex(r"1. Find the divisor (underneath)").scale(1.05).shift(band_shift(4) + DOWN * 0.85)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"2. Divisor zero? UNDEFINED + reason").scale(1.05).shift(band_shift(4) + DOWN * 1.87)
        self.play(Write(m20))
        self.wait(2)
        m21 = Tex(r"3. Zero on top, non-zero below? Answer 0").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m21))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Sharing sweets with nobody
        self.next_band(5)
        t5 = Tex(r"Sharing sweets with nobody").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m22 = Tex(r"12 sweets, 3 friends: 4 each").scale(1.05).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m22))
        self.wait(2)
        m23 = Tex(r"12 sweets, 0 friends: nobody to receive — no answer").scale(1.05).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m23))
        self.wait(2)
        m24 = Tex(r"0 sweets, 12 friends: 0 each").scale(1.05).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m24))
        self.wait(2)
        m25 = MathTex(r"0 \div 12 = 0 \qquad 12 \div 0 \text{ undefined}").scale(1.1).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m25))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m25, color=YELLOW)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_6): The calculator that says Math Error
        self.next_band(6)
        t6 = Tex(r"The calculator that says Math Error").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m26 = MathTex(r"12 \div \tfrac{1}{2} = 24, \quad 12 \div 0{,}1 = 120").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m26))
        self.wait(2)
        m27 = MathTex(r"12 \div 0{,}01 = 1\,200, \quad 12 \div 0{,}001 = 12\,000").scale(1.1).shift(band_shift(6) + UP * 0.18)
        self.play(Write(m27))
        self.wait(2)
        m28 = Tex(r"The answer runs away as the divisor shrinks").scale(1.05).shift(band_shift(6) + DOWN * 0.85)
        self.play(Write(m28))
        self.wait(2)
        m29 = Tex(r"$12 \div 0$: Math Error — nothing to show").scale(1.05).shift(band_shift(6) + DOWN * 1.87)
        self.play(Write(m29))
        self.wait(2)
        m30 = Tex(r"Not infinity. Not zero. UNDEFINED.").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m30))
        self.wait(2)
        self.wait(3)

        # --- Band 7 (subtopic_7): Spotting a zero underneath
        self.next_band(7)
        t7 = Tex(r"Spotting a zero underneath").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(t7))
        self.wait(1.5)
        m31 = MathTex(r"\text{speed} = \frac{\text{distance}}{\text{time}}, \quad \text{average} = \frac{\text{total}}{\text{how many}}").scale(1.1).shift(band_shift(7) + UP * 1.2)
        self.play(Write(m31))
        self.wait(2)
        m32 = MathTex(r"\frac{120}{0} \;\text{ h} \quad \text{no trip, no speed}").scale(1.1).shift(band_shift(7) + DOWN * 0.17)
        self.play(Write(m32))
        self.wait(2)
        m33 = MathTex(r"\frac{6}{x}: \quad x \neq 0").scale(1.1).shift(band_shift(7) + DOWN * 1.53)
        self.play(Write(m33))
        self.wait(2)
        m34 = Tex(r"Zero on top: zero. Zero underneath: undefined.").scale(1.05).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(m34))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m34, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
