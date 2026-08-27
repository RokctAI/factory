# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from manim import *

# Band-layout whiteboard scene for "Business Cycles: Phases, Indicators and
# Causes" (grade 10, term 1). One band per teaching beat; camera moves down,
# earlier work stays. Exporter-safe mobjects only; the cycle wave and trend
# are hand-built from Line/Arrow segment chains (no Axes/ArcPolygon).
#
# Subtopic shares (subtopics.json, total 1450 s):
# 220/220/210/230/190/190/190.

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
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the wave around the trend ---
        title = Tex("Business Cycles").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        # Hand-built axes: two Arrows.
        origin = LEFT * 5.2 + DOWN * 2.4
        x_axis = Arrow(origin, origin + RIGHT * 9.6, buff=0, stroke_width=4)
        y_axis = Arrow(origin, origin + UP * 4.4, buff=0, stroke_width=4)
        self.play(Create(x_axis), Create(y_axis))
        xlab = Tex("Time").scale(0.9).next_to(x_axis.get_end(), DOWN, buff=0.2)
        ylab = Tex("Real GDP").scale(0.9).next_to(y_axis.get_end(), RIGHT, buff=0.2)
        self.play(Write(xlab), Write(ylab))
        self.wait(1.5)
        # Long-term trend: dashed rising line.
        trend = DashedLine(origin + RIGHT * 0.2 + UP * 0.7,
                           origin + RIGHT * 9.0 + UP * 3.0,
                           color=BLUE, stroke_width=4)
        self.play(Create(trend))
        tlab = Tex("trend", color=BLUE).scale(0.9).move_to(origin + RIGHT * 8.4 + UP * 3.5)
        self.play(Write(tlab))
        self.wait(1.5)
        # The wave: chained Line segments around the trend.
        pts = [origin + RIGHT * 0.2 + UP * 0.3,
               origin + RIGHT * 1.6 + UP * 2.0,
               origin + RIGHT * 2.8 + UP * 2.9,
               origin + RIGHT * 4.2 + UP * 1.2,
               origin + RIGHT * 5.2 + UP * 0.5,
               origin + RIGHT * 6.6 + UP * 2.3,
               origin + RIGHT * 8.2 + UP * 3.6]
        wave = VGroup(*[Line(pts[i], pts[i + 1], color=YELLOW, stroke_width=5)
                        for i in range(len(pts) - 1)])
        for seg in wave:
            self.play(Create(seg), run_time=0.6)
        self.wait(1.5)
        peak_dot = Dot(pts[2], color=RED)
        trough_dot = Dot(pts[4], color=RED)
        peak_lab = Tex("peak").scale(0.9).next_to(peak_dot, UP, buff=0.15)
        trough_lab = Tex("trough").scale(0.9).next_to(trough_dot, DOWN, buff=0.15)
        self.play(Create(peak_dot), Write(peak_lab))
        self.play(Create(trough_dot), Write(trough_lab))
        up_lab = Tex("upswing").scale(0.85).move_to(origin + RIGHT * 0.9 + UP * 2.4)
        down_lab = Tex("downswing").scale(0.85).move_to(origin + RIGHT * 4.6 + UP * 2.2)
        self.play(Write(up_lab))
        self.play(Write(down_lab))
        self.wait(3)

        # --- Band 1 (subtopic_1): four phases + recession definition ---
        self.next_band(1)
        b1t = Tex("Four phases, one discipline").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        b1a = Tex(r"UPSWING: production, jobs, incomes rise").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1b = Tex(r"PEAK: full capacity, prices pressing up").scale(1.0).shift(band_shift(1) + UP * 0.5)
        b1c = Tex(r"DOWNSWING: falling output, retrenchments").scale(1.0).shift(band_shift(1) + DOWN * 0.2)
        b1d = Tex(r"TROUGH: weakest — seeds of recovery").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1a))
        self.play(Write(b1b))
        self.play(Write(b1c))
        self.play(Write(b1d))
        self.wait(2.5)
        b1w = Tex(r"``Cycles run on a timetable''").scale(1.05).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1w))
        self.play(Create(strike(b1w)))
        self.wait(1.5)
        b1e = Tex(r"Recession: 2 consecutive quarters").scale(1.05).shift(band_shift(1) + DOWN * 2.6)
        b1f = Tex(r"of declining real GDP").scale(1.05).shift(band_shift(1) + DOWN * 3.2)
        self.play(Write(b1e))
        self.play(Write(b1f))
        self.play(Create(SurroundingRectangle(VGroup(b1e, b1f), color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): indicators by timing ---
        self.next_band(2)
        b2t = Tex("Indicators — classified by timing").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        b2a = Tex(r"LEADING: move BEFORE the turn").scale(1.05).shift(band_shift(2) + UP * 1.2)
        b2b = Tex(r"vehicle sales, building plans, shares").scale(0.95).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2a))
        self.play(Write(b2b))
        self.wait(2)
        b2c = Tex(r"COINCIDENT: move WITH the cycle").scale(1.05).shift(band_shift(2) + DOWN * 0.3)
        b2d = Tex(r"production, retail sales, employment").scale(0.95).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2c))
        self.play(Write(b2d))
        self.wait(2)
        b2e = Tex(r"LAGGING: turn AFTER the economy").scale(1.05).shift(band_shift(2) + DOWN * 1.8)
        b2f = Tex(r"unemployment, inventories, loans").scale(0.95).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2e))
        self.play(Write(b2f))
        self.wait(2)
        b2g = Tex(r"Warns — confirms — certifies").scale(1.05).shift(band_shift(2) + DOWN * 3.2)
        self.play(Write(b2g))
        self.play(Create(SurroundingRectangle(b2g, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the Reserve Bank's role ---
        self.next_band(3)
        b3t = Tex("Who reads the instruments?").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        b3a = Tex(r"The RESERVE BANK compiles composite").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3b = Tex(r"leading, coincident, lagging indicators").scale(1.05).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3a))
        self.play(Write(b3b))
        self.wait(2.5)
        b3c = Tex(r"...and officially DATES the cycle").scale(1.05).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3c))
        self.play(Create(SurroundingRectangle(b3c, color=GREEN)))
        self.wait(2)
        b3d = Tex(r"SA's waves: commodity prices, droughts,").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        b3e = Tex(r"global conditions, domestic confidence").scale(1.0).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3d))
        self.play(Write(b3e))
        self.wait(3)

        # --- Band 4 (subtopic_3): decomposing the time series ---
        self.next_band(4)
        b4t = Tex("Four movements in one series").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        b4a = Tex(r"TREND: decades-long direction").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4b = Tex(r"CYCLICAL: multi-year waves").scale(1.05).shift(band_shift(4) + UP * 0.5)
        b4c = Tex(r"SEASONAL: calendar patterns yearly").scale(1.05).shift(band_shift(4) + DOWN * 0.2)
        b4d = Tex(r"IRREGULAR: one-off shocks, no pattern").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4a))
        self.play(Write(b4b))
        self.play(Write(b4c))
        self.play(Write(b4d))
        self.wait(2.5)
        b4w = Tex(r"``December retail jump $=$ upswing''").scale(1.0).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4w))
        self.play(Create(strike(b4w)))
        self.wait(1.5)
        b4e = Tex(r"That's SEASON, not cycle — hence").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        b4f = Tex(r"seasonally adjusted figures").scale(1.0).shift(band_shift(4) + DOWN * 3.2)
        self.play(Write(b4e))
        self.play(Write(b4f))
        self.play(Create(SurroundingRectangle(b4f, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): exogenous vs endogenous causes ---
        self.next_band(5)
        b5t = Tex("Why cycles happen").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        b5a = Tex(r"EXOGENOUS — from OUTSIDE the system:").scale(1.05).shift(band_shift(5) + UP * 1.2)
        b5b = Tex(r"drought, wars, pandemics,").scale(1.0).shift(band_shift(5) + UP * 0.5)
        b5c = Tex(r"world commodity price swings").scale(1.0).shift(band_shift(5) + DOWN * 0.1)
        self.play(Write(b5a))
        self.play(Write(b5b))
        self.play(Write(b5c))
        self.wait(2.5)
        b5d = Tex(r"ENDOGENOUS — from INSIDE:").scale(1.05).shift(band_shift(5) + DOWN * 1.0)
        b5e = Tex(r"optimism waves, credit expanding").scale(1.0).shift(band_shift(5) + DOWN * 1.7)
        b5f = Tex(r"then tightening, injections vs leakages").scale(1.0).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5d))
        self.play(Write(b5e))
        self.play(Write(b5f))
        self.wait(2)
        b5g = Tex(r"Real cycles: outside shock, inside amplifier").scale(1.0).shift(band_shift(5) + DOWN * 3.2)
        self.play(Write(b5g))
        self.play(Create(SurroundingRectangle(b5g, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): effects phase by phase ---
        self.next_band(6)
        b6t = Tex("Effects — why the phase matters").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        b6a = Tex(r"Downswing: unemployment up, incomes").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6b = Tex(r"down, tax revenue falls as needs rise").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6a))
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = Tex(r"Postponed investment weakens the").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        b6d = Tex(r"NEXT upswing").scale(1.0).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6c))
        self.play(Write(b6d))
        self.wait(2)
        b6e = Tex(r"Upswing: jobs and revenue recover;").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        b6f = Tex(r"late boom: prices and interest rise").scale(1.0).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6e))
        self.play(Write(b6f))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the economy breathes ---
        self.next_band(7)
        b7t = Tex("The economy breathes").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex(r"Breathing in: more work, more spending").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7b = Tex(r"Full lungs: flat out, prices creeping").scale(1.0).shift(band_shift(7) + UP * 0.5)
        b7c = Tex(r"Breathing out: short shifts, quiet tills").scale(1.0).shift(band_shift(7) + DOWN * 0.2)
        b7d = Tex(r"Empty: hardest — but cheap, ready to turn").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7a))
        self.wait(1.5)
        self.play(Write(b7b))
        self.wait(1.5)
        self.play(Write(b7c))
        self.wait(1.5)
        self.play(Write(b7d))
        self.wait(2)
        b7e = Tex(r"Never on schedule; recession $=$").scale(1.05).shift(band_shift(7) + DOWN * 1.9)
        b7f = Tex(r"two quarters of shrinking production").scale(1.05).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7e))
        self.play(Write(b7f))
        self.play(Create(SurroundingRectangle(b7f, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): headlights, speedometer, mirror ---
        self.next_band(8)
        b8t = Tex("Headlights, speedometer, mirror").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"Headlights $=$ leading: building plans,").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8b = Tex(r"orders — tomorrow decided today").scale(1.0).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8a))
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex(r"Speedometer $=$ coincident: this").scale(1.0).shift(band_shift(8) + DOWN * 0.3)
        b8d = Tex(r"month's production, sales, jobs").scale(1.0).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(b8c))
        self.play(Write(b8d))
        self.wait(2)
        b8e = Tex(r"Mirror $=$ lagging: unemployment").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        b8f = Tex(r"peaks AFTER the trough").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8e))
        self.play(Write(b8f))
        self.play(Create(SurroundingRectangle(VGroup(b8e, b8f), color=GREEN)))
        self.wait(2)
        b8g = Tex(r"The Reserve Bank watches all three").scale(1.0).shift(band_shift(8) + DOWN * 3.2)
        self.play(Write(b8g))
        self.wait(3)

        # --- Band 9 (subtopic_7): why the wave comes, who gets wet ---
        self.next_band(9)
        b9t = Tex("Why the wave comes — who gets wet").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex(r"Outside stones: drought, oil, world").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9b = Tex(r"prices for platinum and coal").scale(1.0).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9a))
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex(r"Inside sloshing: mood and credit,").scale(1.0).shift(band_shift(9) + DOWN * 0.3)
        b9d = Tex(r"pumping the wave, cutting the trough").scale(1.0).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(b9c))
        self.play(Write(b9d))
        self.wait(2.5)
        b9e = Tex(r"Never equally wet: shop floor before").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        b9f = Tex(r"boardroom; the state squeezed both ways").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9e))
        self.play(Write(b9f))
        self.wait(2)
        b9g = Tex(r"Debt down at the peak, patience at the trough").scale(0.95).shift(band_shift(9) + DOWN * 3.3)
        self.play(Write(b9g))
        self.play(Create(SurroundingRectangle(b9g, color=GREEN)))
        self.wait(4)
