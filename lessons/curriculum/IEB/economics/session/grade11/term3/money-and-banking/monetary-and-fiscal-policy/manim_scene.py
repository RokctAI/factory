# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
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
        m2 = Tex("the repo rate; independent;").scale(0.72).move_to(mbox.get_center() + DOWN * 0.05)
        m3 = Tex(r"band: 3\% to 6\%").scale(0.75).move_to(mbox.get_center() + DOWN * 0.65)
        self.play(Create(mbox), Write(m1))
        self.play(Write(m2), Write(m3))
        self.wait(2.5)
        fbox = Rectangle(width=5.6, height=2.1).shift(RIGHT * 3.4 + UP * 0.6)
        f1 = Tex("FISCAL: the Minister of Finance").scale(0.8).move_to(fbox.get_center() + UP * 0.6)
        f2 = Tex("spending and taxation;").scale(0.75).move_to(fbox.get_center() + DOWN * 0.05)
        f3 = Tex("the annual Budget").scale(0.75).move_to(fbox.get_center() + DOWN * 0.65)
        self.play(Create(fbox), Write(f1))
        self.play(Write(f2), Write(f3))
        self.wait(2.5)
        test = Tex("The sorting question: WHOSE HAND is on the lever?").scale(1.0).shift(DOWN * 1.2)
        self.play(Write(test))
        self.play(Create(SurroundingRectangle(test, color=GREEN)))
        self.wait(2.5)
        lab = Tex("Adds spending power: EXPANSIONARY. Withdraws it: CONTRACTIONARY.").scale(0.75).shift(DOWN * 2.3)
        self.play(Write(lab))
        self.wait(3)

        # --- Band 1 (subtopic_2): the repo rate and the transmission chain ---
        self.next_band(1)
        b1_title = Tex(r"Inflation past 6\%: the SARB raises the REPO rate").scale(1.0).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(2)
        c1 = Tex("1. Repo up: the banks' own funding costs more").scale(0.85).shift(band_shift(1) + UP * 1.6)
        c2 = Tex("2. Banks lift PRIME, their benchmark lending rate").scale(0.85).shift(band_shift(1) + UP * 0.75)
        c3 = Tex("3. Bonds, vehicle finance, cards, overdrafts dearer").scale(0.85).shift(band_shift(1) + DOWN * 0.1)
        c4 = Tex("4. Households and firms hold back and postpone").scale(0.85).shift(band_shift(1) + DOWN * 0.95)
        c5 = Tex("5. Aggregate demand cools: inflation eases to the band").scale(0.85).shift(band_shift(1) + DOWN * 1.8)
        prev = None
        for m in (c1, c2, c3, c4, c5):
            self.play(Write(m))
            if prev is not None:
                self.play(Create(Arrow(prev.get_bottom() + DOWN * 0.02, m.get_top() + UP * 0.02,
                                       buff=0.05, stroke_width=3, max_tip_length_to_length_ratio=0.4)))
            prev = m
            self.wait(1.6)
        c6 = Tex("Contractionary — a medicine with side effects on jobs").scale(0.85).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(c6))
        self.play(Create(SurroundingRectangle(c5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_3): the minister's two instruments ---
        self.next_band(2)
        b2_title = Tex("The Minister's toolbox: exactly two instruments").scale(1.0).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        g1 = Tex("1. Spending: salaries, grants, roads — a river of demand").scale(0.9).shift(band_shift(2) + UP * 1.3)
        g2 = Tex(r"Narrow the river $\Rightarrow$ less demand: contractionary").scale(0.9).shift(band_shift(2) + UP * 0.4)
        self.play(Write(g1))
        self.wait(2)
        self.play(Write(g2))
        self.wait(2.5)
        g3 = Tex("2. Taxation: income tax, company tax, VAT, excise").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        g4 = Tex(r"Raise them $\Rightarrow$ shallower pockets: contractionary").scale(0.9).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(g3))
        self.wait(2)
        self.play(Write(g4))
        self.wait(2.5)
        g5 = Tex("Reverse gear: widen the river, lighten the taxes — expansionary").scale(0.8).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(g5))
        self.wait(3)

        # --- Band 3 (subtopic_3): classify the scenario + the trap ---
        self.next_band(3)
        b3_title = Tex("Classify every move in the scenario").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        k1 = Tex("SARB raises repo: contractionary MONETARY").scale(0.95).shift(band_shift(3) + UP * 1.3)
        k2 = Tex("Treasury restrains spending: contractionary FISCAL").scale(0.95).shift(band_shift(3) + UP * 0.4)
        k3 = Tex("Treasury raises taxes: contractionary FISCAL").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(k1))
        self.wait(2)
        self.play(Write(k2))
        self.wait(2)
        self.play(Write(k3))
        self.play(Create(SurroundingRectangle(VGroup(k1, k2, k3), color=GREEN)))
        self.wait(2.5)
        k4 = Tex(r"``The Minister of Finance raised the repo rate''").scale(0.95).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(k4))
        self.play(Create(strike(k4)))
        self.wait(1.5)
        k5 = Tex("Wrong hand: the repo rate is the Reserve Bank's alone").scale(0.9).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(k5))
        self.wait(3)

        # --- Band 4 (subtopic_4): comparing the two policies ---
        self.next_band(4)
        b4_title = Tex("Side by side: the master comparison").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        p1 = Tex("Monetary: FAST but BLUNT — the MPC sits every second").scale(0.85).shift(band_shift(4) + UP * 1.3)
        p1b = Tex("month, but the rate lands on every borrower alike").scale(0.85).shift(band_shift(4) + UP * 0.5)
        self.play(Write(p1))
        self.play(Write(p1b))
        self.wait(2.5)
        p2 = Tex("Fiscal: SLOW but AIMED — one Budget a year,").scale(0.9).shift(band_shift(4) + DOWN * 0.4)
        p2b = Tex("but a duty or a programme can be pointed precisely").scale(0.9).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(p2))
        self.play(Write(p2b))
        self.wait(2.5)
        p3 = Tex("The bondholder feels repo within a month — every").scale(0.9).shift(band_shift(4) + DOWN * 2.1)
        p3b = Tex("policy has weight-bearers: name who carries it").scale(0.9).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(p3))
        self.play(Write(p3b))
        self.wait(3)

        # --- Band 5 (subtopic_4): cooperation + the five-move routine ---
        self.next_band(5)
        b5_title = Tex("Cooperate or collide — then the routine").scale(1.05).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        r1 = Tex("Both tightening: inflation surrenders fastest").scale(0.95).shift(band_shift(5) + UP * 1.4)
        r2 = Tex("Bank tightens while treasury pours: collision —").scale(0.95).shift(band_shift(5) + UP * 0.55)
        r2b = Tex("the Bank must tighten further; borrowers pay").scale(0.95).shift(band_shift(5) + DOWN * 0.25)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.play(Write(r2b))
        self.wait(2.5)
        r3 = Tex("Routine: 1 the problem; 2 the driver;").scale(0.9).shift(band_shift(5) + DOWN * 1.2)
        r4 = Tex("3 the instrument; 4 direction and label;").scale(0.9).shift(band_shift(5) + DOWN * 2.0)
        r5 = Tex("5 walk the chain to spending and prices").scale(0.9).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(r3))
        self.wait(1.8)
        self.play(Write(r4))
        self.wait(1.8)
        self.play(Write(r5))
        self.play(Create(SurroundingRectangle(VGroup(r3, r4, r5), color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): two steering wheels, one fire ---
        self.next_band(6)
        b6_title = Tex("Two drivers, two steering wheels").scale(1.15).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(2)
        s1 = Tex("SARB: sets the price of borrowing — builds nothing,").scale(0.85).shift(band_shift(6) + UP * 1.4)
        s1b = Tex(r"pays no grants, guards the rand: 3\% to 6\%").scale(0.85).shift(band_shift(6) + UP * 0.6)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.wait(2.5)
        s2 = Tex("Minister: the country's household account — pay,").scale(0.85).shift(band_shift(6) + DOWN * 0.3)
        s2b = Tex("grants and clinics out; tax, VAT and levies in").scale(0.85).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(s2))
        self.play(Write(s2b))
        self.wait(2.5)
        s3 = Tex("The economy is a fire you are managing:").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        s3b = Tex("wood on $=$ expansionary; damped down $=$ contractionary").scale(0.85).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(s3))
        self.play(Write(s3b))
        self.play(Create(SurroundingRectangle(s3b, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_6): from Pretoria to the kitchen table ---
        self.next_band(7)
        b7_title = Tex("One number in Pretoria, one kitchen table").scale(1.0).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(2)
        t1 = Tex("Repo up: the banks' own money just got dearer").scale(0.9).shift(band_shift(7) + UP * 1.4)
        t2 = Tex("Prime follows by Friday — banks are not charities").scale(0.9).shift(band_shift(7) + UP * 0.55)
        t3 = Tex("Bond, car, store account: every debt costs more").scale(0.9).shift(band_shift(7) + DOWN * 0.3)
        t4 = Tex("The fridge waits; the second bakkie is not financed").scale(0.9).shift(band_shift(7) + DOWN * 1.15)
        t5 = Tex("Less money chasing goods: price rises lose their nerve").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        for m in (t1, t2, t3, t4, t5):
            self.play(Write(m))
            self.wait(1.8)
        t6 = Tex("Every rate decision is a weighing of pains").scale(0.9).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(t6))
        self.wait(3)

        # --- Band 8 (subtopic_7): the Budget's two taps ---
        self.next_band(8)
        b8_title = Tex("The Budget's two taps: fast tool, slow tool").scale(1.05).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        u1 = Tex("Tap 1 spending: ease closed to settle prices, open in recession").scale(0.8).shift(band_shift(8) + UP * 1.4)
        u2 = Tex("Tap 2 taxes: up to cool spending, down to revive it").scale(0.85).shift(band_shift(8) + UP * 0.55)
        self.play(Write(u1))
        self.wait(2)
        self.play(Write(u2))
        self.wait(2)
        u3 = Tex(r"``The Minister raises the repo rate to fight inflation''").scale(0.85).shift(band_shift(8) + DOWN * 0.35)
        self.play(Write(u3))
        self.play(Create(strike(u3)))
        self.wait(1.5)
        u4 = Tex("The minister holds the taps, not the wheel").scale(0.9).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(u4))
        self.wait(2)
        u5 = Tex("Monetary fast but blunt; fiscal slow but aimed").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(u5))
        self.play(Create(SurroundingRectangle(u5, color=GREEN)))
        self.wait(2)
        u6 = Tex("Wheel and taps pulling together beat them fighting").scale(0.85).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(u6))
        self.wait(4)
