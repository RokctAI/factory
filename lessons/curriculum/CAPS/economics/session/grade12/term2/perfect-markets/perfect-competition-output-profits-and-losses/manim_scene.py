from manim import *

# Band-layout whiteboard scene for the perfect-competition session duo.
# Part 1 (Expert): subtopics 1-4; Part 2 (Simplifier): subtopics 5-7.
# Subtopic durations 230/260/255/230/190/195/200 of 1560 s — band dwell
# times are apportioned to match. All diagrams are hand-built from
# exporter-safe primitives (Arrow/Line/Dot/Rectangle/Tex only).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def axes(origin, w, h, xlab, ylab):
    """Two arrows + labels; the exporter has no Axes support."""
    xa = Arrow(origin, origin + RIGHT * w, buff=0, stroke_width=3)
    ya = Arrow(origin, origin + UP * h, buff=0, stroke_width=3)
    xl = Tex(xlab).scale(0.9).next_to(origin + RIGHT * w, DOWN, buff=0.2)
    yl = Tex(ylab).scale(0.9).next_to(origin + UP * h, LEFT, buff=0.2)
    return VGroup(xa, ya, xl, yl)


def chain(origin, pts, color=WHITE, sw=5):
    """Polyline curve: short Line segments, exporter-safe."""
    g = VGroup()
    for a, b in zip(pts[:-1], pts[1:]):
        g.add(Line(origin + RIGHT * a[0] + UP * a[1],
                   origin + RIGHT * b[0] + UP * b[1],
                   color=color, stroke_width=sw))
    return g


class PerfectCompetitionOutputProfitsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the five assumptions ---
        title = Tex("Perfect Competition: Output, Profit, Loss").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        a_head = Tex("Five assumptions (a mark each):").scale(1.1).shift(UP * 1.5)
        self.play(Write(a_head))
        self.wait(1.5)
        a1 = Tex("1. Very many small buyers and sellers").scale(1.05).shift(UP * 0.7)
        a2 = Tex("2. Homogeneous product — every unit identical").scale(1.05).shift(DOWN * 0.1)
        a3 = Tex("3. Free entry and exit — no barriers").scale(1.05).shift(DOWN * 0.9)
        a4 = Tex("4. Perfect knowledge of all prices").scale(1.05).shift(DOWN * 1.7)
        a5 = Tex("5. Mobile factors; no collusion").scale(1.05).shift(DOWN * 2.5)
        for m in (a1, a2, a3, a4, a5):
            self.play(Write(m))
            self.wait(1.5)
        self.wait(2)

        # --- Band 1 (subtopic_1): industry sets the price, business takes it ---
        self.next_band(1)
        b1_title = Tex("Industry sets the price; business takes it").scale(1.15).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        o1 = band_shift(1) + LEFT * 5.6 + DOWN * 2.3
        ax1 = axes(o1, 4.6, 3.8, "Q", "P")
        lab1 = Tex("Industry").scale(1.0).shift(band_shift(1) + LEFT * 3.4 + UP * 1.9)
        self.play(Create(ax1), Write(lab1))
        self.wait(1)
        dcurve = chain(o1, [(0.5, 3.2), (2.2, 1.9), (3.9, 1.0)], color=BLUE)
        dl = Tex("D").scale(0.9).next_to(o1 + RIGHT * 3.9 + UP * 1.0, RIGHT, buff=0.15)
        self.play(Create(dcurve), Write(dl))
        self.wait(1)
        scurve = chain(o1, [(0.5, 0.8), (2.2, 1.9), (3.9, 3.1)], color=YELLOW)
        sl = Tex("S").scale(0.9).next_to(o1 + RIGHT * 3.9 + UP * 3.1, RIGHT, buff=0.15)
        self.play(Create(scurve), Write(sl))
        self.wait(1)
        e_dot = Dot(o1 + RIGHT * 2.2 + UP * 1.9, color=GREEN)
        e_guide = DashedLine(o1 + UP * 1.9, o1 + RIGHT * 2.2 + UP * 1.9, stroke_width=2)
        e_lab = Tex("R10").scale(0.9).next_to(o1 + UP * 1.9, LEFT, buff=0.15)
        self.play(Create(e_guide), Create(e_dot), Write(e_lab))
        self.wait(2)
        o2 = band_shift(1) + RIGHT * 1.0 + DOWN * 2.3
        ax2 = axes(o2, 4.6, 3.8, "Q", "P")
        lab2 = Tex("One business").scale(1.0).shift(band_shift(1) + RIGHT * 3.3 + UP * 1.9)
        self.play(Create(ax2), Write(lab2))
        self.wait(1)
        flat = Line(o2 + RIGHT * 0.3 + UP * 1.9, o2 + RIGHT * 4.3 + UP * 1.9,
                    color=GREEN, stroke_width=5)
        flat_lab = MathTex(r"D = AR = MR = P").scale(1.0).shift(band_shift(1) + RIGHT * 3.3 + UP * 0.4)
        p_lab = Tex("R10").scale(0.9).next_to(o2 + UP * 1.9, LEFT, buff=0.15)
        self.play(Create(flat), Write(p_lab))
        self.wait(1.5)
        self.play(Write(flat_lab))
        taker = Tex("Price taker: only decision is quantity").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(taker))
        self.play(Create(SurroundingRectangle(flat_lab, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): cost curves and MR = MC ---
        self.next_band(2)
        b2_title = Tex("Costs under the flat revenue line").scale(1.15).shift(band_shift(2) + UP * 2.6)
        self.play(Write(b2_title))
        self.wait(1.5)
        o3 = band_shift(2) + LEFT * 4.6 + DOWN * 2.6
        ax3 = axes(o3, 8.2, 4.6, "Q", "R")
        self.play(Create(ax3))
        self.wait(1)
        mc = chain(o3, [(1.0, 2.3), (1.9, 1.4), (3.0, 1.9), (4.2, 3.4), (4.9, 4.3)], color=RED)
        mc_lab = Tex("MC").scale(0.95).next_to(o3 + RIGHT * 4.9 + UP * 4.3, RIGHT, buff=0.15)
        self.play(Create(mc), Write(mc_lab))
        self.wait(1.5)
        ac = chain(o3, [(0.8, 3.6), (2.0, 2.1), (3.0, 1.85), (4.6, 2.4), (5.8, 3.3)], color=BLUE)
        ac_lab = Tex("AC").scale(0.95).next_to(o3 + RIGHT * 5.8 + UP * 3.3, RIGHT, buff=0.15)
        self.play(Create(ac), Write(ac_lab))
        self.wait(1.5)
        cut = Tex("MC cuts AC at AC's lowest point").scale(1.0).shift(band_shift(2) + RIGHT * 2.6 + UP * 1.7)
        self.play(Write(cut))
        self.wait(2)
        price = Line(o3 + RIGHT * 0.3 + UP * 3.0, o3 + RIGHT * 7.6 + UP * 3.0,
                     color=GREEN, stroke_width=5)
        price_lab = Tex("R15").scale(0.9).next_to(o3 + UP * 3.0, LEFT, buff=0.15)
        pmr = MathTex(r"P = MR").scale(0.95).next_to(o3 + RIGHT * 7.6 + UP * 3.0, UP, buff=0.15)
        self.play(Create(price), Write(price_lab), Write(pmr))
        self.wait(1.5)
        q_dot = Dot(o3 + RIGHT * 3.9 + UP * 3.0, color=YELLOW)
        q_guide = DashedLine(o3 + RIGHT * 3.9 + UP * 3.0, o3 + RIGHT * 3.9, stroke_width=2)
        q_lab = Tex("200").scale(0.9).next_to(o3 + RIGHT * 3.9, DOWN, buff=0.15)
        self.play(Create(q_dot), Create(q_guide), Write(q_lab))
        self.wait(1.5)
        rule = MathTex(r"\text{Produce where } MR = MC \text{ (MC rising)}").scale(1.05).shift(band_shift(2) + RIGHT * 2.8 + UP * 0.6)
        self.play(Write(rule))
        self.play(Create(SurroundingRectangle(rule, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): normal vs economic profit, the calculation ---
        self.next_band(3)
        b3_title = Tex("Normal profit or economic profit?").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Normal profit is INCLUDED in the cost curves").scale(1.05).shift(band_shift(3) + UP * 1.4)
        b3_l2 = MathTex(r"P = AC: \text{ normal profit only (break-even)}").scale(1.05).shift(band_shift(3) + UP * 0.5)
        b3_l3 = MathTex(r"P > AC: \text{ economic (supernormal) profit}").scale(1.05).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"P = 15,\; AC = 12,\; Q = 200").scale(1.1).shift(band_shift(3) + DOWN * 1.4)
        b3_l5 = MathTex(r"(15 - 12) \times 200 = \text{R}600").scale(1.15).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): losses and the shut-down decision ---
        self.next_band(4)
        b4_title = Tex("Losses and the shut-down decision").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"P < AC \;\Rightarrow\; \text{economic loss}").scale(1.05).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("Fixed costs: rent, insurance — owed at zero output").scale(1.0).shift(band_shift(4) + UP * 0.5)
        b4_l3 = Tex("Variable costs: materials, wages — avoidable").scale(1.0).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = MathTex(r"P \geq AVC: \text{ produce — helps pay the rent}").scale(1.05).shift(band_shift(4) + DOWN * 1.3)
        b4_l5 = MathTex(r"P < \text{min } AVC: \text{ shut down}").scale(1.05).shift(band_shift(4) + DOWN * 2.2)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4, b4_l5):
            self.play(Write(m))
            self.wait(1.8)
        b4_l6 = Tex("Supply curve $=$ rising MC above min AVC").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l6, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the long run and the two efficiencies ---
        self.next_band(5)
        b5_title = Tex("The long run: entry and exit do the work").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Profit $\\Rightarrow$ entry $\\Rightarrow$ supply right $\\Rightarrow$ P falls").scale(1.05).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("Loss $\\Rightarrow$ exit $\\Rightarrow$ supply left $\\Rightarrow$ P rises").scale(1.05).shift(band_shift(5) + UP * 0.5)
        b5_l3 = Tex("Both end at the bottom of the AC curve").scale(1.05).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2.5)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"P = MC = \text{minimum } AC").scale(1.2).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex("Allocative ($P = MC$) + productive (min $AC$)").scale(1.0).shift(band_shift(5) + DOWN * 2.4)
        b5_l6 = Tex("efficiency — only this structure gets both").scale(1.0).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): the Competition Act's three institutions ---
        self.next_band(6)
        b6_title = Tex("Competition Act, 1998 — three institutions").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        r1 = Rectangle(width=3.6, height=1.5).shift(band_shift(6) + LEFT * 4.2 + UP * 0.6)
        r1_a = Tex("Commission").scale(1.0).shift(band_shift(6) + LEFT * 4.2 + UP * 0.9)
        r1_b = Tex("investigates").scale(0.9).shift(band_shift(6) + LEFT * 4.2 + UP * 0.3)
        self.play(Create(r1), Write(r1_a), Write(r1_b))
        self.wait(2)
        ar1 = Arrow(band_shift(6) + LEFT * 2.3 + UP * 0.6, band_shift(6) + LEFT * 1.7 + UP * 0.6, buff=0, stroke_width=4)
        r2 = Rectangle(width=3.6, height=1.5).shift(band_shift(6) + UP * 0.6)
        r2_a = Tex("Tribunal").scale(1.0).shift(band_shift(6) + UP * 0.9)
        r2_b = Tex("adjudicates").scale(0.9).shift(band_shift(6) + UP * 0.3)
        self.play(Create(ar1), Create(r2), Write(r2_a), Write(r2_b))
        self.wait(2)
        ar2 = Arrow(band_shift(6) + RIGHT * 1.7 + UP * 0.6, band_shift(6) + RIGHT * 2.3 + UP * 0.6, buff=0, stroke_width=4)
        r3 = Rectangle(width=3.6, height=1.5).shift(band_shift(6) + RIGHT * 4.2 + UP * 0.6)
        r3_a = Tex("Appeal Court").scale(1.0).shift(band_shift(6) + RIGHT * 4.2 + UP * 0.9)
        r3_b = Tex("hears appeals").scale(0.9).shift(band_shift(6) + RIGHT * 4.2 + UP * 0.3)
        self.play(Create(ar2), Create(r3), Write(r3_a), Write(r3_b))
        self.wait(2)
        b6_l1 = Tex("Tribunal can block mergers, impose conditions,").scale(1.0).shift(band_shift(6) + DOWN * 1.0)
        b6_l2 = Tex("and fine up to 10\\% of annual turnover").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): what the Act attacks, and why ---
        self.next_band(7)
        b7_title = Tex("What the Act attacks").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Horizontal: price fixing, market division,").scale(1.0).shift(band_shift(7) + UP * 1.5)
        b7_l2 = Tex("bid rigging — bread cartel, 2010 stadiums").scale(1.0).shift(band_shift(7) + UP * 0.8)
        b7_l3 = Tex("Vertical: minimum resale price maintenance").scale(1.0).shift(band_shift(7))
        b7_l4 = Tex("Abuse of dominance: predatory pricing").scale(1.0).shift(band_shift(7) + DOWN * 0.8)
        b7_l5 = Tex("Merger control — plus PUBLIC INTEREST test").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4, b7_l5):
            self.play(Write(m))
            self.wait(1.8)
        b7_l6 = Tex("Collusion turns price takers into a price MAKER").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): forty tables of tomatoes ---
        self.next_band(8)
        b8_title = Tex("Forty tables of tomatoes").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Try R12 a kilo: buyers step to the next table").scale(1.05).shift(band_shift(8) + UP * 1.4)
        self.play(Write(b8_l1))
        self.play(Create(strike(b8_l1)))
        self.wait(2)
        b8_l2 = Tex("Try R8: sells out — but threw away R2 a kilo").scale(1.05).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l2))
        self.play(Create(strike(b8_l2)))
        self.wait(2)
        b8_l3 = Tex("The street made the price R10 — no table moves it").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("R10 = her price, revenue per kilo, and").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        b8_l5 = Tex("revenue from one more kilo — three names").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(1.5)
        b8_l6 = Tex("Only decision left: HOW MANY kilos").scale(1.05).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): how many kilos — the one rule ---
        self.next_band(9)
        b9_title = Tex("How many kilos? — the one rule").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Each kilo fetches R10; each extra kilo costs more").scale(1.0).shift(band_shift(9) + UP * 1.4)
        b9_l2 = Tex("Keep adding while a kilo earns more than it costs").scale(1.0).shift(band_shift(9) + UP * 0.5)
        b9_l3 = Tex("Stop when the next kilo would cost over R10").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        for m in (b9_l1, b9_l2, b9_l3):
            self.play(Write(m))
            self.wait(2)
        b9_l4 = MathTex(r"\text{That is all } MR = MC \text{ says}").scale(1.1).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("All-in cost R9: R1/kg surplus — economic profit").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        b9_l6 = Tex("Cost R10: normal profit. Cost R11: sewing machine").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l5))
        self.wait(2)
        self.play(Write(b9_l6))
        self.wait(3)

        # --- Band 10 (subtopic_7): the street corrects itself ---
        self.next_band(10)
        b10_title = Tex("The street corrects itself").scale(1.2).shift(band_shift(10) + UP * 2.6)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Profit invites entry: 40 tables, then 50, then 60").scale(1.0).shift(band_shift(10) + UP * 1.7)
        b10_l2 = Tex("Price slips R10 toward R9 until the surplus is gone").scale(1.0).shift(band_shift(10) + UP * 0.9)
        b10_l3 = Tex("Drought year: losses, exit, price climbs back").scale(1.0).shift(band_shift(10) + UP * 0.1)
        for m in (b10_l1, b10_l2, b10_l3):
            self.play(Write(m))
            self.wait(2)
        b10_l4 = Tex("Resting point: price $=$ cheapest cost per kilo").scale(1.05).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("Sunday deal: nobody sells below R15").scale(1.0).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l5))
        self.play(Create(strike(b10_l5)))
        self.wait(1.5)
        b10_l6 = Tex("Illegal collusion — Commission investigates,").scale(1.0).shift(band_shift(10) + DOWN * 2.4)
        b10_l7 = Tex("Tribunal fines up to 10\\% of turnover").scale(1.0).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.wait(4)
