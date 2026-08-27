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

# Band-layout whiteboard scene for the session duo "What Economics Studies"
# (grade 10, term 1). One band per teaching beat; the camera moves down to
# fresh space and earlier work stays on the canvas. Only exporter-safe
# mobjects are used (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/
# SurroundingRectangle/VGroup); reveals are write-only.
#
# Subtopic time shares (subtopics.json, total 1440 s):
# 220/220/220/210/190/190/190 -> bands are apportioned accordingly.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class WhatEconomicsStudiesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the definition, needs and wants ---
        title = Tex("What Economics Studies").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex(r"Social science: LIMITED resources").scale(1.15).shift(UP * 1.0)
        d2 = Tex(r"vs UNLIMITED needs and wants").scale(1.15).shift(UP * 0.2)
        self.play(Write(d1))
        self.play(Write(d2))
        self.wait(2.5)
        d3 = Tex(r"NEEDS: survival and dignity").scale(1.05).shift(DOWN * 0.8)
        d4 = Tex(r"WANTS: endless — one dies, next steps up").scale(1.05).shift(DOWN * 1.6)
        self.play(Write(d3))
        self.wait(2)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(VGroup(d1, d2), color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): four factors, four rewards, three processes ---
        self.next_band(1)
        b1t = Tex("Four factors, four rewards").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        b1a = Tex(r"Natural resources $\rightarrow$ rent").scale(1.05).shift(band_shift(1) + UP * 1.2)
        b1b = Tex(r"Labour $\rightarrow$ wages").scale(1.05).shift(band_shift(1) + UP * 0.4)
        b1c = Tex(r"Capital $\rightarrow$ interest").scale(1.05).shift(band_shift(1) + DOWN * 0.4)
        b1d = Tex(r"Entrepreneurship $\rightarrow$ profit").scale(1.05).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1a))
        self.play(Write(b1b))
        self.play(Write(b1c))
        self.play(Write(b1d))
        self.wait(2.5)
        b1e = Tex(r"Processes: production, exchange, consumption").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1e))
        self.play(Create(SurroundingRectangle(b1e, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): micro vs macro ---
        self.next_band(2)
        b2t = Tex("Micro vs Macro").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        b2a = Tex(r"MICRO: one household, one firm,").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2b = Tex(r"one market — close range").scale(1.05).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2a))
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = Tex(r"MACRO: the economy as one whole —").scale(1.05).shift(band_shift(2) + DOWN * 0.6)
        b2d = Tex(r"inflation, unemployment, national output").scale(1.0).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2c))
        self.play(Write(b2d))
        self.wait(2.5)
        b2e = Tex(r"One shop's bread price: micro").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        b2f = Tex(r"the national cost of living: macro").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2e))
        self.play(Write(b2f))
        self.wait(3)

        # --- Band 3 (subtopic_2): working branches, positive vs normative ---
        self.next_band(3)
        b3t = Tex("Branches and two kinds of sentence").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        b3a = Tex(r"Theory, applied, history, development").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3a))
        self.wait(2)
        b3b = Tex(r"POSITIVE: what IS — testable").scale(1.05).shift(band_shift(3) + UP * 0.3)
        b3c = Tex(r"``growth was nought comma nine percent''").scale(0.95).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3b))
        self.play(Write(b3c))
        self.wait(2.5)
        b3d = Tex(r"NORMATIVE: what OUGHT to be").scale(1.05).shift(band_shift(3) + DOWN * 1.3)
        b3e = Tex(r"``the fuel levy should be scrapped''").scale(0.95).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3d))
        self.play(Write(b3e))
        box3 = SurroundingRectangle(VGroup(b3b, b3d), color=GREEN)
        self.play(Create(box3))
        self.wait(3)

        # --- Band 4 (subtopic_3): the scientific loop ---
        self.next_band(4)
        b4t = Tex("The method: a four-step loop").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        b4a = Tex(r"1. OBSERVATION — watch, record data").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4b = Tex(r"2. HYPOTHESIS — propose an explanation").scale(1.05).shift(band_shift(4) + UP * 0.4)
        b4c = Tex(r"3. TESTING — statistics and history").scale(1.05).shift(band_shift(4) + DOWN * 0.4)
        b4d = Tex(r"4. LAW — what survives, e.g. law of demand").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4a))
        self.wait(2)
        self.play(Write(b4b))
        self.wait(2)
        self.play(Write(b4c))
        self.wait(2)
        self.play(Write(b4d))
        self.wait(2)
        b4e = Tex(r"CETERIS PARIBUS: all else held equal").scale(1.05).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4e))
        self.play(Create(SurroundingRectangle(b4e, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): tools and honest limits ---
        self.next_band(5)
        b5t = Tex("Tools — and honest limits").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        b5a = Tex(r"Data: Stats SA, the Reserve Bank").scale(1.05).shift(band_shift(5) + UP * 1.2)
        b5b = Tex(r"Indices: CPI — thousands in one number").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5c = Tex(r"Models: simplified on purpose").scale(1.05).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5a))
        self.wait(2)
        self.play(Write(b5b))
        self.wait(2)
        self.play(Write(b5c))
        self.wait(2.5)
        b5d = Tex(r"People react to predictions —").scale(1.0).shift(band_shift(5) + DOWN * 1.4)
        b5e = Tex(r"so laws are tendencies, not certainties").scale(1.0).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5d))
        self.play(Write(b5e))
        self.wait(3)

        # --- Band 6 (subtopic_4): economics among the sciences ---
        self.next_band(6)
        b6t = Tex("Economics among the sciences").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        b6a = Tex(r"SOCIAL science: human behaviour").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6b = Tex(r"...but the most quantitative member").scale(1.05).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6a))
        self.play(Write(b6b))
        self.wait(2.5)
        b6w = Tex(r"``Economics $=$ chemistry with money''").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6w))
        self.play(Create(strike(b6w)))
        self.wait(2)
        b6c = Tex(r"No controlled repeats on a society —").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        b6d = Tex(r"scientific METHOD, human material").scale(1.05).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(b6c))
        self.play(Write(b6d))
        self.play(Create(SurroundingRectangle(b6d, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the science of not enough ---
        self.next_band(7)
        b7t = Tex("The science of not enough").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex(r"R60 at the tuckshop, endless wants").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7b = Tex(r"feed one want — the next steps up").scale(1.05).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7a))
        self.play(Write(b7b))
        self.wait(2.5)
        b7c = Tex(r"Car wash: yard, cousins, hose, nerve").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        b7d = Tex(r"= four factors in a driveway").scale(1.05).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7c))
        self.play(Write(b7d))
        self.wait(2.5)
        b7e = Tex(r"Make, swap, use — every economy's engine").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7e))
        self.play(Create(SurroundingRectangle(b7e, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): close-up lens, drone shot ---
        self.next_band(8)
        b8t = Tex("Close-up lens, drone shot").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"Close-up: the salon's braid price,").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8b = Tex(r"one firm hiring — micro").scale(1.05).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8a))
        self.play(Write(b8b))
        self.wait(2.5)
        b8c = Tex(r"Drone: all prices rising — inflation;").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        b8d = Tex(r"millions job-hunting — unemployment").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8c))
        self.play(Write(b8d))
        self.wait(2.5)
        b8e = Tex(r"Measure vs wish: positive vs normative").scale(1.0).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8e))
        self.play(Create(SurroundingRectangle(b8e, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): testing like a scientist ---
        self.next_band(9)
        b9t = Tex("Testing like a scientist").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex(r"Notice: Monday queues longest").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9b = Tex(r"Guess, then watch three Mondays").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9a))
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex(r"Ceteris paribus: one thread at a time").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9c))
        self.wait(2)
        b9d = Tex(r"Water never reacts to the forecast —").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        b9e = Tex(r"people do: a science that stays humble").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9d))
        self.play(Write(b9e))
        self.play(Create(SurroundingRectangle(b9e, color=GREEN)))
        self.wait(4)
