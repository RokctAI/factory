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

# Band-layout whiteboard scene for "Physical and Chemical Change" (Part 1
# Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe
# mobjects only; write-only reveals; camera moves down band by band. Band
# time apportioned to subtopics.json (230/235/240/240/185/185/185 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class PhysicalChemicalChangeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the deciding question ---
        title = Tex("Physical and Chemical Change").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("The deciding question:").scale(1.1).shift(UP * 1.1)
        self.play(Write(b0_l1))
        b0_l2 = Tex("IS A NEW SUBSTANCE FORMED?").scale(1.15).shift(UP * 0.2)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2.5)
        b0_l3 = Tex("Physical: no new substance — melted chocolate;").scale(0.9).shift(DOWN * 0.9)
        b0_l4 = Tex("particles survive, usually easy to reverse").scale(0.95).shift(DOWN * 1.6)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex("Chemical: NEW substances — the struck match;").scale(0.9).shift(DOWN * 2.4)
        b0_l6 = Tex("bonds break and re-form, hard to reverse").scale(0.95).shift(DOWN * 3.1)
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_2): physical change up close ---
        self.next_band(1)
        b1_t = Tex("Physical change: same particles").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("State changes: washing dries, dew returns —").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("one substance in three outfits").scale(1.0).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Dissolving: sun the basin, crystals return").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Shape and size: tearing, grating, grinding").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("energy change alone proves nothing —").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        b1_l6 = Tex("the washing line runs on sunshine, still physical").scale(0.9).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_3): the five signs of chemical change ---
        self.next_band(2)
        b2_t = Tex("Evidence of a chemical change").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("1. Gas produced: lemon juice on bicarb foams").scale(0.9).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(1.5)
        b2_l2 = Tex("2. Precipitate: a yellow solid snows from clear liquids").scale(0.85).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l2))
        self.wait(1.5)
        b2_l3 = Tex("3. Permanent colour change: copper roof turns green").scale(0.85).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l3))
        self.wait(1.5)
        b2_l4 = Tex("4. Temperature change on its own:").scale(0.95).shift(band_shift(2) + DOWN * 1.2)
        b2_l5 = Tex("hand warmer exothermic, sherbet endothermic").scale(0.9).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(2)
        b2_l6 = Tex("5. Light or sound: sparkler blaze, hydrogen pop").scale(0.9).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_3): signs are evidence, not verdicts ---
        self.next_band(3)
        b3_t = Tex("Evidence, then the verdict").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("bubbles alone can mislead: boiling").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("also bubbles, and boiling is physical").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("the verdict is always the same question:").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = Tex("has a NEW substance appeared?").scale(1.05).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)
        b3_l5 = Tex("one-way traffic: blackened toast, sour milk,").scale(0.95).shift(band_shift(3) + DOWN * 2.4)
        b3_l6 = Tex("set concrete — none of them return").scale(1.0).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_4): conservation of mass and energy ---
        self.next_band(4)
        b4_t = Tex("What is conserved in BOTH changes").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("Mass: atoms regroup, never vanish").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\text{mass of products} = \text{mass of reactants}").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)
        b4_l3 = Tex("wood SEEMS to lose mass — gases escape unweighed;").scale(0.85).shift(band_shift(4) + DOWN * 0.9)
        b4_l4 = Tex("steel wool SEEMS to gain — count the oxygen in").scale(0.9).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("energy is conserved too — it only moves;").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        b4_l6 = Tex("energy flow never decides the classification").scale(0.95).shift(band_shift(4) + DOWN * 3.2)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_4): the tricky cases ---
        self.next_band(5)
        b5_t = Tex("The tricky cases").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("Boiling water: steam is still water — physical").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex(r"Electrolysis: water $\to$ H$_2$ + O$_2$ — chemical").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("Sugar dissolving: physical; sugar in the").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex("pan: melts, then caramel — chemical").scale(0.95).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Fizzy drink: gas escaping — physical; fizzing tablet: new CO$_2$").scale(0.8).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l5))
        self.wait(2)
        b5_l6 = Tex("Candle: wax melts while wax burns — both at once").scale(0.9).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): the ice tray and the braai fire ---
        self.next_band(6)
        b6_t = Tex("The ice tray and the braai fire").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("Freeze, melt, refill, freeze — always WATER:").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("same stuff, different outfit").scale(1.0).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("By morning the wood is ash and gone gases —").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("no cooling un-burns wood").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Test: can simple means bring it back?").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_6): clues at the scene ---
        self.next_band(7)
        b7_t = Tex("Clues at the scene").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("unexpected foam; a solid from nowhere;").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("a colour that will not come back;").scale(0.95).shift(band_shift(7) + UP * 0.5)
        b7_l3 = Tex("heat nobody added; light from the change").scale(0.95).shift(band_shift(7) + DOWN * 0.2)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex("fizzy-drink bubbles frame an innocent change —").scale(0.9).shift(band_shift(7) + DOWN * 1.2)
        b7_l5 = Tex("conviction needs a NEW SUBSTANCE").scale(1.05).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(2)
        b7_l6 = Tex("toast went in bread, came out black, stays black: yes").scale(0.85).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l6))
        self.wait(3)

        # --- Band 8 (subtopic_7): the candle doing both ---
        self.next_band(8)
        b8_t = Tex("The candle doing both at once").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Top: wax melts, runs, hardens back —").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("physical, reversible by cooling").scale(1.0).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Wick: wax burns to CO$_2$ and water vapour —").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex("chemical, never coming back").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2.5)
        b8_l5 = Tex("weigh candle, gases and oxygen used:").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        b8_l6 = Tex("the ledger balances — atoms never vanish").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(4)
