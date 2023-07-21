import turtle


class Stvorcova(turtle.Turtle):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.speed(0)
        self.pu()
        self.setpos(x, y)
        self.pd()

    def stvorec(self, velkost):
        for i in range(4):
            self.fd(velkost)
            self.rt(90)


class Vlnovkova(Stvorcova):
    def fd(self, dlzka):
        while dlzka >= 5:
            self.lt(60)
            super().fd(5)
            self.rt(120)
            super().fd(5)
            self.lt(60)
            dlzka -= 5
        super().fd(dlzka)


s = Vlnovkova()
s.stvorec(50)

turtle.mainloop()
