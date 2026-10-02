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

# Band-layout whiteboard scene for conservation-of-ecosystems (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex/MathTex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (230/240/220/230/180/190/180 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ConservationOfEcosystemsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.15).shift(band_shift(k) + UP * 2.4)
        self.play(Write(t))
        self.wait(1.5)
        made = []
        for i, r in enumerate(rows):
            m = Tex(r).scale(scale).shift(band_shift(k) + UP * (1.3 - 0.95 * i))
            self.play(Write(m))
            self.wait(2.3)
            made.append(m)
        if box is not None:
            self.play(Create(SurroundingRectangle(made[box], color=box_color)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): why conserve
        self.write_rows(0, "Conservation: protect, manage, use wisely", [
            "Ecosystem services: catchment water, wetlands, pollination, soil, fish",
            "Biodiversity: genes, species, ecosystems",
            "South Africa: about 2\\% of the land, close to 10\\% of plant species",
            "Cape Floral Region: about 9 000 species, roughly 70\\% endemic",
        ], box=2)

        # --- Band 1 (subtopic_2): environmentalists and organisations
        self.next_band(1)
        self.write_rows(1, "Environmentalists: five kinds of method", [
            "Protected areas: Kruger 1898 and 1926; Marine Protected Areas",
            "Laws: Biodiversity Act 2004, quotas, permits, CITES",
            "Rescue: anti-poaching, SANCCOB, captive breeding, seed banks",
            "Restore and monitor: Working for Water 1995; Red Lists",
        ], scale=0.78, box=0)

        # --- Band 2 (subtopic_3): individuals
        self.next_band(2)
        self.write_rows(2, "Individuals: action, problem, how", [
            "Save water: Cape Town 2018, 50 litres per person per day",
            "Save electricity: less coal burnt, less pollution",
            "Reduce, then reuse, then recycle",
            "SASSI: green buy, orange think twice, red do not buy",
        ], box=3)

        # --- Band 3 (subtopic_4): sustainable use and plans
        self.next_band(3)
        self.write_rows(3, "Sustainable use: live on the interest", [
            "Use no faster than the resource is replaced",
            "Kosi Bay fish traps; Makuleke contractual park, 1998",
            "Plan check: cause, action, fixes cause?, who pays, how measured",
            "Penguins: close sardine fishing near colonies, count pairs",
        ], scale=0.78, box=2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        errs = [
            "``Conservation means no use at all''",
            "``Only the government can conserve''",
            "``A fence around a park is enough''",
            "``Recycling is the first step''",
        ]
        for i, e in enumerate(errs):
            m = Tex(e).scale(0.9).shift(band_shift(4) + UP * (1.3 - 1.0 * i))
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): live on the interest
        self.next_band(5)
        self.write_rows(5, "Live on the interest", [
            "Capital: the fish, the grass, the trees",
            "Interest: what regrows each year",
            "Spend the interest: lasts for ever. Spend the capital: gone",
            "The account pays out water, pollination, fish, jobs",
        ], scale=0.85, box=2)

        # --- Band 6 (subtopic_6): the guardians
        self.next_band(6)
        self.write_rows(6, "The guardians", [
            "Guard: rangers, no-fishing zones that refill the coast",
            "Rule: catch limits, permits, no trade in horn or ivory",
            "Rescue and repair: 19 000 penguins washed; alien trees cut",
            "Count: is the plan working?",
        ], scale=0.82, box=3)

        # --- Band 7 (subtopic_7): Monday list
        self.next_band(7)
        rows = self.write_rows(7, "What you can do on Monday", [
            "Short showers, lights off, reduce before recycle",
            "Check the fish list; plant indigenous; join a clean-up",
            "Stay on the boardwalk: nests under your feet",
        ], scale=0.85)
        last = Tex("Look after the account so it keeps paying.").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
