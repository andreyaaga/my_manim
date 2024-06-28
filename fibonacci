from manim import *

class Fibonacci(Scene):

    def construct(self):
        square = VGroup()

        def fibonacci(n):
            if n in (1, 2):
                return 1
            return fibonacci(n - 1) + fibonacci(n - 2)

        for i in range(11, 1, -1):
            A = always_redraw(lambda: Dot(DR+DL * fibonacci(i) / 35))
            B = always_redraw(lambda: Dot(DR+UL * fibonacci(i) / 35))
            C = always_redraw(lambda: Dot(DR+UR * fibonacci(i) / 35))
            D = always_redraw(lambda: Dot(DR+DR * fibonacci(i) / 35))
            square.add(Polygon(A.get_center(), B.get_center(), C.get_center(), D.get_center(), color=WHITE))

        square[1].next_to(square[0], LEFT, buff=0, aligned_edge=UP)
        square[2].next_to(square[1], DOWN, buff=0, aligned_edge=LEFT)
        square[3].next_to(square[2], RIGHT, buff=0, aligned_edge=DOWN)
        square[4].next_to(square[3], UP, buff=0, aligned_edge=RIGHT)
        square[5].next_to(square[4], LEFT, buff=0, aligned_edge=UP)
        square[6].next_to(square[5], DOWN, buff=0, aligned_edge=LEFT)
        square[7].next_to(square[6], RIGHT, buff=0, aligned_edge=DOWN)
        square[8].next_to(square[7], UP, buff=0, aligned_edge=RIGHT)
        square[9].next_to(square[8], LEFT, buff=0, aligned_edge=UP)


        points = [square[0].get_vertices()[3],
                  1.2*DOWN+2*RIGHT,
                  square[1].get_vertices()[2],
                  square[2].get_vertices()[1],
                  square[3].get_vertices()[0],
                  square[4].get_vertices()[3],
                  square[5].get_vertices()[2],
                  square[6].get_vertices()[1],
                  square[7].get_vertices()[0],
                  square[8].get_vertices()[3],
                  square[9].get_vertices()[2],
                  square[9].get_vertices()[0]]
        curve = VMobject(fill_color=ORANGE, stroke_color=ORANGE, stroke_width=5).set_points_smoothly(points)

        pointss = [square[0].get_vertices()[3],
                   square[1].get_vertices()[2],
                   square[2].get_vertices()[1],
                   square[3].get_vertices()[0],
                   square[4].get_vertices()[3],
                   square[5].get_vertices()[2],
                   square[6].get_vertices()[1],
                   square[7].get_vertices()[0],
                   square[8].get_vertices()[3],
                   square[9].get_vertices()[2],
                   square[9].get_vertices()[0]]

        lines = VGroup(*[Line(pointss[i], pointss[(i + 1) % len(pointss)], color=BLUE) for i in range(len(pointss))])


        self.wait()
        self.play(Create(square), run_time=6)
        self.wait()
        self.play(Create(lines[0:10]), run_time=4)
        self.wait()
        self.play(Create(curve), run_time=4)
        self.wait()
