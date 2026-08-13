from manim import *

# Band-layout whiteboard scene for "Circular Flow, Leakages and Injections"
# (grade 10, term 1). One band per teaching beat; camera moves down, earlier
# work stays. The circular-flow diagram is hand-built from labelled
# Rectangles and Arrows only (exporter-safe primitives).
#
# Subtopic shares (subtopics.json, total 1420 s):
# 210/210/180/240/190/200/190.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CircularFlowLeakagesInjectionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): households and firms, the first loop ---
        title = Tex("The Circular Flow").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        hh_box = Rectangle(width=3.4, height=1.2).shift(LEFT * 4.0 + DOWN * 0.4)
        hh_lab = Tex("Households").scale(1.0).move_to(hh_box)
        fm_box = Rectangle(width=3.4, height=1.2).shift(RIGHT * 4.0 + DOWN * 0.4)
        fm_lab = Tex("Firms").scale(1.0).move_to(fm_box)
        self.play(Create(hh_box), Write(hh_lab))
        self.play(Create(fm_box), Write(fm_lab))
        self.wait(2)
        a_fact = Arrow(LEFT * 2.2 + UP * 0.6, RIGHT * 2.2 + UP * 0.6,
                       buff=0, color=YELLOW, stroke_width=4)
        l_fact = Tex("factors of production").scale(0.8).next_to(a_fact, UP, buff=0.15)
        self.play(Create(a_fact), Write(l_fact))
        self.wait(2)
        a_inc = Arrow(RIGHT * 2.2 + UP * 0.05, LEFT * 2.2 + UP * 0.05,
                      buff=0, color=GREEN, stroke_width=4)
        l_inc = Tex("wages, rent, interest, profit").scale(0.75).next_to(a_inc, DOWN, buff=0.12)
        self.play(Create(a_inc), Write(l_inc))
        self.wait(2)
        a_spend = Arrow(LEFT * 2.2 + DOWN * 1.5, RIGHT * 2.2 + DOWN * 1.5,
                        buff=0, color=GREEN, stroke_width=4)
        l_spend = Tex("spending on goods").scale(0.8).next_to(a_spend, UP, buff=0.12)
        self.play(Create(a_spend), Write(l_spend))
        self.wait(2)
        a_goods = Arrow(RIGHT * 2.2 + DOWN * 2.2, LEFT * 2.2 + DOWN * 2.2,
                        buff=0, color=YELLOW, stroke_width=4)
        l_goods = Tex("goods and services").scale(0.8).next_to(a_goods, DOWN, buff=0.12)
        self.play(Create(a_goods), Write(l_goods))
        self.wait(3)

        # --- Band 1 (subtopic_1): real vs money flows, two markets ---
        self.next_band(1)
        b1t = Tex("Two markets, two kinds of flow").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        b1a = Tex(r"Factor market: factors hired,").scale(1.05).shift(band_shift(1) + UP * 1.2)
        b1b = Tex(r"factor incomes paid back").scale(1.05).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1a))
        self.play(Write(b1b))
        self.wait(2)
        b1c = Tex(r"Goods market: spending in,").scale(1.05).shift(band_shift(1) + DOWN * 0.3)
        b1d = Tex(r"goods and services out").scale(1.05).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1c))
        self.play(Write(b1d))
        self.wait(2)
        b1e = Tex(r"REAL flows one way, MONEY flows the").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        b1f = Tex(r"other — every real flow has a money flow").scale(1.0).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1e))
        self.play(Write(b1f))
        self.play(Create(SurroundingRectangle(VGroup(b1e, b1f), color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): savings leak, investment injects ---
        self.next_band(2)
        b2t = Tex("Leakages and injections").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        bank = Rectangle(width=4.2, height=1.1).shift(band_shift(2) + UP * 0.9)
        bank_lab = Tex("Financial sector").scale(0.95).move_to(bank)
        self.play(Create(bank), Write(bank_lab))
        a_save = Arrow(band_shift(2) + LEFT * 4.6 + UP * 0.9, bank.get_left(),
                       buff=0.1, color=RED, stroke_width=4)
        l_save = Tex("savings (leakage)").scale(0.85).next_to(a_save, UP, buff=0.12)
        self.play(Create(a_save), Write(l_save))
        self.wait(2)
        a_inv = Arrow(bank.get_right(), band_shift(2) + RIGHT * 4.6 + UP * 0.9,
                      buff=0.1, color=GREEN, stroke_width=4)
        l_inv = Tex("investment (injection)").scale(0.85).next_to(a_inv, UP, buff=0.12)
        self.play(Create(a_inv), Write(l_inv))
        self.wait(2.5)
        b2a = Tex(r"Banks lend savings to firms, which").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        b2b = Tex(r"buy machines, buildings, equipment").scale(1.0).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2a))
        self.play(Write(b2b))
        self.wait(2)
        b2c = Tex(r"Leakage: money out of the stream.").scale(1.0).shift(band_shift(2) + DOWN * 2.2)
        b2d = Tex(r"Injection: money pumped back in.").scale(1.0).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2c))
        self.play(Write(b2d))
        self.wait(3)

        # --- Band 3 (subtopic_2): the equilibrium comparison ---
        self.next_band(3)
        b3t = Tex("Grow, shrink, or hold steady").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        b3a = MathTex(r"\text{leakages} > \text{injections} \Rightarrow \text{contracts}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3b = MathTex(r"\text{injections} > \text{leakages} \Rightarrow \text{expands}").scale(1.05).shift(band_shift(3) + UP * 0.2)
        b3c = MathTex(r"\text{leakages} = \text{injections} \Rightarrow \text{equilibrium}").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3a))
        self.wait(2)
        self.play(Write(b3b))
        self.wait(2)
        self.play(Write(b3c))
        self.play(Create(SurroundingRectangle(b3c, color=GREEN)))
        self.wait(2.5)
        b3w = Tex(r"``Leakages bad, injections good''").scale(1.05).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3w))
        self.play(Create(strike(b3w)))
        self.wait(1.5)
        b3d = Tex(r"They describe DIRECTION, not virtue —").scale(1.0).shift(band_shift(3) + DOWN * 2.6)
        b3e = Tex(r"savings finance tomorrow's investment").scale(1.0).shift(band_shift(3) + DOWN * 3.3)
        self.play(Write(b3d))
        self.play(Write(b3e))
        self.wait(3)

        # --- Band 4 (subtopic_3): adding government ---
        self.next_band(4)
        b4t = Tex("Adding government").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        gov = Rectangle(width=4.0, height=1.1).shift(band_shift(4) + UP * 0.9)
        gov_lab = Tex("Government").scale(0.95).move_to(gov)
        self.play(Create(gov), Write(gov_lab))
        a_tax = Arrow(band_shift(4) + LEFT * 4.6 + UP * 0.9, gov.get_left(),
                      buff=0.1, color=RED, stroke_width=4)
        l_tax = Tex("taxes (leakage)").scale(0.85).next_to(a_tax, UP, buff=0.12)
        self.play(Create(a_tax), Write(l_tax))
        self.wait(2)
        a_gsp = Arrow(gov.get_right(), band_shift(4) + RIGHT * 4.6 + UP * 0.9,
                      buff=0.1, color=GREEN, stroke_width=4)
        l_gsp = Tex("spending (injection)").scale(0.85).next_to(a_gsp, UP, buff=0.12)
        self.play(Create(a_gsp), Write(l_gsp))
        self.wait(2.5)
        b4a = Tex(r"Teachers, nurses, roads, schools,").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4b = Tex(r"grants — plus public goods both ways").scale(1.0).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4a))
        self.play(Write(b4b))
        self.wait(2)
        b4c = Tex(r"Tally: leakages — savings, taxes;").scale(1.0).shift(band_shift(4) + DOWN * 2.2)
        b4d = Tex(r"injections — investment, gov. spending").scale(1.0).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4c))
        self.play(Write(b4d))
        self.wait(3)

        # --- Band 5 (subtopic_4): the foreign sector opens the economy ---
        self.next_band(5)
        b5t = Tex("The foreign sector — opening up").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        fs = Rectangle(width=4.2, height=1.1).shift(band_shift(5) + UP * 0.9)
        fs_lab = Tex("Foreign sector").scale(0.95).move_to(fs)
        self.play(Create(fs), Write(fs_lab))
        a_imp = Arrow(band_shift(5) + LEFT * 4.6 + UP * 0.9, fs.get_left(),
                      buff=0.1, color=RED, stroke_width=4)
        l_imp = Tex("imports (leakage)").scale(0.85).next_to(a_imp, UP, buff=0.12)
        self.play(Create(a_imp), Write(l_imp))
        self.wait(2)
        a_exp = Arrow(fs.get_right(), band_shift(5) + RIGHT * 4.6 + UP * 0.9,
                      buff=0.1, color=GREEN, stroke_width=4)
        l_exp = Tex("exports (injection)").scale(0.85).next_to(a_exp, UP, buff=0.12)
        self.play(Create(a_exp), Write(l_exp))
        self.wait(2.5)
        b5a = Tex(r"Phones from China: money leaves.").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        b5b = Tex(r"Our gold, fruit, wine sold: money enters.").scale(1.0).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5a))
        self.play(Write(b5b))
        self.wait(2)
        b5c = Tex(r"Open economy: 4 participants, 3 markets").scale(1.0).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5c))
        self.wait(3)

        # --- Band 6 (subtopic_4): master lists and the three doors ---
        self.next_band(6)
        b6t = Tex("The master lists — three doors").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        b6a = Tex(r"Leakages: savings, taxes, imports").scale(1.05).shift(band_shift(6) + UP * 1.2)
        b6b = Tex(r"Injections: investment, gov.\ spending,").scale(1.05).shift(band_shift(6) + UP * 0.5)
        b6c = Tex(r"exports").scale(1.05).shift(band_shift(6) + DOWN * 0.1)
        self.play(Write(b6a))
        self.wait(2)
        self.play(Write(b6b))
        self.play(Write(b6c))
        box6 = SurroundingRectangle(VGroup(b6a, b6b, b6c), color=GREEN)
        self.play(Create(box6))
        self.wait(2)
        b6d = Tex(r"Bank door: savings out, investment in").scale(0.95).shift(band_shift(6) + DOWN * 1.0)
        b6e = Tex(r"Government door: taxes out, spending in").scale(0.95).shift(band_shift(6) + DOWN * 1.7)
        b6f = Tex(r"Border door: imports out, exports in").scale(0.95).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6d))
        self.play(Write(b6e))
        self.play(Write(b6f))
        self.wait(2)
        b6g = Tex(r"Japanese TV? Leakage. New clinic? Injection.").scale(0.9).shift(band_shift(6) + DOWN * 3.1)
        self.play(Write(b6g))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): Friday in the neighbourhood ---
        self.next_band(7)
        b7t = Tex("Friday in the neighbourhood").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex(r"Wage lands Friday; Saturday it's at the").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7b = Tex(r"spaza, the rank, the shop — and their").scale(1.0).shift(band_shift(7) + UP * 0.5)
        b7c = Tex(r"takings pay the next wages: it CIRCLES").scale(1.0).shift(band_shift(7) + DOWN * 0.2)
        self.play(Write(b7a))
        self.play(Write(b7b))
        self.play(Write(b7c))
        self.wait(2.5)
        b7d = Tex(r"Hiring side of life $=$ factor market").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        b7e = Tex(r"Till side of life $=$ goods market").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7d))
        self.play(Write(b7e))
        self.wait(2)
        b7f = Tex(r"Two-lane traffic: real things one way,").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        b7g = Tex(r"money the other").scale(1.0).shift(band_shift(7) + DOWN * 3.3)
        self.play(Write(b7f))
        self.play(Write(b7g))
        self.wait(3)

        # --- Band 8 (subtopic_6): three drains and three taps ---
        self.next_band(8)
        b8t = Tex("Three drains, three taps").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"Bank door: auntie's R500 saved (drain),").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8b = Tex(r"lent for the bakery's oven (tap)").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8a))
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex(r"SARS door: tax out (drain), clinics,").scale(0.95).shift(band_shift(8) + DOWN * 0.3)
        b8d = Tex(r"salaries, roads back in (tap)").scale(0.95).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(b8c))
        self.play(Write(b8d))
        self.wait(2)
        b8e = Tex(r"Border door: China phone out (drain),").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        b8f = Tex(r"wine to Britain in (tap)").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8e))
        self.play(Write(b8f))
        self.wait(2)
        b8g = Tex(r"Learn three doors, not six facts").scale(1.05).shift(band_shift(8) + DOWN * 3.2)
        self.play(Write(b8g))
        self.play(Create(SurroundingRectangle(b8g, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): reading the water level ---
        self.next_band(9)
        b9t = Tex("Reading the water level").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex(r"Drains beat taps: level drops —").scale(1.05).shift(band_shift(9) + UP * 1.2)
        b9b = Tex(r"quiet tills, shorter shifts").scale(1.05).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9a))
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex(r"Taps beat drains: level rises —").scale(1.05).shift(band_shift(9) + DOWN * 0.3)
        b9d = Tex(r"more spending, production, hiring").scale(1.05).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(b9c))
        self.play(Write(b9d))
        self.wait(2)
        b9e = Tex(r"Equal: equilibrium — ``things are stable''").scale(1.05).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9e))
        self.play(Create(SurroundingRectangle(b9e, color=GREEN)))
        self.wait(2)
        b9f = Tex(r"Every headline is a drain or a tap:").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        b9g = Tex(r"infrastructure spending $=$ tap opening").scale(1.0).shift(band_shift(9) + DOWN * 3.3)
        self.play(Write(b9f))
        self.play(Write(b9g))
        self.wait(4)
