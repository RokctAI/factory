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

# Band-layout whiteboard scene for "Unemployment: Causes, Consequences and
# Solutions" (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier 5-7).
# Exporter-safe primitives only; add-only lifecycle.
# Subtopic durations: 220/230/220/230/190/200/190 of 1480 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class UnemploymentSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===================== Part 1 — Expert =====================
        # --- Band 0 (subtopic_1): definitions and measurement ---
        title = Tex("Unemployment: Causes, Consequences, Solutions").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0a = Tex("Strict: without work, available, actively seeking").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0a))
        self.wait(2)
        b0b = Tex("Expanded: adds discouraged work-seekers").scale(1.05).shift(UP * 0.4)
        self.play(Write(b0b))
        self.wait(2)
        b0wrong = Tex("Rate $=$ unemployed $\\div$ population").scale(1.0).shift(DOWN * 0.6)
        self.play(Write(b0wrong))
        self.play(Create(strike(b0wrong)))
        self.wait(1.5)
        b0c = MathTex(r"\text{Rate} = \frac{\text{unemployed}}{\text{labour force}} \times 100").scale(0.96).shift(DOWN * 1.8)
        self.play(Write(b0c))
        self.play(Create(SurroundingRectangle(b0c, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): SA's six characteristics ---
        self.next_band(1)
        b1t = Tex("SA unemployment — six characteristics").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = Tex("Structural: persists through upswings").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1b = Tex("Youth-concentrated: first-timers wait longest").scale(0.95).shift(band_shift(1) + UP * 0.5)
        b1c = Tex("Skill-divided: falls steeply as skill rises").scale(0.95).shift(band_shift(1) + DOWN * 0.2)
        b1d = Tex("Spatially uneven: former homelands heaviest").scale(0.95).shift(band_shift(1) + DOWN * 0.9)
        b1e = Tex("Long-term: joblessness erodes skills, networks").scale(0.95).shift(band_shift(1) + DOWN * 1.6)
        b1f = Tex("Large discouragement margin: expanded $>$ strict").scale(0.95).shift(band_shift(1) + DOWN * 2.3)
        for m in (b1a, b1b, b1c, b1d, b1e, b1f):
            self.play(Write(m))
            self.wait(1.5)
        b1g = Tex("So: growth alone will not clear it").scale(1.0).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1g))
        self.play(Create(SurroundingRectangle(b1g, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): frictional, structural, cyclical ---
        self.next_band(2)
        b2t = Tex("Types: the cure follows the cause").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex("FRICTIONAL: between jobs, short-term").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2a2 = Tex("$\\rightarrow$ remedy: information, job matching").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2a))
        self.play(Write(b2a2))
        self.wait(2.5)
        b2b = Tex("STRUCTURAL: skills or location mismatch —").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        b2b2 = Tex("SA's dominant type $\\rightarrow$ education, training,").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        b2b3 = Tex("spatial remedies").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2b))
        self.play(Write(b2b2))
        self.play(Write(b2b3))
        self.wait(2.5)
        b2c = Tex("CYCLICAL: downswing retrenchments $\\rightarrow$ demand").scale(1.0).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2c))
        self.wait(3)

        # --- Band 3 (subtopic_2): seasonal, technological ---
        self.next_band(3)
        b3t = Tex("Two more types complete the five").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("SEASONAL: harvest, holiday retail, tourism").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3a2 = Tex("$\\rightarrow$ diversification, off-season training").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3a))
        self.play(Write(b3a2))
        self.wait(2.5)
        b3b = Tex("TECHNOLOGICAL: machines replace tasks —").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        b3b2 = Tex("mechanised mining, automated tills").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        b3b3 = Tex("$\\rightarrow$ retrain toward the work machines create").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3b))
        self.play(Write(b3b2))
        self.play(Write(b3b3))
        self.wait(2.5)
        b3c = Tex("Diagnose the type, then match the remedy").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3c))
        self.play(Create(SurroundingRectangle(b3c, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): causes stacked in layers ---
        self.next_band(4)
        b4t = Tex("Causes stack in layers").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("Structural-historical: capital-intensive economy,").scale(0.95).shift(band_shift(4) + UP * 1.1)
        b4a2 = Tex("skills pipeline, apartheid's spatial legacy").scale(0.95).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4a))
        self.play(Write(b4a2))
        self.wait(2.5)
        b4b = Tex("Demand-side: slow growth, weak investment").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4b))
        self.wait(2)
        b4c = Tex("Supply-side: large cohorts arrive each year").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4c))
        self.wait(2)
        b4d = Tex("Frictions: information gaps, transport costs").scale(0.95).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4d))
        self.wait(2)
        b4e = Tex("A good answer names several layers").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4e))
        self.wait(3)

        # --- Band 5 (subtopic_3): consequences and the loop ---
        self.next_band(5)
        b5t = Tex("Consequences on three levels — and a loop").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("Individual: lost income, eroded skills, dignity").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5b = Tex("Economy: output forgone — inside the PPC;").scale(0.95).shift(band_shift(5) + UP * 0.5)
        b5b2 = Tex("weaker circular flow; budget squeezed both sides").scale(0.95).shift(band_shift(5) + DOWN * 0.2)
        b5c = Tex("Society: inequality, exclusion, strained cohesion").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5a))
        self.wait(2)
        self.play(Write(b5b))
        self.play(Write(b5b2))
        self.wait(2)
        self.play(Write(b5c))
        self.wait(2)
        l1 = Tex("less hiring").scale(0.85).shift(band_shift(5) + DOWN * 2.0 + LEFT * 4.4)
        l2 = Tex("less spending").scale(0.85).shift(band_shift(5) + DOWN * 2.0 + LEFT * 0.4)
        l3 = Tex("less production").scale(0.85).shift(band_shift(5) + DOWN * 2.0 + RIGHT * 3.8)
        la1 = Arrow(l1.get_right(), l2.get_left(), buff=0.15, color=RED)
        la2 = Arrow(l2.get_right(), l3.get_left(), buff=0.15, color=RED)
        la3 = Arrow(l3.get_bottom() + DOWN * 0.1, l1.get_bottom() + DOWN * 0.1,
                    buff=0.1, color=RED)
        self.play(Write(l1))
        self.play(Create(la1), Write(l2))
        self.play(Create(la2), Write(l3))
        self.play(Create(la3))
        self.wait(1.5)
        b5d = Tex("Solutions try to break this loop").scale(1.0).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5d))
        self.wait(3)

        # --- Band 6 (subtopic_4): the three approaches ---
        self.next_band(6)
        b6t = Tex("Three approaches, three jobs").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("Growth of production: sustainable jobs via").scale(0.95).shift(band_shift(6) + UP * 1.1)
        b6a2 = Tex("labour-intensive sectors, SMEs, exports —").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6a3 = Tex("limit: can bypass the unskilled").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(b6a))
        self.play(Write(b6a2))
        self.play(Write(b6a3))
        self.wait(2.5)
        b6b = Tex("Public works (EPWP): income, experience, assets —").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        b6b2 = Tex("limit: temporary; a bridge, not a destination").scale(0.95).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6b))
        self.play(Write(b6b2))
        self.wait(2.5)
        b6c = Tex("UIF (1\\% $+$ 1\\%): cushions the shock — limit:").scale(0.95).shift(band_shift(6) + DOWN * 2.8)
        b6c2 = Tex("only reaches those who WERE formally employed").scale(0.95).shift(band_shift(6) + DOWN * 3.5)
        self.play(Write(b6c))
        self.play(Write(b6c2))
        self.wait(3)

        # --- Band 7 (subtopic_4): diagnose before prescribing ---
        self.next_band(7)
        b7t = Tex("The mature conclusion").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("Cyclical needs demand; frictional needs").scale(1.05).shift(band_shift(7) + UP * 1.0)
        b7a2 = Tex("information; structural needs training and").scale(1.05).shift(band_shift(7) + UP * 0.3)
        b7a3 = Tex("spatial remedies — supported by the others").scale(1.05).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(b7a))
        self.play(Write(b7a2))
        self.play(Write(b7a3))
        self.wait(2.5)
        b7b = Tex("Diagnose before prescribing —").scale(1.1).shift(band_shift(7) + DOWN * 1.5)
        b7b2 = Tex("no single instrument solves a structural problem").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7b))
        self.play(Write(b7b2))
        self.play(Create(SurroundingRectangle(VGroup(b7b, b7b2), color=GREEN)))
        self.wait(3)

        # ===================== Part 2 — Simplifier =====================
        # --- Band 8 (subtopic_5): the queue that doesn't move ---
        self.next_band(8)
        b8t = Tex("The queue that doesn't move").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("YOUNG: first jobs need experience to get experience").scale(0.95).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex("SPLIT BY SKILL: three at the engineering firm's gate").scale(0.95).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("SPREAD UNEVENLY: the gate is two taxis away").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex("LONG-STANDING: each month rusts a skill").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8d))
        self.wait(2)
        b8e = Tex("Some stopped coming: strict count misses them,").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        b8e2 = Tex("expanded count sees them — ask which count").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8e))
        self.play(Write(b8e2))
        self.play(Create(SurroundingRectangle(b8e2, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): five stories, five fixes ---
        self.next_band(9)
        b9t = Tex("Five stories for the same empty hands").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("1. Graduate in the gap $\\rightarrow$ faster matching").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9a))
        self.wait(2)
        b9b = Tex("2. Shaft closed, skills fit nothing $\\rightarrow$ training,").scale(0.95).shift(band_shift(9) + UP * 0.4)
        b9b2 = Tex("trades, closing the distance — SA's big one").scale(0.95).shift(band_shift(9) + DOWN * 0.3)
        self.play(Write(b9b))
        self.play(Write(b9b2))
        self.wait(2)
        b9c = Tex("3. Downswing retrenchment $\\rightarrow$ demand").scale(0.95).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9c))
        self.wait(2)
        b9d = Tex("4. Fruit-picker's quiet months $\\rightarrow$ diversify").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        b9e = Tex("5. Replaced by the machine $\\rightarrow$ retrain").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9d))
        self.wait(2)
        self.play(Write(b9e))
        self.wait(2)
        b9f = Tex("One cure for all five? Someone's selling something").scale(0.9).shift(band_shift(9) + DOWN * 3.4)
        self.play(Write(b9f))
        self.wait(3)

        # --- Band 10 (subtopic_7): bridges, engines and nets ---
        self.next_band(10)
        b10t = Tex("Bridges, engines and nets").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("ENGINE — growth: but growing in WHAT?").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10a2 = Tex("Mines add machines; farms and sites add hands").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10a))
        self.play(Write(b10a2))
        self.wait(2.5)
        b10b = Tex("BRIDGE — public works: real income, real CV,").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        b10b2 = Tex("but it must LEAD somewhere").scale(0.95).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10b))
        self.play(Write(b10b2))
        self.wait(2.5)
        b10c = Tex("NET — UIF: claim only from a job you HAD;").scale(0.95).shift(band_shift(10) + DOWN * 2.1)
        b10c2 = Tex("the never-employed stand outside the net").scale(0.95).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10c))
        self.play(Write(b10c2))
        self.play(Create(SurroundingRectangle(b10c2, color=GREEN)))
        self.wait(4)
