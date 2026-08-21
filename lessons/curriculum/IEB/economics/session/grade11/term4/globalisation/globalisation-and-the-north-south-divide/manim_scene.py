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

# Band-layout whiteboard scene for the session duo "Globalisation and the
# North/South Divide" (Grade 11, Term 4, IEB catalogue). One band per
# teaching step; the camera moves down and nothing is removed. Exporter-safe
# mobjects only; diagrams hand-built from Rectangles, Arrows and Tex. Band
# time apportioned to subtopics.json (240/250/250/240/205/205/210 of 1600 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class GlobalisationNorthSouthSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): definition + technology causes ---
        title = Tex("What Globalisation Is — and Why").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Economies interconnected and interdependent —").scale(0.9).shift(UP * 1.5)
        d1b = Tex("components of a single world system").scale(0.9).shift(UP * 0.75)
        self.play(Write(d1))
        self.play(Write(d1b))
        self.wait(2)
        d2 = Tex("Test: an event on one continent moves").scale(0.85).shift(DOWN * 0.1)
        d2b = Tex("jobs and prices on another within weeks").scale(0.85).shift(DOWN * 0.8)
        self.play(Write(d2))
        self.play(Write(d2b))
        self.play(Create(SurroundingRectangle(VGroup(d2, d2b), color=GREEN)))
        self.wait(2.5)
        d3 = Tex("Technology: container + cables + computing").scale(0.9).shift(DOWN * 1.9)
        d4 = Tex("= the global value chain: slice production anywhere").scale(0.85).shift(DOWN * 2.8)
        self.play(Write(d3))
        self.wait(2)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_1): policy causes ---
        self.next_band(1)
        b1_title = Tex("Policy: the second family").scale(1.1).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        p1 = Tex("Tariffs negotiated down, round after round").scale(0.95).shift(band_shift(1) + UP * 1.4)
        p2 = Tex("WTO, 1995: referee for most of world trade").scale(0.95).shift(band_shift(1) + UP * 0.55)
        self.play(Write(p1))
        self.wait(2)
        self.play(Write(p2))
        self.wait(2)
        p3 = Tex("Exchange controls dismantled: finance at a keystroke").scale(0.9).shift(band_shift(1) + DOWN * 0.35)
        self.play(Write(p3))
        self.wait(2)
        p4 = Tex("China 1978, Soviet bloc 1989, South Africa 1994:").scale(0.9).shift(band_shift(1) + DOWN * 1.25)
        p4b = Tex("billions rejoin one market").scale(0.9).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(p4))
        self.play(Write(p4b))
        self.wait(2.5)
        p5 = Tex("Possible by technology; permitted by policy").scale(0.95).shift(band_shift(1) + DOWN * 2.95)
        self.play(Write(p5))
        self.play(Create(SurroundingRectangle(p5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the gains column ---
        self.next_band(2)
        b2_title = Tex("The scorecard: gains").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        g1 = Tex("Specialisation: lower prices, wider choice").scale(0.9).shift(band_shift(2) + UP * 1.4)
        g2 = Tex("FDI: Kariega, East London, Rosslyn —").scale(0.9).shift(band_shift(2) + UP * 0.55)
        g2b = Tex("100 000+ jobs building vehicles for the world").scale(0.9).shift(band_shift(2) + DOWN * 0.2)
        self.play(Write(g1))
        self.wait(2)
        self.play(Write(g2))
        self.play(Write(g2b))
        self.wait(2.5)
        g3 = Tex("Knowledge diffuses: mobile money, solar, medicine").scale(0.85).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(g3))
        self.wait(2)
        g4 = Tex("Export-led growth: hundreds of millions out of poverty").scale(0.85).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(g4))
        self.play(Create(SurroundingRectangle(g4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the losses column + verdict ---
        self.next_band(3)
        b3_title = Tex("The scorecard: losses — and the verdict").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        l1 = Tex("Imports hollowed out textile and footwear towns:").scale(0.85).shift(band_shift(3) + UP * 1.4)
        l1b = Tex("tens of thousands of jobs gone").scale(0.85).shift(band_shift(3) + UP * 0.6)
        self.play(Write(l1))
        self.play(Write(l1b))
        self.wait(2.5)
        l2 = Tex("Contagion: 2008 began abroad, cut SA shifts in a year").scale(0.85).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(l2))
        self.wait(2)
        l3 = Tex("Race to the bottom: mobile capital outruns the tax base").scale(0.85).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(l3))
        self.wait(2)
        l4 = Tex("Verdict: grows the total, moves the shares —").scale(0.9).shift(band_shift(3) + DOWN * 2.1)
        l4b = Tex("harvest gains, cushion losses").scale(0.9).shift(band_shift(3) + DOWN * 2.85)
        self.play(Write(l4))
        self.play(Write(l4b))
        self.play(Create(SurroundingRectangle(VGroup(l4, l4b), color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the divide and its three mechanisms ---
        self.next_band(4)
        b4_title = Tex("The North/South divide: three mechanisms").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        m1 = Tex("Shorthand about wealth, not latitude").scale(0.9).shift(band_shift(4) + UP * 1.4)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex("1. Terms of trade: sell raw, buy made —").scale(0.9).shift(band_shift(4) + UP * 0.5)
        m2b = Tex("the treadmill runs faster every year").scale(0.9).shift(band_shift(4) + DOWN * 0.25)
        self.play(Write(m2))
        self.play(Write(m2b))
        self.wait(2.5)
        m3 = Tex("2. Debt in dollars: Northern rates squeeze").scale(0.9).shift(band_shift(4) + DOWN * 1.15)
        m3b = Tex("Southern clinics").scale(0.9).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(m3))
        self.play(Write(m3b))
        self.wait(2)
        m4 = Tex("3. Voice: rules drafted where the votes leaned North").scale(0.85).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(m4))
        self.wait(3)

        # --- Band 5 (subtopic_3): the divide is moving ---
        self.next_band(5)
        b5_title = Tex("The divide is not frozen").scale(1.1).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        v1 = Tex("China, India, Brazil: the centre of gravity").scale(0.9).shift(band_shift(5) + UP * 1.4)
        v1b = Tex("drags southward").scale(0.9).shift(band_shift(5) + UP * 0.65)
        self.play(Write(v1))
        self.play(Write(v1b))
        self.wait(2.5)
        v2 = Tex("BRICS — South Africa inside — demands a voice").scale(0.9).shift(band_shift(5) + DOWN * 0.25)
        self.play(Write(v2))
        self.wait(2)
        v3 = Tex("AfCFTA: the South builds its own market").scale(0.9).shift(band_shift(5) + DOWN * 1.15)
        self.play(Write(v3))
        self.wait(2)
        v4 = Tex("Narrowing sharply in Asia; persisting,").scale(0.9).shift(band_shift(5) + DOWN * 2.05)
        v4b = Tex("sometimes widening, across Africa").scale(0.9).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(v4))
        self.play(Write(v4b))
        self.play(Create(SurroundingRectangle(VGroup(v4, v4b), color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): South Africa inside the global economy ---
        self.next_band(6)
        b6_title = Tex("South Africa inside the system").scale(1.1).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        s1 = Tex("Openness: exports + imports well over half of GDP").scale(0.85).shift(band_shift(6) + UP * 1.4)
        self.play(Write(s1))
        self.play(Create(SurroundingRectangle(s1, color=GREEN)))
        self.wait(2.5)
        s2 = Tex("Petrol tracks world oil; bread tracks world wheat;").scale(0.85).shift(band_shift(6) + UP * 0.45)
        s2b = Tex("the platinum belt tracks world vehicle demand").scale(0.85).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(s2))
        self.play(Write(s2b))
        self.wait(2.5)
        s3 = Tex("Links: AfCFTA for manufactures, preferential access").scale(0.8).shift(band_shift(6) + DOWN * 1.2)
        s3b = Tex("North, BRICS and its bank, WTO underneath").scale(0.8).shift(band_shift(6) + DOWN * 1.95)
        self.play(Write(s3))
        self.play(Write(s3b))
        self.wait(2.5)
        s4 = Tex("Sandton finance like the North; raw exports like the South").scale(0.75).shift(band_shift(6) + DOWN * 2.85)
        self.play(Write(s4))
        self.wait(3)

        # --- Band 7 (subtopic_4): the two-handed policy debate ---
        self.next_band(7)
        b7_title = Tex("The two-handed debate").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(1.5)
        h1 = Tex("Hand one: integrate deeper — export markets,").scale(0.85).shift(band_shift(7) + UP * 1.4)
        h1b = Tex("investment, industrialise through the African market").scale(0.85).shift(band_shift(7) + UP * 0.6)
        self.play(Write(h1))
        self.play(Write(h1b))
        self.wait(2.5)
        h2 = Tex("Hand two: protect strategically — tariffs and").scale(0.85).shift(band_shift(7) + DOWN * 0.3)
        h2b = Tex("local content while industries rebuild").scale(0.85).shift(band_shift(7) + DOWN * 1.05)
        self.play(Write(h2))
        self.play(Write(h2b))
        self.wait(2.5)
        h3 = Tex("Openness grows the pie and moves the slices:").scale(0.85).shift(band_shift(7) + DOWN * 2.0)
        h3b = Tex("pair integration with skills and safety nets").scale(0.85).shift(band_shift(7) + DOWN * 2.75)
        self.play(Write(h3))
        self.play(Write(h3b))
        self.play(Create(SurroundingRectangle(h3b, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the world in your pocket ---
        self.next_band(8)
        b8_title = Tex("The world in your pocket").scale(1.15).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        w1 = Tex("One phone: design, chip, glass, cobalt, lithium,").scale(0.85).shift(band_shift(8) + UP * 1.4)
        w1b = Tex("assembly — and a cable ashore at Melkbosstrand").scale(0.85).shift(band_shift(8) + UP * 0.6)
        self.play(Write(w1))
        self.play(Write(w1b))
        self.wait(2.5)
        w2 = Tex("Door one: containers cheap, cables instant").scale(0.9).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(w2))
        self.wait(2)
        w3 = Tex("Door two: tariffs down, WTO referee, money freed,").scale(0.85).shift(band_shift(8) + DOWN * 1.2)
        w3b = Tex("closed giants return — SA reopens after 1994").scale(0.85).shift(band_shift(8) + DOWN * 1.95)
        self.play(Write(w3))
        self.play(Write(w3b))
        self.wait(2.5)
        w4 = Tex("Possible + permitted: every causes answer needs both").scale(0.85).shift(band_shift(8) + DOWN * 2.85)
        self.play(Write(w4))
        self.play(Create(SurroundingRectangle(w4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): one shop now — winners and losers ---
        self.next_band(9)
        b9_title = Tex("One shop: who won, who lost").scale(1.1).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        o1 = Tex("Kariega wins: hatchbacks to Europe,").scale(0.9).shift(band_shift(9) + UP * 1.4)
        o1b = Tex("tens of thousands of pay packets").scale(0.9).shift(band_shift(9) + UP * 0.65)
        self.play(Write(o1))
        self.play(Write(o1b))
        self.wait(2.5)
        o2 = Tex("Every trolley wins: the unannounced pay rise").scale(0.9).shift(band_shift(9) + DOWN * 0.25)
        self.play(Write(o2))
        self.wait(2)
        o3 = Tex("Footwear towns lose: machines silent, jobs gone").scale(0.9).shift(band_shift(9) + DOWN * 1.15)
        self.play(Write(o3))
        self.wait(2)
        o4 = Tex("2008: one shop, one flu — a million jobs").scale(0.9).shift(band_shift(9) + DOWN * 2.05)
        self.play(Write(o4))
        self.wait(2)
        o5 = Tex("Grows the total, moves the shares").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(o5))
        self.play(Create(SurroundingRectangle(o5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): top of the map, bottom of the map ---
        self.next_band(10)
        b10_title = Tex("Top of the map, bottom of the map").scale(1.1).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        t1 = Tex("The chocolate bar: beans for cents in Ghana,").scale(0.85).shift(band_shift(10) + UP * 1.4)
        t1b = Tex("thirty rand on the shelf in Europe").scale(0.85).shift(band_shift(10) + UP * 0.65)
        self.play(Write(t1))
        self.play(Write(t1b))
        self.wait(2.5)
        t2 = Tex("The money lives in the finishing").scale(0.95).shift(band_shift(10) + DOWN * 0.25)
        self.play(Write(t2))
        self.play(Create(SurroundingRectangle(t2, color=GREEN)))
        self.wait(2)
        t3 = Tex("Two more weights: dollar debt, and rules").scale(0.85).shift(band_shift(10) + DOWN * 1.15)
        t3b = Tex("written in Northern rooms").scale(0.85).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(t3))
        self.play(Write(t3b))
        self.wait(2.5)
        t4 = Tex("The reply: finish what we dig and grow —").scale(0.85).shift(band_shift(10) + DOWN * 2.8)
        t4b = Tex("and sell it to Africa first").scale(0.85).shift(band_shift(10) + DOWN * 3.5)
        self.play(Write(t4))
        self.play(Write(t4b))
        self.wait(4)
