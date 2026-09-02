# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band-layout whiteboard scene for "Magnets and Magnetic Fields" (Part 1 —
# Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7). Exporter-safe
# mobjects only (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/VGroup); the bar
# magnet and field arcs are hand-built from Rectangles, Lines and Arrows.
# Add-only lifecycle. Band time apportioned to subtopics.json
# (230/240/240/250/180/190/190 of 1520 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class MagnetsAndMagneticFieldsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): force without touching ---
        title = Tex("Magnets and Magnetic Fields").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("A steel pin leaps an air gap — force without touching").scale(0.9).shift(UP * 1.2)
        self.play(Write(d1))
        self.wait(2.5)
        d2 = Tex("The field: a REGION in space where a magnet").scale(0.95).shift(UP * 0.2)
        d2b = Tex("or ferromagnetic material feels a force").scale(0.95).shift(DOWN * 0.5)
        self.play(Write(d2))
        self.play(Write(d2b))
        self.play(Create(SurroundingRectangle(VGroup(d2, d2b), color=GREEN)))
        self.wait(3)
        d3 = Tex("Ferromagnetic: iron, steel, cobalt, nickel").scale(0.95).shift(DOWN * 1.7)
        self.play(Write(d3))
        self.wait(2)
        d4 = Tex("Copper, aluminium, glass, paper: indifferent").scale(0.9).shift(DOWN * 2.6)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the family of fields ---
        self.next_band(1)
        b1t = Tex("Three fields, one grammar").scale(1.2).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1t))
        self.wait(2)
        b1a = Tex("Gravitational field $\\to$ acts on MASS — attracts only").scale(0.9).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1a))
        self.wait(2.5)
        b1b = Tex("Electric field $\\to$ acts on CHARGE — attracts or repels").scale(0.9).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1b))
        self.wait(2.5)
        b1c = Tex("Magnetic field $\\to$ magnets + ferromagnetics").scale(0.9).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1c))
        self.wait(2.5)
        b1d = Tex("Charges exist alone; POLES never do").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1d))
        self.play(Create(SurroundingRectangle(b1d, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): poles and the interaction rule ---
        self.next_band(2)
        b2t = Tex("Poles come in pairs").scale(1.2).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2t))
        self.wait(2)
        # bar magnet from primitives
        mag = Rectangle(width=4.0, height=0.9).shift(band_shift(2) + UP * 0.9)
        nl = Tex("N").scale(1.0).move_to(band_shift(2) + UP * 0.9 + LEFT * 1.5)
        sl = Tex("S").scale(1.0).move_to(band_shift(2) + UP * 0.9 + RIGHT * 1.5)
        mid = Line(band_shift(2) + UP * 1.35, band_shift(2) + UP * 0.45)
        self.play(Create(mag), Create(mid), Write(nl), Write(sl))
        self.wait(2.5)
        b2a = Tex("Hung from a thread, it settles north-south").scale(0.9).shift(band_shift(2) + DOWN * 0.2)
        self.play(Write(b2a))
        self.wait(2.5)
        b2b = Tex("Like poles REPEL; opposite poles ATTRACT").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2b))
        self.play(Create(SurroundingRectangle(b2b, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): cutting, and the domain picture ---
        self.next_band(3)
        b3t = Tex("Saw it in half — and fail").scale(1.15).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3t))
        self.wait(2)
        h1 = Rectangle(width=1.8, height=0.7).shift(band_shift(3) + UP * 1.1 + LEFT * 1.6)
        h1n = Tex("N").scale(0.7).move_to(band_shift(3) + UP * 1.1 + LEFT * 2.2)
        h1s = Tex("S").scale(0.7).move_to(band_shift(3) + UP * 1.1 + LEFT * 1.0)
        h2 = Rectangle(width=1.8, height=0.7).shift(band_shift(3) + UP * 1.1 + RIGHT * 1.6)
        h2n = Tex("N").scale(0.7).move_to(band_shift(3) + UP * 1.1 + RIGHT * 1.0)
        h2s = Tex("S").scale(0.7).move_to(band_shift(3) + UP * 1.1 + RIGHT * 2.2)
        self.play(Create(h1), Write(h1n), Write(h1s))
        self.play(Create(h2), Write(h2n), Write(h2s))
        self.wait(2.5)
        b3a = Tex("Every piece: a complete two-poled magnet").scale(0.95).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3a))
        self.wait(2.5)
        b3b = Tex("Why: DOMAINS — neighbourhoods of aligned electron fields").scale(0.85).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3b))
        self.wait(2.5)
        b3c = Tex("Unmagnetised: random. Magnetised: aligned").scale(0.95).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3c))
        self.wait(2)
        b3d = Tex("No monopole has ever been found").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3d))
        self.play(Create(SurroundingRectangle(b3d, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the four field-line rules ---
        self.next_band(4)
        b4t = Tex("Field lines: the four rules").scale(1.2).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("1. From N to S outside the magnet — arrows on").scale(0.9).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4a))
        self.wait(2)
        b4b = Tex("2. Crowded lines $=$ strong field — densest at poles").scale(0.9).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4b))
        self.wait(2)
        b4c = Tex("3. Lines NEVER cross").scale(0.9).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4c))
        self.wait(2)
        b4d = Tex("4. The real field is three-dimensional").scale(0.9).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4d))
        self.wait(2)
        b4e = Tex("The drawings ARE the marks in this topic").scale(0.9).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4e))
        self.wait(3)

        # --- Band 5 (subtopic_3): the bar-magnet pattern, drawn ---
        self.next_band(5)
        b5t = Tex("The bar-magnet pattern").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5t))
        self.wait(2)
        mag2 = Rectangle(width=3.0, height=0.7).shift(band_shift(5) + DOWN * 0.4)
        m2n = Tex("N").scale(0.8).move_to(band_shift(5) + DOWN * 0.4 + LEFT * 1.1)
        m2s = Tex("S").scale(0.8).move_to(band_shift(5) + DOWN * 0.4 + RIGHT * 1.1)
        self.play(Create(mag2), Write(m2n), Write(m2s))
        self.wait(2)
        # field arcs as arrows built from short line chains
        a1 = Arrow(band_shift(5) + DOWN * 0.4 + LEFT * 1.7, band_shift(5) + UP * 1.3 + LEFT * 0.2, buff=0, stroke_width=3)
        a2 = Arrow(band_shift(5) + UP * 1.3 + LEFT * 0.2, band_shift(5) + DOWN * 0.4 + RIGHT * 1.7, buff=0, stroke_width=3)
        a3 = Arrow(band_shift(5) + DOWN * 0.4 + LEFT * 1.7, band_shift(5) + DOWN * 2.1 + LEFT * 0.2, buff=0, stroke_width=3)
        a4 = Arrow(band_shift(5) + DOWN * 2.1 + LEFT * 0.2, band_shift(5) + DOWN * 0.4 + RIGHT * 1.7, buff=0, stroke_width=3)
        self.play(Create(a1), Create(a2))
        self.play(Create(a3), Create(a4))
        self.wait(2.5)
        b5a = Tex("A fountain: out of N, around, into S").scale(0.9).move_to(band_shift(5) + UP * 1.9)
        self.play(Write(b5a))
        self.wait(2)
        b5b = Tex("Filings show SHAPE; compasses show DIRECTION").scale(0.85).move_to(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5b))
        self.play(Create(SurroundingRectangle(b5b, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_3): two magnets together ---
        self.next_band(6)
        b6t = Tex("Two magnets: the exam's two drawings").scale(1.1).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("N facing S: a dense BRIDGE of lines — attraction").scale(0.9).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6a))
        self.wait(2.5)
        br1 = Arrow(band_shift(6) + UP * 0.4 + LEFT * 1.8, band_shift(6) + UP * 0.4 + RIGHT * 1.8, buff=0, stroke_width=4)
        self.play(Create(br1))
        self.wait(2)
        b6b = Tex("N facing N: lines bend AWAY — repulsion").scale(0.9).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6b))
        self.wait(2.5)
        n1 = Dot(band_shift(6) + DOWN * 1.6, radius=0.06)
        b6c = Tex("Neutral point between them: the fields cancel").scale(0.85).shift(band_shift(6) + DOWN * 2.3)
        self.play(Create(n1), Write(b6c))
        self.play(Create(SurroundingRectangle(b6c, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the Earth is a magnet ---
        self.next_band(7)
        b7t = Tex("The Earth is a magnet").scale(1.2).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7t))
        self.wait(2)
        earth = Circle(radius=1.1, color=BLUE).shift(band_shift(7) + UP * 0.4)
        core = Rectangle(width=0.5, height=1.6).shift(band_shift(7) + UP * 0.4)
        self.play(Create(earth), Create(core))
        self.wait(2)
        b7a = Tex("As if a giant bar magnet lay along the axis").scale(0.9).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7a))
        self.wait(2.5)
        b7b = Tex("A compass: a small magnet answering the planet").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7b))
        self.wait(2)
        b7c = Tex("The pole in the north is magnetically a SOUTH pole").scale(0.85).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7c))
        self.play(Create(SurroundingRectangle(b7c, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): the shield in the sky ---
        self.next_band(8)
        b8t = Tex("Two norths, one shield").scale(1.15).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Geographic pole: fixed point of the spin axis").scale(0.9).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8a))
        self.wait(2.5)
        b8b = Tex("Magnetic pole: hundreds of km away — and it drifts").scale(0.9).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8b))
        self.wait(2.5)
        b8c = Tex("The field deflects the solar wind around the planet").scale(0.9).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8c))
        self.wait(2.5)
        b8d = Tex("Particles funnelled to the poles: AURORAS").scale(0.9).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8d))
        self.wait(2)
        b8e = Tex("Solar eruptions $\\to$ magnetic storms: radio, satellites, grids").scale(0.8).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8e))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): the invisible bubble ---
        self.next_band(9)
        b9t = Tex("The invisible bubble").scale(1.2).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9t))
        self.wait(2)
        bub = Circle(radius=1.6, color=BLUE).shift(band_shift(9) + UP * 0.3)
        mg = Rectangle(width=0.9, height=0.4).shift(band_shift(9) + UP * 0.3)
        self.play(Create(bub), Create(mg))
        self.wait(2)
        b9a = Tex("The door grabs the magnet BEFORE they touch").scale(0.9).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9a))
        self.wait(2.5)
        b9b = Tex("Strongest up close; fades with distance").scale(0.9).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex("VIP list only: iron, steel, cobalt, nickel").scale(0.9).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(b9c))
        self.wait(3)

        # --- Band 10 (subtopic_6): the pin you cannot divorce ---
        self.next_band(10)
        b10t = Tex("The pin you cannot divorce").scale(1.2).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("Snip the pin: a new south grows at every cut").scale(0.9).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10a))
        self.wait(2.5)
        b10b = Tex("Grind it to dust: every speck has both poles").scale(0.9).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10b))
        self.wait(2.5)
        b10c = Tex("Domains: a stadium crowd doing the wave").scale(0.95).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10c))
        self.play(Create(SurroundingRectangle(b10c, color=GREEN)))
        self.wait(2.5)
        b10d = Tex("Drop it: crowd loses rhythm — weaker magnet").scale(0.9).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10d))
        self.wait(2)
        b10e = Tex("Stroke a needle: recruit the crowd — new magnet").scale(0.9).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10e))
        self.wait(3)

        # --- Band 11 (subtopic_7): the needle that knows north ---
        self.next_band(11)
        b11t = Tex("The needle that knows north").scale(1.2).shift(band_shift(11) + UP * 2.3)
        self.play(Write(b11t))
        self.wait(2)
        b11a = Tex("Floating needle swings north-south — every time").scale(0.9).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11a))
        self.wait(2.5)
        b11b = Tex("The planet's bubble is turning it").scale(0.95).shift(band_shift(11) + UP * 0.3)
        self.play(Write(b11b))
        self.wait(2.5)
        b11c = Tex("Needle's N points north $\\to$ that pole acts SOUTH").scale(0.9).shift(band_shift(11) + DOWN * 0.7)
        self.play(Write(b11c))
        self.play(Create(SurroundingRectangle(b11c, color=GREEN)))
        self.wait(2.5)
        b11d = Tex("Map's north and needle's north: hundreds of km apart").scale(0.85).shift(band_shift(11) + DOWN * 1.7)
        self.play(Write(b11d))
        self.wait(2)
        b11e = Tex("The shield glows green at the poles: auroras").scale(0.9).shift(band_shift(11) + DOWN * 2.6)
        self.play(Write(b11e))
        self.wait(4)
