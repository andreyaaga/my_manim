from manim import *

class LaTexSimple(Scene):
    def construct(self):

        dot_1a = Dot(2*DOWN+4*LEFT,0)
        dot_2a = Dot(2*DL,0)
        text = Text("Правило многоугольника", font="Cambria Math", font_size=30).to_edge(UP, buff=0.2)
        dot_1b = Dot(3*DR,0)
        dot_2b = Dot(DOWN+4*RIGHT,0)

        dot_1c = Dot(DR,0)
        dot_2c = Dot(UP,0)

        dot_1d = Dot(3*UP+2*LEFT,0)
        dot_2d = Dot(2*UR,0)

        dot_1abcd = Dot(2*DL)
        dot_2abcd = Dot(UP+4*RIGHT)

        a = always_redraw(lambda: Arrow(dot_1a, dot_2a, color=YELLOW, tip_length=0.2, buff=0))
        b = always_redraw(lambda: Arrow(dot_1b, dot_2b, color=YELLOW, tip_length=0.2, buff=0))
        c = always_redraw(lambda: Arrow(dot_1c, dot_2c, color=YELLOW, tip_length=0.2, buff=0))
        d = always_redraw(lambda: Arrow(dot_1d, dot_2d, color=YELLOW, tip_length=0.2, buff=0))
        vektori = VGroup(a,b,c,d)
        abcd = always_redraw(lambda: Arrow(dot_1abcd, dot_2abcd, color=ORANGE, tip_length=0.2, buff=0))
        dot = Dot(2*DR)

        label = always_redraw(
            lambda: MathTex(r"\overrightarrow{a}",
                            r"\overrightarrow{b}",
                            r"\overrightarrow{c}",
                            r"\overrightarrow{d}",
                            r"\overrightarrow{a}+\overrightarrow{b}+\overrightarrow{c}+\overrightarrow{d}",
                            font_size=40))

        always_redraw(lambda: label[0].move_to(1.2*a.get_center()))
        always_redraw(lambda: label[1].move_to(1.2*b.get_center()))
        always_redraw(lambda: label[2].next_to(1.3*c.get_center()))
        always_redraw(lambda: label[3].move_to(1.2*d.get_center()))
        always_redraw(lambda: label[4:].move_to(1.5*abcd.get_center()).rotate(np.arctan(3/6)))


        self.play(Create(vektori), Write(label[0:4]), Write(text), run_time=3)
        self.wait(2)
        self.play(ApplyMethod(dot_1c.shift, 2*DL+UL),
                  ApplyMethod(dot_2c.shift, 2*DL+UL),
                  ApplyMethod(dot_1b.shift, 5*LEFT+2*UP+UL),
                  ApplyMethod(dot_2b.shift,5*LEFT+2*UP+UL),
                  ApplyMethod(dot_1a.shift, 3*UR+UL),
                  ApplyMethod(dot_2a.shift, 3*UR+UL),
                  ApplyMethod(dot_1d.shift, 2*DOWN+3*RIGHT+UL),
                  ApplyMethod(dot_2d.shift, 2*DOWN+3*RIGHT+UL),
                  run_time=2)
        self.wait(2)
        self.play(Create(abcd), Write(label[4]), run_time=3)
        self.wait(2)
        self.play(FadeOut(label, vektori, text, abcd, shift=DOWN), run_time=2)
