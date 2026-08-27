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

# Band-layout whiteboard scene for "Reaction Rate and Collision Theory"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only; graphs hand-built from Line/Dot/Tex.
# Write-only reveals.
# Subtopic durations 235/240/240/240/195/195/195 of 1540 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ReactionRateCollisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): definition + rate calculation ---
        title = Tex("Reaction Rate and Collision Theory").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_eq = MathTex(r"\text{rate} = \frac{\Delta n}{\Delta t} \;\; [\text{mol·s}^{-1}]").scale(1.1).shift(UP * 1.0)
        self.play(Write(b0_eq))
        self.play(Create(SurroundingRectangle(b0_eq, color=GREEN)))
        self.wait(2.5)
        b0_l1 = Tex("flask loses 3,3 g CO$_2$ in 60 s").scale(0.95).shift(UP * 0.0)
        b0_l2 = MathTex(r"n = 3{,}3 \div 44 = 0{,}075\ \text{mol}").scale(0.95).shift(DOWN * 0.9)
        b0_l3 = MathTex(r"\text{rate} = 0{,}075 \div 60 = 0{,}00125\ \text{mol·s}^{-1}").scale(0.95).shift(DOWN * 1.8)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2)
        b0_l4 = Tex("rate: how fast. extent: how much. Keep them apart.").scale(0.9).shift(DOWN * 2.8)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_2): collision theory, first factors ---
        self.next_band(1)
        b1_title = Tex("Effective collisions only").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = Tex("1. correct orientation").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("2. energy $\\geq$ activation energy").scale(1.0).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("nature: calcium beats magnesium in water").scale(0.9).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = Tex("surface: steel wool burns; the nail glows").scale(0.9).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_rule = Tex("rate $=$ effective collisions per second").scale(0.95).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_rule))
        self.play(Create(SurroundingRectangle(b1_rule, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): concentration, temperature, catalyst ---
        self.next_band(2)
        b2_title = Tex("The remaining levers").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex("concentration / pressure: more particles, more collisions").scale(0.85).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = Tex("temperature: bigger FRACTION beats $E_a$").scale(0.95).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex("catalyst: faster, and NOT consumed").scale(0.95).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_wrong = Tex("Temperature only adds more collisions").scale(0.9).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l4 = Tex("it upgrades each collision's chance of success").scale(0.9).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_3): measurement techniques ---
        self.next_band(3)
        b3_title = Tex("Measuring rate: log something against time").scale(1.0).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = Tex("gas volume — syringe").scale(0.95).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("mass loss — open flask on a balance").scale(0.95).shift(band_shift(3) + UP * 0.3)
        b3_l3 = Tex("turbidity — the vanishing cross").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = Tex("colour change — eye or instrument").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l1))
        self.wait(1.5)
        self.play(Write(b3_l2))
        self.wait(1.5)
        self.play(Write(b3_l3))
        self.wait(1.5)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_rule = Tex("cross vanishes sooner $=$ faster: think one over time").scale(0.9).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_rule))
        self.play(Create(SurroundingRectangle(b3_rule, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): powder vs ribbon, same plateau ---
        self.next_band(4)
        b4_title = Tex("Powder vs ribbon: same magnesium, same acid").scale(0.95).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        # Axes
        o4 = band_shift(4) + LEFT * 4.5 + DOWN * 2.2
        ax_x = Line(o4, o4 + RIGHT * 7.5)
        ax_y = Line(o4, o4 + UP * 4.0)
        self.play(Create(ax_x), Create(ax_y))
        lab_x = Tex("time").scale(0.7).shift(o4 + RIGHT * 7.6 + DOWN * 0.4)
        lab_y = Tex("V(H$_2$)").scale(0.7).shift(o4 + UP * 4.2 + LEFT * 0.5)
        self.play(Write(lab_x), Write(lab_y))
        # Powder curve: steep then flat (polyline)
        p1 = Line(o4, o4 + RIGHT * 1.2 + UP * 2.6, color=GREEN)
        p2 = Line(o4 + RIGHT * 1.2 + UP * 2.6, o4 + RIGHT * 2.4 + UP * 3.2, color=GREEN)
        p3 = Line(o4 + RIGHT * 2.4 + UP * 3.2, o4 + RIGHT * 7.0 + UP * 3.2, color=GREEN)
        # Ribbon curve: gentle then same plateau
        r1 = Line(o4, o4 + RIGHT * 2.8 + UP * 1.6, color=BLUE)
        r2 = Line(o4 + RIGHT * 2.8 + UP * 1.6, o4 + RIGHT * 5.2 + UP * 3.0, color=BLUE)
        r3 = Line(o4 + RIGHT * 5.2 + UP * 3.0, o4 + RIGHT * 7.0 + UP * 3.2, color=BLUE)
        self.play(Create(p1), Create(p2), Create(p3))
        self.wait(2)
        self.play(Create(r1), Create(r2), Create(r3))
        self.wait(2)
        b4_l1 = Tex("steeper start, SAME finish").scale(0.9).shift(band_shift(4) + RIGHT * 3.2 + UP * 1.6)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): energy distribution + temperature ---
        self.next_band(5)
        b5_title = Tex("Molecular energy distribution").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        o5 = band_shift(5) + LEFT * 4.5 + DOWN * 2.0
        ax5x = Line(o5, o5 + RIGHT * 7.5)
        ax5y = Line(o5, o5 + UP * 3.6)
        self.play(Create(ax5x), Create(ax5y))
        # Hump drawn as a polyline
        h1 = Line(o5, o5 + RIGHT * 1.5 + UP * 2.6, color=BLUE)
        h2 = Line(o5 + RIGHT * 1.5 + UP * 2.6, o5 + RIGHT * 3.5 + UP * 1.0, color=BLUE)
        h3 = Line(o5 + RIGHT * 3.5 + UP * 1.0, o5 + RIGHT * 7.0 + UP * 0.2, color=BLUE)
        self.play(Create(h1), Create(h2), Create(h3))
        ea = Line(o5 + RIGHT * 4.6, o5 + RIGHT * 4.6 + UP * 3.2, color=RED)
        ea_lab = Tex("$E_a$").scale(0.8).shift(o5 + RIGHT * 4.6 + UP * 3.5)
        self.play(Create(ea), Write(ea_lab))
        self.wait(2)
        b5_l1 = Tex("only the tail RIGHT of $E_a$ can react").scale(0.9).shift(band_shift(5) + RIGHT * 2.4 + UP * 1.4)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex("heat: curve shifts right, flattens — tail swells").scale(0.85).shift(band_shift(5) + RIGHT * 2.4 + UP * 0.5)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): catalyst on the PE diagram ---
        self.next_band(6)
        b6_title = Tex("The catalyst moves the LINE, not the curve").scale(1.0).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("alternative pathway, lower $E_a$").scale(0.95).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = Tex("more of the SAME particles clear the new bar").scale(0.9).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_wrong = Tex("A catalyst changes $\\Delta H$").scale(0.95).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        self.wait(2)
        b6_l3 = Tex("hump lower; start, end and $\\Delta H$ untouched").scale(0.9).shift(band_shift(6) + DOWN * 1.7)
        b6_l4 = Tex("and the catalyst is never consumed").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): how fast is not how far ---
        self.next_band(7)
        b7_title = Tex("How fast is not how far").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("crushed tablet, warm water: gone in seconds").scale(0.9).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("whole tablet, cold water: minutes of lazy fizz").scale(0.9).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("same TOTAL gas from both glasses").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("rate differed; extent identical").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (subtopic_6): bumper cars ---
        self.next_band(8)
        b8_title = Tex("Bumper cars: only hard hits count").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("more cars $=$ concentration").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("break the big car up $=$ surface area").scale(0.95).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("power the motors $=$ temperature").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("catalyst: lowers the BAR, holds the gate open all night").scale(0.85).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_rule = Tex("every answer: more counting bumps per second").scale(0.9).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_rule))
        self.play(Create(SurroundingRectangle(b8_rule, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): reading the story off the graph ---
        self.next_band(9)
        b9_title = Tex("Steepness, bend, plateau").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("steepness $=$ speed").scale(0.95).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("bend $=$ tiring, reactants running out").scale(0.95).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("plateau height $=$ extent, the finish line").scale(0.95).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_wrong = Tex("Faster means more product").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_wrong))
        self.play(Create(strike(b9_wrong)))
        self.wait(2)
        b9_l4 = Tex("sprint, tire, stop — same shelf for same amounts").scale(0.9).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4))
        self.wait(4)
