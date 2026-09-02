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

# Band-layout whiteboard scene for the session duo "GDP and GNI" (grade 10,
# term 1). One band per teaching beat; the camera moves down to fresh space
# and earlier work stays on the canvas. Only exporter-safe mobjects are used
# (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/SurroundingRectangle/VGroup);
# reveals are write-only.
#
# Subtopic time shares (subtopics.json, total 1440 s):
# 210/220/220/220/190/190/190 -> bands are apportioned accordingly.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GdpAndGniSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): three gauges on one pipe ---
        title = Tex("GDP and GNI").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex(r"Three gauges on one pipe:").scale(1.1).shift(UP * 1.0)
        self.play(Write(d1))
        self.wait(1.5)
        g1 = Tex(r"PRODUCTION — what firms create").scale(1.0).shift(UP * 0.2)
        g2 = Tex(r"INCOME — wages, rent, interest, profit").scale(1.0).shift(DOWN * 0.6)
        g3 = Tex(r"SPENDING — what buys the output").scale(1.0).shift(DOWN * 1.4)
        self.play(Write(g1))
        self.wait(2)
        self.play(Write(g2))
        self.wait(2)
        self.play(Write(g3))
        self.wait(2.5)
        d2 = Tex(r"In principle: one total").scale(1.05).shift(DOWN * 2.4)
        self.play(Write(d2))
        self.play(Create(SurroundingRectangle(d2, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the GDP definition, phrase by phrase ---
        self.next_band(1)
        b1t = Tex("GDP, phrase by phrase").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        b1a = Tex(r"Total MARKET VALUE — priced, addable").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1b = Tex(r"of all FINAL goods and services").scale(1.0).shift(band_shift(1) + UP * 0.4)
        b1c = Tex(r"produced WITHIN the borders").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        b1d = Tex(r"in a GIVEN PERIOD — a yearly flow").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1a))
        self.wait(2)
        self.play(Write(b1b))
        self.wait(2)
        self.play(Write(b1c))
        self.wait(2)
        self.play(Write(b1d))
        self.wait(2.5)
        b1e = Tex(r"Every phrase earns marks — recite in full").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1e))
        self.play(Create(SurroundingRectangle(VGroup(b1a, b1d), color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the wool chain, no double counting ---
        self.next_band(2)
        b2t = Tex("The wool chain — count once").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        b2a = Tex(r"Fleece R30 $\rightarrow$ yarn R70 $\rightarrow$ jersey R200").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2a))
        self.wait(2.5)
        b2w = Tex(r"``GDP $=$ 30 + 70 + 200 $=$ R300''").scale(1.0).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2w))
        self.play(Create(strike(b2w)))
        self.wait(2)
        b2b = Tex(r"Only R200 of value exists —").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        b2c = Tex(r"fleece and yarn live inside the jersey").scale(1.0).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2b))
        self.play(Write(b2c))
        self.wait(2.5)
        b2d = Tex(r"Value added: 30 + 40 + 130 $=$ R200").scale(1.0).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2d))
        self.play(Create(SurroundingRectangle(b2d, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the border rule and the excluded list ---
        self.next_band(3)
        b3t = Tex("The border rule — and the excluded").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        b3a = Tex(r"Australian-owned mine on our soil:").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3b = Tex(r"counts HERE — geography, not passports").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3a))
        self.play(Write(b3b))
        self.wait(2.5)
        b3c = Tex(r"Our nurse in London: Britain's GDP").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3c))
        self.wait(2)
        b3d = Tex(r"Excluded: second-hand sales, share").scale(1.0).shift(band_shift(3) + DOWN * 1.3)
        b3e = Tex(r"shuffles, grants, most unpaid work —").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        b3f = Tex(r"nothing NEW is produced").scale(1.0).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3d))
        self.play(Write(b3e))
        self.play(Write(b3f))
        self.play(Create(SurroundingRectangle(b3f, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): GNI and the bridge ---
        self.next_band(4)
        b4t = Tex("GNI — following the factors home").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        b4a = Tex(r"GDP: WHERE produced").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4b = Tex(r"GNI: WHO earned the income").scale(1.05).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4a))
        self.play(Write(b4b))
        self.wait(2.5)
        b4c = Tex(r"GNI $=$ GDP $-$ factor income out").scale(1.05).shift(band_shift(4) + DOWN * 0.5)
        b4d = Tex(r"$+$ factor income in").scale(1.05).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4c))
        self.play(Write(b4d))
        self.play(Create(SurroundingRectangle(VGroup(b4c, b4d), color=GREEN)))
        self.wait(2.5)
        b4e = Tex(r"SA: GNI a bit below GDP; Lesotho: above").scale(0.95).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4e))
        self.wait(3)

        # --- Band 5 (subtopic_4): per capita and the limits ---
        self.next_band(5)
        b5t = Tex("Corrections and honest limits").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        b5a = Tex(r"Per capita: divide by population").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5b = Tex(r"Compare years: strip out inflation").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5a))
        self.play(Write(b5b))
        self.wait(2.5)
        b5c = Tex(r"Blind to: distribution, unpaid work,").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        b5d = Tex(r"well-being, the environment").scale(1.0).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5c))
        self.play(Write(b5d))
        self.wait(2.5)
        b5e = Tex(r"A speedometer, not a report card").scale(1.05).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5e))
        self.play(Create(SurroundingRectangle(b5e, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): counting everything the street made ---
        self.next_band(6)
        b6t = Tex("Counting the street's year").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex(r"Tuckshop, salon, panel beater, car wash").scale(1.0).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6a))
        self.wait(2)
        b6b = Tex(r"Parts R400 inside the R1 500 repair —").scale(1.0).shift(band_shift(6) + UP * 0.3)
        b6c = Tex(r"count once, or count the R1 100 added").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6b))
        self.play(Write(b6c))
        self.wait(2.5)
        b6d = Tex(r"Old bakkie resold, granny's grant:").scale(1.0).shift(band_shift(6) + DOWN * 1.4)
        b6e = Tex(r"money moved, nothing new made").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6d))
        self.play(Write(b6e))
        self.play(Create(SurroundingRectangle(b6e, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_6): the where-rule and the who-rule ---
        self.next_band(7)
        b7t = Tex("The where-rule and the who-rule").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex(r"WHERE (GDP): made on this street —").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7b = Tex(r"outsider's bottle store counts here").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7a))
        self.play(Write(b7b))
        self.wait(2.5)
        b7c = Tex(r"WHO (GNI): earned by our people —").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        b7d = Tex(r"the daughter in Cape Town counts now").scale(1.0).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7c))
        self.play(Write(b7d))
        self.wait(2.5)
        b7e = Tex(r"The GAP between them is the story").scale(1.05).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7e))
        self.play(Create(SurroundingRectangle(b7e, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_7): what the big number can't see ---
        self.next_band(8)
        b8t = Tex("What the big number can't see").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"1. Who got it — averages bury the split").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8b = Tex(r"2. Work with no till — gran's childcare").scale(1.0).shift(band_shift(8) + UP * 0.4)
        b8c = Tex(r"3. How life feels — safety, learning").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        b8d = Tex(r"4. What got used up — the felled tree").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8a))
        self.wait(2)
        self.play(Write(b8b))
        self.wait(2)
        self.play(Write(b8c))
        self.wait(2)
        self.play(Write(b8d))
        self.wait(2.5)
        b8e = Tex(r"Count carefully; question the count").scale(1.05).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8e))
        self.play(Create(SurroundingRectangle(b8e, color=GREEN)))
        self.wait(4)
