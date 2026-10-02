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

# Band-layout whiteboard scene for adaptations-and-extinction (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex/MathTex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (220/240/230/220/190/180/190 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AdaptationsExtinctionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): what an adaptation is
        title = Tex("Adaptation: fitted to the habitat").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = Tex("An inherited feature that improves survival and reproduction in a habitat").scale(0.8).shift(UP * 1.2)
        l2 = Tex("Gemsbok, Kalahari: sand above 60$^\\circ$C, no water for months").scale(0.85).shift(UP * 0.2)
        l3 = Tex("Pale coat; body to 45$^\\circ$C and nasal cooling; night feeding, melons").scale(0.8).shift(DOWN * 0.7)
        l4 = Tex("Answer in three: feature, habitat problem, how it helps").scale(0.9).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): three kinds
        self.next_band(1)
        b1_title = Tex("Structural, functional, behavioural").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        rows = [
            r"\text{Structural (a part): giraffe neck, fox ears, succulent stem, spines}",
            r"\text{Functional (a process): heat tolerance, concentrated urine, venom}",
            r"\text{Behavioural (a habit): nocturnal, migration, sentry, nest over water}",
            r"\text{Hibernation: mainly functional, with a behavioural element}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.72).shift(band_shift(1) + UP * (1.3 - 0.8 * i))
            self.play(Write(m))
            self.wait(2.2)
        self.wait(1.5)

        # --- Band 2 (subtopic_3): extinction
        self.next_band(2)
        b2_title = Tex("Extinction: no living individuals remain").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Natural: climate shift, asteroid (66 Ma), volcanoes, disease, competition").scale(0.78).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex("Permian die-off 252 Ma: Karoo rocks full of Lystrosaurus afterwards").scale(0.78).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex("Human: habitat loss, hunting, aliens, pollution, climate change").scale(0.82).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex("Today: hundreds of times the natural rate, and permanent").scale(0.85).shift(band_shift(2) + DOWN * 1.5)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): South African cases
        self.next_band(3)
        b3_title = Tex("South Africa: lost and threatened").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Bluebuck, c. 1800: farms and hunting. Quagga, 1883: meat, hides, sheep").scale(0.78).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("Riverine rabbit: riverside Karoo bush ploughed and grazed").scale(0.82).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex("African penguin: sardines overfished, oil. Black rhino: horn poaching").scale(0.78).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = Tex("Red List: vulnerable, endangered, critically endangered, extinct").scale(0.8).shift(band_shift(3) + DOWN * 1.8)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``The animal adapted during its life''").scale(0.9).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("``Venom is structural because it is inside the body''").scale(0.9).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex("``A zoo species cannot be extinct in the wild''").scale(0.9).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex("``Breeding look-alikes brings the quagga back''").scale(0.9).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): built for the job
        self.next_band(5)
        b5_title = Tex("Built for the job").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("A screwdriver is useless for nails: every tool fits one job").scale(0.85).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("Gemsbok: pale coat, fever on purpose, night feeding, melons").scale(0.85).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("Born with it, cannot learn it; only good for its own place").scale(0.85).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("Three bits: feature, problem, how it helps").scale(0.95).shift(band_shift(5) + DOWN * 1.5)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): three kinds of clever
        self.next_band(6)
        b6_title = Tex("Three kinds of clever").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("A part you can see: ears, neck, fat stem, spines").scale(0.9).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex("A process inside: heat tolerance, strong urine, venom, cocoon").scale(0.85).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("A habit: night-time, migration, sentry, nest over water").scale(0.85).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("Part, process, habit: say which, then say the job").scale(0.9).shift(band_shift(6) + DOWN * 1.5)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): gone for good
        self.next_band(7)
        b7_title = Tex("Gone for good").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        rows = [
            r"\text{Home changes faster than the creature: the tool no longer fits}",
            r"\text{Quagga: shot out by the 1870s, last died Amsterdam 1883}",
            r"\text{Bluebuck c. 1800; next in line: rabbit, penguin, rhino}",
            r"\text{Extinct = gone everywhere, for ever}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.8).shift(band_shift(7) + UP * (1.3 - 0.75 * i))
            self.play(Write(m))
            self.wait(2.0)
        b7_l5 = Tex("Fitted to a home. Lose the home, lose the species.").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=YELLOW)))
        self.wait(4)
