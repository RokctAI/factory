# Copyright (c) 2026 RokctAI
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

# Band-layout whiteboard scene for the Assembly Diagrams and Packaging Models
# session duo. One band per teaching beat, camera-only transitions, add-only
# lifecycle, exporter-supported mobjects only (the crate is drawn as a
# Rectangle with a Dot grid — a top view of the can spots). Band time
# apportioned to subtopics.json (220/220/230/260/190/180/180 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AssemblyDiagramsPackagingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the parts list ---
        title = Tex("Assembly Diagrams and Packaging").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_h = Tex("The parts list comes first").scale(1.05).shift(UP * 1.5)
        self.play(Write(b0_h))
        self.wait(1.5)
        plist = Rectangle(width=8.4, height=3.4).shift(DOWN * 0.6)
        self.play(Create(plist))
        b0_r1 = Tex("A \\; side panel \\; $\\times 2$ \\quad B \\; shelf \\; $\\times 4$").scale(0.95).shift(UP * 0.4)
        b0_r2 = Tex("C \\; bracket \\; $\\times 8$ \\quad D \\; screw \\; $\\times 16$").scale(0.95).shift(DOWN * 0.5)
        b0_r3 = Tex("E \\; back board \\; $\\times 1$").scale(0.95).shift(DOWN * 1.4)
        self.play(Write(b0_r1))
        self.wait(2)
        self.play(Write(b0_r2))
        self.wait(2)
        self.play(Write(b0_r3))
        self.wait(2)
        b0_rule = Tex("First instruction: check contents against the list").scale(1.0).shift(DOWN * 2.7)
        self.play(Write(b0_rule))
        self.wait(3)

        # --- Band 1 (subtopic_1): the symbols, translated ---
        self.next_band(1)
        b1_t = Tex("Translating the symbols").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("Numbered circle: a step — follow the order").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("Dotted line: what slides or screws into what").scale(1.0).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex("Arrow: direction — curved means turn to tighten").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = Tex("Magnified circle: zoom into the tricky detail").scale(1.0).shift(band_shift(1) + DOWN * 1.6)
        b1_l5 = Tex("Crossed-out picture: the common MISTAKE").scale(1.0).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): do the quantities interlock? ---
        self.next_band(2)
        b2_t = Tex("Do the quantities interlock?").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"4 \text{ shelves} \times 2 = 8 \text{ brackets} \; \checkmark").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"8 \text{ brackets} \times 2 = 16 \text{ screws} \; \checkmark").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("Only 14 screws in the packet?").scale(1.05).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = MathTex(r"14 \div 2 = 7 \text{ brackets — 1 short of 8}").scale(1.05).shift(band_shift(2) + DOWN * 1.7)
        b2_l5 = MathTex(r"\text{Missing screws: } 16 - 14 = 2").scale(1.05).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): pricing the shortage, catching misprints ---
        self.next_band(3)
        b3_t = Tex("Pricing the shortage").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("Screws sell in packets of 6 at R18").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("2 short $\\Rightarrow$ still buy 1 FULL packet: R18").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("Misprint check: 4 shelves, 8 brackets, 12 screws?").scale(1.0).shift(band_shift(3) + DOWN * 0.9)
        b3_l4 = MathTex(r"8 \times 2 = 16, \text{ so 12 is a misprint for } 16").scale(1.05).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l3))
        self.wait(2.5)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): packing the small crate ---
        self.next_band(4)
        b4_t = Tex("Cans (6 cm wide) in a 30 x 24 x 12 crate").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_t))
        self.wait(1.5)
        crate = Rectangle(width=5.0, height=4.0).shift(band_shift(4) + LEFT * 3.4 + DOWN * 0.6)
        self.play(Create(crate))
        for row in range(4):
            dots = VGroup(*[
                Dot(band_shift(4) + LEFT * 3.4 + DOWN * 0.6
                    + LEFT * 2.0 + RIGHT * 1.0 * col + UP * 1.5 + DOWN * 1.0 * row,
                    radius=0.3, color=BLUE)
                for col in range(5)
            ])
            self.play(Create(dots), run_time=0.6)
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Length: } 30 \div 6 = 5").scale(1.0).shift(band_shift(4) + RIGHT * 3.3 + UP * 1.0)
        b4_l2 = MathTex(r"\text{Width: } 24 \div 6 = 4").scale(1.0).shift(band_shift(4) + RIGHT * 3.3 + UP * 0.1)
        b4_l3 = MathTex(r"\text{Layer: } 5 \times 4 = 20").scale(1.0).shift(band_shift(4) + RIGHT * 3.3 + DOWN * 0.8)
        b4_l4 = MathTex(r"\text{Height: } 12 \div 12 = 1").scale(1.0).shift(band_shift(4) + RIGHT * 3.3 + DOWN * 1.7)
        self.play(Write(b4_l1))
        self.wait(1.5)
        self.play(Write(b4_l2))
        self.wait(1.5)
        self.play(Write(b4_l3))
        self.wait(1.5)
        self.play(Write(b4_l4))
        self.wait(1.5)
        b4_ans = Tex("Capacity: 20 cans").scale(1.05).shift(band_shift(4) + RIGHT * 3.3 + DOWN * 2.7)
        self.play(Write(b4_ans))
        self.play(Create(SurroundingRectangle(b4_ans, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the big crate and the three rules ---
        self.next_band(5)
        b5_t = Tex("The 36 x 30 x 24 crate, and the rules").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"36 \div 6 = 6, \quad 30 \div 6 = 5, \quad 6 \times 5 = 30").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"\text{Height: } 24 \div 12 = 2 \text{ layers} \Rightarrow 60 \text{ cans}").scale(0.84).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_r1 = Tex("Divide dimension by dimension — never volumes").scale(0.95).shift(band_shift(5) + DOWN * 0.8)
        b5_r2 = Tex("Remainders round DOWN: 32 cm still fits only 5").scale(0.95).shift(band_shift(5) + DOWN * 1.7)
        b5_r3 = Tex("Match units first: 60 mm across = 6 cm").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_r1))
        self.wait(2)
        self.play(Write(b5_r2))
        self.wait(2)
        self.play(Write(b5_r3))
        self.wait(3)

        # --- Band 6 (subtopic_4): cost per can ---
        self.next_band(6)
        b6_t = Tex("Which crate is better value?").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Small: } \text{R}4{,}50 \div 20 = 22{,}5 \text{ c per can}").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"\text{Large: } \text{R}9{,}60 \div 60 = 16 \text{ c per can}").scale(1.05).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_ans = Tex("Per can, the large crate wins by 6,5 c").scale(1.05).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_ans))
        self.play(Create(SurroundingRectangle(b6_ans, color=GREEN)))
        self.wait(2)
        b6_l3 = Tex("Across 600 cans a month: R39 saved").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l3))
        self.wait(3)

        # --- Band 7 (subtopic_4): cheapest for the actual job ---
        self.next_band(7)
        b7_t = Tex("But the job is only 25 cans this week").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("One large crate: R9,60 (35 spots wasted)").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{Two small crates: } 2 \times \text{R}4{,}50 = \text{R}9{,}00").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_ans = Tex("For THIS job the small crates win by 60 c").scale(1.05).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_ans))
        self.play(Create(SurroundingRectangle(b7_ans, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex("Capacity down, containers UP, rand vs rand").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        b7_l4 = Tex("Practical factor: weight and rattling space").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the instruction sheet is a recipe ---
        self.next_band(8)
        b8_t = Tex("The instruction sheet is a recipe").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Parts list = ingredients — count them FIRST").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Numbered steps = the method — order matters:").scale(1.0).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("no icing before baking, no back board early").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Exploded view = the dish photographed mid-air").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        b8_l5 = Tex("Crossed-out picture = the burnt version").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l4))
        self.wait(2.5)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): eggs in an egg box ---
        self.next_band(9)
        b9_t = Tex("Eggs in an egg box").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("The crate floor is a grid of spots: 5 by 4 = 20").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("Big crate: 6 by 5 = 30 per floor, 2 floors = 60").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Leftover space is nothing: 32 cm still fits 5").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_ans = Tex("BUYING rounds up; FITTING rounds down").scale(1.05).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_ans))
        self.play(Create(SurroundingRectangle(b9_ans, color=GREEN)))
        b9_l4 = Tex("Never divide volumes — corners are dead air").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): big box, small box, best box ---
        self.next_band(10)
        b10_t = Tex("Big box, small box, best box").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Better PER CAN: 16 c beats 22,5 c — big box").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Better FOR THE JOB of 25 cans:").scale(1.0).shift(band_shift(10) + UP * 0.2)
        b10_l3 = Tex("R9,00 (two small) beats R9,60 (one big)").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_ans = Tex("The bulk deal is only a deal if you use the bulk").scale(1.0).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_ans))
        self.play(Create(SurroundingRectangle(b10_ans, color=GREEN)))
        self.wait(2)
        b10_l4 = Tex("Two different winners, two different questions").scale(1.0).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l4))
        self.wait(4)
