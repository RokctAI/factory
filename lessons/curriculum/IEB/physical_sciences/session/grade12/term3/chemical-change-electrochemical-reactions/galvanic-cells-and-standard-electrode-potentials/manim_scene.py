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

# Band-layout whiteboard scene for "Galvanic Cells and Standard Electrode
# Potentials" (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only; the zinc-copper cell is hand-built from
# Rectangles (electrodes), Lines (beakers, wire, salt bridge) and Tex labels.
# Subtopic durations 235/240/240/235/190/195/195 of 1530 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class GalvanicCellsPotentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): redox bookkeeping ---
        title = Tex("Galvanic Cells and Electrode Potentials").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("OIL RIG: Oxidation Is Loss, Reduction Is Gain").scale(0.95).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=GREEN)))
        self.wait(2.5)
        b0_l2 = Tex("Oxidising agent: takes electrons, is itself reduced").scale(0.9).shift(UP * 0.3)
        b0_l3 = Tex("Reducing agent: gives electrons, is itself oxidised").scale(0.9).shift(DOWN * 0.5)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex("Anode: where oxidation occurs").scale(0.95).shift(DOWN * 1.5)
        b0_l5 = Tex("Cathode: where reduction occurs").scale(0.95).shift(DOWN * 2.3)
        b0_l6 = Tex("Electrolyte: conducts by moving ions").scale(0.95).shift(DOWN * 3.1)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_2): the zinc-copper cell, drawn ---
        self.next_band(1)
        b1_title = Tex("The zinc-copper cell").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        c1 = band_shift(1) + DOWN * 0.6
        # Two beakers as open-top outlines.
        beak_l = VGroup(
            Line(c1 + LEFT * 4.4 + UP * 0.8, c1 + LEFT * 4.4 + DOWN * 1.2),
            Line(c1 + LEFT * 4.4 + DOWN * 1.2, c1 + LEFT * 1.6 + DOWN * 1.2),
            Line(c1 + LEFT * 1.6 + DOWN * 1.2, c1 + LEFT * 1.6 + UP * 0.8),
        )
        beak_r = VGroup(
            Line(c1 + RIGHT * 1.6 + UP * 0.8, c1 + RIGHT * 1.6 + DOWN * 1.2),
            Line(c1 + RIGHT * 1.6 + DOWN * 1.2, c1 + RIGHT * 4.4 + DOWN * 1.2),
            Line(c1 + RIGHT * 4.4 + DOWN * 1.2, c1 + RIGHT * 4.4 + UP * 0.8),
        )
        self.play(Create(beak_l), Create(beak_r))
        el_zn = Rectangle(width=0.25, height=1.6).move_to(c1 + LEFT * 3.6 + UP * 0.4)
        el_cu = Rectangle(width=0.25, height=1.6).move_to(c1 + RIGHT * 3.6 + UP * 0.4)
        self.play(Create(el_zn), Create(el_cu))
        lab_zn = Tex("Zn anode $-$").scale(0.75).shift(c1 + LEFT * 3.6 + DOWN * 1.6)
        lab_cu = Tex("Cu cathode $+$").scale(0.75).shift(c1 + RIGHT * 3.6 + DOWN * 1.6)
        self.play(Write(lab_zn), Write(lab_cu))
        # External wire with voltmeter.
        wire = VGroup(
            Line(c1 + LEFT * 3.6 + UP * 1.2, c1 + LEFT * 3.6 + UP * 2.0),
            Line(c1 + LEFT * 3.6 + UP * 2.0, c1 + RIGHT * 3.6 + UP * 2.0),
            Line(c1 + RIGHT * 3.6 + UP * 2.0, c1 + RIGHT * 3.6 + UP * 1.2),
        )
        volt = Circle(radius=0.35).move_to(c1 + UP * 2.0)
        lab_v = Tex("V").scale(0.7).move_to(c1 + UP * 2.0)
        self.play(Create(wire))
        self.play(Create(volt), Write(lab_v))
        # Salt bridge between the beakers.
        bridge = VGroup(
            Line(c1 + LEFT * 2.4 + UP * 0.2, c1 + LEFT * 2.4 + UP * 1.1),
            Line(c1 + LEFT * 2.4 + UP * 1.1, c1 + RIGHT * 2.4 + UP * 1.1),
            Line(c1 + RIGHT * 2.4 + UP * 1.1, c1 + RIGHT * 2.4 + UP * 0.2),
        )
        lab_sb = Tex("salt bridge").scale(0.7).shift(c1 + UP * 1.45)
        self.play(Create(bridge), Write(lab_sb))
        self.wait(2)
        lab_e = Tex("electrons: Zn $\\rightarrow$ Cu").scale(0.75).shift(c1 + UP * 2.6)
        self.play(Write(lab_e))
        self.wait(3)

        # --- Band 2 (subtopic_2): running the cell ---
        self.next_band(2)
        b2_title = Tex("Run the cell: what you observe").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{anode: } Zn \rightarrow Zn^{2+} + 2e^-").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{cathode: } Cu^{2+} + 2e^- \rightarrow Cu").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("Zn strip loses mass; Cu strip gains mass").scale(0.95).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = Tex("Blue $CuSO_4$ colour fades").scale(0.95).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = Tex("Bridge: completes circuit AND").scale(0.95).shift(band_shift(2) + DOWN * 2.5)
        b2_l6 = Tex("keeps both half-cells neutral").scale(0.95).shift(band_shift(2) + DOWN * 3.3)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): the table and its anchor ---
        self.next_band(3)
        b3_title = Tex("Standard electrode potentials").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Standard: 1 mol$\\cdot$dm$^{-3}$, 25$^\\circ$C, standard pressure").scale(0.85).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("Anchor: standard hydrogen electrode $= 0$ V").scale(0.95).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = MathTex(r"Cu^{2+}/Cu: +0,34\ \text{V} \quad Zn^{2+}/Zn: -0,76\ \text{V}").scale(0.9).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex("More positive: stronger oxidising agent (left)").scale(0.9).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = Tex("More negative: stronger reducing agent (right)").scale(0.9).shift(band_shift(3) + DOWN * 2.5)
        b3_l6 = Tex("Higher potential takes the cathode").scale(0.95).shift(band_shift(3) + DOWN * 3.3)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(2)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_4): cell notation + the emf calculation ---
        self.next_band(4)
        b4_title = Tex("Cell notation and emf").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"Zn(s)\,|\,Zn^{2+}(aq)\,||\,Cu^{2+}(aq)\,|\,Cu(s)").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex("Anode left, cathode right, $||$ = salt bridge").scale(0.9).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode}").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = MathTex(r"E^\circ_{cell} = 0,34 - (-0,76) = 1,10\ \text{V}").scale(1.0).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex("Brackets on the negative, every time").scale(0.9).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): Al-Ag and the flat battery ---
        self.next_band(5)
        b5_title = Tex("Second example: aluminium-silver").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"Al: -1,66\ \text{V} \quad Ag: +0,80\ \text{V}").scale(0.95).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("Silver higher: silver is the cathode").scale(0.95).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"E^\circ_{cell} = 0,80 - (-1,66) = 2,46\ \text{V}").scale(1.0).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex("Positive emf $=$ spontaneous as labelled").scale(0.95).shift(band_shift(5) + DOWN * 1.7)
        b5_l5 = Tex("Negative answer? Swap anode and cathode").scale(0.95).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.wait(2)
        b5_l6 = Tex("Flat battery: equilibrium, emf $= 0$").scale(0.95).shift(band_shift(5) + DOWN * 3.3)
        self.play(Write(b5_l6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): chemistry that pays in electricity ---
        self.next_band(6)
        b6_title = Tex("Chemistry that pays in electricity").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Zinc in blue solution: trade happens on the spot,").scale(0.9).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("energy wasted as heat").scale(0.95).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Separate the beakers: electrons must").scale(0.95).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = Tex("commute through YOUR wire $=$ current").scale(0.95).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2.5)
        b6_l5 = Tex("Voltage $=$ how badly both sides want the trade").scale(0.9).shift(band_shift(6) + DOWN * 2.4)
        b6_l6 = Tex("Flat $=$ transaction complete, not leaked").scale(0.9).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(b6_l5))
        self.wait(2)
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_6): the bridge that keeps the peace ---
        self.next_band(7)
        b7_title = Tex("The bridge that keeps the peace").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Left beaker gains $+$ charge, right loses it —").scale(0.9).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("imbalance would stall the cell in moments").scale(0.9).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Bridge $=$ corridor for IONS, not electrons").scale(0.95).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("Two-storey circuit: electrons upstairs in the wire,").scale(0.85).shift(band_shift(7) + DOWN * 1.5)
        b7_l5 = Tex("ions downstairs through solution and bridge").scale(0.85).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(2.5)
        b7_l6 = Tex("Lift the bridge: voltmeter drops to zero instantly").scale(0.85).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7_l6))
        self.wait(3)

        # --- Band 8 (subtopic_7): the league table ---
        self.next_band(8)
        b8_title = Tex("The league table of electron grabbers").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Top (big $+$): fierce grabbers — fluorine champion").scale(0.85).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Bottom (big $-$): soft touches — lithium, potassium").scale(0.85).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Higher rank grabs; lower rank surrenders").scale(0.95).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = MathTex(r"\text{Cu vs Zn: gap} = 1,10\ \text{V}").scale(0.95).shift(band_shift(8) + DOWN * 1.5)
        b8_l5 = MathTex(r"\text{Ag vs Al: gap} = 2,46\ \text{V}").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex("The gap IS the voltage on the label").scale(0.95).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l6))
        self.wait(4)
