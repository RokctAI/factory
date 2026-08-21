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

# Band-layout whiteboard scene for "Value, Utility and Market Structures"
# (grade 10, term 2 — IEB catalogue). One band per teaching beat; camera moves
# down, earlier work stays. Mostly text boards with simple hand-built
# comparisons (exporter-safe primitives; write-only reveals).
#
# Subtopic shares (subtopics.json, total 1450 s):
# 220/230/220/210/190/190/190 — subtopics 1-3 each get paired bands where the
# argument splits naturally.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ValueUtilityMarketStructuresSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): utility is subjective ---
        title = Tex("Value, Utility and Market Structures").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0a = Tex(r"Utility: satisfaction a user derives").scale(1.05).shift(UP * 1.4)
        self.play(Write(b0a))
        self.wait(2)
        b0b = Tex(r"SUBJECTIVE — it lives in the person,").scale(1.0).shift(UP * 0.5)
        b0c = Tex(r"not in the object").scale(1.0).shift(DOWN * 0.2)
        self.play(Write(b0b))
        self.play(Write(b0c))
        self.wait(2.5)
        b0d = Tex(r"Raincoat: storm vs cloudless day").scale(0.95).shift(DOWN * 1.2)
        self.play(Write(b0d))
        self.wait(2)
        b0e = Tex(r"Different worths make trade possible").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(b0e))
        self.play(Create(SurroundingRectangle(b0e, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the two values, the paradox ---
        self.next_band(1)
        b1t = Tex("Two values, one riddle").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        b1a = Tex(r"Value in USE: usefulness to the owner").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1b = Tex(r"Value in EXCHANGE: what it fetches traded").scale(1.0).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1a))
        self.play(Write(b1b))
        self.wait(2.5)
        b1w = Tex(r"``More useful must mean more expensive''").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1w))
        self.play(Create(strike(b1w)))
        self.wait(2)
        b1c = Tex(r"Water: vital, abundant $\to$ cents").scale(1.0).shift(band_shift(1) + DOWN * 1.3)
        b1d = Tex(r"Diamonds: ornamental, rare $\to$ fortunes").scale(1.0).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1c))
        self.play(Write(b1d))
        self.wait(2)
        b1e = Tex(r"Scarcity rules exchange value:").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        b1f = Tex(r"abundance cheapens, scarcity makes dear").scale(1.0).shift(band_shift(1) + DOWN * 3.6)
        self.play(Write(b1e))
        self.play(Write(b1f))
        self.play(Create(SurroundingRectangle(VGroup(b1e, b1f), color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the perfect market ---
        self.next_band(2)
        b2t = Tex("The perfect market — the benchmark").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        conds = [
            r"1. Many buyers, many sellers",
            r"2. Homogeneous product",
            r"3. Perfect knowledge",
            r"4. Free entry and exit",
        ]
        for i, c in enumerate(conds):
            m = Tex(c).scale(1.0).shift(band_shift(2) + UP * (1.2 - i * 0.7))
            self.play(Write(m), run_time=0.8)
            self.wait(1)
        b2a = Tex(r"Result: everyone a PRICE TAKER —").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        b2b = Tex(r"the crossing point rules them all").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2a))
        self.play(Write(b2b))
        self.play(Create(SurroundingRectangle(VGroup(b2a, b2b), color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): imperfect structures ---
        self.next_band(3)
        b3t = Tex("When conditions fail").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        b3a = Tex(r"MONOPOLY: one seller — patented seed,").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3b = Tex(r"sole rail operator — a price MAKER").scale(0.95).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3a))
        self.play(Write(b3b))
        self.wait(2.5)
        b3c = Tex(r"OLIGOPOLY: a few giants — banks, fuel,").scale(0.95).shift(band_shift(3) + DOWN * 0.4)
        b3d = Tex(r"networks — watching each other").scale(0.95).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3c))
        self.play(Write(b3d))
        self.wait(2.5)
        b3e = Tex(r"MONOPOLISTIC COMPETITION: many similar").scale(0.95).shift(band_shift(3) + DOWN * 2.0)
        b3f = Tex(r"but differentiated — coffee shops, brands").scale(0.95).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3e))
        self.play(Write(b3f))
        self.wait(2)
        b3g = Tex(r"Sort by: sellers, similarity, entry").scale(1.0).shift(band_shift(3) + DOWN * 3.6)
        self.play(Write(b3g))
        self.play(Create(SurroundingRectangle(b3g, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): world markets, electronic effects ---
        self.next_band(4)
        b4t = Tex("World markets, electronic markets").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        b4a = Tex(r"Gold and the rand: priced by the planet,").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4b = Tex(r"felt in every mining town").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4a))
        self.play(Write(b4b))
        self.wait(2.5)
        b4c = Tex(r"Electronics: WIDER (Mthatha vs Singapore),").scale(0.9).shift(band_shift(4) + DOWN * 0.4)
        b4d = Tex(r"FASTER (seconds), better KNOWLEDGE,").scale(0.9).shift(band_shift(4) + DOWN * 1.1)
        b4e = Tex(r"lower ENTRY, new market FORMS").scale(0.9).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4c))
        self.play(Write(b4d))
        self.play(Write(b4e))
        self.play(Create(SurroundingRectangle(VGroup(b4c, b4d, b4e), color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): balancing the account ---
        self.next_band(5)
        b5t = Tex("Balance the ledger").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        b5a = Tex(r"Platform owners hold the new gates").scale(1.0).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5a))
        self.wait(2)
        b5b = Tex(r"Small sellers face world-sized rivals").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5b))
        self.wait(2)
        b5c = Tex(r"Data costs: the digital divide is a").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        b5d = Tex(r"new barrier to entry").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5c))
        self.play(Write(b5d))
        self.wait(2.5)
        b5e = Tex(r"Wider, faster, better informed —").scale(1.0).shift(band_shift(5) + DOWN * 2.1)
        b5f = Tex(r"not automatically fairer").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5e))
        self.play(Write(b5f))
        self.play(Create(SurroundingRectangle(VGroup(b5e, b5f), color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the five functions of markets ---
        self.next_band(6)
        b6t = Tex("What markets DO — five functions").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6t))
        self.wait(1.5)
        funcs = [
            r"1. FORM prices (the crossing point)",
            r"2. ALLOCATE resources (prices steer)",
            r"3. INFORM (one number, millions briefed)",
            r"4. RATION (scarce goods to those who pay)",
            r"5. LINK strangers (farmer to tailor)",
        ]
        for i, f in enumerate(funcs):
            m = Tex(f).scale(0.9).shift(band_shift(6) + UP * (1.4 - i * 0.7))
            self.play(Write(m), run_time=0.8)
            self.wait(0.8)
        b6a = Tex(r"Markets make prices; prices do the rest").scale(0.95).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6a))
        self.play(Create(SurroundingRectangle(b6a, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the festival bottle ---
        self.next_band(7)
        b7t = Tex("Why water costs R30 at the festival").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex(r"Same bottle: R9 at the caf\'e,").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7b = Tex(r"R30 inside the fence — YOU changed").scale(1.0).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7a))
        self.play(Write(b7b))
        self.wait(2.5)
        b7c = Tex(r"Use-worth: water beats diamonds").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        b7d = Tex(r"Trading-worth: scarcity beats nobility").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7c))
        self.play(Write(b7d))
        self.wait(2.5)
        b7e = Tex(r"Fence the crowd in $\to$ water scarce").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        b7f = Tex(r"$\to$ price triples: the rule, reversed").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7e))
        self.play(Write(b7f))
        self.play(Create(SurroundingRectangle(b7f, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the tomato market and the big four banks ---
        self.next_band(8)
        b8t = Tex("A Saturday of market structures").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"Sunrise tomatoes: forty growers, identical").scale(0.9).shift(band_shift(8) + UP * 1.2)
        b8b = Tex(r"crates, visible prices — everyone TAKES").scale(0.9).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8a))
        self.play(Write(b8b))
        self.wait(2.5)
        b8c = Tex(r"Four big banks: oligopoly, watching").scale(0.9).shift(band_shift(8) + DOWN * 0.4)
        b8d = Tex(r"each other; patented seed: monopoly MAKES").scale(0.9).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8c))
        self.play(Write(b8d))
        self.wait(2.5)
        b8e = Tex(r"Coffee-shop street: many, similar,").scale(0.9).shift(band_shift(8) + DOWN * 2.0)
        b8f = Tex(r"differentiated — small pricing power").scale(0.9).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8e))
        self.play(Write(b8f))
        self.play(Create(SurroundingRectangle(VGroup(b8e, b8f), color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): the market in your pocket ---
        self.next_band(9)
        b9t = Tex("The market in your pocket").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex(r"Farmer scrolls the auction group first —").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9b = Tex(r"knowledge is bargaining power").scale(0.95).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9a))
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex(r"But: platform gates, world rivals,").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        b9d = Tex(r"and data as the new locked gate").scale(0.95).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9c))
        self.play(Write(b9d))
        self.wait(2.5)
        b9e = Tex(r"Old or electronic, the same five jobs:").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        b9f = Tex(r"form, steer, message, ration, connect").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9e))
        self.play(Write(b9f))
        self.play(Create(SurroundingRectangle(VGroup(b9e, b9f), color=GREEN)))
        self.wait(4)
