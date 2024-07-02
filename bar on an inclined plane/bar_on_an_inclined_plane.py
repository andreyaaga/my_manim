from manim import  *


class PolygonalShapes(Scene):
    def construct(self):
        line = Line(DOWN+4*LEFT,DOWN+4*RIGHT).set_stroke(GREY, 3, 0.5)
        prisma = Polygon(DR,DOWN+2*LEFT,UR, color=WHITE)
        brusok = always_redraw(lambda: Polygon(0*LEFT, 0.5*UP, RIGHT+0.5*UP, RIGHT, color=ORANGE).rotate(np.arctan(2/3)).
                               next_to(Line(DOWN+2*LEFT, UR).get_center(), UP, buff=-0.15))

        dot_mg = Dot(brusok.get_center(), 0)
        dot_N = Dot(brusok.get_center(), 0)
        dot_F = Dot(brusok.get_center(), 0)
        mg = always_redraw((lambda: Arrow(dot_mg, Dot(dot_mg.get_center() + (4/1.8)*DOWN), color=RED, tip_length=0.2, buff=0)))
        dot = VGroup(dot_F, dot_N, dot_mg)
        N = always_redraw(lambda:Arrow(dot_N, Dot(dot_N.get_center() + (5/1.8)*UP), color=DARK_BLUE, tip_length=0.2, buff=0).
             rotate(np.arctan(2/3), about_point=brusok.get_center()))
        F = always_redraw(lambda:Arrow(dot_F, Dot(dot_F.get_center() + (3/1.8)*RIGHT), color=GREEN, tip_length=0.2, buff=0))



        label = always_redraw(lambda: MathTex(r"\overrightarrow{mg}", r"\overrightarrow{N}", r"\overrightarrow{F}", font_size=30))
        always_redraw(lambda: label[0].move_to(Dot(1.1*(dot_mg.get_center() + (4/1.8)*DOWN))))
        always_redraw(lambda: label[1].move_to(Dot(1.1*(dot_N.get_center() + (5/1.8)*UP)).
                                               rotate(np.arctan(2/3), about_point=brusok.get_center())))
        always_redraw(lambda: label[2].move_to(Dot(1.1*(dot_F.get_center() + (3/1.8)*RIGHT))))

        self.play(Create(line), run_time=2)
        self.play(Create(prisma), run_time=3)
        self.play(Create(brusok), run_time=2)
        self.play(Create(mg), Create(N), Create(F), Write(label), run_time=2)
        self.wait(2)
        self.play(ApplyMethod(dot.shift, 0.5*DOWN+(3/4)*LEFT),
                  ApplyMethod(brusok.shift, 0.5*DOWN+(3/4)*LEFT),
                  ApplyMethod(label.shift, 0.5*DOWN+(3/4)*LEFT),
                  run_time=4,
                  rate_func=there_and_back)
        self.play(ApplyMethod(dot.shift, 0.5 * UP + (3 / 4) * RIGHT),
                  ApplyMethod(brusok.shift, 0.5 * UP + (3 / 4) * RIGHT),
                  ApplyMethod(label.shift, 0.5 * UP + (3 / 4) * RIGHT),
                  run_time=4,
                  rate_func=there_and_back)
        self.wait()
        self.play(FadeOut(line, brusok, prisma, label),
                  ApplyMethod(dot_mg.shift,(4/1.8)*UP),
                  ApplyMethod(dot_N.shift, 1.3*RIGHT+0.8*DOWN),
                  run_time=3)
        self.wait()
