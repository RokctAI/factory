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

# Band-layout whiteboard scene for the Assembling with Instructions session duo.
# Part 1 — Expert: subtopics 1-4 (diagram language, parts list audit, sequence,
# DIY cost decision). Part 2 — Simplifier: subtopics 5-7 re-teach with the
# lounge-floor framing. Durations 215/225/225/225/195/195/200 of 1480 s.
# Exporter-safe mobjects only; add-only lifecycle; camera moves between bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AssemblingWithInstructionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(15)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the language of instruction diagrams ---
        title = Tex("Assembling with Instructions").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Exploded diagram: parts burst apart at joints").scale(1.05).shift(UP * 1.1)
        b0_l2 = Tex("Step numbers dictate the SEQUENCE").scale(1.1).shift(UP * 0.2)
        b0_l3 = Tex("Arrows are verbs: slide, rotate, press home").scale(1.05).shift(DOWN * 0.7)
        b0_l4 = Tex("Crossed-out mallet: never force a part").scale(1.1).shift(DOWN * 1.6)
        self.play(Write(b0_l1)); self.wait(2)
        self.play(Write(b0_l2)); self.wait(2)
        self.play(Write(b0_l3)); self.wait(2)
        self.play(Write(b0_l4)); self.wait(3)

        # --- Band 1 (subtopic_1): orientation symbols and the two readings ---
        self.next_band(1)
        b1_title = Tex("Orientation marks carry the weight").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("L and R panels are mirror-drilled twins").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("Swap them: peg holes face the room").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex("Tick and cross: right and wrong, side by side").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = Tex("Read twice: once fully, then step by step").scale(1.05).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2.5)
        self.play(Write(b1_l3)); self.wait(2)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the parts list as a document ---
        self.next_band(2)
        b2_title = Tex("The parts list: the kit's register").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        # Recreate the parts list as a bordered table (rect + rows of Tex)
        table = Rectangle(width=8.0, height=3.6).shift(band_shift(2) + DOWN * 0.4)
        self.play(Create(table))
        row1 = Tex("A \\; side panels \\; 2 \\quad B \\; doors \\; 2").scale(0.95).shift(band_shift(2) + UP * 0.8)
        row2 = Tex("C \\; shelves \\; 3 \\quad D \\; back panel \\; 1").scale(0.95).shift(band_shift(2) + UP * 0.0)
        row3 = Tex("cam locks \\; 12 \\quad cam bolts \\; 12 \\quad dowels \\; 10").scale(0.9).shift(band_shift(2) + DOWN * 0.8)
        row4 = Tex("hinges \\; 4 \\quad screws \\; 20 \\quad Allen key \\; 1").scale(0.9).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(row1)); self.wait(1.5)
        self.play(Write(row2)); self.wait(1.5)
        self.play(Write(row3)); self.wait(1.5)
        self.play(Write(row4)); self.wait(2)
        b2_note = Tex("Audit the count BEFORE building").scale(1.05).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_note))
        self.wait(3)

        # --- Band 3 (subtopic_2): the shortage sums ---
        self.next_band(3)
        b3_title = Tex("Counting with a sting").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"12 - 9 = 3 \text{ cam locks missing}").scale(1.1).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("Each shelf needs 4: only 2 shelves can lock").scale(1.05).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"25 \times 18 = 450 \text{ screws needed}").scale(1.1).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = MathTex(r"450 \div 40 = 11,25 \to 12 \text{ boxes}").scale(1.1).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l1)); self.wait(2.5)
        self.play(Write(b3_l2)); self.wait(2.5)
        self.play(Write(b3_l3)); self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the one-way sequence ---
        self.next_band(4)
        b4_title = Tex("Order matters: assembly runs one way").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Dowels $\\to$ cam bolts $\\to$ shelves on one side").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex("Second panel $\\to$ square $\\to$ back $\\to$ doors $\\to$ stand").scale(0.95).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1)); self.wait(2)
        self.play(Write(b4_l2)); self.wait(2.5)
        b4_wrong = Tex("Nail the back panel first?").scale(1.05).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(2)
        b4_l3 = Tex("The back seals the face the shelves enter through").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        b4_l4 = Tex("Undo wrong steps in REVERSE order").scale(1.05).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l3)); self.wait(2.5)
        self.play(Write(b4_l4)); self.wait(3)

        # --- Band 5 (subtopic_3): wiring the plug — colours are regulation ---
        self.next_band(5)
        b5_title = Tex("The three-pin plug: colours are regulation").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        # Plug diagram: body + three labelled terminals
        plug = Rectangle(width=3.4, height=2.8).shift(band_shift(5) + LEFT * 3.6 + DOWN * 0.5)
        self.play(Create(plug))
        earth = Dot(plug.get_top() + DOWN * 0.6, color=GREEN)
        live = Dot(plug.get_bottom() + UP * 0.7 + RIGHT * 1.0, color=RED)
        neut = Dot(plug.get_bottom() + UP * 0.7 + LEFT * 1.0, color=BLUE)
        e_lab = Tex("E").scale(0.9).next_to(earth, UP, buff=0.12)
        l_lab = Tex("L").scale(0.9).next_to(live, DOWN, buff=0.12)
        n_lab = Tex("N").scale(0.9).next_to(neut, DOWN, buff=0.12)
        self.play(Create(earth), Write(e_lab))
        self.play(Create(live), Write(l_lab))
        self.play(Create(neut), Write(n_lab))
        self.wait(2)
        b5_l1 = Tex("BROWN $\\to$ LIVE (right)").scale(1.0).shift(band_shift(5) + RIGHT * 2.9 + UP * 1.0)
        b5_l2 = Tex("BLUE $\\to$ NEUTRAL (left)").scale(1.0).shift(band_shift(5) + RIGHT * 2.9 + UP * 0.1)
        b5_l3 = Tex("GREEN-YELLOW $\\to$ EARTH (top)").scale(0.95).shift(band_shift(5) + RIGHT * 2.9 + DOWN * 0.8)
        self.play(Write(b5_l1)); self.wait(1.5)
        self.play(Write(b5_l2)); self.wait(1.5)
        self.play(Write(b5_l3)); self.wait(2)
        b5_l4 = Tex("Grip clamps the SHEATH, never the cores").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        b5_l5 = Tex("Swapped brown-blue still heats — but stays live").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l4)); self.wait(2)
        self.play(Write(b5_l5)); self.wait(3)

        # --- Band 6 (subtopic_4): the three-option cost table ---
        self.next_band(6)
        b6_title = Tex("The do-it-yourself decision, in rands").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Self: } 2\;499 + 300 = \text{R2 799}").scale(1.1).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"\text{Warehouse: } 2\;499 + 300 + 450 = \text{R3 249}").scale(1.05).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"\text{Handyman: } 2\;499 + 300 + 3 \times 180 = \text{R3 339}").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        b6_l4 = Tex("Self-assembly saves R450 / R540").scale(1.1).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l1)); self.wait(2)
        self.play(Write(b6_l2)); self.wait(2)
        self.play(Write(b6_l3)); self.wait(2.5)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): risk and percentages ---
        self.next_band(7)
        b7_title = Tex("Price the risk, then the percentages").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Step 8 needs four hands — a split door costs R520").scale(0.95).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"450 \div 2\;499 \times 100 = 18,0\%").scale(1.1).shift(band_shift(7) + UP * 0.1)
        b7_l3 = MathTex(r"2\;499 + 550 = 3\;049 > 3\;000 \text{ (free fit)}").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        b7_l4 = MathTex(r"\text{Lamp really costs } 550 - 450 = \text{R}100").scale(1.05).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l1)); self.wait(2.5)
        self.play(Write(b7_l2)); self.wait(2.5)
        self.play(Write(b7_l3)); self.wait(2.5)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): pictures that give orders ---
        self.next_band(8)
        b8_title = Tex("Pictures that give orders").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = Tex("Exploded view: parts hang where they live").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Numbers order, circles zoom, arrows move").scale(1.05).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("L and R are twins with mirrored holes").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = Tex("Read the whole sheet before touching a part").scale(1.05).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l1)); self.wait(3)
        self.play(Write(b8_l2)); self.wait(3)
        self.play(Write(b8_l3)); self.wait(3)
        self.play(Write(b8_l4)); self.wait(3.5)

        # --- Band 9 (subtopic_6): roll call before building ---
        self.next_band(9)
        b9_title = Tex("Count everything before you build anything").scale(1.05).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = Tex("Roll call: tick every part on the list").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"12 - 9 = 3 \text{ missing} \Rightarrow 2 \text{ shelves lock}").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_l3 = MathTex(r"25 \times 18 = 450; \;\; 450 \div 40 = 11,25 \to 12").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = Tex("Eleven boxes arrive ten screws short").scale(1.05).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l1)); self.wait(3)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(3)
        self.play(Write(b9_l3)); self.wait(3)
        self.play(Write(b9_l4)); self.wait(3.5)

        # --- Band 10 (subtopic_7): shortcuts and the plug ---
        self.next_band(10)
        b10_title = Tex("The shortcut is the longest road in the box").scale(1.05).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = Tex("The thin back sheet keeps the corners square").scale(1.05).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("Wrong-order moves get undone in reverse").scale(1.05).shift(band_shift(10) + UP * 0.2)
        b10_l3 = Tex("Brown right, blue left, green-yellow top").scale(1.05).shift(band_shift(10) + DOWN * 0.8)
        b10_l4 = Tex("Swapped wires still heat — check, never assume").scale(1.0).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l1)); self.wait(3)
        self.play(Write(b10_l2)); self.wait(3)
        self.play(Write(b10_l3)); self.wait(3)
        self.play(Write(b10_l4)); self.wait(3.5)

        # --- Band 11 (subtopic_7): the decision in rands ---
        self.next_band(11)
        b11_title = Tex("Defend the choice in rands").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2.5)
        b11_l1 = MathTex(r"\text{Self R2 799, warehouse R3 249, handyman R3 339}").scale(0.95).shift(band_shift(11) + UP * 1.1)
        b11_l2 = Tex("Saving R450 or more — if four hands show up").scale(1.05).shift(band_shift(11) + UP * 0.1)
        b11_l3 = Tex("A split door at R520 eats the saving").scale(1.05).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11_l1))
        self.play(Create(SurroundingRectangle(b11_l1, color=GREEN)))
        self.wait(3.5)
        self.play(Write(b11_l2)); self.wait(3.5)
        self.play(Write(b11_l3)); self.wait(4)
