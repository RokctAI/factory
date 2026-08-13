from manim import *

# Band-layout whiteboard scene for the revision duo "Basic Concepts and
# Markets Essentials" (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier
# subtopics 5-7). All diagrams hand-built from exporter-safe primitives:
# axes = two Arrows, curves = chained Lines, flows = Arrows + Rectangles.
# Add-only lifecycle. Durations: 235/235/230/240/195/190/195 of 1520 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BasicConceptsMarketsRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===================== Part 1 — Expert =====================
        # --- Band 0 (subtopic_1): scarcity, choice, opportunity cost ---
        title = Tex("Revision: Basic Concepts and Markets").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0a = Tex("Scarce resources vs unlimited wants —").scale(1.05).shift(UP * 1.2)
        b0a2 = Tex("scarcity is permanent, a shortage passes").scale(1.05).shift(UP * 0.5)
        self.play(Write(b0a))
        self.play(Write(b0a2))
        self.wait(2)
        b0b = Tex("Opportunity cost $=$ the NEXT BEST alternative").scale(1.05).shift(DOWN * 0.4)
        self.play(Write(b0b))
        self.play(Create(SurroundingRectangle(b0b, color=GREEN)))
        self.wait(2)
        b0c = Tex("Three questions: WHAT $\\cdot$ HOW $\\cdot$ FOR WHOM").scale(0.98).shift(DOWN * 1.5)
        self.play(Write(b0c))
        self.wait(2)
        b0d = Tex("Micro: one unit $\\cdot$ Macro: the totals").scale(1.0).shift(DOWN * 2.4)
        self.play(Write(b0d))
        self.wait(3)

        # --- Band 1 (subtopic_1): the production possibility curve ---
        self.next_band(1)
        b1t = Tex("The production possibility curve").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        O1 = band_shift(1) + DOWN * 2.6 + LEFT * 4.8

        def P1(x, y):
            return O1 + RIGHT * x + UP * y

        ax1x = Arrow(P1(0, 0), P1(7.0, 0), buff=0, stroke_width=3)
        ax1y = Arrow(P1(0, 0), P1(0, 4.4), buff=0, stroke_width=3)
        l1x = Tex("Maize").scale(0.8).move_to(P1(6.4, -0.4))
        l1y = Tex("Clothing").scale(0.8).move_to(P1(-0.9, 4.1))
        self.play(Create(ax1x), Create(ax1y))
        self.play(Write(l1x), Write(l1y))
        self.wait(2)
        ppc = VGroup(
            Line(P1(0.2, 3.9), P1(2.2, 3.5), color=BLUE, stroke_width=5),
            Line(P1(2.2, 3.5), P1(4.0, 2.4), color=BLUE, stroke_width=5),
            Line(P1(4.0, 2.4), P1(5.0, 0.3), color=BLUE, stroke_width=5),
        )
        self.play(Create(ppc[0]), Create(ppc[1]), Create(ppc[2]))
        self.wait(2)
        d_on = Dot(P1(4.0, 2.4), color=GREEN)
        t_on = Tex("on: efficient", color=GREEN).scale(0.7).move_to(P1(5.6, 2.8))
        self.play(FadeIn(d_on), Write(t_on))
        self.wait(1.5)
        d_in = Dot(P1(1.8, 1.4), color=RED)
        t_in = Tex("inside: unemployment", color=RED).scale(0.7).move_to(P1(1.9, 0.9))
        self.play(FadeIn(d_in), Write(t_in))
        self.wait(1.5)
        d_out = Dot(P1(5.6, 3.6))
        t_out = Tex("beyond: unattainable").scale(0.7).move_to(P1(5.9, 4.1))
        self.play(FadeIn(d_out), Write(t_out))
        self.wait(2)
        gr_ar = Arrow(P1(2.9, 2.9), P1(4.0, 3.9), buff=0, color=GREEN)
        t_gr = Tex("outward shift $=$ growth", color=GREEN).scale(0.7).move_to(P1(5.4, 4.7))
        self.play(Create(gr_ar), Write(t_gr))
        self.wait(3)

        # --- Band 2 (subtopic_2): the circular flow ---
        self.next_band(2)
        b2t = Tex("The circular flow").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        rH = Rectangle(width=3.6, height=1.2).shift(band_shift(2) + LEFT * 4.2 + DOWN * 0.4)
        tH = Tex("Households").scale(0.9).move_to(rH.get_center())
        rF = Rectangle(width=3.6, height=1.2).shift(band_shift(2) + RIGHT * 4.2 + DOWN * 0.4)
        tF = Tex("Firms").scale(0.9).move_to(rF.get_center())
        self.play(Create(rH), Write(tH))
        self.play(Create(rF), Write(tF))
        self.wait(2)
        a_fac = Arrow(rH.get_top() + UP * 0.05, rF.get_top() + UP * 0.05,
                      buff=0.1, color=BLUE)
        t_fac = Tex("factors of production", color=BLUE).scale(0.75).shift(band_shift(2) + UP * 0.9)
        self.play(Create(a_fac), Write(t_fac))
        self.wait(1.5)
        a_inc = Arrow(rF.get_bottom() + DOWN * 0.05, rH.get_bottom() + DOWN * 0.05,
                      buff=0.1, color=GREEN)
        t_inc = Tex("income (wages, rent, interest, profit)", color=GREEN).scale(0.75).shift(band_shift(2) + DOWN * 1.6)
        self.play(Create(a_inc), Write(t_inc))
        self.wait(2)
        b2a = Tex("Goods flow one way, money the other —").scale(0.95).shift(band_shift(2) + DOWN * 2.4)
        b2b = Tex("product market and factor market close the circle").scale(0.95).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2a))
        self.play(Write(b2b))
        self.wait(3)

        # --- Band 3 (subtopic_2): leakages, injections, GDP vs GNI ---
        self.next_band(3)
        b3t = Tex("Leakages, injections and the national numbers").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("Leak out: savings $\\cdot$ taxes $\\cdot$ imports").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3b = Tex("Inject in: investment $\\cdot$ govt spending $\\cdot$ exports").scale(0.99).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3a))
        self.wait(2)
        self.play(Write(b3b))
        self.play(Create(SurroundingRectangle(VGroup(b3a, b3b), color=GREEN)))
        self.wait(2)
        b3wrong = Tex("GDP counts the flour AND the bread").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3wrong))
        self.play(Create(strike(b3wrong)))
        b3c = Tex("Final goods only — no double counting").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3c))
        self.wait(2)
        b3d = Tex("GDP: WHERE-rule (inside borders);").scale(1.0).shift(band_shift(3) + DOWN * 2.3)
        b3e = Tex("GNI: WHO-rule (follows factor income home)").scale(1.0).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3d))
        self.play(Write(b3e))
        self.wait(3)

        # --- Band 4 (subtopic_3): demand, supply and equilibrium ---
        self.next_band(4)
        b4t = Tex("Demand, supply and equilibrium").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        O4 = band_shift(4) + DOWN * 2.6 + LEFT * 4.6

        def P4(x, y):
            return O4 + RIGHT * x + UP * y

        ax4x = Arrow(P4(0, 0), P4(7.0, 0), buff=0, stroke_width=3)
        ax4y = Arrow(P4(0, 0), P4(0, 4.4), buff=0, stroke_width=3)
        l4x = Tex("Q").scale(0.8).move_to(P4(6.8, -0.4))
        l4y = Tex("P").scale(0.8).move_to(P4(-0.5, 4.1))
        self.play(Create(ax4x), Create(ax4y))
        self.play(Write(l4x), Write(l4y))
        self.wait(1.5)
        dem = VGroup(
            Line(P4(0.7, 3.8), P4(3.0, 2.0), color=ORANGE, stroke_width=5),
            Line(P4(3.0, 2.0), P4(5.6, 0.5), color=ORANGE, stroke_width=5),
        )
        t_d = Tex("D", color=ORANGE).scale(0.9).move_to(P4(6.0, 0.9))
        self.play(Create(dem[0]), Create(dem[1]), Write(t_d))
        self.wait(2)
        sup = VGroup(
            Line(P4(0.7, 0.5), P4(3.0, 2.0), color=BLUE, stroke_width=5),
            Line(P4(3.0, 2.0), P4(5.6, 3.8), color=BLUE, stroke_width=5),
        )
        t_s = Tex("S", color=BLUE).scale(0.9).move_to(P4(6.0, 3.6))
        self.play(Create(sup[0]), Create(sup[1]), Write(t_s))
        self.wait(2)
        eq = Dot(P4(3.0, 2.0), color=GREEN)
        t_e = Tex("equilibrium: no queue, no pile", color=GREEN).scale(0.7).move_to(P4(3.4, 4.2))
        self.play(FadeIn(eq), Write(t_e))
        self.wait(3)

        # --- Band 5 (subtopic_3): movement vs shift, drought in four steps ---
        self.next_band(5)
        b5t = Tex("Movement along vs shift of the curve").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5wrong = Tex("A price change shifts the product's own curve").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5wrong))
        self.play(Create(strike(b5wrong)))
        self.wait(2)
        b5a = Tex("Price moves you ALONG; everything else shifts").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5a))
        self.play(Create(SurroundingRectangle(b5a, color=GREEN)))
        self.wait(2)
        b5b = Tex("Drought in four steps:").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5b))
        b5c = Tex("1. supply shifts LEFT $\\;$ 2. excess demand at old price").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        b5d = Tex("3. shortage bids price UP $\\;$ 4. new equilibrium:").scale(0.95).shift(band_shift(5) + DOWN * 2.4)
        b5e = Tex("higher price, lower quantity").scale(0.95).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5c))
        self.wait(2)
        self.play(Write(b5d))
        self.play(Write(b5e))
        self.wait(3)

        # --- Band 6 (subtopic_4): utility, value, price; market types ---
        self.next_band(6)
        b6t = Tex("Utility, value, price — and market types").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("Utility: satisfaction $\\cdot$ Value: utility $+$ scarcity").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6b = Tex("Price: value expressed in money").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6a))
        self.wait(2)
        self.play(Write(b6b))
        self.wait(2)
        b6c = Tex("Water: essential, abundant, cheap;").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6c2 = Tex("diamonds: trivial, scarce, dear").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6c))
        self.play(Write(b6c2))
        self.wait(2)
        b6d = Tex("Perfect: many sellers, identical goods, free entry").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        b6e = Tex("Imperfect: monopoly (1), oligopoly (few)").scale(0.95).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6d))
        self.wait(2)
        self.play(Write(b6e))
        self.wait(3)

        # --- Band 7 (subtopic_4): the business cycle wave ---
        self.next_band(7)
        b7t = Tex("The business cycle — four phases").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        O7 = band_shift(7) + DOWN * 0.4 + LEFT * 5.6

        def P7(x, y):
            return O7 + RIGHT * x + UP * y

        base = Line(P7(0, 0), P7(11.0, 0), stroke_width=2)
        self.play(Create(base))
        wave = VGroup(
            Line(P7(0.4, -1.2), P7(2.6, 1.2), color=BLUE, stroke_width=5),
            Line(P7(2.6, 1.2), P7(4.6, 1.6), color=BLUE, stroke_width=5),
            Line(P7(4.6, 1.6), P7(7.2, -1.2), color=BLUE, stroke_width=5),
            Line(P7(7.2, -1.2), P7(8.6, -1.5), color=BLUE, stroke_width=5),
            Line(P7(8.6, -1.5), P7(10.6, 1.0), color=BLUE, stroke_width=5),
        )
        t_rec = Tex("recovery").scale(0.7).move_to(P7(1.0, 0.8))
        t_pro = Tex("prosperity").scale(0.7).move_to(P7(3.6, 2.1))
        t_res = Tex("recession").scale(0.7).move_to(P7(6.6, 0.5))
        t_dep = Tex("depression").scale(0.7).move_to(P7(8.0, -2.0))
        self.play(Create(wave[0]), Write(t_rec))
        self.wait(1.5)
        self.play(Create(wave[1]), Write(t_pro))
        self.wait(1.5)
        self.play(Create(wave[2]), Write(t_res))
        self.wait(1.5)
        self.play(Create(wave[3]), Write(t_dep))
        self.play(Create(wave[4]))
        self.wait(2)
        b7a = Tex("Leading: headlights $\\cdot$ coincident: speedometer").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        b7b = Tex("lagging (unemployment): rearview mirror").scale(0.95).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7a))
        self.play(Write(b7b))
        self.wait(3)

        # ===================== Part 2 — Simplifier =====================
        # --- Band 8 (subtopic_5): one wallet, three questions ---
        self.next_band(8)
        b8t = Tex("One wallet, three questions").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("R400 in the wallet, R600 on the list —").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8a2 = Tex("the gap is permanent: there is only choosing").scale(1.05).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8a))
        self.play(Write(b8a2))
        self.wait(2.5)
        b8b = Tex("The price tag behind the price tag:").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8b2 = Tex("only the best thing forgone counts").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8b))
        self.play(Write(b8b2))
        self.wait(2.5)
        b8c = Tex("The oven: on the curve — fully used; inside — idle;").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        b8c2 = Tex("bigger oven — the whole curve moves out: growth").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8c))
        self.play(Write(b8c2))
        self.play(Create(SurroundingRectangle(b8c2, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the circle of money on one street ---
        self.next_band(9)
        b9t = Tex("The circle of money on one street").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Factory pays wages $\\rightarrow$ spaza and salon $\\rightarrow$ wages again").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2)
        b9b = Tex("Drains: saving, tax, imports").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9c = Tex("Taps: investment, govt spending, exports").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9b))
        self.wait(2)
        self.play(Write(b9c))
        self.play(Create(SurroundingRectangle(VGroup(b9b, b9c), color=GREEN)))
        self.wait(2)
        b9d = Tex("Count finished things only: loaf yes, flour no").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9d))
        self.wait(2)
        b9e = Tex("GDP: made here $\\cdot$ GNI: earned by our people").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9e))
        self.wait(3)

        # --- Band 10 (subtopic_7): the cooler box and the breathing economy ---
        self.next_band(10)
        b10t = Tex("The cooler box, and the economy that breathes").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("R30: drinks sweat, pile pushes price down").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10b = Tex("R5: queue is the shortage, pulls price up").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10a))
        self.wait(2)
        self.play(Write(b10b))
        self.wait(2)
        b10c = Tex("Between them: no pile, no queue — equilibrium").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10c))
        self.play(Create(SurroundingRectangle(b10c, color=GREEN)))
        self.wait(2)
        b10d = Tex("Price moves you along; cold day or new seller").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        b10d2 = Tex("moves the whole curve").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10d))
        self.play(Write(b10d2))
        self.wait(2)
        b10e = Tex("Inhale, peak, exhale, trough — then again").scale(1.0).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10e))
        self.wait(4)
