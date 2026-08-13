from manim import *

# Band layout: one frame-height band per teaching beat; the camera moves down,
# nothing is removed. Exporter-supported mobjects only (Tex/MathTex/Line/
# Rectangle/SurroundingRectangle); every line is a single-string Write reveal.
#
# Covers all seven subtopics (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# band time roughly proportional to subtopics.json
# (210/215/225/235/190/195/200 of 1470 s).

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
        # Intro beat: topic full screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the metric ladder ---
        title = Tex("Conversions and Estimating").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l1 = MathTex(r"1\text{ km} = 1\,000\text{ m}, \quad 1\text{ m} = 1\,000\text{ mm}").scale(0.94).shift(UP * 1.1)
        l2 = MathTex(r"1\text{ kg} = 1\,000\text{ g}, \quad 1\ \ell = 1\,000\text{ m}\ell").scale(0.99).shift(UP * 0.2)
        l3 = Tex(r"Exception: 1 m $= 100$ cm; 1 cm $= 10$ mm").scale(1.05).shift(DOWN * 0.7)
        self.play(Write(l1)); self.wait(2)
        self.play(Write(l2)); self.wait(2)
        self.play(Write(l3)); self.wait(2)
        rule = Tex(r"To a SMALLER unit: multiply. LARGER: divide.").scale(1.05).shift(DOWN * 1.7)
        self.play(Write(rule))
        self.play(Create(SurroundingRectangle(rule, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): worked conversions + habits ---
        self.next_band(1)
        b1_title = Tex("Direction decided first").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"2{,}4\text{ km} = 2{,}4 \times 1\,000 = 2\,400\text{ m}").scale(1.1).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"750\text{ g} = 750 \div 1\,000 = 0{,}75\text{ kg}").scale(1.1).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"18\text{ k}\ell = 18 \times 1\,000 = 18\,000\ \ell").scale(1.1).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3)); self.wait(2)
        b1_l4 = Tex(r"Room 4,2 m by 340 cm: make it 4,2 m by 3,4 m FIRST").scale(0.95).shift(band_shift(1) + DOWN * 1.7)
        b1_l5 = Tex(r"Sense check: a bath of 8\,000 $\ell$? Recheck!").scale(1.0).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l4)); self.wait(2.5)
        self.play(Write(b1_l5)); self.wait(2.5)

        # --- Band 2 (subtopic_2): imperial conversions, both directions ---
        self.next_band(2)
        b2_title = Tex("Crossing into imperial").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_t1 = Tex(r"1 inch $= 2{,}54$ cm; \; 1 foot $= 30{,}48$ cm").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_t2 = Tex(r"1 mile $\approx 1{,}609$ km; \; 1 kg $\approx 2{,}2$ lb").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_t1)); self.wait(2)
        self.play(Write(b2_t2)); self.wait(2)
        b2_l1 = MathTex(r"50\text{ kg} = 50 \times 2{,}2 = 110\text{ lb}").scale(1.1).shift(band_shift(2) + DOWN * 0.6)
        b2_l2 = MathTex(r"33\text{ lb} = 33 \div 2{,}2 = 15\text{ kg}").scale(1.1).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l1)); self.wait(2.5)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): height, speed and the direction trap ---
        self.next_band(3)
        b3_title = Tex("The direction trap").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"6\text{ ft} = 6 \times 30{,}48 = 182{,}88\text{ cm} \approx 1{,}83\text{ m}").scale(0.95).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"60\text{ mph} = 60 \times 1{,}609 = 96{,}54\text{ km/h}").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1)); self.wait(2.5)
        self.play(Write(b3_l2)); self.wait(2.5)
        b3_l3 = Tex(r"Ask: which unit is BIGGER?").scale(1.1).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = Tex(r"1 kg $>$ 1 lb, so pounds must be the bigger number").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = Tex(r"Round only at the end, to what the context can use").scale(1.0).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l3)); self.wait(2)
        self.play(Write(b3_l4)); self.wait(2)
        self.play(Write(b3_l5)); self.wait(2.5)

        # --- Band 4 (subtopic_3): temperature by formula ---
        self.next_band(4)
        b4_title = Tex(r"Temperature: the oven at 350 °F").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_f1 = Tex(r"°F to °C: subtract 32, $\times 5$, $\div 9$").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_f1)); self.wait(2)
        b4_l1 = MathTex(r"350 - 32 = 318").scale(1.1).shift(band_shift(4) + UP * 0.3)
        b4_l2 = MathTex(r"318 \times 5 = 1\,590").scale(1.1).shift(band_shift(4) + DOWN * 0.6)
        b4_l3 = MathTex(r"1\,590 \div 9 = 176{,}67\ °C").scale(1.1).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l1)); self.wait(2)
        self.play(Write(b4_l2)); self.wait(2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = Tex(r"Set the dial to 180 °C — the nearest setting").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l4)); self.wait(2.5)

        # --- Band 5 (subtopic_3): the other direction, and time ---
        self.next_band(5)
        b5_title = Tex("Fever charts and timetables").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"38{,}5 \times 9 = 346{,}5; \;\; \div 5 = 69{,}3; \;\; + 32 = 101{,}3\ °F").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1)); self.wait(2.5)
        b5_wrong = MathTex(r"16{,}05 - 14{,}20 = 1{,}85 \quad \text{(not a time!)}").scale(1.0).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l2 = Tex(r"14:20 to 16:05: count forwards — 1 h 45 min").scale(1.0).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l2)); self.wait(2.5)
        b5_l3 = Tex(r"Bus: 05:45 $+$ 6 h $=$ 11:45; $+$ 40 min $=$ 12:25").scale(1.0).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): paint coverage ---
        self.next_band(6)
        b6_title = Tex(r"Paint: 5 $\ell$ covers 20 m$^2$").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Unit rate: } 20 \div 5 = 4\text{ m}^2 \text{ per litre}").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"\text{Two coats: } 54 \times 2 = 108\text{ m}^2").scale(1.05).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"\text{Paint needed: } 108 \div 4 = 27\ \ell").scale(1.1).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l1)); self.wait(2.5)
        self.play(Write(b6_l2)); self.wait(2.5)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): what to buy ---
        self.next_band(7)
        b7_title = Tex(r"The shop sells tins, not litres").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"5 $\ell$ tin R429; \; 20 $\ell$ drum R1\,549").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{Drum} + 2\text{ tins: } 1\,549 + 858 = R2\,407").scale(1.05).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"\text{Six tins: } 6 \times 429 = R2\,574").scale(1.05).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = MathTex(r"\text{Saving: } 2\,574 - 2\,407 = R167").scale(1.1).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l1)); self.wait(2)
        self.play(Write(b7_l2)); self.wait(2.5)
        self.play(Write(b7_l3)); self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("Answer in a sentence: buy the drum and two tins").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5)); self.wait(2.5)

        # --- Band 8 (subtopic_4): doses and recipes ---
        self.next_band(8)
        b8_title = Tex("Doses and recipes scale the same way").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"7{,}5 \times 3 \times 5 = 112{,}5\text{ m}\ell \Rightarrow 2\text{ bottles}").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"Teaspoon $\approx 5$ m$\ell$, so 7,5 m$\ell$ $=$ 1$\tfrac{1}{2}$ teaspoons").scale(0.91).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1)); self.wait(2.5)
        self.play(Write(b8_l2)); self.wait(2.5)
        b8_l3 = MathTex(r"\text{Serve 30 from 4: scale by } 30 \div 4 = 7{,}5").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = MathTex(r"3\text{ eggs} \times 7{,}5 = 22{,}5 \Rightarrow \text{buy }23").scale(1.05).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l3)); self.wait(2)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = Tex("Paint and eggs round UP; a dose never rounds").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l5)); self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): moving the decimal point ---
        self.next_band(9)
        b9_title = Tex("Everything metric is built on a thousand").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = Tex("A kilometre is a long way; a metre is one step").scale(1.05).shift(band_shift(9) + UP * 1.2)
        b9_l2 = MathTex(r"2{,}4\text{ km} = 2\,400\text{ m} \quad \text{(lots of steps)}").scale(1.05).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1)); self.wait(3)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(3)
        b9_l3 = Tex("Smaller unit, bigger number. Bigger unit, smaller.").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3)); self.wait(3)
        b9_l4 = Tex("Fingernail $\\approx$ 1 cm; step $\\approx$ 1 m; bottle 2 $\\ell$").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        b9_l5 = Tex("A 700 kg cousin? Something broke three lines ago").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l4)); self.wait(3)
        self.play(Write(b9_l5)); self.wait(3.5)

        # --- Band 10 (subtopic_6): granny's recipe ---
        self.next_band(10)
        b10_title = Tex("Granny's recipe says 350 degrees").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = Tex("Celsius freezes at 0; Fahrenheit freezes at 32").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1)); self.wait(3)
        b10_l2 = MathTex(r"350 - 32 = 318; \;\; \times 5 = 1\,590; \;\; \div 9 = 176{,}67").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(3)
        b10_l3 = Tex("Take the 32 off FIRST coming down; add it LAST going up").scale(0.95).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l3)); self.wait(3)
        b10_l4 = MathTex(r"\text{Cement: } 50 \times 2{,}2 = 110\text{ lb}; \quad 33 \div 2{,}2 = 15\text{ kg}").scale(0.83).shift(band_shift(10) + DOWN * 1.7)
        b10_l5 = Tex("Bigger unit becomes more of the smaller — like rands to cents").scale(0.9).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l4)); self.wait(3)
        self.play(Write(b10_l5)); self.wait(3.5)

        # --- Band 11 (subtopic_7): how much paint, how much medicine ---
        self.next_band(11)
        b11_title = Tex("The tin tells you the rate").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2.5)
        b11_l1 = MathTex(r"20 \div 5 = 4\text{ m}^2\text{ per litre}; \quad 108 \div 4 = 27\ \ell").scale(0.88).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11_l1)); self.wait(3)
        b11_l2 = Tex(r"Buy the 20 $\ell$ drum $+$ two tins: R2\,407, saves R167").scale(1.0).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11_l2))
        self.play(Create(SurroundingRectangle(b11_l2, color=GREEN)))
        self.wait(3)
        b11_l3 = MathTex(r"\text{Medicine: } 112{,}5\text{ m}\ell \Rightarrow 2\text{ bottles}").scale(0.95).shift(band_shift(11) + DOWN * 0.8)
        self.play(Write(b11_l3)); self.wait(3)
        b11_l4 = MathTex(r"\text{Feed 30 from 4: } \times 7{,}5; \quad 3\text{ eggs} \to 23\text{ eggs}").scale(0.9).shift(band_shift(11) + DOWN * 1.8)
        self.play(Write(b11_l4)); self.wait(3)
        b11_l5 = Tex("Read the rate, scale it, then decide what to BUY").scale(1.0).shift(band_shift(11) + DOWN * 2.7)
        self.play(Write(b11_l5)); self.wait(4)
