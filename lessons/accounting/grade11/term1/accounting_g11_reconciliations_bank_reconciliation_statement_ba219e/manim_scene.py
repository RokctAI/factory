from manim import *

class BankReconciliationScene(Scene):
    def construct(self):
        # SUBTOPIC 1: Welcome and Introduction
        title = Text("Bank Reconciliation Statement", font_size=40, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        rule = Text("Numbers Never Lie.", font_size=30, slant=ITALIC)
        rule.next_to(title, DOWN)
        self.play(FadeIn(rule))
        self.wait(2)
        self.play(FadeOut(rule))

        # SUBTOPIC 2: Drawing the Skeleton and the Bank Balance
        # Draw Skeleton
        v_line1 = Line(UP*2, DOWN*3).shift(LEFT*2)
        v_line2 = Line(UP*2, DOWN*3).shift(RIGHT*2)
        h_line1 = Line(LEFT*5, RIGHT*4).shift(UP*2)
        h_line2 = Line(LEFT*5, RIGHT*4).shift(UP*1.2)

        heading_details = Text("Details", font_size=24).move_to(LEFT*3.5 + UP*1.6)
        heading_debit = Text("Debit (R)", font_size=24).move_to(ORIGIN + UP*1.6)
        heading_credit = Text("Credit (R)", font_size=24).move_to(RIGHT*3 + UP*1.6)

        self.play(Create(h_line1), Create(h_line2), Create(v_line1), Create(v_line2))
        self.play(Write(heading_details), Write(heading_debit), Write(heading_credit))
        self.wait(1)

        # Post Bank Balance
        detail_balance = Text("Credit balance as per Bank Statement", font_size=20).next_to(LEFT*5 + UP*0.8, RIGHT)
        val_balance = Text("5 320", font_size=20).move_to(RIGHT*3 + UP*0.8)

        self.play(Write(detail_balance))
        self.wait(1)
        self.play(Write(val_balance))
        self.wait(2)

        # SUBTOPIC 3: Outstanding Items
        # Outstanding deposit
        detail_dep = Text("Credit outstanding deposit", font_size=20).next_to(LEFT*5 + UP*0.2, RIGHT)
        val_dep = Text("2 100", font_size=20).move_to(RIGHT*3 + UP*0.2)

        self.play(Write(detail_dep))
        self.wait(1)
        self.play(Write(val_dep))
        self.wait(2)

        # Outstanding cheques
        detail_chq = Text("Debit outstanding cheques:", font_size=20).next_to(LEFT*5 + DOWN*0.4, RIGHT)
        detail_chq1 = Text("No. 411", font_size=20).next_to(LEFT*4.5 + DOWN*1.0, RIGHT)
        val_chq1 = Text("1 480", font_size=20).move_to(ORIGIN + DOWN*1.0)
        detail_chq2 = Text("No. 415", font_size=20).next_to(LEFT*4.5 + DOWN*1.6, RIGHT)
        val_chq2 = Text("650", font_size=20).move_to(ORIGIN + DOWN*1.6)

        self.play(Write(detail_chq))
        self.wait(1)
        self.play(Write(detail_chq1), Write(val_chq1))
        self.wait(1)
        self.play(Write(detail_chq2), Write(val_chq2))
        self.wait(2)

        # SUBTOPIC 4: Balancing and Conclusion
        h_line_total_top = Line(LEFT*5, RIGHT*4).shift(DOWN*2.2)

        detail_ledger = Text("Debit balance as per Bank Account", font_size=20).next_to(LEFT*5 + DOWN*2.6, RIGHT)
        val_ledger = Text("5 290", font_size=20).move_to(ORIGIN + DOWN*2.6)

        self.play(Create(h_line_total_top))
        self.wait(1)

        self.play(Write(detail_ledger))
        self.wait(1)
        self.play(Write(val_ledger))
        self.wait(1)

        h_line_total_bot1 = Line(LEFT*5, RIGHT*4).shift(DOWN*3.0)
        h_line_total_bot2 = Line(LEFT*5, RIGHT*4).shift(DOWN*3.1)

        val_tot_deb = Text("7 420", font_size=20).move_to(ORIGIN + DOWN*3.4)
        val_tot_cred = Text("7 420", font_size=20).move_to(RIGHT*3 + DOWN*3.4)

        self.play(Create(h_line_total_bot1), Create(h_line_total_bot2))
        self.play(Write(val_tot_deb), Write(val_tot_cred))
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)
