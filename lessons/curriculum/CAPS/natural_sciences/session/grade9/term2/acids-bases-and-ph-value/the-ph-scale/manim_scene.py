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


class PhScaleSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Acids, Bases and Neutral Substances
        title = Tex("Acids, bases, neutral").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Acids release H+; formulae start with H").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Bases cancel acids; alkalis release OH-").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Neutral: pure water, salt and sugar solutions").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Strong bases are as corrosive as strong acids").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The pH Scale from 1 to 14
        self.next_band(1)
        b1_title = Tex("The pH scale").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Below 7: acidic. 7: neutral. Above 7: basic").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Further from 7: stronger").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = MathTex(r"10 \times 10 = 100").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("pH 3 is 100 times more acidic than pH 5").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): pH in Everyday Life and Safe Handling
        self.next_band(2)
        b2_title = Tex("pH in everyday life").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Stomach 1 to 2; blood 7,4").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Enamel dissolves below 5,5").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Crops: about 6 to 7; lime for acidic soil").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Always add acid to water").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Interpreting pH Data and the Error Museum
        self.next_band(3)
        b3_title = Tex("Interpreting data").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("pH 2: strong acid. pH 7: neutral").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("pH 9: weak base. pH 13: strong base").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Dilution moves pH towards 7").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("It never crosses 7 by dilution").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Interpreting pH Data and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``pH 1 is a weak acid''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``pH 10 is twice as basic as pH 5''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Bases are safe''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Add water to acid''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Sour and Soapy
        self.next_band(5)
        b5_title = Tex("Sour and soapy").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Acids: sour, like lemon and vinegar").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Bases: bitter and soapy").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Neutral: water, sugar water").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Acids and bases cancel out").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Number Line
        self.next_band(6)
        b6_title = Tex("The number line").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("7 in the middle").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Lemon 2, vinegar 3, coffee 5").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Sea water 8, ammonia 11, drain cleaner 14").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Each step is ten times").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): pH All Around You
        self.next_band(7)
        b7_title = Tex("pH all around you").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Stomach about 1 or 2").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Teeth dissolve below 5,5").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Blue hydrangeas: acidic soil").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Never mix cleaning products").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l2, color=YELLOW)))
        self.wait(4)
