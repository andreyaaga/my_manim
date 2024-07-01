from manim import *

class Parallelogram_Rule(Scene):
    def construct(self):

        dot = Dot(radius=0.02,color=YELLOW)
        dot_1 = Dot(2*UP, 0.001, color=YELLOW)
        dot_2 = Dot(1.5*RIGHT, 0.001, color=YELLOW)

        text = Text("Правило параллелограмма", font="Cambria Math", font_size=30).to_edge(UP, buff=0.2)

        e_1 = always_redraw(lambda:Arrow(0*DL, dot_1, color=YELLOW, buff=0, tip_length=0.2))
        e_2 = always_redraw(lambda:Arrow(0*DL, 2*Line(dot_1, dot_2).get_center(), color=YELLOW, buff=0, tip_length=0.2))
        e_3 = always_redraw(lambda:Arrow(0*DL, dot_2, color=YELLOW, buff=0, tip_length=0.2))
        line_1 = always_redraw(lambda:DashedLine(dot_1, 2*Line(dot_1, dot_2).get_center()).set_stroke(GREY, 3, 0.5))
        line_2 = always_redraw(lambda:DashedLine(dot_2, 2*Line(dot_1, dot_2).get_center()).set_stroke(GREY, 3, 0.5))
        a = always_redraw(lambda:MathTex(r"\overrightarrow{a}").move_to(1.25*dot_1.get_center()))
        b = always_redraw(lambda:MathTex(r"\overrightarrow{b}").move_to(1.25*dot_2.get_center()))
        ab = always_redraw(lambda:MathTex(r"\overrightarrow{a}+\overrightarrow{b}").move_to(1.3*2*Line(dot_1, dot_2).get_center()))

        self.play(Write(text), run_time=2)
        self.play(Create(e_1), Create(e_2), Create(e_3), FadeIn(dot), Create(line_1), Create(line_2), Write(a), Write(b), Write(ab))
        self.wait()
        self.play(Rotate(dot_1, 0.62*PI, about_point=ORIGIN), Rotate(dot_2, -0.62*PI, about_point=ORIGIN),
                  run_time=7, rate_func=there_and_back)
        self.wait()
        self.play(ApplyMethod(dot_1.shift, DOWN), ApplyMethod(dot_2.shift, 2*RIGHT),
                  run_time=4, rate_func=there_and_back)
        self.play(ApplyMethod(dot_1.shift, 4*DOWN), ApplyMethod(dot_2.shift, 4 * LEFT),
                  run_time=6, rate_func=there_and_back)
        self.wait(2)
        self.play(FadeOut(e_1, e_2, e_3, a, b, ab, line_1, line_2, text, dot, shift=DOWN), run_time=2)
        self.wait(2)

