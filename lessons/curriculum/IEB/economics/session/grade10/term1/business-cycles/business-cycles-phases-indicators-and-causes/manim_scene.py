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

# Band-layout whiteboard scene for the session duo "Business Cycles: Phases,
# Indicators and Causes" (grade 10, term 1). One band per teaching beat; the
# camera moves down to fresh space and earlier work stays on the canvas. Only
# exporter-safe mobjects are used (Tex/MathTex/Line/Arrow/Dot/Circle/
# Rectangle/SurroundingRectangle/VGroup); reveals are write-only.
#
# Subtopic time shares (subtopics.json, total 1450 s):
# 220/220/210/230/190/190/190 -> bands are apportioned accordingly.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BusinessCyclesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the wave around the trend ---
        title = Tex("Business Cycles").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        # Trend line rising gently, with wave dots above and below it.
        trend = Line(LEFT * 4 + DOWN * 1.2, RIGHT * 4 + UP * 0.6, stroke_width=4)
        self.play(Create(trend))
        t_lab = Tex("trend").scale(0.9).shift(RIGHT * 3.2 + UP * 1.1)
        self.play(Write(t_lab))
        self.wait(1.5)
        w1 = Dot(LEFT * 3 + DOWN * 0.4)
        w2 = Dot(LEFT * 1 + UP * 0.6)
        w3 = Dot(RIGHT * 1 + DOWN * 0.6)
        w4 = Dot(RIGHT * 3 + UP * 1.0)
        self.play(Create(w1), Create(w2), Create(w3), Create(w4))
        wave_lab = Tex("the wave: above, below, again").scale(0.95).shift(DOWN * 1.9)
        self.play(Write(wave_lab))
        self.wait(2.5)
        d1 = Tex(r"Recurring rise and fall of activity").scale(1.05).shift(DOWN * 2.7)
        self.play(Write(d1))
        self.wait(3)

        # --- Band 1 (subtopic_1): four phases + recession definition ---
        self.next_band(1)
        b1t = Tex("Four phases").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        b1a = Tex(r"UPSWING: output, hiring, incomes rising").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1b = Tex(r"PEAK: full stretch, prices straining").scale(1.0).shift(band_shift(1) + UP * 0.4)
        b1c = Tex(r"DOWNSWING: sliding, retrenchments").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        b1d = Tex(r"TROUGH: weakest — recovery gathering").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1a))
        self.wait(2)
        self.play(Write(b1b))
        self.wait(2)
        self.play(Write(b1c))
        self.wait(2)
        self.play(Write(b1d))
        self.wait(2.5)
        b1e = Tex(r"Recession: two consecutive quarters").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        b1f = Tex(r"of declining real GDP").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1e))
        self.play(Write(b1f))
        self.play(Create(SurroundingRectangle(VGroup(b1e, b1f), color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): indicators by timing ---
        self.next_band(2)
        b2t = Tex("Indicators, classified by timing").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        b2a = Tex(r"LEADING: bend first — building plans,").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2b = Tex(r"new orders, shares, confidence").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2a))
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = Tex(r"COINCIDENT: move with — output,").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        b2d = Tex(r"retail sales, current employment").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2c))
        self.play(Write(b2d))
        self.wait(2.5)
        b2e = Tex(r"LAGGING: turn after — unemployment,").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        b2f = Tex(r"inventories, outstanding credit").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2e))
        self.play(Write(b2f))
        self.wait(3)

        # --- Band 3 (subtopic_2): the Reserve Bank's role ---
        self.next_band(3)
        b3t = Tex("The Reserve Bank's two jobs").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        b3a = Tex(r"1. Compile COMPOSITE indicators —").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3b = Tex(r"many series merged into one line").scale(1.05).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3a))
        self.play(Write(b3b))
        self.wait(2.5)
        b3c = Tex(r"2. DATE the cycle officially —").scale(1.05).shift(band_shift(3) + DOWN * 0.6)
        b3d = Tex(r"turning points announced after the fact").scale(1.0).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3c))
        self.play(Write(b3d))
        self.wait(2.5)
        b3e = Tex(r"Leading warns, coincident confirms,").scale(1.0).shift(band_shift(3) + DOWN * 2.2)
        b3f = Tex(r"lagging certifies").scale(1.0).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3e))
        self.play(Write(b3f))
        self.play(Create(SurroundingRectangle(b3f, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): decomposing the time series ---
        self.next_band(4)
        b4t = Tex("Four movements in one series").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        b4a = Tex(r"TREND: decades, gently upward").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4b = Tex(r"CYCLICAL: the multi-year wave").scale(1.0).shift(band_shift(4) + UP * 0.4)
        b4c = Tex(r"SEASONAL: December leaps, harvests").scale(1.0).shift(band_shift(4) + DOWN * 0.4)
        b4d = Tex(r"IRREGULAR: floods, strikes — noise").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4a))
        self.wait(2)
        self.play(Write(b4b))
        self.wait(2)
        self.play(Write(b4c))
        self.wait(2)
        self.play(Write(b4d))
        self.wait(2.5)
        b4w = Tex(r"``December's leap $=$ an upswing''").scale(1.0).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4w))
        self.play(Create(strike(b4w)))
        b4e = Tex(r"Ask WHICH movement you are seeing").scale(1.0).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4e))
        self.play(Create(SurroundingRectangle(b4e, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): exogenous vs endogenous causes ---
        self.next_band(5)
        b5t = Tex("Why cycles happen").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        b5a = Tex(r"EXOGENOUS: outside stones —").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5b = Tex(r"drought, war, pandemic, world prices").scale(1.0).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5a))
        self.play(Write(b5b))
        self.wait(2.5)
        b5c = Tex(r"ENDOGENOUS: inside the machine —").scale(1.05).shift(band_shift(5) + DOWN * 0.6)
        b5d = Tex(r"mood waves, credit swelling and snapping").scale(1.0).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5c))
        self.play(Write(b5d))
        self.wait(2.5)
        b5e = Tex(r"Real cycles: a stone in sloshing water").scale(1.0).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5e))
        self.play(Create(SurroundingRectangle(b5e, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): effects phase by phase ---
        self.next_band(6)
        b6t = Tex("Effects — never shared equally").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        b6a = Tex(r"Downswing: jobs lost, last hired first out").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6b = Tex(r"revenue falls as grant needs rise").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6a))
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = Tex(r"Postponed investment weakens").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        b6d = Tex(r"the NEXT upswing").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6c))
        self.play(Write(b6d))
        self.wait(2)
        b6e = Tex(r"Upswing: recovery — then prices").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        b6f = Tex(r"and interest rates push upward").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6e))
        self.play(Write(b6f))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the economy breathes ---
        self.next_band(7)
        b7t = Tex("The economy breathes").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex(r"Breathing in: hiring feeds spending").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7b = Tex(r"Full lungs: flat out, prices creeping").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7a))
        self.play(Write(b7b))
        self.wait(2.5)
        b7c = Tex(r"Breathing out: shifts shorten, cuts spread").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        b7d = Tex(r"Empty: hardest — yet recovery gathers").scale(1.0).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7c))
        self.play(Write(b7d))
        self.wait(2.5)
        b7e = Tex(r"Never on a timetable; recession $=$").scale(1.0).shift(band_shift(7) + DOWN * 2.2)
        b7f = Tex(r"two shrinking quarters in a row").scale(1.0).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7e))
        self.play(Write(b7f))
        self.play(Create(SurroundingRectangle(b7f, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): headlights, speedometer, mirror ---
        self.next_band(8)
        b8t = Tex("Three instruments, three directions").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"HEADLIGHTS ahead: plans, orders,").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8b = Tex(r"confidence — decisions about tomorrow").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8a))
        self.play(Write(b8b))
        self.wait(2.5)
        b8c = Tex(r"SPEEDOMETER now: output, sales, jobs").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex(r"MIRROR behind: unemployment peaks").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        b8e = Tex(r"after the trough has passed").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8d))
        self.play(Write(b8e))
        self.wait(2.5)
        b8f = Tex(r"Reserve Bank: watches all three dials").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8f))
        self.play(Create(SurroundingRectangle(b8f, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): why the wave comes, who gets wet ---
        self.next_band(9)
        b9t = Tex("Why the wave comes, who gets wet").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex(r"Outside: drought, oil, world ore prices").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9b = Tex(r"Inside: mood and credit, self-feeding").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9a))
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex(r"Wettest: last hired, least trained;").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        b9d = Tex(r"government squeezed from both ends").scale(1.0).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9c))
        self.play(Write(b9d))
        self.wait(2.5)
        b9e = Tex(r"Self-defence: settle debt near the peak,").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        b9f = Tex(r"hold steady near the trough").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9e))
        self.play(Write(b9f))
        self.play(Create(SurroundingRectangle(b9f, color=GREEN)))
        self.wait(4)
