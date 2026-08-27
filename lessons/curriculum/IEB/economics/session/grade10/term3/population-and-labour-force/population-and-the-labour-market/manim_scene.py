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

# Band-layout whiteboard scene for "Population and the Labour Market"
# (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier subtopics 5-7).
# Exporter-safe primitives only (axes are two Arrows, curves are Line
# chains); add-only lifecycle. Durations: 220/230/220/210/190/190/190 of 1450 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PopulationLabourMarketSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===================== Part 1 — Expert =====================
        # --- Band 0 (subtopic_1): only two forces change a population ---
        title = Tex("Population and the Labour Market").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0a = Tex("Only two forces change a population:").scale(1.1).shift(UP * 1.2)
        self.play(Write(b0a))
        self.wait(2)
        b0b = Tex("Natural growth $=$ births $-$ deaths").scale(1.1).shift(UP * 0.4)
        b0c = Tex("Migration $=$ arrivals $-$ departures").scale(1.1).shift(DOWN * 0.4)
        self.play(Write(b0b))
        self.wait(2)
        self.play(Write(b0c))
        self.wait(2)
        b0d = MathTex(r"30 - 12 = 18 \text{ per } 1\,000 = 1{,}8\% \text{ a year}").scale(1.1).shift(DOWN * 1.4)
        self.play(Write(b0d))
        self.play(Create(SurroundingRectangle(b0d, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the demographic cycle's four stages ---
        self.next_band(1)
        b1t = Tex("The demographic cycle — four stages").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = Tex("1. High stationary: many born, many die young").scale(1.0).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1a))
        self.wait(2)
        b1b = Tex("2. Early expanding: deaths COLLAPSE, births stay high").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1b))
        self.wait(2)
        b1c = Tex("3. Late expanding: births descend — growth decelerates").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1c))
        self.wait(2)
        b1d = Tex("4. Low stationary: both low — numbers level off").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1d))
        self.wait(2)
        b1e = Tex("SA: later expanding — young, still growing, slowing").scale(1.05).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1e))
        self.play(Create(SurroundingRectangle(b1e, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): Russian dolls of definitions ---
        self.next_band(2)
        b2t = Tex("Who is the labour force? Definitions nest").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        r_pop = Rectangle(width=11.0, height=4.6).shift(band_shift(2) + DOWN * 0.8)
        t_pop = Tex("Population: every person").scale(0.9).shift(band_shift(2) + UP * 1.1)
        self.play(Create(r_pop), Write(t_pop))
        self.wait(2)
        r_wa = Rectangle(width=9.0, height=3.2).shift(band_shift(2) + DOWN * 1.1)
        t_wa = Tex("Working age: 15--64 — could work").scale(0.9).shift(band_shift(2) + UP * 0.1)
        self.play(Create(r_wa), Write(t_wa))
        self.wait(2)
        r_lf = Rectangle(width=7.0, height=1.8).shift(band_shift(2) + DOWN * 1.5)
        t_lf = Tex("Labour force: employed $+$ strictly unemployed").scale(0.85).shift(band_shift(2) + DOWN * 1.1)
        t_lf2 = Tex("(no work, available, actively looking)").scale(0.8).shift(band_shift(2) + DOWN * 1.9)
        self.play(Create(r_lf), Write(t_lf))
        self.play(Write(t_lf2))
        self.wait(3)
        b2d = Tex("Discouraged seekers: strict drops them, expanded restores them").scale(0.9).shift(band_shift(2) + DOWN * 3.3)
        self.play(Write(b2d))
        self.wait(3)

        # --- Band 3 (subtopic_2): the two ratios and their denominators ---
        self.next_band(3)
        b3t = Tex("Every ratio needs its denominator").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3wrong = Tex("Unemployment rate $=$ unemployed $\\div$ population").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3wrong))
        self.play(Create(strike(b3wrong)))
        self.wait(2)
        b3a = MathTex(r"\text{Rate} = \frac{\text{unemployed}}{\text{labour force}} \times 100").scale(0.95).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3a))
        self.play(Create(SurroundingRectangle(b3a, color=GREEN)))
        self.wait(3)
        b3b = MathTex(r"\text{Participation} = \frac{\text{labour force}}{\text{working-age}} \times 100").scale(0.85).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3b))
        self.wait(2)
        b3c = Tex("Youth rate: young jobless $\\div$ YOUNG labour force").scale(0.9).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3c))
        self.wait(3)

        # --- Band 4 (subtopic_3): the labour market diagram ---
        self.next_band(4)
        b4t = Tex("The labour market: the wage is the price").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        O = band_shift(4) + DOWN * 2.4 + LEFT * 4.6

        def P(x, y):
            return O + RIGHT * x + UP * y

        ax_x = Arrow(P(0, 0), P(7.2, 0), buff=0, stroke_width=3)
        ax_y = Arrow(P(0, 0), P(0, 4.2), buff=0, stroke_width=3)
        lab_x = Tex("Quantity of labour").scale(0.8).move_to(P(6.0, -0.5))
        lab_y = Tex("Wage").scale(0.8).move_to(P(-0.8, 3.9))
        self.play(Create(ax_x), Create(ax_y))
        self.play(Write(lab_x), Write(lab_y))
        self.wait(2)
        sup = VGroup(
            Line(P(0.6, 0.5), P(3.0, 1.9), color=BLUE, stroke_width=5),
            Line(P(3.0, 1.9), P(5.6, 3.6), color=BLUE, stroke_width=5),
        )
        lab_s = Tex("S: households sell hours", color=BLUE).scale(0.75).move_to(P(5.4, 4.0))
        self.play(Create(sup[0]), Create(sup[1]))
        self.play(Write(lab_s))
        self.wait(2)
        dem = VGroup(
            Line(P(0.6, 3.6), P(3.0, 1.9), color=ORANGE, stroke_width=5),
            Line(P(3.0, 1.9), P(5.6, 0.5), color=ORANGE, stroke_width=5),
        )
        lab_d = Tex("D: firms buy (derived)", color=ORANGE).scale(0.75).move_to(P(6.2, 1.0))
        self.play(Create(dem[0]), Create(dem[1]))
        self.play(Write(lab_d))
        self.wait(2)
        eq = Dot(P(3.0, 1.9), color=GREEN)
        lab_e = Tex("going wage", color=GREEN).scale(0.75).move_to(P(1.8, 2.4))
        self.play(FadeIn(eq), Write(lab_e))
        self.wait(3)

        # --- Band 5 (subtopic_3): derived demand and the skill partition ---
        self.next_band(5)
        b5t = Tex("Derived demand, and a market split by skill").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("A firm hires for the OUTPUT workers generate:").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5a2 = Tex("no demand for wiring, no demand for electricians").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5a))
        self.play(Write(b5a2))
        self.wait(2.5)
        b5b = Tex("Scarce skills: demand chases supply — salaries climb").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5b))
        self.wait(2)
        b5c = Tex("Unskilled: supply dwarfs demand — pay squeezed down").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5c))
        self.wait(2)
        b5d = Tex("Skills mismatch: the structural core of SA unemployment").scale(0.95).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5d))
        self.play(Create(SurroundingRectangle(b5d, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): four habits for labour statistics ---
        self.next_band(6)
        b6t = Tex("Reading labour statistics — four habits").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2.5)
        b6a = Tex("1. Definition first: strict or expanded?").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6a))
        self.wait(2.5)
        b6b = Tex("2. Name the denominator every time").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = Tex("3. Look under the headline: age, province, skill").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6c))
        self.wait(2.5)
        b6d = Tex("4. Explain the mechanism behind the number").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6d))
        self.wait(2.5)
        b6box = SurroundingRectangle(VGroup(b6a, b6b, b6c, b6d), color=GREEN)
        self.play(Create(b6box))
        b6e = Tex("Analysis traces causes; description repeats figures").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6e))
        self.wait(3)

        # ===================== Part 2 — Simplifier =====================
        # --- Band 7 (subtopic_5): Mvubu Street as a census ---
        self.next_band(7)
        b7t = Tex("Mvubu Street as a census").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("Babies $-$ funerals $=$ natural growth;").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7a2 = Tex("add moved-in $-$ moved-out $=$ full change").scale(1.05).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7a))
        self.play(Write(b7a2))
        self.wait(2)
        b7b = Tex("Four chapters: cradles $=$ funerals $\\rightarrow$ clinic opens,").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7b2 = Tex("street swells $\\rightarrow$ smaller families $\\rightarrow$ frozen").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7b))
        self.play(Write(b7b2))
        self.wait(2.5)
        b7c = Tex("Every December a matric class joins the job queue").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7c))
        self.play(Create(SurroundingRectangle(b7c, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): sorting the Sunday table ---
        self.next_band(8)
        b8t = Tex("Sort the Sunday table onto the team sheet").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Ma, nurse on night shift: employed — on the field").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex("Uncle Vusi, four applications: unemployed — benched").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("Ayanda in matric: learner — off the sheet").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex("Sipho stopped applying: strict out, expanded in").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8d))
        self.wait(2)
        b8wrong = Tex("Divide the benched by the whole table").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8wrong))
        self.play(Create(strike(b8wrong)))
        b8right = Tex("Divide by the team: field $+$ bench").scale(1.05).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8right))
        self.play(Create(SurroundingRectangle(b8right, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): two gates at dawn ---
        self.next_band(9)
        b9t = Tex("The wage is a price at a gate").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Counter spun around: families SELL hours,").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9a2 = Tex("firms BUY them — the wage is the handshake price").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9a))
        self.play(Write(b9a2))
        self.wait(2.5)
        b9b = Tex("No orders, no shifts — demand is borrowed").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex("Artisans' gate: short queue, strong pay").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        b9d = Tex("General gate: queue round the block, wage near the floor").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9c))
        self.wait(2)
        self.play(Write(b9d))
        self.wait(2)
        b9e = Tex("A certificate is the boarding pass between gates").scale(1.05).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9e))
        self.play(Create(SurroundingRectangle(b9e, color=GREEN)))
        self.wait(4)
