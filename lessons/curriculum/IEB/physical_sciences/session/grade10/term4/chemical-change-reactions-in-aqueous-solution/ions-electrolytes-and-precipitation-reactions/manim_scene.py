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

# Band-layout whiteboard scene for "Ions, Electrolytes and Precipitation
# Reactions" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics
# 5-7). Exporter-safe mobjects only (Tex/MathTex/Line/Arrow/Dot/Circle/
# Rectangle/VGroup), add-only lifecycle; the water molecule and conductivity
# tester are hand-built from primitives. Band time apportioned to
# subtopics.json (230/240/240/270/190/190/200 of 1560 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class IonsElectrolytesPrecipitationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(15)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): water the polar molecule ---
        title = Tex("Ions, Electrolytes and Precipitation").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("The water molecule is POLAR").scale(1.1).shift(UP * 1.3)
        self.play(Write(d1))
        self.wait(2)
        # hand-built H2O sketch: one O circle, two H circles, charge labels
        oc = Circle(radius=0.55, color=RED).shift(DOWN * 0.6 + LEFT * 1.0)
        ol = MathTex(r"\text{O}").scale(0.9).move_to(oc.get_center())
        h1 = Circle(radius=0.32, color=BLUE).shift(DOWN * 0.05 + RIGHT * 0.1)
        h1l = MathTex(r"\text{H}").scale(0.75).move_to(h1.get_center())
        h2 = Circle(radius=0.32, color=BLUE).shift(DOWN * 1.25 + RIGHT * 0.1)
        h2l = MathTex(r"\text{H}").scale(0.75).move_to(h2.get_center())
        dm = MathTex(r"\delta^-").scale(0.9).move_to(oc.get_center() + LEFT * 1.1)
        dp = MathTex(r"\delta^+").scale(0.9).move_to(h1.get_center() + RIGHT * 0.9)
        self.play(Create(oc), Write(ol))
        self.play(Create(h1), Write(h1l), Create(h2), Write(h2l))
        self.play(Write(dm), Write(dp))
        self.wait(2.5)
        d2 = Tex("Oxygen corner slightly $-$, hydrogen corners slightly $+$").scale(0.9).shift(DOWN * 2.2)
        self.play(Write(d2))
        self.wait(2)
        d3 = Tex("A grappling hook for anything built from charge").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(d3))
        self.wait(3)

        # --- Band 1 (subtopic_1): dissolution of copper sulfate ---
        self.next_band(1)
        b1t = Tex("Dissolution: copper sulfate into water").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = Tex("O-faces mob Cu$^{2+}$; H-faces mob SO$_4^{2-}$").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1a))
        self.wait(2.5)
        b1b = Tex("Freed ions wear a water shell: HYDRATION").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1b))
        self.wait(2.5)
        b1c = MathTex(r"\text{CuSO}_4\text{(s)} \to \text{Cu}^{2+}(aq) + \text{SO}_4^{2-}(aq)").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1c))
        self.play(Create(SurroundingRectangle(b1c, color=GREEN)))
        self.wait(2.5)
        b1d = Tex(r"Charge audit: $(+2) + (-2) = 0$ — balanced").scale(1.0).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1d))
        self.wait(2)
        b1e = Tex("The spreading blue IS the hydrated Cu$^{2+}$ ion").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1e))
        self.wait(3)

        # --- Band 2 (subtopic_1): two more dissolutions ---
        self.next_band(2)
        b2t = Tex("Practise the pattern").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = MathTex(r"\text{MgCl}_2\text{(s)} \to \text{Mg}^{2+}(aq) + 2\,\text{Cl}^-(aq)").scale(0.95).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2a))
        self.wait(2.5)
        b2b = Tex(r"Audit: $(+2) + 2(-1) = 0$").scale(0.95).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = MathTex(r"\text{KNO}_3\text{(s)} \to \text{K}^+(aq) + \text{NO}_3^-(aq)").scale(1.0).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2c))
        self.wait(2.5)
        b2d = Tex("Check both: atoms balance AND charge balances").scale(1.0).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2d))
        self.play(Create(SurroundingRectangle(b2d, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the conductivity tester ---
        self.next_band(3)
        b3t = Tex("The conductivity tester").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3t))
        self.wait(2)
        # beaker + electrodes + wires + battery + bulb, from primitives
        beaker = Rectangle(width=3.2, height=1.8).shift(band_shift(3) + DOWN * 1.6 + LEFT * 2.2)
        e1 = Line(band_shift(3) + LEFT * 2.9 + UP * 0.2, band_shift(3) + LEFT * 2.9 + DOWN * 2.0, stroke_width=6)
        e2 = Line(band_shift(3) + LEFT * 1.5 + UP * 0.2, band_shift(3) + LEFT * 1.5 + DOWN * 2.0, stroke_width=6)
        w1 = Line(band_shift(3) + LEFT * 2.9 + UP * 0.2, band_shift(3) + LEFT * 2.9 + UP * 1.2, stroke_width=4)
        w2 = Line(band_shift(3) + LEFT * 2.9 + UP * 1.2, band_shift(3) + RIGHT * 0.2 + UP * 1.2, stroke_width=4)
        batt = Rectangle(width=1.0, height=0.5).shift(band_shift(3) + RIGHT * 0.7 + UP * 1.2)
        bl = Tex("battery").scale(0.7).move_to(band_shift(3) + RIGHT * 0.7 + UP * 1.8)
        w3 = Line(band_shift(3) + RIGHT * 1.2 + UP * 1.2, band_shift(3) + RIGHT * 2.6 + UP * 1.2, stroke_width=4)
        bulb = Circle(radius=0.35).shift(band_shift(3) + RIGHT * 2.95 + UP * 1.2)
        bulbl = Tex("bulb").scale(0.7).move_to(band_shift(3) + RIGHT * 2.95 + UP * 1.9)
        w4 = Line(band_shift(3) + RIGHT * 3.3 + UP * 1.2, band_shift(3) + RIGHT * 4.0 + UP * 1.2, stroke_width=4)
        w5 = Line(band_shift(3) + RIGHT * 4.0 + UP * 1.2, band_shift(3) + RIGHT * 4.0 + DOWN * 2.6, stroke_width=4)
        w6 = Line(band_shift(3) + RIGHT * 4.0 + DOWN * 2.6, band_shift(3) + LEFT * 1.5 + DOWN * 2.6, stroke_width=4)
        w7 = Line(band_shift(3) + LEFT * 1.5 + DOWN * 2.6, band_shift(3) + LEFT * 1.5 + DOWN * 2.0, stroke_width=4)
        self.play(Create(beaker))
        self.play(Create(e1), Create(e2))
        self.play(Create(w1), Create(w2), Create(batt), Write(bl))
        self.play(Create(w3), Create(bulb), Write(bulbl), Create(w4), Create(w5), Create(w6), Create(w7))
        self.wait(2.5)
        b3a = Tex("Distilled water: dead").scale(0.9).move_to(band_shift(3) + RIGHT * 3.3 + DOWN * 0.2)
        b3b = Tex("Salt water: bright").scale(0.9).move_to(band_shift(3) + RIGHT * 3.3 + DOWN * 0.9)
        b3c = Tex("Sugar water: dead").scale(0.9).move_to(band_shift(3) + RIGHT * 3.3 + DOWN * 1.6)
        self.play(Write(b3a))
        self.wait(1.5)
        self.play(Write(b3b))
        self.wait(1.5)
        self.play(Write(b3c))
        self.wait(3)

        # --- Band 4 (subtopic_2): electrolytes and the trap ---
        self.next_band(4)
        b4t = Tex("Electrolytes: solutions that conduct").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("A current needs mobile charge carriers: IONS").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4a))
        self.wait(2.5)
        b4b = Tex("Salt $\\to$ ion crowd $\\to$ light: electrolyte").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4b))
        self.wait(2)
        b4c = Tex("Sugar enters WHOLE — neutral molecules").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4c))
        self.wait(2)
        b4d = Tex("Brighter bulb $=$ higher ion concentration").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4d))
        self.wait(2)
        b4e = Tex("Conductivity measures solubility").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4e))
        self.play(Create(strike(b4e)))
        self.wait(3)

        # --- Band 5 (subtopic_3): precipitation ---
        self.next_band(5)
        b5t = Tex("Two clear solutions make a solid").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("Barium meets sulfate: an INSOLUBLE pairing").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5a))
        self.wait(2.5)
        b5b = MathTex(r"\text{BaCl}_2\text{(aq)} + \text{Na}_2\text{SO}_4\text{(aq)}").scale(1.0).shift(band_shift(5) + UP * 0.2)
        b5c = MathTex(r"\to \text{BaSO}_4\text{(s)} + 2\,\text{NaCl(aq)}").scale(1.0).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5b))
        self.play(Write(b5c))
        self.play(Create(SurroundingRectangle(VGroup(b5b, b5c), color=GREEN)))
        self.wait(3)
        b5d = Tex("The (s) IS the precipitate — the white cloud").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5d))
        self.wait(2)
        b5e = Tex("ION EXCHANGE: partners swap, a solid escapes").scale(0.95).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5e))
        self.wait(3)

        # --- Band 6 (subtopic_3): the solubility short-list ---
        self.next_band(6)
        b6t = Tex("The Grade 10 solubility short-list").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("All nitrates: soluble — never precipitate").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6a))
        self.wait(2)
        b6b = Tex("Common Na, K, NH$_4$ compounds: soluble").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6b))
        self.wait(2)
        b6c = Tex("Famous insolubles: AgCl, AgBr, AgI").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6c))
        self.wait(2)
        b6d = Tex("BaSO$_4$; most carbonates; yellow PbI$_2$").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6d))
        self.wait(2)
        b6e = Tex("No insoluble pairing $=$ no reaction at all").scale(1.0).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6e))
        self.wait(3)

        # --- Band 7 (subtopic_4): the ion test kit ---
        self.next_band(7)
        b7t = Tex("The ion test kit: acid first, reagent second").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("HNO$_3$ then AgNO$_3$: white $\\to$ Cl$^-$").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7a))
        self.wait(2)
        b7b = Tex("cream $\\to$ Br$^-$, \\; yellow $\\to$ I$^-$").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7b))
        self.wait(2)
        b7c = Tex("HNO$_3$ then Ba(NO$_3$)$_2$: white that PERSISTS $\\to$ SO$_4^{2-}$").scale(0.88).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7c))
        self.wait(2.5)
        b7d = Tex("White solid fizzing away in acid $\\to$ CO$_3^{2-}$").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7d))
        self.wait(2)
        b7e = Tex("Acid unmasks the carbonate impostor first").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7e))
        self.wait(3)

        # --- Band 8 (subtopic_4): the bottle verdict ---
        self.next_band(8)
        b8t = Tex("The storeroom bottle, solved").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Add acid: no fizz $\\to$ no carbonate").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex("Add AgNO$_3$: WHITE snow falls").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("Cross-check Ba(NO$_3$)$_2$: nothing $\\to$ no sulfate").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex("Verdict: chloride, Cl$^-$").scale(1.15).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8d))
        self.play(Create(SurroundingRectangle(b8d, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_4): the four reaction types ---
        self.next_band(9)
        b9t = Tex("The four reaction types").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("1. Precipitation — a solid escapes").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2)
        b9b = Tex("2. Gas-forming — a gas escapes").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex("3. Acid-base — protons handed across").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9c))
        self.wait(2)
        b9d = Tex("4. Redox — ELECTRONS handed across").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9d))
        self.wait(2)
        b9e = Tex("Redox fingerprint: atoms change charge (Mg $\\to$ Mg$^{2+}$)").scale(0.9).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9e))
        self.play(Create(SurroundingRectangle(b9e, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 10 (subtopic_5): what water does to salt ---
        self.next_band(10)
        b10t = Tex("What water does to salt").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("Water: a tiny two-faced molecule").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10a))
        self.wait(2)
        b10b = Tex("Salt scaffold dismantled — ions levered off, escorted").scale(0.95).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10b))
        self.wait(2.5)
        b10c = MathTex(r"\text{NaCl(s)} \to \text{Na}^+(aq) + \text{Cl}^-(aq)").scale(1.05).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10c))
        self.play(Create(SurroundingRectangle(b10c, color=GREEN)))
        self.wait(2.5)
        b10d = Tex("aq $=$ `swimming in water'").scale(1.0).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10d))
        self.wait(2)
        b10e = Tex("Sugar leaves whole — no charged pieces").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10e))
        self.wait(3)

        # --- Band 11 (subtopic_6): the light bulb detective ---
        self.next_band(11)
        b11t = Tex("The light bulb detective").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11t))
        self.wait(2)
        b11a = Tex("Plain water: dark. Salt: bright. Sugar: dark").scale(1.0).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11a))
        self.wait(2.5)
        b11b = Tex("The bulb detects IONS — swimming charges").scale(1.0).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11b))
        self.wait(2.5)
        b11c = Tex("More salt $\\to$ more swimmers $\\to$ brighter").scale(1.0).shift(band_shift(11) + DOWN * 0.8)
        self.play(Write(b11c))
        self.wait(2)
        b11d = Tex("Dark bulb $=$ nothing dissolved").scale(1.0).shift(band_shift(11) + DOWN * 1.8)
        self.play(Write(b11d))
        self.play(Create(strike(b11d)))
        self.wait(2)
        b11e = Tex("Dissolving and conducting: two separate talents").scale(0.95).shift(band_shift(11) + DOWN * 2.8)
        self.play(Write(b11e))
        self.wait(3)

        # --- Band 12 (subtopic_7): snow in a glass ---
        self.next_band(12)
        b12t = Tex("Snow in a glass — white and gold").scale(1.15).shift(band_shift(12) + UP * 2.2)
        self.play(Write(b12t))
        self.wait(2)
        b12a = Tex("Some ion couples cannot swim: they weld solid").scale(0.95).shift(band_shift(12) + UP * 1.2)
        self.play(Write(b12a))
        self.wait(2.5)
        b12b = MathTex(r"\text{Pb(NO}_3)_2\text{(aq)} + 2\,\text{KI(aq)}").scale(1.0).shift(band_shift(12) + UP * 0.4)
        b12b2 = MathTex(r"\to \text{PbI}_2\text{(s)} + 2\,\text{KNO}_3\text{(aq)}").scale(1.0).shift(band_shift(12) + DOWN * 0.4)
        self.play(Write(b12b))
        self.play(Write(b12b2))
        self.play(Create(SurroundingRectangle(VGroup(b12b, b12b2), color=GREEN)))
        self.wait(3)
        b12c = Tex("Mystery bottle drill: acid $\\to$ silver $\\to$ barium").scale(0.95).shift(band_shift(12) + DOWN * 1.3)
        self.play(Write(b12c))
        self.wait(2)
        b12d = Tex("Fizz: carbonate. White/cream/yellow: halides").scale(0.95).shift(band_shift(12) + DOWN * 2.1)
        self.play(Write(b12d))
        self.wait(2)
        b12e = Tex("Our bottle: no fizz, white silver snow $\\to$ chloride").scale(0.9).shift(band_shift(12) + DOWN * 2.9)
        self.play(Write(b12e))
        self.wait(4)
