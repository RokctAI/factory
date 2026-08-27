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

# BAND LAYOUT: sequential vertical bands, one frame-height each; the camera
# moves down between teaching steps and nothing is ever removed. Only
# exporter-supported mobjects (Tex/MathTex, Line, Rectangle/
# SurroundingRectangle) with write-only reveals — no sub-part transforms.
# The floor plan and elevation are hand-built from Rectangles and Lines
# (no Arc: the door swing is shown as a straight leaf line).
#
# Mirrors script.md across the seven subtopics of the duo (Part 1 — Expert:
# subtopics 1-4; Part 2 — Simplifier: 5-7); band time proportional to
# subtopics.json.

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


class ScaleFloorElevationPlansSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the number scale ---
        title = Tex("Scale, Floor Plans and Elevation Plans").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Number scale 1 : 50 — same units both sides").scale(1.0).shift(UP * 1.3)
        self.play(Write(l01))
        self.wait(2)
        l02 = MathTex(r"1:50: \; 1 \text{ cm} = 50 \text{ cm} = 0{,}5 \text{ m}").scale(1.05).shift(UP * 0.4)
        l03 = MathTex(r"1:100: \; 1 \text{ cm} = 100 \text{ cm} = 1 \text{ m}").scale(1.05).shift(DOWN * 0.5)
        l04 = MathTex(r"1:500\,000: \; 1 \text{ cm} = 5 \text{ km}").scale(1.05).shift(DOWN * 1.4)
        self.play(Write(l02))
        self.wait(2)
        self.play(Write(l03))
        self.wait(2)
        self.play(Write(l04))
        self.wait(2)
        l05 = Tex("Bigger second number = smaller drawing").scale(0.95).shift(DOWN * 2.4)
        self.play(Write(l05))
        self.wait(3)

        # --- Band 1 (subtopic_1): the bar scale and the photocopier ---
        self.next_band(1)
        b1_t = Tex("The bar scale: a ruler printed on the page").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        bar = Rectangle(width=6.0, height=0.4).shift(band_shift(1) + UP * 1.0)
        self.play(Create(bar))
        for x in (-1.5, 0.0, 1.5):
            tick = Line(UP * 0.2, DOWN * 0.2).shift(band_shift(1) + UP * 1.0 + RIGHT * x)
            self.play(Create(tick), run_time=0.4)
        b1_l1 = Tex("Each 2 cm segment is labelled 1 m — same as 1 : 50").scale(0.9).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Photocopy at 80\\%: the ratio becomes a lie").scale(0.95).shift(band_shift(1) + DOWN * 0.9)
        b1_l3 = Tex("The bar shrinks WITH the page — still true").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): ruler to reality and back ---
        self.next_band(2)
        b2_t = Tex("Page to real: multiply. Real to page: divide.").scale(1.0).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"9{,}0 \text{ cm} \times 50 = 450 \text{ cm} = 4{,}50 \text{ m}").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"6{,}4 \text{ cm} \times 50 = 320 \text{ cm} = 3{,}20 \text{ m}").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        b2_l3 = Tex("Stoep 4,8 m at 1 : 100 onto the page:").scale(0.95).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = MathTex(r"480 \text{ cm} \div 100 = 4{,}8 \text{ cm}").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Convert to one unit FIRST, then apply the ratio").scale(0.9).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the quotation ---
        self.next_band(3)
        b3_t = Tex("From measurements to money").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Floor: } 4{,}50 \times 3{,}20 = 14{,}4 \text{ m}^2").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"\text{Carpet: } 14{,}4 \times 165 = 2\,376{,}00").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = MathTex(r"\text{Skirting: } 15{,}4 - 0{,}9 = 14{,}5 \text{ m} \to 551{,}00").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"\text{Stoep: } 9{,}6 \div 0{,}05 = 192 \to \times 1{,}05 \to 202").scale(0.95).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Materials round UP — always").scale(0.95).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): reading a floor plan ---
        self.next_band(4)
        b4_t = Tex("Reading a floor plan").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        room = Rectangle(width=5.4, height=3.4).shift(band_shift(4) + DOWN * 0.4)
        self.play(Create(room))
        self.wait(1.5)
        door_leaf = Line(ORIGIN, UP * 0.9).shift(band_shift(4) + DOWN * 2.1 + LEFT * 1.6)
        self.play(Create(door_leaf))
        b4_l1 = Tex("Gap + leaf line: a door and its swing").scale(0.85).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        win = Line(LEFT * 0.7, RIGHT * 0.7).shift(band_shift(4) + UP * 1.3 + RIGHT * 1.2)
        self.play(Create(win))
        b4_l2 = Tex("Triple line: a window. Shaded pair: a wall.").scale(0.85).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"4\,500 \text{ on a plan} = 4\,500 \text{ mm} = 4{,}5 \text{ m}").scale(0.95).shift(band_shift(4) + DOWN * 3.3)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): the elevation ---
        self.next_band(5)
        b5_t = Tex("The elevation: straight-on, no perspective").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        wall = Rectangle(width=5.0, height=2.6).shift(band_shift(5) + DOWN * 0.6)
        self.play(Create(wall))
        winr = Rectangle(width=1.5, height=1.0).shift(band_shift(5) + DOWN * 0.4 + RIGHT * 1.0)
        self.play(Create(winr))
        self.wait(1.5)
        b5_l1 = Tex("Wall height 2,6 m; sill at 1,0 m; window 1,0 m tall").scale(0.85).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("Named for the direction the wall FACES").scale(0.9).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("It answers ``how high?'' — the plan answers ``where?''").scale(0.85).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5_l3))
        self.wait(3)

        # --- Band 6 (subtopic_4): combining the two drawings ---
        self.next_band(6)
        b6_t = Tex("Combining the two drawings").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Plan: perimeter } 15{,}4 \text{ m}").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = MathTex(r"\text{Elevation: height } 2{,}6 \text{ m}").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"15{,}4 \times 2{,}6 = 40{,}04 \text{ m}^2").scale(1.05).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"40{,}04 - 1{,}89 - 1{,}5 = 36{,}65 \text{ m}^2").scale(1.05).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex("Neither drawing could do this alone").scale(0.95).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the shrunk house ---
        self.next_band(7)
        b7_t = Tex("The shrunk house").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("1 : 50 = fifty times smaller than real life").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"9{,}0 \times 50 = 450 \text{ cm} = 4{,}50 \text{ m}").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_l3 = MathTex(r"\text{Real to page: } 480 \div 100 = 4{,}8 \text{ cm}").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Photocopiers don't know ratios —").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        b7_l5 = Tex("that is why the little ruler is there").scale(0.95).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): bird's eye vs standing in front ---
        self.next_band(8)
        b8_t = Tex("Bird's eye vs standing in front").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Floor plan: roof off, looking down — WHERE?").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Elevation: square in front — HOW HIGH?").scale(0.95).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Layout and floor space: ask the plan").scale(0.95).shift(band_shift(8) + DOWN * 0.6)
        b8_l4 = Tex("Heights and the roof: ask the elevation").scale(0.95).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = Tex("North elevation = the wall FACING north").scale(0.95).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): the shopping list ---
        self.next_band(9)
        b9_t = Tex("Turning the plan into a shopping list").scale(1.05).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = MathTex(r"\text{Carpet: } 14{,}4 \times 165 = 2\,376{,}00").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"\text{Skirting: } 14{,}5 \times 38 = 551{,}00").scale(0.95).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"\text{Blocks: } 192 \times 1{,}05 = 201{,}6 \to 202").scale(0.95).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"\text{Walls: } 40{,}04 - 1{,}89 - 1{,}5 = 36{,}65 \text{ m}^2").scale(0.95).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("Two sheets of paper + a ruler = a quotation").scale(0.95).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l5))
        self.wait(4)
