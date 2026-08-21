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

# Band-layout whiteboard scene for the IEB Grade 12 Geography session duo
# "Industry Types and Location Factors". Bands cover all seven subtopics
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7) with
# dwell time proportional to subtopics.json (225/250/245/230/210/240/230 of
# 1630 s). The ice-cream value chain and the orientation test are hand-built
# from exporter-safe primitives only (Tex/MathTex/Line/Arrow/Dot/Rectangle/
# VGroup); add-only lifecycle, the camera moves down between bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class IndustryTypesLocationFactorsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # --- Band 0 (subtopic_1): the sector's share and value added ---
        title = Tex("Industry Types and Location Factors").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Secondary sector: $\pm$ a fifth of GDP").scale(1.1).shift(UP * 0.9)
        b0_l2 = Tex(r"Manufacturing 12--14\%, one in ten jobs").scale(1.1).shift(UP * 0.1)
        self.play(Write(b0_l1)); self.wait(2)
        self.play(Write(b0_l2)); self.wait(2)
        b0_l3 = Tex(r"Value added: chrome $\rightarrow$ ferrochrome $\rightarrow$ steel goods").scale(1.0).shift(DOWN * 0.9)
        self.play(Write(b0_l3)); self.wait(2)
        b0_l4 = Tex(r"Export raw, import finished $=$ sell cheap, buy dear").scale(1.0).shift(DOWN * 1.8)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the four arguments for manufacturing ---
        self.next_band(1)
        b1_t = Tex("Four arguments for manufacturing").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex(r"1. Value added --- the beneficiation case").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex(r"2. Formal jobs + employment multipliers").scale(1.05).shift(band_shift(1) + UP * 0.3)
        b1_l3 = Tex(r"3. Linkages: backward to farms and mines,").scale(1.05).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = Tex(r"forward to trade, transport, finance").scale(1.05).shift(band_shift(1) + DOWN * 1.2)
        b1_l5 = Tex(r"4. Export diversification --- vehicles lead").scale(1.05).shift(band_shift(1) + DOWN * 2.0)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4, b1_l5):
            self.play(Write(m))
            self.wait(1.8)
        b1_l6 = Tex(r"Rosslyn, East London, Durban, Kariega").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l6))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): heavy/light, raw-material/market orientated ---
        self.next_band(2)
        b2_t = Tex("The field guide, in contrasting pairs").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex(r"Heavy: steel, fuel-from-coal --- land, rail, water").scale(0.95).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex(r"Light: clothing, food --- parks by main roads").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1)); self.wait(1.8)
        self.play(Write(b2_l2)); self.wait(2)
        b2_l3 = Tex(r"Raw-material-orientated: input shrinks or spoils").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = Tex(r"$\rightarrow$ fish canneries at St Helena Bay").scale(0.95).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l3)); self.wait(1.8)
        self.play(Write(b2_l4)); self.wait(2)
        b2_l5 = Tex(r"Market-orientated: output travels worst").scale(0.95).shift(band_shift(2) + DOWN * 1.9)
        b2_l6 = Tex(r"$\rightarrow$ bottlers and bakeries sit in cities").scale(0.95).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l5)); self.wait(1.8)
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): footloose, ubiquitous, bridge + the test ---
        self.next_band(3)
        b3_t = Tex("Footloose, ubiquitous, bridge").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex(r"Footloose: light or digital --- follows skills").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex(r"Ubiquitous: every town --- bakery, brickworks").scale(1.0).shift(band_shift(3) + UP * 0.3)
        b3_l3 = Tex(r"Bridge: break-of-bulk --- East London's harbour plants").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        for m in (b3_l1, b3_l2, b3_l3):
            self.play(Write(m))
            self.wait(1.8)
        b3_l4 = Tex(r"One-line test: which end costs more to move?").scale(1.05).shift(band_shift(3) + DOWN * 1.5)
        b3_l5 = Tex(r"The factory parks at the expensive end").scale(1.05).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l4)); self.wait(1.8)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the eight location factors ---
        self.next_band(4)
        b4_t = Tex("Eight weights on the location scale").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        rows = [
            r"Raw materials --- the cannery goes to the fish",
            r"Labour --- skills wait in the metros",
            r"Water --- paper mills on KZN rivers",
            r"Energy --- smelters on the coalfields",
            r"Transport --- the Durban--Gauteng spine",
            r"Markets --- Gauteng's buying power",
        ]
        for i, txt in enumerate(rows):
            m = Tex(txt).scale(0.95).shift(band_shift(4) + UP * (1.1 - 0.7 * i))
            self.play(Write(m))
            self.wait(1.6)
        self.wait(2.5)

        # --- Band 5 (subtopic_3): the two humans + the weighing skill ---
        self.next_band(5)
        b5_t = Tex("The two human weights").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex(r"Political intervention: SEZs, IDZs,").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"incentives, policy certainty").scale(1.05).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1)); self.wait(1.6)
        self.play(Write(b5_l2)); self.wait(1.8)
        b5_l3 = Tex(r"Competition and trade: tariffs, AfCFTA,").scale(1.05).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex(r"cheap imports hollowing textile towns").scale(1.05).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l3)); self.wait(1.6)
        self.play(Write(b5_l4)); self.wait(1.8)
        b5_l5 = Tex(r"Scenario skill: name the 2--3 factors that").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        b5_l6 = Tex(r"dominate for THAT industry --- the weighing").scale(1.0).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l5)); self.wait(1.5)
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): what holds industry back ---
        self.next_band(6)
        b6_t = Tex("What holds industry back").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex(r"Load-shedding, failing rail, queuing ports").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex(r"Scarce skills, strikes, crime, cheap imports").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex(r"Distance from world markets").scale(1.0).shift(band_shift(6) + DOWN * 0.3)
        for m in (b6_l1, b6_l2, b6_l3):
            self.play(Write(m))
            self.wait(1.7)
        b6_l4 = Tex(r"Structural: over-concentration in four regions").scale(1.0).shift(band_shift(6) + DOWN * 1.1)
        b6_l5 = Tex(r"+ pollution (Vaal Triangle, south Durban)").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4)); self.wait(1.7)
        self.play(Write(b6_l5)); self.wait(1.7)
        b6_l6 = Tex(r"Evaluate $=$ both pans: hindrance AND strength").scale(1.0).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the ice-cream rule ---
        self.next_band(7)
        b7_t = Tex("The ice-cream rule").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        sc7 = band_shift(7)
        s1 = Tex(r"milk\\R7").scale(1.0).shift(sc7 + UP * 0.9 + LEFT * 4.0)
        s2 = Tex(r"tub\\R70").scale(1.0).shift(sc7 + UP * 0.9)
        s3 = Tex(r"cones\\R200+").scale(1.0).shift(sc7 + UP * 0.9 + RIGHT * 4.0)
        self.play(Write(s1))
        self.wait(1.2)
        a1 = Arrow(sc7 + UP * 0.9 + LEFT * 3.0, sc7 + UP * 0.9 + LEFT * 1.1, color=GREEN, buff=0.1)
        self.play(Create(a1), Write(s2))
        self.wait(1.2)
        a2 = Arrow(sc7 + UP * 0.9 + RIGHT * 1.1, sc7 + UP * 0.9 + RIGHT * 3.0, color=GREEN, buff=0.1)
        self.play(Create(a2), Write(s3))
        self.wait(2)
        b7_l1 = Tex(r"The middle jump is manufacturing:").scale(1.05).shift(sc7 + DOWN * 0.4)
        b7_l2 = Tex(r"raw thing $\rightarrow$ made thing $=$ value added").scale(1.05).shift(sc7 + DOWN * 1.1)
        self.play(Write(b7_l1)); self.wait(1.8)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex(r"One plant turns a dozen other gears:").scale(1.0).shift(sc7 + DOWN * 2.0)
        b7_l4 = Tex(r"dairies, tubs, cold trucks --- multipliers").scale(1.0).shift(sc7 + DOWN * 2.7)
        self.play(Write(b7_l3)); self.wait(1.6)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (subtopic_6): the chip-shop test ---
        self.next_band(8)
        b8_t = Tex("The chip-shop test").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex(r"What is more of a pain to move ---").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"what it USES, or what it SELLS?").scale(1.05).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1)); self.wait(1.6)
        self.play(Write(b8_l2)); self.wait(2)
        b8_l3 = Tex(r"Spoiling, shrinking fish $\rightarrow$ cannery at the bay").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex(r"Fresh bread, heavy bottles $\rightarrow$ plant in town").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l3)); self.wait(1.8)
        self.play(Write(b8_l4)); self.wait(2)
        b8_l5 = Tex(r"Five questions: heavy or light? which end?").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        b8_l6 = Tex(r"footloose? everywhere? at the bridge?").scale(1.0).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l5)); self.wait(1.6)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): choosing an address, and why it is hard ---
        self.next_band(9)
        b9_t = Tex("Choosing an address, and what makes it hard").scale(1.05).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex(r"Checklist: ingredients, workers, water,").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"power, transport, customers, incentives").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1)); self.wait(1.6)
        self.play(Write(b9_l2)); self.wait(1.8)
        b9_l3 = Tex(r"Weigh, don't recite: 2--3 questions dominate").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l3)); self.wait(2)
        b9_l4 = Tex(r"From the news: power cuts, limping trains,").scale(1.0).shift(band_shift(9) + DOWN * 1.2)
        b9_l5 = Tex(r"scarce skills, strikes, stolen cable, imports").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4)); self.wait(1.6)
        self.play(Write(b9_l5)); self.wait(1.8)
        b9_l6 = Tex(r"Balance: Africa's most complete industrial machine").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(4)
