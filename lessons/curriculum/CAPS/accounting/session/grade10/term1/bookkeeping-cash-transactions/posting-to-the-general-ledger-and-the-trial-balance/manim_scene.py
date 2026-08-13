from manim import *

# Band-layout whiteboard scene for posting to the general ledger + trial
# balance session duo. Exporter-safe primitives only; write-only reveals.
# Band time follows subtopics.json (180/210/190/200/160/190/190 of 1320 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PostingAndTrialBalanceSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(15)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the ledger's architecture ---
        title = Tex("The General Ledger and the Trial Balance").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        # A T-account skeleton
        t_top = Line(LEFT * 2.8 + UP * 1.2, RIGHT * 2.8 + UP * 1.2, stroke_width=4)
        t_stem = Line(UP * 1.2, DOWN * 0.4, stroke_width=4)
        self.play(Create(t_top), Create(t_stem))
        t_dr = Tex("Debit").scale(0.95).move_to([-1.5, 0.7, 0])
        t_cr = Tex("Credit").scale(0.95).move_to([1.5, 0.7, 0])
        self.play(Write(t_dr), Write(t_cr)); self.wait(2)
        l01 = Tex("One account per item — all its movements").scale(1.0).shift(DOWN * 1.1)
        self.play(Write(l01)); self.wait(2)
        l02 = Tex("Balance sheet section: A, O, L accounts").scale(1.0).shift(DOWN * 2.0)
        l03 = Tex("Nominal section: incomes and expenses").scale(1.0).shift(DOWN * 2.8)
        self.play(Write(l02)); self.wait(1.5)
        self.play(Write(l03))
        self.wait(3)

        # --- Band 1 (subtopic_1): folios; totals post ---
        self.next_band(1)
        b1_t = Tex("Folios and the posting discipline").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_t)); self.wait(1.5)
        b1_l1 = Tex("Folio in the ledger: which journal page").scale(1.05).shift(band_shift(1) + UP * 1.3)
        b1_l2 = Tex("(CRJ 1, CPJ 1) the amount came from").scale(1.05).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l1)); self.play(Write(b1_l2)); self.wait(2.5)
        b1_l3 = Tex("Any amount can be traced both ways").scale(1.05).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1_l3)); self.wait(2)
        b1_l4 = Tex("TOTALS post, not lines —").scale(1.1).shift(band_shift(1) + DOWN * 1.5)
        b1_l5 = Tex("only sundry items post by name").scale(1.05).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_l4)); self.wait(1.5)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): posting the CRJ ---
        self.next_band(2)
        b2_t = Tex("Posting the CRJ").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_t)); self.wait(1.5)
        b2_l1 = Tex("Bank total: DEBIT Bank R56 900").scale(1.05).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("Sales total: CREDIT Sales R4 500").scale(1.05).shift(band_shift(2) + UP * 0.6)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Write(b2_l2)); self.wait(2)
        b2_l3 = Tex("Cost of Sales R3 600 posts TWICE:").scale(1.05).shift(band_shift(2) + DOWN * 0.3)
        b2_l4 = Tex("DEBIT Cost of Sales; CREDIT Trading Stock").scale(1.0).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l3)); self.wait(1.5)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)
        b2_l5 = Tex("Sundries by name: CREDIT Capital R50 000;").scale(0.95).shift(band_shift(2) + DOWN * 2.1)
        b2_l6 = Tex("CREDIT Rent Income R2 400").scale(1.0).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l5)); self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): auditing the CRJ's double entry ---
        self.next_band(3)
        b3_t = Tex("Audit the month's double entry").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_t)); self.wait(1.5)
        b3_wrong = Tex("Trading Stock's credit partners Bank").scale(1.05).shift(band_shift(3) + UP * 1.3)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l1 = Tex("It partners the Cost of Sales DEBIT").scale(1.05).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1)); self.wait(2)
        b3_l2 = MathTex(r"\text{Debits: } 56\,900 + 3\,600 = 60\,500").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        b3_l3 = MathTex(r"\text{Credits: } 4\,500 + 50\,000 + 2\,400 + 3\,600").scale(0.95).shift(band_shift(3) + DOWN * 1.5)
        b3_l4 = MathTex(r"= 60\,500\ \checkmark").scale(1.1).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l2)); self.wait(2)
        self.play(Write(b3_l3)); self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): posting the CPJ ---
        self.next_band(4)
        b4_t = Tex("Posting the CPJ").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_t)); self.wait(1.5)
        b4_l1 = Tex("Bank total: CREDIT Bank R22 500").scale(1.05).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("DEBIT Trading Stock R8 000; Wages R3 000").scale(1.0).shift(band_shift(4) + UP * 0.6)
        self.play(Write(b4_l1)); self.wait(2)
        self.play(Write(b4_l2)); self.wait(2)
        b4_l3 = Tex("Sundries, all debits: Rent Expense R3 500;").scale(0.95).shift(band_shift(4) + DOWN * 0.3)
        b4_l4 = Tex("Equipment R6 000; Drawings R2 000").scale(1.0).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l3)); self.play(Write(b4_l4)); self.wait(2.5)
        b4_l5 = MathTex(r"8\,000 + 3\,000 + 3\,500 + 6\,000 + 2\,000").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        b4_l6 = MathTex(r"= 22\,500\ \checkmark").scale(1.1).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l5)); self.wait(1.5)
        self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l6, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): balancing the Bank account ---
        self.next_band(5)
        b5_t = Tex("Balancing Bank").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_t)); self.wait(1.5)
        # Bank T-account with figures
        t_top = Line(LEFT * 3.4 + UP * 1.5, RIGHT * 3.4 + UP * 1.5,
                     stroke_width=4).shift(band_shift(5))
        t_stem = Line(UP * 1.5, DOWN * 1.2, stroke_width=4).shift(band_shift(5))
        self.play(Create(t_top), Create(t_stem))
        t_dr = Tex("56 900").scale(1.0).move_to([-1.7, 0.9, 0]).shift(band_shift(5))
        t_cr = Tex("22 500").scale(1.0).move_to([1.7, 0.9, 0]).shift(band_shift(5))
        self.play(Write(t_dr)); self.wait(1.5)
        self.play(Write(t_cr)); self.wait(1.5)
        t_cd = Tex("Balance c/d 34 400").scale(0.9).move_to([1.9, 0.0, 0]).shift(band_shift(5))
        t_bd = Tex("Balance b/d 34 400").scale(0.9).move_to([-1.9, -0.8, 0]).shift(band_shift(5))
        self.play(Write(t_cd)); self.wait(2)
        self.play(Write(t_bd))
        self.play(Create(SurroundingRectangle(t_bd, color=GREEN)))
        self.wait(2.5)
        b5_l1 = Tex("Trading Stock: 8 000 $-$ 3 600 = R4 400 debit").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        b5_l2 = Tex("Nominal accounts are not balanced monthly").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2))
        self.wait(3)

        # --- Band 6 (subtopic_4): the trial balance ---
        self.next_band(6)
        b6_t = Tex("The trial balance").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_t)); self.wait(1.5)
        mid = Line(UP * 1.7, DOWN * 2.0, stroke_width=3).shift(band_shift(6))
        self.play(Create(mid))
        b6_dh = Tex("Debits").scale(1.0).move_to([-3.0, 1.4, 0]).shift(band_shift(6))
        b6_ch = Tex("Credits").scale(1.0).move_to([3.0, 1.4, 0]).shift(band_shift(6))
        self.play(Write(b6_dh), Write(b6_ch)); self.wait(1.5)
        b6_d1 = Tex("Bank 34 400; Stock 4 400").scale(0.9).move_to([-3.0, 0.7, 0]).shift(band_shift(6))
        b6_d2 = Tex("Equipment 6 000; Drawings 2 000").scale(0.9).move_to([-3.0, 0.0, 0]).shift(band_shift(6))
        b6_d3 = Tex("CoS 3 600; Wages 3 000").scale(0.9).move_to([-3.0, -0.7, 0]).shift(band_shift(6))
        b6_d4 = Tex("Rent Expense 3 500").scale(0.9).move_to([-3.0, -1.4, 0]).shift(band_shift(6))
        b6_c1 = Tex("Capital 50 000").scale(0.9).move_to([3.0, 0.7, 0]).shift(band_shift(6))
        b6_c2 = Tex("Sales 4 500").scale(0.9).move_to([3.0, 0.0, 0]).shift(band_shift(6))
        b6_c3 = Tex("Rent Income 2 400").scale(0.9).move_to([3.0, -0.7, 0]).shift(band_shift(6))
        self.play(Write(b6_d1)); self.play(Write(b6_d2))
        self.play(Write(b6_d3)); self.play(Write(b6_d4)); self.wait(1.5)
        self.play(Write(b6_c1)); self.play(Write(b6_c2)); self.play(Write(b6_c3))
        self.wait(2)
        b6_tot = MathTex(r"56\,900 = 56\,900\ \checkmark").scale(1.15).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_tot))
        self.play(Create(SurroundingRectangle(b6_tot, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): what it proves; hunting differences ---
        self.next_band(7)
        b7_t = Tex("What the trial balance proves").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_t)); self.wait(1.5)
        b7_l1 = Tex("Proves ARITHMETIC equality only").scale(1.05).shift(band_shift(7) + UP * 1.4)
        self.play(Write(b7_l1)); self.wait(2)
        b7_wrong = Tex("It balances, so the books are correct").scale(1.05).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(2)
        b7_l2 = Tex("Wrong account, right side: still balances").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        b7_l3 = Tex("Whole transaction left out: still balances").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l2)); self.wait(1.5)
        self.play(Write(b7_l3)); self.wait(2)
        b7_l4 = Tex("Difference = an amount: posted once only").scale(0.95).shift(band_shift(7) + DOWN * 2.1)
        b7_l5 = Tex("Divisible by 2: wrong side; by 9: transposed").scale(0.95).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l4)); self.wait(1.5)
        self.play(Write(b7_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the filing cabinet ---
        self.next_band(8)
        b8_t = Tex("The filing cabinet").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("Diaries = sorting room: what happened, in order").scale(0.95).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex("Cabinet = one drawer per THING").scale(1.05).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1)); self.wait(2)
        self.play(Write(b8_l2)); self.wait(2)
        b8_l3 = Tex("Posting = carry each total to its drawer,").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex("drop it on the growing side, note the source").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l3)); self.play(Write(b8_l4)); self.wait(2.5)
        b8_l5 = Tex("CRJ 1 / CPJ 1 = return tickets for auditing").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): one month comes home ---
        self.next_band(9)
        b9_t = Tex("One month comes home").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_t)); self.wait(2)
        b9_l1 = Tex("In: Bank left 56 900; Sales right 4 500;").scale(0.95).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex("CoS left 3 600 with Stock right 3 600;").scale(0.95).shift(band_shift(9) + UP * 0.5)
        b9_l3 = Tex("Capital right 50 000; Rent Income right 2 400").scale(0.95).shift(band_shift(9) + DOWN * 0.3)
        self.play(Write(b9_l1)); self.wait(1.5)
        self.play(Write(b9_l2)); self.wait(1.5)
        self.play(Write(b9_l3)); self.wait(2)
        b9_l4 = Tex("Out: Bank right 22 500; Stock left 8 000;").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        b9_l5 = Tex("Wages, Rent, Equipment, Drawings — left").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l4)); self.play(Write(b9_l5)); self.wait(2)
        b9_l6 = MathTex(r"\text{Bank: } 56\,900 - 22\,500 = \text{R34 400}").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the weigh-in ---
        self.next_band(10)
        b10_t = Tex("The weigh-in").scale(1.2).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_t)); self.wait(2)
        b10_l1 = Tex("Lefts: 34 400 + 4 400 + 6 000 + 2 000").scale(1.0).shift(band_shift(10) + UP * 1.3)
        b10_l2 = Tex("+ 3 600 + 3 000 + 3 500 = 56 900").scale(1.0).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l1)); self.play(Write(b10_l2)); self.wait(2.5)
        b10_l3 = MathTex(r"\text{Rights: } 50\,000 + 4\,500 + 2\,400 = 56\,900\ \checkmark").scale(0.88).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex("Level scales test the WEIGHING, not the FILING").scale(0.95).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(b10_l4)); self.wait(2)
        b10_l5 = Tex("Gap = amount: dropped once; halves: wrong").scale(0.95).shift(band_shift(10) + DOWN * 2.3)
        b10_l6 = Tex("side; divisible by 9: digits swapped").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l5)); self.play(Write(b10_l6))
        self.wait(4)
