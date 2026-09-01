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

# Band-layout whiteboard scene for "Unemployment: Causes, Consequences and
# Solutions" (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier subtopics 5-7).
# Exporter-safe primitives only; add-only lifecycle.
# Subtopic durations: 220/230/220/230/190/200/190 of 1480 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class UnemploymentSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===================== Part 1 — Expert =====================
        # --- Band 0 (subtopic_1): definitions and measurement ---
        title = Tex("Unemployment: Causes, Consequences, Solutions").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0a = Tex("Strict: without work, available, ACTIVELY seeking").scale(0.95).shift(UP * 1.1)
        self.play(Write(b0a))
        self.wait(2)
        b0b = Tex("Expanded: adds the discouraged").scale(1.0).shift(UP * 0.3)
        self.play(Write(b0b))
        self.wait(2)
        b0c = Tex("Rate $=$ unemployed $\\div$ LABOUR FORCE").scale(1.0).shift(DOWN * 0.6)
        self.play(Write(b0c))
        self.play(Create(SurroundingRectangle(b0c, color=GREEN)))
        self.wait(2)
        b0wrong = Tex("Rate $=$ unemployed $\\div$ population").scale(0.95).shift(DOWN * 1.7)
        self.play(Write(b0wrong))
        self.play(Create(strike(b0wrong)))
        self.wait(3)

        # --- Band 1 (subtopic_1): six features of SA unemployment ---
        self.next_band(1)
        b1t = Tex("Six features, each with a consequence").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = Tex("Structural $\\cdot$ youth-heavy $\\cdot$ skill-sorted").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1a))
        self.wait(2)
        b1b = Tex("geographic $\\cdot$ long-duration $\\cdot$ wide discouragement").scale(0.95).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1b))
        self.wait(2)
        b1c = Tex("It survives upswings; growth alone will not clear it").scale(0.95).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1c))
        self.wait(2)
        b1d = Tex("Always ask: which count is the headline quoting?").scale(0.95).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1d))
        self.play(Create(SurroundingRectangle(b1d, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): frictional, structural, cyclical ---
        self.next_band(2)
        b2t = Tex("Types: the cure follows the cause").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex("FRICTIONAL: the gap between jobs —").scale(0.95).shift(band_shift(2) + UP * 1.1)
        b2a2 = Tex("cure: information and faster matching").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2a))
        self.play(Write(b2a2))
        self.wait(2.5)
        b2b = Tex("STRUCTURAL: skills and places mismatch demand —").scale(0.9).shift(band_shift(2) + DOWN * 0.5)
        b2b2 = Tex("cure: training, trades, shorter distances").scale(0.9).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2b))
        self.play(Write(b2b2))
        self.wait(2.5)
        b2c = Tex("CYCLICAL: the downswing at the payroll —").scale(0.9).shift(band_shift(2) + DOWN * 2.0)
        b2c2 = Tex("cure: restored demand").scale(0.9).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2c))
        self.play(Write(b2c2))
        self.wait(3)

        # --- Band 3 (subtopic_2): seasonal, technological ---
        self.next_band(3)
        b3t = Tex("Two more types complete the five").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("SEASONAL: work with a calendar —").scale(0.95).shift(band_shift(3) + UP * 1.1)
        b3a2 = Tex("harvests, festive retail, tourism months").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3a))
        self.play(Write(b3a2))
        self.wait(2)
        b3b = Tex("cure: diversify, and fill the off-season").scale(0.95).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3b))
        self.wait(2)
        b3c = Tex("TECHNOLOGICAL: tasks absorbed by machines —").scale(0.9).shift(band_shift(3) + DOWN * 1.3)
        b3c2 = Tex("cure: retrain toward what machines cannot do").scale(0.9).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3c))
        self.play(Write(b3c2))
        self.wait(2)
        b3d = Tex("Five types, five cures — diagnosis first").scale(1.0).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3d))
        self.play(Create(SurroundingRectangle(b3d, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): causes stacked in layers ---
        self.next_band(4)
        b4t = Tex("Causes, stacked in layers").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("Historical-structural: capital-intensive economy,").scale(0.9).shift(band_shift(4) + UP * 1.1)
        b4a2 = Tex("skills pipeline thin, people parked far from work").scale(0.9).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4a))
        self.play(Write(b4a2))
        self.wait(2.5)
        b4b = Tex("Demand: slow growth, hesitant investment").scale(0.9).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4b))
        self.wait(2)
        b4c = Tex("Supply: large young cohorts arriving yearly").scale(0.9).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4c))
        self.wait(2)
        b4d = Tex("Friction: search costs tax the poorest seekers").scale(0.9).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4d))
        self.play(Create(SurroundingRectangle(b4d, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): consequences and the loop ---
        self.next_band(5)
        b5t = Tex("Consequences on three levels").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("Person: income, skills, dignity eroding").scale(0.95).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5a))
        self.wait(2)
        b5b = Tex("Economy: inside the PPC; weak demand; fiscus squeezed").scale(0.85).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5b))
        self.wait(2)
        b5c = Tex("Society: inequality, exclusion, strain").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5c))
        self.wait(2)
        r5 = Rectangle(width=9.6, height=1.1).shift(band_shift(5) + DOWN * 1.7)
        b5d = Tex("no wage $\\to$ no spending $\\to$ no orders $\\to$ no hiring").scale(0.85).move_to(r5.get_center())
        self.play(Create(r5), Write(b5d))
        self.wait(2)
        b5e = Tex("Every solution tries to cut this loop somewhere").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5e))
        self.play(Create(SurroundingRectangle(b5e, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the three approaches ---
        self.next_band(6)
        b6t = Tex("Three approaches, none sufficient alone").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("GROWTH: durable jobs — if growth needs people").scale(0.9).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6a))
        self.wait(2)
        b6b = Tex("PUBLIC PROGRAMMES: income, first work record,").scale(0.9).shift(band_shift(6) + UP * 0.3)
        b6b2 = Tex("public assets — temporary, budget-funded").scale(0.9).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6b))
        self.play(Write(b6b2))
        self.wait(2.5)
        b6c = Tex("UIF: one percent + one percent; temporary benefits;").scale(0.85).shift(band_shift(6) + DOWN * 1.3)
        b6c2 = Tex("contributors only").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6c))
        self.play(Write(b6c2))
        self.wait(2)
        b6d = Tex("Strengths AND limits, for each — always").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6d))
        self.play(Create(SurroundingRectangle(b6d, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): diagnose before prescribing ---
        self.next_band(7)
        b7t = Tex("Diagnose, then prescribe").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("Cyclical $\\to$ demand $\\cdot$ frictional $\\to$ information").scale(0.95).shift(band_shift(7) + UP * 1.0)
        self.play(Write(b7a))
        self.wait(2)
        b7b = Tex("Structural $\\to$ skills, mobility,").scale(0.95).shift(band_shift(7) + UP * 0.2)
        b7b2 = Tex("labour-absorbing growth").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7b))
        self.play(Write(b7b2))
        self.wait(2)
        b7wrong = Tex("One instrument cures all five types").scale(0.95).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7wrong))
        self.play(Create(strike(b7wrong)))
        self.wait(2)
        b7c = Tex("Bridges bridging, nets cushioning, engines pulling").scale(0.9).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7c))
        self.play(Create(SurroundingRectangle(b7c, color=GREEN)))
        self.wait(3)

        # ===================== Part 2 — Simplifier =====================
        # --- Band 8 (subtopic_5): three thousand applications ---
        self.next_band(8)
        b8t = Tex("The queue that doesn't move").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Forty posts. Three thousand applications.").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex("Young $\\cdot$ split by skill $\\cdot$ mapped by history $\\cdot$ long").scale(0.9).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("Across town: an artisan post advertised three times").scale(0.9).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex("Those who stopped applying: seen only").scale(0.95).shift(band_shift(8) + DOWN * 1.6)
        b8d2 = Tex("by the expanded count").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8d))
        self.play(Write(b8d2))
        self.play(Create(SurroundingRectangle(b8d2, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): five stories, five fixes ---
        self.next_band(9)
        b9t = Tex("Five stories, five fixes").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Lerato: the gap — faster matching").scale(0.9).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9a))
        self.wait(2)
        b9b = Tex("Jabu and Zanele: the mismatch — training,").scale(0.9).shift(band_shift(9) + UP * 0.4)
        b9b2 = Tex("trades, transport").scale(0.9).shift(band_shift(9) + DOWN * 0.3)
        self.play(Write(b9b))
        self.play(Write(b9b2))
        self.wait(2)
        b9c = Tex("Pieter: the downswing — demand returns him").scale(0.9).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9c))
        self.wait(2)
        b9d = Tex("Naomi: the season $\\cdot$ Sizwe: the machine").scale(0.9).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9d))
        self.wait(2)
        b9e = Tex("One cure for all five is a failed diagnosis").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9e))
        self.play(Create(SurroundingRectangle(b9e, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): bridges, engines and nets ---
        self.next_band(10)
        b10t = Tex("Bridges, engines and nets").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("ENGINE: growth — but the labour-hungry kind").scale(0.95).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10a))
        self.wait(2)
        b10b = Tex("BRIDGE: public work — judged by where it lands").scale(0.95).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10b))
        self.wait(2)
        b10c = Tex("NET: the UIF — one percent plus one percent,").scale(0.95).shift(band_shift(10) + DOWN * 0.6)
        b10c2 = Tex("with its hole where the young stand").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10c))
        self.play(Write(b10c2))
        self.wait(2.5)
        b10d = Tex("All three, with limits named — that is precision").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10d))
        self.play(Create(SurroundingRectangle(b10d, color=GREEN)))
        self.wait(4)
