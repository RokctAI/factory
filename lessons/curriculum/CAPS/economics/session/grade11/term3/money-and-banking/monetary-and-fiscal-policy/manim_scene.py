from manim import *

# Band-layout whiteboard scene for the session duo "Monetary and Fiscal
# Policy" (Grade 11, Term 3). One band per teaching step; the camera moves
# down and nothing is removed. Exporter-safe mobjects only; the two-driver
# boxes and the repo transmission chain are hand-built from Rectangles,
# Arrows and Tex. Band time apportioned to subtopics.json
# (210/230/220/240/180/190/180 of 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MonetaryFiscalPolicySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): two policies, two drivers ---
        title = Tex("Monetary and Fiscal Policy").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        mbox = Rectangle(width=5.6, height=2.1).shift(LEFT * 3.4 + UP * 0.6)
        m1 = Tex("MONETARY: the SARB").scale(0.85).move_to(mbox.get_center() + UP * 0.6)
        m2 = Tex("repo rate; independent;").scale(0.75).move_to(mbox.get_center() + DOWN * 0.05)
        m3 = Tex(r"target band 3--6\%").scale(0.75).move_to(mbox.get_center() + DOWN * 0.65)
        self.play(Create(mbox), Write(m1))
        self.play(Write(m2), Write(m3))
        self.wait(2.5)
        fbox = Rectangle(width=5.6, height=2.1).shift(RIGHT * 3.4 + UP * 0.6)
        f1 = Tex("FISCAL: the Minister of Finance").scale(0.8).move_to(fbox.get_center() + UP * 0.6)
        f2 = Tex("government spending; taxation;").scale(0.75).move_to(fbox.get_center() + DOWN * 0.05)
        f3 = Tex("the annual Budget").scale(0.75).move_to(fbox.get_center() + DOWN * 0.65)
        self.play(Create(fbox), Write(f1))
        self.play(Write(f2), Write(f3))
        self.wait(2.5)
        test = Tex(r"The sorting test: WHOSE HAND is on the instrument?").scale(1.0).shift(DOWN * 1.2)
        self.play(Write(test))
        self.play(Create(SurroundingRectangle(test, color=GREEN)))
        self.wait(2.5)
        lab = Tex("Speeds spending up: EXPANSIONARY. Slows it: CONTRACTIONARY.").scale(0.8).shift(DOWN * 2.3)
        self.play(Write(lab))
        self.wait(3)

        # --- Band 1 (subtopic_2): the repo rate and the transmission chain ---
        self.next_band(1)
        b1_title = Tex(r"Inflation above 6\%: the SARB raises the REPO rate").scale(1.0).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(2)
        c1 = Tex("1. Repo up: banks pay more to borrow from the SARB").scale(0.85).shift(band_shift(1) + UP * 1.6)
        c2 = Tex("2. Banks raise their PRIME lending rate").scale(0.85).shift(band_shift(1) + UP * 0.75)
        c3 = Tex("3. Home loans, car finance, cards all cost more").scale(0.85).shift(band_shift(1) + DOWN * 0.1)
        c4 = Tex("4. Households and firms cut back and postpone").scale(0.85).shift(band_shift(1) + DOWN * 0.95)
        c5 = Tex("5. Aggregate demand slows: inflation drifts back to band").scale(0.85).shift(band_shift(1) + DOWN * 1.8)
        prev = None
        for m in (c1, c2, c3, c4, c5):
            self.play(Write(m))
            if prev is not None:
                self.play(Create(Arrow(prev.get_bottom() + DOWN * 0.02, m.get_top() + UP * 0.02,
                                       buff=0.05, stroke_width=3, max_tip_length_to_length_ratio=0.4)))
            prev = m
            self.wait(1.6)
        c6 = Tex("Contractionary — and it cools growth and jobs too").scale(0.85).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(c6))
        self.play(Create(SurroundingRectangle(c5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_3): the minister's two instruments ---
        self.next_band(2)
        b2_title = Tex("The Minister's toolbox: two fiscal instruments").scale(1.05).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        g1 = Tex("1. Government spending: salaries, grants, roads").scale(0.95).shift(band_shift(2) + UP * 1.3)
        g2 = Tex(r"Cut its growth $\Rightarrow$ less demand $\Rightarrow$ contractionary").scale(0.9).shift(band_shift(2) + UP * 0.4)
        self.play(Write(g1))
        self.wait(2)
        self.play(Write(g2))
        self.wait(2.5)
        g3 = Tex("2. Taxation: income tax, company tax, VAT, excise").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        g4 = Tex(r"Raise taxes $\Rightarrow$ less in pockets $\Rightarrow$ contractionary").scale(0.9).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(g3))
        self.wait(2)
        self.play(Write(g4))
        self.wait(2.5)
        g5 = Tex("Reverse gear: more spending, lower taxes — expansionary").scale(0.85).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(g5))
        self.wait(3)

        # --- Band 3 (subtopic_3): classify the scenario + the trap ---
        self.next_band(3)
        b3_title = Tex("Classify the whole scenario").scale(1.15).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        k1 = Tex("SARB raises repo: contractionary MONETARY").scale(0.95).shift(band_shift(3) + UP * 1.3)
        k2 = Tex("Government cuts spending: contractionary FISCAL").scale(0.95).shift(band_shift(3) + UP * 0.4)
        k3 = Tex("Government raises taxes: contractionary FISCAL").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(k1))
        self.wait(2)
        self.play(Write(k2))
        self.wait(2)
        self.play(Write(k3))
        self.play(Create(SurroundingRectangle(VGroup(k1, k2, k3), color=GREEN)))
        self.wait(2.5)
        k4 = Tex(r"``The Minister of Finance raises the repo rate''").scale(0.95).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(k4))
        self.play(Create(strike(k4)))
        self.wait(1.5)
        k5 = Tex("The SARB controls the repo rate — wrong hand, no marks").scale(0.9).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(k5))
        self.wait(3)

        # --- Band 4 (subtopic_4): comparing the two policies ---
        self.next_band(4)
        b4_title = Tex("Side by side: the comparison the exam loves").scale(1.05).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        p1 = Tex("Monetary: FAST but BLUNT — MPC meets every two").scale(0.9).shift(band_shift(4) + UP * 1.3)
        p1b = Tex("months, but the repo hits every borrower at once").scale(0.9).shift(band_shift(4) + UP * 0.5)
        self.play(Write(p1))
        self.play(Write(p1b))
        self.wait(2.5)
        p2 = Tex("Fiscal: SLOW but AIMED — one Budget a year,").scale(0.9).shift(band_shift(4) + DOWN * 0.4)
        p2b = Tex("but a tax or a project can be targeted precisely").scale(0.9).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(p2))
        self.play(Write(p2b))
        self.wait(2.5)
        p3 = Tex("Repo bites borrowers first — every policy has").scale(0.9).shift(band_shift(4) + DOWN * 2.1)
        p3b = Tex("a distributional edge: say who carries it").scale(0.9).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(p3))
        self.play(Write(p3b))
        self.wait(3)

        # --- Band 5 (subtopic_4): pulling together + the five-step routine ---
        self.next_band(5)
        b5_title = Tex("Together or apart — and the routine").scale(1.1).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        r1 = Tex("Both contractionary: inflation falls fastest").scale(0.95).shift(band_shift(5) + UP * 1.4)
        r2 = Tex("SARB tightens while treasury spends freely:").scale(0.95).shift(band_shift(5) + UP * 0.55)
        r2b = Tex("they fight — the SARB must tighten harder").scale(0.95).shift(band_shift(5) + DOWN * 0.25)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.play(Write(r2b))
        self.wait(2.5)
        r3 = Tex("Routine: 1 name the problem; 2 name the driver;").scale(0.9).shift(band_shift(5) + DOWN * 1.2)
        r4 = Tex("3 name the instrument; 4 classify the direction;").scale(0.9).shift(band_shift(5) + DOWN * 2.0)
        r5 = Tex("5 walk the transmission chain to prices").scale(0.9).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(r3))
        self.wait(1.8)
        self.play(Write(r4))
        self.wait(1.8)
        self.play(Write(r5))
        self.play(Create(SurroundingRectangle(VGroup(r3, r4, r5), color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): two steering wheels, one balloon ---
        self.next_band(6)
        b6_title = Tex("Two drivers, two steering wheels").scale(1.15).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(2)
        s1 = Tex("SARB: sets the PRICE OF BORROWING — spends nothing,").scale(0.85).shift(band_shift(6) + UP * 1.4)
        s1b = Tex(r"builds nothing, guards the band of 3 to 6\%").scale(0.85).shift(band_shift(6) + UP * 0.6)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.wait(2.5)
        s2 = Tex("Minister: the country's HOUSEHOLD BUDGET —").scale(0.85).shift(band_shift(6) + DOWN * 0.3)
        s2b = Tex("teachers, grants, clinics in; tax and VAT collected").scale(0.85).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(s2))
        self.play(Write(s2b))
        self.wait(2.5)
        s3 = Tex("The economy is a balloon of spending:").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        s3b = Tex("air in $=$ expansionary; air out $=$ contractionary").scale(0.9).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(s3))
        self.play(Write(s3b))
        self.play(Create(SurroundingRectangle(s3b, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_6): one number in Pretoria, your street ---
        self.next_band(7)
        b7_title = Tex("How one number in Pretoria reaches your street").scale(1.0).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(2)
        t1 = Tex("Repo up: banks' own borrowing gets dearer").scale(0.9).shift(band_shift(7) + UP * 1.4)
        t2 = Tex("Prime up: banks pass it straight on").scale(0.9).shift(band_shift(7) + UP * 0.55)
        t3 = Tex("The bond, the car instalment, the store card rise").scale(0.9).shift(band_shift(7) + DOWN * 0.3)
        t4 = Tex("The lounge suite waits; the second workshop waits").scale(0.9).shift(band_shift(7) + DOWN * 1.15)
        t5 = Tex("Less money chasing goods: price rises slow down").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        for m in (t1, t2, t3, t4, t5):
            self.play(Write(m))
            self.wait(1.8)
        t6 = Tex("Choosing between two pains — not magic").scale(0.9).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(t6))
        self.wait(3)

        # --- Band 8 (subtopic_7): the Budget's two taps ---
        self.next_band(8)
        b8_title = Tex("The Budget's two taps: fast tool, slow tool").scale(1.05).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        u1 = Tex("Tap 1 spending: down to cool prices, up in recession").scale(0.85).shift(band_shift(8) + UP * 1.4)
        u2 = Tex("Tap 2 taxes: up to calm spending, down to revive it").scale(0.85).shift(band_shift(8) + UP * 0.55)
        self.play(Write(u1))
        self.wait(2)
        self.play(Write(u2))
        self.wait(2)
        u3 = Tex(r"``The Minister raises the repo rate to fight inflation''").scale(0.85).shift(band_shift(8) + DOWN * 0.35)
        self.play(Write(u3))
        self.play(Create(strike(u3)))
        self.wait(1.5)
        u4 = Tex("Wrong hand on the lever — that IS the answer").scale(0.9).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(u4))
        self.wait(2)
        u5 = Tex("Monetary fast but blunt; fiscal slow but aimed").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(u5))
        self.play(Create(SurroundingRectangle(u5, color=GREEN)))
        self.wait(2)
        u6 = Tex("Two hands pulling together beat two hands fighting").scale(0.85).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(u6))
        self.wait(4)
