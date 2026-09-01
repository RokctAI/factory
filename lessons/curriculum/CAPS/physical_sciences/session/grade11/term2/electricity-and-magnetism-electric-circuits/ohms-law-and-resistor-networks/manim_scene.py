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

# Band-layout whiteboard scene for the Ohm's Law and Resistor Networks duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell proportional to subtopics.json (225/240/240/240/185/190/190
# of 1510 s). Exporter-safe mobjects only (circuit drawn from Rectangles,
# Lines and Tex labels); add-only lifecycle; camera bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class OhmsLawResistorNetworksSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): Ohm's law ---
        title = Tex("Ohm's Law and Resistor Networks").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("$I \\propto V$, provided temperature is constant").scale(1.0).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = MathTex(r"R = \frac{V}{I}").scale(1.3).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=BLUE)))
        self.wait(2.5)
        b0_l3 = MathTex(r"V = IR, \quad I = \frac{V}{R}").scale(1.05).shift(DOWN * 1.2)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = MathTex(r"\frac{12\ \text{V}}{3\ \text{A}} = 4\ \Omega").scale(1.05).shift(DOWN * 2.4)
        self.play(Write(b0_l4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): ohmic vs non-ohmic graphs ---
        self.next_band(1)
        b1_title = Tex("Ohmic vs non-ohmic").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        # left graph: ohmic straight line
        axL_x = Arrow(LEFT * 5.5 + DOWN * 1.6, LEFT * 2.3 + DOWN * 1.6, buff=0)
        axL_y = Arrow(LEFT * 5.5 + DOWN * 1.6, LEFT * 5.5 + UP * 1.2, buff=0)
        lLx = MathTex(r"V").scale(0.8).shift(band_shift(1) + LEFT * 2.1 + DOWN * 1.9)
        lLy = MathTex(r"I").scale(0.8).shift(band_shift(1) + LEFT * 5.8 + UP * 1.2)
        ohmic = Line(LEFT * 5.5 + DOWN * 1.6, LEFT * 2.7 + UP * 0.9, color=GREEN)
        for m in (axL_x, axL_y, ohmic):
            m.shift(band_shift(1))
        self.play(Create(axL_x), Create(axL_y), Write(lLx), Write(lLy))
        self.play(Create(ohmic))
        lohm = Tex("straight through origin").scale(0.75).shift(band_shift(1) + LEFT * 4.0 + UP * 1.5)
        self.play(Write(lohm))
        self.wait(2)
        # right graph: filament flattening polyline
        axR_x = Arrow(RIGHT * 0.7 + DOWN * 1.6, RIGHT * 3.9 + DOWN * 1.6, buff=0)
        axR_y = Arrow(RIGHT * 0.7 + DOWN * 1.6, RIGHT * 0.7 + UP * 1.2, buff=0)
        lRx = MathTex(r"V").scale(0.8).shift(band_shift(1) + RIGHT * 4.2 + DOWN * 1.9)
        lRy = MathTex(r"I").scale(0.8).shift(band_shift(1) + RIGHT * 0.4 + UP * 1.2)
        fil = VGroup(
            Line(RIGHT * 0.7 + DOWN * 1.6, RIGHT * 1.5 + DOWN * 0.6, color=YELLOW),
            Line(RIGHT * 1.5 + DOWN * 0.6, RIGHT * 2.3 + UP * 0.0, color=YELLOW),
            Line(RIGHT * 2.3 + UP * 0.0, RIGHT * 3.1 + UP * 0.35, color=YELLOW),
            Line(RIGHT * 3.1 + UP * 0.35, RIGHT * 3.8 + UP * 0.55, color=YELLOW),
        )
        for m in (axR_x, axR_y, fil):
            m.shift(band_shift(1))
        self.play(Create(axR_x), Create(axR_y), Write(lRx), Write(lRy))
        self.play(Create(fil))
        lfil = Tex("filament: flattens").scale(0.75).shift(band_shift(1) + RIGHT * 2.6 + UP * 1.5)
        self.play(Write(lfil))
        self.wait(2)
        b1_l1 = Tex("Hot filament: resistance climbs with temperature").scale(0.9).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l1))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): series ---
        self.next_band(2)
        b2_title = Tex("Series: one path, same current").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        w1 = Line(LEFT * 4.0 + UP * 1.2, LEFT * 2.2 + UP * 1.2)
        r1 = Rectangle(width=1.4, height=0.6).shift(LEFT * 1.5 + UP * 1.2)
        w2 = Line(LEFT * 0.8 + UP * 1.2, RIGHT * 0.6 + UP * 1.2)
        r2 = Rectangle(width=1.4, height=0.6).shift(RIGHT * 1.3 + UP * 1.2)
        w3 = Line(RIGHT * 2.0 + UP * 1.2, RIGHT * 3.8 + UP * 1.2)
        lr1 = MathTex(r"4\ \Omega").scale(0.85).shift(LEFT * 1.5 + UP * 2.0)
        lr2 = MathTex(r"12\ \Omega").scale(0.85).shift(RIGHT * 1.3 + UP * 2.0)
        for m in (w1, r1, w2, r2, w3, lr1, lr2):
            m.shift(band_shift(2))
        self.play(Create(w1), Create(r1), Write(lr1))
        self.play(Create(w2), Create(r2), Write(lr2), Create(w3))
        self.wait(2)
        b2_l1 = MathTex(r"R_{tot} = R_1 + R_2 + R_3").scale(1.1).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=BLUE)))
        self.wait(2.5)
        b2_l2 = MathTex(r"4 + 12 = 16\ \Omega").scale(1.1).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("Each added resistor: another obstacle").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l3))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): parallel ---
        self.next_band(3)
        b3_title = Tex("Parallel: same voltage, currents add").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\frac{1}{R_{tot}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}").scale(1.05).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=BLUE)))
        self.wait(2.5)
        b3_l2 = MathTex(r"\frac{4 \times 12}{4 + 12} = \frac{48}{16} = 3\ \Omega").scale(1.05).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("ALWAYS below the smallest branch").scale(1.0).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = MathTex(r"\tfrac{1}{6} + \tfrac{2}{6} + \tfrac{3}{6} = 1 \;\Rightarrow\; 1\ \Omega").scale(0.9).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Remember to flip the reciprocal at the end").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the mixed network diagram ---
        self.next_band(4)
        b4_title = Tex(r"12 V battery, 2 $\Omega$, then 6 $\Omega$ and 3 $\Omega$").scale(0.95).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        bat = Rectangle(width=0.7, height=1.2).shift(LEFT * 4.0 + UP * 0.3)
        lbat = Tex("12 V").scale(0.8).shift(LEFT * 5.0 + UP * 0.3)
        wt1 = Line(LEFT * 4.0 + UP * 0.9, LEFT * 4.0 + UP * 1.7)
        wt2 = Line(LEFT * 4.0 + UP * 1.7, LEFT * 2.0 + UP * 1.7)
        rs = Rectangle(width=1.4, height=0.6).shift(LEFT * 1.3 + UP * 1.7)
        lrs = MathTex(r"2\ \Omega").scale(0.8).shift(LEFT * 1.3 + UP * 2.35)
        wt3 = Line(LEFT * 0.6 + UP * 1.7, RIGHT * 2.6 + UP * 1.7)
        wj1 = Line(RIGHT * 2.6 + UP * 1.7, RIGHT * 2.6 + UP * 1.1)
        wb1 = Line(RIGHT * 2.6 + UP * 1.1, RIGHT * 1.9 + UP * 1.1)
        wb2 = Line(RIGHT * 2.6 + UP * 1.1, RIGHT * 3.3 + UP * 1.1)
        rp1 = Rectangle(width=0.6, height=1.0).shift(RIGHT * 1.9 + UP * 0.3)
        rp2 = Rectangle(width=0.6, height=1.0).shift(RIGHT * 3.3 + UP * 0.3)
        lrp1 = MathTex(r"6\ \Omega").scale(0.8).shift(RIGHT * 1.0 + UP * 0.3)
        lrp2 = MathTex(r"3\ \Omega").scale(0.8).shift(RIGHT * 4.2 + UP * 0.3)
        wb3 = Line(RIGHT * 1.9 + DOWN * 0.5, RIGHT * 2.6 + DOWN * 0.5)
        wb4 = Line(RIGHT * 3.3 + DOWN * 0.5, RIGHT * 2.6 + DOWN * 0.5)
        wj2 = Line(RIGHT * 2.6 + DOWN * 0.5, RIGHT * 2.6 + DOWN * 1.1)
        wbot = Line(RIGHT * 2.6 + DOWN * 1.1, LEFT * 4.0 + DOWN * 1.1)
        wt4 = Line(LEFT * 4.0 + DOWN * 1.1, LEFT * 4.0 + DOWN * 0.3)
        circuit = VGroup(bat, lbat, wt1, wt2, rs, lrs, wt3, wj1, wb1, wb2,
                         rp1, rp2, lrp1, lrp2, wb3, wb4, wj2, wbot, wt4)
        circuit.shift(band_shift(4))
        self.play(Create(bat), Write(lbat), Create(wt1), Create(wt2))
        self.play(Create(rs), Write(lrs), Create(wt3))
        self.play(Create(wj1), Create(wb1), Create(wb2), Create(rp1), Write(lrp1))
        self.play(Create(rp2), Write(lrp2), Create(wb3), Create(wb4), Create(wj2))
        self.play(Create(wbot), Create(wt4))
        self.wait(2.5)
        b4_l1 = Tex("Collapse it to one resistance first").scale(1.0).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l1))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): collapse and total current ---
        self.next_band(5)
        b5_l1 = MathTex(r"6 \parallel 3: \; \frac{6 \times 3}{6 + 3} = 2\ \Omega").scale(1.05).shift(band_shift(5) + UP * 2.0)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"R_{tot} = 2 + 2 = 4\ \Omega").scale(1.1).shift(band_shift(5) + UP * 0.9)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"I = \frac{V}{R_{tot}} = \frac{12}{4} = 3\ \text{A}").scale(1.1).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex(r"3 A flows through the battery and the 2 $\Omega$").scale(0.95).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_3): voltages and branch currents ---
        self.next_band(6)
        b6_l1 = MathTex(r"V_{series} = 3 \times 2 = 6\ \text{V}").scale(1.05).shift(band_shift(6) + UP * 2.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"V_{parallel} = 12 - 6 = 6\ \text{V both branches}").scale(0.95).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"I_6 = \frac{6}{6} = 1\ \text{A}, \quad I_3 = \frac{6}{3} = 2\ \text{A}").scale(1.0).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = MathTex(r"\text{Checks: } 6 + 6 = 12\ \text{V}, \quad 1 + 2 = 3\ \text{A}").scale(0.95).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Smaller resistance carries the larger current").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l5))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): power, and the audit ---
        self.next_band(7)
        b7_title = Tex("Power: the rate of converting energy").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"P = VI = I^2R = \frac{V^2}{R}").scale(1.15).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=BLUE)))
        self.wait(2.5)
        b7_l2 = MathTex(r"\text{Battery: } 12 \times 3 = 36\ \text{W}").scale(1.0).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"3^2 \times 2 = 18, \;\; \frac{6^2}{6} = 6, \;\; \frac{6^2}{3} = 12").scale(1.0).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = MathTex(r"18 + 6 + 12 = 36\ \text{W — all accounted for}").scale(0.95).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): energy and the bill ---
        self.next_band(8)
        b8_l1 = MathTex(r"W = P\,\Delta t: \; 100 \times 60 = 6\ 000\ \text{J}").scale(0.95).shift(band_shift(8) + UP * 2.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"1\ \text{kWh} = 3{,}6 \times 10^{6}\ \text{J}").scale(1.05).shift(band_shift(8) + UP * 1.0)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"\text{kWh} = \text{kW} \times \text{hours}").scale(1.05).shift(band_shift(8) + UP * 0.0)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=BLUE)))
        self.wait(2.5)
        b8_l4 = Tex(r"Kettle: $2 \times 0{,}5 = 1$ kWh $=$ R2,50").scale(0.95).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex(r"Geyser: 12 kWh/day $\approx$ R900 a month").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex("kWh is ENERGY, not power").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l6))
        self.wait(2.5)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): one road or many roads ---
        self.next_band(9)
        b9_title = Tex("One road or many roads").scale(1.2).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Series: roadblocks on one road — all slower").scale(0.95).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Parallel: side roads — traffic flows easier").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"4\ \Omega \text{ with } 12\ \Omega \text{ beside it: } 3\ \Omega").scale(0.9).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("More roads, easier travel — below the smallest").scale(0.95).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Your home is wired in parallel: full 230 V each").scale(0.95).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_6): the four-move walk ---
        self.next_band(10)
        b10_title = Tex("Shrink, total, spend, split").scale(1.2).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"\text{1. Shrink: } 6 \parallel 3 = 2, \; +2 = 4\ \Omega").scale(0.95).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"\text{2. Total: } \frac{12}{4} = 3\ \text{A}").scale(0.95).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"\text{3. Spend: } 6\ \text{V series}, \; 6\ \text{V left for the pair}").scale(0.9).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = MathTex(r"\text{4. Split: } 1\ \text{A and } 2\ \text{A}, \; 1 + 2 = 3").scale(0.9).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2.5)
        b10_l5 = Tex("The easier road carries more traffic").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (subtopic_7): reading the bill ---
        self.next_band(11)
        b11_title = Tex("Reading the bill like a physicist").scale(1.15).shift(band_shift(11) + UP * 2.3)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex("Municipalities sell kilowatt-hours").scale(0.95).shift(band_shift(11) + UP * 1.3)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = Tex(r"kilowatts $\times$ hours $\times$ tariff").scale(1.05).shift(band_shift(11) + UP * 0.4)
        self.play(Write(b11_l2))
        self.play(Create(SurroundingRectangle(b11_l2, color=GREEN)))
        self.wait(2.5)
        b11_l3 = Tex(r"Geyser: 3 kW $\times$ 4 h $=$ 12 kWh $\approx$ R30/day").scale(0.95).shift(band_shift(11) + DOWN * 0.6)
        self.play(Write(b11_l3))
        self.wait(2.5)
        b11_l4 = Tex("Watts: speed of spending.").scale(0.95).shift(band_shift(11) + DOWN * 1.6)
        b11_l5 = Tex("Kilowatt-hours: total spent").scale(0.95).shift(band_shift(11) + DOWN * 2.3)
        self.play(Write(b11_l4))
        self.play(Write(b11_l5))
        self.wait(2.5)
        b11_l6 = Tex("Attack big powers and long times first").scale(0.95).shift(band_shift(11) + DOWN * 3.1)
        self.play(Write(b11_l6))
        self.wait(4)
