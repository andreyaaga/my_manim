from manim import *


class CreationUncreationHexagon(Scene):
    def construct(self):

        A = Dot(3 * LEFT)
        B = Dot(1.5 * LEFT + UP * 1.5 * np.sqrt(3))
        C = Dot(1.5 * RIGHT + UP * 1.5 * np.sqrt(3))
        D = Dot(3 * RIGHT)
        E = Dot(1.5 * RIGHT + DOWN * 1.5 * np.sqrt(3))
        F = Dot(1.5 * LEFT + DOWN * 1.5 * np.sqrt(3))

        AB = Line(A, B)
        BC = Line(B, C)
        CD = Line(C, D)
        DE = Line(D, E)
        EF = Line(E, F)
        FA = Line(F, A)

        hexagon = VGroup()
        for i in range(1, 50):
            new_AB = Line(AB[-1].get_center(), BC[-1].get_center())
            new_BC = Line(BC[-1].get_center(), CD[-1].get_center())
            new_CD = Line(CD[-1].get_center(), DE[-1].get_center())
            new_DE = Line(DE[-1].get_center(), EF[-1].get_center())
            new_EF = Line(EF[-1].get_center(), FA[-1].get_center())
            new_FA = Line(FA[-1].get_center(), AB[-1].get_center())

            hexagon.add(Polygon(new_AB.get_center(),
                                new_BC.get_center(),
                                new_CD.get_center(),
                                new_DE.get_center(),
                                new_EF.get_center(),
                                new_FA.get_center(),
                                color=BLUE).set_stroke(width=2))

            AB.add(new_AB)
            BC.add(new_BC)
            CD.add(new_CD)
            DE.add(new_DE)
            EF.add(new_EF)
            FA.add(new_FA)

        self.wait()
        self.play(Create(hexagon,0), run_time=5)
        self.wait()
        self.play(Uncreate(hexagon, lag_ratio=0), run_time=5)
        self.wait()
