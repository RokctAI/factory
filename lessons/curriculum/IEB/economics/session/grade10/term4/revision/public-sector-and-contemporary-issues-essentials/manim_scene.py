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

# Band-layout whiteboard scene for the revision duo "Public Sector and
# Contemporary Issues Essentials" (Part 1 — Expert subtopics 1-4,
# Part 2 — Simplifier subtopics 5-7). Exporter-safe primitives only.
# Subtopic durations: 240/230/240/250/195/195/210 of 1560 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PublicSectorContemporaryRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===================== Part 1 — Expert =====================
        # --- Band 0 (subtopic_1): taxes and subsidies ---
        title = Tex("Revision Sweep Two: the State and the Big Issues").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0a = Tex("Tax: supply LEFT — dearer, less sold").scale(1.0).shift(UP * 1.1)
        self.play(Write(b0a))
        self.wait(2)
        b0b = Tex("Subsidy or zero-rating: supply RIGHT —").scale(1.0).shift(UP * 0.3)
        b0b2 = Tex("cheaper, more sold").scale(1.0).shift(DOWN * 0.4)
        self.play(Write(b0b))
        self.play(Write(b0b2))
        self.wait(2)
        b0c = Tex("Staples VAT-free; most goods at fifteen percent").scale(0.95).shift(DOWN * 1.3)
        self.play(Write(b0c))
        self.wait(2)
        b0d = Tex("The state shrinks markets it distrusts, widens others").scale(0.9).shift(DOWN * 2.2)
        self.play(Write(b0d))
        self.play(Create(SurroundingRectangle(b0d, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the ceiling makes a shortage ---
        self.next_band(1)
        b1t = Tex("Ceiling: pinned BELOW equilibrium").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        ax1v = Line(band_shift(1) + DOWN * 1.8 + LEFT * 3.2, band_shift(1) + UP * 1.4 + LEFT * 3.2)
        ax1h = Line(band_shift(1) + DOWN * 1.8 + LEFT * 3.2, band_shift(1) + DOWN * 1.8 + RIGHT * 2.8)
        self.play(Create(ax1v), Create(ax1h))
        dem1 = Line(band_shift(1) + UP * 1.2 + LEFT * 2.8, band_shift(1) + DOWN * 1.5 + RIGHT * 2.4)
        sup1 = Line(band_shift(1) + DOWN * 1.5 + LEFT * 2.8, band_shift(1) + UP * 1.2 + RIGHT * 2.4)
        self.play(Create(dem1), Create(sup1))
        self.wait(1.5)
        ceil = Line(band_shift(1) + DOWN * 0.9 + LEFT * 3.2, band_shift(1) + DOWN * 0.9 + RIGHT * 2.6,
                    color=YELLOW)
        t_ceil = Tex("ceiling").scale(0.8).shift(band_shift(1) + DOWN * 0.6 + RIGHT * 3.3)
        self.play(Create(ceil), Write(t_ceil))
        self.wait(2)
        b1a = Tex("Demand exceeds supply: a shortage that cannot close").scale(0.9).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1a))
        self.wait(2)
        b1b = Tex("Queues, rationing, black markets").scale(0.95).shift(band_shift(1) + DOWN * 3.2)
        self.play(Write(b1b))
        self.play(Create(SurroundingRectangle(b1b, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_1): the floor makes a surplus ---
        self.next_band(2)
        b2t = Tex("Floor: pinned ABOVE equilibrium").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex("Supply exceeds demand: a standing surplus —").scale(0.95).shift(band_shift(2) + UP * 1.0)
        b2a2 = Tex("buy it, store it, or export it at a loss").scale(0.95).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2a))
        self.play(Write(b2a2))
        self.wait(2.5)
        b2b = Tex("Minimum wage: a floor under labour").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2b))
        self.wait(2)
        b2c = Tex("Lifts earnings for those employed;").scale(0.95).shift(band_shift(2) + DOWN * 1.5)
        b2c2 = Tex("can reduce how many get hired").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2c))
        self.play(Write(b2c2))
        self.wait(2)
        b2d = Tex("Both halves, every time").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2d))
        self.play(Create(SurroundingRectangle(b2d, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): barter to industry in five stages ---
        self.next_band(3)
        b3t = Tex("Five stages, five problems solved").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("1 self-sufficiency $\\to$ 2 surplus and barter").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3a))
        self.wait(2)
        b3b = Tex("Barter's anchor: the double coincidence of wants").scale(0.95).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3b))
        self.wait(2)
        b3c = Tex("3 money: exchange $\\cdot$ account $\\cdot$ store $\\cdot$ deferred payment").scale(0.85).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3c))
        self.wait(2)
        b3d = Tex("4 the state: currency, contracts, courts, tax").scale(0.95).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3d))
        self.wait(2)
        b3e = Tex("5 industry: SA's mineral revolution — diamonds, gold").scale(0.9).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3e))
        self.play(Create(SurroundingRectangle(b3e, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): who counts, and derived demand ---
        self.next_band(4)
        b4t = Tex("The labour force, fenced").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        r4 = Rectangle(width=8.4, height=1.6).shift(band_shift(4) + UP * 0.6)
        t4 = Tex("15--64, working or actively seeking").scale(0.9).move_to(r4.get_center())
        self.play(Create(r4), Write(t4))
        self.wait(2)
        b4a = Tex("Outside: learners, homemakers, retired, discouraged").scale(0.9).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4a))
        self.wait(2)
        b4b = Tex("Demand for labour is DERIVED —").scale(0.95).shift(band_shift(4) + DOWN * 1.6)
        b4b2 = Tex("the bakery hires because bread sells").scale(0.95).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4b))
        self.play(Write(b4b2))
        self.play(Create(SurroundingRectangle(b4b2, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the three Acts and the ladder ---
        self.next_band(5)
        b5t = Tex("Three statutes, one ladder").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("Basic Conditions: the floor — hours, leave, notice").scale(0.9).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5a))
        self.wait(2)
        b5b = Tex("Labour Relations: unions, bargaining, strikes, lock-outs").scale(0.85).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5b))
        self.wait(2)
        b5c = Tex("Employment Equity: fair hiring, past exclusion corrected").scale(0.85).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5c))
        self.wait(2)
        b5d = Tex("Deadlock ladder: conciliation $\\to$ arbitration $\\to$ Labour Court").scale(0.85).shift(band_shift(5) + DOWN * 1.5)
        self.play(Write(b5d))
        self.wait(2)
        b5e = Tex("Procedure followed: protected strike").scale(0.95).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5e))
        self.play(Create(SurroundingRectangle(b5e, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): unemployment compressed ---
        self.next_band(6)
        b6t = Tex("Unemployment: the skeleton").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("Strict: seeking $\\cdot$ Expanded: plus discouraged").scale(0.95).shift(band_shift(6) + UP * 1.1)
        b6b = Tex("Rate: unemployed over LABOUR FORCE").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6a))
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = Tex("Five types: frictional, structural, cyclical,").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6c2 = Tex("seasonal, technological — cure follows cause").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6c))
        self.play(Write(b6c2))
        self.wait(2.5)
        b6d = Tex("Structural is South Africa's dominant type").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6d))
        self.play(Create(SurroundingRectangle(b6d, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): redress by factor, and the table ---
        self.next_band(7)
        b7t = Tex("Redress by factor of production").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("Land: restitution $\\cdot$ redistribution $\\cdot$ tenure").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7a))
        self.wait(2)
        b7b = Tex("Labour: equity + skills $\\cdot$ Capital: ownership + finance").scale(0.85).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7b))
        self.wait(2)
        b7c = Tex("Entrepreneurship: support to the first customer").scale(0.9).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7c))
        self.wait(2)
        b7d = Tex("Instrument + support, or no livelihood").scale(1.0).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7d))
        self.play(Create(SurroundingRectangle(b7d, color=GREEN)))
        self.wait(2)
        b7e = Tex("NEDLAC: government, business, labour, community").scale(0.9).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7e))
        self.wait(3)

        # ===================== Part 2 — Simplifier =====================
        # --- Band 8 (subtopic_5): referees, ceilings and floors ---
        self.next_band(8)
        b8t = Tex("Referees, ceilings and floors").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Tax: dearer on purpose $\\cdot$ zero-rate: cheaper on purpose").scale(0.85).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex("Ceilings make queues").scale(1.05).shift(band_shift(8) + UP * 0.2)
        b8c = Tex("Floors make piles").scale(1.05).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8b))
        self.play(Write(b8c))
        self.wait(2)
        b8wrong = Tex("A pinned price removes the shortage").scale(0.95).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8wrong))
        self.play(Create(strike(b8wrong)))
        self.wait(2)
        b8d = Tex("Minimum wage: protection and pressure, together").scale(0.95).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8d))
        self.play(Create(SurroundingRectangle(b8d, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): swapping goats to swiping cards ---
        self.next_band(9)
        b9t = Tex("From swapping goats to swiping cards").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Sipho's goat finds no partner —").scale(0.95).shift(band_shift(9) + UP * 1.1)
        b9a2 = Tex("the double coincidence fails him").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9a))
        self.play(Write(b9a2))
        self.wait(2.5)
        b9b = Tex("Money's four jobs: go-between, measuring rod,").scale(0.9).shift(band_shift(9) + DOWN * 0.5)
        b9b2 = Tex("storage jar, promise-keeper").scale(0.9).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9b))
        self.play(Write(b9b2))
        self.wait(2.5)
        b9c = Tex("Then the state, then the machines —").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        b9c2 = Tex("pulled inland by diamonds and gold").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9c))
        self.play(Write(b9c2))
        self.wait(3)

        # --- Band 10 (subtopic_7): the gate, the team, the starting line ---
        self.next_band(10)
        b10t = Tex("The gate, the team and the starting line").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("Team: 15--64, working or hunting for work").scale(0.95).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10a))
        self.wait(2)
        b10b = Tex("Rules: floor of conditions, one voice, fair hiring;").scale(0.9).shift(band_shift(10) + UP * 0.3)
        b10b2 = Tex("ladder: peacemaker, referee, court").scale(0.9).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10b))
        self.play(Write(b10b2))
        self.wait(2.5)
        b10c = Tex("Five queues in one: gap, mismatch, downswing,").scale(0.9).shift(band_shift(10) + DOWN * 1.3)
        b10c2 = Tex("season, machine — five different fixes").scale(0.9).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10c))
        self.play(Write(b10c2))
        self.wait(2.5)
        b10d = Tex("The starting line: redress, factor by factor").scale(0.95).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10d))
        self.play(Create(SurroundingRectangle(b10d, color=GREEN)))
        self.wait(4)
