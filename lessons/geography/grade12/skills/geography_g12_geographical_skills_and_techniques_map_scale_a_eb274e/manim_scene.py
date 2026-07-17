from manim import *

class GeographyMapScale(Scene):
    def construct(self):
        # Subtopic 1: Introduction to Map Scale
        title_intro = Text("Map Scale", font_size=48).to_edge(UP)
        self.play(Write(title_intro))
        self.wait(1)

        scale_ratio = MathTex(r"1 : 50\,000", font_size=64)
        self.play(FadeIn(scale_ratio))
        self.wait(2)

        meaning_1 = Text("1 unit on map", font_size=36, color=BLUE).next_to(scale_ratio, DOWN, buff=1)
        meaning_2 = Text("50 000 units in reality", font_size=36, color=GREEN).next_to(meaning_1, DOWN, buff=0.5)

        self.play(Write(meaning_1))
        self.wait(1)
        self.play(Write(meaning_2))
        self.wait(3)

        self.play(FadeOut(scale_ratio), FadeOut(meaning_1), FadeOut(meaning_2))

        # Subtopic 2: Unit Conversions
        title_units = Text("Unit Conversions", font_size=48).to_edge(UP)
        self.play(Transform(title_intro, title_units))
        self.wait(1)

        cm_to_m = MathTex(r"100 \text{ cm} = 1 \text{ m}", font_size=48)
        m_to_km = MathTex(r"1000 \text{ m} = 1 \text{ km}", font_size=48).next_to(cm_to_m, DOWN, buff=0.5)

        self.play(Write(cm_to_m))
        self.wait(2)
        self.play(Write(m_to_km))
        self.wait(2)

        cm_to_km_text = Text("How many cm in 1 km?", font_size=40).next_to(m_to_km, DOWN, buff=1)
        self.play(Write(cm_to_km_text))
        self.wait(1)

        cm_to_km_calc = MathTex(r"100 \times 1000 = 100\,000 \text{ cm}", font_size=48).next_to(cm_to_km_text, DOWN, buff=0.5)
        self.play(Write(cm_to_km_calc))
        self.wait(3)

        rule_box = SurroundingRectangle(cm_to_km_calc, color=YELLOW)
        self.play(Create(rule_box))
        self.wait(2)

        self.play(FadeOut(cm_to_m), FadeOut(m_to_km), FadeOut(cm_to_km_text), FadeOut(cm_to_km_calc), FadeOut(rule_box))

        # Subtopic 3: Calculating Real Distance
        title_calc = Text("Calculating Real Distance", font_size=48).to_edge(UP)
        self.play(Transform(title_intro, title_calc))
        self.wait(1)

        formula = MathTex(r"\text{Real Distance} = \text{Map Distance} \times \text{Scale factor}", font_size=40)
        self.play(Write(formula))
        self.wait(2)

        self.play(formula.animate.to_edge(UP, buff=1.5))

        step1 = MathTex(r"\text{Real Distance} = 8,6 \text{ cm} \times 50\,000", font_size=48)
        self.play(Write(step1))
        self.wait(2)

        step2 = MathTex(r"= 430\,000 \text{ cm}", font_size=48).next_to(step1, DOWN, aligned_edge=LEFT)
        self.play(Write(step2))
        self.wait(2)

        conversion_text = Text("Convert to km: divide by 100 000", font_size=36, color=YELLOW).next_to(step2, DOWN, buff=0.5)
        self.play(Write(conversion_text))
        self.wait(2)

        step3 = MathTex(r"= \frac{430\,000}{100\,000} \text{ km}", font_size=48).next_to(conversion_text, DOWN, aligned_edge=LEFT)
        self.play(Write(step3))
        self.wait(2)

        step4 = MathTex(r"= 4,3 \text{ km}", font_size=48, color=GREEN).next_to(step3, DOWN, aligned_edge=LEFT)
        self.play(Write(step4))
        self.wait(3)

        self.play(FadeOut(formula), FadeOut(step1), FadeOut(step2), FadeOut(conversion_text), FadeOut(step3), FadeOut(step4))

        # Subtopic 4: The Shortcut
        title_shortcut = Text("The Shortcut", font_size=48).to_edge(UP)
        self.play(Transform(title_intro, title_shortcut))
        self.wait(1)

        shortcut_base = MathTex(r"1 \text{ cm} = 50\,000 \text{ cm}", font_size=48)
        self.play(Write(shortcut_base))
        self.wait(2)

        shortcut_div = MathTex(r"1 \text{ cm} = \frac{50\,000}{100\,000} \text{ km}", font_size=48).next_to(shortcut_base, DOWN)
        self.play(Write(shortcut_div))
        self.wait(2)

        shortcut_res = MathTex(r"1 \text{ cm} = 0,5 \text{ km}", font_size=48, color=YELLOW).next_to(shortcut_div, DOWN)
        self.play(Write(shortcut_res))
        self.wait(3)

        self.play(shortcut_res.animate.to_edge(UP, buff=1.5), FadeOut(shortcut_base), FadeOut(shortcut_div))

        short_step1 = MathTex(r"\text{Real Distance} = 8,6 \times 0,5 \text{ km}", font_size=48)
        self.play(Write(short_step1))
        self.wait(2)

        short_step2 = MathTex(r"= 4,3 \text{ km}", font_size=48, color=GREEN).next_to(short_step1, DOWN, aligned_edge=LEFT)
        self.play(Write(short_step2))
        self.wait(3)

        self.play(FadeOut(title_intro), FadeOut(shortcut_res), FadeOut(short_step1), FadeOut(short_step2))

        # Signoff
        signoff = Text("See you on the trail.", font_size=48, color=BLUE)
        self.play(Write(signoff))
        self.wait(2)
        self.play(FadeOut(signoff))
