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

# Band layout: one frame-height band per teaching beat; the camera moves down,
# nothing is removed. Every mobject serializes to the exporter's
# text/line/rect/dot/circle vocabulary; every line of working is a
# single-string Tex/MathTex revealed with Write — no sub-part transforms.
#
# Covers all seven subtopics of the session duo (Part 1 — Expert: subtopics
# 1-4; Part 2 — Simplifier: subtopics 5-7), band time roughly proportional to
# subtopics.json (210/215/225/235/190/195/200 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ConversionsAndEstimatingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the metric ladder ---
        title = Tex("Conversions and Estimating").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        m1 = Tex(r"1 m $= 1\,000$ mm; \; 1 km $= 1\,000$ m").scale(1.05).shift(UP * 1.1)
        m2 = Tex(r"1 kg $= 1\,000$ g; \; 1 t $= 1\,000$ kg").scale(1.05).shift(UP * 0.2)
        m3 = Tex(r"1 $\ell$ $= 1\,000$ m$\ell$; \; 1 k$\ell$ $= 1\,000$ $\ell$").scale(1.05).shift(DOWN * 0.7)
        m4 = Tex(r"Exception: 1 m $= 100$ cm; \; 1 cm $= 10$ mm").scale(1.05).shift(DOWN * 1.6)
        self.play(Write(m1)); self.wait(2)
        self.play(Write(m2)); self.wait(2)
        self.play(Write(m3)); self.wait(2)
        self.play(Write(m4)); self.wait(2.5)

        # --- Band 1 (subtopic_1): worked conversions + habits ---
        self.next_band(1)
        b1_title = Tex("Smaller unit: multiply. Larger unit: divide.").scale(1.1).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"3{,}6 \text{ km} = 3{,}6 \times 1\,000 = 3\,600 \text{ m}").scale(1.05).shift(band_shift(1) + UP * 1.3)
        b1_l2 = MathTex(r"250 \text{ g} = 250 \div 1\,000 = 0{,}25 \text{ kg}").scale(1.05).shift(band_shift(1) + UP * 0.4)
        b1_l3 = MathTex(r"24 \text{ k}\ell = 24 \times 1\,000 = 24\,000 \ \ell").scale(1.05).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3)); self.wait(2)
        b1_r1 = Tex(r"Convert BEFORE calculating: 3,8 m $\times$ 260 cm").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        b1_r2 = MathTex(r"\Rightarrow 3{,}8 \text{ m} \times 2{,}6 \text{ m}").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_r1)); self.wait(2)
        self.play(Write(b1_r2))
        self.play(Create(SurroundingRectangle(b1_r2, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): imperial conversions, both directions ---
        self.next_band(2)
        b2_title = Tex("Crossing into imperial — the table is supplied").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_t = Tex(r"1 in $= 2{,}54$ cm; 1 ft $= 30{,}48$ cm; 1 mi $\approx 1{,}609$ km; 1 kg $\approx 2{,}2$ lb").scale(0.85).shift(band_shift(2) + UP * 1.4)
        self.play(Write(b2_t)); self.wait(2.5)
        b2_l1 = MathTex(r"25 \text{ kg} \times 2{,}2 = 55 \text{ lb}").scale(1.1).shift(band_shift(2) + UP * 0.4)
        b2_l2 = MathTex(r"44 \text{ lb} \div 2{,}2 = 20 \text{ kg}").scale(1.1).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2_l1)); self.wait(2.5)
        self.play(Write(b2_l2)); self.wait(2.5)
        b2_rule = Tex("Which unit is BIGGER? The bigger unit makes MORE of the smaller").scale(0.9).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_rule))
        self.wait(3)

        # --- Band 3 (subtopic_2): height, speed and the direction trap ---
        self.next_band(3)
        b3_title = Tex("Height and speed, sense-checked").scale(1.1).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"5'10'' = 70 \text{ in}; \; 70 \times 2{,}54 = 177{,}8 \text{ cm} \approx 1{,}78 \text{ m}").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"45 \text{ mph} = 45 \times 1{,}609 \approx 72{,}4 \text{ km/h}").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1)); self.wait(2.5)
        self.play(Write(b3_l2)); self.wait(2.5)
        b3_l3 = Tex("1,78 m tall, 72 km/h in town — both believable").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = Tex("Round only at the END, to what the context can use").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l3)); self.wait(2.5)
        self.play(Write(b3_l4)); self.wait(3)

        # --- Band 4 (subtopic_3): temperature by formula ---
        self.next_band(4)
        b4_title = Tex(r"Recipe at 400 °F — the oven speaks Celsius").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"F to C: subtract 32 FIRST, then $\times 5$, then $\div 9$").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"400 - 32 = 368").scale(1.05).shift(band_shift(4) + UP * 0.4)
        b4_l3 = MathTex(r"368 \times 5 = 1\,840").scale(1.05).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = MathTex(r"1\,840 \div 9 = 204{,}44\,°C \Rightarrow \text{set } 200\,°C").scale(1.05).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_l1)); self.wait(2)
        self.play(Write(b4_l2)); self.wait(2)
        self.play(Write(b4_l3)); self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the other direction, and time ---
        self.next_band(5)
        b5_title = Tex("Going up, and counting time forwards").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"39\,°C: \; 39 \times 9 = 351; \; \div 5 = 70{,}2; \; + 32 = 102{,}2\,°F").scale(0.95).shift(band_shift(5) + UP * 1.3)
        self.play(Write(b5_l1)); self.wait(2.5)
        b5_w = MathTex(r"15{,}10 - 13{,}35 = 1{,}75 \quad \text{(not a time!)}").scale(1.0).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_w))
        self.play(Create(strike(b5_w)))
        self.wait(2)
        b5_l2 = Tex(r"13:35 $\to$ 14:35 $\to$ 15:10 $=$ 1 h 35").scale(1.05).shift(band_shift(5) + DOWN * 0.7)
        b5_l3 = Tex(r"Bus: 06:50 $+$ 5 h 25 $\to$ 11:50 $+$ 25 min $=$ 12:15").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l2)); self.wait(2.5)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): paint coverage ---
        self.next_band(6)
        b6_title = Tex(r"Label: 5 $\ell$ covers 30 m$^2$").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"30 \div 5 = 6 \text{ m}^2 \text{ per litre}").scale(1.05).shift(band_shift(6) + UP * 1.3)
        b6_l2 = MathTex(r"\text{Wall: } 51 \times 2 \text{ coats} = 102 \text{ m}^2").scale(1.05).shift(band_shift(6) + UP * 0.4)
        b6_l3 = MathTex(r"102 \div 6 = 17 \ \ell").scale(1.1).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l1)); self.wait(2.5)
        self.play(Write(b6_l2)); self.wait(2.5)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): what to buy ---
        self.next_band(7)
        b7_title = Tex("Nobody sells 17 litres").scale(1.1).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{Four 5 } \ell \text{ tins: } 4 \times 465 = R1\,860").scale(1.05).shift(band_shift(7) + UP * 1.3)
        b7_l2 = MathTex(r"\text{One 20 } \ell \text{ drum: } R1\,680").scale(1.05).shift(band_shift(7) + UP * 0.4)
        b7_l3 = MathTex(r"1\,860 - 1\,680 = R180 \text{ saved}").scale(1.05).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l1)); self.wait(2.5)
        self.play(Write(b7_l2)); self.wait(2.5)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("Answer in a sentence: buy the drum for R1\\,680").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (subtopic_4): doses and recipes ---
        self.next_band(8)
        b8_title = Tex("Doses and recipes scale the same way").scale(1.1).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"10 \text{ m}\ell \times 2 \times 7 = 140 \text{ m}\ell \Rightarrow \text{two 120 m}\ell \text{ bottles}").scale(0.95).shift(band_shift(8) + UP * 1.3)
        b8_l2 = MathTex(r"\text{Scale factor: } 27 \div 6 = 4{,}5").scale(1.05).shift(band_shift(8) + UP * 0.3)
        b8_l3 = MathTex(r"3 \text{ eggs} \times 4{,}5 = 13{,}5 \Rightarrow \text{buy } 14").scale(1.05).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l1)); self.wait(2.5)
        self.play(Write(b8_l2)); self.wait(2.5)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_rule = Tex("Paint and eggs round UP; money to cents; a dose never").scale(0.95).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_rule))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): moving the decimal point ---
        self.next_band(9)
        b9_title = Tex("Everything metric is a thousand").scale(1.15).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = MathTex(r"3{,}6 \text{ km} = 3\,600 \text{ m}").scale(1.1).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1)); self.wait(3)
        b9_l2 = Tex("Smaller unit, bigger number. Bigger unit, smaller number.").scale(0.95).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2)); self.wait(3)
        b9_l3 = Tex("Anchors: fingernail 1 cm; stride 1 m; bottle 2 $\\ell$").scale(0.95).shift(band_shift(9) + DOWN * 0.7)
        b9_l4 = Tex("A 4\\,000 $\\ell$ kettle? Go back three lines").scale(0.95).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l3)); self.wait(3)
        self.play(Write(b9_l4)); self.wait(3.5)

        # --- Band 10 (subtopic_6): granny's recipe ---
        self.next_band(10)
        b10_title = Tex("Granny's recipe in Fahrenheit").scale(1.15).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = Tex(r"Coming down: $-32$ first, then $\times 5$, then $\div 9$").scale(1.0).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10_l1)); self.wait(3)
        b10_l2 = MathTex(r"400 - 32 = 368; \; \times 5 = 1\,840; \; \div 9 = 204{,}44").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(3)
        b10_l3 = Tex("Set the oven to 200 and the bake behaves").scale(1.0).shift(band_shift(10) + DOWN * 0.7)
        b10_l4 = Tex("Going up: $\\times 9$, $\\div 5$, add the 32 LAST").scale(1.0).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_l3)); self.wait(3)
        self.play(Write(b10_l4)); self.wait(3.5)

        # --- Band 11 (subtopic_7): how much paint, how much medicine ---
        self.next_band(11)
        b11_title = Tex("How much paint, how much medicine").scale(1.15).shift(band_shift(11) + UP * 2.4)
        self.play(Write(b11_title))
        self.wait(2.5)
        b11_l1 = MathTex(r"102 \div 6 = 17 \ \ell \Rightarrow \text{buy the 20 } \ell \text{ drum, } R1\,680").scale(0.95).shift(band_shift(11) + UP * 1.3)
        self.play(Write(b11_l1)); self.wait(3)
        b11_l2 = MathTex(r"10 \times 2 \times 7 = 140 \text{ m}\ell \Rightarrow \text{two bottles}").scale(1.0).shift(band_shift(11) + UP * 0.3)
        self.play(Write(b11_l2)); self.wait(3)
        b11_l3 = MathTex(r"27 \div 6 = 4{,}5; \; 3 \text{ eggs} \to 13{,}5 \to 14").scale(1.0).shift(band_shift(11) + DOWN * 0.6)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(3)
        b11_l4 = Tex("Read the rate, scale it, then decide what to BUY").scale(1.0).shift(band_shift(11) + DOWN * 1.6)
        self.play(Write(b11_l4))
        self.wait(4)
