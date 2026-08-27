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

# Band layout: one frame-height band per teaching beat; the camera moves down,
# nothing is removed. Exporter-supported mobjects only (Tex/MathTex/Line/
# Rectangle/SurroundingRectangle); single-string Write reveals throughout.
#
# Covers all seven subtopics (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# band time roughly proportional to subtopics.json
# (215/220/225/230/195/195/195 of 1475 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ScalesAndStreetMapsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the number scale ---
        title = Tex("Scales and Street Maps").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l1 = MathTex(r"1 : 50\,000 \;\; \text{— 1 cm on paper} = 50\,000\text{ cm real}").scale(0.97).shift(UP * 1.1)
        self.play(Write(l1)); self.wait(2.5)
        l2 = Tex("Measure, multiply, convert — in that order").scale(1.05).shift(UP * 0.2)
        self.play(Write(l2))
        self.play(Create(SurroundingRectangle(l2, color=GREEN)))
        self.wait(2.5)
        l3 = MathTex(r"7 \times 50\,000 = 350\,000\text{ cm}").scale(1.05).shift(DOWN * 0.8)
        l4 = MathTex(r"\div 100 = 3\,500\text{ m}; \quad \div 1\,000 = 3{,}5\text{ km}").scale(1.02).shift(DOWN * 1.7)
        self.play(Write(l3)); self.wait(2)
        self.play(Write(l4)); self.wait(2.5)

        # --- Band 1 (subtopic_1): the reverse, and the sense test ---
        self.next_band(1)
        b1_title = Tex("The calculation reverses cleanly").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"9\text{ km} = 900\,000\text{ cm}").scale(1.1).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"900\,000 \div 50\,000 = 18\text{ cm of paper}").scale(1.1).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1)); self.wait(2.5)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("Map to ground GROWS; ground to map SHRINKS").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = Tex(r"Anchor: 100\,000 cm in a kilometre").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l3)); self.wait(2.5)
        self.play(Write(b1_l4)); self.wait(2.5)

        # --- Band 2 (subtopic_2): the bar scale ---
        self.next_band(2)
        b2_title = Tex("The bar scale: 2 cm stands for 10 km").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        bar = Rectangle(width=6.0, height=0.5).shift(band_shift(2) + UP * 1.2)
        seg1 = Line(band_shift(2) + UP * 1.45 + LEFT * 1.0, band_shift(2) + UP * 0.95 + LEFT * 1.0)
        seg2 = Line(band_shift(2) + UP * 1.45 + RIGHT * 1.0, band_shift(2) + UP * 0.95 + RIGHT * 1.0)
        self.play(Create(bar))
        self.play(Create(seg1), Create(seg2))
        bar_lab = Tex(r"0 \qquad\quad 10 km \qquad\quad 20 km \qquad\quad 30 km").scale(0.8).shift(band_shift(2) + UP * 0.5)
        self.play(Write(bar_lab))
        self.wait(2)
        b2_l1 = MathTex(r"\text{Every centimetre} = 5\text{ km}").scale(1.05).shift(band_shift(2) + DOWN * 0.4)
        b2_l2 = MathTex(r"9\text{ cm route: } 9 \times 5 = 45\text{ km}").scale(1.1).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l1)); self.wait(2.5)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex("No ruler? Tick the route on paper, step it along the bar").scale(0.9).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l3)); self.wait(2.5)

        # --- Band 3 (subtopic_2): the photocopier problem ---
        self.next_band(3)
        b3_title = Tex("Why maps carry a bar at all").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Photocopy at 80\%: every road shrinks").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex(r"The printed 1 : 50\,000 is now a lie").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1)); self.wait(2.5)
        self.play(Write(b3_l2)); self.wait(2.5)
        b3_l3 = Tex("The bar shrinks WITH the roads — it stays true").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Number scale: exact but fragile. Bar: rough but robust.").scale(0.95).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4)); self.wait(2.5)

        # --- Band 4 (subtopic_3): grids and directions ---
        self.next_band(4)
        b4_title = Tex("Finding the place: grid B3").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Column B crosses row 3 — the block, not the doorstep").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1)); self.wait(2.5)
        b4_l2 = Tex("Compass words are fixed: north top, east right").scale(0.95).shift(band_shift(4) + UP * 0.2)
        b4_l3 = Tex(r"``Up and to the right'' earns nothing — say north-east").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l2)); self.wait(2.5)
        self.play(Write(b4_l3)); self.wait(2.5)
        b4_l4 = Tex("Route words travel with you: left, right, straight").scale(0.95).shift(band_shift(4) + DOWN * 1.6)
        b4_l5 = Tex("Heading south, west is on your RIGHT — orient first!").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l4)); self.wait(2.5)
        self.play(Write(b4_l5)); self.wait(2.5)

        # --- Band 5 (subtopic_4): distance, time ---
        self.next_band(5)
        b5_title = Tex("From the map to the clock").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"12 \times 150\,000 = 1\,800\,000\text{ cm} = 18\text{ km}").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1)); self.wait(2.5)
        b5_l2 = MathTex(r"\text{Time} = 18 \div 60 = 0{,}3\text{ h}").scale(1.1).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2)); self.wait(2)
        b5_wrong = Tex(r"0,3 hours $=$ 30 minutes").scale(1.0).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l3 = MathTex(r"0{,}3 \times 60 = 18\text{ minutes}").scale(1.1).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): fuel, rands and the comparison ---
        self.next_band(6)
        b6_title = Tex("Fuel, rands, and who should drive").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"18 \div 100 \times 8 = 1{,}44\ \ell").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"1{,}44 \times 23{,}50 = R33{,}84; \;\; \text{return } R67{,}68").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1)); self.wait(2.5)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex(r"Taxi: R52 return each; four people pay R208").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        b6_l4 = Tex(r"``For four travellers the car is cheaper by R140,32''").scale(0.95).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l3)); self.wait(2.5)
        self.play(Write(b6_l4)); self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the shrinking machine ---
        self.next_band(7)
        b7_title = Tex("The world through a shrinking machine").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2.5)
        b7_l1 = Tex(r"Everything got 50\,000 times smaller — evenly").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1)); self.wait(3)
        b7_l2 = MathTex(r"7\text{ cm} \to 350\,000\text{ cm} \to 3\,500\text{ m} \to 3{,}5\text{ km}").scale(0.91).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(3)
        b7_l3 = Tex(r"Back again: 9 km $= 900\,000$ cm $\div$ 50\,000 $=$ 18 cm").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3)); self.wait(3)
        b7_l4 = Tex("Clinic 70 km away? You divided the wrong way — fix it").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4)); self.wait(3.5)

        # --- Band 8 (subtopic_6): the honest little bar ---
        self.next_band(8)
        b8_title = Tex("The bar that survives the photocopier").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = Tex(r"One stripe: 10 km, and it measures 2 cm — so 5 km per cm").scale(0.9).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1)); self.wait(3)
        b8_l2 = MathTex(r"9 \times 5 = 45\text{ km to the turn-off}").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(3)
        b8_l3 = Tex("Shrink the map: the ratio lies, the bar shrinks along").scale(0.95).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3)); self.wait(3)
        b8_l4 = Tex("Its weakness is your eyesight — exact vs robust, say both").scale(0.9).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4)); self.wait(3.5)

        # --- Band 9 (subtopic_7): blocks, turns and petrol money ---
        self.next_band(9)
        b9_title = Tex("Block, turns, kilometres, minutes, rands").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = Tex(r"North up Market, right into Grobler, clinic on the left").scale(0.9).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1)); self.wait(3)
        b9_l2 = MathTex(r"18\text{ km at }60\text{ km/h} = 0{,}3\text{ h} = 18\text{ min}").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2)); self.wait(3)
        b9_l3 = MathTex(r"1{,}44\ \ell \times 23{,}50 = R33{,}84; \;\; \text{return } R67{,}68").scale(0.95).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3)); self.wait(3)
        b9_l4 = Tex(r"Four in the car: about R17 each against the taxi's R52").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(4)
