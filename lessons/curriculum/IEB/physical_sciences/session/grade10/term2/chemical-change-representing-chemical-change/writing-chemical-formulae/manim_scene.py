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

# Band-layout whiteboard scene for "Writing Chemical Formulae" (Part 1
# Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe
# mobjects only; write-only reveals; camera moves down band by band. Band
# time apportioned to subtopics.json (230/240/250/270/160/160/160 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class WritingFormulaeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the one law ---
        title = Tex("Writing Chemical Formulae").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("The one law: charges must cancel").scale(1.05).shift(UP * 1.0)
        self.play(Write(b0_l1))
        b0_l2 = MathTex(r"\text{total} + \ \text{plus total} - \ = 0").scale(1.0).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2.5)
        b0_l3 = Tex("metals lose electrons: cations +").scale(0.95).shift(DOWN * 0.9)
        b0_l4 = Tex("non-metals gain electrons: anions $-$").scale(0.95).shift(DOWN * 1.6)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex(r"KBr: $+1-1=0$; CaO: $+2-2=0$; AlCl$_3$: $+3-3=0$").scale(0.85).shift(DOWN * 2.6)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_2): calcium chloride by crossover ---
        self.next_band(1)
        b1_t = Tex("Calcium chloride by crossover").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"\mathrm{Ca^{2+}} \quad \mathrm{Cl^{-}}").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("cross the sizes: 2 drops under Cl, 1 under Ca").scale(0.9).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"\mathrm{CaCl_2}").scale(1.2).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = Tex("audit: $+2$ and $2 \\times (-1)$ — zero, proven").scale(0.9).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the two safety rules ---
        self.next_band(2)
        b2_t = Tex("Two safety rules on the rails").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex(r"1. simplify: Ca$_2$O$_2$ is CaO in disguise").scale(0.95).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("smallest whole-number ratio, always").scale(0.95).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex(r"2. never show a subscript of one:").scale(0.95).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = Tex(r"CaCl$_2$, not Ca$_1$Cl$_2$").scale(0.95).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): ammonium sulphate and the brackets ---
        self.next_band(3)
        b3_t = Tex("Ammonium sulphate and the bracket rule").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex(r"teams: NH$_4^{+}$ and SO$_4^{2-}$ — two ammoniums needed").scale(0.85).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"\mathrm{(NH_4)_2SO_4}").scale(1.15).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = Tex(r"no bracket: NH$_{42}$SO$_4$ — forty-two hydrogens").scale(0.9).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("the bracket: THIS WHOLE TEAM, taken twice").scale(0.9).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex(r"count: 2 N, 8 H, 1 S, 4 O; charges $+2-2=0$").scale(0.85).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_4): iron(III) oxide ---
        self.next_band(4)
        b4_t = Tex("Iron(III) oxide — the numeral is the charge").scale(1.0).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex(r"Fe$^{3+}$ meets O$^{2-}$: LCM of 3 and 2 is 6").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\mathrm{Fe_2O_3}").scale(1.2).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)
        b4_l3 = Tex(r"audit: $2(+3) = +6$; $3(-2) = -6$; zero").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("iron(II) oxide is FeO — a DIFFERENT substance").scale(0.9).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_4): the five-step method ---
        self.next_band(5)
        b5_t = Tex("The five-step method").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("1. name both ions — numerals and -ate endings help").scale(0.85).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(1.5)
        b5_l2 = Tex("2. write the ions WITH their charges").scale(0.85).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l2))
        self.wait(1.5)
        b5_l3 = Tex("3. find the neutral ratio — logic or crossover").scale(0.85).shift(band_shift(5) + DOWN * 0.2)
        self.play(Write(b5_l3))
        self.wait(1.5)
        b5_l4 = Tex("4. simplify, bracket multiplied teams, hide the ones").scale(0.85).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l4))
        self.wait(1.5)
        b5_l5 = Tex("5. audit charges and atoms").scale(0.85).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): the till must balance ---
        self.next_band(6)
        b6_t = Tex("The till must balance").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("givers: K hands out 1, Ca 2, Al 3 — positive").scale(0.9).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("takers: Br takes 1, O takes 2, N takes 3 — negative").scale(0.85).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("calcium hands out two, so call two chlorides").scale(0.9).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex(r"CaCl$_2$ — the drawer closes at zero").scale(0.95).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_6): the team rides in one taxi ---
        self.next_band(7)
        b7_t = Tex("The team rides in one taxi").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex(r"ammonium: five atoms, ONE passenger, fare $+1$").scale(0.9).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("two groups travel? brackets are the taxi:").scale(0.9).shift(band_shift(7) + UP * 0.3)
        b7_l3 = MathTex(r"\mathrm{(NH_4)_2SO_4}").scale(1.1).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex("two outside multiplies all inside: 2 N, 8 H").scale(0.9).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex(r"one group, no taxi; two hydroxides: Mg(OH)$_2$").scale(0.85).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_7): the name whispers the charge ---
        self.next_band(8)
        b8_t = Tex("When the name whispers the charge").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("iron(III) = the iron handing out three").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("three and two meet at six: two irons, three oxygens").scale(0.85).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex(r"Fe$_2$O$_3$ — rust on the farm gate").scale(0.95).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("iron(II) oxide: FeO — change the numeral,").scale(0.9).shift(band_shift(8) + DOWN * 1.5)
        b8_l5 = Tex("change the substance").scale(0.9).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(4)
