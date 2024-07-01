from manim import *

class Lens(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{textcomp}")

        F = 1.5 # фокусное расстояние 
        a_1 = 2.2 # расстояние от предмета до линзы

        delta_1 = 1.6 # смещение предмета 

        b_1 = (a_1 * F) / (a_1 - F) # расстояние от изображения до линзы
        a_2 = a_1 + delta_1 # новое расстояние от предмета до линзы
        b_2 = ((a_1 + delta_1) * F) / ((a_1 + delta_1) - F) # новое расстояние от изображения до линзы
        G_1 = b_1 / a_1 # увеличение предмета 
        G_2 = b_2 / a_2 #  новое увеличение предмета
        delta_b_1 = abs(b_1 - b_2) # смещение изображения
        delta_G_1 = abs(G_2 - G_1) # изменение увеличения предмета

        delta_2 = -1.4

        b_1 = (a_1 * F) / (a_1 - F)
        a_3 = a_1 + delta_2
        b_3 = ((a_1 + delta_2) * F) / ((a_1 + delta_2) - F)
        G_3 = b_3 / a_3
        delta_b_2 = abs(b_1 - b_3)
        delta_G_2 = abs(G_3 - G_1)


        lens_col = DoubleArrow(2.5 * UP, 2.5 * DOWN, tip_length=0.2)
        opt_ax = DashedLine(6*LEFT, 6*RIGHT).set_stroke(GREY, 3, 0.5)
        left_F = Tex("F", font_size=40).shift(F*LEFT+0.3*DOWN)
        left_2F = Tex("2F", font_size=40).shift(F*2*LEFT+0.3*DOWN)
        right_F = Tex("F", font_size=40).shift(F*RIGHT+0.3*DOWN)
        right_2F = Tex("2F", font_size=40).shift(F*2*RIGHT+0.3*DOWN)
        F = VGroup(left_F,left_2F, right_F, right_2F)
        bar_left_F = Line(0.07*UP+1.5*LEFT, 0.07*DOWN+1.5*LEFT)
        bar_left_2F = Line(0.07*UP+3*LEFT, 0.07*DOWN+3*LEFT)
        bar_right_F = Line(0.07*UP+1.5*RIGHT, 0.07*DOWN+1.5*RIGHT)
        bar_right_2F = Line(0.07*UP+3*RIGHT, 0.07*DOWN+3*RIGHT)
        bar = VGroup(bar_right_F, bar_left_2F, bar_left_F, bar_right_2F)

        dot = Dot(ORIGIN, 0.1, color = YELLOW)
        dot_1 = Dot(a_1*LEFT, 0)
        dot_2 = Dot(a_1*LEFT+UP,0)
        dot_3 = Dot(b_1*RIGHT+G_1*DOWN,0)
        dot_4 = Dot(b_1*RIGHT,0)

        arrow = always_redraw(lambda: Arrow(dot_1, dot_2, tip_length=0.2, buff=0, color=DARK_BLUE))
        arrow_im = always_redraw(lambda: Arrow(dot_4, dot_3, tip_length=0.2, buff=0, color=DARK_BLUE))
        ray_1 = always_redraw(lambda: DashedLine(dot_2, dot_3, color=YELLOW, dashed_ratio=0.6, dash_length=0.1))
        ray_2 = always_redraw(lambda: DashedLine(dot_2, UP, color=YELLOW, dashed_ratio=0.6, dash_length=0.1))
        ray_3 = always_redraw(lambda : DashedLine(UP, dot_3, color=YELLOW, dashed_ratio=0.6, dash_length=0.1))

        text_1 = Text("Собирающая линза", font="Cambria Math", font_size=35).shift(3*DOWN)
        eq = MathTex(r"\dfrac{1}{F}"
                     r"="
                     r"\dfrac{1}{d}"
                     r"+"
                     r"\dfrac{1}{f}", font_size=35).shift(2*UR)
        shapes = VGroup(eq)
        rect = RoundedRectangle(height=1, width=2, color=GREY, corner_radius=0.2).set_stroke(GREY, 3, 1).next_to(shapes.get_center()+1.25*LEFT)

        line_1 = Line(a_1*LEFT+0.1*DOWN, a_1*LEFT+1.2*DOWN).set_stroke(GREY, 3, 0.5)
        line_2 = Line(b_1*RIGHT+0.1*DOWN, b_1*RIGHT+1.2*DOWN).set_stroke(GREY, 3, 0.5)
        arrow_1 = DoubleArrow(a_1*LEFT+1.1*DOWN, 1.1*DOWN, tip_length=0.12, buff=0.1 )
        arrow_2 = DoubleArrow(b_1 * RIGHT + 1.1 * DOWN, 1.1 * DOWN, tip_length=0.12, buff=0.1)
        d = MathTex("d", font_size=35).next_to(arrow_1.get_center(), DOWN, buff=0.1)
        f = MathTex("f", font_size=35).next_to(arrow_2.get_center(), DOWN, buff=0.1)

        self.play(Create(lens_col), Create(opt_ax), Write(F), Create(bar), run_time=2)
        self.wait()
        self.play(Write(text_1), run_time=3)
        self.wait()
        self.play(Create(arrow))
        self.wait()
        self.play(Create(ray_1), Create(ray_2))
        self.play(Create(ray_3))
        self.wait()
        self.play(Create(arrow_im), FadeIn(dot))
        self.wait()
        self.play(ApplyMethod(dot_1.shift, delta_1 * LEFT),
                  ApplyMethod(dot_2.shift, delta_1 * LEFT),
                  ApplyMethod(dot_3.shift, delta_b_1*LEFT+delta_G_1*UP),
                  ApplyMethod(dot_4.shift, delta_b_1*LEFT),
                  run_time=8,
                  rate_func=there_and_back)
        self.wait()
        self.play(Create(line_1), Create(line_2))
        self.play(Create(arrow_1), Create(arrow_2))
        self.play(Write(d), Write(f))
        self.wait()
        self.play(FadeIn(shapes, shift=UP), run_time=3, lag_ratio=0.1)
        self.wait()
        self.play(Create(rect), run_time=2)
        self.play(Uncreate(rect), run_time=2)
        self.wait(2)
